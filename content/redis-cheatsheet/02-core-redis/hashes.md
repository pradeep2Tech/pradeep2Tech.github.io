---
title: "Hashes"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Field-level object storage and hash operation patterns."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Hashes"
module: 2
moduleTitle: "Core Redis"
sectionRef: "2.2"
weight: 202
cheatSheet: true

aliases:
  - "/redis-cheatsheet/hashes/"
---

## Executive Summary

**Hashes** store field â†’ value maps â€” ideal for **objects** (user, session, product attributes) with O(1) single-field access.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `HSET` / `HGET` | Set/get one field |
| `HMSET` / `HMGET` | Multi field (HMSET deprecated â€” use `HSET` multi) |
| `HGETALL` | All fields â€” careful on large hashes |
| `HINCRBY` | Atomic numeric field increment |
| `HSCAN` | Cursor iteration |

Small hashes use **listpack** encoding; large ones use **hash table**.

---

## Quick Reference

```bash
HSET user:42 name Alice email alice@example.com
HGET user:42 name
HMGET user:42 name email
HGETALL user:42
HINCRBY user:42 loginCount 1
HEXISTS user:42 email
HDEL user:42 tempField
HLEN user:42
HSCAN user:42 0 MATCH name* COUNT 100
```

---

## Snippets

### Session hash

```bash
HSET session:abc userId 42 roles admin,editor
EXPIRE session:abc 1800
```

### Partial update without reading full object

```bash
HSET product:99 price 19.99 stock 42
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `HGETALL` on 10k fields | `HSCAN` or field-specific `HMGET` |
| Nested objects | Flatten fields or use RedisJSON |
| Expecting per-field TTL | Expire whole key or use separate keys |

---

## What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

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
## What are the tradeoffs of caching entire DTOs versus hash field projections?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Follow-up Questions
What requirement in: What are the tradeoffs of caching entire DTOs versus hash field projections is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

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
## What are the tradeoffs of caching entire DTOs versus hash field projections?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Follow-up Questions
What requirement in: What are the tradeoffs of caching entire DTOs versus hash field projections is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

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
## What are the tradeoffs of caching entire DTOs versus hash field projections?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Follow-up Questions
What requirement in: What are the tradeoffs of caching entire DTOs versus hash field projections is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

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
## What are the tradeoffs of caching entire DTOs versus hash field projections?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Follow-up Questions
What requirement in: What are the tradeoffs of caching entire DTOs versus hash field projections is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Strings](/redis-cheatsheet/02-core-redis/strings/)
- [Next: Lists](/redis-cheatsheet/02-core-redis/lists/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
