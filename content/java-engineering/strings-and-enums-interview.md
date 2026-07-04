---
title: "Strings & Enums Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "String immutability, interning, builders, text blocks, and enum patterns."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Strings & Enums"
module: 1
moduleTitle: "Language Fundamentals"
sectionRef: "1.2"
interviewHandbook: true
aliases:
  - strings-and-enums-ref
---

## Why is String immutable?

**Difficulty:** Easy · **Time:** 1 min

### Short Answer

Thread safety, security, hash caching, and safe sharing as map keys.

### Detailed Explanation

Immutable strings can be shared across threads without synchronization. Security: credential/URL strings cannot be mutated after validation. `hashCode()` is cached after first compute. Trade-off: concatenation creates new objects — use `StringBuilder` in loops.

### Internal Working

OpenJDK may use compact strings (byte-backed LATIN1) internally since Java 9.

### Production Notes

Never build SQL by concatenation — use prepared statements.

### Common Mistakes

Assuming `substring` always copies (modern JDKs may share backing).

### Interview Questions

1. String pool vs `intern()`?
2. Text blocks (15+) use cases?

### Follow-up Questions

- String pool vs `intern()`?
- Text blocks (15+) use cases?

---
## StringBuilder vs String concat in loops?

**Difficulty:** Easy · **Time:** 30 sec

### Short Answer

Concat in loop is O(n²); StringBuilder is O(n) total.

### Detailed Explanation

Each `+` in a loop may create intermediate String objects. Compiler optimizes few-operand concat but not arbitrary loops. `StringBuilder` (not thread-safe) for single-thread; `StringBuffer` only for legacy.

### Interview Questions

1. When is `+` concat acceptable?

### Follow-up Questions

- When is `+` concat acceptable?

---
## Enum vs int constants — why enum?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Type safety, singleton semantics, `EnumSet`/`EnumMap`, serialization by name.

### Detailed Explanation

Enums are classes with fixed instances — compiler checks exhaustiveness in switches. `EnumSet` is bit-vector backed. Persist `name()`, never `ordinal()`. Strategy enum pattern embeds behavior per constant.

### Interview Questions

1. When use `EnumSet` over `HashSet<Day>`?

### Follow-up Questions

- When use `EnumSet` over `HashSet<Day>`?

---
