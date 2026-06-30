---
title: "Python Language Basics"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Syntax, types, literals, operators, control flow, variables, and scope — one-page recap."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Language Basics"
module: 1
moduleTitle: "Language Basics"
sectionRef: "1.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Indentation defines blocks — 4 spaces (PEP 8); no braces.
- Names bind to objects — assignment does not copy unless you explicitly do.
- LEGB scope: Local → Enclosing → Global → Built-in.
- Built-in types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, `None`.

---

## Reference Tables

| Construct | Syntax | Notes |
| :--- | :--- | :--- |
| Assignment | `x = 1` | Rebinding ≠ mutate |
| Comparison chain | `a < b < c` | `a < b and b < c` |
| `if` / `elif` / `else` | Indented blocks | `x if cond else y` |
| `for` / `while` | `for i in iterable:` | Prefer `for` when bounds known |
| `match` (3.10+) | `match x:` / `case` | Structural patterns |
| Walrus `:=` | `if (n := len(xs)) > 0:` | Inside expressions |

| Type | Literal / notes |
| :--- | :--- |
| `int` | `1_000_000`, `0xFF`, unlimited precision |
| `float` | `1.0`, `1e-3` — use `Decimal` for money |
| `str` | `'a'`, triple-quoted strings, f-strings |
| `bool` | `True` / `False` — subclass of `int` |
| `list` | `[1, 2]`, mutable |
| `tuple` | `(1, 2)`, immutable container |
| `dict` | `{"k": v}`, insertion-ordered (3.7+) |
| `set` | `{1, 2}`, unique unordered |
| `None` | Singleton `NoneType` |

| Operator | Meaning |
| :--- | :--- |
| `//` | Floor division |
| `**` | Exponentiation |
| `is` / `is not` | Identity — not value equality |
| `in` | Membership |

| Scope | Rule |
| :--- | :--- |
| `global x` | Rebind module-level name in function |
| `nonlocal x` | Rebind enclosing (non-global) name |
| Unpacking | `a, *rest, z = seq` |

---

## Snippets

```python
# Types & literals
price: float = 19.99
tags: list[str] = ["api", "python"]
config: dict[str, int] = {"retries": 3, "timeout": 30}

# Pattern matching (3.10+)
match command.split():
    case ["quit"]:
        sys.exit(0)
    case ["load", path]:
        load_file(path)
    case _:
        print("unknown")

# Unpacking & scope
x, y, *middle, z = range(5)
```

---

## Internals & Gotchas

- `==` vs `is` — use `is` only for `None`, `True`, `False`.
- Default mutable args (`def f(xs=[])`) created once — use `None` sentinel.
- Tuple of mutables can still change contents.

---

## Production Notes

- Pin `requires-python` in `pyproject.toml`.
- Use `ruff` / Black in CI.

---

## Interview Probes


{< interview-answer >}
**Q:** What is truthy?

**A:** Falsy: `None`, `False`, `0`, ``, `[]`, `{}`, `set()`.
{< /interview-answer >}

---

## See Also

- [Next: Functions](/python-cheatsheet/functions/)
- [Python Cheatsheet Index](/python-cheatsheet/)
