---
title: "Concurrency Overview"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Model selection hub — asyncio, threads, processes."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Concurrency"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.1"
weight: 401
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/concurrency/"
---

## At a Glance

- CPython [GIL](/python-cheatsheet/03-python-internals/gil/) limits CPU parallelism in threads — see canonical page for internals.
- I/O-bound → `asyncio` or threads; CPU-bound → `multiprocessing` or native extensions.
- Mix models carefully — blocking call in async event loop stalls all tasks.

---

## Reference Tables

| Model | Best for | GIL impact |
| :--- | :--- | :--- |
| `asyncio` | Many concurrent I/O waits | N/A (single thread) |
| `threading` | Blocking I/O libraries | Limited CPU parallelism |
| `multiprocessing` | CPU-bound Python code | Bypass GIL (separate interpreters) |
| `concurrent.futures` | Unified pool API | Thread or process executor |

```mermaid
flowchart LR
  IO[I/O bound] --> async[asyncio / threads]
  CPU[CPU bound] --> mp[multiprocessing / Rust/C ext]
```

---

## Snippets

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(fetch, url) for url in urls]
    for fut in as_completed(futures):
        handle(fut.result())
```

---

## Internals & Gotchas

- Async is not faster CPU — it schedules I/O wait better.
- Thread safety: protect shared mutable state — see [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/).
- `asyncio.run()` creates/closes event loop — entry point for scripts.

---

## Production Notes

- Offload blocking IO with `asyncio.to_thread` (3.9+) in async apps.
- Size thread pools from downstream limits (DB connections, API rate).



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Gil](/python-cheatsheet/03-python-internals/gil/)
- [Next: Asyncio](/python-cheatsheet/04-concurrency/asyncio/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
