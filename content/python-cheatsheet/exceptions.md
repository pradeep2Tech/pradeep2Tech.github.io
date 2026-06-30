---
title: "Exceptions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "try/except/else/finally, exception hierarchy, chaining, and custom types."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Exceptions"
module: 5
moduleTitle: "Advanced Language Features"
sectionRef: "5.1"
ShowToc: true
cheatSheet: true
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

---

## Interview Probes


{< interview-answer >}
**Q:** else vs finally?

**A:** `else` is for code that must not run if try failed. `finally` is unconditional cleanup (close socket, release lock).
{< /interview-answer >}

---

## See Also

- [Previous: Modules](/python-cheatsheet/modules/)
- [Next: Decorators](/python-cheatsheet/decorators/)
- [Context Managers](/python-cheatsheet/context-managers/)
- [Python Cheatsheet Index](/python-cheatsheet/)
