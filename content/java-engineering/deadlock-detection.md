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
ShowToc: true
interviewHandbook: true
---

## Four conditions for deadlock?

### Short Answer

Mutual exclusion, hold-and-wait, no preemption, circular wait — break one to prevent.

### Detailed Explanation

Prevention: global lock ordering, `tryLock` with backoff, timeouts. Detection: thread dump shows 'Found one Java-level deadlock'.

### Production Notes

jcmd Thread.print / JFR lock events.

### Follow-up Questions

- Live lock vs deadlock?

---
