---
title: "Architect-Level Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Curated architect-level Go interview questions."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Architect"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.2"
weight: 802
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/).

# Architect-Level Questions

1. What are the main components of the Go runtime and how do they interact at process startup?
2. How does the Go linker differ from a traditional dynamic linker in terms of deployment artifacts?
3. How did goroutine preemption change from Go 1.13 to Go 1.14+ and why does it matter?
4. What is the netpoller and how does it integrate with channel and network I/O blocking?
5. What are STW phases in Go GC and how have pause times trended over releases?
6. What is a write barrier in Go's GC and when does it apply?
7. How does the Go compiler represent interface values internally (type, data)?
8. What is the size cost of an interface{} holding a small value versus a pointer?
9. How do pipelines compose channels and where does backpressure belong?
10. What is the share-memory-by-communicating idiom and its limits?
11. How does runtime/trace help diagnose scheduler latency?
12. How can struct field ordering affect memory padding and cache lines?
13. What GOMAXPROCS setting is appropriate for container CPU limits?
14. How would you tune GOGC for a latency-sensitive versus batch workload?
15. What runbook steps apply when OOMKilled in Kubernetes for a Go pod?
16. What causes select fair starvation and how do you reproduce it?
17. What is your first-hour checklist for a Go service latency regression after deploy?
18. How do you configure RED versus USE metrics for Go microservices?
19. How long should Shutdown context timeout be relative to pod terminationGracePeriodSeconds?
20. What alerting rules catch goroutine leaks before OOM?
21. How does Minimal Version Selection resolve conflicting module requirements?
22. How would you design error types for a multi-tenant API with retry hints?
23. What is the difference between comparable and copyable types in Go generics constraints?
