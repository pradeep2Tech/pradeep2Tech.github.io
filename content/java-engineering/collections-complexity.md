---
title: "Collections Complexity (Cheat Sheet)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Big-O cheat sheet for List, Set, Map, Queue — one-screen interview revision."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Collections Big-O"
module: 6
moduleTitle: "Interview Cheat Sheets"
sectionRef: "6.4"
cheatSheet: true
interviewHandbook: true
---

## At a Glance

- Interview one-pager — average vs worst case for hash structures.
- Tree structures: O(log n) guaranteed.
- Iteration on hash maps: O(capacity + size).
- Concurrent structures: same big-O with different constants and weak iteration.

---

## Reference Tables

| List op | ArrayList | LinkedList |
| :--- | :---: | :---: |
| `get(i)` | **O(1)** | O(n) |
| `add(end)` | O(1)* | **O(1)** |
| `add(i)` | O(n) | O(n) |

| Set op | HashSet | TreeSet |
| :--- | :---: | :---: |
| `add/contains` | O(1) avg | O(log n) |
| Iteration order | None | Sorted |

| Map op | HashMap | TreeMap | CHM |
| :--- | :---: | :---: | :---: |
| `get/put` | O(1) avg | O(log n) | O(1) avg |
| `containsValue` | O(n) | O(n) | O(n) |

| Queue | offer/poll |
| :--- | :---: |
| `ArrayDeque` | O(1) |
| `PriorityQueue` | O(log n) |

---

## Snippets

```java
// O(1) avg membership
Set<String> tags = new HashSet<>(List.of("java", "jvm"));
NavigableMap<Integer, String> ranks = new TreeMap<>();
```

---

## Internals & Gotchas

- Hash collision → list/tree bin — worst case per bin.
- `LinkedList` as queue rarely beats `ArrayDeque`.
- CHM `size()` approximate under contention.

---

## Production Notes

- State avg vs worst in design reviews for hash-based stores.
- Pre-size collections when size known.

---

## Interview Probes


{< interview-answer >}
**Q:** ArrayList vs LinkedList for 1M random reads?

**A:** ArrayList O(1) per get — LinkedList O(n).
{< /interview-answer >}

{< interview-answer >}
**Q:** When TreeMap worth O(log n)?

**A:** Sorted keys, range queries — not pure get/put throughput.
{< /interview-answer >}

---

## See Also

- [Previous: Thread Lifecycle Cheat Sheet](/java-engineering/thread-lifecycle-cheatsheet/)
- [Next: Java Version Migration](/java-engineering/java-version-migration-guide/)
- [Collection Selection Matrix](/java-engineering/collection-selection-matrix/)
- [Java Engineering Handbook Index](/java-engineering/)
