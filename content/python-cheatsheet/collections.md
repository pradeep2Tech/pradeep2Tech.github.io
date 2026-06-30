---
title: "Collections"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "list, tuple, dict, set, deque — mutability, complexity, and when to pick each."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Collections"
module: 2
moduleTitle: "Collections & Comprehensions"
sectionRef: "2.1"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** dict vs OrderedDict today?

**A:** Built-in `dict` preserves insertion order since 3.7 (guaranteed 3.7+). `OrderedDict` still useful for `move_to_end` and equality ignoring order.
{< /interview-answer >}

---

## See Also

- [Previous: Functions](/python-cheatsheet/functions/)
- [Next: Comprehensions](/python-cheatsheet/comprehensions/)
- [Comprehensions](/python-cheatsheet/comprehensions/)
- [Iterators](/python-cheatsheet/iterators/)
- [Python Cheatsheet Index](/python-cheatsheet/)
