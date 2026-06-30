---
title: "Multithreading"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "threading module, locks, queues, GIL impact, and when threads help."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Multithreading"
module: 6
moduleTitle: "Concurrency"
sectionRef: "6.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `threading.Thread` for OS threads; prefer `ThreadPoolExecutor` for pools.
- Use `queue.Queue` for producer-consumer — thread-safe without manual locks.
- GIL limits CPU parallelism — threads still help when waiting on I/O or releasing GIL.

---

## Reference Tables

| Primitive | Use |
| :--- | :--- |
| `Lock` / `RLock` | Mutual exclusion |
| `Condition` | Wait/notify |
| `Semaphore` | Counting resource limit |
| `Event` | One-shot signal |
| `Queue` | Safe handoff |

| Module | Notes |
| :--- | :--- |
| `threading` | Low-level threads |
| `concurrent.futures` | Higher-level pools |

---

## Snippets

```python
import threading
from queue import Queue

q: Queue[WorkItem] = Queue(maxsize=1000)

def worker():
    while True:
        item = q.get()
        try:
            process(item)
        finally:
            q.task_done()

for _ in range(4):
    threading.Thread(target=worker, daemon=True).start()
```

---

## Internals & Gotchas

- Daemon threads killed abruptly on main exit — not for cleanup work.
- `Lock` not reentrant by default — use `RLock` if same thread re-enters.
- Race on `if not dict: dict[k]=` — use locks or concurrent collections.

---

## Production Notes

- Name threads for debugging (`threading.current_thread().name`).
- Cap pool size; unbounded threads exhaust memory and FDs.

---

## Interview Probes


{< interview-answer >}
**Q:** Why GIL exists?

**A:** Protects CPython object memory management from races without per-object locks. Simplifies C API at cost of CPU parallelism.
{< /interview-answer >}

---

## See Also

- [Previous: Asyncio](/python-cheatsheet/asyncio/)
- [Next: Multiprocessing](/python-cheatsheet/multiprocessing/)
- [Concurrency](/python-cheatsheet/concurrency/)
- [Multiprocessing](/python-cheatsheet/multiprocessing/)
- [Python Cheatsheet Index](/python-cheatsheet/)
