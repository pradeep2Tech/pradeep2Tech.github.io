---
title: "Data Structures"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Redis type selection and key modeling basics."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Data Struct"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.2"
weight: 102

aliases:
  - "/redis-cheatsheet/data-structures/"
---

## Executive Summary

Every Redis key maps to **one typed value**. Pick the type by access pattern â€” not everything is a JSON string. Types share **TTL on the key**, not per-field TTL (except streams entries have IDs).

---

## Core Concepts

| Type | Use when | Core commands |
| :--- | :--- | :--- |
| **String** | Counters, cache blobs, bitmaps | `GET`, `SET`, `INCR` |
| **Hash** | Object fields (user profile) | `HSET`, `HGET`, `HGETALL` |
| **List** | Queue, timeline tail | `LPUSH`, `RPOP`, `BLPOP` |
| **Set** | Unique tags, intersections | `SADD`, `SINTER` |
| **Sorted set** | Rankings, delayed jobs by score | `ZADD`, `ZRANGEBYSCORE` |
| **Stream** | Log, consumer groups | `XADD`, `XREADGROUP` |
| **HyperLogLog** | Cardinality estimate | `PFADD`, `PFCOUNT` |
| **GEO** | Lat/long (sorted-set backed) | `GEOADD`, `GEORADIUS` |

Encoding internals and upgrade thresholds are covered in [Memory Management](/redis-cheatsheet/03-redis-internals/memory-management/).

---

## Quick Reference

```bash
redis-cli TYPE mykey
redis-cli OBJECT ENCODING mykey
redis-cli TTL mykey
redis-cli PTTL mykey
redis-cli EXPIRE mykey 3600
redis-cli PERSIST mykey
```

---

## Snippets

### Key naming convention

```
app:entity:id:field
session:{userId}
cache:product:{sku}
lock:order:{orderId}
```

### Inspect type

```bash
redis-cli HSET user:42 name Alice age 30
redis-cli TYPE user:42        # hash
redis-cli OBJECT ENCODING user:42
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Storing JSON strings for field updates | Use **Hash** or RedisJSON module |
| `HGETALL` on huge hashes | `HSCAN` or fetch needed fields |
| TTL on hash field | TTL is on **key** â€” split keys if per-field expiry needed |

---

## What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Follow-up Questions
Which type would you choose for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string, and what command path proves it under peak cardinality?

---
## When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Follow-up Questions
What requirement in: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes is decisive if throughput numbers are similar across options?

---
## How does TTL-at-key-level architecture affect session design versus field-level expiry needs?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Follow-up Questions
What requirement in: How does TTL-at-key-level architecture affect session design versus field-level expiry needs is decisive if throughput numbers are similar across options?

---
## How would you design key namespaces for microservices sharing one cluster without coupling?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you design key namespaces for microservices sharing one cluster without coupling.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you design key namespaces for microservices sharing one cluster without coupling appears in production metrics?

---
<!-- interview-answers:end -->

---

## What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Follow-up Questions
Which type would you choose for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string, and what command path proves it under peak cardinality?

---
## When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Follow-up Questions
What requirement in: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes is decisive if throughput numbers are similar across options?

---
## How does TTL-at-key-level architecture affect session design versus field-level expiry needs?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Follow-up Questions
What requirement in: How does TTL-at-key-level architecture affect session design versus field-level expiry needs is decisive if throughput numbers are similar across options?

---
## How would you design key namespaces for microservices sharing one cluster without coupling?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you design key namespaces for microservices sharing one cluster without coupling.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you design key namespaces for microservices sharing one cluster without coupling appears in production metrics?

---
<!-- interview-answers:end -->

---

## What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Follow-up Questions
Which type would you choose for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string, and what command path proves it under peak cardinality?

---
## When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Follow-up Questions
What requirement in: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes is decisive if throughput numbers are similar across options?

---
## How does TTL-at-key-level architecture affect session design versus field-level expiry needs?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Follow-up Questions
What requirement in: How does TTL-at-key-level architecture affect session design versus field-level expiry needs is decisive if throughput numbers are similar across options?

---
## How would you design key namespaces for microservices sharing one cluster without coupling?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you design key namespaces for microservices sharing one cluster without coupling.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you design key namespaces for microservices sharing one cluster without coupling appears in production metrics?

---
<!-- interview-answers:end -->

---

## What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Follow-up Questions
Which type would you choose for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string, and what command path proves it under peak cardinality?

---
## When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Follow-up Questions
What requirement in: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes is decisive if throughput numbers are similar across options?

---
## How does TTL-at-key-level architecture affect session design versus field-level expiry needs?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Follow-up Questions
What requirement in: How does TTL-at-key-level architecture affect session design versus field-level expiry needs is decisive if throughput numbers are similar across options?

---
## How would you design key namespaces for microservices sharing one cluster without coupling?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you design key namespaces for microservices sharing one cluster without coupling.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you design key namespaces for microservices sharing one cluster without coupling appears in production metrics?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Architecture](/redis-cheatsheet/01-fundamentals/architecture/)
- [Next: Strings](/redis-cheatsheet/02-core-redis/strings/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
