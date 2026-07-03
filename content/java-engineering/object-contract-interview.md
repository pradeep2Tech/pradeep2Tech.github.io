---
title: "Object Contract Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "equals, hashCode, toString, Comparable, and collection contract."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Object Contract"
module: 1
moduleTitle: "Language Fundamentals"
sectionRef: "1.6"
ShowToc: true
interviewHandbook: true
aliases:
  - interfaces-and-object-contract
---

## equals/hashCode contract?

### Short Answer

If equal objects must have same hashCode; reflexive, symmetric, transitive, consistent.

### Detailed Explanation

Breaking contract breaks `HashMap`/`HashSet` — objects become unfindable. Use `Objects.equals`/`Objects.hash`. For records, generated automatically.

### Internal Working

HashMap bin lookup uses hash then equals.

### Production Notes

Don't use mutable fields in equals/hashCode for map keys.

### Follow-up Questions

- What fields to include in equals?
- IDE generate pitfalls?

---
## Comparable vs Comparator?

### Short Answer

Comparable: natural order inside type (`compareTo`). Comparator: external, multiple orderings, lambdas.

### Detailed Explanation

`TreeSet`/`TreeMap` need Comparable or provided Comparator. `Comparator.comparing` chains with `thenComparing`.

---
