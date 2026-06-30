---
title: "Redis Cluster"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Hash slots, 16384 partitions, resharding, and cluster-aware clients."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Cluster"
module: 5
moduleTitle: "Durability & High Availability"
sectionRef: "5.4"
ShowToc: true
---

## Executive Summary

**Redis Cluster** shards keys across **16384 hash slots** on multiple primaries — each with replicas. Clients must be **cluster-aware** (`MOVED`/`ASK` redirects).

---

## Core Concepts

| Topic | Detail |
| :--- | :--- |
| **Slot** | `CRC16(key) mod 16384` |
| **Hash tag** | `{user}:profile` and `{user}:orders` → same slot |
| **MOVED** | Permanent redirect — client updates slot map |
| **ASK** | Temporary during resharding |
| **Min nodes** | 3 primaries typical for production |

Multi-key ops require same slot — use hash tags.

---

## Quick Reference

```bash
CLUSTER INFO
CLUSTER NODES
CLUSTER SLOTS
CLUSTER KEYSLOT mykey
redis-cli --cluster create host1:6379 host2:6379 --cluster-replicas 1
redis-cli --cluster reshard host1:6379
redis-cli -c -h host1 -p 6379   # cluster mode
```

---

## Snippets

### Hash tag for multi-key transaction

```bash
MSET {user:42}:name Alice {user:42}:email a@b.com
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `MGET` keys on different slots | Cluster rejects — use hash tags or separate calls |
| Non-cluster client | Gets `MOVED` errors |
| Lua with multiple keys | All keys must share slot |

---

## Related Topics

- [Previous: Sentinel](/redis-cheatsheet/sentinel/)
- [Next: Eviction](/redis-cheatsheet/eviction-policies/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
