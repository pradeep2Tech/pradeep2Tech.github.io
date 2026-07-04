"""Generate LLD stub markdown files from data/design_patterns_modules.yaml."""
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TITLES = {
    "single-responsibility-principle": (
        "Single Responsibility Principle",
        "SRP",
        "solid",
        "A class should have only one reason to change — separate concerns into cohesive units.",
    ),
    "open-closed-principle": (
        "Open-Closed Principle",
        "Open-Closed Principle",
        "solid",
        "Open for extension, closed for modification — plug in behavior without editing core logic.",
    ),
    "liskov-substitution-principle": (
        "Liskov Substitution Principle",
        "Liskov Substitution Principle",
        "solid",
        "Subtypes must be substitutable for their base types without breaking client expectations.",
    ),
    "interface-segregation-principle": (
        "Interface Segregation Principle",
        "Interface Segregation Principle",
        "solid",
        "Clients should not depend on methods they do not use — prefer small, role-specific interfaces.",
    ),
    "dependency-inversion-principle": (
        "Dependency Inversion Principle",
        "Dependency Inversion Principle",
        "solid",
        "Depend on abstractions, not concretions — high-level modules should not depend on low-level details.",
    ),
    "solid-principles-composition-guide": (
        "SOLID Principles Composition Guide",
        "SOLID Composition Guide",
        "solid",
        "How SOLID principles work together — smell-to-fix map and composition over inheritance.",
    ),
    "factory-method-pattern": (
        "Factory Method Pattern",
        "Factory Method",
        "creational",
        "Defer object creation to subclasses or providers while keeping client code on abstractions.",
    ),
    "abstract-factory-pattern": (
        "Abstract Factory Pattern",
        "Abstract Factory",
        "creational",
        "Create families of related objects without naming concrete classes.",
    ),
    "builder-pattern": (
        "Builder Pattern",
        "Builder",
        "creational",
        "Construct complex objects step-by-step with a fluent, readable API.",
    ),
    "prototype-pattern": (
        "Prototype Pattern",
        "Prototype",
        "creational",
        "Clone existing instances instead of building from scratch when construction is expensive.",
    ),
    "singleton-pattern": (
        "Singleton Pattern",
        "Singleton",
        "creational",
        "Ensure a single shared instance — and when Spring scopes make manual singletons unnecessary.",
    ),
    "adapter-pattern": (
        "Adapter Pattern",
        "Adapter",
        "structural",
        "Wrap a legacy or third-party API behind an interface your domain already understands.",
    ),
    "decorator-pattern": (
        "Decorator Pattern",
        "Decorator",
        "structural",
        "Add responsibilities dynamically without subclass explosion.",
    ),
    "facade-pattern": (
        "Facade Pattern",
        "Facade",
        "structural",
        "Provide a simplified entry point over a complex subsystem.",
    ),
    "proxy-pattern": (
        "Proxy Pattern",
        "Proxy",
        "structural",
        "Control access to a real subject — lazy load, cache, security, or remote delegation.",
    ),
    "composite-pattern": (
        "Composite Pattern",
        "Composite",
        "structural",
        "Treat individual objects and compositions uniformly in tree structures.",
    ),
    "bridge-pattern": (
        "Bridge Pattern",
        "Bridge",
        "structural",
        "Decouple abstraction from implementation so both can vary independently.",
    ),
    "flyweight-pattern": (
        "Flyweight Pattern",
        "Flyweight",
        "structural",
        "Share intrinsic state across many fine-grained objects to reduce memory.",
    ),
    "strategy-pattern": (
        "Strategy Pattern",
        "Strategy",
        "behavioral",
        "Encapsulate interchangeable algorithms and select them at runtime.",
    ),
    "observer-pattern": (
        "Observer Pattern",
        "Observer",
        "behavioral",
        "Notify dependents automatically when subject state changes.",
    ),
    "command-pattern": (
        "Command Pattern",
        "Command",
        "behavioral",
        "Encapsulate requests as objects to support undo, queueing, and logging.",
    ),
    "state-pattern": (
        "State Pattern",
        "State",
        "behavioral",
        "Delegate behavior to state objects as internal state transitions.",
    ),
    "chain-of-responsibility-pattern": (
        "Chain of Responsibility Pattern",
        "Chain of Responsibility",
        "behavioral",
        "Pass a request along a handler chain until one processes it.",
    ),
    "template-method-pattern": (
        "Template Method Pattern",
        "Template Method",
        "behavioral",
        "Define algorithm skeleton in base class; subclasses override steps.",
    ),
    "iterator-pattern": (
        "Iterator Pattern",
        "Iterator",
        "behavioral",
        "Traverse collections without exposing internal representation.",
    ),
    "mediator-pattern": (
        "Mediator Pattern",
        "Mediator",
        "behavioral",
        "Centralize complex interactions between colleagues to reduce coupling.",
    ),
    "memento-pattern": (
        "Memento Pattern",
        "Memento",
        "behavioral",
        "Capture and restore object state without breaking encapsulation.",
    ),
    "visitor-pattern": (
        "Visitor Pattern",
        "Visitor",
        "behavioral",
        "Add operations to object structures without modifying element classes.",
    ),
    "repository-and-unit-of-work": (
        "Repository & Unit of Work",
        "Repository & UoW",
        "architecture",
        "Persistence abstraction with transactional boundary coordination.",
    ),
    "dependency-injection-inversion-of-control": (
        "Dependency Injection & Inversion of Control",
        "DI & IoC",
        "architecture",
        "Spring-style composition root — wiring dependencies via container, not `new`.",
    ),
    "dto-entity-mapper-separation": (
        "DTO vs Entity Mapper Separation",
        "DTO vs Entity",
        "architecture",
        "Keep API contracts separate from persistence/domain models.",
    ),
    "layered-vs-hexagonal-architecture": (
        "Layered vs Hexagonal Architecture",
        "Layered vs Hexagonal",
        "architecture",
        "Compare classic tiers with ports-and-adapters for testable boundaries.",
    ),
    "domain-driven-design-building-blocks": (
        "Domain-Driven Design Building Blocks",
        "DDD Building Blocks",
        "architecture",
        "Entity, Value Object, Aggregate, and Domain Service in LLD interviews.",
    ),
    "specification-pattern": (
        "Specification Pattern",
        "Specification",
        "architecture",
        "Composable business rules for queries and validation.",
    ),
    "parking-lot-system-lld": (
        "Parking Lot System LLD",
        "Parking Lot LLD",
        "case-study",
        "Classic LLD — spots, vehicles, tickets, pricing strategies, and concurrency.",
    ),
    "elevator-control-system-lld": (
        "Elevator Control System LLD",
        "Elevator LLD",
        "case-study",
        "State machine, scheduling algorithm, and multi-elevator coordination.",
    ),
    "in-memory-rate-limiter-lld": (
        "In-Memory Rate Limiter LLD",
        "Rate Limiter LLD",
        "case-study",
        "Token bucket / sliding window in-process — Strategy and thread-safety.",
    ),
    "notification-service-lld": (
        "Notification Service LLD",
        "Notification LLD",
        "case-study",
        "Channel strategy (email, SMS, push), observer dispatch, and retry.",
    ),
    "task-scheduler-lld": (
        "Task Scheduler LLD",
        "Task Scheduler LLD",
        "case-study",
        "Priority queue, worker pool, and command/job encapsulation.",
    ),
    "strategy-vs-state-vs-template-method": (
        "Strategy vs State vs Template Method",
        "Strategy vs State vs Template",
        "comparison",
        "Decision guide — three behavioral patterns juniors confuse.",
    ),
    "decorator-vs-proxy-vs-bridge": (
        "Decorator vs Proxy vs Bridge",
        "Decorator vs Proxy vs Bridge",
        "comparison",
        "Structural pattern disambiguation with intent and lifetime rules.",
    ),
    "factory-method-vs-abstract-factory-vs-builder": (
        "Factory Method vs Abstract Factory vs Builder",
        "Factory vs Builder",
        "comparison",
        "Creational pattern selection for object vs family vs stepwise construction.",
    ),
}

SKIP = {"single-responsibility-principle", "strategy-pattern"}

IMPL_SECTION = r"""
### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" python="Python" >}}
{{< impl-tab lang="java" >}}

```java
// TODO: minimal Java reference implementation
public interface Example {
    void execute();
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
// TODO: idiomatic Go equivalent
type Example interface {
    Execute()
}
```

{{< /impl-tab >}}
{{< impl-tab lang="python" >}}

```python
# TODO: idiomatic Python equivalent (Protocol / dataclass)
from typing import Protocol

class Example(Protocol):
    def execute(self) -> None: ...
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---
"""


def stub_body(title: str) -> str:
    return f"""### Problem & Intent

_TODO: Describe what {title} solves and the dominant design force it addresses._

---

### When to Use / When NOT to Use

| Situation | Use? | Why |
| :--- | :---: | :--- |
| _TODO: positive scenario_ | Yes | _reason_ |
| _TODO: negative scenario_ | No | _prefer simpler approach_ |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class Context
    class Abstraction
    Context --> Abstraction : uses
```

---

### Interaction Flow

```mermaid
sequenceDiagram
    participant Client
    participant Context
    participant Implementation
    Client->>Context: invoke()
    Context->>Implementation: delegate()
    Implementation-->>Context: result
    Context-->>Client: result
```

---

""" + IMPL_SECTION + """
### Trade-offs & Operational Realities

| Concern | Impact |
| :--- | :--- |
| **Testability** | _TODO_ |
| **Complexity** | _TODO_ |
| **Framework fit** | _TODO_ |

---

### Junior Mistakes

- _TODO: common misapplication_
- _TODO: pattern for pattern's sake_

---

### Senior Questions

1. _TODO: extension without modification probe_
2. _TODO: comparison with adjacent pattern_
3. _TODO: testing strategy_
4. _TODO: production trade-off_

---

### Revision Cheat Sheet

- **One line:** _TODO_
- **Trigger smell:** _TODO_
- **Pairs with:** _TODO_
- **Avoid when:** _TODO_

---

### See Also

- _TODO: link related LLD topics_
"""


def main() -> None:
    with open(ROOT / "data" / "lld_modules.yaml", encoding="utf-8") as f:
        modules = yaml.safe_load(f)["modules"]

    out_dir = ROOT / "content" / "lld"
    out_dir.mkdir(parents=True, exist_ok=True)

    for mod in modules:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        for idx, slug in enumerate(mod["topics"]):
            if slug in SKIP:
                continue
            title, short, tag, desc = TITLES[slug]
            section_ref = f"{mod_id}.{idx + 1}"
            front_matter = f"""---
title: "{title}"
date: 2026-06-30T10:00:00+00:00
draft: true
description: "{desc}"
tags: ["lld", "{tag}", "java", "golang"]
categories: ["Design Patterns"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{section_ref}"
languages: ["java", "golang"]
---

"""
            path = out_dir / f"{slug}.md"
            path.write_text(front_matter + stub_body(title), encoding="utf-8")
            print(f"wrote {path.name}")

    print("done")


if __name__ == "__main__":
    main()
