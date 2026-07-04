---
title: "Object Model"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "PyObject layout, attribute lookup, descriptors, __new__, equality contract."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Object Model"
module: 3
moduleTitle: "Python Internals"
sectionRef: "3.4"
weight: 304
interviewHandbook: true
---

## Quick Revision

- Everything is an object; variables bind names to objects.
- Attribute lookup: instance `__dict__` → class → MRO → descriptors.
- `__eq__` without `__hash__` sets `__hash__ = None` (unhashable).

## Core Concepts

| Mechanism | Role |
| :--- | :--- |
| `PyObject` | `ob_refcnt`, `ob_type`, payload |
| `__dict__` | Per-instance attribute storage (unless `__slots__`) |
| Descriptor | `__get__` / `__set__` / `__delete__` on class attributes |
| `__new__` | Allocates instance; `__init__` initializes |

## Internal Working
```mermaid
flowchart LR
  inst[Instance __dict__] --> cls[Class]
  cls --> mro[MRO parents]
  mro --> desc[Descriptor __get__]
```


```mermaid
sequenceDiagram
  participant Inst
  participant Class
  participant Desc
  Inst->>Class: lookup attr
  alt data descriptor on class
    Class->>Desc: __get__(inst, class)
  else instance __dict__
    Inst-->>Inst: return value
  end
```

## Design Tradeoffs

| Choice | Trade-off |
| :--- | :--- |
| `__slots__` | Lower memory, no arbitrary attrs |
| `__eq__` only | Breaks hash-based collections |
| Descriptors | Power vs complexity |

## Production Usage

- Use `@property` for validation; understand descriptor cost on hot paths.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Bytecode](/python-cheatsheet/03-python-internals/bytecode/)
- [Next: Memory Management](/python-cheatsheet/03-python-internals/memory-management/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
