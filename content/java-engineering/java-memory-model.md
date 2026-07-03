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
ShowToc: true
interviewHandbook: true
---

## What is happens-before?

### Short Answer

Partial ordering guaranteeing visibility — if A happens-before B, B sees A's writes.

### Detailed Explanation

Rules: monitor unlock→lock, volatile write→read, thread start/join, `Concurrent` utilities documented edges. Without happens-before, threads may see stale values due to CPU cache and compiler reordering.

### Internal Working

JMM defines what reorderings are legal; synchronized/volatile constrain them.

### Follow-up Questions

- volatile vs synchronized?
- Double-checked locking fix?

---
## What does volatile guarantee?

### Short Answer

Visibility and ordering for reads/writes — not atomicity of compound ops like i++.

### Detailed Explanation

Volatile read/write establish happens-before. No torn reads/writes for 32/64-bit volatiles on supported platforms. i++ is read-modify-write — use `AtomicInteger` or lock.

### Follow-up Questions

- Why volatile not enough for i++?

---
