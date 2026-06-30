---
title: "DML"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "INSERT, UPDATE, DELETE, UPSERT, and RETURNING patterns."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "DML"
module: 2
moduleTitle: "DDL & DML"
sectionRef: "2.2"
ShowToc: true
---

## Executive Summary

**DML** mutates rows: INSERT, UPDATE, DELETE. PostgreSQL supports powerful `RETURNING` and `ON CONFLICT` upserts.

---

## Core Concepts

| Statement | Notes |
| :--- | :--- |
| `INSERT` | Single/multi-row; `DEFAULT` for omitted columns |
| `UPDATE` | Always add `WHERE` unless intentional full-table update |
| `DELETE` | Same — missing `WHERE` deletes all rows |
| `ON CONFLICT` | Upsert — requires unique index/constraint |
| `RETURNING` | Return inserted/updated rows to client |

---

## Quick Reference

```sql
INSERT INTO events (user_id, kind, payload)
VALUES (1, 'login', '{"ip":"10.0.0.1"}'::jsonb)
RETURNING id, created_at;

UPDATE accounts SET balance = balance - 100
WHERE id = 5 AND balance >= 100
RETURNING balance;

DELETE FROM sessions WHERE expires_at < now() RETURNING id;
```

---

## Snippets

```sql
-- Upsert
INSERT INTO inventory (sku, qty)
VALUES ('X', 10)
ON CONFLICT (sku) DO UPDATE
  SET qty = inventory.qty + EXCLUDED.qty;

-- Bulk insert from SELECT
INSERT INTO archive_orders SELECT * FROM orders WHERE created_at < '2024-01-01';
```

---

## Common Gotchas

- `ON CONFLICT DO NOTHING` silently skips — log or count if you need visibility.
- Large updates: batch by primary key range to reduce lock duration.
- `COPY` beats INSERT for bulk loads — see Backup page for `COPY` format.

---

## Related Topics

- [Previous: DDL](/postgresql-cheatsheet/ddl/)
- [Next: Joins](/postgresql-cheatsheet/joins/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
