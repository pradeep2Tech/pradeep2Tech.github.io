---
title: "Classes"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Attributes, properties, dunder methods."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Classes"
module: 2
moduleTitle: "Core Python"
sectionRef: "2.2"
weight: 202
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/classes/"
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
- `__new__` / descriptor protocol: [Object Model](/python-cheatsheet/03-python-internals/object-model/).
- Name mangling: `__private` → `_ClassName__private` (not security).

---

## Production Notes

- Keep domain logic on entities; avoid anemic models only when ORM demands it.
- Use `__slots__` on high-volume objects after profiling memory.

---

## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/) — answers on canonical topic pages.




---

---

## See Also

- [Previous: Oop](/python-cheatsheet/02-core-python/oop/)
- [Next: Dataclasses](/python-cheatsheet/02-core-python/dataclasses/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
