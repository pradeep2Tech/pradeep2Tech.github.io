---
title: "Design Patterns Handbook Infographic Plan"
date: 2026-07-03T14:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["design-patterns", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, and optional future static images — not separate image assets unless generated later.

**Meta file:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Revision cheat sheet | Markdown bullets under `### Revision Cheat Sheet` | Every pattern page (exists) |
| Comparison one-pager | Markdown table | `05-pattern-comparisons/*` |
| Pattern decision tree | Mermaid `flowchart TD` | `09-pattern-selection-guide/pattern-decision-tree.md` |
| SOLID smell map | Mermaid `flowchart TD` | `01-solid-principles/solid-principles-composition-guide.md` |
| Anti-pattern catalog | Symptom → fix table | `07-anti-patterns/_index.md` |
| Interview cram sheet | Single-page table | `11-learning-paths/design-patterns-interview-revision-path.md` |
| LLD requirements card | FR/NFR table | `08-lld-case-studies/*` |
| GoF family poster | Module index tables | `02`–`04` section `_index.md` |

---

## By Major Topic

### SOLID Principles

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| One reason to change | Before/after responsibility split | `single-responsibility-principle.md` | — Exists (impl-tabs) |
| Extension vs modification | Open/closed decision table | `open-closed-principle.md` | — Exists |
| Substitutability contract | LSP violation checklist | `liskov-substitution-principle.md` | — Exists |
| Interface granularity | Fat vs thin interface table | `interface-segregation-principle.md` | — Exists |
| Depend on abstractions | DIP vs DI distinction card | `dependency-inversion-principle.md` + DI page | P1 |
| Smell → SOLID letter | Flowchart poster | `solid-principles-composition-guide.md` | P0 |

### Creational Patterns

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Creational family at-a-glance | 5-column comparison | `02-creational-patterns/_index.md` | P1 |
| Factory vs Builder vs Abstract Factory | 3-way matrix | `05-pattern-comparisons/` (split pages) | P0 |
| Singleton thread-safety | Init strategy table | `singleton-pattern.md` | P1 |

### Structural Patterns

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Wrapper trio disambiguation | Intent/lifetime/structure matrix | `decorator-vs-proxy-vs-bridge.md` | — Exists |
| Adapter vs Facade | When-to-use card | `05-pattern-comparisons/` or selection guide | P1 |
| Composite tree operations | Uniform vs leaf table | `composite-pattern.md` | P2 |

### Behavioral Patterns

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Strategy vs State vs Template | 3-column decision matrix | `strategy-vs-state.md` (split) | P0 |
| Observer vs Mediator | Communication topology card | `04-behavioral-patterns/_index.md` | P1 |
| Command undo/redo | Command stack diagram | `command-pattern.md` | — Exists (sequence) |

### Architectural Principles

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Layered vs Hexagonal | Side-by-side topology | `layered-vs-hexagonal-architecture.md` | — Exists |
| DDD building blocks | Entity/VO/Aggregate/Service card | `domain-driven-design-building-blocks.md` | P1 |
| DI styles | Constructor/setter/interface injection table | `dependency-injection-inversion-of-control.md` | P1 |
| DTO boundary | API vs domain layer card | `dto-entity-mapper-separation.md` | — Exists |

### Anti-Patterns (New)

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| God Object symptoms | Smell checklist | `god-object.md` | P0 |
| Anemic vs rich domain | Comparison table | `anemic-domain-model.md` | P0 |
| Shotgun Surgery | Change blast radius diagram | `shotgun-surgery.md` | P1 |
| Golden Hammer | "If all you have is…" matrix | `golden-hammer.md` | P1 |
| Anti-pattern index | Symptom → page → fix pattern | `07-anti-patterns/_index.md` | P0 |

### LLD Case Studies

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Parking lot | Entity + strategy matrix | `parking-lot.md` | — Exists |
| Rate limiter | Algorithm comparison (token/leaky/sliding) | `rate-limiter.md` | P1 |
| Elevator | State + scheduling card | `elevator-control-system.md` | — Exists |
| Notification | Channel × template matrix | `notification-system.md` | P1 |
| Ride sharing | Matching + pricing forces | `ride-sharing-system.md` | P0 |
| Library management | Loan/reservation lifecycle | `library-management-system.md` | P1 |
| LLD interview framework | FR/NFR → class diagram checklist | `08-lld-case-studies/_index.md` | P0 |

### Pattern Selection (New)

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Master pattern decision tree | Mermaid flowchart poster | `pattern-decision-tree.md` | P0 |
| Pattern by design force | Force → pattern table | `when-to-use-which-pattern.md` | P0 |
| Composition vs inheritance | Decision card | `composition-vs-inheritance.md` | P0 |
| Interface vs abstract class | Language-aware table (Java/Go) | `interface-vs-abstract-class.md` | P0 |

### Interview Guide (New)

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 150 index | Category filter table | `top-150-design-pattern-questions.md` | P0 |
| Architect probes (subset) | Printable question list | `architect-pattern-questions.md` | P1 |
| Comparison drills | Paired pattern questions | `pattern-comparison-questions.md` | P1 |
| SOLID scenario bank | Principle → scenario map | `solid-principles-questions.md` | P1 |
| LLD whiteboard prompts | Case study question list | `lld-questions.md` | P1 |

### Learning Paths (New)

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Senior engineer (2-week) | Week/day module schedule | `design-patterns-senior-engineer-path.md` | P1 |
| Lead (architecture focus) | Module 06 + 08 emphasis | `design-patterns-lead-path.md` | P1 |
| Architect (tradeoffs) | Comparison + anti-pattern weight | `design-patterns-architect-path.md` | P1 |
| 30-minute revision | One-page cram sheet | `design-patterns-interview-revision-path.md` | P0 |
| Concept → page map | Registry visual (subset) | `11-learning-paths/_index.md` | P2 |

---

## Existing Assets (Preserve)

| Asset | Location | Action |
| :--- | :--- | :--- |
| When to Use / NOT table | All 42 pattern pages | Keep — maps to new template "When NOT To Use" |
| Trade-offs table | All 42 pattern pages | Keep — maps to "Tradeoffs" section |
| Revision Cheat Sheet | All 42 pattern pages | Keep — embed in learning paths |
| Junior Mistakes | All 42 pattern pages | Keep — maps to "Common Mistakes" (LLD) or anti-patterns |
| Senior Questions | All 42 pattern pages | Migrate duplicates to interview module; keep 3–5 per page |
| Pattern Comparison at a Glance | 3 comparison pages | Keep — expand on split pages |

---

## Production Checklist Infographics

Embed in case study / architect sections (Phase C):

| Checklist | Page |
| :--- | :--- |
| LLD whiteboard structure | `08-lld-case-studies/_index.md` |
| Pattern selection ADR | `09-pattern-selection-guide/when-to-use-which-pattern.md` |
| SOLID review checklist | `01-solid-principles/solid-principles-composition-guide.md` |
| Anti-pattern code review | `07-anti-patterns/_index.md` |
| Architect interview prep | `11-learning-paths/design-patterns-architect-path.md` |

---

## Priority Summary

| Priority | Deliverables |
| :---: | :--- |
| **P0** | Pattern decision tree, Top 150 index, anti-pattern catalog, 30-min revision path, creational/behavioral comparison matrices, ride-sharing forces card |
| **P1** | DIP vs DI card, DDD building blocks poster, DI styles table, LLD framework checklist, learning path schedules |
| **P2** | Composite operations card, concept registry visual, optional quadrant charts |

---

## Asset Generation Notes

- **Phase B:** Markdown tables + Mermaid decision trees on new modules (07, 09, 10, 11)
- **Phase C:** Enhance existing Revision Cheat Sheets into learning-path aggregates
- **Phase D:** Optional PNG/SVG exports from Mermaid for social/print — out of scope Phase A–B
- **Python tab:** When added, include language column in interface-vs-abstract-class infographic

---

**STOP — Implement infographics during Phase B/C content depth work.**
