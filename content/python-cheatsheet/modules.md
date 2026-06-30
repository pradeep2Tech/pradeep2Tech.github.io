---
title: "Modules & Imports"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "import styles, __name__, packages, __init__.py, and circular import mitigation."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Modules"
module: 4
moduleTitle: "Modules & Packages"
sectionRef: "4.1"
ShowToc: true
cheatSheet: true
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
- Namespace packages: multiple dirs on `sys.path` contribute to same package.

---

## Production Notes

- Explicit public API via `__all__` and stable import paths.
- Lazy imports in CLI cold-start paths to reduce startup time.

---

## Interview Probes


{< interview-answer >}
**Q:** Relative vs absolute imports?

**A:** Absolute (`from mypkg.utils import x`) preferred for clarity. Relative for intra-package without hardcoding top-level name.
{< /interview-answer >}

---

## See Also

- [Previous: OOP](/python-cheatsheet/oop/)
- [Next: Exceptions](/python-cheatsheet/exceptions/)
- [Packaging](/python-cheatsheet/packaging/)
- [Venv](/python-cheatsheet/virtual-environments/)
- [Python Cheatsheet Index](/python-cheatsheet/)
