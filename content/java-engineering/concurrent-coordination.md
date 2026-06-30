---
title: "Concurrent Coordination"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CountDownLatch, CyclicBarrier, Semaphore, Phaser, Exchanger use cases."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Coordination"
module: 6
moduleTitle: "Concurrency"
sectionRef: "6.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Coordination primitives — not data structures.
- `CountDownLatch` — one-shot wait for N events.
- `CyclicBarrier` — reusable rendezvous; optional barrier action.
- `Semaphore` — permit pool; not mutual exclusion unless 1 permit.

---

## Reference Tables

| Class | Reusable | Typical pattern |
| :--- | :---: | :--- |
| `CountDownLatch` | No | Start gun / await startup |
| `CyclicBarrier` | Yes | Parallel phases |
| `Semaphore` | Yes | Limit concurrency |
| `Phaser` | Yes | Dynamic party count |
| `Exchanger` | Yes | Pair swap buffer |

| vs `join()` | Coordination primitive |
| :--- | :--- |
| Thread join | One thread completion |
| Latch | Many events, any thread counts down |
| Barrier | Threads meet at phase gate |

| `Phaser` advantage | |
| :--- | :--- |
| Dynamic register/deregister | Flexible fork/join workflows |
| Tiered phases | Multi-stage pipelines |

---

## Snippets

```java
var start = new CountDownLatch(1);
var done = new CountDownLatch(workerCount);
for (int i = 0; i < workerCount; i++) {
    pool.execute(() -> {
start.await();
try { work(); } finally { done.countDown(); }
    });
}
start.countDown();
done.await();
```

---

## Internals & Gotchas

- Await parks thread (platform) — virtual threads unmount carrier.
- Barrier broken if thread interrupted/timeout — reset or new instance.
- Semaphore fairness flag reduces throughput.

---

## Production Notes

- Prefer structured concurrency (21+) over manual latch/barrier wiring where possible.
- Always handle `InterruptedException` — restore interrupt flag.
- Time-bound waits in prod: `await(timeout, unit)`.

---

## Interview Probes


{< interview-answer >}
**Q:** Latch vs Barrier?

**A:** Latch: one or more threads wait for count to zero (one-shot). Barrier: N threads wait for each other at point, reusable.
{< /interview-answer >}

{< interview-answer >}
**Q:** Semaphore vs fixed pool?

**A:** Semaphore limits concurrent access to resource; thread pool limits threads executing tasks — related but different layer.
{< /interview-answer >}

---

## See Also

- [Previous: Locks & Atomics](/java-engineering/locks-and-atomics/)
- [Next: Virtual Threads](/java-engineering/virtual-threads-structured-concurrency/)
- [Java Engineering Handbook Index](/java-engineering/)
