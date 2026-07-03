---
title: "Asyncio"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "async/await, TaskGroup, event loop."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Asyncio"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.2"
weight: 402
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/asyncio/"
---

## At a Glance

- Coroutines (`async def`) are awaitable; don't call without `await` or `create_task`.
- Event loop schedules tasks — one thread default; use `asyncio.run` as main entry.
- Prefer `asyncio.TaskGroup` (3.11+) over bare `gather` for structured concurrency.

---

## Reference Tables

| API | Role |
| :--- | :--- |
| `await coro` | Suspend until complete |
| `create_task` | Schedule concurrent coroutine |
| `gather` | Wait for multiple awaitables |
| `TaskGroup` | Structured task tree; cancel siblings on error |
| `wait_for` / `timeout` | Deadline control |
| `Semaphore` | Limit concurrency |

| Pitfall | Fix |
| :--- | :--- |
| Blocking `time.sleep` | `await asyncio.sleep` |
| Sync HTTP lib | `httpx.AsyncClient` or `to_thread` |

---

## Snippets

```python
import asyncio

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker("a"))
        tg.create_task(worker("b"))

async def worker(name: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api/{name}")
        return r.json()

asyncio.run(main())
```

---

## Internals & Gotchas

- Un-awaited coroutine warning — silent bug.
- Loop per thread — don't share across threads without `asyncio.run_coroutine_threadsafe`.
- Cancellation raises `CancelledError` — clean up in `finally`.

---

## Production Notes

- Set global HTTP client session limits; reuse connections.
- Propagate tracing context with `contextvars`.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Concurrency](/python-cheatsheet/04-concurrency/concurrency/)
- [Next: Multithreading](/python-cheatsheet/04-concurrency/multithreading/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
