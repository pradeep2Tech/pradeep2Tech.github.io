---
title: "Redis HyperLogLog"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "PFADD/PFCOUNT — approximate distinct counts in fixed memory."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "HyperLogLog"
module: 3
moduleTitle: "Specialized Structures"
sectionRef: "3.2"
ShowToc: true
---

## Executive Summary

**HyperLogLog** estimates **cardinality** (~0.81% error) using **~12 KB** per key regardless of billions of elements — not for membership tests.

---

## Core Concepts

| Property | Value |
| :--- | :--- |
| **Commands** | `PFADD`, `PFCOUNT`, `PFMERGE` |
| **Memory** | ~12 KB per key |
| **Exact?** | No — approximate distinct count |
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
| Test membership | HLL cannot — use Set or Bloom (module) |
| Small cardinalities | Error dominates — Set may be fine under ~10k |

---

## Related Topics

- [Previous: Bitmaps](/redis-cheatsheet/bitmaps/)
- [Next: Streams](/redis-cheatsheet/streams/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
