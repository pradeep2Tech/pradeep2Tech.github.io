---
title: "Materialized Views"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "REFRESH, CONCURRENTLY, indexes on mat views, and staleness trade-offs."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Mat Views"
module: 6
moduleTitle: "Advanced SQL"
sectionRef: "6.2"
ShowToc: true
---

## Executive Summary

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

## Related Topics

- [Previous: Views](/postgresql-cheatsheet/views/)
- [Next: CTEs](/postgresql-cheatsheet/ctes/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
