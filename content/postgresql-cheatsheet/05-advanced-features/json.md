---
title: "JSON & JSONB"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "json vs jsonb, operators, GIN indexing."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "JSON"
module: 5
moduleTitle: "Advanced Features"
sectionRef: "5.5"
weight: 505
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/json/
---

## Quick Revision

PostgreSQL offers **json** (text storage) and **jsonb** (binary, indexable). Prefer **jsonb** for querying; **json** preserves exact formatting.

---

## Core Concepts

| Operator | Meaning |
| :--- | :--- |
| `->` | Get JSON object field (as json) |
| `->>` | Get field as text |
| `#>` | Path array |
| `@>` | Contains |
| `?` | Key exists |
| `jsonb_set` | Update nested value |

---

## Quick Reference

```sql
SELECT payload->>'kind' AS kind,
       payload->'meta'->>'ip' AS ip
FROM events
WHERE payload @> '{"kind":"login"}';

UPDATE settings
SET body = jsonb_set(body, '{theme}', '"dark"')
WHERE user_id = 1;
```

---

## Snippets

```sql
CREATE TABLE events (
  id bigserial PRIMARY KEY,
  payload jsonb NOT NULL DEFAULT '{}'
);
CREATE INDEX idx_events_kind ON events ((payload->>'kind'));
JSON indexing patterns → canonical [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/) (GIN/jsonb_path_ops).
```

---

## Common Gotchas

- `jsonb` deduplicates keys and does not preserve key order.
- Cast with `::jsonb` — invalid JSON throws error.
- For heavy JSON analytics consider generated columns + B-tree index.

---


## Interview Answers

## Question {#q-93}

How does jsonb_path_ops differ from default jsonb GIN ops?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how does jsonb_path_ops differ from default jsonb gin ops?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/json/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-125}

What extensions support column-level encryption tradeoffs?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: what extensions support column-level encryption tradeoffs?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Security** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/json/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Mat Views](/postgresql-cheatsheet/05-advanced-features/materialized-views/)
- [Next: Views](/postgresql-cheatsheet/05-advanced-features/views/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
