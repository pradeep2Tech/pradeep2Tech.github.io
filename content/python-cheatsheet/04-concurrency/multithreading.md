---
title: "Multithreading"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "threading, locks, queues."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Threading"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.3"
weight: 403
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/multithreading/"
---

## At a Glance

- `threading.Thread` for OS threads; prefer `ThreadPoolExecutor` for pools.
- Use `queue.Queue` for producer-consumer — thread-safe without manual locks.
- [GIL](/python-cheatsheet/03-python-internals/gil/) limits CPU parallelism — threads help for I/O-bound work.

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



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Asyncio](/python-cheatsheet/04-concurrency/asyncio/)
- [Next: Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
