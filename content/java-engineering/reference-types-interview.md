---
title: "Reference Types Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Soft, weak, phantom references and Cleaner."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "References"
module: 4
moduleTitle: "JVM"
sectionRef: "4.6"
ShowToc: true
interviewHandbook: true
---

## Soft vs weak vs phantom?

### Short Answer

Soft: cleared before OOM — memory-sensitive cache. Weak: next GC — canonical mappings. Phantom: after finalize/enqueue — post-mortem cleanup.

### Detailed Explanation

ReferenceQueue notifies when referent cleared. Prefer `Cleaner` over finalization (deprecated).

### Follow-up Questions

- WeakHashMap behavior?
- PhantomReference use case?

---
