---
title: "sync Package"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "WaitGroup, Once, Pool, Cond, and Map — coordination primitives."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "sync"
module: 6
moduleTitle: "Synchronization"
sectionRef: "6.3"
ShowToc: true
cheatSheet: true
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

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: RWMutex](/golang-cheatsheet/rwmutex/)
- [Next: Testing](/golang-cheatsheet/testing/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
