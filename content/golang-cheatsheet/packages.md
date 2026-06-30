---
title: "Packages"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "package layout, exports, init(), and internal packages."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Packages"
module: 3
moduleTitle: "Packages & Errors"
sectionRef: "3.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Code is organized in **packages** — one directory, one package (usually). **Exported** names start with uppercase. `init()` runs at package load time.

---

## Reference Tables

| Rule | Detail |
| :--- | :--- |
| Package name | Short, lowercase, matches last import path segment |
| Export | `Foo` exported; `foo` package-private |
| `internal/` | Importable only from parent tree |
| `init()` | No args/returns; multiple per file; order within package undefined |
| `main` | `func main()` in `package main` |

```
myapp/
  cmd/api/main.go      # package main
  internal/service/    # internal packages
  pkg/client/          # public library code
```

---

## Snippets

```go
// client/client.go
package client

import "errors"

var ErrNotFound = errors.New("not found")

func Get(id string) (*Item, error) {
    // ...
    return nil, ErrNotFound
}
```

---

## Internals & Gotchas

- Import cycle is a **compile error** — extract shared types to third package.
- `init()` side effects make testing harder — keep minimal.
- Package name should not include underscores or `util`.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Methods](/golang-cheatsheet/methods/)
- [Next: Errors](/golang-cheatsheet/error-handling/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
