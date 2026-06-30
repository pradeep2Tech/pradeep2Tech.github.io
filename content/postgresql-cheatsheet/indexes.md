---
title: "Indexes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "B-tree, GIN, GiST, BRIN, partial, and covering index patterns."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Indexes"
module: 3
moduleTitle: "Query Performance"
sectionRef: "3.1"
ShowToc: true
---

## Executive Summary

Indexes accelerate reads at write/storage cost. Default **B-tree** suits most equality/range queries; specialized indexes for JSON, text search, and geospatial.

---

## Core Concepts

| Type | Best for |
| :--- | :--- |
| **B-tree** (default) | `=`, `<`, `>`, `BETWEEN`, `ORDER BY` |
| **Hash** | Equality only — rarely needed vs B-tree |
| **GIN** | jsonb, arrays, full-text |
| **GiST** | Geometric, range types, full-text |
| **BRIN** | Very large, naturally ordered tables |
| **Partial** | `WHERE active = true` — smaller, targeted |

---

## Quick Reference

```sql
CREATE INDEX idx_orders_user_created ON orders (user_id, created_at DESC);
CREATE INDEX idx_users_email_lower ON users (lower(email));
CREATE UNIQUE INDEX idx_products_sku ON products (sku);

-- Covering index (INCLUDE — PG 11+)
CREATE INDEX idx_orders_cover ON orders (user_id) INCLUDE (total, status);
```

---

## Snippets

```sql
-- JSONB GIN
CREATE INDEX idx_events_payload ON events USING gin (payload jsonb_path_ops);

-- Partial index
CREATE INDEX idx_active_users ON users (last_login) WHERE status = 'active';
```

---

## Common Gotchas

- Unused indexes waste write amplification — check `pg_stat_user_indexes`.
- `REINDEX CONCURRENTLY` rebuilds without blocking reads (PG 12+).
- Too many indexes on hot write tables hurts INSERT/UPDATE throughput.

---

## Related Topics

- [Previous: Joins](/postgresql-cheatsheet/joins/)
- [Next: EXPLAIN](/postgresql-cheatsheet/explain/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
