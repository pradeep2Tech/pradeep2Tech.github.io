---
title: "Documents"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB document model cheat sheet — BSON types, _id, dot notation, arrays, and embedded vs referenced data."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Documents"
module: 1
moduleTitle: "Core & Data Model"
sectionRef: "1.2"
ShowToc: true
---

## Executive Summary

MongoDB stores **BSON** documents (binary JSON). Every document requires an **`_id`** field (auto-generated `ObjectId` if omitted). Documents support nested objects, arrays, and rich types beyond JSON.

---

## Core Concepts

| BSON Type | Notes |
| :--- | :--- |
| `ObjectId` | 12-byte ID — 4-byte timestamp + machine + pid + counter |
| `String` | UTF-8 |
| `Int32` / `Int64` / `Double` / `Decimal128` | Use `Decimal128` for money |
| `Date` | UTC milliseconds since epoch |
| `BinData` | Binary blobs |
| `Array` | Ordered; multikey indexes apply |
| `Document` | Nested sub-documents |
| `Null` / `Undefined` | `Undefined` deprecated — avoid |
| `Regex` | Pattern matching in queries |

```mermaid
flowchart LR
  doc["{ _id, name, address: { city }, tags: [] }"]
  doc --> field[Field paths via dot notation]
  doc --> arr[Array indexing tags.0]
```

---

## Quick Reference

| Operation | Syntax |
| :--- | :--- |
| Field access | `doc.address.city` or `"address.city"` in queries |
| Array element | `"tags.0"`, `"tags.-1"` (positional update) |
| Array match any | `"tags": "mongodb"` |
| Array match all | `{ tags: { $all: ["a", "b"] } }` |
| Exists check | `{ field: { $exists: true } }` |
| Type check | `{ field: { $type: "string" } }` |

| Limit | Value |
| :--- | :--- |
| Max document size | 16 MB |
| Max nesting depth | 100 levels |
| Field name | Cannot start with `$` (reserved) |

---

## Snippets

```javascript
// ObjectId inspection
ObjectId("507f1f77bcf86cd799439011").getTimestamp()

// Insert with explicit _id
db.users.insertOne({
  _id: "user-42",
  email: "a@example.com",
  profile: { name: "Ada", roles: ["admin"] },
  createdAt: new Date()
})

// Update nested field
db.users.updateOne(
  { _id: "user-42" },
  { $set: { "profile.name": "Ada Lovelace" } }
)

// Array operators
db.users.updateOne(
  { _id: "user-42" },
  { $push: { "profile.roles": "editor" } }
)
```

---

## Common Gotchas

- `_id` is immutable — delete and re-insert to change it.
- Duplicate keys in a single document are invalid BSON (last wins in some parsers — don't rely on it).
- `ObjectId` is not guaranteed globally unique under extreme clock skew — use UUID if required.
- 16 MB limit includes field names and BSON overhead — large blobs belong in GridFS or object storage.

---

## Related Topics

- [Previous: Architecture](/mongodb-cheatsheet/architecture/)
- [Next: Collections](/mongodb-cheatsheet/collections/)
- [Schema Design](/mongodb-cheatsheet/schema-design/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
