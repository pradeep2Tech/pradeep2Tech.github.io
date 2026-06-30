---
title: "Redis Hashes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Field-value maps, HSET/HGET, and compact encoding for small objects."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Hashes"
module: 2
moduleTitle: "Core Data Types"
sectionRef: "2.2"
ShowToc: true
---

## Executive Summary

**Hashes** store field → value maps — ideal for **objects** (user, session, product attributes) with O(1) single-field access.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `HSET` / `HGET` | Set/get one field |
| `HMSET` / `HMGET` | Multi field (HMSET deprecated — use `HSET` multi) |
| `HGETALL` | All fields — careful on large hashes |
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

## Related Topics

- [Previous: Strings](/redis-cheatsheet/strings/)
- [Next: Lists](/redis-cheatsheet/lists/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
