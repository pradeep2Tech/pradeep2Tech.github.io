---
title: "Iterators & Iterables"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "__iter__/__next__, itertools."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Iterators"
module: 2
moduleTitle: "Core Python"
sectionRef: "2.6"
weight: 206
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/iterators/"
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



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Context Managers](/python-cheatsheet/02-core-python/context-managers/)
- [Next: Generators](/python-cheatsheet/02-core-python/generators/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
