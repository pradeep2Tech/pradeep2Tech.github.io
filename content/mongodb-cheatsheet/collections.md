---
title: "Collections"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB collections cheat sheet — creation, capped collections, validation, naming, and database admin."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Collections"
module: 1
moduleTitle: "Core & Data Model"
sectionRef: "1.3"
ShowToc: true
---

## Executive Summary

A **collection** is a grouping of documents within a **database**. Collections are schema-flexible by default; optional **JSON Schema validation** enforces structure at write time.

---

## Core Concepts

| Concept | Recap |
| :--- | :--- |
| **Database** | Namespace container — `use mydb` |
| **Collection** | Analogous to a table — no enforced columns |
| **Capped collection** | Fixed size FIFO — like a ring buffer |
| **Time series** | Optimized collection type for metrics (5.0+) |
| **View** | Read-only aggregation pipeline — no storage |
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

- Collections are created implicitly on first insert — validation must be added before bad data lands.
- `count()` deprecated — use `countDocuments` or `estimatedDocumentCount`.
- Capped collections cannot be sharded; documents cannot be deleted individually (only FIFO eviction).
- `system.profile` and `system.js` are special — avoid naming conflicts.

---

## Related Topics

- [Previous: Documents](/mongodb-cheatsheet/documents/)
- [Next: CRUD](/mongodb-cheatsheet/crud/)
- [Schema Design](/mongodb-cheatsheet/schema-design/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
