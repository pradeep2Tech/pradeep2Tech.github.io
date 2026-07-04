---
title: "Deadlock Detection & Prevention"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Four conditions, lock ordering, tryLock, thread dump analysis."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Deadlock"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.7"
interviewHandbook: true
---

## Four conditions for deadlock?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Mutual exclusion, hold-and-wait, no preemption, circular wait — break one to prevent.

### Detailed Explanation

Prevention: global lock ordering, `tryLock` with backoff, timeouts. Detection: thread dump shows 'Found one Java-level deadlock'.

### Production Notes

jcmd Thread.print / JFR lock events.

### Interview Questions

1. Break circular wait without global ordering — possible?
2. Difference between deadlock and livelock?
3. How does `ReentrantLock.tryLock` help?

### Follow-up Questions

- Live lock vs deadlock?

---
## How do you diagnose deadlock in production?

**Difficulty:** Medium · **Time:** 2 min

### Short Answer

Thread dump (`jcmd <pid> Thread.print`, `jstack`) shows 'Found one Java-level deadlock' with cycle. JFR `jdk.JavaMonitorEnter` / lock events give timing.

### Detailed Explanation

Prevention beats detection: consistent lock order, timeout locks, avoid nested locks across subsystems. Libraries like deadlock detectors in tests (cycle in lock graph).

### Interview Questions

1. Can you have deadlock without synchronized?
2. Database deadlock vs JVM deadlock — same four conditions?

---
## Deadlock Interview Drill

### 1. Transfer between two accounts — classic fix?

Lock accounts in consistent order (e.g. by id).

---

### 2. tryLock with timeout — what do you do on failure?

Backoff, log, fail transaction, or ordered retry.

---
