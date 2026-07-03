---
title: "Concurrent Collections Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CHM, CopyOnWrite, BlockingQueue — when to use which."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Concurrent Collections"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.8"
ShowToc: true
interviewHandbook: true
aliases:
  - concurrent-collections-interview
---

## CHM vs Collections.synchronizedMap?

### Short Answer

CHM: bin-level locking/CAS — better write scalability. synchronizedMap: locks entire map per op.

### Detailed Explanation

CHM forbids null keys/values. Weakly consistent iterators.

### Follow-up Questions

- See ConcurrentHashMap Internals

---
## CopyOnWriteArrayList when?

### Short Answer

Read-mostly, rare writes, iterators must not throw ConcurrentModificationException.

### Detailed Explanation

Write copies entire array — O(n). Good for listener lists, config snapshots. Bad for write-heavy metrics.

---
## BlockingQueue for backpressure?

### Short Answer

Bounded queue blocks producers when full — natural backpressure for thread pools.

### Detailed Explanation

`ArrayBlockingQueue` fixed capacity; size from SLA and memory budget.

---
