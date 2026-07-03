---
title: "Pub/Sub"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Fan-out messaging semantics and delivery caveats."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Pub/Sub"
module: 4
moduleTitle: "Distributed Systems"
sectionRef: "4.3"
weight: 403
ShowToc: true

aliases:
  - "/redis-cheatsheet/pub-sub/"
---

## Executive Summary

**Pub/Sub** is fire-and-forget **fan-out messaging** â€” subscribers only receive messages while connected; **no persistence**, no acks, no replay.

---

## Core Concepts

| Mode | Subscribe |
| :--- | :--- |
| Channel | `SUBSCRIBE news` |
| Pattern | `PSUBSCRIBE news.*` |
| Publish | `PUBLISH news.sports "score"` |

Separate connection recommended â€” subscriber connection blocks in subscribe mode.

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

For full invalidation flow and consistency tradeoffs, see [Cache Invalidation](/redis-cheatsheet/05-production-patterns/cache-invalidation/).

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Message loss if no subscriber | Use **Streams** or external broker |
| Slow subscriber | Disconnect â€” no backlog |
| `SUBSCRIBE` on shared pool connection | Dedicated pub/sub connections |

---

## How does Pub/Sub fit into cache invalidation architecture without becoming a system of record?

### Short Answer
The senior-level decision is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by defining who invalidates on partial updates and out-of-order writes for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record updates one entity?

---
## How would you investigate Pub/Sub subscribers missing invalidation messages intermittently?

### Short Answer
The production-grade Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by defining who invalidates on partial updates and out-of-order writes for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently updates one entity?

---
## What happens to in-flight Pub/Sub messages during primary failover?

### Short Answer
For this question, the architecturally correct Redis answer is using Pub/Sub only for ephemeral fan-out where message loss during disconnect is acceptable for: What happens to in-flight Pub/Sub messages during primary failover.

### Detailed Explanation
Pub/Sub delivers only to connected subscribers — no persistence, backlog, or acks — unlike Streams or external brokers for: What happens to in-flight Pub/Sub messages during primary failover.

### Internal Working
Slow subscribers are disconnected; dedicated connections are required because SUBSCRIBE blocks the connection for: What happens to in-flight Pub/Sub messages during primary failover.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by pairing invalidation signals with cache TTL and source-of-truth refresh for: What happens to in-flight Pub/Sub messages during primary failover.

### Common Mistakes
Using Pub/Sub as a job queue or on shared pool connections causes lost work and stuck clients for: What happens to in-flight Pub/Sub messages during primary failover.

### Follow-up Questions
What happens to in-flight Pub/Sub messages during failover in: What happens to in-flight Pub/Sub messages during primary failover, and is that acceptable?

---
## When does Redis Pub/Sub suffice for feature-flag propagation versus polling?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Follow-up Questions
What requirement in: When does Redis Pub/Sub suffice for feature-flag propagation versus polling is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## How does Pub/Sub fit into cache invalidation architecture without becoming a system of record?

### Short Answer
The senior-level decision is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by defining who invalidates on partial updates and out-of-order writes for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record updates one entity?

---
## How would you investigate Pub/Sub subscribers missing invalidation messages intermittently?

### Short Answer
The production-grade Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by defining who invalidates on partial updates and out-of-order writes for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently updates one entity?

---
## What happens to in-flight Pub/Sub messages during primary failover?

### Short Answer
For this question, the architecturally correct Redis answer is using Pub/Sub only for ephemeral fan-out where message loss during disconnect is acceptable for: What happens to in-flight Pub/Sub messages during primary failover.

### Detailed Explanation
Pub/Sub delivers only to connected subscribers — no persistence, backlog, or acks — unlike Streams or external brokers for: What happens to in-flight Pub/Sub messages during primary failover.

### Internal Working
Slow subscribers are disconnected; dedicated connections are required because SUBSCRIBE blocks the connection for: What happens to in-flight Pub/Sub messages during primary failover.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by pairing invalidation signals with cache TTL and source-of-truth refresh for: What happens to in-flight Pub/Sub messages during primary failover.

### Common Mistakes
Using Pub/Sub as a job queue or on shared pool connections causes lost work and stuck clients for: What happens to in-flight Pub/Sub messages during primary failover.

### Follow-up Questions
What happens to in-flight Pub/Sub messages during failover in: What happens to in-flight Pub/Sub messages during primary failover, and is that acceptable?

---
## When does Redis Pub/Sub suffice for feature-flag propagation versus polling?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Follow-up Questions
What requirement in: When does Redis Pub/Sub suffice for feature-flag propagation versus polling is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## How does Pub/Sub fit into cache invalidation architecture without becoming a system of record?

### Short Answer
The senior-level decision is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by defining who invalidates on partial updates and out-of-order writes for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record updates one entity?

---
## How would you investigate Pub/Sub subscribers missing invalidation messages intermittently?

### Short Answer
The production-grade Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by defining who invalidates on partial updates and out-of-order writes for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently updates one entity?

---
## What happens to in-flight Pub/Sub messages during primary failover?

### Short Answer
For this question, the architecturally correct Redis answer is using Pub/Sub only for ephemeral fan-out where message loss during disconnect is acceptable for: What happens to in-flight Pub/Sub messages during primary failover.

### Detailed Explanation
Pub/Sub delivers only to connected subscribers — no persistence, backlog, or acks — unlike Streams or external brokers for: What happens to in-flight Pub/Sub messages during primary failover.

### Internal Working
Slow subscribers are disconnected; dedicated connections are required because SUBSCRIBE blocks the connection for: What happens to in-flight Pub/Sub messages during primary failover.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by pairing invalidation signals with cache TTL and source-of-truth refresh for: What happens to in-flight Pub/Sub messages during primary failover.

### Common Mistakes
Using Pub/Sub as a job queue or on shared pool connections causes lost work and stuck clients for: What happens to in-flight Pub/Sub messages during primary failover.

### Follow-up Questions
What happens to in-flight Pub/Sub messages during failover in: What happens to in-flight Pub/Sub messages during primary failover, and is that acceptable?

---
## When does Redis Pub/Sub suffice for feature-flag propagation versus polling?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Follow-up Questions
What requirement in: When does Redis Pub/Sub suffice for feature-flag propagation versus polling is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## How does Pub/Sub fit into cache invalidation architecture without becoming a system of record?

### Short Answer
The senior-level decision is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by defining who invalidates on partial updates and out-of-order writes for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record updates one entity?

---
## How would you investigate Pub/Sub subscribers missing invalidation messages intermittently?

### Short Answer
The production-grade Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by defining who invalidates on partial updates and out-of-order writes for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently updates one entity?

---
## What happens to in-flight Pub/Sub messages during primary failover?

### Short Answer
For this question, the architecturally correct Redis answer is using Pub/Sub only for ephemeral fan-out where message loss during disconnect is acceptable for: What happens to in-flight Pub/Sub messages during primary failover.

### Detailed Explanation
Pub/Sub delivers only to connected subscribers — no persistence, backlog, or acks — unlike Streams or external brokers for: What happens to in-flight Pub/Sub messages during primary failover.

### Internal Working
Slow subscribers are disconnected; dedicated connections are required because SUBSCRIBE blocks the connection for: What happens to in-flight Pub/Sub messages during primary failover.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by pairing invalidation signals with cache TTL and source-of-truth refresh for: What happens to in-flight Pub/Sub messages during primary failover.

### Common Mistakes
Using Pub/Sub as a job queue or on shared pool connections causes lost work and stuck clients for: What happens to in-flight Pub/Sub messages during primary failover.

### Follow-up Questions
What happens to in-flight Pub/Sub messages during failover in: What happens to in-flight Pub/Sub messages during primary failover, and is that acceptable?

---
## When does Redis Pub/Sub suffice for feature-flag propagation versus polling?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Follow-up Questions
What requirement in: When does Redis Pub/Sub suffice for feature-flag propagation versus polling is decisive if throughput numbers are similar across options?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Transactions](/redis-cheatsheet/04-distributed-systems/transactions/)
- [Next: Streams](/redis-cheatsheet/04-distributed-systems/streams/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
