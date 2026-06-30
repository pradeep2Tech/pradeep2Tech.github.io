---
title: "Stored Procedures"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CREATE PROCEDURE, CALL, transactions inside procedures (PG 11+)."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Procedures"
module: 7
moduleTitle: "Server-Side Programming"
sectionRef: "7.3"
ShowToc: true
---

## Executive Summary

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

## Related Topics

- [Previous: Triggers](/postgresql-cheatsheet/triggers/)
- [Next: VACUUM](/postgresql-cheatsheet/vacuum/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
