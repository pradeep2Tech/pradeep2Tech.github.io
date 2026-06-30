---
title: "Memory Model"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Happens-before, visibility, atomics, and data races in Go."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Memory Model"
module: 8
moduleTitle: "Runtime"
sectionRef: "8.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Go's **memory model** defines when reads/writes are visible across goroutines via **happens-before** edges. Data races are undefined behavior — use sync or channels.

---

## Reference Tables

| Happens-before from | Examples |
| :--- | :--- |
| Channel ops | Send happens-before receive completes |
| `sync` primitives | Unlock happens-before next Lock |
| `Once` | `Do` completion before return |
| `atomic` | Atomic ops provide synchronization |

```go
// DATA RACE — undefined
var x int
go func() { x++ }()
x++

// FIX
var mu sync.Mutex
go func() { mu.Lock(); x++; mu.Unlock() }()
```

---

## Snippets

```go
import "sync/atomic"

var count atomic.Int64
count.Add(1)
```

---

## Internals & Gotchas

- `go test -race` catches races — run in CI.
- `volatile` doesn't exist — use `atomic` or mutex.
- Compiler/CPU reordering invisible within single goroutine sequential consistency.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Reflection](/golang-cheatsheet/reflection/)
- [Next: GC](/golang-cheatsheet/garbage-collection/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
