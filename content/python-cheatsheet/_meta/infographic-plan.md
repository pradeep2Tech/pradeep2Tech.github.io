---
title: "Python Handbook Infographic Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["python-cheatsheet", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, and optional future static images — not separate image assets unless generated later.

**Meta files:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Quick revision sheet | Markdown table + bullets | Page **Quick Revision** section or `10-learning-paths/python-interview-revision-path.md` |
| Comparison one-pager | Markdown table | Topic canonical pages |
| Decision tree | Mermaid `flowchart TD` | concurrency, collections, performance, troubleshooting |
| Troubleshooting flowchart | Mermaid `flowchart TD` | profiling, garbage-collection, asyncio, error-handling |
| Interview cheat sheet | Single-page categorized table | `09-interview-guide/top-150-interview-questions.md` |
| Internals poster | Mermaid `flowchart TB` | python-runtime, cpython-internals, object-model |
| Ops runbook card | Symptom → cause → fix table | production-checklists, observability |

---

## By Module

### 01 Fundamentals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Type quick-ref | Type → mutability → hashable matrix | `language-basics.md` | P2 |
| Scope rules card | LEGB + `global`/`nonlocal` | `language-basics.md` | P2 |
| Function signature matrix | `/`, `*`, `*args`, `**kwargs` | `functions.md` | P1 |
| Collection picker | Access pattern → type | `collections.md` | P0 |
| Import style card | absolute vs relative vs package | `modules.md` | P2 |
| Exception clause order | try/except/else/finally | `exceptions.md` | P2 |
| Typing constructs card | Union, Optional, Protocol, Generic | `typing.md` | P1 |

### 02 Core Python

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| MRO diamond diagram | Multiple inheritance (exists) | `oop.md` | — Exists |
| Method types card | instance / classmethod / staticmethod | `classes.md` | P1 |
| `__eq__`/`__hash__` contract | Define both or neither | `object-model.md` | P0 |
| Dataclass option matrix | frozen/slots/kw_only/order | `dataclasses.md` | P2 |
| Decorator stack order | `@a @b` evaluation | `decorators.md` | P1 |
| Context manager API card | class vs `@contextmanager` | `context-managers.md` | P2 |
| Iterator vs generator | Protocol comparison table | `iterators.md` + `generators.md` | P1 |
| Comprehension forms | list/dict/set/gen syntax | `comprehensions.md` | P3 |

### 03 Python Internals

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Execution pipeline | source → bytecode → eval | `bytecode.md` | P0 |
| Import system layers | sys.meta_path → finder → loader | `python-runtime.md` | P0 |
| CPython stack poster | Parser, compiler, ceval, objects | `cpython-internals.md` | P0 |
| PyObject layout | ob_refcnt, ob_type, ob_ptr | `object-model.md` | P0 |
| Attribute lookup chain | instance → class → descriptor | `object-model.md` | P0 |
| Descriptor types card | data vs non-data descriptor | `object-model.md` | P1 |
| Refcount + cycle GC | Two-layer memory reclamation | `garbage-collection.md` | P0 |
| Generational GC thresholds | gen0/1/2 trigger card | `garbage-collection.md` | P1 |
| GIL timeline | acquire → bytecode ticks → release | `gil.md` | P0 |
| GIL vs free-threading | 3.13+ note card | `gil.md` | P2 |
| pymalloc overview | arenas, pools, blocks | `memory-management.md` | P1 |

### 04 Concurrency

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Concurrency model picker | I/O vs CPU (exists as mermaid) | `concurrency.md` | — Exists |
| asyncio vs threads vs processes | Feature comparison table | `concurrency.md` | P0 |
| Async pitfalls card | blocking sleep, sync HTTP, un-awaited coro | `asyncio.md` | P0 |
| Threading primitives | Lock/RLock/Condition/Event/Queue | `multithreading.md` | P1 |
| Process start methods | spawn/fork/forkserver | `multiprocessing.md` | P1 |
| Pool sizing heuristics | CPU cores vs I/O wait | `concurrency-patterns.md` | P0 |
| Producer-consumer recipe | Queue + workers + backpressure | `concurrency-patterns.md` | P0 |
| `asyncio.to_thread` pattern | When to offload blocking | `asyncio.md` | P1 |

### 05 Performance

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Optimization hierarchy | algorithm → structure → C extension | `performance-optimization.md` | P0 |
| Profiler toolkit matrix | Tool × what it measures × when | `profiling.md` | P0 |
| cProfile reading card | cumulative vs per-call | `profiling.md` | P0 |
| tracemalloc workflow | start → snapshot → compare | `profiling.md` | P1 |
| Benchmark checklist | warmup, iterations, statistics | `benchmarking.md` | P1 |
| Memory optimization patterns | slots, gens, weakref, bounded cache | `memory-optimization.md` | P0 |

### 06 Production Python

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Logging layers | logger/handler/formatter/filter | `logging.md` | P0 |
| Structured log fields | timestamp, level, trace_id, message | `logging.md` | P0 |
| Config precedence | default → file → env → secret | `configuration-management.md` | P0 |
| Observability pillars | logs, metrics, traces | `observability.md` | P0 |
| OpenTelemetry components | tracer, meter, propagator | `observability.md` | P1 |
| Exception boundary card | domain → HTTP/status mapping | `error-handling.md` | P1 |
| Pre-deploy checklist | deps, config, health, logging | `production-checklists.md` | P0 |
| Incident triage checklist | symptom → metric → action | `production-checklists.md` | P0 |

### 07 Packaging & Distribution

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| pyproject.toml anatomy | [project], [build-system], [tool] | `packaging.md` | P1 |
| src vs flat layout | pros/cons | `packaging.md` | P1 |
| Wheel vs sdist | when to publish which | `packaging.md` | P2 |
| Lock file policy | apps pin, libraries range | `dependency-management.md` | P0 |
| uv vs pip vs poetry | tool comparison | `dependency-management.md` | P1 |
| venv activation card | Unix vs Windows | `virtual-environments.md` | P2 |

### 08 Testing

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Testing pyramid | unit/integration/e2e ratios | `testing.md` | P0 |
| pytest fixture scopes | function/module/session | `pytest.md` | P1 |
| mock vs patch card | when to use which | `mocking.md` | P0 |
| patch target rules | where to patch (use path) | `mocking.md` | P0 |
| CI test stages | lint → typecheck → unit → integration | `test-strategies.md` | P1 |

### 09 Interview Guide

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 150 index | Category × count × deep dive link | `top-150-interview-questions.md` | P0 |
| Question distribution | Internals 40 / Concurrency 30 / Performance 25 / Troubleshooting 20 / Production 15 / Core 20 | `top-150-interview-questions.md` | P0 |
| Architect top picks | 25-question subset table | `architect-questions.md` | P1 |
| Troubleshooting drills | 20 scenario questions | `troubleshooting-questions.md` | P1 |
| Performance drills | 25 tuning questions | `performance-questions.md` | P1 |

### 10 Learning Paths

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Senior engineer path | Week-by-week topic order | `python-senior-engineer-path.md` | P1 |
| Lead path | Production + concurrency + troubleshooting emphasis | `python-lead-path.md` | P1 |
| Architect path | Internals + performance + packaging + interview | `python-architect-path.md` | P1 |
| Interview revision | 48-hour cram schedule + topic clusters | `python-interview-revision-path.md` | P0 |

---

## Existing Assets to Preserve (Phase B)

| Asset | Source file | Action |
| :--- | :--- | :--- |
| MRO diamond mermaid | `oop.md` | Keep on canonical page |
| I/O vs CPU mermaid | `concurrency.md` | Keep; add decision tree |
| Reference tables (all pages) | 21 topic pages | Preserve in Quick Revision or Core Concepts |
| Code snippets | All pages | Preserve; expand on internals pages |
| `interview-answer` shortcodes | All topic pages | **Migrate** to Layer 2 `## Question` blocks; remove shortcodes |

---

## 12-Section Template — Infographic Mapping

| Template section | Primary visual asset |
| :--- | :--- |
| Quick Revision | One-page table (revision sheet) |
| Core Concepts | Concept matrix |
| Internal Working | Mermaid sequence / flowchart |
| Runtime Behavior | Execution pipeline diagram |
| Design Tradeoffs | Pros/cons comparison table |
| Production Usage | Pattern recipe cards |
| Performance Considerations | Profiler/tuning heuristic |
| Troubleshooting | Decision tree mermaid |
| Common Mistakes | Anti-pattern bullet card |
| Interview Questions | Link to Top 150 only (Layer 1) |
| Architect Notes | ADR-style tradeoff table |
| Checklists | Pre-prod / incident checklists |

**Rule:** Do not add empty sections — pair each section with at least one visual when the section exists.

**Cheat-sheet pages (01-fundamentals, 02-core-python):** May retain slim `At a Glance` + tables format; add architect sections only where interview depth required.

---

## Top 150 Question Category Visual (Phase B)

Single table on `top-150-interview-questions.md`:

| Category | Min count | Deep dive module |
| :--- | :---: | :--- |
| Internals & Runtime | 40 | `03-python-internals/` |
| Concurrency & Async | 30 | `04-concurrency/`, `03-python-internals/gil.md` |
| Performance | 25 | `05-performance/` |
| Troubleshooting | 20 | `05-performance/profiling.md`, `06-production-python/`, internals |
| Production Engineering | 15 | `06-production-python/` |
| Core Python & Typing | 20 | `01-fundamentals/`, `02-core-python/` |

---

## Phase Rollout

| Phase | Deliverable |
| :--- | :--- |
| **B** | P0 infographics on all new pages; preserve 2 mermaids; Top 150 category table; migrate interview shortcodes |
| **C** | P1 comparison one-pagers; learning path schedules; remaining diagrams |
| **D** | Optional static PNG exports from Mermaid for social/share (out of scope unless requested) |

---

## Out of Scope

- Custom SVG illustration files
- Design Patterns / System Design / SOLID / Microservices handbook content
- Modifying handbooks outside `python-cheatsheet/`

---

**Phase A infographic plan complete. Awaiting approval before Phase B.**
