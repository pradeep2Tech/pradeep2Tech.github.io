---
title: "Goroutines"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "go keyword, lifecycle, GOMAXPROCS, and goroutine leaks."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Goroutines"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.1"
weight: 401
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/goroutines/"
---

## At a Glance

- **Goroutines** are lightweight threads scheduled by the Go runtime on OS threads (`GOMAXPROCS`). Start with `go f()`. Always know **how they exit** and how errors propagate.

---

## Reference Tables

For the **GMP scheduler** diagram and preemption detail, see [Scheduler](/golang-cheatsheet/03-go-internals/scheduler/).


| Concept | Detail |
| :--- | :--- |
| Stack | Starts small, grows/shrinks |
| Scheduler | M:N — see [Scheduler](/golang-cheatsheet/03-go-internals/scheduler/) |
| `GOMAXPROCS` | Default `runtime.NumCPU()` |
| Leak | Blocked forever on send/recv |

```go
go func() {
    if err := work(); err != nil {
        log.Printf("work: %v", err)
    }
}()

// wait for completion
var wg sync.WaitGroup
wg.Add(1)
go func() { defer wg.Done(); work() }()
wg.Wait()
```

---

## Snippets

```go
errCh := make(chan error, 1)
go func() {
    errCh <- doWork()
}()
if err := <-errCh; err != nil {
    return err
}
```

---

## Internals & Gotchas

- Main exiting kills all goroutines — see [Graceful Shutdown](/golang-cheatsheet/06-production-go/graceful-shutdown/).
- Panic in goroutine crashes process unless recovered.
- Unbounded `go` spawn → OOM; use worker pools or semaphores.

---

## Production Notes

- Bound goroutine count; always pair spawn with exit/cancel path.

---

## What is the difference between concurrency and parallelism in Go services?

### Short Answer
Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for goroutines.

### Detailed Explanation
Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.

### Internal Working
Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.

### Production Notes
Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.

### Common Mistakes
Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.

### Follow-up Questions
What observable metric or test would prove your design handles this goroutines concern in production?

---
## How can unbounded goroutine creation cause production incidents?

### Short Answer
Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for goroutines.

### Detailed Explanation
Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.

### Internal Working
Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.

### Production Notes
Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.

### Common Mistakes
Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.

### Follow-up Questions
What observable metric or test would prove your design handles this goroutines concern in production?

---
## What happens to child goroutines when main returns without synchronization?

### Short Answer
Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for goroutines.

### Detailed Explanation
Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.

### Internal Working
Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.

### Production Notes
Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.

### Common Mistakes
Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.

### Follow-up Questions
What observable metric or test would prove your design handles this goroutines concern in production?

---
## How should errors from goroutines propagate to the caller?

### Short Answer
Interfaces are implicit (type, data) pairs; typed nil breaks `== nil`. Errors use wrapping with `%w` and `errors.Is/As`.

### Detailed Explanation
An interface value is nil only when both type and data are nil. A nil pointer inside a non-nil interface type is a classic API bug. Error chains preserve cause for inspection.

### Internal Working
Method sets determine satisfaction — pointer vs value receivers matter. Error wrapping builds an unwrap chain inspected by Is/As.

### Production Notes
Keep interfaces small at boundaries. Never log and return the same error. Use sentinel errors sparingly with documented semantics.

### Common Mistakes
Comparing wrapped errors with `==`. Returning typed nil pointers in interfaces. Giant interfaces that hinder testing.

### Follow-up Questions
How would you test `errors.Is` through three layers of `%w` wrapping?

---
## Why does panic in a goroutine crash the whole process unless recovered?

### Short Answer
Profile first (CPU, heap, goroutine); reduce allocations; validate with benchmarks and benchstat.

### Detailed Explanation
Performance work starts with measurement: pprof for hot paths, allocs/op for GC pressure, trace for scheduling delays. Optimize the dominant cost, not assumed bottlenecks.

### Internal Working
CPU profile samples on-CPU stacks. Heap profile shows in-use or allocated objects. Block/mutex profiles expose contention.

### Production Notes
Expose pprof on admin interfaces only. Compare benchmarks across Go versions with benchstat. Set GOMAXPROCS to CPU limit in K8s.

### Common Mistakes
Optimizing cold paths. Disabling GC instead of reducing allocations. Trusting micro-benchmarks without realistic input sizes.

### Follow-up Questions
What regression guard would you add in CI for alloc/op on critical handlers?

---
## How do you detect goroutine leaks in a long-running HTTP service?

### Short Answer
Prefer clear ownership: channels for orchestration, mutex for shared state; always bound concurrency and propagate context.

### Detailed Explanation
Go encourages sharing memory by communicating, but mutexes are often simpler for caches and counters. Combine WaitGroup, context, and buffered channels for backpressure.

### Internal Working
Unbuffered channels synchronize; buffered channels decouple up to capacity. nil channels block forever in select — useful for disabling cases.

### Production Notes
Define goroutine lifecycle: who starts, who stops, how errors return. Implement graceful shutdown with context cancel and server drain.

### Common Mistakes
Leaked goroutines blocked on channels. Closing channels from the receiver side. select+default spin loops.

### Follow-up Questions
When would you choose errgroup with context over a raw WaitGroup?

---
## How do you interpret a panic stack trace with multiple goroutines?

### Short Answer
Production Go services need structured logs, metrics, traces, safe config loading, and graceful shutdown on SIGTERM.

### Detailed Explanation
Operate with correlation IDs across logs and traces. Load config from env with validation at startup. On shutdown, stop accepting, drain in-flight work, then release resources.

### Internal Working
context cancellation propagates to downstream calls. net/http Server.Shutdown uses context timeout. OTel SDK exports spans/metrics to collectors.

### Production Notes
Align shutdown timeout with K8s terminationGracePeriodSeconds. Run govulncheck/staticcheck in CI. Never log secrets.

### Common Mistakes
Ignoring SIGTERM until kill. Storing context in structs. Missing health vs readiness separation.

### Follow-up Questions
How do you verify graceful shutdown under load in a staging environment?

---
## How do you validate a fix for a goroutine leak with load testing?

### Short Answer
Prefer clear ownership: channels for orchestration, mutex for shared state; always bound concurrency and propagate context.

### Detailed Explanation
Go encourages sharing memory by communicating, but mutexes are often simpler for caches and counters. Combine WaitGroup, context, and buffered channels for backpressure.

### Internal Working
Unbuffered channels synchronize; buffered channels decouple up to capacity. nil channels block forever in select — useful for disabling cases.

### Production Notes
Define goroutine lifecycle: who starts, who stops, how errors return. Implement graceful shutdown with context cancel and server drain.

### Common Mistakes
Leaked goroutines blocked on channels. Closing channels from the receiver side. select+default spin loops.

### Follow-up Questions
When would you choose errgroup with context over a raw WaitGroup?

---
<!-- interview-answers:end -->

---

## What is the difference between concurrency and parallelism in Go services?

### Short Answer
The senior-level answer is tying language rules to runtime and production observability — for: What is the difference between concurrency and parallelism in Go services.

### Detailed Explanation
Senior answers combine mechanism, tradeoffs, and verification for: What is the difference between concurrency and parallelism in Go services.

### Internal Working
Go couples compile-time types with runtime scheduler/GC behavior — anchor: What is the difference between concurrency and parallelism in Go services.

### Production Notes
Prove it under load with trace plus metrics, not micro-benchmarks alone on any change suggested by: What is the difference between concurrency and parallelism in Go services.

### Common Mistakes
Hand-waving without profiles, tests, or happens-before reasoning fails: What is the difference between concurrency and parallelism in Go services.

### Follow-up Questions
What evidence would convince you your answer to: What is the difference between concurrency and parallelism in Go services holds at scale?

---
## How can unbounded goroutine creation cause production incidents?

### Short Answer
In production Go, the decisive factor is tying language rules to runtime and production observability — for: How can unbounded goroutine creation cause production incidents.

### Detailed Explanation
Senior answers combine mechanism, tradeoffs, and verification for: How can unbounded goroutine creation cause production incidents.

### Internal Working
Go couples compile-time types with runtime scheduler/GC behavior — anchor: How can unbounded goroutine creation cause production incidents.

### Production Notes
Document the tradeoff in an ADR with rollback criteria on any change suggested by: How can unbounded goroutine creation cause production incidents.

### Common Mistakes
Hand-waving without profiles, tests, or happens-before reasoning fails: How can unbounded goroutine creation cause production incidents.

### Follow-up Questions
What evidence would convince you your answer to: How can unbounded goroutine creation cause production incidents holds at scale?

---
## What happens to child goroutines when main returns without synchronization?

### Short Answer
The architecturally sound response is tying language rules to runtime and production observability — for: What happens to child goroutines when main returns without synchronization.

### Detailed Explanation
Senior answers combine mechanism, tradeoffs, and verification for: What happens to child goroutines when main returns without synchronization.

### Internal Working
Go couples compile-time types with runtime scheduler/GC behavior — anchor: What happens to child goroutines when main returns without synchronization.

### Production Notes
Gate the change on alloc/op and p99 regression checks on any change suggested by: What happens to child goroutines when main returns without synchronization.

### Common Mistakes
Hand-waving without profiles, tests, or happens-before reasoning fails: What happens to child goroutines when main returns without synchronization.

### Follow-up Questions
What evidence would convince you your answer to: What happens to child goroutines when main returns without synchronization holds at scale?

---
## How should errors from goroutines propagate to the caller?

### Short Answer
The mechanism-first explanation is errors are values; wrap with `%w`; inspect with Is/As — for: How should errors from goroutines propagate to the caller.

### Detailed Explanation
Distinguish sentinel vs typed errors; log OR return, not both, when covering: How should errors from goroutines propagate to the caller.

### Internal Working
Wrap chains preserve unwrap for Is/As; `%v` breaks inspection — mechanism for: How should errors from goroutines propagate to the caller.

### Production Notes
Map errors to HTTP/gRPC codes at boundaries for: How should errors from goroutines propagate to the caller.

### Common Mistakes
Comparing wrapped errors with `==` or duplicating logs fails: How should errors from goroutines propagate to the caller.

### Follow-up Questions
What retry taxonomy would you attach to errors in: How should errors from goroutines propagate to the caller?

---
## Why does panic in a goroutine crash the whole process unless recovered?

### Short Answer
The senior-level answer is triage with pprof goroutine/heap, traces, logs, and race detector — for: Why does panic in a goroutine crash the whole process unless recovered.

### Detailed Explanation
Isolate symptom (leak, deadlock, OOM, latency) before config churn for: Why does panic in a goroutine crash the whole process unless recovered.

### Internal Working
Stack labels show blocked chan/mutex/select; GC thrash shows in gctrace — signals for: Why does panic in a goroutine crash the whole process unless recovered.

### Production Notes
Reproduce under load; capture profiles at peak for: Why does panic in a goroutine crash the whole process unless recovered.

### Common Mistakes
Shotgun GOMAXPROCS/GC toggles without evidence worsens: Why does panic in a goroutine crash the whole process unless recovered.

### Follow-up Questions
What is your first reversible mitigation in the first 30 minutes for: Why does panic in a goroutine crash the whole process unless recovered?

---
## How do you detect goroutine leaks in a long-running HTTP service?

### Short Answer
The senior-level answer is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: How do you detect goroutine leaks in a long-running HTTP service.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: How do you detect goroutine leaks in a long-running HTTP service.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: How do you detect goroutine leaks in a long-running HTTP service.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: How do you detect goroutine leaks in a long-running HTTP service.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: How do you detect goroutine leaks in a long-running HTTP service.

### Follow-up Questions
How would you structure shutdown so: How do you detect goroutine leaks in a long-running HTTP service cannot hang the process?

---
## How do you interpret a panic stack trace with multiple goroutines?

### Short Answer
The mechanism-first explanation is structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: How do you interpret a panic stack trace with multiple goroutines.

### Detailed Explanation
Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: How do you interpret a panic stack trace with multiple goroutines.

### Internal Working
OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: How do you interpret a panic stack trace with multiple goroutines.

### Production Notes
Run staticcheck/govulncheck; protect pprof admin ports for: How do you interpret a panic stack trace with multiple goroutines.

### Common Mistakes
Missing readiness vs liveness or logging secrets breaks production answers to: How do you interpret a panic stack trace with multiple goroutines.

### Follow-up Questions
What alert would fire first if: How do you interpret a panic stack trace with multiple goroutines regresses in prod?

---
## How do you validate a fix for a goroutine leak with load testing?

### Short Answer
The mechanism-first explanation is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: How do you validate a fix for a goroutine leak with load testing.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: How do you validate a fix for a goroutine leak with load testing.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: How do you validate a fix for a goroutine leak with load testing.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: How do you validate a fix for a goroutine leak with load testing.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: How do you validate a fix for a goroutine leak with load testing.

### Follow-up Questions
How would you structure shutdown so: How do you validate a fix for a goroutine leak with load testing cannot hang the process?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Reflection](/golang-cheatsheet/03-go-internals/reflection/)
- [Next: Channels](/golang-cheatsheet/04-concurrency/channels/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
