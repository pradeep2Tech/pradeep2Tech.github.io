---
title: "Channels"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Buffered vs unbuffered, close semantics, range, and fan-in/fan-out."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Channels"
module: 5
moduleTitle: "Concurrency"
sectionRef: "5.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Channels coordinate goroutines — **typed conduits**. Unbuffered = synchronous handoff; buffered = async up to capacity. **Close** signals no more sends; receivers drain then get zero value + `ok=false`.

---

## Reference Tables

| Type | Behavior |
| :--- | :--- |
| `chan T` | Unbuffered — send blocks until recv |
| `chan T` (cap>0) | Buffered — blocks when full |
| Close | `close(ch)` — only sender should close |
| Range | `for v := range ch` until closed |

```go
ch := make(chan int)       // unbuffered
buf := make(chan int, 10)  // buffered

ch <- 1
v := <-ch

close(ch)
v, ok := <-ch // ok false when drained
```

---

## Snippets

```go
// fan-in
func merge(cs ...<-chan int) <-chan int {
    out := make(chan int)
    var wg sync.WaitGroup
    for _, c := range cs {
        wg.Add(1)
        go func(c <-chan int) {
            defer wg.Done()
            for v := range c {
                out <- v
            }
        }(c)
    }
    go func() { wg.Wait(); close(out) }()
    return out
}
```

---

## Internals & Gotchas

- Send on closed channel **panics**.
- Close from non-sender side is a bug.
- `nil` channel blocks forever on send/recv — useful in `select`.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Goroutines](/golang-cheatsheet/goroutines/)
- [Next: Select](/golang-cheatsheet/select/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
