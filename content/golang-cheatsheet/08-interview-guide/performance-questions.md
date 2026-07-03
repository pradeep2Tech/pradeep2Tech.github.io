---
title: "Performance Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Go performance and profiling interview questions."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Performance Q"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.4"
weight: 804
ShowToc: true
interviewHandbook: true
---

Questions only — no answers.

# Performance Questions

1. How do you capture a CPU profile from a production process safely?
2. What does a flat versus cum column mean in pprof CPU output?
3. How do you distinguish alloc_objects from inuse_space in heap profiles?
4. When would you use goroutine profile versus trace?
5. How does runtime/trace help diagnose scheduler latency?
6. What is benchstat and how do you compare two benchmark runs?
7. Why use b.ReportAllocs() and what does allocs/op indicate?
8. How do you reduce benchmark noise on shared CI runners?
9. What mistakes make micro-benchmarks misleading for production?
10. List three allocation-reduction tactics for hot HTTP handlers.
11. When is sync.Pool the wrong tool for object reuse?
12. How does preallocating slices with make([]T, 0, n) reduce GC pressure?
13. How can struct field ordering affect memory padding and cache lines?
14. When should you prefer value semantics over pointers for small structs?
15. How do string conversions from []byte cause allocations and how to avoid?
16. What is the cost of defer in tight loops — myth versus reality?
17. How do you profile mutex contention with block profile?
18. What GOMAXPROCS setting is appropriate for container CPU limits?
19. How would you tune GOGC for a latency-sensitive versus batch workload?
20. When is forcing runtime.GC() ever justified in production?
21. How do you find allocation hotspots from pprof allocs profile?
22. What is the impact of excessive interface boxing on allocations?
23. How do you benchmark concurrent code without data races?
24. What strategies reduce lock contention in read-heavy caches?
25. How do you triage a sudden spike in goroutine count from /debug/pprof/goroutine?
