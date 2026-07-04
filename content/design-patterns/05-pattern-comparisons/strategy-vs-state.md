---
title: "Strategy vs State"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "Algorithm selection versus lifecycle-driven behavior."
tags: ["design-patterns", "lld"]
categories: ["Design Patterns"]
shortTitle: "Strategy vs State"
module: 5
moduleTitle: "Pattern Comparisons"
sectionRef: "5.4"
weight: 504
aliases:
  - "/design-patterns/strategy-vs-state-vs-template-method/"
---

### Problem & Intent

**Strategy** swaps interchangeable **algorithms** chosen externally. **State** changes **behavior as internal lifecycle phase** changes. Both use delegation — the difference is **who drives change** and whether **transitions** are domain rules.

---

### Pattern Comparison at a Glance

| Dimension | Strategy | State |
| :--- | :--- | :--- |
| **Who selects** | Client / context setter | Context on transition |
| **Transitions** | None between strategies | Core feature |
| **Typical domain** | Payment method, pricing tier | Order status, TCP phase |
| **Smell fixed** | `switch` on mode | `if (status == …)` |

---

### When to Use / When NOT to Use

| Situation | Strategy | State |
| :--- | :---: | :---: |
| Checkout picks payment method | Yes | — |
| Order: Pending → Paid → Shipped | — | Yes |
| User role (not lifecycle) | Yes | — |
| Fixed workflow, one varying step | — | — → [Template Method](/design-patterns/04-behavioral-patterns/template-method-pattern/) |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class CheckoutService {
        -PricingStrategy strategy
        +setStrategy(s)
    }
    class OrderContext {
        -OrderState state
        +pay()
        +ship()
    }
    CheckoutService --> PricingStrategy
    OrderContext --> OrderState
```

---

### Interaction Flow

```mermaid
sequenceDiagram
    participant C as OrderContext
    participant S as PaidState
    C->>S: pay()
    S->>C: transitionTo(Shipped)
```

---

### Implementation

See [Strategy](/design-patterns/04-behavioral-patterns/strategy-pattern/) and [State](/design-patterns/04-behavioral-patterns/state-pattern/).

---

### Trade-offs & Operational Realities

| Tradeoff | Strategy | State |
| :--- | :--- | :--- |
| **Concurrency** | Usually stateless algos | Transitions must be atomic |
| **Go fit** | Small interfaces | State structs + context |

---

### Junior Mistakes

- State for configuration that never transitions.
- Strategy when invalid operations depend on lifecycle phase.

---

### Senior Questions

1. Can a State object contain a Strategy?
2. How do you test all transitions?

---

### Revision Cheat Sheet

- **Strategy** → external algorithm swap.
- **State** → internal phase machine.

---

### See Also

- [Behavioral 3-way guide](/design-patterns/05-pattern-comparisons/strategy-vs-state-vs-template-method/)
- [Parking Lot LLD](/design-patterns/08-lld-case-studies/parking-lot/)
