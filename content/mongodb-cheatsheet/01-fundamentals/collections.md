---
title: "Collections"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Collections, validation, capped and time series collections."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Collections"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.2"
weight: 112
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/mongodb-cheatsheet/collections/"
---

## Executive Summary

A **collection** is a grouping of documents within a **database**. Collections are schema-flexible by default; optional **JSON Schema validation** enforces structure at write time.

---

## Core Concepts

| Concept | Recap |
| :--- | :--- |
| **Database** | Namespace container â€” `use mydb` |
| **Collection** | Analogous to a table â€” no enforced columns |
| **Capped collection** | Fixed size FIFO â€” like a ring buffer |
| **Time series** | Optimized collection type for metrics (5.0+) |
| **View** | Read-only aggregation pipeline â€” no storage |
| **Change stream** | Watch insert/update/delete on collection |

---

## Quick Reference

```javascript
// List & switch
show dbs
use ecommerce
show collections

// Create (explicit)
db.createCollection("orders", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["orderId", "total"],
      properties: {
        orderId: { bsonType: "string" },
        total: { bsonType: ["int", "long", "double", "decimal"] }
      }
    }
  },
  validationLevel: "strict",      // "moderate" | "off"
  validationAction: "error"       // "warn"
})

// Capped collection (oplog-style)
db.createCollection("logs", { capped: true, size: 10485760, max: 5000 })

// Time series (5.0+)
db.createCollection("metrics", {
  timeseries: { timeField: "ts", metaField: "sensor", granularity: "seconds" }
})

// Rename / drop
db.orders.renameCollection("orders_archive")
db.old_logs.drop()
```

| Naming rules | |
| :--- | :--- |
| Max length | 120 bytes (UTF-8) |
| Invalid chars | `/`, `\`, `.`, `"`, `*`, space, `$`, NUL |
| Reserved | `system.*` prefix |

---

## Snippets

```javascript
// Collection stats
db.orders.stats()
db.orders.estimatedDocumentCount()
db.orders.countDocuments({ status: "open" })  // accurate, uses index if possible

// Collations (case-insensitive index/query)
db.users.createIndex(
  { email: 1 },
  { collation: { locale: "en", strength: 2 } }
)
db.users.find({ email: "Ada@Example.com" }).collation({ locale: "en", strength: 2 })
```

---

## Common Gotchas

- Collections are created implicitly on first insert â€” validation must be added before bad data lands.
- `count()` deprecated â€” use `countDocuments` or `estimatedDocumentCount`.
- Capped collections cannot be sharded; documents cannot be deleted individually (only FIFO eviction).
- `system.profile` and `system.js` are special â€” avoid naming conflicts.

---

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## When should time series collections replace hand-rolled bucketing schemas?

### Short Answer
The practical MongoDB answer is modeling to dominant read/write paths, then embedding only where growth is bounded for: When should time series collections replace hand-rolled bucketing schemas.

### Detailed Explanation
Schema-first decisions in MongoDB should be query-first in practice, so colocate fields that are read together and externalize unbounded fan-out to references or buckets for: When should time series collections replace hand-rolled bucketing schemas.

### Internal Working
Document growth, index fan-out, and update locality decide the true cost profile internally, which is why embedding works best when mutation scope stays narrow for: When should time series collections replace hand-rolled bucketing schemas.

### Production Notes
You justify it by aligning schema, index, and topology to the access pattern by replaying realistic tenant skew, cardinality growth, and migration paths before freezing the model for: When should time series collections replace hand-rolled bucketing schemas.

### Common Mistakes
A common mistake is copying relational normalization or, conversely, embedding unbounded arrays until 16 MB limits and write amplification appear for: When should time series collections replace hand-rolled bucketing schemas.

### Follow-up Questions
What cardinality limit, migration trigger, and fallback model would you define up front to keep: When should time series collections replace hand-rolled bucketing schemas safe over 3 years?

---
## What is the tradeoff between JSON Schema validation at write time versus application-only validation?

### Short Answer
For this question, the architecturally correct answer is modeling to dominant read/write paths, then embedding only where growth is bounded for: What is the tradeoff between JSON Schema validation at write time versus application-only validation.

### Detailed Explanation
Schema-first decisions in MongoDB should be query-first in practice, so colocate fields that are read together and externalize unbounded fan-out to references or buckets for: What is the tradeoff between JSON Schema validation at write time versus application-only validation.

### Internal Working
Document growth, index fan-out, and update locality decide the true cost profile internally, which is why embedding works best when mutation scope stays narrow for: What is the tradeoff between JSON Schema validation at write time versus application-only validation.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality by replaying realistic tenant skew, cardinality growth, and migration paths before freezing the model for: What is the tradeoff between JSON Schema validation at write time versus application-only validation.

### Common Mistakes
A common mistake is copying relational normalization or, conversely, embedding unbounded arrays until 16 MB limits and write amplification appear for: What is the tradeoff between JSON Schema validation at write time versus application-only validation.

### Follow-up Questions
What cardinality limit, migration trigger, and fallback model would you define up front to keep: What is the tradeoff between JSON Schema validation at write time versus application-only validation safe over 3 years?

---
## How do views differ architecturally from materialized aggregation results?

### Short Answer
The production-grade answer is pushing selective `$match` and projection early, then containing fan-out stages for: How do views differ architecturally from materialized aggregation results.

### Detailed Explanation
Aggregation pipelines stay fast when stage order protects index use and minimizes intermediate document width before `$lookup`, `$group`, or `$facet` for: How do views differ architecturally from materialized aggregation results.

### Internal Working
The optimizer can reorder some stages, but blocking operators still dominate memory and spill behavior under skewed inputs for: How do views differ architecturally from materialized aggregation results.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk by inspecting stage-level execution stats, spill metrics, and cardinality explosions for: How do views differ architecturally from materialized aggregation results.

### Common Mistakes
Typical mistakes are joining before filtering, missing foreign indexes, and normalizing data that should have been embedded for: How do views differ architecturally from materialized aggregation results.

### Follow-up Questions
Which stage in: How do views differ architecturally from materialized aggregation results currently dominates runtime, and do you have evidence that schema change beats pipeline tuning?

---
## How do collation choices at index creation affect case-insensitive search architecture?

### Short Answer
The practical MongoDB answer is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: How do collation choices at index creation affect case-insensitive search architecture.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: How do collation choices at index creation affect case-insensitive search architecture.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: How do collation choices at index creation affect case-insensitive search architecture.

### Production Notes
You justify it by aligning schema, index, and topology to the access pattern with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: How do collation choices at index creation affect case-insensitive search architecture.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: How do collation choices at index creation affect case-insensitive search architecture.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: How do collation choices at index creation affect case-insensitive search architecture in your team?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Documents](/mongodb-cheatsheet/01-fundamentals/documents/)
- [Next: Crud](/mongodb-cheatsheet/01-fundamentals/crud/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
