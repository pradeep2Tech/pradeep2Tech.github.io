---
title: "Views"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CREATE VIEW, updatable views, security_barrier, and dependencies."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Views"
module: 6
moduleTitle: "Advanced SQL"
sectionRef: "6.1"
ShowToc: true
---

## Executive Summary

Views store a query definition — no data duplication. **Updatable views** need simple single-table rules or `INSTEAD OF` triggers.

---

## Core Concepts

| Feature | Notes |
| :--- | :--- |
| `CREATE VIEW` | Named saved query |
| `CREATE OR REPLACE VIEW` | Swap definition |
| `security_barrier` | Row-level security helper |
| Updatable | Simple views — one base table, no aggregates |

---

## Quick Reference

```sql
CREATE VIEW active_customers AS
SELECT id, email, name
FROM customers
WHERE status = 'active';

CREATE OR REPLACE VIEW order_summary AS
SELECT customer_id, count(*) AS order_count, sum(total) AS revenue
FROM orders
GROUP BY customer_id;
```

---

## Snippets

```sql
-- Check if updatable
SELECT table_name, is_insertable_into
FROM information_schema.views
WHERE table_schema = 'public';
```

---

## Common Gotchas

- Complex views with joins/aggregates are read-only unless triggers added.
- `WITH CHECK OPTION` enforces inserts/updates match view predicate.
- Views hide columns — not a security boundary without RLS/grants.

---

## Related Topics

- [Previous: Replication](/postgresql-cheatsheet/replication/)
- [Next: Mat Views](/postgresql-cheatsheet/materialized-views/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
