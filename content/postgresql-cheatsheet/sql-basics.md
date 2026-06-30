---
title: "SQL Basics"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, and psql essentials."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "SQL Basics"
module: 1
moduleTitle: "Getting Started"
sectionRef: "1.2"
ShowToc: true
---

## Executive Summary

PostgreSQL speaks standard SQL with rich types and operators. Master **SELECT** filtering, sorting, and limits before joins and aggregates.

---

## Core Concepts

| Clause | Purpose |
| :--- | :--- |
| `SELECT` | Project columns or expressions |
| `FROM` | Source table(s) |
| `WHERE` | Filter rows before grouping |
| `GROUP BY` | Aggregate buckets |
| `HAVING` | Filter groups |
| `ORDER BY` | Sort result |
| `LIMIT` / `OFFSET` | Paginate (prefer keyset pagination at scale) |

---

## Quick Reference

```sql
SELECT id, email, created_at
FROM users
WHERE status = 'active'
  AND created_at >= '2026-01-01'
ORDER BY created_at DESC
LIMIT 50;

SELECT DISTINCT country FROM customers;
SELECT count(*) FROM orders WHERE total > 100;
```

---

## Snippets

```sql
-- psql meta
\l          -- databases
\dt         -- tables
\d users    -- describe table
\x          -- expanded display
\timing on  -- query timing
```

---

## Common Gotchas

- `NULL` comparisons need `IS NULL` / `IS NOT NULL`, not `= NULL`.
- Double quotes = identifiers; single quotes = string literals.
- `SELECT *` is fine in psql; avoid in application code.

---

## Related Topics

- [Previous: Install](/postgresql-cheatsheet/installation/)
- [Next: Common SQL](/postgresql-cheatsheet/most-common-sql-commands/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
