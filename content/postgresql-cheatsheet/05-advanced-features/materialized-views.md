---
title: "Materialized Views"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "REFRESH, CONCURRENTLY, staleness trade-offs."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Mat Views"
module: 5
moduleTitle: "Advanced Features"
sectionRef: "5.4"
weight: 504
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/materialized-views/
---

## Quick Revision

Materialized views **cache** query results on disk. Refresh synchronously or **CONCURRENTLY** (requires unique index).

---

## Core Concepts

| Command | Blocks reads? |
| :--- | :--- |
| `REFRESH MATERIALIZED VIEW` | Yes — exclusive lock |
| `REFRESH ... CONCURRENTLY` | No — needs UNIQUE index |

---

## Quick Reference

```sql
CREATE MATERIALIZED VIEW daily_revenue AS
SELECT date_trunc('day', created_at) AS day, sum(total) AS revenue
FROM orders
GROUP BY 1;

CREATE UNIQUE INDEX ON daily_revenue (day);

REFRESH MATERIALIZED VIEW CONCURRENTLY daily_revenue;
```

---

## Snippets

```sql
-- Staleness acceptable? Schedule via pg_cron or external job
-- For real-time dashboards prefer regular view + proper indexes
```

---

## Common Gotchas

- CONCURRENTLY refresh can fail if unique constraint violated mid-refresh.
- Mat views don't auto-update — plan refresh cadence vs freshness SLA.
- Large refreshes: consider incremental patterns or summary tables.

---


## Interview Answers

## Question {#q-91}

How do materialized views trade freshness for read performance?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how do materialized views trade freshness for read performance?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/materialized-views/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-92}

When should REFRESH MATERIALIZED VIEW CONCURRENTLY be avoided?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: when should refresh materialized view concurrently be avoided?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/05-advanced-features/materialized-views/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Triggers](/postgresql-cheatsheet/05-advanced-features/triggers/)
- [Next: JSON](/postgresql-cheatsheet/05-advanced-features/json/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
