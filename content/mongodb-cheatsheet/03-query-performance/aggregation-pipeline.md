---
title: "Aggregation Pipeline"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Pipeline stages, $lookup, $facet, optimization patterns."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Aggregation"
module: 3
moduleTitle: "Query & Performance"
sectionRef: "3.5"
weight: 305
cheatSheet: true
interviewHandbook: true
aliases:
  - "/mongodb-cheatsheet/aggregation-pipeline/"
---

## Executive Summary

The **aggregation pipeline** processes documents through ordered **stages**. Each stage transforms the stream. Use `$match` early to leverage indexes; `$lookup` for server-side joins.

---

## Core Concepts

```mermaid
flowchart LR
  docs[Documents] --> match["$match"]
  match --> group["$group"]
  group --> lookup["$lookup"]
  lookup --> project["$project"]
  project --> out[Results]
```

| Stage | Purpose |
| :--- | :--- |
| `$match` | Filter â€” like `find`; put first when possible |
| `$project` | Shape fields â€” include/exclude/compute |
| `$group` | `_id` + accumulators (`$sum`, `$avg`, `$push`) |
| `$sort` | Order results |
| `$limit` / `$skip` | Pagination |
| `$lookup` | Left outer join to another collection |
| `$unwind` | Flatten arrays â€” one doc per element |
| `$facet` | Parallel sub-pipelines |
| `$bucket` / `$bucketAuto` | Histogram grouping |
| `$merge` / `$out` | Write results to collection |

---

## Quick Reference â€” Accumulators

| Accumulator | Use |
| :--- | :--- |
| `$sum` | Total or count with `{ $sum: 1 }` |
| `$avg` | Average |
| `$min` / `$max` | Extremes |
| `$first` / `$last` | With `$sort` inside `$group` |
| `$push` / `$addToSet` | Collect values |
| `$mergeObjects` | Merge documents |

---

## Snippets

```javascript
// Revenue by category (last 30 days)
db.orders.aggregate([
  { $match: { createdAt: { $gte: new Date(Date.now() - 30*864e5) } } },
  { $group: {
      _id: "$category",
      revenue: { $sum: "$total" },
      count: { $sum: 1 }
  }},
  { $sort: { revenue: -1 } }
])

// $lookup (correlated subquery style)
db.orders.aggregate([
  { $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer"
  }},
  { $unwind: "$customer" },
  { $project: { orderId: 1, "customer.email": 1, total: 1 } }
])

// $facet â€” page + total count in one round trip
db.products.aggregate([
  { $match: { inStock: true } },
  { $facet: {
      data: [{ $sort: { price: 1 } }, { $skip: 20 }, { $limit: 10 }],
      meta: [{ $count: "total" }]
  }}
])
```

---

## Common Gotchas

- `$lookup` without index on `foreignField` scans the foreign collection.
- `$group` with large cardinality `_id` can exhaust RAM â€” use `allowDiskUse: true`.
- 100 MB default in-memory limit per stage â€” Atlas/server config can raise it.
- `$where` and `$function` disable index use â€” avoid in hot paths.

---

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## When does `$lookup` indicate a schema modeling problem rather than a query problem?

### Short Answer
The senior-level decision is pushing selective `$match` and projection early, then containing fan-out stages for: When does `$lookup` indicate a schema modeling problem rather than a query problem.

### Detailed Explanation
Aggregation pipelines stay fast when stage order protects index use and minimizes intermediate document width before `$lookup`, `$group`, or `$facet` for: When does `$lookup` indicate a schema modeling problem rather than a query problem.

### Internal Working
The optimizer can reorder some stages, but blocking operators still dominate memory and spill behavior under skewed inputs for: When does `$lookup` indicate a schema modeling problem rather than a query problem.

### Production Notes
You justify it by balancing latency, durability, and operational toil by inspecting stage-level execution stats, spill metrics, and cardinality explosions for: When does `$lookup` indicate a schema modeling problem rather than a query problem.

### Common Mistakes
Typical mistakes are joining before filtering, missing foreign indexes, and normalizing data that should have been embedded for: When does `$lookup` indicate a schema modeling problem rather than a query problem.

### Follow-up Questions
Which stage in: When does `$lookup` indicate a schema modeling problem rather than a query problem currently dominates runtime, and do you have evidence that schema change beats pipeline tuning?

---
## How do you tune aggregation `$lookup` pipeline order for index use?

### Short Answer
The production-grade answer is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: How do you tune aggregation `$lookup` pipeline order for index use.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: How do you tune aggregation `$lookup` pipeline order for index use.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: How do you tune aggregation `$lookup` pipeline order for index use.

### Production Notes
You justify it by minimizing cross-shard work and rollback risk with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: How do you tune aggregation `$lookup` pipeline order for index use.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: How do you tune aggregation `$lookup` pipeline order for index use.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: How do you tune aggregation `$lookup` pipeline order for index use in your team?

---
## When is `allowDiskUse: true` acceptable versus a design smell?

### Short Answer
The senior-level decision is pushing selective `$match` and projection early, then containing fan-out stages for: When is `allowDiskUse: true` acceptable versus a design smell.

### Detailed Explanation
Aggregation pipelines stay fast when stage order protects index use and minimizes intermediate document width before `$lookup`, `$group`, or `$facet` for: When is `allowDiskUse: true` acceptable versus a design smell.

### Internal Working
The optimizer can reorder some stages, but blocking operators still dominate memory and spill behavior under skewed inputs for: When is `allowDiskUse: true` acceptable versus a design smell.

### Production Notes
You justify it by balancing latency, durability, and operational toil by inspecting stage-level execution stats, spill metrics, and cardinality explosions for: When is `allowDiskUse: true` acceptable versus a design smell.

### Common Mistakes
Typical mistakes are joining before filtering, missing foreign indexes, and normalizing data that should have been embedded for: When is `allowDiskUse: true` acceptable versus a design smell.

### Follow-up Questions
Which stage in: When is `allowDiskUse: true` acceptable versus a design smell currently dominates runtime, and do you have evidence that schema change beats pipeline tuning?

---
## What `$facet` patterns reduce round trips without exploding memory?

### Short Answer
For this question, the architecturally correct answer is pushing selective `$match` and projection early, then containing fan-out stages for: What `$facet` patterns reduce round trips without exploding memory.

### Detailed Explanation
Aggregation pipelines stay fast when stage order protects index use and minimizes intermediate document width before `$lookup`, `$group`, or `$facet` for: What `$facet` patterns reduce round trips without exploding memory.

### Internal Working
The optimizer can reorder some stages, but blocking operators still dominate memory and spill behavior under skewed inputs for: What `$facet` patterns reduce round trips without exploding memory.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality by inspecting stage-level execution stats, spill metrics, and cardinality explosions for: What `$facet` patterns reduce round trips without exploding memory.

### Common Mistakes
Typical mistakes are joining before filtering, missing foreign indexes, and normalizing data that should have been embedded for: What `$facet` patterns reduce round trips without exploding memory.

### Follow-up Questions
Which stage in: What `$facet` patterns reduce round trips without exploding memory currently dominates runtime, and do you have evidence that schema change beats pipeline tuning?

---
## How does the aggregation optimizer push `$match` before `$lookup`?

### Short Answer
The practical MongoDB answer is pushing selective `$match` and projection early, then containing fan-out stages for: How does the aggregation optimizer push `$match` before `$lookup`.

### Detailed Explanation
Aggregation pipelines stay fast when stage order protects index use and minimizes intermediate document width before `$lookup`, `$group`, or `$facet` for: How does the aggregation optimizer push `$match` before `$lookup`.

### Internal Working
The optimizer can reorder some stages, but blocking operators still dominate memory and spill behavior under skewed inputs for: How does the aggregation optimizer push `$match` before `$lookup`.

### Production Notes
You justify it by aligning schema, index, and topology to the access pattern by inspecting stage-level execution stats, spill metrics, and cardinality explosions for: How does the aggregation optimizer push `$match` before `$lookup`.

### Common Mistakes
Typical mistakes are joining before filtering, missing foreign indexes, and normalizing data that should have been embedded for: How does the aggregation optimizer push `$match` before `$lookup`.

### Follow-up Questions
Which stage in: How does the aggregation optimizer push `$match` before `$lookup` currently dominates runtime, and do you have evidence that schema change beats pipeline tuning?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Geospatial](/mongodb-cheatsheet/03-query-performance/geospatial/)
- [Next: Query Optimization](/mongodb-cheatsheet/03-query-performance/query-optimization/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
