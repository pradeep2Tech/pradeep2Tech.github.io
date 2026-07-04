---
title: "ForkJoinPool Internals"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Work-stealing, common pool, parallel streams, CompletableFuture default executor."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "ForkJoinPool"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.6"
interviewHandbook: true
---

## How does ForkJoinPool work-stealing work?

**Difficulty:** Hard · **Time:** 2 min

### Short Answer

Each worker has deque; pushes own tasks, steals from others' deque tail when idle.

### Detailed Explanation

Divide-and-conquer tasks `fork` subtasks, `join` results. Stealing balances load. `commonPool()` shared by parallel streams and default `CompletableFuture` async — risk of starvation.

### Internal Working

Not used for virtual thread scheduling.

### Production Notes

Pass explicit Executor to CompletableFuture; don't block inside common pool.

### Interview Questions

1. Why is blocking in parallelStream dangerous?
2. ForkJoinPool common pool parallelism default?
3. Difference between work-stealing and traditional thread pool queue?

### Follow-up Questions

- Parallel stream thread pool?

---
## Parallel streams and common pool pitfalls?

**Difficulty:** Medium · **Time:** 2 min

### Short Answer

`parallelStream()` uses `ForkJoinPool.commonPool()` — shared globally; blocking or IO inside pipeline starves other users of the pool.

### Detailed Explanation

Fix: custom pool via `ForkJoinPool.submit(() -> list.parallelStream()...).get()` or use explicit Executor. CPU-bound, non-blocking transforms only in parallel streams.

### Common Mistakes

- Calling `parallelStream` on small collections — overhead exceeds benefit.

### Interview Questions

1. When is parallelStream actually faster?
2. How does Spliterator SPLIT_CHARACTERISTICS affect parallelism?

---
## ForkJoinPool Interview Drill

### 1. CompletableFuture.supplyAsync with no executor — which pool?

ForkJoinPool.commonPool().

---

### 2. Virtual threads use ForkJoinPool?

No — carrier pool is separate (ForkJoinPool by default for carriers).

---
