---
title: "Joins"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "INNER, LEFT, LATERAL joins and top-N per group patterns."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Joins"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.4"
weight: 104
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/joins/
---

## Quick Revision

Joins combine rows from multiple relations. PostgreSQL optimizes join order; explicit join syntax beats comma-FROM for readability.

---

## Core Concepts

| Join | Keeps |
| :--- | :--- |
| `INNER JOIN` | Matching rows only |
| `LEFT JOIN` | All left + matches (NULLs on right miss) |
| `RIGHT JOIN` | Mirror of LEFT |
| `FULL OUTER` | All from both sides |
| `CROSS JOIN` | Cartesian product |
| `LATERAL` | Subquery per left row — great for top-N per group |

---

## Quick Reference

```sql
SELECT o.id, o.total, c.email
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id
WHERE o.status = 'paid';

SELECT c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.created_at > now() - interval '30 days';
```

---

## Snippets

```sql
-- Top 3 orders per customer (LATERAL)
SELECT c.id, recent.*
FROM customers c
CROSS JOIN LATERAL (
  SELECT id, total FROM orders
  WHERE customer_id = c.id
  ORDER BY created_at DESC LIMIT 3
) recent;
```

---

## Common Gotchas

- `LEFT JOIN ... WHERE right.col = x` filters NULLs — often becomes INNER join semantics.
- Join on indexed columns — avoid functions on join keys.
- `USING (id)` shorthand when column names match.

---

## See Also

- [Previous: DML](/postgresql-cheatsheet/01-fundamentals/dml/)
- [Next: CTEs](/postgresql-cheatsheet/01-fundamentals/ctes/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
