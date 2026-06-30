---
title: "CRUD"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB CRUD cheat sheet — find, insert, update, delete, operators, projections, and bulk writes."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "CRUD"
module: 1
moduleTitle: "Core & Data Model"
sectionRef: "1.4"
ShowToc: true
---

## Executive Summary

MongoDB CRUD maps to **`insert*`**, **`find*`**, **`update*`**, and **`delete*`** methods. Updates use **update operators** (`$set`, `$inc`, …) — never replace the whole document unless intentional.

---

## Core Concepts

| Method | Purpose |
| :--- | :--- |
| `insertOne` / `insertMany` | Create documents |
| `find` / `findOne` | Read with filter, projection, sort, skip, limit |
| `updateOne` / `updateMany` / `replaceOne` | Modify matched documents |
| `deleteOne` / `deleteMany` | Remove matched documents |
| `bulkWrite` | Mixed ordered/unordered batch |

---

## Quick Reference — Query Operators

| Operator | Example |
| :--- | :--- |
| Comparison | `{ age: { $gte: 18, $lt: 65 } }` |
| Logical | `{ $and: [{ a: 1 }, { b: 2 }] }`, `$or`, `$nor`, `$not` |
| Element | `{ field: { $exists: true } }`, `$type` |
| Array | `$in`, `$nin`, `$all`, `$size`, `$elemMatch` |
| Evaluation | `$regex`, `$expr`, `$jsonSchema`, `$mod` |

---

## Quick Reference — Update Operators

| Operator | Effect |
| :--- | :--- |
| `$set` / `$unset` | Set or remove fields |
| `$inc` / `$mul` | Numeric increment/multiply |
| `$push` / `$pull` / `$addToSet` | Array mutations |
| `$rename` | Rename field |
| `$currentDate` | Set to current date |
| `$setOnInsert` | Apply only on upsert insert |
| `$bit` | Bitwise AND/OR/XOR |

---

## Snippets

```javascript
// Find with projection & sort
db.orders.find(
  { status: "shipped", total: { $gte: 100 } },
  { orderId: 1, total: 1, _id: 0 }
).sort({ createdAt: -1 }).limit(20)

// Upsert
db.inventory.updateOne(
  { sku: "ABC" },
  { $inc: { qty: 1 }, $setOnInsert: { sku: "ABC", createdAt: new Date() } },
  { upsert: true }
)

// Array filters (update matching array elements)
db.products.updateOne(
  { _id: 1 },
  { $set: { "reviews.$[elem].verified": true } },
  { arrayFilters: [{ "elem.rating": { $gte: 4 } }] }
)

// Bulk write
db.orders.bulkWrite([
  { insertOne: { document: { orderId: "O1" } } },
  { updateOne: { filter: { orderId: "O2" }, update: { $set: { status: "paid" } } } },
  { deleteOne: { filter: { orderId: "O3" } } }
], { ordered: false })
```

---

## Common Gotchas

- `updateOne` without operators replaces the document (legacy behavior) — always use `$set` etc.
- `findOneAndUpdate` returns the **pre-update** document by default — use `{ returnDocument: "after" }`.
- Large `skip` values are slow — use range queries on indexed fields for pagination.
- `deleteMany({})` removes all documents but keeps indexes — `drop()` removes the collection.

---

## Related Topics

- [Previous: Collections](/mongodb-cheatsheet/collections/)
- [Next: Indexes](/mongodb-cheatsheet/indexes/)
- [Aggregation Pipeline](/mongodb-cheatsheet/aggregation-pipeline/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
