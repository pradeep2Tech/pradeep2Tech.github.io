---
title: "Redis Transactions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MULTI/EXEC, WATCH, optimistic locking, and pipeline vs transaction."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Transactions"
module: 4
moduleTitle: "Messaging & Atomicity"
sectionRef: "4.2"
ShowToc: true
---

## Executive Summary

**MULTI/EXEC** batches commands atomically — all queued commands run in sequence without interleaving. **Not** rollback on failure mid-batch. **WATCH** enables optimistic locking.

---

## Core Concepts

| Feature | Behavior |
| :--- | :--- |
| `MULTI` | Start queue |
| `EXEC` | Run all or nothing if `WATCH` keys changed |
| `DISCARD` | Abort queue |
| `WATCH key` | Abort `EXEC` if key modified since `WATCH` |
| **Pipeline** | Batch without atomicity — faster for bulk |

Errors: compile-time (bad command in `MULTI`) vs exec-time (e.g. `INCR` on string).

---

## Quick Reference

```bash
WATCH balance:42
GET balance:42
MULTI
DECRBY balance:42 10
INCRBY balance:99 10
EXEC
# EXEC returns nil if WATCH key changed
```

---

## Snippets

### Transfer with WATCH

```bash
WATCH account:A account:B
MULTI
DECRBY account:A 50
INCRBY account:B 50
EXEC
```

Prefer **Lua** for complex atomic logic.

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Expecting RDBMS-style rollback | Failed command doesn't undo prior commands in `EXEC` |
| Long `MULTI` block | Blocks other clients — keep short |
| `WATCH` on hot keys | High abort rate — use Lua or Redisson |

---

## Related Topics

- [Previous: Pub/Sub](/redis-cheatsheet/pub-sub/)
- [Next: Lua Scripts](/redis-cheatsheet/lua-scripts/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
