---
title: "Go Handbook Infographic Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["golang-cheatsheet", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, and optional future static images — not separate image assets unless generated later.

**Meta file:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Quick revision card | Markdown table + bullets | Page **Quick Revision** section |
| Decision tree | Mermaid `flowchart TD` | Troubleshooting, production, escape-analysis |
| Comparison one-pager | Markdown table | Mutex vs channel, stack vs heap |
| Interview cram sheet | Single-page topic table | `09-learning-paths/golang-interview-revision-path.md` |
| Runtime poster | Mermaid `flowchart TB` | `go-runtime.md`, `scheduler.md` |
| Checklist card | Markdown checklist | `production-checklists.md` |

---

## By Major Topic

### 01 Fundamentals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Slice header (ptr/len/cap) | 3-column reference card | `01-fundamentals/slices.md` | — Partial |
| append growth factor | Table (~2x) | `01-fundamentals/slices.md` | P1 |
| Array vs slice | Side-by-side card | `01-fundamentals/arrays.md` | — Exists (table) |
| Map ops quick ref | Operator table | `01-fundamentals/maps.md` | — Exists |
| Receiver decision | Value vs pointer matrix | `01-fundamentals/methods.md` | P1 |

### 02 Core Go

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Nil interface trap | Before/after `(type,data)` card | `02-core-go/interfaces.md` | P0 |
| Error tools matrix | `Is` / `As` / `%w` when-to-use | `02-core-go/error-handling.md` | P1 |
| go.mod directives | Directive cheat sheet | `02-core-go/go-modules.md` | — Partial |
| MVS vs pinning | Comparison card | `02-core-go/dependency-management.md` | P2 |

### 03 Go Internals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Runtime component map | Layered stack poster | `03-go-internals/go-runtime.md` | P0 |
| GMP one-pager | G/M/P roles table | `03-go-internals/scheduler.md` | P0 |
| Preemption timeline | Go 1.14+ async preemption | `03-go-internals/scheduler.md` | P1 |
| Happens-before sources | Table (chan, mutex, atomic, Once) | `03-go-internals/memory-model.md` | — Partial |
| GC phases | Tri-color visual | `03-go-internals/garbage-collection.md` | — Partial |
| GOGC knob card | Heap trigger formula | `03-go-internals/garbage-collection.md` | P1 |
| Escape rules | "Stays on stack if…" checklist | `03-go-internals/escape-analysis.md` | P0 |
| Reflection cost | When to use / avoid matrix | `03-go-internals/reflection.md` | P2 |

### 04 Concurrency

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Channel semantics | Buffered vs unbuffered card | `04-concurrency/channels.md` | P1 |
| select patterns | Timeout / default / nil chan | `04-concurrency/select.md` | P1 |
| Context constructors | When to use which | `04-concurrency/context.md` | P1 |
| Mutex vs channel | Decision matrix (share memory / communicate) | `04-concurrency/concurrency-patterns.md` | P0 |
| sync package map | Type → use case table | `04-concurrency/sync-package.md` | — Partial |
| Concurrency pattern catalog | Worker pool / pipeline / fan-out | `04-concurrency/concurrency-patterns.md` | P0 |
| Goroutine leak symptoms | Symptom → cause table | `04-concurrency/goroutines.md` | P1 |

### 05 Performance

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| pprof profile types | CPU / heap / goroutine / block / mutex | `05-performance/profiling.md` | P0 |
| Profiling workflow | Capture → analyze → validate | `05-performance/profiling.md` | P0 |
| Allocation tactics | Pool / prealloc / value semantics | `05-performance/performance-optimization.md` | P1 |
| Benchmark flags | `-bench`, `-benchmem`, `-cpuprofile` | `05-performance/benchmarking.md` | P1 |
| Struct layout | Field order / padding example | `05-performance/memory-optimization.md` | P2 |

### 06 Production Go

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Structured logging fields | Required production fields | `06-production-go/logging.md` | P1 |
| Config precedence | Env > file > default | `06-production-go/configuration-management.md` | P1 |
| Observability pillars | Metrics / traces / logs | `06-production-go/observability.md` | P1 |
| Graceful shutdown phases | Stop accept → drain → cleanup | `06-production-go/graceful-shutdown.md` | P0 |
| Production readiness checklist | Pre-deploy card | `06-production-go/production-checklists.md` | P0 |
| `-race` in CI | When required matrix | `06-production-go/production-checklists.md` | P1 |

### 07 Testing

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Table-driven template | Scaffold card | `07-testing/testing.md` | — Partial |
| Test type matrix | Unit / integration / fuzz / bench | `07-testing/test-strategies.md` | P1 |
| Mock strategies | Hand mock vs codegen | `07-testing/mocking.md` | P1 |

### 08 Interview Guide

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 150 topic index | Category → count table | `08-interview-guide/top-150-interview-questions.md` | P0 |
| Architect probes | Printable question list | `08-interview-guide/architect-questions.md` | P1 |
| 30-minute revision | One-page cram sheet | `09-learning-paths/golang-interview-revision-path.md` | P0 |
| Question → page map | Deep dive link table | `08-interview-guide/top-150-interview-questions.md` | P0 |

### 09 Learning Paths

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Senior engineer path | Week-by-week reading order | `09-learning-paths/golang-senior-engineer-path.md` | P1 |
| Lead path | Concurrency + production focus | `09-learning-paths/golang-lead-path.md` | P1 |
| Architect path | Runtime + tradeoffs spine | `09-learning-paths/golang-architect-path.md` | P1 |
| Concept registry visual | Topic → canonical page (subset) | `_meta/concept-registry.md` | P2 |

---

## Revision Sheet Consolidation

Prefer **`09-learning-paths/golang-interview-revision-path.md`** as the single printable cram page:

| Section | Source pages |
| :--- | :--- |
| Runtime cram | `go-runtime`, `scheduler`, `escape-analysis`, `garbage-collection` Quick Revision |
| Concurrency cram | `goroutines`, `channels`, `context`, `concurrency-patterns` |
| Performance cram | `profiling`, `performance-optimization` |
| Production cram | `graceful-shutdown`, `observability`, `production-checklists` |
| Top traps | `interfaces` (nil), `slices` (aliasing), `maps` (concurrent) |

---

## Production Checklist Infographics

Embed in **Checklists** section (Phase C):

| Checklist | Page |
| :--- | :--- |
| Service go-live | `06-production-go/production-checklists.md` |
| Concurrency review | `04-concurrency/concurrency-patterns.md` |
| Performance review | `05-performance/performance-optimization.md` |
| Observability baseline | `06-production-go/observability.md` |
| Interview day-of | `09-learning-paths/golang-interview-revision-path.md` |

---

## Priority Summary

| Priority | Deliverables |
| :---: | :--- |
| **P0** | Nil interface card, GMP one-pager, escape checklist, mutex-vs-channel matrix, pprof types card, graceful shutdown phases, Top 150 index, 30-min revision sheet |
| **P1** | GOGC card, context constructors, channel semantics, config precedence, observability pillars, test type matrix |
| **P2** | MVS card, struct padding, reflection matrix, concept registry visual |

---

## Asset Generation Notes

- **Phase B:** Markdown tables on new page skeletons; migrate existing tables from flat pages
- **Phase C:** Mermaid per `mermaid-plan.md`; expand Quick Revision sections
- **Phase D:** Answer-layer interview blocks with embedded mini-cards
- **Build script:** Do not regenerate infographic sections from `build_golang_cheatsheet.py`
- **Future:** Optional PNG/SVG exports from Mermaid — out of scope Phase A–B

---

**STOP — Implement infographics during Phase C content depth work.**
