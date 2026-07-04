---
title: "Troubleshooting Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Production troubleshooting interview questions for Go."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Troubleshooting Q"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.3"
weight: 803
interviewHandbook: true
---

Questions only — no answers.

# Troubleshooting Questions

1. What stack patterns indicate a goroutine blocked on channel receive forever?
2. How do you debug a deadlock involving sync.Mutex lock ordering?
3. What does go test -race output tell you and what are false-positive pitfalls?
4. How do you interpret a panic stack trace with multiple goroutines?
5. What causes 'fatal error: all goroutines are asleep - deadlock!'?
6. How do you diagnose memory leaks that are actually slice backing-array retention?
7. What symptoms distinguish GC thrashing from CPU-bound slowness?
8. How do you find which HTTP handler allocates the most per request?
9. What runbook steps apply when OOMKilled in Kubernetes for a Go pod?
10. How do context deadline exceeded storms appear in logs and metrics?
11. What causes select fair starvation and how do you reproduce it?
12. How do you debug a production issue only reproducible under -race?
13. What is the fix for WaitGroup misuse that panics with negative counter?
14. How do you trace a request ID through logs when middleware order is wrong?
15. What indicates interface nil comparison bugs in JSON API responses?
16. How do you validate a fix for a goroutine leak with load testing?
17. What pprof signs suggest mutex contention as the bottleneck?
18. How do map concurrent write panics manifest and what is the permanent fix?
19. What is your first-hour checklist for a Go service latency regression after deploy?
20. What fields belong in structured production logs for a REST API?
