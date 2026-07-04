---
title: "Architect-Level Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Curated architect-level Python interview questions."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Architect"
module: 9
moduleTitle: "Interview Guide"
sectionRef: "9.2"
weight: 902
interviewHandbook: true
---

Questions only — no answers.

# Architect-Level Questions

1. Walk through what happens from `python script.py` to the first line of user code executing.
2. What roles do `sys.meta_path`, finders, and loaders play in the import system?
3. Describe the major subsystems of the CPython interpreter at a high level.
4. What is the eval loop (`ceval`) and what does it execute?
5. How does CPython compile source to bytecode — parser, AST, and compiler stages?
6. How does attribute lookup work on instances — `__dict__`, class, MRO, descriptors?
7. What is pymalloc and how do arenas/pools affect fragmentation?
8. Why was the GIL introduced in CPython — what tradeoff does it represent?
9. How does free-threading (PEP 703) change the GIL story for architects planning upgrades?
10. How do you choose between asyncio, threading, and multiprocessing for a workload?
11. How do you implement backpressure in a Python pipeline without unbounded memory?
12. Compare asyncio versus threads for 1000 concurrent HTTP calls — memory and complexity.
13. When should CPU-bound stages in a pipeline use processes after asyncio I/O stages?
14. What pitfalls arise from mixing `fork` with already-started threads?
15. When should you replace a Python hot loop with NumPy, Cython, or a C extension?
16. How do you set SLO-driven performance budgets before optimizing?
17. How do you load secrets without committing them — env, vault, or runtime injection?
18. How do you add OpenTelemetry tracing without drowning in span volume?
