---
title: "Shotgun Surgery"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "Anti-pattern — shotgun surgery symptoms, causes, and corrective design."
tags: ["design-patterns", "lld"]
categories: ["Design Patterns"]
shortTitle: "Shotgun"
module: 7
moduleTitle: "Anti-Patterns"
sectionRef: "7.4"
weight: 704
ShowToc: true
---

### Problem & Intent

**Shotgun surgery** — one logical change requires edits across many classes. It often violates [OCP](/design-patterns/01-solid-principles/open-closed-principle/) and indicates missing abstraction or duplicated policy.

---

### When to Use / When NOT to Use

| Situation | Shotgun? | Why |
| :--- | :---: | :--- |
| New report format touches 12 packages | Yes | Extract strategy or template |
| Rename field in one bounded context | No | Normal refactor |

---

### Structure (Class Diagram)

```mermaid
flowchart TD
    Change[Add tax rule] --> F1[File 1]
    Change --> F2[File 2]
    Change --> F3[File 3]
```

---

### Interaction Flow

```mermaid
flowchart LR
    R[Requirement] --> S1[Service A]
    R --> S2[Service B]
    R --> S3[Controller C]
```

---

### Implementation

Consolidate variation behind [Strategy](/design-patterns/04-behavioral-patterns/strategy-pattern/), [Template Method](/design-patterns/04-behavioral-patterns/template-method-pattern/), or configuration.

---

### Trade-offs & Operational Realities

| Approach | Benefit |
| :--- | :--- |
| **Extract policy object** | Single edit point |
| **Feature flags** | Decouple deploy from code paths |

---

### Junior Mistakes

- Copy-paste `if (country == "US")` across layers.
- Fear of abstraction → repeated surgery.

---

### Senior Questions

1. How do you measure blast radius before/after refactor?
2. When does DRY cause wrong abstraction?

---

### Revision Cheat Sheet

- **One change → many files** = smell.
- **Fix:** encapsulate what varies (OCP).

---

### See Also

- [OCP](/design-patterns/01-solid-principles/open-closed-principle/)
- [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/)
