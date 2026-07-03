---
title: "Design Patterns Handbook Mermaid Diagram Plan"
date: 2026-07-03T14:00:00+00:00
draft: true
description: "Diagram opportunities by topic — Phase B/C implementation backlog."
tags: ["design-patterns", "meta", "planning"]
---

# Mermaid Diagram Plan

**Principle:** Diagrams on **canonical pages only**. Non-canonical pages link to diagram section.

**Existing diagrams:** **84** `mermaid` blocks across **41** topic files (~2 per page: `classDiagram` + `sequenceDiagram`/`flowchart`). Comparison pages have **4** each.

**Current placement:** Under `### Structure (Class Diagram)` and `### Interaction Flow` per `lld-posts.mdc`.

**Phase B template mapping:**

| Old section | New template section |
| :--- | :--- |
| Structure (Class Diagram) | Structure Diagram |
| Interaction Flow | Internal Working |

---

## 01 SOLID Principles

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `single-responsibility-principle.md` | `classDiagram` | Split responsibilities | — | **Exists** |
| `single-responsibility-principle.md` | `sequenceDiagram` | placeOrder orchestration | — | **Exists** |
| `open-closed-principle.md` | `classDiagram` | Extension without modification | — | **Exists** |
| `liskov-substitution-principle.md` | `classDiagram` | Rectangle/Square substitutability | — | **Exists** |
| `interface-segregation-principle.md` | `classDiagram` | Fat vs segregated interfaces | — | **Exists** |
| `dependency-inversion-principle.md` | `classDiagram` | High-level → abstraction | — | **Exists** |
| `solid-principles-composition-guide.md` | `flowchart TD` | Smell → SOLID letter mapping | P1 | **Planned** |
| `solid-principles-composition-guide.md` | `classDiagram` | Before/after refactor | — | **Exists** |

---

## 02 Creational Patterns

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| All 5 pattern pages | `classDiagram` + `sequenceDiagram` | Creator/product relationship | — | **Exists** (10 blocks) |
| `builder-pattern.md` | `sequenceDiagram` | Step-by-step build flow | P2 | Enhance existing |
| `prototype-pattern.md` | `flowchart LR` | Clone vs new allocation | P2 | Planned |
| `singleton-pattern.md` | `flowchart TD` | Thread-safe init paths | P1 | Planned |

---

## 03 Structural Patterns

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| All 7 pattern pages | `classDiagram` + flow/sequence | Wrapper hierarchies | — | **Exists** (14 blocks) |
| `composite-pattern.md` | `classDiagram` | Tree parent/child | — | **Exists** |
| `flyweight-pattern.md` | `flowchart TB` | Intrinsic vs extrinsic state | P2 | Planned |

---

## 04 Behavioral Patterns

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| All 10 pattern pages | `classDiagram` + sequence | Strategy/observer/state flows | — | **Exists** (20 blocks) |
| `state-pattern.md` | `stateDiagram-v2` | Order lifecycle transitions | P1 | Planned (replace flowchart) |
| `chain-of-responsibility-pattern.md` | `flowchart LR` | Handler chain | P2 | Enhance |

---

## 05 Pattern Comparisons

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `decorator-vs-proxy-vs-bridge.md` | 2× `classDiagram` + 2× sequence | Side-by-side intent | — | **Exists** (4 blocks) |
| `factory-method-vs-abstract-factory-vs-builder.md` | 4 blocks | Creational disambiguation | — | **Exists** — split in Phase B |
| `strategy-vs-state-vs-template-method.md` | 4 blocks | Behavioral disambiguation | — | **Exists** — split in Phase B |
| `factory-vs-builder.md` | `classDiagram` | Construction vs factory | P0 | Planned (new) |
| `factory-vs-abstract-factory.md` | `classDiagram` | Single vs family factories | P0 | Planned (new) |
| `strategy-vs-state.md` | `classDiagram` | Algorithm swap vs lifecycle | P0 | Planned (new) |
| `composition-vs-inheritance.md` | `classDiagram` | Has-a vs is-a | P0 | Planned (new) |
| `interface-vs-abstract-class.md` | `flowchart TD` | Selection decision | P0 | Planned (new) |

---

## 06 Architectural Principles

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `dependency-injection-inversion-of-control.md` | `classDiagram` | Composition root | — | **Exists** |
| `layered-vs-hexagonal-architecture.md` | `classDiagram` | Layers vs ports/adapters | — | **Exists** |
| `domain-driven-design-building-blocks.md` | `classDiagram` | Entity/VO/Aggregate | — | **Exists** |
| `dto-entity-mapper-separation.md` | `sequenceDiagram` | API → domain mapping | — | **Exists** |
| `repository-and-unit-of-work.md` | `classDiagram` | Persistence boundary | — | **Exists** |
| `layered-vs-hexagonal-architecture.md` | `flowchart LR` | Request path through layers | P1 | Planned |
| `domain-driven-design-building-blocks.md` | `erDiagram` | Aggregate boundaries | P1 | Planned |

---

## 07 Anti-Patterns (New)

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `god-object.md` | `classDiagram` | Monolith class responsibilities | P0 | Planned |
| `anemic-domain-model.md` | `classDiagram` | Logic in services vs entities | P0 | Planned |
| `spaghetti-code.md` | `flowchart TD` | Tangled dependency graph | P1 | Planned |
| `shotgun-surgery.md` | `flowchart LR` | One change → many files | P1 | Planned |
| `golden-hammer.md` | `flowchart TD` | Pattern misapplication tree | P1 | Planned |

---

## 08 LLD Case Studies

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `parking-lot.md` | `classDiagram` + sequence | Park/exit flow | — | **Exists** |
| `elevator-control-system.md` | `classDiagram` + sequence | Dispatch + state | — | **Exists** |
| `rate-limiter.md` | `classDiagram` + sequence | Token bucket | — | **Exists** |
| `notification-system.md` | `classDiagram` + sequence | Multi-channel dispatch | — | **Exists** |
| `task-scheduler-lld.md` | `classDiagram` + sequence | Command queue | — | **Exists** |
| `ride-sharing-system.md` | `classDiagram` | Rider/driver/matching | P0 | Planned (new) |
| `ride-sharing-system.md` | `sequenceDiagram` | Request → match → trip | P0 | Planned |
| `library-management-system.md` | `classDiagram` | Book/member/loan | P1 | Planned (new) |

---

## 09 Pattern Selection Guide (New)

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `pattern-decision-tree.md` | `flowchart TD` | GoF pattern selection tree | P0 | Planned |
| `pattern-decision-tree.md` | `flowchart TD` | Creational sub-tree | P0 | Planned |
| `pattern-decision-tree.md` | `flowchart TD` | Structural wrapper sub-tree | P0 | Planned |
| `when-to-use-which-pattern.md` | `quadrantChart` or matrix | Pattern fit by force | P1 | Optional |

---

## 10 Interview Guide

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| All interview files | — | Link to topic diagrams only | P3 | N/A |

---

## 11 Learning Paths

| Page | Diagram type | Purpose | Priority | Status |
| :--- | :--- | :--- | :---: | :--- |
| `design-patterns-interview-revision-path.md` | `flowchart LR` | 30-min revision order | P1 | Planned |
| `design-patterns-architect-path.md` | `flowchart TB` | Module dependency graph | P2 | Planned |

---

## Diagram Quality Rules (Phase B)

| Rule | Detail |
| :--- | :--- |
| Syntax | Hugo fenced ` ```mermaid ` blocks |
| Labels | Quote edge labels; camelCase node IDs |
| Max per page | 2 in initial pass; comparison pages up to 4 |
| Placement | Structure Diagram + Internal Working sections |
| Avoid | Duplicate classDiagram on pattern + comparison pages |
| LLD case studies | `classDiagram` for domain model; `sequenceDiagram` for main flow |
| Anti-patterns | Before (smell) vs after (fix) side-by-side class diagrams |

---

## Priority Summary

| Priority | Count | Focus |
| :---: | :---: | :--- |
| **Exists** | 84 blocks | All GoF + arch + 5 LLD + 3 comparisons |
| **P0** | 12 | Pattern decision trees, new comparisons, ride-sharing, anti-pattern smells |
| **P1** | 10 | State diagram, SOLID smell map, DDD erDiagram, revision path |
| **P2** | 6 | Prototype/flyweight enhancements, architect path |

---

## Implementation Phases

| Phase | Diagrams |
| :--- | :--- |
| **B** | Pattern decision tree (P0); new comparison page diagrams; anti-pattern before/after |
| **C** | Ride-sharing + library LLD; stateDiagram-v2 on state-pattern; DDD erDiagram |
| **D** | Quadrant charts, architect path module graph |

---

**STOP — Implement diagrams during Phase B/C content work.**
