---
title: "Rate Limiter"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Rate limiting algorithms with Redis data structures."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Rate Limit"
module: 5
moduleTitle: "Production Patterns"
sectionRef: "5.7"
weight: 507

aliases:
  - "/redis-cheatsheet/rate-limiter/"
---

## Executive Summary

Redis counters + TTL implement **fixed window**, **sliding window** (sorted set or INCR with multiple buckets), and **token bucket** â€” atomic via `INCR` or Lua.

---

## Core Concepts

| Algorithm | Sketch |
| :--- | :--- |
| **Fixed window** | `INCR rate:user:42:minute` + `EXPIRE 60` |
| **Sliding window** | `ZADD` timestamp members; trim old |
| **Token bucket** | Hash: tokens + last_refill; Lua refill |
| **Global limit** | Single key or sharded counters |

---

## Quick Reference

```bash
INCR rate:api:user:42:202606301045
EXPIRE rate:api:user:42:202606301045 60
# if count > limit â†’ 429
```

---

## Snippets

### Sliding window (sorted set)

```bash
ZADD rate:user:42 now now
ZREMRANGEBYSCORE rate:user:42 0 now-60000
ZCARD rate:user:42
EXPIRE rate:user:42 61
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Fixed window burst at boundary | 2Ã— traffic at edges â€” use sliding |
| Race without atomicity | `INCR` is atomic; complex logic â†’ Lua |
| Hot key on global limit | Shard counter keys |

---

## When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk appears in production metrics?

---
## How do you debug rate limiter drift when counters look correct per key but limits feel wrong?

### Short Answer
The practical Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing boundary bursts at window edges for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Follow-up Questions
How would you shard a global rate limit key if: How do you debug rate limiter drift when counters look correct per key but limits feel wrong saturates one Redis primary?

---
## How would you optimize a sliding-window rate limiter implemented with sorted sets?

### Short Answer
For this question, the architecturally correct Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing boundary bursts at window edges for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Follow-up Questions
How would you shard a global rate limit key if: How would you optimize a sliding-window rate limiter implemented with sorted sets saturates one Redis primary?

---
## How do global rate limit counters scale when a single INCR key becomes hot?

### Short Answer
The senior-level decision is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do global rate limit counters scale when a single INCR key becomes hot.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do global rate limit counters scale when a single INCR key becomes hot.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do global rate limit counters scale when a single INCR key becomes hot.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing boundary bursts at window edges for: How do global rate limit counters scale when a single INCR key becomes hot.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do global rate limit counters scale when a single INCR key becomes hot.

### Follow-up Questions
How would you shard a global rate limit key if: How do global rate limit counters scale when a single INCR key becomes hot saturates one Redis primary?

---
## How would you choose fixed-window versus sliding-window rate limits for an API gateway?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Follow-up Questions
What requirement in: How would you choose fixed-window versus sliding-window rate limits for an API gateway is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk appears in production metrics?

---
## How do you debug rate limiter drift when counters look correct per key but limits feel wrong?

### Short Answer
The practical Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing boundary bursts at window edges for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Follow-up Questions
How would you shard a global rate limit key if: How do you debug rate limiter drift when counters look correct per key but limits feel wrong saturates one Redis primary?

---
## How would you optimize a sliding-window rate limiter implemented with sorted sets?

### Short Answer
For this question, the architecturally correct Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing boundary bursts at window edges for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Follow-up Questions
How would you shard a global rate limit key if: How would you optimize a sliding-window rate limiter implemented with sorted sets saturates one Redis primary?

---
## How do global rate limit counters scale when a single INCR key becomes hot?

### Short Answer
The senior-level decision is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do global rate limit counters scale when a single INCR key becomes hot.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do global rate limit counters scale when a single INCR key becomes hot.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do global rate limit counters scale when a single INCR key becomes hot.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing boundary bursts at window edges for: How do global rate limit counters scale when a single INCR key becomes hot.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do global rate limit counters scale when a single INCR key becomes hot.

### Follow-up Questions
How would you shard a global rate limit key if: How do global rate limit counters scale when a single INCR key becomes hot saturates one Redis primary?

---
## How would you choose fixed-window versus sliding-window rate limits for an API gateway?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Follow-up Questions
What requirement in: How would you choose fixed-window versus sliding-window rate limits for an API gateway is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk appears in production metrics?

---
## How do you debug rate limiter drift when counters look correct per key but limits feel wrong?

### Short Answer
The practical Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing boundary bursts at window edges for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Follow-up Questions
How would you shard a global rate limit key if: How do you debug rate limiter drift when counters look correct per key but limits feel wrong saturates one Redis primary?

---
## How would you optimize a sliding-window rate limiter implemented with sorted sets?

### Short Answer
For this question, the architecturally correct Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing boundary bursts at window edges for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Follow-up Questions
How would you shard a global rate limit key if: How would you optimize a sliding-window rate limiter implemented with sorted sets saturates one Redis primary?

---
## How do global rate limit counters scale when a single INCR key becomes hot?

### Short Answer
The senior-level decision is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do global rate limit counters scale when a single INCR key becomes hot.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do global rate limit counters scale when a single INCR key becomes hot.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do global rate limit counters scale when a single INCR key becomes hot.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing boundary bursts at window edges for: How do global rate limit counters scale when a single INCR key becomes hot.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do global rate limit counters scale when a single INCR key becomes hot.

### Follow-up Questions
How would you shard a global rate limit key if: How do global rate limit counters scale when a single INCR key becomes hot saturates one Redis primary?

---
## How would you choose fixed-window versus sliding-window rate limits for an API gateway?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Follow-up Questions
What requirement in: How would you choose fixed-window versus sliding-window rate limits for an API gateway is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk appears in production metrics?

---
## How do you debug rate limiter drift when counters look correct per key but limits feel wrong?

### Short Answer
The practical Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing boundary bursts at window edges for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Follow-up Questions
How would you shard a global rate limit key if: How do you debug rate limiter drift when counters look correct per key but limits feel wrong saturates one Redis primary?

---
## How would you optimize a sliding-window rate limiter implemented with sorted sets?

### Short Answer
For this question, the architecturally correct Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing boundary bursts at window edges for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Follow-up Questions
How would you shard a global rate limit key if: How would you optimize a sliding-window rate limiter implemented with sorted sets saturates one Redis primary?

---
## How do global rate limit counters scale when a single INCR key becomes hot?

### Short Answer
The senior-level decision is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do global rate limit counters scale when a single INCR key becomes hot.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do global rate limit counters scale when a single INCR key becomes hot.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do global rate limit counters scale when a single INCR key becomes hot.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing boundary bursts at window edges for: How do global rate limit counters scale when a single INCR key becomes hot.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do global rate limit counters scale when a single INCR key becomes hot.

### Follow-up Questions
How would you shard a global rate limit key if: How do global rate limit counters scale when a single INCR key becomes hot saturates one Redis primary?

---
## How would you choose fixed-window versus sliding-window rate limits for an API gateway?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Follow-up Questions
What requirement in: How would you choose fixed-window versus sliding-window rate limits for an API gateway is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Session Store](/redis-cheatsheet/05-production-patterns/session-store/)
- [Next: Eviction Policies](/redis-cheatsheet/06-performance-operations/eviction-policies/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
