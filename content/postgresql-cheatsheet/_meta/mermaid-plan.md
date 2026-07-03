---
title: "PostgreSQL Handbook Mermaid Diagram Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Diagram opportunities by topic — Phase B/C implementation backlog."
tags: ["postgresql-cheatsheet", "meta", "planning"]
---

# Mermaid Diagram Plan

**Principle:** Diagrams on **canonical pages only**. Non-canonical pages link to diagram section.

**Existing diagrams (in repo today):** 1 across 1 file.

| File | Diagram type | Topic |
| :--- | :--- | :--- |
| `mvcc.md` | `flowchart LR` | UPDATE → new tuple → VACUUM reclaim |

---

## 01 Fundamentals

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `sql-basics.md` | — | Skip — clause tables sufficient | P3 | N/A |
| `joins.md` | `flowchart LR` | INNER vs LEFT null preservation | P2 | Planned |
| `joins.md` | `flowchart TB` | LATERAL top-N-per-group pattern | P2 | Planned |
| `ctes.md` | `flowchart LR` | Recursive CTE anchor + recursive term | P2 | Planned |
| `window-functions.md` | `flowchart LR` | PARTITION BY vs GROUP BY row retention | P3 | Planned |

---

## 02 Core PostgreSQL

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `architecture.md` | `flowchart TB` | postmaster → backends → bgwriter/checkpointer/walwriter | P0 | Planned |
| `architecture.md` | `flowchart LR` | Client → pooler → PostgreSQL processes | P0 | Planned |
| `storage-engine.md` | `flowchart TB` | Relation → fork → page → tuple | P0 | Planned |
| `storage-engine.md` | `flowchart LR` | Heap page layout (header, line pointers, tuples) | P0 | Planned |
| `storage-engine.md` | `sequenceDiagram` | INSERT path: buffer → WAL → heap | P0 | Planned |
| `storage-engine.md` | `flowchart TB` | TOAST out-of-line storage for wide values | P1 | Planned |
| `storage-engine.md` | `flowchart LR` | FSM + Visibility Map role | P1 | Planned |
| `storage-engine.md` | `flowchart LR` | HOT update (same page, no index update) | P1 | Planned |
| `wal.md` | `sequenceDiagram` | Commit: WAL flush → CLOG → visibility | P0 | Planned |
| `wal.md` | `flowchart LR` | WAL segment rotation + archive | P0 | Planned |
| `wal.md` | `sequenceDiagram` | Crash recovery: redo from checkpoint | P0 | Planned |
| `mvcc.md` | `flowchart LR` | Tuple version chain | — | **Exists** |
| `mvcc.md` | `flowchart TB` | Snapshot visibility decision tree | P1 | Planned |
| `mvcc.md` | `sequenceDiagram` | UPDATE creates new row version | P1 | Planned |
| `isolation-levels.md` | `flowchart TD` | Anomaly × isolation level matrix (visual) | P1 | Planned |
| `isolation-levels.md` | `sequenceDiagram` | READ COMMITTED re-snapshot per statement | P1 | Planned |
| `locks.md` | `flowchart TD` | Lock mode compatibility matrix (simplified) | P1 | Planned |
| `locks.md` | `sequenceDiagram` | Deadlock detection cycle | P1 | Planned |
| `transactions.md` | `sequenceDiagram` | SAVEPOINT partial rollback | P2 | Planned |

---

## 03 Query Performance

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `indexes.md` | `flowchart TB` | B-tree structure (root → leaf → heap) | P0 | Planned |
| `indexes.md` | `flowchart LR` | Index type picker (B-tree/GIN/GiST/BRIN) | P1 | Planned |
| `indexes.md` | `flowchart LR` | Index-only scan + visibility map check | P1 | Planned |
| `explain.md` | `flowchart TB` | Sample plan tree anatomy | P0 | Planned |
| `explain.md` | `flowchart LR` | Estimated vs actual rows mismatch | P1 | Planned |
| `query-optimization.md` | `flowchart TD` | Parser → rewriter → planner → executor | P0 | Planned |
| `query-optimization.md` | `flowchart LR` | Nested Loop vs Hash Join vs Merge Join | P0 | Planned |
| `query-optimization.md` | `flowchart TB` | Parallel gather → workers → gather merge | P1 | Planned |
| `performance-tuning.md` | `flowchart TB` | Tuning layers: SQL → index → config → hardware | P1 | Planned |
| `partitioning.md` | `flowchart LR` | Partition pruning at plan time | P1 | Planned |
| `partitioning.md` | `flowchart TB` | RANGE monthly partition timeline | P2 | Planned |
| `sharding.md` | `flowchart TB` | Citus coordinator → worker shards | P1 | Planned |

---

## 04 High Availability

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `replication.md` | `flowchart LR` | Primary WAL stream → standby | P0 | Planned |
| `replication.md` | `flowchart TB` | Sync vs async replication paths | P0 | Planned |
| `replication.md` | `sequenceDiagram` | Logical replication publication → slot → apply | P1 | Planned |
| `failover.md` | `sequenceDiagram` | Primary failure → promotion → clients reconnect | P0 | Planned |
| `failover.md` | `flowchart TB` | Patroni / HA stack (etcd + API + PG) | P0 | Planned |
| `backup-restore.md` | `flowchart LR` | Logical vs physical backup paths | P1 | Planned |
| `disaster-recovery.md` | `sequenceDiagram` | PITR timeline: base backup + WAL replay | P0 | Planned |
| `disaster-recovery.md` | `flowchart TD` | RPO/RTO tradeoff by backup tier | P1 | Planned |

---

## 05 Advanced Features

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `materialized-views.md` | `sequenceDiagram` | REFRESH CONCURRENTLY swap | P2 | Planned |
| `triggers.md` | `sequenceDiagram` | BEFORE ROW trigger modifies NEW | P3 | Planned |
| `json.md` | `flowchart LR` | json (text) vs jsonb (binary) query path | P2 | Planned |

---

## 06 Production Operations

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `monitoring.md` | `flowchart LR` | pg_stat_activity → pg_stat_statements → logs | P0 | Planned |
| `monitoring.md` | `sequenceDiagram` | Slow query detection workflow | P1 | Planned |
| `connection-pooling.md` | `flowchart TB` | App instances → PgBouncer → PostgreSQL | P0 | Planned |
| `connection-pooling.md` | `flowchart LR` | Session vs transaction pooling semantics | P0 | Planned |
| `vacuum.md` | `sequenceDiagram` | Autovacuum cycle on dead tuples | P1 | Planned |
| `vacuum.md` | `flowchart TD` | Freeze / wraparound protection timeline | P1 | Planned |
| `troubleshooting.md` | `flowchart TD` | Slow query triage tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Blocking / lock wait triage tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Replication lag triage tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Bloat / autovacuum triage tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Connection exhaustion triage tree | P1 | Planned |
| `capacity-planning.md` | `flowchart TB` | Memory budget: shared_buffers + work_mem × ops | P1 | Planned |

---

## 07 Comparisons

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `postgresql-vs-mysql.md` | `flowchart TD` | OLTP fit decision (PG vs MySQL) | P1 | Planned |
| `postgresql-vs-oracle.md` | `flowchart TD` | Migration program phases | P2 | Planned |
| `postgresql-vs-mongodb.md` | `flowchart TD` | Relational vs document workload fit | P1 | Planned |

---

## 08 Interview Guide

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `top-150-interview-questions.md` | — | Link to topic diagrams only | P3 | N/A |
| `postgresql-interview-revision-path.md` | `flowchart LR` | Revision order by topic cluster | P2 | Planned |

---

## Diagram Quality Rules (Phase B)

1. Max **2 diagrams per page** in initial pass; add more in Phase C if needed.
2. Prefer `sequenceDiagram` for commit, failover, PITR, replication, trigger flows.
3. Prefer `flowchart TD` for troubleshooting decision trees.
4. Prefer `flowchart TB` for architecture / storage topology.
5. No diagram-only pages — always paired with prose.
6. Alt text via adjacent heading (Hugo/Mermaid accessibility).
7. Preserve existing `mvcc.md` diagram — enhance, do not remove without replacement.

---

## Priority Summary

| Priority | Count | Focus |
| :---: | :---: | :--- |
| P0 | 22 | architecture, storage-engine, wal, planner, indexes, HA, failover, PITR, monitoring, pooling, troubleshooting trees |
| P1 | 24 | MVCC depth, locks, replication modes, partition, sharding, vacuum freeze, capacity |
| P2 | 12 | Fundamentals joins/CTEs, advanced features, comparison ADRs |
| P3 | 4 | Skip pages where tables suffice |

**Phase B minimum:** All P0 diagrams on new canonical pages.  
**Phase C:** P1–P2 backlog on upgraded topic pages.

---

## Preserve / Relocate

| Existing asset | Action |
| :--- | :--- |
| MVCC UPDATE flow (`mvcc.md`) | Keep on canonical page; add visibility tree in Phase B |
