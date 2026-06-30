---
title: "Virtual Environments"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "venv, pip, uv, dependency pinning, and reproducible installs."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Venv"
module: 7
moduleTitle: "Runtime & Tooling"
sectionRef: "7.3"
ShowToc: true
cheatSheet: true
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

## Interview Probes


{< interview-answer >}
**Q:** venv vs conda?

**A:** venv isolates Python packages for a given interpreter. Conda manages binaries and non-Python deps too — heavier, common in data science.
{< /interview-answer >}

---

## See Also

- [Previous: Packaging](/python-cheatsheet/packaging/)
- [Next: Interview](/python-cheatsheet/interview-questions/)
- [Packaging](/python-cheatsheet/packaging/)
- [Python Cheatsheet Index](/python-cheatsheet/)
