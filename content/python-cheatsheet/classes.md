---
title: "Classes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "__init__, attributes, properties, __slots__, and class vs instance namespaces."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Classes"
module: 3
moduleTitle: "OOP"
sectionRef: "3.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Instance `__dict__` holds attributes unless `__slots__` restricts.
- `@property` for computed/validated fields; `@classmethod` / `@staticmethod` for alternate constructors.
- Dataclasses (see dedicated page) reduce boilerplate for data carriers.

---

## Reference Tables

| Member | First arg | Typical use |
| :--- | :--- | :--- |
| Instance method | `self` | Behavior on instance |
| `@classmethod` | `cls` | Factory, alt constructors |
| `@staticmethod` | none | Namespaced helper |
| `@property` | `self` | Getter/setter/deleter |

| Dunder | Role |
| :--- | :--- |
| `__init__` | Initialize (not allocate) |
| `__repr__` / `__str__` | Debug vs user string |
| `__eq__` / `__hash__` | Equality contract |

---

## Snippets

```python
class User:
    __slots__ = ("id", "email")  # no per-instance __dict__

    def __init__(self, id: int, email: str) -> None:
        self.id = id
        self.email = email

    @classmethod
    def from_row(cls, row: dict) -> "User":
        return cls(row["id"], row["email"])

    @property
    def domain(self) -> str:
        return self.email.split("@", 1)[1]
```

---

## Internals & Gotchas

- Defining `__eq__` without `__hash__` makes instances unhashable (hash set to None).
- `__init__` ≠ `__new__` — latter controls instance creation (singletons, immutables).
- Name mangling: `__private` → `_ClassName__private` (not security).

---

## Production Notes

- Keep domain logic on entities; avoid anemic models only when ORM demands it.
- Use `__slots__` on high-volume objects after profiling memory.

---

## Interview Probes


{< interview-answer >}
**Q:** When use __slots__?

**A:** When you have millions of small instances and memory dominates. Trade-off: no arbitrary attributes, subclasses must declare slots too.
{< /interview-answer >}

---

## See Also

- [Previous: Comprehensions](/python-cheatsheet/comprehensions/)
- [Next: OOP](/python-cheatsheet/oop/)
- [OOP](/python-cheatsheet/oop/)
- [Dataclasses](/python-cheatsheet/dataclasses/)
- [Python Cheatsheet Index](/python-cheatsheet/)
