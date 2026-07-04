---
title: "Capacity Planning"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "CPU, memory, connection, and storage sizing with growth estimation."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Capacity"
module: 6
moduleTitle: "Production Operations"
sectionRef: "6.5"
weight: 605
interviewHandbook: true
---

## Quick Revision

- **CPU**: active queries + parallel workers + autovacuum.
- **RAM**: `shared_buffers` + `work_mem` × concurrent sorts + OS cache.
- **Connections**: apps × pool size ≤ `max_connections`.
- **Storage**: data + indexes + WAL + bloat headroom + retention.

## Core Concepts

| Resource | Heuristic starting point |
| :--- | :--- |
| `shared_buffers` | 25% RAM (benchmark on large hosts) |
| `effective_cache_size` | 50–75% RAM (planner hint) |
| `work_mem` | Conservative global; raise per-role/session for reports |
| WAL disk | Sustained write MB/s × retention window |
| Replicas | +read CPU; replay can lag on CPU-bound replicas |

## Scalability

- Partition before single-table maintenance becomes painful.
- Read replicas scale reads, not writes — [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/) for write scale-out.


## Interview Answers

## Question {#q-90}

What OS-level tuning complements PostgreSQL on Linux for OLTP?

### Short Answer

Size CPU, RAM, connections, and WAL disk from measured peaks. This directly answers: what os-level tuning complements postgresql on linux for oltp?

### Detailed Explanation

Leave headroom for autovacuum and replication replay. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/capacity-planning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-95}

How do you capacity-plan WAL disk throughput for peak write bursts?

### Short Answer

Size CPU, RAM, connections, and WAL disk from measured peaks. This directly answers: how do you capacity-plan wal disk throughput for peak write bursts?

### Detailed Explanation

Leave headroom for autovacuum and replication replay. For **Performance** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/capacity-planning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-146}

What capacity triggers prompt adding a new replica versus partition pruning tuning?

### Short Answer

Size CPU, RAM, connections, and WAL disk from measured peaks. This directly answers: what capacity triggers prompt adding a new replica versus partition pruning tuning?

### Detailed Explanation

Leave headroom for autovacuum and replication replay. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/capacity-planning/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/)
- [Next: vs MySQL](/postgresql-cheatsheet/07-comparisons/postgresql-vs-mysql/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
