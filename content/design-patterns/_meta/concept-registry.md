---
title: "Design Patterns Concept Registry"
date: 2026-07-03T14:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per design concept."
tags: ["design-patterns", "meta", "planning"]
---

# Design Patterns Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase A — registry defined; enforcement in Phase B/C.

**URL convention (Phase B):** `/design-patterns/<module>/<slug>/` — registry uses target filenames.

---

## SOLID Principles

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Single Responsibility Principle (SRP) | `01-solid-principles/single-responsibility-principle.md` | Exists (flat) | Reference post |
| Open/Closed Principle (OCP) | `01-solid-principles/open-closed-principle.md` | Exists | |
| Liskov Substitution Principle (LSP) | `01-solid-principles/liskov-substitution-principle.md` | Exists | |
| Interface Segregation Principle (ISP) | `01-solid-principles/interface-segregation-principle.md` | Exists | |
| Dependency Inversion Principle (DIP) | `01-solid-principles/dependency-inversion-principle.md` | Exists | Mechanism → DI page |
| SOLID synthesis / smell-to-fix map | `01-solid-principles/solid-principles-composition-guide.md` | Exists | Capstone; not a 6th letter |

---

## Creational Patterns (GoF)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Factory Method | `02-creational-patterns/factory-method-pattern.md` | Exists | |
| Abstract Factory | `02-creational-patterns/abstract-factory-pattern.md` | Exists | |
| Builder | `02-creational-patterns/builder-pattern.md` | Exists | |
| Prototype | `02-creational-patterns/prototype-pattern.md` | Exists | |
| Singleton | `02-creational-patterns/singleton-pattern.md` | Exists | Abuse → golden-hammer |

---

## Structural Patterns (GoF)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Adapter | `03-structural-patterns/adapter-pattern.md` | Exists | |
| Bridge | `03-structural-patterns/bridge-pattern.md` | Exists | |
| Composite | `03-structural-patterns/composite-pattern.md` | Exists | |
| Decorator | `03-structural-patterns/decorator-pattern.md` | Exists | |
| Facade | `03-structural-patterns/facade-pattern.md` | Exists | |
| Flyweight | `03-structural-patterns/flyweight-pattern.md` | Exists | |
| Proxy | `03-structural-patterns/proxy-pattern.md` | Exists | |

---

## Behavioral Patterns (GoF)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Chain of Responsibility | `04-behavioral-patterns/chain-of-responsibility-pattern.md` | Exists | |
| Command | `04-behavioral-patterns/command-pattern.md` | Exists | |
| Iterator | `04-behavioral-patterns/iterator-pattern.md` | Exists | |
| Mediator | `04-behavioral-patterns/mediator-pattern.md` | Exists | |
| Memento | `04-behavioral-patterns/memento-pattern.md` | Exists | |
| Observer | `04-behavioral-patterns/observer-pattern.md` | Exists | |
| State | `04-behavioral-patterns/state-pattern.md` | Exists | |
| Strategy | `04-behavioral-patterns/strategy-pattern.md` | Exists | Reference post |
| Template Method | `04-behavioral-patterns/template-method-pattern.md` | Exists | |
| Visitor | `04-behavioral-patterns/visitor-pattern.md` | Exists | |

---

## Pattern Comparisons

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Factory vs Builder | `05-pattern-comparisons/factory-vs-builder.md` | **Planned** | Split from 3-in-1 guide |
| Factory vs Abstract Factory | `05-pattern-comparisons/factory-vs-abstract-factory.md` | **Planned** | Split from 3-in-1 guide |
| Decorator vs Proxy vs Bridge | `05-pattern-comparisons/decorator-vs-proxy-vs-bridge.md` | Exists | |
| Strategy vs State | `05-pattern-comparisons/strategy-vs-state.md` | **Planned** | Split from 3-in-1 guide |
| Composition vs Inheritance | `05-pattern-comparisons/composition-vs-inheritance.md` | **Planned** | |
| Interface vs Abstract Class | `05-pattern-comparisons/interface-vs-abstract-class.md` | **Planned** | |
| Creational trio (legacy 3-in-1) | `factory-method-vs-abstract-factory-vs-builder.md` | Exists | **Deprecate** — alias to split pages |
| Behavioral trio (legacy 3-in-1) | `strategy-vs-state-vs-template-method.md` | Exists | **Deprecate** — alias to split pages |

---

## Architectural Principles

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Dependency Injection / IoC | `06-architectural-principles/dependency-injection-inversion-of-control.md` | Exists | DIP principle → SOLID page |
| Layered vs Hexagonal Architecture | `06-architectural-principles/layered-vs-hexagonal-architecture.md` | Exists | |
| DDD Building Blocks | `06-architectural-principles/domain-driven-design-building-blocks.md` | Exists | Entity, VO, Aggregate, Repository |
| DTO / Entity / Mapper Separation | `06-architectural-principles/dto-entity-mapper-separation.md` | Exists | |
| Repository + Unit of Work | `06-architectural-principles/repository-and-unit-of-work.md` | Exists | Extended topic (not in original 4) |
| Specification Pattern | `06-architectural-principles/specification-pattern.md` | Exists | Extended topic |

---

## Anti-Patterns

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| God Object | `07-anti-patterns/god-object.md` | **Planned** | Links to SRP |
| Anemic Domain Model | `07-anti-patterns/anemic-domain-model.md` | **Planned** | Links to DDD |
| Spaghetti Code | `07-anti-patterns/spaghetti-code.md` | **Planned** | |
| Shotgun Surgery | `07-anti-patterns/shotgun-surgery.md` | **Planned** | Links to OCP |
| Golden Hammer | `07-anti-patterns/golden-hammer.md` | **Planned** | Links to pattern-selection |

---

## LLD Case Studies

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Elevator Control System | `08-lld-case-studies/elevator-control-system.md` | Exists as `*-lld` | State pattern application |
| Rate Limiter | `08-lld-case-studies/rate-limiter.md` | Exists as `in-memory-rate-limiter-lld` | |
| Parking Lot | `08-lld-case-studies/parking-lot.md` | Exists as `parking-lot-system-lld` | Reference case study |
| Notification System | `08-lld-case-studies/notification-system.md` | Exists as `notification-service-lld` | Observer + Strategy |
| Ride Sharing System | `08-lld-case-studies/ride-sharing-system.md` | **Planned** | |
| Library Management System | `08-lld-case-studies/library-management-system.md` | **Planned** | |
| Task Scheduler (bonus) | `08-lld-case-studies/task-scheduler-lld.md` | Exists | Not in target 6 |

---

## Pattern Selection

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| When to use which pattern | `09-pattern-selection-guide/when-to-use-which-pattern.md` | **Planned** | |
| Pattern decision tree | `09-pattern-selection-guide/pattern-decision-tree.md` | **Planned** | |

---

## Cross-Cutting Design Concepts

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Composition over inheritance | `05-pattern-comparisons/composition-vs-inheritance.md` | **Planned** | |
| Program to an interface | `01-solid-principles/dependency-inversion-principle.md` | Exists | |
| Favor delegation over inheritance | `05-pattern-comparisons/composition-vs-inheritance.md` | **Planned** | |
| Separation of concerns | `01-solid-principles/single-responsibility-principle.md` | Exists | |
| Encapsulate what varies | `01-solid-principles/open-closed-principle.md` | Exists | |
| Polymorphism / substitutability | `01-solid-principles/liskov-substitution-principle.md` | Exists | |
| Interface granularity | `01-solid-principles/interface-segregation-principle.md` | Exists | |
| Inversion of control container | `06-architectural-principles/dependency-injection-inversion-of-control.md` | Exists | |
| Ports and adapters | `06-architectural-principles/layered-vs-hexagonal-architecture.md` | Exists | |
| Aggregate root / bounded context | `06-architectural-principles/domain-driven-design-building-blocks.md` | Exists | |

---

## Interview Layer

| Concept | Canonical Page | Status |
| :--- | :--- | :--- |
| Question index (150) | `10-interview-guide/top-150-design-pattern-questions.md` | **Planned** |
| Architect pattern probes | `10-interview-guide/architect-pattern-questions.md` | **Planned** |
| Pattern comparison probes | `10-interview-guide/pattern-comparison-questions.md` | **Planned** |
| SOLID probes | `10-interview-guide/solid-principles-questions.md` | **Planned** |
| LLD design probes | `10-interview-guide/lld-questions.md` | **Planned** |
| Per-page Senior Questions | Individual pattern pages `### Senior Questions` | Exists — migrate to interview module links |

---

## Learning Paths

| Concept | Canonical Page | Status |
| :--- | :--- | :--- |
| Senior engineer path | `11-learning-paths/design-patterns-senior-engineer-path.md` | **Planned** |
| Lead path | `11-learning-paths/design-patterns-lead-path.md` | **Planned** |
| Architect path | `11-learning-paths/design-patterns-architect-path.md` | **Planned** |
| Interview revision path | `11-learning-paths/design-patterns-interview-revision-path.md` | **Planned** |

---

## Enforcement Checklist (Phase B)

1. Grep handbook for each concept keyword; verify ≤ 2 sentences outside canonical page.
2. Add **See Also** link to canonical page from non-canonical mentions.
3. Top 150 `Deep Dive` column must resolve to canonical page Hugo URL.
4. Comparison pages must not repeat full pattern explanations — link to `02`–`04` modules.
5. LLD case studies reference patterns in ≤ 2 sentences + link.
6. New pages require registry row before merge.
