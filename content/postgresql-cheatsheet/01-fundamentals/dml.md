---
title: "DML"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "INSERT, UPDATE, DELETE, UPSERT, and RETURNING patterns."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "DML"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.3"
weight: 103
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/dml/
---

## Quick Revision

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


## Interview Answers

## Question {#q-126}

How do you prevent SQL injection with parameterized queries in ORMs?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how do you prevent sql injection with parameterized queries in orms?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Security** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/01-fundamentals/dml/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: DDL](/postgresql-cheatsheet/01-fundamentals/ddl/)
- [Next: Joins](/postgresql-cheatsheet/01-fundamentals/joins/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
