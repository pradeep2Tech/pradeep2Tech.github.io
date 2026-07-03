---
title: "Virtual Threads Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Carriers, pinning, structured concurrency, ScopedValue vs ThreadLocal."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Virtual Threads"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.11"
ShowToc: true
interviewHandbook: true
aliases:
  - virtual-threads-structured-concurrency
---

## Platform vs virtual threads?

### Short Answer

Platform: 1:1 OS thread, ~MB stack. Virtual: JVM-scheduled, cheap — mount on carrier pool.

### Detailed Explanation

Blocking IO on VT releases carrier when unmounted. Massive concurrency for thread-per-request without reactive rewrite.

### Follow-up Questions

- What is pinning?
- Structured concurrency goal?

---
## What is thread pinning?

### Short Answer

Virtual thread blocks carrier when holding synchronized monitor or native code — limits scalability.

### Detailed Explanation

ReentrantLock doesn't pin (usually). Monitor pinning improved in newer JDKs — still audit synchronized blocks on hot paths.

### Production Notes

Review JDBC drivers, JNI, synchronized — use jfr pinning events.

---
