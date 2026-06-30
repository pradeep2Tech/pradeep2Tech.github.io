---
title: "Iterators & Iterables"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "__iter__/__next__, StopIteration, itertools, and lazy evaluation."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Iterators"
module: 5
moduleTitle: "Advanced Language Features"
sectionRef: "5.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Iterable has `__iter__`; iterator has `__iter__` returning self and `__next__`.
- `StopIteration` ends iteration — don't catch it outside iterator protocol.
- `itertools` provides memory-efficient combinatorial utilities.

---

## Reference Tables

| Object | Protocol |
| :--- | :--- |
| Iterable | `__iter__()` returns iterator |
| Iterator | `__iter__()` + `__next__()` |
| Sequence | `__getitem__` + length |

| itertools | Purpose |
| :--- | :--- |
| `chain` | Flatten iterables |
| `groupby` | Adjacent grouping (sort first!) |
| `islice` | Lazy slice |
| `batched` (3.12+) | Fixed-size chunks |

---

## Snippets

```python
class Countdown:
    def __init__(self, start: int) -> None:
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

from itertools import batched
for group in batched(stream(), 100):
    bulk_insert(group)
```

---

## Internals & Gotchas

- `for x in obj` calls `iter(obj)` then repeated `next` until `StopIteration`.
- Custom iterators rarely needed — generators simpler.
- `groupby` only groups consecutive equal keys.

---

## Production Notes

- Batch DB/API calls with iterators + `batched`.
- Avoid materializing large `list(iterator)` at API boundaries.

---

## Interview Probes


{< interview-answer >}
**Q:** iterable vs iterator?

**A:** Iterable can produce multiple iterators (list). Iterator is stateful single-pass cursor. `iter(iterable)` may return new iterator each time.
{< /interview-answer >}

---

## See Also

- [Previous: Generators](/python-cheatsheet/generators/)
- [Next: Context Managers](/python-cheatsheet/context-managers/)
- [Generators](/python-cheatsheet/generators/)
- [Collections](/python-cheatsheet/collections/)
- [Python Cheatsheet Index](/python-cheatsheet/)
