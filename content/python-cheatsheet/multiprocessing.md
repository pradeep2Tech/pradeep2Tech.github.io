---
title: "Multiprocessing"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Process pools, shared memory, spawn/fork, and CPU-bound parallelism."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Multiprocessing"
module: 6
moduleTitle: "Concurrency"
sectionRef: "6.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Separate memory spaces — share data via `Queue`, `Pipe`, or `multiprocessing.Manager`.
- Windows uses `spawn` — import guard `if __name__ == '__main__'` required.
- `ProcessPoolExecutor` maps function over iterables for CPU work.

---

## Reference Tables

| Start method | Behavior |
| :--- | :--- |
| `spawn` | Clean interpreter (Windows default) |
| `fork` | Copy parent process (Unix — careful with threads) |
| `forkserver` | Server forks workers |

| Share state | Safe? |
| :--- | :--- |
| `Queue` / `Pipe` | ✓ |
| `shared_memory` (3.8+) | ✓ with sync |
| Global list | ✗ not across processes |

---

## Snippets

```python
from concurrent.futures import ProcessPoolExecutor

def cpu_heavy(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        results = list(pool.map(cpu_heavy, range(1000)))
```

---

## Internals & Gotchas

- Picklable top-level functions only for `multiprocessing` on Windows.
- Large data shipping between processes is expensive — share memory or chunk.
- Mixing `fork` + threads can duplicate broken state.

---

## Production Notes

- Worker count ≈ CPU cores for CPU-bound; measure queue depth.
- Use joblib or dask for larger distributed compute.

---

## Interview Probes


{< interview-answer >}
**Q:** threads vs processes for CPU work?

**A:** Processes bypass GIL — true parallel CPU. Threads won't scale CPU-bound Python loops.
{< /interview-answer >}

---

## See Also

- [Previous: Multithreading](/python-cheatsheet/multithreading/)
- [Next: Memory](/python-cheatsheet/memory-management/)
- [Concurrency](/python-cheatsheet/concurrency/)
- [Memory](/python-cheatsheet/memory-management/)
- [Python Cheatsheet Index](/python-cheatsheet/)
