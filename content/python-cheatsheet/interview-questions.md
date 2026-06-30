---
title: "Python Interview Questions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "High-yield Python probes — GIL, MRO, decorators, mutability, and asyncio."
tags: ["python", "python-cheatsheet", "cheatsheet", "handbook"]
categories: ["Python Cheatsheet"]
shortTitle: "Interview"
module: 8
moduleTitle: "Interview Cheat Sheets"
sectionRef: "8.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Expect deep dives on mutability, GIL, MRO, decorators, and async pitfalls.
- Whiteboard API design: exceptions, typing, and context managers for resources.
- Know stdlib trade-offs — when list vs deque, dict vs DB, threads vs asyncio.

---

## Reference Tables

| Theme | Must-know |
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
| "async is always faster" | Faster when I/O wait dominates |

---

## Internals & Gotchas

- Trick questions often involve mutable default args, late-binding closures, and `is` vs `==`.
- `[[0]*3]*3` creates shared inner lists — classic gotcha.
- Descriptor protocol powers properties, classmethods, staticmethods.

---

## Production Notes

- Interviewers probe production judgment — logging, timeouts, resource cleanup.
- Mention `typing`, tests (pytest), and packaging literacy for senior roles.

---

## Interview Probes


{< interview-answer >}
**Q:** What is the GIL?

**A:** Global Interpreter Lock — mutex allowing one thread to execute Python bytecode at a time in a process. I/O and many C extensions release it. CPU-bound parallelism needs multiprocessing or native extensions.
{< /interview-answer >}

{< interview-answer >}
**Q:** Explain decorators.

**A:** Functions that take a callable and return a callable, applied at definition time via `@`. Used for cross-cutting concerns: retry, auth, timing. `functools.wraps` preserves metadata.
{< /interview-answer >}

{< interview-answer >}
**Q:** list vs tuple?

**A:** List mutable, unhashable, more memory. Tuple immutable (if elements hashable, tuple hashable), can be dict key, faster iteration, signals fixed structure.
{< /interview-answer >}

{< interview-answer >}
**Q:** How does `async/await` work?

**A:** Coroutine functions return coroutine objects scheduled on an event loop. `await` yields control until I/O completes without blocking the thread. Requires async-compatible libraries.
{< /interview-answer >}

{< interview-answer >}
**Q:** MRO in multiple inheritance?

**A:** C3 linearization orders bases for method lookup. `super()` uses MRO for cooperative calls — not simply 'parent class'.
{< /interview-answer >}

---

## See Also

- [Previous: Venv](/python-cheatsheet/virtual-environments/)
- [Python Cheatsheet Index](/python-cheatsheet/)
