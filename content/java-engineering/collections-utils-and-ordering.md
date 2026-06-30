---
title: "Collections Utils & Ordering"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Collections/Arrays utilities, Comparable vs Comparator, unmodifiable views."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Utils & Ordering"
module: 3
moduleTitle: "Collections"
sectionRef: "3.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `Collections` — algorithms, wrappers, empty/singleton, synchronized views.
- `Arrays` — sort, binarySearch, parallel prefix, stream bridge.
- `Comparable` natural order vs `Comparator` pluggable order.
- Unmodifiable wrappers throw on mutation — not immutable copies.

---

## Reference Tables

| `Collections` | Note |
| :--- | :--- |
| `sort`, `reverse`, `shuffle` | In-place on `List` |
| `unmodifiableList/Map/Set` | Wrapper — delegate still mutable |
| `synchronizedList` | Every method locked — prefer concurrent types |
| `checkedList` | Runtime type check on add |
| `emptyList`, `singleton` | Shared instances |

| `Arrays` | Complexity |
| :--- | :--- |
| `sort` (primitives) | Dual-Pivot quicksort O(n log n) |
| `binarySearch` | Requires sorted O(log n) |
| `parallelSort` | ForkJoin for large arrays |
| `mismatch` | First differing index |

| Ordering | When |
| :--- | :--- |
| `Comparable` | Single natural order baked into type |
| `Comparator.comparing` | Field-based, composable, reversed |
| `Comparator.nullsFirst/Last` | Explicit null policy |

---

## Snippets

```java
List<String> ro = List.copyOf(mutable); // truly immutable snapshot
Comparator<Person> byAgeThenName = Comparator
    .comparingInt(Person::age)
    .thenComparing(Person::name, String.CASE_INSENSITIVE_ORDER);
```

---

## Internals & Gotchas

- `List.copyOf`/`Map.copyOf` (10+) — compact immutable; reject nulls.
- `Collections.sort` uses TimSort for objects — stable O(n log n).
- Binary search: `-(insertionPoint) - 1` on miss.

---

## Production Notes

- Never expose internal mutable list — return `List.copyOf` or unmodifiable wrapper with documented mutability.
- Stable sort matters for paginated UI — TimSort is stable.

---

## Interview Probes


{< interview-answer >}
**Q:** unmodifiable vs immutable?

**A:** Unmodifiable view: backing collection can still change. `List.of`/`copyOf` cannot be structurally modified.
{< /interview-answer >}

{< interview-answer >}
**Q:** PECS in comparators?

**A:** Comparators are contravariant on type for sorting mixed subtypes — usually sort `List<Employee>` with `Comparator<Employee>`, not wildcards.
{< /interview-answer >}

---

## See Also

- [Previous: Maps](/java-engineering/map-implementations-ref/)
- [Next: HashMap Internals](/java-engineering/hashmap-internals/)
- [Java Engineering Handbook Index](/java-engineering/)
