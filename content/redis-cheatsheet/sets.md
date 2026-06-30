---
title: "Redis Sets"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "SADD/SMEMBERS, set algebra, and membership at O(1)."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Sets"
module: 2
moduleTitle: "Core Data Types"
sectionRef: "2.4"
ShowToc: true
---

## Executive Summary

**Sets** are unordered unique strings — **O(1)** add/remove/membership; **set algebra** (`SINTER`, `SUNION`, `SDIFF`) powers tagging and relationship queries.

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
| `SINTER` on huge sets | Can block event loop — consider pre-compute or sharding |

---

## Related Topics

- [Previous: Lists](/redis-cheatsheet/lists/)
- [Next: Sorted Sets](/redis-cheatsheet/sorted-sets/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
