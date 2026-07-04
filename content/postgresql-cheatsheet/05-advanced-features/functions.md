---
title: "Functions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "PL/pgSQL and SQL functions — volatility, security."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Functions"
module: 5
moduleTitle: "Advanced Features"
sectionRef: "5.1"
weight: 501
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/functions/
---

## Quick Revision

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


## Interview Answers

## Question {#q-118}

What risks does SECURITY DEFINER without locked search_path create?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: what risks does security definer without locked search_path create?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Security** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/functions/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: DR](/postgresql-cheatsheet/04-high-availability/disaster-recovery/)
- [Next: Procedures](/postgresql-cheatsheet/05-advanced-features/stored-procedures/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
