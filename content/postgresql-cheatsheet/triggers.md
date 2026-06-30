---
title: "Triggers"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "BEFORE/AFTER, ROW/STATEMENT, NEW/OLD, and WHEN clauses."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Triggers"
module: 7
moduleTitle: "Server-Side Programming"
sectionRef: "7.2"
ShowToc: true
---

## Executive Summary

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

## Related Topics

- [Previous: Functions](/postgresql-cheatsheet/functions/)
- [Next: Procedures](/postgresql-cheatsheet/stored-procedures/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
