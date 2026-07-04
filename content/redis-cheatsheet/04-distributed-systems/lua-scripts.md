---
title: "Lua Scripts"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Atomic server-side scripts and key-slot safety."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Lua"
module: 4
moduleTitle: "Distributed Systems"
sectionRef: "4.5"
weight: 405

aliases:
  - "/redis-cheatsheet/lua-scripts/"
---

## Executive Summary

**Lua scripts** run **atomically** on the server â€” no other commands interleave. Use for compare-and-set, rate limits, and lock release checks.

---

## Core Concepts

| API | Purpose |
| :--- | :--- |
| `EVAL script numkeys key [key ...] arg [arg ...]` | Run script |
| `EVALSHA sha` | Run cached bytecode |
| `SCRIPT LOAD` | Preload â†’ SHA |

Scripts should be deterministic. Redis 7+ supports **Functions** (persistent library).

---

## Quick Reference

```bash
EVAL "return redis.call('GET', KEYS[1])" 1 mykey
SCRIPT LOAD "return redis.call('INCR', KEYS[1])"
EVALSHA <sha> 1 counter
```

---

## Snippets

### Safe lock release

Use the canonical lock release pattern in [Distributed Lock](/redis-cheatsheet/04-distributed-systems/distributed-lock/).

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| Long Lua scripts | Blocks entire server â€” keep O(1) |
| Non-deterministic calls banned | No `TIME`, random, or cross-slot keys in Cluster |
| Hard-coded keys in Cluster | All keys in same hash slot or use hash tags `{tag}` |

---

## How do Lua scripts affect your architecture for atomic inventory decrements?

### Short Answer
The senior-level decision is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Follow-up Questions
How do you version and deploy script changes safely for: How do Lua scripts affect your architecture for atomic inventory decrements across rolling restarts?

---
## How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster?

### Short Answer
The production-grade Redis answer is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Follow-up Questions
How do you version and deploy script changes safely for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster across rolling restarts?

---
## Why prefer Lua over WATCH/MULTI for contested hot keys?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: Why prefer Lua over WATCH/MULTI for contested hot keys in your architecture?

---
## How would you implement a token bucket refill accurately with Lua?

### Short Answer
The senior-level decision is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you implement a token bucket refill accurately with Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you implement a token bucket refill accurately with Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you implement a token bucket refill accurately with Lua.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing GC pause and clock skew scenarios against lock TTL for: How would you implement a token bucket refill accurately with Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you implement a token bucket refill accurately with Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you implement a token bucket refill accurately with Lua outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## How do Lua scripts affect your architecture for atomic inventory decrements?

### Short Answer
The senior-level decision is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Follow-up Questions
How do you version and deploy script changes safely for: How do Lua scripts affect your architecture for atomic inventory decrements across rolling restarts?

---
## How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster?

### Short Answer
The production-grade Redis answer is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Follow-up Questions
How do you version and deploy script changes safely for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster across rolling restarts?

---
## Why prefer Lua over WATCH/MULTI for contested hot keys?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: Why prefer Lua over WATCH/MULTI for contested hot keys in your architecture?

---
## How would you implement a token bucket refill accurately with Lua?

### Short Answer
The senior-level decision is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you implement a token bucket refill accurately with Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you implement a token bucket refill accurately with Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you implement a token bucket refill accurately with Lua.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing GC pause and clock skew scenarios against lock TTL for: How would you implement a token bucket refill accurately with Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you implement a token bucket refill accurately with Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you implement a token bucket refill accurately with Lua outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## How do Lua scripts affect your architecture for atomic inventory decrements?

### Short Answer
The senior-level decision is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Follow-up Questions
How do you version and deploy script changes safely for: How do Lua scripts affect your architecture for atomic inventory decrements across rolling restarts?

---
## How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster?

### Short Answer
The production-grade Redis answer is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Follow-up Questions
How do you version and deploy script changes safely for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster across rolling restarts?

---
## Why prefer Lua over WATCH/MULTI for contested hot keys?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: Why prefer Lua over WATCH/MULTI for contested hot keys in your architecture?

---
## How would you implement a token bucket refill accurately with Lua?

### Short Answer
The senior-level decision is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you implement a token bucket refill accurately with Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you implement a token bucket refill accurately with Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you implement a token bucket refill accurately with Lua.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing GC pause and clock skew scenarios against lock TTL for: How would you implement a token bucket refill accurately with Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you implement a token bucket refill accurately with Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you implement a token bucket refill accurately with Lua outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## How do Lua scripts affect your architecture for atomic inventory decrements?

### Short Answer
The senior-level decision is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Follow-up Questions
How do you version and deploy script changes safely for: How do Lua scripts affect your architecture for atomic inventory decrements across rolling restarts?

---
## How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster?

### Short Answer
The production-grade Redis answer is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Follow-up Questions
How do you version and deploy script changes safely for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster across rolling restarts?

---
## Why prefer Lua over WATCH/MULTI for contested hot keys?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: Why prefer Lua over WATCH/MULTI for contested hot keys in your architecture?

---
## How would you implement a token bucket refill accurately with Lua?

### Short Answer
The senior-level decision is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you implement a token bucket refill accurately with Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you implement a token bucket refill accurately with Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you implement a token bucket refill accurately with Lua.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing GC pause and clock skew scenarios against lock TTL for: How would you implement a token bucket refill accurately with Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you implement a token bucket refill accurately with Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you implement a token bucket refill accurately with Lua outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Streams](/redis-cheatsheet/04-distributed-systems/streams/)
- [Next: Caching Patterns](/redis-cheatsheet/05-production-patterns/caching-patterns/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
