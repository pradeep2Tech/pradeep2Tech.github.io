---
title: "Performance Tuning"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "work_mem, shared_buffers, connection pooling, and query tuning knobs."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Perf Tuning"
module: 3
moduleTitle: "Query Performance"
sectionRef: "3.3"
ShowToc: true
---

## Executive Summary

Tune at three layers: **query/SQL**, **indexes**, and **server config**. Measure with `pg_stat_statements`, `EXPLAIN (ANALYZE)`, and OS metrics before cranking knobs.

---

## Core Concepts

| Parameter | Starting guidance |
| :--- | :--- |
| `shared_buffers` | ~25% RAM (cap ~8GB on large boxes — test) |
| `effective_cache_size` | ~50–75% RAM — planner hint |
| `work_mem` | Per sort/hash operation — don't set globally huge |
| `maintenance_work_mem` | VACUUM, CREATE INDEX builds |
| `max_connections` | Prefer pooler (PgBouncer) over thousands |

---

## Quick Reference

```sql
-- Session knobs
SET work_mem = '64MB';  -- careful — per operation per query
SET random_page_cost = 1.1;  -- SSD/NVMe

-- Find slow queries (extension)
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC LIMIT 20;
```

---

## Snippets

```ini
# postgresql.conf snippets
shared_buffers = 4GB
effective_cache_size = 12GB
work_mem = 32MB
maintenance_work_mem = 1GB
wal_compression = on
```

---

## Common Gotchas

- Raising `max_connections` without a pooler increases memory and context switching.
- Connection pooling (transaction mode) is almost always required in microservices.
- Partition pruning and partial indexes often beat raw parameter tuning.

---

## Related Topics

- [Previous: EXPLAIN](/postgresql-cheatsheet/explain/)
- [Next: Transactions](/postgresql-cheatsheet/transactions/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
