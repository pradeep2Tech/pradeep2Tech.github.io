---
title: "Redis Strings"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "GET/SET, counters, bitmap base, and string encoding internals."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Strings"
module: 2
moduleTitle: "Core Data Types"
sectionRef: "2.1"
ShowToc: true
---

## Executive Summary

**Strings** are Redis's simplest type — binary-safe blobs up to **512 MB**. Used for caching, counters, distributed flags, and as the underlying type for **bitmaps**.

---

## Core Concepts

| Feature | Detail |
| :--- | :--- |
| **Binary safe** | Any byte sequence |
| **Atomic counters** | `INCR`, `INCRBY`, `DECR` |
| **Conditional set** | `SET key val NX EX 30` — lock + TTL |
| **Batch** | `MGET`, `MSET` |
| **Encoding** | `int` for integers, `embstr`/`raw` for strings |

---

## Quick Reference

```bash
SET cache:item:1 "payload" EX 300
GET cache:item:1
SETNX lock:job 1
INCR page:views
INCRBY wallet:42 100
APPEND log:buf "line\n"
STRLEN cache:item:1
GETRANGE cache:item:1 0 99
SETBIT flags 7 1
GETBIT flags 7
```

---

## Snippets

### Cache-aside read

```bash
GET product:99
# miss → load DB → SET product:99 "{json}" EX 600
```

### Compare-and-set pattern

```bash
SET balance:42 100
# optimistic: WATCH + MULTI or Lua script
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Large values in strings | Split or compress; watch network I/O |
| `GET` + `SET` for counters under race | Use `INCR` — atomic |
| `SETNX` without TTL | Dead lock if client dies — always `SET NX EX` |

---

## Related Topics

- [Previous: Data Structures](/redis-cheatsheet/data-structures/)
- [Next: Hashes](/redis-cheatsheet/hashes/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
