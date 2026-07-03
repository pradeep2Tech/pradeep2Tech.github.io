---
title: "Python Concept Registry"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per Python concept."
tags: ["python-cheatsheet", "meta", "planning"]
---

# Python Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase A — registry defined; enforcement in Phase B.

**Path convention:** Relative to `content/python-cheatsheet/` (target paths shown).

---

## 01 Fundamentals — Language & Types

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Syntax, indentation, blocks | `01-fundamentals/language-basics.md` | Exists (move) | |
| LEGB scope (`global`, `nonlocal`) | `01-fundamentals/language-basics.md` | Exists (move) | |
| Built-in types overview | `01-fundamentals/language-basics.md` | Exists (move) | Deep object model → object-model |
| `==` vs `is` | `03-python-internals/object-model.md` | **Planned** | Brief mention only on language-basics |
| Truthiness / falsy values | `01-fundamentals/language-basics.md` | Exists (move) | |
| `match` / structural pattern matching | `01-fundamentals/language-basics.md` | Exists (move) | |
| Function definition (`def`) | `01-fundamentals/functions.md` | Exists (move) | |
| `*args` / `**kwargs` | `01-fundamentals/functions.md` | Exists (move) | |
| Positional-only / keyword-only (`/`, `*`) | `01-fundamentals/functions.md` | Exists (move) | |
| Closures / late-binding trap | `01-fundamentals/functions.md` | Exists (move) | |
| Mutable default arguments | `01-fundamentals/functions.md` | Exists (move) | Strip duplicate from language-basics |
| `functools.partial` / `lru_cache` | `01-fundamentals/functions.md` | Exists (move) | Decorator pattern → decorators |
| `list` / `tuple` / `dict` / `set` | `01-fundamentals/collections.md` | Exists (move) | |
| `collections.deque` / `Counter` / `defaultdict` | `01-fundamentals/collections.md` | Exists (move) | |
| Collection time complexity | `01-fundamentals/collections.md` | Exists (move) | |
| `import` / `from` / relative imports | `01-fundamentals/modules.md` | Exists (move) | Import **internals** → python-runtime |
| `__name__` / `__main__` guard | `01-fundamentals/modules.md` | Exists (move) | |
| Packages / `__init__.py` / `__all__` | `01-fundamentals/modules.md` | Exists (move) | |
| Namespace packages (PEP 420) | `01-fundamentals/modules.md` | Exists (move) | |
| Circular import mitigation | `01-fundamentals/modules.md` | Exists (move) | |
| `try` / `except` / `else` / `finally` | `01-fundamentals/exceptions.md` | Exists (move) | |
| Exception hierarchy | `01-fundamentals/exceptions.md` | Exists (move) | |
| `raise ... from` / exception chaining | `01-fundamentals/exceptions.md` | Exists (move) | |
| `ExceptionGroup` / `except*` (3.11+) | `01-fundamentals/exceptions.md` | Exists (move) | |
| Type annotations | `01-fundamentals/typing.md` | Exists (move) | **Primary** typing source |
| `Protocol` / structural subtyping | `01-fundamentals/typing.md` | Exists (move) | Strip from oop except link |
| `TypeVar` / `Generic` / `ParamSpec` | `01-fundamentals/typing.md` | Exists (move) | |
| `TypedDict` / `Literal` / `Final` | `01-fundamentals/typing.md` | Exists (move) | |
| Static checkers (mypy / pyright) | `01-fundamentals/typing.md` | Exists (move) | |

---

## 02 Core Python — Language Features

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Classes / instances | `02-core-python/classes.md` | Exists (move) | |
| `@property` / `@classmethod` / `@staticmethod` | `02-core-python/classes.md` | Exists (move) | Descriptor internals → object-model |
| `__init__` vs `__new__` | `03-python-internals/object-model.md` | **Planned** | Brief on classes |
| `__repr__` / `__str__` | `02-core-python/classes.md` | Exists (move) | |
| `__eq__` / `__hash__` contract | `03-python-internals/object-model.md` | **Planned** | Mention on classes |
| Multiple inheritance / MRO (C3) | `02-core-python/oop.md` | Exists (move) | **Primary** MRO source |
| `super()` cooperative calls | `02-core-python/oop.md` | Exists (move) | |
| ABC / `@abstractmethod` | `02-core-python/oop.md` | Exists (move) | |
| Mixins / composition | `02-core-python/oop.md` | Exists (move) | |
| `@dataclass` | `02-core-python/dataclasses.md` | Exists (move) | |
| `field()` / `default_factory` | `02-core-python/dataclasses.md` | Exists (move) | |
| `frozen` / `slots` dataclass options | `02-core-python/dataclasses.md` | Exists (move) | |
| Dataclass vs NamedTuple vs Pydantic | `02-core-python/dataclasses.md` | Exists (move) | |
| Decorators (`@` syntax) | `02-core-python/decorators.md` | Exists (move) | **Primary** |
| `functools.wraps` | `02-core-python/decorators.md` | Exists (move) | |
| Parametrized decorators | `02-core-python/decorators.md` | Exists (move) | |
| Class decorators | `02-core-python/decorators.md` | Exists (move) | |
| Context managers (`with`) | `02-core-python/context-managers.md` | Exists (move) | |
| `__enter__` / `__exit__` | `02-core-python/context-managers.md` | Exists (move) | |
| `@contextmanager` / `ExitStack` | `02-core-python/context-managers.md` | Exists (move) | |
| Async context managers | `04-concurrency/asyncio.md` | Exists (move) | Link from context-managers |
| Iterable protocol | `02-core-python/iterators.md` | Exists (move) | **Primary** |
| Iterator protocol / `StopIteration` | `02-core-python/iterators.md` | Exists (move) | |
| `itertools` | `02-core-python/iterators.md` | Exists (move) | |
| Generators (`yield`) | `02-core-python/generators.md` | Exists (move) | **Primary** |
| `yield from` / generator methods | `02-core-python/generators.md` | Exists (move) | |
| List/dict/set comprehensions | `02-core-python/comprehensions.md` | Exists (move) | |
| Generator expressions | `02-core-python/comprehensions.md` | Exists (move) | Lazy eval detail → generators |

---

## 03 Python Internals — Runtime & VM

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Python execution model | `03-python-internals/python-runtime.md` | **Planned** | |
| Interpreter startup / shutdown | `03-python-internals/python-runtime.md` | **Planned** | |
| Import system (`sys.meta_path`, finders, loaders) | `03-python-internals/python-runtime.md` | **Planned** | Strip depth from modules |
| `sys.path` / `PYTHONPATH` | `03-python-internals/python-runtime.md` | **Planned** | |
| CPython architecture overview | `03-python-internals/cpython-internals.md` | **Planned** | |
| Eval loop / ceval | `03-python-internals/cpython-internals.md` | **Planned** | |
| PyObject / PyTypeObject | `03-python-internals/object-model.md` | **Planned** | |
| Instance `__dict__` / attribute lookup | `03-python-internals/object-model.md` | **Planned** | |
| Descriptor protocol | `03-python-internals/object-model.md` | **Planned** | |
| `__slots__` memory layout | `03-python-internals/object-model.md` | **Planned** | Usage patterns on classes |
| Name mangling | `03-python-internals/object-model.md` | **Planned** | |
| Compilation pipeline (source → code object) | `03-python-internals/bytecode.md` | **Planned** | |
| Bytecode / opcodes | `03-python-internals/bytecode.md` | **Planned** | |
| `dis` module | `03-python-internals/bytecode.md` | **Planned** | |
| Frame objects / stack | `03-python-internals/bytecode.md` | **Planned** | |
| Reference counting | `03-python-internals/garbage-collection.md` | **Planned** | Strip from memory-management |
| Generational cyclic GC | `03-python-internals/garbage-collection.md` | **Planned** | |
| `gc` module / `gc.collect()` | `03-python-internals/garbage-collection.md` | **Planned** | |
| `weakref` | `03-python-internals/garbage-collection.md` | **Planned** | Move from memory-management |
| Memory overview (RSS, arenas, pymalloc) | `03-python-internals/memory-management.md` | Exists (split) | Overview only |
| `sys.getsizeof` limitations | `03-python-internals/memory-management.md` | Exists (split) | |
| Global Interpreter Lock (GIL) | `03-python-internals/gil.md` | **Planned** | **Primary** — strip from concurrency pages |
| GIL release points | `03-python-internals/gil.md` | **Planned** | |
| GIL vs `nogil` / free-threading (3.13+) | `03-python-internals/gil.md` | **Planned** | Phase C if needed |

---

## 04 Concurrency & Parallelism

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Concurrency model selection (I/O vs CPU) | `04-concurrency/concurrency.md` | Exists (move) | Hub — no GIL deep dive |
| `asyncio` event loop | `04-concurrency/asyncio.md` | Exists (move) | **Primary** |
| `async`/`await` coroutines | `04-concurrency/asyncio.md` | Exists (move) | |
| `TaskGroup` / structured concurrency | `04-concurrency/asyncio.md` | Exists (move) | |
| `asyncio.to_thread` | `04-concurrency/asyncio.md` | Exists (move) | |
| `threading` module | `04-concurrency/multithreading.md` | Exists (move) | |
| Locks / `RLock` / `Condition` / `Event` | `04-concurrency/multithreading.md` | Exists (move) | |
| `queue.Queue` | `04-concurrency/multithreading.md` | Exists (move) | Patterns → concurrency-patterns |
| Daemon threads | `04-concurrency/multithreading.md` | Exists (move) | |
| `multiprocessing` | `04-concurrency/multiprocessing.md` | Exists (move) | |
| `spawn` / `fork` / `forkserver` | `04-concurrency/multiprocessing.md` | Exists (move) | |
| `shared_memory` / IPC | `04-concurrency/multiprocessing.md` | Exists (move) | |
| `concurrent.futures` | `04-concurrency/concurrency-patterns.md` | **Planned** | Strip duplicate snippets |
| Thread pools / process pools | `04-concurrency/concurrency-patterns.md` | **Planned** | |
| Producer-consumer | `04-concurrency/concurrency-patterns.md` | **Planned** | |
| Backpressure | `04-concurrency/concurrency-patterns.md` | **Planned** | |
| Task scheduling / semaphores | `04-concurrency/concurrency-patterns.md` | **Planned** | |

---

## 05 Performance

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| CPU optimization strategies | `05-performance/performance-optimization.md` | **Planned** | |
| Efficient data structures | `05-performance/performance-optimization.md` | **Planned** | Link collections |
| Algorithmic complexity in Python | `05-performance/performance-optimization.md` | **Planned** | |
| `cProfile` / `profile` | `05-performance/profiling.md` | **Planned** | |
| `line_profiler` | `05-performance/profiling.md` | **Planned** | |
| `memory_profiler` / `tracemalloc` | `05-performance/profiling.md` | **Planned** | Move tracemalloc from memory-management |
| `py-spy` / sampling profilers | `05-performance/profiling.md` | **Planned** | |
| `timeit` | `05-performance/benchmarking.md` | **Planned** | |
| `pytest-benchmark` | `05-performance/benchmarking.md` | **Planned** | |
| Statistical rigor / warmup | `05-performance/benchmarking.md` | **Planned** | |
| Peak memory reduction | `05-performance/memory-optimization.md` | **Planned** | |
| `__slots__` for memory (production) | `05-performance/memory-optimization.md` | **Planned** | Link object-model |
| Generator pipelines for memory | `05-performance/memory-optimization.md` | **Planned** | Link generators |
| Bounded caches | `05-performance/memory-optimization.md` | **Planned** | |

---

## 06 Production Python

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Structured logging | `06-production-python/logging.md` | **Planned** | |
| Log levels / handlers / formatters | `06-production-python/logging.md` | **Planned** | |
| `logging` vs `structlog` | `06-production-python/logging.md` | **Planned** | |
| Environment variables | `06-production-python/configuration-management.md` | **Planned** | |
| Secrets management | `06-production-python/configuration-management.md` | **Planned** | |
| `pydantic-settings` / 12-factor config | `06-production-python/configuration-management.md` | **Planned** | |
| Metrics (Prometheus / statsd) | `06-production-python/observability.md` | **Planned** | |
| Distributed tracing (OpenTelemetry) | `06-production-python/observability.md` | **Planned** | |
| `contextvars` for request context | `06-production-python/observability.md` | **Planned** | Brief on asyncio |
| Production exception mapping | `06-production-python/error-handling.md` | **Planned** | vs syntax on exceptions.md |
| Retry / circuit breaker patterns | `06-production-python/error-handling.md` | **Planned** | Not microservices handbook |
| Pre-deploy checklist | `06-production-python/production-checklists.md` | **Planned** | |
| Incident response checklist | `06-production-python/production-checklists.md` | **Planned** | |

---

## 07 Packaging & Distribution

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| `pyproject.toml` (PEP 621) | `07-packaging-distribution/packaging.md` | Exists (move) | |
| Build backends (hatchling, setuptools) | `07-packaging-distribution/packaging.md` | Exists (move) | |
| Wheels / sdist | `07-packaging-distribution/packaging.md` | Exists (move) | |
| Entry points / `[project.scripts]` | `07-packaging-distribution/packaging.md` | Exists (move) | |
| src layout | `07-packaging-distribution/packaging.md` | Exists (move) | |
| PyPI publishing | `07-packaging-distribution/packaging.md` | Exists (move) | |
| `venv` creation / activation | `07-packaging-distribution/virtual-environments.md` | Exists (move) | |
| `pip` / `uv` | `07-packaging-distribution/virtual-environments.md` | Exists (move) | |
| Lock files (`uv.lock`, `poetry.lock`) | `07-packaging-distribution/dependency-management.md` | **Planned** | |
| `pip-compile` / dependency resolution | `07-packaging-distribution/dependency-management.md` | **Planned** | |
| Apps vs libraries dependency policy | `07-packaging-distribution/dependency-management.md` | **Planned** | |
| Poetry workflow | `07-packaging-distribution/poetry.md` | **Planned** | |

---

## 08 Testing

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Testing pyramid / strategy | `08-testing/testing.md` | **Planned** | |
| Unit vs integration vs e2e | `08-testing/testing.md` | **Planned** | |
| `pytest` basics | `08-testing/pytest.md` | **Planned** | |
| Fixtures / conftest | `08-testing/pytest.md` | **Planned** | |
| Parametrization | `08-testing/pytest.md` | **Planned** | |
| `unittest.mock` / `Mock` / `MagicMock` | `08-testing/mocking.md` | **Planned** | |
| `patch` / `patch.object` | `08-testing/mocking.md` | **Planned** | |
| Dependency isolation | `08-testing/mocking.md` | **Planned** | |
| Coverage / CI integration | `08-testing/test-strategies.md` | **Planned** | |
| Property-based testing (`hypothesis`) | `08-testing/test-strategies.md` | **Planned** | |

---

## 09 Interview Guide (Layer 1 — Questions Only)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Top 150 question index | `09-interview-guide/top-150-interview-questions.md` | **Planned** | Replaces interview-questions |
| Architect question subset | `09-interview-guide/architect-questions.md` | **Planned** | |
| Troubleshooting question subset | `09-interview-guide/troubleshooting-questions.md` | **Planned** | |
| Performance question subset | `09-interview-guide/performance-questions.md` | **Planned** | |

**Answer layer:** Every Top 150 question maps to exactly one topic page `## Question` block (Layer 2) — see `navigation-plan.md` answer map.

---

## 10 Learning Paths

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Senior engineer curriculum | `10-learning-paths/python-senior-engineer-path.md` | **Planned** | |
| Lead engineer curriculum | `10-learning-paths/python-lead-path.md` | **Planned** | |
| Architect curriculum | `10-learning-paths/python-architect-path.md` | **Planned** | |
| Interview revision (48h) | `10-learning-paths/python-interview-revision-path.md` | **Planned** | |

---

## Cross-Registry Rules (Phase B)

1. Remove all `interview-answer` shortcodes from topic pages — answers live in Layer 2 blocks or linked anchors.
2. `concurrency.md` may keep decision diagram but **must not** explain GIL mechanics — link `gil.md`.
3. `memory-management.md` after split: overview + pymalloc only; GC → `garbage-collection.md`; profiling → `profiling.md`.
4. No topic from Design Patterns / System Design / SOLID / Microservices handbooks — link out if needed.
