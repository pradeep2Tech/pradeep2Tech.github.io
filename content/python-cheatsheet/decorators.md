---
title: "Decorators"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "@syntax, functools.wraps, parameterized decorators, and class decorators."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Decorators"
module: 5
moduleTitle: "Advanced Language Features"
sectionRef: "5.2"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** How does @decorator work?

**A:**  `@deco` on `def f` is `f = deco(f)`. `deco` receives the function object and returns the replacement (usually a wrapper).
{< /interview-answer >}

---

## See Also

- [Previous: Exceptions](/python-cheatsheet/exceptions/)
- [Next: Generators](/python-cheatsheet/generators/)
- [Functions](/python-cheatsheet/functions/)
- [Context Managers](/python-cheatsheet/context-managers/)
- [Python Cheatsheet Index](/python-cheatsheet/)
