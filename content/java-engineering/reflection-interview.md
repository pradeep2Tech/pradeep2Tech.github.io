---
title: "Reflection Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Runtime inspection, annotation retention, modules, performance."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Reflection"
module: 5
moduleTitle: "Platform APIs"
sectionRef: "5.1"
interviewHandbook: true
aliases:
  - reflection-annotations-ref
---

## Annotation retention SOURCE vs CLASS vs RUNTIME?

**Difficulty:** Easy · **Time:** 30 sec

### Short Answer

SOURCE: compile-only. CLASS: bytecode, not runtime reflection. RUNTIME: visible via reflection.

### Detailed Explanation

Framework annotations (JPA, Spring) need RUNTIME. `@Override` is SOURCE.

### Interview Questions

1. Module opens for deep reflection?

### Follow-up Questions

- Module opens for deep reflection?

---
## Reflection cost and mitigation?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

Method lookup expensive — cache MethodHandle, use compile-time annotation processing, Spring AOT.

### Detailed Explanation

Modules (9+): `opens` package for frameworks. Prefer build-time indexing over classpath scanning.

---
