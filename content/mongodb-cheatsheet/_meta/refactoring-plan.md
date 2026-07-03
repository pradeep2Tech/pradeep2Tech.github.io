---
title: "MongoDB Handbook Refactoring Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Phase A inventory — quality, duplication, gaps, and recommended actions."
tags: ["mongodb-cheatsheet", "meta", "planning"]
---

# Phase A — Repository Inventory

**Scope:** `content/mongodb-cheatsheet/` (18 markdown files)  
**Audience:** Senior Engineers, Technical Leads, Architects (6+ years)  
**Status:** Planning only — **no content rewritten in Phase A**

**Target structure:** 7 modules (`01-fundamentals` … `07-learning-paths`) + `_meta/` — implemented in Phase B within the same Hugo section slug (`mongodb-cheatsheet`) unless slug rename is approved separately.

---

## Executive Summary

| Metric | Assessment |
| :--- | :--- |
| **Structure** | **Flat** — 4 modules in yaml; no numbered folders |
| **Template compliance** | Cheat-sheet skeleton (`Executive Summary`, `Core Concepts`, `Snippets`) — **not** the 14-section architect template |
| **Average page depth** | ~100 lines — strong for 2-minute brush-up; **weak** for architect/production depth |
| **Duplication** | **High** — read/write concern, oplog, explain, WiredTiger, shard key, embed/reference repeated across 4–6 files |
| **Canonical discipline** | **None** — no concept registry enforced |
| **Interview Layer 1** | **Missing** — only `interview-questions.md` with 6 answered probes (wrong model) |
| **Interview Layer 2** | **Missing** — no `## Question` answer blocks on topic pages |
| **Production ops** | **Thin** — no monitoring, troubleshooting, backup, or capacity canonical pages |
| **Storage internals** | **Fragmented** — WiredTiger mentioned in `architecture.md` + `performance.md` only |
| **Cross-handbook overlap** | `database-handbook/mongodb.md` and `mongodb-vs-postgresql.md` exist — different purpose (selection ADR); link, do not duplicate deep dives |
| **Build scripts** | None — hand edits safe |

**Recommended Phase B focus:** Restructure into 7 modules, enforce concept registry, split `performance.md`, create 11 missing canonical pages, replace interview layer, add learning paths — **preserve** valuable cheat-sheet tables/snippets.

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
| `_index.md` | Section landing; links to database handbook | 5 | 2 | 4 | One paragraph; no module map or learning paths | **Keep** — expand with 7-module overview + learning path links |
| `architecture.md` | Deployment topology, processes, RC/WC tables | 6 | 7 | 7 | WiredTiger/oplog/RC/WC duplicate `replication`, `performance`; storage too shallow for canonical | **Keep** — **canonical** for deployment topology only; strip storage + consistency depth |
| `documents.md` | BSON types, `_id`, dot notation, arrays | 7 | 3 | 6 | Syntax-heavy for architect audience but correct fundamentals | **Move** → `01-fundamentals/documents.md` |
| `collections.md` | Collections, validation, capped, time series | 6 | 4 | 5 | Shell syntax overlaps `crud`, `mongo-shell-commands` | **Move** → `01-fundamentals/collections.md` |
| `crud.md` | CRUD methods, query/update operators | 6 | 4 | 4 | Operator tables are certification-style; low architect value | **Move** → `01-fundamentals/crud.md`; slim in Phase B |
| `atlas-basics.md` | Atlas tiers, SRV, CLI, Search index JSON | 6 | 5 | 7 | Backup/PITR/VPC mentioned but not canonical; overlaps `text-search` Atlas Search | **Move** → `01-fundamentals/atlas-basics.md`; deepen ops cross-links |
| `indexes.md` | Index types, ESR, partial explain stages | 7 | 6 | 8 | `explain` overlaps `performance.md`; should split to `explain-plan.md` | **Move** → `03-query-performance/indexes.md` |
| `ttl-index.md` | TTL expiry patterns | 7 | 2 | 6 | Focused, accurate | **Move** → `03-query-performance/ttl-index.md` |
| `text-search.md` | `$text` vs Atlas Search | 7 | 4 | 6 | Atlas Search also in `atlas-basics.md` | **Move** → `03-query-performance/text-search.md` |
| `geospatial.md` | GeoJSON, 2dsphere, geo operators | 7 | 2 | 5 | Solid specialist page | **Move** → `03-query-performance/geospatial.md` |
| `aggregation-pipeline.md` | Pipeline stages, `$lookup`, `$facet` | 6 | 4 | 7 | No planner/optimization internals; RAM limit noted only | **Move** → `03-query-performance/aggregation-pipeline.md`; link `query-optimization.md` |
| `replication.md` | Replica set, oplog, elections, read prefs | 6 | 7 | 9 | RC/WC tables duplicate `architecture`; election/rollback shallow | **Move** → `02-core-mongodb/replication.md` — **canonical** for replication |
| `sharding.md` | Shard key, chunks, balancer, zones | 7 | 5 | 9 | Chunk migration internals thin; jumbo chunks noted only | **Move** → `02-core-mongodb/sharding.md` — **canonical** for sharding |
| `transactions.md` | Multi-doc ACID, sessions, retryable writes | 6 | 4 | 8 | 2PC sequence shallow; contention guidance thin | **Move** → `02-core-mongodb/transactions.md` |
| `schema-design.md` | Embed/reference, bucketing, polymorphism | 8 | 4 | 9 | Best architect content in repo | **Move** → `02-core-mongodb/schema-design.md` — **canonical** for schema |
| `performance.md` | Explain snippet, profiler, working set, mongostat | 6 | 8 | 8 | Jack-of-all-trades: query + storage + replication lag + pooling | **Split** → `04-production-operations/performance.md` (tuning only); extract monitoring, capacity, explain |
| `mongo-shell-commands.md` | mongosh CRUD, admin, rs/sh helpers | 5 | 7 | 3 | Duplicates 6+ topic pages; syntax memorization | **Demote** → appendix or fold into `monitoring.md` / `troubleshooting.md` quick-ref |
| `interview-questions.md` | 6 Q&A with `interview-answer` shortcode | 5 | 9 | 5 | Wrong interview model (answers inline); duplicates topic pages | **Replace** → `06-interview-guide/` (questions only) |

---

## Missing Files (Phase B Create)

| File | Priority | Rationale |
| :--- | :---: | :--- |
| `02-core-mongodb/storage-engine.md` | P0 | WiredTiger/MVCC/checkpoints/journaling — no canonical page |
| `03-query-performance/query-optimization.md` | P0 | Query planner, covered queries, agg optimization — scattered |
| `03-query-performance/explain-plan.md` | P0 | `executionStats`, `winningPlan` — partial in `indexes` + `performance` |
| `04-production-operations/monitoring.md` | P0 | mongostat/mongotop/Atlas metrics/lag/slow query — absent |
| `04-production-operations/troubleshooting.md` | P0 | Runbooks for lag, hot shard, OOM, elections — absent |
| `04-production-operations/backup-recovery.md` | P1 | mongodump/PITR/oplog recovery — only Atlas one-liner |
| `04-production-operations/capacity-planning.md` | P1 | Working set sizing, shard sizing — one bullet in `performance` |
| `05-comparisons/mongodb-vs-postgresql.md` | P1 | Architect comparisons; link to `database-handbook` for ADR |
| `05-comparisons/mongodb-vs-cassandra.md` | P2 | Missing entirely |
| `05-comparisons/mongodb-vs-couchbase.md` | P2 | Missing entirely |
| `06-interview-guide/top-150-interview-questions.md` | P0 | Exactly 150 questions, no answers |
| `06-interview-guide/architect-questions.md` | P1 | Subset (~40 architecture) |
| `06-interview-guide/troubleshooting-questions.md` | P1 | Subset (~30 troubleshooting) |
| `06-interview-guide/performance-questions.md` | P1 | Subset (~25 performance) |
| `07-learning-paths/mongodb-senior-engineer-path.md` | P1 | Missing |
| `07-learning-paths/mongodb-lead-path.md` | P1 | Missing |
| `07-learning-paths/mongodb-architect-path.md` | P1 | Missing |
| `07-learning-paths/mongodb-interview-revision-path.md` | P1 | Missing |
| Section `_index.md` × 7 | P1 | Module landing stubs |

---

## Duplicate Content (Semantic Overlap > 50%)

| Concept cluster | Appears in | Canonical target (Phase B) |
| :--- | :--- | :--- |
| Deployment topology (mongod/mongos/config) | `architecture`, `sharding`, `replication` | `02-core-mongodb/architecture.md` |
| WiredTiger / cache / page faults | `architecture`, `performance` | `02-core-mongodb/storage-engine.md` |
| Read concern / write concern | `architecture`, `replication`, `transactions`, `interview-questions` | `02-core-mongodb/replication.md` |
| Read preference | `architecture`, `replication` | `02-core-mongodb/replication.md` |
| Oplog | `architecture`, `replication`, `interview-questions` | `02-core-mongodb/replication.md` |
| Elections / failover / rollback | `replication`, `interview-questions` | `02-core-mongodb/replication.md` |
| Shard key selection / hot spots | `sharding`, `schema-design`, `interview-questions` | `02-core-mongodb/sharding.md` (distribution); `schema-design.md` (model coupling) |
| Embed vs reference | `schema-design`, `documents`, `interview-questions` | `02-core-mongodb/schema-design.md` |
| `explain` / COLLSCAN / IXSCAN | `indexes`, `performance`, `interview-questions` | `03-query-performance/explain-plan.md` + `query-optimization.md` |
| ESR / compound indexes | `indexes`, `performance`, `interview-questions` | `03-query-performance/indexes.md` |
| Aggregation `$match` first | `aggregation-pipeline`, `performance` | `03-query-performance/aggregation-pipeline.md` |
| Profiler / slow queries | `performance` | `04-production-operations/monitoring.md` |
| mongostat / mongotop | `performance` | `04-production-operations/monitoring.md` |
| Working set / RAM sizing | `performance` | `04-production-operations/capacity-planning.md` |
| Replication lag | `performance` | `04-production-operations/troubleshooting.md` |
| Atlas backup / PITR | `atlas-basics` | `04-production-operations/backup-recovery.md` |
| Atlas Search | `text-search`, `atlas-basics` | `03-query-performance/text-search.md` |
| MongoDB vs PostgreSQL | `interview-questions`, `database-handbook/mongodb-vs-postgresql` | `05-comparisons/mongodb-vs-postgresql.md` (handbook deep dive); link database-handbook |
| mongosh CRUD/rs/sh commands | `mongo-shell-commands`, `crud`, `replication`, `sharding` | Topic pages canonical; shell page demoted |

---

## Weak Files (Quality < 6 or Interview Value < 6)

| File | Issue |
| :--- | :--- |
| `_index.md` | Landing stub only |
| `mongo-shell-commands.md` | Syntax duplication; low architect interview value |
| `interview-questions.md` | 6 answers only; violates Layer 1 model; high duplication |
| `crud.md` | Operator memorization — not senior-interview focus |
| `collections.md` | Admin/shell focus |

---

## Fragmented Concepts (Need Split or Consolidate)

| Concept | Current state | Phase B action |
| :--- | :--- | :--- |
| WiredTiger internals | 2-sentence mentions | **Create** `storage-engine.md` |
| Query planner / index selection | Explain table in `indexes`; bullets in `performance` | **Create** `query-optimization.md` + `explain-plan.md` |
| Production monitoring | 4 lines in `performance` | **Create** `monitoring.md` |
| Troubleshooting runbooks | Symptom table in `performance` only | **Create** `troubleshooting.md` |
| Backup / DR | Atlas PITR bullet | **Create** `backup-recovery.md` |
| Capacity planning | One bullet (working set) | **Create** `capacity-planning.md` |
| Interview Q&A | 6 inline answers | **Replace** with Top 150 + answer layer on topic pages |
| Performance tuning | Mixed with monitoring/capacity | **Narrow** `performance.md` to tuning patterns |

---

## Outdated or Misaligned Content

| Item | Issue |
| :--- | :--- |
| Module yaml | 4 modules — does not match 7-module target |
| Front matter `module` / `sectionRef` | Flat numbering (1.1–4.5) — needs remap after folder move |
| `interview-questions.md` | Uses `interview-answer` shortcode with full answers — conflicts with Layer 1 spec |
| `_index.md` | Describes "cheat sheets" only — undersells handbook depth target |
| `collections.md` | `count()` deprecated note — accurate; keep |
| `geospatial.md` | 2d legacy note — accurate; keep with canonical geospatial page |
| Cross-link to `database-handbook` | Correct pattern — preserve in comparisons module |

---

## External Content (Out of Scope — Link Only)

| Location | Relationship to handbook |
| :--- | :--- |
| `database-handbook/mongodb.md` | **Selection ADR** — when to choose MongoDB; not operational depth |
| `database-handbook/mongodb-vs-postgresql.md` | **Comparison ADR** — link from `05-comparisons/`; avoid duplicating trade-off tables |
| `interview-prep/` | May reference MongoDB — no merge in Phase B |

---

## Phase B Action Summary (Pending Approval)

| Priority | Action |
| :---: | :--- |
| P0 | Create folder structure `01-fundamentals` … `07-learning-paths` |
| P0 | Move 17 topic files to target paths; add Hugo `aliases` for old URLs |
| P0 | Create `storage-engine.md`, `query-optimization.md`, `explain-plan.md` |
| P0 | Create `monitoring.md`, `troubleshooting.md` |
| P0 | Create `top-150-interview-questions.md` (exactly 150, questions only) |
| P0 | Enforce `_meta/concept-registry.md` — trim duplicates to ≤2 sentences + link |
| P1 | Create `backup-recovery.md`, `capacity-planning.md` |
| P1 | Create comparison pages + learning paths (4 files) |
| P1 | Create `architect-questions.md`, `troubleshooting-questions.md`, `performance-questions.md` |
| P1 | Update `mongodb_cheatsheet_modules.yaml` + `mongodb_cheatsheet_order.yaml` |
| P1 | Rewrite section `_index.md` pages + handbook `_index.md` |
| P2 | Upgrade priority pages to 14-section architect template (non-empty sections only) |
| P2 | Answer layer batch 1 (~40 questions on canonical pages) |
| P2 | Demote or remove `mongo-shell-commands.md`; delete `interview-questions.md` |
| P3 | Answer layer batch 2 (remaining 110 questions) |

---

## Phase A Deliverables Checklist

- [x] `_meta/refactoring-plan.md` (this file)
- [x] `_meta/concept-registry.md`
- [x] `_meta/navigation-plan.md`
- [x] `_meta/mermaid-plan.md`
- [x] `_meta/infographic-plan.md`

**Status:** Phase B complete — content restructured; answer layer (Phase C) pending.

---

## Phase B Completion Checklist

- [x] 7-module folder structure (`01-fundamentals` … `07-learning-paths`)
- [x] 15 topic files moved with Hugo `aliases`
- [x] 11 new canonical pages created
- [x] `top-150-interview-questions.md` (exactly 150 questions, no answers)
- [x] `architect-questions.md`, `troubleshooting-questions.md`, `performance-questions.md`
- [x] 4 learning path pages
- [x] Section `_index.md` × 7 + handbook `_index.md` rewritten
- [x] `data/mongodb_cheatsheet_modules.yaml` + `mongodb_cheatsheet_order.yaml` updated
- [x] `scripts/generate_mongodb_handbook_refactor.py` for regeneration
- [x] Removed `mongo-shell-commands.md`, `interview-questions.md`
- [x] Concept registry trimming on `architecture`, `indexes`, `performance`, `replication`
- [x] Answer layer on topic pages (Phase C — all 150 on canonical pages)
- [x] Full Related Topics link audit across all moved pages (→ **See Also** with yaml order)

**Phase C complete** — answer layer, P0 mermaid (8 pages), Top 150 anchor deep dives.

**Phase D complete** — per-question unique answers (`mongodb_top150_unique_answers.py`); re-run `phase_c_mongodb_handbook.py` after answer updates.
