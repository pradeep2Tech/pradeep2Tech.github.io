---
title: "Strings"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "String operations, counters, and value encoding basics."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Strings"
module: 2
moduleTitle: "Core Redis"
sectionRef: "2.1"
weight: 201
ShowToc: true
cheatSheet: true

aliases:
  - "/redis-cheatsheet/strings/"
---

## Executive Summary

**Strings** are Redis's simplest type â€” binary-safe blobs up to **512 MB**. Used for caching, counters, distributed flags, and as the underlying type for **bitmaps**.

---

## Core Concepts

| Feature | Detail |
| :--- | :--- |
| **Binary safe** | Any byte sequence |
| **Atomic counters** | `INCR`, `INCRBY`, `DECR` |
| **Conditional set** | `SET key val NX EX 30` â€” lock + TTL |
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

Use the canonical cache-aside flow in [Caching Patterns](/redis-cheatsheet/05-production-patterns/caching-patterns/).bash
GET product:99
# miss â†’ load DB â†’ SET product:99 "{json}" EX 600
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
| `GET` + `SET` for counters under race | Use `INCR` â€” atomic |
| `SETNX` without TTL | Dead lock if client dies â€” always `SET NX EX` |

---

## How do large values in strings affect network and latency more than CPU on the server?

### Short Answer
The senior-level decision is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How do large values in strings affect network and latency more than CPU on the server.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How do large values in strings affect network and latency more than CPU on the server.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How do large values in strings affect network and latency more than CPU on the server.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts using slowlog, latency doctor, and before/after benchmarks for: How do large values in strings affect network and latency more than CPU on the server.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How do large values in strings affect network and latency more than CPU on the server.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How do large values in strings affect network and latency more than CPU on the server?

---
<!-- interview-answers:end -->

---

## How do large values in strings affect network and latency more than CPU on the server?

### Short Answer
The senior-level decision is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How do large values in strings affect network and latency more than CPU on the server.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How do large values in strings affect network and latency more than CPU on the server.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How do large values in strings affect network and latency more than CPU on the server.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts using slowlog, latency doctor, and before/after benchmarks for: How do large values in strings affect network and latency more than CPU on the server.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How do large values in strings affect network and latency more than CPU on the server.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How do large values in strings affect network and latency more than CPU on the server?

---
<!-- interview-answers:end -->

---

## How do large values in strings affect network and latency more than CPU on the server?

### Short Answer
The senior-level decision is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How do large values in strings affect network and latency more than CPU on the server.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How do large values in strings affect network and latency more than CPU on the server.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How do large values in strings affect network and latency more than CPU on the server.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts using slowlog, latency doctor, and before/after benchmarks for: How do large values in strings affect network and latency more than CPU on the server.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How do large values in strings affect network and latency more than CPU on the server.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How do large values in strings affect network and latency more than CPU on the server?

---
<!-- interview-answers:end -->

---

## How do large values in strings affect network and latency more than CPU on the server?

### Short Answer
The senior-level decision is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How do large values in strings affect network and latency more than CPU on the server.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How do large values in strings affect network and latency more than CPU on the server.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How do large values in strings affect network and latency more than CPU on the server.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts using slowlog, latency doctor, and before/after benchmarks for: How do large values in strings affect network and latency more than CPU on the server.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How do large values in strings affect network and latency more than CPU on the server.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How do large values in strings affect network and latency more than CPU on the server?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Data Structures](/redis-cheatsheet/01-fundamentals/data-structures/)
- [Next: Hashes](/redis-cheatsheet/02-core-redis/hashes/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
