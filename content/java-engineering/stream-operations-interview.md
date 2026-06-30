---
title: "Stream Operations (Interview)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Intermediate vs terminal ops, collectors, and parallel stream traps."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Streams Interview"
module: 11
moduleTitle: "Interview Cheat Sheets"
sectionRef: "11.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Intermediate = lazy; terminal = eager trigger.
- Short-circuit: `findFirst`, `anyMatch`, `limit`.
- `reduce` vs `collect` — monoid vs mutable container.
- Parallel: split characteristics matter.

---

## Reference Tables

| Intermediate | Effect |
| :--- | :--- |
| `filter` | Predicate |
| `map` | 1:1 transform |
| `flatMap` | 1:many flatten |
| `distinct` | HashSet-backed |
| `sorted` | Materializes |
| `peek` | Debug side-effect |

| Terminal | Result |
| :--- | :--- |
| `collect` | Mutable reduction |
| `reduce` | Immutable combine |
| `count` | long |
| `min`/`max` | Optional |

| Parallel requirement | |
| :--- | :--- |
| Associative combiner | Required |
| No shared mutation | Required |
| `ORDERED` + parallel | May buffer |

---

## Snippets

```java
boolean anyExpensive = orders.stream()
    .filter(o -> o.amount() > 10_000)
    .findAny()
    .isPresent();
```

---

## Internals & Gotchas

- `Spliterator.ORDERED` preserved unless `unordered()`.
- `Collectors.toMap` needs merge function on duplicate keys.
- Primitive streams avoid `Integer` boxing.

---

## Production Notes

- Don't parallelize by default.
- Close resource-backed streams.

---

## Interview Probes


{< interview-answer >}
**Q:** Why is sorted() expensive?

**A:** Requires full input materialization to sort — not streaming sort for arbitrary pipelines.
{< /interview-answer >}

{< interview-answer >}
**Q:** peek misuse?

**A:** Debugging only — not for business logic; may not run if stream optimized away in theory — don't rely on side effects.
{< /interview-answer >}

---

## See Also

- [Previous: Collections Big-O](/java-engineering/collections-complexity/)
- [Next: Concurrent Collections](/java-engineering/concurrent-collections-interview/)
- [Java Engineering Handbook Index](/java-engineering/)
