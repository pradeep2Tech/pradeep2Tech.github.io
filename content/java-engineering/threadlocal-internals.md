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
ShowToc: true
interviewHandbook: true
---

## How does ThreadLocal work internally?

### Short Answer

Each `Thread` holds a `ThreadLocalMap` — weak keys (ThreadLocal), strong values.

### Detailed Explanation

`ThreadLocal.set` gets current thread's map, creates entry keyed by ThreadLocal identity. `get` looks up same map. Keys are weak — ThreadLocal GC'd when no strong ref, but values linger until next set/remove if key collected.

### Internal Working

OpenJDK: `Thread.threadLocals` field.

### Production Notes

Always `remove()` in finally for pool threads.

### Follow-up Questions

- ThreadLocal vs ScopedValue?
- Millions of virtual threads + ThreadLocal?

---
## ThreadLocal memory leak in thread pools?

### Short Answer

Pool threads live forever — ThreadLocal values retained until removed.

### Detailed Explanation

Request context in ThreadLocal without `remove()` after task leaks prior request data and heap. Critical in Tomcat/executor pools.

### Production Notes

try/finally with remove(); prefer ScopedValue (21+) for virtual threads.

---
