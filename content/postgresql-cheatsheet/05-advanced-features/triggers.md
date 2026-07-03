---
title: "Triggers"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "BEFORE/AFTER, ROW/STATEMENT triggers."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Triggers"
module: 5
moduleTitle: "Advanced Features"
sectionRef: "5.3"
weight: 503
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/triggers/
---

## Quick Revision

Triggers run functions automatically on DML events. Use for audit, denormalization, and enforcement — avoid hiding business logic that belongs in services.

---

## Core Concepts

| Timing | Level |
| :--- | :--- |
| `BEFORE` / `AFTER` | `ROW` or `STATEMENT` |
| `INSERT` / `UPDATE` / `DELETE` | Combine in one trigger or split |
| `WHEN (condition)` | Filter fired rows |

---

## Quick Reference

```sql
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  NEW.updated_at := now();
  RETURN NEW;
END;
$$;

CREATE TRIGGER trg_users_updated
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION set_updated_at();
```

---

## Snippets

```sql
-- Audit trigger sketch
CREATE TABLE users_audit (LIKE users);
CREATE TRIGGER trg_users_audit
AFTER UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION audit_row();
```

---

## Common Gotchas

- `BEFORE` triggers can modify `NEW`; `AFTER` cannot.
- Statement-level triggers see no `NEW`/`OLD` row variables.
- Triggers add latency and complicate bulk loads — disable for migrations if needed.

---


## Interview Answers

## Question {#q-121}

What audit options exist for DDL and DML in regulated environments?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: what audit options exist for ddl and dml in regulated environments?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Security** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/triggers/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-148}

When should business logic live in triggers versus application services?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: when should business logic live in triggers versus application services?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/triggers/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Procedures](/postgresql-cheatsheet/05-advanced-features/stored-procedures/)
- [Next: Mat Views](/postgresql-cheatsheet/05-advanced-features/materialized-views/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)