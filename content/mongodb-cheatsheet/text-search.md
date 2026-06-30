---
title: "Text Search"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB text search cheat sheet — $text index, $search, weights, language, and Atlas Search overview."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Text Search"
module: 2
moduleTitle: "Queries & Indexes"
sectionRef: "2.4"
ShowToc: true
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

// Atlas Search (via $search stage — requires Atlas Search index)
db.articles.aggregate([
  { $search: {
      index: "default",
      text: { query: "kubernetes mongodb", path: ["title", "body"] }
  }}
])
```

---

## Common Gotchas

- Text index tokenizes and stems — poor fit for SKU codes or exact identifiers (use regular index).
- Case-insensitive regex on unindexed fields scans the collection — use text or Atlas Search.
- Combining `$text` with other operators in `$or` has restrictions — check server version docs.
- Atlas Search indexes are separate from standard indexes — define via Atlas UI or API.

---

## Related Topics

- [Previous: TTL Index](/mongodb-cheatsheet/ttl-index/)
- [Next: Geospatial](/mongodb-cheatsheet/geospatial/)
- [Indexes](/mongodb-cheatsheet/indexes/)
- [Atlas Basics](/mongodb-cheatsheet/atlas-basics/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
