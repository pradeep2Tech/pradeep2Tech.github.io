---
title: "Redis Concept Registry"
date: 2026-07-03T13:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per Redis concept."
tags: ["redis-cheatsheet", "meta", "planning"]
---

# Redis Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase B — registry enforced on moved pages; answer layer in Phase C.

---

## Runtime & Fundamentals

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Single-threaded command execution | `01-fundamentals/architecture.md` | Exists | I/O threads → same page |
| Event loop / epoll | `01-fundamentals/architecture.md` | Exists | |
| I/O threads (Redis 6+) | `01-fundamentals/architecture.md` | Exists | |
| Keyspace (global dict → robj) | `01-fundamentals/architecture.md` | Exists | |
| Data type selection matrix | `01-fundamentals/data-structures.md` | Exists | Not per-type command depth |
| Key naming conventions | `01-fundamentals/data-structures.md` | Exists | |
| TTL on keys (not fields) | `01-fundamentals/data-structures.md` | Exists | |
| TYPE / OBJECT ENCODING inspection | `01-fundamentals/data-structures.md` | Exists | Encoding internals → memory-management |

---

## Core Data Types

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Strings (binary-safe, counters) | `02-core-redis/strings.md` | Exists | |
| String encodings (int, embstr, raw) | `03-redis-internals/memory-management.md` | **Planned** | Type page: ≤2 sentences |
| Hashes (field maps) | `02-core-redis/hashes.md` | Exists | |
| Lists (queues, stacks) | `02-core-redis/lists.md` | Exists | |
| Sets (membership, algebra) | `02-core-redis/sets.md` | Exists | |
| Sorted sets (rank, score) | `02-core-redis/sorted-sets.md` | Exists | |
| Bitmaps (bit arrays on strings) | `02-core-redis/bitmaps.md` | Exists | |
| HyperLogLog (cardinality sketch) | `02-core-redis/hyperloglog.md` | Exists | |
| GEO (sorted-set backed) | `02-core-redis/sorted-sets.md` | Exists | Mention in data-structures only |

---

## Internals & Protocol

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Redis memory model | `03-redis-internals/memory-management.md` | **Planned** | |
| `used_memory` vs `used_memory_rss` | `03-redis-internals/memory-management.md` | **Planned** | |
| jemalloc / allocator behavior | `03-redis-internals/memory-management.md` | **Planned** | |
| Encodings (ziplist, listpack, intset, hashtable, skiplist) | `03-redis-internals/memory-management.md` | **Planned** | |
| Memory fragmentation | `03-redis-internals/memory-management.md` | **Planned** | |
| Memory optimization (`MEMORY PURGE`, key design) | `03-redis-internals/memory-management.md` | **Planned** | |
| `MEMORY USAGE` / `MEMORY STATS` | `03-redis-internals/memory-management.md` | **Planned** | |
| RESP protocol | `03-redis-internals/redis-protocol.md` | **Planned** | |
| Pipelining | `03-redis-internals/redis-protocol.md` | **Planned** | |
| Client request processing path | `03-redis-internals/redis-protocol.md` | **Planned** | |
| RDB snapshots | `03-redis-internals/persistence.md` | Exists | |
| AOF append-only log | `03-redis-internals/persistence.md` | Exists | |
| `appendfsync` modes | `03-redis-internals/persistence.md` | Exists | |
| BGSAVE / fork / copy-on-write | `03-redis-internals/persistence.md` | Exists | |
| AOF rewrite / hybrid RDB preamble | `03-redis-internals/persistence.md` | Exists | Phase B deepen |
| Primary-replica replication | `03-redis-internals/replication.md` | Exists | |
| Partial resync / replication backlog | `03-redis-internals/replication.md` | Exists | |
| `WAIT` command (sync replication) | `03-redis-internals/replication.md` | Exists | Phase B deepen |
| Replica read scaling / stale reads | `03-redis-internals/replication.md` | Exists | |
| Sentinel (monitoring, failover) | `03-redis-internals/sentinel.md` | Exists | |
| Sentinel quorum / SDOWN / ODOWN | `03-redis-internals/sentinel.md` | Exists | |
| Redis Cluster | `03-redis-internals/cluster.md` | Exists | |
| Hash slots (16384) | `03-redis-internals/cluster.md` | Exists | |
| Hash tags `{tag}` | `03-redis-internals/cluster.md` | Exists | |
| MOVED / ASK redirects | `03-redis-internals/cluster.md` | Exists | |
| Cluster resharding | `03-redis-internals/cluster.md` | Exists | Phase B deepen |
| Cluster-aware clients | `03-redis-internals/cluster.md` | Exists | |

---

## Distributed Systems & Coordination

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| MULTI / EXEC transactions | `04-distributed-systems/transactions.md` | Exists | |
| WATCH optimistic locking | `04-distributed-systems/transactions.md` | Exists | |
| Pipeline vs transaction | `04-distributed-systems/transactions.md` | Exists | |
| Pub/Sub (fire-and-forget) | `04-distributed-systems/pub-sub.md` | Exists | |
| Pattern subscribe (PSUBSCRIBE) | `04-distributed-systems/pub-sub.md` | Exists | |
| Streams (append-only log) | `04-distributed-systems/streams.md` | Exists | |
| Consumer groups | `04-distributed-systems/streams.md` | Exists | |
| XACK / XPENDING / XCLAIM | `04-distributed-systems/streams.md` | Exists | |
| Lua scripts (EVAL / EVALSHA) | `04-distributed-systems/lua-scripts.md` | Exists | |
| Redis Functions (Redis 7+) | `04-distributed-systems/lua-scripts.md` | Exists | Phase B deepen |
| Distributed locks | `04-distributed-systems/distributed-lock.md` | Exists | |
| Redlock debate | `04-distributed-systems/distributed-lock.md` | Exists | |
| Fencing tokens | `04-distributed-systems/distributed-lock.md` | Exists | |

---

## Production Patterns

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Cache-aside pattern | `05-production-patterns/caching-patterns.md` | Exists | |
| Read-through / write-through overview | `05-production-patterns/caching-patterns.md` | Exists | |
| Cache refresh strategies | `05-production-patterns/cache-invalidation.md` | **Planned** | |
| Write-through | `05-production-patterns/cache-invalidation.md` | **Planned** | |
| Write-behind | `05-production-patterns/cache-invalidation.md` | **Planned** | |
| Cache-aside invalidation | `05-production-patterns/cache-invalidation.md` | **Planned** | |
| Pub/Sub invalidation broadcast | `05-production-patterns/cache-invalidation.md` | **Planned** | Transport → pub-sub |
| Cache breakdown (hot key) | `05-production-patterns/cache-breakdown.md` | **Planned** | |
| Cache avalanche (expiration storm) | `05-production-patterns/cache-avalanche.md` | **Planned** | |
| TTL jitter | `05-production-patterns/cache-avalanche.md` | **Planned** | Brief mention in caching-patterns OK |
| Cache penetration | `05-production-patterns/cache-penetration.md` | **Planned** | |
| Bloom filter / negative cache | `05-production-patterns/cache-penetration.md` | **Planned** | |
| Session store pattern | `05-production-patterns/session-store.md` | Exists | |
| Rate limiting (fixed window) | `05-production-patterns/rate-limiter.md` | Exists | |
| Sliding window rate limit | `05-production-patterns/rate-limiter.md` | Exists | |
| Token bucket | `05-production-patterns/rate-limiter.md` | Exists | |

---

## Performance & Operations

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| `maxmemory` | `06-performance-operations/eviction-policies.md` | Exists | |
| Eviction policies (LRU/LFU/TTL) | `06-performance-operations/eviction-policies.md` | Exists | |
| Approximate LRU sampling | `06-performance-operations/eviction-policies.md` | Exists | |
| Latency analysis | `06-performance-operations/performance-tuning.md` | **Planned** | |
| Pipeline optimization | `06-performance-operations/performance-tuning.md` | **Planned** | Protocol page links here |
| Command optimization (big keys) | `06-performance-operations/performance-tuning.md` | **Planned** | |
| Throughput tuning | `06-performance-operations/performance-tuning.md` | **Planned** | |
| INFO command sections | `06-performance-operations/monitoring.md` | **Planned** | |
| SLOWLOG | `06-performance-operations/monitoring.md` | **Planned** | |
| LATENCY DOCTOR / LATENCY HISTORY | `06-performance-operations/monitoring.md` | **Planned** | |
| Memory monitoring | `06-performance-operations/monitoring.md` | **Planned** | |
| Cluster monitoring | `06-performance-operations/monitoring.md` | **Planned** | |
| Memory sizing | `06-performance-operations/capacity-planning.md` | **Planned** | |
| Key count / growth estimation | `06-performance-operations/capacity-planning.md` | **Planned** | |
| Cluster node sizing | `06-performance-operations/capacity-planning.md` | **Planned** | |
| High memory usage triage | `06-performance-operations/troubleshooting.md` | **Planned** | |
| Replication lag triage | `06-performance-operations/troubleshooting.md` | **Planned** | |
| Failover issues | `06-performance-operations/troubleshooting.md` | **Planned** | |
| Hot key remediation | `06-performance-operations/troubleshooting.md` | **Planned** | |
| Slow commands / big keys | `06-performance-operations/troubleshooting.md` | **Planned** | |
| Cluster slot imbalance | `06-performance-operations/troubleshooting.md` | **Planned** | |
| KEYS vs SCAN | `06-performance-operations/troubleshooting.md` | **Planned** | |
| MONITOR misuse | `06-performance-operations/troubleshooting.md` | **Planned** | |

---

## Comparisons (Handbook Scope)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Redis vs Memcached | `07-comparisons/redis-vs-memcached.md` | **Planned** | Link `database-handbook/redis-vs-memcached` |
| Redis vs Kafka (streams/log) | `07-comparisons/redis-vs-kafka.md` | **Planned** | Not system-design handbook |
| Redis vs RabbitMQ (queues) | `07-comparisons/redis-vs-rabbitmq.md` | **Planned** | Broker selection only |

---

## Interview & Learning (Index Only)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Top 150 questions (Layer 1) | `08-interview-guide/top-150-interview-questions.md` | **Planned** | Questions only |
| Architect question subset | `08-interview-guide/architect-questions.md` | **Planned** | |
| Troubleshooting question subset | `08-interview-guide/troubleshooting-questions.md` | **Planned** | |
| Performance question subset | `08-interview-guide/performance-questions.md` | **Planned** | |
| Senior engineer learning path | `09-learning-paths/redis-senior-engineer-path.md` | **Planned** | |
| Lead learning path | `09-learning-paths/redis-lead-path.md` | **Planned** | |
| Architect learning path | `09-learning-paths/redis-architect-path.md` | **Planned** | |
| Interview revision path | `09-learning-paths/redis-interview-revision-path.md` | **Planned** | |

---

## Cross-Handbook (Link Only — Not Canonical Here)

| Concept | External canonical | Handbook rule |
| :--- | :--- | :--- |
| When to choose Redis (ADR) | `database-handbook/redis.md` | ≤2 sentences + link |
| Redis vs Memcached (enterprise ADR) | `database-handbook/redis-vs-memcached.md` | Handbook comparison deep dive; cross-link |
| Distributed caching in microservices | `microservices/` (if exists) | **Do not import** — out of scope |

---

## Enforcement Checklist (Phase B)

- [ ] Every concept row has exactly one **Exists** or **Planned** canonical path
- [ ] Non-canonical pages audited for paragraphs > 2 sentences on registered concepts
- [ ] Top 150 **Deep Dive** column resolves to canonical page URL
- [ ] Related Topics footers trimmed — one comparison link on `_index` only
- [ ] `build_redis_cheatsheet.py` respects registry on regeneration
