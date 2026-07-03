---
title: "PostgreSQL Handbook Infographic Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["postgresql-cheatsheet", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, and optional future static images — not separate image assets unless generated later.

**Meta files:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Quick revision sheet | Markdown table + bullets | Page **Quick Revision** section or `09-learning-paths/postgresql-interview-revision-path.md` |
| Comparison one-pager | Markdown table + pros/cons matrix | `07-comparisons/*` |
| Decision tree | Mermaid `flowchart TD` | `troubleshooting.md`, comparisons, `query-optimization.md` |
| Troubleshooting runbook card | Symptom → cause → fix table | `06-production-operations/troubleshooting.md` |
| Architecture poster | Mermaid `flowchart TB` | `architecture.md`, `storage-engine.md`, `wal.md` |
| Interview cheat sheet | Single-page categorized table | `08-interview-guide/top-150-interview-questions.md` |
| Parameter tuning card | Knob → effect → risk table | `performance-tuning.md`, `capacity-planning.md` |
| Observability toolkit | View/extension → purpose table | `monitoring.md` |

---

## By Module

### 01 Fundamentals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| SQL clause order | SELECT pipeline table | `sql-basics.md` | P3 |
| Join type matrix | Join × preserves rows | `joins.md` | P2 |
| UPSERT pattern card | ON CONFLICT recipes | `dml.md` | P2 |
| CTE materialization | MATERIALIZED vs NOT hint card | `ctes.md` | P2 |
| Window frame defaults | ROWS vs RANGE gotchas | `window-functions.md` | P3 |

### 02 Core PostgreSQL

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Process architecture | postmaster + background workers | `architecture.md` | P0 |
| Memory layout | shared_buffers / work_mem / maintenance_work_mem | `architecture.md` | P0 |
| Page structure | 8KB page anatomy | `storage-engine.md` | P0 |
| TOAST strategies | Plain / extended / external | `storage-engine.md` | P0 |
| FSM vs VM | Free space vs all-visible pages | `storage-engine.md` | P1 |
| WAL lifecycle | Insert → WAL → checkpoint → archive | `wal.md` | P0 |
| Checkpoint tuning | max_wal_size / checkpoint_timeout card | `wal.md` | P1 |
| MVCC tuple header | xmin / xmax / ctid fields | `mvcc.md` | P0 |
| Isolation anomaly matrix | Level × dirty/non-repeatable/phantom | `isolation-levels.md` | P0 |
| Lock mode matrix | Mode × conflicting modes | `locks.md` | P1 |
| `FOR UPDATE` vs `SKIP LOCKED` | Queue worker pattern card | `locks.md` | P1 |

### 03 Query Performance

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Index type picker | Type × query pattern | `indexes.md` | P0 |
| Partial vs covering | When to use each | `indexes.md` | P0 |
| EXPLAIN node glossary | Node × meaning × concern | `explain.md` | P0 |
| Plan red flags | Seq Scan on large table, bad estimates | `explain.md` | P0 |
| Planner pipeline | Parse → plan → execute | `query-optimization.md` | P0 |
| Join algorithm picker | NL vs Hash vs Merge | `query-optimization.md` | P0 |
| Statistics checklist | ANALYZE, extended stats, ndistinct | `query-optimization.md` | P1 |
| Tuning knob card | shared_buffers, work_mem, effective_cache_size | `performance-tuning.md` | P0 |
| SSD parameter card | random_page_cost, effective_io_concurrency | `performance-tuning.md` | P1 |
| Partition method matrix | RANGE / LIST / HASH × use case | `partitioning.md` | P1 |
| Shard strategy matrix | Citus / FDW / app routing | `sharding.md` | P1 |

### 04 High Availability

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Replication mode matrix | Physical vs logical × use case | `replication.md` | P0 |
| Sync rep levels | remote_write / remote_apply / quorum | `replication.md` | P1 |
| Slot disk risk card | Idle subscriber → WAL bloat | `replication.md` | P1 |
| HA topology poster | Primary + sync standby + async + pooler | `failover.md` | P0 |
| Patroni components | DCS + health checks + promotion | `failover.md` | P0 |
| Backup method matrix | pg_dump vs base backup vs snapshot | `backup-restore.md` | P1 |
| PITR timeline | Base + WAL replay | `disaster-recovery.md` | P0 |
| RPO/RTO tiers | Backup frequency × recovery steps | `disaster-recovery.md` | P0 |

### 05 Advanced Features

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Function volatility | IMMUTABLE / STABLE / VOLATILE | `functions.md` | P1 |
| SECURITY DEFINER checklist | search_path lockdown | `functions.md` | P1 |
| Procedure vs function | Returns / txn inside | `stored-procedures.md` | P2 |
| Mat view refresh modes | Blocking vs CONCURRENTLY | `materialized-views.md` | P1 |
| json vs jsonb | Storage × indexing × ops | `json.md` | P1 |
| JSON operator card | -> / ->> / @> / ? | `json.md` | P2 |

### 06 Production Operations

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Monitoring toolkit | pg_stat_* views + extensions | `monitoring.md` | P0 |
| Wait event primer | wait_event_type × meaning | `monitoring.md` | P0 |
| pg_stat_statements columns | calls, mean, total, rows | `monitoring.md` | P0 |
| Pool mode matrix | Session / transaction / statement | `connection-pooling.md` | P0 |
| Pool sizing formula | apps × pool_size ≤ max_connections | `connection-pooling.md` | P0 |
| Autovacuum tuning card | scale_factor / threshold per table | `vacuum.md` | P1 |
| Bloat symptom table | n_dead_tup / age / long txn | `vacuum.md` | P1 |
| Freeze / wraparound card | age(datfrozenxid) thresholds | `vacuum.md` | P1 |
| Slow query runbook | Symptom → explain → fix | `troubleshooting.md` | P0 |
| Blocking runbook | pg_locks query → kill vs wait | `troubleshooting.md` | P0 |
| Replication lag runbook | Lag bytes → slot → network | `troubleshooting.md` | P0 |
| Connection storm runbook | max_connections → pooler | `troubleshooting.md` | P0 |
| CPU/RAM sizing worksheet | cores, RAM, connections | `capacity-planning.md` | P0 |
| Storage growth model | data + WAL + index overhead | `capacity-planning.md` | P1 |

### 07 Comparisons

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| PostgreSQL vs MySQL | ACID / JSON / extensions / replication | `postgresql-vs-mysql.md` | P0 |
| PostgreSQL vs Oracle | Licensing / PL-SQL / RAC / features | `postgresql-vs-oracle.md` | P0 |
| PostgreSQL vs MongoDB | Schema / joins / document flexibility | `postgresql-vs-mongodb.md` | P0 |
| Cross-link card | Link to database-handbook ADR pages | All comparison pages | P1 |

### 08 Interview Guide

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 150 index | Category × count × deep dive link | `top-150-interview-questions.md` | P0 |
| Question distribution | Arch 40 / Trouble 30 / Perf 25 / Rel 20 / Sec 15 | `top-150-interview-questions.md` | P0 |
| Architect top picks | 25-question subset table | `architect-questions.md` | P1 |
| Troubleshooting drills | 25 scenario questions | `troubleshooting-questions.md` | P1 |
| Performance drills | 25 tuning questions | `performance-questions.md` | P1 |

### 09 Learning Paths

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Senior engineer path | Week-by-week topic order | `postgresql-senior-engineer-path.md` | P1 |
| Lead path | Ops + performance + troubleshooting emphasis | `postgresql-lead-path.md` | P1 |
| Architect path | Internals + HA + comparisons | `postgresql-architect-path.md` | P1 |
| Interview revision | 48-hour cram schedule + topic clusters | `postgresql-interview-revision-path.md` | P0 |

---

## Existing Assets to Preserve (Phase B)

| Asset | Source file | Action |
| :--- | :--- | :--- |
| MVCC UPDATE mermaid | `mvcc.md` | Keep on canonical page |
| Isolation anomaly table | `isolation-levels.md` | Keep; enhance with visual matrix |
| Index type table | `indexes.md` | Keep; add internals in Phase C |
| EXPLAIN node table | `explain.md` | Keep; add plan tree mermaid |
| Replication mode table | `replication.md` | Keep; split failover content out |
| Backup method table | `backup-restore.md` | Keep; PITR depth → `disaster-recovery.md` |
| Parameter tuning table | `performance-tuning.md` | Keep; strip pooling rows |
| pg_stat_activity snippets | `locks.md`, `most-common-sql-commands.md` | **Consolidate** → `monitoring.md` |
| Interview shortcode answers | `interview-questions.md` | **Migrate** to topic page `## Question` blocks |

---

## 14-Section Template — Infographic Mapping

| Template section | Primary visual asset |
| :--- | :--- |
| Quick Revision | One-page table (revision sheet) |
| Core Concepts | Concept matrix |
| Internal Working | Mermaid sequence / flowchart |
| Architecture | Topology poster |
| Design Tradeoffs | Pros/cons comparison table |
| Production Patterns | Pattern recipe cards |
| Scalability | Partition / shard / replica heuristic |
| Reliability | Replication + DR tier matrix |
| Security | pg_hba + RLS layer diagram (Phase C) |
| Observability | Monitoring toolkit table |
| Troubleshooting | Decision tree mermaid |
| Common Mistakes | Anti-pattern bullet card |
| Interview Questions | Link to Top 150 only |
| Checklists | Pre-prod / incident checklists |

**Rule:** Do not add empty sections — pair each section with at least one visual when the section exists.

---

## Top 150 Question Category Visual (Phase B)

Single table on `top-150-interview-questions.md`:

| Category | Min count | Deep dive module |
| :--- | :---: | :--- |
| Architecture | 40 | `02-core-postgresql/`, `04-high-availability/` |
| Troubleshooting | 30 | `06-production-operations/troubleshooting.md` |
| Performance | 25 | `03-query-performance/`, `06-production-operations/monitoring.md` |
| Reliability | 20 | `04-high-availability/`, `wal.md`, `vacuum.md` |
| Security | 15 | `architecture.md` (Phase C security page if added) |

**Topic focus areas (from requirements):**

Storage Engine, WAL, MVCC, Transactions, Isolation, Locking, Query Planner, EXPLAIN, Vacuum, Autovacuum, Index Internals, Partitioning, Replication, Failover, PITR, Monitoring, Capacity, PgBouncer, Performance Tuning, HA, vs Oracle, vs MySQL.

**Avoid:** Syntax memorization, certification-style trivia.

---

## Top 150 → Answer Location Map (Planning Sample)

Phase B generates full 150 rows. Sample mapping pattern:

| Q# range | Topic cluster | Primary answer page |
| :--- | :--- | :--- |
| 1–15 | Storage engine / heap / TOAST | `storage-engine.md` |
| 16–30 | WAL / checkpoints / recovery | `wal.md` |
| 31–45 | MVCC / visibility / HOT | `mvcc.md` |
| 46–55 | Isolation / transactions | `isolation-levels.md`, `transactions.md` |
| 56–65 | Locks / deadlocks | `locks.md` |
| 66–80 | Planner / EXPLAIN / stats | `query-optimization.md`, `explain.md` |
| 81–90 | Indexes / partitioning | `indexes.md`, `partitioning.md` |
| 91–105 | Vacuum / bloat / freeze | `vacuum.md` |
| 106–120 | Replication / failover / DR | `replication.md`, `failover.md`, `disaster-recovery.md` |
| 121–130 | Monitoring / troubleshooting | `monitoring.md`, `troubleshooting.md` |
| 131–140 | Pooling / capacity / tuning | `connection-pooling.md`, `capacity-planning.md`, `performance-tuning.md` |
| 141–150 | Comparisons / architect scenarios | `07-comparisons/*`, `failover.md` |

Each question gets exactly one `Deep Dive` URL with optional `#anchor`.

---

## Phase Rollout

| Phase | Deliverable |
| :--- | :--- |
| **B** | P0 infographics on all new pages; preserve existing mermaid; Top 150 category table + 150 questions |
| **C** | P1 comparison one-pagers; learning path schedules; security depth; answer layer on topic pages |
| **D** | Optional static PNG exports from Mermaid (out of scope unless requested) |

---

## Out of Scope

- Custom SVG illustration files
- Modifying `database-handbook` visuals
- Modifying other handbook sections per user constraint
- `most-common-sql-commands.md` content — merge into monitoring, not standalone infographic
