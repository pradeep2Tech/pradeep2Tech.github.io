---
title: "Most Common SQL Commands"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Day-to-day PostgreSQL commands — CRUD, meta-queries, and session helpers."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Common SQL"
module: 1
moduleTitle: "Getting Started"
sectionRef: "1.3"
ShowToc: true
---

## Executive Summary

A single-page recap of commands you reach for daily — CRUD, catalog queries, and session management.

---

## Core Concepts

| Task | Command |
| :--- | :--- |
| List tables | `\dt` or `SELECT * FROM pg_tables WHERE schemaname = 'public';` |
| Table size | `pg_total_relation_size('tablename')` |
| Active queries | `pg_stat_activity` |
| Kill query | `SELECT pg_cancel_backend(pid);` or `pg_terminate_backend(pid)` |
| Current user/db | `SELECT current_user, current_database();` |

---

## Quick Reference

```sql
-- CRUD
INSERT INTO products (sku, name, price) VALUES ('A1', 'Widget', 9.99);
UPDATE products SET price = 10.99 WHERE sku = 'A1';
DELETE FROM products WHERE sku = 'A1';

-- Upsert (see DML page)
INSERT INTO products (sku, name, price) VALUES ('A1', 'Widget', 9.99)
ON CONFLICT (sku) DO UPDATE SET name = EXCLUDED.name, price = EXCLUDED.price;

-- Grants
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
```

---

## Snippets

```sql
-- Find duplicate keys
SELECT email, count(*) FROM users GROUP BY email HAVING count(*) > 1;

-- Explain last query cost
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM orders WHERE user_id = 42;
```

---

## Common Gotchas

- Use `RETURNING` on INSERT/UPDATE/DELETE to avoid a second round-trip.
- `TRUNCATE` is DDL-fast but cannot be rolled back in some cases — locks table.
- Prefer parameterized queries from apps — never string-concat SQL.

---

## Related Topics

- [Previous: SQL Basics](/postgresql-cheatsheet/sql-basics/)
- [Next: DDL](/postgresql-cheatsheet/ddl/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
