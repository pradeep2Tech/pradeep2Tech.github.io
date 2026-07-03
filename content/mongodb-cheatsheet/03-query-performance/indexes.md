---
title: "Indexes"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Index types, ESR rule, compound, partial, sparse, wildcard."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Indexes"
module: 3
moduleTitle: "Query & Performance"
sectionRef: "3.1"
weight: 301
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/mongodb-cheatsheet/indexes/"
---

## Executive Summary

Indexes accelerate queries and enforce uniqueness. WiredTiger uses **B-tree** indexes by default. The **ESR rule** guides compound index field order: **E**quality, **S**ort, **R**ange.

---

## Core Concepts

| Index type | Use |
| :--- | :--- |
| **Single field** | `{ field: 1 }` or `-1` for sort direction |
| **Compound** | Multiple fields â€” order matters |
| **Multikey** | Auto-created when indexing array fields |
| **Text** | Full-text search â€” one per collection |
| **2dsphere** | Geo queries on GeoJSON |
| **Hashed** | Shard key candidate â€” equality only |
| **Partial** | Index subset matching filter |
| **Sparse** | Skip docs missing the field |
| **Wildcard** | `{ "attributes.$**": 1 }` for dynamic schemas |

---

## Quick Reference

```javascript
// Create indexes
db.orders.createIndex({ customerId: 1, createdAt: -1 })
db.users.createIndex({ email: 1 }, { unique: true })
db.events.createIndex(
  { status: 1 },
  { partialFilterExpression: { status: { $eq: "active" } } }
)

// List & drop
db.orders.getIndexes()
db.orders.dropIndex("customerId_1_createdAt_-1")

// Explain
db.orders.find({ customerId: "C1" }).sort({ createdAt: -1 }).explain("executionStats")
```

| `explain` stage | Meaning |
| :--- | :--- |
| `COLLSCAN` | Full collection scan â€” usually bad at scale |
| `IXSCAN` | Index scan â€” good |
| `FETCH` | Load documents after index lookup |
| `PROJECTION_COVERED` | Index-only â€” no FETCH needed |

---

## Snippets

```javascript
// Covered query â€” include all projected/sorted/filtered fields in index
db.orders.createIndex({ status: 1, orderId: 1, total: 1 })
db.orders.find(
  { status: "open" },
  { _id: 0, orderId: 1, total: 1 }
)

// Index intersection (use sparingly â€” prefer compound)
// MongoDB may AND multiple single-field indexes

// Hide index (test before drop)
db.orders.hideIndex("legacy_field_1")
db.orders.unhideIndex("legacy_field_1")
```

---

## Common Gotchas

- Too many indexes slow writes â€” each index is updated on insert/update.
- Compound index `{ a: 1, b: 1 }` supports `{ a }` and `{ a, b }` but not `{ b }` alone.
- Multikey indexes cannot enforce unique compound keys across array elements in all cases.
- Background index build is default in modern versions â€” still monitor load during build.

---

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## How do you detect and fix index builds stuck in background on large collections?

### Short Answer
The production-grade answer is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: How do you detect and fix index builds stuck in background on large collections.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: How do you detect and fix index builds stuck in background on large collections.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: How do you detect and fix index builds stuck in background on large collections.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: How do you detect and fix index builds stuck in background on large collections.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: How do you detect and fix index builds stuck in background on large collections.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: How do you detect and fix index builds stuck in background on large collections in your team?

---
## What ESR ordering would you use for `{ status, createdAt, amount }` filters?

### Short Answer
For this question, the architecturally correct answer is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: What ESR ordering would you use for `{ status, createdAt, amount }` filters.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: What ESR ordering would you use for `{ status, createdAt, amount }` filters.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: What ESR ordering would you use for `{ status, createdAt, amount }` filters.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: What ESR ordering would you use for `{ status, createdAt, amount }` filters.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: What ESR ordering would you use for `{ status, createdAt, amount }` filters.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: What ESR ordering would you use for `{ status, createdAt, amount }` filters in your team?

---
## How do partial indexes reduce write amplification for status-filtered queries?

### Short Answer
The senior-level decision is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: How do partial indexes reduce write amplification for status-filtered queries.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: How do partial indexes reduce write amplification for status-filtered queries.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: How do partial indexes reduce write amplification for status-filtered queries.

### Production Notes
You justify it by balancing latency, durability, and operational toil with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: How do partial indexes reduce write amplification for status-filtered queries.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: How do partial indexes reduce write amplification for status-filtered queries.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: How do partial indexes reduce write amplification for status-filtered queries in your team?

---
## How does collation-aware indexing affect sort stage elimination?

### Short Answer
The production-grade answer is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: How does collation-aware indexing affect sort stage elimination.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: How does collation-aware indexing affect sort stage elimination.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: How does collation-aware indexing affect sort stage elimination.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: How does collation-aware indexing affect sort stage elimination.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: How does collation-aware indexing affect sort stage elimination.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: How does collation-aware indexing affect sort stage elimination in your team?

---
## How do multikey indexes behave when array fields grow unbounded?

### Short Answer
The production-grade answer is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: How do multikey indexes behave when array fields grow unbounded.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: How do multikey indexes behave when array fields grow unbounded.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: How do multikey indexes behave when array fields grow unbounded.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: How do multikey indexes behave when array fields grow unbounded.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: How do multikey indexes behave when array fields grow unbounded.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: How do multikey indexes behave when array fields grow unbounded in your team?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Schema Design](/mongodb-cheatsheet/02-core-mongodb/schema-design/)
- [Next: Ttl Index](/mongodb-cheatsheet/03-query-performance/ttl-index/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
