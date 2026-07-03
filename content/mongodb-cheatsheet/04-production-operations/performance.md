---
title: "Performance"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Production performance tuning — pooling, pagination, bulk patterns."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Performance"
module: 4
moduleTitle: "Production Operations"
sectionRef: "4.1"
weight: 401
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/mongodb-cheatsheet/performance/"
---

## Quick Revision

- Tune queries and indexes first; then schema; then hardware and topology.
- Use [Explain Plan](/mongodb-cheatsheet/03-query-performance/explain-plan/) before adding indexes.
- Monitoring and capacity: [Monitoring](/mongodb-cheatsheet/04-production-operations/monitoring/) · [Capacity Planning](/mongodb-cheatsheet/04-production-operations/capacity-planning/).

## Executive Summary

Holistic performance tuning for production MongoDB deployments — connection pooling, bulk patterns, and pagination strategies. Query planner and index design live on dedicated pages.

---

## Core Concepts

| Layer | Lever |
| :--- | :--- |
| **Query** | Indexes, projections, `$match` first in aggregation |
| **Schema** | Embed to avoid joins; avoid unbounded growth |
| **Storage** | WiredTiger cache (default ~50% RAM âˆ’ 1 GB) |
| **Replication** | Offload reads to secondaries with acceptable staleness |
| **Sharding** | Horizontal scale when single replica set saturates |

---

## Quick Reference


For symptom → cause → fix runbooks, see [Troubleshooting](/mongodb-cheatsheet/04-production-operations/troubleshooting/).

---

## Snippets

```javascript
// Pagination â€” avoid large skip; use range on indexed field
db.orders.find({ _id: { $gt: lastId } }).sort({ _id: 1 }).limit(50)

// Projection reduces network and decode cost
db.users.find({ status: "active" }, { email: 1, _id: 0 })

// Bulk unordered inserts
db.events.insertMany(docs, { ordered: false })

// Connection pool (driver) â€” default often 100; tune per app instances
// maxPoolSize in URI or MongoClientSettings
```


---

## Common Gotchas

- `$regex` prefix wildcard (`/^.*foo/`) cannot use index â€” anchor left (`/^foo/`).
- Case-insensitive regex without collation scans the collection.
- `allowDiskUse` in aggregation spills to disk â€” slower but prevents failures.
- Many app instances Ã— large `maxPoolSize` can overwhelm mongod â€” size pools globally.

---

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## How would you diagnose connection storms from misconfigured connection pools?

### Short Answer
The production-grade answer is modeling to dominant read/write paths, then embedding only where growth is bounded for: How would you diagnose connection storms from misconfigured connection pools.

### Detailed Explanation
Schema-first decisions in MongoDB should be query-first in practice, so colocate fields that are read together and externalize unbounded fan-out to references or buckets for: How would you diagnose connection storms from misconfigured connection pools.

### Internal Working
Document growth, index fan-out, and update locality decide the true cost profile internally, which is why embedding works best when mutation scope stays narrow for: How would you diagnose connection storms from misconfigured connection pools.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk by replaying realistic tenant skew, cardinality growth, and migration paths before freezing the model for: How would you diagnose connection storms from misconfigured connection pools.

### Common Mistakes
A common mistake is copying relational normalization or, conversely, embedding unbounded arrays until 16 MB limits and write amplification appear for: How would you diagnose connection storms from misconfigured connection pools.

### Follow-up Questions
What cardinality limit, migration trigger, and fallback model would you define up front to keep: How would you diagnose connection storms from misconfigured connection pools safe over 3 years?

---
## How does large `skip` pagination degrade performance and what pattern replaces it?

### Short Answer
For this question, the architecturally correct answer is modeling to dominant read/write paths, then embedding only where growth is bounded for: How does large `skip` pagination degrade performance and what pattern replaces it.

### Detailed Explanation
Schema-first decisions in MongoDB should be query-first in practice, so colocate fields that are read together and externalize unbounded fan-out to references or buckets for: How does large `skip` pagination degrade performance and what pattern replaces it.

### Internal Working
Document growth, index fan-out, and update locality decide the true cost profile internally, which is why embedding works best when mutation scope stays narrow for: How does large `skip` pagination degrade performance and what pattern replaces it.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality by replaying realistic tenant skew, cardinality growth, and migration paths before freezing the model for: How does large `skip` pagination degrade performance and what pattern replaces it.

### Common Mistakes
A common mistake is copying relational normalization or, conversely, embedding unbounded arrays until 16 MB limits and write amplification appear for: How does large `skip` pagination degrade performance and what pattern replaces it.

### Follow-up Questions
What cardinality limit, migration trigger, and fallback model would you define up front to keep: How does large `skip` pagination degrade performance and what pattern replaces it safe over 3 years?

---
## How do you right-size `maxPoolSize` across 50 application pods?

### Short Answer
The production-grade answer is modeling to dominant read/write paths, then embedding only where growth is bounded for: How do you right-size `maxPoolSize` across 50 application pods.

### Detailed Explanation
Schema-first decisions in MongoDB should be query-first in practice, so colocate fields that are read together and externalize unbounded fan-out to references or buckets for: How do you right-size `maxPoolSize` across 50 application pods.

### Internal Working
Document growth, index fan-out, and update locality decide the true cost profile internally, which is why embedding works best when mutation scope stays narrow for: How do you right-size `maxPoolSize` across 50 application pods.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk by replaying realistic tenant skew, cardinality growth, and migration paths before freezing the model for: How do you right-size `maxPoolSize` across 50 application pods.

### Common Mistakes
A common mistake is copying relational normalization or, conversely, embedding unbounded arrays until 16 MB limits and write amplification appear for: How do you right-size `maxPoolSize` across 50 application pods.

### Follow-up Questions
What cardinality limit, migration trigger, and fallback model would you define up front to keep: How do you right-size `maxPoolSize` across 50 application pods safe over 3 years?

---
## What bulk write patterns maximize insert throughput on sharded collections?

### Short Answer
The senior-level decision is choosing a shard key that preserves query targeting and distributes writes, not just one that looks high-cardinality, for: What bulk write patterns maximize insert throughput on sharded collections.

### Detailed Explanation
In MongoDB sharding, the wrong leading key creates hot chunks, scatter-gather queries, or jumbo chunks, so key choice must follow real filters and time-skew behavior for: What bulk write patterns maximize insert throughput on sharded collections.

### Internal Working
`mongos` routes via config metadata and chunk ranges, so shard-key entropy and monotonicity directly control migration pressure and balancer load for: What bulk write patterns maximize insert throughput on sharded collections.

### Production Notes
You justify it by balancing latency, durability, and operational toil by load-testing chunk distribution, migration rate, and per-shard opcounters before production for: What bulk write patterns maximize insert throughput on sharded collections.

### Common Mistakes
Teams often choose hashed keys that break range locality or ranged keys that hotspot writes because they skipped workload replay for: What bulk write patterns maximize insert throughput on sharded collections.

### Follow-up Questions
How would you prove shard targeting percentage, not just throughput, for: What bulk write patterns maximize insert throughput on sharded collections before launch?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Explain Plan](/mongodb-cheatsheet/03-query-performance/explain-plan/)
- [Next: Monitoring](/mongodb-cheatsheet/04-production-operations/monitoring/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
