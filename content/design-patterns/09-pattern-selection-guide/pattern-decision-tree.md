---
title: "Pattern Decision Tree"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "Mermaid decision trees for creational, behavioral, and structural pattern selection."
tags: ["design-patterns", "lld"]
categories: ["Design Patterns"]
shortTitle: "Decision Tree"
module: 9
moduleTitle: "Pattern Selection Guide"
sectionRef: "9.2"
weight: 902
ShowToc: true
---

# Pattern Decision Tree

Use this tree in design reviews and interviews. Full explanations live on linked canonical pages only.

```mermaid
flowchart TD
    Start([Design problem]) --> Create{Object creation?}
    Create -->|Yes| Family{Related product family?}
    Family -->|Yes| AF[Abstract Factory]
    Family -->|No| Complex{Many optional steps?}
    Complex -->|Yes| B[Builder]
    Complex -->|No| FM[Factory Method]
    Create -->|No| Behavior{Behavior varies?}
    Behavior -->|Yes| Lifecycle{Lifecycle phases?}
    Lifecycle -->|Yes| ST[State]
    Lifecycle -->|No| STR[Strategy]
    Behavior -->|No| Structure{Structure / wrapping?}
    Structure -->|Yes| Wrap{Intent?}
    Wrap -->|Add features| DEC[Decorator]
    Wrap -->|Control access| PRX[Proxy]
    Wrap -->|Split abstraction| BR[Bridge]
    Wrap -->|Legacy API| AD[Adapter]
```

## Creational Sub-tree

| Question | Pattern |
| :--- | :--- |
| One product, which impl? | [Factory Method](/design-patterns/02-creational-patterns/factory-method-pattern/) |
| Consistent family? | [Abstract Factory](/design-patterns/02-creational-patterns/abstract-factory-pattern/) |
| Stepwise build + validation? | [Builder](/design-patterns/02-creational-patterns/builder-pattern/) |

## Comparison Shortcuts

- Factory vs Builder → [comparison](/design-patterns/05-pattern-comparisons/factory-vs-builder/)
- Strategy vs State → [comparison](/design-patterns/05-pattern-comparisons/strategy-vs-state/)
- Decorator vs Proxy vs Bridge → [comparison](/design-patterns/05-pattern-comparisons/decorator-vs-proxy-vs-bridge/)

## See Also

- [When to use which pattern](/design-patterns/09-pattern-selection-guide/when-to-use-which-pattern/)
- [Anti-patterns](/design-patterns/07-anti-patterns/)
