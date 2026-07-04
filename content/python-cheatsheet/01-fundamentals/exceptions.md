---
title: "Exceptions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "try/except, hierarchy, chaining."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Exceptions"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.5"
weight: 115
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/exceptions/"
---

## At a Glance

- Catch specific exceptions — bare `except:` swallows `KeyboardInterrupt`.
- `raise ... from e` preserves exception chain (`__cause__`).
- `else` runs if no exception; `finally` always runs (cleanup).

---

## Reference Tables

| Clause | Runs when |
| :--- | :--- |
| `try` | Always first |
| `except Exc` | Matching exception raised |
| `else` | No exception in try |
| `finally` | Always (unless hard exit) |

| Common base | Examples |
| :--- | :--- |
| `Exception` | Catch app-level errors |
| `ValueError` | Bad value, right type |
| `TypeError` | Wrong type |
| `OSError` / subclasses | IO, network errno |

---

## Snippets

```python
try:
    data = load(path)
except FileNotFoundError as e:
    logger.warning("missing %s", path)
    raise
except json.JSONDecodeError as e:
    raise ConfigError(f"bad json: {path}") from e
else:
    validate(data)
finally:
    release_lock()

class AppError(Exception):
    '''Domain error with optional code.'''
    def __init__(self, message: str, *, code: str = "ERR") -> None:
        super().__init__(message)
        self.code = code
```

---

## Internals & Gotchas

- `ExceptionGroup` / `except*` (3.11+) for multiple errors in async/task groups.
- Don't use exceptions for normal control flow in hot paths.
- `sys.exc_info()` only valid inside except block.

---

## Production Notes

- Map domain errors to HTTP/status at boundary layer only.
- Log with `exc_info=True` once at handler — avoid duplicate stack traces.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Modules](/python-cheatsheet/01-fundamentals/modules/)
- [Next: Typing](/python-cheatsheet/01-fundamentals/typing/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
