"""Build Go Cheat Sheet pages from data/golang_cheatsheet_modules.yaml."""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "golang-cheatsheet"
DATE = "2026-06-30T10:00:00+00:00"
SECTION = "golang-cheatsheet"

# slug -> (title, shortTitle, description)
TOPIC_META: dict[str, tuple[str, str, str]] = {
    "language-basics": (
        "Go Language Basics",
        "Language Basics",
        "Syntax, types, zero values, variables, constants, and control flow — one-page recap.",
    ),
    "functions": (
        "Functions",
        "Functions",
        "Signatures, multiple returns, variadic params, closures, and named results.",
    ),
    "structs": (
        "Structs",
        "Structs",
        "Struct types, embedding, tags, and JSON marshaling patterns.",
    ),
    "interfaces": (
        "Interfaces",
        "Interfaces",
        "Implicit satisfaction, nil interfaces, type assertions, and type switches.",
    ),
    "pointers": (
        "Pointers",
        "Pointers",
        "Address-of, dereference, new vs make, and when pointers matter in Go.",
    ),
    "methods": (
        "Methods",
        "Methods",
        "Value vs pointer receivers, method sets, and interface satisfaction.",
    ),
    "packages": (
        "Packages",
        "Packages",
        "package layout, exports, init(), and internal packages.",
    ),
    "error-handling": (
        "Error Handling",
        "Errors",
        "error interface, fmt.Errorf, errors.Is/As, wrapping, and sentinel errors.",
    ),
    "slices": (
        "Slices",
        "Slices",
        "slice header, append, copy, subslicing, and capacity gotchas.",
    ),
    "arrays": (
        "Arrays",
        "Arrays",
        "Fixed-size arrays, array vs slice, and when arrays appear in APIs.",
    ),
    "maps": (
        "Maps",
        "Maps",
        "map operations, iteration order, nil maps, and sync.Map overview.",
    ),
    "goroutines": (
        "Goroutines",
        "Goroutines",
        "go keyword, scheduler model, GOMAXPROCS, and goroutine leaks.",
    ),
    "channels": (
        "Channels",
        "Channels",
        "Buffered vs unbuffered, close semantics, range, and fan-in/fan-out.",
    ),
    "select": (
        "Select",
        "Select",
        "Multiplexing channels, default case, timeouts, and non-blocking patterns.",
    ),
    "context": (
        "Context",
        "Context",
        "context.Context, cancellation, deadlines, and passing values.",
    ),
    "mutex": (
        "Mutex",
        "Mutex",
        "sync.Mutex, Lock/Unlock, defer unlock, and common deadlock patterns.",
    ),
    "rwmutex": (
        "RWMutex",
        "RWMutex",
        "sync.RWMutex — concurrent reads, exclusive writes, and upgrade rules.",
    ),
    "sync-package": (
        "sync Package",
        "sync",
        "WaitGroup, Once, Pool, Cond, and Map — coordination primitives.",
    ),
    "testing": (
        "Testing",
        "Testing",
        "testing package, table-driven tests, benchmarks, and testify overview.",
    ),
    "reflection": (
        "Reflection",
        "Reflection",
        "reflect.Type, reflect.Value, Kind, and when to avoid reflection.",
    ),
    "memory-model": (
        "Memory Model",
        "Memory Model",
        "Happens-before, visibility, atomics, and data races in Go.",
    ),
    "garbage-collection": (
        "Garbage Collection",
        "GC",
        "Go GC tri-color mark-sweep, GOGC, pacing, and allocation tuning.",
    ),
    "go-modules": (
        "Go Modules",
        "Modules",
        "go.mod, go.sum, module path, replace, and workspace mode.",
    ),
    "dependency-management": (
        "Dependency Management",
        "Dependencies",
        "go get, versioning, minimal version selection, and vendoring.",
    ),
    "interview-questions": (
        "Go Interview Questions",
        "Interview",
        "High-signal Go interview probes — concurrency, interfaces, slices, and GC.",
    ),
}


def flatten_topics(modules: list) -> list[str]:
    topics: list[str] = []
    for mod in modules:
        if mod.get("groups"):
            for group in mod["groups"]:
                topics.extend(group["topics"])
        else:
            topics.extend(mod["topics"])
    return topics


def iter_module_topics(modules: list) -> list[tuple[int, str, str, int]]:
    result: list[tuple[int, str, str, int]] = []
    for mod in modules:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        slugs = flatten_topics([mod])
        for idx, slug in enumerate(slugs, start=1):
            result.append((mod_id, mod_title, slug, idx))
    return result


def write_order_yaml(topics: list[str], path: Path) -> None:
    header = (
        "# Flat topic order — derived from golang_cheatsheet_modules.yaml.\n"
        "# Prefer editing data/golang_cheatsheet_modules.yaml for module structure.\n"
        "topics:\n"
    )
    path.write_text(header + "".join(f"  - {s}\n" for s in topics), encoding="utf-8")


def see_also(slug: str, ordered: list[str]) -> str:
    links: list[str] = []
    idx = ordered.index(slug)
    if idx > 0:
        prev = ordered[idx - 1]
        links.append(f"- [Previous: {TOPIC_META[prev][1]}](/{SECTION}/{prev}/)")
    if idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        links.append(f"- [Next: {TOPIC_META[nxt][1]}](/{SECTION}/{nxt}/)")
    links.append(f"- [Go Cheat Sheet Index](/{SECTION}/)")
    return "\n".join(links)


def page_body(
    summary: str,
    concepts: str,
    quick_ref: str,
    snippets: str,
    gotchas: str,
    related: str,
    glance: list[str] | None = None,
    production: str = "",
) -> str:
    bullets = glance if glance else [summary]
    tables = concepts.strip()
    if quick_ref.strip():
        tables = tables + "\n\n" + quick_ref.strip()
    prod = production.strip() or "- See [Effective Go](https://go.dev/doc/effective_go) for idioms."
    return f"""## At a Glance

{chr(10).join(f"- {b}" for b in bullets)}

---

## Reference Tables

{tables}

---

## Snippets

{snippets.strip()}

---

## Internals & Gotchas

{gotchas.strip()}

---

## Production Notes

{prod}

---

## See Also

{related.strip()}
"""


TOPIC_BODIES: dict[str, dict[str, str]] = {
    "language-basics": {
        "summary": "Go basics in one page — syntax, types, zero values, variables, and control flow.",
        "glance": [
            "C-style braces; semicolons inserted by lexer.",
            "`:=` short declare inside functions; `var` at package level.",
            "Zero values: `0`, `\"\"`, `false`, `nil` for references.",
            "Only `for` loop keyword; `defer` for cleanup.",
        ],
        "concepts": """| Construct | Recap |
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
| `const` | Compile-time; `iota` for enums |""",
        "quick_ref": """| Syntax | Example |
| :--- | :--- |
| Short declare | `x := 42` |
| Multi assign | `a, b := swap(1, 2)` |
| Blank id | `_ = noisy()` |
| Type assertion | `v, ok := x.(T)` |
| iota enum | `const (A = iota; B; C)` |""",
        "snippets": """```go
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
```""",
        "gotchas": """- `:=` only inside functions; package level needs `var`.
- `:=` redeclares at least one new name in block.
- Unused imports/variables are compile errors.
- `const` cannot be slices/maps.""",
        "production": "- Run `go vet` and `staticcheck` in CI.\n- Pin Go version in `go.mod` `go` directive.",
    },
    "syntax": {
        "summary": "Go uses **C-style braces**, **no semicolons** (inserted by lexer), and **explicit types** with type inference via `:=`. Control flow is minimal: `if`, `for`, `switch`, `select`, plus `defer` for cleanup.",
        "concepts": """| Construct | Recap |
| :--- | :--- |
| **Package** | Every file starts with `package name` |
| **Imports** | Single or grouped `import (...)` |
| **if** | Optional init statement: `if err := f(); err != nil { }` |
| **for** | Only loop keyword — classic, while-style, range |
| **switch** | No fallthrough by default; `break` implicit |
| **defer** | LIFO at function return — args evaluated immediately |
| **go** | Starts goroutine — see [Goroutines](/golang-cheatsheet/goroutines/) |

```mermaid
flowchart TD
  src[.go source] --> lexer[Lexer + semicolon insert]
  lexer --> parser[Parser]
  parser --> types[Type checker]
  types --> ir[SSA / IR]
  ir --> machine[Native code]
```""",
        "quick_ref": """| Syntax | Example |
| :--- | :--- |
| Short declare | `x := 42` |
| Multi assign | `a, b := swap(1, 2)` |
| Blank identifier | `_ = noisy()` |
| Type assertion | `v, ok := x.(T)` |
| Range | `for i, v := range s { }` |""",
        "snippets": """```go
// if with init — scope limited to if/else
if n, err := strconv.Atoi(s); err != nil {
    return err
} else if n < 0 {
    return fmt.Errorf("negative: %d", n)
}

// defer — common for unlock/close
mu.Lock()
defer mu.Unlock()

// switch on type
switch v := x.(type) {
case int:
    fmt.Println("int", v)
case string:
    fmt.Println("string", v)
default:
    fmt.Println("unknown")
}
```""",
        "gotchas": """- `:=` only inside functions; use `var` at package level.
- `defer` runs when the **surrounding function** returns, not when the `defer` statement's block ends.
- Unused imports and variables are **compile errors**.
- `switch` cases don't fall through unless `fallthrough` is explicit.""",
    },
    "variables": {
        "summary": "Go variables have **block scope**, **zero values** when uninitialized, and support **`const`** for compile-time constants. Use `:=` for local inference; `var` when you need zero value without assignment.",
        "concepts": """| Form | When to use |
| :--- | :--- |
| `var x int` | Package or function level; explicit zero |
| `x := 1` | Short declare inside functions |
| `const` | Compile-time constants; `iota` for enums |
| Zero value | `0`, `""`, `false`, `nil` for references |

| Type category | Zero value |
| :--- | :--- |
| Numeric | `0` |
| `string` | `""` |
| `bool` | `false` |
| Pointer, slice, map, chan, func, interface | `nil` |""",
        "quick_ref": """```go
var (
    host string = "localhost"
    port int
)

const (
    StatusOK = 200
    StatusNotFound = 404
)

// iota enum
const (
    Pending = iota
    Active
    Closed
)
```""",
        "snippets": """```go
// Grouped declarations
var (
    mu    sync.Mutex
    cache = make(map[string]any)
)

// Shadowing — inner x hides outer
x := 1
{
    x := 2 // new variable in inner block
    _ = x
}
```""",
        "gotchas": """- `:=` redeclares at least one **new** name in the block; otherwise use `=`.
- `const` can only be numbers, strings, or booleans — not slices/maps.
- Package-level `var` init order follows dependency; `init()` runs after.""",
    },
    "functions": {
        "summary": "Functions are first-class values. Go supports **multiple return values** (idiomatic for `result, err`), **variadic** parameters, **named results**, and **closures** that capture variables by reference.",
        "concepts": """| Feature | Notes |
| :--- | :--- |
| Signature | `func name(params) (results)` |
| Multiple returns | `(T, error)` is standard |
| Named results | `func f() (n int, err error)` — naked return |
| Variadic | `func sum(nums ...int)` |
| Closures | Capture outer variables; watch loop variable capture (Go 1.22+ fixed per-iteration) |
| Methods | See [Methods](/golang-cheatsheet/methods/) |""",
        "quick_ref": """| Pattern | Example |
| :--- | :--- |
| Error return | `return nil, fmt.Errorf("...")` |
| Defer recover | `defer func() { if r := recover(); r != nil { } }()` |
| Function type | `type Handler func(http.ResponseWriter, *http.Request)` |
| Anonymous | `go func() { }()` |""",
        "snippets": """```go
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
```""",
        "gotchas": """- Named return values can be confusing in long functions — prefer explicit `return x, err`.
- `recover()` only works inside deferred functions in the **same goroutine**.
- Passing functions to goroutines: capture loop vars explicitly in Go < 1.22.""",
    },
    "structs": {
        "summary": "**Structs** group fields. Go uses **composition over inheritance** via **embedded** anonymous fields. Struct tags drive JSON/XML encoding.",
        "concepts": """| Concept | Recap |
| :--- | :--- |
| Literal | `Point{X: 1, Y: 2}` or `Point{1, 2}` |
| Embedding | Anonymous field promotes methods/fields |
| Tags | `` `json:"name,omitempty"` `` |
| Comparable | Struct comparable if all fields comparable |
| Zero value | All fields zeroed |""",
        "quick_ref": """| Operation | Syntax |
| :--- | :--- |
| Pointer to struct | `&User{Name: "a"}` or `new(User)` |
| Embedded access | `s.Field` promoted from embed |
| Copy | Assignment copies all fields (shallow) |""",
        "snippets": """```go
type User struct {
    ID   int    `json:"id"`
    Name string `json:"name,omitempty"`
}

type Admin struct {
    User            // embedded
    Permissions []string
}

func (u User) String() string {
    return fmt.Sprintf("User(%d)", u.ID)
}
```""",
        "gotchas": """- Embedded pointer fields: `nil` embed → promoted methods may panic.
- Comparing structs with slices/maps inside is **invalid**.
- JSON `omitempty` skips zero values — `false`, `0`, `""`, `nil`.""",
    },
    "interfaces": {
        "summary": "Interfaces are **implicit** — no `implements` keyword. A type satisfies an interface if it has the required methods. The **nil interface trap** (`var i io.Reader = (*bytes.Buffer)(nil)`) is a classic interview topic.",
        "concepts": """```mermaid
flowchart LR
  concrete[Concrete type] -->|method set| iface[Interface value]
  iface -->|type assert| concrete
```

| Concept | Detail |
| :--- | :--- |
| Interface value | `(type, data)` pair |
| Nil interface | `var i io.Reader` — both nil |
| Typed nil | Interface holding nil pointer — **not equal to nil** |
| Empty interface | `any` / `interface{}` |
| Satisfaction | Pointer vs value receiver affects method set |""",
        "quick_ref": """| Operation | Code |
| :--- | :--- |
| Type assertion | `v := i.(T)` or `v, ok := i.(T)` |
| Type switch | `switch v := i.(type) { case T: }` |
| Compile-time check | `var _ io.Reader = (*MyType)(nil)` |""",
        "snippets": """```go
type Reader interface {
    Read(p []byte) (n int, err error)
}

func process(r Reader) error {
    buf := make([]byte, 1024)
    _, err := r.Read(buf)
    return err
}

// nil trap
var buf *bytes.Buffer
var r io.Reader = buf
fmt.Println(r == nil) // false
```""",
        "gotchas": """- Keep interfaces **small** — accept interfaces, return concrete types.
- Value receiver methods → value and pointer satisfy; pointer-only methods → only pointer satisfies.
- Don't use `any` when a specific interface documents intent.""",
    },
    "pointers": {
        "summary": "Pointers hold addresses. Go has **no pointer arithmetic**. Use pointers for mutation, large structs, or optional presence (`nil` pointer).",
        "concepts": """| Operator | Meaning |
| :--- | :--- |
| `&x` | Address of x |
| `*p` | Value at p |
| `new(T)` | `*T` allocated, zeroed |
| `make(T)` | Only slice, map, chan — not `new` |

| Prefer pointer when | Prefer value when |
| :--- | :--- |
| Mutate callee state | Small, immutable structs |
| Avoid copy | No mutation needed |
| `nil` means absent | Sync/copy semantics matter |""",
        "quick_ref": """```go
p := new(int)   // *int, zero
*p = 42

type Node struct { Next *Node }

func (n *Node) SetNext(next *Node) { n.Next = next }
```""",
        "snippets": """```go
func swap(a, b *int) {
    *a, *b = *b, *a
}

x, y := 1, 2
swap(&x, &y)
```""",
        "gotchas": """- `new` returns pointer; `make` initializes slice/map/chan internals.
- Taking address of map element is **illegal** (may move on grow).
- `nil` pointer dereference panics.""",
    },
    "methods": {
        "summary": "Methods are functions with a **receiver**. **Value receivers** copy; **pointer receivers** mutate and are required when the method modifies the receiver or the struct is large.",
        "concepts": """| Receiver | Method set includes |
| :--- | :--- |
| `(T)` | Methods with value receiver |
| `(*T)` | Methods with pointer **and** value receiver |

| Rule of thumb | Use |
| :--- | :--- |
| Mutates receiver | Pointer receiver |
| Contains sync.Mutex | Pointer receiver (don't copy mutex) |
| Small immutable type | Value receiver |""",
        "quick_ref": """```go
type Counter struct{ n int }

func (c *Counter) Inc() { c.n++ }
func (c Counter) Value() int { return c.n }
```""",
        "snippets": """```go
type Buffer struct {
    b []byte
}

func (b *Buffer) Write(p []byte) (int, error) {
    b.b = append(b.b, p...)
    return len(p), nil
}

func (b Buffer) Len() int { return len(b.b) }
```""",
        "gotchas": """- Calling pointer method on addressable value auto-takes `&`.
- Interface satisfaction uses **method set** of the stored type.
- Don't mix value/pointer receivers on same type without reason.""",
    },
    "packages": {
        "summary": "Code is organized in **packages** — one directory, one package (usually). **Exported** names start with uppercase. `init()` runs at package load time.",
        "concepts": """| Rule | Detail |
| :--- | :--- |
| Package name | Short, lowercase, matches last import path segment |
| Export | `Foo` exported; `foo` package-private |
| `internal/` | Importable only from parent tree |
| `init()` | No args/returns; multiple per file; order within package undefined |
| `main` | `func main()` in `package main` |""",
        "quick_ref": """```
myapp/
  cmd/api/main.go      # package main
  internal/service/    # internal packages
  pkg/client/          # public library code
```""",
        "snippets": """```go
// client/client.go
package client

import "errors"

var ErrNotFound = errors.New("not found")

func Get(id string) (*Item, error) {
    // ...
    return nil, ErrNotFound
}
```""",
        "gotchas": """- Import cycle is a **compile error** — extract shared types to third package.
- `init()` side effects make testing harder — keep minimal.
- Package name should not include underscores or `util`.""",
    },
    "error-handling": {
        "summary": "Errors are values implementing `error` (`Error() string`). Idiomatic Go returns `err` as last value. Use **`errors.Is`**, **`errors.As`**, and **`fmt.Errorf` with `%w`** for wrapping.",
        "concepts": """| Tool | Use |
| :--- | :--- |
| `errors.New` | Sentinel errors |
| `fmt.Errorf("...: %w", err)` | Wrap for chain |
| `errors.Is(err, target)` | Sentinel match through wrap |
| `errors.As(err, &target)` | Typed error extraction |
| `panic` / `recover` | Programmer bugs only — not control flow |""",
        "quick_ref": """```go
var ErrNotFound = errors.New("not found")

if errors.Is(err, ErrNotFound) { }

var pathErr *os.PathError
if errors.As(err, &pathErr) { }
```""",
        "snippets": """```go
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
```""",
        "gotchas": """- Don't compare wrapped errors with `==` to sentinel — use `errors.Is`.
- `%v` vs `%w` — only `%w` participates in unwrap chain.
- Log or return — avoid both (duplicate logs).""",
    },
    "slices": {
        "summary": "Slices are **views** over an array: `(pointer, len, cap)`. **`append`** may reallocate. Slices are reference-like but not pointers.",
        "concepts": """```mermaid
flowchart LR
  slice["slice header"] --> array["backing array"]
```

| Field | Meaning |
| :--- | :--- |
| `len` | Visible elements |
| `cap` | From ptr to end of backing array |
| `append` | Grows cap ~2x when needed |""",
        "quick_ref": """| Op | Code |
| :--- | :--- |
| Make | `s := make([]int, 0, 64)` |
| Subslice | `s[low:high]` shares backing array |
| Copy | `copy(dst, src)` |
| Clear (1.21+) | `clear(s)` |""",
        "snippets": """```go
s := []int{1, 2, 3}
s = append(s, 4)

sub := s[1:3] // shares backing array
sub[0] = 99   // mutates s[1]

// avoid leak: sub = append(sub[:0:0], sub...)
```""",
        "gotchas": """- Subslices retain backing array → memory leaks if large array, small slice kept.
- `append` to subsliced header may overwrite shared region if cap allows.
- `nil` slice vs empty slice: JSON `null` vs `[]` if you care.""",
    },
    "arrays": {
        "summary": "Arrays have **fixed size** — part of the type (`[3]int` ≠ `[4]int`). Rare in APIs; prefer slices. Arrays are **values** (copied on assignment).",
        "concepts": """| Array | Slice |
| :--- | :--- |
| `[N]T` fixed | `[]T` dynamic length |
| Value semantics | Header + backing array |
| Comparable | Not comparable if element not comparable |""",
        "quick_ref": """```go
var a [3]int = [3]int{1, 2, 3}
b := [...]int{1, 2, 3} // compiler counts

// array to slice
s := a[:] // slice view of array
```""",
        "snippets": """```go
// crypto keys, fixed buffers
var key [32]byte
copy(key[:], seed)
```""",
        "gotchas": """- Large arrays as parameters copy entire value — pass pointer or slice.
- `[ ]` in function param is slice, not array.""",
    },
    "maps": {
        "summary": "Maps are hash tables — **reference type** (like slices). Must be initialized with `make` or literal before write. **Iteration order is randomized**.",
        "concepts": """| Op | Code |
| :--- | :--- |
| Literal | `m := map[string]int{"a": 1}` |
| Make | `m := make(map[string]int, 100)` |
| Read | `v := m[k]` — zero value if missing |
| Check | `v, ok := m[k]` |
| Delete | `delete(m, k)` |""",
        "quick_ref": """| Topic | Note |
| :--- | :--- |
| Nil map | Read OK; write panics |
| Not addressable elements | Can't `&m[k]` |
| Concurrent | Use `sync.Map` or mutex + map |""",
        "snippets": """```go
counts := make(map[string]int)
counts["go"]++

if v, ok := counts["rust"]; ok {
    _ = v
}

for k, v := range counts {
    fmt.Println(k, v)
}
```""",
        "gotchas": """- Never R/W same map from goroutines without sync.
- Taking pointer to value in map forbidden.
- Map keys must be comparable — no slices/maps/funcs as keys.""",
    },
    "goroutines": {
        "summary": "**Goroutines** are lightweight threads scheduled by the Go runtime on OS threads (`GOMAXPROCS`). Start with `go f()`. Always know **how they exit** and how errors propagate.",
        "concepts": """```mermaid
flowchart TB
  g1[Goroutine] --> p[P]
  g2[Goroutine] --> p
  p[M] --> os[OS thread]
```

| Concept | Detail |
| :--- | :--- |
| Stack | Starts small, grows/shrinks |
| Scheduler | M:N — work stealing |
| `GOMAXPROCS` | Default `runtime.NumCPU()` |
| Leak | Blocked forever on send/recv |""",
        "quick_ref": """```go
go func() {
    if err := work(); err != nil {
        log.Printf("work: %v", err)
    }
}()

// wait for completion
var wg sync.WaitGroup
wg.Add(1)
go func() { defer wg.Done(); work() }()
wg.Wait()
```""",
        "snippets": """```go
errCh := make(chan error, 1)
go func() {
    errCh <- doWork()
}()
if err := <-errCh; err != nil {
    return err
}
```""",
        "gotchas": """- Main exiting kills all goroutines — no graceful shutdown by default.
- Panic in goroutine crashes process unless recovered.
- Unbounded `go` spawn → OOM; use worker pools or semaphores.""",
    },
    "channels": {
        "summary": "Channels coordinate goroutines — **typed conduits**. Unbuffered = synchronous handoff; buffered = async up to capacity. **Close** signals no more sends; receivers drain then get zero value + `ok=false`.",
        "concepts": """| Type | Behavior |
| :--- | :--- |
| `chan T` | Unbuffered — send blocks until recv |
| `chan T` (cap>0) | Buffered — blocks when full |
| Close | `close(ch)` — only sender should close |
| Range | `for v := range ch` until closed |""",
        "quick_ref": """```go
ch := make(chan int)       // unbuffered
buf := make(chan int, 10)  // buffered

ch <- 1
v := <-ch

close(ch)
v, ok := <-ch // ok false when drained
```""",
        "snippets": """```go
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
```""",
        "gotchas": """- Send on closed channel **panics**.
- Close from non-sender side is a bug.
- `nil` channel blocks forever on send/recv — useful in `select`.""",
    },
    "select": {
        "summary": "`select` waits on multiple channel operations — like `switch` for channels. Use **`default`** for non-blocking tries; combine with `time.After` for timeouts.",
        "concepts": """| Case | Behavior |
| :--- | :--- |
| Ready channel op | One chosen pseudo-randomly if multiple ready |
| `default` | Runs if nothing ready |
| `nil` channel | Never selected |
| Empty select | Blocks forever |""",
        "quick_ref": """```go
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
```""",
        "snippets": """```go
timeout := time.After(2 * time.Second)
select {
case res := <-resultCh:
    return res, nil
case <-timeout:
    return nil, errors.New("timeout")
}
```""",
        "gotchas": """- `select` with only `default` in a loop can spin CPU — add sleep or block elsewhere.
- Don't mix receiving zero values without checking `ok` after close.""",
    },
    "context": {
        "summary": "`context.Context` carries **deadlines**, **cancellation**, and request-scoped values. Pass as **first parameter** `ctx context.Context`. Never store in structs long-term.",
        "concepts": """| Constructor | Purpose |
| :--- | :--- |
| `context.Background()` | Root — main, init, tests |
| `context.TODO()` | Placeholder |
| `WithCancel(parent)` | Manual cancel |
| `WithTimeout` / `WithDeadline` | Auto cancel |
| `WithValue` | Request-scoped data — use sparingly |""",
        "quick_ref": """```go
ctx, cancel := context.WithTimeout(parent, 5*time.Second)
defer cancel()

req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
```""",
        "snippets": """```go
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
```""",
        "gotchas": """- Cancel propagates to children — always `defer cancel()`.
- `WithValue` keys should be unexported types to avoid collisions.
- Don't pass `nil` Context — use `context.Background()`.""",
    },
    "mutex": {
        "summary": "`sync.Mutex` provides **exclusive** lock. Prefer **`defer mu.Unlock()`** immediately after `Lock()`. Protect shared mutable state — not individual reads if `RWMutex` fits.",
        "concepts": """| API | Use |
| :--- | :--- |
| `Lock()` / `Unlock()` | Exclusive access |
| `TryLock()` (1.18+) | Non-blocking attempt |
| Copy | Mutex must not be copied after first use |""",
        "quick_ref": """```go
type SafeMap struct {
    mu sync.Mutex
    m  map[string]int
}

func (s *SafeMap) Inc(key string) {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.m[key]++
}
```""",
        "snippets": """```go
var mu sync.Mutex
var balance int

func deposit(amount int) {
    mu.Lock()
    defer mu.Unlock()
    balance += amount
}
```""",
        "gotchas": """- Lock ordering across goroutines → deadlock — establish global order.
- Holding lock during I/O blocks all waiters — copy data and release.
- Don't embed mutex in exported struct if callers might copy struct.""",
    },
    "rwmutex": {
        "summary": "`sync.RWMutex` allows **many readers** OR **one writer**. Better read-heavy caches; writers still exclude everyone.",
        "concepts": """| Method | Access |
| :--- | :--- |
| `RLock` / `RUnlock` | Shared read |
| `Lock` / `Unlock` | Exclusive write |
| Rule | No `RLock` while holding `Lock` upgrade |""",
        "quick_ref": """```go
type Cache struct {
    mu sync.RWMutex
    data map[string]string
}

func (c *Cache) Get(k string) (string, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    v, ok := c.data[k]
    return v, ok
}
```""",
        "snippets": """```go
func (c *Cache) Set(k, v string) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.data[k] = v
}
```""",
        "gotchas": """- Writer starvation possible under constant readers — rare but know it.
- `RWMutex` is heavier than `Mutex` for write-heavy workloads.
- Same no-copy rule as `Mutex`.""",
    },
    "sync-package": {
        "summary": "Package **`sync`** provides low-level primitives beyond channels: **WaitGroup**, **Once**, **Pool**, **Cond**, and **Map**.",
        "concepts": """| Type | Purpose |
| :--- | :--- |
| `WaitGroup` | Wait for N goroutines |
| `Once` | Run exactly once |
| `Pool` | Reuse temporary objects — GC can clear |
| `Cond` | Wait/signal — needs external lock |
| `Map` | Concurrent map — special cases only |""",
        "quick_ref": """```go
var once sync.Once
once.Do(func() { initExpensive() })

var wg sync.WaitGroup
wg.Add(n)
// ... wg.Done() per worker
wg.Wait()
```""",
        "snippets": """```go
var bufPool = sync.Pool{
    New: func() any { return new(bytes.Buffer) },
}

func getBuf() *bytes.Buffer {
    return bufPool.Get().(*bytes.Buffer)
}
```""",
        "gotchas": """- `WaitGroup` — `Add` before `go`; don't copy after use.
- `Pool` objects may disappear anytime — reset state on Get.
- Prefer channel + mutex over `sync.Map` unless read-heavy stable key set.""",
    },
    "testing": {
        "summary": "Tests live in `*_test.go` same package (or `package_test` for black-box). Use **table-driven tests**, **`t.Parallel()`**, and **`go test ./...`** in CI.",
        "concepts": """| Tool | Command / API |
| :--- | :--- |
| Run | `go test ./...` |
| Verbose | `go test -v` |
| Coverage | `go test -cover ./...` |
| Benchmark | `func BenchmarkX(b *testing.B)` |
| Example | `func ExampleX()` — compile-checked docs |""",
        "quick_ref": """```go
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
```""",
        "snippets": """```go
func BenchmarkHash(b *testing.B) {
    b.ReportAllocs()
    for i := 0; i < b.N; i++ {
        _ = hash(payload)
    }
}
```""",
        "gotchas": """- `t.Fatal` inside goroutine doesn't stop test reliably — use `t.Run` sync or channels.
- Race detector: `go test -race` — CI essential for concurrent code.
- `init()` in tests affects all tests in package.""",
    },
    "reflection": {
        "summary": "**Reflection** inspects types at runtime via `reflect.Type` and `reflect.Value`. Powerful for serializers and DI — **avoid** on hot paths; loses compile-time safety.",
        "concepts": """| API | Role |
| :--- | :--- |
| `reflect.TypeOf(v)` | Static type |
| `reflect.ValueOf(v)` | Runtime value |
| `Kind()` | Underlying kind — `Struct`, `Ptr`, `Slice` |
| `Field` / `Set` | Struct field access — need addressable value to Set |""",
        "quick_ref": """```go
v := reflect.ValueOf(x)
if v.Kind() == reflect.Ptr {
    v = v.Elem()
}
for i := 0; i < v.NumField(); i++ {
    f := v.Type().Field(i)
    _ = f.Name
}
```""",
        "snippets": """```go
func deepEqual(a, b any) bool {
    return reflect.DeepEqual(a, b)
}
```""",
        "gotchas": """- `reflect.Value` must be **addressable** to modify.
- Breaking refactor won't compile-check reflection-based field access.
- Prefer generics (1.18+) over reflection when possible.""",
    },
    "memory-model": {
        "summary": "Go's **memory model** defines when reads/writes are visible across goroutines via **happens-before** edges. Data races are undefined behavior — use sync or channels.",
        "concepts": """| Happens-before from | Examples |
| :--- | :--- |
| Channel ops | Send happens-before receive completes |
| `sync` primitives | Unlock happens-before next Lock |
| `Once` | `Do` completion before return |
| `atomic` | Atomic ops provide synchronization |""",
        "quick_ref": """```go
// DATA RACE — undefined
var x int
go func() { x++ }()
x++

// FIX
var mu sync.Mutex
go func() { mu.Lock(); x++; mu.Unlock() }()
```""",
        "snippets": """```go
import "sync/atomic"

var count atomic.Int64
count.Add(1)
```""",
        "gotchas": """- `go test -race` catches races — run in CI.
- `volatile` doesn't exist — use `atomic` or mutex.
- Compiler/CPU reordering invisible within single goroutine sequential consistency.""",
    },
    "garbage-collection": {
        "summary": "Go uses a **non-generational, concurrent tri-color mark-sweep** collector. Tuning via **`GOGC`** (default 100). **STW** pauses are short but exist.",
        "concepts": """```mermaid
flowchart LR
  alloc[Allocation] --> heap[Heap]
  heap --> mark[Concurrent mark]
  mark --> sweep[Sweep]
```

| Knob | Effect |
| :--- | :--- |
| `GOGC=100` | Heap doubles before next GC cycle |
| `GOGC=off` | Disable GC (debug only) |
| `GODEBUG=gctrace=1` | Log GC events |
| `runtime.GC()` | Force GC — rarely in prod |""",
        "quick_ref": """| Goal | Approach |
| :--- | :--- |
| Less GC CPU | Reduce allocations — pools, reuse buffers |
| Lower latency | Fewer pointers, smaller heap |
| Profile | `pprof` heap/allocs |""",
        "snippets": """```go
// prefer sync.Pool for short-lived buffers
// prefer value semantics for hot structs
// preallocate slices: make([]T, 0, n)
```""",
        "gotchas": """- Finalizers (`runtime.SetFinalizer`) run unpredictably — don't rely for cleanup.
- Large heap = longer mark phase — allocation rate matters more than live set alone.
- `uintptr` is not a GC root — keep pointer alive.""",
    },
    "go-modules": {
        "summary": "**Go modules** are the unit of dependency versioning since Go 1.16+. Defined by **`go.mod`** at module root; checksums in **`go.sum`**.",
        "concepts": """| File | Role |
| :--- | :--- |
| `go.mod` | Module path, Go version, require/replace/exclude |
| `go.sum` | Cryptographic checksums of module contents |
| `go.work` | Multi-module workspace (local dev) |

| Directive | Purpose |
| :--- | :--- |
| `module` | Import path prefix |
| `require` | Dependencies |
| `replace` | Local fork or vanity redirect |
| `retract` | Withdraw bad versions |""",
        "quick_ref": """```bash
go mod init example.com/myapp
go mod tidy
go mod verify
go mod graph
```""",
        "snippets": """```go
module github.com/org/project

go 1.22

require (
    github.com/lib/pq v1.10.9
)
```""",
        "gotchas": """- Commit `go.sum` — required for reproducible builds.
- Major version `/v2` in module path for v2+ APIs.
- `replace` in go.mod is local-only — don't rely in published libraries.""",
    },
    "dependency-management": {
        "summary": "Go uses **Minimal Version Selection (MVS)** — `go.mod` lists minimum versions; build picks lowest compatible set. Upgrade with **`go get pkg@version`**.",
        "concepts": """| Command | Action |
| :--- | :--- |
| `go get pkg@latest` | Upgrade to latest |
| `go get pkg@v1.2.3` | Pin version |
| `go get pkg@none` | Remove dependency |
| `go mod vendor` | Copy deps to `vendor/` |
| `go list -m all` | Resolved module list |""",
        "quick_ref": """```bash
go get -u ./...
go get github.com/foo/bar@v1.5.0
go mod tidy   # add missing, drop unused
```""",
        "snippets": """```bash
# private module
GOPRIVATE=github.com/myorg/*
go env -w GOPRIVATE=github.com/myorg/*
```""",
        "gotchas": """- `go get -u` in library repos — bump carefully; consumers resolve MVS.
- Vendoring: `-mod=vendor` in CI for hermetic builds.
- Pseudo-versions for untagged commits: `v0.0.0-20240101120000-abcdef`.""",
    },
    "interview-questions": {
        "summary": "High-signal **Go interview** topics: interface nil semantics, slice internals, concurrency patterns, error handling, and GC/allocation trade-offs.",
        "concepts": """| Topic | Classic question |
| :--- | :--- |
| Interfaces | Why `interface == nil` is false with typed nil |
| Slices | What `append` does to cap/len and aliasing |
| Concurrency | Buffered vs unbuffered; when to use mutex vs channel |
| Errors | `%w` vs `%v`; `errors.Is` |
| Runtime | What GOGC does; how to reduce GC pressure |""",
        "quick_ref": """| Probe | Strong answer shape |
| :--- | :--- |
| Goroutine vs thread | M:N scheduling, smaller stacks, cooperative points |
| Map concurrency | Not safe — mutex or sync.Map |
| Context | Cancellation tree; first param; defer cancel |
| defer order | LIFO; args evaluated at defer statement |""",
        "snippets": """```go
// Q: What prints?
var w io.Writer
var buf *bytes.Buffer
w = buf
fmt.Println(w == nil) // false

// Q: slice after append
x := []int{1, 2, 3}
y := append(x[:2], 99)
// know shared backing array effects
```""",
        "gotchas": """- Memorize **nil interface** and **slice header** — most common loops.
- "Share memory by communicating" — but know when mutex is simpler.
- Read [Effective Go](https://go.dev/doc/effective_go) and Go FAQ for phrasing.""",
    },
}


def front_matter(slug: str, mod_id: int, mod_title: str, topic_idx: int) -> str:
    title, short, desc = TOPIC_META[slug]
    return f"""---
title: "{title}"
date: {DATE}
draft: false
description: "{desc}"
tags: ["golang", "go", "golang-cheatsheet", "cheatsheet", "handbook"]
categories: ["Go Cheat Sheet"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{mod_id}.{topic_idx}"
cheatSheet: true
---

"""


def main() -> None:
    if (CONTENT / "01-fundamentals").is_dir():
        print(
            "Go handbook uses nested module layout; "
            "skipping flat cheat-sheet regen. Edit content/golang-cheatsheet/ directly."
        )
        return

    modules_path = DATA / "golang_cheatsheet_modules.yaml"
    with modules_path.open(encoding="utf-8") as f:
        modules = yaml.safe_load(f)["modules"]

    ordered = flatten_topics(modules)
    write_order_yaml(ordered, DATA / "golang_cheatsheet_order.yaml")

    CONTENT.mkdir(parents=True, exist_ok=True)
    valid_slugs = set(ordered)

    for mod_id, mod_title, slug, topic_idx in iter_module_topics(modules):
        if slug not in TOPIC_BODIES:
            raise KeyError(f"Missing body for topic: {slug}")
        body_data = TOPIC_BODIES[slug]
        related = see_also(slug, ordered)
        body = page_body(
            summary=body_data["summary"],
            concepts=body_data["concepts"],
            quick_ref=body_data["quick_ref"],
            snippets=body_data["snippets"],
            gotchas=body_data["gotchas"],
            related=related,
            glance=body_data.get("glance"),
            production=body_data.get("production", ""),
        )
        path = CONTENT / f"{slug}.md"
        path.write_text(front_matter(slug, mod_id, mod_title, topic_idx) + body, encoding="utf-8")

    for path in CONTENT.glob("*.md"):
        if path.name == "_index.md":
            continue
        slug = path.stem
        if slug not in valid_slugs:
            path.unlink()
            print(f"pruned orphan: {path.name}")

    print(f"Wrote {len(ordered)} pages to {CONTENT}")


if __name__ == "__main__":
    main()
