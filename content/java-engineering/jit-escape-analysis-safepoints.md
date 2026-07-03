---
title: "JIT, Escape Analysis & Safepoints"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "C1/C2 tiers, stack allocation, safepoint STW operations."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "JIT & Safepoints"
module: 4
moduleTitle: "JVM"
sectionRef: "4.5"
ShowToc: true
interviewHandbook: true
---

## What is escape analysis?

### Short Answer

JIT determines if object escapes method/thread — non-escaping objects may be stack-allocated or scalar-replaced.

### Detailed Explanation

Not guaranteed observable — don't rely on for correctness. Eliminates allocation for short-lived non-escaping objects.

### Follow-up Questions

- Scalar replacement?

---
## What is a safepoint?

### Short Answer

Point where JVM can safely pause all threads for GC, deopt, JVMTI — not every bytecode instruction.

### Detailed Explanation

Long counted loops poll safepoint. STW GC roots scanned at safepoint. Rare infinite loops without poll blocked GC in old bugs.

---
