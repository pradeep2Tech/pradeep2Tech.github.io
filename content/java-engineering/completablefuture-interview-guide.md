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
ShowToc: true
interviewHandbook: true
aliases:
  - async-completablefuture
---

## thenApply vs thenCompose?

### Short Answer

`thenApply`: map result to value. `thenCompose`: flatMap — function returns another CompletableFuture.

### Detailed Explanation

Nested `get()` blocks — chain with thenCompose. Completion uses CAS on result stack (AltResult for exceptions).

### Production Notes

Always pass explicit Executor for app work — not commonPool().

### Follow-up Questions

- orTimeout / completeOnTimeout?
- exceptionally vs handle?

---
