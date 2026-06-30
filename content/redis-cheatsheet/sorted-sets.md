---
title: "Redis Sorted Sets"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "ZADD/ZRANGE, scores, rank, and leaderboards."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Sorted Sets"
module: 2
moduleTitle: "Core Data Types"
sectionRef: "2.5"
ShowToc: true
---

## Executive Summary

**Sorted sets (ZSET)** combine unique member + **float score** — sorted by score in **O(log N)**. Leaderboards, priority queues, and time-indexed data.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `ZADD` | Add/update score |
| `ZRANGE` / `ZREVRANGE` | Rank by index |
| `ZRANGEBYSCORE` | Score range query |
| `ZRANK` / `ZREVRANK` | Position of member |
| `ZINCRBY` | Atomic score bump |
| `ZPOPMIN` / `ZPOPMAX` | Pop lowest/highest |

Encoding: **listpack** (small) or **skip list + hash table**.

---

## Quick Reference

```bash
ZADD leaderboard 100 player1 200 player2 150 player3
ZREVRANGE leaderboard 0 9 WITHSCORES
ZRANK leaderboard player2
ZINCRBY leaderboard 50 player1
ZRANGEBYSCORE tasks 0 1690000000 LIMIT 0 10
ZREM leaderboard player3
ZCARD leaderboard
ZCOUNT leaderboard 100 200
```

---

## Snippets

### Delayed job queue (score = run-at epoch ms)

```bash
ZADD delayed 1690000000000 job-uuid-1
ZRANGEBYSCORE delayed 0 1690000100000 LIMIT 0 1
ZREM delayed job-uuid-1
```

### Top-N with ties

```bash
ZREVRANGE leaderboard 0 99 WITHSCORES
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Score collisions for time ordering | Use composite score or stream IDs |
| `ZRANGEBYSCORE` on huge range | Add `LIMIT` |
| Updating member name | Remove + add — member string is identity |

---

## Related Topics

- [Previous: Sets](/redis-cheatsheet/sets/)
- [Next: Bitmaps](/redis-cheatsheet/bitmaps/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
