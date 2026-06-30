---
title: "Typing"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Annotations, generics, Protocol, TypeAlias, Literal, and runtime checking."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Typing"
module: 5
moduleTitle: "Advanced Language Features"
sectionRef: "5.6"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** Protocol vs ABC?

**A:** Protocol is structural (duck typing with types) — no inheritance required. ABC is nominal — must subclass explicitly.
{< /interview-answer >}

---

## See Also

- [Previous: Context Managers](/python-cheatsheet/context-managers/)
- [Next: Dataclasses](/python-cheatsheet/dataclasses/)
- [Dataclasses](/python-cheatsheet/dataclasses/)
- [Classes](/python-cheatsheet/classes/)
- [Python Cheatsheet Index](/python-cheatsheet/)
