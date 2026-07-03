---
title: "CAS & Lock-Free Programming"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Compare-and-swap, ABA problem, AtomicReference, LongAdder vs AtomicLong."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "CAS"
module: 3
moduleTitle: "Concurrency"
sectionRef: "3.4"
ShowToc: true
interviewHandbook: true
---

## What is CAS?

### Short Answer

Compare-And-Swap: atomically update if current value equals expected — hardware primitive (cmpxchg).

### Detailed Explanation

Basis of `AtomicInteger.incrementAndGet`, CHM bin updates. Lock-free algorithms retry on contention instead of blocking.

### Internal Working

On x86, CAS maps to LOCK CMPXCHG.

### Follow-up Questions

- CAS vs lock — when prefer each?

---
## ABA problem?

### Short Answer

Value changes A→B→A; CAS sees expected A and succeeds though state changed in between.

### Detailed Explanation

Problem in lock-free stacks/queues with recycling. Fix: versioned references (`AtomicStampedReference`, `AtomicMarkableReference`) or hazard pointers / epoch-based reclamation.

### Follow-up Questions

- Where does ABA matter in Java APIs?

---
## LongAdder vs AtomicLong?

### Short Answer

LongAdder stripes counters across cells — lower contention under many writers; AtomicLong single value.

### Detailed Explanation

LongAdder: `add` spreads across cells, `sum` aggregates. Better for high-throughput metrics. AtomicLong when you need consistent reads of exact current value or CAS on single counter.

### Production Notes

Use LongAdder for request counters; AtomicLong for sequence IDs.

---
