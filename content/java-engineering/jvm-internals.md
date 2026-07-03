---
title: "JVM Internals Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Bytecode pipeline, class loading overview, interpreter vs JIT entry points."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "JVM Internals"
module: 4
moduleTitle: "JVM"
sectionRef: "4.2"
ShowToc: true
interviewHandbook: true
aliases:
  - jvm-internals-quick-ref
---

## Class loading phases?

### Short Answer

Loading → Linking (verify, prepare, resolve) → Initialization (run clinit).

### Detailed Explanation

Loading: define Class. Linking: allocate static fields, resolve symbolic refs. Init: execute static blocks once.

### Follow-up Questions

- See ClassLoader Internals

---
## Interpreter vs JIT?

### Short Answer

Interpreter starts immediately; C1/C2 JIT compiles hot methods to native code.

### Detailed Explanation

Tiered compilation: C1 quick compile, C2 aggressive opts. Deoptimization when assumptions break (megamorphic calls).

### Follow-up Questions

- See JIT & Safepoints page

---
