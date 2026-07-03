---
title: "Language Fundamentals"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Primitives, var, records, switch patterns — interview essentials for senior Java engineers."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Language Basics"
module: 1
moduleTitle: "Language Fundamentals"
sectionRef: "1.1"
ShowToc: true
interviewHandbook: true
aliases:
  - core-java-quick-ref
---

## Why prefer primitives over wrappers in hot loops?

### Short Answer

Primitives avoid heap allocation and autoboxing overhead.

### Detailed Explanation

Wrapper types (`Integer`, `Long`) are objects — each autobox may allocate on the heap and add cache pressure. In tight loops over millions of iterations, `int` arithmetic is faster and GC-friendly. Collections require generics, so use primitive-specialized libraries (fastutil, Eclipse Collections) when numeric throughput matters.

### Internal Working

Autoboxing calls `Integer.valueOf` which may hit the small-integer cache (-128 to 127) or allocate.

### Production Notes

Profile before micro-optimizing; readability wins in business logic.

### Common Mistakes

Using `Integer` in `List` where values are always non-null.

### Follow-up Questions

- What is the default value of a local `int` vs field?
- When does widening vs narrowing apply?

---
## What does `final` on a reference mean?

### Short Answer

The reference binding cannot change; the referenced object may still mutate.

### Detailed Explanation

`final User user` means you cannot reassign `user` to another object. If `User` is mutable, `user.setName()` is still legal. Immutability requires an immutable class design (records, unmodifiable fields).

### Follow-up Questions

- How do `final` fields affect JVM initialization and visibility?

---
## Arrays covariant but generics invariant — explain.

### Short Answer

`String[]` is an `Object[]` at runtime; `List<String>` is not a `List<Object>`.

### Detailed Explanation

Arrays carry runtime element type information — assigning `Object[] o = new String[1]; o[0] = 1` fails at runtime with `ArrayStoreException`. Generics erase type parameters at compile time; the compiler rejects unsafe assignments to preserve type safety without runtime checks on every read.

### Internal Working

Type erasure: `List<String>` bytecode is `List`.

### Production Notes

Don't use arrays for generic APIs — prefer `List<T>`.

### Follow-up Questions

- What is heap pollution?
- Why no `new T[]`?

---
## Pattern matching switch and exhaustiveness (17+/21+)

### Short Answer

Switch on sealed types must cover all permitted subtypes; compiler enforces exhaustiveness.

### Detailed Explanation

Sealed classes/interfaces restrict subclasses (`permits`). Combined with pattern switches, the compiler verifies all cases are handled — no default needed when exhaustive. Records destructure in case labels: `case Point(int x, int y)`.

### Follow-up Questions

- Difference between classic switch and switch expressions?

---
