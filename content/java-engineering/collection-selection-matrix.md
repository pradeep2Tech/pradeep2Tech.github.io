---
title: "Java Collections Interview Refresh"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Choose Java collections by access pattern, ordering, and concurrency."
tags: ["java", "collections", "interview", "cheatsheet"]
categories: ["Java Engineering Handbook"]
shortTitle: "Collections"
module: 2
moduleTitle: "Collections Refresh"
sectionRef: "2.1"
cheatSheet: true
aliases: ["collections-decision-matrix", "list-set-queue-comparison", "collections-utils-and-ordering"]
---

## At a Glance

- Start from access pattern, ordering, mutation rate, concurrency, and memory—not habit.
- Know expected complexity and semantic guarantees; implementation details are optional probes.
- For shared mutable state, prefer ownership or immutability before concurrent collections.

---

## Selection Matrix

| Need | Default choice | Change when |
| :--- | :--- | :--- |
| Indexed sequence | `ArrayList` | Use `ArrayDeque` for queue/stack operations |
| Unique values | `HashSet` | `LinkedHashSet` for insertion order; `TreeSet` for sorted/range operations |
| Key/value lookup | `HashMap` | `LinkedHashMap` for stable/LRU order; `TreeMap` for sorted/range keys |
| FIFO/LIFO | `ArrayDeque` | `BlockingQueue` for producer-consumer coordination |
| Priority processing | `PriorityQueue` | It orders removal, not iteration |
| Concurrent map | `ConcurrentHashMap` | Use atomic `compute`, `merge`, or `putIfAbsent` for compound changes |
| Read-mostly list | `CopyOnWriteArrayList` | Avoid when writes are frequent or lists are large |
| Bounded work buffer | `ArrayBlockingQueue` | Capacity creates backpressure; unbounded queues hide overload |

## Complexity Refresh

| Operation | Typical cost | Caveat |
| :--- | :--: | :--- |
| `ArrayList.get` | O(1) | Middle insert/remove is O(n) |
| `HashMap.get/put` | O(1) average | Correct immutable key contract matters |
| `TreeMap.get/put` | O(log n) | Pays for ordering and range queries |
| `PriorityQueue.offer/poll` | O(log n) | `peek` is O(1) |
| `containsValue` on map | O(n) | Value lookup is not indexed |

## Interview Decisions

| Prompt | Strong answer |
| :--- | :--- |
| `ArrayList` vs `LinkedList` | Usually `ArrayList`: locality, memory, O(1) indexed access; linked traversal rarely wins |
| Immutable vs unmodifiable | Immutable cannot change; unmodifiable may be a view of mutable backing data |
| Fail-fast iterator | Best-effort bug detection, not a thread-safety guarantee |
| Why CHM disallows null | Null would make “absent” ambiguous during concurrent reads |
| LRU cache | `LinkedHashMap` works locally; distributed cache needs expiry, capacity, consistency, and metrics |

## Quick Gotchas

- Pre-size a large known collection, but do not guess oversized capacities everywhere.
- Never mutate keys after insertion.
- `Collections.synchronizedMap` does not make multi-step logic atomic.
- Choose bounded queues and define rejection/backpressure behavior.
- Do not claim `LinkedList` is faster without the actual access pattern and measurement.

---

## See Also

[← Core Java](/java-engineering/language-fundamentals/) · [Concurrency →](/java-engineering/java-threading-interview-guide/)
