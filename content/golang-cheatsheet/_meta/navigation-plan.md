---
title: "Go Handbook Navigation Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["golang-cheatsheet", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/golang_cheatsheet_modules.yaml` and `data/golang_cheatsheet_order.yaml`.

**Constraint:** Keep Hugo section slug `golang-cheatsheet` (curriculum entry unchanged unless approved). Add nested numbered folders inside the section — same pattern as `kafka-handbook/` and `mongodb-cheatsheet/`.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo |
| :--- | :---: | :---: | :---: |
| Language Basics | 1 | 2 | 2 |
| Types & Structs | 2 | 4 | 4 |
| Packages & Errors | 3 | 2 | 2 |
| Collections | 4 | 3 | 3 |
| Concurrency | 5 | 4 | 4 |
| Synchronization | 6 | 3 | 3 |
| Testing & Reflection | 7 | 2 | 2 |
| Runtime | 8 | 2 | 2 |
| Modules & Tooling | 9 | 2 | 2 |
| Interview | 10 | 1 | 1 |

**Total:** 25 flat topic pages at section root.  
**Sidebar resolution:** `site.GetPage "golang-cheatsheet/<slug>"` — nested paths require yaml update (e.g. `04-concurrency/goroutines`).

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "Fundamentals"
    topics:
      - 01-fundamentals/language-basics
      - 01-fundamentals/functions
      - 01-fundamentals/structs
      - 01-fundamentals/arrays
      - 01-fundamentals/slices
      - 01-fundamentals/maps
      - 01-fundamentals/methods

  - id: 2
    focus: "Core Go"
    topics:
      - 02-core-go/interfaces
      - 02-core-go/pointers
      - 02-core-go/packages
      - 02-core-go/go-modules
      - 02-core-go/dependency-management
      - 02-core-go/error-handling

  - id: 3
    focus: "Go Internals"
    topics:
      - 03-go-internals/go-runtime
      - 03-go-internals/scheduler
      - 03-go-internals/memory-model
      - 03-go-internals/garbage-collection
      - 03-go-internals/escape-analysis
      - 03-go-internals/reflection

  - id: 4
    focus: "Concurrency"
    topics:
      - 04-concurrency/goroutines
      - 04-concurrency/channels
      - 04-concurrency/select
      - 04-concurrency/mutex
      - 04-concurrency/rwmutex
      - 04-concurrency/sync-package
      - 04-concurrency/context
      - 04-concurrency/concurrency-patterns

  - id: 5
    focus: "Performance"
    topics:
      - 05-performance/performance-optimization
      - 05-performance/profiling
      - 05-performance/benchmarking
      - 05-performance/memory-optimization

  - id: 6
    focus: "Production Go"
    topics:
      - 06-production-go/logging
      - 06-production-go/configuration-management
      - 06-production-go/observability
      - 06-production-go/graceful-shutdown
      - 06-production-go/production-checklists

  - id: 7
    focus: "Testing"
    topics:
      - 07-testing/testing
      - 07-testing/mocking
      - 07-testing/test-strategies

  - id: 8
    focus: "Interview Guide"
    topics:
      - 08-interview-guide/top-150-interview-questions
      - 08-interview-guide/architect-questions
      - 08-interview-guide/troubleshooting-questions
      - 08-interview-guide/performance-questions

  - id: 9
    focus: "Learning Paths"
    topics:
      - 09-learning-paths/golang-senior-engineer-path
      - 09-learning-paths/golang-lead-path
      - 09-learning-paths/golang-architect-path
      - 09-learning-paths/golang-interview-revision-path
```

**Topic count:** 49 pages (25 migrated + 24 new) + 9 section indexes + handbook `_index.md`.

---

## URL Migration & Aliases

Preserve existing flat URLs with Hugo `aliases` on moved pages:

| Old URL | New path | Alias on new page |
| :--- | :--- | :--- |
| `/golang-cheatsheet/language-basics/` | `01-fundamentals/language-basics` | `/golang-cheatsheet/language-basics/` |
| `/golang-cheatsheet/goroutines/` | `04-concurrency/goroutines` | `/golang-cheatsheet/goroutines/` |
| `/golang-cheatsheet/interview-questions/` | `08-interview-guide/top-150-interview-questions` | `/golang-cheatsheet/interview-questions/` |
| … | (all 25 existing slugs) | Same pattern |

**Phase B:** Add aliases to every migrated file front matter.

---

## Reading Orders

### Senior Engineer (first pass)

1. `01-fundamentals/slices` → `02-core-go/interfaces` → `02-core-go/error-handling`
2. `04-concurrency/goroutines` → `channels` → `context` → `concurrency-patterns`
3. `03-go-internals/scheduler` → `memory-model` → `garbage-collection`
4. `07-testing/testing` → `05-performance/profiling`

### Interview Revision (48 hours)

1. `09-learning-paths/golang-interview-revision-path` (curated cram)
2. `08-interview-guide/top-150-interview-questions` (question sweep)
3. Deep dives: `interfaces`, `slices`, `scheduler`, `concurrency-patterns`, `garbage-collection`, `profiling`

### Architect Panel

1. `03-go-internals/go-runtime` → `scheduler` → `escape-analysis`
2. `04-concurrency/concurrency-patterns` → `06-production-go/graceful-shutdown` → `observability`
3. `08-interview-guide/architect-questions`

---

## Cross-Link Strategy

| From | To | Link pattern |
| :--- | :--- | :--- |
| Every page | Concept registry | Footer: "Canonical concepts → `_meta/concept-registry`" (internal meta only) |
| Fundamentals | Internals | `slices.md` → `escape-analysis.md` for heap escape |
| Concurrency | Internals | `goroutines.md` → `scheduler.md` |
| Performance | Internals | `memory-optimization.md` → `garbage-collection.md` |
| Interview questions | Topic answers | `Deep Dive` column → `/golang-cheatsheet/03-go-internals/scheduler/#q-42` |
| `_index.md` | Learning paths | Module 9 links |
| Production pages | Concurrency | `graceful-shutdown.md` → `context.md` |

**Prev/Next:** Regenerate `See Also` chains per module order in yaml (not global flat order).

---

## Landing Page (`_index.md`) Updates

| Section | Content |
| :--- | :--- |
| Title | "Go Handbook" (subtitle: senior engineer reference) |
| Audience table | Senior / Lead / Architect start paths |
| Module map | 9 modules with page counts |
| Positioning | Remove "cheat sheet only" — hybrid quick-revision + depth |
| Regen warning | Note handbook pages exempt from `build_golang_cheatsheet.py` |
| Cross-handbook | Link microservices/k8s as **peer** sections only — no content import |

---

## Sidebar / Layout Verification

| Check | Action |
| :--- | :--- |
| `curriculum_sidebar.yaml` | Confirm `golang-cheatsheet` entry uses `golang_cheatsheet_modules` |
| Nested `GetPage` | Test `hugo server` with `04-concurrency/goroutines` slug |
| `cheatSheet: true` | Fundamentals keep cheat-sheet layout; internals/production use full template |
| `ShowToc: true` | All topic pages |
| Module front matter | Update `module` / `moduleTitle` / `sectionRef` on every page |

---

## Interview Navigation

### Top 150 Distribution (exact counts)

| Category | Count | Example topics |
| :--- | :---: | :--- |
| Internals & Runtime | 40 | GMP, escape analysis, GC pacing, iface representation |
| Concurrency | 30 | Channel close, select fairness, context leaks, sync.Map |
| Performance | 25 | pprof interpretation, benchstat, allocation hotspots |
| Troubleshooting | 20 | Goroutine leak debug, deadlock, panic traces, race fixes |
| Production Engineering | 15 | Graceful shutdown, OTel, config/secrets, structured logs |
| Core Go & Testing | 20 | Nil interface, error wrapping, table tests, fuzzing |
| **Total** | **150** | |

### Subset files (questions pulled from Top 150)

| File | Target count | Focus |
| :--- | :---: | :--- |
| `architect-questions.md` | ~35 | Runtime, tradeoffs, production design |
| `troubleshooting-questions.md` | ~25 | Leaks, races, deadlocks, OOM, pprof |
| `performance-questions.md` | ~25 | GC, alloc, benchmarks, profiling |

### Answer anchor convention

```markdown
## Question: Why is a typed nil not equal to nil interface?

### Short Answer
...
```

Link from Top 150: `02-core-go/interfaces/#question-why-is-a-typed-nil-not-equal-to-nil-interface`

---

## Build Script Impact

| File | Phase B action |
| :--- | :--- |
| `scripts/build_golang_cheatsheet.py` | Stop writing to nested paths OR limit to `01-fundamentals` quick-ref regeneration |
| `data/golang_cheatsheet_modules.yaml` | Replace with 9-module structure above |
| `data/golang_cheatsheet_order.yaml` | Auto-derive flat order from modules |

---

## Phase B Navigation Checklist

1. [ ] Create 9 module folders + `_index.md` stubs
2. [ ] Move 25 files with aliases
3. [ ] Create 24 new topic pages
4. [ ] Update yaml modules + order
5. [ ] Rewrite handbook `_index.md`
6. [ ] Verify Hugo build + sidebar
7. [ ] Update `See Also` prev/next per module
8. [ ] Generate Top 150 with Deep Dive URLs

---

**STOP — Implement navigation in Phase B after approval.**
