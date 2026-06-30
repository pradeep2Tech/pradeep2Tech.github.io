---
title: "Testing"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "testing package, table-driven tests, benchmarks, and testify overview."
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "Testing"
module: 7
moduleTitle: "Testing & Reflection"
sectionRef: "7.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Tests live in `*_test.go` same package (or `package_test` for black-box). Use **table-driven tests**, **`t.Parallel()`**, and **`go test ./...`** in CI.

---

## Reference Tables

| Tool | Command / API |
| :--- | :--- |
| Run | `go test ./...` |
| Verbose | `go test -v` |
| Coverage | `go test -cover ./...` |
| Benchmark | `func BenchmarkX(b *testing.B)` |
| Example | `func ExampleX()` — compile-checked docs |

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        a, b, want int
    }{
        {1, 2, 3},
        {0, 0, 0},
    }
    for _, tt := range tests {
        t.Run(fmt.Sprintf("%d+%d", tt.a, tt.b), func(t *testing.T) {
            if got := Add(tt.a, tt.b); got != tt.want {
                t.Fatalf("got %d want %d", got, tt.want)
            }
        })
    }
}
```

---

## Snippets

```go
func BenchmarkHash(b *testing.B) {
    b.ReportAllocs()
    for i := 0; i < b.N; i++ {
        _ = hash(payload)
    }
}
```

---

## Internals & Gotchas

- `t.Fatal` inside goroutine doesn't stop test reliably — use `t.Run` sync or channels.
- Race detector: `go test -race` — CI essential for concurrent code.
- `init()` in tests affects all tests in package.

---

## Production Notes

- See [Effective Go](https://go.dev/doc/effective_go) for idioms.

---

## See Also

- [Previous: sync](/golang-cheatsheet/sync-package/)
- [Next: Reflection](/golang-cheatsheet/reflection/)
- [Go Cheat Sheet Index](/golang-cheatsheet/)
