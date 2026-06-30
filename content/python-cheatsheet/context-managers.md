---
title: "Context Managers"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "with statement, __enter__/__exit__, contextlib, and resource cleanup."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Context Managers"
module: 5
moduleTitle: "Advanced Language Features"
sectionRef: "5.5"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** contextmanager vs class CM?

**A:** Generator style concise for simple setup/teardown. Class when complex state or reusable configurable manager.
{< /interview-answer >}

---

## See Also

- [Previous: Iterators](/python-cheatsheet/iterators/)
- [Next: Typing](/python-cheatsheet/typing/)
- [Exceptions](/python-cheatsheet/exceptions/)
- [Decorators](/python-cheatsheet/decorators/)
- [Python Cheatsheet Index](/python-cheatsheet/)
