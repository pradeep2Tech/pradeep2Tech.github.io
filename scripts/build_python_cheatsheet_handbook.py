"""Build Python Cheatsheet pages from data/python_cheatsheet_modules.yaml."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import NamedTuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "python-cheatsheet"
DATE = "2026-06-30T10:00:00+00:00"

TOPIC_META: dict[str, tuple[str, str, str]] = {
    "language-basics": (
        "Python Language Basics",
        "Language Basics",
        "Syntax, types, literals, operators, control flow, variables, and scope — one-page recap.",
    ),
    "functions": (
        "Functions",
        "Functions",
        "def, args, *args/**kwargs, lambdas, closures, and functools patterns.",
    ),
    "collections": (
        "Collections",
        "Collections",
        "list, tuple, dict, set, deque — mutability, complexity, and when to pick each.",
    ),
    "comprehensions": (
        "Comprehensions",
        "Comprehensions",
        "List/dict/set comprehensions and generator expressions — readability vs performance.",
    ),
    "classes": (
        "Classes",
        "Classes",
        "__init__, attributes, properties, __slots__, and class vs instance namespaces.",
    ),
    "oop": (
        "OOP in Python",
        "OOP",
        "Inheritance, MRO, super(), dunder methods, ABCs, and composition patterns.",
    ),
    "modules": (
        "Modules & Imports",
        "Modules",
        "import styles, __name__, packages, __init__.py, and circular import mitigation.",
    ),
    "exceptions": (
        "Exceptions",
        "Exceptions",
        "try/except/else/finally, exception hierarchy, chaining, and custom types.",
    ),
    "decorators": (
        "Decorators",
        "Decorators",
        "@syntax, functools.wraps, parameterized decorators, and class decorators.",
    ),
    "generators": (
        "Generators",
        "Generators",
        "yield, yield from, generator pipelines, and memory-efficient iteration.",
    ),
    "iterators": (
        "Iterators & Iterables",
        "Iterators",
        "__iter__/__next__, StopIteration, itertools, and lazy evaluation.",
    ),
    "context-managers": (
        "Context Managers",
        "Context Managers",
        "with statement, __enter__/__exit__, contextlib, and resource cleanup.",
    ),
    "typing": (
        "Typing",
        "Typing",
        "Annotations, generics, Protocol, TypeAlias, Literal, and runtime checking.",
    ),
    "dataclasses": (
        "Dataclasses",
        "Dataclasses",
        "@dataclass options, field(), frozen, slots, and vs NamedTuple/Pydantic.",
    ),
    "concurrency": (
        "Concurrency Overview",
        "Concurrency",
        "GIL, I/O vs CPU-bound, choosing asyncio vs threads vs processes.",
    ),
    "asyncio": (
        "Asyncio",
        "Asyncio",
        "async/await, event loop, tasks, gather, timeouts, and async context managers.",
    ),
    "multithreading": (
        "Multithreading",
        "Multithreading",
        "threading module, locks, queues, GIL impact, and when threads help.",
    ),
    "multiprocessing": (
        "Multiprocessing",
        "Multiprocessing",
        "Process pools, shared memory, spawn/fork, and CPU-bound parallelism.",
    ),
    "memory-management": (
        "Memory Management",
        "Memory",
        "Reference counting, gc module, weakref, __slots__, and profiling leaks.",
    ),
    "packaging": (
        "Packaging",
        "Packaging",
        "pyproject.toml, setuptools, wheels, entry points, and publishing.",
    ),
    "virtual-environments": (
        "Virtual Environments",
        "Venv",
        "venv, pip, uv, dependency pinning, and reproducible installs.",
    ),
    "interview-questions": (
        "Python Interview Questions",
        "Interview",
        "High-yield Python probes — GIL, MRO, decorators, mutability, and asyncio.",
    ),
}

EXTRA_RELATED: dict[str, list[str]] = {
    "syntax": ["variables", "functions"],
    "variables": ["syntax", "collections"],
    "functions": ["decorators", "comprehensions"],
    "collections": ["comprehensions", "iterators"],
    "comprehensions": ["generators", "collections"],
    "classes": ["oop", "dataclasses"],
    "oop": ["classes", "typing"],
    "modules": ["packaging", "virtual-environments"],
    "exceptions": ["context-managers"],
    "decorators": ["functions", "context-managers"],
    "generators": ["iterators", "comprehensions"],
    "iterators": ["generators", "collections"],
    "context-managers": ["exceptions", "decorators"],
    "typing": ["dataclasses", "classes"],
    "dataclasses": ["classes", "typing"],
    "concurrency": ["asyncio", "multithreading", "multiprocessing"],
    "asyncio": ["concurrency", "multithreading"],
    "multithreading": ["concurrency", "multiprocessing"],
    "multiprocessing": ["concurrency", "memory-management"],
    "memory-management": ["collections", "generators"],
    "packaging": ["virtual-environments", "modules"],
    "virtual-environments": ["packaging"],
}


def flatten_topics(modules: list) -> list[str]:
    topics: list[str] = []
    for mod in modules:
        if mod.get("groups"):
            for group in mod["groups"]:
                topics.extend(group["topics"])
        else:
            topics.extend(mod["topics"])
    return topics


def iter_module_topics(modules: list) -> list[tuple[int, str, str, int]]:
    result: list[tuple[int, str, str, int]] = []
    for mod in modules:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        slugs = flatten_topics([mod])
        for idx, slug in enumerate(slugs, start=1):
            result.append((mod_id, mod_title, slug, idx))
    return result


def write_order_yaml(topics: list[str], path: Path) -> None:
    header = (
        "# Flat topic order — derived from python_cheatsheet_modules.yaml.\n"
        "# Prefer editing data/python_cheatsheet_modules.yaml for module structure.\n"
        "topics:\n"
    )
    path.write_text(header + "".join(f"  - {s}\n" for s in topics), encoding="utf-8")


def interview_block(q: str, a: str) -> str:
    return f"""{{< interview-answer >}}
**Q:** {q}

**A:** {a}
{{< /interview-answer >}}"""


def page_body(
    glance: list[str],
    tables: str,
    snippets: str = "",
    internals: str = "",
    production: str = "",
    interviews: list[tuple[str, str]] | None = None,
    see_also: str = "",
) -> str:
    sections = [
        "## At a Glance",
        "",
        "\n".join(f"- {b}" for b in glance),
        "",
        "---",
        "",
        "## Reference Tables",
        "",
        tables.strip(),
    ]
    if snippets.strip():
        sections.extend(["", "---", "", "## Snippets", "", snippets.strip()])
    sections.extend(["", "---", "", "## Internals & Gotchas", "", internals.strip()])
    sections.extend(["", "---", "", "## Production Notes", "", production.strip()])
    if interviews:
        sections.extend(["", "---", "", "## Interview Probes", ""])
        for q, a in interviews:
            sections.extend(["", interview_block(q, a)])
    sections.extend(["", "---", "", "## See Also", "", see_also.strip()])
    return "\n".join(sections) + "\n"


def see_also_links(slug: str, ordered: list[str]) -> str:
    links: list[str] = []
    idx = ordered.index(slug)
    if idx > 0:
        prev = ordered[idx - 1]
        links.append(f"- [Previous: {TOPIC_META[prev][1]}](/python-cheatsheet/{prev}/)")
    if idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        links.append(f"- [Next: {TOPIC_META[nxt][1]}](/python-cheatsheet/{nxt}/)")
    for rel in EXTRA_RELATED.get(slug, []):
        if rel in TOPIC_META:
            links.append(f"- [{TOPIC_META[rel][1]}](/python-cheatsheet/{rel}/)")
    links.append("- [Python Cheatsheet Index](/python-cheatsheet/)")
    return "\n".join(links)


def front_matter(slug: str, mod_id: int, mod_title: str, topic_idx: int) -> str:
    title, short, desc = TOPIC_META[slug]
    return f"""---
title: "{title}"
date: {DATE}
draft: false
description: "{desc}"
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{mod_id}.{topic_idx}"
cheatSheet: true
---

"""


def normalize(body: str) -> str:
    return body.strip() + "\n"


class TopicSpec(NamedTuple):
    glance: list[str]
    tables: str
    snippets: str
    internals: str
    production: str
    interviews: list[tuple[str, str]] | None


PAGE_BODIES: dict[str, TopicSpec] = {}


def topic(
    glance: list[str],
    tables: str,
    snippets: str = "",
    internals: str = "",
    production: str = "",
    interviews: list[tuple[str, str]] | None = None,
) -> TopicSpec:
    return TopicSpec(glance, tables, snippets, internals, production, interviews)


PAGE_BODIES["language-basics"] = topic(
    [
        "Indentation defines blocks — 4 spaces (PEP 8); no braces.",
        "Names bind to objects — assignment does not copy unless you explicitly do.",
        "LEGB scope: Local → Enclosing → Global → Built-in.",
        "Built-in types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, `None`.",
    ],
    """| Construct | Syntax | Notes |
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
| Unpacking | `a, *rest, z = seq` |""",
    """```python
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
```""",
    "- `==` vs `is` — use `is` only for `None`, `True`, `False`.\n- Default mutable args (`def f(xs=[])`) created once — use `None` sentinel.\n- Tuple of mutables can still change contents.",
    "- Pin `requires-python` in `pyproject.toml`.\n- Use `ruff` / Black in CI.",
    [("What is truthy?", "Falsy: `None`, `False`, `0`, `""`, `[]`, `{}`, `set()`.")],
)

PAGE_BODIES["functions"] = topic(
    [
        "Functions are first-class — assign, pass, return, store in collections.",
        "`*args` tuple, `**kwargs` dict — only in definition signature position.",
        "Use type hints on public APIs; defaults evaluated once at def time.",
    ],
    """| Parameter kind | Syntax | Example |
| :--- | :--- | :--- |
| Positional-only | `/ before ` | `def f(a, b, /, c):` |
| Keyword-only | `*` separator | `def f(a, *, b):` |
| Var positional | `*args` | Extra positional args |
| Var keyword | `**kwargs` | Extra keyword args |

| Tool | Use |
| :--- | :--- |
| `functools.partial` | Pre-fill arguments |
| `functools.lru_cache` | Memoize pure calls |
| `functools.singledispatch` | Type-based overload |""",
    """```python
def connect(host: str, port: int = 443, *, timeout: float = 5.0) -> None:
    ...

def apply(fn, /, *args, **kwargs):
    return fn(*args, **kwargs)

# Lambda — single expression only
key_fn = lambda r: (r.priority, r.created_at)

@lru_cache(maxsize=128)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```""",
    "- Closures capture variables by reference — late-binding loop variable trap in lambdas.\n- Recursive depth limited by stack — tail recursion not optimized.\n- `return` in generator makes it a generator function (contains `yield`).",
    "- Keep signatures stable; use keyword-only for new optional params.\n- Document exceptions raised; don't catch-all inside library helpers.",
    [("Why avoid mutable default args?", "Default values are evaluated once at function definition. A shared list/dict mutates across calls. Idiom: `def f(xs=None): xs = [] if xs is None else xs`.")],
)

PAGE_BODIES["collections"] = topic(
    [
        "`list` ordered mutable; `tuple` ordered immutable; `dict` insertion-ordered (3.7+).",
        "`set`/`frozenset` — hashable unique elements; `frozenset` is immutable/hashable.",
        "Pick by access pattern and concurrency needs — no single 'best' collection.",
    ],
    """| Type | Ordered | Mutable | Hashable | Typical ops |
| :--- | :---: | :---: | :---: | :--- |
| `list` | ✓ | ✓ | ✗ | index O(1), insert mid O(n) |
| `tuple` | ✓ | ✗ | ✓* | fixed records, dict keys |
| `dict` | ✓ | ✓ | ✗ | get/set avg O(1) |
| `set` | ✗ | ✓ | ✗ | membership O(1) avg |
| `deque` | ✓ | ✓ | ✗ | O(1) append/pop both ends |

*Tuple hashable only if all elements hashable.""",
    """```python
from collections import defaultdict, Counter, deque

counts = Counter(tokens)
by_user: dict[str, list] = defaultdict(list)
queue: deque[str] = deque(maxlen=1000)

# dict merge (3.9+)
merged = base | overrides

# structural sharing — cheap copies
view = existing_dict | {"k": "v"}
```""",
    "- `list.sort()` in-place; `sorted()` returns new list.\n- Dict keys must be hashable; values can be anything.\n- `is` not valid for deep equality — use `==` or `dataclasses`/`pydantic`.",
    "- Use `collections.deque` for bounded in-memory buffers.\n- For large numeric arrays prefer `numpy` or `array.array` — not plain lists.",
    [("dict vs OrderedDict today?", "Built-in `dict` preserves insertion order since 3.7 (guaranteed 3.7+). `OrderedDict` still useful for `move_to_end` and equality ignoring order.")],
)

PAGE_BODIES["comprehensions"] = topic(
    [
        "List/dict/set comprehensions build collections; generator expressions are lazy.",
        "Prefer comprehensions for simple transforms; switch to loop for complex logic.",
        "Nested comprehensions read right-to-left — flatten with intermediate generator when unclear.",
    ],
    """| Form | Syntax | Eager/Lazy |
| :--- | :--- | :--- |
| List | `[f(x) for x in xs if p(x)]` | Eager |
| Dict | `{k: v for k, v in pairs}` | Eager |
| Set | `{x for x in xs}` | Eager |
| Generator | `(f(x) for x in xs)` | Lazy |

| Guideline | Reason |
| :--- | :--- |
| Max 2 clauses | Readability |
| No side effects inside | Surprising order/duplication |
| Use gen expr for large streams | Memory |""",
    """```python
squares = [n * n for n in range(10) if n % 2]
index = {name: i for i, name in enumerate(names)}
unique_lengths = {len(w) for w in words}

# generator — sum without building list
total = sum(x * x for x in huge_iterable)

# dict comp from two iterables
mapping = {k: v for k, v in zip(keys, values) if v is not None}
```""",
    "- Comprehension scope isolates loop variables (Py3).\n- Walrus in comprehension (3.8+): `[y for x in data if (y := f(x)) > 0]`.\n- Set comp deduplicates — don't rely on order.",
    "- Profile before micro-optimizing — gen expr wins on memory, not always CPU.\n- Log pipelines: build explicit stages for observability.",
    [("List comp vs map/filter?", "Comprehensions are idiomatic and often faster to read. `map`/`filter` shine with existing callables and lazy iterators.")],
)

PAGE_BODIES["classes"] = topic(
    [
        "Instance `__dict__` holds attributes unless `__slots__` restricts.",
        "`@property` for computed/validated fields; `@classmethod` / `@staticmethod` for alternate constructors.",
        "Dataclasses (see dedicated page) reduce boilerplate for data carriers.",
    ],
    """| Member | First arg | Typical use |
| :--- | :--- | :--- |
| Instance method | `self` | Behavior on instance |
| `@classmethod` | `cls` | Factory, alt constructors |
| `@staticmethod` | none | Namespaced helper |
| `@property` | `self` | Getter/setter/deleter |

| Dunder | Role |
| :--- | :--- |
| `__init__` | Initialize (not allocate) |
| `__repr__` / `__str__` | Debug vs user string |
| `__eq__` / `__hash__` | Equality contract |""",
    """```python
class User:
    __slots__ = ("id", "email")  # no per-instance __dict__

    def __init__(self, id: int, email: str) -> None:
        self.id = id
        self.email = email

    @classmethod
    def from_row(cls, row: dict) -> "User":
        return cls(row["id"], row["email"])

    @property
    def domain(self) -> str:
        return self.email.split("@", 1)[1]
```""",
    "- Defining `__eq__` without `__hash__` makes instances unhashable (hash set to None).\n- `__init__` ≠ `__new__` — latter controls instance creation (singletons, immutables).\n- Name mangling: `__private` → `_ClassName__private` (not security).",
    "- Keep domain logic on entities; avoid anemic models only when ORM demands it.\n- Use `__slots__` on high-volume objects after profiling memory.",
    [("When use __slots__?", "When you have millions of small instances and memory dominates. Trade-off: no arbitrary attributes, subclasses must declare slots too.")],
)

PAGE_BODIES["oop"] = topic(
    [
        "Multiple inheritance supported — MRO (C3 linearization) resolves method lookup.",
        "`super()` follows MRO, not just parent class — critical in diamonds.",
        "Prefer composition + Protocol typing over deep inheritance hierarchies.",
    ],
    """| Pattern | Mechanism |
| :--- | :--- |
| Inheritance | `class Child(Parent):` |
| MRO | `Child.__mro__` or `help(Child)` |
| Abstract base | `abc.ABC` + `@abstractmethod` |
| Protocol (structural) | `typing.Protocol` — duck typing with types |
| Mixins | Small orthogonal parent classes |

```mermaid
flowchart TD
  C[Child] --> P1[ParentA]
  C --> P2[ParentB]
  P1 --> O[object]
  P2 --> O
```

""",
    """```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, id: str) -> object: ...

class LoggingMixin:
    def log(self, msg: str) -> None:
        print(msg)

class Service(LoggingMixin):
    def run(self) -> None:
        self.log("start")

# cooperative super in multiple inheritance
class A:
    def method(self): return "A" + super().method()
```""",
    "- `super()` in `__init__` must be called in cooperative multiple inheritance.\n- Mixins should not define `__init__` without accepting `**kwargs`.\n- `isinstance(x, Protocol)` works with `@runtime_checkable` only.",
    "- Favor small ABCs at integration boundaries (ports).\n- Document extension points; seal internal classes with leading `_`.",
    [("Explain MRO briefly.", "C3 linearization orders base classes so each class appears before its parents and order is consistent across the hierarchy. Method lookup walks `__mro__`.")],
)

PAGE_BODIES["modules"] = topic(
    [
        "`import pkg.mod` vs `from pkg import mod` — latter binds name in current namespace.",
        "`if __name__ == '__main__':` guards script-only execution.",
        "Packages are directories with `__init__.py` (still recommended) or namespace packages (PEP 420).",
    ],
    """| Import style | Effect |
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
| `__name__` | Module name; `__main__` when run as script |""",
    """```python
# package/__init__.py — facade pattern
from .core import connect
__all__ = ["connect"]

# relative import inside package
from .utils import normalize

if __name__ == "__main__":
    main()
```""",
    "- Circular imports: defer import inside function or extract shared types to third module.\n- `import *` pollutes namespace — avoid except in `__init__.py` facades.\n- Namespace packages: multiple dirs on `sys.path` contribute to same package.",
    "- Explicit public API via `__all__` and stable import paths.\n- Lazy imports in CLI cold-start paths to reduce startup time.",
    [("Relative vs absolute imports?", "Absolute (`from mypkg.utils import x`) preferred for clarity. Relative for intra-package without hardcoding top-level name.")],
)

PAGE_BODIES["exceptions"] = topic(
    [
        "Catch specific exceptions — bare `except:` swallows `KeyboardInterrupt`.",
        "`raise ... from e` preserves exception chain (`__cause__`).",
        "`else` runs if no exception; `finally` always runs (cleanup).",
    ],
    """| Clause | Runs when |
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
| `OSError` / subclasses | IO, network errno |""",
    """```python
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
```""",
    "- `ExceptionGroup` / `except*` (3.11+) for multiple errors in async/task groups.\n- Don't use exceptions for normal control flow in hot paths.\n- `sys.exc_info()` only valid inside except block.",
    "- Map domain errors to HTTP/status at boundary layer only.\n- Log with `exc_info=True` once at handler — avoid duplicate stack traces.",
    [("else vs finally?", "`else` is for code that must not run if try failed. `finally` is unconditional cleanup (close socket, release lock).")],
)

PAGE_BODIES["decorators"] = topic(
    [
        "Decorators are callables transforming callables — syntactic sugar for `f = dec(f)`.",
        "Use `@functools.wraps(fn)` to preserve `__name__` and `__doc__`.",
        "Stack bottom-up: `@a @b def f` → `f = a(b(f))`.",
    ],
    """| Pattern | Sketch |
| :--- | :--- |
| Simple | `def deco(fn): ... return wrapper` |
| Parametrized | `def deco(arg): def inner(fn): ...` |
| Class decorator | Callable class with `__call__` |
| `classmethod` | Descriptor decorating functions in class body |

| stdlib | Role |
| :--- | :--- |
| `functools.wraps` | Metadata preservation |
| `functools.lru_cache` | Caching decorator |
| `contextlib.contextmanager` | Generator → context manager |""",
    """```python
from functools import wraps

def retry(times: int):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for _ in range(times):
                try:
                    return fn(*args, **kwargs)
                except TransientError as e:
                    last = e
            raise last
        return wrapper
    return decorator

@retry(3)
def fetch():
    ...
```""",
    "- Decorators run at import/definition time — heavy work slows module load.\n- Stacked decorators: inner applied first.\n- `staticmethod`/`classmethod` are descriptor decorators, not plain wrappers.",
    "- Idempotent decorators for testability (detect if already wrapped).\n- Type checkers need `ParamSpec`/`TypeVar` on generic decorators.",
    [("How does @decorator work?", " `@deco` on `def f` is `f = deco(f)`. `deco` receives the function object and returns the replacement (usually a wrapper).")],
)

PAGE_BODIES["generators"] = topic(
    [
        "Any function containing `yield` returns a generator iterator when called.",
        "`yield from subgen` delegates send/throw/close to sub-generator.",
        "Generators are single-pass — exhaust once unless tee'd/copied.",
    ],
    """| Operation | Effect |
| :--- | :--- |
| `next(g)` | Advance to next `yield` |
| `g.send(v)` | Resume with injected value |
| `g.throw(exc)` | Inject exception at yield point |
| `g.close()` | Raise `GeneratorExit` |

| Use case | Why generator |
| :--- | :--- |
| Streaming parse | Constant memory |
| Pipeline stages | Composable lazy transforms |
| Coroutine (legacy) | Pre-async style — prefer async def |""",
    """```python
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
```""",
    "- Generator objects hold frame state — not thread-safe without external sync.\n- `return value` in generator becomes `StopIteration.value` (3.3+).\n- Don't mix generator coroutines with `async` without understanding semantics.",
    "- Bound generator pipelines with max in-flight work (queues).\n- Use `itertools.islice` to peek without full materialize.",
    [("Generator vs list comp?", "Generator expr lazy — O(1) memory. List comp materializes all elements. Choose based on consumer (one pass vs reuse/random access).")],
)

PAGE_BODIES["iterators"] = topic(
    [
        "Iterable has `__iter__`; iterator has `__iter__` returning self and `__next__`.",
        "`StopIteration` ends iteration — don't catch it outside iterator protocol.",
        "`itertools` provides memory-efficient combinatorial utilities.",
    ],
    """| Object | Protocol |
| :--- | :--- |
| Iterable | `__iter__()` returns iterator |
| Iterator | `__iter__()` + `__next__()` |
| Sequence | `__getitem__` + length |

| itertools | Purpose |
| :--- | :--- |
| `chain` | Flatten iterables |
| `groupby` | Adjacent grouping (sort first!) |
| `islice` | Lazy slice |
| `batched` (3.12+) | Fixed-size chunks |""",
    """```python
class Countdown:
    def __init__(self, start: int) -> None:
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

from itertools import batched
for group in batched(stream(), 100):
    bulk_insert(group)
```""",
    "- `for x in obj` calls `iter(obj)` then repeated `next` until `StopIteration`.\n- Custom iterators rarely needed — generators simpler.\n- `groupby` only groups consecutive equal keys.",
    "- Batch DB/API calls with iterators + `batched`.\n- Avoid materializing large `list(iterator)` at API boundaries.",
    [("iterable vs iterator?", "Iterable can produce multiple iterators (list). Iterator is stateful single-pass cursor. `iter(iterable)` may return new iterator each time.")],
)

PAGE_BODIES["context-managers"] = topic(
    [
        "`with` calls `__enter__` / `__exit__` — exceptions propagate unless `__exit__` returns True.",
        "`contextlib.contextmanager` turns generator into CM (yield once).",
        "`contextlib.ExitStack` manages dynamic number of contexts.",
    ],
    """| API | Role |
| :--- | :--- |
| `__enter__` | Setup; return bound resource |
| `__exit__(exc_type, exc, tb)` | Teardown; return True to suppress |
| `@contextmanager` | Generator-based CM |
| `AsyncContextManager` | `async with` |

| stdlib CM | Resource |
| :--- | :--- |
| `open()` | Files |
| `threading.Lock` | Locks |
| `decimal.localcontext` | Context vars |""",
    """```python
from contextlib import contextmanager, ExitStack

@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        logger.info("%s %.3fs", label, time.perf_counter() - start)

with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in paths]
    merge(files)
```""",
    "- `__exit__` runs even if `__enter__` failed (if object partially constructed).\n- Don't yield twice in `@contextmanager`.\n- Suppressing exceptions in `__exit__` hides bugs — rare.",
    "- Always use `with open(...)` — never bare `open` without close.\n- Nest `with` or `ExitStack` for transactions + files + locks.",
    [("contextmanager vs class CM?", "Generator style concise for simple setup/teardown. Class when complex state or reusable configurable manager.")],
)

PAGE_BODIES["typing"] = topic(
    [
        "Annotations are not enforced at runtime by default — use mypy/pyright.",
        "3.9+ built-in generics: `list[str]`, `dict[str, int]` — prefer over `typing.List`.",
        "`Protocol` for structural subtyping; `TypeVar` for generics.",
    ],
    """| Construct | Example |
| :--- | :--- |
| Union | `str | int` or `Union[str, int]` |
| Optional | `str | None` |
| Callable | `Callable[[int], str]` |
| TypeVar | `T = TypeVar('T')` |
| ParamSpec | Decorator preserving signature |
| Literal | `Literal['GET', 'POST']` |
| Final | `Final[int] = 42` |

| Tool | Role |
| :--- | :--- |
| mypy / pyright | Static check |
| `typing.get_type_hints` | Runtime introspection |""",
    """```python
from typing import Protocol, TypeVar, Generic

class SupportsClose(Protocol):
    def close(self) -> None: ...

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

def first(items: list[T]) -> T:
    return items[0]
```""",
    "- `from __future__ import annotations` postpones evaluation (PEP 563 behavior in 3.11+ evolving).\n- `Any` disables checking — use narrowly.\n- `TypedDict` for dict shapes; not runtime validated.",
    "- Type public APIs; run pyright in CI on library code.\n- Align Pydantic models at HTTP boundary with internal TypedDict/dataclass.",
    [("Protocol vs ABC?", "Protocol is structural (duck typing with types) — no inheritance required. ABC is nominal — must subclass explicitly.")],
)

PAGE_BODIES["dataclasses"] = topic(
    [
        "`@dataclass` auto-generates `__init__`, `__repr__`, comparisons (optional).",
        "`field(default_factory=list)` for mutable defaults.",
        "`frozen=True` makes instances immutable and hashable (if fields hashable).",
    ],
    """| Option | Effect |
| :--- | :--- |
| `frozen=True` | Immutable; defines `__setattr__` |
| `slots=True` (3.10+) | `__slots__` + smaller instances |
| `kw_only=True` (3.10+) | All fields keyword-only |
| `order=True` | Rich comparisons |
| `repr=False` | Skip auto repr |

| vs | When |
| :--- | :--- |
| `NamedTuple` | Lightweight immutable tuples |
| Pydantic | Validation + serialization at boundary |
| attrs | Heavier feature set, similar niche |""",
    """```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float

@dataclass
class Session:
    user_id: str
    roles: list[str] = field(default_factory=list)
    _token: str = field(repr=False, compare=False)
```""",
    "- Field order: non-default before default fields.\n- `__post_init__` for validation after init.\n- `dataclass` not a drop-in for ORM entities with lazy loading.",
    "- Use frozen dataclasses as immutable value objects in domain layer.\n- Serialize with `dataclasses.asdict` only for simple trees — watch cycles.",
    [("dataclass vs dict?", "Dataclass gives typed fields, repr, eq, and IDE support. Dict flexible but error-prone keys and no structure.")],
)

PAGE_BODIES["concurrency"] = topic(
    [
        "CPython GIL: one thread executes Python bytecode at a time per process.",
        "I/O-bound → `asyncio` or threads; CPU-bound → `multiprocessing` or native extensions.",
        "Mix models carefully — blocking call in async event loop stalls all tasks.",
    ],
    """| Model | Best for | GIL impact |
| :--- | :--- | :--- |
| `asyncio` | Many concurrent I/O waits | N/A (single thread) |
| `threading` | Blocking I/O libraries | Limited CPU parallelism |
| `multiprocessing` | CPU-bound Python code | Bypass GIL (separate interpreters) |
| `concurrent.futures` | Unified pool API | Thread or process executor |

```mermaid
flowchart LR
  IO[I/O bound] --> async[asyncio / threads]
  CPU[CPU bound] --> mp[multiprocessing / Rust/C ext]
```

""",
    """```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(fetch, url) for url in urls]
    for fut in as_completed(futures):
        handle(fut.result())
```""",
    "- Async is not faster CPU — it's better scheduling of wait time.\n- Thread safety: protect shared mutable state with locks or lock-free structures.\n- `asyncio.run()` creates/closes event loop — entry point for scripts.",
    "- Offload blocking IO with `asyncio.to_thread` (3.9+) in async apps.\n- Size thread pools from downstream limits (DB connections, API rate).",
    [("When does GIL release?", "Around I/O, many C extension calls, and periodically via bytecode tick — don't rely on tick for correctness.")],
)

PAGE_BODIES["asyncio"] = topic(
    [
        "Coroutines (`async def`) are awaitable; don't call without `await` or `create_task`.",
        "Event loop schedules tasks — one thread default; use `asyncio.run` as main entry.",
        "Prefer `asyncio.TaskGroup` (3.11+) over bare `gather` for structured concurrency.",
    ],
    """| API | Role |
| :--- | :--- |
| `await coro` | Suspend until complete |
| `create_task` | Schedule concurrent coroutine |
| `gather` | Wait for multiple awaitables |
| `TaskGroup` | Structured task tree; cancel siblings on error |
| `wait_for` / `timeout` | Deadline control |
| `Semaphore` | Limit concurrency |

| Pitfall | Fix |
| :--- | :--- |
| Blocking `time.sleep` | `await asyncio.sleep` |
| Sync HTTP lib | `httpx.AsyncClient` or `to_thread` |""",
    """```python
import asyncio

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker("a"))
        tg.create_task(worker("b"))

async def worker(name: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api/{name}")
        return r.json()

asyncio.run(main())
```""",
    "- Un-awaited coroutine warning — silent bug.\n- Loop per thread — don't share across threads without `asyncio.run_coroutine_threadsafe`.\n- Cancellation raises `CancelledError` — clean up in `finally`.",
    "- Set global HTTP client session limits; reuse connections.\n- Propagate tracing context with `contextvars`.",
    [("asyncio vs threads for 1000 HTTP calls?", "Asyncio: one thread, low memory, explicit async APIs. Threads: simpler with blocking libs but higher memory and GIL context switching.")],
)

PAGE_BODIES["multithreading"] = topic(
    [
        "`threading.Thread` for OS threads; prefer `ThreadPoolExecutor` for pools.",
        "Use `queue.Queue` for producer-consumer — thread-safe without manual locks.",
        "GIL limits CPU parallelism — threads still help when waiting on I/O or releasing GIL.",
    ],
    """| Primitive | Use |
| :--- | :--- |
| `Lock` / `RLock` | Mutual exclusion |
| `Condition` | Wait/notify |
| `Semaphore` | Counting resource limit |
| `Event` | One-shot signal |
| `Queue` | Safe handoff |

| Module | Notes |
| :--- | :--- |
| `threading` | Low-level threads |
| `concurrent.futures` | Higher-level pools |""",
    """```python
import threading
from queue import Queue

q: Queue[WorkItem] = Queue(maxsize=1000)

def worker():
    while True:
        item = q.get()
        try:
            process(item)
        finally:
            q.task_done()

for _ in range(4):
    threading.Thread(target=worker, daemon=True).start()
```""",
    "- Daemon threads killed abruptly on main exit — not for cleanup work.\n- `Lock` not reentrant by default — use `RLock` if same thread re-enters.\n- Race on `if not dict: dict[k]=` — use locks or concurrent collections.",
    "- Name threads for debugging (`threading.current_thread().name`).\n- Cap pool size; unbounded threads exhaust memory and FDs.",
    [("Why GIL exists?", "Protects CPython object memory management from races without per-object locks. Simplifies C API at cost of CPU parallelism.")],
)

PAGE_BODIES["multiprocessing"] = topic(
    [
        "Separate memory spaces — share data via `Queue`, `Pipe`, or `multiprocessing.Manager`.",
        "Windows uses `spawn` — import guard `if __name__ == '__main__'` required.",
        "`ProcessPoolExecutor` maps function over iterables for CPU work.",
    ],
    """| Start method | Behavior |
| :--- | :--- |
| `spawn` | Clean interpreter (Windows default) |
| `fork` | Copy parent process (Unix — careful with threads) |
| `forkserver` | Server forks workers |

| Share state | Safe? |
| :--- | :--- |
| `Queue` / `Pipe` | ✓ |
| `shared_memory` (3.8+) | ✓ with sync |
| Global list | ✗ not across processes |""",
    """```python
from concurrent.futures import ProcessPoolExecutor

def cpu_heavy(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        results = list(pool.map(cpu_heavy, range(1000)))
```""",
    "- Picklable top-level functions only for `multiprocessing` on Windows.\n- Large data shipping between processes is expensive — share memory or chunk.\n- Mixing `fork` + threads can duplicate broken state.",
    "- Worker count ≈ CPU cores for CPU-bound; measure queue depth.\n- Use joblib or dask for larger distributed compute.",
    [("threads vs processes for CPU work?", "Processes bypass GIL — true parallel CPU. Threads won't scale CPU-bound Python loops.")],
)

PAGE_BODIES["memory-management"] = topic(
    [
        "Primary GC: reference counting + cyclic garbage detector (`gc` module).",
        "`sys.getsizeof` shallow — doesn't include referenced objects.",
        "Profile with `tracemalloc`, `objgraph`, memory_profiler before optimizing.",
    ],
    """| Technique | Effect |
| :--- | :--- |
| `__slots__` | Reduce per-instance dict overhead |
| `weakref` | Avoid reference cycles to large graphs |
| Gen expr vs list | Lower peak memory |
| `gc.collect()` | Force cyclic GC — rarely in prod hot path |

| Symptom | Likely cause |
| :--- | :--- |
| Steady RSS growth | Leaked globals, caches, cycles |
| Spike on request | Large materialized collections |""",
    """```python
import tracemalloc

tracemalloc.start()
# ... run workload ...
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:10]:
    print(stat)

import weakref
cache = weakref.WeakValueDictionary()
```""",
    "- C extensions may allocate off-heap — RSS > Python object totals.\n- `del x` drops reference; object freed when refcount 0 (unless cycle).\n- Interned strings and small ints cached — don't rely on identity.",
    "- Bound caches (`lru_cache(maxsize=...)`, TTL).\n- Stream large files; don't read entire blob into memory.",
    [("Why cyclic GC?", "Reference counting alone can't free cycles (A→B→A). Generational cyclic collector runs periodically.")],
)

PAGE_BODIES["packaging"] = topic(
    [
        "`pyproject.toml` is canonical project metadata (PEP 621).",
        "Build backends: `setuptools`, `hatchling`, `flit`, `poetry-core`.",
        "Wheels (`.whl`) preferred for install speed — sdist for source distribution.",
    ],
    """| File | Role |
| :--- | :--- |
| `pyproject.toml` | Metadata, deps, tool config |
| `src/package/` | Src layout (recommended) |
| `MANIFEST.in` | Extra sdist files (setuptools) |

| Command | Purpose |
| :--- | :--- |
| `pip install -e .` | Editable dev install |
| `python -m build` | Build sdist + wheel |
| `twine upload dist/*` | Publish to PyPI |""",
    """```toml
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
```""",
    "- Version in one place — dynamic version from VCS with hatch/setuptools-scm.\n- Namespace packages don't require `__init__.py` but explicit is clearer.\n- Lock files: `uv.lock` / `poetry.lock` for apps, not always for libraries.",
    "- Pin deps in applications; libraries specify ranges.\n- Sign tags; use trusted publishing to PyPI (OIDC).",
    [("src layout vs flat?", "Src layout (`src/pkg`) prevents accidental import from repo root during dev — fewer 'works on my machine' packaging bugs.")],
)

PAGE_BODIES["virtual-environments"] = topic(
    [
        "`python -m venv .venv` creates isolated site-packages and interpreter shim.",
        "Activate modifies PATH — `source .venv/bin/activate` (Unix) or `.venv\\Scripts\\activate` (Windows).",
        "`uv` / `pip-tools` speed up resolve and reproducible installs.",
    ],
    """| Tool | Role |
| :--- | :--- |
| `venv` | Stdlib environment creation |
| `pip` | Install from PyPI/VCS/local |
| `uv` | Fast resolver/installer (Rust) |
| `pip-compile` | Lock requirements.in → .txt |

| Practice | Why |
| :--- | :--- |
| One venv per project | Isolated deps |
| Commit lockfile (apps) | Reproducible deploys |
| `.python-version` / `requires-python` | Document runtime |""",
    """```bash
python -m venv .venv
# Unix
source .venv/bin/activate
# Windows PowerShell
.venv\\Scripts\\Activate.ps1

pip install -U pip
pip install -e ".[dev]"

# uv alternative
uv venv && uv pip install -e .
```""",
    "- Never commit `.venv/` — add to `.gitignore`.\n- System Python on macOS/Linux may be externally managed (PEP 668) — use venv.\n- `pip install` into global Python breaks OS tools.",
    "- CI: cache venv or `uv` lock; matrix test `requires-python` lower bound.\n- Docker: multi-stage build, install deps before copying source.",
    [("venv vs conda?", "venv isolates Python packages for a given interpreter. Conda manages binaries and non-Python deps too — heavier, common in data science.")],
)

PAGE_BODIES["interview-questions"] = topic(
    [
        "Expect deep dives on mutability, GIL, MRO, decorators, and async pitfalls.",
        "Whiteboard API design: exceptions, typing, and context managers for resources.",
        "Know stdlib trade-offs — when list vs deque, dict vs DB, threads vs asyncio.",
    ],
    """| Theme | Must-know |
| :--- | :--- |
| Data model | mutability, copy vs reference, hash/equality |
| OOP | MRO, `super`, descriptors, `@property` |
| Concurrency | GIL, asyncio vs threads vs processes |
| Runtime | imports, GIL release points, GC cycles |
| Style | EAFP vs LBYL, idiomatic comprehensions |

| Red flag answer | Better |
| :--- | :--- |
| "Python is pass-by-reference" | Call-by-object-reference |
| "Threads parallelize CPU in Python" | Processes or native code for CPU |
| "async is always faster" | Faster when I/O wait dominates |""",
    "",
    "- Trick questions often involve mutable default args, late-binding closures, and `is` vs `==`.\n- `[[0]*3]*3` creates shared inner lists — classic gotcha.\n- Descriptor protocol powers properties, classmethods, staticmethods.",
    "- Interviewers probe production judgment — logging, timeouts, resource cleanup.\n- Mention `typing`, tests (pytest), and packaging literacy for senior roles.",
    [
        ("What is the GIL?", "Global Interpreter Lock — mutex allowing one thread to execute Python bytecode at a time in a process. I/O and many C extensions release it. CPU-bound parallelism needs multiprocessing or native extensions."),
        ("Explain decorators.", "Functions that take a callable and return a callable, applied at definition time via `@`. Used for cross-cutting concerns: retry, auth, timing. `functools.wraps` preserves metadata."),
        ("list vs tuple?", "List mutable, unhashable, more memory. Tuple immutable (if elements hashable, tuple hashable), can be dict key, faster iteration, signals fixed structure."),
        ("How does `async/await` work?", "Coroutine functions return coroutine objects scheduled on an event loop. `await` yields control until I/O completes without blocking the thread. Requires async-compatible libraries."),
        ("MRO in multiple inheritance?", "C3 linearization orders bases for method lookup. `super()` uses MRO for cooperative calls — not simply 'parent class'."),
    ],
)


def main() -> None:
    raise SystemExit(
        "Deprecated after Phase B refactor. "
        "Handbook content lives under content/python-cheatsheet/<module>/ "
        "and is generated by scripts/generate_python_handbook_refactor.py. "
        "Edit topic files directly or extend that generator."
    )
    modules_path = DATA / "python_cheatsheet_modules.yaml"
    modules = yaml.safe_load(modules_path.read_text(encoding="utf-8"))["modules"]
    ordered = flatten_topics(modules)
    write_order_yaml(ordered, DATA / "python_cheatsheet_order.yaml")

    CONTENT.mkdir(parents=True, exist_ok=True)
    expected = {f"{slug}.md" for slug in ordered}

    for mod_id, mod_title, slug, topic_idx in iter_module_topics(modules):
        spec = PAGE_BODIES[slug]
        body = page_body(
            spec.glance,
            spec.tables,
            spec.snippets,
            spec.internals,
            spec.production,
            spec.interviews,
            see_also_links(slug, ordered),
        )
        path = CONTENT / f"{slug}.md"
        path.write_text(front_matter(slug, mod_id, mod_title, topic_idx) + normalize(body), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")

    for orphan in CONTENT.glob("*.md"):
        if orphan.name != "_index.md" and orphan.name not in expected:
            orphan.unlink()
            print(f"removed orphan {orphan.relative_to(ROOT)}")

    print(f"done — {len(ordered)} topics")


if __name__ == "__main__":
    main()
