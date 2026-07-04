---
title: "Functions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Signatures, multiple returns, variadic params, closures, and named results."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Functions"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.2"
weight: 112
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/functions/"
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
| Methods | See [Methods](/golang-cheatsheet/01-fundamentals/methods/) |

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
    fmt.Printf(format+"\n", args...)
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

- Apply patterns from this page in code review and incident postmortems.

---

## What changed in Go 1.22 loop variable capture semantics?

### Short Answer
Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for functions.

### Detailed Explanation
Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.

### Internal Working
Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.

### Production Notes
Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.

### Common Mistakes
Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.

### Follow-up Questions
What observable metric or test would prove your design handles this functions concern in production?

---
<!-- interview-answers:end -->

---

## What changed in Go 1.22 loop variable capture semantics?

### Short Answer
The senior-level answer is know Go 1.22 loop semantics, defer LIFO, and closure capture rules — for: What changed in Go 1.22 loop variable capture semantics.

### Detailed Explanation
Connect syntax rules to runtime impact (alloc, escape) when answering: What changed in Go 1.22 loop variable capture semantics.

### Internal Working
Lexer-inserted semicolons and short declare scoping affect correctness in: What changed in Go 1.22 loop variable capture semantics.

### Production Notes
Enforce go vet/staticcheck for patterns tied to: What changed in Go 1.22 loop variable capture semantics.

### Common Mistakes
Relying on pre-1.22 loop capture behavior causes subtle bugs in: What changed in Go 1.22 loop variable capture semantics.

### Follow-up Questions
What test would catch a regression related to: What changed in Go 1.22 loop variable capture semantics?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Language Basics](/golang-cheatsheet/01-fundamentals/language-basics/)
- [Next: Structs](/golang-cheatsheet/01-fundamentals/structs/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
