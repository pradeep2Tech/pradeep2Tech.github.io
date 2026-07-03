---
title: "Performance Optimization"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Allocation reduction, object reuse, memory optimization, and efficient concurrency."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Optimization"
module: 5
moduleTitle: "Performance"
sectionRef: "5.1"
weight: 501
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- Reduce allocations in hot paths.
- Reuse buffers with `sync.Pool` — see [sync Package](/golang-cheatsheet/04-concurrency/sync-package/).
- Bound goroutine count.

## Core Concepts

| Tactic | When |
| :--- | :--- |
| Preallocate slices | Known upper bound on size |
| sync.Pool | Short-lived, resettable objects |
| Value semantics | Small immutable structs |
| String builder | Concatenation in loops |

## Performance Considerations

Profile before optimizing — [Profiling](/golang-cheatsheet/05-performance/profiling/).

## Core Concepts

| Tactic | Mechanism |
| :--- | :--- |
| Preallocate slices | Fewer grow copies |
| sync.Pool | Reuse transient buffers |
| strings.Builder | Avoid N² string concat |
| Pass `[]byte` | Reduce string conversions |
| Value receivers | Fewer heap objects |
| Bounded workers | Stable goroutine count |

## Design Tradeoffs

| sync.Pool | Custom free list |
| :--- | :--- |
| GC may clear pool anytime | Predictable reuse |
| Low boilerplate | Must size and audit manually |

## Checklists

- [ ] Baseline benchmark with `-benchmem`
- [ ] CPU + allocs profile before change
- [ ] benchstat compare after change


---

## List three allocation-reduction tactics for hot HTTP handlers.

### Short Answer
The senior-level answer is profile first (CPU, heap, goroutine), then reduce allocs and contention — for: List three allocation-reduction tactics for hot HTTP handlers..

### Detailed Explanation
Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: List three allocation-reduction tactics for hot HTTP handlers..

### Internal Working
Flat vs cum in pprof; allocs/op drives GC — internal tools for: List three allocation-reduction tactics for hot HTTP handlers..

### Production Notes
Prove it under load with trace plus metrics, not micro-benchmarks alone on changes affecting: List three allocation-reduction tactics for hot HTTP handlers..

### Common Mistakes
Optimizing cold paths or micro-benchmarking without realistic inputs misleads: List three allocation-reduction tactics for hot HTTP handlers..

### Follow-up Questions
Which single profile view would you open first for: List three allocation-reduction tactics for hot HTTP handlers.?

---
## When is sync.Pool the wrong tool for object reuse?

### Short Answer
In production Go, the decisive factor is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: When is sync.Pool the wrong tool for object reuse.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: When is sync.Pool the wrong tool for object reuse.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: When is sync.Pool the wrong tool for object reuse.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: When is sync.Pool the wrong tool for object reuse.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: When is sync.Pool the wrong tool for object reuse.

### Follow-up Questions
How would you structure shutdown so: When is sync.Pool the wrong tool for object reuse cannot hang the process?

---
## How do string conversions from []byte cause allocations and how to avoid?

### Short Answer
In production Go, the decisive factor is profile first (CPU, heap, goroutine), then reduce allocs and contention — for: How do string conversions from []byte cause allocations and how to avoid.

### Detailed Explanation
Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: How do string conversions from []byte cause allocations and how to avoid.

### Internal Working
Flat vs cum in pprof; allocs/op drives GC — internal tools for: How do string conversions from []byte cause allocations and how to avoid.

### Production Notes
Document the tradeoff in an ADR with rollback criteria on changes affecting: How do string conversions from []byte cause allocations and how to avoid.

### Common Mistakes
Optimizing cold paths or micro-benchmarking without realistic inputs misleads: How do string conversions from []byte cause allocations and how to avoid.

### Follow-up Questions
Which single profile view would you open first for: How do string conversions from []byte cause allocations and how to avoid?

---
## What is the cost of defer in tight loops — myth versus reality?

### Short Answer
The architecturally sound response is profile first (CPU, heap, goroutine), then reduce allocs and contention — for: What is the cost of defer in tight loops — myth versus reality.

### Detailed Explanation
Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: What is the cost of defer in tight loops — myth versus reality.

### Internal Working
Flat vs cum in pprof; allocs/op drives GC — internal tools for: What is the cost of defer in tight loops — myth versus reality.

### Production Notes
Gate the change on alloc/op and p99 regression checks on changes affecting: What is the cost of defer in tight loops — myth versus reality.

### Common Mistakes
Optimizing cold paths or micro-benchmarking without realistic inputs misleads: What is the cost of defer in tight loops — myth versus reality.

### Follow-up Questions
Which single profile view would you open first for: What is the cost of defer in tight loops — myth versus reality?

---
## What is the impact of excessive interface boxing on allocations?

### Short Answer
The senior-level answer is interfaces are implicit (type,data) pairs; typed nil breaks `== nil` — for: What is the impact of excessive interface boxing on allocations.

### Detailed Explanation
Tie method sets (value vs pointer receivers) to satisfaction and API design for: What is the impact of excessive interface boxing on allocations.

### Internal Working
Small interfaces at boundaries; empty interface boxes values and may allocate — internal angle on: What is the impact of excessive interface boxing on allocations.

### Production Notes
Use compile-time `var _ IF = (*T)(nil)` checks; test JSON nil edge cases for: What is the impact of excessive interface boxing on allocations.

### Common Mistakes
Returning typed nil pointers in interface-typed APIs is a classic bug in: What is the impact of excessive interface boxing on allocations.

### Follow-up Questions
How would you refactor a fat interface exposed by: What is the impact of excessive interface boxing on allocations?

---
## What strategies reduce lock contention in read-heavy caches?

### Short Answer
The architecturally sound response is tying language rules to runtime and production observability — for: What strategies reduce lock contention in read-heavy caches.

### Detailed Explanation
Senior answers combine mechanism, tradeoffs, and verification for: What strategies reduce lock contention in read-heavy caches.

### Internal Working
Go couples compile-time types with runtime scheduler/GC behavior — anchor: What strategies reduce lock contention in read-heavy caches.

### Production Notes
Gate the change on alloc/op and p99 regression checks on any change suggested by: What strategies reduce lock contention in read-heavy caches.

### Common Mistakes
Hand-waving without profiles, tests, or happens-before reasoning fails: What strategies reduce lock contention in read-heavy caches.

### Follow-up Questions
What evidence would convince you your answer to: What strategies reduce lock contention in read-heavy caches holds at scale?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Concurrency Patterns](/golang-cheatsheet/04-concurrency/concurrency-patterns/)
- [Next: Profiling](/golang-cheatsheet/05-performance/profiling/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
