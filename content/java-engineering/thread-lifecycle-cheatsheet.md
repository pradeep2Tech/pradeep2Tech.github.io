---
title: "Thread Lifecycle (Cheat Sheet)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Platform thread state diagram and virtual thread notes."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Thread Lifecycle"
module: 6
moduleTitle: "Interview Cheat Sheets"
sectionRef: "6.3"
interviewHandbook: true
cheatSheet: true
aliases:
  - thread-lifecycle-interview
---


```mermaid
stateDiagram-v2
  [*] --> NEW
  NEW --> RUNNABLE: start
  RUNNABLE --> BLOCKED: monitor lock
  RUNNABLE --> WAITING: wait/join/park
  RUNNABLE --> TIMED_WAITING: sleep/timeout
  BLOCKED --> RUNNABLE: lock acquired
  WAITING --> RUNNABLE: notify/unpark
  TIMED_WAITING --> RUNNABLE: timeout
  RUNNABLE --> TERMINATED: run ends
```

| State | Cause |
| :--- | :--- |
| BLOCKED | Waiting for synchronized monitor |
| WAITING | `wait`, `join`, `park` — no timeout |
| TIMED_WAITING | `sleep`, timed `wait`/`join` |

| Platform vs Virtual | |
| :--- | :--- |
| Cost | ~MB stack vs cheap VT |
| Blocking IO | VT unmounts carrier; pinning if synchronized/native |

**Deep dive:** [Java Threading Interview Guide](/java-engineering/java-threading-interview-guide/)
