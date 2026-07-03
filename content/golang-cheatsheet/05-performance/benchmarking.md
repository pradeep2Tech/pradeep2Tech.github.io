---
title: "Benchmarking"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "testing.B, benchmem, benchstat, and benchmark methodology."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Benchmarking"
module: 5
moduleTitle: "Performance"
sectionRef: "5.3"
weight: 503
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- `func BenchmarkX(b *testing.B)` in `*_test.go`
- `b.ReportAllocs()` for allocs/op
- `benchstat old.txt new.txt` for comparison

## Common Mistakes

- Benchmarking debug builds.
- Not resetting timer after setup (`b.ResetTimer()`).

## Internal Working

```go
func BenchmarkFoo(b *testing.B) {
    b.ReportAllocs()
    data := setup()
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        Foo(data)
    }
}
```

```bash
go test -bench=. -benchmem -count=10 ./... > old.txt
# after change
go test -bench=. -benchmem -count=10 ./... > new.txt
benchstat old.txt new.txt
```

## Common Mistakes

- Benchmarking with `-race` (slow, different behavior).
- Not calling `ResetTimer` after expensive setup.


---

## What is benchstat and how do you compare two benchmark runs?

### Short Answer
The senior-level answer is profile first (CPU, heap, goroutine), then reduce allocs and contention — for: What is benchstat and how do you compare two benchmark runs.

### Detailed Explanation
Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: What is benchstat and how do you compare two benchmark runs.

### Internal Working
Flat vs cum in pprof; allocs/op drives GC — internal tools for: What is benchstat and how do you compare two benchmark runs.

### Production Notes
Prove it under load with trace plus metrics, not micro-benchmarks alone on changes affecting: What is benchstat and how do you compare two benchmark runs.

### Common Mistakes
Optimizing cold paths or micro-benchmarking without realistic inputs misleads: What is benchstat and how do you compare two benchmark runs.

### Follow-up Questions
Which single profile view would you open first for: What is benchstat and how do you compare two benchmark runs?

---
## Why use b.ReportAllocs() and what does allocs/op indicate?

### Short Answer
In production Go, the decisive factor is profile first (CPU, heap, goroutine), then reduce allocs and contention — for: Why use b.ReportAllocs() and what does allocs/op indicate.

### Detailed Explanation
Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: Why use b.ReportAllocs() and what does allocs/op indicate.

### Internal Working
Flat vs cum in pprof; allocs/op drives GC — internal tools for: Why use b.ReportAllocs() and what does allocs/op indicate.

### Production Notes
Document the tradeoff in an ADR with rollback criteria on changes affecting: Why use b.ReportAllocs() and what does allocs/op indicate.

### Common Mistakes
Optimizing cold paths or micro-benchmarking without realistic inputs misleads: Why use b.ReportAllocs() and what does allocs/op indicate.

### Follow-up Questions
Which single profile view would you open first for: Why use b.ReportAllocs() and what does allocs/op indicate?

---
## How do you reduce benchmark noise on shared CI runners?

### Short Answer
The architecturally sound response is profile first (CPU, heap, goroutine), then reduce allocs and contention — for: How do you reduce benchmark noise on shared CI runners.

### Detailed Explanation
Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: How do you reduce benchmark noise on shared CI runners.

### Internal Working
Flat vs cum in pprof; allocs/op drives GC — internal tools for: How do you reduce benchmark noise on shared CI runners.

### Production Notes
Gate the change on alloc/op and p99 regression checks on changes affecting: How do you reduce benchmark noise on shared CI runners.

### Common Mistakes
Optimizing cold paths or micro-benchmarking without realistic inputs misleads: How do you reduce benchmark noise on shared CI runners.

### Follow-up Questions
Which single profile view would you open first for: How do you reduce benchmark noise on shared CI runners?

---
## What mistakes make micro-benchmarks misleading for production?

### Short Answer
The mechanism-first explanation is profile first (CPU, heap, goroutine), then reduce allocs and contention — for: What mistakes make micro-benchmarks misleading for production.

### Detailed Explanation
Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: What mistakes make micro-benchmarks misleading for production.

### Internal Working
Flat vs cum in pprof; allocs/op drives GC — internal tools for: What mistakes make micro-benchmarks misleading for production.

### Production Notes
Validate with pprof, benchmarks, and race-detector coverage on changes affecting: What mistakes make micro-benchmarks misleading for production.

### Common Mistakes
Optimizing cold paths or micro-benchmarking without realistic inputs misleads: What mistakes make micro-benchmarks misleading for production.

### Follow-up Questions
Which single profile view would you open first for: What mistakes make micro-benchmarks misleading for production?

---
## How do you benchmark concurrent code without data races?

### Short Answer
In production Go, the decisive factor is happens-before edges from channels, mutex, Once, and atomic — data races are UB — for: How do you benchmark concurrent code without data races.

### Detailed Explanation
List synchronization sources and why racy code can 'work' yet remain invalid when answering: How do you benchmark concurrent code without data races.

### Internal Working
Without a happens-before edge, reads/writes have no guaranteed visibility across goroutines — core to: How do you benchmark concurrent code without data races.

### Production Notes
Run `go test -race` in CI for packages touched by: How do you benchmark concurrent code without data races.

### Common Mistakes
Using atomics for multi-field invariants or skipping race tests on 'simple' counters fails: How do you benchmark concurrent code without data races.

### Follow-up Questions
Show the minimal sync fix (mutex vs channel) you would accept in review for: How do you benchmark concurrent code without data races.

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Profiling](/golang-cheatsheet/05-performance/profiling/)
- [Next: Memory Optimization](/golang-cheatsheet/05-performance/memory-optimization/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
