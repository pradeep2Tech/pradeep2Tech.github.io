---
title: "Redis Bitmaps"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "SETBIT/GETBIT, BITOP, and bitfield commands for compact flags."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Bitmaps"
module: 3
moduleTitle: "Specialized Structures"
sectionRef: "3.1"
ShowToc: true
---

## Executive Summary

**Bitmaps** treat a string value as a bit array — **SETBIT/GETBIT** for flags, **BITOP** for AND/OR/XOR, extremely compact for boolean analytics.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `SETBIT key offset 1` | Set bit |
| `GETBIT key offset` | Read bit |
| `BITCOUNT key` | Count set bits |
| `BITOP AND dest k1 k2` | Bitwise ops |
| `BITFIELD` | Get/set/int increment on bit fields |

Classic use: **DAU** — `SETBIT visits:2026-06-30 userId 1`.

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
| Sparse high offsets | Memory grows to max offset — consider Hash or HLL |
| User IDs not dense integers | Map to dense index or use Set/HLL |
| `BITOP` on large keys | CPU spike on single thread |

---

## Related Topics

- [Previous: Sorted Sets](/redis-cheatsheet/sorted-sets/)
- [Next: HyperLogLog](/redis-cheatsheet/hyperloglog/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
