---
title: "Locks & Atomics Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "synchronized, volatile, ReentrantLock, atomics, and when each is architecturally correct."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Locks & Atomics"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.3"
interviewHandbook: true
---

## Why is volatile not enough for i++?

### Short Answer

`volatile` guarantees visibility and ordering, not atomicity of read-modify-write operations.

### Detailed Explanation

`i++` compiles to load → increment → store. Another thread can interleave between steps, losing updates. Use `AtomicInteger.incrementAndGet()`, `synchronized`, or `Lock` for compound updates.

### Internal Working

`volatile` inserts memory barriers so writes are visible to subsequent reads across threads. It does not make the full RMW sequence atomic.

### Production Notes

Prefer `LongAdder` for high-contention counters; `AtomicLong` when you need a consistent read of the exact value.

### Common Mistakes

Declaring a counter `volatile` and expecting thread-safe increments.

### Follow-up Questions

- [CAS & Lock-Free Programming](/java-engineering/cas-and-lock-free-programming/)
- [Java Memory Model](/java-engineering/java-memory-model/)

---

## synchronized vs ReentrantLock?

### Short Answer

`synchronized` is simpler and JVM-optimized; `ReentrantLock` offers `tryLock`, fairness, timeouts, and multiple `Condition`s.

### Detailed Explanation

Both provide mutual exclusion and memory visibility (monitor release/acquire establishes happens-before). `ReentrantLock` must `unlock()` in `finally`. Avoid locking on `String` literals or boxed integers (intern collisions).

### Production Notes

Always `unlock()` in `finally`. For read-heavy maps, prefer `ConcurrentHashMap` over wrapping with locks.

### Follow-up Questions

- `ReadWriteLock` vs `StampedLock` optimistic read?
- [Deadlock Detection](/java-engineering/deadlock-detection/)

---

## Mechanism selection

| Mechanism | Best for |
| :--- | :--- |
| `synchronized` | Simple mutual exclusion |
| `volatile` | Single-writer flags, publication |
| `ReentrantLock` | tryLock, timeouts, conditions |
| `ReadWriteLock` | Many readers, rare writers |
| `StampedLock` | Read-mostly with validation |
| `Atomic*` | Counters, flags, CAS updates |

---

## See Also

- [Previous: Java Memory Model](/java-engineering/java-memory-model/)
- [Next: CAS & Lock-Free](/java-engineering/cas-and-lock-free-programming/)
- [ConcurrentHashMap Internals](/java-engineering/concurrenthashmap-internals/)
- [Java Engineering Handbook Index](/java-engineering/)
