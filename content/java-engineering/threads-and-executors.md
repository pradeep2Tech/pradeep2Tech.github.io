---
title: "Threads & Executors"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Thread lifecycle, pools, ForkJoinPool, shutdown, and task submission models."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Threads & Executors"
module: 6
moduleTitle: "Concurrency"
sectionRef: "6.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Platform thread = OS thread; expensive (~1MB stack default).
- Prefer `ExecutorService` over raw `new Thread()` for pool lifecycle.
- `shutdown()` vs `shutdownNow()` — graceful vs interrupt workers.
- Uncaught exception handler per thread or `ThreadFactory`.

---

## Reference Tables

| State | Meaning |
| :--- | :--- |
| NEW | Created, not started |
| RUNNABLE | Eligible to run |
| BLOCKED/WAITING/TIMED_WAITING | Parked on lock/condition/sleep |
| TERMINATED | `run` completed |

| Executor | When |
| :--- | :--- |
| `newFixedThreadPool(n)` | Bounded workers, unbounded queue |
| `newCachedThreadPool` | Short-lived bursty tasks — unbounded growth risk |
| `newSingleThreadExecutor` | Sequential tasks, ordered |
| `ForkJoinPool` | Divide-and-conquer, parallel streams |
| `Executors.newVirtualThreadPerTaskExecutor` (21+) | Massive blocking IO |

| Shutdown | Behavior |
| :--- | :--- |
| `shutdown` | No new tasks; finish queued |
| `shutdownNow` | Interrupt workers, return pending |
| `awaitTermination` | Block with timeout |

---

## Snippets

```java
ExecutorService pool = Executors.newFixedThreadPool(8);
Future<Result> f = pool.submit(() -> compute());
try {
    Result r = f.get(5, TimeUnit.SECONDS);
} finally {
    pool.shutdown();
    pool.awaitTermination(30, TimeUnit.SECONDS);
}
```

---

## Internals & Gotchas

- `Thread.start` happens-before `run` body.
- `volatile`/`synchronized` establish visibility across threads.
- Pool queue unbounded → OOM under sustained overload.

---

## Production Notes

- Name threads via custom `ThreadFactory` for diagnostics.
- Set pool sizes from metrics — not `Runtime.getRuntime().availableProcessors()` alone for mixed workloads.
- Always shutdown pools on app stop.

---

## Interview Probes


{< interview-answer >}
**Q:** Fixed pool sizing?

**A:** CPU-bound ≈ cores; blocking IO ≈ higher or virtual threads; measure queue depth and latency.
{< /interview-answer >}

{< interview-answer >}
**Q:** Difference interrupt vs shutdownNow?

**A:** `shutdownNow` interrupts running tasks; cooperative cancellation required in task loop.
{< /interview-answer >}

---

## See Also

- [Previous: Streams](/java-engineering/streams-quick-ref/)
- [Next: CompletableFuture](/java-engineering/async-completablefuture/)
- [Java Engineering Handbook Index](/java-engineering/)
