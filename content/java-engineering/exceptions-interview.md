---
title: "Exceptions Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Checked vs unchecked, try-with-resources, suppression, API design."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Exceptions"
module: 1
moduleTitle: "Language Fundamentals"
sectionRef: "1.5"
ShowToc: true
interviewHandbook: true
aliases:
  - exceptions-quick-ref
---

## Checked vs unchecked exceptions?

### Short Answer

Checked: must declare or catch (`IOException`). Unchecked: `RuntimeException` and errors — programming bugs or unrecoverable.

### Detailed Explanation

Modern API design favors unchecked for most application errors — avoids polluting signatures. Checked useful when caller can recover (retry IO).

### Follow-up Questions

- When wrap checked in unchecked?

---
## try-with-resources — how does it work?

### Short Answer

Auto-closes `AutoCloseable` resources in reverse order; suppresses close exceptions if body threw.

### Detailed Explanation

Compiler desugars to try/finally with null-safe close. Suppressed exceptions attached to primary via `addSuppressed`.

### Follow-up Questions

- What if close() throws?

---
