---
title: "PostgreSQL Handbook Navigation Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["postgresql-cheatsheet", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/postgresql_cheatsheet_modules.yaml` and `postgresql_cheatsheet_order.yaml`.

**Hugo section slug:** `postgresql-cheatsheet` (unchanged in Phase B unless rename approved — avoids breaking `curriculum_sections.yaml`).

**Folder naming:** Numbered modules inside `content/postgresql-cheatsheet/` mirror `kafka-handbook` / `mongodb-cheatsheet` pattern.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo |
| :--- | :---: | :---: | :---: |
| Getting Started | 1 | 3 | 3 |
| DDL & DML | 2 | 3 | 3 |
| Query Performance | 3 | 3 | 3 |
| Transactions & Concurrency | 4 | 4 | 4 |
| Scaling & HA | 5 | 3 | 3 |
| Advanced SQL | 6 | 5 | 5 |
| Server-Side Programming | 7 | 3 | 3 |
| Operations & Maintenance | 8 | 2 | 2 |
| Interview Prep | 9 | 1 | 1 |

**Total topic pages:** 27 (+ `_index.md`)  
**Structure:** Flat files at section root — no nested folders  
**Sidebar resolution:** `site.GetPage "postgresql-cheatsheet/<slug>"`  
**Build script:** `scripts/build_postgresql_cheatsheet.py` — must be updated in Phase B

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "Fundamentals"
    path: "01-fundamentals"
    topics:
      - 01-fundamentals/sql-basics
      - 01-fundamentals/ddl
      - 01-fundamentals/dml
      - 01-fundamentals/joins
      - 01-fundamentals/ctes
      - 01-fundamentals/window-functions      # extension
      - 01-fundamentals/installation          # appendix / demoted

  - id: 2
    focus: "Core PostgreSQL"
    path: "02-core-postgresql"
    topics:
      - 02-core-postgresql/architecture           # NEW
      - 02-core-postgresql/storage-engine         # NEW
      - 02-core-postgresql/wal                    # NEW
      - 02-core-postgresql/mvcc
      - 02-core-postgresql/transactions
      - 02-core-postgresql/isolation-levels
      - 02-core-postgresql/locks

  - id: 3
    focus: "Query Performance"
    path: "03-query-performance"
    topics:
      - 03-query-performance/indexes
      - 03-query-performance/explain
      - 03-query-performance/query-optimization   # NEW
      - 03-query-performance/performance-tuning
      - 03-query-performance/partitioning
      - 03-query-performance/sharding             # extension

  - id: 4
    focus: "High Availability"
    path: "04-high-availability"
    topics:
      - 04-high-availability/replication
      - 04-high-availability/failover             # NEW
      - 04-high-availability/backup-restore
      - 04-high-availability/disaster-recovery    # NEW

  - id: 5
    focus: "Advanced Features"
    path: "05-advanced-features"
    topics:
      - 05-advanced-features/functions
      - 05-advanced-features/stored-procedures
      - 05-advanced-features/triggers
      - 05-advanced-features/materialized-views
      - 05-advanced-features/json
      - 05-advanced-features/views                # optional keep

  - id: 6
    focus: "Production Operations"
    path: "06-production-operations"
    topics:
      - 06-production-operations/vacuum
      - 06-production-operations/monitoring         # NEW
      - 06-production-operations/capacity-planning  # NEW
      - 06-production-operations/troubleshooting    # NEW
      - 06-production-operations/connection-pooling # NEW

  - id: 7
    focus: "Comparisons"
    path: "07-comparisons"
    topics:
      - 07-comparisons/postgresql-vs-mysql          # NEW
      - 07-comparisons/postgresql-vs-oracle         # NEW
      - 07-comparisons/postgresql-vs-mongodb        # NEW

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
      - 09-learning-paths/postgresql-senior-engineer-path
      - 09-learning-paths/postgresql-lead-path
      - 09-learning-paths/postgresql-architect-path
      - 09-learning-paths/postgresql-interview-revision-path
```

**Topic count after Phase B:** 27 moved − 1 merged (`most-common-sql-commands`) + 18 new + 4 interview + 4 learning paths = **~52 pages** (+ 9 section indexes + handbook `_index` + `_meta`)

---

## URL Aliases (Backward Compatibility)

Add Hugo front matter `aliases` on moved pages to preserve GitHub Pages links:

| Old URL | New URL |
| :--- | :--- |
| `/postgresql-cheatsheet/sql-basics/` | `/postgresql-cheatsheet/01-fundamentals/sql-basics/` |
| `/postgresql-cheatsheet/ddl/` | `/postgresql-cheatsheet/01-fundamentals/ddl/` |
| `/postgresql-cheatsheet/dml/` | `/postgresql-cheatsheet/01-fundamentals/dml/` |
| `/postgresql-cheatsheet/joins/` | `/postgresql-cheatsheet/01-fundamentals/joins/` |
| `/postgresql-cheatsheet/ctes/` | `/postgresql-cheatsheet/01-fundamentals/ctes/` |
| `/postgresql-cheatsheet/window-functions/` | `/postgresql-cheatsheet/01-fundamentals/window-functions/` |
| `/postgresql-cheatsheet/installation/` | `/postgresql-cheatsheet/01-fundamentals/installation/` |
| `/postgresql-cheatsheet/most-common-sql-commands/` | `/postgresql-cheatsheet/06-production-operations/monitoring/` (redirect note) |
| `/postgresql-cheatsheet/indexes/` | `/postgresql-cheatsheet/03-query-performance/indexes/` |
| `/postgresql-cheatsheet/explain/` | `/postgresql-cheatsheet/03-query-performance/explain/` |
| `/postgresql-cheatsheet/performance-tuning/` | `/postgresql-cheatsheet/03-query-performance/performance-tuning/` |
| `/postgresql-cheatsheet/partitioning/` | `/postgresql-cheatsheet/03-query-performance/partitioning/` |
| `/postgresql-cheatsheet/sharding/` | `/postgresql-cheatsheet/03-query-performance/sharding/` |
| `/postgresql-cheatsheet/mvcc/` | `/postgresql-cheatsheet/02-core-postgresql/mvcc/` |
| `/postgresql-cheatsheet/transactions/` | `/postgresql-cheatsheet/02-core-postgresql/transactions/` |
| `/postgresql-cheatsheet/isolation-levels/` | `/postgresql-cheatsheet/02-core-postgresql/isolation-levels/` |
| `/postgresql-cheatsheet/locks/` | `/postgresql-cheatsheet/02-core-postgresql/locks/` |
| `/postgresql-cheatsheet/replication/` | `/postgresql-cheatsheet/04-high-availability/replication/` |
| `/postgresql-cheatsheet/backup-restore/` | `/postgresql-cheatsheet/04-high-availability/backup-restore/` |
| `/postgresql-cheatsheet/vacuum/` | `/postgresql-cheatsheet/06-production-operations/vacuum/` |
| `/postgresql-cheatsheet/functions/` | `/postgresql-cheatsheet/05-advanced-features/functions/` |
| `/postgresql-cheatsheet/stored-procedures/` | `/postgresql-cheatsheet/05-advanced-features/stored-procedures/` |
| `/postgresql-cheatsheet/triggers/` | `/postgresql-cheatsheet/05-advanced-features/triggers/` |
| `/postgresql-cheatsheet/materialized-views/` | `/postgresql-cheatsheet/05-advanced-features/materialized-views/` |
| `/postgresql-cheatsheet/json/` | `/postgresql-cheatsheet/05-advanced-features/json/` |
| `/postgresql-cheatsheet/views/` | `/postgresql-cheatsheet/05-advanced-features/views/` |
| `/postgresql-cheatsheet/interview-questions/` | `/postgresql-cheatsheet/08-interview-guide/top-150-interview-questions/` |

---

## Reading Order (Recommended Defaults)

### Module 2 — Core PostgreSQL (internals first)

```
architecture → storage-engine → wal → mvcc → transactions → isolation-levels → locks
```

### Module 3 — Query Performance

```
indexes → explain → query-optimization → performance-tuning → partitioning → sharding
```

### Module 4 — High Availability

```
wal (cross-link) → replication → failover → backup-restore → disaster-recovery
```

### Module 6 — Production Operations

```
monitoring → connection-pooling → vacuum → troubleshooting → capacity-planning
```

---

## Prev/Next Chain (Phase B)

Replace flat `Related Topics` footer links with module-aware prev/next from `postgresql_cheatsheet_order.yaml`.

**Order file:** Flat list of full nested slugs (e.g. `02-core-postgresql/wal`) — ~52 entries.

**Skip in sidebar:** `_meta/*` pages (`draft: true`).

---

## `_index.md` Landing Page (Phase B)

Expand handbook `_index.md` with:

1. Audience statement (6+ years, senior, lead, architect)
2. Module table (9 modules + topic count)
3. Learning path quick links
4. Link to `database-handbook/postgresql.md` for product selection
5. Link to `_meta/concept-registry.md` (draft — optional hide from nav)

Each module `_index.md`:

- 2–3 sentence module purpose
- Ordered topic list with one-line descriptions
- "Start here" link for module entry page

---

## Cross-Link Strategy

| From | To | Rule |
| :--- | :--- | :--- |
| All topic pages | Concept registry canonical | ≤2 sentences + link for shared concepts |
| `01-fundamentals/*` | `03-query-performance/explain.md` | When mentioning optimization |
| `02-core-postgresql/mvcc.md` | `06-production-operations/vacuum.md` | Dead tuples |
| `02-core-postgresql/wal.md` | `04-high-availability/*` | Replication + DR |
| `07-comparisons/*` | `database-handbook/*` | ADR depth external |
| `08-interview-guide/*` | Canonical topic `#` anchors | Deep Dive column |
| `interview-prep/top-150` | `08-interview-guide/top-150` | Align PostgreSQL rows |

---

## GitHub Pages / Hugo Config

| Item | Action |
| :--- | :--- |
| `data/curriculum_sections.yaml` | No change — slug stays `postgresql-cheatsheet` |
| `data/postgresql_cheatsheet_modules.yaml` | Replace with 9-module structure |
| `data/postgresql_cheatsheet_order.yaml` | Replace with nested slug order |
| `scripts/build_postgresql_cheatsheet.py` | Update `TOPIC_META`, paths, template; or mark hand-crafted pages non-regen |
| Layouts | Existing `postgresql-cheatsheet/list.html` + `single.html` — verify nested path resolution |
| `ShowPageNums` | Keep on handbook `_index` |

---

## Interview Navigation (Phase B)

| Page | Sidebar label | Content |
| :--- | :--- | :--- |
| `top-150-interview-questions.md` | Top 150 Questions | 150 rows: #, Question, Level, Role, Category, Deep Dive URL |
| `architect-questions.md` | Architect Questions | 25–30 subset — questions only |
| `troubleshooting-questions.md` | Troubleshooting Drills | 25–30 subset |
| `performance-questions.md` | Performance Drills | 25–30 subset |

**Top 150 distribution target:**

| Category | Min count |
| :--- | :---: |
| Architecture | 40 |
| Troubleshooting | 30 |
| Performance | 25 |
| Reliability | 20 |
| Security | 15 |

**Role balance:** Developer, Senior Engineer, Lead, Architect across all categories.

---

## Phase B Minimum Navigation Deliverable

1. Nested folders + file moves with aliases
2. Updated yaml + order files
3. Module `_index.md` placeholders (9)
4. Expanded handbook `_index.md`
5. Delete or redirect `most-common-sql-commands.md`
6. Replace `interview-questions.md` with interview module

**STOP — await approval before executing moves.**
