---
title: "Partitioning"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Declarative RANGE, LIST, HASH partitioning."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Partitioning"
module: 3
moduleTitle: "Query Performance"
sectionRef: "3.5"
weight: 305
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/partitioning/
---

## Quick Revision

**Declarative partitioning** splits one logical table into physical children. Pruning skips irrelevant partitions at plan time.

---

## Core Concepts

| Method | Key |
| :--- | :--- |
| **RANGE** | Dates, numeric ranges |
| **LIST** | Discrete values (region, status) |
| **HASH** | Even spread when no natural key |

---

## Quick Reference

```sql
CREATE TABLE measurements (
  id bigserial,
  device_id int NOT NULL,
  recorded_at timestamptz NOT NULL,
  value double precision
) PARTITION BY RANGE (recorded_at);

CREATE TABLE measurements_2026_01 PARTITION OF measurements
  FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');

CREATE INDEX ON measurements (device_id, recorded_at);
```

---

## Snippets

```sql
-- Attach existing table as partition
CREATE TABLE measurements_old (LIKE measurements INCLUDING ALL);
ALTER TABLE measurements ATTACH PARTITION measurements_old
  FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

---

## Common Gotchas

- Partition key must appear in PK/unique constraints (include partition key).
- Create future partitions before data arrives — or use `DEFAULT` partition.
- Global uniqueness across partitions requires careful constraint design.

---


## Interview Answers

## Question {#q-28}

How does declarative partitioning change planner behavior via partition pruning?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how does declarative partitioning change planner behavior via partition pruning?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/partitioning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-29}

What constraints apply to primary keys on partitioned tables?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: what constraints apply to primary keys on partitioned tables?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/partitioning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-85}

How does partition pruning fail when queries omit partition key predicates?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how does partition pruning fail when queries omit partition key predicates?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/partitioning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Perf Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/)
- [Next: Sharding](/postgresql-cheatsheet/03-query-performance/sharding/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)