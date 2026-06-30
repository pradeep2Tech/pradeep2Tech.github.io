---
title: "Generators"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "yield, yield from, generator pipelines, and memory-efficient iteration."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Generators"
module: 5
moduleTitle: "Advanced Language Features"
sectionRef: "5.3"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** Generator vs list comp?

**A:** Generator expr lazy — O(1) memory. List comp materializes all elements. Choose based on consumer (one pass vs reuse/random access).
{< /interview-answer >}

---

## See Also

- [Previous: Decorators](/python-cheatsheet/decorators/)
- [Next: Iterators](/python-cheatsheet/iterators/)
- [Iterators](/python-cheatsheet/iterators/)
- [Comprehensions](/python-cheatsheet/comprehensions/)
- [Python Cheatsheet Index](/python-cheatsheet/)
