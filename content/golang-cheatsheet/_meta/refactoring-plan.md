---
title: "Go Handbook Refactoring Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Phase A inventory — quality, duplication, gaps, and recommended actions."
tags: ["golang-cheatsheet", "meta", "planning"]
---

# Phase A — Repository Inventory

**Scope:** `content/golang-cheatsheet/` (25 topic pages + `_index.md`)  
**Audience:** Senior Engineers, Technical Leads, Architects (6+ years)  
**Status:** Planning only — **no content rewritten in Phase A**

**Target structure:** 9 modules (`01-fundamentals` … `09-learning-paths`) + `_meta/` — implemented in Phase B within the same Hugo section slug (`golang-cheatsheet`) unless slug rename is approved separately.

---

## Executive Summary

| Metric | Assessment |
| :--- | :--- |
| **Structure** | **Flat** — 10 modules in `data/golang_cheatsheet_modules.yaml`; no numbered folders |
| **Template compliance** | Cheat-sheet skeleton (`At a Glance`, `Reference Tables`, `Snippets`, `Internals & Gotchas`) — **not** the 12-section architect template |
| **Average page depth** | ~70–100 lines — strong for 2-minute brush-up; **weak** for senior/architect depth |
| **Duplication** | **Moderate–High** — method sets, WaitGroup, sync.Map, context cancellation, fan-in, GMP scheduler, allocation tuning repeated across 2–4 files |
| **Canonical discipline** | **None** — no concept registry enforced |
| **Interview Layer 1** | **Wrong model** — `interview-questions.md` has ~8 answered probes inline (not 150 questions-only) |
| **Interview Layer 2** | **Missing** — no `## Question` answer blocks on topic pages |
| **Runtime / internals** | **Fragmented** — GMP only on `goroutines.md`; no `go-runtime`, `scheduler`, or `escape-analysis` pages |
| **Performance** | **Missing module** — `pprof` mentioned once in `garbage-collection.md`; no profiling, benchmarking, or optimization pages |
| **Production engineering** | **Absent** — no logging, observability, config, or graceful shutdown |
| **Testing** | **Thin** — table tests + benchmarks only; no mocking or integration strategy |
| **Build scripts** | `scripts/build_golang_cheatsheet.py` — hand edits **overwritten on regen** unless script updated |

**Recommended Phase B focus:** Restructure into 9 modules, enforce concept registry, preserve valuable cheat-sheet tables/snippets, create 24 missing canonical pages, replace interview layer, add learning paths, update `golang_cheatsheet_modules.yaml` — **not** a Hugo slug rename.

---

## Scoring Guide

| Dimension | 1 | 10 |
| :--- | :--- | :--- |
| **Quality** | Inaccurate or trivial | Accurate, production-grade, maintainable |
| **Duplication** | Unique (1) | Heavily repeated elsewhere (10) |
| **Interview Value** | Not useful in senior interviews | High architect-panel value |

Subscores in **Quality**: accuracy, production relevance, internals depth, concurrency depth, performance depth, interview usefulness.

---

## File Inventory

| File | Purpose | Quality | Duplication | Interview Value | Problems | Action |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| `_index.md` | Section landing; module map; regen instructions | 6 | 2 | 5 | Cheat-sheet positioning; links Design Patterns/Microservices; no learning paths | **Keep** — rebrand as Go Handbook; 9-module map; link `09-learning-paths/` |
| `language-basics.md` | Syntax, types, zero values, control flow | 5 | 3 | 3 | Beginner syntax; type assertion duplicates `interfaces.md` | **Move** → `01-fundamentals/language-basics.md`; slim assertion to 1 sentence + link |
| `functions.md` | Signatures, closures, variadic, named returns | 5 | 4 | 4 | `recover` overlaps goroutines; methods pointer to methods page | **Move** → `01-fundamentals/functions.md` |
| `structs.md` | Structs, embedding, JSON tags | 6 | 3 | 5 | Solid fundamentals; shallow for architect | **Move** → `01-fundamentals/structs.md` |
| `arrays.md` | Fixed arrays vs slices | 5 | 5 | 4 | Overlaps `slices.md` array comparison table | **Move** → `01-fundamentals/arrays.md` — **canonical** for arrays only |
| `slices.md` | Slice header, append, subslicing, leaks | 7 | 4 | 8 | Best collection page; backing-array gotchas are interview-critical | **Move** → `01-fundamentals/slices.md` — **canonical** for slices |
| `maps.md` | Map ops, nil map, iteration | 6 | 6 | 6 | `sync.Map` mention duplicates `sync-package.md` | **Move** → `01-fundamentals/maps.md`; trim sync.Map to ≤2 sentences + link |
| `methods.md` | Value vs pointer receivers, method sets | 6 | 7 | 7 | Method-set rules duplicate `interfaces.md` | **Move** → `01-fundamentals/methods.md` — **canonical** for receivers/method sets |
| `interfaces.md` | Implicit interfaces, nil trap, type assert | 7 | 6 | 9 | Nil interface is high-signal; method set table duplicates `methods.md` | **Move** → `02-core-go/interfaces.md`; trim method-set depth; link `methods.md` |
| `pointers.md` | `&`, `*`, new vs make | 5 | 4 | 5 | Stack/heap not covered (→ escape-analysis) | **Move** → `02-core-go/pointers.md` |
| `packages.md` | Layout, exports, init, internal | 6 | 2 | 5 | Adequate fundamentals | **Move** → `02-core-go/packages.md` |
| `error-handling.md` | `errors.Is/As`, `%w`, sentinels | 7 | 3 | 8 | Strong idioms; no production error taxonomy | **Move** → `02-core-go/error-handling.md` — **canonical** for errors |
| `go-modules.md` | go.mod, go.sum, replace, workspace | 6 | 6 | 6 | Overlaps `dependency-management.md` on tidy/get | **Move** → `02-core-go/go-modules.md` — **canonical** for module file/directives |
| `dependency-management.md` | MVS, go get, vendoring, GOPRIVATE | 6 | 7 | 6 | `go get`/`tidy` duplicate `go-modules.md` | **Move** → `02-core-go/dependency-management.md` — **canonical** for version resolution/vendoring |
| `goroutines.md` | `go` keyword, basic GMP, leaks, GOMAXPROCS | 6 | 7 | 8 | Scheduler depth belongs on `scheduler.md`; WaitGroup duplicates `sync-package.md` | **Move** → `04-concurrency/goroutines.md`; strip GMP deep dive; link scheduler |
| `channels.md` | Buffered/unbuffered, close, fan-in snippet | 6 | 6 | 8 | Fan-in/fan-out belong on `concurrency-patterns.md` | **Move** → `04-concurrency/channels.md` — **canonical** for channel semantics |
| `select.md` | Multiplexing, default, timeouts | 6 | 5 | 7 | `ctx.Done()` case duplicates `context.md` | **Move** → `04-concurrency/select.md` |
| `context.md` | Cancellation, deadlines, WithValue | 7 | 6 | 9 | Worker loop duplicates graceful-shutdown patterns | **Move** → `04-concurrency/context.md` — **canonical** for Context API |
| `mutex.md` | sync.Mutex, defer unlock, deadlocks | 6 | 5 | 7 | SafeMap example duplicates `maps.md` concurrency note | **Move** → `04-concurrency/mutex.md` |
| `rwmutex.md` | RWMutex read/write rules | 6 | 3 | 6 | Writer starvation noted — good | **Move** → `04-concurrency/rwmutex.md` |
| `sync-package.md` | WaitGroup, Once, Pool, Cond, Map | 7 | 7 | 8 | Pool overlaps GC tuning; Map overlaps `maps.md` | **Move** → `04-concurrency/sync-package.md` — **canonical** for sync primitives |
| `memory-model.md` | Happens-before, races, atomics | 6 | 4 | 9 | Thin but accurate; no sequential consistency detail | **Move** → `03-go-internals/memory-model.md` — **canonical** |
| `garbage-collection.md` | Tri-color GC, GOGC, gctrace | 6 | 5 | 8 | pprof mention should link `profiling.md`; alloc tips → performance pages | **Move** → `03-go-internals/garbage-collection.md` — **canonical** for GC |
| `reflection.md` | reflect.Type/Value, Kind, pitfalls | 5 | 2 | 6 | Adequate overview; no iface representation detail | **Move** → `03-go-internals/reflection.md` |
| `testing.md` | Table tests, benchmarks, race flag | 5 | 3 | 6 | No mocking, integration, or fuzzing | **Move** → `07-testing/testing.md`; split strategies to new pages |
| `interview-questions.md` | 8 topic summaries + code probes with answers | 4 | 9 | 4 | Wrong interview model; duplicates slices/interfaces/concurrency | **Replace** → `08-interview-guide/top-150-interview-questions.md` + 3 subset files |

---

## Missing Files (Phase B Create)

| File | Priority | Rationale |
| :--- | :---: | :--- |
| `03-go-internals/go-runtime.md` | P0 | Runtime architecture, components, execution flow — no canonical page |
| `03-go-internals/scheduler.md` | P0 | GMP, work stealing, preemption — fragmented on `goroutines.md` |
| `03-go-internals/escape-analysis.md` | P0 | Stack vs heap, compiler escape rules — absent |
| `04-concurrency/concurrency-patterns.md` | P0 | Worker pools, fan-out/in, pipelines, backpressure — partial on `channels.md` |
| `05-performance/performance-optimization.md` | P0 | Allocation reduction, object reuse, efficient concurrency |
| `05-performance/profiling.md` | P0 | pprof CPU/heap/goroutine — one bullet in GC page only |
| `05-performance/benchmarking.md` | P0 | `testing.B`, benchstat, noise — partial on `testing.md` |
| `05-performance/memory-optimization.md` | P1 | Slice prealloc, pointer density, GC interaction |
| `06-production-go/logging.md` | P0 | Structured logging, correlation IDs — absent |
| `06-production-go/configuration-management.md` | P0 | Env vars, config loading, secrets — absent |
| `06-production-go/observability.md` | P0 | Metrics, tracing, OpenTelemetry — absent |
| `06-production-go/graceful-shutdown.md` | P0 | Signals, drain, cleanup — one line on `goroutines.md` |
| `06-production-go/production-checklists.md` | P1 | Pre-deploy / ops checklists — absent |
| `07-testing/mocking.md` | P0 | Interface mocks, test doubles, codegen |
| `07-testing/test-strategies.md` | P0 | Unit/integration/concurrency test patterns |
| `08-interview-guide/top-150-interview-questions.md` | P0 | Exactly 150 questions, no answers |
| `08-interview-guide/architect-questions.md` | P1 | Subset (~35 architect probes) |
| `08-interview-guide/troubleshooting-questions.md` | P1 | Subset (~25 troubleshooting) |
| `08-interview-guide/performance-questions.md` | P1 | Subset (~25 performance) |
| `09-learning-paths/golang-senior-engineer-path.md` | P1 | Missing |
| `09-learning-paths/golang-lead-path.md` | P1 | Missing |
| `09-learning-paths/golang-architect-path.md` | P1 | Missing |
| `09-learning-paths/golang-interview-revision-path.md` | P1 | Missing |
| Section `_index.md` × 9 | P1 | Module landing stubs |

**Total new pages:** 24 topic pages + 9 section indexes = 33 files.

---

## Duplicate Content (Semantic Overlap > 50%)

| Concept cluster | Appears in | Canonical target (Phase B) |
| :--- | :--- | :--- |
| Method sets (value vs pointer receiver) | `interfaces.md`, `methods.md`, `interview-questions.md` | `01-fundamentals/methods.md` |
| Nil interface / typed nil | `interfaces.md`, `interview-questions.md` | `02-core-go/interfaces.md` |
| Slice header / append / aliasing | `slices.md`, `arrays.md`, `interview-questions.md` | `01-fundamentals/slices.md` |
| Map concurrency safety | `maps.md`, `mutex.md`, `sync-package.md` | `01-fundamentals/maps.md` (safety); `04-concurrency/sync-package.md` (`sync.Map`) |
| GMP / M:N scheduling | `goroutines.md` (diagram + bullets) | `03-go-internals/scheduler.md` |
| WaitGroup coordination | `goroutines.md`, `channels.md`, `sync-package.md` | `04-concurrency/sync-package.md` |
| Context cancellation | `context.md`, `select.md`, `goroutines.md` | `04-concurrency/context.md` |
| Fan-in / fan-out | `channels.md` (merge snippet) | `04-concurrency/concurrency-patterns.md` |
| sync.Pool / allocation reduction | `sync-package.md`, `garbage-collection.md` | `05-performance/performance-optimization.md` + `sync-package.md` (API) |
| GOGC / GC pacing | `garbage-collection.md` | `03-go-internals/garbage-collection.md` |
| pprof / heap profiling | `garbage-collection.md` (one row) | `05-performance/profiling.md` |
| go get / go mod tidy | `go-modules.md`, `dependency-management.md` | Split: directives → `go-modules.md`; commands/MVS → `dependency-management.md` |
| Benchmarks | `testing.md` | `05-performance/benchmarking.md` (depth); `07-testing/testing.md` (basics) |
| Race detector | `memory-model.md`, `testing.md` | `03-go-internals/memory-model.md` (why); `07-testing/testing.md` (how in CI) |
| Graceful shutdown | `goroutines.md` (one bullet) | `06-production-go/graceful-shutdown.md` |
| Generic "See Effective Go" production note | **All 25 pages** | Replace with page-specific production guidance in Phase C |

---

## Weak Files (Quality ≤ 5 or Architect Depth Insufficient)

| File | Issue | Phase B/C action |
| :--- | :--- | :--- |
| `language-basics.md` | Certification-style syntax; low senior value | Keep as quick-revision only; no expansion |
| `arrays.md` | Very thin; rarely standalone interview topic | Keep short; cross-link slices |
| `pointers.md` | No escape-analysis linkage | Add 2-sentence pointer + link `escape-analysis.md` |
| `packages.md` | No build tags, `go:embed`, or module boundaries | Expand in Phase C |
| `reflection.md` | No interface representation (iface/eface) | Expand Internal Working in Phase C |
| `testing.md` | No fuzzing (`testing.F`), httptest, or build tags | Split; link `mocking.md`, `test-strategies.md` |
| `interview-questions.md` | Wrong format; duplicates 6 topic summaries | **Delete** after migration to `08-interview-guide/` |

---

## Fragmented Concepts (No Single Canonical Home)

| Concept | Current state | Canonical page (new or existing) |
| :--- | :--- | :--- |
| Go runtime architecture | Scattered on `goroutines.md` | `03-go-internals/go-runtime.md` **NEW** |
| GMP scheduler / preemption | One diagram on `goroutines.md` | `03-go-internals/scheduler.md` **NEW** |
| Escape analysis / stack vs heap | Not covered | `03-go-internals/escape-analysis.md` **NEW** |
| Worker pools / pipelines | Fan-in snippet on `channels.md` | `04-concurrency/concurrency-patterns.md` **NEW** |
| CPU/memory/goroutine profiling | One table row in GC | `05-performance/profiling.md` **NEW** |
| Benchmark methodology | Partial on `testing.md` | `05-performance/benchmarking.md` **NEW** |
| Structured logging / correlation | Absent | `06-production-go/logging.md` **NEW** |
| OpenTelemetry / metrics | Absent | `06-production-go/observability.md` **NEW** |
| Signal handling / drain | One bullet | `06-production-go/graceful-shutdown.md` **NEW** |
| Interface-based mocks | Absent | `07-testing/mocking.md` **NEW** |

---

## Outdated or Inaccurate Content

| Location | Issue | Severity |
| :--- | :--- | :--- |
| `functions.md` L54 | Broken string literal in `logf` snippet (`format+"` newline) | **Bug** — fix in Phase B |
| `_index.md` | "25 pages · 10 modules" — will change | Cosmetic |
| `goroutines.md` Mermaid | Simplified G→P→M; missing local run queue / work stealing | Incomplete, not wrong |
| `garbage-collection.md` | "non-generational" — correct for current GC; note hybrid aspects in Phase C | Low |
| All pages | `Production Notes` → generic Effective Go link | **Placeholder** — not production guidance |

---

## Interview Readiness Gap

| Requirement | Current | Target (Phase B) |
| :--- | :--- | :--- |
| Top 150 questions | 0 (8 inline Q&A instead) | `08-interview-guide/top-150-interview-questions.md` |
| Distribution: 40 internals | ~5 implicit in pages | 40 tagged questions |
| Distribution: 30 concurrency | ~8 | 30 tagged questions |
| Distribution: 25 performance | ~2 | 25 tagged questions |
| Distribution: 20 troubleshooting | 0 | 20 tagged questions |
| Distribution: 15 production | 0 | 15 tagged questions |
| Remaining 20 | — | Core Go, testing, errors (senior-level) |
| Answer layer | None | `## Question` blocks on canonical pages |
| Subset files | None | architect, troubleshooting, performance |
| Deep dive links | N/A | Hugo URLs + `#` anchors |

---

## Hugo / Navigation Changes (Phase B Preview)

| Asset | Current | Phase B |
| :--- | :--- | :--- |
| Section slug | `golang-cheatsheet` | **Keep** (curriculum yaml unchanged unless approved) |
| Module data | `data/golang_cheatsheet_modules.yaml` (10 flat modules) | 9 modules with nested paths |
| Order data | `data/golang_cheatsheet_order.yaml` | Regenerate from modules |
| Layouts | `layouts/golang-cheatsheet/` | Verify nested path resolution |
| Aliases | None | Flat URLs → nested paths (e.g. `/golang-cheatsheet/goroutines/`) |
| Build script | `scripts/build_golang_cheatsheet.py` | Update `PAGE_BODIES` or disable regen for handbook pages |
| `cheatSheet: true` | All pages | **Hybrid:** quick-revision sections retain cheat-sheet UX; internals/production pages use full template |

---

## Phase B Task Checklist (Awaiting Approval)

1. Create `_meta/` files (this Phase A deliverable) ✓
2. Create numbered module folders + section `_index.md` stubs
3. Move 25 existing pages to target paths (preserve content)
4. Create 24 missing canonical pages (skeleton + Quick Revision minimum)
5. Delete `interview-questions.md` after Top 150 migration
6. Generate `top-150-interview-questions.md` (150 questions, no answers)
7. Create architect / troubleshooting / performance subset files
8. Update `golang_cheatsheet_modules.yaml` + order yaml
9. Add Hugo aliases for all flat → nested URL moves
10. Update `_index.md` landing (handbook positioning, learning paths)
11. Fix `functions.md` broken snippet
12. Update build script to avoid overwriting handbook content

**Phase C (post-structure):** Enforce concept registry (≤2 sentences + link), add answer layer batched by module, Mermaid per `mermaid-plan.md`, depth expansion per canonical template.

---

**STOP — Await approval before Phase B content or structure changes.**
