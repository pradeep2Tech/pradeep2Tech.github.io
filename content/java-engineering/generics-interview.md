---
title: "Generics Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "PECS, erasure, bounds, and common compiler errors."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Generics"
module: 1
moduleTitle: "Language Fundamentals"
sectionRef: "1.4"
interviewHandbook: true
aliases:
  - generics-quick-ref
---

## What is PECS?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Producer Extends, Consumer Super — wildcard direction for API flexibility.

### Detailed Explanation

If you read from a structure (producer), use `? extends T`. If you write into it (consumer), use `? super T`. `Collections.copy(List<? super T> dest, List<? extends T> src)` is the canonical example.

### Interview Questions

1. Why can't you add to `List<? extends Number>`?

### Follow-up Questions

- Why can't you add to `List<? extends Number>`?

---
## What is type erasure?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Generic type parameters are erased at runtime; bytecode uses raw types and casts.

### Detailed Explanation

`List<String>` becomes `List` at runtime. You cannot `new T()`, `T[]`, or `instanceof List<String>`. Bridge methods preserve polymorphism for generic overrides.

### Interview Questions

1. What is heap pollution?
2. How does `List.class` work at runtime?

### Follow-up Questions

- What is heap pollution?
- How does `List.class` work at runtime?

---
## Why no `List<int>`?

**Difficulty:** Easy · **Time:** 30 sec

### Short Answer

Generics require reference types; primitives cannot be type arguments.

### Detailed Explanation

Use `IntStream`, primitive arrays, or libraries like fastutil for compact numeric storage.

---
