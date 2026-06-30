---
title: "DDL"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CREATE/ALTER/DROP — schemas, tables, constraints, and types."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "DDL"
module: 2
moduleTitle: "DDL & DML"
sectionRef: "2.1"
ShowToc: true
---

## Executive Summary

**DDL** defines structure: schemas, tables, constraints, indexes, and types. Changes are transactional in PostgreSQL.

---

## Core Concepts

| Statement | Use |
| :--- | :--- |
| `CREATE TABLE` | New relation with columns + constraints |
| `ALTER TABLE` | Add/drop column, constraint, rename |
| `CREATE INDEX` | Speed lookups (see Indexes) |
| `DROP` | Remove object — `CASCADE` drops dependents |
| `TRUNCATE` | Fast empty table — resets identity optionally |

---

## Quick Reference

```sql
CREATE SCHEMA IF NOT EXISTS billing;

CREATE TABLE billing.invoices (
  id          bigserial PRIMARY KEY,
  customer_id bigint NOT NULL REFERENCES customers(id),
  amount      numeric(12,2) NOT NULL CHECK (amount >= 0),
  status      text NOT NULL DEFAULT 'draft',
  issued_at   timestamptz NOT NULL DEFAULT now(),
  UNIQUE (customer_id, issued_at)
);

ALTER TABLE billing.invoices ADD COLUMN notes text;
ALTER TABLE billing.invoices RENAME COLUMN notes TO memo;
```

---

## Snippets

```sql
-- Common types
-- serial/bigserial, uuid, text, varchar(n), boolean, int, bigint,
-- numeric(p,s), real/double precision, date, time, timestamptz, jsonb

CREATE TYPE order_status AS ENUM ('pending', 'paid', 'shipped', 'cancelled');
```

---

## Common Gotchas

- `ALTER ... ADD COLUMN ... DEFAULT` may rewrite table on older PG — plan maintenance window.
- Use `IF NOT EXISTS` / `IF EXISTS` in migrations for idempotency.
- `DEFERRABLE` constraints allow batch loads within a transaction.

---

## Related Topics

- [Previous: Common SQL](/postgresql-cheatsheet/most-common-sql-commands/)
- [Next: DML](/postgresql-cheatsheet/dml/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
