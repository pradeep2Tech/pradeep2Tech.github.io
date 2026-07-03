---
title: "Performance Optimization"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "CPU/memory optimization, data structures, best practices. Profile first — [Profiling](/python-cheatsheet/05-performance/"
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Perf Opt"
module: 5
moduleTitle: "Performance"
sectionRef: "5.1"
weight: 501
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- Profile first — [Profiling](/python-cheatsheet/05-performance/profiling/) before micro-opts.
- Win on algorithm and data structure, then C extensions/NumPy, then bytecode tricks.
- Set SLO budgets (p95 latency, RSS) before tuning.

## Core Concepts

| Layer | Actions |
| :--- | :--- |
| Algorithm | Better complexity class, fewer passes |
| Data structures | `deque`, `set`, generators vs materialized lists |
| Stdlib vs native | NumPy, `orjson`, Rust/C extensions for hot loops |
| Interpreter | Locals over globals; avoid attribute chains in tight loops |

## Internal Working

Python bytecode executes under the [GIL](/python-cheatsheet/03-python-internals/gil/) in threads — CPU-bound pure Python needs processes or native code. Optimizing Python loops without measuring often fights the interpreter instead of the real bottleneck.

## Design Tradeoffs

| Choice | Trade-off |
| :--- | :--- |
| List comp vs generator | Memory vs reuse/random access |
| `__slots__` | Memory vs flexibility |
| Cython/Rust extension | Speed vs build/deploy complexity |
| Async rewrite | Throughput vs library ecosystem |

## Production Usage

- Establish baseline with `cProfile` + `tracemalloc` on representative traffic.
- Optimize top 3 cumulative-time functions only; re-profile after each change.
- Document performance assumptions in ADRs for hot services.

## Performance Considerations

- Exception-based control flow in hot paths is costly.
- String `+=` in loops — use `''.join` for many concatenations.
- Import time matters for CLI/serverless cold start.

## Troubleshooting

| Symptom | Likely cause |
| :--- | :--- |
| CPU high, few threads busy | GIL + CPU-bound Python loop |
| Memory climb per request | Unbounded list materialization or cache |
| Slow after deploy | New import side effect or logging volume |

## Common Mistakes

- Premature optimization without profiler evidence.
- Rewriting in async when workload is CPU-bound.

## Architect Notes

Performance work is a **measurement discipline** — tie every change to a metric and rollback plan.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Concurrency Patterns](/python-cheatsheet/04-concurrency/concurrency-patterns/)
- [Next: Profiling](/python-cheatsheet/05-performance/profiling/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
