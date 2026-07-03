---
title: "Design Patterns Handbook Refactoring Plan"
date: 2026-07-03T14:00:00+00:00
draft: true
description: "Phase A inventory — quality, duplication, gaps, and recommended actions."
tags: ["design-patterns", "meta", "planning"]
---

# Phase A — Repository Inventory

**Scope:** `content/design-patterns/` (43 markdown files: 42 topics + `_index.md`)  
**Audience:** Senior Engineers, Leads, Architects (6+ years)  
**Status:** Planning only — **no content rewritten in Phase A**

**Vision:** Transform from "Pattern Catalog" → **Design Principles, Patterns & LLD Handbook**

---

## Executive Summary

| Metric | Assessment |
| :--- | :--- |
| **Structure** | Flat directory; 7 modules in `design_patterns_modules.yaml` — target is **11 numbered subfolders** |
| **GoF coverage** | **Complete** — all 23 GoF patterns exist and are published |
| **SOLID coverage** | **5/5 letters** + `solid-principles-composition-guide` capstone |
| **Template compliance** | 42/42 follow `lld-posts.mdc` (10 `###` sections, Mermaid, `impl-tabs`) — **not** the new Phase B templates |
| **Duplication** | **High** — `OrderManager` / `OrderFacade` / `OrderService` domain repeated across 10+ files |
| **Canonical discipline** | **None** — no concept registry enforced yet |
| **Anti-patterns** | **0/5** — entire module missing |
| **Pattern selection** | **0/2** — entire module missing |
| **Interview guide** | **0/5** — no Top 150, no architect/comparison/SOLID/LLD question banks |
| **Learning paths** | **0/4** — missing |
| **LLD case studies** | **5/6** — missing ride-sharing, library management; extra `task-scheduler-lld` |
| **Pattern comparisons** | **3/6** — consolidated 3-in-1 guides exist; target wants 6 pairwise/split pages |
| **Mermaid** | **84 blocks** across 42 files (~2 per page; comparison pages have 4) |
| **Languages** | Java + Go via `impl-tabs` everywhere; **no Python** (target template requires Python in Phase B) |
| **draft status** | All 43 files `draft: false` despite ~22 missing target pages |

**Recommended Phase B focus:** Create `_meta` enforcement, reorganize into 11 modules, add missing modules (07–11), migrate templates, deduplicate order-domain cluster, generate Top 150 questions — **not** rewrite existing strong reference posts from scratch.

---

## File Inventory

| File | Category | Quality | Duplication | Interview Value | Problems | Action |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| `_index.md` | Landing | 6 | 1 | 5 | No curriculum tables for modules 07–11; no learning-path links | **Rewrite** — handbook vision + module map |
| `single-responsibility-principle.md` | M1 SOLID → 01 | 9 | 7 | 9 | `OrderManager` god-class reused across SOLID/arch cluster; **reference post** per `lld-posts.mdc` | **Keep** — canonical SRP; trim cross-file example reuse in Phase B |
| `open-closed-principle.md` | M1 → 01 | 8 | 5 | 9 | Invoice/discount example distinct; same teaching arc as siblings | **Keep** — canonical OCP |
| `liskov-substitution-principle.md` | M1 → 01 | 8 | 4 | 9 | Rectangle/Square — standard, self-contained | **Keep** — canonical LSP |
| `interface-segregation-principle.md` | M1 → 01 | 8 | 4 | 8 | Printer/scanner split — self-contained | **Keep** — canonical ISP |
| `dependency-inversion-principle.md` | M1 → 01 | 8 | 7 | 9 | Overlaps DI/IoC + repository + layered arch on order domain | **Keep** — canonical DIP; link to DI page ≤2 sentences |
| `solid-principles-composition-guide.md` | M1 extra → 01 capstone | 9 | 8 | 10 | Repeats `OrderManager`/`OrderFacade`; unique `Smell-to-Fix Map` | **Keep** — move to `01-solid-principles/` as synthesis finale |
| `factory-method-pattern.md` | M2 creational → 02 | 8 | 6 | 8 | Overlaps consolidated comparison guide | **Keep** — canonical Factory Method |
| `abstract-factory-pattern.md` | M2 → 02 | 8 | 6 | 7 | UI widget families overlap comparison | **Keep** — canonical Abstract Factory |
| `builder-pattern.md` | M2 → 02 | 8 | 6 | 8 | Stepwise construction duplicated in comparison | **Keep** — canonical Builder |
| `prototype-pattern.md` | M2 → 02 | 8 | 3 | 6 | Longest creational post; lower interview frequency | **Keep** — canonical Prototype |
| `singleton-pattern.md` | M2 → 02 | 8 | 5 | 8 | Metrics registry overlaps DI theme; anti-pattern angle missing | **Keep** — link future `golden-hammer` / god-object |
| `adapter-pattern.md` | M3 structural → 03 | 8 | 4 | 8 | Payment-gateway adapter; some order-domain bleed | **Keep** — canonical Adapter |
| `decorator-pattern.md` | M3 → 03 | 8 | 7 | 8 | Intent duplicated in comparison guide | **Keep** — canonical Decorator |
| `facade-pattern.md` | M3 → 03 | 8 | 7 | 9 | `OrderFacade` overlaps SOLID composition + layered arch | **Keep** — canonical Facade |
| `proxy-pattern.md` | M3 → 03 | 8 | 7 | 9 | Lazy-load subject overlaps comparison | **Keep** — canonical Proxy |
| `composite-pattern.md` | M3 → 03 | 7 | 3 | 7 | File-system tree — standalone | **Keep** — canonical Composite |
| `bridge-pattern.md` | M3 → 03 | 8 | 7 | 7 | Payment/UI bridge overlaps comparison | **Keep** — canonical Bridge |
| `flyweight-pattern.md` | M3 → 03 | 8 | 2 | 6 | Glyph editor — unique; rare interview topic | **Keep** — canonical Flyweight |
| `strategy-pattern.md` | M4 behavioral → 04 | 9 | 6 | 10 | **Reference post**; pricing overlaps comparison + parking-lot | **Keep** — canonical Strategy |
| `observer-pattern.md` | M4 → 04 | 7 | 5 | 8 | Event dispatch overlaps `notification-service-lld` | **Keep** — canonical Observer |
| `command-pattern.md` | M4 → 04 | 8 | 4 | 8 | Undo/queue; task-scheduler echoes command | **Keep** — canonical Command |
| `state-pattern.md` | M4 → 04 | 8 | 7 | 9 | Order lifecycle overlaps comparison heavily | **Keep** — canonical State |
| `chain-of-responsibility-pattern.md` | M4 → 04 | 8 | 3 | 8 | Auth/filter chain — distinct | **Keep** — canonical Chain of Responsibility |
| `template-method-pattern.md` | M4 → 04 | 8 | 7 | 7 | Data-import skeleton overlaps comparison | **Keep** — canonical Template Method |
| `iterator-pattern.md` | M4 → 04 | 7 | 2 | 6 | Lower interview frequency | **Keep** — canonical Iterator |
| `mediator-pattern.md` | M4 → 04 | 7 | 2 | 7 | Chat room — distinct from observer | **Keep** — canonical Mediator |
| `memento-pattern.md` | M4 → 04 | 7 | 2 | 6 | Undo stack — niche | **Keep** — canonical Memento |
| `visitor-pattern.md` | M4 → 04 | 7 | 2 | 6 | Tax calculation — niche | **Keep** — canonical Visitor |
| `repository-and-unit-of-work.md` | M5 arch → 06 | 8 | 7 | 9 | `OrderManager`/`OrderService` repeats SOLID cluster; not in target 06 list | **Keep** — assign to 06 as 5th topic or fold into DDD page |
| `dependency-injection-inversion-of-control.md` | M5 → 06 | 8 | 6 | 9 | Overlaps DIP post; same lesson arc | **Keep** — canonical DI/IoC |
| `dto-entity-mapper-separation.md` | M5 → 06 | 8 | 5 | 8 | Order DTO mapping — fits arch cluster | **Keep** — canonical DTO/Entity separation |
| `layered-vs-hexagonal-architecture.md` | M5 → 06 | 8 | 7 | 9 | `OrderService` ports — overlaps DIP/repository | **Keep** — canonical layered vs hexagonal |
| `domain-driven-design-building-blocks.md` | M5 → 06 | 8 | 5 | 9 | Target lists 4 arch files — this is 5th | **Keep** — canonical DDD building blocks |
| `specification-pattern.md` | M5 extra → 06 or 09 | 7 | 4 | 7 | Not in target 06 list; overlaps Chain/validation | **Keep** — bonus; link from pattern-selection guide |
| `strategy-vs-state-vs-template-method.md` | M7 → 05 | 9 | 8 | 10 | **High overlap by design** with 3 pattern posts | **Split** → `strategy-vs-state.md` + fold Template into selection guide or keep as 3rd comparison |
| `decorator-vs-proxy-vs-bridge.md` | M7 → 05 | 9 | 8 | 10 | Consolidates 3 structural posts | **Keep** — canonical structural disambiguation |
| `factory-method-vs-abstract-factory-vs-builder.md` | M7 → 05 | 9 | 8 | 9 | Consolidates 3 creational posts | **Split** → `factory-vs-builder.md` + `factory-vs-abstract-factory.md` per target |
| `parking-lot-system-lld.md` | M6 → 08 | 9 | 3 | 10 | **Best case study** — Strategy + SRP woven in | **Keep** — rename to `parking-lot.md` |
| `elevator-control-system-lld.md` | M6 → 08 | 8 | 2 | 9 | State + scheduling — strong | **Keep** — rename to `elevator-control-system.md` |
| `in-memory-rate-limiter-lld.md` | M6 → 08 | 8 | 3 | 9 | Token bucket — distinct | **Keep** — rename to `rate-limiter.md` |
| `notification-service-lld.md` | M6 → 08 | 8 | 5 | 9 | Observer + Strategy; overlaps observer-pattern | **Keep** — rename to `notification-system.md` |
| `task-scheduler-lld.md` | M6 extra → 08 | 8 | 3 | 9 | Not in target list; Command + priority queue | **Keep** — bonus case study or demote to appendix |

**Scoring guide:** Quality = accuracy + production depth + maintainability. Duplication = 1 (unique) – 10 (heavily repeated). Interview Value = usefulness in senior/architect interviews.

---

## Duplicate Content (Semantic Overlap > 60%)

| Concept cluster | Appears in | Canonical target (Phase B) |
| :--- | :--- | :--- |
| `OrderManager` god class → split responsibilities | SRP, SOLID composition, facade, repository, DIP, layered arch, DTO mapper, singleton, DDD | `01-solid-principles/single-responsibility-principle.md` |
| `OrderFacade` orchestration | facade, SOLID composition, layered arch | `03-structural-patterns/facade-pattern.md` |
| `OrderService` + ports/adapters | DIP, DI/IoC, layered-vs-hexagonal, repository, DDD | `06-architectural-principles/dependency-injection-inversion-of-control.md` |
| Strategy vs State vs Template Method | 3 pattern posts + comparison + parking-lot, rate-limiter, elevator | `05-pattern-comparisons/strategy-vs-state.md` (new split) |
| Decorator vs Proxy vs Bridge | 3 structural posts + comparison | `05-pattern-comparisons/decorator-vs-proxy-vs-bridge.md` |
| Factory vs Abstract Factory vs Builder | 3 creational posts + comparison | Split comparisons in Phase B |
| DIP (principle) vs DI (mechanism) | `dependency-inversion-principle`, `dependency-injection-inversion-of-control` | DIP = `01-solid-principles/`; DI = `06-architectural-principles/` |
| Observer theory vs notification LLD | `observer-pattern`, `notification-service-lld` | Observer = `04-behavioral-patterns/`; LLD = `08-lld-case-studies/` |
| lld-posts 10-section skeleton | All 42 topic pages | Migrate to new templates in Phase B — preserve Mermaid + impl-tabs |

---

## Missing Topics (Not Canonical Anywhere)

| Topic | Interview priority | Proposed canonical page (Phase B) |
| :--- | :---: | :--- |
| God Object anti-pattern | High | `07-anti-patterns/god-object.md` |
| Anemic Domain Model | High | `07-anti-patterns/anemic-domain-model.md` |
| Spaghetti Code | Medium | `07-anti-patterns/spaghetti-code.md` |
| Shotgun Surgery | High | `07-anti-patterns/shotgun-surgery.md` |
| Golden Hammer | High | `07-anti-patterns/golden-hammer.md` |
| When to use which pattern | High | `09-pattern-selection-guide/when-to-use-which-pattern.md` |
| Pattern decision tree | High | `09-pattern-selection-guide/pattern-decision-tree.md` |
| Factory vs Builder (pairwise) | High | `05-pattern-comparisons/factory-vs-builder.md` |
| Factory vs Abstract Factory | High | `05-pattern-comparisons/factory-vs-abstract-factory.md` |
| Strategy vs State (pairwise) | High | `05-pattern-comparisons/strategy-vs-state.md` |
| Composition vs Inheritance | High | `05-pattern-comparisons/composition-vs-inheritance.md` |
| Interface vs Abstract Class | High | `05-pattern-comparisons/interface-vs-abstract-class.md` |
| Ride Sharing LLD | High | `08-lld-case-studies/ride-sharing-system.md` |
| Library Management LLD | Medium | `08-lld-case-studies/library-management-system.md` |
| Top 150 design pattern questions | High | `10-interview-guide/top-150-design-pattern-questions.md` |
| Architect pattern questions | High | `10-interview-guide/architect-pattern-questions.md` |
| Pattern comparison questions | High | `10-interview-guide/pattern-comparison-questions.md` |
| SOLID principles questions | High | `10-interview-guide/solid-principles-questions.md` |
| LLD questions | High | `10-interview-guide/lld-questions.md` |
| Senior engineer learning path | Medium | `11-learning-paths/design-patterns-senior-engineer-path.md` |
| Lead learning path | Medium | `11-learning-paths/design-patterns-lead-path.md` |
| Architect learning path | Medium | `11-learning-paths/design-patterns-architect-path.md` |
| Interview revision path | High | `11-learning-paths/design-patterns-interview-revision-path.md` |
| Python examples | Medium | Add to all pattern pages per new template (Phase C) |

---

## Weak Files (Quality < 7 or Structural Gap)

| File | Issue |
| :--- | :--- |
| `_index.md` | Thin landing; no module 07–11 navigation |
| `iterator-pattern.md`, `memento-pattern.md`, `mediator-pattern.md`, `visitor-pattern.md` | Complete but lower interview depth (7/10) |
| `specification-pattern.md` | Outside target IA; thinner than arch peers |
| Entire modules 07, 09, 10, 11 | **Missing** |

---

## Fragmented Concepts (Need Split or Consolidate)

| Concept | Current state | Phase B action |
| :--- | :--- | :--- |
| 3-in-1 comparison guides | `factory-method-vs-*`, `strategy-vs-state-vs-*` | Split to match target 6 comparison pages; keep consolidated as redirect aliases |
| Architecture module (6 files) | Target lists 4; repo has 6 + repository + specification | Keep all 6 target + repository + specification as extended 06 |
| Flat URLs `/design-patterns/<slug>/` | 42 published URLs | Add Hugo `aliases` on moved files after subfolder migration |
| Template (lld-posts vs new) | All pages use lld-posts 10-section | Phase B: migrate headings; keep impl-tabs + Mermaid |
| Order-domain examples | 10+ files | Vary domains in arch cluster (payments, inventory, auth) |

---

## Outdated Content / Structural Debt

| Item | Issue |
| :--- | :--- |
| `data/design_patterns_modules.yaml` | 7 modules; target is 11 |
| No `_meta/` folder | Created in Phase A |
| No concept registry enforcement | Duplication unchecked |
| All `draft: false` | Published flag despite 22+ missing pages |
| No Python in impl-tabs | Target template requires Java + Go + Python |
| `solid-principles-composition-guide` | Module 1.6 — not one of 5 SOLID letters |
| Comparison naming | `*-lld` suffix on case studies vs target clean names |

---

## Phase B Action Summary (Pending Approval)

| Priority | Action |
| :---: | :--- |
| P0 | Reorganize into `01-solid-principles/` … `11-learning-paths/` subfolders |
| P0 | Update `design_patterns_modules.yaml` + `design_patterns_order.yaml` |
| P0 | Create `07-anti-patterns/` (5 files) |
| P0 | Create `09-pattern-selection-guide/` (2 files) |
| P0 | Create `10-interview-guide/` — Top 150 + 4 question banks (questions only) |
| P0 | Create `11-learning-paths/` (4 files) |
| P1 | Split comparison guides; add `composition-vs-inheritance`, `interface-vs-abstract-class` |
| P1 | Create `ride-sharing-system.md`, `library-management-system.md` |
| P1 | Enforce concept registry — trim order-domain duplication to ≤2 sentences + link |
| P1 | Add Hugo aliases for flat → nested URL migration |
| P2 | Migrate pages to new templates (Pattern / SOLID / LLD / Comparison) |
| P2 | Add Python impl-tab (or third tab) per target template |
| P2 | Expand architect notes + tradeoff sections on reference posts |
| P3 | Optional: demote `task-scheduler-lld` or keep as bonus in module 08 |

---

## Phase A Deliverables Checklist

- [x] `_meta/refactoring-plan.md` (this file)
- [x] `_meta/concept-registry.md`
- [x] `_meta/navigation-plan.md`
- [x] `_meta/mermaid-plan.md`
- [x] `_meta/infographic-plan.md`

**STOP — Await approval before Phase B execution.**
