"""Generate refactored Design Patterns handbook content (Phase B)."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DP = ROOT / "content" / "design-patterns"
DATA = ROOT / "data"
DATE = "2026-07-03T14:00:00+00:00"
BASE = "/design-patterns"

FM_PATTERN = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: [{tags}]
categories: ["Design Patterns"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
languages: [{languages}]
ShowToc: true{extra_fm}{aliases}
---

"""

FM_INTERVIEW = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["design-patterns", "lld", "interview"]
categories: ["Design Patterns"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
ShowToc: true
interviewHandbook: true{aliases}
---

"""


def aliases_block(*paths: str) -> str:
    if not paths:
        return ""
    lines = "\n".join(f'  - "{p}"' for p in paths)
    return f"\naliases:\n{lines}"


def read_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return re.sub(r"^---.*?---\n", "", text, count=1, flags=re.DOTALL)


# old flat slug -> new relative path (under design-patterns/)
SLUG_TO_NEW: dict[str, str] = {
    "single-responsibility-principle": "01-solid-principles/single-responsibility-principle",
    "open-closed-principle": "01-solid-principles/open-closed-principle",
    "liskov-substitution-principle": "01-solid-principles/liskov-substitution-principle",
    "interface-segregation-principle": "01-solid-principles/interface-segregation-principle",
    "dependency-inversion-principle": "01-solid-principles/dependency-inversion-principle",
    "solid-principles-composition-guide": "01-solid-principles/solid-principles-composition-guide",
    "factory-method-pattern": "02-creational-patterns/factory-method-pattern",
    "abstract-factory-pattern": "02-creational-patterns/abstract-factory-pattern",
    "builder-pattern": "02-creational-patterns/builder-pattern",
    "prototype-pattern": "02-creational-patterns/prototype-pattern",
    "singleton-pattern": "02-creational-patterns/singleton-pattern",
    "adapter-pattern": "03-structural-patterns/adapter-pattern",
    "bridge-pattern": "03-structural-patterns/bridge-pattern",
    "composite-pattern": "03-structural-patterns/composite-pattern",
    "decorator-pattern": "03-structural-patterns/decorator-pattern",
    "facade-pattern": "03-structural-patterns/facade-pattern",
    "flyweight-pattern": "03-structural-patterns/flyweight-pattern",
    "proxy-pattern": "03-structural-patterns/proxy-pattern",
    "chain-of-responsibility-pattern": "04-behavioral-patterns/chain-of-responsibility-pattern",
    "command-pattern": "04-behavioral-patterns/command-pattern",
    "iterator-pattern": "04-behavioral-patterns/iterator-pattern",
    "mediator-pattern": "04-behavioral-patterns/mediator-pattern",
    "memento-pattern": "04-behavioral-patterns/memento-pattern",
    "observer-pattern": "04-behavioral-patterns/observer-pattern",
    "state-pattern": "04-behavioral-patterns/state-pattern",
    "strategy-pattern": "04-behavioral-patterns/strategy-pattern",
    "template-method-pattern": "04-behavioral-patterns/template-method-pattern",
    "visitor-pattern": "04-behavioral-patterns/visitor-pattern",
    "decorator-vs-proxy-vs-bridge": "05-pattern-comparisons/decorator-vs-proxy-vs-bridge",
    "factory-method-vs-abstract-factory-vs-builder": "05-pattern-comparisons/factory-method-vs-abstract-factory-vs-builder",
    "strategy-vs-state-vs-template-method": "05-pattern-comparisons/strategy-vs-state-vs-template-method",
    "dependency-injection-inversion-of-control": "06-architectural-principles/dependency-injection-inversion-of-control",
    "layered-vs-hexagonal-architecture": "06-architectural-principles/layered-vs-hexagonal-architecture",
    "domain-driven-design-building-blocks": "06-architectural-principles/domain-driven-design-building-blocks",
    "dto-entity-mapper-separation": "06-architectural-principles/dto-entity-mapper-separation",
    "repository-and-unit-of-work": "06-architectural-principles/repository-and-unit-of-work",
    "specification-pattern": "06-architectural-principles/specification-pattern",
    "parking-lot-system-lld": "08-lld-case-studies/parking-lot",
    "elevator-control-system-lld": "08-lld-case-studies/elevator-control-system",
    "in-memory-rate-limiter-lld": "08-lld-case-studies/rate-limiter",
    "notification-service-lld": "08-lld-case-studies/notification-system",
    "task-scheduler-lld": "08-lld-case-studies/task-scheduler-lld",
}

# Topic metadata for moved files: (mod, mod_title, ref, weight, short, title override optional)
TOPIC_META: dict[str, tuple[int, str, str, int, str]] = {
    "01-solid-principles/single-responsibility-principle": (1, "SOLID Principles", "1.1", 101, "SRP"),
    "01-solid-principles/open-closed-principle": (1, "SOLID Principles", "1.2", 102, "OCP"),
    "01-solid-principles/liskov-substitution-principle": (1, "SOLID Principles", "1.3", 103, "LSP"),
    "01-solid-principles/interface-segregation-principle": (1, "SOLID Principles", "1.4", 104, "ISP"),
    "01-solid-principles/dependency-inversion-principle": (1, "SOLID Principles", "1.5", 105, "DIP"),
    "01-solid-principles/solid-principles-composition-guide": (1, "SOLID Principles", "1.6", 106, "SOLID Guide"),
    "02-creational-patterns/factory-method-pattern": (2, "Creational Patterns", "2.1", 201, "Factory Method"),
    "02-creational-patterns/abstract-factory-pattern": (2, "Creational Patterns", "2.2", 202, "Abstract Factory"),
    "02-creational-patterns/builder-pattern": (2, "Creational Patterns", "2.3", 203, "Builder"),
    "02-creational-patterns/prototype-pattern": (2, "Creational Patterns", "2.4", 204, "Prototype"),
    "02-creational-patterns/singleton-pattern": (2, "Creational Patterns", "2.5", 205, "Singleton"),
    "03-structural-patterns/adapter-pattern": (3, "Structural Patterns", "3.1", 301, "Adapter"),
    "03-structural-patterns/bridge-pattern": (3, "Structural Patterns", "3.2", 302, "Bridge"),
    "03-structural-patterns/composite-pattern": (3, "Structural Patterns", "3.3", 303, "Composite"),
    "03-structural-patterns/decorator-pattern": (3, "Structural Patterns", "3.4", 304, "Decorator"),
    "03-structural-patterns/facade-pattern": (3, "Structural Patterns", "3.5", 305, "Facade"),
    "03-structural-patterns/flyweight-pattern": (3, "Structural Patterns", "3.6", 306, "Flyweight"),
    "03-structural-patterns/proxy-pattern": (3, "Structural Patterns", "3.7", 307, "Proxy"),
    "04-behavioral-patterns/chain-of-responsibility-pattern": (4, "Behavioral Patterns", "4.1", 401, "Chain"),
    "04-behavioral-patterns/command-pattern": (4, "Behavioral Patterns", "4.2", 402, "Command"),
    "04-behavioral-patterns/iterator-pattern": (4, "Behavioral Patterns", "4.3", 403, "Iterator"),
    "04-behavioral-patterns/mediator-pattern": (4, "Behavioral Patterns", "4.4", 404, "Mediator"),
    "04-behavioral-patterns/memento-pattern": (4, "Behavioral Patterns", "4.5", 405, "Memento"),
    "04-behavioral-patterns/observer-pattern": (4, "Behavioral Patterns", "4.6", 406, "Observer"),
    "04-behavioral-patterns/state-pattern": (4, "Behavioral Patterns", "4.7", 407, "State"),
    "04-behavioral-patterns/strategy-pattern": (4, "Behavioral Patterns", "4.8", 408, "Strategy"),
    "04-behavioral-patterns/template-method-pattern": (4, "Behavioral Patterns", "4.9", 409, "Template Method"),
    "04-behavioral-patterns/visitor-pattern": (4, "Behavioral Patterns", "4.10", 410, "Visitor"),
    "05-pattern-comparisons/decorator-vs-proxy-vs-bridge": (5, "Pattern Comparisons", "5.3", 503, "Dec vs Proxy"),
    "05-pattern-comparisons/factory-method-vs-abstract-factory-vs-builder": (5, "Pattern Comparisons", "5.9", 509, "Creational 3-way"),
    "05-pattern-comparisons/strategy-vs-state-vs-template-method": (5, "Pattern Comparisons", "5.10", 510, "Behavioral 3-way"),
    "06-architectural-principles/dependency-injection-inversion-of-control": (6, "Architectural Principles", "6.1", 601, "DI / IoC"),
    "06-architectural-principles/layered-vs-hexagonal-architecture": (6, "Architectural Principles", "6.2", 602, "Layered vs Hex"),
    "06-architectural-principles/domain-driven-design-building-blocks": (6, "Architectural Principles", "6.3", 603, "DDD Blocks"),
    "06-architectural-principles/dto-entity-mapper-separation": (6, "Architectural Principles", "6.4", 604, "DTO Separation"),
    "06-architectural-principles/repository-and-unit-of-work": (6, "Architectural Principles", "6.5", 605, "Repository"),
    "06-architectural-principles/specification-pattern": (6, "Architectural Principles", "6.6", 606, "Specification"),
    "08-lld-case-studies/parking-lot": (8, "LLD Case Studies", "8.3", 803, "Parking Lot"),
    "08-lld-case-studies/elevator-control-system": (8, "LLD Case Studies", "8.1", 801, "Elevator"),
    "08-lld-case-studies/rate-limiter": (8, "LLD Case Studies", "8.2", 802, "Rate Limiter"),
    "08-lld-case-studies/notification-system": (8, "LLD Case Studies", "8.4", 804, "Notification"),
    "08-lld-case-studies/task-scheduler-lld": (8, "LLD Case Studies", "8.7", 807, "Task Scheduler"),
}


def fix_links(body: str) -> str:
    for old_slug, new_rel in sorted(SLUG_TO_NEW.items(), key=lambda x: -len(x[0])):
        old_url = f"{BASE}/{old_slug}/"
        new_url = f"{BASE}/{new_rel}/"
        body = body.replace(old_url, new_url)
    # legacy comparison paths
    body = body.replace(f"{BASE}/factory-method-vs-abstract-factory-vs-builder/", f"{BASE}/05-pattern-comparisons/factory-vs-builder/")
    body = body.replace(f"{BASE}/strategy-vs-state-vs-template-method/", f"{BASE}/05-pattern-comparisons/strategy-vs-state/")
    return body


def extract_fm_block(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---", text, flags=re.DOTALL)
    return m.group(1) if m else ""


def fm_line(block: str, key: str, default: str = "") -> str:
    for line in block.splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return default


def write_pattern(rel: str, body: str, *, old_slug: str | None = None, desc: str = "", title: str = ""):
    path = DP / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    meta_key = rel.removesuffix(".md")
    mod, mod_title, ref, weight, short = TOPIC_META.get(meta_key, (1, "Design Patterns", "1.0", 100, "Topic"))
    old_path = DP / f"{old_slug}.md" if old_slug else None
    if old_path and old_path.exists():
        raw = old_path.read_text(encoding="utf-8")
        block = extract_fm_block(raw)
        if not title:
            title = fm_line(block, "title", short).strip('"')
        if not desc:
            desc = fm_line(block, "description", title).strip('"')
        tags = fm_line(block, "tags", '["lld", "java", "golang"]')
        langs = fm_line(block, "languages", '["java", "golang"]')
    else:
        title = title or short
        desc = desc or title
        tags = '["lld", "java", "golang"]'
        langs = '["java", "golang"]'
    alias = aliases_block(f"{BASE}/{old_slug}/") if old_slug else ""
    tags_inner = tags.strip()
    if tags_inner.startswith("["):
        tags_inner = tags_inner[1:-1].strip()
    text = FM_PATTERN.format(
        title=title.replace('"', "'"),
        date=DATE,
        desc=desc.replace('"', "'"),
        tags=tags_inner,
        short=short,
        mod=mod,
        mod_title=mod_title,
        ref=ref,
        weight=weight,
        languages=langs.strip("[]").strip(),
        extra_fm="",
        aliases=alias,
    ) + fix_links(body.strip()) + "\n"
    path.write_text(text, encoding="utf-8")


FM_INDEX = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["design-patterns", "lld"]
categories: ["Design Patterns"]
shortTitle: "{short}"
ShowPageNums: true{aliases}
---

"""


def write_simple(rel: str, body: str, *, title: str, desc: str, short: str, mod: int, mod_title: str, ref: str, weight: int, interview: bool = False, aliases: tuple[str, ...] = ()):
    path = DP / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    alias = aliases_block(*aliases)
    if interview:
        text = FM_INTERVIEW.format(
            title=title, date=DATE, desc=desc, short=short, mod=mod, mod_title=mod_title, ref=ref, weight=weight, aliases=alias
        ) + body.strip() + "\n"
    elif rel == "_index.md":
        text = FM_INDEX.format(title=title, date=DATE, desc=desc, short=short, aliases=alias) + body.strip() + "\n"
    else:
        text = FM_INDEX.format(title=title, date=DATE, desc=desc, short=short, aliases=alias).replace(
            'ShowPageNums: true', f"module: {mod}\nmoduleTitle: \"{mod_title}\"\nsectionRef: \"{ref}\"\nweight: {weight}\nShowToc: true"
        ) + body.strip() + "\n"
    path.write_text(text, encoding="utf-8")


def move_all_existing() -> None:
    for old_slug, new_rel in SLUG_TO_NEW.items():
        old = DP / f"{old_slug}.md"
        if not old.exists():
            continue
        body = read_body(old)
        write_pattern(new_rel + ".md", body, old_slug=old_slug)


def section_indexes() -> None:
    sections = [
        ("01-solid-principles", "SOLID Principles", "Single-responsibility through dependency inversion, plus composition guide.", 1),
        ("02-creational-patterns", "Creational Patterns", "GoF creational patterns — object creation families.", 2),
        ("03-structural-patterns", "Structural Patterns", "Composition, wrapping, and structural reuse.", 3),
        ("04-behavioral-patterns", "Behavioral Patterns", "Algorithms, notification, and object collaboration.", 4),
        ("05-pattern-comparisons", "Pattern Comparisons", "Disambiguate patterns juniors confuse.", 5),
        ("06-architectural-principles", "Architectural Principles", "DI, DDD, layering, and persistence boundaries.", 6),
        ("07-anti-patterns", "Anti-Patterns", "Smells, misuse, and corrective patterns.", 7),
        ("08-lld-case-studies", "LLD Case Studies", "Applied low-level design interview scenarios.", 8),
        ("09-pattern-selection-guide", "Pattern Selection Guide", "When to use which pattern — decision support.", 9),
        ("10-interview-guide", "Interview Guide", "150-question bank and role-specific subsets.", 10),
        ("11-learning-paths", "Learning Paths", "Curated reading by seniority and goal.", 11),
    ]
    for folder, title, desc, mod in sections:
        write_simple(
            f"{folder}/_index.md",
            f"# {title}\n\n{desc}\n\nSee [handbook index]({BASE}/).\n",
            title=title,
            desc=desc,
            short=title,
            mod=mod,
            mod_title="Design Patterns Handbook",
            ref="0",
            weight=mod,
        )


def comparison_factory_vs_builder() -> None:
    body = f"""### Problem & Intent

**Factory Method** and **Builder** both hide construction — but Factory Method picks **which implementation** of one product type, while Builder assembles **one complex object** step-by-step. Confusing them yields a Builder for two fields or a Factory with twelve constructor parameters.

---

### Pattern Comparison at a Glance

| Dimension | Factory Method | Builder |
| :--- | :--- | :--- |
| **Intent** | Defer concrete product to subclass/provider | Separate construction from representation |
| **Products** | One interface, multiple impls | One aggregate, optional parts |
| **Client call** | `factory.create()` | `builder.setA().setB().build()` |
| **Validation** | At creation time | Often at `build()` |
| **Smell** | `switch` on type | Telescoping constructor |

---

### When to Use / When NOT to Use

| Situation | Factory Method | Builder |
| :--- | :---: | :---: |
| Postgres vs MySQL connection from config | Yes | — |
| HTTP request with 10 optional headers | — | Yes |
| Spring `@Bean` returns interface impl | Yes | — |
| Immutable object, 3 required fields | Maybe | Maybe — record may suffice |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class ConnectionFactory {{
        <<interface>>
        +create() Connection
    }}
    class PostgresFactory
    class HttpRequestBuilder {{
        +header(k,v)
        +body(b)
        +build() HttpRequest
    }}
    ConnectionFactory <|.. PostgresFactory
```

---

### Interaction Flow

```mermaid
sequenceDiagram
    participant Client
    participant Factory as ConnectionFactory
    participant Product as Connection
    Client->>Factory: create()
    Factory->>Product: new impl
    Product-->>Client: Connection
```

---

### Implementation

See canonical pages: [Factory Method]({BASE}/02-creational-patterns/factory-method-pattern/) and [Builder]({BASE}/02-creational-patterns/builder-pattern/).

---

### Trade-offs & Operational Realities

| Tradeoff | Factory Method | Builder |
| :--- | :--- | :--- |
| **Complexity** | Low per product | Higher fluent API surface |
| **Testability** | Mock factory | Mock builder or director |
| **Framework fit** | DI `@Bean` | Step DSLs, test fixtures |

---

### Junior Mistakes

- Using Builder when a constructor or factory function suffices.
- Using Factory Method when families of related products need [Abstract Factory]({BASE}/05-pattern-comparisons/factory-vs-abstract-factory/).

---

### Senior Questions

1. Where would validation live in each pattern?
2. How does Go `functional options` relate to Builder?

---

### Revision Cheat Sheet

- **Factory Method** → which single product implementation.
- **Builder** → many optional fields, one `build()` validation.

---

### See Also

- [Factory vs Abstract Factory]({BASE}/05-pattern-comparisons/factory-vs-abstract-factory/)
- [Creational 3-way guide]({BASE}/05-pattern-comparisons/factory-method-vs-abstract-factory-vs-builder/)
- [Pattern decision tree]({BASE}/09-pattern-selection-guide/pattern-decision-tree/)
"""
    write_simple(
        "05-pattern-comparisons/factory-vs-builder.md",
        body,
        title="Factory Method vs Builder",
        desc="Pairwise comparison — single product selection versus stepwise assembly.",
        short="Factory vs Builder",
        mod=5,
        mod_title="Pattern Comparisons",
        ref="5.1",
        weight=501,
        aliases=(f"{BASE}/factory-method-vs-abstract-factory-vs-builder/",),
    )


def comparison_factory_vs_abstract() -> None:
    body = f"""### Problem & Intent

**Factory Method** creates **one product type** with polymorphic implementations. **Abstract Factory** creates **families of related products** that must stay consistent (UI theme, cloud provider bundle). Use Factory Method twice before reaching for Abstract Factory.

---

### Pattern Comparison at a Glance

| Dimension | Factory Method | Abstract Factory |
| :--- | :--- | :--- |
| **Products per factory** | One | Multiple related |
| **Consistency constraint** | None | Cross-product (theme) |
| **Variation axis** | Which impl of one type | Which platform bundle |
| **Typical smell** | Scattered `new` | Mismatched Mac button + Win scrollbar |

---

### When to Use / When NOT to Use

| Situation | Factory Method | Abstract Factory |
| :--- | :---: | :---: |
| Single `Connection` type | Yes | — |
| `Button` + `Checkbox` same OS theme | — | Yes |
| AWS S3 + SQS + Secrets as bundle | — | Yes |
| Two unrelated products | Two factory methods | No |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class DocumentFactory {{
        +createParser() Parser
    }}
    class UIFactory {{
        +createButton() Button
        +createCheckbox() Checkbox
    }}
```

---

### Interaction Flow

```mermaid
flowchart LR
    A[Client] --> B{{Need family?}}
    B -->|No| C[Factory Method]
    B -->|Yes| D[Abstract Factory]
```

---

### Implementation

See [Factory Method]({BASE}/02-creational-patterns/factory-method-pattern/) and [Abstract Factory]({BASE}/02-creational-patterns/abstract-factory-pattern/).

---

### Trade-offs & Operational Realities

| Tradeoff | Factory Method | Abstract Factory |
| :--- | :--- | :--- |
| **Adding product** | New subclass | New method on factory + all impls |
| **Test doubles** | One mock product | Mock entire family |

---

### Junior Mistakes

- Abstract Factory for one product type.
- Factory Method when cross-product consistency is required.

---

### Senior Questions

1. How does Abstract Factory relate to plugin architectures?
2. When does DI container replace hand-rolled abstract factories?

---

### Revision Cheat Sheet

- **One type** → Factory Method.
- **Consistent family** → Abstract Factory.

---

### See Also

- [Factory vs Builder]({BASE}/05-pattern-comparisons/factory-vs-builder/)
- [Creational 3-way guide]({BASE}/05-pattern-comparisons/factory-method-vs-abstract-factory-vs-builder/)
"""
    write_simple(
        "05-pattern-comparisons/factory-vs-abstract-factory.md",
        body,
        title="Factory Method vs Abstract Factory",
        desc="Single product creation versus consistent product families.",
        short="Factory vs AF",
        mod=5,
        mod_title="Pattern Comparisons",
        ref="5.2",
        weight=502,
    )


def comparison_strategy_vs_state() -> None:
    body = f"""### Problem & Intent

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
| Fixed workflow, one varying step | — | — → [Template Method]({BASE}/04-behavioral-patterns/template-method-pattern/) |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class CheckoutService {{
        -PricingStrategy strategy
        +setStrategy(s)
    }}
    class OrderContext {{
        -OrderState state
        +pay()
        +ship()
    }}
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

See [Strategy]({BASE}/04-behavioral-patterns/strategy-pattern/) and [State]({BASE}/04-behavioral-patterns/state-pattern/).

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

- [Behavioral 3-way guide]({BASE}/05-pattern-comparisons/strategy-vs-state-vs-template-method/)
- [Parking Lot LLD]({BASE}/08-lld-case-studies/parking-lot/)
"""
    write_simple(
        "05-pattern-comparisons/strategy-vs-state.md",
        body,
        title="Strategy vs State",
        desc="Algorithm selection versus lifecycle-driven behavior.",
        short="Strategy vs State",
        mod=5,
        mod_title="Pattern Comparisons",
        ref="5.4",
        weight=504,
        aliases=(f"{BASE}/strategy-vs-state-vs-template-method/",),
    )


def comparison_composition_vs_inheritance() -> None:
    body = f"""### Problem & Intent

**Composition** (has-a) favors runtime flexibility and test doubles. **Inheritance** (is-a) shares implementation and enforces contracts — but tight coupling and fragile base classes drive teams toward composition + interfaces.

---

### Pattern Comparison at a Glance

| Dimension | Composition | Inheritance |
| :--- | :--- | :--- |
| **Coupling** | Looser | Tighter to base |
| **Runtime change** | Swap delegate | Fixed hierarchy |
| **Reuse** | Delegate behavior | Override hooks |
| **Go default** | Preferred | Embedding, not subclassing |

---

### When to Use / When NOT to Use

| Situation | Composition | Inheritance |
| :--- | :---: | :---: |
| Pricing policy varies at runtime | Yes | — |
| Template Method fixed skeleton | — | Yes (or composition + strategy) |
| Deep framework extension points | Maybe | Yes if hooks are stable |
| Single-language Go service | Yes | Rare |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class Bird {{
        -FlyBehavior fly
        +move()
    }}
    class Duck {{
        +quack()
    }}
    Bird --> FlyBehavior
    class FlyingDuck
    Duck <|-- FlyingDuck
```

---

### Interaction Flow

```mermaid
flowchart TD
    Q{{Behavior varies at runtime?}}
    Q -->|Yes| C[Composition + Strategy]
    Q -->|No| I{{Stable is-a taxonomy?}}
    I -->|Yes| H[Inheritance / Template Method]
    I -->|No| C
```

---

### Implementation

Prefer [Strategy]({BASE}/04-behavioral-patterns/strategy-pattern/) and [Decorator]({BASE}/03-structural-patterns/decorator-pattern/) for composition; [Template Method]({BASE}/04-behavioral-patterns/template-method-pattern/) for inheritance hooks.

---

### Trade-offs & Operational Realities

| Tradeoff | Composition | Inheritance |
| :--- | :--- | :--- |
| **Testability** | Easy mock delegate | Subclass test matrix |
| **LSP risk** | Lower | Higher |

---

### Junior Mistakes

- Inheritance for code reuse only (violates LSP).
- Composition explosion without interfaces.

---

### Senior Questions

1. How does LSP constrain inheritance choices?
2. When is Template Method still idiomatic in Java?

---

### Revision Cheat Sheet

- **Favor composition** for varying behavior.
- **Inheritance** for stable taxonomies and hook methods.

---

### See Also

- [LSP]({BASE}/01-solid-principles/liskov-substitution-principle/)
- [Interface vs Abstract Class]({BASE}/05-pattern-comparisons/interface-vs-abstract-class/)
"""
    write_simple(
        "05-pattern-comparisons/composition-vs-inheritance.md",
        body,
        title="Composition vs Inheritance",
        desc="Has-a versus is-a — flexibility, LSP, and pattern selection.",
        short="Comp vs Inherit",
        mod=5,
        mod_title="Pattern Comparisons",
        ref="5.5",
        weight=505,
    )


def comparison_interface_vs_abstract() -> None:
    body = f"""### Problem & Intent

**Interfaces** define contracts without shared state. **Abstract classes** share implementation and optional hooks. Language features (Java default methods, Go implicit interfaces) change the calculus — but the design force is the same: **how much shared code vs pure abstraction**.

---

### Pattern Comparison at a Glance

| Dimension | Interface | Abstract Class |
| :--- | :--- | :--- |
| **Multiple inheritance** | Yes (Java) | Single |
| **Shared state** | No | Yes |
| **Default behavior** | Default methods (Java 8+) | Concrete + abstract methods |
| **Go** | Implicit interfaces | No abstract classes — use embedding |

---

### When to Use / When NOT to Use

| Situation | Interface | Abstract Class |
| :--- | :---: | :---: |
| PaymentGateway contract | Yes | — |
| Template Method with shared steps | — | Yes |
| Cross-cutting capability (Serializable) | Yes | — |
| Need ctor enforcement + shared fields | — | Yes |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class PaymentGateway {{
        <<interface>>
        +charge(amount)
    }}
    class AbstractExporter {{
        +export()
        #loadData()
        #writeOutput()*
    }}
```

---

### Interaction Flow

```mermaid
flowchart TD
    A{{Need shared implementation?}}
    A -->|No| I[Interface]
    A -->|Yes| B{{Multiple roles?}}
    B -->|Yes| I
    B -->|No| AC[Abstract class]
```

---

### Implementation

See [ISP]({BASE}/01-solid-principles/interface-segregation-principle/) and [Template Method]({BASE}/04-behavioral-patterns/template-method-pattern/).

---

### Trade-offs & Operational Realities

| Tradeoff | Interface | Abstract Class |
| :--- | :--- | :--- |
| **Evolution** | Adding methods breaks impls | Can add concrete methods |
| **Testing** | Trivial fakes | Subclass or spy |

---

### Junior Mistakes

- Fat interface violating ISP.
- Abstract class as dumping ground for unrelated helpers.

---

### Senior Questions

1. How do sealed classes change extension in Java 17+?
2. How do Go interfaces stay small?

---

### Revision Cheat Sheet

- **Contract only** → interface.
- **Shared skeleton** → abstract class (Java); composition in Go.

---

### See Also

- [Composition vs Inheritance]({BASE}/05-pattern-comparisons/composition-vs-inheritance/)
- [DIP]({BASE}/01-solid-principles/dependency-inversion-principle/)
"""
    write_simple(
        "05-pattern-comparisons/interface-vs-abstract-class.md",
        body,
        title="Interface vs Abstract Class",
        desc="Contract-only abstractions versus shared implementation skeletons.",
        short="Iface vs Abstract",
        mod=5,
        mod_title="Pattern Comparisons",
        ref="5.6",
        weight=506,
    )


def anti_pattern(slug: str, title: str, ref: str, weight: int, body: str) -> None:
    write_simple(
        f"07-anti-patterns/{slug}.md",
        body,
        title=title,
        desc=f"Anti-pattern — {title.lower()} symptoms, causes, and corrective design.",
        short=title.split()[0],
        mod=7,
        mod_title="Anti-Patterns",
        ref=ref,
        weight=weight,
    )


def anti_patterns() -> None:
    anti_pattern(
        "god-object",
        "God Object",
        "7.1",
        701,
        f"""### Problem & Intent

A **god object** centralizes too many responsibilities — persistence, validation, notifications, reporting — becoming the single point every change touches. It violates [SRP]({BASE}/01-solid-principles/single-responsibility-principle/) and blocks independent testing.

---

### When to Use / When NOT to Use

| Situation | God Object? | Why |
| :--- | :---: | :--- |
| Class name is `Manager`, `Handler`, `Util` with 20+ methods | Smell | Split by reason to change |
| Prototype script under 200 lines | Maybe OK | Revisit before production |
| Legacy module with no tests | Anti-pattern | Incremental extract |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class OrderManager {{
        +validate()
        +save()
        +email()
        +generatePdf()
        +applyDiscount()
    }}
```

---

### Interaction Flow

```mermaid
flowchart TD
    A[Schema change] --> G[God Object]
    B[Email template change] --> G
    C[Tax rule change] --> G
```

---

### Implementation

**Corrective pattern:** Extract [Facade]({BASE}/03-structural-patterns/facade-pattern/) only after splitting services — facade orchestrates, it does not absorb all logic.

---

### Trade-offs & Operational Realities

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Big-bang rewrite** | Clean model | High risk |
| **Strangler extract** | Safer | Temporary duplication |

---

### Junior Mistakes

- Renaming `OrderManager` to `OrderService` without splitting responsibilities.
- Adding another `if` branch instead of new class.

---

### Senior Questions

1. How do you prioritize extractions from a god class?
2. What metrics prove the refactor worked?

---

### Revision Cheat Sheet

- **Symptom:** many unrelated imports, huge test setup.
- **Fix:** SRP splits + DIP for dependencies.

---

### See Also

- [SRP]({BASE}/01-solid-principles/single-responsibility-principle/)
- [SOLID composition guide]({BASE}/01-solid-principles/solid-principles-composition-guide/)
- [Shotgun Surgery]({BASE}/07-anti-patterns/shotgun-surgery/)
""",
    )
    anti_pattern(
        "anemic-domain-model",
        "Anemic Domain Model",
        "7.2",
        702,
        f"""### Problem & Intent

**Anemic domain model** puts all behavior in service classes while entities are getters/setters. CRUD templates encourage it — but business rules scatter, invariants leak, and [DDD aggregates]({BASE}/06-architectural-principles/domain-driven-design-building-blocks/) cannot enforce consistency.

---

### When to Use / When NOT to Use

| Situation | Anemic? | Why |
| :--- | :---: | :--- |
| `OrderService` mutates `Order` fields directly | Yes | Move rules into `Order` |
| Read-only reporting DTO | OK | Not domain core |
| Rich `Order.cancel()` checks state | No | Rich model |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class Order {{
        +getStatus()
        +setStatus()
    }}
    class OrderService {{
        +cancel(order)
    }}
```

---

### Interaction Flow

```mermaid
sequenceDiagram
    participant S as OrderService
    participant O as Order
    S->>O: setStatus(CANCELLED)
    Note over S,O: Rules live in service, not entity
```

---

### Implementation

Move invariants into entities; services coordinate transactions and infrastructure.

---

### Trade-offs & Operational Realities

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Anemic + services** | Fast CRUD scaffolding | Rules scatter |
| **Rich domain** | Cohesive invariants | Steeper learning curve |

---

### Junior Mistakes

- Treating DTOs as domain entities.
- Testing only service layer, never domain rules.

---

### Senior Questions

1. Where should cross-aggregate rules live?
2. How does anemic model relate to [Transaction Script]({BASE}/06-architectural-principles/domain-driven-design-building-blocks/)?

---

### Revision Cheat Sheet

- **Tell, don't ask** — entities own behavior.
- **Services** orchestrate, not replace domain logic.

---

### See Also

- [DDD Building Blocks]({BASE}/06-architectural-principles/domain-driven-design-building-blocks/)
- [DTO Separation]({BASE}/06-architectural-principles/dto-entity-mapper-separation/)
""",
    )
    anti_pattern(
        "spaghetti-code",
        "Spaghetti Code",
        "7.3",
        703,
        f"""### Problem & Intent

**Spaghetti code** tangles control flow — cyclic dependencies, global state, and callbacks with no clear entry point. It differs from a legitimately complex workflow that still has bounded modules and tests.

---

### When to Use / When NOT to Use

| Situation | Spaghetti? | Why |
| :--- | :---: | :--- |
| Cannot trace request path without 6 hops | Yes | Introduce layers / facades |
| Event-driven with documented boundaries | No | Complexity with structure |

---

### Structure (Class Diagram)

```mermaid
flowchart TD
    A --> B --> C --> A
    B --> D --> B
```

---

### Interaction Flow

```mermaid
flowchart LR
    E[Entry] --> ???[Unclear modules]
```

---

### Implementation

Break cycles with [DIP]({BASE}/01-solid-principles/dependency-inversion-principle/), introduce [Facade]({BASE}/03-structural-patterns/facade-pattern/), extract [Chain of Responsibility]({BASE}/04-behavioral-patterns/chain-of-responsibility-pattern/) for pipelines.

---

### Trade-offs & Operational Realities

| Fix | Risk |
| :--- | :--- |
| Module boundaries | Temporary feature freeze |
| Incremental strangler | Parallel paths during migration |

---

### Junior Mistakes

- Adding `// TODO refactor` for years.
- Copy-paste branches instead of shared abstractions.

---

### Senior Questions

1. How do you map dependencies to find cycles?
2. When is event spaghetti acceptable?

---

### Revision Cheat Sheet

- **Symptom:** fear of touching one file.
- **Fix:** layers, interfaces, kill globals.

---

### See Also

- [God Object]({BASE}/07-anti-patterns/god-object/)
- [Layered vs Hexagonal]({BASE}/06-architectural-principles/layered-vs-hexagonal-architecture/)
""",
    )
    anti_pattern(
        "shotgun-surgery",
        "Shotgun Surgery",
        "7.4",
        704,
        f"""### Problem & Intent

**Shotgun surgery** — one logical change requires edits across many classes. It often violates [OCP]({BASE}/01-solid-principles/open-closed-principle/) and indicates missing abstraction or duplicated policy.

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

Consolidate variation behind [Strategy]({BASE}/04-behavioral-patterns/strategy-pattern/), [Template Method]({BASE}/04-behavioral-patterns/template-method-pattern/), or configuration.

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

- [OCP]({BASE}/01-solid-principles/open-closed-principle/)
- [Golden Hammer]({BASE}/07-anti-patterns/golden-hammer/)
""",
    )
    anti_pattern(
        "golden-hammer",
        "Golden Hammer",
        "7.5",
        705,
        f"""### Problem & Intent

**Golden hammer** — every problem looks like a nail for your favorite pattern (Singleton, microservices, event sourcing). Patterns are tools; misapplication adds ceremony without reducing change cost.

---

### When to Use / When NOT to Use

| Situation | Golden Hammer? | Why |
| :--- | :---: | :--- |
| Singleton for every shared bean | Yes | Use DI scope |
| Strategy for one never-changing algorithm | Yes | YAGNI |
| Appropriate State for order lifecycle | No | Legitimate fit |

---

### Structure (Class Diagram)

```mermaid
flowchart TD
    P[Problem] --> S{{Always Strategy?}}
    S -->|Yes| GH[Golden Hammer]
    S -->|No| DT[Decision tree]
```

---

### Interaction Flow

```mermaid
flowchart LR
    T[Team] --> Pat[Favorite Pattern]
    Pat --> All[Every ticket]
```

---

### Implementation

Use [pattern decision tree]({BASE}/09-pattern-selection-guide/pattern-decision-tree/) and [when-to-use guide]({BASE}/09-pattern-selection-guide/when-to-use-which-pattern/).

---

### Trade-offs & Operational Realities

| Cost of misuse | Example |
| :--- | :--- |
| **Test burden** | Mocking unnecessary factories |
| **Onboarding** | Juniors learn patterns not domain |

---

### Junior Mistakes

- Naming classes `XStrategy` without swappable algorithms.
- Singleton for testability destruction.

---

### Senior Questions

1. How do architects review for pattern fit vs fashion?
2. What ADR documents pattern rejection?

---

### Revision Cheat Sheet

- **Ask:** what force does this pattern solve?
- **Read:** [Pattern selection guide]({BASE}/09-pattern-selection-guide/)

---

### See Also

- [Singleton]({BASE}/02-creational-patterns/singleton-pattern/)
- [When to use which pattern]({BASE}/09-pattern-selection-guide/when-to-use-which-pattern/)
""",
    )


def pattern_selection() -> None:
    write_simple(
        "09-pattern-selection-guide/when-to-use-which-pattern.md",
        f"""# When To Use Which Pattern

Architect-level pattern selection by **design force** — not by name recognition.

## By Design Force

| Force | Consider | Canonical page |
| :--- | :--- | :--- |
| Hide which single product is created | Factory Method | [Factory Method]({BASE}/02-creational-patterns/factory-method-pattern/) |
| Consistent product family | Abstract Factory | [Abstract Factory]({BASE}/02-creational-patterns/abstract-factory-pattern/) |
| Complex object, many optional steps | Builder | [Builder]({BASE}/02-creational-patterns/builder-pattern/) |
| Expensive clone vs rebuild | Prototype | [Prototype]({BASE}/02-creational-patterns/prototype-pattern/) |
| Exactly one coordinated instance | Singleton (careful) | [Singleton]({BASE}/02-creational-patterns/singleton-pattern/) |
| Legacy API mismatch | Adapter | [Adapter]({BASE}/03-structural-patterns/adapter-pattern/) |
| Add behavior without subclassing | Decorator | [Decorator]({BASE}/03-structural-patterns/decorator-pattern/) |
| Simplified subsystem API | Facade | [Facade]({BASE}/03-structural-patterns/facade-pattern/) |
| Control access / lazy load | Proxy | [Proxy]({BASE}/03-structural-patterns/proxy-pattern/) |
| Tree structures | Composite | [Composite]({BASE}/03-structural-patterns/composite-pattern/) |
| Algorithm varies at runtime | Strategy | [Strategy]({BASE}/04-behavioral-patterns/strategy-pattern/) |
| Behavior varies with lifecycle | State | [State]({BASE}/04-behavioral-patterns/state-pattern/) |
| Notify many dependents | Observer | [Observer]({BASE}/04-behavioral-patterns/observer-pattern/) |
| Encapsulate request + undo | Command | [Command]({BASE}/04-behavioral-patterns/command-pattern/) |

## When NOT To Use Patterns

- One implementation, no variation → plain constructor.
- Pattern name without force → see [Golden Hammer]({BASE}/07-anti-patterns/golden-hammer/).

## See Also

- [Pattern decision tree]({BASE}/09-pattern-selection-guide/pattern-decision-tree/)
- [Pattern comparisons]({BASE}/05-pattern-comparisons/)
""",
        title="When To Use Which Pattern",
        desc="Design-force matrix for GoF and architectural pattern selection.",
        short="When To Use",
        mod=9,
        mod_title="Pattern Selection Guide",
        ref="9.1",
        weight=901,
    )
    write_simple(
        "09-pattern-selection-guide/pattern-decision-tree.md",
        f"""# Pattern Decision Tree

Use this tree in design reviews and interviews. Full explanations live on linked canonical pages only.

```mermaid
flowchart TD
    Start([Design problem]) --> Create{{Object creation?}}
    Create -->|Yes| Family{{Related product family?}}
    Family -->|Yes| AF[Abstract Factory]
    Family -->|No| Complex{{Many optional steps?}}
    Complex -->|Yes| B[Builder]
    Complex -->|No| FM[Factory Method]
    Create -->|No| Behavior{{Behavior varies?}}
    Behavior -->|Yes| Lifecycle{{Lifecycle phases?}}
    Lifecycle -->|Yes| ST[State]
    Lifecycle -->|No| STR[Strategy]
    Behavior -->|No| Structure{{Structure / wrapping?}}
    Structure -->|Yes| Wrap{{Intent?}}
    Wrap -->|Add features| DEC[Decorator]
    Wrap -->|Control access| PRX[Proxy]
    Wrap -->|Split abstraction| BR[Bridge]
    Wrap -->|Legacy API| AD[Adapter]
```

## Creational Sub-tree

| Question | Pattern |
| :--- | :--- |
| One product, which impl? | [Factory Method]({BASE}/02-creational-patterns/factory-method-pattern/) |
| Consistent family? | [Abstract Factory]({BASE}/02-creational-patterns/abstract-factory-pattern/) |
| Stepwise build + validation? | [Builder]({BASE}/02-creational-patterns/builder-pattern/) |

## Comparison Shortcuts

- Factory vs Builder → [comparison]({BASE}/05-pattern-comparisons/factory-vs-builder/)
- Strategy vs State → [comparison]({BASE}/05-pattern-comparisons/strategy-vs-state/)
- Decorator vs Proxy vs Bridge → [comparison]({BASE}/05-pattern-comparisons/decorator-vs-proxy-vs-bridge/)

## See Also

- [When to use which pattern]({BASE}/09-pattern-selection-guide/when-to-use-which-pattern/)
- [Anti-patterns]({BASE}/07-anti-patterns/)
""",
        title="Pattern Decision Tree",
        desc="Mermaid decision trees for creational, behavioral, and structural pattern selection.",
        short="Decision Tree",
        mod=9,
        mod_title="Pattern Selection Guide",
        ref="9.2",
        weight=902,
    )


def lld_ride_sharing() -> None:
    body = f"""### Problem & Intent

Design a **ride-sharing** system: riders request trips, drivers accept, fares compute with surge pricing, and trip state progresses from requested → in-progress → completed. Forces: **matching**, **pricing strategy**, **state machine**, concurrency on driver availability.

---

### When to Use / When NOT to Use

| Situation | Include? | Why |
| :--- | :---: | :--- |
| Nearest-driver matching | Yes | Core dispatch |
| Surge by demand zone | Yes | [Strategy]({BASE}/04-behavioral-patterns/strategy-pattern/) |
| Multi-city fleet ops | Scope out | Needs distributed index |
| Real-time GPS streaming | Mention | Out of in-memory LLD scope |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class RideService {{
        +requestRide(rider, pickup, dropoff) Ride
        +acceptRide(driver, rideId)
        +completeRide(rideId)
    }}
    class Ride {{
        -RideStatus status
        +transition(event)
    }}
    class DriverPool {{
        +findNearest(location) Driver
    }}
    class FareCalculator {{
        -PricingStrategy strategy
    }}
    RideService --> Ride
    RideService --> DriverPool
    RideService --> FareCalculator
    FareCalculator --> PricingStrategy
```

---

### Interaction Flow

```mermaid
sequenceDiagram
    participant R as Rider
    participant RS as RideService
    participant D as DriverPool
    participant Ride
    R->>RS: requestRide()
    RS->>D: findNearest()
    D-->>RS: Driver
    RS->>Ride: create REQUESTED
    RS-->>R: rideId + ETA
```

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
public enum RideStatus {{ REQUESTED, ACCEPTED, IN_PROGRESS, COMPLETED, CANCELLED }}

public final class Ride {{
    private RideStatus status = RideStatus.REQUESTED;
    public void accept() {{
        if (status != RideStatus.REQUESTED) throw new IllegalStateException();
        status = RideStatus.ACCEPTED;
    }}
}}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
type RideStatus int
const (
    Requested RideStatus = iota
    Accepted
    InProgress
    Completed
)

type Ride struct {{
    status RideStatus
}}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

### Trade-offs & Operational Realities

| Decision | Tradeoff |
| :--- | :--- |
| In-memory driver pool | Fast LLD; production needs geo index |
| Strategy for surge | Extensible; avoid if single flat rate |

---

### Junior Mistakes

- God `RideManager` with matching + payment + notification.
- No explicit trip state — boolean flags everywhere.

---

### Senior Questions

1. How do you handle driver race on accept?
2. Where do domain events vs integration events go?

---

### Revision Cheat Sheet

- **Entities:** Rider, Driver, Ride.
- **Patterns:** State (trip), Strategy (fare), SRP services.

---

### See Also

- [State Pattern]({BASE}/04-behavioral-patterns/state-pattern/)
- [Strategy Pattern]({BASE}/04-behavioral-patterns/strategy-pattern/)
- [Parking Lot LLD]({BASE}/08-lld-case-studies/parking-lot/)
"""
    write_simple(
        "08-lld-case-studies/ride-sharing-system.md",
        body,
        title="Ride Sharing System LLD",
        desc="Ride matching, surge pricing, and trip lifecycle — State and Strategy applied.",
        short="Ride Sharing",
        mod=8,
        mod_title="LLD Case Studies",
        ref="8.5",
        weight=805,
    )


def lld_library() -> None:
    body = f"""### Problem & Intent

**Library management:** members borrow and return books, reservations queue for unavailable copies, fines accrue on late return. Forces: **inventory per copy**, **loan lifecycle**, **fine policy**.

---

### When to Use / When NOT to Use

| Situation | Include? | Why |
| :--- | :---: | :--- |
| Multiple copies per title | Yes | Copy vs Book separation |
| Reservation queue | Yes | Fairness rules |
| Inter-library loan network | Scope out | Federation complexity |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class LibraryService {{
        +borrow(member, bookId) Loan
        +returnBook(loanId)
        +reserve(member, bookId)
    }}
    class Book {{
        +isbn
        +title
    }}
    class BookCopy {{
        +copyId
        +available
    }}
    class Loan {{
        +dueDate
        +return()
    }}
    class Member
    Book "1" --> "*" BookCopy
    LibraryService --> Loan
```

---

### Interaction Flow

```mermaid
sequenceDiagram
    participant M as Member
    participant L as LibraryService
    participant C as BookCopy
    M->>L: borrow(bookId)
    L->>C: mark unavailable
    L-->>M: Loan + dueDate
```

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
public record Loan(String id, String memberId, String copyId, LocalDate dueDate) {{
    public Money fineOn(LocalDate returnDate, FinePolicy policy) {{
        return policy.calculate(dueDate, returnDate);
    }}
}}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
type Loan struct {{
    ID, MemberID, CopyID string
    DueDate            time.Time
}}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

### Trade-offs & Operational Realities

| Decision | Tradeoff |
| :--- | :--- |
| Fine as Strategy | Flexible policies |
| Reservation FIFO | Simple; priority needs heap |

---

### Junior Mistakes

- Single `Book` entity with `available: boolean` for 50 copies.
- Fines calculated in controller.

---

### Senior Questions

1. How do two members reserve the last copy?
2. State vs Strategy for loan status?

---

### Revision Cheat Sheet

- **Book** (title) vs **BookCopy** (inventory unit).
- **Loan** owns return + fine calculation hook.

---

### See Also

- [State Pattern]({BASE}/04-behavioral-patterns/state-pattern/)
- [Library fine anti-patterns]({BASE}/07-anti-patterns/anemic-domain-model/)
"""
    write_simple(
        "08-lld-case-studies/library-management-system.md",
        body,
        title="Library Management System LLD",
        desc="Books, copies, loans, reservations, and fines — inventory and lifecycle design.",
        short="Library LLD",
        mod=8,
        mod_title="LLD Case Studies",
        ref="8.6",
        weight=806,
    )


def interview_guide() -> None:
    from design_patterns_questions_data import QUESTIONS

    assert len(QUESTIONS) == 150
    rows = "\n".join(
        f'| {i} | {q} | {d} | {l} | {t} | [{path.split("/")[-1].replace("-", " ").title()}]({BASE}/{path}/) |'
        for i, (q, d, l, t, path) in enumerate(QUESTIONS, 1)
    )
    write_simple(
        "10-interview-guide/top-150-design-pattern-questions.md",
        f"""Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. **Questions only** — each **Deep Dive** links to the canonical handbook page.

**Distribution:** Pattern Tradeoffs 40 · Pattern Comparisons 30 · SOLID 25 · LLD Design 25 · Architecture 15 · Anti-Patterns 15

| # | Question | Difficulty | Level | Topic | Deep Dive |
|---|----------|------------|--------|-------|-----------|
{rows}
""",
        title="Top 150 Design Pattern Questions",
        desc="150 production-oriented design pattern and LLD interview questions.",
        short="Top 150",
        mod=10,
        mod_title="Interview Guide",
        ref="10.1",
        weight=1001,
        interview=True,
    )

    def subset(topic: str, title: str, ref: str, weight: int, limit: int = 25) -> list[str]:
        return [q for q, _, _, t, _ in QUESTIONS if t == topic][:limit]

    trade = subset("Pattern Tradeoffs", "Pattern Tradeoffs", "10.2", 1002, 40)
    comp = subset("Pattern Comparison", "Pattern Comparisons", "10.3", 1003, 30)
    solid = subset("SOLID", "SOLID Principles", "10.4", 1004, 25)
    lld = subset("LLD Design", "LLD Design", "10.5", 1005, 25)
    arch = [q for q, _, l, t, _ in QUESTIONS if t == "Architecture" or (t == "Pattern Tradeoffs" and l == "Architect")][:25]
    architect_qs = [q for q, _, l, _, _ in QUESTIONS if l == "Architect"][:40]

    for fname, title, ref, weight, qs in [
        ("architect-pattern-questions.md", "Architect Pattern Questions", "10.2", 1002, architect_qs),
        ("pattern-comparison-questions.md", "Pattern Comparison Questions", "10.3", 1003, comp),
        ("solid-principles-questions.md", "SOLID Principles Questions", "10.4", 1004, solid),
        ("lld-questions.md", "LLD Design Questions", "10.5", 1005, lld),
    ]:
        body = (
            f"Questions only — no answers. Sourced from [Top 150]({BASE}/10-interview-guide/top-150-design-pattern-questions/).\n\n"
            f"# {title}\n\n"
            + "\n".join(f"{i}. {q}" for i, q in enumerate(qs, 1))
        )
        write_simple(
            f"10-interview-guide/{fname}",
            body,
            title=title,
            desc=f"{title} — interview question bank.",
            short=title.split()[0],
            mod=10,
            mod_title="Interview Guide",
            ref=ref,
            weight=weight,
            interview=True,
        )


def learning_paths() -> None:
    write_simple(
        "11-learning-paths/design-patterns-senior-engineer-path.md",
        f"""# Senior Engineer Path

**Audience:** Senior engineers (5–8 years) sharpening LLD and GoF pattern fluency.  
**Time:** ~8–10 hours.  
**Outcome:** Select patterns by force, implement with Java/Go, pass LLD screens.

## Reading Order

1. [SOLID Principles]({BASE}/01-solid-principles/) — SRP through DIP
2. [SOLID Composition Guide]({BASE}/01-solid-principles/solid-principles-composition-guide/)
3. [Creational]({BASE}/02-creational-patterns/) + [Structural]({BASE}/03-structural-patterns/) — skim all
4. [Behavioral]({BASE}/04-behavioral-patterns/) — focus Strategy, Observer, State, Command
5. [Pattern Comparisons]({BASE}/05-pattern-comparisons/) — all six pages
6. [Pattern Selection]({BASE}/09-pattern-selection-guide/)
7. [Parking Lot]({BASE}/08-lld-case-studies/parking-lot/) + [Rate Limiter]({BASE}/08-lld-case-studies/rate-limiter/)

## Practice

- [Top 150]({BASE}/10-interview-guide/top-150-design-pattern-questions/) — Senior Engineer rows
- [SOLID Questions]({BASE}/10-interview-guide/solid-principles-questions/)

## See Also

- [Interview Revision Path]({BASE}/11-learning-paths/design-patterns-interview-revision-path/)
""",
        title="Senior Engineer Path",
        desc="GoF patterns, SOLID, comparisons, and core LLD case studies.",
        short="Senior Path",
        mod=11,
        mod_title="Learning Paths",
        ref="11.1",
        weight=1101,
        interview=True,
    )
    write_simple(
        "11-learning-paths/design-patterns-lead-path.md",
        f"""# Technical Lead Path

**Goal:** Lead design reviews — tradeoffs, anti-patterns, architecture boundaries.

1. [Architectural Principles]({BASE}/06-architectural-principles/) — DI, DDD, layering
2. [Anti-Patterns]({BASE}/07-anti-patterns/) — all five
3. [LLD Case Studies]({BASE}/08-lld-case-studies/) — elevator, notification, ride sharing
4. [Pattern Comparison Questions]({BASE}/10-interview-guide/pattern-comparison-questions/)
5. [Repository & Unit of Work]({BASE}/06-architectural-principles/repository-and-unit-of-work/)
""",
        title="Technical Lead Path",
        desc="Architecture principles, anti-patterns, and advanced LLD for tech leads.",
        short="Lead Path",
        mod=11,
        mod_title="Learning Paths",
        ref="11.2",
        weight=1102,
        interview=True,
    )
    write_simple(
        "11-learning-paths/design-patterns-architect-path.md",
        f"""# Architect Path

**Goal:** ADR-level pattern selection, tradeoffs, and platform consistency.

1. [Pattern Selection Guide]({BASE}/09-pattern-selection-guide/)
2. [All Pattern Comparisons]({BASE}/05-pattern-comparisons/)
3. [Layered vs Hexagonal]({BASE}/06-architectural-principles/layered-vs-hexagonal-architecture/)
4. [DDD Building Blocks]({BASE}/06-architectural-principles/domain-driven-design-building-blocks/)
5. [Anti-Patterns]({BASE}/07-anti-patterns/golden-hammer/) + [God Object]({BASE}/07-anti-patterns/god-object/)
6. [Architect Pattern Questions]({BASE}/10-interview-guide/architect-pattern-questions/)
""",
        title="Architect Path",
        desc="Pattern ADRs, architectural principles, and architect interview probes.",
        short="Architect Path",
        mod=11,
        mod_title="Learning Paths",
        ref="11.3",
        weight=1103,
        interview=True,
    )
    write_simple(
        "11-learning-paths/design-patterns-interview-revision-path.md",
        f"""# Interview Revision Path

**Goal:** 48-hour cram before senior/architect design interviews.

| Block | Time | Focus |
| :--- | :--- | :--- |
| **Block 1** | 2h | [SOLID]({BASE}/01-solid-principles/) + [composition guide]({BASE}/01-solid-principles/solid-principles-composition-guide/) |
| **Block 2** | 2h | [Comparisons]({BASE}/05-pattern-comparisons/) — factory, strategy, decorator triads |
| **Block 3** | 2h | [Parking Lot]({BASE}/08-lld-case-studies/parking-lot/) · [Rate Limiter]({BASE}/08-lld-case-studies/rate-limiter/) · [Elevator]({BASE}/08-lld-case-studies/elevator-control-system/) |
| **Block 4** | 1h | [Anti-Patterns]({BASE}/07-anti-patterns/) index |
| **Block 5** | 2h | [Top 150]({BASE}/10-interview-guide/top-150-design-pattern-questions/) skim |
| **Block 6** | 1h | [Decision tree]({BASE}/09-pattern-selection-guide/pattern-decision-tree/) |

Pair with [Architect Questions]({BASE}/10-interview-guide/architect-pattern-questions/).
""",
        title="Interview Revision Path",
        desc="48-hour design pattern and LLD interview cram schedule.",
        short="Revision Path",
        mod=11,
        mod_title="Learning Paths",
        ref="11.4",
        weight=1104,
        interview=True,
    )


def handbook_index() -> None:
    write_simple(
        "_index.md",
        f"""# Design Principles, Patterns & LLD Handbook

Structured curriculum from **SOLID** foundations through **GoF patterns**, **architectural principles**, **anti-patterns**, and **applied LLD case studies** — with Java and Go implementations.

## Modules

| # | Module | Focus |
| :---: | :--- | :--- |
| 1 | [SOLID Principles]({BASE}/01-solid-principles/) | SRP, OCP, LSP, ISP, DIP + composition guide |
| 2 | [Creational Patterns]({BASE}/02-creational-patterns/) | Factory, Builder, Singleton, Prototype |
| 3 | [Structural Patterns]({BASE}/03-structural-patterns/) | Adapter, Decorator, Proxy, Composite, … |
| 4 | [Behavioral Patterns]({BASE}/04-behavioral-patterns/) | Strategy, Observer, State, Command, … |
| 5 | [Pattern Comparisons]({BASE}/05-pattern-comparisons/) | Disambiguation guides |
| 6 | [Architectural Principles]({BASE}/06-architectural-principles/) | DI, DDD, layering, repositories |
| 7 | [Anti-Patterns]({BASE}/07-anti-patterns/) | God object, anemic domain, golden hammer |
| 8 | [LLD Case Studies]({BASE}/08-lld-case-studies/) | Parking lot, elevator, rate limiter, … |
| 9 | [Pattern Selection]({BASE}/09-pattern-selection-guide/) | When to use which pattern |
| 10 | [Interview Guide]({BASE}/10-interview-guide/) | Top 150 + role-specific banks |
| 11 | [Learning Paths]({BASE}/11-learning-paths/) | Senior, lead, architect, revision |

## Quick Start

| Goal | Start here |
| :--- | :--- |
| **Interview cram** | [Interview Revision Path]({BASE}/11-learning-paths/design-patterns-interview-revision-path/) |
| **Which pattern?** | [Pattern decision tree]({BASE}/09-pattern-selection-guide/pattern-decision-tree/) |
| **LLD practice** | [Parking Lot]({BASE}/08-lld-case-studies/parking-lot/) |
| **SOLID refresh** | [SRP]({BASE}/01-solid-principles/single-responsibility-principle/) |

## Learning Paths

| Path | Audience |
| :--- | :--- |
| [Senior Engineer]({BASE}/11-learning-paths/design-patterns-senior-engineer-path/) | GoF + core LLD |
| [Technical Lead]({BASE}/11-learning-paths/design-patterns-lead-path/) | Architecture + anti-patterns |
| [Architect]({BASE}/11-learning-paths/design-patterns-architect-path/) | Tradeoffs + ADRs |
| [Interview Revision]({BASE}/11-learning-paths/design-patterns-interview-revision-path/) | 48-hour cram |
""",
        title="Design Patterns",
        desc="SOLID principles, GoF design patterns, architecture patterns, and applied LLD case studies.",
        short="Design Patterns",
        mod=0,
        mod_title="Design Patterns Handbook",
        ref="0",
        weight=0,
    )


def write_yaml() -> None:
    modules_yaml = """# Design Patterns — module index (canonical structure).
modules:
  - id: 1
    focus: "SOLID Principles"
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
"""
    order_yaml = """topics:
"""
    for line in modules_yaml.splitlines():
        m = re.match(r"\s+-\s+([\w-]+/[\w-]+)", line)
        if m:
            order_yaml += f"  - {m.group(1)}\n"

    (DATA / "design_patterns_modules.yaml").write_text(modules_yaml, encoding="utf-8")
    (DATA / "design_patterns_order.yaml").write_text(order_yaml, encoding="utf-8")


def cleanup_flat_files() -> None:
    for old_slug in SLUG_TO_NEW:
        p = DP / f"{old_slug}.md"
        if p.exists():
            p.unlink()


def main() -> None:
    section_indexes()
    move_all_existing()
    comparison_factory_vs_builder()
    comparison_factory_vs_abstract()
    comparison_strategy_vs_state()
    comparison_composition_vs_inheritance()
    comparison_interface_vs_abstract()
    anti_patterns()
    pattern_selection()
    lld_ride_sharing()
    lld_library()
    interview_guide()
    learning_paths()
    handbook_index()
    write_yaml()
    cleanup_flat_files()
    print("Design Patterns Phase B complete.")


if __name__ == "__main__":
    main()
