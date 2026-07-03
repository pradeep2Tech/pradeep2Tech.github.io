---
title: "DDL"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "CREATE/ALTER/DROP — schemas, tables, constraints, and types."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "DDL"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.2"
weight: 102
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/ddl/
---

## Quick Revision

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


## Interview Answers

## Question {#q-120}

How should application roles be scoped for least privilege?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how should application roles be scoped for least privilege?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Security** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/01-fundamentals/ddl/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-141}

How do you design schema migrations for zero-downtime deploys?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how do you design schema migrations for zero-downtime deploys?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/01-fundamentals/ddl/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: SQL Basics](/postgresql-cheatsheet/01-fundamentals/sql-basics/)
- [Next: DML](/postgresql-cheatsheet/01-fundamentals/dml/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)