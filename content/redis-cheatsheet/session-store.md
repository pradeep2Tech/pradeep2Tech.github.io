---
title: "Redis Session Store"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Hash-based sessions, TTL refresh, and sticky vs shared sessions."
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["Redis Cheatsheet"]
shortTitle: "Session Store"
module: 7
moduleTitle: "Application Patterns"
sectionRef: "7.4"
ShowToc: true
---

## Executive Summary

Store sessions as **Hash** (`session:id` → fields) or **String** (serialized JSON) with **TTL**. Shared Redis enables **stateless** app servers behind a load balancer.

---

## Core Concepts

| Approach | Pros |
| :--- | :--- |
| **Hash fields** | Partial updates, smaller payloads |
| **JSON string** | Simple serialization |
| **TTL refresh** | `EXPIRE` on each request (sliding session) |
| **Cookie** | Store only session ID — not data |

Spring Session Redis uses hash + default namespace.

---

## Quick Reference

```bash
HSET session:abc userId 42 roles admin
EXPIRE session:abc 1800
HGETALL session:abc
DEL session:abc
TTL session:abc
```

---

## Snippets

### Spring Session (conceptual)

```yaml
spring.session.store-type: redis
spring.data.redis.host: localhost
```

Session key pattern: `spring:session:sessions:<id>`

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Large session blobs | Keep minimal data in session |
| No TTL | Memory leak — always expire |
| Session fixation | Rotate ID on login |
| GDPR — sensitive data in Redis | Encrypt or store reference only |

---

## Related Topics

- [Previous: Rate Limiter](/redis-cheatsheet/rate-limiter/)
- [Next: Commands](/redis-cheatsheet/common-redis-commands/)
- [Redis Cheatsheet Index](/redis-cheatsheet/)
- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
- [Database Handbook](/database-handbook/)
