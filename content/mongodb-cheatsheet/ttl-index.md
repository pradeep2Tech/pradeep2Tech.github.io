---
title: "TTL Index"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB TTL index cheat sheet — automatic document expiry, expireAfterSeconds, and session cleanup patterns."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "TTL Index"
module: 2
moduleTitle: "Queries & Indexes"
sectionRef: "2.3"
ShowToc: true
---

## Executive Summary

A **TTL index** is a special single-field index on a **Date** field. MongoDB's background thread deletes documents when `indexedDate + expireAfterSeconds` passes. Deletion is **not instantaneous** — typically within 60 seconds.

---

## Core Concepts

| Rule | Detail |
| :--- | :--- |
| Field type | Must be BSON Date or array of Dates |
| Index shape | Single-field only — no compound TTL |
| `expireAfterSeconds` | Seconds after indexed date value |
| `0` value | Delete when date value is reached exactly |
| Replica sets | TTL runs on primary only |

---

## Quick Reference

```javascript
// Sessions expire 24 hours after lastActivity
db.sessions.createIndex(
  { lastActivity: 1 },
  { expireAfterSeconds: 86400 }
)

// Delete at exact timestamp (e.g. event end time)
db.events.createIndex(
  { expiresAt: 1 },
  { expireAfterSeconds: 0 }
)

// Modify TTL
db.runCommand({
  collMod: "sessions",
  index: { keyPattern: { lastActivity: 1 }, expireAfterSeconds: 3600 }
})
```

---

## Snippets

```javascript
// Pattern: sliding session TTL — update date on each request
db.sessions.updateOne(
  { sessionId: "abc" },
  { $set: { lastActivity: new Date(), userId: "u1" } },
  { upsert: true }
)

// TTL + partial index (expire only completed jobs)
db.jobs.createIndex(
  { completedAt: 1 },
  {
    expireAfterSeconds: 604800,  // 7 days
    partialFilterExpression: { status: "done" }
  }
)
```

---

## Common Gotchas

- TTL deletes whole documents — not individual fields.
- Deletion lag means do not rely on TTL for real-time security boundaries (use app-level checks too).
- Cannot TTL-index `_id` (contains creation time but is not a Date field).
- Large collections may see bursty delete load — monitor IOPS.

---

## Related Topics

- [Previous: Aggregation Pipeline](/mongodb-cheatsheet/aggregation-pipeline/)
- [Next: Text Search](/mongodb-cheatsheet/text-search/)
- [Indexes](/mongodb-cheatsheet/indexes/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
