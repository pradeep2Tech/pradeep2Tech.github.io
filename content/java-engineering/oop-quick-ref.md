---
title: "OOP Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Classes, inheritance, polymorphism, encapsulation, records, sealed types."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "OOP"
module: 2
moduleTitle: "OOP"
sectionRef: "2.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Composition over inheritance for reuse; inheritance for true subtype polymorphism.
- `final` class/method blocks extension; use when invariants must hold.
- Records (16+): immutable data carriers; not a drop-in for JPA entities.
- Sealed (17+): controlled hierarchy — pairs with exhaustive pattern switches.

---

## Reference Tables

| Mechanism | Compile-time | Runtime |
| :--- | :--- | :--- |
| Overloading | Resolved by static type + signature | — |
| Overriding | — | Virtual dispatch via vtable/itable |
| Hiding (static) | Resolved statically | No polymorphism |
| `default` interface | — | `invokeinterface` + default method table |

| Type | Fields | Inheritance | Best for |
| :--- | :--- | :--- | :--- |
| `class` | Any | Single extends | Mutable domain objects |
| `record` | `final` components | Implements only | DTOs, value objects |
| `sealed class` | Any | Permitted subs only | Closed ADTs |
| `enum` | Fixed set | `Enum` only | Constants + behavior |
| `interface` | `public static final` | Multiple | Contracts, traits |

| Modifier | Class | Method | Field |
| :--- | :---: | :---: | :---: |
| `public` | ✓ | ✓ | ✓ |
| `protected` | — | ✓ subclass | — |
| package-private | default | default | default |
| `private` | — | ✓ | ✓ |

---

## Snippets

```java
public record Point(int x, int y) {
    public Point { if (x < 0 || y < 0) throw new IllegalArgumentException(); }
}

public sealed interface Shape permits Circle, Rectangle {}
public final class Circle implements Shape { /* ... */ }
```

---

## Internals & Gotchas

- Inner classes hold implicit outer ref — leak risk in long-lived callbacks.
- Static nested: no outer ref — prefer for helpers.
- `Object` header: mark word + klass pointer (64-bit compressed oops typical).
- Records: synthetic accessors, canonical ctor, no setters.

---

## Production Notes

- Don't expose mutable internals — defensive copy on getters.
- Liskov: subtypes must not strengthen preconditions or weaken postconditions.
- Avoid deep inheritance trees >2 levels in business code.

---

## Interview Probes


{< interview-answer >}
**Q:** Record vs class?

**A:** Record = transparent immutable aggregate with generated equals/hashCode/toString. No inheritance except interfaces. Not for entities needing identity lifecycle or lazy fields.
{< /interview-answer >}

{< interview-answer >}
**Q:** Sealed types benefit?

**A:** Compiler-checked exhaustiveness in switches; documents allowed subtypes; enables safer domain modeling without visitor boilerplate for every extension.
{< /interview-answer >}

---

## See Also

- [Previous: Strings & Enums](/java-engineering/strings-and-enums-ref/)
- [Next: Object Contract](/java-engineering/interfaces-and-object-contract/)
- [Java Engineering Handbook Index](/java-engineering/)
