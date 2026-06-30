---
title: "Go Language Basics"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Syntax, types, zero values, variables, constants, and control flow — one-page recap."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Language Basics"
module: 1
moduleTitle: "Language Basics"
sectionRef: "1.1"
ShowToc: true
cheatSheet: true
---

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

## See Also

- [Next: Functions](/golang-cheatsheet/functions/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
