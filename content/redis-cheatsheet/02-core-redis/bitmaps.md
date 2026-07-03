---
title: "Bitmaps"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Bit-level operations for dense boolean tracking."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Bitmaps"
module: 2
moduleTitle: "Core Redis"
sectionRef: "2.6"
weight: 206
ShowToc: true
cheatSheet: true

aliases:
  - "/redis-cheatsheet/bitmaps/"
---

## Executive Summary

**Bitmaps** treat a string value as a bit array â€” **SETBIT/GETBIT** for flags, **BITOP** for AND/OR/XOR, extremely compact for boolean analytics.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `SETBIT key offset 1` | Set bit |
| `GETBIT key offset` | Read bit |
| `BITCOUNT key` | Count set bits |
| `BITOP AND dest k1 k2` | Bitwise ops |
| `BITFIELD` | Get/set/int increment on bit fields |

Classic use: **DAU** â€” `SETBIT visits:2026-06-30 userId 1`.

---

## Quick Reference

```bash
SETBIT visits:2026-06-30 42 1
GETBIT visits:2026-06-30 42
BITCOUNT visits:2026-06-30
BITOP AND active both:2026-06-29 both:2026-06-30
BITFIELD flags GET u8 0
```

---

## Snippets

### Daily active users

```bash
SETBIT dau:2026-06-30 10042 1
BITCOUNT dau:2026-06-30
```

### Feature flags per user segment

```bash
SETBIT features:beta userId 1
GETBIT features:beta userId
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Sparse high offsets | Memory grows to max offset â€” consider Hash or HLL |
| User IDs not dense integers | Map to dense index or use Set/HLL |
| `BITOP` on large keys | CPU spike on single thread |

---

## How do BITOP and BITCOUNT scale poorly on large sparse bitmaps?

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
<!-- interview-answers:end -->

---

## How do BITOP and BITCOUNT scale poorly on large sparse bitmaps?

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
<!-- interview-answers:end -->

---

## How do BITOP and BITCOUNT scale poorly on large sparse bitmaps?

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
<!-- interview-answers:end -->

---

## How do BITOP and BITCOUNT scale poorly on large sparse bitmaps?

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
<!-- interview-answers:end -->

---

## See Also

- [Previous: Sorted Sets](/redis-cheatsheet/02-core-redis/sorted-sets/)
- [Next: Hyperloglog](/redis-cheatsheet/02-core-redis/hyperloglog/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
