---
title: "Asyncio"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "async/await, event loop, tasks, gather, timeouts, and async context managers."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Asyncio"
module: 6
moduleTitle: "Concurrency"
sectionRef: "6.2"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** asyncio vs threads for 1000 HTTP calls?

**A:** Asyncio: one thread, low memory, explicit async APIs. Threads: simpler with blocking libs but higher memory and GIL context switching.
{< /interview-answer >}

---

## See Also

- [Previous: Concurrency](/python-cheatsheet/concurrency/)
- [Next: Multithreading](/python-cheatsheet/multithreading/)
- [Concurrency](/python-cheatsheet/concurrency/)
- [Multithreading](/python-cheatsheet/multithreading/)
- [Python Cheatsheet Index](/python-cheatsheet/)
