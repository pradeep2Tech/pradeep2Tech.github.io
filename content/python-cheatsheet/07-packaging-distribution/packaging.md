---
title: "Packaging"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "pyproject.toml, wheels, publishing."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Packaging"
module: 7
moduleTitle: "Packaging & Distribution"
sectionRef: "7.1"
weight: 701
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/packaging/"
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



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Production Checklists](/python-cheatsheet/06-production-python/production-checklists/)
- [Next: Dependency Management](/python-cheatsheet/07-packaging-distribution/dependency-management/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
