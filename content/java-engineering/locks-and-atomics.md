---
title: "Locks & Atomics"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "synchronized, volatile, ReentrantLock, StampedLock, Atomic* and VarHandle."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Locks & Atomics"
module: 6
moduleTitle: "Concurrency"
sectionRef: "6.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `synchronized` — intrinsic lock on object/monitor.
- `volatile` — visibility + ordering, not atomic compound ops.
- `ReentrantLock` — tryLock, fairness, interruptible lock.
- `java.util.concurrent.atomic.*` — CAS primitives for counters/flags.

---

## Reference Tables

| Mechanism | Scope | Best for |
| :--- | :--- | :--- |
| `synchronized` | Block/method | Simple mutual exclusion |
| `volatile` | Field | Single-writer flags, DCL idiom (with care) |
| `ReentrantLock` | Explicit | tryLock, timeouts, conditions |
| `ReadWriteLock` | Read-heavy | Many readers, rare writers |
| `StampedLock` | Optimistic read | Read-mostly with validation |
| `AtomicInteger` etc. | Single variable | Counters, sequence |

| `happens-before` edge | |
| :--- | :--- |
| Monitor unlock → lock | `synchronized` |
| `volatile` write → read | Visibility |
| `Thread.start` | Start of thread |
| `Concurrent` utils | Documented per class |

| Deadlock needs | Prevention |
| :--- | :--- |
| Circular wait | Lock ordering |
| Hold and wait | tryLock with backoff |
| | Timed locks |

---

## Snippets

```java
private final AtomicLong seq = new AtomicLong();
long next = seq.incrementAndGet();

lock.lock();
try {
    // critical section
} finally {
    lock.unlock();
}
```

---

## Internals & Gotchas

- `synchronized` biased locking (historically) — JVM elides uncontended locks until revocation.
- `VarHandle` (9+) — low-level fences on fields/arrays.
- False sharing: pad hot counters or use `@Contended` (JVM flag).

---

## Production Notes

- Prefer higher-level `ConcurrentHashMap`, `LongAdder` over raw locks when fits.
- Always `unlock` in `finally`.
- Avoid `synchronized` on Strings/literals/boxed Integers — intern collisions.

---

## Interview Probes


{< interview-answer >}
**Q:** volatile enough for i++?

**A:** No — read-modify-write not atomic. Use `AtomicInteger` or synchronization.
{< /interview-answer >}

{< interview-answer >}
**Q:** ReentrantLock vs synchronized?

**A:** Lock: tryLock, fairness, multiple Conditions. synchronized: simpler, JVM optimized, blocks in thread dump clearly.
{< /interview-answer >}

---

## See Also

- [Previous: CompletableFuture](/java-engineering/async-completablefuture/)
- [Next: Coordination](/java-engineering/concurrent-coordination/)
- [Java Engineering Handbook Index](/java-engineering/)
