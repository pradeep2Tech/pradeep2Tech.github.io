---
title: "ConcurrentHashMap Internals"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Bins, CAS, sizeCtl, compute methods, and iteration semantics under contention."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "CHM Internals"
module: 2
moduleTitle: "Collections"
sectionRef: "2.3"
ShowToc: true
interviewHandbook: true
---

## At a Glance

- No global lock — per-bin synchronization / CAS on Java 8+.
- `sizeCtl` coordinates initialization and resize.
- `compute*` methods atomic at key level — prefer over get+put.
- Weakly consistent iterators — reflect some concurrent updates.

---

## Reference Tables

| Era | Mechanism |
| :--- | :--- |
| Java 7 | Segment locks (16 default) |
| Java 8+ | Node array like HashMap + synchronized bin head / CAS + tree bins |
| Resize | Multi-thread assisted transfer |

| Method | Atomicity |
| :--- | :--- |
| `putIfAbsent` | Key-level |
| `compute` | Read-modify-write atomic |
| `merge` | Atomic combine |
| `replace(K,V,V)` | Compare-and-swap value |

| vs `Hashtable` | CHM |
| :--- | :--- |
| Lock scope | Whole table | Bin-level |
| Null | Allowed | Forbidden |
| Iterators | Enumerator fail-fast | Weakly consistent |

---

## Snippets

```java
chm.compute(key, (k, v) -> v == null ? 1 : v + 1);
chm.merge(key, 1, Integer::sum);

// Avoid
Integer v = chm.get(k);
chm.put(k, v + 1); // race
```

---

## Internals & Gotchas

- `CounterCell` striping for `size()` approximation under contention.
- Forwarding nodes during resize — `helpTransfer` lets other threads assist.
- `ConcurrentHashMap.keySet()` view operations may be weaker than `ConcurrentSkipListSet` for ordered needs.

---

## Production Notes

- Use `compute`/`merge` for counters — not `get`+`put`.
- Bulk `forEach` parallel threshold — rarely needed; measure first.
- No null keys/values — use sentinel `Optional`-like marker objects if needed.

---

## Interview Probes


{< interview-answer >}
**Q:** CHM size() accuracy?

**A:** May be approximate under heavy concurrent updates — documented behavior; don't use as strict invariant check without external sync.
{< /interview-answer >}

{< interview-answer >}
**Q:** Why forbid null in CHM?

**A:** Ambiguity: `get` returns null for missing vs null value — Doug Lea design avoids double-meaning in concurrent context.
{< /interview-answer >}

---

## See Also

- [Previous: HashMap Internals](/java-engineering/hashmap-internals/)
- [Next: Map Implementations](/java-engineering/map-implementations/)
- [Locks & Atomics](/java-engineering/locks-and-atomics/)
- [Concurrent Collections](/java-engineering/concurrent-collections/)
- [Java Engineering Handbook Index](/java-engineering/)
