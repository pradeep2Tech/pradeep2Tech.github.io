---
title: "CRUD"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Find, insert, update, delete, operators, and bulk writes."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "CRUD"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.3"
weight: 113
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/mongodb-cheatsheet/crud/"
---

## Executive Summary

MongoDB CRUD maps to **`insert*`**, **`find*`**, **`update*`**, and **`delete*`** methods. Updates use **update operators** (`$set`, `$inc`, â€¦) â€” never replace the whole document unless intentional.

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

## Quick Reference â€” Query Operators

| Operator | Example |
| :--- | :--- |
| Comparison | `{ age: { $gte: 18, $lt: 65 } }` |
| Logical | `{ $and: [{ a: 1 }, { b: 2 }] }`, `$or`, `$nor`, `$not` |
| Element | `{ field: { $exists: true } }`, `$type` |
| Array | `$in`, `$nin`, `$all`, `$size`, `$elemMatch` |
| Evaluation | `$regex`, `$expr`, `$jsonSchema`, `$mod` |

---

## Quick Reference â€” Update Operators

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

- `updateOne` without operators replaces the document (legacy behavior) â€” always use `$set` etc.
- `findOneAndUpdate` returns the **pre-update** document by default â€” use `{ returnDocument: "after" }`.
- Large `skip` values are slow â€” use range queries on indexed fields for pagination.
- `deleteMany({})` removes all documents but keeps indexes â€” `drop()` removes the collection.

---

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## How do you prevent `$where` and server-side JavaScript from becoming security holes?

### Short Answer
The practical MongoDB answer is implementing layered controls: private connectivity, least-privilege roles, TLS, and managed secrets for: How do you prevent `$where` and server-side JavaScript from becoming security holes.

### Detailed Explanation
MongoDB security is defense-in-depth; network isolation and RBAC boundaries limit blast radius, while encryption and audit trails satisfy compliance for: How do you prevent `$where` and server-side JavaScript from becoming security holes.

### Internal Working
Authn/authz, transport encryption, and optional client-side field encryption each protect different threat surfaces for: How do you prevent `$where` and server-side JavaScript from becoming security holes.

### Production Notes
You justify it by aligning schema, index, and topology to the access pattern with role reviews, credential rotation drills, network path validation, and audit evidence retention for: How do you prevent `$where` and server-side JavaScript from becoming security holes.

### Common Mistakes
Common failures include internet-exposed endpoints, static credentials in config files, and broad admin roles for applications in: How do you prevent `$where` and server-side JavaScript from becoming security holes.

### Follow-up Questions
Which control in: How do you prevent `$where` and server-side JavaScript from becoming security holes gives the largest blast-radius reduction right now: network, RBAC, or key management?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Collections](/mongodb-cheatsheet/01-fundamentals/collections/)
- [Next: Atlas Basics](/mongodb-cheatsheet/01-fundamentals/atlas-basics/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
