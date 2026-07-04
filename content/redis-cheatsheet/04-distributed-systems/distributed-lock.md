---
title: "Distributed Lock"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Lock correctness, token ownership, and failure boundaries."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Dist Lock"
module: 4
moduleTitle: "Distributed Systems"
sectionRef: "4.1"
weight: 401

aliases:
  - "/redis-cheatsheet/distributed-lock/"
---

## Executive Summary

Minimal lock: **`SET key token NX PX ttl`**. Release only if token matches (Lua). **Redlock** (multi-instance) is debated â€” prefer **fencing tokens** with durable store for correctness.

---

## Core Concepts

| Rule | Why |
| :--- | :--- |
| **Unique token** | Prevent deleting another owner's lock |
| **TTL** | Auto-release if holder dies |
| **Lua unlock** | Compare-and-del atomically |
| **Fencing** | Monotonic token to storage prevents stale writes |

Libraries: Redisson, Lettuce recipes, Spring Integration.

---

## Quick Reference

```bash
SET lock:resource:1 uuid NX PX 30000
# renew with Lua if work runs longer
# release via EVAL compare-and-del
```

---

## Snippets

```lua
-- acquire returns OK or nil
return redis.call('SET', KEYS[1], ARGV[1], 'NX', 'PX', ARGV[2])
```

```lua
-- release
if redis.call('GET', KEYS[1]) == ARGV[1] then return redis.call('DEL', KEYS[1]) else return 0 end
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `SETNX` without TTL | Deadlock |
| `DEL` without token check | Deletes another client's lock |
| Long GC pause > TTL | Lock expires; use fencing + short critical sections |

---

## How do you debug distributed lock double-execution after TTL expiry?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you debug distributed lock double-execution after TTL expiry.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you debug distributed lock double-execution after TTL expiry.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you debug distributed lock double-execution after TTL expiry.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How do you debug distributed lock double-execution after TTL expiry.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you debug distributed lock double-execution after TTL expiry.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you debug distributed lock double-execution after TTL expiry outlives the Redis lock TTL?

---
## How do fencing tokens prevent stale lock holders from corrupting durable storage?

### Short Answer
The practical Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing GC pause and clock skew scenarios against lock TTL for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do fencing tokens prevent stale lock holders from corrupting durable storage outlives the Redis lock TTL?

---
## What correctness gaps remain with SET key token NX PX even when unlock uses Lua?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: What correctness gaps remain with SET key token NX PX even when unlock uses Lua outlives the Redis lock TTL?

---
## How would you argue for or against Redlock in a multi-datacenter inventory system?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you argue for or against Redlock in a multi-datacenter inventory system outlives the Redis lock TTL?

---
## How do you implement a correct distributed lock release with token verification?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you implement a correct distributed lock release with token verification.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you implement a correct distributed lock release with token verification.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you implement a correct distributed lock release with token verification.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: How do you implement a correct distributed lock release with token verification.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you implement a correct distributed lock release with token verification.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you implement a correct distributed lock release with token verification outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## How do you debug distributed lock double-execution after TTL expiry?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you debug distributed lock double-execution after TTL expiry.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you debug distributed lock double-execution after TTL expiry.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you debug distributed lock double-execution after TTL expiry.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How do you debug distributed lock double-execution after TTL expiry.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you debug distributed lock double-execution after TTL expiry.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you debug distributed lock double-execution after TTL expiry outlives the Redis lock TTL?

---
## How do fencing tokens prevent stale lock holders from corrupting durable storage?

### Short Answer
The practical Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing GC pause and clock skew scenarios against lock TTL for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do fencing tokens prevent stale lock holders from corrupting durable storage outlives the Redis lock TTL?

---
## What correctness gaps remain with SET key token NX PX even when unlock uses Lua?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: What correctness gaps remain with SET key token NX PX even when unlock uses Lua outlives the Redis lock TTL?

---
## How would you argue for or against Redlock in a multi-datacenter inventory system?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you argue for or against Redlock in a multi-datacenter inventory system outlives the Redis lock TTL?

---
## How do you implement a correct distributed lock release with token verification?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you implement a correct distributed lock release with token verification.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you implement a correct distributed lock release with token verification.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you implement a correct distributed lock release with token verification.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: How do you implement a correct distributed lock release with token verification.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you implement a correct distributed lock release with token verification.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you implement a correct distributed lock release with token verification outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## How do you debug distributed lock double-execution after TTL expiry?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you debug distributed lock double-execution after TTL expiry.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you debug distributed lock double-execution after TTL expiry.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you debug distributed lock double-execution after TTL expiry.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How do you debug distributed lock double-execution after TTL expiry.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you debug distributed lock double-execution after TTL expiry.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you debug distributed lock double-execution after TTL expiry outlives the Redis lock TTL?

---
## How do fencing tokens prevent stale lock holders from corrupting durable storage?

### Short Answer
The practical Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing GC pause and clock skew scenarios against lock TTL for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do fencing tokens prevent stale lock holders from corrupting durable storage outlives the Redis lock TTL?

---
## What correctness gaps remain with SET key token NX PX even when unlock uses Lua?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: What correctness gaps remain with SET key token NX PX even when unlock uses Lua outlives the Redis lock TTL?

---
## How would you argue for or against Redlock in a multi-datacenter inventory system?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you argue for or against Redlock in a multi-datacenter inventory system outlives the Redis lock TTL?

---
## How do you implement a correct distributed lock release with token verification?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you implement a correct distributed lock release with token verification.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you implement a correct distributed lock release with token verification.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you implement a correct distributed lock release with token verification.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: How do you implement a correct distributed lock release with token verification.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you implement a correct distributed lock release with token verification.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you implement a correct distributed lock release with token verification outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## How do you debug distributed lock double-execution after TTL expiry?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you debug distributed lock double-execution after TTL expiry.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you debug distributed lock double-execution after TTL expiry.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you debug distributed lock double-execution after TTL expiry.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How do you debug distributed lock double-execution after TTL expiry.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you debug distributed lock double-execution after TTL expiry.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you debug distributed lock double-execution after TTL expiry outlives the Redis lock TTL?

---
## How do fencing tokens prevent stale lock holders from corrupting durable storage?

### Short Answer
The practical Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing GC pause and clock skew scenarios against lock TTL for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do fencing tokens prevent stale lock holders from corrupting durable storage outlives the Redis lock TTL?

---
## What correctness gaps remain with SET key token NX PX even when unlock uses Lua?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: What correctness gaps remain with SET key token NX PX even when unlock uses Lua outlives the Redis lock TTL?

---
## How would you argue for or against Redlock in a multi-datacenter inventory system?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you argue for or against Redlock in a multi-datacenter inventory system outlives the Redis lock TTL?

---
## How do you implement a correct distributed lock release with token verification?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you implement a correct distributed lock release with token verification.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you implement a correct distributed lock release with token verification.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you implement a correct distributed lock release with token verification.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: How do you implement a correct distributed lock release with token verification.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you implement a correct distributed lock release with token verification.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you implement a correct distributed lock release with token verification outlives the Redis lock TTL?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Cluster](/redis-cheatsheet/03-redis-internals/cluster/)
- [Next: Transactions](/redis-cheatsheet/04-distributed-systems/transactions/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
