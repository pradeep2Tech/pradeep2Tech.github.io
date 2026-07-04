---
title: "Senior Engineer Path"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "GoF patterns, SOLID, comparisons, and core LLD case studies."
tags: ["design-patterns", "lld", "interview"]
categories: ["Design Patterns"]
shortTitle: "Senior Path"
module: 11
moduleTitle: "Learning Paths"
sectionRef: "11.1"
weight: 1101
interviewHandbook: true
---

# Senior Engineer Path

**Audience:** Senior engineers (5–8 years) sharpening LLD and GoF pattern fluency.

**Duration:** 2 weeks (~4 hours/week).

**Prerequisite:** Comfortable with OOP in Java or Go; skim [SRP](/design-patterns/01-solid-principles/single-responsibility-principle/) first.

**Outcome:** Select patterns by force, implement with Java/Go tabs, pass LLD screens.

---

## Week 1 — Foundations and creational/structural

| Day | Read | Practice |
| :---: | :--- | :--- |
| 1 | [SOLID module](/design-patterns/01-solid-principles/) — all 5 principles | Draw class diagram for checkout without god class |
| 2 | [SOLID Composition Guide](/design-patterns/01-solid-principles/solid-principles-composition-guide/) | Refactor one smell from [God Object](/design-patterns/07-anti-patterns/god-object/) |
| 3 | [Creational patterns](/design-patterns/02-creational-patterns/) — Factory, Builder, Singleton | When **not** to use singleton |
| 4 | [Structural patterns](/design-patterns/03-structural-patterns/) — Adapter, Decorator, Facade | Compare [Decorator vs Proxy](/design-patterns/05-pattern-comparisons/decorator-vs-proxy-vs-bridge/) |
| 5 | [Pattern comparisons](/design-patterns/05-pattern-comparisons/) — first 3 pages | Answer 5 rows from [Top 150](/design-patterns/10-interview-guide/top-150-design-pattern-questions/) |

---

## Week 2 — Behavioral, selection, case studies

| Day | Read | Practice |
| :---: | :--- | :--- |
| 6 | [Behavioral](/design-patterns/04-behavioral-patterns/) — Strategy, Observer, State, Command | Whiteboard vending machine state |
| 7 | [Pattern selection guide](/design-patterns/09-pattern-selection-guide/) | [Decision tree](/design-patterns/09-pattern-selection-guide/pattern-decision-tree/) for notification system |
| 8 | [Parking Lot LLD](/design-patterns/08-lld-case-studies/parking-lot/) | Implement core entities in Java or Go |
| 9 | [Rate Limiter LLD](/design-patterns/08-lld-case-studies/rate-limiter/) | Token bucket vs sliding window |
| 10 | **Mock** | 45 min LLD: library management — cite 3 patterns with tradeoffs |

---

## See also

- [Interview Revision Path](/design-patterns/11-learning-paths/design-patterns-interview-revision-path/)
- [Architect Path](/design-patterns/11-learning-paths/design-patterns-architect-path/)
