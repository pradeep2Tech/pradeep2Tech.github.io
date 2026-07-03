---
title: "MongoDB Handbook Navigation Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["mongodb-cheatsheet", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/mongodb_cheatsheet_modules.yaml` and `mongodb_cheatsheet_order.yaml`.

**Hugo section slug:** `mongodb-cheatsheet` (unchanged in Phase B unless rename approved — avoids breaking `curriculum_sections.yaml`).

**Folder naming:** Numbered modules inside `content/mongodb-cheatsheet/` mirror `kafka-handbook` pattern.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo |
| :--- | :---: | :---: | :---: |
| Core & Data Model | 1 | 4 | 4 (+ `architecture` listed first in order yaml) |
| Queries & Indexes | 2 | 5 | 5 |
| Scale & Reliability | 3 | 3 | 3 |
| Design, Ops & Reference | 4 | 5 | 5 |

**Total topic pages:** 17 (+ `_index.md`)  
**Structure:** Flat files at section root — no nested folders  
**Sidebar resolution:** `site.GetPage "mongodb-cheatsheet/<slug>"`

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "Fundamentals"
    path: "01-fundamentals"
    topics:
      - 01-fundamentals/documents
      - 01-fundamentals/collections
      - 01-fundamentals/crud
      - 01-fundamentals/atlas-basics

  - id: 2
    focus: "Core MongoDB"
    path: "02-core-mongodb"
    topics:
      - 02-core-mongodb/architecture
      - 02-core-mongodb/storage-engine          # NEW
      - 02-core-mongodb/replication
      - 02-core-mongodb/sharding
      - 02-core-mongodb/transactions
      - 02-core-mongodb/schema-design

  - id: 3
    focus: "Query & Performance"
    path: "03-query-performance"
    topics:
      - 03-query-performance/indexes
      - 03-query-performance/ttl-index
      - 03-query-performance/text-search
      - 03-query-performance/geospatial
      - 03-query-performance/aggregation-pipeline
      - 03-query-performance/query-optimization   # NEW
      - 03-query-performance/explain-plan           # NEW

  - id: 4
    focus: "Production Operations"
    path: "04-production-operations"
    topics:
      - 04-production-operations/performance
      - 04-production-operations/monitoring       # NEW
      - 04-production-operations/troubleshooting  # NEW
      - 04-production-operations/backup-recovery  # NEW
      - 04-production-operations/capacity-planning # NEW

  - id: 5
    focus: "Comparisons"
    path: "05-comparisons"
    topics:
      - 05-comparisons/mongodb-vs-postgresql      # NEW
      - 05-comparisons/mongodb-vs-cassandra       # NEW
      - 05-comparisons/mongodb-vs-couchbase       # NEW

  - id: 6
    focus: "Interview Guide"
    path: "06-interview-guide"
    topics:
      - 06-interview-guide/top-150-interview-questions  # NEW
      - 06-interview-guide/architect-questions          # NEW
      - 06-interview-guide/troubleshooting-questions    # NEW
      - 06-interview-guide/performance-questions        # NEW

  - id: 7
    focus: "Learning Paths"
    path: "07-learning-paths"
    topics:
      - 07-learning-paths/mongodb-senior-engineer-path
      - 07-learning-paths/mongodb-lead-path
      - 07-learning-paths/mongodb-architect-path
      - 07-learning-paths/mongodb-interview-revision-path
```

**Topic count after Phase B:** 17 moved + 11 new + 4 interview + 4 learning paths = **36 pages** (+ 7 section indexes + handbook `_index` + `_meta`)

---

## URL Aliases (Backward Compatibility)

Add Hugo front matter `aliases` on moved pages to preserve GitHub Pages links:

| Old URL | New URL |
| :--- | :--- |
| `/mongodb-cheatsheet/architecture/` | `/mongodb-cheatsheet/02-core-mongodb/architecture/` |
| `/mongodb-cheatsheet/documents/` | `/mongodb-cheatsheet/01-fundamentals/documents/` |
| `/mongodb-cheatsheet/collections/` | `/mongodb-cheatsheet/01-fundamentals/collections/` |
| `/mongodb-cheatsheet/crud/` | `/mongodb-cheatsheet/01-fundamentals/crud/` |
| `/mongodb-cheatsheet/atlas-basics/` | `/mongodb-cheatsheet/01-fundamentals/atlas-basics/` |
| `/mongodb-cheatsheet/indexes/` | `/mongodb-cheatsheet/03-query-performance/indexes/` |
| `/mongodb-cheatsheet/ttl-index/` | `/mongodb-cheatsheet/03-query-performance/ttl-index/` |
| `/mongodb-cheatsheet/text-search/` | `/mongodb-cheatsheet/03-query-performance/text-search/` |
| `/mongodb-cheatsheet/geospatial/` | `/mongodb-cheatsheet/03-query-performance/geospatial/` |
| `/mongodb-cheatsheet/aggregation-pipeline/` | `/mongodb-cheatsheet/03-query-performance/aggregation-pipeline/` |
| `/mongodb-cheatsheet/replication/` | `/mongodb-cheatsheet/02-core-mongodb/replication/` |
| `/mongodb-cheatsheet/sharding/` | `/mongodb-cheatsheet/02-core-mongodb/sharding/` |
| `/mongodb-cheatsheet/transactions/` | `/mongodb-cheatsheet/02-core-mongodb/transactions/` |
| `/mongodb-cheatsheet/schema-design/` | `/mongodb-cheatsheet/02-core-mongodb/schema-design/` |
| `/mongodb-cheatsheet/performance/` | `/mongodb-cheatsheet/04-production-operations/performance/` |
| `/mongodb-cheatsheet/interview-questions/` | `/mongodb-cheatsheet/06-interview-guide/top-150-interview-questions/` |
| `/mongodb-cheatsheet/mongo-shell-commands/` | Remove or redirect to `04-production-operations/monitoring/` |

---

## Landing Page (`_index.md`)

| Section | Phase B update |
| :--- | :--- |
| Title / description | Shift from "cheatsheet" to "handbook" while keeping `mongodb-cheatsheet` slug |
| Module table | 7 modules with links to section `_index.md` |
| Learning paths | Prominent links to `07-learning-paths/` |
| Cross-handbook | Keep links to [Database Handbook — MongoDB](/database-handbook/mongodb/) and [MongoDB vs PostgreSQL](/database-handbook/mongodb-vs-postgresql/) |
| Maintainer meta | Optional link to `_meta/concept-registry.md` (`draft: true`) |
| Audience callout | Senior engineer / lead / architect |

---

## Section Index Pages

Create or rewrite `01-fundamentals/_index.md` through `07-learning-paths/_index.md` with:

- Module purpose (2–3 sentences)
- Ordered reading list (canonical pages)
- "Start here if…" guidance per persona
- Link to concept registry subset for module

---

## Front Matter Standardization

| Field | Phase B rule |
| :--- | :--- |
| `cheatSheet` | `true` on fundamentals quick-ref pages only; `false` on architect depth pages |
| `module` / `moduleTitle` | Remap to 1–7 |
| `sectionRef` | `Module.Topic` within new structure |
| `draft` | `false` for published topics; `true` for `_meta/*` |
| `tags` | Add `mongodb-handbook` alongside `mongodb-cheatsheet` for discoverability |

---

## Prev / Next Navigation

**Current:** Manual "Related Topics" footer links (flat chain).  
**Phase B:**

1. Drive order from `mongodb_cheatsheet_order.yaml` (nested slugs).
2. Keep Related Topics but add **canonical link** for cross-module concepts.
3. Section-aware prev/next via yaml order (same pattern as `kafka-handbook`).

---

## Cross-Link Strategy

| From | To | Rule |
| :--- | :--- | :--- |
| Any topic page | Concept deep dive | Link canonical page from registry |
| `05-comparisons/*` | `database-handbook/*` | "See also" — ADR context only |
| `06-interview-guide/top-150` | Topic pages | `Deep Dive` column = Hugo URL + `#anchor` |
| `01-fundamentals/atlas-basics` | `04-production-operations/*` | Ops depth |
| `03-query-performance/indexes` | `explain-plan`, `query-optimization` | No duplicate explain tables |

---

## Yaml Files to Update (Phase B)

| File | Change |
| :--- | :--- |
| `data/mongodb_cheatsheet_modules.yaml` | 7 modules, nested topic slugs |
| `data/mongodb_cheatsheet_order.yaml` | Full reading order (~36 topics) |
| `data/curriculum_sections.yaml` | Optional `menuLabel` tweak: "MongoDB Handbook" |
| `data/curriculum_sidebar.yaml` | Verify section appears under handbooks group |

**Out of scope:** `database_handbook_modules.yaml`, `kafka_handbook_*`, other handbooks.

---

## GitHub Pages Optimization

- Nested URLs improve information scent (`/02-core-mongodb/replication/`).
- Aliases prevent 404s from existing links in blog posts and `_index.md`.
- Section `_index.md` pages become crawl hubs for each module.
- Top 150 page: table of contents with category anchors (Architecture, Troubleshooting, Performance, Reliability, Security).
- `ShowToc: true` on all architect-depth pages.

---

## Optional Future: Slug Rename

| Option | Pros | Cons |
| :--- | :--- | :--- |
| Keep `mongodb-cheatsheet` | No curriculum yaml change; aliases sufficient | URL says "cheatsheet" |
| Rename to `mongodb-handbook` | Matches content positioning | Requires `curriculum_sections.yaml`, layouts, all inbound links |

**Phase A recommendation:** Keep slug; update titles and menu label only.

---

## Phase B Navigation Checklist

- [ ] Create 7 module folders + section `_index.md`
- [ ] Move files with aliases
- [ ] Update yaml modules + order
- [ ] Rewrite handbook `_index.md`
- [ ] Fix all internal `/mongodb-cheatsheet/<flat>/` links in moved files
- [ ] Verify Hugo build + sidebar resolution
