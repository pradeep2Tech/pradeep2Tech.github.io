---
title: "MongoDB Handbook Mermaid Diagram Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Diagram opportunities by topic — Phase B/C implementation backlog."
tags: ["mongodb-cheatsheet", "meta", "planning"]
---

# Mermaid Diagram Plan

**Principle:** Diagrams on **canonical pages only**. Non-canonical pages link to diagram section.

**Existing diagrams (in repo today):** 6 across 5 files.

| File | Diagram type | Topic |
| :--- | :--- | :--- |
| `architecture.md` | `flowchart TB` | App → driver → mongos/replica set |
| `documents.md` | `flowchart LR` | Document field paths |
| `geospatial.md` | `flowchart LR` | 2dsphere → geo operators |
| `aggregation-pipeline.md` | `flowchart LR` | Pipeline stages |
| `replication.md` | `flowchart LR` | Primary → oplog → secondaries |
| `sharding.md` | `flowchart TB` | mongos → shards + balancer |
| `schema-design.md` | `flowchart TD` | Embed vs reference decision |
| `transactions.md` | `sequenceDiagram` | Transaction commit flow |

---

## 01 Fundamentals

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `documents.md` | `flowchart LR` | BSON types / nesting | — | **Exists** |
| `collections.md` | `flowchart TB` | Collection types (standard, capped, time series, view) | P2 | Planned |
| `crud.md` | — | Skip — operator tables sufficient | P3 | N/A |
| `atlas-basics.md` | `flowchart LR` | App → Atlas cluster → cloud provider | P1 | Planned |
| `atlas-basics.md` | `flowchart TB` | Atlas tier selection (M0 vs M10+) | P2 | Planned |

---

## 02 Core MongoDB

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `architecture.md` | `flowchart TB` | Deployment topology | — | **Exists** |
| `architecture.md` | `flowchart LR` | Standalone vs RS vs sharded decision | P1 | Planned |
| `storage-engine.md` | `flowchart TB` | WiredTiger: cache → disk → journal | P0 | Planned |
| `storage-engine.md` | `sequenceDiagram` | Write path: RAM → journal → checkpoint | P0 | Planned |
| `storage-engine.md` | `flowchart LR` | MVCC snapshot read vs write | P1 | Planned |
| `replication.md` | `flowchart LR` | Oplog tailing | — | **Exists** |
| `replication.md` | `sequenceDiagram` | Election on primary failure | P0 | Planned |
| `replication.md` | `sequenceDiagram` | Rollback after failover | P1 | Planned |
| `replication.md` | `flowchart TB` | Read concern levels vs visibility | P1 | Planned |
| `sharding.md` | `flowchart TB` | mongos routing | — | **Exists** |
| `sharding.md` | `sequenceDiagram` | Chunk migration between shards | P0 | Planned |
| `sharding.md` | `flowchart LR` | Targeted vs scatter-gather query paths | P1 | Planned |
| `sharding.md` | `flowchart TB` | Hot shard (monotonic key) vs balanced | P1 | Planned |
| `transactions.md` | `sequenceDiagram` | 2PC commit | — | **Exists** |
| `transactions.md` | `sequenceDiagram` | Cross-shard transaction coordination | P2 | Planned |
| `schema-design.md` | `flowchart TD` | Embed/reference decision | — | **Exists** |
| `schema-design.md` | `erDiagram` | Parent-child embed vs ref models | P2 | Planned |

---

## 03 Query & Performance

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `indexes.md` | `flowchart LR` | ESR compound index field order | P1 | Planned |
| `indexes.md` | `flowchart TB` | Multikey index on array field | P2 | Planned |
| `query-optimization.md` | `flowchart TD` | Query planner: parse → plan → execute | P0 | Planned |
| `query-optimization.md` | `flowchart LR` | COLLSCAN vs IXSCAN decision | P0 | Planned |
| `explain-plan.md` | `flowchart TB` | `winningPlan` stage tree anatomy | P0 | Planned |
| `explain-plan.md` | `flowchart LR` | `totalDocsExamined` vs `nReturned` | P1 | Planned |
| `aggregation-pipeline.md` | `flowchart LR` | Pipeline stages | — | **Exists** |
| `aggregation-pipeline.md` | `flowchart TB` | `$lookup` + index on foreignField | P1 | Planned |
| `ttl-index.md` | `sequenceDiagram` | TTL monitor delete cycle | P2 | Planned |
| `text-search.md` | `flowchart LR` | `$text` vs Atlas Search paths | P2 | Planned |
| `geospatial.md` | `flowchart LR` | Geo operators | — | **Exists** |

---

## 04 Production Operations

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `performance.md` | `flowchart TB` | Tuning layers: query → schema → hardware | P1 | Planned |
| `monitoring.md` | `flowchart LR` | Telemetry: mongostat → profiler → Atlas | P0 | Planned |
| `monitoring.md` | `sequenceDiagram` | Slow query detection flow | P1 | Planned |
| `troubleshooting.md` | `flowchart TD` | Replication lag decision tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Slow query triage tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Chunk imbalance / jumbo chunk triage | P1 | Planned |
| `troubleshooting.md` | `flowchart TD` | OOM / cache pressure triage | P1 | Planned |
| `backup-recovery.md` | `sequenceDiagram` | PITR restore timeline | P1 | Planned |
| `backup-recovery.md` | `flowchart LR` | Backup types: dump vs snapshot vs oplog | P1 | Planned |
| `capacity-planning.md` | `flowchart TB` | Working set vs RAM | P0 | Planned |
| `capacity-planning.md` | `flowchart LR` | When to shard (vertical → horizontal) | P1 | Planned |

---

## 05 Comparisons

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `mongodb-vs-postgresql.md` | `quadrantChart` or `flowchart TD` | Document vs relational fit | P1 | Planned |
| `mongodb-vs-cassandra.md` | `flowchart TD` | Write scale / tunable consistency | P2 | Planned |
| `mongodb-vs-couchbase.md` | `flowchart TD` | JSON doc + cache co-location | P2 | Planned |

---

## 06 Interview Guide

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `top-150-interview-questions.md` | — | Link to topic diagrams only | P3 | N/A |
| `mongodb-interview-revision-path.md` | `flowchart LR` | Revision order by topic cluster | P2 | Planned |

---

## Diagram Quality Rules (Phase B)

1. Max **2 diagrams per page** in initial pass; add more in Phase C if needed.
2. Prefer `sequenceDiagram` for failover, elections, migrations, transactions.
3. Prefer `flowchart TD` for troubleshooting decision trees.
4. No diagram-only pages — always paired with prose.
5. Alt text via adjacent heading (Hugo/Mermaid accessibility).

---

## Priority Summary

| Priority | Count | Focus |
| :---: | :---: | :--- |
| P0 | 12 | storage-engine, elections, chunk migration, query planner, explain, monitoring, troubleshooting trees, working set |
| P1 | 18 | Architecture decisions, replication depth, performance layers, backup, comparisons |
| P2 | 12 | Specialist indexes, TTL, text search, schema ER, cross-shard txn |
| P3 | 4 | CRUD skip, interview index skip |

**Phase B minimum:** All P0 diagrams on new canonical pages.  
**Phase C:** P1–P2 backlog on upgraded topic pages.
