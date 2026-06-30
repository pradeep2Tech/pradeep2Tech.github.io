---
title: "CTEs"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "WITH, recursive CTEs, MATERIALIZED hint, and readability vs optimization."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "CTEs"
module: 6
moduleTitle: "Advanced SQL"
sectionRef: "6.3"
ShowToc: true
---

## Executive Summary

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

## Related Topics

- [Previous: Mat Views](/postgresql-cheatsheet/materialized-views/)
- [Next: Windows](/postgresql-cheatsheet/window-functions/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
