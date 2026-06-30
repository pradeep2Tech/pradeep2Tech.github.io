---
title: "Redis Rate Limiter"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Fixed window, sliding window, and token bucket with INCR/EXPIRE."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Rate Limiter"
module: 7
moduleTitle: "Application Patterns"
sectionRef: "7.3"
ShowToc: true
---

## Executive Summary

Redis counters + TTL implement **fixed window**, **sliding window** (sorted set or INCR with multiple buckets), and **token bucket** — atomic via `INCR` or Lua.

---

## Core Concepts

| Algorithm | Sketch |
| :--- | :--- |
| **Fixed window** | `INCR rate:user:42:minute` + `EXPIRE 60` |
| **Sliding window** | `ZADD` timestamp members; trim old |
| **Token bucket** | Hash: tokens + last_refill; Lua refill |
| **Global limit** | Single key or sharded counters |

---

## Quick Reference

```bash
INCR rate:api:user:42:202606301045
EXPIRE rate:api:user:42:202606301045 60
# if count > limit → 429
```

---

## Snippets

### Sliding window (sorted set)

```bash
ZADD rate:user:42 now now
ZREMRANGEBYSCORE rate:user:42 0 now-60000
ZCARD rate:user:42
EXPIRE rate:user:42 61
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Fixed window burst at boundary | 2× traffic at edges — use sliding |
| Race without atomicity | `INCR` is atomic; complex logic → Lua |
| Hot key on global limit | Shard counter keys |

---

## Related Topics

- [Previous: Distributed Lock](/redis-cheatsheet/distributed-lock/)
- [Next: Session Store](/redis-cheatsheet/session-store/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
