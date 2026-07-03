"""Phase D: P1/P2 mermaid, fundamentals expansion, unique answer refresh."""
from __future__ import annotations

import re
from pathlib import Path

from phase_c_golang_handbook import (
    ANSWER_END,
    ANSWER_START,
    HB,
    BASE,
    SKIP_ANSWER_PREFIXES,
    append_answers,
    build_answer_blocks,
    build_see_also,
    group_questions_by_page,
    insert_mermaid,
    load_topic_order,
    remove_old_answers,
    remove_section,
    strip_front_matter,
)

MERMAID_P1: dict[str, str] = {
    "01-fundamentals/slices.md": """
```mermaid
flowchart TB
  old[backing array cap=4] --> append[append within cap]
  append --> share[mutates shared region]
  old --> grow[append exceeds cap]
  grow --> newarr[new backing array]
```
""",
    "02-core-go/error-handling.md": """
```mermaid
flowchart TB
  err[root error] --> w1["fmt.Errorf %w"]
  w1 --> w2["fmt.Errorf %w"]
  w2 --> handler[handler]
  handler --> is[errors.Is / As]
```
""",
    "04-concurrency/channels.md": """
```mermaid
sequenceDiagram
  participant S as Sender
  participant B as Buffered chan cap=N
  participant R as Receiver
  S->>B: send until full
  B-->>S: block on full
  R->>B: receive
  B-->>S: unblock send
```
""",
    "03-go-internals/memory-model.md": """
```mermaid
sequenceDiagram
  participant G1 as Goroutine A
  participant Mu as Mutex
  participant G2 as Goroutine B
  G1->>Mu: Lock / Unlock
  Mu->>G2: Lock observes write
  Note over G1,G2: unlock happens-before lock
```
""",
    "03-go-internals/garbage-collection.md": """
```mermaid
flowchart TB
  mut[mutator write] --> wb[write barrier]
  wb --> mark[mark phase]
  mark --> pace[GOGC pacing]
  pace --> sweep[sweep phase]
```
""",
    "06-production-go/observability.md": """
```mermaid
sequenceDiagram
  participant S as Service
  participant OT as OTel SDK
  participant C as Collector
  participant P as Prometheus
  S->>OT: start span
  OT->>C: export trace
  S->>P: scrape metrics
```
""",
    "07-testing/test-strategies.md": """
```mermaid
flowchart TB
  unit[Unit tests] --> integ[Integration tagged]
  integ --> bench[Benchmarks]
  bench --> race[Race / fuzz]
```
""",
}

MERMAID_P2: dict[str, str] = {
    "01-fundamentals/slices.md": """
```mermaid
flowchart LR
  big[large array] --> sub[small subslice]
  sub --> leak[retained backing array]
```
""",
    "04-concurrency/select.md": """
```mermaid
flowchart TD
  ready[multiple cases ready] --> pick[pseudo-random choice]
  pick --> run[execute one case]
  nil[nil channel case] --> skip[never selected]
```
""",
    "04-concurrency/mutex.md": """
```mermaid
sequenceDiagram
  participant G1
  participant G2
  participant Mu as Mutex
  G1->>Mu: Lock
  G2->>Mu: Lock blocks
  G1->>Mu: Unlock
  Mu->>G2: acquire
```
""",
    "05-performance/memory-optimization.md": """
```mermaid
flowchart LR
  bad[bool int64 bool padding] --> good[int64 bool bool]
```
""",
    "03-go-internals/reflection.md": """
```mermaid
flowchart TB
  v[value] --> vo[ValueOf]
  vo --> kind[Kind]
  kind --> field[Field / Set if addressable]
```
""",
    "07-testing/mocking.md": """
```mermaid
flowchart LR
  iface[interface] --> mock[fake / mock]
  mock --> sut[system under test]
```
""",
    "06-production-go/configuration-management.md": """
```mermaid
flowchart TB
  env[environment] --> load[load config]
  file[config file] --> load
  load --> validate[validate struct]
  validate --> app[application]
```
""",
}

FUNDAMENTALS_QUICK_REVISION: dict[str, str] = {
    "01-fundamentals/language-basics.md": """
## Quick Revision

- Go is statically typed, compiled, with garbage collection and CSP-style concurrency.
- **Zero values** are useful defaults; `nil` for references must be checked before use.
- **`defer`** runs LIFO at function return — common for unlock/close.
- **Go 1.22+** fixes per-iteration loop variable capture in `for` loops.
- Type assertions on interfaces: see [Interfaces](/golang-cheatsheet/02-core-go/interfaces/) — max 2 sentences here.

""",
    "01-fundamentals/arrays.md": """
## Quick Revision

- Arrays are **values** (`[N]T`); size is part of the type.
- Prefer **slices** in APIs; arrays appear for crypto keys, fixed buffers, stack arrays.
- Large array parameters **copy** — pass `*[N]T` or slice instead.
- Converting array to slice: `a[:]` — see [Slices](/golang-cheatsheet/01-fundamentals/slices/) for aliasing rules.

""",
    "02-core-go/pointers.md": """
## Quick Revision

- `&` address-of, `*` dereference; no pointer arithmetic.
- `new(T)` allocates zeroed `*T`; `make` only for slice/map/chan.
- Stack vs heap: [Escape Analysis](/golang-cheatsheet/03-go-internals/escape-analysis/).

""",
}


def insert_mermaid_if_missing(rel_path: str, body: str, snippets: dict[str, str]) -> str:
    snippet = snippets.get(rel_path)
    if not snippet or snippet.strip() in body:
        return body
    for heading in ("## Internal Working", "## Reference Tables", "## Core Concepts", "## At a Glance"):
        if heading in body:
            return body.replace(heading, f"{heading}\n{snippet.strip()}\n", 1)
    return body.rstrip() + "\n\n" + snippet.strip() + "\n"


def add_quick_revision(rel_path: str, body: str) -> str:
    block = FUNDAMENTALS_QUICK_REVISION.get(rel_path)
    if not block or "## Quick Revision" in body:
        return body
    if body.startswith("## At a Glance"):
        return block.strip() + "\n\n" + body
    return block.strip() + "\n\n" + body


def refresh_answers_on_pages(topics: list[str], groups) -> int:
    count = 0
    for slug in topics:
        rel = f"{slug}.md"
        path = HB / rel
        if not path.exists():
            continue
        if any(slug.startswith(p) for p in SKIP_ANSWER_PREFIXES):
            continue
        fm, body = strip_front_matter(path.read_text(encoding="utf-8"))
        body = remove_old_answers(body)
        blocks = build_answer_blocks(groups.get(rel, []))
        body = append_answers(body, blocks)
        body = remove_section(body, "See Also")
        body = body.rstrip() + "\n\n---\n\n" + build_see_also(slug, topics)
        path.write_text(fm + "\n\n" + body.lstrip("\n"), encoding="utf-8")
        count += 1
    return count


def apply_fundamentals_and_mermaid(topics: list[str]) -> int:
    count = 0
    for slug in topics:
        rel = f"{slug}.md"
        path = HB / rel
        if not path.exists():
            continue
        if any(slug.startswith(p) for p in SKIP_ANSWER_PREFIXES):
            continue
        fm, body = strip_front_matter(path.read_text(encoding="utf-8"))
        original = body
        body = add_quick_revision(rel, body)
        body = insert_mermaid_if_missing(rel, body, MERMAID_P1)
        body = insert_mermaid_if_missing(rel, body, MERMAID_P2)
        if body != original:
            path.write_text(fm + "\n\n" + body.lstrip("\n"), encoding="utf-8")
            count += 1
    return count


def main() -> None:
    # verify unique answers load
    from golang_top150_unique_answers import UNIQUE_ANSWERS

    assert len(UNIQUE_ANSWERS) == 150

    topics = load_topic_order()
    nav_topics = [
        t for t in topics
        if not t.startswith("08-interview-guide/") and not t.startswith("09-learning-paths/")
    ]
    groups = group_questions_by_page()

    m = apply_fundamentals_and_mermaid(nav_topics)
    n = refresh_answers_on_pages(nav_topics, groups)

    print(
        f"Phase D complete: {m} pages updated with QR/mermaid, "
        f"{n} pages refreshed with unique answers, "
        f"P1={len(MERMAID_P1)} P2={len(MERMAID_P2)} diagrams."
    )


if __name__ == "__main__":
    main()
