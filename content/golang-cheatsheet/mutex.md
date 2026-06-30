---
title: "Mutex"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "sync.Mutex, Lock/Unlock, defer unlock, and common deadlock patterns."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Mutex"
module: 6
moduleTitle: "Synchronization"
sectionRef: "6.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `sync.Mutex` provides **exclusive** lock. Prefer **`defer mu.Unlock()`** immediately after `Lock()`. Protect shared mutable state — not individual reads if `RWMutex` fits.

---

## Reference Tables

| API | Use |
| :--- | :--- |
| `Lock()` / `Unlock()` | Exclusive access |
| `TryLock()` (1.18+) | Non-blocking attempt |
| Copy | Mutex must not be copied after first use |

```go
type SafeMap struct {
    mu sync.Mutex
    m  map[string]int
}

func (s *SafeMap) Inc(key string) {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.m[key]++
}
```

---

## Snippets

```go
var mu sync.Mutex
var balance int

func deposit(amount int) {
    mu.Lock()
    defer mu.Unlock()
    balance += amount
}
```

---

## Internals & Gotchas

- Lock ordering across goroutines → deadlock — establish global order.
- Holding lock during I/O blocks all waiters — copy data and release.
- Don't embed mutex in exported struct if callers might copy struct.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Context](/golang-cheatsheet/context/)
- [Next: RWMutex](/golang-cheatsheet/rwmutex/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
