---
title: "Redis Handbook Navigation Plan"
date: 2026-07-03T13:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["redis-cheatsheet", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/redis_cheatsheet_modules.yaml` and `redis_cheatsheet_order.yaml`.

**Hugo section slug:** `redis-cheatsheet` (unchanged in Phase B unless rename approved — avoids breaking `curriculum_sections.yaml`).

**Folder naming:** Numbered modules inside `content/redis-cheatsheet/` mirror `kafka-handbook` and `mongodb-cheatsheet` pattern.

**Menu label (optional Phase B):** `Redis Handbook` in `curriculum_sections.yaml` while keeping slug.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo |
| :--- | :---: | :---: | :---: |
| Architecture & Model | 1 | 2 | 2 |
| Core Data Types | 2 | 5 | 5 |
| Specialized Structures | 3 | 3 | 3 |
| Messaging & Atomicity | 4 | 3 | 3 |
| Durability & HA | 5 | 4 | 4 |
| Memory Management | 6 | 1 | 1 |
| Application Patterns | 7 | 4 | 4 |
| Reference | 8 | 2 | 2 |

**Total topic pages:** 24 (+ `_index.md`)  
**Structure:** Flat files at section root — no nested folders  
**Sidebar resolution:** `site.GetPage "redis-cheatsheet/<slug>"`  
**Build script:** `scripts/build_redis_cheatsheet.py` generates flat layout from yaml

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "Fundamentals"
    path: "01-fundamentals"
    topics:
      - 01-fundamentals/architecture
      - 01-fundamentals/data-structures

  - id: 2
    focus: "Core Redis"
    path: "02-core-redis"
    topics:
      - 02-core-redis/strings
      - 02-core-redis/hashes
      - 02-core-redis/lists
      - 02-core-redis/sets
      - 02-core-redis/sorted-sets
      - 02-core-redis/bitmaps
      - 02-core-redis/hyperloglog

  - id: 3
    focus: "Redis Internals"
    path: "03-redis-internals"
    topics:
      - 03-redis-internals/memory-management          # NEW
      - 03-redis-internals/persistence
      - 03-redis-internals/replication
      - 03-redis-internals/sentinel
      - 03-redis-internals/cluster
      - 03-redis-internals/redis-protocol             # NEW

  - id: 4
    focus: "Distributed Systems"
    path: "04-distributed-systems"
    topics:
      - 04-distributed-systems/distributed-lock
      - 04-distributed-systems/transactions
      - 04-distributed-systems/pub-sub
      - 04-distributed-systems/streams
      - 04-distributed-systems/lua-scripts

  - id: 5
    focus: "Production Patterns"
    path: "05-production-patterns"
    topics:
      - 05-production-patterns/caching-patterns
      - 05-production-patterns/session-store
      - 05-production-patterns/rate-limiter
      - 05-production-patterns/cache-invalidation     # NEW
      - 05-production-patterns/cache-breakdown          # NEW
      - 05-production-patterns/cache-avalanche          # NEW
      - 05-production-patterns/cache-penetration        # NEW

  - id: 6
    focus: "Performance & Operations"
    path: "06-performance-operations"
    topics:
      - 06-performance-operations/performance-tuning    # NEW
      - 06-performance-operations/troubleshooting     # NEW
      - 06-performance-operations/monitoring          # NEW
      - 06-performance-operations/capacity-planning     # NEW
      - 06-performance-operations/eviction-policies

  - id: 7
    focus: "Comparisons"
    path: "07-comparisons"
    topics:
      - 07-comparisons/redis-vs-memcached               # NEW
      - 07-comparisons/redis-vs-kafka                 # NEW
      - 07-comparisons/redis-vs-rabbitmq              # NEW

  - id: 8
    focus: "Interview Guide"
    path: "08-interview-guide"
    topics:
      - 08-interview-guide/top-150-interview-questions  # NEW
      - 08-interview-guide/architect-questions          # NEW
      - 08-interview-guide/troubleshooting-questions    # NEW
      - 08-interview-guide/performance-questions        # NEW

  - id: 9
    focus: "Learning Paths"
    path: "09-learning-paths"
    topics:
      - 09-learning-paths/redis-senior-engineer-path
      - 09-learning-paths/redis-lead-path
      - 09-learning-paths/redis-architect-path
      - 09-learning-paths/redis-interview-revision-path
```

**Topic count after Phase B:** 22 moved + 10 new + 3 comparisons + 4 interview + 4 learning paths = **43 pages** (+ 9 section indexes + handbook `_index` + `_meta`)

**Removed from navigation:** `common-redis-commands`, `interview-questions` (content folded / replaced)

---

## Reading Order (Recommended `redis_cheatsheet_order.yaml`)

1. `01-fundamentals/architecture`
2. `01-fundamentals/data-structures`
3. `02-core-redis/strings` … `hyperloglog` (type order)
4. `03-redis-internals/memory-management`
5. `03-redis-internals/redis-protocol`
6. `03-redis-internals/persistence` → `replication` → `sentinel` → `cluster`
7. `04-distributed-systems/distributed-lock` → `transactions` → `pub-sub` → `streams` → `lua-scripts`
8. `05-production-patterns/caching-patterns` → cache failure pages → `session-store` → `rate-limiter`
9. `06-performance-operations/eviction-policies` → `performance-tuning` → `monitoring` → `capacity-planning` → `troubleshooting`
10. `07-comparisons/*`
11. `08-interview-guide/top-150-interview-questions` → subset pages
12. `09-learning-paths/*`

**Note:** Current flat order interleaves streams before persistence (module 3 → 4 → 5 jump). Phase B order groups internals before distributed systems.

---

## URL Aliases (Backward Compatibility)

Add Hugo front matter `aliases` on moved pages:

| Old URL | New URL |
| :--- | :--- |
| `/redis-cheatsheet/architecture/` | `/redis-cheatsheet/01-fundamentals/architecture/` |
| `/redis-cheatsheet/data-structures/` | `/redis-cheatsheet/01-fundamentals/data-structures/` |
| `/redis-cheatsheet/strings/` | `/redis-cheatsheet/02-core-redis/strings/` |
| `/redis-cheatsheet/hashes/` | `/redis-cheatsheet/02-core-redis/hashes/` |
| `/redis-cheatsheet/lists/` | `/redis-cheatsheet/02-core-redis/lists/` |
| `/redis-cheatsheet/sets/` | `/redis-cheatsheet/02-core-redis/sets/` |
| `/redis-cheatsheet/sorted-sets/` | `/redis-cheatsheet/02-core-redis/sorted-sets/` |
| `/redis-cheatsheet/bitmaps/` | `/redis-cheatsheet/02-core-redis/bitmaps/` |
| `/redis-cheatsheet/hyperloglog/` | `/redis-cheatsheet/02-core-redis/hyperloglog/` |
| `/redis-cheatsheet/persistence/` | `/redis-cheatsheet/03-redis-internals/persistence/` |
| `/redis-cheatsheet/replication/` | `/redis-cheatsheet/03-redis-internals/replication/` |
| `/redis-cheatsheet/sentinel/` | `/redis-cheatsheet/03-redis-internals/sentinel/` |
| `/redis-cheatsheet/cluster/` | `/redis-cheatsheet/03-redis-internals/cluster/` |
| `/redis-cheatsheet/transactions/` | `/redis-cheatsheet/04-distributed-systems/transactions/` |
| `/redis-cheatsheet/pub-sub/` | `/redis-cheatsheet/04-distributed-systems/pub-sub/` |
| `/redis-cheatsheet/streams/` | `/redis-cheatsheet/04-distributed-systems/streams/` |
| `/redis-cheatsheet/lua-scripts/` | `/redis-cheatsheet/04-distributed-systems/lua-scripts/` |
| `/redis-cheatsheet/distributed-lock/` | `/redis-cheatsheet/04-distributed-systems/distributed-lock/` |
| `/redis-cheatsheet/caching-patterns/` | `/redis-cheatsheet/05-production-patterns/caching-patterns/` |
| `/redis-cheatsheet/session-store/` | `/redis-cheatsheet/05-production-patterns/session-store/` |
| `/redis-cheatsheet/rate-limiter/` | `/redis-cheatsheet/05-production-patterns/rate-limiter/` |
| `/redis-cheatsheet/eviction-policies/` | `/redis-cheatsheet/06-performance-operations/eviction-policies/` |
| `/redis-cheatsheet/common-redis-commands/` | `/redis-cheatsheet/06-performance-operations/monitoring/` |
| `/redis-cheatsheet/interview-questions/` | `/redis-cheatsheet/08-interview-guide/top-150-interview-questions/` |

---

## Landing Page (`_index.md`)

| Section | Phase B update |
| :--- | :--- |
| Title / description | Shift from "cheatsheet" to "handbook" while keeping `redis-cheatsheet` slug |
| Module table | 9 modules with links to section `_index.md` |
| Learning paths | Prominent links to `09-learning-paths/` |
| Cross-handbook | Keep link to [Database Handbook — Redis](/database-handbook/redis/) and [Redis vs Memcached](/database-handbook/redis-vs-memcached/) |
| Remove | Link to `/microservices/` (out of scope) |
| Maintainer meta | Optional link to `_meta/concept-registry.md` (`draft: true`) |
| Audience callout | Senior engineer / lead / architect |

---

## Section Index Pages

Create or rewrite `01-fundamentals/_index.md` through `09-learning-paths/_index.md` with:

- Module purpose (2–3 sentences)
- Ordered reading list (canonical pages)
- "Start here if…" guidance per persona
- Link to concept registry subset for module

---

## Front Matter Standardization

| Field | Phase B rule |
| :--- | :--- |
| `cheatSheet` | `true` on `02-core-redis/*` quick-ref pages only; `false` on architect depth pages |
| `module` / `moduleTitle` | Remap to 1–9 |
| `sectionRef` | `Module.Topic` within new structure |
| `draft` | `false` for published topics; `true` for `_meta/*` |
| `tags` | Add `redis-handbook` alongside `redis-cheatsheet` |
| `interviewHandbook` | `true` on `08-interview-guide/*` pages |

---

## Prev / Next Navigation

**Current:** Manual "Related Topics" footer links (flat chain with inconsistent order — e.g. persistence links from lua-scripts).  
**Phase B:**

1. Drive order from `redis_cheatsheet_order.yaml` (nested slugs).
2. Replace repetitive "Related Topics" with **See Also** (prev/next + canonical links).
3. Remove duplicate `redis-vs-memcached` link from every page footer.

---

## Cross-Link Strategy

| From | To | Rule |
| :--- | :--- | :--- |
| Any topic page | Concept deep dive | Link canonical page from registry |
| `07-comparisons/*` | `database-handbook/*` | "See also" — ADR context only |
| `08-interview-guide/top-150` | Topic pages | `Deep Dive` column = Hugo URL |
| `05-production-patterns/caching-patterns` | cache failure pages | No duplicate stampede/penetration depth |
| `01-fundamentals/architecture` | `memory-management`, `redis-protocol` | Strip duplicated paragraphs |
| `02-core-redis/*` | `01-fundamentals/data-structures` | Type selection only on overview |

---

## Yaml Files to Update (Phase B)

| File | Change |
| :--- | :--- |
| `data/redis_cheatsheet_modules.yaml` | 9 modules, nested topic slugs |
| `data/redis_cheatsheet_order.yaml` | Full reading order (~43 topics) |
| `data/curriculum_sections.yaml` | Optional `menuLabel`: "Redis Handbook" |
| `data/curriculum_sidebar.yaml` | Verify section unchanged (slug same) |
| `scripts/build_redis_cheatsheet.py` | Nested paths, new topic meta, remove demoted pages |

**Out of scope:** `database_handbook_modules.yaml`, `kafka_handbook_*`, other handbooks.

---

## GitHub Pages Optimization

- Nested URLs improve information scent (`/03-redis-internals/cluster/`).
- Aliases prevent 404s from existing links in blog posts and `_index.md`.
- Section `_index.md` pages become crawl hubs for each module.
- Top 150 page: TOC with category anchors (Architecture, Troubleshooting, Performance, Reliability, Scalability).
- `ShowToc: true` on all architect-depth pages.

---

## Optional Future: Slug Rename

| Option | Pros | Cons |
| :--- | :--- | :--- |
| Keep `redis-cheatsheet` | No curriculum yaml change; aliases sufficient | URL says "cheatsheet" |
| Rename to `redis-handbook` | Matches content positioning | Requires `curriculum_sections.yaml`, layouts, all inbound links |

**Phase A recommendation:** Keep slug; update titles and menu label only.

---

## Phase B Navigation Checklist

- [ ] Create 9 module folders + section `_index.md`
- [ ] Move files with aliases
- [ ] Update yaml modules + order
- [ ] Update `build_redis_cheatsheet.py`
- [ ] Rewrite handbook `_index.md`
- [ ] Fix all internal `/redis-cheatsheet/<flat>/` links in moved files
- [ ] Verify Hugo build + sidebar resolution
