---
title: "PostgreSQL Handbook Refactoring Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Phase A inventory — quality, duplication, gaps, and recommended actions."
tags: ["postgresql-cheatsheet", "meta", "planning"]
---

# Phase A — Repository Inventory

**Scope:** `content/postgresql-cheatsheet/` (28 markdown files)  
**Audience:** Senior Engineers, Technical Leads, Architects (6+ years)  
**Status:** Planning only — **no content rewritten in Phase A**

**Target structure:** 9 modules (`01-fundamentals` … `09-learning-paths`) + `_meta/` — implemented in Phase B within the same Hugo section slug (`postgresql-cheatsheet`) unless slug rename is approved separately.

**Build script:** `scripts/build_postgresql_cheatsheet.py` regenerates pages from `data/postgresql_cheatsheet_modules.yaml` — Phase B must update script + yaml or hand edits will be overwritten on regen.

---

## Executive Summary

| Metric | Assessment |
| :--- | :--- |
| **Structure** | **Flat** — 9 modules in yaml; no numbered folders |
| **Template compliance** | Cheat-sheet skeleton (`Executive Summary`, `Core Concepts`, `Snippets`) — **not** the 14-section architect template |
| **Average page depth** | ~75 lines — strong for 2-minute brush-up; **weak** for architect/production depth |
| **Duplication** | **High** — MVCC/vacuum, EXPLAIN/stats, pg_stat_activity, WAL/replication/backup, CRUD, PgBouncer, index types repeated across 3–6 files |
| **Canonical discipline** | **None** — no concept registry enforced |
| **Interview Layer 1** | **Missing** — only `interview-questions.md` with 3 answered probes (wrong model) |
| **Interview Layer 2** | **Missing** — no `## Question` answer blocks on topic pages |
| **Production ops** | **Thin** — no monitoring, troubleshooting, capacity, connection pooling, or DR canonical pages |
| **Storage internals** | **Missing** — no heap/page/TOAST/WAL architecture pages |
| **Cross-handbook overlap** | `database-handbook/postgresql.md` (ADR), `local-concurrency-mvcc.md`, `cost-based-query-optimization.md`, `lock-graphs-deadlocks-latching.md` — link, do not duplicate deep dives |
| **Cross-section overlap** | `interview-prep/top-150-interview-questions.md` references 15+ PostgreSQL paths — must align Deep Dive URLs in Phase B |

**Recommended Phase B focus:** Restructure into 9 modules, enforce concept registry, create 18 missing canonical pages, split performance/monitoring/troubleshooting, replace interview layer, add learning paths — **preserve** valuable cheat-sheet tables/snippets.

---

## Scoring Guide

| Dimension | 1 | 10 |
| :--- | :--- | :--- |
| **Quality** | Inaccurate or trivial | Accurate, production-grade, maintainable |
| **Duplication** | Unique | Heavily repeated elsewhere |
| **Interview Value** | Not useful in senior interviews | High architect-panel value |

Subscores used in **Quality** column: accuracy, production relevance, architecture depth, performance depth, troubleshooting value.

---

## File Inventory

| File | Purpose | Quality | Duplication | Interview Value | Problems | Action |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| `_index.md` | Section landing; links to database handbook | 5 | 2 | 4 | One paragraph; no module map or learning paths | **Keep** — expand with 9-module overview + learning path links |
| `installation.md` | Install on Linux/macOS/Docker; psql basics | 6 | 3 | 3 | Not in target structure; junior-focused; `pg_stat_statements` mention belongs on monitoring | **Demote** → `01-fundamentals/installation.md` appendix or fold bootstrap into `02-core-postgresql/architecture.md` |
| `sql-basics.md` | SELECT, WHERE, ORDER BY, LIMIT, psql meta | 6 | 5 | 4 | Syntax-heavy for architect audience; overlaps `most-common-sql-commands` | **Move** → `01-fundamentals/sql-basics.md`; slim psql meta to monitoring quick-ref |
| `most-common-sql-commands.md` | Daily CRUD, catalog queries, session helpers | 5 | 8 | 3 | Duplicates `sql-basics`, `dml`, `locks`, `explain`; certification-style | **Merge** — fold unique catalog snippets into `monitoring.md` / `troubleshooting.md`; **delete** or demote to appendix |
| `ddl.md` | CREATE/ALTER, types, constraints | 7 | 3 | 5 | Solid fundamentals; `ALTER ADD COLUMN` rewrite note is production-relevant | **Move** → `01-fundamentals/ddl.md` |
| `dml.md` | INSERT/UPDATE/DELETE, UPSERT, RETURNING | 7 | 4 | 5 | Upsert patterns good; bulk-load note belongs on storage-engine | **Move** → `01-fundamentals/dml.md` |
| `joins.md` | Join types, LATERAL, top-N per group | 7 | 2 | 6 | LATERAL pattern is senior-relevant | **Move** → `01-fundamentals/joins.md` |
| `ctes.md` | WITH, recursive, MATERIALIZED hints | 7 | 4 | 7 | Planner interaction noted but shallow; overlaps planned `query-optimization.md` | **Move** → `01-fundamentals/ctes.md`; link canonical planner page |
| `indexes.md` | B-tree, GIN, GiST, BRIN, partial, covering | 7 | 6 | 8 | GIN/jsonb duplicates `json.md`; no index internals (B-tree page splits) | **Move** → `03-query-performance/indexes.md` — **canonical** for indexes |
| `explain.md` | EXPLAIN nodes, ANALYZE, BUFFERS | 7 | 6 | 9 | Stats tuning overlaps `performance-tuning`, `vacuum`; no JSON plan format | **Move** → `03-query-performance/explain.md` — **canonical** for reading plans |
| `performance-tuning.md` | shared_buffers, work_mem, pg_stat_statements, PgBouncer mention | 6 | 7 | 8 | Jack-of-all-trades: config + pooling + query stats; no capacity methodology | **Move** → `03-query-performance/performance-tuning.md`; strip pooling to `connection-pooling.md` |
| `transactions.md` | BEGIN/COMMIT, SAVEPOINT, ACID | 6 | 4 | 7 | Serializable retry noted; no 2PC/subtransactions depth | **Move** → `02-core-postgresql/transactions.md` |
| `isolation-levels.md` | RC, RR, Serializable anomaly table | 7 | 6 | 9 | Overlaps `mvcc.md` snapshot narrative; overlaps `database-handbook/local-concurrency-mvcc.md` | **Move** → `02-core-postgresql/isolation-levels.md` — **canonical** for isolation |
| `mvcc.md` | xmin/xmax, snapshots, vacuum interaction | 6 | 7 | 10 | Best concurrency content but thin on heap/tuple chain; one mermaid only | **Move** → `02-core-postgresql/mvcc.md` — **canonical** for MVCC; deepen in Phase C |
| `locks.md` | Row/table/advisory locks, pg_locks, deadlocks | 7 | 6 | 9 | pg_stat_activity queries duplicate `most-common-sql-commands`; overlaps db-handbook lock-graphs | **Move** → `02-core-postgresql/locks.md` — **canonical** for locking |
| `partitioning.md` | RANGE/LIST/HASH, pruning, attach | 7 | 3 | 8 | Constraint-on-PK rule correct; no partition-wise join | **Move** → `03-query-performance/partitioning.md` |
| `sharding.md` | Citus, FDW, app routing | 6 | 4 | 7 | Not in target tree; valuable architect content | **Keep** → `03-query-performance/sharding.md` (scalability extension) |
| `replication.md` | Streaming, logical, slots, pg_basebackup | 6 | 7 | 9 | Failover/Patroni/RPO shallow; WAL overlap with backup; no sync rep params | **Move** → `04-high-availability/replication.md` — **canonical** for replication modes |
| `views.md` | CREATE VIEW, updatable, security_barrier | 6 | 2 | 4 | Not in target structure; low architect priority | **Merge** → brief section in `05-advanced-features/materialized-views.md` or keep as `05-advanced-features/views.md` |
| `materialized-views.md` | REFRESH, CONCURRENTLY, staleness | 7 | 2 | 6 | Focused, accurate | **Move** → `05-advanced-features/materialized-views.md` |
| `window-functions.md` | ROW_NUMBER, LAG/LEAD, frames | 7 | 2 | 5 | SQL syntax focus; not in target tree | **Keep** → `01-fundamentals/window-functions.md` (analytics SQL module) |
| `json.md` | json vs jsonb, operators, GIN | 7 | 5 | 6 | GIN index duplicates `indexes.md` | **Move** → `05-advanced-features/json.md` |
| `functions.md` | Volatility, PL/pgSQL, SECURITY DEFINER | 7 | 2 | 7 | search_path hijack note is production-grade | **Move** → `05-advanced-features/functions.md` |
| `triggers.md` | BEFORE/AFTER, audit patterns | 6 | 2 | 5 | Adequate cheat sheet | **Move** → `05-advanced-features/triggers.md` |
| `stored-procedures.md` | PROCEDURE vs FUNCTION, CALL | 6 | 3 | 5 | Transaction-in-procedure distinction useful | **Move** → `05-advanced-features/stored-procedures.md` |
| `vacuum.md` | VACUUM, autovacuum, freeze, bloat | 7 | 7 | 9 | Overlaps `mvcc.md`, `performance-tuning`; no visibility map/FSM | **Move** → `06-production-operations/vacuum.md` — **canonical** for vacuum |
| `backup-restore.md` | pg_dump, base backup, PITR mention | 6 | 6 | 8 | PITR/WAL archive shallow; overlaps replication | **Move** → `04-high-availability/backup-restore.md`; split DR depth to `disaster-recovery.md` |
| `interview-questions.md` | 6 theme table + 3 `interview-answer` shortcodes | 5 | 9 | 5 | Wrong interview model (answers inline); duplicates topic pages | **Replace** → `08-interview-guide/` (questions only) |

---

## Missing Files (Phase B Create)

| File | Priority | Rationale |
| :--- | :---: | :--- |
| `02-core-postgresql/architecture.md` | P0 | Process model, shared memory, bgwriter, checkpointer — no canonical page |
| `02-core-postgresql/storage-engine.md` | P0 | Heap, page layout, TOAST, FSM, visibility map, buffer cache — **required** |
| `02-core-postgresql/wal.md` | P0 | WAL segments, checkpoints, crash recovery — foundation for replication/DR |
| `03-query-performance/query-optimization.md` | P0 | Planner, cost model, stats, cardinality, join selection, parallel query |
| `04-high-availability/failover.md` | P0 | Promotion, Patroni, HA topology, sync/async tradeoffs |
| `04-high-availability/disaster-recovery.md` | P0 | PITR, RPO/RTO, WAL recovery strategy |
| `06-production-operations/monitoring.md` | P0 | pg_stat_activity, pg_stat_statements, pg_locks, wait events |
| `06-production-operations/troubleshooting.md` | P0 | Deadlocks, blocking, slow queries, bloat, lag, autovacuum, connections |
| `06-production-operations/connection-pooling.md` | P0 | PgBouncer modes, pool sizing, prepared statement semantics |
| `06-production-operations/capacity-planning.md` | P1 | CPU/RAM/connection/storage sizing heuristics |
| `07-comparisons/postgresql-vs-mysql.md` | P1 | Architect selection ADR |
| `07-comparisons/postgresql-vs-oracle.md` | P1 | Migration / feature parity framing |
| `07-comparisons/postgresql-vs-mongodb.md` | P1 | Document vs relational; link db-handbook, not duplicate |
| `08-interview-guide/top-150-interview-questions.md` | P0 | Exactly 150 questions, no answers |
| `08-interview-guide/architect-questions.md` | P1 | Top subset — questions only |
| `08-interview-guide/troubleshooting-questions.md` | P1 | Top subset — questions only |
| `08-interview-guide/performance-questions.md` | P1 | Top subset — questions only |
| `09-learning-paths/postgresql-senior-engineer-path.md` | P1 | Curated reading order |
| `09-learning-paths/postgresql-lead-path.md` | P1 | Ops + performance emphasis |
| `09-learning-paths/postgresql-architect-path.md` | P1 | HA + comparisons + internals |
| `09-learning-paths/postgresql-interview-revision-path.md` | P1 | 48-hour cram schedule |

**Section `_index.md` files:** Create for modules `01`–`09` in Phase B (9 placeholders).

---

## Duplicate Content (Semantic Overlap > 60%)

| Concept cluster | Appears in | Canonical target (Phase B) |
| :--- | :--- | :--- |
| MVCC / xmin / xmax / snapshots | `mvcc`, `isolation-levels`, `vacuum`, `locks`, `interview-questions`, `database-handbook/local-concurrency-mvcc.md` | `02-core-postgresql/mvcc.md` |
| VACUUM / autovacuum / bloat / freeze | `vacuum`, `mvcc`, `performance-tuning`, `interview-questions` | `06-production-operations/vacuum.md` |
| Isolation levels / anomalies | `isolation-levels`, `transactions`, `mvcc`, `interview-questions`, db-handbook | `02-core-postgresql/isolation-levels.md` |
| EXPLAIN / plan nodes / ANALYZE | `explain`, `performance-tuning`, `indexes`, `ctes`, `most-common-sql-commands` | `03-query-performance/explain.md` + `query-optimization.md` |
| Planner stats / cardinality | `explain`, `performance-tuning`, `vacuum` (ANALYZE) | `03-query-performance/query-optimization.md` |
| Index types / partial / covering | `indexes`, `json`, `interview-questions` | `03-query-performance/indexes.md` |
| pg_stat_statements / slow queries | `performance-tuning`, `explain`, `most-common-sql-commands` | `06-production-operations/monitoring.md` |
| pg_stat_activity / cancel backend | `locks`, `most-common-sql-commands` | `06-production-operations/monitoring.md` |
| WAL / base backup / PITR | `replication`, `backup-restore` | `02-core-postgresql/wal.md` + `04-high-availability/disaster-recovery.md` |
| Streaming vs logical replication | `replication`, `backup-restore`, `interview-questions` | `04-high-availability/replication.md` |
| Failover / promotion / RPO | `replication`, `backup-restore` (thin) | `04-high-availability/failover.md` |
| PgBouncer / max_connections | `performance-tuning`, `interview-prep` Q83 | `06-production-operations/connection-pooling.md` |
| CRUD / UPSERT | `sql-basics`, `dml`, `most-common-sql-commands` | `01-fundamentals/dml.md` |
| GIN / jsonb indexing | `json`, `indexes` | `03-query-performance/indexes.md` (index) + `05-advanced-features/json.md` (operators) |
| Partition vs shard scale-out | `partitioning`, `sharding`, `replication` (read replicas) | `partitioning.md` + `sharding.md` |
| Cheat-sheet boilerplate | All 27 topic pages | Upgrade to architect template; **omit empty sections** |

---

## Fragmented Concepts (No Single Canonical Home Today)

| Concept | Current fragments | Phase B canonical |
| :--- | :--- | :--- |
| PostgreSQL process architecture | Scattered in `installation`, `performance-tuning` | `architecture.md` |
| Heap / page / tuple storage | `mvcc` (1 paragraph), db-handbook B+ tree generic | `storage-engine.md` |
| WAL / checkpoints | `replication`, `backup-restore` (snippets) | `wal.md` |
| Query planner internals | `explain` (nodes only), db-handbook cost-based | `query-optimization.md` |
| Connection pooling | `performance-tuning` (2 bullets) | `connection-pooling.md` |
| HA / Patroni | `replication` (1 bullet) | `failover.md` |
| DR / PITR | `backup-restore` (table row) | `disaster-recovery.md` |
| Observability | `locks`, `performance-tuning`, `most-common-sql-commands` | `monitoring.md` |
| Incident runbooks | None | `troubleshooting.md` |
| Capacity sizing | `performance-tuning` (parameter table only) | `capacity-planning.md` |

---

## Weak Files (Quality ≤ 5 or Architect Gap)

| File | Issue |
| :--- | :--- |
| `most-common-sql-commands.md` | High duplication; low architect value — primary merge candidate |
| `interview-questions.md` | Wrong model; only 3 answers; duplicates topic depth |
| `_index.md` | No navigation story |
| `installation.md` | Below target audience seniority |
| `replication.md` | HA/failover depth insufficient for lead/architect interviews |
| `performance-tuning.md` | Mixes unrelated concerns without methodology |
| `mvcc.md` | Interview-critical but lacks heap/tuple chain internals |

---

## Outdated or Accuracy Flags

| Item | Location | Note |
| :--- | :--- | :--- |
| `EXECUTE FUNCTION` trigger syntax | `triggers.md` | PG 14+ syntax — document version note in Phase B |
| `ALTER ADD COLUMN` rewrite | `ddl.md` | PG 11+ fast default — clarify version-specific behavior |
| RR phantom row | `isolation-levels.md` | PG RR is snapshot isolation — correct but needs SSI distinction for Serializable |
| Build script regen | `scripts/build_postgresql_cheatsheet.py` | Will overwrite Phase B hand edits unless script updated |

---

## Cross-Handbook Boundaries (Do Not Duplicate in Phase B)

| External page | Purpose | Link strategy |
| :--- | :--- | :--- |
| `database-handbook/postgresql.md` | Product selection ADR | Link from comparisons + `_index` |
| `database-handbook/local-concurrency-mvcc.md` | Generic MVCC theory | Link from `mvcc.md`; PG-specific visibility on canonical page |
| `database-handbook/cost-based-query-optimization.md` | Generic optimizer theory | Link from `query-optimization.md` |
| `database-handbook/lock-graphs-deadlocks-latching.md` | Generic deadlock theory | Link from `locks.md`, `troubleshooting.md` |
| `database-handbook/oracle-vs-postgresql.md` | Migration ADR | Link from `postgresql-vs-oracle.md` |
| `interview-prep/top-150-interview-questions.md` | Cross-stack Top 150 | Update PostgreSQL Deep Dive URLs to new paths in Phase B |

---

## Phase B Task Checklist (Awaiting Approval)

1. Create `_meta/` enforcement + numbered module folders `01`–`09`
2. Update `data/postgresql_cheatsheet_modules.yaml` + `postgresql_cheatsheet_order.yaml`
3. Update `scripts/build_postgresql_cheatsheet.py` for new structure (or disable regen for hand-crafted pages)
4. Add Hugo `aliases` for all moved flat URLs
5. Create 18 missing canonical pages (P0 first)
6. Merge `most-common-sql-commands.md` → monitoring/troubleshooting; delete or appendix
7. Replace `interview-questions.md` with `08-interview-guide/` Layer 1 (150 questions)
8. Add Layer 2 answer blocks on canonical topic pages (batched)
9. Strip duplicate deep dives per concept registry
10. Expand `_index.md` + module `_index.md` landing pages

---

## Phase C (Post-Structure)

- Deepen storage-engine, wal, query-optimization internals
- Mermaid P0 backlog (see `mermaid-plan.md`)
- Infographic P0 tables (see `infographic-plan.md`)
- Security section (RLS, pg_hba, SCRAM) — no canonical page today; add to `architecture.md` or dedicated page if approved

---

**STOP — Phase A complete. Await approval before Phase B content changes.**
