"""Build Java Engineering Handbook pages from data/java_engineering_modules.yaml."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import Callable

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "java-engineering"
DATE = "2026-06-30T10:00:00+00:00"

# slug -> (title, shortTitle, description)
TOPIC_META: dict[str, tuple[str, str, str]] = {
    "core-java-quick-ref": (
        "Core Java Quick Reference",
        "Core Java",
        "Primitives, wrappers, control flow, arrays, and varargs — architect one-pager.",
    ),
    "strings-and-enums-ref": (
        "Strings & Enums Reference",
        "Strings & Enums",
        "Immutability, interning, text blocks, StringBuilder vs concat, enum patterns.",
    ),
    "oop-quick-ref": (
        "OOP Quick Reference",
        "OOP",
        "Classes, inheritance, polymorphism, encapsulation, records, sealed types.",
    ),
    "interfaces-and-object-contract": (
        "Interfaces & Object Contract",
        "Object Contract",
        "equals/hashCode/toString, Comparable, default methods, composition over inheritance.",
    ),
    "collections-decision-matrix": (
        "Collections Decision Matrix",
        "Collection Choice",
        "Pick List/Set/Map/Queue by access pattern, ordering, concurrency, and null policy.",
    ),
    "list-set-queue-comparison": (
        "List, Set & Queue Comparison",
        "List/Set/Queue",
        "Implementation trade-offs — ArrayList, HashSet, TreeSet, ArrayDeque, PriorityQueue.",
    ),
    "map-implementations-ref": (
        "Map Implementations Reference",
        "Maps",
        "HashMap, LinkedHashMap, TreeMap, ConcurrentHashMap, WeakHashMap, IdentityHashMap.",
    ),
    "collections-utils-and-ordering": (
        "Collections Utils & Ordering",
        "Utils & Ordering",
        "Collections/Arrays utilities, Comparable vs Comparator, unmodifiable views.",
    ),
    "hashmap-internals": (
        "HashMap Internals",
        "HashMap Internals",
        "Buckets, spread, resize, treeify, load factor, and JDK implementation shifts.",
    ),
    "concurrenthashmap-internals": (
        "ConcurrentHashMap Internals",
        "CHM Internals",
        "Bins, CAS, sizeCtl, compute methods, and iteration semantics under contention.",
    ),
    "exceptions-quick-ref": (
        "Exceptions Quick Reference",
        "Exceptions",
        "Checked vs unchecked, try-with-resources, suppression, and API design rules.",
    ),
    "generics-quick-ref": (
        "Generics Quick Reference",
        "Generics",
        "Type parameters, wildcards, PECS, erasure, and common compiler errors.",
    ),
    "functional-java-ref": (
        "Functional Java Reference",
        "Functional Java",
        "Functional interfaces, lambdas, method references, Optional patterns.",
    ),
    "streams-quick-ref": (
        "Streams Quick Reference",
        "Streams",
        "Lazy pipelines, collectors, primitive streams, parallel pitfalls.",
    ),
    "threads-and-executors": (
        "Threads & Executors",
        "Threads & Executors",
        "Thread lifecycle, pools, ForkJoinPool, shutdown, and task submission models.",
    ),
    "async-completablefuture": (
        "Async & CompletableFuture",
        "CompletableFuture",
        "Composition, async supply/run, exceptionally, orTimeout, and executor choice.",
    ),
    "locks-and-atomics": (
        "Locks & Atomics",
        "Locks & Atomics",
        "synchronized, volatile, ReentrantLock, StampedLock, Atomic* and VarHandle.",
    ),
    "concurrent-coordination": (
        "Concurrent Coordination",
        "Coordination",
        "CountDownLatch, CyclicBarrier, Semaphore, Phaser, Exchanger use cases.",
    ),
    "virtual-threads-structured-concurrency": (
        "Virtual Threads & Structured Concurrency",
        "Virtual Threads",
        "Project Loom carriers, pinning, structured tasks, ScopedValue vs ThreadLocal.",
    ),
    "jvm-memory-and-gc": (
        "JVM Memory & GC",
        "Memory & GC",
        "Heap regions, collectors (G1, ZGC, Shenandoah), allocation, and GC logs.",
    ),
    "memory-leaks-and-oom": (
        "Memory Leaks & OOM",
        "Leaks & OOM",
        "Reference types, common leak patterns, Metaspace, direct memory, diagnosis.",
    ),
    "jvm-internals-quick-ref": (
        "JVM Internals Quick Reference",
        "JVM Internals",
        "Class loaders, JIT tiers, bytecode pipeline, and safepoints.",
    ),
    "jvm-flags-and-tuning": (
        "JVM Flags & Tuning",
        "JVM Flags",
        "Production flag sets for heap, GC, diagnostics, and container awareness.",
    ),
    "java-lts-release-matrix": (
        "Java LTS Release Matrix",
        "LTS Matrix",
        "Java 8/11/17/21/25 support timeline, migration checkpoints, and vendor builds.",
    ),
    "java-recent-features": (
        "Java Recent Features Rollup",
        "Recent Features",
        "Post-17 language and API highlights through current JDK — records to virtual threads.",
    ),
    "java-io-nio-ref": (
        "Java IO & NIO Reference",
        "IO & NIO",
        "Streams vs channels, Path/Files, buffers, selectors, and migration path.",
    ),
    "reflection-annotations-ref": (
        "Reflection & Annotations Reference",
        "Reflection",
        "Core reflection APIs, annotation retention, processors, and module boundaries.",
    ),
    "serialization-quick-ref": (
        "Serialization Quick Reference",
        "Serialization",
        "Serializable contract, serialVersionUID, Externalizable, and safer alternatives.",
    ),
    "collections-complexity": (
        "Collections Complexity (Interview)",
        "Collections Big-O",
        "Big-O cheat sheet for List, Set, Map, Queue — interview one-pager.",
    ),
    "stream-operations-interview": (
        "Stream Operations (Interview)",
        "Streams Interview",
        "Intermediate vs terminal ops, collectors, and parallel stream traps.",
    ),
    "concurrent-collections-interview": (
        "Concurrent Collections (Interview)",
        "Concurrent Collections",
        "CHM vs synchronized wrappers, CopyOnWrite, BlockingQueue family.",
    ),
    "gc-summary-interview": (
        "GC Summary (Interview)",
        "GC Interview",
        "Collector comparison, pause vs throughput, and tuning talking points.",
    ),
    "java-version-features-interview": (
        "Java Version Features (Interview)",
        "Version Features",
        "What shipped in each LTS and recent releases — whiteboard facts.",
    ),
    "memory-diagram-interview": (
        "Memory Diagram (Interview)",
        "Memory Diagram",
        "Stack, heap, metaspace, TLAB, and object layout talking points.",
    ),
    "thread-lifecycle-interview": (
        "Thread Lifecycle (Interview)",
        "Thread Lifecycle",
        "Platform vs virtual thread states, blocking, and executor mapping.",
    ),
}

# slug -> extra related handbook slugs (beyond prev/next)
EXTRA_RELATED: dict[str, list[str]] = {
    "hashmap-internals": ["collections-decision-matrix", "map-implementations-ref", "concurrenthashmap-internals"],
    "concurrenthashmap-internals": ["hashmap-internals", "locks-and-atomics", "concurrent-collections-interview"],
    "streams-quick-ref": ["functional-java-ref", "stream-operations-interview"],
    "jvm-memory-and-gc": ["memory-leaks-and-oom", "gc-summary-interview", "jvm-flags-and-tuning"],
    "java-lts-release-matrix": ["java-recent-features", "java-version-features-interview"],
    "virtual-threads-structured-concurrency": ["threads-and-executors", "async-completablefuture"],
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
        "# Flat topic order — derived from java_engineering_modules.yaml.\n"
        "# Prefer editing data/java_engineering_modules.yaml for module structure.\n"
        "topics:\n"
    )
    path.write_text(header + "".join(f"  - {s}\n" for s in topics), encoding="utf-8")


def interview_block(q: str, a: str) -> str:
    return f"""{{< interview-answer >}}
**Q:** {q}

**A:** {a}
{{< /interview-answer >}}"""


def page_body(
    glance: list[str],
    tables: str,
    snippets: str = "",
    internals: str = "",
    production: str = "",
    interviews: list[tuple[str, str]] | None = None,
    see_also: str = "",
) -> str:
    sections = [
        "## At a Glance",
        "",
        "\n".join(f"- {b}" for b in glance),
        "",
        "---",
        "",
        "## Reference Tables",
        "",
        tables.strip(),
    ]
    if snippets.strip():
        sections.extend(["", "---", "", "## Snippets", "", snippets.strip()])
    sections.extend(["", "---", "", "## Internals & Gotchas", "", internals.strip()])
    sections.extend(["", "---", "", "## Production Notes", "", production.strip()])
    if interviews:
        sections.extend(["", "---", "", "## Interview Probes", ""])
        for q, a in interviews:
            sections.extend(["", interview_block(q, a)])
    sections.extend(["", "---", "", "## See Also", "", see_also.strip()])
    return "\n".join(sections) + "\n"


def see_also_links(slug: str, ordered: list[str]) -> str:
    links: list[str] = []
    idx = ordered.index(slug)
    if idx > 0:
        prev = ordered[idx - 1]
        links.append(f"- [Previous: {TOPIC_META[prev][1]}](/java-engineering/{prev}/)")
    if idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        links.append(f"- [Next: {TOPIC_META[nxt][1]}](/java-engineering/{nxt}/)")
    for rel in EXTRA_RELATED.get(slug, []):
        if rel in TOPIC_META:
            links.append(f"- [{TOPIC_META[rel][1]}](/java-engineering/{rel}/)")
    links.append("- [Java Engineering Handbook Index](/java-engineering/)")
    return "\n".join(links)


def front_matter(slug: str, mod_id: int, mod_title: str, topic_idx: int) -> str:
    title, short, desc = TOPIC_META[slug]
    return f"""---
title: "{title}"
date: {DATE}
draft: false
description: "{desc}"
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{mod_id}.{topic_idx}"
cheatSheet: true
---

"""


def normalize(body: str) -> str:
    body = textwrap.dedent(body)
    body = re.sub(r"\n {8}", "\n", body)
    return body.strip() + "\n"


# --- Topic body builders (filled in below) ---
TOPIC_BUILDERS: dict[str, Callable[[str], str]] = {}


def register(slug: str):
    def decorator(fn: Callable[[str], str]):
        TOPIC_BUILDERS[slug] = fn
        return fn
    return decorator


@register("core-java-quick-ref")
def _core_java(see_also: str) -> str:
    return page_body(
        glance=[
            "Eight primitives + `void`; wrappers box on demand — watch autoboxing in generics/collections.",
            "`final` on reference = binding immutable; object state may still mutate.",
            "Arrays are covariant (`String[]` is `Object[]`); generics are invariant.",
            "Switch: classic + pattern matching (17+) — exhaustiveness required on sealed hierarchies.",
        ],
        tables="""
| Primitive | Size | Default | Wrapper | Notes |
| :--- | :---: | :---: | :--- | :--- |
| `byte` | 8b | 0 | `Byte` | Rare except IO/buffers |
| `short` | 16b | 0 | `Short` | |
| `int` | 32b | 0 | `Integer` | Prefer over `long` unless needed |
| `long` | 64b | 0L | `Long` | Suffix `L` on literals |
| `float` | 32b | 0.0f | `Float` | Avoid for money |
| `double` | 64b | 0.0d | `Double` | Default FP type |
| `char` | 16b UTF-16 | `\\u0000` | `Character` | Not full Unicode code point |
| `boolean` | 1b* | `false` | `Boolean` | *JVM-dependent |

| Control | Gotcha |
| :--- | :--- |
| Enhanced `for` | No index; can't remove during iteration on `List` |
| `switch` on `String` | NPE if selector null (classic switch) |
| `break`/`continue` labels | Rare — prefer extract method |
| Varargs | Last param; overload resolution prefers fixed arity |

```mermaid
flowchart LR
  src[Source .java] --> javac[javac]
  javac --> bytecode[.class bytecode]
  bytecode --> jvm[JVM class loader]
  jvm --> interp[Interpreter / C1 / C2 JIT]
```
""",
        snippets="""
```java
// Prefer primitives in hot loops; avoid Integer in collections if millions of entries
int sum = 0;
for (int i = 0; i < n; i++) sum += values[i];

// Pattern switch (21+) — exhaustiveness on sealed types
switch (shape) {
    case Circle c -> area(c.radius());
    case Rectangle r -> area(r.w(), r.h());
}

// var (10+) — local only, not fields/parameters
var map = Map.of("k", 1);
```
""",
        internals="- Widening conversions are implicit; narrowing requires cast.\n- `==` on wrappers compares references unless unboxed; use `Objects.equals`.\n- `static` init order: static fields → static blocks → instance chain on `new`.\n- `record` components are `final` fields with canonical ctor and generated equals/hashCode.",
        production="- Enable `-Xlint:all` in CI; fix deprecation before LTS upgrades.\n- Avoid `Vector`/`Hashtable`; use `ArrayList` + external sync or concurrent types.\n- Money: `BigDecimal` + `MathContext`, never `double`.",
        interviews=[
            ("Why is `float`/`double` bad for currency?", "`double` is binary FP — decimal fractions like 0.1 are inexact. Use `BigDecimal` with explicit scale/rounding mode."),
            ("Covariant arrays vs invariant generics?", "Arrays carry runtime element type → `ArrayStoreException` at runtime. Generics erase type params — compiler enforces safety; no `new List<String>[10]`."),
        ],
        see_also=see_also,
    )


@register("strings-and-enums-ref")
def _strings_enums(see_also: str) -> str:
    return page_body(
        glance=[
            "`String` is immutable, UTF-16 `char` sequence; Java 21+ also has compact strings / UTF-8 byte backing internally.",
            "Literal pooling: compile-time constants interned; `intern()` costly — avoid in hot paths.",
            "Text blocks (15+) for multiline; `formatted`/`String.format` for templates.",
            "Enums: singleton-like, serializable, can implement interfaces; prefer over int constants.",
        ],
        tables="""
| Operation | API | Complexity / note |
| :--- | :--- | :--- |
| Concat in loop | `StringBuilder` | O(n) total vs O(n²) for `+` in loop |
| Comparison | `equals` / `equalsIgnoreCase` | Never `==` unless interned literal |
| Search | `indexOf`, `contains` | Mind surrogate pairs for emoji |
| Split | `split(regex)` | Trailing empty strings dropped unless limit |
| Join | `String.join`, `Collectors.joining` | Prefer over manual builder for lists |

| Enum pattern | Use when |
| :--- | :--- |
| Simple constants | `enum Status { OPEN, CLOSED }` |
| Fields + ctor | Each constant carries data |
| Strategy enum | `enum Op { PLUS { int apply(int a,int b){...} } }` |
| `EnumSet` / `EnumMap` | Bitset/array-backed — fast, compact |

| Builder | Thread-safe | When |
| :--- | :---: | :--- |
| `StringBuilder` | No | Single-thread concat |
| `StringBuffer` | Yes | Legacy only |
| `String` concat `+` | N/A | OK for few operands; compiler may use builder |
""",
        snippets="""
```java
// Text block + formatted (21+) — multiline string literal in source
String json = String.format("{\\"id\\": %d, \\"name\\": \\"%s\\"}", id, name);

EnumSet<Day> weekend = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
EnumMap<Day, Integer> hours = new EnumMap<>(Day.class);
```
""",
        internals="- `hashCode` caches after first compute (field `hash` in OpenJDK).\n- `substring` (pre-7) copied; modern JDK shares array/compact representation.\n- `enum` values(): clone each call — cache if hot.\n- Switch on enum: compiler synthesizes ordinal map — don't rely on ordinal in persisted data.",
        production="- Log user input with length cap; avoid logging full payloads in prod.\n- Locale: use `toLowerCase(Locale.ROOT)` for identifiers.\n- Persist enums by name (`name()`), never `ordinal()`.",
        interviews=[
            ("`String` immutability — why?", "Thread-safe sharing, safe as map keys, hash caching, security (can't mutate URL/credential strings). Trade-off: many intermediate objects on concat."),
            ("When `EnumSet` over `HashSet<Enum>`?", "`EnumSet` is bit vector — O(1) ops, no boxing, compact. Use for flag sets over enum universe."),
        ],
        see_also=see_also,
    )


@register("oop-quick-ref")
def _oop(see_also: str) -> str:
    return page_body(
        glance=[
            "Composition over inheritance for reuse; inheritance for true subtype polymorphism.",
            "`final` class/method blocks extension; use when invariants must hold.",
            "Records (16+): immutable data carriers; not a drop-in for JPA entities.",
            "Sealed (17+): controlled hierarchy — pairs with exhaustive pattern switches.",
        ],
        tables="""
| Mechanism | Compile-time | Runtime |
| :--- | :--- | :--- |
| Overloading | Resolved by static type + signature | — |
| Overriding | — | Virtual dispatch via vtable/itable |
| Hiding (static) | Resolved statically | No polymorphism |
| `default` interface | — | `invokeinterface` + default method table |

| Type | Fields | Inheritance | Best for |
| :--- | :--- | :--- | :--- |
| `class` | Any | Single extends | Mutable domain objects |
| `record` | `final` components | Implements only | DTOs, value objects |
| `sealed class` | Any | Permitted subs only | Closed ADTs |
| `enum` | Fixed set | `Enum` only | Constants + behavior |
| `interface` | `public static final` | Multiple | Contracts, traits |

| Modifier | Class | Method | Field |
| :--- | :---: | :---: | :---: |
| `public` | ✓ | ✓ | ✓ |
| `protected` | — | ✓ subclass | — |
| package-private | default | default | default |
| `private` | — | ✓ | ✓ |
""",
        snippets="""
```java
public record Point(int x, int y) {
    public Point { if (x < 0 || y < 0) throw new IllegalArgumentException(); }
}

public sealed interface Shape permits Circle, Rectangle {}
public final class Circle implements Shape { /* ... */ }
```
""",
        internals="- Inner classes hold implicit outer ref — leak risk in long-lived callbacks.\n- Static nested: no outer ref — prefer for helpers.\n- `Object` header: mark word + klass pointer (64-bit compressed oops typical).\n- Records: synthetic accessors, canonical ctor, no setters.",
        production="- Don't expose mutable internals — defensive copy on getters.\n- Liskov: subtypes must not strengthen preconditions or weaken postconditions.\n- Avoid deep inheritance trees >2 levels in business code.",
        interviews=[
            ("Record vs class?", "Record = transparent immutable aggregate with generated equals/hashCode/toString. No inheritance except interfaces. Not for entities needing identity lifecycle or lazy fields."),
            ("Sealed types benefit?", "Compiler-checked exhaustiveness in switches; documents allowed subtypes; enables safer domain modeling without visitor boilerplate for every extension."),
        ],
        see_also=see_also,
    )


@register("interfaces-and-object-contract")
def _object_contract(see_also: str) -> str:
    return page_body(
        glance=[
            "`equals`/`hashCode` contract: equal objects → same hash; implement together.",
            "`toString` for logs — never parse; use structured logging.",
            "`Comparable` = natural order; `Comparator` = external/multiple orders.",
            "Default methods: evolve interfaces without breaking implementors.",
        ],
        tables="""
| Method | Contract highlight |
| :--- | :--- |
| `equals(Object)` | Reflexive, symmetric, transitive, consistent; `null` → false |
| `hashCode()` | Must change when fields used in equals change |
| `compareTo` | Consistent with equals if natural ordering is total |
| `clone()` | Shallow by default — prefer copy ctor/factory |

| `equals` implementation checklist | |
| :--- | :--- |
| 1 | `if (this == o) return true` |
| 2 | `if (!(o instanceof Target t)) return false` — pattern match in modern Java |
| 3 | Compare significant fields with `Objects.equals` |
| 4 | Override `hashCode` with same fields |

| Interface evolution | JDK approach |
| :--- | :--- |
| `default` method | Body on interface |
| `static` method | Utility on interface |
| Private method | Shared default helper |
""",
        snippets="""
```java
@Override
public boolean equals(Object o) {
    return o instanceof User u
        && id == u.id
        && Objects.equals(email, u.email);
}

@Override
public int hashCode() {
    return Objects.hash(id, email);
}

Comparator<User> byName = Comparator.comparing(User::name)
    .thenComparingInt(User::id);
```
""",
        internals="- `instanceof` pattern binding avoids double cast.\n- `Comparator` contract: anti-symmetric, transitive; inconsistent with equals OK (e.g. `TreeSet` with comparator not aligned to equals).\n- `identityHashCode` ≠ `hashCode` after override.",
        production="- Use `Objects.equals` / `hash` — handles nulls.\n- For JPA entities: business-key equals or avoid collection membership by entity.\n- Document if class is value vs identity type.",
        interviews=[
            ("Broken equals/hashCode symptom in HashMap?", "Equal keys land in different buckets → duplicates, 'lost' updates. Or mutations after insert break bucket invariant."),
            ("Comparable vs Comparator in TreeSet?", "`TreeSet` uses Comparator if provided; else natural order via Comparable. Comparator inconsistent with equals → set may contain 'duplicate' values per equals."),
        ],
        see_also=see_also,
    )


@register("collections-decision-matrix")
def _coll_matrix(see_also: str) -> str:
    return page_body(
        glance=[
            "Start from access pattern: indexed, keyed, unique, FIFO/LIFO, priority, concurrent.",
            "Ordering costs O(log n) — pay only when you need sorted or predictable iteration.",
            "Null policy differs per implementation — document team convention.",
            "Iteration over hash maps: O(capacity + size) — factor in table load.",
        ],
        tables="""
```mermaid
flowchart TD
  need[Need collection?] --> keyed{Keyed?}
  keyed -->|yes| map[See Map matrix]
  keyed -->|no| unique{Unique elements?}
  unique -->|yes| set[See Set matrix]
  unique -->|no| seq{Indexed access?}
  seq -->|yes| al[ArrayList default]
  seq -->|no| q[Queue/Deque matrix]
```

| Need | Default | Alternatives |
| :--- | :--- | :--- |
| General list | `ArrayList` | `LinkedList` rare |
| Unique unordered | `HashSet` | `LinkedHashSet` for order |
| Unique sorted | `TreeSet` | `ConcurrentSkipListSet` concurrent |
| Key-value | `HashMap` | See map page |
| FIFO queue | `ArrayDeque` | `LinkedBlockingQueue` bounded |
| Priority | `PriorityQueue` | Not thread-safe |
| Concurrent map | `ConcurrentHashMap` | Never `Collections.synchronizedMap` for heavy write |
| LRU cache | `LinkedHashMap` access-order | Caffeine for production |
""",
        snippets="""
```java
// LRU via LinkedHashMap
Map<K,V> lru = new LinkedHashMap<>(16, 0.75f, true) {
    @Override protected boolean removeEldestEntry(Map.Entry<K,V> e) {
        return size() > MAX;
    }
};
```
""",
        internals="- `Arrays.asList` fixed-size — `set` OK, `add` throws.\n- `List.of`/`Map.of` immutable — no nulls.\n- `subList` backed by parent — structural changes invalidate.",
        production="- State average vs worst case for hash structures in design docs.\n- Pre-size maps: `new HashMap<>(expectedSize / 0.75f + 1)`.\n- For read-mostly immutable snapshots: `Map.copyOf`, `List.copyOf`.",
        interviews=[
            ("Choose collection for 10M random reads by index?", "`ArrayList` — O(1) get. `LinkedList` O(n) per access."),
            ("When LinkedHashMap over HashMap?", "Insertion/access-order iteration, LRU caches, predictable debugging. Small memory overhead for links."),
        ],
        see_also=see_also,
    )


@register("list-set-queue-comparison")
def _lsq(see_also: str) -> str:
    return page_body(
        glance=[
            "`ArrayList`: default list — cache-friendly contiguous array.",
            "`LinkedList`: doubly-linked — only for deque ops at both ends without index access.",
            "`HashSet`/`LinkedHashSet`/`TreeSet`: uniqueness with different ordering guarantees.",
            "Stacks: `ArrayDeque` — never `java.util.Stack` (extends Vector).",
        ],
        tables="""
| List op | ArrayList | LinkedList | Vector |
| :--- | :---: | :---: | :---: |
| `get(i)` | **O(1)** | O(n) | **O(1)** |
| `add(end)` | O(1)* | **O(1)** | O(1)* |
| `add(i)` | O(n) | O(n) | O(n) |
| Memory | Low overhead | Node per element | Sync overhead |

| Set op | HashSet | LinkedHashSet | TreeSet |
| :--- | :---: | :---: | :---: |
| `add/contains` | O(1) avg | O(1) avg | O(log n) |
| Iteration order | Undefined | Insertion | Sorted |
| `null` | 1 allowed | 1 allowed | Usually no |

| Deque/Queue | ArrayDeque | PriorityQueue | LinkedBlockingQueue |
| :--- | :---: | :---: | :---: |
| `offer/poll` | O(1) | O(log n) | blocking O(1) avg |
| Thread-safe | No | No | Yes |
| Bounded | No | No | Optional capacity |
""",
        snippets="""
```java
Deque<Task> stack = new ArrayDeque<>();
stack.push(task);
Task t = stack.pop();

Queue<Event> pq = new PriorityQueue<>(Comparator.comparing(Event::severity).reversed());
```
""",
        internals="- `ArrayList` grow ~1.5×; amortized append.\n- `PriorityQueue` is min-heap by natural order or comparator.\n- `TreeSet` backed by `TreeMap` dummy value.",
        production="- Replace `Stack`/`Vector` in legacy code during touch.\n- Large lists: consider primitive lists (Eclipse Collections, fastutil) or columnar storage.",
        interviews=[
            ("ArrayList vs LinkedList myth?", "LinkedList rarely wins on modern JVM — pointer chasing hurts cache; ArrayList wins except niche deque with no index."),
            ("PriorityQueue iterator order?", "Not sorted — only `poll` returns head. To sorted list: drain to array and sort or use stream."),
        ],
        see_also=see_also,
    )


@register("map-implementations-ref")
def _maps(see_also: str) -> str:
    return page_body(
        glance=[
            "`HashMap`: default single-threaded map.",
            "`LinkedHashMap`: insertion or access order — LRU pattern.",
            "`TreeMap`: `NavigableMap`, range views, `floor`/`ceiling` keys.",
            "`ConcurrentHashMap`: concurrent reads/writes; no null keys/values.",
        ],
        tables="""
| Map | Null key | Null value | Thread-safe | Ordered |
| :--- | :---: | :---: | :---: | :--- |
| HashMap | 1 | many | No | No |
| LinkedHashMap | 1 | many | No | Insertion/access |
| TreeMap | No | Yes | No | Sorted |
| ConcurrentHashMap | No | No | Yes | No |
| WeakHashMap | Yes | Yes | No | No |
| IdentityHashMap | Yes | Yes | No | Identity |

| Use case | Map |
| :--- | :--- |
| General | `HashMap` |
| Config / ordered props | `LinkedHashMap` |
| Schedulers / timelines | `TreeMap` |
| Shared cache index | `ConcurrentHashMap` |
| Listener registry (GC keys) | `WeakHashMap` |
| Serialization identity | `IdentityHashMap` |

| `NavigableMap` ops | Purpose |
| :--- | :--- |
| `subMap`, `headMap`, `tailMap` | Range without copy |
| `floorKey`, `ceilingKey` | Neighbor search |
| `descendingMap` | Reverse view |
""",
        snippets="""
```java
ConcurrentHashMap<String, AtomicInteger> counts = new ConcurrentHashMap<>();
counts.computeIfAbsent(key, k -> new AtomicInteger()).incrementAndGet();

NavigableMap<Instant, Event> timeline = new TreeMap<>();
Event e = timeline.floorEntry(t).getValue();
```
""",
        internals="- `TreeMap` Red-Black tree; comparator must be consistent with equals if used as `Set` keys.\n- `WeakHashMap` entries expire when key only weakly reachable — values may linger until next access.\n- `EnumMap` array-backed — fastest for enum keys.",
        production="- `ConcurrentHashMap.size()` may be approximate under contention (JDK-dependent).\n- Don't use `HashTable`/`Hashtable` — legacy synchronized entire map.\n- For high-performance caches: Caffeine/Guava with eviction stats.",
        interviews=[
            ("CHM vs `Collections.synchronizedMap`?", "CHM lock-striping/CAS — finer granularity. synchronizedMap locks whole map per op — poor write scalability."),
            ("TreeMap when worth O(log n)?", "Sorted keys, range queries, navigable ops. Not for pure get/put hot paths."),
        ],
        see_also=see_also,
    )


@register("collections-utils-and-ordering")
def _coll_utils(see_also: str) -> str:
    return page_body(
        glance=[
            "`Collections` — algorithms, wrappers, empty/singleton, synchronized views.",
            "`Arrays` — sort, binarySearch, parallel prefix, stream bridge.",
            "`Comparable` natural order vs `Comparator` pluggable order.",
            "Unmodifiable wrappers throw on mutation — not immutable copies.",
        ],
        tables="""
| `Collections` | Note |
| :--- | :--- |
| `sort`, `reverse`, `shuffle` | In-place on `List` |
| `unmodifiableList/Map/Set` | Wrapper — delegate still mutable |
| `synchronizedList` | Every method locked — prefer concurrent types |
| `checkedList` | Runtime type check on add |
| `emptyList`, `singleton` | Shared instances |

| `Arrays` | Complexity |
| :--- | :--- |
| `sort` (primitives) | Dual-Pivot quicksort O(n log n) |
| `binarySearch` | Requires sorted O(log n) |
| `parallelSort` | ForkJoin for large arrays |
| `mismatch` | First differing index |

| Ordering | When |
| :--- | :--- |
| `Comparable` | Single natural order baked into type |
| `Comparator.comparing` | Field-based, composable, reversed |
| `Comparator.nullsFirst/Last` | Explicit null policy |
""",
        snippets="""
```java
List<String> ro = List.copyOf(mutable); // truly immutable snapshot
Comparator<Person> byAgeThenName = Comparator
    .comparingInt(Person::age)
    .thenComparing(Person::name, String.CASE_INSENSITIVE_ORDER);
```
""",
        internals="- `List.copyOf`/`Map.copyOf` (10+) — compact immutable; reject nulls.\n- `Collections.sort` uses TimSort for objects — stable O(n log n).\n- Binary search: `-(insertionPoint) - 1` on miss.",
        production="- Never expose internal mutable list — return `List.copyOf` or unmodifiable wrapper with documented mutability.\n- Stable sort matters for paginated UI — TimSort is stable.",
        interviews=[
            ("unmodifiable vs immutable?", "Unmodifiable view: backing collection can still change. `List.of`/`copyOf` cannot be structurally modified."),
            ("PECS in comparators?", "Comparators are contravariant on type for sorting mixed subtypes — usually sort `List<Employee>` with `Comparator<Employee>`, not wildcards."),
        ],
        see_also=see_also,
    )


@register("hashmap-internals")
def _hm_internals(see_also: str) -> str:
    return page_body(
        glance=[
            "Array of bins; index = `(n-1) & hash` after spread (`hash ^ hash>>>16`).",
            "Load factor 0.75 — resize 2× when `size > threshold`.",
            "Bin length ≥8 and treeify threshold → red-black tree per bin (Java 8+).",
            "JDK 8+ linked list bins; treeify on collision depth.",
        ],
        tables="""
| Constant | Typical value | Meaning |
| :--- | :---: | :--- |
| Default capacity | 16 | Power of 2 |
| Load factor | 0.75 | Space/time trade-off |
| Treeify threshold | 8 | List → tree in bin |
| Untreeify threshold | 6 | Tree → list when shrink |

| Operation | Average | Worst (attacks/poor hash) |
| :--- | :---: | :---: |
| `get` | O(1) | O(log n) treeified / O(n) list |
| `put` | O(1) | Same |
| `resize` | O(n) | Rehash all entries |

```mermaid
flowchart LR
  key[Key] --> hc[hashCode spread]
  hc --> idx[bin index]
  idx --> bin{bin type}
  bin --> list[Linked list]
  bin --> tree[RB tree if deep]
```
""",
        snippets="""
```java
// Bad: mutable key field used in hashCode
class BadKey {
    String id;
    public int hashCode() { return id.hashCode(); } // id mutated after insert breaks map
}

// Good: immutable key fields
record UserKey(String tenant, long id) {}
```
""",
        internals="- Resize creates new table — reinsert all entries — STW for caller thread only on that map instance.\n- `HashMap` iterator is fail-fast on concurrent structural mod.\n- `LinkedHashMap` hooks `afterInsertion`/`afterAccess` for LRU.\n- JDK 17+: minor optimizations; algorithm unchanged conceptually.",
        production="{{% warning %}}\nDo not use user-controlled keys with weak `hashCode` — collision DoS risk; consider limiting map size or using `LinkedHashMap` + eviction.\n{{% /warning %}}\n- Pre-size expected entries.\n- Never mutate keys while in map.",
        interviews=[
            ("Why power-of-two capacity?", "Bit mask `(n-1) & hash` is fast modulo; requires good spread function to avoid index clustering."),
            ("When treeify?", "When single bin chain length exceeds threshold — degrades to tree to bound worst case O(log n) per bin."),
        ],
        see_also=see_also,
    )


@register("concurrenthashmap-internals")
def _chm_internals(see_also: str) -> str:
    return page_body(
        glance=[
            "No global lock — per-bin synchronization / CAS on Java 8+.",
            "`sizeCtl` coordinates initialization and resize.",
            "`compute*` methods atomic at key level — prefer over get+put.",
            "Weakly consistent iterators — reflect some concurrent updates.",
        ],
        tables="""
| Era | Mechanism |
| :--- | :--- |
| Java 7 | Segment locks (16 default) |
| Java 8+ | Node array like HashMap + synchronized bin head / CAS + tree bins |
| Resize | Multi-thread assisted transfer |

| Method | Atomicity |
| :--- | :--- |
| `putIfAbsent` | Key-level |
| `compute` | Read-modify-write atomic |
| `merge` | Atomic combine |
| `replace(K,V,V)` | Compare-and-swap value |

| vs `Hashtable` | CHM |
| :--- | :--- |
| Lock scope | Whole table | Bin-level |
| Null | Allowed | Forbidden |
| Iterators | Enumerator fail-fast | Weakly consistent |
""",
        snippets="""
```java
chm.compute(key, (k, v) -> v == null ? 1 : v + 1);
chm.merge(key, 1, Integer::sum);

// Avoid
Integer v = chm.get(k);
chm.put(k, v + 1); // race
```
""",
        internals="- `CounterCell` striping for `size()` approximation under contention.\n- Forwarding nodes during resize — `helpTransfer` lets other threads assist.\n- `ConcurrentHashMap.keySet()` view operations may be weaker than `ConcurrentSkipListSet` for ordered needs.",
        production="- Use `compute`/`merge` for counters — not `get`+`put`.\n- Bulk `forEach` parallel threshold — rarely needed; measure first.\n- No null keys/values — use sentinel `Optional`-like marker objects if needed.",
        interviews=[
            ("CHM size() accuracy?", "May be approximate under heavy concurrent updates — documented behavior; don't use as strict invariant check without external sync."),
            ("Why forbid null in CHM?", "Ambiguity: `get` returns null for missing vs null value — Doug Lea design avoids double-meaning in concurrent context."),
        ],
        see_also=see_also,
    )


@register("exceptions-quick-ref")
def _exceptions(see_also: str) -> str:
    return page_body(
        glance=[
            "Checked: must handle or declare — `IOException`, `SQLException`.",
            "Unchecked: `RuntimeException` — programming bugs, optional handling.",
            "`Error`: serious JVM issues — generally don't catch.",
            "try-with-resources (7+): auto-close `AutoCloseable` in LIFO order.",
        ],
        tables="""
| Type | Examples | Handle? |
| :--- | :--- | :--- |
| Checked | `IOException` | Compile-time |
| Unchecked | `IllegalArgumentException` | Optional |
| Error | `OutOfMemoryError` | Usually propagate |
| `Throwable` | Root | Catch only at boundary |

| Pattern | Use |
| :--- | :--- |
| Fail fast | Validate early, throw unchecked |
| Wrap + cause | `new ServiceException(\"msg\", e)` preserve stack |
| Suppressed | try-with-resources multiple close failures |
| Multi-catch | `catch (IOException | SQLException e)` |

| Anti-pattern | Fix |
| :--- | :--- |
| Swallow empty catch | Log or rethrow |
| Catch `Exception` everywhere | Catch specific at low level |
| Control flow via exceptions | Use return codes/Optional |
""",
        snippets="""
```java
try (var in = Files.newInputStream(path);
     var out = Files.newOutputStream(target)) {
    in.transferTo(out);
} catch (IOException e) {
    throw new UncheckedIOException(e);
}
```
""",
        internals="- Exception creation captures stack trace — expensive in hot path.\n- `fillInStackTrace` can be overridden for lightweight exceptions (rare).\n- `addSuppressed` links close exceptions from TWR.",
        production="- Global handler at service boundary maps to HTTP/gRPC codes.\n- Never log and swallow security/auth failures.\n- Use domain unchecked exceptions for invariant violations.",
        interviews=[
            ("Checked exceptions controversy?", "Forces handling but encourages empty catches and wrapping layers. Modern APIs (Spring, NIO streams) lean unchecked + wrap."),
            ("try-with-resources order?", "Resources closed reverse declaration order; primary exception wins, others suppressed."),
        ],
        see_also=see_also,
    )


@register("generics-quick-ref")
def _generics(see_also: str) -> str:
    return page_body(
        glance=[
            "Compile-time type safety; erased at runtime — no `new T()`.",
            "PECS: Producer `extends`, Consumer `super`.",
            "Wildcards more flexible than type params at API boundaries.",
            "Type erasure → bridge methods, heap pollution warnings.",
        ],
        tables="""
| Syntax | Meaning |
| :--- | :--- |
| `<T>` | Type parameter |
| `<? extends T>` | Upper bounded wildcard (producer) |
| `<? super T>` | Lower bounded wildcard (consumer) |
| `<T extends Comparable<T>>` | F-bounded |

| PECS | Role | Wildcard |
| :--- | :--- | :--- |
| Producer (read) | `Collection<? extends T>` | `extends` |
| Consumer (write) | `Collection<? super T>` | `super` |

| Limitation | Workaround |
| :--- | :--- |
| `new T()` | Factory/Supplier |
| `T[]` array | `ArrayList` or `(T[]) Object[]` with care |
| `instanceof T` | `Class<T>` token |
| Primitive generics | IntStream, specialized libs |
""",
        snippets="""
```java
// PECS copy
void copy(List<? extends Number> src, List<? super Number> dest) {
    for (Number n : src) dest.add(n);
}

public <T> T requireNonNull(T ref, String msg) { /* ... */ }
```
""",
        internals="- Erasure replaces type vars with bounds or Object.\n- Bridge methods preserve polymorphism after erasure.\n- Reifiable types: primitives, raw classes, arrays of reifiable, wildcards with `?` only.",
        production="- Avoid raw types in new code — `-Xlint:unchecked`.\n- API returns `List<T>` not `List` — callers stay typed.\n- For JSON: type tokens (`TypeReference`) with Jackson/Gson.",
        interviews=[
            ("Why can't `if (obj instanceof List<String>)`?", "Generics erasure — runtime only knows `List`. Use `List.class` and cast with validation or pattern `List<?>`."),
            ("PECS example?", "`Collections.sort(List<T>)` takes `List<T>`; `addAll(Collection<? extends T>)` producer read; `addAll(Collection<? super T>)` consumer write in `copy` helpers."),
        ],
        see_also=see_also,
    )


@register("functional-java-ref")
def _functional(see_also: str) -> str:
    return page_body(
        glance=[
            "`@FunctionalInterface` — one abstract method (SAM); Object methods don't count.",
            "Lambdas: syntactic sugar for anonymous SAM instances — capture must be effectively final.",
            "Method references: `Type::static`, `instance::method`, `Type::new`.",
            "`Optional` — return type for absent values; never fields/parameters/collections.",
        ],
        tables="""
| Interface | Method | Typical use |
| :--- | :--- | :--- |
| `Supplier<T>` | `get` | Lazy factory |
| `Consumer<T>` | `accept` | Side effect |
| `Predicate<T>` | `test` | Filter |
| `Function<T,R>` | `apply` | Map |
| `UnaryOperator<T>` | `apply` | Same-type map |
| `BiFunction<T,U,R>` | `apply` | Combine |

| Lambda form | Example |
| :--- | :--- |
| No params | `() -> System.nanoTime()` |
| One param | `x -> x * 2` |
| Block body | `(a, b) -> { validate(a); return a + b; }` |

| Method ref | Equivalent lambda |
| :--- | :--- |
| `String::valueOf` | `x -> String.valueOf(x)` |
| `list::add` | `x -> list.add(x)` |
| `ArrayList::new` | `() -> new ArrayList<>()` |

| Optional anti-use | Prefer |
| :--- | :--- |
| `Optional` field | Nullable or empty object |
| `Optional` parameter | Overloads |
| `get()` without check | `orElseThrow`, `orElse` |
""",
        snippets="""
```java
Function<String, Integer> len = String::length;
Predicate<User> active = u -> u.status() == Status.ACTIVE;

Optional<User> user = repo.findById(id);
return user.map(User::email).orElseThrow(() -> new NotFoundException(id));
```
""",
        internals="- Lambdas may be invokedynamic + LambdaMetafactory — not always inner classes.\n- Serialization of lambdas uses `SerializedLambda` — fragile across versions.\n- `Optional` is `final` with private ctor — not for JSON null mapping by default.",
        production="- Keep lambdas short; extract named methods when >3 lines.\n- Don't parallelize streams solely because lambdas exist.\n- Use `Objects.requireNonNull` in factories, not Optional for required params.",
        interviews=[
            ("Effectively final — why?", "Captured locals must not change — JVM needs stable closure snapshot without synchronized mutable cell."),
            ("Optional in API design?", "Good for return types signaling absence. Bad as field (serializable pain) or param (overload clearer)."),
        ],
        see_also=see_also,
    )


@register("streams-quick-ref")
def _streams(see_also: str) -> str:
    return page_body(
        glance=[
            "Lazy intermediate ops; single terminal op triggers pipeline.",
            "Streams don't store data — source must not be modified during pipeline (except concurrent sources).",
            "Primitive streams (`IntStream`) avoid boxing overhead.",
            "Parallel streams use `ForkJoinPool.commonPool()` — default parallelism = CPUs-1.",
        ],
        tables="""
| Stage | Examples | Notes |
| :--- | :--- | :--- |
| Source | `collection.stream()`, `Stream.of`, `Files.lines` | Close resource streams |
| Intermediate | `filter`, `map`, `flatMap`, `distinct`, `sorted`, `peek` | Lazy, chained |
| Terminal | `collect`, `reduce`, `forEach`, `count`, `findFirst` | Triggers execution |

| Collector | Result |
| :--- | :--- |
| `toList()` (16+) | Mutable list |
| `toUnmodifiableList()` | Immutable |
| `toMap` | Merge function required on duplicate keys |
| `groupingBy` | `Map<K, List<T>>` |
| `partitioningBy` | `Map<Boolean, List<T>>` |

| Pitfall | Issue |
| :--- | :--- |
| `sorted()` on large data | Materializes — O(n log n) memory |
| `parallel()` + ordered op | May lose order benefit |
| Side effects in `forEach` | Race unless concurrent collection |
| `Stream` reuse | Illegal — one terminal only |
""",
        snippets="""
```java
Map<Department, Long> headcount = employees.stream()
    .filter(e -> e.active())
    .collect(Collectors.groupingBy(Employee::dept, Collectors.counting()));

long sum = invoices.stream().mapToInt(Invoice::amountCents).sum();
```
""",
        internals="- Spliterator characteristics: `SIZED`, `ORDERED`, `DISTINCT` enable optimizations.\n- `flatMap` one-to-many; `map` one-to-one.\n- Short-circuit: `findFirst`, `anyMatch` stop early.",
        production="{{% tip %}}\nPrefer `toList()` over `collect(Collectors.toList())` on Java 16+.\n{{% /tip %}}\n- Don't use parallel on small collections (<10k) or IO-bound tasks.\n- Close `Files.lines` with try-with-resources.",
        interviews=[
            ("Why lazy?", "Fuse operations; skip work for short-circuit; avoid intermediate collections when chained."),
            ("parallel stream when?", "Large in-memory CPU-bound transforms with no shared mutable state and spliterator splits well. Not for IO or small lists."),
        ],
        see_also=see_also,
    )


@register("threads-and-executors")
def _threads(see_also: str) -> str:
    return page_body(
        glance=[
            "Platform thread = OS thread; expensive (~1MB stack default).",
            "Prefer `ExecutorService` over raw `new Thread()` for pool lifecycle.",
            "`shutdown()` vs `shutdownNow()` — graceful vs interrupt workers.",
            "Uncaught exception handler per thread or `ThreadFactory`.",
        ],
        tables="""
| State | Meaning |
| :--- | :--- |
| NEW | Created, not started |
| RUNNABLE | Eligible to run |
| BLOCKED/WAITING/TIMED_WAITING | Parked on lock/condition/sleep |
| TERMINATED | `run` completed |

| Executor | When |
| :--- | :--- |
| `newFixedThreadPool(n)` | Bounded workers, unbounded queue |
| `newCachedThreadPool` | Short-lived bursty tasks — unbounded growth risk |
| `newSingleThreadExecutor` | Sequential tasks, ordered |
| `ForkJoinPool` | Divide-and-conquer, parallel streams |
| `Executors.newVirtualThreadPerTaskExecutor` (21+) | Massive blocking IO |

| Shutdown | Behavior |
| :--- | :--- |
| `shutdown` | No new tasks; finish queued |
| `shutdownNow` | Interrupt workers, return pending |
| `awaitTermination` | Block with timeout |
""",
        snippets="""
```java
ExecutorService pool = Executors.newFixedThreadPool(8);
Future<Result> f = pool.submit(() -> compute());
try {
    Result r = f.get(5, TimeUnit.SECONDS);
} finally {
    pool.shutdown();
    pool.awaitTermination(30, TimeUnit.SECONDS);
}
```
""",
        internals="- `Thread.start` happens-before `run` body.\n- `volatile`/`synchronized` establish visibility across threads.\n- Pool queue unbounded → OOM under sustained overload.",
        production="- Name threads via custom `ThreadFactory` for diagnostics.\n- Set pool sizes from metrics — not `Runtime.getRuntime().availableProcessors()` alone for mixed workloads.\n- Always shutdown pools on app stop.",
        interviews=[
            ("Fixed pool sizing?", "CPU-bound ≈ cores; blocking IO ≈ higher or virtual threads; measure queue depth and latency."),
            ("Difference interrupt vs shutdownNow?", "`shutdownNow` interrupts running tasks; cooperative cancellation required in task loop."),
        ],
        see_also=see_also,
    )


@register("async-completablefuture")
def _cf(see_also: str) -> str:
    return page_body(
        glance=[
            "Composable async pipeline — `thenApply`, `thenCompose`, `allOf`, `anyOf`.",
            "Always pass explicit `Executor` for application work — don't rely on `ForkJoinPool.commonPool()` in services.",
            "`orTimeout` / `completeOnTimeout` (9+) for SLA bounds.",
            "Exception handling: `handle`, `exceptionally`, `whenComplete`.",
        ],
        tables="""
| Method | Use |
| :--- | :--- |
| `supplyAsync` | Async value |
| `runAsync` | Async void |
| `thenApply` | Map result sync |
| `thenCompose` | FlatMap future |
| `thenCombine` | Merge two futures |
| `allOf` | Wait all — void aggregate |
| `anyOf` | First complete wins |

| Composition trap | Fix |
| :--- | :--- |
| Nested `get()` | `thenCompose` chain |
| Blocking on common pool | Dedicated executor |
| Lost exception | `handle` / `whenComplete` log |
| No timeout | `orTimeout`, `completeOnTimeout` |
""",
        snippets="""
```java
CompletableFuture<Order> order = validate(cart)
    .thenCompose(v -> reserveInventory(cart))
    .thenCompose(v -> chargePayment(cart))
    .orTimeout(10, TimeUnit.SECONDS);

order.whenComplete((o, ex) -> { if (ex != null) audit.fail(ex); });
```
""",
        internals="- `CompletableFuture` stored in `AltResult` for completion — CAS completion stack.\n- `async` stages run on executor; non-async run on completing thread.",
        production="- Propagate tracing context manually or via OpenTelemetry context wrappers.\n- Bulkhead: separate executors per dependency.\n- Don't block in `thenApply` on event loop threads.",
        interviews=[
            ("thenApply vs thenCompose?", "`thenApply` maps value to value; `thenCompose` maps value to another Future — avoids nested futures."),
            ("Default executor risk?", "Common pool shared with parallel streams — starvation/cross-talk. Use named executor per domain."),
        ],
        see_also=see_also,
    )


@register("locks-and-atomics")
def _locks(see_also: str) -> str:
    return page_body(
        glance=[
            "`synchronized` — intrinsic lock on object/monitor.",
            "`volatile` — visibility + ordering, not atomic compound ops.",
            "`ReentrantLock` — tryLock, fairness, interruptible lock.",
            "`java.util.concurrent.atomic.*` — CAS primitives for counters/flags.",
        ],
        tables="""
| Mechanism | Scope | Best for |
| :--- | :--- | :--- |
| `synchronized` | Block/method | Simple mutual exclusion |
| `volatile` | Field | Single-writer flags, DCL idiom (with care) |
| `ReentrantLock` | Explicit | tryLock, timeouts, conditions |
| `ReadWriteLock` | Read-heavy | Many readers, rare writers |
| `StampedLock` | Optimistic read | Read-mostly with validation |
| `AtomicInteger` etc. | Single variable | Counters, sequence |

| `happens-before` edge | |
| :--- | :--- |
| Monitor unlock → lock | `synchronized` |
| `volatile` write → read | Visibility |
| `Thread.start` | Start of thread |
| `Concurrent` utils | Documented per class |

| Deadlock needs | Prevention |
| :--- | :--- |
| Circular wait | Lock ordering |
| Hold and wait | tryLock with backoff |
| | Timed locks |
""",
        snippets="""
```java
private final AtomicLong seq = new AtomicLong();
long next = seq.incrementAndGet();

lock.lock();
try {
    // critical section
} finally {
    lock.unlock();
}
```
""",
        internals="- `synchronized` biased locking (historically) — JVM elides uncontended locks until revocation.\n- `VarHandle` (9+) — low-level fences on fields/arrays.\n- False sharing: pad hot counters or use `@Contended` (JVM flag).",
        production="- Prefer higher-level `ConcurrentHashMap`, `LongAdder` over raw locks when fits.\n- Always `unlock` in `finally`.\n- Avoid `synchronized` on Strings/literals/boxed Integers — intern collisions.",
        interviews=[
            ("volatile enough for i++?", "No — read-modify-write not atomic. Use `AtomicInteger` or synchronization."),
            ("ReentrantLock vs synchronized?", "Lock: tryLock, fairness, multiple Conditions. synchronized: simpler, JVM optimized, blocks in thread dump clearly."),
        ],
        see_also=see_also,
    )


@register("concurrent-coordination")
def _coordination(see_also: str) -> str:
    return page_body(
        glance=[
            "Coordination primitives — not data structures.",
            "`CountDownLatch` — one-shot wait for N events.",
            "`CyclicBarrier` — reusable rendezvous; optional barrier action.",
            "`Semaphore` — permit pool; not mutual exclusion unless 1 permit.",
        ],
        tables="""
| Class | Reusable | Typical pattern |
| :--- | :---: | :--- |
| `CountDownLatch` | No | Start gun / await startup |
| `CyclicBarrier` | Yes | Parallel phases |
| `Semaphore` | Yes | Limit concurrency |
| `Phaser` | Yes | Dynamic party count |
| `Exchanger` | Yes | Pair swap buffer |

| vs `join()` | Coordination primitive |
| :--- | :--- |
| Thread join | One thread completion |
| Latch | Many events, any thread counts down |
| Barrier | Threads meet at phase gate |

| `Phaser` advantage | |
| :--- | :--- |
| Dynamic register/deregister | Flexible fork/join workflows |
| Tiered phases | Multi-stage pipelines |
""",
        snippets="""
```java
var start = new CountDownLatch(1);
var done = new CountDownLatch(workerCount);
for (int i = 0; i < workerCount; i++) {
    pool.execute(() -> {
        start.await();
        try { work(); } finally { done.countDown(); }
    });
}
start.countDown();
done.await();
```
""",
        internals="- Await parks thread (platform) — virtual threads unmount carrier.\n- Barrier broken if thread interrupted/timeout — reset or new instance.\n- Semaphore fairness flag reduces throughput.",
        production="- Prefer structured concurrency (21+) over manual latch/barrier wiring where possible.\n- Always handle `InterruptedException` — restore interrupt flag.\n- Time-bound waits in prod: `await(timeout, unit)`.",
        interviews=[
            ("Latch vs Barrier?", "Latch: one or more threads wait for count to zero (one-shot). Barrier: N threads wait for each other at point, reusable."),
            ("Semaphore vs fixed pool?", "Semaphore limits concurrent access to resource; thread pool limits threads executing tasks — related but different layer."),
        ],
        see_also=see_also,
    )


@register("virtual-threads-structured-concurrency")
def _vt(see_also: str) -> str:
    return page_body(
        glance=[
            "Virtual threads (21+): cheap — mount/unmount on carrier platform threads.",
            "Ideal for blocking IO — not CPU-bound parallel work.",
            "Pinning: synchronized/native/blocking on carrier — avoid synchronized in hot VT paths or use `ReentrantLock`.",
            "Structured concurrency (preview/incubator): parent scope owns child lifetimes.",
        ],
        tables="""
| Workload | Platform threads | Virtual threads |
| :--- | :--- | :--- |
| Blocking HTTP/DB | Few thousand max | Millions feasible |
| CPU compute | Preferred | Wrong tool |
| Thread-local heavy | OK | Prefer `ScopedValue` |

| Pinning cause | Mitigation |
| :--- | :--- |
| `synchronized` in VT block | `ReentrantLock` |
| Native JNI blocking | Minimize |
| Carrier pool exhaustion | Monitor pinned count (JFR) |

| API (21+) | Purpose |
| :--- | :--- |
| `Thread.startVirtualThread` | Fire-and-forget |
| `Executors.newVirtualThreadPerTaskExecutor` | Per-task VT |
| `StructuredTaskScope` (preview) | Cancel siblings on failure |

```mermaid
flowchart LR
  vt1[Virtual Thread] --> carrier[Carrier Platform Thread]
  vt2[Virtual Thread] --> carrier
  vt3[Virtual Thread] --> carrier
```
""",
        snippets="""
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    List<Future<String>> futures = urls.stream()
        .map(url -> executor.submit(() -> fetch(url)))
        .toList();
}
```
""",
        internals="- Continuation yield on blocking IO — carrier free for other VTs.\n- `ThreadLocal` on millions of VTs — memory blowup; `ScopedValue` (preview) for implicit context.\n- `ForkJoinPool` not used for VT scheduling — separate scheduler.",
        production="- Enable JFR `jdk.VirtualThreadPinned` events in staging.\n- Size connection pools for expected concurrent blocking calls, not thread count.\n- Don't pool virtual threads — create per task.",
        interviews=[
            ("VT vs reactive (WebFlux)?", "VT: blocking style code, simpler migration. Reactive: backpressure native, steeper model. VT needs pool sizing for downstream."),
            ("What is pinning?", "VT stuck on carrier during native/sync block — reduces scalability; monitor and refactor locks."),
        ],
        see_also=see_also,
    )


@register("jvm-memory-and-gc")
def _memory_gc(see_also: str) -> str:
    return page_body(
        glance=[
            "Heap: young (Eden + Survivors) + old gen; all Java objects (except off-heap/direct).",
            "Non-heap: Metaspace (class metadata), CodeCache, thread stacks, direct buffers.",
            "Default collector (17+ server): G1; low-latency options: ZGC, Shenandoah.",
            "GC logs: unified `-Xlog:gc*` (9+).",
        ],
        tables="""
| Region | Holds | GC event |
| :--- | :--- | :--- |
| Eden | New objects | Minor GC |
| Survivor | Copied young | Minor GC |
| Old | Tenured | Major / mixed |
| Metaspace | Class metadata | Metaspace GC trigger |

| Collector | Pause goal | Heap scale |
| :--- | :--- | :--- |
| G1 | Configurable target | General purpose |
| ZGC | Sub-ms typical | Large heaps |
| Shenandoah | Concurrent compact | Large heaps |
| Parallel | Throughput | Batch |

| Flag (11+) | Effect |
| :--- | :--- |
| `-XX:+UseG1GC` | G1 (often default) |
| `-XX:MaxGCPauseMillis` | G1 pause target |
| `-XX:+UseZGC` | ZGC |
| `-Xlog:gc*:file=gc.log:time,uptime,level,tags` | Logging |
""",
        snippets="""
```bash
# Container-aware heap (10+)
java -XX:MaxRAMPercentage=75.0 -XX:+UseG1GC -jar app.jar
```
""",
        internals="- TLAB: per-thread Eden allocation buffer — reduces CAS contention.\n- Card table / remembered set for cross-gen references.\n- Humongous objects (G1): >50% region size → special handling.",
        production="- Set heap max in containers — never rely on default ergonomics alone.\n- Tune after metrics: GC pause P99, allocation rate, promotion failure.\n- `-XX:+HeapDumpOnOutOfMemoryError` with path on persistent volume.",
        interviews=[
            ("Minor vs major GC?", "Minor: young gen collection, frequent, stop-the-world usually short. Major/old: tenured collection — longer pauses unless mostly concurrent collector."),
            ("When ZGC over G1?", "Very large heaps, strict pause SLAs, willing to trade some CPU. Measure — not default for all services."),
        ],
        see_also=see_also,
    )


@register("memory-leaks-and-oom")
def _leaks(see_also: str) -> str:
    return page_body(
        glance=[
            "Java leak = reachable but unused objects — GC cannot reclaim.",
            "Common: static collections, listeners, ThreadLocal, classloader leaks in containers.",
            "OOM types: heap, Metaspace, direct memory, unable to create native thread.",
            "Diagnose: heap dump, MAT/VisualVM, async profiler, JFR.",
        ],
        tables="""
| Reference | GC behavior | Use |
| :--- | :--- | :--- |
| Strong | Never if reachable | Default |
| Soft | Cleared before OOM | Memory-sensitive cache |
| Weak | Next GC | Canonical mappings |
| Phantom | After finalize/enqueue | Post-mortem cleanup |

| Leak pattern | Fix |
| :--- | :--- |
| Static `Map` cache no eviction | Bounded cache + TTL |
| Listener not removed | Weak refs or explicit remove |
| `ThreadLocal` in pool threads | `remove()` in finally |
| Reloaded WAR classloader | Undeploy hook, avoid static refs to app classes |

| OOM message | Likely cause |
| :--- | :--- |
| Java heap space | Object retention |
| Metaspace | Class explosion / reload |
| Direct buffer memory | NIO leak |
| unable to create native thread | Thread spawn storm |
""",
        snippets="""
```java
try {
    threadLocal.set(ctx);
    process();
} finally {
    threadLocal.remove(); // critical in pooled threads
}
```
""",
        internals="- Finalization deprecated (9+) — prefer `Cleaner`/`PhantomReference`.\n- `String` deduplication (G1 option) saves heap for duplicate char arrays.\n- Off-heap leaks won't trigger heap GC — monitor `BufferPoolMXBean`.",
        production="- Cap caches; expose size metrics.\n- Automate heap dump on OOM in prod (with disk guard).\n- Review reactive/Netty direct buffer allocators.",
        interviews=[
            ("Can you leak memory with GC?", "Yes — logical leaks keep strong references (static, singleton registries, class loaders)."),
            ("Soft vs weak cache?", "Soft survives until memory pressure — good for image caches. Weak disappears aggressively — canonical keys."),
        ],
        see_also=see_also,
    )


@register("jvm-internals-quick-ref")
def _jvm_internals(see_also: str) -> str:
    return page_body(
        glance=[
            "Load → Link (verify, prepare, resolve) → Initialize.",
            "Bootstrap → Platform → Application class loaders delegation model.",
            "JIT: C1 (fast compile) → C2 (aggressive opt) — tiered compilation.",
            "Safepoints: STW operations (GC, deopt, JVMTI) — not every bytecode.",
        ],
        tables="""
| Loader | Loads |
| :--- | :--- |
| Bootstrap | `java.*`, core libs |
| Platform | JDK modules |
| Application | Classpath/module path app code |

| JIT tier | Role |
| :--- | :--- |
| Interpreter | Startup |
| C1 | Quick native |
| C2 | Hot spot optimization |

| Bytecode → machine | Phase |
| :--- | :--- |
| javac | Source to .class |
| Class loader | Define Class |
| Interpreter/JIT | Execute native |

| Tool | Inspects |
| :--- | :--- |
| `javap -c -v` | Bytecode |
| `jcmd <pid> Compiler.queue` | JIT |
| `jfr` | Safepoints, compile |
""",
        snippets="""
```bash
java -XX:+PrintCompilation -jar app.jar   # legacy style
java -XX:StartFlightRecording=settings=profile -jar app.jar
```
""",
        internals="- Escape analysis may stack-allocate non-escaping objects (not guaranteed).\n- Inlining driven by hotness — `-XX:MaxInlineLevel`.\n- Deoptimization on invalidated assumptions (e.g. monomorphic call site becomes megamorphic).",
        production="- Avoid giant class loaders reloading same classes — Metaspace churn.\n- Warm up JIT before latency benchmarks.\n- Module path (9+) reduces illegal reflective access — plan opens for frameworks.",
        interviews=[
            ("Class loader delegation why?", "Parent-first prevents core class spoofing; child sees parent definitions — security + single definition principle."),
            ("Safepoint bias?", "Long counted loops may poll safepoint — rare infinite loop without safepoint blocks GC in old JDK bugs; know `CompileCommand` escape hatches."),
        ],
        see_also=see_also,
    )


@register("jvm-flags-and-tuning")
def _jvm_flags(see_also: str) -> str:
    return page_body(
        glance=[
            "Ergonomic defaults adapt to container cgroup memory (10+).",
            "Always set explicit max heap in K8s — `-XX:MaxRAMPercentage` or `-Xmx`.",
            "Diagnostic flags: `NativeMemoryTracking`, `HeapDumpOnOutOfMemoryError`.",
            "Unlock experimental GC only with vendor support and benchmarks.",
        ],
        tables="""
| Category | Example flags |
| :--- | :--- |
| Heap | `-Xms`, `-Xmx`, `-XX:MaxRAMPercentage=75` |
| GC | `-XX:+UseG1GC`, `-XX:MaxGCPauseMillis=200` |
| Diagnostics | `-XX:+HeapDumpOnOutOfMemoryError`, `-XX:HeapDumpPath` |
| Logging | `-Xlog:gc*,safepoint:file=gc.log:time,level,tags` |
| JIT | `-XX:CICompilerCount`, `-XX:-TieredCompilation` (rare) |
| Container | `-XX:+UseContainerSupport` (default 10+) |

| Anti-pattern | Why |
| :--- | :--- |
| Huge `-Xms` == `-Xmx` always | Wastes K8s memory at idle |
| Copy-paste 8GB heap | OOMKill in 512Mi pod |
| Aggressive `-XX:MaxGCPauseMillis=10` | Throughput collapse |

| Prod starter (G1, container) | |
| :--- | :--- |
| `-XX:MaxRAMPercentage=75.0` | |
| `-XX:+UseG1GC` | if not default |
| `-XX:+HeapDumpOnOutOfMemoryError` | |
| `-Xlog:gc*:file=/logs/gc.log:time,uptime,level,tags` | |
""",
        snippets="""
```bash
# Print ergonomics decision
java -XX:+PrintFlagsFinal -version | grep Heap
java -XshowSettings:system -version
```
""",
        internals="- `-XX:+AlwaysPreTouch` touches pages at startup — longer start, fewer runtime faults.\n- `-XX:ActiveProcessorCount` overrides CPU count for GC/worker sizing.\n- Flag availability varies by vendor build (Oracle, Temurin, Corretto).",
        production="- Document flag rationale in runbook — not tribal knowledge.\n- Change one variable at a time when tuning.\n- Test GC upgrades on canary with production-like allocation profile.",
        interviews=[
            ("MaxRAMPercentage vs Xmx?", "Percentage of container-visible RAM — portable across pod sizes. `-Xmx` fixed — predictable absolute cap."),
            ("When disable explicit GC (`System.gc`)?", "`-XX:+DisableExplicitGC` if libraries trigger full GC via `System.gc` — but may break DirectByteBuffer cleanup relying on `Cleaner`; evaluate NIO libs first."),
        ],
        see_also=see_also,
    )


@register("java-lts-release-matrix")
def _lts(see_also: str) -> str:
    return page_body(
        glance=[
            "LTS releases: 8, 11, 17, 21, 25 — extended vendor support windows.",
            "Non-LTS (6-month): feature releases — production only if you own upgrade cadence.",
            "Migration path: bytecode usually forward-compatible; watch removed APIs and strong encapsulation.",
            "Vendor builds (Temurin, Corretto, Oracle) share OpenJDK core with support deltas.",
        ],
        tables="""
| LTS | GA | Highlights | Typical EOL (vendor-dependent) |
| :---: | :--- | :--- | :--- |
| 8 | 2014 | Lambdas, streams, Optional | Extended support offerings |
| 11 | 2018 | HTTP client, var in lambda, removal of JavaEE modules | 2026+ depending vendor |
| 17 | 2021 | Sealed, records, strong encapsulation | Long-term |
| 21 | 2023 | Virtual threads, sequenced collections, pattern matching mature | Long-term |
| 25 | 2025 | Next LTS baseline features | TBD |

| Migration checkpoint | Action |
| :--- | :--- |
| 8 → 11 | Remove JAXB/JAX-WS if on classpath; `var` optional |
| 11 → 17 | Strong encapsulation — `--add-opens` audit; records/sealed |
| 17 → 21 | Virtual threads pilot; prepare pinning monitors |
| Any | Run `jdeps`, `jdeprscan`, integration tests on target JDK |

| Build tool | JDK support |
| :--- | :--- |
| Maven compiler release | `-release 17` |
| Gradle toolchain | `java.toolchain.languageVersion` |
| Runtime vs compile | CI matrix both |
""",
        snippets="""
```xml
<!-- Maven -->
<release>21</release>
```
```gradle
java { toolchain { languageVersion = JavaLanguageVersion.of(21) } }
```
""",
        internals="- LTS cadence shifted: 21 LTS after 17; 25 continues 3-year pattern post-Oracle announcement.\n- Preview features require `--enable-preview` — not for prod without plan.\n- `javac --release` sets API and bytecode level.",
        production="- Pin CI and prod to same major LTS; automate CVE image rebuilds.\n- Maintain SBOM with JDK distribution provenance.\n- Test on target JDK in staging minimum 2 weeks before prod cutover.",
        interviews=[
            ("Why LTS for enterprises?", "Predictable support, vendor patches, slower change absorption — aligns with compliance and long maintenance contracts."),
            ("release vs target vs source?", "`--release N` sets bytecode + API surface; `target` alone doesn't limit APIs; prefer `release` for reproducible builds."),
        ],
        see_also=see_also,
    )


@register("java-recent-features")
def _recent(see_also: str) -> str:
    return page_body(
        glance=[
            "Rollup of post-8 language/API wins architects actually adopt in production.",
            "Records, sealed, pattern matching reduce boilerplate and enable exhaustiveness.",
            "Virtual threads + structured concurrency change blocking service economics.",
            "Collections: `SequencedCollection`, `getFirst`/`getLast` (21+).",
        ],
        tables="""
| Area | Feature | Since |
| :--- | :--- | :---: |
| Language | `var` local inference | 10 |
| Language | Text blocks | 15 |
| Language | Records | 16 |
| Language | Sealed classes | 17 |
| Language | Pattern matching `instanceof` | 16 |
| Language | Switch patterns | 21 |
| Language | String templates (preview) | 21+ |
| Concurrency | Virtual threads | 21 |
| API | `HttpClient` | 11 |
| API | `List.of`, `Map.of` immutable factories | 9 |
| API | `Optional.isEmpty`, `stream.toList` | 11 / 16 |

| Adopt now (17/21 LTS) | Defer / preview |
| :--- | :--- |
| Records for DTOs | String templates until final |
| Sealed domain ADTs | Foreign API without need |
| Virtual threads for IO services | Structured concurrency until standardized |
| `switch` expressions | |

| Removed / deprecated watch | |
| :--- | :--- |
| Security manager | Deprecated 17, removal planned |
| Finalization | Deprecated 9 |
| Applet API | Removed |
""",
        snippets="""
```java
record AuditEvent(Instant at, String actor, String action) {}

if (obj instanceof String s && !s.isBlank()) {
    process(s);
}

switch (day) {
    case MONDAY, FRIDAY -> scheduleReview();
    case SATURDAY, SUNDAY -> rest();
    default -> work();
}
```
""",
        internals="- Records are final — frameworks use bytecode enhancement for JPA (discouraged) or mapping layers.\n- Virtual threads change thread-per-request without reactive rewrite.\n- Pattern switches compile to tableswitch/lookupswitch + type tests.",
        production="- Enable features via toolchain not reflection hacks.\n- Track JEP status for previews in use.\n- Library ecosystem (Lombok overlap) — align team standards.",
        interviews=[
            ("Record vs Lombok `@Value`?", "Record is language-native, serialization-friendly, pattern matching ready. Lombok more flexible but external processor dependency."),
            ("Biggest 21 production win?", "Virtual threads for blocking microservices — simpler than reactive for many teams; still requires JDBC/driver and pool review."),
        ],
        see_also=see_also,
    )


@register("java-io-nio-ref")
def _io(see_also: str) -> str:
    return page_body(
        glance=[
            "Classic IO: stream-oriented, blocking — `InputStream`/`Reader`.",
            "NIO: buffers, channels, selectors — scalable non-blocking servers.",
            "NIO.2 (7+): `Path`, `Files` — preferred file API.",
            "`transferTo`/`mmap` for bulk zero-copy where supported.",
        ],
        tables="""
| API | Model | Blocking |
| :--- | :--- | :---: |
| `InputStream` | Byte stream | Yes |
| `Reader` | Char stream | Yes |
| `FileChannel` | Byte channel | Configurable |
| `SocketChannel` + `Selector` | Multiplex | Non-blocking |
| `Files.readAllLines` | Convenience | Yes |

| Operation | API |
| :--- | :--- |
| Walk tree | `Files.walk`, `walkFileTree` |
| Copy/move | `Files.copy`, `Files.move` |
| Attributes | `Files.readAttributes` |
| Watch dir | `WatchService` |

| Buffer key methods | |
| :--- | :--- |
| `flip` | Prepare for read after write |
| `clear` | Reset for write |
| `compact` | Partial consume |
""",
        snippets="""
```java
Path dir = Path.of("/data/inbox");
try (var lines = Files.lines(dir.resolve("events.jsonl"))) {
    lines.map(this::parse).forEach(this::handle);
}

long copied = inChannel.transferTo(0, inChannel.size(), outChannel);
```
""",
        internals="- `Files.lines` uses stream — must close (try-with-resources).\n- `DirectByteBuffer` off-heap — GC via `Cleaner`, not young GC.\n- `Selector` wake-up/spurious wakeup patterns on shutdown.",
        production="- Set charset explicitly — `StandardCharsets.UTF_8`.\n- Large files: stream, don't `readAllBytes`.\n- For high-performance IO: Netty or mapped files with measurement.",
        interviews=[
            ("NIO vs NIO.2?", "NIO (1.4): channels/buffers/selectors. NIO.2 (7): Path/Files/AsynchronousFileChannel — file system focus. Colloquially 'NIO' often means whole package tree."),
            ("When mmap?", "Large read-mostly files, random access — OS page cache leverage. Writes and portability complexity."),
        ],
        see_also=see_also,
    )


@register("reflection-annotations-ref")
def _reflection(see_also: str) -> str:
    return page_body(
        glance=[
            "Reflection: inspect/instantiate at runtime — breaks encapsulation, bypasses compile checks.",
            "Annotations: metadata — retention `SOURCE`/`CLASS`/`RUNTIME`.",
            "Modules (9+): `opens` packages for deep reflection to frameworks.",
            "Prefer compile-time annotation processing over runtime reflection scans.",
        ],
        tables="""
| Retention | Visible |
| :--- | :--- |
| `SOURCE` | Compiler only (`@Override`) |
| `CLASS` | Bytecode, not runtime |
| `RUNTIME` | Reflection |

| Meta-annotation | Purpose |
| :--- | :--- |
| `@Target` | Where applicable |
| `@Retention` | Lifetime |
| `@Documented` | Javadoc |
| `@Inherited` | Subclass inherits |

| Reflection cost | Mitigation |
| :--- | :--- |
| Method lookup | Cache `MethodHandle` |
| setAccessible | `trySetAccessible` + module opens |
| Startup scan | Index at build time (Spring AOT) |

| Built-in | Role |
| :--- | :--- |
| `@Deprecated` | API lifecycle |
| `@FunctionalInterface` | SAM check |
| `@SuppressWarnings` | Compiler noise |
""",
        snippets="""
```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Audited {
    String action();
}

Method m = clazz.getDeclaredMethod("save", Order.class);
m.setAccessible(true); // may fail on module encapsulation
```
""",
        internals="- `MethodHandles` + `VarHandles` faster than raw `Method.invoke` after warmup.\n- GraalVM native image requires reachability metadata for reflection.\n- Annotation proxies implement `Annotation` interface at runtime.",
        production="- Minimize reflection in hot paths — generate bytecode or use records.\n- Document `--add-opens` requirements for JDK 17+.\n- Security: don't reflect on user-supplied class names.",
        interviews=[
            ("Why modules hurt reflection?", "Strong encapsulation — internal packages not open by default; frameworks need explicit `opens` or command-line flags."),
            ("SOURCE vs RUNTIME annotations?", "SOURCE for compile-time checks/generation; RUNTIME for DI/mapping frameworks scanning at startup."),
        ],
        see_also=see_also,
    )


@register("serialization-quick-ref")
def _serialization(see_also: str) -> str:
    return page_body(
        glance=[
            "Java serialization: brittle, slow, security risk — avoid for new cross-service contracts.",
            "Prefer JSON/Protobuf/Avro with schema evolution.",
            "If required: `serialVersionUID`, explicit `readObject` validation.",
            "`Externalizable` manual control vs default reflection walk.",
        ],
        tables="""
| Mechanism | Pros | Cons |
| :--- | :--- | :--- |
| `Serializable` | Built-in | Fragile, opaque |
| `Externalizable` | Control | Boilerplate |
| JSON + Jackson | Human, interoperable | Schema discipline |
| Protobuf | Compact, versioned | Codegen |

| Security | Mitigation |
| :--- | :--- |
| Gadget chains | Don't deserialize untrusted |
| | `ObjectInputFilter` (9+) |
| | Allowlist classes |

| UID rule | |
| :--- | :--- |
| Change incompatible fields | Bump `serialVersionUID` |
| Compatible add optional field | Often OK with defaults |

| Alternative | When |
| :--- | :--- |
| `Record` + JSON | APIs |
| `ByteBuffer` + schema | High perf internal |
""",
        snippets="""
```java
private static final ObjectInputFilter filter =
    ObjectInputFilter.Config.createFilter(
        "com.myapp.**;java.base/java.lang.String;!*");

ObjectInputStream ois = new ObjectInputStream(in);
ois.setObjectInputFilter(filter);
```
""",
        internals="- `writeObject`/`readObject` hooks for custom serialization.\n- `transient` skips fields.\n- Enum serialization special-cased by name.",
        production="{{% warning %}}\nNever accept Java serialized blobs from untrusted clients — RCE history.\n{{% /warning %}}\n- Migrate session replication to JSON or sticky sessions.\n- RMI/JMX exposure audit in legacy apps.",
        interviews=[
            ("serialVersionUID purpose?", "Version handshake — mismatch throws `InvalidClassException`. Without explicit UID, compiler generates from structure — fragile across compilers."),
            ("ObjectInputFilter?", "JDK allowlist/denylist during deserialization — defense in depth if legacy serialization unavoidable."),
        ],
        see_also=see_also,
    )


@register("collections-complexity")
def _coll_complexity(see_also: str) -> str:
    return page_body(
        glance=[
            "Interview one-pager — average vs worst case for hash structures.",
            "Tree structures: O(log n) guaranteed.",
            "Iteration on hash maps: O(capacity + size).",
            "Concurrent structures: same big-O with different constants and weak iteration.",
        ],
        tables="""
| List op | ArrayList | LinkedList |
| :--- | :---: | :---: |
| `get(i)` | **O(1)** | O(n) |
| `add(end)` | O(1)* | **O(1)** |
| `add(i)` | O(n) | O(n) |

| Set op | HashSet | TreeSet |
| :--- | :---: | :---: |
| `add/contains` | O(1) avg | O(log n) |
| Iteration order | None | Sorted |

| Map op | HashMap | TreeMap | CHM |
| :--- | :---: | :---: | :---: |
| `get/put` | O(1) avg | O(log n) | O(1) avg |
| `containsValue` | O(n) | O(n) | O(n) |

| Queue | offer/poll |
| :--- | :---: |
| `ArrayDeque` | O(1) |
| `PriorityQueue` | O(log n) |
""",
        snippets="""
```java
// O(1) avg membership
Set<String> tags = new HashSet<>(List.of("java", "jvm"));
NavigableMap<Integer, String> ranks = new TreeMap<>();
```
""",
        internals="- Hash collision → list/tree bin — worst case per bin.\n- `LinkedList` as queue rarely beats `ArrayDeque`.\n- CHM `size()` approximate under contention.",
        production="- State avg vs worst in design reviews for hash-based stores.\n- Pre-size collections when size known.",
        interviews=[
            ("ArrayList vs LinkedList for 1M random reads?", "ArrayList O(1) per get — LinkedList O(n)."),
            ("When TreeMap worth O(log n)?", "Sorted keys, range queries — not pure get/put throughput."),
        ],
        see_also=see_also,
    )


@register("stream-operations-interview")
def _stream_interview(see_also: str) -> str:
    return page_body(
        glance=[
            "Intermediate = lazy; terminal = eager trigger.",
            "Short-circuit: `findFirst`, `anyMatch`, `limit`.",
            "`reduce` vs `collect` — monoid vs mutable container.",
            "Parallel: split characteristics matter.",
        ],
        tables="""
| Intermediate | Effect |
| :--- | :--- |
| `filter` | Predicate |
| `map` | 1:1 transform |
| `flatMap` | 1:many flatten |
| `distinct` | HashSet-backed |
| `sorted` | Materializes |
| `peek` | Debug side-effect |

| Terminal | Result |
| :--- | :--- |
| `collect` | Mutable reduction |
| `reduce` | Immutable combine |
| `count` | long |
| `min`/`max` | Optional |

| Parallel requirement | |
| :--- | :--- |
| Associative combiner | Required |
| No shared mutation | Required |
| `ORDERED` + parallel | May buffer |
""",
        snippets="""
```java
boolean anyExpensive = orders.stream()
    .filter(o -> o.amount() > 10_000)
    .findAny()
    .isPresent();
```
""",
        internals="- `Spliterator.ORDERED` preserved unless `unordered()`.\n- `Collectors.toMap` needs merge function on duplicate keys.\n- Primitive streams avoid `Integer` boxing.",
        production="- Don't parallelize by default.\n- Close resource-backed streams.",
        interviews=[
            ("Why is sorted() expensive?", "Requires full input materialization to sort — not streaming sort for arbitrary pipelines."),
            ("peek misuse?", "Debugging only — not for business logic; may not run if stream optimized away in theory — don't rely on side effects."),
        ],
        see_also=see_also,
    )


@register("concurrent-collections-interview")
def _conc_coll_interview(see_also: str) -> str:
    return page_body(
        glance=[
            "CHM default concurrent map — not `Hashtable`.",
            "`CopyOnWriteArrayList` — read-heavy, rare writes.",
            "BlockingQueue family for producer-consumer.",
            "`Collections.synchronized*` — whole-structure lock.",
        ],
        tables="""
| Type | Implementation | Notes |
| :--- | :--- | :--- |
| Concurrent map | `ConcurrentHashMap` | No nulls |
| Concurrent set | `ConcurrentHashMap.newKeySet()` | Backed by CHM |
| Sorted concurrent | `ConcurrentSkipListMap` | O(log n) |
| Copy-on-write list | `CopyOnWriteArrayList` | Snapshot iterators |
| Bounded buffer | `ArrayBlockingQueue` | Fixed capacity |
| Unbounded linked | `LinkedBlockingQueue` | Watch memory |

| Choose | When |
| :--- | :--- |
| CHM | Shared mutable map |
| COW list | Event listeners, config snapshots |
| `BlockingQueue` | Thread pool work queues |
| `LinkedBlockingQueue` + capacity | Backpressure |
""",
        snippets="""
```java
BlockingQueue<Task> queue = new ArrayBlockingQueue<>(1000);
queue.put(task); // blocks if full — backpressure
```
""",
        internals="- COW: write copies entire array — O(n) write.\n- CHM weakly consistent iterators.\n- `DelayQueue` for scheduled tasks.",
        production="- Size blocking queues from SLA and memory.\n- Don't use COW for write-heavy metrics buffers.",
        interviews=[
            ("CopyOnWrite when?", "Read-mostly, iterator must not throw CME, writes rare — listener lists."),
            ("CHM vs synchronized HashMap?", "CHM finer locking/CAS — synchronizedMap serializes all ops."),
        ],
        see_also=see_also,
    )


@register("gc-summary-interview")
def _gc_interview(see_also: str) -> str:
    return page_body(
        glance=[
            "Throughput vs latency collectors — no free lunch.",
            "Generational hypothesis: most objects die young.",
            "GC roots: stacks, statics, JNI, synchronized monitors.",
            "Tune with data: logs, JFR, pause percentiles.",
        ],
        tables="""
| Collector | Goal |
| :--- | :--- |
| G1 | Balance, regional |
| ZGC | Low pause, colored pointers |
| Shenandoah | Concurrent compact |
| Parallel | Max throughput batch |

| Term | Meaning |
| :--- | :--- |
| Minor GC | Young collection |
| Full GC | Often whole heap STW — investigate if frequent |
| Promotion | Survivors → old |
| Mixed GC (G1) | Partial old regions |

| Red flag | Action |
| :--- | :--- |
| Frequent Full GC | Heap too small or leak |
| Long pause spikes | Tune or switch collector |
| High allocation rate | Object churn profiling |
""",
        snippets="""
```bash
-Xlog:gc*:file=gc.log:time,uptime,level,tags
```
""",
        internals="- STW phases: snapshot roots at safepoint.\n- Concurrent collectors still brief pauses.\n- Metaspace GC distinct from heap GC.",
        production="- Alert on pause P99 and GC time %.\n- Capacity plan includes GC overhead CPU.",
        interviews=[
            ("Generational hypothesis?", "Most objects short-lived — collecting young gen frequently is cheap; few promote to old."),
            ("ZGC vs G1 trade-off?", "ZGC targets low pauses on large heaps with more CPU/barrier cost — validate on workload."),
        ],
        see_also=see_also,
    )


@register("java-version-features-interview")
def _version_interview(see_also: str) -> str:
    return page_body(
        glance=[
            "Whiteboard LTS deltas — 8→11→17→21.",
            "Records/sealed/patterns = 16–21 story.",
            "Modules strong encapsulation = 9/17 enforcement.",
            "Virtual threads = 21 headline.",
        ],
        tables="""
| Release | Headline features |
| :---: | :--- |
| 8 | Lambdas, streams, `Optional`, `java.time` |
| 11 | HTTP client, `var` in lambda, removed JavaEE modules |
| 17 | Records, sealed, pattern `instanceof` |
| 21 | Virtual threads, sequenced collections, pattern switch |
| 25 | LTS rollup — check release notes for GA |

| Question angle | Answer shape |
| :--- | :--- |
| Why upgrade? | Security, support, performance, language productivity |
| Risk | Removed APIs, reflection, dependencies |
| Preview features | Not in prod without flag plan |
""",
        snippets="""
```java
// 17+ style
public sealed interface Result permits Ok, Err {}
public record Ok<T>(T value) implements Result {}
```
""",
        internals="- `-release` flag ties bytecode to API.\n- LTS support timelines vendor-specific.",
        production="- Automate dependency compatibility scans on JDK bump.\n- Run canary with new JDK before fleet.",
        interviews=[
            ("Top 3 Java 17 features for teams?", "Records (DTOs), sealed (domain), pattern matching (cleaner code paths) — plus strong encapsulation forcing dependency updates."),
            ("8 to 21 biggest infra change?", "Module encapsulation + remove illegal reflective access; thread model option with virtual threads."),
        ],
        see_also=see_also,
    )


@register("memory-diagram-interview")
def _memory_interview(see_also: str) -> str:
    return page_body(
        glance=[
            "Stack: frames, locals, operand stack per thread.",
            "Heap: objects, arrays — shared across threads.",
            "Metaspace: class metadata (post-8).",
            "Off-heap: direct buffers, mapped files.",
        ],
        tables="""
```mermaid
flowchart TB
  subgraph perThread [Per thread]
    stack[Stack - frames]
    pc[Program Counter]
  end
  subgraph shared [Shared]
    heap[Heap - objects]
    meta[Metaspace - classes]
    code[Code Cache]
  end
  stack --> heap
```

| Region | Stores | GC |
| :--- | :--- | :--- |
| Stack | Primitives, refs | Auto on pop |
| Heap Young | New objects | Minor GC |
| Heap Old | Tenured | Major/mixed |
| Metaspace | Class metadata | Class unloading |
| Direct | NIO buffers | Cleaner / explicit |

| Object layout (64b, compressed oops) | |
| :--- | :--- |
| Mark word | Hash, locks, GC age |
| Klass pointer | Class metadata |
| Fields | + padding |
""",
        snippets="""
```java
// stack: primitives and references
// heap: new Object()
Object o = new Object();
```
""",
        internals="- TLAB allocation in Eden reduces contention.\n- Escape analysis may scalar-replace — not guaranteed observable.\n- `-XX:+UseCompressedOops` default on 64-bit heaps <32GB.",
        production="- Thread stack size `-Xss` matters at thousands of platform threads — not virtual threads.\n- Monitor Metaspace in dynamic class loaders (Groovy, JSR223).",
        interviews=[
            ("Stack vs heap?", "Stack: thread-local frames, automatic lifetime. Heap: shared objects, GC-managed — references on stack point to heap objects."),
            ("Where do static fields live?", "Field data in heap inside class mirror; metadata in Metaspace — static references are heap objects."),
        ],
        see_also=see_also,
    )


@register("thread-lifecycle-interview")
def _thread_interview(see_also: str) -> str:
    return page_body(
        glance=[
            "Platform thread states map to `Thread.State` enum.",
            "BLOCKED = monitor entry; WAITING/TIMED_WAITING = `wait`, `park`, `join`.",
            "Virtual threads: mount/unmount — not a 1:1 OS thread.",
            "Executors decouple task submission from thread lifecycle.",
        ],
        tables="""
```mermaid
stateDiagram-v2
  [*] --> NEW
  NEW --> RUNNABLE: start
  RUNNABLE --> BLOCKED: monitor lock
  RUNNABLE --> WAITING: wait/join/park
  RUNNABLE --> TIMED_WAITING: sleep/timeout
  BLOCKED --> RUNNABLE: lock acquired
  WAITING --> RUNNABLE: notify/unpark
  TIMED_WAITING --> RUNNABLE: timeout/notify
  RUNNABLE --> TERMINATED: run ends
```

| State | Cause |
| :--- | :--- |
| RUNNABLE | Eligible — may be running or waiting for CPU |
| BLOCKED | Waiting for monitor |
| WAITING | `Object.wait`, `join`, `LockSupport.park` |
| TIMED_WAITING | `sleep`, timed `wait`, `join` with timeout |

| Platform vs virtual | |
| :--- | :--- |
| OS thread cost | ~MB stack vs cheap VT |
| Blocking IO | Blocks carrier if pinned |
| `Thread.State` | Still reported — interpret carefully |
""",
        snippets="""
```java
Thread t = Thread.startVirtualThread(() -> fetch(url));
t.join();
```
""",
        internals="- `RUNNABLE` includes running on CPU or ready on run queue.\n- Interrupt sets flag — cooperative handling required.\n- Virtual thread park releases carrier.",
        production="- Thread dumps: distinguish deadlock vs pool exhaustion.\n- Don't rely on thread count for VT workloads — use request metrics.",
        interviews=[
            ("BLOCKED vs WAITING?", "BLOCKED waiting for synchronized monitor entry. WAITING voluntary no timeout — `wait`, `park`, `join` without timeout."),
            ("How virtual threads affect thread dumps?", "Many virtual threads listed — look for carrier pool and pinned threads; interpret blocking on IO vs pinning."),
        ],
        see_also=see_also,
    )


def main() -> None:
    """Sync topic order and prune orphan pages. Content is hand-maintained in content/."""
    modules_path = DATA / "java_engineering_modules.yaml"
    with open(modules_path, encoding="utf-8") as f:
        modules = yaml.safe_load(f)["modules"]

    ordered = flatten_topics(modules)
    write_order_yaml(ordered, DATA / "java_engineering_order.yaml")

    CONTENT.mkdir(parents=True, exist_ok=True)
    missing_files = [s for s in ordered if not (CONTENT / f"{s}.md").exists()]
    if missing_files:
        raise SystemExit(f"Missing content files: {missing_files}")

    keep = {"_index.md"} | {f"{s}.md" for s in ordered}
    deleted = 0
    for path in CONTENT.glob("*.md"):
        if path.name not in keep:
            path.unlink()
            deleted += 1
            print(f"Deleted {path.relative_to(ROOT)}")

    print(f"\nSummary: order synced, {deleted} orphans deleted, {len(ordered)} topics.")


if __name__ == "__main__":
    main()

