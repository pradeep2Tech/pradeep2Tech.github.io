---
title: "Streams & Collectors Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Lazy pipelines, collectors, lambdas, Optional, and parallel stream pitfalls."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Streams"
module: 1
moduleTitle: "Language Fundamentals"
sectionRef: "1.7"
ShowToc: true
interviewHandbook: true
aliases:
  - streams-quick-ref
  - stream-operations-interview
  - functional-java-ref
---

## Why are streams lazy?

### Short Answer

Intermediate ops fuse; execution deferred until terminal op — enables short-circuit and optimization.

### Detailed Explanation

Pipeline builds operator chain (sink wrapping). Single terminal op triggers traversal. Short-circuit ops (`findFirst`, `anyMatch`, `limit`) stop early.

### Internal Working

Spliterator characteristics (`SIZED`, `ORDERED`, `DISTINCT`) enable optimizations.

### Production Notes

Don't reuse a Stream after terminal operation.

### Follow-up Questions

- What is a Spliterator?
- Difference reduce vs collect?

---
## When to use parallel streams?

### Short Answer

Large in-memory CPU-bound work, associative ops, no shared mutation, good spliterator splitting.

### Detailed Explanation

Uses `ForkJoinPool.commonPool()`. Bad for IO, small collections (<10k), or ordered pipelines where order matters. Side effects in `forEach` need thread-safe collections.

### Internal Working

Default parallelism = CPUs - 1.

### Production Notes

Parallelizing by default in services.

### Follow-up Questions

- What makes a combiner associative?
- Common pool starvation risk?

---
## Collectors.toMap duplicate key pitfall?

### Short Answer

Without merge function, duplicate keys throw `IllegalStateException`.

### Detailed Explanation

Use `toMap(keyFn, valFn, mergeFn)` or `groupingBy`. Java 16+ prefer `toList()` over `collect(toList())`.

---
## Optional in API design — good or bad?

### Short Answer

Good as return type signaling absence; bad as field, parameter, or collection element.

### Detailed Explanation

Optional not serializable by default; JSON mapping awkward. Use overloads for optional params. Never `optional.get()` without check.

### Follow-up Questions

- Effectively final in lambdas — why?

---
