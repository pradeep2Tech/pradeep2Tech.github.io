---
title: "Redis Lua Scripts"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "EVAL/EVALSHA, atomic server-side logic, and script caching."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Lua Scripts"
module: 4
moduleTitle: "Messaging & Atomicity"
sectionRef: "4.3"
ShowToc: true
---

## Executive Summary

**Lua scripts** run **atomically** on the server — no other commands interleave. Use for compare-and-set, rate limits, and lock release checks.

---

## Core Concepts

| API | Purpose |
| :--- | :--- |
| `EVAL script numkeys key [key ...] arg [arg ...]` | Run script |
| `EVALSHA sha` | Run cached bytecode |
| `SCRIPT LOAD` | Preload → SHA |

Scripts should be deterministic. Redis 7+ supports **Functions** (persistent library).

---

## Quick Reference

```bash
EVAL "return redis.call('GET', KEYS[1])" 1 mykey
SCRIPT LOAD "return redis.call('INCR', KEYS[1])"
EVALSHA <sha> 1 counter
```

---

## Snippets

### Safe lock release

```lua
if redis.call('GET', KEYS[1]) == ARGV[1] then
  return redis.call('DEL', KEYS[1])
else
  return 0
end
```

```bash
EVAL "<script>" 1 lock:order:1 token-uuid
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Long Lua scripts | Blocks entire server — keep O(1) |
| Non-deterministic calls banned | No `TIME`, random, or cross-slot keys in Cluster |
| Hard-coded keys in Cluster | All keys in same hash slot or use hash tags `{tag}` |

---

## Related Topics

- [Previous: Transactions](/redis-cheatsheet/transactions/)
- [Next: Persistence](/redis-cheatsheet/persistence/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
