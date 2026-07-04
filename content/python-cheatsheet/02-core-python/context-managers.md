---
title: "Context Managers"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "with, __enter__/__exit__, ExitStack."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Context Mgr"
module: 2
moduleTitle: "Core Python"
sectionRef: "2.5"
weight: 205
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/context-managers/"
---

## At a Glance

- `with` calls `__enter__` / `__exit__` — exceptions propagate unless `__exit__` returns True.
- `contextlib.contextmanager` turns generator into CM (yield once).
- `contextlib.ExitStack` manages dynamic number of contexts.

---

## Reference Tables

| API | Role |
| :--- | :--- |
| `__enter__` | Setup; return bound resource |
| `__exit__(exc_type, exc, tb)` | Teardown; return True to suppress |
| `@contextmanager` | Generator-based CM |
| `AsyncContextManager` | `async with` |

| stdlib CM | Resource |
| :--- | :--- |
| `open()` | Files |
| `threading.Lock` | Locks |
| `decimal.localcontext` | Context vars |

---

## Snippets

```python
from contextlib import contextmanager, ExitStack

@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        logger.info("%s %.3fs", label, time.perf_counter() - start)

with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in paths]
    merge(files)
```

---

## Internals & Gotchas

- `__exit__` runs even if `__enter__` failed (if object partially constructed).
- Don't yield twice in `@contextmanager`.
- Suppressing exceptions in `__exit__` hides bugs — rare.

---

## Production Notes

- Always use `with open(...)` — never bare `open` without close.
- Nest `with` or `ExitStack` for transactions + files + locks.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Decorators](/python-cheatsheet/02-core-python/decorators/)
- [Next: Iterators](/python-cheatsheet/02-core-python/iterators/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
