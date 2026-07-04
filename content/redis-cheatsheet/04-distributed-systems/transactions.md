---
title: "Transactions"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "MULTI/EXEC and optimistic coordination semantics."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Transactions"
module: 4
moduleTitle: "Distributed Systems"
sectionRef: "4.2"
weight: 402

aliases:
  - "/redis-cheatsheet/transactions/"
---

## Executive Summary

**MULTI/EXEC** batches commands atomically â€” all queued commands run in sequence without interleaving. **Not** rollback on failure mid-batch. **WATCH** enables optimistic locking.

---

## Core Concepts

| Feature | Behavior |
| :--- | :--- |
| `MULTI` | Start queue |
| `EXEC` | Run all or nothing if `WATCH` keys changed |
| `DISCARD` | Abort queue |
| `WATCH key` | Abort `EXEC` if key modified since `WATCH` |
| **Pipeline** | Batch without atomicity â€” faster for bulk |

Errors: compile-time (bad command in `MULTI`) vs exec-time (e.g. `INCR` on string).

---

## Quick Reference

```bash
WATCH balance:42
GET balance:42
MULTI
DECRBY balance:42 10
INCRBY balance:99 10
EXEC
# EXEC returns nil if WATCH key changed
```

---

## Snippets

### Transfer with WATCH

```bash
WATCH account:A account:B
MULTI
DECRBY account:A 50
INCRBY account:B 50
EXEC
```

Prefer **Lua** for complex atomic logic.

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Expecting RDBMS-style rollback | Failed command doesn't undo prior commands in `EXEC` |
| Long `MULTI` block | Blocks other clients â€” keep short |
| `WATCH` on hot keys | High abort rate â€” use Lua or Redisson |

---

## What architecture pitfalls appear when using Redis transactions across many hot keys?

### Short Answer
The practical Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by load-testing synchronized expiry and hot-key miss scenarios for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What architecture pitfalls appear when using Redis transactions across many hot keys in your architecture?

---
## Why does MULTI/EXEC not provide rollback semantics like a relational transaction?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction, and what cluster slot constraints apply?

---
<!-- interview-answers:end -->

---

## What architecture pitfalls appear when using Redis transactions across many hot keys?

### Short Answer
The practical Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by load-testing synchronized expiry and hot-key miss scenarios for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What architecture pitfalls appear when using Redis transactions across many hot keys in your architecture?

---
## Why does MULTI/EXEC not provide rollback semantics like a relational transaction?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction, and what cluster slot constraints apply?

---
<!-- interview-answers:end -->

---

## What architecture pitfalls appear when using Redis transactions across many hot keys?

### Short Answer
The practical Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by load-testing synchronized expiry and hot-key miss scenarios for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What architecture pitfalls appear when using Redis transactions across many hot keys in your architecture?

---
## Why does MULTI/EXEC not provide rollback semantics like a relational transaction?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction, and what cluster slot constraints apply?

---
<!-- interview-answers:end -->

---

## What architecture pitfalls appear when using Redis transactions across many hot keys?

### Short Answer
The practical Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by load-testing synchronized expiry and hot-key miss scenarios for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What architecture pitfalls appear when using Redis transactions across many hot keys in your architecture?

---
## Why does MULTI/EXEC not provide rollback semantics like a relational transaction?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction, and what cluster slot constraints apply?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Distributed Lock](/redis-cheatsheet/04-distributed-systems/distributed-lock/)
- [Next: Pub Sub](/redis-cheatsheet/04-distributed-systems/pub-sub/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
