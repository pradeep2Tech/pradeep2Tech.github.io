---
title: "Redis Handbook Mermaid Diagram Plan"
date: 2026-07-03T13:00:00+00:00
draft: true
description: "Diagram opportunities by topic — Phase B/C implementation backlog."
tags: ["redis-cheatsheet", "meta", "planning"]
---

# Mermaid Diagram Plan

**Principle:** Diagrams on **canonical pages only**. Non-canonical pages link to diagram section.

**Existing diagrams (in repo today):** 4 across 4 files.

| File | Diagram type | Topic |
| :--- | :--- | :--- |
| `architecture.md` | `flowchart TB` | Clients → I/O threads → event loop → keyspace → persistence/repl |
| `replication.md` | `flowchart LR` | Primary → replication stream → replicas |
| `streams.md` | `flowchart LR` | Producer → stream → consumer group → XACK |
| `caching-patterns.md` | `flowchart LR` | Cache-aside read path |

---

## 01 Fundamentals

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `architecture.md` | `flowchart TB` | Runtime model | — | **Exists** |
| `architecture.md` | `flowchart LR` | Single instance vs Sentinel vs Cluster topology | P0 | Planned |
| `architecture.md` | `sequenceDiagram` | Command path: client → I/O → event loop → reply | P1 | Planned |
| `data-structures.md` | `flowchart TD` | Type picker decision tree | P1 | Planned |
| `data-structures.md` | — | Skip command tables | P3 | N/A |

---

## 02 Core Redis

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `strings.md` | — | Command quick-ref sufficient | P3 | N/A |
| `hashes.md` | — | Skip unless session layout added | P3 | N/A |
| `lists.md` | `flowchart LR` | Stack vs queue vs blocking consumer | P2 | Planned |
| `lists.md` | `flowchart TD` | List queue vs Streams migration decision | P2 | Planned |
| `sets.md` | — | Skip | P3 | N/A |
| `sorted-sets.md` | `flowchart LR` | Leaderboard / delayed job by score | P2 | Planned |
| `bitmaps.md` | `flowchart TD` | Dense vs sparse user ID → bitmap fit | P2 | Planned |
| `hyperloglog.md` | — | Single-property type — table sufficient | P3 | N/A |

---

## 03 Redis Internals

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `memory-management.md` | `flowchart TB` | robj → encoding → allocator | P0 | Planned |
| `memory-management.md` | `flowchart LR` | ziplist/listpack → hashtable upgrade path | P0 | Planned |
| `memory-management.md` | `flowchart TD` | Fragmentation triage (`mem_fragmentation_ratio`) | P1 | Planned |
| `redis-protocol.md` | `sequenceDiagram` | RESP request/response round trip | P0 | Planned |
| `redis-protocol.md` | `sequenceDiagram` | Pipelining: N commands, 1 RTT | P0 | Planned |
| `persistence.md` | `flowchart TB` | RDB vs AOF vs hybrid decision | P0 | Planned |
| `persistence.md` | `sequenceDiagram` | BGSAVE fork + copy-on-write | P0 | Planned |
| `persistence.md` | `sequenceDiagram` | AOF rewrite cycle | P1 | Planned |
| `replication.md` | `flowchart LR` | Replication stream | — | **Exists** |
| `replication.md` | `sequenceDiagram` | Full sync vs partial resync | P0 | Planned |
| `replication.md` | `sequenceDiagram` | `WAIT` after write for durability | P1 | Planned |
| `sentinel.md` | `flowchart TB` | Sentinel quorum monitoring topology | P0 | Planned |
| `sentinel.md` | `sequenceDiagram` | Failover: SDOWN → ODOWN → promote replica | P0 | Planned |
| `cluster.md` | `flowchart TB` | 16384 slots across primaries + replicas | P0 | Planned |
| `cluster.md` | `sequenceDiagram` | MOVED redirect on wrong node | P1 | Planned |
| `cluster.md` | `sequenceDiagram` | Resharding: ASK vs MOVED | P1 | Planned |
| `cluster.md` | `flowchart LR` | Hash tag colocation for multi-key ops | P1 | Planned |

---

## 04 Distributed Systems

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `distributed-lock.md` | `sequenceDiagram` | Acquire → work → token-checked release | P0 | Planned |
| `distributed-lock.md` | `sequenceDiagram` | TTL expiry + stale writer (fencing need) | P0 | Planned |
| `transactions.md` | `sequenceDiagram` | WATCH → MULTI → EXEC abort on conflict | P1 | Planned |
| `transactions.md` | `flowchart LR` | Pipeline vs MULTI/EXEC vs Lua | P1 | Planned |
| `pub-sub.md` | `flowchart LR` | Publisher → channel → N subscribers | P1 | Planned |
| `streams.md` | `flowchart LR` | Consumer group flow | — | **Exists** |
| `streams.md` | `sequenceDiagram` | Pending → XCLAIM reclaim after crash | P0 | Planned |
| `lua-scripts.md` | `sequenceDiagram` | Script atomicity vs interleaved commands | P1 | Planned |

---

## 05 Production Patterns

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `caching-patterns.md` | `flowchart LR` | Cache-aside | — | **Exists** |
| `caching-patterns.md` | `flowchart LR` | Write-through vs write-behind overview | P1 | Planned |
| `cache-invalidation.md` | `sequenceDiagram` | DB write → cache delete/update paths | P0 | Planned |
| `cache-breakdown.md` | `sequenceDiagram` | Hot key thundering herd | P0 | Planned |
| `cache-avalanche.md` | `flowchart TD` | Synchronized TTL expiry storm | P0 | Planned |
| `cache-penetration.md` | `flowchart LR` | Miss → DB flood → Bloom filter guard | P0 | Planned |
| `session-store.md` | `flowchart LR` | LB → stateless app → Redis session hash | P2 | Planned |
| `rate-limiter.md` | `flowchart TB` | Fixed vs sliding vs token bucket | P1 | Planned |

---

## 06 Performance & Operations

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `performance-tuning.md` | `flowchart TB` | Latency layers: network → command → single thread | P0 | Planned |
| `performance-tuning.md` | `flowchart LR` | Pipeline vs transaction throughput | P1 | Planned |
| `monitoring.md` | `flowchart LR` | INFO → slowlog → latency doctor pipeline | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | High memory usage decision tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Replication lag triage tree | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Hot key / slow command triage | P0 | Planned |
| `troubleshooting.md` | `flowchart TD` | Cluster slot imbalance triage | P1 | Planned |
| `capacity-planning.md` | `flowchart TB` | Memory sizing: keys × overhead + replication | P0 | Planned |
| `capacity-planning.md` | `flowchart LR` | When to scale up vs Cluster out | P1 | Planned |
| `eviction-policies.md` | `flowchart TD` | Policy picker (volatile vs allkeys, LRU vs LFU) | P1 | Planned |

---

## 07 Comparisons

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `redis-vs-memcached.md` | `flowchart TD` | Rich types + persistence vs pure cache | P1 | Planned |
| `redis-vs-kafka.md` | `flowchart TD` | Streams vs Kafka log retention/scale | P1 | Planned |
| `redis-vs-rabbitmq.md` | `flowchart TD` | Task queue routing vs Redis list/stream | P1 | Planned |

---

## 08 Interview Guide

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `top-150-interview-questions.md` | — | Link to topic diagrams only | P3 | N/A |
| `redis-interview-revision-path.md` | `flowchart LR` | Revision order by topic cluster | P2 | Planned |

---

## Diagram Quality Rules (Phase B)

1. Max **2 diagrams per page** in initial pass; add more in Phase C if needed.
2. Prefer `sequenceDiagram` for failover, replication, locks, cache races, protocol.
3. Prefer `flowchart TD` for troubleshooting decision trees and policy pickers.
4. No diagram-only pages — always paired with prose.
5. Alt text via adjacent heading (Hugo/Mermaid accessibility).

---

## Priority Summary

| Priority | Count | Focus |
| :---: | :---: | :--- |
| P0 | 22 | memory-management, protocol, persistence fork, replication resync, sentinel failover, cluster slots, cache failure modes, monitoring, troubleshooting trees, capacity |
| P1 | 16 | Architecture topology, resharding, transactions, rate limiter, eviction picker, comparisons |
| P2 | 8 | Lists/streams migration, bitmaps, session, interview revision path |
| P3 | 6 | Core type command pages skip |

**Phase B minimum:** All P0 diagrams on new canonical pages + preserve 4 existing diagrams.  
**Phase C:** P1–P2 backlog on upgraded topic pages.
