---
title: "Memory Management"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Reference counting, gc module, weakref, __slots__, and profiling leaks."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Memory"
module: 7
moduleTitle: "Runtime & Tooling"
sectionRef: "7.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Primary GC: reference counting + cyclic garbage detector (`gc` module).
- `sys.getsizeof` shallow — doesn't include referenced objects.
- Profile with `tracemalloc`, `objgraph`, memory_profiler before optimizing.

---

## Reference Tables

| Technique | Effect |
| :--- | :--- |
| `__slots__` | Reduce per-instance dict overhead |
| `weakref` | Avoid reference cycles to large graphs |
| Gen expr vs list | Lower peak memory |
| `gc.collect()` | Force cyclic GC — rarely in prod hot path |

| Symptom | Likely cause |
| :--- | :--- |
| Steady RSS growth | Leaked globals, caches, cycles |
| Spike on request | Large materialized collections |

---

## Snippets

```python
import tracemalloc

tracemalloc.start()
# ... run workload ...
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:10]:
    print(stat)

import weakref
cache = weakref.WeakValueDictionary()
```

---

## Internals & Gotchas

- C extensions may allocate off-heap — RSS > Python object totals.
- `del x` drops reference; object freed when refcount 0 (unless cycle).
- Interned strings and small ints cached — don't rely on identity.

---

## Production Notes

- Bound caches (`lru_cache(maxsize=...)`, TTL).
- Stream large files; don't read entire blob into memory.

---

## Interview Probes


{< interview-answer >}
**Q:** Why cyclic GC?

**A:** Reference counting alone can't free cycles (A→B→A). Generational cyclic collector runs periodically.
{< /interview-answer >}

---

## See Also

- [Previous: Multiprocessing](/python-cheatsheet/multiprocessing/)
- [Next: Packaging](/python-cheatsheet/packaging/)
- [Collections](/python-cheatsheet/collections/)
- [Generators](/python-cheatsheet/generators/)
- [Python Cheatsheet Index](/python-cheatsheet/)
