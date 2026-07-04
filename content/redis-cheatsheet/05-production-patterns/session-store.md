---
title: "Session Store"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Session modeling, TTL policy, and failover behavior."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Session"
module: 5
moduleTitle: "Production Patterns"
sectionRef: "5.6"
weight: 506

aliases:
  - "/redis-cheatsheet/session-store/"
---

## Executive Summary

Store sessions as **Hash** (`session:id` â†’ fields) or **String** (serialized JSON) with **TTL**. Shared Redis enables **stateless** app servers behind a load balancer.

---

## Core Concepts

| Approach | Pros |
| :--- | :--- |
| **Hash fields** | Partial updates, smaller payloads |
| **JSON string** | Simple serialization |
| **TTL refresh** | `EXPIRE` on each request (sliding session) |
| **Cookie** | Store only session ID â€” not data |

Spring Session Redis uses hash + default namespace.

---

## Quick Reference

```bash
HSET session:abc userId 42 roles admin
EXPIRE session:abc 1800
HGETALL session:abc
DEL session:abc
TTL session:abc
```

---

## Snippets

### Spring Session (conceptual)

```yaml
spring.session.store-type: redis
spring.data.redis.host: localhost
```

Session key pattern: `spring:session:sessions:<id>`

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Large session blobs | Keep minimal data in session |
| No TTL | Memory leak â€” always expire |
| Session fixation | Rotate ID on login |
| GDPR â€” sensitive data in Redis | Encrypt or store reference only |

---

## How would you troubleshoot session loss after a Sentinel failover during peak traffic?

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
## What session durability expectations are realistic when Redis is only a cache?

### Short Answer
The senior-level decision is storing minimal session fields in Redis with TTL refresh and cookie holding only opaque session ID for: What session durability expectations are realistic when Redis is only a cache.

### Detailed Explanation
Hash fields allow partial updates; JSON strings simplify serialization but increase rewrite cost for: What session durability expectations are realistic when Redis is only a cache.

### Internal Working
Session loss on failover is acceptable for cache-only sessions but not if Redis is sole session store without replication discipline for: What session durability expectations are realistic when Redis is only a cache.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by rotating session ID on login and bounding payload size for: What session durability expectations are realistic when Redis is only a cache.

### Common Mistakes
Putting PII in session blobs without encryption or TTL is a common compliance mistake for: What session durability expectations are realistic when Redis is only a cache.

### Follow-up Questions
Which session fields must survive failover for: What session durability expectations are realistic when Redis is only a cache, and how do clients handle invalidation?

---
## What session fields belong in Redis versus only in signed cookies?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What session fields belong in Redis versus only in signed cookies.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What session fields belong in Redis versus only in signed cookies.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What session fields belong in Redis versus only in signed cookies.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: What session fields belong in Redis versus only in signed cookies.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What session fields belong in Redis versus only in signed cookies.

### Follow-up Questions
What requirement in: What session fields belong in Redis versus only in signed cookies is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## How would you troubleshoot session loss after a Sentinel failover during peak traffic?

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
## What session durability expectations are realistic when Redis is only a cache?

### Short Answer
The senior-level decision is storing minimal session fields in Redis with TTL refresh and cookie holding only opaque session ID for: What session durability expectations are realistic when Redis is only a cache.

### Detailed Explanation
Hash fields allow partial updates; JSON strings simplify serialization but increase rewrite cost for: What session durability expectations are realistic when Redis is only a cache.

### Internal Working
Session loss on failover is acceptable for cache-only sessions but not if Redis is sole session store without replication discipline for: What session durability expectations are realistic when Redis is only a cache.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by rotating session ID on login and bounding payload size for: What session durability expectations are realistic when Redis is only a cache.

### Common Mistakes
Putting PII in session blobs without encryption or TTL is a common compliance mistake for: What session durability expectations are realistic when Redis is only a cache.

### Follow-up Questions
Which session fields must survive failover for: What session durability expectations are realistic when Redis is only a cache, and how do clients handle invalidation?

---
## What session fields belong in Redis versus only in signed cookies?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What session fields belong in Redis versus only in signed cookies.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What session fields belong in Redis versus only in signed cookies.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What session fields belong in Redis versus only in signed cookies.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: What session fields belong in Redis versus only in signed cookies.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What session fields belong in Redis versus only in signed cookies.

### Follow-up Questions
What requirement in: What session fields belong in Redis versus only in signed cookies is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## How would you troubleshoot session loss after a Sentinel failover during peak traffic?

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
## What session durability expectations are realistic when Redis is only a cache?

### Short Answer
The senior-level decision is storing minimal session fields in Redis with TTL refresh and cookie holding only opaque session ID for: What session durability expectations are realistic when Redis is only a cache.

### Detailed Explanation
Hash fields allow partial updates; JSON strings simplify serialization but increase rewrite cost for: What session durability expectations are realistic when Redis is only a cache.

### Internal Working
Session loss on failover is acceptable for cache-only sessions but not if Redis is sole session store without replication discipline for: What session durability expectations are realistic when Redis is only a cache.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by rotating session ID on login and bounding payload size for: What session durability expectations are realistic when Redis is only a cache.

### Common Mistakes
Putting PII in session blobs without encryption or TTL is a common compliance mistake for: What session durability expectations are realistic when Redis is only a cache.

### Follow-up Questions
Which session fields must survive failover for: What session durability expectations are realistic when Redis is only a cache, and how do clients handle invalidation?

---
## What session fields belong in Redis versus only in signed cookies?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What session fields belong in Redis versus only in signed cookies.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What session fields belong in Redis versus only in signed cookies.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What session fields belong in Redis versus only in signed cookies.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: What session fields belong in Redis versus only in signed cookies.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What session fields belong in Redis versus only in signed cookies.

### Follow-up Questions
What requirement in: What session fields belong in Redis versus only in signed cookies is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## How would you troubleshoot session loss after a Sentinel failover during peak traffic?

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
## What session durability expectations are realistic when Redis is only a cache?

### Short Answer
The senior-level decision is storing minimal session fields in Redis with TTL refresh and cookie holding only opaque session ID for: What session durability expectations are realistic when Redis is only a cache.

### Detailed Explanation
Hash fields allow partial updates; JSON strings simplify serialization but increase rewrite cost for: What session durability expectations are realistic when Redis is only a cache.

### Internal Working
Session loss on failover is acceptable for cache-only sessions but not if Redis is sole session store without replication discipline for: What session durability expectations are realistic when Redis is only a cache.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by rotating session ID on login and bounding payload size for: What session durability expectations are realistic when Redis is only a cache.

### Common Mistakes
Putting PII in session blobs without encryption or TTL is a common compliance mistake for: What session durability expectations are realistic when Redis is only a cache.

### Follow-up Questions
Which session fields must survive failover for: What session durability expectations are realistic when Redis is only a cache, and how do clients handle invalidation?

---
## What session fields belong in Redis versus only in signed cookies?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What session fields belong in Redis versus only in signed cookies.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What session fields belong in Redis versus only in signed cookies.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What session fields belong in Redis versus only in signed cookies.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: What session fields belong in Redis versus only in signed cookies.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What session fields belong in Redis versus only in signed cookies.

### Follow-up Questions
What requirement in: What session fields belong in Redis versus only in signed cookies is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Cache Penetration](/redis-cheatsheet/05-production-patterns/cache-penetration/)
- [Next: Rate Limiter](/redis-cheatsheet/05-production-patterns/rate-limiter/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
