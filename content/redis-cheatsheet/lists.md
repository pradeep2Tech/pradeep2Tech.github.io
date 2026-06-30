---
title: "Redis Lists"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "LPUSH/RPOP, blocking pops, and list-backed queues."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Lists"
module: 2
moduleTitle: "Core Data Types"
sectionRef: "2.3"
ShowToc: true
---

## Executive Summary

**Lists** are doubly-linked lists of strings — used as **stacks**, **queues**, and **blocking work queues** with `BLPOP`/`BRPOP`.

---

## Core Concepts

| Pattern | Commands |
| :--- | :--- |
| Stack | `LPUSH` + `LPOP` |
| Queue | `LPUSH` + `RPOP` |
| Blocking consumer | `BLPOP queue 0` |
| Trim bounded log | `LPUSH` + `LTRIM` |
| Reliable queue | `RPOPLPUSH` / `BRPOPLPUSH` (deprecated → streams) |

---

## Quick Reference

```bash
LPUSH jobs "task-1" "task-2"
RPOP jobs
BLPOP jobs 30
LLEN jobs
LRANGE jobs 0 -1
LTRIM jobs 0 999
LINDEX jobs 0
LINSERT jobs BEFORE "task-2" "task-1b"
```

---

## Snippets

### Simple job queue

```bash
# producer
LPUSH queue:email '{"to":"a@b.com"}'
# worker (blocking 10s)
BLPOP queue:email 10
```

### Recent-items cap

```bash
LPUSH recent:42 itemId
LTRIM recent:42 0 49
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| At-most-once with `RPOP` | Worker crash loses job — use **Streams** + consumer group |
| `LRANGE 0 -1` on huge list | O(N) — paginate with indexes |
| Multiple consumers on one list | Race on `RPOP` — one winner only |

---

## Related Topics

- [Previous: Hashes](/redis-cheatsheet/hashes/)
- [Next: Sets](/redis-cheatsheet/sets/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
