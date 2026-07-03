---
title: "Memory Diagram (Cheat Sheet)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "One-screen stack, heap, metaspace, and object layout."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Memory Diagram"
module: 6
moduleTitle: "Interview Cheat Sheets"
sectionRef: "6.2"
ShowToc: true
interviewHandbook: true
cheatSheet: true
aliases:
  - memory-diagram-interview
---


```mermaid
flowchart TB
  subgraph perThread [Per thread]
    stack[Stack - frames]
    pc[Program Counter]
  end
  subgraph shared [Shared]
    heap[Heap - Young / Old]
    meta[Metaspace]
    code[Code Cache]
  end
  stack --> heap
```

| Region | Stores | GC |
| :--- | :--- | :--- |
| Stack | Locals, refs | Auto on pop |
| Eden | New objects | Minor GC |
| Old | Tenured | Major / mixed |
| Metaspace | Class metadata | Class unloading |
| Direct | NIO buffers | Cleaner |

| Object (64b, compressed oops) | |
| :--- | :--- |
| Mark word | Hash, locks, GC age |
| Klass pointer | Class metadata |
| Fields | + padding |

**Deep dive:** [JVM Memory, GC & OOM Guide](/java-engineering/jvm-memory-gc-oom-guide/)
