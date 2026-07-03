---
title: "Typing"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Annotations, Protocol, generics."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Typing"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.6"
weight: 116
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/typing/"
---

## At a Glance

- Annotations are not enforced at runtime by default — use mypy/pyright.
- 3.9+ built-in generics: `list[str]`, `dict[str, int]` — prefer over `typing.List`.
- `Protocol` for structural subtyping; `TypeVar` for generics.

---

## Reference Tables

| Construct | Example |
| :--- | :--- |
| Union | `str | int` or `Union[str, int]` |
| Optional | `str | None` |
| Callable | `Callable[[int], str]` |
| TypeVar | `T = TypeVar('T')` |
| ParamSpec | Decorator preserving signature |
| Literal | `Literal['GET', 'POST']` |
| Final | `Final[int] = 42` |

| Tool | Role |
| :--- | :--- |
| mypy / pyright | Static check |
| `typing.get_type_hints` | Runtime introspection |

---

## Snippets

```python
from typing import Protocol, TypeVar, Generic

class SupportsClose(Protocol):
    def close(self) -> None: ...

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

def first(items: list[T]) -> T:
    return items[0]
```

---

## Internals & Gotchas

- `from __future__ import annotations` postpones evaluation (PEP 563 behavior in 3.11+ evolving).
- `Any` disables checking — use narrowly.
- `TypedDict` for dict shapes; not runtime validated.

---

## Production Notes

- Type public APIs; run pyright in CI on library code.
- Align Pydantic models at HTTP boundary with internal TypedDict/dataclass.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Exceptions](/python-cheatsheet/01-fundamentals/exceptions/)
- [Next: Oop](/python-cheatsheet/02-core-python/oop/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
