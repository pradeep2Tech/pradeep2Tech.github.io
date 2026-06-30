---
title: "Streams Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Lazy pipelines, collectors, primitive streams, parallel pitfalls."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Streams"
module: 5
moduleTitle: "Functional & Streams"
sectionRef: "5.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Lazy intermediate ops; single terminal op triggers pipeline.
- Streams don't store data — source must not be modified during pipeline (except concurrent sources).
- Primitive streams (`IntStream`) avoid boxing overhead.
- Parallel streams use `ForkJoinPool.commonPool()` — default parallelism = CPUs-1.

---

## Reference Tables

| Stage | Examples | Notes |
| :--- | :--- | :--- |
| Source | `collection.stream()`, `Stream.of`, `Files.lines` | Close resource streams |
| Intermediate | `filter`, `map`, `flatMap`, `distinct`, `sorted`, `peek` | Lazy, chained |
| Terminal | `collect`, `reduce`, `forEach`, `count`, `findFirst` | Triggers execution |

| Collector | Result |
| :--- | :--- |
| `toList()` (16+) | Mutable list |
| `toUnmodifiableList()` | Immutable |
| `toMap` | Merge function required on duplicate keys |
| `groupingBy` | `Map<K, List<T>>` |
| `partitioningBy` | `Map<Boolean, List<T>>` |

| Pitfall | Issue |
| :--- | :--- |
| `sorted()` on large data | Materializes — O(n log n) memory |
| `parallel()` + ordered op | May lose order benefit |
| Side effects in `forEach` | Race unless concurrent collection |
| `Stream` reuse | Illegal — one terminal only |

---

## Snippets

```java
Map<Department, Long> headcount = employees.stream()
    .filter(e -> e.active())
    .collect(Collectors.groupingBy(Employee::dept, Collectors.counting()));

long sum = invoices.stream().mapToInt(Invoice::amountCents).sum();
```

---

## Internals & Gotchas

- Spliterator characteristics: `SIZED`, `ORDERED`, `DISTINCT` enable optimizations.
- `flatMap` one-to-many; `map` one-to-one.
- Short-circuit: `findFirst`, `anyMatch` stop early.

---

## Production Notes

{{% tip %}}
Prefer `toList()` over `collect(Collectors.toList())` on Java 16+.
{{% /tip %}}
- Don't use parallel on small collections (<10k) or IO-bound tasks.
- Close `Files.lines` with try-with-resources.

---

## Interview Probes


{< interview-answer >}
**Q:** Why lazy?

**A:** Fuse operations; skip work for short-circuit; avoid intermediate collections when chained.
{< /interview-answer >}

{< interview-answer >}
**Q:** parallel stream when?

**A:** Large in-memory CPU-bound transforms with no shared mutable state and spliterator splits well. Not for IO or small lists.
{< /interview-answer >}

---

## See Also

- [Previous: Functional Java](/java-engineering/functional-java-ref/)
- [Next: Threads & Executors](/java-engineering/threads-and-executors/)
- [Functional Java](/java-engineering/functional-java-ref/)
- [Streams Interview](/java-engineering/stream-operations-interview/)
- [Java Engineering Handbook Index](/java-engineering/)
