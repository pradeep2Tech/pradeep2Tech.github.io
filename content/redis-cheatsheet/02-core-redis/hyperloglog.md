---
title: "HyperLogLog"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Probabilistic cardinality estimation patterns."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "HyperLogLog"
module: 2
moduleTitle: "Core Redis"
sectionRef: "2.7"
weight: 207
ShowToc: true
cheatSheet: true

aliases:
  - "/redis-cheatsheet/hyperloglog/"
---

## Executive Summary

**HyperLogLog** estimates **cardinality** (~0.81% error) using **~12 KB** per key regardless of billions of elements â€” not for membership tests.

---

## Core Concepts

| Property | Value |
| :--- | :--- |
| **Commands** | `PFADD`, `PFCOUNT`, `PFMERGE` |
| **Memory** | ~12 KB per key |
| **Exact?** | No â€” approximate distinct count |
| **Merge** | `PFMERGE` unions sketches |

Use for: UV counts, unique IPs, funnel dedup at scale.

---

## Quick Reference

```bash
PFADD uv:2026-06-30 user-1 user-2 user-1
PFCOUNT uv:2026-06-30
PFMERGE uv:week23 uv:day1 uv:day2 uv:day3
PFCOUNT uv:week23
```

---

## Snippets

### Page unique views

```bash
PFADD page:/home:uv session-abc session-def session-abc
PFCOUNT page:/home:uv
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Need exact count | Use Set (memory cost) or external store |
| Test membership | HLL cannot â€” use Set or Bloom (module) |
| Small cardinalities | Error dominates â€” Set may be fine under ~10k |

---

## When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Follow-up Questions
What requirement in: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Follow-up Questions
What requirement in: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Follow-up Questions
What requirement in: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Follow-up Questions
What requirement in: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Bitmaps](/redis-cheatsheet/02-core-redis/bitmaps/)
- [Next: Memory Management](/redis-cheatsheet/03-redis-internals/memory-management/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
