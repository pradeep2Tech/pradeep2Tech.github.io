---
title: "Decorators"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "@syntax, wraps, parametrized decorators."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Decorators"
module: 2
moduleTitle: "Core Python"
sectionRef: "2.4"
weight: 204
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/decorators/"
---

## At a Glance

- Decorators are callables transforming callables — syntactic sugar for `f = dec(f)`.
- Use `@functools.wraps(fn)` to preserve `__name__` and `__doc__`.
- Stack bottom-up: `@a @b def f` → `f = a(b(f))`.

---

## Reference Tables

| Pattern | Sketch |
| :--- | :--- |
| Simple | `def deco(fn): ... return wrapper` |
| Parametrized | `def deco(arg): def inner(fn): ...` |
| Class decorator | Callable class with `__call__` |
| `classmethod` | Descriptor decorating functions in class body |

| stdlib | Role |
| :--- | :--- |
| `functools.wraps` | Metadata preservation |
| `functools.lru_cache` | Caching decorator |
| `contextlib.contextmanager` | Generator → context manager |

---

## Snippets

```python
from functools import wraps

def retry(times: int):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for _ in range(times):
                try:
                    return fn(*args, **kwargs)
                except TransientError as e:
                    last = e
            raise last
        return wrapper
    return decorator

@retry(3)
def fetch():
    ...
```

---

## Internals & Gotchas

- Decorators run at import/definition time — heavy work slows module load.
- Stacked decorators: inner applied first.
- `staticmethod`/`classmethod` are descriptor decorators, not plain wrappers.

---

## Production Notes

- Idempotent decorators for testability (detect if already wrapped).
- Type checkers need `ParamSpec`/`TypeVar` on generic decorators.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Dataclasses](/python-cheatsheet/02-core-python/dataclasses/)
- [Next: Context Managers](/python-cheatsheet/02-core-python/context-managers/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
