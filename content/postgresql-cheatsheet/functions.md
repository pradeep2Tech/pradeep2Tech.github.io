---
title: "Functions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "PL/pgSQL and SQL functions — parameters, volatility, and security."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Functions"
module: 7
moduleTitle: "Server-Side Programming"
sectionRef: "7.1"
ShowToc: true
---

## Executive Summary

User-defined functions encapsulate logic in the database. Mark **volatility** correctly — wrong labels break indexes and optimization.

---

## Core Concepts

| Volatility | Meaning |
| :--- | :--- |
| `IMMUTABLE` | Same in/out always — safe in indexes |
| `STABLE` | Same within one scan/statement |
| `VOLATILE` (default) | Can change anytime — side effects OK |

---

## Quick Reference

```sql
CREATE OR REPLACE FUNCTION full_name(first text, last text)
RETURNS text
LANGUAGE sql
IMMUTABLE
AS $$ SELECT first || ' ' || last $$;

SELECT full_name(first_name, last_name) FROM users;
```

---

## Snippets

```sql
CREATE OR REPLACE FUNCTION apply_discount(price numeric, pct numeric)
RETURNS numeric
LANGUAGE plpgsql
STABLE
AS $$
BEGIN
  IF pct < 0 OR pct > 100 THEN
    RAISE EXCEPTION 'invalid pct %', pct;
  END IF;
  RETURN round(price * (1 - pct/100), 2);
END;
$$;
```

---

## Common Gotchas

- `SECURITY DEFINER` runs as owner — tighten `search_path` to prevent hijacking.
- Prefer SQL functions when possible — inlinable.
- Heavy logic in DB vs app — team skill and deploy cadence matter.

---

## Related Topics

- [Previous: JSON](/postgresql-cheatsheet/json/)
- [Next: Triggers](/postgresql-cheatsheet/triggers/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
