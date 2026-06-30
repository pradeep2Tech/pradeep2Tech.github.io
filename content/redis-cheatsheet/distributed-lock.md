---
title: "Redis Distributed Lock"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "SET NX PX, Redlock debate, and fencing tokens."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Distributed Lock"
module: 7
moduleTitle: "Application Patterns"
sectionRef: "7.2"
ShowToc: true
---

## Executive Summary

Minimal lock: **`SET key token NX PX ttl`**. Release only if token matches (Lua). **Redlock** (multi-instance) is debated — prefer **fencing tokens** with durable store for correctness.

---

## Core Concepts

| Rule | Why |
| :--- | :--- |
| **Unique token** | Prevent deleting another owner's lock |
| **TTL** | Auto-release if holder dies |
| **Lua unlock** | Compare-and-del atomically |
| **Fencing** | Monotonic token to storage prevents stale writes |

Libraries: Redisson, Lettuce recipes, Spring Integration.

---

## Quick Reference

```bash
SET lock:resource:1 uuid NX PX 30000
# renew with Lua if work runs longer
# release via EVAL compare-and-del
```

---

## Snippets

```lua
-- acquire returns OK or nil
return redis.call('SET', KEYS[1], ARGV[1], 'NX', 'PX', ARGV[2])
```

```lua
-- release
if redis.call('GET', KEYS[1]) == ARGV[1] then return redis.call('DEL', KEYS[1]) else return 0 end
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `SETNX` without TTL | Deadlock |
| `DEL` without token check | Deletes another client's lock |
| Long GC pause > TTL | Lock expires; use fencing + short critical sections |

---

## Related Topics

- [Previous: Caching Patterns](/redis-cheatsheet/caching-patterns/)
- [Next: Rate Limiter](/redis-cheatsheet/rate-limiter/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
