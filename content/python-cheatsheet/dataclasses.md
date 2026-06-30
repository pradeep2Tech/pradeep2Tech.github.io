---
title: "Dataclasses"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "@dataclass options, field(), frozen, slots, and vs NamedTuple/Pydantic."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Dataclasses"
module: 5
moduleTitle: "Advanced Language Features"
sectionRef: "5.7"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** dataclass vs dict?

**A:** Dataclass gives typed fields, repr, eq, and IDE support. Dict flexible but error-prone keys and no structure.
{< /interview-answer >}

---

## See Also

- [Previous: Typing](/python-cheatsheet/typing/)
- [Next: Concurrency](/python-cheatsheet/concurrency/)
- [Classes](/python-cheatsheet/classes/)
- [Typing](/python-cheatsheet/typing/)
- [Python Cheatsheet Index](/python-cheatsheet/)
