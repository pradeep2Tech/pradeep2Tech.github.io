---
title: "Java Memory Model Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "happens-before, visibility, ordering, and volatile semantics."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "JMM"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.2"
interviewHandbook: true
---

The **Java Memory Model (JMM)** defines which writes are visible to which reads across threads. Without happens-before edges, CPUs and compilers may reorder or cache values — leading to subtle bugs in double-checked locking, lazy init, and lock-free code.

---

## What is happens-before?

**Difficulty:** Hard · **Time:** 3 min

### Short Answer

Partial ordering guaranteeing visibility — if A happens-before B, B sees A's writes.

### Detailed Explanation

Rules: monitor unlock→lock, volatile write→read, thread start/join, `Concurrent` utilities documented edges. Without happens-before, threads may see stale values due to CPU cache and compiler reordering.

### Internal Working

JMM defines what reorderings are legal; synchronized/volatile constrain them.

### Interview Questions

1. volatile vs synchronized?
2. Double-checked locking fix?

### Follow-up Questions

- volatile vs synchronized?
- Double-checked locking fix?

---
## What does volatile guarantee?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Visibility and ordering for reads/writes — not atomicity of compound ops like i++.

### Detailed Explanation

Volatile read/write establish happens-before. No torn reads/writes for 32/64-bit volatiles on supported platforms. i++ is read-modify-write — use `AtomicInteger` or lock.

### Interview Questions

1. Why volatile not enough for i++?

### Follow-up Questions

- Why volatile not enough for i++?

---
## Double-checked locking — why broken and fix?

**Difficulty:** Hard · **Time:** 2 min

### Short Answer

Without volatile on instance ref, another thread may see partially constructed object due to reordering.

### Detailed Explanation

Fix: `private volatile Singleton instance`, holder idiom, or enum singleton. Volatile write establishes happens-before for readers.

### Production Notes

Prefer DI or enum singleton — avoid hand-rolled DCL in new code.

### Common Mistakes

- DCL without volatile on the instance reference (broken pre-JMM5 pattern).
- Using volatile on fields inside the object but not on the publishing reference.

### Interview Questions

1. List three happens-before rules without looking them up.
2. Why does `Thread.start` establish happens-before?
3. Safe publication: stack confinement vs volatile vs final fields?

### Follow-up Questions

- Safe publication idioms?

---
## JMM Interview Drill

### 1. Is `volatile` enough for `count++`?

No — compound RMW needs atomics or synchronization.

---

### 2. Does reordering happen on single-threaded code?

Yes, compiler may reorder if as-if-serial semantics preserved.

---

### 3. How does `ConcurrentHashMap` relate to JMM?

Documented happens-before on successful `put` → subsequent `get`.

---
