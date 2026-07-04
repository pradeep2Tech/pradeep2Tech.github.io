---
title: "Performance Questions"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Performance-focused subset from Redis interview question bank."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Perf Q"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.4"
weight: 804
interviewHandbook: true
---

Performance-focused subset with **inline answers**.

# Performance Questions

<!-- interview-guide-answers:start -->

### Q71. How does pipelining improve throughput without changing Redis single-threaded execution?

### Short Answer
The practical Redis answer is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How does pipelining improve throughput without changing Redis single-threaded execution, and what cluster slot constraints apply?

---
### Q72. What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO?

### Short Answer
For this question, the architecturally correct Redis answer is using RESP over TCP with connection pooling and pipelining to cut round trips without expecting multi-command parallelism on the server for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Detailed Explanation
Pipelining batches many commands in one RTT while Redis still executes them sequentially — throughput gains come from network efficiency, not parallel command threads for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Internal Working
Cluster clients must handle MOVED/ASK redirects and maintain slot maps; protocol-level retries differ from application idempotency for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by profiling client RTT versus server `slowlog` entries for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Common Mistakes
A frequent mistake is huge pipelines without backpressure, causing timeouts and memory pressure on both client and server for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Follow-up Questions
What pipeline batch size and timeout would you cap for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO given your p99 SLO?

---
### Q73. When does MGET outperform pipelined GET for the same key batch?

### Short Answer
The production-grade Redis answer is using RESP over TCP with connection pooling and pipelining to cut round trips without expecting multi-command parallelism on the server for: When does MGET outperform pipelined GET for the same key batch.

### Detailed Explanation
Pipelining batches many commands in one RTT while Redis still executes them sequentially — throughput gains come from network efficiency, not parallel command threads for: When does MGET outperform pipelined GET for the same key batch.

### Internal Working
Cluster clients must handle MOVED/ASK redirects and maintain slot maps; protocol-level retries differ from application idempotency for: When does MGET outperform pipelined GET for the same key batch.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by profiling client RTT versus server `slowlog` entries for: When does MGET outperform pipelined GET for the same key batch.

### Common Mistakes
A frequent mistake is huge pipelines without backpressure, causing timeouts and memory pressure on both client and server for: When does MGET outperform pipelined GET for the same key batch.

### Follow-up Questions
What pipeline batch size and timeout would you cap for: When does MGET outperform pipelined GET for the same key batch given your p99 SLO?

---
### Q74. How do large values in strings affect network and latency more than CPU on the server?

### Short Answer
The senior-level decision is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How do large values in strings affect network and latency more than CPU on the server.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How do large values in strings affect network and latency more than CPU on the server.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How do large values in strings affect network and latency more than CPU on the server.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts using slowlog, latency doctor, and before/after benchmarks for: How do large values in strings affect network and latency more than CPU on the server.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How do large values in strings affect network and latency more than CPU on the server.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How do large values in strings affect network and latency more than CPU on the server?

---
### Q75. What command choices turn O(1) expectations into O(N) event-loop blockers?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Follow-up Questions
Which type would you choose for: What command choices turn O(1) expectations into O(N) event-loop blockers, and what command path proves it under peak cardinality?

---
### Q76. How would you tune io-threads and io-threads-do-reads for a read-heavy workload?

### Short Answer
For this question, the architecturally correct Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology using slowlog, latency doctor, and before/after benchmarks for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload?

---
### Q77. What is the performance impact of appendfsync always versus everysec for write-heavy caches?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Follow-up Questions
What requirement in: What is the performance impact of appendfsync always versus everysec for write-heavy caches is decisive if throughput numbers are similar across options?

---
### Q78. How does RDB fork latency interact with memory overcommit and COW during BGSAVE?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE after a hard kill test?

---
### Q79. When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

---
### Q80. How do maxmemory-samples settings affect eviction accuracy and CPU?

### Short Answer
For this question, the architecturally correct Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by alerting before hit ratio collapses and testing eviction under synthetic fill for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How do maxmemory-samples settings affect eviction accuracy and CPU?

---
### Q81. What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds?

### Short Answer
The production-grade Redis answer is separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Detailed Explanation
Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Internal Working
`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Common Mistakes
Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Follow-up Questions
Which encoding upgrade or key-shape change would you test first to reduce memory for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds?

---
### Q82. How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Follow-up Questions
What requirement in: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance is decisive if throughput numbers are similar across options?

---
### Q83. What client connection pool sizing formula avoids Redis maxclients saturation?

### Short Answer
The practical Redis answer is sizing memory as key count × (value + metadata overhead) plus replication and headroom for fork for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Detailed Explanation
Plan growth with key cardinality forecasts, encoding assumptions, and replica factor — Cluster adds coordination overhead for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Internal Working
Connection count from many pods can exhaust `maxclients` before memory fills for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew with load tests that include failover and snapshot windows for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Common Mistakes
Sizing only for data bytes without overhead, replicas, or COW margin causes emergency scale events for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Follow-up Questions
At what memory or ops/sec threshold would you trigger horizontal scale for: What client connection pool sizing formula avoids Redis maxclients saturation?

---
### Q84. How does TLS add latency, and where would you terminate TLS for cache workloads?

### Short Answer
For this question, the architecturally correct Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology using slowlog, latency doctor, and before/after benchmarks for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How does TLS add latency, and where would you terminate TLS for cache workloads?

---
### Q85. When does sharding with Cluster improve throughput versus larger single-instance hardware?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Follow-up Questions
What requirement in: When does sharding with Cluster improve throughput versus larger single-instance hardware is decisive if throughput numbers are similar across options?

---
### Q86. How do BITOP and BITCOUNT scale poorly on large sparse bitmaps?

### Short Answer
The senior-level decision is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by validating command complexity and memory per key for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Follow-up Questions
Which type would you choose for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps, and what command path proves it under peak cardinality?

---
### Q87. What ZSET range query patterns need LIMIT to protect p99 latency?

### Short Answer
The practical Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew using slowlog, latency doctor, and before/after benchmarks for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: What ZSET range query patterns need LIMIT to protect p99 latency?

---
### Q88. How would you optimize a sliding-window rate limiter implemented with sorted sets?

### Short Answer
For this question, the architecturally correct Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing boundary bursts at window edges for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Follow-up Questions
How would you shard a global rate limit key if: How would you optimize a sliding-window rate limiter implemented with sorted sets saturates one Redis primary?

---
### Q89. What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

### Short Answer
The production-grade Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention using slowlog, latency doctor, and before/after benchmarks for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

---
### Q90. How does replication backlog sizing affect partial resync performance after brief outages?

### Short Answer
The senior-level decision is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How does replication backlog sizing affect partial resync performance after brief outages.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How does replication backlog sizing affect partial resync performance after brief outages.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How does replication backlog sizing affect partial resync performance after brief outages.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by correlating `master_repl_offset` with replica offsets and write spikes for: How does replication backlog sizing affect partial resync performance after brief outages.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How does replication backlog sizing affect partial resync performance after brief outages.

### Follow-up Questions
Which writes in: How does replication backlog sizing affect partial resync performance after brief outages require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q91. What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Follow-up Questions
Which type would you choose for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026, and what command path proves it under peak cardinality?

---
### Q92. How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew appears in production metrics?

---
### Q93. When does probabilistic early expiration improve tail latency versus naive TTL refresh?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Follow-up Questions
What requirement in: When does probabilistic early expiration improve tail latency versus naive TTL refresh is decisive if throughput numbers are similar across options?

---
### Q94. How do Streams MAXLEN approximate trimming trade memory for ingestion throughput?

### Short Answer
The senior-level decision is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring XPENDING depth and trimming with MAXLEN ~ for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput?

---
### Q95. What metrics prove your cache hit ratio improvements actually reduced database load?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Follow-up Questions
Which type would you choose for: What metrics prove your cache hit ratio improvements actually reduced database load, and what command path proves it under peak cardinality?

---

<!-- interview-guide-answers:end -->

---

## See Also

- [Previous: Troubleshooting Questions](/redis-cheatsheet/08-interview-guide/troubleshooting-questions/)
- [Next: Senior Engineer Path](/redis-cheatsheet/09-learning-paths/redis-senior-engineer-path/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
- [Redis Handbook Index](/redis-cheatsheet/)
