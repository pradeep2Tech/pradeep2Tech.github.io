---
title: "Design Patterns Handbook Navigation Plan"
date: 2026-07-03T14:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["design-patterns", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/design_patterns_modules.yaml` and `design_patterns_order.yaml`.

**Vision:** Sidebar reads as **Design Principles, Patterns & LLD Handbook** — 11 modules, not a flat pattern catalog.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo | Target folder |
| :--- | :---: | :---: | :---: | :--- |
| SOLID & Design Foundations | 1 | 6 | 6 | `01-solid-principles/` |
| Creational Patterns | 2 | 5 | 5 | `02-creational-patterns/` |
| Structural Patterns | 3 | 7 | 7 | `03-structural-patterns/` |
| Behavioral Patterns | 4 | 10 | 10 | `04-behavioral-patterns/` |
| LLD Architecture Patterns | 5 | 6 | 6 | `06-architectural-principles/` |
| Applied LLD Case Studies | 6 | 5 | 5 | `08-lld-case-studies/` |
| Pattern Comparison Guides | 7 | 3 | 3 | `05-pattern-comparisons/` |
| Anti-Patterns | — | 0 | 0 | `07-anti-patterns/` |
| Pattern Selection | — | 0 | 0 | `09-pattern-selection-guide/` |
| Interview Guide | — | 0 | 0 | `10-interview-guide/` |
| Learning Paths | — | 0 | 0 | `11-learning-paths/` |

**Layout today:** All 42 topics flat under `content/design-patterns/<slug>.md`  
**Sidebar resolution:** `site.GetPage "design-patterns/<slug>"` (flat slug)

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "SOLID Principles"
    moduleTitle: "SOLID Principles"
    topics:
      - 01-solid-principles/single-responsibility-principle
      - 01-solid-principles/open-closed-principle
      - 01-solid-principles/liskov-substitution-principle
      - 01-solid-principles/interface-segregation-principle
      - 01-solid-principles/dependency-inversion-principle
      - 01-solid-principles/solid-principles-composition-guide

  - id: 2
    focus: "Creational Patterns"
    topics:
      - 02-creational-patterns/factory-method-pattern
      - 02-creational-patterns/abstract-factory-pattern
      - 02-creational-patterns/builder-pattern
      - 02-creational-patterns/prototype-pattern
      - 02-creational-patterns/singleton-pattern

  - id: 3
    focus: "Structural Patterns"
    topics:
      - 03-structural-patterns/adapter-pattern
      - 03-structural-patterns/bridge-pattern
      - 03-structural-patterns/composite-pattern
      - 03-structural-patterns/decorator-pattern
      - 03-structural-patterns/facade-pattern
      - 03-structural-patterns/flyweight-pattern
      - 03-structural-patterns/proxy-pattern

  - id: 4
    focus: "Behavioral Patterns"
    topics:
      - 04-behavioral-patterns/chain-of-responsibility-pattern
      - 04-behavioral-patterns/command-pattern
      - 04-behavioral-patterns/iterator-pattern
      - 04-behavioral-patterns/mediator-pattern
      - 04-behavioral-patterns/memento-pattern
      - 04-behavioral-patterns/observer-pattern
      - 04-behavioral-patterns/state-pattern
      - 04-behavioral-patterns/strategy-pattern
      - 04-behavioral-patterns/template-method-pattern
      - 04-behavioral-patterns/visitor-pattern

  - id: 5
    focus: "Pattern Comparisons"
    topics:
      - 05-pattern-comparisons/factory-vs-builder
      - 05-pattern-comparisons/factory-vs-abstract-factory
      - 05-pattern-comparisons/decorator-vs-proxy-vs-bridge
      - 05-pattern-comparisons/strategy-vs-state
      - 05-pattern-comparisons/composition-vs-inheritance
      - 05-pattern-comparisons/interface-vs-abstract-class

  - id: 6
    focus: "Architectural Principles"
    topics:
      - 06-architectural-principles/dependency-injection-inversion-of-control
      - 06-architectural-principles/layered-vs-hexagonal-architecture
      - 06-architectural-principles/domain-driven-design-building-blocks
      - 06-architectural-principles/dto-entity-mapper-separation
      - 06-architectural-principles/repository-and-unit-of-work
      - 06-architectural-principles/specification-pattern

  - id: 7
    focus: "Anti-Patterns"
    topics:
      - 07-anti-patterns/god-object
      - 07-anti-patterns/anemic-domain-model
      - 07-anti-patterns/spaghetti-code
      - 07-anti-patterns/shotgun-surgery
      - 07-anti-patterns/golden-hammer

  - id: 8
    focus: "LLD Case Studies"
    topics:
      - 08-lld-case-studies/elevator-control-system
      - 08-lld-case-studies/rate-limiter
      - 08-lld-case-studies/parking-lot
      - 08-lld-case-studies/notification-system
      - 08-lld-case-studies/ride-sharing-system
      - 08-lld-case-studies/library-management-system
      - 08-lld-case-studies/task-scheduler-lld

  - id: 9
    focus: "Pattern Selection Guide"
    topics:
      - 09-pattern-selection-guide/when-to-use-which-pattern
      - 09-pattern-selection-guide/pattern-decision-tree

  - id: 10
    focus: "Interview Guide"
    topics:
      - 10-interview-guide/top-150-design-pattern-questions
      - 10-interview-guide/architect-pattern-questions
      - 10-interview-guide/pattern-comparison-questions
      - 10-interview-guide/solid-principles-questions
      - 10-interview-guide/lld-questions

  - id: 11
    focus: "Learning Paths"
    topics:
      - 11-learning-paths/design-patterns-senior-engineer-path
      - 11-learning-paths/design-patterns-lead-path
      - 11-learning-paths/design-patterns-architect-path
      - 11-learning-paths/design-patterns-interview-revision-path
```

**Module renumbering note:** Current yaml uses M5=Architecture, M6=Case Studies, M7=Comparisons. Phase B aligns module **id** with folder prefix (`05` = comparisons, `06` = architecture, etc.).

---

## Section Index Pages (Phase B)

Create `_index.md` in each numbered subfolder:

| Folder | Index content |
| :--- | :--- |
| `01-solid-principles/_index.md` | SOLID reading order; link to composition guide as finale |
| `02-creational-patterns/_index.md` | Creational family map; link to comparisons |
| `03-structural-patterns/_index.md` | Wrapper family; link to decorator-vs-proxy-vs-bridge |
| `04-behavioral-patterns/_index.md` | Variation vs notification vs sequencing |
| `05-pattern-comparisons/_index.md` | Read comparisons **instead of** re-reading all patterns |
| `06-architectural-principles/_index.md` | DIP → DI → DDD progression |
| `07-anti-patterns/_index.md` | Smell catalog with links to corrective patterns |
| `08-lld-case-studies/_index.md` | Case study difficulty order |
| `09-pattern-selection-guide/_index.md` | Entry point for "which pattern?" |
| `10-interview-guide/_index.md` | Layer 1 questions only; link to canonical pages |
| `11-learning-paths/_index.md` | Role-based path selector |

---

## Landing Page (`design-patterns/_index.md`)

| Section | Phase B update |
| :--- | :--- |
| Title / description | "Design Principles, Patterns & LLD Handbook" |
| Module table | 11 modules with links to section `_index.md` |
| Quick start | Senior engineer path + pattern decision tree |
| Meta links | `_meta/concept-registry.md` (draft, maintainer) |
| Reading order | SOLID → GoF by category → Comparisons → Architecture → LLD |

---

## Hugo Aliases (Preserve Flat URLs)

Every moved file gets `aliases` in front matter:

| Old URL | New path |
| :--- | :--- |
| `/design-patterns/single-responsibility-principle/` | `01-solid-principles/single-responsibility-principle.md` |
| `/design-patterns/strategy-pattern/` | `04-behavioral-patterns/strategy-pattern.md` |
| `/design-patterns/parking-lot-system-lld/` | `08-lld-case-studies/parking-lot.md` |
| `/design-patterns/factory-method-vs-abstract-factory-vs-builder/` | Redirect to `05-pattern-comparisons/factory-vs-builder` + siblings |
| `/design-patterns/strategy-vs-state-vs-template-method/` | Redirect to `05-pattern-comparisons/strategy-vs-state` |

**Apply aliases to all 42 existing slugs** before removing flat files.

---

## Top 150 Deep Dive Column (Phase B)

| Current | Target |
| :--- | :--- |
| No interview file exists | Create `top-150-design-pattern-questions.md` |
| N/A | `Deep Dive` column → Hugo link to canonical page |
| Per-page Senior Questions | Keep on pattern pages; interview file duplicates as **questions only** |

**Distribution (minimum):**

| Category | Count |
| :--- | :---: |
| Pattern tradeoffs | 40 |
| Pattern comparisons | 30 |
| SOLID principles | 25 |
| LLD design | 25 |
| Architectural principles | 15 |
| Anti-patterns | 15 |
| **Total** | **150** |

---

## Cross-Link Strategy

Every published topic page ends with **See Also** (max 6 links):

| Link type | Example |
| :--- | :--- |
| Canonical pattern | Comparison → `strategy-pattern` |
| Corrective pattern | Anti-pattern god-object → SRP |
| Comparison | Factory Method → `factory-vs-builder` |
| Architecture | Strategy → DI page |
| LLD application | Observer → notification-system case study |
| Interview | → Top 150 filtered rows |
| Selection | → `when-to-use-which-pattern` |

**Remove in Phase B:** Repeated `OrderManager` walkthroughs outside SRP canonical page.

---

## Breadcrumb Recommendations

```
Design Patterns > SOLID Principles > Single Responsibility Principle
Design Patterns > Pattern Comparisons > Strategy vs State
Design Patterns > LLD Case Studies > Parking Lot
Design Patterns > Interview Guide > Top 150
```

Ensure `moduleTitle` + `sectionRef` front matter updates (e.g. `5.4` for `strategy-vs-state`).

---

## Files Outside Sidebar Navigation

| File | Nav treatment |
| :--- | :--- |
| `_meta/*.md` | `draft: true` — exclude from sidebar |
| Legacy 3-in-1 comparison files | Hugo aliases only; remove from yaml after split |

---

## Sidebar QA Checklist (Phase B)

- [ ] Every `design_patterns_order.yaml` entry resolves via `hugo server`
- [ ] No orphan pages (all content pages in order yaml)
- [ ] Modules 07, 09, 10, 11 appear in sidebar
- [ ] Prev/next navigation works on nested slugs
- [ ] All 42 legacy flat URLs redirect via aliases
- [ ] Section `_index.md` pages render module TOC
- [ ] Interview guide pages show questions only (no answers)

---

## `curriculum_sections.yaml` Impact

**No change required** — section slug remains `design-patterns`. Only internal IA and yaml reorder.

---

**STOP — Implement navigation changes in Phase B after approval.**
