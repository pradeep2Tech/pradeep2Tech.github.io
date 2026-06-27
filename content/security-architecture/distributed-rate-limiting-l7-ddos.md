---
title: "Distributed Rate Limiting Topologies & L7 DDoS Mitigation"
date: 2026-06-28T16:00:00+00:00
draft: false
description: "Highly available distributed rate-limiting at the API gateway — local token batching, Redis Lua atomic counters, L7 DDoS mitigation, and fail-open runbooks."
tags: ["security-architecture", "rate-limiting", "ddos", "redis", "api-gateway", "envoy", "zero-trust"]
categories: ["Security Architecture"]
shortTitle: "Distributed Rate Limiting & L7 DDoS"
---

This structural playbook details the design of a highly available, low-latency **distributed rate-limiting infrastructure** capable of mitigating Layer 7 application-layer DDoS attacks, brute-force vectors, and resource-exhaustion traffic at the system boundary.

The gateway evaluates traffic in two phases: a zero-network-hop local token check on the fast path, and an atomic Redis sync on cache miss or exhaustion. Authorized requests forward over inner mTLS; throttled clients receive structured `429` responses with enforced backoff headers.

---

## 1. Architectural Topology & Flow

Malicious client groups hit checkout and auth endpoints at scale. The Envoy gateway checks a local in-memory token slice first; only on miss does it execute an atomic Lua script against the Redis cluster before deciding to forward or throttle.

```mermaid
sequenceDiagram
    autonumber
    actor Attacker as Malicious Client Group
    participant GW as API Gateway (Envoy Node)
    participant LocalCache as Local Memory (In-Memory Counter)
    participant Redis as Redis Cluster (Global State)
    participant Backend as Downstream Compute Cluster

    Attacker->>GW: HTTP GET /api/v2/checkout (True-Client-IP / JWT Claim)
    activate GW

    Note over GW, LocalCache: Phase 1: Local Token Quota Check
    GW->>LocalCache: Check Cached Token Allocation

    alt Local Cache Token Available (Fast Path)
        LocalCache-->>GW: Token Granted (0ms Latency)
    else Local Cache Exhausted / Cache Miss (Slow Path)
        LocalCache-->>GW: Allocation Miss / Sync Required

        Note over GW, Redis: Phase 2: Atomic Global Sync via Lua Script
        GW->>Redis: EVALSHA rate_limit.lua [Key, Limit, Window, TokensNeeded]
        activate Redis
        Note over Redis: Executes atomically; blocks concurrent race conditions
        Redis-->>GW: Return [Allowed, RemainingTokens, ResetTime]
        deactivate Redis

        GW->>LocalCache: Refresh Local Token Slice (Batch Allocation)
    end

    alt Traffic Authorized
        GW->>Backend: Forward Request via Inner mTLS Mesh
        Backend-->>GW: HTTP 200 OK
        GW-->>Attacker: HTTP 200 OK
    else Limit Exceeded (Throttled)
        GW-->>Attacker: HTTP 429 Too Many Requests (Retry-After: 30)
        deactivate GW
    end
```

---

## 2. Production Implementation Mechanics

### Algorithmic Evaluation Strategy

To handle internet-scale request velocity, system designers must pick the right mathematical rate-limiting model based on memory and accuracy trade-offs.

**Token bucket algorithm**

| Aspect | Detail |
| :--- | :--- |
| **Mechanics** | An internal bucket is assigned a maximum capacity (C). It fills at a steady constant refill rate (r) tokens per second. Every incoming request consumes exactly one token. |
| **Trade-off** | Excellent for handling bursty traffic (bursts up to capacity C pass instantly). Tracking precise sub-second refill timestamps across an expansive distributed system introduces synchronization challenges. |

**Sliding window counter algorithm**

| Aspect | Detail |
| :--- | :--- |
| **Mechanics** | Time is segmented into fixed blocks (e.g., 1 minute). The limiter reads the request count of the previous window and tracks a running counter in the current window. Current velocity is estimated dynamically. |
| **Trade-off** | Highly memory-efficient — O(1) space complexity per client profile. Smooths burst spikes at window boundaries without the heavy log-storage overhead of a sliding window log. |

Estimated rate formula:

```
Estimated Rate = (Count_prev × Time_remaining_in_current_window / Window_size) + Count_current
```

### Race-Condition Eradication (Atomic Redis Lua Implementation)

To prevent distributed API worker instances from triggering race conditions (read-modify-write synchronization bugs), token bucket or sliding counter math must run atomically inside the memory engine using an explicit evaluation script.

```lua
-- Production-Grade Sliding Window Counter Atomic Lua Script
-- KEYS[1]: Rate limit tracking identifier
--   Use a Redis Hash Tag so all keys for one session land on the same cluster slot:
--   rate:limit:{usr_90210}:checkout  (NOT rate:limit:usr_90210:checkout)
-- ARGV[1]: Max limit threshold per window
-- ARGV[2]: Current window epoch timestamp string identifier

local current_count = redis.call("HINCRBY", KEYS[1], ARGV[2], 1)

-- If this is the initial request within this time slice, set an execution expiration window
if current_count == 1 then
    redis.call("EXPIRE", KEYS[1], 120) -- Set 2-minute window retention bounds
end

-- Calculate total weight across the sliding window map boundaries
-- (Additional sliding logic parses out sub-key parameters here...)

if current_count > tonumber(ARGV[1]) then
    return 0 -- Limit breached: Deny request execution
end
return 1 -- Request authorized within limits
```

> **Engineering note (Redis Cluster):** Lua scripts execute atomically on a single shard. In a multi-node **Redis Cluster**, any script that touches multiple keys will throw a **CROSSSLOT** runtime error if those keys hash to different slots. Wrap the session-scoped segment of every rate-limit key in curly-brace **hash tags** — e.g., `rate:limit:{usr_90210}:checkout` — so all evaluation keys for one user session co-locate on the same cluster node. If a script must read both a counter key and a companion metadata key, both key names must share the identical `{tag}` substring.

---

## 3. The Security Architect's Interrogation (Hard Q&A)

### Q1: Running a Redis transaction lookup on every single incoming API connection introduces an extra network hop. How do you prevent this security infrastructure from ruining our p99 latency guarantees?

**Platform Architect Answer:** We use a **Local-Distributed Hybrid Token Allocation Model** to decouple request validation from the remote cluster network path. Instead of executing a remote sync on every single API call, our Edge Envoy proxies request token blocks in batches (e.g., claiming **100 tokens at once** via a single Redis atomic instruction).

The proxy then evaluates subsequent client requests locally in-memory with **0 ms network latency**. The remote Redis cluster is only queried when the local token block is completely exhausted, or once every **2-second** synchronization cycle. This drops our cross-network evaluation footprint by over **95%** while keeping our global rate-limiting bounds highly accurate.

### Q2: If an attacker launches a large botnet attack that targets our endpoints using millions of fake IP addresses, won't your rate limiter cause a memory-exhaustion failure inside Redis by writing millions of untrusted tracking keys?

**Platform Architect Answer:** This is a classic risk known as **Rate-Limiter Storage Exhaustion**. To block this vector, we structure our tracking identifiers around authenticated claims rather than unvalidated network strings wherever possible. For unauthenticated public routes where we must track by IP, we deploy two distinct layers of defense:

First, we route public ingress traffic through an Anycast Edge network (e.g., Cloudflare Magic Transit or AWS Shield) to scrub out volumetric Layer 3/4 packet sweeps and enforce coarse edge throttling before requests ever hit our API Gateway subnets. Second, inside our internal rate-limiting layer, we replace long-lived key definitions with high-efficiency fixed-size tracking structures like **Sliding Bloom Filters** or low-footprint rolling hashes. This caps our maximum possible memory consumption to a strict, predictable constant ceiling, regardless of attack volume.

---

## 4. Failures at Scale & Operational Runbook

### Scenario A: Global State Store Partition Isolation (The Redis Cluster Crash)

**The failure:** A severe network partition or cluster failure takes the central Redis rate-limiting state store completely offline. The API Gateways begin throwing connection timeouts, risking an immediate cascade failure that could take down all incoming product routes.

**The runbook architecture:**

1. **Enforce strict fail-open circuit breakers:** The rate-limiting client wrapper inside the API Gateway must implement an explicit, isolated timeout gate (capped at a hard **15 ms** limit). If the Redis connection pool fails or drops requests beyond this window, the circuit breaker trips and falls back to an immediate **Fail-Open** posture.
2. **Toggle coarse local sub-throttling:** While in a Fail-Open state, the system trades global tracking accuracy for platform availability. The gateways automatically switch to localized, coarse-grained tracking engines built directly into the local Envoy process memory space (e.g., using standard token bucket filters scoped locally per container instance) to protect downstream microservices from compute exhaustion until the central Redis fabric recovers.

### Scenario B: Client Retry Storm Replication (The "Thundering Herd" Worsening)

**The failure:** The system experiences a minor latency spike, and the rate limiter correctly starts throttling traffic with **HTTP 429 Too Many Requests**. However, client applications are poorly configured and launch aggressive, immediate retry loops without backoff. This amplifies the traffic surge, turning a minor bottleneck into a self-inflicted application-layer DDoS attack.

**The runbook architecture:**

- **Enforce prescriptive backoff headers:** Every single throttled response must inject structured, browser-enforced backoff markers:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
X-RateLimit-Reset: 1774843230
```

- **Downstream gateway jitter rejection gating:** Configure the ingress edge proxies to inspect retry patterns. If a client app continues to blast requests while under an active throttling penalty without waiting for the designated `Retry-After` window, the edge proxy automatically drops the connection at the L4/L7 transport layer using a low-overhead **TCP Reset (RST)**, blocking the traffic before it can consume any internal application worker threads.

---

*Previous: [Defensive Input Pipelines: Eradicating SQLi & XSS](/security-architecture/defensive-input-pipelines/)* · *Next: [Cloud Secret Management & Envelope Encryption Architecture](/security-architecture/cloud-secrets-envelope-encryption/)*
