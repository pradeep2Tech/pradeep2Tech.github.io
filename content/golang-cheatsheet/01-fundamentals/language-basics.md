---
title: "Go Language Basics"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Syntax, types, zero values, variables, constants, and control flow."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Language Basics"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.1"
weight: 111
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/language-basics/"
---

## Quick Revision

- Go is statically typed, compiled, with garbage collection and CSP-style concurrency.
- **Zero values** are useful defaults; `nil` for references must be checked before use.
- **`defer`** runs LIFO at function return — common for unlock/close.
- **Go 1.22+** fixes per-iteration loop variable capture in `for` loops.
- Type assertions on interfaces: see [Interfaces](/golang-cheatsheet/02-core-go/interfaces/) — max 2 sentences here.

## At a Glance

- C-style braces; semicolons inserted by lexer.
- `:=` short declare inside functions; `var` at package level.
- Zero values: `0`, `""`, `false`, `nil` for references.
- Only `for` loop keyword; `defer` for cleanup.

---

## Reference Tables

| Construct | Recap |
| :--- | :--- |
| **Package** | Every file: `package name` |
| **if** | Optional init: `if err := f(); err != nil { }` |
| **for** | Classic, while-style, `range` |
| **switch** | No fallthrough unless explicit |
| **defer** | LIFO at function return |

| Type category | Zero value | Example |
| :--- | :--- | :--- |
| Numeric | `0` | `int`, `int64`, `float64` |
| `string` | `""` | UTF-8 bytes |
| `bool` | `false` | |
| Pointer, slice, map, chan, func, interface | `nil` | check before use |

| Declaration | When |
| :--- | :--- |
| `var x int` | Package/function; explicit zero |
| `x := 1` | Short declare inside function |
| `const` | Compile-time; `iota` for enums |

| Syntax | Example |
| :--- | :--- |
| Short declare | `x := 42` |
| Multi assign | `a, b := swap(1, 2)` |
| Blank id | `_ = noisy()` |
| Type assertion | `v, ok := x.(T)` |
| iota enum | `const (A = iota; B; C)` |

---

## Snippets

```go
// if with init
if n, err := strconv.Atoi(s); err != nil {
    return err
}

// defer
mu.Lock()
defer mu.Unlock()

// iota
const (
    Pending = iota
    Active
    Closed
)
```

---

## Internals & Gotchas

- `:=` only inside functions; package level needs `var`.
- `:=` redeclares at least one new name in block.
- Unused imports/variables are compile errors.
- `const` cannot be slices/maps.

---

## Production Notes

- Run `go vet` and `staticcheck` in CI.
- Pin Go version in `go.mod` `go` directive.

---

---

---

## See Also

- [Next: Functions](/golang-cheatsheet/01-fundamentals/functions/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
