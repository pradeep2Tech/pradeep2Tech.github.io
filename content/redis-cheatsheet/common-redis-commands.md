---
title: "Common Redis Commands"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Server, key, info, and admin commands you'll run in production."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Commands"
module: 8
moduleTitle: "Reference"
sectionRef: "8.1"
ShowToc: true
---

## Executive Summary

Production **admin**, **key**, and **debug** commands — bookmark this page for on-call.

---

## Core Concepts

| Category | Commands |
| :--- | :--- |
| **Server** | `INFO`, `CONFIG GET/SET`, `SHUTDOWN`, `SLOWLOG` |
| **Keys** | `DEL`, `UNLINK`, `EXISTS`, `SCAN`, `TYPE`, `TTL` |
| **Debug** | `LATENCY DOCTOR`, `MEMORY DOCTOR`, `OBJECT` |
| **Danger** | `FLUSHALL`, `KEYS`, `DEBUG SEGFAULT` |

---

## Quick Reference

```bash
# Health
redis-cli PING
redis-cli INFO server | grep redis_version
redis-cli SLOWLOG GET 10

# Key scan (prod-safe)
redis-cli SCAN 0 MATCH user:* COUNT 100

# Memory
redis-cli MEMORY USAGE mykey
redis-cli MEMORY STATS

# Bulk delete (async free)
redis-cli UNLINK key1 key2

# Client management
redis-cli CLIENT KILL TYPE normal ADDR ...
redis-cli CLIENT PAUSE 5000
```

---

## Snippets

### Safe iteration

```bash
SCAN 0 MATCH cache:* COUNT 500
```

Repeat with returned cursor until 0.

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `KEYS *` | Blocks — `SCAN` |
| `FLUSHALL` without `ASYNC` | Blocks on large datasets |
| `CONFIG SET` without persist | Lost on restart — update `redis.conf` |

---

## Related Topics

- [Previous: Session Store](/redis-cheatsheet/session-store/)
- [Next: Interview](/redis-cheatsheet/interview-questions/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
