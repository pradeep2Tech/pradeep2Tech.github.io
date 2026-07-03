---
title: "Redis Handbook Refactoring Plan"
date: 2026-07-03T13:00:00+00:00
draft: true
description: "Phase A inventory — quality, duplication, gaps, and recommended actions."
tags: ["redis-cheatsheet", "meta", "planning"]
---

# Phase A — Repository Inventory

**Scope:** `content/redis-cheatsheet/` (24 markdown files)  
**Audience:** Senior Engineers, Technical Leads, Architects (6+ years)  
**Status:** Planning only — **no content rewritten in Phase A**

**Target structure:** 9 modules (`01-fundamentals` … `09-learning-paths`) + `_meta/` — implemented in Phase B within the same Hugo section slug (`redis-cheatsheet`) unless slug rename is approved separately.

---

## Executive Summary

| Metric | Assessment |
| :--- | :--- |
| **Structure** | **Flat** — 8 modules in yaml; no numbered folders |
| **Template compliance** | Cheat-sheet skeleton (`Executive Summary`, `Core Concepts`, `Quick Reference`, `Snippets`) — **not** the 14-section architect template |
| **Average page depth** | ~85 lines — strong for 2-minute brush-up; **weak** for architect/production depth |
| **Duplication** | **High** — encodings, memory, cache patterns, locks, eviction, KEYS/SCAN, monitoring commands repeated across 3–6 files |
| **Canonical discipline** | **None** — no concept registry enforced |
| **Interview Layer 1** | **Wrong model** — `interview-questions.md` has 4 inline `interview-answer` blocks (answers on question page) |
| **Interview Layer 2** | **Missing** — no `## Interview Questions` answer blocks on topic pages |
| **Production ops** | **Thin** — no monitoring, troubleshooting, performance tuning, or capacity canonical pages |
| **Internals** | **Fragmented** — memory model split across `architecture`, `data-structures`, per-type pages; no `memory-management.md` or `redis-protocol.md` |
| **Cache failure modes** | **Bundled** — stampede/avalanche/penetration/breakdown crammed into `caching-patterns.md` (~15 lines) |
| **Comparisons** | **External only** — `redis-vs-memcached` in `database-handbook/`; no Kafka/RabbitMQ comparison in handbook |
| **Build scripts** | `scripts/build_redis_cheatsheet.py` — Phase B must update script or hand edits will be overwritten on regen |

**Recommended Phase B focus:** Restructure into 9 modules, enforce concept registry, create 17 missing canonical pages, replace interview layer with Top 150 (questions only), add learning paths — **preserve** valuable cheat-sheet tables, mermaid diagrams, and Lua snippets.

---

## Scoring Guide

| Dimension | 1 | 10 |
| :--- | :--- | :--- |
| **Quality** | Inaccurate or trivial | Accurate, production-grade, maintainable |
| **Duplication** | Unique | Heavily repeated elsewhere |
| **Interview Value** | Not useful in senior interviews | High architect-panel value |

Subscores used in **Quality** column: accuracy, production relevance, internals depth, scalability depth, troubleshooting value.

---

## File Inventory

| File | Purpose | Quality | Duplication | Interview Value | Problems | Action |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| `_index.md` | Section landing; links to database-handbook + microservices | 4 | 3 | 3 | One paragraph; no module map; links to out-of-scope microservices handbook | **Keep** — expand with 9-module overview + learning paths; remove microservices deep-link |
| `architecture.md` | Event loop, I/O threads, RESP recap, memory one-liner | 6 | 6 | 8 | Jack-of-all-trades: protocol + memory + threading; should be topology/runtime only | **Move** → `01-fundamentals/architecture.md` — **canonical** for runtime model; strip memory/protocol depth |
| `data-structures.md` | Type picker table, encoding overview, TTL | 7 | 5 | 7 | Encoding depth duplicates per-type pages + future `memory-management.md` | **Move** → `01-fundamentals/data-structures.md` — **canonical** for type selection matrix only |
| `strings.md` | String commands, cache-aside snippet, SET NX mention | 6 | 4 | 5 | Cache-aside duplicates `caching-patterns`; lock pattern duplicates `distributed-lock` | **Move** → `02-core-redis/strings.md` |
| `hashes.md` | Hash commands, session snippet | 6 | 3 | 5 | Session pattern overlaps `session-store.md` | **Move** → `02-core-redis/hashes.md` |
| `lists.md` | List queue patterns, BLPOP | 6 | 3 | 6 | Reliable queue vs streams noted but shallow | **Move** → `02-core-redis/lists.md` |
| `sets.md` | Set algebra, HLL cross-ref | 6 | 2 | 5 | Solid quick-ref | **Move** → `02-core-redis/sets.md` |
| `sorted-sets.md` | ZSET commands, delayed job pattern | 7 | 2 | 7 | Delayed queue pattern is interview-relevant | **Move** → `02-core-redis/sorted-sets.md` |
| `bitmaps.md` | Bitmap commands, DAU pattern | 6 | 2 | 5 | Sparse offset pitfall is good | **Move** → `02-core-redis/bitmaps.md` |
| `hyperloglog.md` | HLL commands, cardinality | 6 | 2 | 6 | Accurate; internals shallow | **Move** → `02-core-redis/hyperloglog.md` |
| `persistence.md` | RDB, AOF, hybrid, fork COW | 6 | 5 | 9 | Good interview topic but thin on rewrite/AOF internals | **Move** → `03-redis-internals/persistence.md` — **canonical** for RDB/AOF |
| `replication.md` | Primary-replica, partial resync, lag | 6 | 4 | 9 | `WAIT`, backlog sizing shallow; no split-brain discussion | **Move** → `03-redis-internals/replication.md` — **canonical** |
| `sentinel.md` | Failover, quorum, SDOWN/ODOWN | 6 | 3 | 9 | Client discovery shallow; no split-brain runbook | **Move** → `03-redis-internals/sentinel.md` — **canonical** |
| `cluster.md` | Hash slots, MOVED/ASK, hash tags | 7 | 3 | 10 | Best HA content in repo; resharding internals thin | **Move** → `03-redis-internals/cluster.md` — **canonical** |
| `transactions.md` | MULTI/EXEC, WATCH, pipeline vs txn | 6 | 4 | 8 | Exec-time error behavior noted; cluster constraints thin | **Move** → `04-distributed-systems/transactions.md` |
| `pub-sub.md` | Fire-and-forget, pattern subscribe | 6 | 3 | 7 | Invalidation pattern duplicates cache topics | **Move** → `04-distributed-systems/pub-sub.md` |
| `streams.md` | Consumer groups, XACK, pending | 7 | 3 | 9 | Has mermaid; XAUTOCLAIM shallow | **Move** → `04-distributed-systems/streams.md` — **canonical** |
| `lua-scripts.md` | EVAL, atomicity, lock release Lua | 7 | 5 | 8 | Lock release script duplicates `distributed-lock.md` | **Move** → `04-distributed-systems/lua-scripts.md` — **canonical** for server-side scripting |
| `distributed-lock.md` | SET NX PX, Redlock, fencing | 7 | 5 | 10 | Best correctness content; Lua snippets duplicate `lua-scripts` | **Move** → `04-distributed-systems/distributed-lock.md` — **canonical** |
| `caching-patterns.md` | Cache-aside, write-through/behind, stampede | 6 | 8 | 8 | Bundles 4+ concepts that need dedicated pages; mermaid useful | **Move** → `05-production-patterns/caching-patterns.md`; **split** invalidation/breakdown/avalanche/penetration |
| `session-store.md` | Hash/JSON session, TTL refresh | 6 | 3 | 6 | Spring Session mention only; no cluster session stickiness | **Move** → `05-production-patterns/session-store.md` |
| `rate-limiter.md` | Fixed/sliding/token bucket | 7 | 3 | 8 | Hot key on global limit noted; good | **Move** → `05-production-patterns/rate-limiter.md` |
| `eviction-policies.md` | maxmemory policies, LRU sampling | 7 | 6 | 8 | Memory policy overlaps `architecture`, `caching-patterns` | **Move** → `06-performance-operations/eviction-policies.md` — **canonical** |
| `common-redis-commands.md` | INFO, SCAN, SLOWLOG, MEMORY admin | 5 | 8 | 4 | Duplicates 6+ pages; command memorization focus | **Demote** — fold into `monitoring.md` + `troubleshooting.md` quick-ref; delete or appendix |
| `interview-questions.md` | 4 answered probes + theme table | 5 | 9 | 5 | Wrong interview model; duplicates persistence/cluster/locks | **Replace** → `08-interview-guide/top-150-interview-questions.md` |

---

## Missing Files (Phase B Create)

| File | Priority | Rationale |
| :--- | :---: | :--- |
| `03-redis-internals/memory-management.md` | P0 | Memory model, encodings, fragmentation, optimization — scattered today |
| `03-redis-internals/redis-protocol.md` | P0 | RESP, pipelining, request path — one paragraph in `architecture` only |
| `06-performance-operations/performance-tuning.md` | P0 | Latency, pipeline, command optimization — absent |
| `06-performance-operations/monitoring.md` | P0 | INFO, slowlog, latency doctor — partial in `common-redis-commands` |
| `06-performance-operations/troubleshooting.md` | P0 | Hot keys, lag, failover, slow commands — absent |
| `06-performance-operations/capacity-planning.md` | P0 | Memory sizing, cluster sizing — absent |
| `05-production-patterns/cache-invalidation.md` | P0 | Write-through/behind/aside refresh — bundled in `caching-patterns` |
| `05-production-patterns/cache-breakdown.md` | P0 | Hot key / breakdown — one bullet in `caching-patterns` |
| `05-production-patterns/cache-avalanche.md` | P0 | Expiration storms — TTL jitter only in `caching-patterns` |
| `05-production-patterns/cache-penetration.md` | P0 | Null key attacks, Bloom filter — one bullet only |
| `07-comparisons/redis-vs-memcached.md` | P1 | Handbook comparison page; link `database-handbook` ADR |
| `07-comparisons/redis-vs-kafka.md` | P1 | Streams vs log; when not to use Redis as broker |
| `07-comparisons/redis-vs-rabbitmq.md` | P1 | Task queue vs Redis lists/streams |
| `08-interview-guide/top-150-interview-questions.md` | P0 | Exactly 150 questions, no answers |
| `08-interview-guide/architect-questions.md` | P1 | Subset (~40 architecture) |
| `08-interview-guide/troubleshooting-questions.md` | P1 | Subset (~30 troubleshooting) |
| `08-interview-guide/performance-questions.md` | P1 | Subset (~25 performance) |
| `09-learning-paths/redis-senior-engineer-path.md` | P1 | Missing |
| `09-learning-paths/redis-lead-path.md` | P1 | Missing |
| `09-learning-paths/redis-architect-path.md` | P1 | Missing |
| `09-learning-paths/redis-interview-revision-path.md` | P1 | Missing |
| Section `_index.md` × 9 | P1 | Module landing stubs |

**Topic count after Phase B:** 22 moved + 10 new ops/cache + 3 comparisons + 4 interview + 4 learning paths = **43 pages** (+ 9 section indexes + handbook `_index` + `_meta`)

---

## Duplicate Content (Semantic Overlap > 50%)

| Concept cluster | Appears in | Canonical target (Phase B) |
| :--- | :--- | :--- |
| Single-threaded event loop / I/O threads | `architecture`, `interview-questions` | `01-fundamentals/architecture.md` |
| RESP / pipelining | `architecture` | `03-redis-internals/redis-protocol.md` |
| Memory model (`used_memory`, jemalloc, RSS) | `architecture`, `eviction-policies`, `common-redis-commands` | `03-redis-internals/memory-management.md` |
| Type encodings (ziplist, listpack, intset) | `data-structures`, `strings`, `hashes`, `lists`, `sorted-sets` | `03-redis-internals/memory-management.md` (internals); type pages keep ≤2 sentences |
| RDB vs AOF trade-offs | `persistence`, `architecture` (diagram), `interview-questions` | `03-redis-internals/persistence.md` |
| Replication lag / partial resync | `replication`, `persistence` (related) | `03-redis-internals/replication.md` |
| Sentinel vs Cluster | `sentinel`, `cluster`, `interview-questions` | respective canonical pages + comparison in architect questions |
| Hash slots / MOVED / ASK | `cluster`, `lua-scripts`, `interview-questions` | `03-redis-internals/cluster.md` |
| Cache-aside / write-through / write-behind | `caching-patterns`, `strings` | `05-production-patterns/caching-patterns.md` + `cache-invalidation.md` |
| Cache stampede / thundering herd | `caching-patterns`, `distributed-lock` (stampede lock) | `cache-breakdown.md` + `cache-avalanche.md` |
| Cache penetration / negative cache | `caching-patterns` | `cache-penetration.md` |
| Pub/Sub cache invalidation | `pub-sub`, `caching-patterns` | `cache-invalidation.md` (pattern); `pub-sub.md` (transport only) |
| Distributed lock (SET NX PX, Lua unlock) | `distributed-lock`, `lua-scripts`, `strings`, `interview-questions` | `04-distributed-systems/distributed-lock.md` |
| MULTI/EXEC vs Lua vs pipeline | `transactions`, `lua-scripts`, `strings` | `transactions.md` + `lua-scripts.md` |
| Pub/Sub vs Streams | `pub-sub`, `streams`, `lists` | `pub-sub.md` + `streams.md` |
| maxmemory / eviction policies | `eviction-policies`, `architecture`, `caching-patterns` | `06-performance-operations/eviction-policies.md` |
| KEYS vs SCAN / MONITOR danger | `architecture`, `common-redis-commands` | `06-performance-operations/troubleshooting.md` + `monitoring.md` |
| INFO / SLOWLOG / LATENCY DOCTOR | `architecture`, `common-redis-commands` | `06-performance-operations/monitoring.md` |
| Rate limiting algorithms | `rate-limiter`, `lua-scripts` | `05-production-patterns/rate-limiter.md` |
| Session hash pattern | `hashes`, `session-store` | `05-production-patterns/session-store.md` |
| Redis vs Memcached | `_index`, every Related Topics footer, `database-handbook` | `07-comparisons/redis-vs-memcached.md` (handbook); link database-handbook ADR |

---

## Weak Files (Quality < 6 or Interview Value < 6)

| File | Issue |
| :--- | :--- |
| `_index.md` | Landing stub; microservices cross-link out of scope |
| `common-redis-commands.md` | Syntax duplication across 6+ pages; certification-style |
| `interview-questions.md` | 4 answers only; violates Layer 1 model; high duplication |
| `strings.md` | Command-heavy; cache/lock patterns belong elsewhere |
| `lists.md` | Queue depth insufficient for senior panel without streams link |

---

## Fragmented Concepts (Need Split or Consolidate)

| Concept | Current state | Phase B action |
| :--- | :--- | :--- |
| Memory management | 1-line mentions in 5 files | **Create** `memory-management.md` |
| RESP protocol | 2 sentences in `architecture` | **Create** `redis-protocol.md` |
| Performance tuning | Absent | **Create** `performance-tuning.md` |
| Monitoring | 4 commands in `common-redis-commands` | **Create** `monitoring.md` |
| Troubleshooting runbooks | Gotchas only | **Create** `troubleshooting.md` |
| Capacity planning | Absent | **Create** `capacity-planning.md` |
| Cache failure modes | 3 bullets in `caching-patterns` | **Split** 4 dedicated pages |
| Interview Q&A | 4 inline answers | **Replace** with Top 150 + answer layer on topic pages |
| Admin commands | Standalone page | **Fold** into monitoring/troubleshooting |

---

## Outdated or Misaligned Content

| Item | Issue |
| :--- | :--- |
| Module yaml | 8 modules — does not match 9-module target |
| Front matter `module` / `sectionRef` | Flat numbering (1.1–8.2) — needs remap after folder move |
| `interview-questions.md` | Uses `interview-answer` shortcode — conflicts with Layer 1 spec |
| `_index.md` | Links to `/microservices/` — out of scope per refactor rules |
| `lists.md` | Notes `BRPOPLPUSH` deprecated → streams — accurate; keep |
| `lua-scripts.md` | Redis 7+ Functions mentioned — accurate; expand in Phase B |
| `persistence.md` | Related Topics chain skips streams module order — navigation bug |
| `build_redis_cheatsheet.py` | Regenerates flat structure — must update for Phase B |
| Related Topics footers | All 24 pages link `database-handbook/redis-vs-memcached` — redundant noise |

---

## External Content (Out of Scope — Link Only)

| Location | Relationship to handbook |
| :--- | :--- |
| `database-handbook/redis.md` | **Selection ADR** — when to choose Redis; not operational depth |
| `database-handbook/redis-vs-memcached.md` | **Comparison ADR** — link from `07-comparisons/`; avoid duplicating trade-off tables |
| `interview-prep/` | May reference Redis — no merge in Phase B |
| `microservices/` | Caching architecture — link removed from `_index`; no content import |

---

## Top 150 Interview Plan (Phase B)

| Category | Min count | Primary answer locations |
| :--- | :---: | :--- |
| Architecture | 40 | `01-fundamentals/`, `03-redis-internals/`, `07-comparisons/` |
| Troubleshooting | 30 | `06-performance-operations/troubleshooting.md`, `monitoring.md` |
| Performance | 25 | `performance-tuning.md`, `eviction-policies.md`, `capacity-planning.md` |
| Reliability | 20 | `persistence.md`, `replication.md`, `sentinel.md`, `distributed-lock.md` |
| Scalability | 15 | `cluster.md`, `memory-management.md`, cache breakdown pages |

**Avoid:** CLI syntax, command memorization, certification-style trivia.

---

## Phase B Action Summary (Pending Approval)

| Priority | Action |
| :---: | :--- |
| P0 | Create folder structure `01-fundamentals` … `09-learning-paths` |
| P0 | Move 22 topic files to target paths; add Hugo `aliases` for old URLs |
| P0 | Create `memory-management.md`, `redis-protocol.md` |
| P0 | Create `performance-tuning.md`, `monitoring.md`, `troubleshooting.md`, `capacity-planning.md` |
| P0 | Create `cache-invalidation.md`, `cache-breakdown.md`, `cache-avalanche.md`, `cache-penetration.md` |
| P0 | Create `top-150-interview-questions.md` (exactly 150, questions only) |
| P0 | Enforce `_meta/concept-registry.md` — trim duplicates to ≤2 sentences + link |
| P1 | Create comparison pages (3) + learning paths (4) |
| P1 | Create `architect-questions.md`, `troubleshooting-questions.md`, `performance-questions.md` |
| P1 | Update `redis_cheatsheet_modules.yaml` + `redis_cheatsheet_order.yaml` |
| P1 | Update `scripts/build_redis_cheatsheet.py` for new structure |
| P1 | Rewrite section `_index.md` pages + handbook `_index.md` |
| P2 | Upgrade priority pages to 14-section architect template (non-empty sections only) |
| P2 | Answer layer batch 1 (~50 questions on canonical pages) |
| P2 | Remove `common-redis-commands.md`, `interview-questions.md` |
| P3 | Answer layer batch 2 (remaining 100 questions) |
| P3 | P0 mermaid + infographic rollout per `_meta/mermaid-plan.md` |

---

## Phase A Deliverables Checklist

- [x] `_meta/refactoring-plan.md` (this file)
- [x] `_meta/concept-registry.md`
- [x] `_meta/navigation-plan.md`
- [x] `_meta/mermaid-plan.md`
- [x] `_meta/infographic-plan.md`

**Status:** Phase C complete — answer layer, P0 mermaid, Top 150 anchors. Optional Phase D: unique answer polish.

---

## Phase B Completion Checklist

- [x] 9-module folder structure (`01-fundamentals` … `09-learning-paths`)
- [x] 22 topic files moved with Hugo `aliases`
- [x] 13 new canonical pages created (internals, ops, cache failures, comparisons)
- [x] `top-150-interview-questions.md` (exactly 150 questions, no answers)
- [x] `architect-questions.md`, `troubleshooting-questions.md`, `performance-questions.md`
- [x] 4 learning path pages
- [x] Section `_index.md` × 9 + handbook `_index.md` rewritten
- [x] `data/redis_cheatsheet_modules.yaml` + `data/redis_cheatsheet_order.yaml` updated
- [x] `scripts/generate_redis_handbook_refactor.py` for regeneration
- [x] Removed flat `common-redis-commands.md`, `interview-questions.md`, and legacy topic files
- [x] `build_redis_cheatsheet.py` deprecated (guards against flat regen)
- [x] Answer layer on topic pages (Phase C — all 150 on canonical pages)
- [x] Top 150 anchor deep dives (`Page — Qn` links)
- [x] P0 mermaid on 11 canonical pages
- [x] `read_old()` git fallback in generate script (fixes empty moved pages)
- [ ] Per-question unique answer polish (Phase D — optional SME pass)
