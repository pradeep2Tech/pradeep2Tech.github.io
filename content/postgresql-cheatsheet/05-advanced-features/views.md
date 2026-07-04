---
title: "Views"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "CREATE VIEW, updatable views, security_barrier."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Views"
module: 5
moduleTitle: "Advanced Features"
sectionRef: "5.6"
weight: 506
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/views/
---

## Quick Revision

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


## Interview Answers

## Question {#q-119}

How do row-level security policies complement GRANT?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how do row-level security policies complement grant?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Security** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/views/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: JSON](/postgresql-cheatsheet/05-advanced-features/json/)
- [Next: VACUUM](/postgresql-cheatsheet/06-production-operations/vacuum/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
