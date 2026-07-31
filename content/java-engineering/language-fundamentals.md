---
title: "Core Java Interview Refresh"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "One-page refresh of Java language decisions for experienced engineers."
tags: ["java", "interview", "cheatsheet"]
categories: ["Java Engineering Handbook"]
shortTitle: "Core Java"
module: 1
moduleTitle: "Core Java Refresh"
sectionRef: "1.1"
cheatSheet: true
aliases: ["core-java-quick-ref"]
---

## At a Glance

- Answer with **when and why**, not textbook definitions.
- Prefer composition, immutability, explicit contracts, and simple failure handling.
- Know language features well enough to review production code; skip compiler/JVM internals unless asked.

---

## Language and Design Decisions

| Topic | Interview answer | Production judgment |
| :--- | :--- | :--- |
| Interface vs abstract class | Interface defines capability; abstract class shares state/implementation | Prefer interfaces at boundaries; inherit only for a stable IS-A model |
| Composition vs inheritance | Composition delegates and changes independently | Default to composition; inheritance couples lifecycle and behavior |
| Record vs class | Record is a transparent immutable data carrier | Use for DTOs/value responses; use class when identity or mutable lifecycle matters |
| Sealed hierarchy | Restricts valid subtypes | Useful for closed domain outcomes and exhaustive pattern matching |
| `final` | Prevents reassignment, override, or inheritance | A final reference does not make its object immutable |
| Pass-by-value | Java copies primitive values and object references | A method can mutate the referenced object, not replace the caller's reference |
| Immutable type | Final state, no mutators, defensive copies | Safer sharing, caching, and concurrent use |

## Contracts You Must Recall

| Contract | Rule | Typical failure |
| :--- | :--- | :--- |
| `equals` / `hashCode` | Equal objects must have equal hashes | Lost lookup after mutating a map key |
| `Comparable` / `Comparator` | Natural order vs external ordering | Ordering inconsistent with equality |
| Checked exception | Caller can reasonably recover | Leaking infrastructure exceptions through domain APIs |
| Unchecked exception | Programming error or unrecoverable operation | Catching `Exception` and hiding the cause |
| Try-with-resources | Closes in reverse declaration order | Missing suppressed exception during diagnosis |

## Generics, Lambdas, and Streams

| Question | Quick answer |
| :--- | :--- |
| `? extends T` | Producer: read values as `T`; do not add |
| `? super T` | Consumer: safely add `T`; reads are `Object` |
| Why type erasure matters | Generic type arguments are mostly unavailable at runtime |
| `map` vs `flatMap` | Transform one value vs transform and flatten nested values |
| `reduce` vs `collect` | Immutable associative reduction vs mutable accumulation |
| `Optional` | Good return type for absence; avoid fields, parameters, and `get()` |
| Parallel stream | Use only for measured, CPU-bound, independent, sufficiently large work |

## Quick Gotchas

- Never use mutable business fields in a `HashMap` key.
- Do not return `null` collections; return an empty collection.
- Do not use exceptions for normal control flow.
- Stream side effects make correctness and parallel execution harder.
- Defensive copying must happen on both input and output for mutable fields.

## Answer Frame

> “I would choose **X** because of **this constraint**. The trade-off is **Y**. In production I would guard against **Z**.”

---

## See Also

[Collections →](/java-engineering/collection-selection-matrix/) · [Interview Sprint](/java-engineering/top-100-java-interview-questions/)
