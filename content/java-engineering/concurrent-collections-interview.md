---
title: "Concurrent Collections (Interview)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CHM vs synchronized wrappers, CopyOnWrite, BlockingQueue family."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Concurrent Collections"
module: 11
moduleTitle: "Interview Cheat Sheets"
sectionRef: "11.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- CHM default concurrent map — not `Hashtable`.
- `CopyOnWriteArrayList` — read-heavy, rare writes.
- BlockingQueue family for producer-consumer.
- `Collections.synchronized*` — whole-structure lock.

---

## Reference Tables

| Type | Implementation | Notes |
| :--- | :--- | :--- |
| Concurrent map | `ConcurrentHashMap` | No nulls |
| Concurrent set | `ConcurrentHashMap.newKeySet()` | Backed by CHM |
| Sorted concurrent | `ConcurrentSkipListMap` | O(log n) |
| Copy-on-write list | `CopyOnWriteArrayList` | Snapshot iterators |
| Bounded buffer | `ArrayBlockingQueue` | Fixed capacity |
| Unbounded linked | `LinkedBlockingQueue` | Watch memory |

| Choose | When |
| :--- | :--- |
| CHM | Shared mutable map |
| COW list | Event listeners, config snapshots |
| `BlockingQueue` | Thread pool work queues |
| `LinkedBlockingQueue` + capacity | Backpressure |

---

## Snippets

```java
BlockingQueue<Task> queue = new ArrayBlockingQueue<>(1000);
queue.put(task); // blocks if full — backpressure
```

---

## Internals & Gotchas

- COW: write copies entire array — O(n) write.
- CHM weakly consistent iterators.
- `DelayQueue` for scheduled tasks.

---

## Production Notes

- Size blocking queues from SLA and memory.
- Don't use COW for write-heavy metrics buffers.

---

## Interview Probes


{< interview-answer >}
**Q:** CopyOnWrite when?

**A:** Read-mostly, iterator must not throw CME, writes rare — listener lists.
{< /interview-answer >}

{< interview-answer >}
**Q:** CHM vs synchronized HashMap?

**A:** CHM finer locking/CAS — synchronizedMap serializes all ops.
{< /interview-answer >}

---

## See Also

- [Previous: Streams Interview](/java-engineering/stream-operations-interview/)
- [Next: GC Interview](/java-engineering/gc-summary-interview/)
- [Java Engineering Handbook Index](/java-engineering/)
