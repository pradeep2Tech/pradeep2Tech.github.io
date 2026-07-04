---
title: "Top 150 Python Interview Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "150 production-oriented Python interview questions mapped to handbook topics."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Top 150"
module: 9
moduleTitle: "Interview Guide"
sectionRef: "9.1"
weight: 901
interviewHandbook: true
aliases:
- "/python-cheatsheet/interview-questions/"
---

Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. **Questions only — no answers.**

**Distribution:** Internals & Runtime 40 · Concurrency & Async 30 · Performance 25 · Troubleshooting 20 · Production 15 · Core Python 20

| # | Question | Difficulty | Level | Topic | Deep Dive |
|---|----------|------------|--------|-------|-----------|
| 1 | Walk through what happens from `python script.py` to the first line of user code executing. | Hard | Architect | Internals | [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/) |
| 2 | How does CPython locate and load a module on `import pkg.mod`? | Hard | Lead | Internals | [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/) |
| 3 | What roles do `sys.meta_path`, finders, and loaders play in the import system? | Hard | Architect | Internals | [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/) |
| 4 | When would you use `importlib` programmatically instead of a static import? | Medium | Senior Engineer | Internals | [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/) |
| 5 | How does `if __name__ == '__main__'` interact with multiprocessing spawn on Windows? | Medium | Senior Engineer | Internals | [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/) |
| 6 | Describe the major subsystems of the CPython interpreter at a high level. | Hard | Architect | Internals | [Cpython Internals](/python-cheatsheet/03-python-internals/cpython-internals/) |
| 7 | What is the eval loop (`ceval`) and what does it execute? | Hard | Architect | Internals | [Cpython Internals](/python-cheatsheet/03-python-internals/cpython-internals/) |
| 8 | How do C extensions interact with the CPython object model and reference counting? | Hard | Lead | Internals | [Cpython Internals](/python-cheatsheet/03-python-internals/cpython-internals/) |
| 9 | What is the difference between a code object and a function object? | Medium | Senior Engineer | Internals | [Bytecode](/python-cheatsheet/03-python-internals/bytecode/) |
| 10 | How would you use `dis` to inspect a hot function in production troubleshooting? | Medium | Senior Engineer | Internals | [Bytecode](/python-cheatsheet/03-python-internals/bytecode/) |
| 11 | What bytecode patterns indicate inefficient loop or attribute access? | Hard | Lead | Internals | [Bytecode](/python-cheatsheet/03-python-internals/bytecode/) |
| 12 | How does CPython compile source to bytecode — parser, AST, and compiler stages? | Hard | Architect | Internals | [Bytecode](/python-cheatsheet/03-python-internals/bytecode/) |
| 13 | What is stored in a frame object during execution? | Medium | Senior Engineer | Internals | [Bytecode](/python-cheatsheet/03-python-internals/bytecode/) |
| 14 | Explain call-by-object-reference in Python with a mutating argument example. | Medium | Senior Engineer | Internals | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 15 | How does attribute lookup work on instances — `__dict__`, class, MRO, descriptors? | Hard | Architect | Internals | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 16 | What is the descriptor protocol and how do `@property` and `classmethod` use it? | Hard | Lead | Internals | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 17 | When does defining `__eq__` without `__hash__` break `dict` keys or `set` membership? | Medium | Senior Engineer | Internals | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 18 | What is the difference between `__new__` and `__init__` for immutable types? | Medium | Senior Engineer | Internals | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 19 | How do `__slots__` change instance memory layout and attribute behavior? | Medium | Senior Engineer | Internals | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 20 | Why are small integers and some strings interned — and when does identity (`is`) mislead? | Medium | Senior Engineer | Internals | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 21 | How does reference counting reclaim objects — and what happens at refcount zero? | Medium | Senior Engineer | Internals | [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/) |
| 22 | Why is a cyclic garbage collector needed if reference counting exists? | Medium | Senior Engineer | Internals | [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/) |
| 23 | How do generational GC thresholds (gen0/1/2) affect pause behavior? | Hard | Lead | Internals | [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/) |
| 24 | When is `gc.collect()` justified in production versus a code smell? | Medium | Lead | Internals | [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/) |
| 25 | How do `weakref` and `WeakValueDictionary` help break reference cycles? | Medium | Senior Engineer | Internals | [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/) |
| 26 | What does `sys.getsizeof` include and exclude — why is RSS often much larger? | Medium | Senior Engineer | Internals | [Memory Management](/python-cheatsheet/03-python-internals/memory-management/) |
| 27 | What is pymalloc and how do arenas/pools affect fragmentation? | Hard | Architect | Internals | [Memory Management](/python-cheatsheet/03-python-internals/memory-management/) |
| 28 | How do C extensions allocate off-heap memory that Python profilers miss? | Hard | Lead | Internals | [Memory Management](/python-cheatsheet/03-python-internals/memory-management/) |
| 29 | What is the Global Interpreter Lock and what does it protect? | Medium | Senior Engineer | Internals | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 30 | Why was the GIL introduced in CPython — what tradeoff does it represent? | Hard | Architect | Internals | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 31 | When does CPython release the GIL during execution? | Medium | Senior Engineer | Internals | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 32 | How does the GIL limit CPU-bound multithreading — and what are the workarounds? | Medium | Senior Engineer | Internals | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 33 | What production implications does the GIL have for mixed I/O and CPU workloads? | Hard | Lead | Internals | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 34 | How does free-threading (PEP 703) change the GIL story for architects planning upgrades? | Hard | Architect | Internals | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 35 | What is C3 linearization and how does `Child.__mro__` resolve method lookup? | Medium | Senior Engineer | Core Python | [Oop](/python-cheatsheet/02-core-python/oop/) |
| 36 | How does `super()` follow MRO in cooperative multiple inheritance? | Hard | Lead | Core Python | [Oop](/python-cheatsheet/02-core-python/oop/) |
| 37 | How do decorators transform functions at definition time — `@deco` desugaring? | Medium | Senior Engineer | Core Python | [Decorators](/python-cheatsheet/02-core-python/decorators/) |
| 38 | Why is `functools.wraps` necessary on decorator wrappers? | Easy | Senior Engineer | Core Python | [Decorators](/python-cheatsheet/02-core-python/decorators/) |
| 39 | What is the difference between an iterable and an iterator? | Medium | Senior Engineer | Core Python | [Iterators](/python-cheatsheet/02-core-python/iterators/) |
| 40 | How do generator objects preserve frame state between `yield` calls? | Hard | Lead | Core Python | [Generators](/python-cheatsheet/02-core-python/generators/) |
| 41 | How do you choose between asyncio, threading, and multiprocessing for a workload? | Hard | Architect | Concurrency | [Concurrency](/python-cheatsheet/04-concurrency/concurrency/) |
| 42 | Why is a blocking call inside an async event loop catastrophic? | Medium | Senior Engineer | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 43 | How does `asyncio.TaskGroup` improve on bare `asyncio.gather` for error handling? | Medium | Lead | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 44 | When would you use `asyncio.to_thread` versus rewriting with an async library? | Medium | Senior Engineer | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 45 | How do coroutines differ from generators at the protocol level? | Hard | Lead | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 46 | What happens when a coroutine is created but never awaited? | Easy | Senior Engineer | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 47 | How does cancellation propagate through `asyncio` tasks and `CancelledError`? | Hard | Lead | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 48 | How would you size a thread pool for 500 concurrent blocking HTTP fetches? | Medium | Lead | Concurrency | [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/) |
| 49 | What is the producer-consumer pattern with `queue.Queue` and how do you shut down workers cleanly? | Medium | Senior Engineer | Concurrency | [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/) |
| 50 | How do you implement backpressure in a Python pipeline without unbounded memory? | Hard | Architect | Concurrency | [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/) |
| 51 | When is `ThreadPoolExecutor` preferable to raw `threading.Thread`? | Medium | Senior Engineer | Concurrency | [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/) |
| 52 | When is `ProcessPoolExecutor` the wrong tool despite CPU-bound work? | Hard | Lead | Concurrency | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 53 | Why does Windows require `if __name__ == '__main__'` for multiprocessing? | Medium | Senior Engineer | Concurrency | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 54 | What are the tradeoffs of `spawn` versus `fork` start methods? | Hard | Lead | Concurrency | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 55 | Why is sharing a global list across processes unsafe — what should you use instead? | Medium | Senior Engineer | Concurrency | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 56 | How expensive is pickling large objects sent to process pool workers? | Hard | Lead | Concurrency | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 57 | What synchronization primitives would you use to protect a shared counter in threads? | Medium | Senior Engineer | Concurrency | [Multithreading](/python-cheatsheet/04-concurrency/multithreading/) |
| 58 | When is `RLock` required instead of `Lock`? | Easy | Senior Engineer | Concurrency | [Multithreading](/python-cheatsheet/04-concurrency/multithreading/) |
| 59 | Why are daemon threads risky for cleanup work on process exit? | Medium | Senior Engineer | Concurrency | [Multithreading](/python-cheatsheet/04-concurrency/multithreading/) |
| 60 | How does the GIL affect a thread pool running mostly NumPy linear algebra? | Hard | Lead | Concurrency | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 61 | Compare asyncio versus threads for 1000 concurrent HTTP calls — memory and complexity. | Hard | Architect | Concurrency | [Concurrency](/python-cheatsheet/04-concurrency/concurrency/) |
| 62 | How do `contextvars` preserve request context across `asyncio` tasks? | Medium | Lead | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 63 | What is structured concurrency and how does Python 3.11+ support it? | Medium | Lead | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 64 | How would you limit concurrency to 10 simultaneous DB connections in asyncio? | Medium | Senior Engineer | Concurrency | [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/) |
| 65 | What race condition appears in `if key not in d: d[key] = []` without a lock? | Medium | Senior Engineer | Concurrency | [Multithreading](/python-cheatsheet/04-concurrency/multithreading/) |
| 66 | How do you safely publish results from multiple threads to the main thread? | Medium | Senior Engineer | Concurrency | [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/) |
| 67 | When should CPU-bound stages in a pipeline use processes after asyncio I/O stages? | Hard | Architect | Concurrency | [Concurrency](/python-cheatsheet/04-concurrency/concurrency/) |
| 68 | How does `asyncio.run()` manage the event loop lifecycle? | Easy | Senior Engineer | Concurrency | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 69 | What pitfalls arise from mixing `fork` with already-started threads? | Hard | Architect | Concurrency | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 70 | How do semaphores differ from locks for rate-limiting concurrent work? | Medium | Senior Engineer | Concurrency | [Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/) |
| 71 | What is your workflow for profiling a slow API endpoint with `cProfile`? | Medium | Senior Engineer | Performance | [Profiling](/python-cheatsheet/05-performance/profiling/) |
| 72 | How do you interpret cumulative versus per-call time in `cProfile` output? | Medium | Senior Engineer | Performance | [Profiling](/python-cheatsheet/05-performance/profiling/) |
| 73 | When would you reach for `line_profiler` over `cProfile`? | Medium | Lead | Performance | [Profiling](/python-cheatsheet/05-performance/profiling/) |
| 74 | How does `tracemalloc` help isolate memory growth by allocation site? | Medium | Senior Engineer | Performance | [Profiling](/python-cheatsheet/05-performance/profiling/) |
| 75 | What sampling profilers (e.g. `py-spy`) offer that deterministic profilers do not? | Hard | Lead | Performance | [Profiling](/python-cheatsheet/05-performance/profiling/) |
| 76 | How do you avoid measuring cold-start noise when benchmarking Python code? | Medium | Senior Engineer | Performance | [Benchmarking](/python-cheatsheet/05-performance/benchmarking/) |
| 77 | When is `timeit` insufficient and you need statistical benchmarking? | Medium | Senior Engineer | Performance | [Benchmarking](/python-cheatsheet/05-performance/benchmarking/) |
| 78 | What algorithmic changes beat micro-optimizing Python loops? | Medium | Lead | Performance | [Performance Optimization](/python-cheatsheet/05-performance/performance-optimization/) |
| 79 | When should you replace a Python hot loop with NumPy, Cython, or a C extension? | Hard | Architect | Performance | [Performance Optimization](/python-cheatsheet/05-performance/performance-optimization/) |
| 80 | How do list comprehensions compare to generator expressions for memory and speed? | Medium | Senior Engineer | Performance | [Comprehensions](/python-cheatsheet/02-core-python/comprehensions/) |
| 81 | When is `deque` strictly better than `list` for queue workloads? | Easy | Senior Engineer | Performance | [Collections](/python-cheatsheet/01-fundamentals/collections/) |
| 82 | What are the memory tradeoffs of `@dataclass(slots=True)` at scale? | Medium | Senior Engineer | Performance | [Memory Optimization](/python-cheatsheet/05-performance/memory-optimization/) |
| 83 | How do bounded caches (`lru_cache(maxsize=...)`) prevent memory leaks? | Medium | Senior Engineer | Performance | [Memory Optimization](/python-cheatsheet/05-performance/memory-optimization/) |
| 84 | When does string concatenation in a loop require `''.join` instead of `+=`? | Easy | Senior Engineer | Performance | [Performance Optimization](/python-cheatsheet/05-performance/performance-optimization/) |
| 85 | How do you profile import-time cost for CLI cold start? | Medium | Lead | Performance | [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/) |
| 86 | What dict/set operations are O(1) average and when do they degrade? | Medium | Senior Engineer | Performance | [Collections](/python-cheatsheet/01-fundamentals/collections/) |
| 87 | How would you diagnose CPU saturation versus GIL contention in threads? | Hard | Lead | Performance | [Gil](/python-cheatsheet/03-python-internals/gil/) |
| 88 | What is the cost of excessive exception handling in hot paths? | Medium | Senior Engineer | Performance | [Performance Optimization](/python-cheatsheet/05-performance/performance-optimization/) |
| 89 | How do you benchmark asyncio code without blocking the event loop? | Hard | Lead | Performance | [Benchmarking](/python-cheatsheet/05-performance/benchmarking/) |
| 90 | When does `__slots__` hurt more than help? | Medium | Senior Engineer | Performance | [Memory Optimization](/python-cheatsheet/05-performance/memory-optimization/) |
| 91 | How do you validate a performance fix did not regress memory? | Medium | Lead | Performance | [Profiling](/python-cheatsheet/05-performance/profiling/) |
| 92 | What patterns reduce pickle overhead in multiprocessing pipelines? | Hard | Lead | Performance | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 93 | How do local variables speed up attribute access in tight loops? | Easy | Senior Engineer | Performance | [Performance Optimization](/python-cheatsheet/05-performance/performance-optimization/) |
| 94 | When should you stream with generators instead of building intermediate lists? | Medium | Senior Engineer | Performance | [Generators](/python-cheatsheet/02-core-python/generators/) |
| 95 | How do you set SLO-driven performance budgets before optimizing? | Hard | Architect | Performance | [Performance Optimization](/python-cheatsheet/05-performance/performance-optimization/) |
| 96 | RSS grows steadily over 24h — how do you distinguish a leak from healthy caching? | Hard | Lead | Troubleshooting | [Profiling](/python-cheatsheet/05-performance/profiling/) |
| 97 | How do you find reference cycles holding large object graphs alive? | Hard | Lead | Troubleshooting | [Garbage Collection](/python-cheatsheet/03-python-internals/garbage-collection/) |
| 98 | Event loop is sluggish but CPU is low — what async pitfalls do you check first? | Medium | Senior Engineer | Troubleshooting | [Asyncio](/python-cheatsheet/04-concurrency/asyncio/) |
| 99 | Thread pool tasks hang on shutdown — what causes deadlock on `Queue.join`? | Medium | Senior Engineer | Troubleshooting | [Multithreading](/python-cheatsheet/04-concurrency/multithreading/) |
| 100 | Process pool workers die silently — how do you debug pickling and import errors? | Hard | Lead | Troubleshooting | [Multiprocessing](/python-cheatsheet/04-concurrency/multiprocessing/) |
| 101 | Import works locally but fails in Docker — how do you trace `sys.path` and packaging? | Medium | Senior Engineer | Troubleshooting | [Python Runtime](/python-cheatsheet/03-python-internals/python-runtime/) |
| 102 | Mutable default argument bug appears only under load — how do you reproduce and fix? | Easy | Senior Engineer | Troubleshooting | [Functions](/python-cheatsheet/01-fundamentals/functions/) |
| 103 | Closure in a loop captures wrong variable — explain and fix the late-binding trap. | Medium | Senior Engineer | Troubleshooting | [Functions](/python-cheatsheet/01-fundamentals/functions/) |
| 104 | `is` versus `==` caused a subtle bug with cached integers — walk through it. | Medium | Senior Engineer | Troubleshooting | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 105 | Descriptor on a class breaks when accessed on instance versus class — why? | Hard | Lead | Troubleshooting | [Object Model](/python-cheatsheet/03-python-internals/object-model/) |
| 106 | Circular import at startup — what refactoring patterns resolve it? | Medium | Senior Engineer | Troubleshooting | [Modules](/python-cheatsheet/01-fundamentals/modules/) |
| 107 | Unhandled exception in `__exit__` masks the original error — how does context manager protocol behave? | Medium | Senior Engineer | Troubleshooting | [Context Managers](/python-cheatsheet/02-core-python/context-managers/) |
| 108 | Generator consumed twice yields nothing the second time — how do you tee or re-fetch? | Easy | Senior Engineer | Troubleshooting | [Generators](/python-cheatsheet/02-core-python/generators/) |
| 109 | Type checker passes but runtime fails — where do annotations lie? | Medium | Senior Engineer | Troubleshooting | [Typing](/python-cheatsheet/01-fundamentals/typing/) |
| 110 | pytest tests pass locally but fail in CI intermittently — timing and isolation suspects? | Hard | Lead | Troubleshooting | [Test Strategies](/python-cheatsheet/08-testing/test-strategies/) |
| 111 | Mock patched the wrong import path — how does `patch` target resolution work? | Medium | Senior Engineer | Troubleshooting | [Mocking](/python-cheatsheet/08-testing/mocking/) |
| 112 | Logging duplicates every line three times — what handler configuration causes that? | Easy | Senior Engineer | Troubleshooting | [Logging](/python-cheatsheet/06-production-python/logging/) |
| 113 | Config missing in prod but present in staging — how do you audit env var precedence? | Medium | Lead | Troubleshooting | [Configuration Management](/python-cheatsheet/06-production-python/configuration-management/) |
| 114 | OpenTelemetry trace breaks across threads — how do you propagate context? | Hard | Lead | Troubleshooting | [Observability](/python-cheatsheet/06-production-python/observability/) |
| 115 | Wheel installs on Linux CI but not macOS dev machine — what packaging mismatch? | Medium | Senior Engineer | Troubleshooting | [Packaging](/python-cheatsheet/07-packaging-distribution/packaging/) |
| 116 | How do you structure production logging with JSON and correlation IDs? | Medium | Lead | Production | [Logging](/python-cheatsheet/06-production-python/logging/) |
| 117 | What log levels belong in hot paths versus startup diagnostics? | Easy | Senior Engineer | Production | [Logging](/python-cheatsheet/06-production-python/logging/) |
| 118 | How do you load secrets without committing them — env, vault, or runtime injection? | Hard | Architect | Production | [Configuration Management](/python-cheatsheet/06-production-python/configuration-management/) |
| 119 | What is a sane 12-factor configuration layout for a Python service? | Medium | Lead | Production | [Configuration Management](/python-cheatsheet/06-production-python/configuration-management/) |
| 120 | Which RED/USE metrics would you export from a FastAPI or Django service? | Hard | Lead | Production | [Observability](/python-cheatsheet/06-production-python/observability/) |
| 121 | How do you add OpenTelemetry tracing without drowning in span volume? | Hard | Architect | Production | [Observability](/python-cheatsheet/06-production-python/observability/) |
| 122 | Where should domain exceptions be mapped to HTTP responses in a layered app? | Medium | Lead | Production | [Error Handling](/python-cheatsheet/06-production-python/error-handling/) |
| 123 | How do you avoid logging the same stack trace in every middleware layer? | Medium | Senior Engineer | Production | [Error Handling](/python-cheatsheet/06-production-python/error-handling/) |
| 124 | What belongs on a Python service pre-deploy checklist? | Medium | Lead | Production | [Production Checklists](/python-cheatsheet/06-production-python/production-checklists/) |
| 125 | How do you pin `requires-python` and test the lower bound in CI? | Medium | Senior Engineer | Production | [Packaging](/python-cheatsheet/07-packaging-distribution/packaging/) |
| 126 | When should applications commit a lock file but libraries specify ranges only? | Medium | Lead | Production | [Dependency Management](/python-cheatsheet/07-packaging-distribution/dependency-management/) |
| 127 | How do you structure pytest for unit versus integration suites in CI? | Medium | Senior Engineer | Production | [Test Strategies](/python-cheatsheet/08-testing/test-strategies/) |
| 128 | What test doubles do you use at repository boundaries versus HTTP clients? | Medium | Lead | Production | [Mocking](/python-cheatsheet/08-testing/mocking/) |
| 129 | How do you reproduce production-only bugs with recorded fixtures safely? | Hard | Lead | Production | [Test Strategies](/python-cheatsheet/08-testing/test-strategies/) |
| 130 | What health and readiness probes should a Python worker expose in Kubernetes? | Medium | Lead | Production | [Production Checklists](/python-cheatsheet/06-production-python/production-checklists/) |
| 131 | Why are mutable default arguments dangerous — what is the correct idiom? | Easy | Senior Engineer | Core Python | [Functions](/python-cheatsheet/01-fundamentals/functions/) |
| 132 | Explain `Protocol` versus ABC for interface design in a large codebase. | Medium | Lead | Core Python | [Typing](/python-cheatsheet/01-fundamentals/typing/) |
| 133 | How do `TypedDict` and dataclasses differ for API response shapes? | Medium | Senior Engineer | Core Python | [Dataclasses](/python-cheatsheet/02-core-python/dataclasses/) |
| 134 | What does `from __future__ import annotations` change for forward references? | Medium | Senior Engineer | Core Python | [Typing](/python-cheatsheet/01-fundamentals/typing/) |
| 135 | How do context managers guarantee cleanup on exceptions? | Medium | Senior Engineer | Core Python | [Context Managers](/python-cheatsheet/02-core-python/context-managers/) |
| 136 | When is a class-based context manager better than `@contextmanager`? | Easy | Senior Engineer | Core Python | [Context Managers](/python-cheatsheet/02-core-python/context-managers/) |
| 137 | How does `ExceptionGroup` and `except*` change error handling in 3.11+? | Medium | Lead | Core Python | [Exceptions](/python-cheatsheet/01-fundamentals/exceptions/) |
| 138 | What is EAFP versus LBYL and when is each idiomatic in Python? | Easy | Senior Engineer | Core Python | [Exceptions](/python-cheatsheet/01-fundamentals/exceptions/) |
| 139 | How do you design a custom exception hierarchy for a domain module? | Medium | Lead | Core Python | [Exceptions](/python-cheatsheet/01-fundamentals/exceptions/) |
| 140 | What is `ParamSpec` for and where do generic decorators need it? | Hard | Lead | Core Python | [Typing](/python-cheatsheet/01-fundamentals/typing/) |
| 141 | How does `functools.singledispatch` enable type-based overloads? | Medium | Senior Engineer | Core Python | [Functions](/python-cheatsheet/01-fundamentals/functions/) |
| 142 | When would you choose Pydantic over a frozen dataclass at the HTTP boundary? | Medium | Lead | Core Python | [Dataclasses](/python-cheatsheet/02-core-python/dataclasses/) |
| 143 | How does `yield from` delegate to sub-generators and propagate exceptions? | Medium | Senior Engineer | Core Python | [Generators](/python-cheatsheet/02-core-python/generators/) |
| 144 | What makes an object a valid `dict` key — hashability rules? | Easy | Senior Engineer | Core Python | [Collections](/python-cheatsheet/01-fundamentals/collections/) |
| 145 | How do namespace packages (PEP 420) differ from regular packages? | Medium | Senior Engineer | Core Python | [Modules](/python-cheatsheet/01-fundamentals/modules/) |
| 146 | What is the src layout and why does it prevent import bugs? | Medium | Senior Engineer | Packaging | [Packaging](/python-cheatsheet/07-packaging-distribution/packaging/) |
| 147 | How do entry points (`[project.scripts]`) wire CLI commands? | Easy | Senior Engineer | Packaging | [Packaging](/python-cheatsheet/07-packaging-distribution/packaging/) |
| 148 | When is Poetry preferable to hatchling + uv for dependency management? | Medium | Lead | Packaging | [Poetry](/python-cheatsheet/07-packaging-distribution/poetry/) |
| 149 | How do pytest fixtures share setup across modules with `conftest.py`? | Medium | Senior Engineer | Testing | [Pytest](/python-cheatsheet/08-testing/pytest/) |
| 150 | What is the testing pyramid and how much integration testing is enough? | Medium | Lead | Testing | [Testing](/python-cheatsheet/08-testing/testing/) |
