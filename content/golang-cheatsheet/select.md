---
title: "Select"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Multiplexing channels, default case, timeouts, and non-blocking patterns."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Select"
module: 5
moduleTitle: "Concurrency"
sectionRef: "5.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `select` waits on multiple channel operations — like `switch` for channels. Use **`default`** for non-blocking tries; combine with `time.After` for timeouts.

---

## Reference Tables

| Case | Behavior |
| :--- | :--- |
| Ready channel op | One chosen pseudo-randomly if multiple ready |
| `default` | Runs if nothing ready |
| `nil` channel | Never selected |
| Empty select | Blocks forever |

```go
select {
case v := <-ch:
    use(v)
case ch <- x:
    // sent
case <-ctx.Done():
    return ctx.Err()
default:
    // non-blocking
}
```

---

## Snippets

```go
timeout := time.After(2 * time.Second)
select {
case res := <-resultCh:
    return res, nil
case <-timeout:
    return nil, errors.New("timeout")
}
```

---

## Internals & Gotchas

- `select` with only `default` in a loop can spin CPU — add sleep or block elsewhere.
- Don't mix receiving zero values without checking `ok` after close.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: Channels](/golang-cheatsheet/channels/)
- [Next: Context](/golang-cheatsheet/context/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
