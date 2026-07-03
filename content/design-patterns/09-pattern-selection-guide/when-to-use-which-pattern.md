---
title: "When To Use Which Pattern"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "Design-force matrix for GoF and architectural pattern selection."
tags: ["design-patterns", "lld"]
categories: ["Design Patterns"]
shortTitle: "When To Use"
module: 9
moduleTitle: "Pattern Selection Guide"
sectionRef: "9.1"
weight: 901
ShowToc: true
---

# When To Use Which Pattern

Architect-level pattern selection by **design force** — not by name recognition.

## By Design Force

| Force | Consider | Canonical page |
| :--- | :--- | :--- |
| Hide which single product is created | Factory Method | [Factory Method](/design-patterns/02-creational-patterns/factory-method-pattern/) |
| Consistent product family | Abstract Factory | [Abstract Factory](/design-patterns/02-creational-patterns/abstract-factory-pattern/) |
| Complex object, many optional steps | Builder | [Builder](/design-patterns/02-creational-patterns/builder-pattern/) |
| Expensive clone vs rebuild | Prototype | [Prototype](/design-patterns/02-creational-patterns/prototype-pattern/) |
| Exactly one coordinated instance | Singleton (careful) | [Singleton](/design-patterns/02-creational-patterns/singleton-pattern/) |
| Legacy API mismatch | Adapter | [Adapter](/design-patterns/03-structural-patterns/adapter-pattern/) |
| Add behavior without subclassing | Decorator | [Decorator](/design-patterns/03-structural-patterns/decorator-pattern/) |
| Simplified subsystem API | Facade | [Facade](/design-patterns/03-structural-patterns/facade-pattern/) |
| Control access / lazy load | Proxy | [Proxy](/design-patterns/03-structural-patterns/proxy-pattern/) |
| Tree structures | Composite | [Composite](/design-patterns/03-structural-patterns/composite-pattern/) |
| Algorithm varies at runtime | Strategy | [Strategy](/design-patterns/04-behavioral-patterns/strategy-pattern/) |
| Behavior varies with lifecycle | State | [State](/design-patterns/04-behavioral-patterns/state-pattern/) |
| Notify many dependents | Observer | [Observer](/design-patterns/04-behavioral-patterns/observer-pattern/) |
| Encapsulate request + undo | Command | [Command](/design-patterns/04-behavioral-patterns/command-pattern/) |

## When NOT To Use Patterns

- One implementation, no variation → plain constructor.
- Pattern name without force → see [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/).

## See Also

- [Pattern decision tree](/design-patterns/09-pattern-selection-guide/pattern-decision-tree/)
- [Pattern comparisons](/design-patterns/05-pattern-comparisons/)
