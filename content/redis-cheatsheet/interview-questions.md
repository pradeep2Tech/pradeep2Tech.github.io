---
title: "Redis Interview Questions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "High-signal Redis probes for senior backend and architect interviews."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Interview"
module: 8
moduleTitle: "Reference"
sectionRef: "8.2"
ShowToc: true
---

## Executive Summary

High-signal **Redis interview probes** — architecture, persistence, cluster, caching, and correctness traps.

---

## Core Concepts

| Theme | Sample probe |
| :--- | :--- |
| **Threading** | Why single-threaded? I/O threads? |
| **Durability** | RDB vs AOF trade-offs |
| **Cache** | Cache-aside vs write-through; stampede |
| **HA** | Sentinel vs Cluster |
| **Correctness** | Distributed lock pitfalls |

---

## Quick Reference

Quick drills: explain `SET NX EX`, `WATCH`/`MULTI`, hash slot math, `volatile-lru` vs `allkeys-lru`, replica lag.

---

## Snippets

{{< interview-answer >}}
**Q:** Why is Redis fast?

**A:** In-memory data structures, single-threaded command path (no lock contention), efficient encodings, optional I/O threading, and simple protocol. Bottleneck is usually memory size, network, or single-core CPU — not disk I/O for pure cache workloads.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** Can you lose data with `appendfsync everysec`?

**A:** Yes — up to ~1 second of writes if the process crashes between write and fsync. `always` is safer but slower. Many caches accept `everysec`; financial primary stores may not.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** How does Redis Cluster split keys?

**A:** 16384 hash slots; slot = CRC16(key) mod 16384. Hash tags `{...}` force colocation. Clients track slot → node map and follow MOVED/ASK redirects.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** What's wrong with `SETNX` for locks?

**A:** No TTL → deadlock if client dies. Must use `SET key token NX PX ms`. Unlock must compare token in Lua before DEL. Still doesn't prevent stale work after TTL expiry without fencing tokens.
{{< /interview-answer >}}

---

## Common Gotchas

Practice explaining **exactly-once** (impossible with basic Redis queue), **hot keys**, and **big key** remediation (`UNLINK`, split, read replicas).

---

## Related Topics

- [Previous: Commands](/redis-cheatsheet/common-redis-commands/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
