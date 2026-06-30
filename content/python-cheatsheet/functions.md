---
title: "Functions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "def, args, *args/**kwargs, lambdas, closures, and functools patterns."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Functions"
module: 1
moduleTitle: "Language Basics"
sectionRef: "1.2"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** Why avoid mutable default args?

**A:** Default values are evaluated once at function definition. A shared list/dict mutates across calls. Idiom: `def f(xs=None): xs = [] if xs is None else xs`.
{< /interview-answer >}

---

## See Also

- [Previous: Language Basics](/python-cheatsheet/language-basics/)
- [Next: Collections](/python-cheatsheet/collections/)
- [Decorators](/python-cheatsheet/decorators/)
- [Comprehensions](/python-cheatsheet/comprehensions/)
- [Python Cheatsheet Index](/python-cheatsheet/)
