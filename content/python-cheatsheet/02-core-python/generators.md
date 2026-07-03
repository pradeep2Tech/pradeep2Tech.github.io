---
title: "Generators"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "yield, yield from, pipelines."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Generators"
module: 2
moduleTitle: "Core Python"
sectionRef: "2.7"
weight: 207
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/generators/"
---

## At a Glance

- Any function containing `yield` returns a generator iterator when called.
- `yield from subgen` delegates send/throw/close to sub-generator.
- Generators are single-pass — exhaust once unless tee'd/copied.

---

## Reference Tables

| Operation | Effect |
| :--- | :--- |
| `next(g)` | Advance to next `yield` |
| `g.send(v)` | Resume with injected value |
| `g.throw(exc)` | Inject exception at yield point |
| `g.close()` | Raise `GeneratorExit` |

| Use case | Why generator |
| :--- | :--- |
| Streaming parse | Constant memory |
| Pipeline stages | Composable lazy transforms |
| Coroutine (legacy) | Pre-async style — prefer async def |

---

## Snippets

```python
def read_chunks(path, size=65536):
    with open(path, "rb") as f:
        while chunk := f.read(size):
            yield chunk

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# consumer
for line in (ln.strip() for ln in open("log.txt")):
    process(line)
```

---

## Internals & Gotchas

- Generator objects hold frame state — not thread-safe without external sync.
- `return value` in generator becomes `StopIteration.value` (3.3+).
- Don't mix generator coroutines with `async` without understanding semantics.

---

## Production Notes

- Bound generator pipelines with max in-flight work (queues).
- Use `itertools.islice` to peek without full materialize.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Iterators](/python-cheatsheet/02-core-python/iterators/)
- [Next: Comprehensions](/python-cheatsheet/02-core-python/comprehensions/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
