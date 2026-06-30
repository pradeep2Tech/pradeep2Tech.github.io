---
title: "Functions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Signatures, multiple returns, variadic params, closures, and named results."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Functions"
module: 1
moduleTitle: "Language Basics"
sectionRef: "1.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Functions are first-class values. Go supports **multiple return values** (idiomatic for `result, err`), **variadic** parameters, **named results**, and **closures** that capture variables by reference.

---

## Reference Tables

| Feature | Notes |
| :--- | :--- |
| Signature | `func name(params) (results)` |
| Multiple returns | `(T, error)` is standard |
| Named results | `func f() (n int, err error)` — naked return |
| Variadic | `func sum(nums ...int)` |
| Closures | Capture outer variables; watch loop variable capture (Go 1.22+ fixed per-iteration) |
| Methods | See [Methods](/golang-cheatsheet/methods/) |

| Pattern | Example |
| :--- | :--- |
| Error return | `return nil, fmt.Errorf("...")` |
| Defer recover | `defer func() { if r := recover(); r != nil { } }()` |
| Function type | `type Handler func(http.ResponseWriter, *http.Request)` |
| Anonymous | `go func() { }()` |

---

## Snippets

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// variadic
func logf(format string, args ...any) {
    fmt.Printf(format+"
", args...)
}

// closure factory
func counter() func() int {
    n := 0
    return func() int {
        n++
        return n
    }
}
```

---

## Internals & Gotchas

- Named return values can be confusing in long functions — prefer explicit `return x, err`.
- `recover()` only works inside deferred functions in the **same goroutine**.
- Passing functions to goroutines: capture loop vars explicitly in Go < 1.22.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Language Basics](/golang-cheatsheet/language-basics/)
- [Next: Structs](/golang-cheatsheet/structs/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
