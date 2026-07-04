---
title: "CompletableFuture Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Composition, executors, timeouts, exception handling."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "CompletableFuture"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.10"
interviewHandbook: true
aliases:
  - async-completablefuture
---

## thenApply vs thenCompose?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

`thenApply`: map result to value. `thenCompose`: flatMap — function returns another CompletableFuture.

### Detailed Explanation

Nested `get()` blocks — chain with thenCompose. Completion uses CAS on result stack (AltResult for exceptions).

### Production Notes

Always pass explicit Executor for app work — not commonPool().

### Interview Questions

1. orTimeout / completeOnTimeout?
2. exceptionally vs handle?

### Follow-up Questions

- orTimeout / completeOnTimeout?
- exceptionally vs handle?

---
## CompletableFuture allOf vs anyOf?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

`allOf` completes when all complete (void aggregate). `anyOf` completes when first completes.

### Detailed Explanation

Use `allOf` then join each future for batch fan-in. `anyOf` for racing redundant calls — cancel losers to avoid waste.

### Production Notes

Set timeouts on each leg; do not block on `get()` without timeout in reactive services.

### Interview Questions

1. See [Virtual Threads](/java-engineering/virtual-threads-interview-guide/) for blocking style

### Follow-up Questions

- See [Virtual Threads](/java-engineering/virtual-threads-interview-guide/) for blocking style

---
## exceptionally vs handle?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

`exceptionally` only runs on failure and returns recovery value. `handle` runs always with (result, ex) — unified success/failure path.

### Detailed Explanation

Prefer `handle` when both branches need same downstream type. `whenComplete` for side effects without transforming result.

---
