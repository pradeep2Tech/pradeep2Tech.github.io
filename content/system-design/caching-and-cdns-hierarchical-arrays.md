---
title: "Edge CDNs & Pull/Push Ingestion"
date: 2026-06-28T10:36:00+00:00
draft: false
description: "CDN edge failure modes — origin shield collapse, cache poisoning via Host header, and push-ingest propagation delays across PoPs."
tags: ["system-fundamentals", "caching", "cdn", "distributed-systems"]
categories: ["System Fundamentals"]
shortTitle: "Edge CDNs & Pull/Push Ingestion"
module: 3
moduleTitle: "Distributed Hierarchical Caching Infrastructure"
sectionRef: "3.1"
---

### Hierarchical Caching Architecture
A Content Delivery Network (CDN) acts as a globally distributed reverse proxy network designed to cache and serve static and immutable assets (e.g., images, video fragments, compiled frontend packs, API responses) from Point of Presence (PoP) edge nodes geographically closest to end-users.

```text
[ Globally Distributed Users ]
│               │
▼ (GeoDNS)      ▼
┌──────────────┐┌──────────────┐
│  PoP Edge A  ││  PoP Edge B  │  ◄── Edge Cache Tier
└──────┬───────┘└──────┬───────┘
│               │ (Cache Miss)
▼               ▼
┌──────────────────────────────┐
│     Origin Shield Tier       │  ◄── Intermediate Regional Cache
└──────────────┬───────────────┘
│ (Consolidated Fetch)
▼
┌──────────────────────────────┐
│    Core Origin Services      │  ◄── Persistent Central Infrastructure
└──────────────────────────────┘
```

#### Cache Population Mechanics
* **Pull-Based Ingestion (Lazy Population):** The CDN edge populates dynamically. When a client requests an asset, the edge checks its local storage. On a cache miss, the edge proxies the request back to the origin, caches the returned payload locally based on `Cache-Control` headers, and serves the user.
* **Push-Based Ingestion (Proactive Broadcast):** The core application explicitly uploads or publishes data blocks to the CDN storage bucket system before public traffic hits. Assets are immediately pushed or synchronized out across the global data center ring.

---

### Critical Failure Modes & Operational Vulnerabilities

#### 1. Origin Shield Collapse (Cascading Ingress Stampede)
When dealing with extreme global traffic volumes, a simultaneous cache invalidation or cold startup across dozens of edge PoPs means that multiple distinct nodes will execute independent cache-miss lookups for identical data arrays. If these misses pass straight through to the central infrastructure, the cumulative network wave will overwhelm the origin databases.
* *Mechanics:* An un-shielded edge array of 50 PoP datacenters encountering a hot-key miss can escalate a single missing resource update into 50 parallel heavy backend execution queries.
* *Mitigation:* Deploy an **Origin Shield** tier—a high-capacity regional reverse proxy positioned between the edge PoPs and the central origin. The origin shield pools duplicate inbound edge misses into a single consolidated fetch loop back to the origin services, maintaining high system availability.

#### 2. Cache Poisoning via Unvalidated HTTP Host Headers
Attackers can manipulate edge caching semantics by injecting custom, un-sanitized variables into the HTTP protocol metadata envelope during an active origin lookup stream.
* *Mechanics:* A request containing a modified `Host` or `X-Forwarded-Host` header is routed to the origin via an edge miss. If the backend engine generates absolute URLs dynamically using this raw header value (e.g., compiling link tags to source malicious scripts), the CDN will cache the corrupted response and distribute it to subsequent legitimate users.
* *Mitigation:* Force absolute, explicit internal routing rules within your reverse proxies, and sanitize edge key generation algorithms (`Cache Key Keys`) to verify headers before caching.

#### 3. Push-Ingest Propagation Delay Slumps
While push-based ingestion optimizes latency for high-demand event rollouts by avoiding origin-tier requests, updating or hot-fixing an asset relies on invalidation propagation pipelines.
* *Mechanics:* If a corrupted configuration file or broken frontend script is pushed out globally, it can take minutes for explicit purge commands to completely execute across every international edge node. This creates a data divergence window where users across different regions continue to receive the broken cached code.
* *Mitigation:* Pair push architectures with content-hashed immutable URLs (e.g., `bundle.a8f9c2.js`) rather than using static filenames (e.g., `bundle.js`), completely bypassing edge stale windows during updates.

---

### Ingress Header Telemetry Checklist
When engineering edge proxy definitions, ensure standard transit variables are verified to prevent tracking loss:
* `Cache-Control: public, max-age=31536000, immutable` — Enforces persistent edge retention for immutable static nodes.
* `Surrogate-Key` / `Tags` — Appends custom indexing names to response headers, enabling instant, atomic bulk purging of related items across global PoPs out-of-band.

---

> **Scaling context:** Caching is step 2 on the escalation ladder — see [Scaling Strategies Overview](/system-design/scaling-strategies-overview/). Pair with [Latency vs Throughput](/system-design/latency-vs-throughput/) for cache hit SLOs.

---
