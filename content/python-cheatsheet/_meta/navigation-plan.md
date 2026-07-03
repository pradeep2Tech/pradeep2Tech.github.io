---
title: "Python Handbook Navigation Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["python-cheatsheet", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/python_cheatsheet_modules.yaml` and `data/python_cheatsheet_order.yaml`.

**Hugo section slug:** `python-cheatsheet` (unchanged in Phase B unless rename approved — avoids breaking `curriculum_sections.yaml`).

**Folder naming:** Numbered modules inside `content/python-cheatsheet/` mirror `kafka-handbook` / `mongodb-cheatsheet` pattern.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo |
| :--- | :---: | :---: | :---: |
| Language Basics | 1 | 2 | 2 |
| Collections & Comprehensions | 2 | 2 | 2 |
| OOP | 3 | 2 | 2 |
| Modules & Packages | 4 | 1 | 1 |
| Advanced Language Features | 5 | 7 | 7 |
| Concurrency | 6 | 4 | 4 |
| Runtime & Tooling | 7 | 3 | 3 |
| Interview Cheat Sheets | 8 | 1 | 1 |

**Total topic pages:** 22 (+ `_index.md`)  
**Structure:** Flat files at section root — no nested folders  
**Sidebar resolution:** `site.GetPage "python-cheatsheet/<slug>"`

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "Fundamentals"
    path: "01-fundamentals"
    topics:
      - 01-fundamentals/language-basics
      - 01-fundamentals/functions
      - 01-fundamentals/collections
      - 01-fundamentals/modules
      - 01-fundamentals/exceptions
      - 01-fundamentals/typing

  - id: 2
    focus: "Core Python"
    path: "02-core-python"
    topics:
      - 02-core-python/oop
      - 02-core-python/classes
      - 02-core-python/dataclasses
      - 02-core-python/decorators
      - 02-core-python/context-managers
      - 02-core-python/iterators
      - 02-core-python/generators
      - 02-core-python/comprehensions

  - id: 3
    focus: "Python Internals"
    path: "03-python-internals"
    topics:
      - 03-python-internals/python-runtime
      - 03-python-internals/cpython-internals
      - 03-python-internals/bytecode
      - 03-python-internals/object-model
      - 03-python-internals/memory-management
      - 03-python-internals/garbage-collection
      - 03-python-internals/gil

  - id: 4
    focus: "Concurrency"
    path: "04-concurrency"
    topics:
      - 04-concurrency/concurrency
      - 04-concurrency/asyncio
      - 04-concurrency/multithreading
      - 04-concurrency/multiprocessing
      - 04-concurrency/concurrency-patterns

  - id: 5
    focus: "Performance"
    path: "05-performance"
    topics:
      - 05-performance/performance-optimization
      - 05-performance/profiling
      - 05-performance/benchmarking
      - 05-performance/memory-optimization

  - id: 6
    focus: "Production Python"
    path: "06-production-python"
    topics:
      - 06-production-python/logging
      - 06-production-python/configuration-management
      - 06-production-python/observability
      - 06-production-python/error-handling
      - 06-production-python/production-checklists

  - id: 7
    focus: "Packaging & Distribution"
    path: "07-packaging-distribution"
    topics:
      - 07-packaging-distribution/packaging
      - 07-packaging-distribution/dependency-management
      - 07-packaging-distribution/poetry
      - 07-packaging-distribution/virtual-environments

  - id: 8
    focus: "Testing"
    path: "08-testing"
    topics:
      - 08-testing/testing
      - 08-testing/pytest
      - 08-testing/mocking
      - 08-testing/test-strategies

  - id: 9
    focus: "Interview Guide"
    path: "09-interview-guide"
    topics:
      - 09-interview-guide/top-150-interview-questions
      - 09-interview-guide/architect-questions
      - 09-interview-guide/troubleshooting-questions
      - 09-interview-guide/performance-questions

  - id: 10
    focus: "Learning Paths"
    path: "10-learning-paths"
    topics:
      - 10-learning-paths/python-senior-engineer-path
      - 10-learning-paths/python-lead-path
      - 10-learning-paths/python-architect-path
      - 10-learning-paths/python-interview-revision-path
```

**Total topic pages after Phase B:** 49 (+ 10 module `_index.md` + section `_index.md`)

---

## URL Aliases (Backward Compatibility)

Phase B should add Hugo `aliases` on moved pages to preserve existing links:

| Old path | New path |
| :--- | :--- |
| `/python-cheatsheet/language-basics/` | `/python-cheatsheet/01-fundamentals/language-basics/` |
| `/python-cheatsheet/functions/` | `/python-cheatsheet/01-fundamentals/functions/` |
| `/python-cheatsheet/collections/` | `/python-cheatsheet/01-fundamentals/collections/` |
| `/python-cheatsheet/modules/` | `/python-cheatsheet/01-fundamentals/modules/` |
| `/python-cheatsheet/exceptions/` | `/python-cheatsheet/01-fundamentals/exceptions/` |
| `/python-cheatsheet/typing/` | `/python-cheatsheet/01-fundamentals/typing/` |
| `/python-cheatsheet/oop/` | `/python-cheatsheet/02-core-python/oop/` |
| `/python-cheatsheet/classes/` | `/python-cheatsheet/02-core-python/classes/` |
| `/python-cheatsheet/dataclasses/` | `/python-cheatsheet/02-core-python/dataclasses/` |
| `/python-cheatsheet/decorators/` | `/python-cheatsheet/02-core-python/decorators/` |
| `/python-cheatsheet/context-managers/` | `/python-cheatsheet/02-core-python/context-managers/` |
| `/python-cheatsheet/iterators/` | `/python-cheatsheet/02-core-python/iterators/` |
| `/python-cheatsheet/generators/` | `/python-cheatsheet/02-core-python/generators/` |
| `/python-cheatsheet/comprehensions/` | `/python-cheatsheet/02-core-python/comprehensions/` |
| `/python-cheatsheet/concurrency/` | `/python-cheatsheet/04-concurrency/concurrency/` |
| `/python-cheatsheet/asyncio/` | `/python-cheatsheet/04-concurrency/asyncio/` |
| `/python-cheatsheet/multithreading/` | `/python-cheatsheet/04-concurrency/multithreading/` |
| `/python-cheatsheet/multiprocessing/` | `/python-cheatsheet/04-concurrency/multiprocessing/` |
| `/python-cheatsheet/memory-management/` | `/python-cheatsheet/03-python-internals/memory-management/` |
| `/python-cheatsheet/packaging/` | `/python-cheatsheet/07-packaging-distribution/packaging/` |
| `/python-cheatsheet/virtual-environments/` | `/python-cheatsheet/07-packaging-distribution/virtual-environments/` |
| `/python-cheatsheet/interview-questions/` | `/python-cheatsheet/09-interview-guide/top-150-interview-questions/` |

---

## Section `_index.md` Updates (Phase B)

| Element | Current | Target |
| :--- | :--- | :--- |
| Page count | "22 pages · 8 modules" | "~49 pages · 10 modules" |
| Entry point | Language Basics only | Module map + recommended learning paths |
| Cross-links | Microservices only | Interview guide + internals module callout |
| Audience note | Implicit | Explicit: 6+ years, senior/lead/architect |

---

## Module `_index.md` Files (Phase B Create)

Each numbered folder gets a landing page with:

- Module purpose (2–3 sentences)
- Topic list with one-line descriptions
- Recommended reading order
- Link to relevant learning path
- "Prerequisites" links to prior modules

---

## Prev/Next Navigation

**Current:** Hardcoded in each page `See Also` section.  
**Phase B:** Update `See Also` to module-aware prev/next following yaml order. Optionally enhance `section-nav.html` if it already supports nested paths (verify during Phase B).

**Reading order highlights:**

1. `01-fundamentals` → `02-core-python` → `03-python-internals` (internals after language familiarity)
2. `04-concurrency` requires `03-python-internals/gil.md`
3. `05-performance` requires internals + concurrency context
4. `06-production-python` after fundamentals + concurrency
5. `08-testing` parallel with production module
6. `09-interview-guide` after topic coverage
7. `10-learning-paths` as entry hub alternative

---

## Interview Answer Map (Layer 2)

Every Top 150 question links to one canonical answer location:

| Question category | Primary answer pages |
| :--- | :--- |
| Internals & Runtime (40) | `python-runtime`, `cpython-internals`, `bytecode`, `object-model`, `gil`, `garbage-collection`, `memory-management` |
| Concurrency & Async (30) | `gil`, `asyncio`, `multithreading`, `multiprocessing`, `concurrency`, `concurrency-patterns` |
| Performance (25) | `performance-optimization`, `profiling`, `benchmarking`, `memory-optimization` |
| Troubleshooting (20) | `profiling`, `garbage-collection`, `gil`, `asyncio`, `error-handling`, `observability` |
| Production Engineering (15) | `logging`, `configuration-management`, `observability`, `production-checklists` |
| Language & OOP (20 overflow) | `02-core-python/*`, `01-fundamentals/*` |

**Deep dive link format in Top 150:**

```markdown
| # | Question | Deep Dive |
| 1 | Why does the GIL exist? | [gil.md](/python-cheatsheet/03-python-internals/gil/#question-why-does-the-gil-exist) |
```

**Phase B batches:** Add `## Question` blocks in groups of 25 per module to avoid single-file churn.

---

## Top 150 Distribution (Planned)

| Category | Count | Subset files |
| :--- | :---: | :--- |
| Internals & Runtime | 40 | architect-questions (10), top-150 |
| Concurrency & Async | 30 | architect-questions (5), top-150 |
| Performance | 25 | performance-questions (25) |
| Troubleshooting | 20 | troubleshooting-questions (20) |
| Production Engineering | 15 | architect-questions (10), top-150 |
| Core Python & Typing | 20 | architect-questions (overflow), top-150 |
| **Total** | **150** | |

---

## Cross-Handbook Links (Link Only — No Duplication)

| External section | Link from | Purpose |
| :--- | :--- | :--- |
| `microservices/` | `_index.md`, production-checklists | Service patterns boundary |
| `interview-prep/` | `09-interview-guide/_index.md` | Language-agnostic prep |
| `dsa-coding/` | `performance-optimization.md` | Algorithm problems — not Python internals |

---

## Build Script & Data File Changes (Phase B)

| File | Change |
| :--- | :--- |
| `data/python_cheatsheet_modules.yaml` | 8 → 10 modules; nested topic paths |
| `data/python_cheatsheet_order.yaml` | Regenerate flat topic list from modules |
| `scripts/build_python_cheatsheet_handbook.py` | Add 28 new `TOPIC_META` entries; support nested paths; optional architect template for internals/production/testing pages |
| `data/curriculum_sidebar.yaml` | Verify `python-cheatsheet` entry unchanged |

---

## GitHub Pages Verification Checklist (Phase B)

- [ ] All 22 legacy URLs resolve via aliases
- [ ] Sidebar shows 10 modules with correct nesting
- [ ] `_index.md` module map links resolve
- [ ] Top 150 deep dive links hit valid anchors
- [ ] `draft: true` on `_meta/*` pages (planning only)
- [ ] Mermaid renders on internals + concurrency pages

---

**Phase A navigation plan complete. Awaiting approval before Phase B.**
