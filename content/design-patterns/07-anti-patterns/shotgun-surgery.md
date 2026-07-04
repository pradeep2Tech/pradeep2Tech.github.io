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

{{< impl-tabs default="java" java="Java" golang="Go" python="Python" >}}
{{< impl-tab lang="java" >}}

**Violation — tax rule in 12 files:**

```java
// Controller, service, PDF, email template each duplicate:
if ("US".equals(order.getCountry())) { rate = 0.08; }
```

**Fixed — single policy:**

```java
public interface TaxPolicy { Money rateFor(Order order); }

public class OrderPricing {
    private final TaxPolicy tax;
    public Money total(Order o) { return o.subtotal().plus(tax.rateFor(o)); }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
type TaxPolicy interface { Rate(o Order) decimal.Decimal }

func Total(o Order, tax TaxPolicy) decimal.Decimal {
    return o.Subtotal.Add(tax.Rate(o))
}
```

{{< /impl-tab >}}
{{< impl-tab lang="python" >}}

**Violation:**

```python
class OrderManager:
    def place(self, req: dict) -> None:
        # many unrelated responsibilities in one type
        ...
```

**Fixed:**

```python
class OrderService:
    def __init__(self, validator, repo, notifier) -> None:
        self._validator = validator
        self._repo = repo
        self._notifier = notifier

    def place(self, req: dict) -> str:
        self._validator.check(req)
        return self._repo.save(req)
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

Consolidate variation behind [Strategy](/design-patterns/04-behavioral-patterns/strategy-pattern/) or [Template Method](/design-patterns/04-behavioral-patterns/template-method-pattern/).

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
