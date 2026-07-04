---
title: "JVM Memory, GC & OOM Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Heap regions, collectors, leaks, OOM types, and diagnosis."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Memory & GC"
module: 4
moduleTitle: "JVM"
sectionRef: "4.1"
interviewHandbook: true
aliases:
  - jvm-memory-and-gc
  - memory-leaks-and-oom
  - memory-diagram-interview
  - gc-summary-interview
---

## Stack vs heap?

**Difficulty:** Easy · **Time:** 30 sec

### Short Answer

Stack: per-thread frames, primitives and references, automatic lifetime. Heap: shared objects, GC-managed.

### Detailed Explanation

References on stack point to heap objects. Static field data lives in heap; class metadata in Metaspace.

### Internal Working

See [Memory Diagram Cheat Sheet](/java-engineering/memory-diagram-cheatsheet/).

### Interview Questions

1. Where do static fields live?

### Follow-up Questions

- Where do static fields live?

---
## Minor vs major GC?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Minor: young gen (Eden/Survivor), frequent, usually short STW. Major/old: tenured collection — longer unless concurrent collector.

### Detailed Explanation

Generational hypothesis: most objects die young. Promotion when survivors exceed age threshold.

### Internal Working

TLAB: per-thread Eden buffers reduce allocation contention.

### Interview Questions

1. G1 mixed GC?
2. When ZGC over G1?

### Follow-up Questions

- G1 mixed GC?
- When ZGC over G1?

---
## G1 vs ZGC?

**Difficulty:** Hard · **Time:** 2 min

### Short Answer

G1: regional, balanced default. ZGC: sub-ms pauses, colored pointers, large heaps, more CPU/barrier cost.

### Detailed Explanation

Tune with `-Xlog:gc*` and pause P99. Container: `-XX:MaxRAMPercentage`.

### Production Notes

`-XX:+HeapDumpOnOutOfMemoryError` on persistent volume.

### Interview Questions

1. Shenandoah?
2. Humongous objects in G1?

### Follow-up Questions

- Shenandoah?
- Humongous objects in G1?

---
## Can you leak memory with a GC?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Yes — logical leaks keep strong references (static maps, listeners, ThreadLocal, classloader chains).

### Detailed Explanation

OOM types: heap, Metaspace, direct buffer, unable to create native thread.

### Interview Questions

1. See Reference Types
2. ThreadLocal in pools

### Follow-up Questions

- See Reference Types
- ThreadLocal in pools

---
