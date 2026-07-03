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
ShowToc: true
interviewHandbook: true
---

## How does ForkJoinPool work-stealing work?

### Short Answer

Each worker has deque; pushes own tasks, steals from others' deque tail when idle.

### Detailed Explanation

Divide-and-conquer tasks `fork` subtasks, `join` results. Stealing balances load. `commonPool()` shared by parallel streams and default `CompletableFuture` async — risk of starvation.

### Internal Working

Not used for virtual thread scheduling.

### Production Notes

Pass explicit Executor to CompletableFuture; don't block inside common pool.

### Follow-up Questions

- Parallel stream thread pool?

---
