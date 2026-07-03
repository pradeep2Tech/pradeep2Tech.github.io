---
title: "Sets"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Uniqueness and set algebra operations in Redis."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Sets"
module: 2
moduleTitle: "Core Redis"
sectionRef: "2.4"
weight: 204
ShowToc: true
cheatSheet: true

aliases:
  - "/redis-cheatsheet/sets/"
---

## Executive Summary

**Sets** are unordered unique strings â€” **O(1)** add/remove/membership; **set algebra** (`SINTER`, `SUNION`, `SDIFF`) powers tagging and relationship queries.

---

## Core Concepts

| Operation | Command |
| :--- | :--- |
| Add / remove | `SADD`, `SREM` |
| Membership | `SISMEMBER` |
| All members | `SMEMBERS` (small sets) |
| Iterate | `SSCAN` |
| Intersection | `SINTER key1 key2` |
| Union | `SUNION` |
| Difference | `SDIFF` |

---

## Quick Reference

```bash
SADD tags:article:1 redis cache nosql
SISMEMBER tags:article:1 redis
SMEMBERS tags:article:1
SCARD tags:article:1
SINTER tags:article:1 tags:article:2
SUNION user:1:likes user:2:likes
SDIFF user:1:likes user:2:likes
SREM tags:article:1 nosql
```

---

## Snippets

### Mutual followers (intersection)

```bash
SINTER user:1:followers user:2:followers
```

### Unique visitors (HyperLogLog often better at scale)

```bash
SADD visitors:2026-06-30 user-42
SCARD visitors:2026-06-30
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `SMEMBERS` on large sets | `SSCAN` |
| Storing high-cardinality unique IDs in sets | Use **HyperLogLog** or **Bitmap** if approximate OK |
| `SINTER` on huge sets | Can block event loop â€” consider pre-compute or sharding |

---

---

---

---

---

## See Also

- [Previous: Lists](/redis-cheatsheet/02-core-redis/lists/)
- [Next: Sorted Sets](/redis-cheatsheet/02-core-redis/sorted-sets/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
