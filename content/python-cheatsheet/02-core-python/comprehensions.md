---
title: "Comprehensions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "List/dict/set/gen expressions."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Comprehensions"
module: 2
moduleTitle: "Core Python"
sectionRef: "2.8"
weight: 208
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/comprehensions/"
---

## At a Glance

- List/dict/set comprehensions build collections; generator expressions are lazy.
- Prefer comprehensions for simple transforms; switch to loop for complex logic.
- Nested comprehensions read right-to-left — flatten with intermediate generator when unclear.

---

## Reference Tables

| Form | Syntax | Eager/Lazy |
| :--- | :--- | :--- |
| List | `[f(x) for x in xs if p(x)]` | Eager |
| Dict | `{k: v for k, v in pairs}` | Eager |
| Set | `{x for x in xs}` | Eager |
| Generator | `(f(x) for x in xs)` | Lazy |

| Guideline | Reason |
| :--- | :--- |
| Max 2 clauses | Readability |
| No side effects inside | Surprising order/duplication |
| Use gen expr for large streams | Memory |

---

## Snippets

```python
squares = [n * n for n in range(10) if n % 2]
index = {name: i for i, name in enumerate(names)}
unique_lengths = {len(w) for w in words}

# generator — sum without building list
total = sum(x * x for x in huge_iterable)

# dict comp from two iterables
mapping = {k: v for k, v in zip(keys, values) if v is not None}
```

---

## Internals & Gotchas

- Comprehension scope isolates loop variables (Py3).
- Walrus in comprehension (3.8+): `[y for x in data if (y := f(x)) > 0]`.
- Set comp deduplicates — don't rely on order.

---

## Production Notes

- Profile before micro-optimizing — gen expr wins on memory, not always CPU.
- Log pipelines: build explicit stages for observability.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Generators](/python-cheatsheet/02-core-python/generators/)
- [Next: Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
