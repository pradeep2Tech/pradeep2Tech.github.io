---
title: "sync Package"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "WaitGroup, Once, Pool, Cond, and Map — coordination primitives."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "sync"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.7"
weight: 407
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/sync-package/"
---

## At a Glance

- Package **`sync`** provides low-level primitives beyond channels: **WaitGroup**, **Once**, **Pool**, **Cond**, and **Map**.

---

## Reference Tables

| Type | Purpose |
| :--- | :--- |
| `WaitGroup` | Wait for N goroutines |
| `Once` | Run exactly once |
| `Pool` | Reuse temporary objects — GC can clear |
| `Cond` | Wait/signal — needs external lock |
| `Map` | Concurrent map — special cases only |

```go
var once sync.Once
once.Do(func() { initExpensive() })

var wg sync.WaitGroup
wg.Add(n)
// ... wg.Done() per worker
wg.Wait()
```

---

## Snippets

```go
var bufPool = sync.Pool{
    New: func() any { return new(bytes.Buffer) },
}

func getBuf() *bytes.Buffer {
    return bufPool.Get().(*bytes.Buffer)
}
```

---

## Internals & Gotchas

- `WaitGroup` — `Add` before `go`; don't copy after use.
- `Pool` objects may disappear anytime — reset state on Get.
- Prefer channel + mutex over `sync.Map` unless read-heavy stable key set.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

## What are the correct WaitGroup usage rules (Add before go, no copy)?

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
## When should you use sync.Pool and what state must you reset on Get?

### Short Answer
Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for sync.

### Detailed Explanation
Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.

### Internal Working
Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.

### Production Notes
Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.

### Common Mistakes
Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.

### Follow-up Questions
What observable metric or test would prove your design handles this sync concern in production?

---
## When is sync.Map appropriate versus mutex plus map?

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
## What is the fix for WaitGroup misuse that panics with negative counter?

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

## What are the correct WaitGroup usage rules (Add before go, no copy)?

### Short Answer
The senior-level answer is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: What are the correct WaitGroup usage rules (Add before go, no copy).

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: What are the correct WaitGroup usage rules (Add before go, no copy).

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: What are the correct WaitGroup usage rules (Add before go, no copy).

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: What are the correct WaitGroup usage rules (Add before go, no copy).

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: What are the correct WaitGroup usage rules (Add before go, no copy).

### Follow-up Questions
How would you structure shutdown so: What are the correct WaitGroup usage rules (Add before go, no copy) cannot hang the process?

---
## When should you use sync.Pool and what state must you reset on Get?

### Short Answer
In production Go, the decisive factor is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: When should you use sync.Pool and what state must you reset on Get.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: When should you use sync.Pool and what state must you reset on Get.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: When should you use sync.Pool and what state must you reset on Get.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: When should you use sync.Pool and what state must you reset on Get.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: When should you use sync.Pool and what state must you reset on Get.

### Follow-up Questions
How would you structure shutdown so: When should you use sync.Pool and what state must you reset on Get cannot hang the process?

---
## When is sync.Map appropriate versus mutex plus map?

### Short Answer
The architecturally sound response is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: When is sync.Map appropriate versus mutex plus map.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: When is sync.Map appropriate versus mutex plus map.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: When is sync.Map appropriate versus mutex plus map.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: When is sync.Map appropriate versus mutex plus map.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: When is sync.Map appropriate versus mutex plus map.

### Follow-up Questions
How would you structure shutdown so: When is sync.Map appropriate versus mutex plus map cannot hang the process?

---
## What is the fix for WaitGroup misuse that panics with negative counter?

### Short Answer
The senior-level answer is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: What is the fix for WaitGroup misuse that panics with negative counter.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: What is the fix for WaitGroup misuse that panics with negative counter.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: What is the fix for WaitGroup misuse that panics with negative counter.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: What is the fix for WaitGroup misuse that panics with negative counter.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: What is the fix for WaitGroup misuse that panics with negative counter.

### Follow-up Questions
How would you structure shutdown so: What is the fix for WaitGroup misuse that panics with negative counter cannot hang the process?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Rwmutex](/golang-cheatsheet/04-concurrency/rwmutex/)
- [Next: Context](/golang-cheatsheet/04-concurrency/context/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
