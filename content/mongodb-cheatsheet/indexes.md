---
title: "Indexes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB indexes cheat sheet — single, compound, multikey, partial, sparse, covered queries, and explain."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Indexes"
module: 2
moduleTitle: "Queries & Indexes"
sectionRef: "2.1"
ShowToc: true
---

## Executive Summary

Indexes accelerate queries and enforce uniqueness. WiredTiger uses **B-tree** indexes by default. The **ESR rule** guides compound index field order: **E**quality, **S**ort, **R**ange.

---

## Core Concepts

| Index type | Use |
| :--- | :--- |
| **Single field** | `{ field: 1 }` or `-1` for sort direction |
| **Compound** | Multiple fields — order matters |
| **Multikey** | Auto-created when indexing array fields |
| **Text** | Full-text search — one per collection |
| **2dsphere** | Geo queries on GeoJSON |
| **Hashed** | Shard key candidate — equality only |
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
| `COLLSCAN` | Full collection scan — usually bad at scale |
| `IXSCAN` | Index scan — good |
| `FETCH` | Load documents after index lookup |
| `PROJECTION_COVERED` | Index-only — no FETCH needed |

---

## Snippets

```javascript
// Covered query — include all projected/sorted/filtered fields in index
db.orders.createIndex({ status: 1, orderId: 1, total: 1 })
db.orders.find(
  { status: "open" },
  { _id: 0, orderId: 1, total: 1 }
)

// Index intersection (use sparingly — prefer compound)
// MongoDB may AND multiple single-field indexes

// Hide index (test before drop)
db.orders.hideIndex("legacy_field_1")
db.orders.unhideIndex("legacy_field_1")
```

---

## Common Gotchas

- Too many indexes slow writes — each index is updated on insert/update.
- Compound index `{ a: 1, b: 1 }` supports `{ a }` and `{ a, b }` but not `{ b }` alone.
- Multikey indexes cannot enforce unique compound keys across array elements in all cases.
- Background index build is default in modern versions — still monitor load during build.

---

## Related Topics

- [Previous: CRUD](/mongodb-cheatsheet/crud/)
- [Next: Aggregation Pipeline](/mongodb-cheatsheet/aggregation-pipeline/)
- [TTL Index](/mongodb-cheatsheet/ttl-index/)
- [Performance](/mongodb-cheatsheet/performance/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
