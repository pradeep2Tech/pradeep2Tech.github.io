---
title: "Redis Persistence"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "RDB snapshots, AOF append-only log, and hybrid durability trade-offs."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Persistence"
module: 5
moduleTitle: "Durability & High Availability"
sectionRef: "5.1"
ShowToc: true
---

## Executive Summary

Redis offers **RDB** (point-in-time snapshots) and **AOF** (append-only command log). Production often uses **both**: RDB for fast restarts, AOF for finer durability.

---

## Core Concepts

| Mode | Mechanism | Trade-off |
| :--- | :--- | :--- |
| **RDB** | `SAVE` / `BGSAVE` fork + dump | Compact; may lose data since last snapshot |
| **AOF** | Log every write | `always` / `everysec` / `no` fsync |
| **Hybrid** | RDB preamble in AOF rewrite | Best of both |
| **none** | Pure cache | Fastest; data lost on restart |

`fork` for BGSAVE causes copy-on-write memory spike.

---

## Quick Reference

```bash
SAVE                    # blocking — avoid prod
BGSAVE
LASTSAVE
CONFIG GET save
CONFIG GET appendonly
CONFIG GET appendfsync
BGREWRITEAOF
```

---

## Snippets

```conf
save 900 1
save 300 10
save 60 10000
appendonly yes
appendfsync everysec
no-appendfsync-on-rewrite yes
auto-aof-rewrite-percentage 100
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `appendfsync always` | Durability max; throughput min |
| `everysec` | Up to ~1s loss on crash |
| BGSAVE during memory pressure | Monitor COW — tune `save` rules |

---

## Related Topics

- [Previous: Lua Scripts](/redis-cheatsheet/lua-scripts/)
- [Next: Replication](/redis-cheatsheet/replication/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
