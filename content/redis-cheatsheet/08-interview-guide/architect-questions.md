---
title: "Architect Questions"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Architect-focused subset from the Redis Top 150 question bank."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Architect Q"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.2"
weight: 802
interviewHandbook: true
---

Architect-focused subset from the [Top 150](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/). **Full answers** for each question below.

# Architect Questions

<!-- interview-guide-answers:start -->

### Q2. How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache?

### Short Answer
The senior-level decision is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by running game-day failover tests with connection pool refresh metrics for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache?

---
### Q3. What architectural role does Redis play when it is cache versus when it is the primary data store?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Follow-up Questions
What requirement in: What architectural role does Redis play when it is cache versus when it is the primary data store is decisive if throughput numbers are similar across options?

---
### Q5. When would you shard with Redis Cluster instead of vertical scaling a single primary?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When would you shard with Redis Cluster instead of vertical scaling a single primary appears in production metrics?

---
### Q9. When is Sentinel the right HA layer versus managed cloud failover you do not operate?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Follow-up Questions
What requirement in: When is Sentinel the right HA layer versus managed cloud failover you do not operate is decisive if throughput numbers are similar across options?

---
### Q12. When are Redis Streams architecturally appropriate versus an external log like Kafka?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Follow-up Questions
What requirement in: When are Redis Streams architecturally appropriate versus an external log like Kafka is decisive if throughput numbers are similar across options?

---
### Q13. When are Redis lists or Streams appropriate versus RabbitMQ for task distribution?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Follow-up Questions
What requirement in: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution is decisive if throughput numbers are similar across options?

---
### Q15. What tradeoffs does Redis offer versus Memcached for a pure session cache layer?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Follow-up Questions
What requirement in: What tradeoffs does Redis offer versus Memcached for a pure session cache layer is decisive if throughput numbers are similar across options?

---
### Q16. How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions appears in production metrics?

---
### Q19. What signals indicate a workload has outgrown a single primary before ops teams admit it?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Follow-up Questions
Which type would you choose for: What signals indicate a workload has outgrown a single primary before ops teams admit it, and what command path proves it under peak cardinality?

---
### Q22. How do persistence settings change the architecture story when Redis is marketed as a cache only?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: How do persistence settings change the architecture story when Redis is marketed as a cache only after a hard kill test?

---
### Q23. What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Follow-up Questions
What requirement in: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes is decisive if throughput numbers are similar across options?

---
### Q25. When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk appears in production metrics?

---
### Q26. How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication, and what cluster slot constraints apply?

---
### Q32. How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability?

### Short Answer
For this question, the architecturally correct Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by correlating `master_repl_offset` with replica offsets and write spikes for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Follow-up Questions
Which writes in: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q33. When does TLS termination at proxy versus Redis native TLS change trust boundaries?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Follow-up Questions
What requirement in: When does TLS termination at proxy versus Redis native TLS change trust boundaries is decisive if throughput numbers are similar across options?

---
### Q35. What architectural constraints does Redis impose on exactly-once processing semantics?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Follow-up Questions
Which type would you choose for: What architectural constraints does Redis impose on exactly-once processing semantics, and what command path proves it under peak cardinality?

---
### Q36. How would you map cache patterns (aside, through, behind) to team ownership boundaries?

### Short Answer
For this question, the architecturally correct Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by validating command complexity and memory per key for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Follow-up Questions
Which type would you choose for: How would you map cache patterns (aside, through, behind) to team ownership boundaries, and what command path proves it under peak cardinality?

---
### Q38. How do Redis ACLs change multi-tenant architecture compared to shared-password eras?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras, and what cluster slot constraints apply?

---
### Q39. What cross-datacenter replication options would you compare before choosing Redis Cluster only?

### Short Answer
The practical Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by correlating `master_repl_offset` with replica offsets and write spikes for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Follow-up Questions
Which writes in: What cross-datacenter replication options would you compare before choosing Redis Cluster only require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q40. How would you defend Redis versus a cloud vendor cache in an enterprise architecture review?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Follow-up Questions
What requirement in: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review is decisive if throughput numbers are similar across options?

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
### Q98. When would you disable persistence entirely, and what failure modes remain acceptable?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: When would you disable persistence entirely, and what failure modes remain acceptable after a hard kill test?

---
### Q99. How does min-replicas-to-write protect against write loss during partition events?

### Short Answer
The practical Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How does min-replicas-to-write protect against write loss during partition events.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How does min-replicas-to-write protect against write loss during partition events.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How does min-replicas-to-write protect against write loss during partition events.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by correlating `master_repl_offset` with replica offsets and write spikes for: How does min-replicas-to-write protect against write loss during partition events.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How does min-replicas-to-write protect against write loss during partition events.

### Follow-up Questions
Which writes in: How does min-replicas-to-write protect against write loss during partition events require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q101. How would you design failover testing for Sentinel without corrupting production data?

### Short Answer
The production-grade Redis answer is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How would you design failover testing for Sentinel without corrupting production data.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How would you design failover testing for Sentinel without corrupting production data.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How would you design failover testing for Sentinel without corrupting production data.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by running game-day failover tests with connection pool refresh metrics for: How would you design failover testing for Sentinel without corrupting production data.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How would you design failover testing for Sentinel without corrupting production data.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How would you design failover testing for Sentinel without corrupting production data?

---
### Q102. What split-brain scenarios can occur with misconfigured Sentinel quorum?

### Short Answer
The senior-level decision is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by running game-day failover tests with connection pool refresh metrics for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: What split-brain scenarios can occur with misconfigured Sentinel quorum?

---
### Q107. How do fencing tokens prevent stale lock holders from corrupting durable storage?

### Short Answer
The practical Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing GC pause and clock skew scenarios against lock TTL for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do fencing tokens prevent stale lock holders from corrupting durable storage outlives the Redis lock TTL?

---
### Q108. What correctness gaps remain with SET key token NX PX even when unlock uses Lua?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: What correctness gaps remain with SET key token NX PX even when unlock uses Lua outlives the Redis lock TTL?

---
### Q109. How would you argue for or against Redlock in a multi-datacenter inventory system?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you argue for or against Redlock in a multi-datacenter inventory system outlives the Redis lock TTL?

---
### Q110. What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined after a hard kill test?

---
### Q117. When does adding replicas stop helping read scale because the primary is still the bottleneck?

### Short Answer
The production-grade Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by correlating `master_repl_offset` with replica offsets and write spikes for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Follow-up Questions
Which writes in: When does adding replicas stop helping read scale because the primary is still the bottleneck require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q118. How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec?

### Short Answer
The senior-level decision is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by correlating `master_repl_offset` with replica offsets and write spikes for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Follow-up Questions
Which writes in: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q121. When does horizontal Cluster scaling hit coordination overhead diminishing returns?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does horizontal Cluster scaling hit coordination overhead diminishing returns appears in production metrics?

---
### Q123. What growth triggers move you from one large instance to Cluster beyond memory alone?

### Short Answer
The practical Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What growth triggers move you from one large instance to Cluster beyond memory alone appears in production metrics?

---

<!-- interview-guide-answers:end -->

---

## See Also

- [Previous: Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
- [Next: Troubleshooting Questions](/redis-cheatsheet/08-interview-guide/troubleshooting-questions/)
- [Redis Handbook Index](/redis-cheatsheet/)
