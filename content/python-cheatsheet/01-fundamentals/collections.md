---
title: "Collections"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "list, tuple, dict, set, deque."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Collections"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.3"
weight: 113
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/collections/"
---

## At a Glance

- `list` ordered mutable; `tuple` ordered immutable; `dict` insertion-ordered (3.7+).
- `set`/`frozenset` — hashable unique elements; `frozenset` is immutable/hashable.
- Pick by access pattern and concurrency needs — no single 'best' collection.

---

## Reference Tables

| Type | Ordered | Mutable | Hashable | Typical ops |
| :--- | :---: | :---: | :---: | :--- |
| `list` | ✓ | ✓ | ✗ | index O(1), insert mid O(n) |
| `tuple` | ✓ | ✗ | ✓* | fixed records, dict keys |
| `dict` | ✓ | ✓ | ✗ | get/set avg O(1) |
| `set` | ✗ | ✓ | ✗ | membership O(1) avg |
| `deque` | ✓ | ✓ | ✗ | O(1) append/pop both ends |

*Tuple hashable only if all elements hashable.

---

## Snippets

```python
from collections import defaultdict, Counter, deque

counts = Counter(tokens)
by_user: dict[str, list] = defaultdict(list)
queue: deque[str] = deque(maxlen=1000)

# dict merge (3.9+)
merged = base | overrides

# structural sharing — cheap copies
view = existing_dict | {"k": "v"}
```

---

## Internals & Gotchas

- `list.sort()` in-place; `sorted()` returns new list.
- Dict keys must be hashable; values can be anything.
- `is` not valid for deep equality — use `==` or `dataclasses`/`pydantic`.

---

## Production Notes

- Use `collections.deque` for bounded in-memory buffers.
- For large numeric arrays prefer `numpy` or `array.array` — not plain lists.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Functions](/python-cheatsheet/01-fundamentals/functions/)
- [Next: Modules](/python-cheatsheet/01-fundamentals/modules/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
