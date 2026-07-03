---
title: "Window Functions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "ROW_NUMBER, LAG/LEAD, PARTITION BY, frame clauses."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Windows"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.6"
weight: 106
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/window-functions/
---

## Quick Revision

Window functions compute over a **partition** without collapsing rows like `GROUP BY`. Essential for rankings, running totals, and LAG/LEAD analytics.

---

## Core Concepts

| Function | Purpose |
| :--- | :--- |
| `ROW_NUMBER()` | Unique rank 1..n |
| `RANK()` / `DENSE_RANK()` | Ties handled differently |
| `LAG` / `LEAD` | Previous/next row in partition |
| `SUM() OVER` | Running total |
| `NTILE(n)` | Bucket into n groups |

---

## Quick Reference

```sql
SELECT
  employee_id,
  department,
  salary,
  ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn,
  AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;
```

---

## Snippets

```sql
-- Running total
SELECT order_date, amount,
  SUM(amount) OVER (ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM daily_sales;

-- Dedupe keep latest
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY updated_at DESC) rn
  FROM users
) t WHERE rn = 1;
```

---

## Common Gotchas

- Frame clause defaults differ: `RANGE` vs `ROWS` — off-by-one bugs are common.
- Window functions run after `WHERE` but before final `ORDER BY` in SELECT.
- Index on `(partition_cols, order_cols)` helps only if planner uses sort optimization.

---

## See Also

- [Previous: CTEs](/postgresql-cheatsheet/01-fundamentals/ctes/)
- [Next: Install](/postgresql-cheatsheet/01-fundamentals/installation/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)