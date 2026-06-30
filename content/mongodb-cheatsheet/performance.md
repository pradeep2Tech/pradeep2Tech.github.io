---
title: "Performance"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB performance cheat sheet — explain plans, index strategy, working set, connection pooling, and profiling."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Performance"
module: 4
moduleTitle: "Design, Ops & Reference"
sectionRef: "4.3"
ShowToc: true
---

## Executive Summary

MongoDB performance tuning starts with **query patterns and indexes**, then **working set in RAM**, then **hardware and topology**. Always `explain("executionStats")` before adding indexes blindly.

---

## Core Concepts

| Layer | Lever |
| :--- | :--- |
| **Query** | Indexes, projections, `$match` first in aggregation |
| **Schema** | Embed to avoid joins; avoid unbounded growth |
| **Storage** | WiredTiger cache (default ~50% RAM − 1 GB) |
| **Replication** | Offload reads to secondaries with acceptable staleness |
| **Sharding** | Horizontal scale when single replica set saturates |

---

## Quick Reference

```javascript
// Explain — key metrics
const exp = db.orders.find({ status: "open" }).explain("executionStats")
// totalDocsExamined vs nReturned — aim for ratio near 1
// executionTimeMillis, stage: IXSCAN vs COLLSCAN

// Profiler (slow queries > 100ms)
db.setProfilingLevel(1, { slowms: 100 })
db.system.profile.find().sort({ ts: -1 }).limit(5)

// Current ops
db.currentOp({ "active": true, "secs_running": { $gt: 3 } })

// Index usage stats
db.orders.aggregate([{ $indexStats: {} }])
```

| Symptom | Likely cause |
| :--- | :--- |
| High `docsExamined` | Missing/wrong index |
| Write latency spikes | Too many indexes, large documents |
| Replication lag | Heavy writes, small oplog, disk bound |
| Page faults | Working set exceeds RAM |

---

## Snippets

```javascript
// Pagination — avoid large skip; use range on indexed field
db.orders.find({ _id: { $gt: lastId } }).sort({ _id: 1 }).limit(50)

// Projection reduces network and decode cost
db.users.find({ status: "active" }, { email: 1, _id: 0 })

// Bulk unordered inserts
db.events.insertMany(docs, { ordered: false })

// Connection pool (driver) — default often 100; tune per app instances
// maxPoolSize in URI or MongoClientSettings
```

```bash
# mongostat / mongotop (host tools)
mongostat --uri "mongodb://..." 5
mongotop --uri "mongodb://..." 5
```

---

## Common Gotchas

- `$regex` prefix wildcard (`/^.*foo/`) cannot use index — anchor left (`/^foo/`).
- Case-insensitive regex without collation scans the collection.
- `allowDiskUse` in aggregation spills to disk — slower but prevents failures.
- Many app instances × large `maxPoolSize` can overwhelm mongod — size pools globally.

---

## Related Topics

- [Previous: Atlas Basics](/mongodb-cheatsheet/atlas-basics/)
- [Next: Mongo Shell Commands](/mongodb-cheatsheet/mongo-shell-commands/)
- [Indexes](/mongodb-cheatsheet/indexes/)
- [Sharding](/mongodb-cheatsheet/sharding/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
