---
title: "Memory Management"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "pymalloc overview, RSS, sizing."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Memory"
module: 3
moduleTitle: "Python Internals"
sectionRef: "3.5"
weight: 305
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/memory-management/"
---

## Quick Revision

- CPython uses refcounting plus generational cyclic GC.
- pymalloc manages small object arenas — RSS can exceed `sys.getsizeof` totals.
- Tune memory after profiling — not before.

## At a Glance

- Memory overview — reference counting and cyclic GC: [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/).
- `sys.getsizeof` shallow — doesn't include referenced objects.
- Profile with [Profiling](/python-cheatsheet/05-performance/profiling/) (`cProfile`, `tracemalloc`, `memory_profiler`).

---

## Reference Tables

| Technique | Effect |
| :--- | :--- |
| `__slots__` | Reduce per-instance dict overhead |
| `weakref` | Avoid reference cycles to large graphs |
| Gen expr vs list | Lower peak memory |
| Spike on request | Large materialized collections |

---

## Snippets



---

## Internals & Gotchas

- C extensions may allocate off-heap — RSS > Python object totals.
- `del x` drops a reference; cyclic graphs need the GC — see [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/).
- Interned strings and small ints cached — don't rely on identity.

---

## Production Notes

- Bound caches (`lru_cache(maxsize=...)`, TTL).
- Stream large files; don't read entire blob into memory.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Object Model](/python-cheatsheet/03-python-internals/object-model/)
- [Next: Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
