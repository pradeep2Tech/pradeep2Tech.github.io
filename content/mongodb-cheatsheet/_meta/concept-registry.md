---
title: "MongoDB Concept Registry"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per MongoDB concept."
tags: ["mongodb-cheatsheet", "meta", "planning"]
---

# MongoDB Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase A — registry defined; enforcement in Phase B.

**Path convention:** Relative to `content/mongodb-cheatsheet/` (target paths shown).

---

## 01 Fundamentals — Data Model

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| BSON document model | `01-fundamentals/documents.md` | Exists (move) | |
| `_id` / `ObjectId` | `01-fundamentals/documents.md` | Exists (move) | |
| Dot notation / array paths | `01-fundamentals/documents.md` | Exists (move) | |
| 16 MB document limit | `01-fundamentals/documents.md` | Exists (move) | Also cite in schema-design for design impact |
| Collection / database namespace | `01-fundamentals/collections.md` | Exists (move) | |
| JSON Schema validation | `01-fundamentals/collections.md` | Exists (move) | |
| Capped collections | `01-fundamentals/collections.md` | Exists (move) | |
| Time series collections | `01-fundamentals/collections.md` | Exists (move) | |
| Change streams (concept) | `01-fundamentals/collections.md` | Exists (move) | Internals → replication |
| CRUD operations | `01-fundamentals/crud.md` | Exists (move) | Syntax only — not interview depth |
| Query operators | `01-fundamentals/crud.md` | Exists (move) | |
| Update operators | `01-fundamentals/crud.md` | Exists (move) | |
| Bulk writes | `01-fundamentals/crud.md` | Exists (move) | |
| MongoDB Atlas (managed service) | `01-fundamentals/atlas-basics.md` | Exists (move) | Ops depth → production module |
| `mongodb+srv` connection | `01-fundamentals/atlas-basics.md` | Exists (move) | |
| Atlas cluster tiers (M0/M10+) | `01-fundamentals/atlas-basics.md` | Exists (move) | |
| Atlas Search (product) | `01-fundamentals/atlas-basics.md` | Exists (move) | Query DSL → text-search |
| Atlas Triggers / Data Federation | `01-fundamentals/atlas-basics.md` | Exists (move) | Expand Phase B |

---

## 02 Core MongoDB — Architecture & Platform

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| `mongod` / `mongos` / config servers | `02-core-mongodb/architecture.md` | Exists (move) | **Primary** topology source |
| Standalone vs replica set vs sharded | `02-core-mongodb/architecture.md` | Exists (move) | |
| Deployment topology diagram | `02-core-mongodb/architecture.md` | Exists (move) | |
| WiredTiger storage engine | `02-core-mongodb/storage-engine.md` | **Planned** | Strip from architecture + performance |
| MVCC (document-level) | `02-core-mongodb/storage-engine.md` | **Planned** | |
| Checkpoints | `02-core-mongodb/storage-engine.md` | **Planned** | |
| Journaling (`journal`, `j` write concern) | `02-core-mongodb/storage-engine.md` | **Planned** | Link write concern → replication |
| Compression (snappy/zlib/zstd) | `02-core-mongodb/storage-engine.md` | **Planned** | |
| WiredTiger cache / eviction | `02-core-mongodb/storage-engine.md` | **Planned** | Capacity → capacity-planning |
| Document-level locking | `02-core-mongodb/storage-engine.md` | **Planned** | |
| Replica set | `02-core-mongodb/replication.md` | Exists (move) | |
| Primary / secondary roles | `02-core-mongodb/replication.md` | Exists (move) | |
| Oplog (`local.oplog.rs`) | `02-core-mongodb/replication.md` | Exists (move) | **Primary** oplog source |
| Elections / Raft-style voting | `02-core-mongodb/replication.md` | Exists (move) | Expand Phase B |
| Rollback | `02-core-mongodb/replication.md` | Exists (move) | |
| Read concern (`local`, `majority`, `linearizable`) | `02-core-mongodb/replication.md` | Exists (move) | Strip from architecture |
| Write concern (`w`, `j`, `wtimeout`) | `02-core-mongodb/replication.md` | Exists (move) | |
| Read preference | `02-core-mongodb/replication.md` | Exists (move) | |
| Arbiter / hidden / delayed nodes | `02-core-mongodb/replication.md` | Exists (move) | |
| Change streams (replication dependency) | `02-core-mongodb/replication.md` | Exists (move) | |
| Sharding / horizontal scale | `02-core-mongodb/sharding.md` | Exists (move) | |
| Shard key | `02-core-mongodb/sharding.md` | Exists (move) | **Primary** shard key source |
| Chunks / chunk ranges | `02-core-mongodb/sharding.md` | Exists (move) | |
| Balancer | `02-core-mongodb/sharding.md` | Exists (move) | |
| Chunk migration | `02-core-mongodb/sharding.md` | Exists (move) | Expand Phase B |
| Targeted vs scatter-gather queries | `02-core-mongodb/sharding.md` | Exists (move) | |
| Zone sharding | `02-core-mongodb/sharding.md` | Exists (move) | |
| Jumbo chunks | `02-core-mongodb/sharding.md` | Exists (move) | Troubleshooting link |
| Unique indexes on sharded collections | `02-core-mongodb/sharding.md` | Exists (move) | |
| Multi-document transactions | `02-core-mongodb/transactions.md` | Exists (move) | |
| Sessions / snapshot isolation | `02-core-mongodb/transactions.md` | Exists (move) | |
| Retryable writes | `02-core-mongodb/transactions.md` | Exists (move) | |
| Cross-shard transactions | `02-core-mongodb/transactions.md` | Exists (move) | |
| Embed vs reference | `02-core-mongodb/schema-design.md` | Exists (move) | **Primary** schema source |
| Bucketing pattern | `02-core-mongodb/schema-design.md` | Exists (move) | |
| Polymorphic schema / discriminator | `02-core-mongodb/schema-design.md` | Exists (move) | |
| Access-pattern-first modeling | `02-core-mongodb/schema-design.md` | Exists (move) | |
| Schema + shard key coupling | `02-core-mongodb/schema-design.md` | Exists (move) | Link sharding |

---

## 03 Query & Performance

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Index types (single, compound, multikey) | `03-query-performance/indexes.md` | Exists (move) | |
| ESR rule (Equality, Sort, Range) | `03-query-performance/indexes.md` | Exists (move) | |
| Partial / sparse / wildcard indexes | `03-query-performance/indexes.md` | Exists (move) | |
| Hashed indexes | `03-query-performance/indexes.md` | Exists (move) | Shard key link |
| Covered queries | `03-query-performance/query-optimization.md` | **Planned** | Brief mention in indexes today |
| Index intersection | `03-query-performance/query-optimization.md` | **Planned** | |
| Query planner | `03-query-performance/query-optimization.md` | **Planned** | |
| Index selection | `03-query-performance/query-optimization.md` | **Planned** | |
| COLLSCAN vs IXSCAN | `03-query-performance/query-optimization.md` | **Planned** | Explain detail → explain-plan |
| Aggregation pipeline optimization | `03-query-performance/query-optimization.md` | **Planned** | `$match` early, `$lookup` indexes |
| `explain()` / `executionStats` | `03-query-performance/explain-plan.md` | **Planned** | |
| `winningPlan` / `rejectedPlans` | `03-query-performance/explain-plan.md` | **Planned** | |
| `totalDocsExamined` / `nReturned` ratio | `03-query-performance/explain-plan.md` | **Planned** | |
| `PROJECTION_COVERED` stage | `03-query-performance/explain-plan.md` | **Planned** | |
| TTL indexes | `03-query-performance/ttl-index.md` | Exists (move) | |
| Text indexes / `$text` | `03-query-performance/text-search.md` | Exists (move) | |
| Atlas Search `$search` stage | `03-query-performance/text-search.md` | Exists (move) | |
| GeoJSON / 2dsphere | `03-query-performance/geospatial.md` | Exists (move) | |
| `$geoNear` / `$geoWithin` | `03-query-performance/geospatial.md` | Exists (move) | |
| Aggregation framework | `03-query-performance/aggregation-pipeline.md` | Exists (move) | **Primary** pipeline source |
| `$match`, `$group`, `$lookup`, `$facet` | `03-query-performance/aggregation-pipeline.md` | Exists (move) | |
| `allowDiskUse` / 100 MB stage limit | `03-query-performance/aggregation-pipeline.md` | Exists (move) | |

---

## 04 Production Operations

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Performance tuning (holistic) | `04-production-operations/performance.md` | Exists (move, narrow) | Strip monitoring/capacity |
| Connection pooling | `04-production-operations/performance.md` | Exists (move) | |
| Pagination without large `skip` | `04-production-operations/performance.md` | Exists (move) | |
| Bulk insert patterns | `04-production-operations/performance.md` | Exists (move) | |
| `mongostat` | `04-production-operations/monitoring.md` | **Planned** | |
| `mongotop` | `04-production-operations/monitoring.md` | **Planned** | |
| Atlas metrics / alerts | `04-production-operations/monitoring.md` | **Planned** | |
| Replication lag monitoring | `04-production-operations/monitoring.md` | **Planned** | |
| Profiler / slow query analysis | `04-production-operations/monitoring.md` | **Planned** | |
| `$indexStats` | `04-production-operations/monitoring.md` | **Planned** | |
| `db.currentOp()` | `04-production-operations/monitoring.md` | **Planned** | |
| Replication lag (remediation) | `04-production-operations/troubleshooting.md` | **Planned** | |
| Slow queries (remediation) | `04-production-operations/troubleshooting.md` | **Planned** | |
| Chunk imbalance / jumbo chunks | `04-production-operations/troubleshooting.md` | **Planned** | |
| OOM / cache pressure | `04-production-operations/troubleshooting.md` | **Planned** | |
| Lock contention | `04-production-operations/troubleshooting.md` | **Planned** | |
| Election issues / split brain | `04-production-operations/troubleshooting.md` | **Planned** | |
| `mongodump` / `mongorestore` | `04-production-operations/backup-recovery.md` | **Planned** | |
| Atlas backup / snapshots | `04-production-operations/backup-recovery.md` | **Planned** | |
| Point-in-time recovery (PITR) | `04-production-operations/backup-recovery.md` | **Planned** | |
| Oplog-based recovery | `04-production-operations/backup-recovery.md` | **Planned** | |
| Disaster recovery runbook | `04-production-operations/backup-recovery.md` | **Planned** | |
| Working set | `04-production-operations/capacity-planning.md` | **Planned** | |
| Memory / RAM sizing | `04-production-operations/capacity-planning.md` | **Planned** | |
| Storage planning | `04-production-operations/capacity-planning.md` | **Planned** | |
| Growth planning | `04-production-operations/capacity-planning.md` | **Planned** | |
| Shard sizing | `04-production-operations/capacity-planning.md` | **Planned** | |

---

## 05 Comparisons

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| MongoDB vs PostgreSQL tradeoffs | `05-comparisons/mongodb-vs-postgresql.md` | **Planned** | Link [database-handbook](/database-handbook/mongodb-vs-postgresql/) |
| MongoDB vs Cassandra | `05-comparisons/mongodb-vs-cassandra.md` | **Planned** | |
| MongoDB vs Couchbase | `05-comparisons/mongodb-vs-couchbase.md` | **Planned** | |
| When to choose MongoDB (ADR) | `database-handbook/mongodb.md` | External | Out of scope — link only |

---

## 06 Interview Guide

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Top 150 questions (Layer 1) | `06-interview-guide/top-150-interview-questions.md` | **Planned** | Questions only |
| Architect question subset | `06-interview-guide/architect-questions.md` | **Planned** | |
| Troubleshooting question subset | `06-interview-guide/troubleshooting-questions.md` | **Planned** | |
| Performance question subset | `06-interview-guide/performance-questions.md` | **Planned** | |
| Structured answers (Layer 2) | Topic pages per question mapping | **Planned** | `## Question` blocks |

---

## 07 Learning Paths

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Senior engineer path | `07-learning-paths/mongodb-senior-engineer-path.md` | **Planned** | |
| Technical lead path | `07-learning-paths/mongodb-lead-path.md` | **Planned** | |
| Architect path | `07-learning-paths/mongodb-architect-path.md` | **Planned** | |
| Interview revision path | `07-learning-paths/mongodb-interview-revision-path.md` | **Planned** | |

---

## Cross-Cutting — Security & Observability

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| RBAC / roles | `01-fundamentals/atlas-basics.md` | Partial | Expand or add security section Phase C |
| TLS / encryption in transit | `01-fundamentals/atlas-basics.md` | Partial | |
| Encryption at rest (Atlas) | `01-fundamentals/atlas-basics.md` | Partial | |
| IP allowlist / VPC peering / PrivateLink | `01-fundamentals/atlas-basics.md` | Exists (move) | |
| Auditing | — | **Gap** | Phase C candidate |
| Field-level encryption | — | **Gap** | Phase C candidate |

---

## Deprecated / Demoted

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| mongosh command reference | `mongo-shell-commands.md` → demote | Exists | Not canonical for any concept |
| Legacy `interview-questions.md` | Delete after migration | Exists | Replaced by `06-interview-guide/` |

---

## Enforcement Checklist (Phase B)

- [ ] Each concept row has exactly one **Exists** or **Planned** canonical page
- [ ] Non-canonical pages audited for ≤2 sentence mentions
- [ ] Top 150 questions map to canonical answer locations
- [ ] `database-handbook` links preserved — no duplicate comparison essays
