---
title: "Redis Eviction Policies"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "maxmemory, LRU/LFU/TTL policies, and volatile vs allkeys."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Eviction"
module: 6
moduleTitle: "Memory Management"
sectionRef: "6.1"
ShowToc: true
---

## Executive Summary

When **`maxmemory`** is hit, Redis evicts keys per **`maxmemory-policy`** — critical for cache workloads. **noeviction** returns errors instead (good for non-cache primary store).

---

## Core Concepts

| Policy | Evicts |
| :--- | :--- |
| `noeviction` | Nothing — writes fail |
| `allkeys-lru` | Any key — approximate LRU |
| `allkeys-lfu` | Any key — frequency (Redis 4+) |
| `volatile-lru` | Keys with TTL only |
| `volatile-lfu` | TTL keys by frequency |
| `volatile-ttl` | Shortest TTL first |
| `allkeys-random` / `volatile-random` | Random |

**LRU** is sampled (`maxmemory-samples`), not exact global LRU.

---

## Quick Reference

```bash
CONFIG GET maxmemory
CONFIG GET maxmemory-policy
CONFIG SET maxmemory 4gb
CONFIG SET maxmemory-policy allkeys-lfu
INFO memory
```

---

## Snippets

```conf
maxmemory 2gb
maxmemory-policy allkeys-lfu
maxmemory-samples 10
```

Set **TTL on cache keys** when using `volatile-*` policies.

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `volatile-lru` but keys have no TTL | Nothing evicted → OOM |
| Hot key evicted with LRU | Consider `lfu` or app-level TTL jitter |
| No `maxmemory` in container | Set to ~75% of container limit |

---

## Related Topics

- [Previous: Cluster](/redis-cheatsheet/cluster/)
- [Next: Caching Patterns](/redis-cheatsheet/caching-patterns/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
