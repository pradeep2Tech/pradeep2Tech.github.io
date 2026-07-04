---
title: "Modules & Imports"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "import styles, packages, __main__ guard."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Modules"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.4"
weight: 114
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/modules/"
---

## At a Glance

- `import pkg.mod` vs `from pkg import mod` — latter binds name in current namespace.
- `if __name__ == '__main__':` guards script-only execution.
- Packages are directories with `__init__.py` (still recommended) or namespace packages (PEP 420).

---

## Reference Tables

| Import style | Effect |
| :--- | :--- |
| `import os` | Bind `os` module object |
| `import os.path as osp` | Alias |
| `from os import path` | Bind `path` into namespace |
| `from . import sibling` | Relative (package context) |
| `from ..pkg import x` | Parent package relative |

| File | Purpose |
| :--- | :--- |
| `__init__.py` | Package marker; re-exports |
| `__all__` | Public API for `from pkg import *` |
| `__name__` | Module name; `__main__` when run as script |

---

## Snippets

```python
# package/__init__.py — facade pattern
from .core import connect
__all__ = ["connect"]

# relative import inside package
from .utils import normalize

if __name__ == "__main__":
    main()
```

---

## Internals & Gotchas

- Circular imports: defer import inside function or extract shared types to third module.
- `import *` pollutes namespace — avoid except in `__init__.py` facades.
- Import system internals (finders, loaders): [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/).

---

## Production Notes

- Explicit public API via `__all__` and stable import paths.
- Lazy imports in CLI cold-start paths to reduce startup time.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Collections](/python-cheatsheet/01-fundamentals/collections/)
- [Next: Exceptions](/python-cheatsheet/01-fundamentals/exceptions/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
