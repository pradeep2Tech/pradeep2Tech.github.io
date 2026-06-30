---
title: "RWMutex"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "sync.RWMutex — concurrent reads, exclusive writes, and upgrade rules."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "RWMutex"
module: 6
moduleTitle: "Synchronization"
sectionRef: "6.2"
ShowToc: true
cheatSheet: true
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

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Mutex](/golang-cheatsheet/mutex/)
- [Next: sync](/golang-cheatsheet/sync-package/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
