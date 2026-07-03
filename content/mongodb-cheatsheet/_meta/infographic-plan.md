---
title: "MongoDB Handbook Infographic Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["mongodb-cheatsheet", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, and optional future static images — not separate image assets unless generated later.

**Meta files:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Quick revision sheet | Markdown table + bullets | Page **Quick Revision** section or `07-learning-paths/mongodb-interview-revision-path.md` |
| Comparison one-pager | Markdown table + comparison-table shortcode if available | `05-comparisons/*` |
| Decision tree | Mermaid `flowchart TD` | `schema-design`, `sharding`, `troubleshooting`, comparisons |
| Troubleshooting flowchart | Mermaid `flowchart TD` | `04-production-operations/troubleshooting.md` |
| Interview cheat sheet | Single-page categorized table | `06-interview-guide/top-150-interview-questions.md` |
| Architecture poster | Mermaid `flowchart TB` | `architecture`, `storage-engine`, `replication` |
| Ops runbook card | Symptom → cause → fix table | `troubleshooting.md`, `monitoring.md` |

---

## By Module

### 01 Fundamentals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| BSON type picker | Type → use-when table | `documents.md` | P2 |
| Collection type matrix | Standard / capped / time series / view | `collections.md` | P2 |
| Atlas tier card | M0 / Flex / M10+ feature matrix | `atlas-basics.md` | P1 |
| Atlas connectivity | SRV vs standard URI / PrivateLink | `atlas-basics.md` | P2 |

### 02 Core MongoDB

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Deployment modes | Standalone / RS / sharded one-pager | `architecture.md` | P0 |
| WiredTiger stack | Cache / journal / checkpoint layers | `storage-engine.md` | P0 |
| Compression codecs | snappy vs zlib vs zstd tradeoffs | `storage-engine.md` | P1 |
| Replica set roles | Primary / secondary / arbiter / hidden / delayed | `replication.md` | P0 |
| Read & write concern matrix | Level × durability × latency | `replication.md` | P0 |
| Read preference card | Mode × use case × staleness risk | `replication.md` | P1 |
| Oplog sizing formula | Write rate × maintenance window | `replication.md` | P1 |
| Shard key patterns | Hashed vs ranged vs compound pros/cons | `sharding.md` | P0 |
| Chunk lifecycle | split → migrate → balance | `sharding.md` | P0 |
| Zone sharding map | Region → shard mapping | `sharding.md` | P2 |
| Transaction scope card | Single-doc vs multi-doc vs cross-shard | `transactions.md` | P1 |
| Embed vs reference | Decision tree (exists as mermaid) | `schema-design.md` | — Exists |
| Bucketing pattern | Time-series doc layout example | `schema-design.md` | P1 |
| Schema anti-patterns | Unbounded arrays, mega-doc, over-normalize | `schema-design.md` | P1 |

### 03 Query & Performance

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Index type matrix | Type × query pattern × shard suitability | `indexes.md` | P0 |
| ESR rule card | Equality → Sort → Range examples | `indexes.md` | P0 |
| Covered query checklist | Filter + projection ⊆ index keys | `query-optimization.md` | P0 |
| Planner flow | Parse → plan cache → winning plan | `query-optimization.md` | P0 |
| Explain metrics card | Key fields to read in `executionStats` | `explain-plan.md` | P0 |
| COLLSCAN vs IXSCAN | When each appears + fix | `explain-plan.md` | P0 |
| Aggregation optimization | `$match` first, `$lookup` index, `allowDiskUse` | `aggregation-pipeline.md` | P1 |
| TTL patterns | Session / event expiry recipes | `ttl-index.md` | P2 |
| Text vs Atlas Search | Feature comparison table | `text-search.md` | P1 |
| Geo coordinate reminder | lng,lat order + index requirement | `geospatial.md` | P2 |

### 04 Production Operations

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Performance tuning layers | Query → index → schema → RAM → topology | `performance.md` | P0 |
| Connection pool sizing | instances × poolSize ≤ mongod capacity | `performance.md` | P1 |
| Monitoring toolkit | mongostat / mongotop / profiler / Atlas | `monitoring.md` | P0 |
| Slow query triage | Symptom → explain → index fix flow | `monitoring.md` | P0 |
| Replication lag runbook | Cause → metric → action table | `troubleshooting.md` | P0 |
| Hot shard runbook | Monotonic key → chunk split imbalance | `troubleshooting.md` | P0 |
| OOM / page fault runbook | Working set > RAM → remedy | `troubleshooting.md` | P0 |
| Election failure runbook | Split brain / priority / network | `troubleshooting.md` | P1 |
| Backup method matrix | mongodump vs snapshot vs PITR | `backup-recovery.md` | P1 |
| DR RPO/RTO card | Backup tier → recovery time | `backup-recovery.md` | P1 |
| RAM sizing worksheet | Working set + indexes + connections | `capacity-planning.md` | P0 |
| Shard count heuristic | Data size + write throughput triggers | `capacity-planning.md` | P1 |

### 05 Comparisons

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| MongoDB vs PostgreSQL | Document flexibility vs SQL/ACID/joins | `mongodb-vs-postgresql.md` | P0 |
| MongoDB vs Cassandra | Tunable consistency vs flexible docs | `mongodb-vs-cassandra.md` | P1 |
| MongoDB vs Couchbase | Mobile/edge cache vs general document store | `mongodb-vs-couchbase.md` | P2 |
| Cross-link card | Link to database-handbook ADR pages | All comparison pages | P1 |

### 06 Interview Guide

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 150 index | Category × count × deep dive link | `top-150-interview-questions.md` | P0 |
| Question distribution | Architecture 40 / Troubleshooting 30 / Performance 25 / Reliability 20 / Security 15 | `top-150-interview-questions.md` | P0 |
| Architect top picks | 25-question subset table | `architect-questions.md` | P1 |
| Troubleshooting drills | 25 scenario questions | `troubleshooting-questions.md` | P1 |
| Performance drills | 25 tuning questions | `performance-questions.md` | P1 |

### 07 Learning Paths

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Senior engineer path | Week-by-week topic order | `mongodb-senior-engineer-path.md` | P1 |
| Lead path | Ops + performance + troubleshooting emphasis | `mongodb-lead-path.md` | P1 |
| Architect path | Schema + sharding + comparisons + ADR | `mongodb-architect-path.md` | P1 |
| Interview revision | 48-hour cram schedule + topic clusters | `mongodb-interview-revision-path.md` | P0 |

---

## Existing Assets to Preserve (Phase B)

| Asset | Source file | Action |
| :--- | :--- | :--- |
| Deployment topology mermaid | `architecture.md` | Keep on canonical page |
| Oplog flow mermaid | `replication.md` | Keep; add election diagram |
| Sharding topology mermaid | `sharding.md` | Keep; add migration diagram |
| Schema decision mermaid | `schema-design.md` | Keep |
| Pipeline stage mermaid | `aggregation-pipeline.md` | Keep |
| Geo operator mermaid | `geospatial.md` | Keep |
| BSON path mermaid | `documents.md` | Keep |
| Transaction sequence | `transactions.md` | Keep |
| RC/WC tables | `architecture.md` | **Move** to `replication.md`; replace with link card |
| ESR / explain table | `indexes.md` | Split: ESR stays; explain → `explain-plan.md` |
| Symptom table | `performance.md` | **Move** to `troubleshooting.md` |
| Shard key pros/cons table | `sharding.md` | Keep |
| Text vs Atlas Search table | `text-search.md` | Keep |

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
| Scalability | Shard / RS scaling heuristic |
| Reliability | RC/WC matrix |
| Security | Layer diagram (Phase C) |
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
| Architecture | 40 | `02-core-mongodb/` |
| Troubleshooting | 30 | `04-production-operations/troubleshooting.md` |
| Performance | 25 | `03-query-performance/`, `04-production-operations/performance.md` |
| Reliability | 20 | `02-core-mongodb/replication.md`, `backup-recovery.md` |
| Security | 15 | `atlas-basics.md` (+ Phase C security page) |

---

## Phase Rollout

| Phase | Deliverable |
| :--- | :--- |
| **B** | P0 infographics on all new pages; preserve existing mermaids; Top 150 category table |
| **C** | P1 comparison one-pagers; learning path schedules; security depth |
| **D** | Optional static PNG exports from Mermaid for social/share (out of scope unless requested) |

---

## Out of Scope

- Custom SVG illustration files
- Non-MongoDB handbook infographics
- Modifying `database-handbook` comparison visuals
