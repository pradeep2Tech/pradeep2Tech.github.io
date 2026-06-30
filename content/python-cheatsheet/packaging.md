---
title: "Packaging"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "pyproject.toml, setuptools, wheels, entry points, and publishing."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Packaging"
module: 7
moduleTitle: "Runtime & Tooling"
sectionRef: "7.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `pyproject.toml` is canonical project metadata (PEP 621).
- Build backends: `setuptools`, `hatchling`, `flit`, `poetry-core`.
- Wheels (`.whl`) preferred for install speed — sdist for source distribution.

---

## Reference Tables

| File | Role |
| :--- | :--- |
| `pyproject.toml` | Metadata, deps, tool config |
| `src/package/` | Src layout (recommended) |
| `MANIFEST.in` | Extra sdist files (setuptools) |

| Command | Purpose |
| :--- | :--- |
| `pip install -e .` | Editable dev install |
| `python -m build` | Build sdist + wheel |
| `twine upload dist/*` | Publish to PyPI |

---

## Snippets

```toml
[project]
name = "myservice"
version = "1.2.0"
requires-python = ">=3.11"
dependencies = ["httpx>=0.27", "pydantic>=2"]

[project.scripts]
mysvc = "myservice.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

---

## Internals & Gotchas

- Version in one place — dynamic version from VCS with hatch/setuptools-scm.
- Namespace packages don't require `__init__.py` but explicit is clearer.
- Lock files: `uv.lock` / `poetry.lock` for apps, not always for libraries.

---

## Production Notes

- Pin deps in applications; libraries specify ranges.
- Sign tags; use trusted publishing to PyPI (OIDC).

---

## Interview Probes


{< interview-answer >}
**Q:** src layout vs flat?

**A:** Src layout (`src/pkg`) prevents accidental import from repo root during dev — fewer 'works on my machine' packaging bugs.
{< /interview-answer >}

---

## See Also

- [Previous: Memory](/python-cheatsheet/memory-management/)
- [Next: Venv](/python-cheatsheet/virtual-environments/)
- [Venv](/python-cheatsheet/virtual-environments/)
- [Modules](/python-cheatsheet/modules/)
- [Python Cheatsheet Index](/python-cheatsheet/)
