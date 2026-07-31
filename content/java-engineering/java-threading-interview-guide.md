---
title: "Java Concurrency Interview Refresh"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Concurrency decisions, executors, async composition, and virtual threads in one sheet."
tags: ["java", "concurrency", "interview", "cheatsheet"]
categories: ["Java Engineering Handbook"]
shortTitle: "Concurrency"
module: 3
moduleTitle: "Concurrency Refresh"
sectionRef: "3.1"
cheatSheet: true
aliases: ["threads-and-executors", "thread-lifecycle-interview"]
---

## At a Glance

- Minimize shared mutable state; concurrency bugs are design problems before they are lock problems.
- Bound resources, define overload behavior, propagate cancellation, and measure queues and latency.
- Use virtual threads for high-concurrency blocking I/O—not to make CPU work faster.

---

## Core Guarantees

| Tool | Guarantees | Does not guarantee |
| :--- | :--- | :--- |
| `synchronized` | Mutual exclusion + visibility at monitor boundaries | Fairness or timeout |
| `volatile` | Visibility and ordering for reads/writes | Atomic compound operations such as `count++` |
| Atomic classes | Atomic single-variable updates via CAS | Multi-field invariants |
| `ReentrantLock` | Locking with timeout, interruptibility, conditions | Automatic unlock—use `finally` |
| `ConcurrentHashMap` | Thread-safe individual/atomic map operations | Atomic workflows across unrelated keys |
| Immutability | Safe sharing after safe publication | Mutable dependencies becoming safe |

## Choose the Mechanism

| Situation | Prefer | Why |
| :--- | :--- | :--- |
| Simple critical section | `synchronized` | Clear and hard to misuse |
| Counter under contention | `LongAdder` | Scales writes; snapshot is not transactional |
| Bounded producer-consumer | `BlockingQueue` | Coordination plus backpressure |
| Wait for N tasks | `CountDownLatch` | One-shot completion gate |
| Limit concurrent calls | `Semaphore` | Protects scarce downstream capacity |
| Compose async stages | `CompletableFuture` | Explicit dependency graph and error path |
| Many blocking I/O tasks | Virtual threads | Cheap thread-per-task model |
| CPU-bound parallelism | Fixed pool near core count | More threads add scheduling overhead |

## Executor Checklist

| Decision | What to say in an interview |
| :--- | :--- |
| Pool size | CPU-bound near cores; I/O-bound from measured wait/compute ratio and downstream limits |
| Queue | Bounded; capacity follows memory budget and acceptable waiting time |
| Rejection | Fail fast, shed load, or caller-runs; never silently drop business work |
| Shutdown | Stop intake, await completion, then force/cancel with a deadline |
| Observability | Active threads, queue depth, rejection count, task latency, downstream saturation |

## CompletableFuture and Virtual Threads

| Question | Quick answer |
| :--- | :--- |
| `thenApply` vs `thenCompose` | Transform a result vs flatten a dependent async stage |
| Independent calls | Start together, combine, apply per-call timeouts, preserve errors |
| Common-pool risk | Blocking tasks can starve unrelated work; choose an explicit executor when needed |
| Virtual-thread fit | Request-per-thread code dominated by blocking I/O |
| Virtual-thread limits | CPU, database connections, sockets, and downstream quotas still need bounds |
| Pinning | Blocking while holding some monitors/native frames can occupy a carrier; measure before redesigning |

## Incident Prompts

- **Rejected tasks:** inspect arrival rate, task duration, queue depth, pool configuration, and downstream latency; do not only enlarge the pool.
- **Deadlock:** capture multiple thread dumps, find a lock cycle, then fix lock ordering or ownership.
- **Duplicate payments:** use idempotency and database constraints first; an in-process lock does not protect multiple instances.
- **ThreadLocal leak:** always clean in `finally`; avoid request context hidden in pooled threads.
- **High CPU:** identify hot threads with thread dumps/JFR, then distinguish busy loops, contention, GC, and legitimate load.

## Quick Gotchas

- `sleep` does not release a monitor; `wait` does.
- Always restore interruption or propagate cancellation.
- Never call remote services while holding a broad lock.
- Parallel streams share infrastructure and are not a default performance switch.
- Thread safety includes compound invariants, publication, lifecycle, and failure behavior.

---

## See Also

[← Collections](/java-engineering/collection-selection-matrix/) · [JVM in Production →](/java-engineering/jvm-memory-gc-oom-guide/)
