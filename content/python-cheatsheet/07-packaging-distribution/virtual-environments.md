---
title: "Virtual Environments"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "venv, pip, uv, pinning."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Venv"
module: 7
moduleTitle: "Packaging & Distribution"
sectionRef: "7.4"
weight: 704
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/python-cheatsheet/virtual-environments/"
---

## At a Glance

- `python -m venv .venv` creates isolated site-packages and interpreter shim.
- Activate modifies PATH — `source .venv/bin/activate` (Unix) or `.venv\Scripts\activate` (Windows).
- `uv` / `pip-tools` speed up resolve and reproducible installs.

---

## Reference Tables

| Tool | Role |
| :--- | :--- |
| `venv` | Stdlib environment creation |
| `pip` | Install from PyPI/VCS/local |
| `uv` | Fast resolver/installer (Rust) |
| `pip-compile` | Lock requirements.in → .txt |

| Practice | Why |
| :--- | :--- |
| One venv per project | Isolated deps |
| Commit lockfile (apps) | Reproducible deploys |
| `.python-version` / `requires-python` | Document runtime |

---

## Snippets

```bash
python -m venv .venv
# Unix
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -U pip
pip install -e ".[dev]"

# uv alternative
uv venv && uv pip install -e .
```

---

## Internals & Gotchas

- Never commit `.venv/` — add to `.gitignore`.
- System Python on macOS/Linux may be externally managed (PEP 668) — use venv.
- `pip install` into global Python breaks OS tools.

---

## Production Notes

- CI: cache venv or `uv` lock; matrix test `requires-python` lower bound.
- Docker: multi-stage build, install deps before copying source.

---

## Interview Questions




---

---

## See Also

- [Previous: Poetry](/python-cheatsheet/07-packaging-distribution/poetry/)
- [Next: Testing](/python-cheatsheet/08-testing/testing/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
