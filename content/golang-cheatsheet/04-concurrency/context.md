---
title: "Context"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "context.Context, cancellation, deadlines, and passing values."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Context"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.4"
weight: 404
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/context/"
---

## At a Glance

- `context.Context` carries **deadlines**, **cancellation**, and request-scoped values. Pass as **first parameter** `ctx context.Context`. Never store in structs long-term.

---

## Reference Tables

| Constructor | Purpose |
| :--- | :--- |
| `context.Background()` | Root — main, init, tests |
| `context.TODO()` | Placeholder |
| `WithCancel(parent)` | Manual cancel |
| `WithTimeout` / `WithDeadline` | Auto cancel |
| `WithValue` | Request-scoped data — use sparingly |

```go
ctx, cancel := context.WithTimeout(parent, 5*time.Second)
defer cancel()

req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
```

---

## Snippets

```go
func worker(ctx context.Context) error {
    for {
        select {
        case <-ctx.Done():
            return ctx.Err()
        default:
            if err := step(); err != nil {
                return err
            }
        }
    }
}
```

---

## Internals & Gotchas

- Cancel propagates to children — always `defer cancel()`.
- `WithValue` keys should be unexported types to avoid collisions.
- Don't pass `nil` Context — use `context.Background()`.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

## What are the rules for context.Context cancellation propagation?

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
## Why should context be the first function parameter and not stored in structs?

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
## When is context.WithValue appropriate versus anti-pattern?

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
## What error does ctx.Err() return for deadline versus cancel?

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
## How do context deadline exceeded storms appear in logs and metrics?

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

## What are the rules for context.Context cancellation propagation?

### Short Answer
The mechanism-first explanation is context carries cancel/deadline; pass as first param; never store in structs — for: What are the rules for context.Context cancellation propagation.

### Detailed Explanation
Link context trees to HTTP/gRPC shutdown and SIGTERM handling when discussing: What are the rules for context.Context cancellation propagation.

### Internal Working
Cancel propagates to children; deadlines map to timer-driven cancel — mechanism behind: What are the rules for context.Context cancellation propagation.

### Production Notes
Align Shutdown timeout with K8s grace period for: What are the rules for context.Context cancellation propagation.

### Common Mistakes
Using context.Background() in libraries or leaking WithoutCancel scopes breaks: What are the rules for context.Context cancellation propagation.

### Follow-up Questions
What metric proves drain completed before exit for: What are the rules for context.Context cancellation propagation?

---
## Why should context be the first function parameter and not stored in structs?

### Short Answer
The senior-level answer is context carries cancel/deadline; pass as first param; never store in structs — for: Why should context be the first function parameter and not stored in structs.

### Detailed Explanation
Link context trees to HTTP/gRPC shutdown and SIGTERM handling when discussing: Why should context be the first function parameter and not stored in structs.

### Internal Working
Cancel propagates to children; deadlines map to timer-driven cancel — mechanism behind: Why should context be the first function parameter and not stored in structs.

### Production Notes
Align Shutdown timeout with K8s grace period for: Why should context be the first function parameter and not stored in structs.

### Common Mistakes
Using context.Background() in libraries or leaking WithoutCancel scopes breaks: Why should context be the first function parameter and not stored in structs.

### Follow-up Questions
What metric proves drain completed before exit for: Why should context be the first function parameter and not stored in structs?

---
## When is context.WithValue appropriate versus anti-pattern?

### Short Answer
In production Go, the decisive factor is context carries cancel/deadline; pass as first param; never store in structs — for: When is context.WithValue appropriate versus anti-pattern.

### Detailed Explanation
Link context trees to HTTP/gRPC shutdown and SIGTERM handling when discussing: When is context.WithValue appropriate versus anti-pattern.

### Internal Working
Cancel propagates to children; deadlines map to timer-driven cancel — mechanism behind: When is context.WithValue appropriate versus anti-pattern.

### Production Notes
Align Shutdown timeout with K8s grace period for: When is context.WithValue appropriate versus anti-pattern.

### Common Mistakes
Using context.Background() in libraries or leaking WithoutCancel scopes breaks: When is context.WithValue appropriate versus anti-pattern.

### Follow-up Questions
What metric proves drain completed before exit for: When is context.WithValue appropriate versus anti-pattern?

---
## What error does ctx.Err() return for deadline versus cancel?

### Short Answer
The architecturally sound response is context carries cancel/deadline; pass as first param; never store in structs — for: What error does ctx.Err() return for deadline versus cancel.

### Detailed Explanation
Link context trees to HTTP/gRPC shutdown and SIGTERM handling when discussing: What error does ctx.Err() return for deadline versus cancel.

### Internal Working
Cancel propagates to children; deadlines map to timer-driven cancel — mechanism behind: What error does ctx.Err() return for deadline versus cancel.

### Production Notes
Align Shutdown timeout with K8s grace period for: What error does ctx.Err() return for deadline versus cancel.

### Common Mistakes
Using context.Background() in libraries or leaking WithoutCancel scopes breaks: What error does ctx.Err() return for deadline versus cancel.

### Follow-up Questions
What metric proves drain completed before exit for: What error does ctx.Err() return for deadline versus cancel?

---
## How do context deadline exceeded storms appear in logs and metrics?

### Short Answer
In production Go, the decisive factor is context carries cancel/deadline; pass as first param; never store in structs — for: How do context deadline exceeded storms appear in logs and metrics.

### Detailed Explanation
Link context trees to HTTP/gRPC shutdown and SIGTERM handling when discussing: How do context deadline exceeded storms appear in logs and metrics.

### Internal Working
Cancel propagates to children; deadlines map to timer-driven cancel — mechanism behind: How do context deadline exceeded storms appear in logs and metrics.

### Production Notes
Align Shutdown timeout with K8s grace period for: How do context deadline exceeded storms appear in logs and metrics.

### Common Mistakes
Using context.Background() in libraries or leaking WithoutCancel scopes breaks: How do context deadline exceeded storms appear in logs and metrics.

### Follow-up Questions
What metric proves drain completed before exit for: How do context deadline exceeded storms appear in logs and metrics?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Sync Package](/golang-cheatsheet/04-concurrency/sync-package/)
- [Next: Concurrency Patterns](/golang-cheatsheet/04-concurrency/concurrency-patterns/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
