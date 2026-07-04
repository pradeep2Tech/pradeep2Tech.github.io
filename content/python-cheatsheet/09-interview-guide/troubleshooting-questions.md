---
title: "Troubleshooting Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Production troubleshooting interview questions for Python."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Troubleshooting Q"
module: 9
moduleTitle: "Interview Guide"
sectionRef: "9.3"
weight: 903
interviewHandbook: true
---

Questions only — no answers.

# Troubleshooting Questions

1. RSS grows steadily over 24h — how do you distinguish a leak from healthy caching?
2. How do you find reference cycles holding large object graphs alive?
3. Event loop is sluggish but CPU is low — what async pitfalls do you check first?
4. Thread pool tasks hang on shutdown — what causes deadlock on `Queue.join`?
5. Process pool workers die silently — how do you debug pickling and import errors?
6. Import works locally but fails in Docker — how do you trace `sys.path` and packaging?
7. Mutable default argument bug appears only under load — how do you reproduce and fix?
8. Closure in a loop captures wrong variable — explain and fix the late-binding trap.
9. `is` versus `==` caused a subtle bug with cached integers — walk through it.
10. Descriptor on a class breaks when accessed on instance versus class — why?
11. Circular import at startup — what refactoring patterns resolve it?
12. Unhandled exception in `__exit__` masks the original error — how does context manager protocol behave?
13. Generator consumed twice yields nothing the second time — how do you tee or re-fetch?
14. Type checker passes but runtime fails — where do annotations lie?
15. pytest tests pass locally but fail in CI intermittently — timing and isolation suspects?
16. Mock patched the wrong import path — how does `patch` target resolution work?
17. Logging duplicates every line three times — what handler configuration causes that?
18. Config missing in prod but present in staging — how do you audit env var precedence?
19. OpenTelemetry trace breaks across threads — how do you propagate context?
20. Wheel installs on Linux CI but not macOS dev machine — what packaging mismatch?
