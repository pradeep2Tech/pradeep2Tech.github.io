---
title: "Database Internals & System Design Masterclass"
date: 2026-06-28T10:00:00+00:00
draft: false
description: "Deep dives into storage engines, distributed coordination patterns, schema evolution, query optimization, and vector indexing — from B+ trees to HNSW."
tags: ["database-internals", "postgresql", "sqlite", "storage-engines", "distributed-systems"]
databaseInternalsTocPageSize: 14
ShowPageNums: true
---

A structured masterclass covering the full stack of database engineering — from on-disk B+ tree mechanics and SQLite internals through distributed outbox/inbox patterns, enterprise schema evolution, query optimization, and AI vector indexing.

## Curriculum Overview

| Module | Technical Focus Area | Stubs |
| :----: | :--- | :--- |
| **1** | Local Storage Layer & Embedded Engines | `b-plus-tree-storage-mechanics.md` · `sqlite-architecture-teardown.md` · `acid-two-phase-commit-journaling.md` |
| **2** | Distributed State & Asynchronous Coordination Patterns | `transactional-outbox-pattern.md` · `transactional-inbox-pattern.md` · `outbox-inbox-performance-tuning.md` |
| **3** | Enterprise Relational Schema Architecture & Evolution | `primary-key-selection-strategies.md` · `advanced-schema-optimization.md` · `zero-downtime-migration-frameworks.md` |
| **4** | Query Optimization, Indexing Engines, & Concurrency Control | `cost-based-query-optimization.md` · `local-concurrency-mvcc.md` · `lock-graphs-deadlocks-latching.md` |
| **5** | Distributed Topology Architectures & AI Vector Systems | `distributed-consistency-primitives.md` · `ai-vector-indexing-rag-scaling.md` |

## Topic Index

| Module | Technical Focus Area | Topics |
| :----: | :--- | :--- |
| **1** | Local Storage Layer & Embedded Engines | [1.1 B/B+ Tree Storage Mechanics](/database-internals/b-plus-tree-storage-mechanics/) · [1.2 SQLite Architecture Teardown](/database-internals/sqlite-architecture-teardown/) · [1.3 Two-Phase Commit Journaling](/database-internals/acid-two-phase-commit-journaling/) |
| **2** | Distributed State & Asynchronous Coordination Patterns | [2.1 Transactional Outbox](/database-internals/transactional-outbox-pattern/) · [2.2 Transactional Inbox](/database-internals/transactional-inbox-pattern/) · [2.3 Outbox/Inbox Performance Tuning](/database-internals/outbox-inbox-performance-tuning/) |
| **3** | Enterprise Relational Schema Architecture & Evolution | [3.1 Primary Key Selection](/database-internals/primary-key-selection-strategies/) · [3.2 Schema Optimization Primitives](/database-internals/advanced-schema-optimization/) · [3.3 Zero-Downtime Migrations](/database-internals/zero-downtime-migration-frameworks/) |
| **4** | Query Optimization, Indexing Engines, & Concurrency Control | [4.1 Query Optimization & Execution Plans](/database-internals/cost-based-query-optimization/) · [4.2 Concurrency Isolation & MVCC](/database-internals/local-concurrency-mvcc/) · [4.3 Lock Graphs & Deadlocks](/database-internals/lock-graphs-deadlocks-latching/) |
| **5** | Distributed Topology Architectures & AI Vector Systems | [5.1 Distributed Consistency Primitives](/database-internals/distributed-consistency-primitives/) · [5.2 AI Vector Indexing & RAG](/database-internals/ai-vector-indexing-rag-scaling/) |
