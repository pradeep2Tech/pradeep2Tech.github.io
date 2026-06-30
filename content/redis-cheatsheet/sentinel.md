---
title: "Redis Sentinel"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Automatic failover, quorum, and sentinel-managed topology."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Sentinel"
module: 5
moduleTitle: "Durability & High Availability"
sectionRef: "5.3"
ShowToc: true
---

## Executive Summary

**Sentinel** monitors primaries/replicas, performs **automatic failover**, and acts as a **configuration provider** for clients — typically 3+ sentinel processes for quorum.

---

## Core Concepts

| Concept | Detail |
| :--- | :--- |
| **Quorum** | `sentinel monitor mymaster ... 2` — 2 sentinels to agree on failover |
| **SDOWN/ODOWN** | Subjective vs objective down |
| **Failover** | Elect replica → `REPLICAOF NO ONE` → re-point others |
| **Client** | Ask Sentinel for current primary address |

Sentinel runs as separate processes (or K8s sidecars), not inside `redis-server`.

---

## Quick Reference

```bash
redis-cli -p 26379 SENTINEL masters
redis-cli -p 26379 SENTINEL replicas mymaster
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
redis-cli -p 26379 SENTINEL failover mymaster
```

---

## Snippets

```conf
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Even number of sentinels | Use odd count (3, 5) for split-brain |
| Client cache stale primary | Use sentinel-aware driver with refresh |
| Failover during high write load | `min-replicas-to-write` guard |

---

## Related Topics

- [Previous: Replication](/redis-cheatsheet/replication/)
- [Next: Cluster](/redis-cheatsheet/cluster/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
