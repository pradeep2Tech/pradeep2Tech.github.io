---
title: "RWMutex"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "sync.RWMutex — concurrent reads, exclusive writes, and upgrade rules."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "RWMutex"
module: 4
moduleTitle: "Concurrency"
sectionRef: "4.6"
weight: 406
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/rwmutex/"
---

## At a Glance

- `sync.RWMutex` allows **many readers** OR **one writer**. Better read-heavy caches; writers still exclude everyone.

---

## Reference Tables

| Method | Access |
| :--- | :--- |
| `RLock` / `RUnlock` | Shared read |
| `Lock` / `Unlock` | Exclusive write |
| Rule | No `RLock` while holding `Lock` upgrade |

```go
type Cache struct {
    mu sync.RWMutex
    data map[string]string
}

func (c *Cache) Get(k string) (string, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    v, ok := c.data[k]
    return v, ok
}
```

---

## Snippets

```go
func (c *Cache) Set(k, v string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.data[k] = v
}
```

---

## Internals & Gotchas

- Writer starvation possible under constant readers — rare but know it.
- `RWMutex` is heavier than `Mutex` for write-heavy workloads.
- Same no-copy rule as `Mutex`.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

## When does sync.RWMutex outperform Mutex and when is it slower?

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
## What is writer starvation in RWMutex and is it a practical concern?

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

## When does sync.RWMutex outperform Mutex and when is it slower?

### Short Answer
The architecturally sound response is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: When does sync.RWMutex outperform Mutex and when is it slower.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: When does sync.RWMutex outperform Mutex and when is it slower.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: When does sync.RWMutex outperform Mutex and when is it slower.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: When does sync.RWMutex outperform Mutex and when is it slower.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: When does sync.RWMutex outperform Mutex and when is it slower.

### Follow-up Questions
How would you structure shutdown so: When does sync.RWMutex outperform Mutex and when is it slower cannot hang the process?

---
## What is writer starvation in RWMutex and is it a practical concern?

### Short Answer
The mechanism-first explanation is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: What is writer starvation in RWMutex and is it a practical concern.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: What is writer starvation in RWMutex and is it a practical concern.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: What is writer starvation in RWMutex and is it a practical concern.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: What is writer starvation in RWMutex and is it a practical concern.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: What is writer starvation in RWMutex and is it a practical concern.

### Follow-up Questions
How would you structure shutdown so: What is writer starvation in RWMutex and is it a practical concern cannot hang the process?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Mutex](/golang-cheatsheet/04-concurrency/mutex/)
- [Next: Sync Package](/golang-cheatsheet/04-concurrency/sync-package/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
