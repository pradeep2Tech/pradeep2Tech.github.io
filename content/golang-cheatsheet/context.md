---
title: "Context"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "context.Context, cancellation, deadlines, and passing values."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Context"
module: 5
moduleTitle: "Concurrency"
sectionRef: "5.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `context.Context` carries **deadlines**, **cancellation**, and request-scoped values. Pass as **first parameter** `ctx context.Context`. Never store in structs long-term.

---

## Reference Tables

| Constructor | Purpose |
| :--- | :--- |
| `context.Background()` | Root — main, init, tests |
| `context.TODO()` | Placeholder |
| `WithCancel(parent)` | Manual cancel |
| `WithTimeout` / `WithDeadline` | Auto cancel |
| `WithValue` | Request-scoped data — use sparingly |

```go
ctx, cancel := context.WithTimeout(parent, 5*time.Second)
defer cancel()

req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
```

---

## Snippets

```go
func worker(ctx context.Context) error {
    for {
        select {
        case <-ctx.Done():
            return ctx.Err()
        default:
            if err := step(); err != nil {
                return err
            }
        }
    }
}
```

---

## Internals & Gotchas

- Cancel propagates to children — always `defer cancel()`.
- `WithValue` keys should be unexported types to avoid collisions.
- Don't pass `nil` Context — use `context.Background()`.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Select](/golang-cheatsheet/select/)
- [Next: Mutex](/golang-cheatsheet/mutex/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
