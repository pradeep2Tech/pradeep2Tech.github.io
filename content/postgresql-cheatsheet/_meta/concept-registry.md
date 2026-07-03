---
title: "PostgreSQL Concept Registry"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per PostgreSQL concept."
tags: ["postgresql-cheatsheet", "meta", "planning"]
---

# PostgreSQL Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase A — registry defined; enforcement in Phase B/C.

**Path prefix:** `content/postgresql-cheatsheet/` (shown as module paths below).

---

## 01 Fundamentals

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| SELECT / WHERE / ORDER BY | `01-fundamentals/sql-basics.md` | Exists | Syntax only — not interview depth |
| psql meta-commands | `01-fundamentals/sql-basics.md` | Exists | Ops commands → link `monitoring.md` |
| DDL (CREATE/ALTER/DROP) | `01-fundamentals/ddl.md` | Exists | |
| DML (INSERT/UPDATE/DELETE) | `01-fundamentals/dml.md` | Exists | |
| UPSERT (`ON CONFLICT`) | `01-fundamentals/dml.md` | Exists | |
| `RETURNING` clause | `01-fundamentals/dml.md` | Exists | |
| Join types | `01-fundamentals/joins.md` | Exists | |
| LATERAL join | `01-fundamentals/joins.md` | Exists | |
| CTE (`WITH`) | `01-fundamentals/ctes.md` | Exists | |
| Recursive CTE | `01-fundamentals/ctes.md` | Exists | |
| CTE materialization hints | `01-fundamentals/ctes.md` | Exists | Planner interaction → `query-optimization.md` |
| Window functions | `01-fundamentals/window-functions.md` | Exists | Extension beyond target tree |
| SQL installation / bootstrap | `01-fundamentals/installation.md` | Exists | Demote or appendix in Phase B |

---

## 02 Core PostgreSQL

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| PostgreSQL architecture (processes) | `02-core-postgresql/architecture.md` | **Planned** | postmaster, backends, bgwriter, walwriter |
| Shared memory / buffer pool | `02-core-postgresql/architecture.md` | **Planned** | Cross-link `storage-engine.md` |
| Heap storage | `02-core-postgresql/storage-engine.md` | **Planned** | |
| Page layout (8 KB pages) | `02-core-postgresql/storage-engine.md` | **Planned** | |
| Tuple header / row layout | `02-core-postgresql/storage-engine.md` | **Planned** | |
| TOAST | `02-core-postgresql/storage-engine.md` | **Planned** | |
| FSM (Free Space Map) | `02-core-postgresql/storage-engine.md` | **Planned** | |
| Visibility Map | `02-core-postgresql/storage-engine.md` | **Planned** | Index-only scans |
| Buffer cache / shared_buffers | `02-core-postgresql/storage-engine.md` | **Planned** | Tuning → `performance-tuning.md` |
| WAL (Write-Ahead Log) | `02-core-postgresql/wal.md` | **Planned** | |
| WAL segments / LSN | `02-core-postgresql/wal.md` | **Planned** | |
| Checkpoints | `02-core-postgresql/wal.md` | **Planned** | |
| Crash recovery | `02-core-postgresql/wal.md` | **Planned** | |
| WAL archiving foundation | `02-core-postgresql/wal.md` | **Planned** | DR → `disaster-recovery.md` |
| MVCC | `02-core-postgresql/mvcc.md` | Exists | **Primary** MVCC source |
| xmin / xmax | `02-core-postgresql/mvcc.md` | Exists | |
| Transaction snapshots | `02-core-postgresql/mvcc.md` | Exists | |
| Tuple visibility rules | `02-core-postgresql/mvcc.md` | Exists | Generic theory → db-handbook link |
| HOT updates | `02-core-postgresql/storage-engine.md` | **Planned** | Mention in mvcc ≤2 sentences |
| Transactions (BEGIN/COMMIT) | `02-core-postgresql/transactions.md` | Exists | |
| SAVEPOINT | `02-core-postgresql/transactions.md` | Exists | |
| ACID properties | `02-core-postgresql/transactions.md` | Exists | |
| Isolation levels | `02-core-postgresql/isolation-levels.md` | Exists | **Primary** isolation source |
| READ COMMITTED | `02-core-postgresql/isolation-levels.md` | Exists | |
| REPEATABLE READ (snapshot) | `02-core-postgresql/isolation-levels.md` | Exists | |
| SERIALIZABLE (SSI) | `02-core-postgresql/isolation-levels.md` | Exists | Expand in Phase C |
| Row-level locks | `02-core-postgresql/locks.md` | Exists | |
| Table-level locks | `02-core-postgresql/locks.md` | Exists | |
| Advisory locks | `02-core-postgresql/locks.md` | Exists | |
| `FOR UPDATE` / `FOR SHARE` | `02-core-postgresql/locks.md` | Exists | |
| `SKIP LOCKED` / `NOWAIT` | `02-core-postgresql/locks.md` | Exists | |
| Deadlocks | `02-core-postgresql/locks.md` | Exists | Runbooks → `troubleshooting.md` |
| DDL lock modes | `02-core-postgresql/locks.md` | Exists | |

---

## 03 Query Performance

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| B-tree index | `03-query-performance/indexes.md` | Exists | |
| Hash / GIN / GiST / BRIN | `03-query-performance/indexes.md` | Exists | |
| Partial index | `03-query-performance/indexes.md` | Exists | |
| Covering index (`INCLUDE`) | `03-query-performance/indexes.md` | Exists | |
| Index-only scan | `03-query-performance/indexes.md` | Exists | Requires visibility map |
| Index maintenance (`REINDEX`) | `03-query-performance/indexes.md` | Exists | |
| EXPLAIN output | `03-query-performance/explain.md` | Exists | **Primary** plan reading |
| EXPLAIN (ANALYZE, BUFFERS) | `03-query-performance/explain.md` | Exists | |
| Plan node types (Seq/Index/Bitmap/Join) | `03-query-performance/explain.md` | Exists | |
| Query planner | `03-query-performance/query-optimization.md` | **Planned** | |
| Cost estimation | `03-query-performance/query-optimization.md` | **Planned** | |
| Statistics (`pg_statistic`) | `03-query-performance/query-optimization.md` | **Planned** | |
| ANALYZE (statistics) | `03-query-performance/query-optimization.md` | **Planned** | Vacuum page links here |
| Cardinality estimation | `03-query-performance/query-optimization.md` | **Planned** | |
| Join order / join algorithms | `03-query-performance/query-optimization.md` | **Planned** | |
| Parallel query | `03-query-performance/query-optimization.md` | **Planned** | |
| `work_mem` / sort spill | `03-query-performance/performance-tuning.md` | Exists | |
| `shared_buffers` | `03-query-performance/performance-tuning.md` | Exists | |
| `effective_cache_size` | `03-query-performance/performance-tuning.md` | Exists | |
| `random_page_cost` / SSD tuning | `03-query-performance/performance-tuning.md` | Exists | |
| Declarative partitioning | `03-query-performance/partitioning.md` | Exists | |
| Partition pruning | `03-query-performance/partitioning.md` | Exists | |
| Sharding (Citus / FDW / app) | `03-query-performance/sharding.md` | Exists | Beyond single-node |

---

## 04 High Availability

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Streaming (physical) replication | `04-high-availability/replication.md` | Exists | **Primary** replication |
| Logical replication | `04-high-availability/replication.md` | Exists | |
| Replication slots | `04-high-availability/replication.md` | Exists | |
| Synchronous replication | `04-high-availability/replication.md` | Exists | Expand; failover links |
| `pg_basebackup` | `04-high-availability/replication.md` | Exists | WAL detail → `wal.md` |
| Failover / promotion | `04-high-availability/failover.md` | **Planned** | |
| Patroni / HA orchestration | `04-high-availability/failover.md` | **Planned** | |
| HA architecture patterns | `04-high-availability/failover.md` | **Planned** | |
| `pg_dump` / logical backup | `04-high-availability/backup-restore.md` | Exists | |
| Physical backup | `04-high-availability/backup-restore.md` | Exists | |
| PITR | `04-high-availability/disaster-recovery.md` | **Planned** | |
| WAL recovery | `04-high-availability/disaster-recovery.md` | **Planned** | |
| RPO / RTO | `04-high-availability/disaster-recovery.md` | **Planned** | |
| Backup strategy (3-2-1) | `04-high-availability/disaster-recovery.md` | **Planned** | |

---

## 05 Advanced Features

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| SQL / PL/pgSQL functions | `05-advanced-features/functions.md` | Exists | |
| Function volatility | `05-advanced-features/functions.md` | Exists | |
| `SECURITY DEFINER` | `05-advanced-features/functions.md` | Exists | |
| Stored procedures (`CALL`) | `05-advanced-features/stored-procedures.md` | Exists | |
| Triggers | `05-advanced-features/triggers.md` | Exists | |
| Views | `05-advanced-features/views.md` | Exists | Merge or keep |
| Materialized views | `05-advanced-features/materialized-views.md` | Exists | |
| `REFRESH CONCURRENTLY` | `05-advanced-features/materialized-views.md` | Exists | |
| json vs jsonb | `05-advanced-features/json.md` | Exists | |
| JSON operators | `05-advanced-features/json.md` | Exists | |
| JSON indexing | `03-query-performance/indexes.md` | Exists | json page links only |

---

## 06 Production Operations

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| VACUUM | `06-production-operations/vacuum.md` | Exists | **Primary** vacuum source |
| Autovacuum | `06-production-operations/vacuum.md` | Exists | |
| Transaction ID freeze / wraparound | `06-production-operations/vacuum.md` | Exists | |
| Table bloat | `06-production-operations/vacuum.md` | Exists | Triage → `troubleshooting.md` |
| `VACUUM FULL` vs `pg_repack` | `06-production-operations/vacuum.md` | Exists | |
| `pg_stat_activity` | `06-production-operations/monitoring.md` | **Planned** | |
| `pg_stat_statements` | `06-production-operations/monitoring.md` | **Planned** | |
| `pg_locks` | `06-production-operations/monitoring.md` | **Planned** | |
| Wait events | `06-production-operations/monitoring.md` | **Planned** | |
| Slow query analysis | `06-production-operations/monitoring.md` | **Planned** | |
| PgBouncer | `06-production-operations/connection-pooling.md` | **Planned** | |
| Connection limits | `06-production-operations/connection-pooling.md` | **Planned** | |
| Pool sizing | `06-production-operations/connection-pooling.md` | **Planned** | |
| Transaction vs session pooling | `06-production-operations/connection-pooling.md` | **Planned** | |
| CPU sizing | `06-production-operations/capacity-planning.md` | **Planned** | |
| Memory sizing | `06-production-operations/capacity-planning.md` | **Planned** | |
| Storage / WAL disk planning | `06-production-operations/capacity-planning.md` | **Planned** | |
| Growth estimation | `06-production-operations/capacity-planning.md` | **Planned** | |
| Blocking sessions runbook | `06-production-operations/troubleshooting.md` | **Planned** | |
| Replication lag triage | `06-production-operations/troubleshooting.md` | **Planned** | |
| Autovacuum failure triage | `06-production-operations/troubleshooting.md` | **Planned** | |
| Connection exhaustion triage | `06-production-operations/troubleshooting.md` | **Planned** | |

---

## 07 Comparisons

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| PostgreSQL vs MySQL | `07-comparisons/postgresql-vs-mysql.md` | **Planned** | ADR — not feature dump |
| PostgreSQL vs Oracle | `07-comparisons/postgresql-vs-oracle.md` | **Planned** | Link db-handbook migration |
| PostgreSQL vs MongoDB | `07-comparisons/postgresql-vs-mongodb.md` | **Planned** | Link mongodb comparison page |

---

## 08 Interview Guide

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Top 150 question index | `08-interview-guide/top-150-interview-questions.md` | **Planned** | Questions only |
| Architect question subset | `08-interview-guide/architect-questions.md` | **Planned** | Questions only |
| Troubleshooting question subset | `08-interview-guide/troubleshooting-questions.md` | **Planned** | Questions only |
| Performance question subset | `08-interview-guide/performance-questions.md` | **Planned** | Questions only |
| Answer layer | Topic pages per question mapping | **Planned** | `## Question` blocks on canonical pages |

---

## 09 Learning Paths

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Senior engineer curriculum | `09-learning-paths/postgresql-senior-engineer-path.md` | **Planned** | |
| Lead curriculum | `09-learning-paths/postgresql-lead-path.md` | **Planned** | |
| Architect curriculum | `09-learning-paths/postgresql-architect-path.md` | **Planned** | |
| Interview revision cram | `09-learning-paths/postgresql-interview-revision-path.md` | **Planned** | |

---

## Cross-Registry (External — Link Only)

| Concept | Canonical Page | Notes |
| :--- | :--- | :--- |
| Generic MVCC theory | `database-handbook/local-concurrency-mvcc.md` | Not PG-specific |
| Generic cost-based optimization | `database-handbook/cost-based-query-optimization.md` | |
| Generic deadlock theory | `database-handbook/lock-graphs-deadlocks-latching.md` | |
| PostgreSQL product selection | `database-handbook/postgresql.md` | When to choose PG |
| Oracle migration ADR | `database-handbook/oracle-vs-postgresql.md` | |

---

## Enforcement Checklist (Phase B)

- [ ] Every topic page lists related concepts with links only (no duplicate deep dives)
- [ ] `grep` audit for repeated paragraphs (MVCC, WAL, EXPLAIN, pooling)
- [ ] Interview Top 150 `Deep Dive` column uses Hugo URLs + `#` anchors
- [ ] `interview-prep/top-150-interview-questions.md` PostgreSQL rows updated to new paths
- [ ] Build script topic list matches registry
