---
title: "Sharding"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Citus, FDW, and application-level sharding."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Sharding"
module: 3
moduleTitle: "Query Performance"
sectionRef: "3.6"
weight: 306
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/sharding/
---

## Quick Revision

PostgreSQL single-node scales vertically; **sharding** spreads data across nodes. Options: **Citus**, **FDW**, or app-level routing.

---

## Core Concepts

| Approach | Trade-off |
| :--- | :--- |
| **Citus** | Native distributed PG — colocation, rebalance |
| **Foreign Data Wrapper** | Federated queries — not true shard autonomy |
| **App routing** | Full control — you own cross-shard queries |
| **Read replicas** | Scale reads, not writes — not sharding |

---

## Quick Reference

```sql
-- Citus (extension) sketch
SELECT create_distributed_table('events', 'tenant_id');

-- postgres_fdw
CREATE EXTENSION postgres_fdw;
CREATE SERVER shard1 FOREIGN DATA WRAPPER postgres_fdw
  OPTIONS (host 'shard1.internal', dbname 'app');
```

---

## Snippets

```sql
-- App-level: tenant_id in every query + connection per shard
-- Avoid cross-shard JOINs in hot paths — aggregate in app or OLAP layer
```

---

## Common Gotchas

- Choose shard key early — resharding is painful.
- Co-locate related tables on same shard (Citus `colocate_with`).
- Global sequences and FK across shards need application patterns.

---


## Interview Answers

## Question {#q-30}

When would you choose Citus over native partitioning?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: when would you choose citus over native partitioning?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/sharding/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-134}

What workload signals push you toward sharding versus bigger vertical hardware?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: what workload signals push you toward sharding versus bigger vertical hardware?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/sharding/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-138}

When is foreign data wrapper federation acceptable versus ETL?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: when is foreign data wrapper federation acceptable versus etl?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/sharding/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-139}

How does Citus colocation affect multi-tenant schema design?

### Short Answer

PostgreSQL separates client backends from background workers under postmaster. This directly answers: how does citus colocation affect multi-tenant schema design?

### Detailed Explanation

Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/03-query-performance/sharding/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Partitioning](/postgresql-cheatsheet/03-query-performance/partitioning/)
- [Next: Replication](/postgresql-cheatsheet/04-high-availability/replication/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)