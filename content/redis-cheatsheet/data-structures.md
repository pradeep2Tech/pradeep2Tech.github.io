---
title: "Redis Data Structures Overview"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Type encoding, keyspace, TTL, and when to pick each Redis data type."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Data Structures"
module: 1
moduleTitle: "Architecture & Model"
sectionRef: "1.2"
ShowToc: true
---

## Executive Summary

Every Redis key maps to **one typed value**. Pick the type by access pattern — not everything is a JSON string. Types share **TTL on the key**, not per-field TTL (except streams entries have IDs).

---

## Core Concepts

| Type | Use when | Core commands |
| :--- | :--- | :--- |
| **String** | Counters, cache blobs, bitmaps | `GET`, `SET`, `INCR` |
| **Hash** | Object fields (user profile) | `HSET`, `HGET`, `HGETALL` |
| **List** | Queue, timeline tail | `LPUSH`, `RPOP`, `BLPOP` |
| **Set** | Unique tags, intersections | `SADD`, `SINTER` |
| **Sorted set** | Rankings, delayed jobs by score | `ZADD`, `ZRANGEBYSCORE` |
| **Stream** | Log, consumer groups | `XADD`, `XREADGROUP` |
| **HyperLogLog** | Cardinality estimate | `PFADD`, `PFCOUNT` |
| **GEO** | Lat/long (sorted-set backed) | `GEOADD`, `GEORADIUS` |

**Encoding:** Redis picks compact encodings (ziplist, listpack, intset) for small values and upgrades to hash table / skip list as data grows.

---

## Quick Reference

```bash
redis-cli TYPE mykey
redis-cli OBJECT ENCODING mykey
redis-cli TTL mykey
redis-cli PTTL mykey
redis-cli EXPIRE mykey 3600
redis-cli PERSIST mykey
```

---

## Snippets

### Key naming convention

```
app:entity:id:field
session:{userId}
cache:product:{sku}
lock:order:{orderId}
```

### Inspect type

```bash
redis-cli HSET user:42 name Alice age 30
redis-cli TYPE user:42        # hash
redis-cli OBJECT ENCODING user:42
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Storing JSON strings for field updates | Use **Hash** or RedisJSON module |
| `HGETALL` on huge hashes | `HSCAN` or fetch needed fields |
| TTL on hash field | TTL is on **key** — split keys if per-field expiry needed |

---

## Related Topics

- [Previous: Architecture](/redis-cheatsheet/architecture/)
- [Next: Strings](/redis-cheatsheet/strings/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
