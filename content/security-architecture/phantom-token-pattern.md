---
title: "The Phantom Token Pattern (Edge-to-Internal Exchange)"
date: 2026-06-28T10:00:00+00:00
draft: false
description: "Architectural implementation of the Phantom Token (Split Token) pattern at the ingress boundary — cryptographic assertions, Envoy header mutations, and zero-trust defensive postures."
tags: ["security-architecture", "oauth2", "zero-trust", "api-gateway", "jwt", "envoy"]
categories: ["Security Architecture"]
shortTitle: "Phantom Token Pattern"
---

This structural playbook details the architectural implementation of the **Phantom Token (Split Token)** pattern at the ingress boundary. It provides the exact technical configurations, cryptographic assertions, and defensive engineering postures required to pass zero-trust platform reviews.

External clients present only opaque, reference-style bearer tokens at the edge. The API gateway exchanges them for short-lived, internally signed JWTs before traffic crosses the trust boundary into the service mesh — keeping public tokens opaque while downstream services retain stateless verification.

---

## 1. Architectural Topology & Flow

The ingress path follows a cache-first exchange model: Redis holds previously minted internal JWTs keyed by opaque reference; cache misses trigger OAuth2 token introspection against the Identity Provider before the gateway signs and caches a replacement.

```mermaid
sequenceDiagram
    autonumber
    actor Client as External Client
    participant GW as API Gateway (Envoy Proxy)
    participant Cache as Distributed Cache (Redis cluster)
    participant IdP as Identity Provider (OAuth2 Server)
    participant Backend as Downstream Microservice

    Client->>GW: HTTP GET /orders (Auth: Bearer opaque_xyz123)
    activate GW
    GW->>Cache: GET token:opaque_xyz123
    activate Cache

    alt Cache Hit [Valid Internal JWT Found]
        Cache-->>GW: Return Plaintext Signed JWT
    else Cache Miss / Cache Expired
        Cache-->>GW: Null / Miss
        deactivate Cache
        GW->>IdP: POST /oauth2/introspect (token=opaque_xyz123)
        activate IdP
        Note over IdP: Validate token status, scopes,<br/>and policy constraints
        IdP-->>GW: HTTP 200 {"active": true, "sub": "usr_7710", "scope": "read"}
        deactivate IdP
        GW->>GW: Generate Internal JWT<br/>Sign via Asymmetric Private Key
        GW->>Cache: SETEX token:opaque_xyz123 [TTL = token_remaining_sec]
    end

    GW->>GW: Drop 'opaque_xyz123'<br/>Inject 'Authorization: Bearer Internal_JWT'
    GW->>Backend: Forward Request via mTLS (TLS 1.3)
    deactivate GW
```

---

## 2. Production Implementation Mechanics

### Ingress & Egress Header Mutations (Envoy Configuration)

The API Gateway must intercept incoming untrusted headers, execute the exchange out-of-band, and sanitize downstream headers to prevent header injection attacks.

**Incoming request:**

```http
GET /v1/data HTTP/1.1
Host: api.company.com
Authorization: Bearer st_6a7b8c9d0e1f2g3h4i5j6k7l8m9n0o
```

**Gateway target transformation engine:**

1. The gateway drops the client-facing header completely: `req.headers.remove("Authorization")`.
2. The gateway executes token exchange via a local Lua script or WebAssembly (Wasm) filter.
3. The gateway generates and appends a cryptographically signed internal token.

**Downstream forwarded request:**

```http
GET /v1/data HTTP/1.1
Host: internal-service.vpc.local
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtiLWVkLTB2MSJ9.eyJpc3MiOiJodHRwczovL2FwaS5jb21wYW55LmNvbSIsImF1ZCI6ImludGVybmFsLW1pY3Jvc2VydmljZXMiLCJzdWIiOiJ1c3JfOTAyMTAiLCJzY29wZSI6WyJvcmRlcnM6cmVhZCJdLCJleHAiOjE3NzQ4NDMyMDAsImlhdCI6MTc3NDg0MTQwMCwianRpIjoiY2EtNDExMi1iYiJ9.SignatureHere
```

### Cryptographic Baseline Standards

| Concern | Standard |
| :--- | :--- |
| **Signing protocol** | **ES256** (ECDSA P-256 + SHA-256) or **EdDSA** (Ed25519). Avoid RS256 in high-throughput pipelines — ECDSA/EdDSA yields smaller signatures and faster CPU verification. |
| **Ingress transport** | TLS 1.3 termination at the gateway |
| **Service-to-service** | Strict mTLS with identity tied to SPIFFE/SPIRE X.509 definitions |

---

## 3. The Security Architect's Interrogation (Hard Q&A)

### Q1: If the internal JWT is stateless, how do you handle immediate, real-time user revocation (e.g., account lockouts or security events) within its 15-minute validity window?

**Platform Architect Answer:** We utilize a two-tier revocation model. The internal JWT signature check remains 100% stateless at the downstream service boundary to protect our p99 latency. However, high-priority revocation events emitted by our security team or Identity Provider publish instantly to a global Redis replication stream.

Downstream Envoy sidecars parse this stream to maintain a high-efficiency in-memory Bloom Filter containing only revoked `jti` (JWT ID) claims. The downstream sidecar checks this local memory bitmask in **< 0.1 ms**. If a match occurs, it drops the request with a **401 Unauthorized** before processing hits the core computing layers.

### Q2: How do you prevent an attacker from bypassing the API Gateway and sending a forged internal JWT directly to a backend service?

**Platform Architect Answer:** We enforce zero-trust transport boundary alignment. Microservices do not bind to standard public host interfaces; they run exclusively behind service mesh sidecars within an isolated VPC. Downstream microservices enforce **Strict mTLS Mode**.

The sidecar configuration strictly validates the incoming TLS client certificate. It asserts that the certificate originated from our internal Certificate Authority (SPIRE) and checks that the SPIFFE ID belongs specifically to an authorized source (e.g., `spiffe://cluster.local/ns/ingress/sa/api-gateway`). Any direct unauthenticated connection attempt is terminated immediately at the L4/L7 transport layer before payload parsing begins.

---

## 4. Failures at Scale & Operational Runbook

### Scenario A: The Identity Provider (IdP) Introspection Thundering Herd

**The failure:** Under a major cold-start event (e.g., global service recovery or a cache cluster flushing entirely), thousands of dynamic API containers spin up concurrently, causing a massive surge of cache-miss introspection calls to the IdP. This creates a bottleneck, timing out the ingress pipelines.

**The runbook architecture:**

1. **Request coalescing (SingleFlight engine):** Implement request collapsing at the API Gateway proxy layer. When a cache miss occurs for a specific opaque reference token, only one connection worker is permitted to dispatch an active outbound `/introspect` call to the IdP. Concurrent incoming requests for that exact identical token block wait on a single shared processing promise.
2. **Graceful degraded circuit breaker:** If the IdP response latency exceeds a hard **200 ms** threshold, toggle a local circuit breaker to switch to an ephemeral local stale-cache reading buffer (stale-while-revalidate), preferring slightly stale access privileges over complete platform downtime.

### Scenario B: Cryptographic JWKS Decryption Plan Failures during Key Rotation

**The failure:** A new public key is pushed to the JWKS endpoint during rotation, but downstream containers have hardcoded or aggressively cached the old public key permanently, resulting in sudden, widespread validation drops (Signature Verification Failed).

**The runbook architecture:**

- **Proactive multikey support:** The Identity Server must sign internal tokens using the old private key for a grace period matching the maximum token lifespan ($T_{\text{expiry}}$) while concurrently distributing the new public key via the open JWKS resource matrix (`/.well-known/jwks.json`).
- **Rate-limited dynamic refresh:** Downstream components must look for an unknown key identifier (`kid`). If present, they trigger an immediate cache eviction and perform an on-demand, rate-limited call to the JWKS endpoint to pull the updated key layout, ensuring zero dropped requests.

---

*Next: [SCIM 2.0 Centralization & Enterprise Lifecycle Provisioning](/security-architecture/scim-enterprise-provisioning/)*
