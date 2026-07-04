---
title: "Troubleshooting Questions"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Troubleshooting-focused subset from Redis interview question bank."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Troubleshoot Q"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.3"
weight: 803
interviewHandbook: true
---

Troubleshooting-focused subset with **inline answers**.

# Troubleshooting Questions

<!-- interview-guide-answers:start -->

### Q41. How do you triage sudden memory growth when used_memory rises but key count looks stable?

### Short Answer
The production-grade Redis answer is separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Detailed Explanation
Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Internal Working
`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Common Mistakes
Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Follow-up Questions
Which encoding upgrade or key-shape change would you test first to reduce memory for: How do you triage sudden memory growth when used_memory rises but key count looks stable?

---
### Q42. What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure after a hard kill test?

---
### Q43. How would you diagnose replication lag that only appears during peak write hours?

### Short Answer
The practical Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How would you diagnose replication lag that only appears during peak write hours.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How would you diagnose replication lag that only appears during peak write hours.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How would you diagnose replication lag that only appears during peak write hours.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by correlating `master_repl_offset` with replica offsets and write spikes for: How would you diagnose replication lag that only appears during peak write hours.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How would you diagnose replication lag that only appears during peak write hours.

### Follow-up Questions
Which writes in: How would you diagnose replication lag that only appears during peak write hours require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q44. What does LATENCY DOCTOR tell you that SLOWLOG alone cannot?

### Short Answer
For this question, the architecturally correct Redis answer is correlating INFO sections, slowlog, and latency doctor before changing config during incidents for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Detailed Explanation
INFO exposes memory, stats, replication, and cluster state; SLOWLOG captures commands exceeding threshold for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Internal Working
Cluster health requires per-node slot coverage and lag metrics, not only primary CPU for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by defining dashboards for memory, ops/sec, lag, rejected connections, and evictions for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Common Mistakes
Running MONITOR in production destroys throughput — use targeted telemetry instead for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Follow-up Questions
Which three metrics would page you first for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot, and what thresholds?

---
### Q45. How do you find and remediate hot keys without KEYS or MONITOR in production?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: How do you find and remediate hot keys without KEYS or MONITOR in production in your architecture?

---
### Q46. What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary?

### Short Answer
The senior-level decision is treating Redis as a single-threaded command processor with optional I/O threading, then choosing HA topology to match RPO/RTO for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Detailed Explanation
Redis throughput scales vertically per primary until CPU, memory, or hot-key skew dominates; Sentinel and Cluster solve availability and horizontal scale, not magic parallelism on one key for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Internal Working
Commands execute serially on the event loop, so long operations block all clients on that node — architecture must keep hot paths O(1) and shard before CPU saturates for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts when comparing standalone, Sentinel, and Cluster for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Common Mistakes
A common mistake is assuming Redis is multi-threaded for commands or colocating unrelated blast-radius workloads on one cluster for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Follow-up Questions
What failover time, durability window, and client retry contract would you document before choosing topology for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary?

---
### Q47. How would you troubleshoot Cluster slot imbalance after adding a new primary?

### Short Answer
The practical Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you troubleshoot Cluster slot imbalance after adding a new primary appears in production metrics?

---
### Q48. What is your runbook when clients report MOVED storms after a resharding operation?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What is your runbook when clients report MOVED storms after a resharding operation.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What is your runbook when clients report MOVED storms after a resharding operation.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What is your runbook when clients report MOVED storms after a resharding operation.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What is your runbook when clients report MOVED storms after a resharding operation.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What is your runbook when clients report MOVED storms after a resharding operation.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What is your runbook when clients report MOVED storms after a resharding operation appears in production metrics?

---
### Q49. How do you debug Sentinel failover loops where primaries flap every few minutes?

### Short Answer
The production-grade Redis answer is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by running game-day failover tests with connection pool refresh metrics for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How do you debug Sentinel failover loops where primaries flap every few minutes?

---
### Q50. What causes writes to fail with OOM errors despite setting maxmemory?

### Short Answer
The senior-level decision is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: What causes writes to fail with OOM errors despite setting maxmemory.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: What causes writes to fail with OOM errors despite setting maxmemory.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: What causes writes to fail with OOM errors despite setting maxmemory.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by alerting before hit ratio collapses and testing eviction under synthetic fill for: What causes writes to fail with OOM errors despite setting maxmemory.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: What causes writes to fail with OOM errors despite setting maxmemory.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: What causes writes to fail with OOM errors despite setting maxmemory?

---
### Q51. How would you investigate volatile-lru not evicting keys when memory is full?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How would you investigate volatile-lru not evicting keys when memory is full.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How would you investigate volatile-lru not evicting keys when memory is full.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How would you investigate volatile-lru not evicting keys when memory is full.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: How would you investigate volatile-lru not evicting keys when memory is full.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How would you investigate volatile-lru not evicting keys when memory is full.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How would you investigate volatile-lru not evicting keys when memory is full?

---
### Q52. What forensic steps follow a partial AOF rewrite failure on restart?

### Short Answer
For this question, the architecturally correct Redis answer is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What forensic steps follow a partial AOF rewrite failure on restart.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What forensic steps follow a partial AOF rewrite failure on restart.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What forensic steps follow a partial AOF rewrite failure on restart.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing crash-recovery drills and measuring fork latency under peak write load for: What forensic steps follow a partial AOF rewrite failure on restart.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What forensic steps follow a partial AOF rewrite failure on restart.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What forensic steps follow a partial AOF rewrite failure on restart after a hard kill test?

---
### Q53. How do you detect and fix replica serving stale reads that break business rules?

### Short Answer
The production-grade Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How do you detect and fix replica serving stale reads that break business rules.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How do you detect and fix replica serving stale reads that break business rules.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How do you detect and fix replica serving stale reads that break business rules.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by correlating `master_repl_offset` with replica offsets and write spikes for: How do you detect and fix replica serving stale reads that break business rules.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How do you detect and fix replica serving stale reads that break business rules.

### Follow-up Questions
Which writes in: How do you detect and fix replica serving stale reads that break business rules require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q54. What explains consumer group pending entries growing without XPENDING visibility in dashboards?

### Short Answer
The senior-level decision is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring XPENDING depth and trimming with MAXLEN ~ for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: What explains consumer group pending entries growing without XPENDING visibility in dashboards?

---
### Q55. How would you troubleshoot cache stampede after a popular key expires simultaneously?

### Short Answer
The practical Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by load-testing synchronized expiry and hot-key miss scenarios for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: How would you troubleshoot cache stampede after a popular key expires simultaneously in your architecture?

---
### Q56. What mitigations apply when cache penetration hammers the database for non-existent IDs?

### Short Answer
For this question, the architecturally correct Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by load-testing synchronized expiry and hot-key miss scenarios for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What mitigations apply when cache penetration hammers the database for non-existent IDs in your architecture?

---
### Q57. How do you debug distributed lock double-execution after TTL expiry?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you debug distributed lock double-execution after TTL expiry.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you debug distributed lock double-execution after TTL expiry.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you debug distributed lock double-execution after TTL expiry.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How do you debug distributed lock double-execution after TTL expiry.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you debug distributed lock double-execution after TTL expiry.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you debug distributed lock double-execution after TTL expiry outlives the Redis lock TTL?

---
### Q58. What would you check when BGSAVE consistently fails during memory pressure events?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What would you check when BGSAVE consistently fails during memory pressure events.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What would you check when BGSAVE consistently fails during memory pressure events.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What would you check when BGSAVE consistently fails during memory pressure events.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: What would you check when BGSAVE consistently fails during memory pressure events.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What would you check when BGSAVE consistently fails during memory pressure events.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What would you check when BGSAVE consistently fails during memory pressure events after a hard kill test?

---
### Q59. How do you triage high CPU on Redis when QPS has not increased?

### Short Answer
The practical Redis answer is classifying the symptom (memory, lag, latency, routing) before applying config changes for: How do you triage high CPU on Redis when QPS has not increased.

### Detailed Explanation
Hot keys skew CPU on one shard; big keys inflate latency and replication cost — diagnose with `--hotkeys`, memory sampling, and slowlog for: How do you triage high CPU on Redis when QPS has not increased.

### Internal Working
Replication lag may be backlog, network, or write spike — not always replica hardware for: How do you triage high CPU on Redis when QPS has not increased.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew with a written runbook and rollback criteria for each remediation step for: How do you triage high CPU on Redis when QPS has not increased.

### Common Mistakes
Using KEYS, FLUSHALL without ASYNC, or failover without client drain worsens many incidents for: How do you triage high CPU on Redis when QPS has not increased.

### Follow-up Questions
What evidence proves root cause versus symptom for: How do you triage high CPU on Redis when QPS has not increased before you close the incident?

---
### Q60. What client-side symptoms indicate connection pool exhaustion versus server maxclients?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Follow-up Questions
What requirement in: What client-side symptoms indicate connection pool exhaustion versus server maxclients is decisive if throughput numbers are similar across options?

---
### Q61. How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster?

### Short Answer
The production-grade Redis answer is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Follow-up Questions
How do you version and deploy script changes safely for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster across rolling restarts?

---
### Q62. What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle?

### Short Answer
The senior-level decision is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle appears in production metrics?

---
### Q63. How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning?

### Short Answer
The practical Redis answer is correlating INFO sections, slowlog, and latency doctor before changing config during incidents for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Detailed Explanation
INFO exposes memory, stats, replication, and cluster state; SLOWLOG captures commands exceeding threshold for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Internal Working
Cluster health requires per-node slot coverage and lag metrics, not only primary CPU for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by defining dashboards for memory, ops/sec, lag, rejected connections, and evictions for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Common Mistakes
Running MONITOR in production destroys throughput — use targeted telemetry instead for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Follow-up Questions
Which three metrics would page you first for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning, and what thresholds?

---
### Q64. What causes mem_fragmentation_ratio to climb and when is active defrag appropriate?

### Short Answer
For this question, the architecturally correct Redis answer is separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Detailed Explanation
Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Internal Working
`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Common Mistakes
Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Follow-up Questions
Which encoding upgrade or key-shape change would you test first to reduce memory for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate?

---
### Q65. How would you troubleshoot session loss after a Sentinel failover during peak traffic?

### Short Answer
The production-grade Redis answer is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by running game-day failover tests with connection pool refresh metrics for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How would you troubleshoot session loss after a Sentinel failover during peak traffic?

---
### Q66. What diagnostics differentiate network partition from overloaded primary during timeout storms?

### Short Answer
The senior-level decision is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by validating command complexity and memory per key for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Follow-up Questions
Which type would you choose for: What diagnostics differentiate network partition from overloaded primary during timeout storms, and what command path proves it under peak cardinality?

---
### Q67. How do you debug rate limiter drift when counters look correct per key but limits feel wrong?

### Short Answer
The practical Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing boundary bursts at window edges for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Follow-up Questions
How would you shard a global rate limit key if: How do you debug rate limiter drift when counters look correct per key but limits feel wrong saturates one Redis primary?

---
### Q68. What steps validate AOF integrity before promoting a rebuilt replica?

### Short Answer
For this question, the architecturally correct Redis answer is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What steps validate AOF integrity before promoting a rebuilt replica.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What steps validate AOF integrity before promoting a rebuilt replica.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What steps validate AOF integrity before promoting a rebuilt replica.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing crash-recovery drills and measuring fork latency under peak write load for: What steps validate AOF integrity before promoting a rebuilt replica.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What steps validate AOF integrity before promoting a rebuilt replica.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What steps validate AOF integrity before promoting a rebuilt replica after a hard kill test?

---
### Q69. How would you investigate Pub/Sub subscribers missing invalidation messages intermittently?

### Short Answer
The production-grade Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by defining who invalidates on partial updates and out-of-order writes for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently updates one entity?

---
### Q70. What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec?

### Short Answer
The senior-level decision is classifying the symptom (memory, lag, latency, routing) before applying config changes for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Detailed Explanation
Hot keys skew CPU on one shard; big keys inflate latency and replication cost — diagnose with `--hotkeys`, memory sampling, and slowlog for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Internal Working
Replication lag may be backlog, network, or write spike — not always replica hardware for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts with a written runbook and rollback criteria for each remediation step for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Common Mistakes
Using KEYS, FLUSHALL without ASYNC, or failover without client drain worsens many incidents for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Follow-up Questions
What evidence proves root cause versus symptom for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec before you close the incident?

---

<!-- interview-guide-answers:end -->

---

## See Also

- [Previous: Architect Questions](/redis-cheatsheet/08-interview-guide/architect-questions/)
- [Next: Performance Questions](/redis-cheatsheet/08-interview-guide/performance-questions/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
- [Redis Handbook Index](/redis-cheatsheet/)
