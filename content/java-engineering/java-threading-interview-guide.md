---
title: "Java Threading Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Thread lifecycle, executors, shutdown, platform vs virtual threads."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Threading"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.1"
ShowToc: true
interviewHandbook: true
aliases:
  - threads-and-executors
  - thread-lifecycle-interview
---

## Platform thread states — BLOCKED vs WAITING?

### Short Answer

BLOCKED: waiting for monitor entry. WAITING: voluntary park without timeout (`wait`, `join`, `park`).

### Detailed Explanation

`RUNNABLE` includes running or ready on CPU queue. `TIMED_WAITING`: sleep, timed wait/join.

### Internal Working

See [Thread Lifecycle Cheat Sheet](/java-engineering/thread-lifecycle-cheatsheet/) for diagram.

### Follow-up Questions

- How do virtual threads affect thread dumps?

---
## Fixed thread pool sizing?

### Short Answer

CPU-bound ≈ cores; blocking IO needs higher pool or virtual threads; measure queue depth and latency.

### Detailed Explanation

`newFixedThreadPool` has unbounded queue — sustained overload causes OOM. Always `shutdown()` + `awaitTermination` on app stop.

### Internal Working

Name threads via custom ThreadFactory for diagnostics.

### Production Notes

Using `availableProcessors()` alone for mixed IO/CPU workloads.

### Follow-up Questions

- shutdown vs shutdownNow?
- When cached thread pool?

---
## Thread.start happens-before run?

### Short Answer

Yes — actions in parent before `start()` visible to child thread when `run` begins.

### Detailed Explanation

Part of JMM happens-before rules. Also monitor unlock/lock, volatile write/read.

### Follow-up Questions

- See Java Memory Model page

---
