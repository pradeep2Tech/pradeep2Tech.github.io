---
title: "Performance Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Python performance and tuning interview questions."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Performance Q"
module: 9
moduleTitle: "Interview Guide"
sectionRef: "9.4"
weight: 904
ShowToc: true
interviewHandbook: true
---

Questions only — no answers.

# Performance Questions

1. What is your workflow for profiling a slow API endpoint with `cProfile`?
2. How do you interpret cumulative versus per-call time in `cProfile` output?
3. When would you reach for `line_profiler` over `cProfile`?
4. How does `tracemalloc` help isolate memory growth by allocation site?
5. What sampling profilers (e.g. `py-spy`) offer that deterministic profilers do not?
6. How do you avoid measuring cold-start noise when benchmarking Python code?
7. When is `timeit` insufficient and you need statistical benchmarking?
8. What algorithmic changes beat micro-optimizing Python loops?
9. When should you replace a Python hot loop with NumPy, Cython, or a C extension?
10. How do list comprehensions compare to generator expressions for memory and speed?
11. When is `deque` strictly better than `list` for queue workloads?
12. What are the memory tradeoffs of `@dataclass(slots=True)` at scale?
13. How do bounded caches (`lru_cache(maxsize=...)`) prevent memory leaks?
14. When does string concatenation in a loop require `''.join` instead of `+=`?
15. How do you profile import-time cost for CLI cold start?
16. What dict/set operations are O(1) average and when do they degrade?
17. How would you diagnose CPU saturation versus GIL contention in threads?
18. What is the cost of excessive exception handling in hot paths?
19. How do you benchmark asyncio code without blocking the event loop?
20. When does `__slots__` hurt more than help?
21. How do you validate a performance fix did not regress memory?
22. What patterns reduce pickle overhead in multiprocessing pipelines?
23. How do local variables speed up attribute access in tight loops?
24. When should you stream with generators instead of building intermediate lists?
25. How do you set SLO-driven performance budgets before optimizing?
