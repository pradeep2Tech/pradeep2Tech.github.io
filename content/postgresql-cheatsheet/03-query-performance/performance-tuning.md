---
title: "Performance Tuning"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "shared_buffers, work_mem, and server config knobs."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Perf Tuning"
module: 3
moduleTitle: "Query Performance"
sectionRef: "3.4"
weight: 304
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/performance-tuning/
---

## Quick Revision

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

-- Slow query workload analysis → [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)
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

- Raising `max_connections` without a pooler increases memory and context switching — size pools in [Capacity Planning](/postgresql-cheatsheet/06-production-operations/capacity-planning/).
- Connection pooling is almost always required in microservices — see [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/).
- Partition pruning and partial indexes often beat raw parameter tuning.

---


## Interview Answers

## Question {#q-80}

How should work_mem be sized given concurrent connections?

### Short Answer

On NVMe OLTP, start with **`shared_buffers`** (~25% RAM, benchmark), conservative global **`work_mem`**, and **`random_page_cost`** ≈ 1.1–1.5 so the planner favors index scans.

### Detailed Explanation

`shared_buffers` caches pages in PostgreSQL; `effective_cache_size` hints OS cache to the planner. `work_mem` caps per-sort/hash memory — multiply by concurrent operations, not just connections. On SSD/NVMe, lower `random_page_cost` from default 4.0 so index access looks cheaper versus seq scan.

### Production Notes

Change one knob at a time; capture pg_stat_statements baseline before/after.

### Common Mistakes

Setting work_mem globally to 256MB with 500 concurrent queries — risk OOM.

### Follow-up Questions

- Why is effective_cache_size not allocated memory?
- When does parallel query help?

---

## Question {#q-81}

What is the tradeoff of raising shared_buffers on a 128 GB host?

### Short Answer

Tune queries and indexes before global GUC knobs. This directly answers: what is the tradeoff of raising shared_buffers on a 128 gb host?

### Detailed Explanation

work_mem is per operation — multiply by concurrent queries. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/performance-tuning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-82}

Why set random_page_cost lower on NVMe-backed instances?

### Short Answer

Tune queries and indexes before global GUC knobs. This directly answers: why set random_page_cost lower on nvme-backed instances?

### Detailed Explanation

work_mem is per operation — multiply by concurrent queries. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/performance-tuning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-89}

How would you benchmark a configuration change without production risk?

### Short Answer

Tune queries and indexes before global GUC knobs. This directly answers: how would you benchmark a configuration change without production risk?

### Detailed Explanation

work_mem is per operation — multiply by concurrent queries. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/performance-tuning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Optimizer](/postgresql-cheatsheet/03-query-performance/query-optimization/)
- [Next: Partitioning](/postgresql-cheatsheet/03-query-performance/partitioning/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)