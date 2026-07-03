---
title: "Garbage Collection"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Reference counting, cyclic GC, weakref, performance impact."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "GC"
module: 3
moduleTitle: "Python Internals"
sectionRef: "3.6"
weight: 306
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- Primary reclamation: **reference counting** (immediate when refcount hits 0).
- **Cyclic GC** collects unreachable reference cycles (generations 0/1/2).
- `gc` module introspects cycles; `weakref` breaks strong cycles intentionally.

## Core Concepts

| Layer | Behavior |
| :--- | :--- |
| Refcount | Increment on bind, decrement on del/out-of-scope |
| Cyclic GC | Detects unreachable cycles; runs on thresholds |
| `weakref` | Non-owning references; `WeakValueDictionary` for caches |

## Internal Working
```mermaid
flowchart LR
  g0[gen0] --> g1[gen1]
  g1 --> g2[gen2]
  g2 --> sweep[Collect cycles]
```


```mermaid
flowchart TD
  ref[Refcount to zero] --> free[Deallocate immediately]
  cycle[Reference cycle] --> gc[Generational GC scan]
  gc --> free2[Break cycle and free]
```

```python
import gc, weakref

gc.set_debug(gc.DEBUG_STATS)
gc.collect()  # rarely in hot paths — diagnostics only

cache: weakref.WeakValueDictionary = weakref.WeakValueDictionary()
```

## Performance Considerations

- Large cycles cause GC pauses — break cycles with `weakref` or explicit `clear()`.
- `gc.collect()` in production hot paths is usually a smell.

## Troubleshooting

| Symptom | Action |
| :--- | :--- |
| RSS grows, refcount objects alive | `tracemalloc`, `objgraph`, check globals and caches |
| GC pauses | Reduce cycle creation, tune thresholds carefully |



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Memory Management](/python-cheatsheet/03-python-internals/memory-management/)
- [Next: Gil](/python-cheatsheet/03-python-internals/gil/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
