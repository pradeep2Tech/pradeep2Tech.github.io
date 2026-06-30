---
title: "Error Handling"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "error interface, fmt.Errorf, errors.Is/As, wrapping, and sentinel errors."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Errors"
module: 3
moduleTitle: "Packages & Errors"
sectionRef: "3.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Errors are values implementing `error` (`Error() string`). Idiomatic Go returns `err` as last value. Use **`errors.Is`**, **`errors.As`**, and **`fmt.Errorf` with `%w`** for wrapping.

---

## Reference Tables

| Tool | Use |
| :--- | :--- |
| `errors.New` | Sentinel errors |
| `fmt.Errorf("...: %w", err)` | Wrap for chain |
| `errors.Is(err, target)` | Sentinel match through wrap |
| `errors.As(err, &target)` | Typed error extraction |
| `panic` / `recover` | Programmer bugs only — not control flow |

```go
var ErrNotFound = errors.New("not found")

if errors.Is(err, ErrNotFound) { }

var pathErr *os.PathError
if errors.As(err, &pathErr) { }
```

---

## Snippets

```go
func readConfig(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("read config %s: %w", path, err)
    }
    var cfg Config
    if err := json.Unmarshal(data, &cfg); err != nil {
        return nil, fmt.Errorf("parse config: %w", err)
    }
    return &cfg, nil
}
```

---

## Internals & Gotchas

- Don't compare wrapped errors with `==` to sentinel — use `errors.Is`.
- `%v` vs `%w` — only `%w` participates in unwrap chain.
- Log or return — avoid both (duplicate logs).

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Packages](/golang-cheatsheet/packages/)
- [Next: Slices](/golang-cheatsheet/slices/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
