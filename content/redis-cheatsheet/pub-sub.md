---
title: "Redis Pub/Sub"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "PUBLISH/SUBSCRIBE, pattern channels, and fire-and-forget messaging."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Pub/Sub"
module: 4
moduleTitle: "Messaging & Atomicity"
sectionRef: "4.1"
ShowToc: true
---

## Executive Summary

**Pub/Sub** is fire-and-forget **fan-out messaging** — subscribers only receive messages while connected; **no persistence**, no acks, no replay.

---

## Core Concepts

| Mode | Subscribe |
| :--- | :--- |
| Channel | `SUBSCRIBE news` |
| Pattern | `PSUBSCRIBE news.*` |
| Publish | `PUBLISH news.sports "score"` |

Separate connection recommended — subscriber connection blocks in subscribe mode.

---

## Quick Reference

```bash
# terminal 1
SUBSCRIBE notifications
# terminal 2
PUBLISH notifications "deploy complete"
# pattern
PSUBSCRIBE cache:*
PUBLISH cache:invalidate product:99
PUBSUB CHANNELS
PUBSUB NUMSUB notifications
```

---

## Snippets

### Invalidation broadcast

```bash
PUBLISH cache:invalidate '{"key":"product:99"}'
```

Apps subscribe and evict local/Redis cache keys.

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Message loss if no subscriber | Use **Streams** or external broker |
| Slow subscriber | Disconnect — no backlog |
| `SUBSCRIBE` on shared pool connection | Dedicated pub/sub connections |

---

## Related Topics

- [Previous: Streams](/redis-cheatsheet/streams/)
- [Next: Transactions](/redis-cheatsheet/transactions/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
