---
title: "CTEs"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "WITH, recursive CTEs, MATERIALIZED hints."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "CTEs"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.5"
weight: 105
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/ctes/
---

## Quick Revision

**Common Table Expressions** (`WITH`) improve readability and support recursion. PostgreSQL 12+ inlines non-recursive CTEs by default — use `MATERIALIZED` to force optimization barrier when needed.

---

## Core Concepts

| Form | Use |
| :--- | :--- |
| Simple CTE | Named subquery upfront |
| Recursive | Graphs, hierarchies, bill of materials |
| `MATERIALIZED` | Force materialization (PG 12+) |
| `NOT MATERIALIZED` | Hint inline (PG 12+) |

---

## Quick Reference

```sql
WITH regional_sales AS (
  SELECT region, sum(amount) AS total FROM sales GROUP BY region
),
top_regions AS (
  SELECT region FROM regional_sales WHERE total > 1000000
)
SELECT * FROM customers WHERE region IN (SELECT region FROM top_regions);
```

---

## Snippets

```sql
-- Recursive org chart
WITH RECURSIVE org AS (
  SELECT id, name, manager_id, 1 AS depth
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, org.depth + 1
  FROM employees e JOIN org ON e.manager_id = org.id
)
SELECT * FROM org ORDER BY depth, name;
```

---

## Common Gotchas

- Recursive CTE needs `UNION` (not `UNION ALL`) for cycle safety unless you track visited.
- Overusing CTEs where a subquery suffices can confuse planner — verify with EXPLAIN.
- `WITH ... INSERT` enables writable CTE pipelines.

---


## Interview Answers

## Question {#q-84}

What CTE materialization hints affect planner inlining in PostgreSQL 12+?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: what cte materialization hints affect planner inlining in postgresql 12+?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/01-fundamentals/ctes/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Joins](/postgresql-cheatsheet/01-fundamentals/joins/)
- [Next: Windows](/postgresql-cheatsheet/01-fundamentals/window-functions/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
