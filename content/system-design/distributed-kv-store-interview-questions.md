---
title: "Distributed Key-Value Store (Memcached-Style) — Interview Questions"
date: 2026-06-27T11:30:00+00:00
draft: false
description: "50 senior-level system design interview questions and answers for a Memcached-style distributed key-value cache — LRU internals, consistent hashing, replication lag, cache stampedes, and production failure recovery."
tags: ["system-design", "interview", "distributed-systems", "caching", "memcached", "architecture"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Distributed Key-Value Store (Memcached-Style) at Scale](/system-design/distributed-kv-store/). These questions probe lock-striped LRU internals, consistent hashing trade-offs, async replication semantics, cache avalanche mitigation, and production failover — the topics interviewers dig into after the whiteboard diagram.

---

## Architecture & Trade-offs (1–10)

**1. Why build a custom in-memory engine instead of deploying Redis or Memcached off the shelf?**

Redis bundles structured data types, Lua scripting, and optional disk persistence (RDB/AOF) that add memory and CPU overhead. Memcached is single-threaded per instance. A stripped-down, multithreaded engine optimized for opaque blob get/put/delete maximizes raw throughput and memory efficiency at 23M+ peak RPS.

**2. Why favor an embedded client library over a centralized proxy (e.g. Twemproxy) for request routing?**

A proxy introduces an extra network hop on every operation, adding latency that breaks the sub-2ms p99 budget. An embedded library computes consistent-hash destinations locally and connects directly to the correct shard.

**3. Why is disk persistence excluded from this architecture?**

Write-ahead logging and snapshot I/O introduce unpredictable latency spikes. This is an ephemeral cache — durability comes from replication across nodes and rebuilding from the persistent database on cold start, not from on-disk recovery.

**4. How does this design achieve 99.999% availability for cache queries?**

Every primary shard runs with at least two read replicas across different availability zones. Automated failover via ZooKeeper heartbeats promotes a replica when the primary dies. Client libraries receive topology updates and reroute within seconds.

**5. When would you choose strict consistency over the default eventual consistency model?**

For keys where stale reads cause business-critical errors — financial balances, inventory counts, or session tokens after logout. In strict mode, reads route to the primary or use quorum reads that verify replication offset.

**6. Why use ZooKeeper instead of DNS-based service discovery for cache topology?**

DNS has TTL-based propagation delays (minutes). ZooKeeper watch notifications push membership changes to clients in near real-time — critical when a shard fails and thousands of clients must reroute immediately.

**7. What is the trade-off of async replication vs synchronous quorum writes?**

Async replication maximizes write throughput and keeps p99 latency low, but replicas may serve data that is milliseconds to seconds behind the primary. Sync quorum adds round-trip latency per write but guarantees replicas are up to date before acknowledging.

**8. Why decouple the cache cluster from application servers instead of co-locating cache daemons on app machines?**

Co-location creates resource contention between application logic and cache memory management. A dedicated cluster allows independent scaling of RAM and compute — application pods scale on CPU; cache nodes scale on memory and network I/O.

**9. How does gRPC over HTTP/2 benefit internal cache communication compared to REST?**

Binary protobuf serialization reduces payload overhead. HTTP/2 multiplexing allows multiple in-flight requests over a single TCP connection, reducing connection setup cost at millions of RPS.

**10. Why is PostgreSQL retained as a fallback store if the cache is designed to absorb all reads?**

The cache is ephemeral — keys expire, nodes fail, and cold starts empty the cluster. PostgreSQL (or Spanner) remains the source of truth. Cache misses must resolve somewhere; the DB is only hit on miss, keeping it off the hot path at ≥ 85% hit rate.

---

## Data Structures & Concurrency (11–20)

**11. Why favor lock striping over Java's default ConcurrentHashMap for the LRU engine?**

ConcurrentHashMap locks at the bucket level, which works for standard map operations. LRU requires updating the doubly linked list on every read to move the node to the head. Lock striping groups both the hash index and linked-list mutations under 64 independent stripe locks, reducing global contention.

**12. What happens if two threads access keys that hash to the same lock stripe simultaneously?**

They serialize on that stripe's write lock. Keys mapping to different stripes proceed concurrently. With 64 stripes and uniformly distributed keys, contention probability is low except for extreme hot-key scenarios on the same stripe.

**13. How do you defend against cache avalanche when a massive batch of keys expires simultaneously?**

Apply jittered expirations: `TTL = BaseTTL + Random(0, JitterWindow)`. This spreads expirations over time instead of creating a synchronized miss spike that overwhelms the persistent database.

**14. Why store the key string redundantly in both the hash map and the LRU linked-list node?**

During tail eviction, the system removes the LRU node and must delete the corresponding hash-map entry. Without the redundant key copy, eviction would require an expensive reverse lookup from node pointer to key.

**15. How does Check-And-Set (CAS) prevent lost updates without multi-key transactions?**

Each successful `put` returns a monotonically increasing `cas_version`. A subsequent `put` with `X-CAS-Token` succeeds only if the version matches. If another client updated the key in between, the server returns `409 Conflict` and the caller must re-read and retry.

**16. Is a `get` operation that moves a node to the LRU head considered a write lock operation?**

Yes. In this design, every `get` acquires the stripe write lock to update linked-list topology. This is intentional — read-lock would not protect against concurrent list mutations. The stripe granularity keeps the critical section short.

**17. How do you handle expired keys that are never accessed again (cold expiration)?**

A background sweeper thread periodically walks LRU tail nodes and removes entries whose `expires_at` is in the past. This prevents "zombie" entries from occupying memory until LRU eviction eventually reaches them.

**18. What structural changes occur if keys expand from simple strings to composite multi-attribute identifiers?**

The client library serializes composite attributes into a deterministic delimited string (e.g. `tenant:country:status:value`) before hashing. The core engine remains a simple string-key store; structured routing logic lives at the application layer.

**19. How does consistent hashing minimize key redistribution when a node joins or leaves the cluster?**

Only keys on the added/removed vnode range move — unlike `hash(key) % N`. Ring mechanics: [Consistent Hashing](/system-design/consistent-hashing/).

**20. Why use MurmurHash3 specifically for key-to-shard mapping?**

MurmurHash3 provides fast, well-distributed 32/128-bit hashes with low collision rates. Deterministic output from the same key string is required — cryptographic hashes (SHA-256) are unnecessarily slow for routing decisions.

---

## Scaling & Hot Keys (21–30)

**21. How does consistent hashing address the hot key problem where a single key receives millions of requests per second?**

Consistent hashing alone does not — a single hot key maps to one shard. The system implements key diversification: the client appends a random suffix index (e.g. `homepage:payload_sub_4`), creating multiple copies distributed across virtual nodes. Reads fan out to any copy.

**22. When should you trigger a shard split vs adding more replicas?**

Add replicas when read RPS exceeds per-node capacity but memory is sufficient. Split the shard when memory utilization exceeds ~80% sustained or write RPS per primary exceeds ~1.5M — splitting divides the key range across two new primaries.

**23. What is the purpose of virtual nodes on the consistent hashing ring?**

Even distribution and smaller rebalance units per physical node — see [Consistent Hashing](/system-design/consistent-hashing/) § virtual nodes.

**24. How do you add a new shard to the cluster without downtime?**

Register the new node in ZooKeeper. Clients receive the topology watch event and gradually remap keys that fall on the new node's virtual positions. Existing data on old shards is not migrated immediately — it expires naturally via TTL or LRU, then repopulates on miss.

**25. What happens to throughput when you double the number of shards?**

Write and memory capacity scale roughly linearly. Read capacity scales with the number of replicas, not shards alone. Network bandwidth per node decreases as load spreads, but coordination overhead (ZooKeeper watches, client ring updates) grows logarithmically.

**26. How do you prevent a neighboring shard from overloading when a failed node's key range redistributes?**

Two-way virtual node configuration ensures the failed node's traffic distributes across multiple healthy shards rather than dumping entirely onto the immediate clockwise neighbor on the ring.

**27. At what point does cross-region replication become necessary?**

When intercontinental users experience > 100 ms round-trip latency to a single central region. Regional cache clusters with localized reads/writes eliminate transcontinental network hops.

**28. How do you size the number of lock stripes (64 in this design)?**

More stripes reduce contention but increase memory overhead for lock objects. 64 is a practical default for 16-vCPU nodes — roughly 4 concurrent operations per stripe at peak. Profile and tune based on contention metrics.

**29. Why scale on network I/O metrics rather than CPU for cache nodes?**

Cache nodes are memory- and network-bound. CPU utilization stays low because operations are simple pointer lookups and byte copies. Network saturation at 12.5 Gbps per `r6i.4xlarge` instance is the practical bottleneck.

**30. How do you handle a scenario where the 20 TB active working set assumption proves wrong (cold data is accessed more than expected)?**

Monitor cache hit rate. If it drops below 85%, increase cluster RAM, tighten TTLs on cold keys, or re-evaluate the Pareto assumption with access-frequency histograms. Consider a second-tier warm cache (SSD-backed) for warm-but-not-hot data.

---

## Operations & Resiliency (31–40)

**31. Walk through recovery when a primary cache shard suddenly dies.**

ZooKeeper detects the heartbeat loss within seconds. A read replica initiates leader election and promotes itself to primary. ZooKeeper broadcasts the updated topology. Client libraries reroute writes to the new primary. In-flight writes to the dead primary fail fast; clients retry.

**32. What happens during a network partition between replication zones?**

The primary continues accepting writes (availability prioritized). Isolated replicas serve potentially stale reads. When the partition heals, the primary streams its replication backlog to synchronize followers.

**33. Detail your recovery process when an entire cloud availability zone suffers a complete blackout.**

Multi-AZ replication ensures surviving zones hold replica copies. ZooKeeper removes all nodes in the dark AZ from the active topology. Clients immediately redirect to healthy replicas in surviving AZs. No manual intervention required if quorum is maintained.

**34. How do you mitigate thundering herd when a highly popular key expires?**

The client library acquires a distributed mutex on cache miss. Only the first thread queries the database; subsequent threads wait briefly and retry the cache. Combined with TTL jitter, this prevents synchronized DB stampedes.

**35. What alert metrics indicate the cache cluster is unhealthy?**

Cache hit rate < 85%, p99 latency > 2 ms sustained, memory utilization > 90% without evictions running, replication lag > 5 s, or ZooKeeper session expirations spiking.

**36. How do you perform a rolling upgrade of cache node software without dropping queries?**

Upgrade replicas first (reads shift to other replicas). Promote an upgraded replica to primary. Upgrade the old primary last. Clients handle brief topology changes via ZooKeeper watches.

**37. What is the impact of a ZooKeeper ensemble outage on the running cache cluster?**

Running nodes continue serving requests with the last-known topology cached in client libraries. New nodes cannot join, and failovers cannot be orchestrated until quorum is restored. Maintain a 5-node ensemble with observers to reduce write load.

**38. How do you test failover behavior before production deployment?**

Use chaos engineering (Chaos Mesh, Gremlin) to kill primary pods, inject network partitions, and verify client rerouting, replication catch-up, and hit-rate recovery within SLO targets.

**39. How do you handle mTLS certificate rotation without downtime?**

SPIFFE/SPIRE issues short-lived certificates (hours to days) with automatic rotation. Dual-trust windows allow both old and new CA certificates during the rotation window.

**40. What happens if the persistent database is slow or down while the cache is healthy?**

Cache hits continue serving at full speed. Cache misses fail or time out when calling the DB. Circuit breakers in the client library stop hammering the DB and can serve stale cache values (if configured) or return degraded responses.

---

## Advanced Optimization (41–50)

**41. How do you tune kernel-level socket parameters for sub-millisecond cache latency?**

Increase `SO_RCVBUF`/`SO_SNDBUF`, enable TCP_NODELAY to disable Nagle's algorithm, use `SO_REUSEPORT` for multi-threaded accept, and pin cache threads to NUMA-local CPU cores on bare-metal instances.

**42. What is memory defragmentation and when does it matter for this engine?**

Frequent `put`/`delete` cycles fragment the JVM heap or custom allocator. Fragmentation increases allocation latency and RSS beyond logical data size. Run periodic compaction or use slab allocators with fixed-size buckets aligned to common value sizes.

**43. How do you minimize cross-AZ network costs for replication traffic?**

Keep replication within the same region across AZs (necessary for HA). For cross-region, compress replication logs and batch updates. Only replicate hot-key subsets to remote regions if full replication is cost-prohibitive.

**44. Can you use HTTP/2 Server-Sent Events for cache invalidation notifications to clients?**

For application-tier cache invalidation (not the internal cache protocol), SSE over HTTP/2 is viable for pushing invalidation events to app servers. The cache nodes themselves use async replication logs, not SSE.

**45. How do you protect against denial-of-service via oversized payloads?**

Enforce the 1 MB payload limit at the API gateway before the request reaches cache nodes. Rate-limit per client identity (mTLS service name) with token bucket algorithms returning `429 Too Many Requests`.

**46. Why use cache-aside invalidation instead of write-through on every database update?**

Write-through risks a race: Thread A writes DB, Thread B writes DB, Thread A writes stale value to cache. Invalidation (delete) ensures the next read fetches fresh data from DB and repopulates the cache.

**47. How do you implement request coalescing for identical in-flight `get` requests?**

The client library maintains a per-key `CompletableFuture` map. Concurrent `get` calls for the same key attach to a single in-flight network request. When the response arrives, all waiters receive the result.

**48. What observability signals help distinguish replication lag from a true cache miss?**

Tag responses with `X-Replica-Lag-Ms` header. If lag is high and the value exists on the replica, it is a stale read — not a miss. True misses return `404` with no CAS token.

**49. How would you benchmark this system to validate the sub-2ms p99 target?**

Use coordinated load generators (e.g. memtier_benchmark, custom gRPC clients) from the same AZ. Measure at client library level (not server-only). Run at 2× peak RPS for 30 minutes. Track p50/p95/p99/p999 separately for reads and writes.

**50. What are the main risks of evolving from Stage 3 (read replicas) to Stage 5 (multi-region active-active)?**

Cross-region write conflicts on the same key, increased operational complexity, higher replication costs, and difficulty maintaining a global hit-rate SLO when regional working sets diverge. Conflict resolution (last-write-wins or CRDT) must be explicitly designed.
