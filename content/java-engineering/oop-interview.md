---
title: "OOP Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Inheritance, composition, records, sealed classes, overriding vs overloading."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "OOP"
module: 1
moduleTitle: "Language Fundamentals"
sectionRef: "1.3"
ShowToc: true
interviewHandbook: true
aliases:
  - oop-quick-ref
---

## Composition over inheritance — when to inherit?

### Short Answer

Prefer composition for reuse; inherit for true subtype polymorphism (Liskov).

### Detailed Explanation

Inheritance couples subclasses to parent implementation — fragile base class problem. Use composition + delegation for behavior reuse. Inherit when `is-a` relationship is stable and you need virtual dispatch (`@Override`).

### Follow-up Questions

- What is the fragile base class problem?

---
## Overloading vs overriding?

### Short Answer

Overloading: same name, different signatures — resolved at compile time. Overriding: subclass replaces instance method — runtime dispatch.

### Detailed Explanation

Static methods hide, not override. `@Override` catches signature mistakes. `private`/`final` methods cannot be overridden.

### Follow-up Questions

- Can you override a static method?

---
## Record vs class — when not to use a record?

### Short Answer

Records are immutable data carriers — not for JPA entities or types needing inheritance.

### Detailed Explanation

Records provide canonical constructor, equals/hashCode/toString. They are `final` with final fields. Poor fit for JPA lazy proxies, mutable domain models, or types requiring inheritance hierarchies.

### Follow-up Questions

- Record vs Lombok `@Value`?

---
## Sealed classes purpose?

### Short Answer

Closed hierarchies enabling exhaustive pattern matching and controlled extension.

### Detailed Explanation

Sealed types list permitted subclasses (`permits`). Compiler enforces exhaustiveness in switches. Models ADTs: `sealed interface Result permits Ok, Err`.

### Follow-up Questions

- Sealed vs final class?

---
