---
title: "Stored Procedures"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "CREATE PROCEDURE, CALL, transactions inside."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Procedures"
module: 5
moduleTitle: "Advanced Features"
sectionRef: "5.2"
weight: 502
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/stored-procedures/
---

## Quick Revision

PostgreSQL **procedures** (PG 11+) support transactions inside the routine via `COMMIT`/`ROLLBACK` — unlike functions.

---

## Core Concepts

| Object | Returns | Transactions inside |
| :--- | :--- | :--- |
| **Function** | Value(s) | No — single txn |
| **Procedure** | Optional via OUT | Yes — `CALL` |

---

## Quick Reference

```sql
CREATE OR REPLACE PROCEDURE archive_old_orders(cutoff date)
LANGUAGE plpgsql
AS $$
BEGIN
  INSERT INTO orders_archive SELECT * FROM orders WHERE created_at < cutoff;
  DELETE FROM orders WHERE created_at < cutoff;
  COMMIT;
END;
$$;

CALL archive_old_orders('2024-01-01');
```

---

## Snippets

```sql
-- Function returns set
CREATE FUNCTION active_users()
RETURNS SETOF users
LANGUAGE sql STABLE
AS $$ SELECT * FROM users WHERE status = 'active'; $$;
```

---

## Common Gotchas

- Procedures called with `CALL`; functions in expressions.
- Prefer idempotent migration scripts over procedural DDL in prod.
- Test error paths — unhandled exceptions abort calling transaction.

---


## Interview Answers

## Question {#q-147}

How do stored procedures versus application transactions affect deploy agility?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how do stored procedures versus application transactions affect deploy agility?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/stored-procedures/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Functions](/postgresql-cheatsheet/05-advanced-features/functions/)
- [Next: Triggers](/postgresql-cheatsheet/05-advanced-features/triggers/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)