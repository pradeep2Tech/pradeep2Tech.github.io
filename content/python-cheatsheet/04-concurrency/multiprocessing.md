---
title: "Multiprocessing"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Process pools, spawn/fork, IPC."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Multiproc"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.4"
weight: 404
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/multiprocessing/"
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



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Multithreading](/python-cheatsheet/04-concurrency/multithreading/)
- [Next: Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
