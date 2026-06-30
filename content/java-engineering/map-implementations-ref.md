---
title: "Map Implementations Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "HashMap, LinkedHashMap, TreeMap, ConcurrentHashMap, WeakHashMap, IdentityHashMap."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Maps"
module: 3
moduleTitle: "Collections"
sectionRef: "3.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `HashMap`: default single-threaded map.
- `LinkedHashMap`: insertion or access order — LRU pattern.
- `TreeMap`: `NavigableMap`, range views, `floor`/`ceiling` keys.
- `ConcurrentHashMap`: concurrent reads/writes; no null keys/values.

---

## Reference Tables

| Map | Null key | Null value | Thread-safe | Ordered |
| :--- | :---: | :---: | :---: | :--- |
| HashMap | 1 | many | No | No |
| LinkedHashMap | 1 | many | No | Insertion/access |
| TreeMap | No | Yes | No | Sorted |
| ConcurrentHashMap | No | No | Yes | No |
| WeakHashMap | Yes | Yes | No | No |
| IdentityHashMap | Yes | Yes | No | Identity |

| Use case | Map |
| :--- | :--- |
| General | `HashMap` |
| Config / ordered props | `LinkedHashMap` |
| Schedulers / timelines | `TreeMap` |
| Shared cache index | `ConcurrentHashMap` |
| Listener registry (GC keys) | `WeakHashMap` |
| Serialization identity | `IdentityHashMap` |

| `NavigableMap` ops | Purpose |
| :--- | :--- |
| `subMap`, `headMap`, `tailMap` | Range without copy |
| `floorKey`, `ceilingKey` | Neighbor search |
| `descendingMap` | Reverse view |

---

## Snippets

```java
ConcurrentHashMap<String, AtomicInteger> counts = new ConcurrentHashMap<>();
counts.computeIfAbsent(key, k -> new AtomicInteger()).incrementAndGet();

NavigableMap<Instant, Event> timeline = new TreeMap<>();
Event e = timeline.floorEntry(t).getValue();
```

---

## Internals & Gotchas

- `TreeMap` Red-Black tree; comparator must be consistent with equals if used as `Set` keys.
- `WeakHashMap` entries expire when key only weakly reachable — values may linger until next access.
- `EnumMap` array-backed — fastest for enum keys.

---

## Production Notes

- `ConcurrentHashMap.size()` may be approximate under contention (JDK-dependent).
- Don't use `HashTable`/`Hashtable` — legacy synchronized entire map.
- For high-performance caches: Caffeine/Guava with eviction stats.

---

## Interview Probes


{< interview-answer >}
**Q:** CHM vs `Collections.synchronizedMap`?

**A:** CHM lock-striping/CAS — finer granularity. synchronizedMap locks whole map per op — poor write scalability.
{< /interview-answer >}

{< interview-answer >}
**Q:** TreeMap when worth O(log n)?

**A:** Sorted keys, range queries, navigable ops. Not for pure get/put hot paths.
{< /interview-answer >}

---

## See Also

- [Previous: List/Set/Queue](/java-engineering/list-set-queue-comparison/)
- [Next: Utils & Ordering](/java-engineering/collections-utils-and-ordering/)
- [Java Engineering Handbook Index](/java-engineering/)
