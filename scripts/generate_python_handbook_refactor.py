"""Generate refactored Python handbook content (Phase B)."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "python-cheatsheet"
DATA = ROOT / "data"
DATE = "2026-07-03T12:00:00+00:00"
BASE = "/python-cheatsheet"

FM = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
interviewHandbook: true{aliases}
---

"""

FM_CHEAT = FM.replace("interviewHandbook: true", "cheatSheet: true\ninterviewHandbook: true")


def aliases_block(*paths: str) -> str:
    if not paths:
        return ""
    lines = "\n".join(f'  - "{p}"' for p in paths)
    return f"\naliases:\n{lines}"


def w(rel: str, body: str, *, cheat: bool = False, alias_paths: tuple[str, ...] = (), **fm):
    path = HB / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    tmpl = FM_CHEAT if cheat else FM
    alias = aliases_block(*alias_paths)
    path.write_text(tmpl.format(date=DATE, aliases=alias, **fm) + body.strip() + "\n", encoding="utf-8")


def read_old(name: str) -> str:
    p = HB / name
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    return re.sub(r"^---.*?---\n", "", text, count=1, flags=re.DOTALL)


def fix_links(body: str) -> str:
    mapping = {
        "/python-cheatsheet/language-basics/": f"{BASE}/01-fundamentals/language-basics/",
        "/python-cheatsheet/functions/": f"{BASE}/01-fundamentals/functions/",
        "/python-cheatsheet/collections/": f"{BASE}/01-fundamentals/collections/",
        "/python-cheatsheet/modules/": f"{BASE}/01-fundamentals/modules/",
        "/python-cheatsheet/exceptions/": f"{BASE}/01-fundamentals/exceptions/",
        "/python-cheatsheet/typing/": f"{BASE}/01-fundamentals/typing/",
        "/python-cheatsheet/oop/": f"{BASE}/02-core-python/oop/",
        "/python-cheatsheet/classes/": f"{BASE}/02-core-python/classes/",
        "/python-cheatsheet/dataclasses/": f"{BASE}/02-core-python/dataclasses/",
        "/python-cheatsheet/decorators/": f"{BASE}/02-core-python/decorators/",
        "/python-cheatsheet/context-managers/": f"{BASE}/02-core-python/context-managers/",
        "/python-cheatsheet/iterators/": f"{BASE}/02-core-python/iterators/",
        "/python-cheatsheet/generators/": f"{BASE}/02-core-python/generators/",
        "/python-cheatsheet/comprehensions/": f"{BASE}/02-core-python/comprehensions/",
        "/python-cheatsheet/concurrency/": f"{BASE}/04-concurrency/concurrency/",
        "/python-cheatsheet/asyncio/": f"{BASE}/04-concurrency/asyncio/",
        "/python-cheatsheet/multithreading/": f"{BASE}/04-concurrency/multithreading/",
        "/python-cheatsheet/multiprocessing/": f"{BASE}/04-concurrency/multiprocessing/",
        "/python-cheatsheet/memory-management/": f"{BASE}/03-python-internals/memory-management/",
        "/python-cheatsheet/packaging/": f"{BASE}/07-packaging-distribution/packaging/",
        "/python-cheatsheet/virtual-environments/": f"{BASE}/07-packaging-distribution/virtual-environments/",
        "/python-cheatsheet/interview-questions/": f"{BASE}/09-interview-guide/top-150-interview-questions/",
    }
    for old, new in mapping.items():
        body = body.replace(old, new)
    return body


def strip_interview_shortcodes(body: str) -> str:
    body = re.sub(r"\{< interview-answer >\}[\s\S]*?\{< /interview-answer >\}", "", body)
    body = body.replace("## Interview Probes", "## Interview Questions")
    if "top-150-interview-questions" not in body:
        body = re.sub(
            r"(## Interview Questions\n)",
            r"\1\nSee [Top 150](" + BASE + r"/09-interview-guide/top-150-interview-questions/) — answers on canonical topic pages.\n",
            body,
            count=1,
        )
    return body


def patch_concurrency(body: str) -> str:
    body = body.replace(
        "- CPython GIL: one thread executes Python bytecode at a time per process.",
        "- CPython [GIL](" + BASE + "/03-python-internals/gil/) limits CPU parallelism in threads — see canonical page for internals.",
    )
    body = re.sub(
        r"## Internals & Gotchas\n\n- Async is not faster CPU[\s\S]*?`asyncio\.run\(\)` creates/closes event loop",
        "## Internals & Gotchas\n\n- Async is not faster CPU — it schedules I/O wait better.\n"
        "- Thread safety: protect shared mutable state — see [Concurrency Patterns](" + BASE + "/04-concurrency/concurrency-patterns/).\n"
        "- `asyncio.run()` creates/closes event loop",
        body,
    )
    return body


def patch_multithreading(body: str) -> str:
    body = body.replace(
        "- GIL limits CPU parallelism — threads still help when waiting on I/O or releasing GIL.",
        "- [GIL](" + BASE + "/03-python-internals/gil/) limits CPU parallelism — threads help for I/O-bound work.",
    )
    return body


def patch_memory_overview(body: str) -> str:
    body = body.replace(
        "- Primary GC: reference counting + cyclic garbage detector (`gc` module).",
        "- Memory overview — reference counting and cyclic GC: [Garbage Collection](" + BASE + "/03-python-internals/garbage-collection/).",
    )
    body = body.replace(
        "- Profile with `tracemalloc`, `objgraph`, memory_profiler before optimizing.",
        "- Profile with [Profiling](" + BASE + "/05-performance/profiling/) (`cProfile`, `tracemalloc`, `memory_profiler`).",
    )
    body = re.sub(
        r"\| `gc\.collect\(\)` \| Force cyclic GC[\s\S]*?\| Spike on request \| Large materialized collections \|",
        "| Spike on request | Large materialized collections |",
        body,
    )
    body = re.sub(
        r"## Internals & Gotchas\n\n- C extensions may allocate[\s\S]*?- Interned strings",
        "## Internals & Gotchas\n\n- C extensions may allocate off-heap — RSS > Python object totals.\n"
        "- `del x` drops a reference; cyclic graphs need the GC — see [Garbage Collection](" + BASE + "/03-python-internals/garbage-collection/).\n"
        "- Interned strings",
        body,
    )
    body = re.sub(
        r"```python\nimport tracemalloc[\s\S]*?cache = weakref\.WeakValueDictionary\(\)\n```",
        "",
        body,
    )
    if "## Quick Revision" not in body:
        body = body.replace(
            "## At a Glance",
            "## Quick Revision\n\n"
            "- CPython uses refcounting plus generational cyclic GC.\n"
            "- pymalloc manages small object arenas — RSS can exceed `sys.getsizeof` totals.\n"
            "- Tune memory after profiling — not before.\n\n"
            "## At a Glance",
        )
    return body


def patch_oop(body: str) -> str:
    body = body.replace(
        "| Protocol (structural) | `typing.Protocol` — duck typing with types |",
        "| Protocol (structural) | See [Typing](" + BASE + "/01-fundamentals/typing/) |",
    )
    return body


def patch_modules(body: str) -> str:
    body = body.replace(
        "- Namespace packages: multiple dirs on `sys.path` contribute to same package.",
        "- Import system internals (finders, loaders): [Python Runtime](" + BASE + "/03-python-internals/python-runtime/).",
    )
    return body


def patch_classes(body: str) -> str:
    body = body.replace(
        "- `__init__` ≠ `__new__` — latter controls instance creation (singletons, immutables).",
        "- `__new__` / descriptor protocol: [Object Model](" + BASE + "/03-python-internals/object-model/).",
    )
    return body


SECTIONS = [
    ("01-fundamentals", "Fundamentals", "Language basics, collections, modules, exceptions, typing.", 1),
    ("02-core-python", "Core Python", "OOP, decorators, iterators, generators, comprehensions.", 2),
    ("03-python-internals", "Python Internals", "Runtime, CPython, bytecode, object model, memory, GC, GIL.", 3),
    ("04-concurrency", "Concurrency", "Asyncio, threading, multiprocessing, concurrency patterns.", 4),
    ("05-performance", "Performance", "Profiling, benchmarking, optimization, memory tuning.", 5),
    ("06-production-python", "Production Python", "Logging, config, observability, error handling, checklists.", 6),
    ("07-packaging-distribution", "Packaging & Distribution", "pyproject.toml, dependencies, Poetry, virtual environments.", 7),
    ("08-testing", "Testing", "Strategy, pytest, mocking, CI patterns.", 8),
    ("09-interview-guide", "Interview Guide", "150-question bank and role-specific subsets.", 9),
    ("10-learning-paths", "Learning Paths", "Curated reading paths by seniority and goal.", 10),
]


def new_internals_pages() -> None:
  b = BASE
  w("03-python-internals/python-runtime.md", textwrap.dedent(f"""
    ## Quick Revision

    - `python script.py` → interpreter startup → `sys.path` init → run `__main__` module.
    - `import` uses `sys.meta_path` finders → loaders → module object in `sys.modules`.
    - `if __name__ == '__main__'` guards script-only code; required for multiprocessing `spawn`.

    ## Core Concepts

    | Stage | What happens |
    | :--- | :--- |
    | Startup | Parse flags, init interpreter, import encodings, site |
    | Import | Finder locates spec → loader executes module body |
    | Execution | `PyEval_EvalFrameDefault` runs bytecode in frames |
    | Shutdown | `atexit`, flush stdio, teardown interpreters |

    ## Internal Working

    ```mermaid
    sequenceDiagram
      participant Main
      participant Importlib
      participant Loader
      participant Module
      Main->>Importlib: import pkg.mod
      Importlib->>Importlib: sys.meta_path find_spec
      Importlib->>Loader: exec_module
      Loader->>Module: run module body
      Loader-->>Main: sys.modules[name]
    ```

    **Import path:** Built-in and frozen importers first, then `PathFinder` on `sys.path` entries (including site-packages and editable installs).

  ## Runtime Behavior

    - Circular imports: module partially initialized in `sys.modules` — defer imports or extract shared types.
    - Lazy imports reduce CLI cold start — measure with [Profiling]({b}/05-performance/profiling/).
    - `PYTHONPATH` prepends entries; prefer explicit packaging over manipulating `sys.path` in libraries.

    ## Design Tradeoffs

    | Choice | Trade-off |
    | :--- | :--- |
    | Absolute imports | Clearer, refactor-friendly |
    | Relative imports | Shorter intra-package, breaks if package renamed |
    | Lazy import | Faster startup vs scattered import errors |
    | `importlib.reload` | Dev convenience vs broken invariants |

    ## Production Usage

    - One entry module; package `__init__.py` exposes stable public API via `__all__`.
    - Container images: set `PYTHONUNBUFFERED=1`, pin `requires-python`.

    ## Performance Considerations

    - Import cost is paid once per process (until reload) — profile startup separately.

    ## Troubleshooting

    | Symptom | Check |
    | :--- | :--- |
    | `ModuleNotFoundError` in Docker | `sys.path`, `WORKDIR`, editable vs wheel install |
    | Circular import at startup | Import graph, move shared types |
    | Wrong package version loaded | `pip show`, multiple paths shadowing |

    ## Common Mistakes

    - Mutating `sys.path` in library code.
    - Side effects at import time (network calls, heavy computation).

    ## Interview Questions

    See [Top 150]({b}/09-interview-guide/top-150-interview-questions/) — Internals & Runtime category.

    ## Architect Notes

    Import and startup behavior drive **cold-start SLOs** for serverless and CLI tools — treat as architecture, not trivia.
  """), title="Python Runtime", desc="Execution model, interpreter lifecycle, import system, and runtime flow.", short="Runtime", mod=3, mod_title="Python Internals", ref="3.1", weight=301)

  w("03-python-internals/cpython-internals.md", textwrap.dedent(f"""
    ## Quick Revision

    - CPython = parser + compiler + ceval loop + object system + C API.
    - Most objects are `PyObject*` with refcount and type pointer.
    - C extensions release the GIL around blocking/native work.

    ## Core Concepts

    | Component | Role |
    | :--- | :--- |
    | Parser / AST | Source → concrete syntax tree |
    | Compiler | AST → code objects (bytecode + constants) |
    | ceval | Opcode dispatch loop |
    | Object model | `PyTypeObject`, `PyObject` layout |
    | C-API / ctypes / cffi | Native interop |

    ## Internal Working

    ```mermaid
    flowchart TB
      src[Source] --> parse[Parser]
      parse --> ast[AST]
      ast --> compile[Compiler]
      compile --> code[Code object]
      code --> ceval[Eval loop]
      ceval --> objects[PyObject graph]
    ```

    ## Runtime Behavior

    - Pure Python CPU work holds the [GIL]({b}/03-python-internals/gil/) in the default build.
    - Many stdlib I/O and numeric ops delegate to C that releases the GIL.

    ## Production Usage

    - Hot paths: profile before rewriting in Cython/Rust — see [Performance Optimization]({b}/05-performance/performance-optimization/).

    ## Interview Questions

  See [Top 150]({b}/09-interview-guide/top-150-interview-questions/) — CPython architecture questions.

    ## Architect Notes

    Choosing CPython assumes the GIL model unless you standardize on free-threading builds — plan concurrency accordingly.
  """), title="CPython Internals", desc="CPython architecture, execution engine, object system overview.", short="CPython", mod=3, mod_title="Python Internals", ref="3.2", weight=302)

  w("03-python-internals/bytecode.md", textwrap.dedent(f"""
    ## Quick Revision

    - Source → AST → **code object** (bytecode + consts + names) → frame execution.
    - `dis.dis(fn)` shows opcodes — essential for understanding hot loops.
    - `LOAD_FAST`, `LOAD_ATTR`, `CALL` dominate many profiles.

    ## Core Concepts

    | Artifact | Contains |
    | :--- | :--- |
    | Code object | `co_code`, `co_consts`, `co_names`, `co_varnames`, flags |
    | Frame | Stack, locals, globals, instruction pointer |
    | Opcode | Single VM instruction |

    ## Internal Working

    ```mermaid
    flowchart LR
      src[.py source] --> ast[AST]
      ast --> code[Code object]
      code --> frame[Frame on stack]
      frame --> op[Opcode dispatch]
    ```

    ```python
    import dis

    def hot(x: int) -> int:
        total = 0
        for i in range(x):
            total += i
        return total

    dis.dis(hot)
    ```

    ## Performance Considerations

    - Local variables faster than globals — `LOAD_FAST` vs `LOAD_GLOBAL`.
    - Attribute access in tight loops — cache in local variable.

    ## Troubleshooting

    - Unexpected branches — inspect bytecode after decorator desugaring.

    ## Interview Questions

    See [Top 150]({b}/09-interview-guide/top-150-interview-questions/).
  """), title="Bytecode", desc="Compilation flow, bytecode, dis module, execution process.", short="Bytecode", mod=3, mod_title="Python Internals", ref="3.3", weight=303)

  w("03-python-internals/object-model.md", textwrap.dedent(f"""
    ## Quick Revision

    - Everything is an object; variables bind names to objects.
    - Attribute lookup: instance `__dict__` → class → MRO → descriptors.
    - `__eq__` without `__hash__` sets `__hash__ = None` (unhashable).

    ## Core Concepts

    | Mechanism | Role |
    | :--- | :--- |
    | `PyObject` | `ob_refcnt`, `ob_type`, payload |
    | `__dict__` | Per-instance attribute storage (unless `__slots__`) |
    | Descriptor | `__get__` / `__set__` / `__delete__` on class attributes |
    | `__new__` | Allocates instance; `__init__` initializes |

    ## Internal Working

    ```mermaid
    sequenceDiagram
      participant Inst
      participant Class
      participant Desc
      Inst->>Class: lookup attr
      alt data descriptor on class
        Class->>Desc: __get__(inst, class)
      else instance __dict__
        Inst-->>Inst: return value
      end
    ```

    ## Design Tradeoffs

    | Choice | Trade-off |
    | :--- | :--- |
    | `__slots__` | Lower memory, no arbitrary attrs |
    | `__eq__` only | Breaks hash-based collections |
    | Descriptors | Power vs complexity |

    ## Production Usage

    - Use `@property` for validation; understand descriptor cost on hot paths.

    ## Interview Questions

    See [Top 150]({b}/09-interview-guide/top-150-interview-questions/) — object model and descriptor questions.
  """), title="Object Model", desc="PyObject layout, attribute lookup, descriptors, __new__, equality contract.", short="Object Model", mod=3, mod_title="Python Internals", ref="3.4", weight=304)

  w("03-python-internals/garbage-collection.md", textwrap.dedent(f"""
    ## Quick Revision

    - Primary reclamation: **reference counting** (immediate when refcount hits 0).
    - **Cyclic GC** collects unreachable reference cycles (generations 0/1/2).
    - `gc` module introspects cycles; `weakref` breaks strong cycles intentionally.

    ## Core Concepts

    | Layer | Behavior |
    | :--- | :--- |
    | Refcount | Increment on bind, decrement on del/out-of-scope |
    | Cyclic GC | Detects unreachable cycles; runs on thresholds |
    | `weakref` | Non-owning references; `WeakValueDictionary` for caches |

    ## Internal Working

    ```mermaid
    flowchart TD
      ref[Refcount to zero] --> free[Deallocate immediately]
      cycle[Reference cycle] --> gc[Generational GC scan]
      gc --> free2[Break cycle and free]
    ```

    ```python
    import gc, weakref

    gc.set_debug(gc.DEBUG_STATS)
    gc.collect()  # rarely in hot paths — diagnostics only

    cache: weakref.WeakValueDictionary = weakref.WeakValueDictionary()
    ```

    ## Performance Considerations

    - Large cycles cause GC pauses — break cycles with `weakref` or explicit `clear()`.
    - `gc.collect()` in production hot paths is usually a smell.

    ## Troubleshooting

    | Symptom | Action |
    | :--- | :--- |
    | RSS grows, refcount objects alive | `tracemalloc`, `objgraph`, check globals and caches |
    | GC pauses | Reduce cycle creation, tune thresholds carefully |

    ## Interview Questions

    See [Top 150]({b}/09-interview-guide/top-150-interview-questions/).
  """), title="Garbage Collection", desc="Reference counting, cyclic GC, weakref, performance impact.", short="GC", mod=3, mod_title="Python Internals", ref="3.6", weight=306)

  w("03-python-internals/gil.md", textwrap.dedent(f"""
    ## Quick Revision

    - **GIL** = mutex allowing one thread to execute Python bytecode at a time per process.
    - Protects CPython object internals without per-object locks.
    - Released around I/O and many C extension calls — **not** a fix for CPU-bound threads.

    ## Core Concepts

    | Topic | Detail |
    | :--- | :--- |
    | Purpose | Simplify C API and refcounting thread safety |
    | CPU-bound threads | No parallel bytecode execution |
    | Workarounds | `multiprocessing`, native extensions, free-threading builds |
    | I/O-bound threads | Still useful — GIL released during waits |

    ## Internal Working

    ```mermaid
    sequenceDiagram
      participant T1 as Thread 1
      participant GIL
      participant T2 as Thread 2
      T1->>GIL: acquire
      T1->>T1: run bytecode
      T1->>GIL: release (I/O or tick)
      T2->>GIL: acquire
    ```

    ## Production Usage

    - CPU parallelism → [Multiprocessing]({b}/04-concurrency/multiprocessing/) or vectorized C libs.
    - Mixed workloads → [Concurrency Patterns]({b}/04-concurrency/concurrency-patterns/) (async I/O + process pool for CPU).

    ## Design Tradeoffs

    | Model | When |
    | :--- | :--- |
    | Threads + GIL | Blocking I/O libraries |
    | Asyncio | Many concurrent I/O waits, async APIs |
    | Processes | CPU-bound pure Python |
    | nogil / 3.13+ | Evaluate compatibility before platform bet |

    ## Interview Questions

    See [Top 150]({b}/09-interview-guide/top-150-interview-questions/) — GIL category.

    ## Architect Notes

    The GIL is a **platform constraint** for Python thread scaling — document it in concurrency ADRs.
  """), title="GIL", desc="Global Interpreter Lock internals, release points, production implications.", short="GIL", mod=3, mod_title="Python Internals", ref="3.7", weight=307)


def new_concurrency_perf_prod_pages() -> None:
  b = BASE
  w("04-concurrency/concurrency-patterns.md", textwrap.dedent(f"""
    ## Quick Revision

    - `ThreadPoolExecutor` / `ProcessPoolExecutor` — unified pool API via `concurrent.futures`.
    - Producer-consumer with bounded `queue.Queue` — backpressure via `maxsize`.
    - `asyncio.Semaphore` limits concurrent coroutines.

    ## Core Concepts

    | Pattern | Tool |
    | :--- | :--- |
    | Thread pool | `ThreadPoolExecutor` |
    | Process pool | `ProcessPoolExecutor` |
    | Producer-consumer | `queue.Queue` + workers |
    | Async rate limit | `asyncio.Semaphore` |
    | Backpressure | Bounded queues, semaphores |

    ## Production Usage

    ```python
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import asyncio

    async def bounded_fetch(urls, limit=10):
        sem = asyncio.Semaphore(limit)
        async def one(url):
            async with sem:
                return await client.get(url)
        return await asyncio.gather(*(one(u) for u in urls))

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(fetch, u) for u in urls]
        for fut in as_completed(futures):
            handle(fut.result())
    ```

    ## Performance Considerations

    - Size pools from downstream limits (DB connections, API rate limits).
    - Process pools: minimize pickled payload size.

    ## Interview Questions

    See [Top 150]({b}/09-interview-guide/top-150-interview-questions/).
  """), title="Concurrency Patterns", desc="Thread pools, process pools, producer-consumer, backpressure, scheduling.", short="Patterns", mod=4, mod_title="Concurrency", ref="4.5", weight=405)

  for slug, title, short, ref, wgt, body in [
    ("performance-optimization", "Performance Optimization", "Perf Opt", "5.1", 501,
     f"CPU/memory optimization, data structures, best practices. Profile first — [Profiling]({b}/05-performance/profiling/). Algorithmic wins beat micro-opts. Use NumPy/C extensions for hot numeric loops."),
    ("profiling", "Profiling", "Profiling", "5.2", 502,
     "`cProfile` for call graphs; `line_profiler` for line hotspots; `tracemalloc` / `memory_profiler` for memory. `py-spy` for sampling in production."),
    ("benchmarking", "Benchmarking", "Benchmark", "5.3", 503,
     "`timeit` for micro-benchmarks; warmup iterations; report median and p95. `pytest-benchmark` in CI for regression guards."),
    ("memory-optimization", "Memory Optimization", "Mem Opt", "5.4", 504,
     "Generators over lists; bounded `lru_cache`; `__slots__` after measurement; `weakref` caches. See [Garbage Collection]({b}/03-python-internals/garbage-collection/)."),
    ("logging", "Logging", "Logging", "6.1", 601,
     "Structured JSON logs; `logging` handlers/formatters; correlation IDs via `contextvars`. Avoid duplicate handlers."),
    ("configuration-management", "Configuration Management", "Config", "6.2", 602,
     "12-factor: env vars override files; secrets from vault/secret store; `pydantic-settings` for typed config."),
    ("observability", "Observability", "Observability", "6.3", 603,
     "Logs + metrics (Prometheus) + traces (OpenTelemetry). Propagate trace context across threads and asyncio."),
    ("error-handling", "Error Handling", "Errors", "6.4", 604,
     "Map domain exceptions at boundaries; log once with `exc_info=True`; retries for transient errors only."),
    ("production-checklists", "Production Checklists", "Checklists", "6.5", 605,
     "Pre-deploy: pinned deps, health endpoints, structured logging, config audit. Incident: metrics → logs → profile."),
    ("dependency-management", "Dependency Management", "Deps", "7.2", 702,
     "Apps pin with lock files (`uv.lock`, `pip-tools`); libraries specify compatible ranges. Reproducible CI installs."),
    ("poetry", "Poetry", "Poetry", "7.3", 703,
     "Poetry: `pyproject.toml` + lock + virtualenv management. Compare with hatchling + uv for team workflows."),
    ("testing", "Testing", "Testing", "8.1", 801,
     "Testing pyramid: many unit, fewer integration, minimal e2e. Fast feedback in CI."),
    ("pytest", "pytest", "pytest", "8.2", 802,
     "Fixtures, `conftest.py`, parametrization `@pytest.mark.parametrize`, markers for slow tests."),
    ("mocking", "Mocking", "Mocking", "8.3", 803,
     "`unittest.mock.patch` where object is **used**, not where defined. `Mock`/`MagicMock` for collaborators."),
    ("test-strategies", "Test Strategies", "Test Strategy", "8.4", 804,
     "CI stages: lint → typecheck → unit → integration. Coverage targets on critical paths; `hypothesis` for property tests."),
  ]:
    mod = int(ref.split(".")[0])
    mod_titles = {5: "Performance", 6: "Production Python", 7: "Packaging & Distribution", 8: "Testing"}
    folders = {5: "05-performance", 6: "06-production-python", 7: "07-packaging-distribution", 8: "08-testing"}
    content = textwrap.dedent(f"""
      ## Quick Revision

      - {body}

      ## Core Concepts

      See module topics and [Top 150]({b}/09-interview-guide/top-150-interview-questions/) for interview depth.

      ## Production Usage

      Apply patterns with measurement — profile before optimizing.

      ## Interview Questions

      See [Top 150]({b}/09-interview-guide/top-150-interview-questions/).
    """)
    w(f"{folders[mod]}/{slug}.md", content, title=title, desc=body[:120], short=short, mod=mod, mod_title=mod_titles[mod], ref=ref, weight=wgt)


def main() -> None:
    for folder, title, desc, mod in SECTIONS:
        w(f"{folder}/_index.md", f"# {title}\n\n{desc}\n", title=title, desc=desc, short=title, mod=mod, mod_title="Python Handbook", ref="0", weight=mod)

    PATCHERS = {
        "concurrency.md": patch_concurrency,
        "multithreading.md": patch_multithreading,
        "memory-management.md": patch_memory_overview,
        "oop.md": patch_oop,
        "modules.md": patch_modules,
        "classes.md": patch_classes,
    }

    MOVES = [
        ("language-basics.md", "01-fundamentals/language-basics.md", "Python Language Basics", "Syntax, types, scope, control flow.", "Basics", 1, "Fundamentals", "1.1", 111, "language-basics"),
        ("functions.md", "01-fundamentals/functions.md", "Functions", "def, args, closures, functools.", "Functions", 1, "Fundamentals", "1.2", 112, "functions"),
        ("collections.md", "01-fundamentals/collections.md", "Collections", "list, tuple, dict, set, deque.", "Collections", 1, "Fundamentals", "1.3", 113, "collections"),
        ("modules.md", "01-fundamentals/modules.md", "Modules & Imports", "import styles, packages, __main__ guard.", "Modules", 1, "Fundamentals", "1.4", 114, "modules"),
        ("exceptions.md", "01-fundamentals/exceptions.md", "Exceptions", "try/except, hierarchy, chaining.", "Exceptions", 1, "Fundamentals", "1.5", 115, "exceptions"),
        ("typing.md", "01-fundamentals/typing.md", "Typing", "Annotations, Protocol, generics.", "Typing", 1, "Fundamentals", "1.6", 116, "typing"),
        ("oop.md", "02-core-python/oop.md", "OOP in Python", "MRO, inheritance, ABC, mixins.", "OOP", 2, "Core Python", "2.1", 201, "oop"),
        ("classes.md", "02-core-python/classes.md", "Classes", "Attributes, properties, dunder methods.", "Classes", 2, "Core Python", "2.2", 202, "classes"),
        ("dataclasses.md", "02-core-python/dataclasses.md", "Dataclasses", "@dataclass options and comparisons.", "Dataclasses", 2, "Core Python", "2.3", 203, "dataclasses"),
        ("decorators.md", "02-core-python/decorators.md", "Decorators", "@syntax, wraps, parametrized decorators.", "Decorators", 2, "Core Python", "2.4", 204, "decorators"),
        ("context-managers.md", "02-core-python/context-managers.md", "Context Managers", "with, __enter__/__exit__, ExitStack.", "Context Mgr", 2, "Core Python", "2.5", 205, "context-managers"),
        ("iterators.md", "02-core-python/iterators.md", "Iterators & Iterables", "__iter__/__next__, itertools.", "Iterators", 2, "Core Python", "2.6", 206, "iterators"),
        ("generators.md", "02-core-python/generators.md", "Generators", "yield, yield from, pipelines.", "Generators", 2, "Core Python", "2.7", 207, "generators"),
        ("comprehensions.md", "02-core-python/comprehensions.md", "Comprehensions", "List/dict/set/gen expressions.", "Comprehensions", 2, "Core Python", "2.8", 208, "comprehensions"),
        ("concurrency.md", "04-concurrency/concurrency.md", "Concurrency Overview", "Model selection hub — asyncio, threads, processes.", "Concurrency", 4, "Concurrency", "4.1", 401, "concurrency"),
        ("asyncio.md", "04-concurrency/asyncio.md", "Asyncio", "async/await, TaskGroup, event loop.", "Asyncio", 4, "Concurrency", "4.2", 402, "asyncio"),
        ("multithreading.md", "04-concurrency/multithreading.md", "Multithreading", "threading, locks, queues.", "Threading", 4, "Concurrency", "4.3", 403, "multithreading"),
        ("multiprocessing.md", "04-concurrency/multiprocessing.md", "Multiprocessing", "Process pools, spawn/fork, IPC.", "Multiproc", 4, "Concurrency", "4.4", 404, "multiprocessing"),
        ("memory-management.md", "03-python-internals/memory-management.md", "Memory Management", "pymalloc overview, RSS, sizing.", "Memory", 3, "Python Internals", "3.5", 305, "memory-management"),
        ("packaging.md", "07-packaging-distribution/packaging.md", "Packaging", "pyproject.toml, wheels, publishing.", "Packaging", 7, "Packaging & Distribution", "7.1", 701, "packaging"),
        ("virtual-environments.md", "07-packaging-distribution/virtual-environments.md", "Virtual Environments", "venv, pip, uv, pinning.", "Venv", 7, "Packaging & Distribution", "7.4", 704, "virtual-environments"),
    ]

    for old, new, title, desc, short, mod, mod_title, ref, weight, alias in MOVES:
        body = fix_links(read_old(old))
        body = strip_interview_shortcodes(body)
        patch = PATCHERS.get(old)
        if patch:
            body = patch(body)
        w(new, body, cheat=True, title=title, desc=desc, short=short, mod=mod, mod_title=mod_title, ref=ref, weight=weight, alias_paths=(f"{BASE}/{alias}/",))

    new_internals_pages()
    new_concurrency_perf_prod_pages()

    from python_questions_data import QUESTIONS

    q_rows = "\n".join(
        f'| {n} | {q} | {d} | {l} | {t} | [{doc.split("/")[-1].replace(".md", "")}]({BASE}/{doc.replace(".md", "")}/) |'
        for n, q, d, l, t, doc in QUESTIONS
    )

    w("09-interview-guide/top-150-interview-questions.md", textwrap.dedent(f"""
    Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. **Questions only — no answers.**

    **Distribution:** Internals & Runtime 40 · Concurrency & Async 30 · Performance 25 · Troubleshooting 20 · Production 15 · Core Python 20

    | # | Question | Difficulty | Level | Topic | Deep Dive |
    |---|----------|------------|--------|-------|-----------|
    {q_rows}
    """), title="Top 150 Python Interview Questions", desc="150 production-oriented Python interview questions mapped to handbook topics.", short="Top 150", mod=9, mod_title="Interview Guide", ref="9.1", weight=901, alias_paths=(f"{BASE}/interview-questions/",))

    ARCHITECT_QS = [q for _, q, _, l, _, _ in QUESTIONS if l == "Architect"][:40]
    TROUBLE_QS = [QUESTIONS[i][1] for i in range(95, 115)]
    PERF_QS = [QUESTIONS[i][1] for i in range(70, 95)]

    w("09-interview-guide/architect-questions.md", "Questions only — no answers.\n\n# Architect-Level Questions\n\n" + "\n".join(f"{i}. {q}" for i, q in enumerate(ARCHITECT_QS, 1)), title="Architect-Level Questions", desc="Curated architect-level Python interview questions.", short="Architect", mod=9, mod_title="Interview Guide", ref="9.2", weight=902)
    w("09-interview-guide/troubleshooting-questions.md", "Questions only — no answers.\n\n# Troubleshooting Questions\n\n" + "\n".join(f"{i}. {q}" for i, q in enumerate(TROUBLE_QS, 1)), title="Troubleshooting Questions", desc="Production troubleshooting interview questions for Python.", short="Troubleshooting Q", mod=9, mod_title="Interview Guide", ref="9.3", weight=903)
    w("09-interview-guide/performance-questions.md", "Questions only — no answers.\n\n# Performance Questions\n\n" + "\n".join(f"{i}. {q}" for i, q in enumerate(PERF_QS, 1)), title="Performance Questions", desc="Python performance and tuning interview questions.", short="Performance Q", mod=9, mod_title="Interview Guide", ref="9.4", weight=904)

    w("10-learning-paths/python-senior-engineer-path.md", textwrap.dedent(f"""
    # Python Senior Engineer Path

    | Week | Topics |
    | :--- | :--- |
    | 1 | [Fundamentals]({BASE}/01-fundamentals/) → [Core Python]({BASE}/02-core-python/) |
    | 2 | [Python Internals]({BASE}/03-python-internals/) — runtime, GIL, GC |
    | 3 | [Concurrency]({BASE}/04-concurrency/) → [Performance]({BASE}/05-performance/) |
    | 4 | [Testing]({BASE}/08-testing/) → [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/) |
    """), title="Senior Engineer Path", desc="Four-week path for senior Python engineers.", short="Senior Path", mod=10, mod_title="Learning Paths", ref="10.1", weight=1001)

    w("10-learning-paths/python-lead-path.md", textwrap.dedent(f"""
    # Python Technical Lead Path

    1. [Production Python]({BASE}/06-production-python/) — logging, observability, checklists
    2. [Concurrency Patterns]({BASE}/04-concurrency/concurrency-patterns/) + [Profiling]({BASE}/05-performance/profiling/)
    3. [Packaging]({BASE}/07-packaging-distribution/) — reproducible deploys
    4. [Troubleshooting Questions]({BASE}/09-interview-guide/troubleshooting-questions/)
    """), title="Technical Lead Path", desc="Production, concurrency, and troubleshooting for Python leads.", short="Lead Path", mod=10, mod_title="Learning Paths", ref="10.2", weight=1002)

    w("10-learning-paths/python-architect-path.md", textwrap.dedent(f"""
    # Python Architect Path

    1. [CPython Internals]({BASE}/03-python-internals/cpython-internals/) → [GIL]({BASE}/03-python-internals/gil/) → [Object Model]({BASE}/03-python-internals/object-model/)
    2. [Concurrency]({BASE}/04-concurrency/concurrency/) — model selection ADRs
    3. [Performance]({BASE}/05-performance/) + [Observability]({BASE}/06-production-python/observability/)
    4. [Architect Questions]({BASE}/09-interview-guide/architect-questions/)
    """), title="Architect Path", desc="Internals, concurrency ADRs, and architect interview prep.", short="Architect Path", mod=10, mod_title="Learning Paths", ref="10.3", weight=1003)

    w("10-learning-paths/python-interview-revision-path.md", textwrap.dedent(f"""
    # Python Interview Revision Path

    | Block | Time | Focus |
    | :--- | :--- | :--- |
    | **1** | 2h | [Runtime]({BASE}/03-python-internals/python-runtime/) · [Bytecode]({BASE}/03-python-internals/bytecode/) · [GIL]({BASE}/03-python-internals/gil/) |
    | **2** | 2h | [Object Model]({BASE}/03-python-internals/object-model/) · [GC]({BASE}/03-python-internals/garbage-collection/) |
    | **3** | 2h | [Concurrency]({BASE}/04-concurrency/) · [Patterns]({BASE}/04-concurrency/concurrency-patterns/) |
    | **4** | 2h | [Profiling]({BASE}/05-performance/profiling/) · [Production]({BASE}/06-production-python/) |
    | **5** | 2h | [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/) — all categories |
    """), title="Interview Revision Path", desc="48-hour interview cram schedule.", short="Interview Path", mod=10, mod_title="Learning Paths", ref="10.4", weight=1004)

    w("_index.md", textwrap.dedent(f"""
    # Python Handbook

    Production and interview knowledge for **Senior Engineers**, **Technical Leads**, and **Architects** (6+ years). Target **Python 3.11+**.

    ## Learning Paths

    | Track | Start | Goal |
    | :--- | :--- | :--- |
    | **Interview cram** | [Revision Path]({BASE}/10-learning-paths/python-interview-revision-path/) | 48-hour prep |
    | **Senior engineer** | [Senior Path]({BASE}/10-learning-paths/python-senior-engineer-path/) | Internals + concurrency + testing |
    | **Technical lead** | [Lead Path]({BASE}/10-learning-paths/python-lead-path/) | Production + troubleshooting |
    | **Architect** | [Architect Path]({BASE}/10-learning-paths/python-architect-path/) | CPython, GIL, observability ADRs |
    | **Interview bank** | [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/) | Role-specific subsets |

    ## Modules

    1. **Fundamentals** — language, collections, modules, exceptions, typing
    2. **Core Python** — OOP, decorators, iterators, generators
    3. **Python Internals** — runtime, bytecode, object model, GIL, GC
    4. **Concurrency** — asyncio, threading, multiprocessing, patterns
    5. **Performance** — profiling, benchmarking, optimization
    6. **Production Python** — logging, config, observability
    7. **Packaging** — pyproject, dependencies, venv
    8. **Testing** — pytest, mocking, CI strategy
    9. **Interview Guide** — 150 questions + subsets
    10. **Learning Paths** — curated curricula

    For distributed-system patterns in Python services, see [Microservices](/microservices/).
    """), title="Python Handbook", desc="Python handbook — internals, concurrency, performance, production, and interview prep.", short="Handbook", mod=0, mod_title="Python Handbook", ref="0", weight=1)

    modules_yaml = textwrap.dedent("""\
    # Python Handbook — module index.
    modules:
      - id: 1
        focus: "Fundamentals"
        topics:
          - 01-fundamentals/language-basics
          - 01-fundamentals/functions
          - 01-fundamentals/collections
          - 01-fundamentals/modules
          - 01-fundamentals/exceptions
          - 01-fundamentals/typing

      - id: 2
        focus: "Core Python"
        topics:
          - 02-core-python/oop
          - 02-core-python/classes
          - 02-core-python/dataclasses
          - 02-core-python/decorators
          - 02-core-python/context-managers
          - 02-core-python/iterators
          - 02-core-python/generators
          - 02-core-python/comprehensions

      - id: 3
        focus: "Python Internals"
        topics:
          - 03-python-internals/python-runtime
          - 03-python-internals/cpython-internals
          - 03-python-internals/bytecode
          - 03-python-internals/object-model
          - 03-python-internals/memory-management
          - 03-python-internals/garbage-collection
          - 03-python-internals/gil

      - id: 4
        focus: "Concurrency"
        topics:
          - 04-concurrency/concurrency
          - 04-concurrency/asyncio
          - 04-concurrency/multithreading
          - 04-concurrency/multiprocessing
          - 04-concurrency/concurrency-patterns

      - id: 5
        focus: "Performance"
        topics:
          - 05-performance/performance-optimization
          - 05-performance/profiling
          - 05-performance/benchmarking
          - 05-performance/memory-optimization

      - id: 6
        focus: "Production Python"
        topics:
          - 06-production-python/logging
          - 06-production-python/configuration-management
          - 06-production-python/observability
          - 06-production-python/error-handling
          - 06-production-python/production-checklists

      - id: 7
        focus: "Packaging & Distribution"
        topics:
          - 07-packaging-distribution/packaging
          - 07-packaging-distribution/dependency-management
          - 07-packaging-distribution/poetry
          - 07-packaging-distribution/virtual-environments

      - id: 8
        focus: "Testing"
        topics:
          - 08-testing/testing
          - 08-testing/pytest
          - 08-testing/mocking
          - 08-testing/test-strategies

      - id: 9
        focus: "Interview Guide"
        topics:
          - 09-interview-guide/top-150-interview-questions
          - 09-interview-guide/architect-questions
          - 09-interview-guide/troubleshooting-questions
          - 09-interview-guide/performance-questions

      - id: 10
        focus: "Learning Paths"
        topics:
          - 10-learning-paths/python-senior-engineer-path
          - 10-learning-paths/python-lead-path
          - 10-learning-paths/python-architect-path
          - 10-learning-paths/python-interview-revision-path
    """)

    order_topics = []
    for line in modules_yaml.splitlines():
        m = re.match(r"\s+- ([\w-]+/[\w-]+)$", line)
        if m:
            order_topics.append(m.group(1))

    order_yaml = "# Topic order — derived from python_cheatsheet_modules.yaml.\ntopics:\n" + "\n".join(f"  - {t}" for t in order_topics) + "\n"

    (DATA / "python_cheatsheet_modules.yaml").write_text(modules_yaml, encoding="utf-8")
    (DATA / "python_cheatsheet_order.yaml").write_text(order_yaml, encoding="utf-8")

    OLD_FLAT = [
        "language-basics.md", "functions.md", "collections.md", "modules.md", "exceptions.md", "typing.md",
        "oop.md", "classes.md", "dataclasses.md", "decorators.md", "context-managers.md",
        "iterators.md", "generators.md", "comprehensions.md",
        "concurrency.md", "asyncio.md", "multithreading.md", "multiprocessing.md",
        "memory-management.md", "packaging.md", "virtual-environments.md", "interview-questions.md",
    ]
    for name in OLD_FLAT:
        p = HB / name
        if p.exists():
            p.unlink()

    print(f"Python handbook Phase B complete — {len(order_topics)} topics.")


if __name__ == "__main__":
    main()
