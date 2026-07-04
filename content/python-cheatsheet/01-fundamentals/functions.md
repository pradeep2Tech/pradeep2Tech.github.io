---
title: "Functions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "def, args, closures, functools."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Functions"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.2"
weight: 112
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/functions/"
---

## At a Glance

- Functions are first-class — assign, pass, return, store in collections.
- `*args` tuple, `**kwargs` dict — only in definition signature position.
- Use type hints on public APIs; defaults evaluated once at def time.

---

## Reference Tables

| Parameter kind | Syntax | Example |
| :--- | :--- | :--- |
| Positional-only | `/ before ` | `def f(a, b, /, c):` |
| Keyword-only | `*` separator | `def f(a, *, b):` |
| Var positional | `*args` | Extra positional args |
| Var keyword | `**kwargs` | Extra keyword args |

| Tool | Use |
| :--- | :--- |
| `functools.partial` | Pre-fill arguments |
| `functools.lru_cache` | Memoize pure calls |
| `functools.singledispatch` | Type-based overload |

---

## Snippets

```python
def connect(host: str, port: int = 443, *, timeout: float = 5.0) -> None:
    ...

def apply(fn, /, *args, **kwargs):
    return fn(*args, **kwargs)

# Lambda — single expression only
key_fn = lambda r: (r.priority, r.created_at)

@lru_cache(maxsize=128)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

---

## Internals & Gotchas

- Closures capture variables by reference — late-binding loop variable trap in lambdas.
- Recursive depth limited by stack — tail recursion not optimized.
- `return` in generator makes it a generator function (contains `yield`).

---

## Production Notes

- Keep signatures stable; use keyword-only for new optional params.
- Document exceptions raised; don't catch-all inside library helpers.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Language Basics](/python-cheatsheet/01-fundamentals/language-basics/)
- [Next: Collections](/python-cheatsheet/01-fundamentals/collections/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
