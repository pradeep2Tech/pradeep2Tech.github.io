---
title: "List, Set & Queue Comparison"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Implementation trade-offs — ArrayList, HashSet, TreeSet, ArrayDeque, PriorityQueue."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "List/Set/Queue"
module: 3
moduleTitle: "Collections"
sectionRef: "3.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `ArrayList`: default list — cache-friendly contiguous array.
- `LinkedList`: doubly-linked — only for deque ops at both ends without index access.
- `HashSet`/`LinkedHashSet`/`TreeSet`: uniqueness with different ordering guarantees.
- Stacks: `ArrayDeque` — never `java.util.Stack` (extends Vector).

---

## Reference Tables

| List op | ArrayList | LinkedList | Vector |
| :--- | :---: | :---: | :---: |
| `get(i)` | **O(1)** | O(n) | **O(1)** |
| `add(end)` | O(1)* | **O(1)** | O(1)* |
| `add(i)` | O(n) | O(n) | O(n) |
| Memory | Low overhead | Node per element | Sync overhead |

| Set op | HashSet | LinkedHashSet | TreeSet |
| :--- | :---: | :---: | :---: |
| `add/contains` | O(1) avg | O(1) avg | O(log n) |
| Iteration order | Undefined | Insertion | Sorted |
| `null` | 1 allowed | 1 allowed | Usually no |

| Deque/Queue | ArrayDeque | PriorityQueue | LinkedBlockingQueue |
| :--- | :---: | :---: | :---: |
| `offer/poll` | O(1) | O(log n) | blocking O(1) avg |
| Thread-safe | No | No | Yes |
| Bounded | No | No | Optional capacity |

---

## Snippets

```java
Deque<Task> stack = new ArrayDeque<>();
stack.push(task);
Task t = stack.pop();

Queue<Event> pq = new PriorityQueue<>(Comparator.comparing(Event::severity).reversed());
```

---

## Internals & Gotchas

- `ArrayList` grow ~1.5×; amortized append.
- `PriorityQueue` is min-heap by natural order or comparator.
- `TreeSet` backed by `TreeMap` dummy value.

---

## Production Notes

- Replace `Stack`/`Vector` in legacy code during touch.
- Large lists: consider primitive lists (Eclipse Collections, fastutil) or columnar storage.

---

## Interview Probes


{< interview-answer >}
**Q:** ArrayList vs LinkedList myth?

**A:** LinkedList rarely wins on modern JVM — pointer chasing hurts cache; ArrayList wins except niche deque with no index.
{< /interview-answer >}

{< interview-answer >}
**Q:** PriorityQueue iterator order?

**A:** Not sorted — only `poll` returns head. To sorted list: drain to array and sort or use stream.
{< /interview-answer >}

---

## See Also

- [Previous: Collection Choice](/java-engineering/collections-decision-matrix/)
- [Next: Maps](/java-engineering/map-implementations-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
