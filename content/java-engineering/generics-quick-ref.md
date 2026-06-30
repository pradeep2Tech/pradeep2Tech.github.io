---
title: "Generics Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Type parameters, wildcards, PECS, erasure, and common compiler errors."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Generics"
module: 4
moduleTitle: "Exceptions & Generics"
sectionRef: "4.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Compile-time type safety; erased at runtime — no `new T()`.
- PECS: Producer `extends`, Consumer `super`.
- Wildcards more flexible than type params at API boundaries.
- Type erasure → bridge methods, heap pollution warnings.

---

## Reference Tables

| Syntax | Meaning |
| :--- | :--- |
| `<T>` | Type parameter |
| `<? extends T>` | Upper bounded wildcard (producer) |
| `<? super T>` | Lower bounded wildcard (consumer) |
| `<T extends Comparable<T>>` | F-bounded |

| PECS | Role | Wildcard |
| :--- | :--- | :--- |
| Producer (read) | `Collection<? extends T>` | `extends` |
| Consumer (write) | `Collection<? super T>` | `super` |

| Limitation | Workaround |
| :--- | :--- |
| `new T()` | Factory/Supplier |
| `T[]` array | `ArrayList` or `(T[]) Object[]` with care |
| `instanceof T` | `Class<T>` token |
| Primitive generics | IntStream, specialized libs |

---

## Snippets

```java
// PECS copy
void copy(List<? extends Number> src, List<? super Number> dest) {
    for (Number n : src) dest.add(n);
}

public <T> T requireNonNull(T ref, String msg) { /* ... */ }
```

---

## Internals & Gotchas

- Erasure replaces type vars with bounds or Object.
- Bridge methods preserve polymorphism after erasure.
- Reifiable types: primitives, raw classes, arrays of reifiable, wildcards with `?` only.

---

## Production Notes

- Avoid raw types in new code — `-Xlint:unchecked`.
- API returns `List<T>` not `List` — callers stay typed.
- For JSON: type tokens (`TypeReference`) with Jackson/Gson.

---

## Interview Probes


{< interview-answer >}
**Q:** Why can't `if (obj instanceof List<String>)`?

**A:** Generics erasure — runtime only knows `List`. Use `List.class` and cast with validation or pattern `List<?>`.
{< /interview-answer >}

{< interview-answer >}
**Q:** PECS example?

**A:** `Collections.sort(List<T>)` takes `List<T>`; `addAll(Collection<? extends T>)` producer read; `addAll(Collection<? super T>)` consumer write in `copy` helpers.
{< /interview-answer >}

---

## See Also

- [Previous: Exceptions](/java-engineering/exceptions-quick-ref/)
- [Next: Functional Java](/java-engineering/functional-java-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
