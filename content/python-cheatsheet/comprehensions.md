---
title: "Comprehensions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "List/dict/set comprehensions and generator expressions — readability vs performance."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Comprehensions"
module: 2
moduleTitle: "Collections & Comprehensions"
sectionRef: "2.2"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** List comp vs map/filter?

**A:** Comprehensions are idiomatic and often faster to read. `map`/`filter` shine with existing callables and lazy iterators.
{< /interview-answer >}

---

## See Also

- [Previous: Collections](/python-cheatsheet/collections/)
- [Next: Classes](/python-cheatsheet/classes/)
- [Generators](/python-cheatsheet/generators/)
- [Collections](/python-cheatsheet/collections/)
- [Python Cheatsheet Index](/python-cheatsheet/)
