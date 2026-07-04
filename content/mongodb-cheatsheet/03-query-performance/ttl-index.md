---
title: "TTL Index"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Automatic document expiry with TTL indexes."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "TTL"
module: 3
moduleTitle: "Query & Performance"
sectionRef: "3.2"
weight: 302
cheatSheet: true
interviewHandbook: true
aliases:
  - "/mongodb-cheatsheet/ttl-index/"
---

## Executive Summary

A **TTL index** is a special single-field index on a **Date** field. MongoDB's background thread deletes documents when `indexedDate + expireAfterSeconds` passes. Deletion is **not instantaneous** â€” typically within 60 seconds.

---

## Core Concepts

| Rule | Detail |
| :--- | :--- |
| Field type | Must be BSON Date or array of Dates |
| Index shape | Single-field only â€” no compound TTL |
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
// Pattern: sliding session TTL â€” update date on each request
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

- TTL deletes whole documents â€” not individual fields.
- Deletion lag means do not rely on TTL for real-time security boundaries (use app-level checks too).
- Cannot TTL-index `_id` (contains creation time but is not a Date field).
- Large collections may see bursty delete load â€” monitor IOPS.

---

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## What TTL index misconfigurations cause documents to never expire?

### Short Answer
The senior-level decision is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: What TTL index misconfigurations cause documents to never expire.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: What TTL index misconfigurations cause documents to never expire.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: What TTL index misconfigurations cause documents to never expire.

### Production Notes
You justify it by balancing latency, durability, and operational toil with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: What TTL index misconfigurations cause documents to never expire.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: What TTL index misconfigurations cause documents to never expire.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: What TTL index misconfigurations cause documents to never expire in your team?

---
## How do you design session TTL indexes that survive clock skew?

### Short Answer
The practical MongoDB answer is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: How do you design session TTL indexes that survive clock skew.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: How do you design session TTL indexes that survive clock skew.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: How do you design session TTL indexes that survive clock skew.

### Production Notes
You justify it by aligning schema, index, and topology to the access pattern with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: How do you design session TTL indexes that survive clock skew.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: How do you design session TTL indexes that survive clock skew.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: How do you design session TTL indexes that survive clock skew in your team?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Indexes](/mongodb-cheatsheet/03-query-performance/indexes/)
- [Next: Text Search](/mongodb-cheatsheet/03-query-performance/text-search/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
