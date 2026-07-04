---
title: "Sorted Sets"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Ordered score-based collections for ranks and schedules."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Sorted Sets"
module: 2
moduleTitle: "Core Redis"
sectionRef: "2.5"
weight: 205
cheatSheet: true

aliases:
  - "/redis-cheatsheet/sorted-sets/"
---

## Executive Summary

**Sorted sets (ZSET)** combine unique member + **float score** â€” sorted by score in **O(log N)**. Leaderboards, priority queues, and time-indexed data.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `ZADD` | Add/update score |
| `ZRANGE` / `ZREVRANGE` | Rank by index |
| `ZRANGEBYSCORE` | Score range query |
| `ZRANK` / `ZREVRANK` | Position of member |
| `ZINCRBY` | Atomic score bump |
| `ZPOPMIN` / `ZPOPMAX` | Pop lowest/highest |

Encoding: **listpack** (small) or **skip list + hash table**.

---

## Quick Reference

```bash
ZADD leaderboard 100 player1 200 player2 150 player3
ZREVRANGE leaderboard 0 9 WITHSCORES
ZRANK leaderboard player2
ZINCRBY leaderboard 50 player1
ZRANGEBYSCORE tasks 0 1690000000 LIMIT 0 10
ZREM leaderboard player3
ZCARD leaderboard
ZCOUNT leaderboard 100 200
```

---

## Snippets

### Delayed job queue (score = run-at epoch ms)

```bash
ZADD delayed 1690000000000 job-uuid-1
ZRANGEBYSCORE delayed 0 1690000100000 LIMIT 0 1
ZREM delayed job-uuid-1
```

### Top-N with ties

```bash
ZREVRANGE leaderboard 0 99 WITHSCORES
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Score collisions for time ordering | Use composite score or stream IDs |
| `ZRANGEBYSCORE` on huge range | Add `LIMIT` |
| Updating member name | Remove + add â€” member string is identity |

---

## How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Follow-up Questions
What requirement in: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler is decisive if throughput numbers are similar across options?

---
## What ZSET range query patterns need LIMIT to protect p99 latency?

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
<!-- interview-answers:end -->

---

## How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Follow-up Questions
What requirement in: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler is decisive if throughput numbers are similar across options?

---
## What ZSET range query patterns need LIMIT to protect p99 latency?

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
<!-- interview-answers:end -->

---

## How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Follow-up Questions
What requirement in: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler is decisive if throughput numbers are similar across options?

---
## What ZSET range query patterns need LIMIT to protect p99 latency?

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
<!-- interview-answers:end -->

---

## How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Follow-up Questions
What requirement in: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler is decisive if throughput numbers are similar across options?

---
## What ZSET range query patterns need LIMIT to protect p99 latency?

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
<!-- interview-answers:end -->

---

## See Also

- [Previous: Sets](/redis-cheatsheet/02-core-redis/sets/)
- [Next: Bitmaps](/redis-cheatsheet/02-core-redis/bitmaps/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
