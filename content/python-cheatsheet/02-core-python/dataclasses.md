---
title: "Dataclasses"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "@dataclass options and comparisons."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Dataclasses"
module: 2
moduleTitle: "Core Python"
sectionRef: "2.3"
weight: 203
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/dataclasses/"
---

## At a Glance

- `@dataclass` auto-generates `__init__`, `__repr__`, comparisons (optional).
- `field(default_factory=list)` for mutable defaults.
- `frozen=True` makes instances immutable and hashable (if fields hashable).

---

## Reference Tables

| Option | Effect |
| :--- | :--- |
| `frozen=True` | Immutable; defines `__setattr__` |
| `slots=True` (3.10+) | `__slots__` + smaller instances |
| `kw_only=True` (3.10+) | All fields keyword-only |
| `order=True` | Rich comparisons |
| `repr=False` | Skip auto repr |

| vs | When |
| :--- | :--- |
| `NamedTuple` | Lightweight immutable tuples |
| Pydantic | Validation + serialization at boundary |
| attrs | Heavier feature set, similar niche |

---

## Snippets

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float

@dataclass
class Session:
    user_id: str
    roles: list[str] = field(default_factory=list)
    _token: str = field(repr=False, compare=False)
```

---

## Internals & Gotchas

- Field order: non-default before default fields.
- `__post_init__` for validation after init.
- `dataclass` not a drop-in for ORM entities with lazy loading.

---

## Production Notes

- Use frozen dataclasses as immutable value objects in domain layer.
- Serialize with `dataclasses.asdict` only for simple trees — watch cycles.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Classes](/python-cheatsheet/02-core-python/classes/)
- [Next: Decorators](/python-cheatsheet/02-core-python/decorators/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
