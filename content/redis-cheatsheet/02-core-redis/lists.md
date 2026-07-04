---
title: "Lists"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "List operations for queue and sequence use cases."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Lists"
module: 2
moduleTitle: "Core Redis"
sectionRef: "2.3"
weight: 203
cheatSheet: true

aliases:
  - "/redis-cheatsheet/lists/"
---

## Executive Summary

**Lists** are doubly-linked lists of strings â€” used as **stacks**, **queues**, and **blocking work queues** with `BLPOP`/`BRPOP`.

---

## Core Concepts

| Pattern | Commands |
| :--- | :--- |
| Stack | `LPUSH` + `LPOP` |
| Queue | `LPUSH` + `RPOP` |
| Blocking consumer | `BLPOP queue 0` |
| Trim bounded log | `LPUSH` + `LTRIM` |
| Reliable queue | `RPOPLPUSH` / `BRPOPLPUSH` (deprecated â†’ streams) |

---

## Quick Reference

```bash
LPUSH jobs "task-1" "task-2"
RPOP jobs
BLPOP jobs 30
LLEN jobs
LRANGE jobs 0 -1
LTRIM jobs 0 999
LINDEX jobs 0
LINSERT jobs BEFORE "task-2" "task-1b"
```

---

## Snippets

### Simple job queue

```bash
# producer
LPUSH queue:email '{"to":"a@b.com"}'
# worker (blocking 10s)
BLPOP queue:email 10
```

### Recent-items cap

```bash
LPUSH recent:42 itemId
LTRIM recent:42 0 49
```

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| At-most-once with `RPOP` | Worker crash loses job â€” use **Streams** + consumer group |
| `LRANGE 0 -1` on huge list | O(N) â€” paginate with indexes |
| Multiple consumers on one list | Race on `RPOP` â€” one winner only |

---

## When should lists be retired in favor of Streams for work queues?

### Short Answer
The practical Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: When should lists be retired in favor of Streams for work queues.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: When should lists be retired in favor of Streams for work queues.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: When should lists be retired in favor of Streams for work queues.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring XPENDING depth and trimming with MAXLEN ~ for: When should lists be retired in favor of Streams for work queues.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: When should lists be retired in favor of Streams for work queues.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: When should lists be retired in favor of Streams for work queues?

---
<!-- interview-answers:end -->

---

## When should lists be retired in favor of Streams for work queues?

### Short Answer
The practical Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: When should lists be retired in favor of Streams for work queues.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: When should lists be retired in favor of Streams for work queues.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: When should lists be retired in favor of Streams for work queues.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring XPENDING depth and trimming with MAXLEN ~ for: When should lists be retired in favor of Streams for work queues.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: When should lists be retired in favor of Streams for work queues.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: When should lists be retired in favor of Streams for work queues?

---
<!-- interview-answers:end -->

---

## When should lists be retired in favor of Streams for work queues?

### Short Answer
The practical Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: When should lists be retired in favor of Streams for work queues.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: When should lists be retired in favor of Streams for work queues.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: When should lists be retired in favor of Streams for work queues.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring XPENDING depth and trimming with MAXLEN ~ for: When should lists be retired in favor of Streams for work queues.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: When should lists be retired in favor of Streams for work queues.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: When should lists be retired in favor of Streams for work queues?

---
<!-- interview-answers:end -->

---

## When should lists be retired in favor of Streams for work queues?

### Short Answer
The practical Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: When should lists be retired in favor of Streams for work queues.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: When should lists be retired in favor of Streams for work queues.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: When should lists be retired in favor of Streams for work queues.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring XPENDING depth and trimming with MAXLEN ~ for: When should lists be retired in favor of Streams for work queues.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: When should lists be retired in favor of Streams for work queues.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: When should lists be retired in favor of Streams for work queues?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Hashes](/redis-cheatsheet/02-core-redis/hashes/)
- [Next: Sets](/redis-cheatsheet/02-core-redis/sets/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
