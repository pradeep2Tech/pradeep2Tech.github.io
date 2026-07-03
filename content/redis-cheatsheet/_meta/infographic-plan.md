---
title: "Redis Handbook Infographic Plan"
date: 2026-07-03T13:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["redis-cheatsheet", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, and optional future static images — not separate image assets unless generated later.

**Meta files:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Quick revision sheet | Markdown table + bullets | Page **Quick Revision** section or `09-learning-paths/redis-interview-revision-path.md` |
| Comparison one-pager | Markdown table | `07-comparisons/*` |
| Decision tree | Mermaid `flowchart TD` | `troubleshooting`, `eviction-policies`, `data-structures`, comparisons |
| Troubleshooting flowchart | Mermaid `flowchart TD` | `06-performance-operations/troubleshooting.md` |
| Interview cheat sheet | Single-page categorized table | `08-interview-guide/top-150-interview-questions.md` |
| Architecture poster | Mermaid `flowchart TB` | `architecture`, `cluster`, `sentinel` |
| Ops runbook card | Symptom → cause → fix table | `troubleshooting.md`, `monitoring.md` |
| Pattern recipe card | Step table + snippet | `05-production-patterns/*` |

---

## By Module

### 01 Fundamentals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Runtime stack | Event loop + I/O threads + keyspace layers | `architecture.md` | P0 |
| Deployment mode matrix | Standalone / Sentinel / Cluster | `architecture.md` | P0 |
| Data type picker | Type × access pattern × structure | `data-structures.md` | P0 |
| Key naming card | `app:entity:id` conventions | `data-structures.md` | P2 |
| TTL rules card | Key-level TTL; hash field exception | `data-structures.md` | P1 |

### 02 Core Redis

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| String use-when | Cache blob / counter / bitmap base | `strings.md` | P2 |
| Hash vs JSON string | Field update / memory tradeoff | `hashes.md` | P1 |
| List patterns | Stack / queue / blocking worker | `lists.md` | P1 |
| Set algebra card | SINTER / SUNION / SDIFF recipes | `sets.md` | P2 |
| ZSET patterns | Leaderboard / delayed job / GEO | `sorted-sets.md` | P1 |
| Bitmap vs Set vs HLL | Cardinality / membership / density | `bitmaps.md` + `hyperloglog.md` | P1 |
| HLL accuracy card | ~0.81% error, ~12 KB, no membership | `hyperloglog.md` | P2 |

### 03 Redis Internals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Memory object model | key → robj → encoding → allocator | `memory-management.md` | P0 |
| Encoding upgrade thresholds | listpack → hashtable triggers | `memory-management.md` | P0 |
| Fragmentation ratio card | `mem_fragmentation_ratio` interpret + fix | `memory-management.md` | P0 |
| Memory optimization checklist | key design, hash packing, active defrag | `memory-management.md` | P1 |
| RESP wire format | Simple string / bulk / array recap | `redis-protocol.md` | P1 |
| Pipeline vs non-pipeline RTT | Latency math one-liner table | `redis-protocol.md` | P0 |
| RDB vs AOF matrix | Durability × throughput × recovery | `persistence.md` | P0 |
| `appendfsync` tradeoff card | always / everysec / no | `persistence.md` | P0 |
| Fork COW warning | BGSAVE memory spike | `persistence.md` | P1 |
| Replication offset card | `master_repl_offset` vs replica lag | `replication.md` | P0 |
| Partial resync prerequisites | backlog size × disconnect window | `replication.md` | P1 |
| Sentinel quorum card | odd count, `down-after-milliseconds` | `sentinel.md` | P0 |
| Failover timeline | SDOWN → ODOWN → promote | `sentinel.md` | P0 |
| Hash slot formula | CRC16 mod 16384 + hash tag | `cluster.md` | P0 |
| MOVED vs ASK card | Permanent vs migration redirect | `cluster.md` | P0 |
| Multi-key slot rule | Same slot for MGET / Lua / transaction | `cluster.md` | P1 |

### 04 Distributed Systems

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Lock recipe card | SET NX PX + Lua unlock | `distributed-lock.md` | P0 |
| Redlock vs fencing | Debate summary table | `distributed-lock.md` | P1 |
| MULTI/EXEC vs Lua vs pipeline | Atomicity × rollback × cluster | `transactions.md` | P0 |
| Pub/Sub limitations | No persistence / no backlog | `pub-sub.md` | P1 |
| Streams vs Pub/Sub vs Lists | Delivery semantics matrix | `streams.md` | P0 |
| Consumer group lifecycle | XREADGROUP → XACK → XPENDING | `streams.md` | P0 |
| Lua cluster rules | Same-slot keys, deterministic | `lua-scripts.md` | P1 |

### 05 Production Patterns

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Cache pattern matrix | aside / through / behind | `caching-patterns.md` | P0 |
| Cache-aside flow | Exists as mermaid | `caching-patterns.md` | — Exists |
| Invalidation strategies | delete / update / pub-sub broadcast | `cache-invalidation.md` | P0 |
| Breakdown mitigation | singleflight / local cache / replica read | `cache-breakdown.md` | P0 |
| Avalanche mitigation | TTL jitter / never expire + logical expiry | `cache-avalanche.md` | P0 |
| Penetration mitigation | Bloom / negative cache TTL | `cache-penetration.md` | P0 |
| Session layout | Hash fields + sliding TTL | `session-store.md` | P1 |
| Rate limit algorithm picker | fixed / sliding / token bucket | `rate-limiter.md` | P0 |

### 06 Performance & Operations

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Latency tuning layers | network / pipeline / command / hot key | `performance-tuning.md` | P0 |
| Pipeline sizing card | batch size vs latency SLO | `performance-tuning.md` | P1 |
| INFO sections cheat sheet | server / memory / stats / replication | `monitoring.md` | P0 |
| Slowlog workflow | threshold → SLOWLOG GET → fix | `monitoring.md` | P0 |
| LATENCY DOCTOR card | When to run + interpret | `monitoring.md` | P1 |
| Cluster health metrics | `cluster_state`, slots assigned | `monitoring.md` | P1 |
| Memory sizing worksheet | key size × count + overhead % | `capacity-planning.md` | P0 |
| Cluster sizing heuristic | slots / nodes / replica factor | `capacity-planning.md` | P1 |
| High memory runbook | big keys / fragmentation / no maxmemory | `troubleshooting.md` | P0 |
| Replication lag runbook | backlog / slow commands / network | `troubleshooting.md` | P0 |
| Hot key runbook | monitor → split / local cache / read replica | `troubleshooting.md` | P0 |
| Failover failure runbook | quorum / split brain / `min-replicas-to-write` | `troubleshooting.md` | P1 |
| Eviction policy picker | volatile vs allkeys × LRU vs LFU | `eviction-policies.md` | P0 |
| maxmemory container card | ~75% of K8s limit rule | `eviction-policies.md` | P1 |

### 07 Comparisons

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Redis vs Memcached | Types / persistence / multi-thread | `redis-vs-memcached.md` | P0 |
| Redis vs Kafka | Retention / ordering / ops scale | `redis-vs-kafka.md` | P1 |
| Redis vs RabbitMQ | Routing / acks / task queues | `redis-vs-rabbitmq.md` | P1 |
| Cross-link card | Link to database-handbook ADR | All comparison pages | P1 |

### 08 Interview Guide

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 150 index | Category × count × deep dive link | `top-150-interview-questions.md` | P0 |
| Question distribution | Arch 40 / Troubleshoot 30 / Perf 25 / Reliability 20 / Scale 15 | `top-150-interview-questions.md` | P0 |
| Architect top picks | 40-question subset table | `architect-questions.md` | P1 |
| Troubleshooting drills | 30 scenario questions | `troubleshooting-questions.md` | P1 |
| Performance drills | 25 tuning questions | `performance-questions.md` | P1 |

### 09 Learning Paths

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Senior engineer path | Week-by-week topic order | `redis-senior-engineer-path.md` | P1 |
| Lead path | Ops + troubleshooting emphasis | `redis-lead-path.md` | P1 |
| Architect path | HA + comparisons + cache correctness | `redis-architect-path.md` | P1 |
| Interview revision | 48-hour cram schedule | `redis-interview-revision-path.md` | P0 |

---

## Existing Assets to Preserve (Phase B)

| Asset | Source file | Action |
| :--- | :--- | :--- |
| Runtime mermaid | `architecture.md` | Keep on canonical page |
| Replication flow mermaid | `replication.md` | Keep; add resync sequence |
| Streams consumer group mermaid | `streams.md` | Keep; add XCLAIM sequence |
| Cache-aside mermaid | `caching-patterns.md` | Keep; slim duplicate prose |
| Lock Lua snippets | `distributed-lock.md`, `lua-scripts.md` | **Consolidate** — canonical in `distributed-lock`; `lua-scripts` links |
| Eviction policy table | `eviction-policies.md` | Keep |
| Cluster hash slot table | `cluster.md` | Keep |
| Encoding one-liner | `data-structures.md` | **Move** depth to `memory-management.md` |
| RESP one-liner | `architecture.md` | **Move** to `redis-protocol.md` |
| INFO/MEMORY commands | `common-redis-commands.md` | **Move** to `monitoring.md` |
| 4 interview answers | `interview-questions.md` | **Migrate** to canonical topic pages (Phase C) |

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
| Scalability | Cluster / hot key heuristic |
| Reliability | RDB/AOF + replication matrix |
| Observability | INFO / slowlog toolkit table |
| Troubleshooting | Decision tree mermaid |
| Common Mistakes | Anti-pattern bullet card |
| Interview Questions | Link to Top 150 only |
| Architect Notes | Sentinel vs Cluster ADR card |
| Checklists | Pre-prod / incident checklists |

**Rule:** Do not add empty sections — pair each section with at least one visual when the section exists.

---

## Top 150 Question Category Visual (Phase B)

Single table on `top-150-interview-questions.md`:

| Category | Min count | Deep dive module |
| :--- | :---: | :--- |
| Architecture | 40 | `01-fundamentals/`, `03-redis-internals/`, `07-comparisons/` |
| Troubleshooting | 30 | `06-performance-operations/troubleshooting.md` |
| Performance | 25 | `06-performance-operations/performance-tuning.md`, `eviction-policies.md` |
| Reliability | 20 | `03-redis-internals/persistence.md`, `replication.md`, `sentinel.md`, `distributed-lock.md` |
| Scalability | 15 | `03-redis-internals/cluster.md`, `memory-management.md`, `05-production-patterns/cache-breakdown.md` |

**Level balance:** Developer, Senior Engineer, Lead, Architect — mixed within each category.

---

## Phase Rollout

| Phase | Deliverable |
| :--- | :--- |
| **B** | P0 infographics on all new pages; preserve existing mermaids; Top 150 category table |
| **C** | P1 comparison one-pagers; learning path schedules; answer layer visuals |
| **D** | Optional static PNG exports from Mermaid (out of scope unless requested) |

---

## Out of Scope

- Custom SVG illustration files
- Non-Redis handbook infographics
- Modifying `database-handbook` comparison visuals
- Design patterns / system design / microservices pattern content
