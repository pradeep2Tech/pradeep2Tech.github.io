---
title: "Text Search"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Text indexes, $text, Atlas Search overview."
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "Text Search"
module: 3
moduleTitle: "Query & Performance"
sectionRef: "3.3"
weight: 303
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/mongodb-cheatsheet/text-search/"
---

## Executive Summary

MongoDB provides built-in **text indexes** for basic full-text search via `$text` / `$search`. One text index per collection. For advanced relevance, faceting, and autocomplete use **Atlas Search** (Lucene-based).

---

## Core Concepts

| Feature | Text index (`$text`) | Atlas Search |
| :--- | :--- | :--- |
| Deployment | Self-managed + Atlas | Atlas primarily |
| Index limit | One per collection | Multiple search indexes |
| Stemming | Yes (per language) | Yes + analyzers |
| Phrase search | Limited | Rich query DSL |
| Fuzzy / autocomplete | No | Yes |

---

## Quick Reference

```javascript
// Create text index (compound: only ONE text index allowed)
db.articles.createIndex({
  title: "text",
  body: "text"
}, {
  weights: { title: 10, body: 1 },
  default_language: "english"
})

// Query
db.articles.find(
  { $text: { $search: "mongodb indexing -sql" } },
  { score: { $meta: "textScore" } }
).sort({ score: { $meta: "textScore" } })

// Phrase (quoted)
db.articles.find({ $text: { $search: "\"replica set\"" } })
```

| `$search` operator | Effect |
| :--- | :--- |
| word | Include term |
| `-word` | Exclude term |
| `"phrase"` | Exact phrase |

---

## Snippets

```javascript
// Aggregation with text score
db.articles.aggregate([
  { $match: { $text: { $search: "aggregation pipeline" } } },
  { $addFields: { score: { $meta: "textScore" } } },
  { $match: { score: { $gte: 1.0 } } },
  { $sort: { score: -1 } },
  { $limit: 10 }
])

// Atlas Search (via $search stage â€” requires Atlas Search index)
db.articles.aggregate([
  { $search: {
      index: "default",
      text: { query: "kubernetes mongodb", path: ["title", "body"] }
  }}
])
```

---

## Common Gotchas

- Text index tokenizes and stems â€” poor fit for SKU codes or exact identifiers (use regular index).
- Case-insensitive regex on unindexed fields scans the collection â€” use text or Atlas Search.
- Combining `$text` with other operators in `$or` has restrictions â€” check server version docs.
- Atlas Search indexes are separate from standard indexes â€” define via Atlas UI or API.

---

<!-- interview-answers:start -->

# Interview Answers (Top 150)

## What causes `$text` queries to return unexpected stems or misses on SKUs?

### Short Answer
The senior-level decision is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: What causes `$text` queries to return unexpected stems or misses on SKUs.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: What causes `$text` queries to return unexpected stems or misses on SKUs.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: What causes `$text` queries to return unexpected stems or misses on SKUs.

### Production Notes
You justify it by balancing latency, durability, and operational toil with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: What causes `$text` queries to return unexpected stems or misses on SKUs.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: What causes `$text` queries to return unexpected stems or misses on SKUs.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: What causes `$text` queries to return unexpected stems or misses on SKUs in your team?

---
## When does Atlas Search justify operational complexity over `$text` indexes?

### Short Answer
The senior-level decision is deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: When does Atlas Search justify operational complexity over `$text` indexes.

### Detailed Explanation
Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: When does Atlas Search justify operational complexity over `$text` indexes.

### Internal Working
Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: When does Atlas Search justify operational complexity over `$text` indexes.

### Production Notes
You justify it by balancing latency, durability, and operational toil with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: When does Atlas Search justify operational complexity over `$text` indexes.

### Common Mistakes
Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: When does Atlas Search justify operational complexity over `$text` indexes.

### Follow-up Questions
What threshold in scanned/returned ratio should trigger redesign for: When does Atlas Search justify operational complexity over `$text` indexes in your team?

---
## What hybrid search architecture combines Atlas Search with operational MongoDB data?

### Short Answer
For this question, the architecturally correct answer is modeling to dominant read/write paths, then embedding only where growth is bounded for: What hybrid search architecture combines Atlas Search with operational MongoDB data.

### Detailed Explanation
Schema-first decisions in MongoDB should be query-first in practice, so colocate fields that are read together and externalize unbounded fan-out to references or buckets for: What hybrid search architecture combines Atlas Search with operational MongoDB data.

### Internal Working
Document growth, index fan-out, and update locality decide the true cost profile internally, which is why embedding works best when mutation scope stays narrow for: What hybrid search architecture combines Atlas Search with operational MongoDB data.

### Production Notes
You justify it by proving p95/p99 behavior under realistic cardinality by replaying realistic tenant skew, cardinality growth, and migration paths before freezing the model for: What hybrid search architecture combines Atlas Search with operational MongoDB data.

### Common Mistakes
A common mistake is copying relational normalization or, conversely, embedding unbounded arrays until 16 MB limits and write amplification appear for: What hybrid search architecture combines Atlas Search with operational MongoDB data.

### Follow-up Questions
What cardinality limit, migration trigger, and fallback model would you define up front to keep: What hybrid search architecture combines Atlas Search with operational MongoDB data safe over 3 years?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Ttl Index](/mongodb-cheatsheet/03-query-performance/ttl-index/)
- [Next: Geospatial](/mongodb-cheatsheet/03-query-performance/geospatial/)
- [MongoDB Handbook Index](/mongodb-cheatsheet/)
- [Top 150 Interview Questions](/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/)
