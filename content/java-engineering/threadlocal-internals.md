---
title: "ThreadLocal Internals"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Per-thread storage, ThreadLocalMap, leaks in pooled threads."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "ThreadLocal"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.5"
interviewHandbook: true
---

`ThreadLocal` gives each thread its own copy of a variable — common for `SimpleDateFormat`, request context, and tracing IDs. In **pooled threads**, failure to `remove()` causes leaks and cross-request contamination.

---

## How does ThreadLocal work internally?

**Difficulty:** Medium · **Time:** 2 min

### Short Answer

Each `Thread` holds a `ThreadLocalMap` — weak keys (ThreadLocal), strong values.

### Detailed Explanation

`ThreadLocal.set` gets current thread's map, creates entry keyed by ThreadLocal identity. `get` looks up same map. Keys are weak — ThreadLocal GC'd when no strong ref, but values linger until next set/remove if key collected.

### Internal Working

OpenJDK: `Thread.threadLocals` field.

### Production Notes

Always `remove()` in finally for pool threads.

### Interview Questions

1. ThreadLocal vs ScopedValue?
2. Millions of virtual threads + ThreadLocal?

### Follow-up Questions

- ThreadLocal vs ScopedValue?
- Millions of virtual threads + ThreadLocal?

---
## ThreadLocal memory leak in thread pools?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Pool threads live forever — ThreadLocal values retained until removed.

### Detailed Explanation

Request context in ThreadLocal without `remove()` after task leaks prior request data and heap. Critical in Tomcat/executor pools.

### Production Notes

try/finally with remove(); prefer ScopedValue (21+) for virtual threads.

### Interview Questions

1. Why are ThreadLocal keys weak but values strong?
2. What breaks if you use ThreadLocal with 1M virtual threads?
3. How would you migrate request context to ScopedValue?

---
## ThreadLocal vs ScopedValue (Java 21+)?

**Difficulty:** Medium · **Time:** 2 min

### Short Answer

`ScopedValue` binds immutable context for a **dynamic scope** — inherited by child threads, no map per thread, better for virtual threads.

### Detailed Explanation

ThreadLocal: map on each `Thread`, manual remove. ScopedValue: `ScopedValue.where(KEY, value).run(() -> ...)` — automatic cleanup when scope ends. Preferred for request context in VT-heavy apps.

### Interview Questions

1. Can ScopedValue replace all ThreadLocal uses?
2. How does structured concurrency interact with ScopedValue?

---
## ThreadLocal Interview Drill

### 1. Symptom: user A sees user B data in Tomcat — cause?

ThreadLocal not cleared in pool thread after request.

---

### 2. Where is ThreadLocalMap stored?

On the Thread object (`threadLocals` field).

---
