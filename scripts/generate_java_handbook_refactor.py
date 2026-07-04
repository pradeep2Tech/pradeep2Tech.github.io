"""One-time generator for Java Engineering Handbook interview refactor."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "java-engineering"
DATE = "2026-06-30T10:00:00+00:00"


def fm(
    title: str,
    desc: str,
    short: str,
    module: int,
    module_title: str,
    section: str,
    aliases: list[str] | None = None,
    cheat_sheet: bool = False,
) -> str:
    lines = [
        "---",
        f'title: "{title}"',
        f"date: {DATE}",
        "draft: false",
        f'description: "{desc}"',
        'tags: ["java", "java-engineering", "handbook", "interview"]',
        'categories: ["Java Engineering Handbook"]',
        f'shortTitle: "{short}"',
        f"module: {module}",
        f'moduleTitle: "{module_title}"',
        f'sectionRef: "{section}"',
        "interviewHandbook: true",
    ]
    if cheat_sheet:
        lines.append("cheatSheet: true")
    if aliases:
        lines.append("aliases:")
        for a in aliases:
            lines.append(f"  - {a}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def q(
    title: str,
    difficulty: str,
    time: str,
    short: str,
    detail: str,
    internal: str = "",
    production: str = "",
    mistakes: str | list[str] = "",
    followups: list[str] | None = None,
    interview_probes: list[str] | None = None,
    code: str = "",
) -> str:
    parts = [
        f"## {title}",
        "",
        f"**Difficulty:** {difficulty} · **Time:** {time}",
        "",
        "### Short Answer",
        "",
        short,
        "",
        "### Detailed Explanation",
        "",
        detail,
    ]
    if internal:
        parts.extend(["", "### Internal Working", "", internal])
    if code:
        parts.extend(["", "### Code Example", "", code])
    if production:
        parts.extend(["", "### Production Notes", "", production])
    if mistakes:
        parts.extend(["", "### Common Mistakes", ""])
        if isinstance(mistakes, list):
            parts.extend(f"- {m}" for m in mistakes)
        else:
            parts.append(mistakes)
    probes = interview_probes or followups
    if probes:
        parts.extend(["", "### Interview Questions", ""])
        parts.extend(f"{i}. {p}" for i, p in enumerate(probes, 1))
    if followups:
        parts.extend(["", "### Follow-up Questions", ""])
        parts.extend(f"- {f}" for f in followups)
    parts.append("")
    parts.append("---")
    parts.append("")
    return "\n".join(parts)


def page_intro(text: str) -> str:
    return text.strip() + "\n\n---\n\n"


def interview_bank(title: str, rows: list[tuple[str, str]]) -> str:
    """Append a numbered interview drill section (question, what interviewer wants)."""
    lines = [f"## {title}", ""]
    for i, (question, hint) in enumerate(rows, 1):
        lines.extend([f"### {i}. {question}", "", hint, "", "---", ""])
    return "\n".join(lines)


PAGES: dict[str, str] = {}

# --- Module 1 ---
PAGES["language-fundamentals"] = fm(
    "Language Fundamentals",
    "Primitives, var, records, switch patterns — interview essentials for senior Java engineers.",
    "Language Basics",
    1, "Language Fundamentals", "1.1",
    aliases=["core-java-quick-ref"],
) + q(
    "Why prefer primitives over wrappers in hot loops?",
    "Easy", "30 sec",
    "Primitives avoid heap allocation and autoboxing overhead.",
    "Wrapper types (`Integer`, `Long`) are objects — each autobox may allocate on the heap and add cache pressure. In tight loops over millions of iterations, `int` arithmetic is faster and GC-friendly. Collections require generics, so use primitive-specialized libraries (fastutil, Eclipse Collections) when numeric throughput matters.",
    "Autoboxing calls `Integer.valueOf` which may hit the small-integer cache (-128 to 127) or allocate.",
    "Profile before micro-optimizing; readability wins in business logic.",
    "Using `Integer` in `List` where values are always non-null.",
    followups=["What is the default value of a local `int` vs field?", "When does widening vs narrowing apply?"],
) + q(
    "What does `final` on a reference mean?",
    "Easy", "30 sec",
    "The reference binding cannot change; the referenced object may still mutate.",
    "`final User user` means you cannot reassign `user` to another object. If `User` is mutable, `user.setName()` is still legal. Immutability requires an immutable class design (records, unmodifiable fields).",
    followups=["How do `final` fields affect JVM initialization and visibility?"],
) + q(
    "Arrays covariant but generics invariant — explain.",
    "Medium", "1 min",
    "`String[]` is an `Object[]` at runtime; `List<String>` is not a `List<Object>`.",
    "Arrays carry runtime element type information — assigning `Object[] o = new String[1]; o[0] = 1` fails at runtime with `ArrayStoreException`. Generics erase type parameters at compile time; the compiler rejects unsafe assignments to preserve type safety without runtime checks on every read.",
    "Type erasure: `List<String>` bytecode is `List`.",
    "Don't use arrays for generic APIs — prefer `List<T>`.",
    followups=["What is heap pollution?", "Why no `new T[]`?"],
) + q(
    "Pattern matching switch and exhaustiveness (17+/21+)",
    "Medium", "1 min",
    "Switch on sealed types must cover all permitted subtypes; compiler enforces exhaustiveness.",
    "Sealed classes/interfaces restrict subclasses (`permits`). Combined with pattern switches, the compiler verifies all cases are handled — no default needed when exhaustive. Records destructure in case labels: `case Point(int x, int y)`.",
    followups=["Difference between classic switch and switch expressions?"],
)

PAGES["strings-and-enums-interview"] = fm(
    "Strings & Enums Interview Guide",
    "String immutability, interning, builders, text blocks, and enum patterns.",
    "Strings & Enums",
    1, "Language Fundamentals", "1.2",
    aliases=["strings-and-enums-ref"],
) + q(
    "Why is String immutable?",
    "Easy", "1 min",
    "Thread safety, security, hash caching, and safe sharing as map keys.",
    "Immutable strings can be shared across threads without synchronization. Security: credential/URL strings cannot be mutated after validation. `hashCode()` is cached after first compute. Trade-off: concatenation creates new objects — use `StringBuilder` in loops.",
    "OpenJDK may use compact strings (byte-backed LATIN1) internally since Java 9.",
    "Never build SQL by concatenation — use prepared statements.",
    "Assuming `substring` always copies (modern JDKs may share backing).",
    followups=["String pool vs `intern()`?", "Text blocks (15+) use cases?"],
) + q(
    "StringBuilder vs String concat in loops?",
    "Easy", "30 sec",
    "Concat in loop is O(n²); StringBuilder is O(n) total.",
    "Each `+` in a loop may create intermediate String objects. Compiler optimizes few-operand concat but not arbitrary loops. `StringBuilder` (not thread-safe) for single-thread; `StringBuffer` only for legacy.",
    followups=["When is `+` concat acceptable?"],
) + q(
    "Enum vs int constants — why enum?",
    "Medium", "1 min",
    "Type safety, singleton semantics, `EnumSet`/`EnumMap`, serialization by name.",
    "Enums are classes with fixed instances — compiler checks exhaustiveness in switches. `EnumSet` is bit-vector backed. Persist `name()`, never `ordinal()`. Strategy enum pattern embeds behavior per constant.",
    followups=["When use `EnumSet` over `HashSet<Day>`?"],
)

PAGES["oop-interview"] = fm(
    "OOP Interview Guide",
    "Inheritance, composition, records, sealed classes, overriding vs overloading.",
    "OOP",
    1, "Language Fundamentals", "1.3",
    aliases=["oop-quick-ref"],
) + q(
    "Composition over inheritance — when to inherit?",
    "Medium", "1 min",
    "Prefer composition for reuse; inherit for true subtype polymorphism (Liskov).",
    "Inheritance couples subclasses to parent implementation — fragile base class problem. Use composition + delegation for behavior reuse. Inherit when `is-a` relationship is stable and you need virtual dispatch (`@Override`).",
    followups=["What is the fragile base class problem?"],
) + q(
    "Overloading vs overriding?",
    "Easy", "30 sec",
    "Overloading: same name, different signatures — resolved at compile time. Overriding: subclass replaces instance method — runtime dispatch.",
    "Static methods hide, not override. `@Override` catches signature mistakes. `private`/`final` methods cannot be overridden.",
    followups=["Can you override a static method?"],
) + q(
    "Record vs class — when not to use a record?",
    "Medium", "1 min",
    "Records are immutable data carriers — not for JPA entities or types needing inheritance.",
    "Records provide canonical constructor, equals/hashCode/toString. They are `final` with final fields. Poor fit for JPA lazy proxies, mutable domain models, or types requiring inheritance hierarchies.",
    followups=["Record vs Lombok `@Value`?"],
) + q(
    "Sealed classes purpose?",
    "Medium", "1 min",
    "Closed hierarchies enabling exhaustive pattern matching and controlled extension.",
    "Sealed types list permitted subclasses (`permits`). Compiler enforces exhaustiveness in switches. Models ADTs: `sealed interface Result permits Ok, Err`.",
    followups=["Sealed vs final class?"],
)

PAGES["generics-interview"] = fm(
    "Generics Interview Guide",
    "PECS, erasure, bounds, and common compiler errors.",
    "Generics",
    1, "Language Fundamentals", "1.4",
    aliases=["generics-quick-ref"],
) + q(
    "What is PECS?",
    "Medium", "1 min",
    "Producer Extends, Consumer Super — wildcard direction for API flexibility.",
    "If you read from a structure (producer), use `? extends T`. If you write into it (consumer), use `? super T`. `Collections.copy(List<? super T> dest, List<? extends T> src)` is the canonical example.",
    followups=["Why can't you add to `List<? extends Number>`?"],
) + q(
    "What is type erasure?",
    "Medium", "1 min",
    "Generic type parameters are erased at runtime; bytecode uses raw types and casts.",
    "`List<String>` becomes `List` at runtime. You cannot `new T()`, `T[]`, or `instanceof List<String>`. Bridge methods preserve polymorphism for generic overrides.",
    followups=["What is heap pollution?", "How does `List.class` work at runtime?"],
) + q(
    "Why no `List<int>`?",
    "Easy", "30 sec",
    "Generics require reference types; primitives cannot be type arguments.",
    "Use `IntStream`, primitive arrays, or libraries like fastutil for compact numeric storage.",
)

PAGES["exceptions-interview"] = fm(
    "Exceptions Interview Guide",
    "Checked vs unchecked, try-with-resources, suppression, API design.",
    "Exceptions",
    1, "Language Fundamentals", "1.5",
    aliases=["exceptions-quick-ref"],
) + q(
    "Checked vs unchecked exceptions?",
    "Easy", "1 min",
    "Checked: must declare or catch (`IOException`). Unchecked: `RuntimeException` and errors — programming bugs or unrecoverable.",
    "Modern API design favors unchecked for most application errors — avoids polluting signatures. Checked useful when caller can recover (retry IO).",
    followups=["When wrap checked in unchecked?"],
) + q(
    "try-with-resources — how does it work?",
    "Easy", "30 sec",
    "Auto-closes `AutoCloseable` resources in reverse order; suppresses close exceptions if body threw.",
    "Compiler desugars to try/finally with null-safe close. Suppressed exceptions attached to primary via `addSuppressed`.",
    followups=["What if close() throws?"],
)

PAGES["object-contract-interview"] = fm(
    "Object Contract Interview Guide",
    "equals, hashCode, toString, Comparable, and collection contract.",
    "Object Contract",
    1, "Language Fundamentals", "1.6",
    aliases=["interfaces-and-object-contract"],
) + q(
    "equals/hashCode contract?",
    "Medium", "1 min",
    "If equal objects must have same hashCode; reflexive, symmetric, transitive, consistent.",
    "Breaking contract breaks `HashMap`/`HashSet` — objects become unfindable. Use `Objects.equals`/`Objects.hash`. For records, generated automatically.",
    "HashMap bin lookup uses hash then equals.",
    "Don't use mutable fields in equals/hashCode for map keys.",
    followups=["What fields to include in equals?", "IDE generate pitfalls?"],
) + q(
    "Comparable vs Comparator?",
    "Easy", "30 sec",
    "Comparable: natural order inside type (`compareTo`). Comparator: external, multiple orderings, lambdas.",
    "`TreeSet`/`TreeMap` need Comparable or provided Comparator. `Comparator.comparing` chains with `thenComparing`.",
)

# --- Module 2: collection-selection-matrix ---
PAGES["collection-selection-matrix"] = fm(
    "Collection Selection Matrix",
    "Choose List, Set, Map, Queue by access pattern, ordering, concurrency, and null policy.",
    "Collection Choice",
    2, "Collections", "2.1",
    aliases=["collections-decision-matrix", "list-set-queue-comparison", "collections-utils-and-ordering"],
) + """
Interview-oriented collection selection for senior engineers.

```mermaid
flowchart TD
  need[Need collection?] --> keyed{Keyed?}
  keyed -->|yes| map[Map matrix]
  keyed -->|no| unique{Unique?}
  unique -->|yes| set[Set matrix]
  unique -->|no| seq{Indexed?}
  seq -->|yes| al[ArrayList]
  seq -->|no| q[Queue/Deque]
```

| Need | Default | Alternatives |
| :--- | :--- | :--- |
| General list | `ArrayList` | `LinkedList` rare |
| Unique unordered | `HashSet` | `LinkedHashSet` for order |
| Unique sorted | `TreeSet` | `ConcurrentSkipListSet` |
| Key-value | `HashMap` | See [Map Implementations](/java-engineering/map-implementations/) |
| FIFO / stack | `ArrayDeque` | `LinkedBlockingQueue` bounded |
| Priority | `PriorityQueue` | Not thread-safe |
| Concurrent map | `ConcurrentHashMap` | Not `Collections.synchronizedMap` for writes |
| LRU cache | `LinkedHashMap` access-order | Caffeine in production |

| List op | ArrayList | LinkedList |
| :--- | :---: | :---: |
| `get(i)` | **O(1)** | O(n) |
| `add(end)` | O(1)* | O(1) |
| `add(i)` | O(n) | O(n) |

| Set op | HashSet | TreeSet |
| :--- | :---: | :---: |
| `add/contains` | O(1) avg | O(log n) |
| Iteration order | Undefined | Sorted |

---

""" + q(
    "ArrayList vs LinkedList for 10M random reads?",
    "Easy", "30 sec",
    "`ArrayList` — O(1) indexed access. `LinkedList` is O(n) per get.",
    "LinkedList rarely wins on modern CPUs due to cache misses walking nodes. Use ArrayList unless deque operations at both ends without index access.",
    followups=["When is LinkedList justified?"],
) + q(
    "When LinkedHashMap over HashMap?",
    "Medium", "1 min",
    "Insertion or access-order iteration, LRU caches, predictable debugging.",
    "Maintains doubly-linked list through entries. Access-order mode (`true` ctor flag) moves entries on `get` — classic LRU with `removeEldestEntry`.",
    production="Pre-size: `new HashMap<>(expectedSize / 0.75f + 1)`.",
)

PAGES["map-implementations"] = fm(
    "Map Implementations Interview Guide",
    "HashMap, LinkedHashMap, TreeMap, CHM selection — when to use which.",
    "Maps",
    2, "Collections", "2.4",
    aliases=["map-implementations-ref"],
) + q(
    "HashMap vs TreeMap?",
    "Easy", "30 sec",
    "HashMap: O(1) avg, unordered. TreeMap: O(log n), sorted, `NavigableMap` range ops.",
    "TreeMap needs `Comparable` keys or Comparator. No null keys in TreeMap (usually).",
    followups=["NavigableMap floor/ceiling use cases?"],
) + q(
    "WeakHashMap vs HashMap?",
    "Medium", "1 min",
    "WeakHashMap keys are weak references — entries removed when key only weakly reachable.",
    "Use for listener registries or caches where keys should GC independently. Values need strong refs elsewhere or they disappear too.",
    followups=["IdentityHashMap use case?"],
)

# --- Module 3: Streams ---
PAGES["streams-collectors-interview-guide"] = fm(
    "Streams & Collectors Interview Guide",
    "Lazy pipelines, collectors, lambdas, Optional, and parallel stream pitfalls.",
    "Streams",
    1, "Language Fundamentals", "1.7",
    aliases=["streams-quick-ref", "stream-operations-interview", "functional-java-ref"],
) + q(
    "Why are streams lazy?",
    "Medium", "1 min",
    "Intermediate ops fuse; execution deferred until terminal op — enables short-circuit and optimization.",
    "Pipeline builds operator chain (sink wrapping). Single terminal op triggers traversal. Short-circuit ops (`findFirst`, `anyMatch`, `limit`) stop early.",
    "Spliterator characteristics (`SIZED`, `ORDERED`, `DISTINCT`) enable optimizations.",
    "Don't reuse a Stream after terminal operation.",
    followups=["What is a Spliterator?", "Difference reduce vs collect?"],
) + q(
    "When to use parallel streams?",
    "Medium", "1 min",
    "Large in-memory CPU-bound work, associative ops, no shared mutation, good spliterator splitting.",
    "Uses `ForkJoinPool.commonPool()`. Bad for IO, small collections (<10k), or ordered pipelines where order matters. Side effects in `forEach` need thread-safe collections.",
    "Default parallelism = CPUs - 1.",
    "Parallelizing by default in services.",
    followups=["What makes a combiner associative?", "Common pool starvation risk?"],
) + q(
    "Collectors.toMap duplicate key pitfall?",
    "Easy", "30 sec",
    "Without merge function, duplicate keys throw `IllegalStateException`.",
    "Use `toMap(keyFn, valFn, mergeFn)` or `groupingBy`. Java 16+ prefer `toList()` over `collect(toList())`.",
) + q(
    "Optional in API design — good or bad?",
    "Medium", "1 min",
    "Good as return type signaling absence; bad as field, parameter, or collection element.",
    "Optional not serializable by default; JSON mapping awkward. Use overloads for optional params. Never `optional.get()` without check.",
    followups=["Effectively final in lambdas — why?"],
)

# --- Threading ---
PAGES["java-threading-interview-guide"] = fm(
    "Java Threading Interview Guide",
    "Thread lifecycle, executors, shutdown, platform vs virtual threads.",
    "Threading",
    3, "Concurrency", "3.1",
    aliases=["threads-and-executors", "thread-lifecycle-interview"],
) + q(
    "Platform thread states — BLOCKED vs WAITING?",
    "Medium", "1 min",
    "BLOCKED: waiting for monitor entry. WAITING: voluntary park without timeout (`wait`, `join`, `park`).",
    "`RUNNABLE` includes running or ready on CPU queue. `TIMED_WAITING`: sleep, timed wait/join.",
    "See [Thread Lifecycle Cheat Sheet](/java-engineering/thread-lifecycle-cheatsheet/) for diagram.",
    followups=["How do virtual threads affect thread dumps?"],
) + q(
    "Fixed thread pool sizing?",
    "Medium", "1 min",
    "CPU-bound ≈ cores; blocking IO needs higher pool or virtual threads; measure queue depth and latency.",
    "`newFixedThreadPool` has unbounded queue — sustained overload causes OOM. Always `shutdown()` + `awaitTermination` on app stop.",
    "Name threads via custom ThreadFactory for diagnostics.",
    "Using `availableProcessors()` alone for mixed IO/CPU workloads.",
    followups=["shutdown vs shutdownNow?", "When cached thread pool?"],
) + q(
    "Thread.start happens-before run?",
    "Easy", "30 sec",
    "Yes — actions in parent before `start()` visible to child thread when `run` begins.",
    "Part of JMM happens-before rules. Also monitor unlock/lock, volatile write/read.",
    followups=["See Java Memory Model page"],
)

PAGES["java-memory-model"] = fm(
    "Java Memory Model Interview Guide",
    "happens-before, visibility, ordering, and volatile semantics.",
    "JMM",
    3, "Concurrency", "3.2",
) + page_intro("""
The **Java Memory Model (JMM)** defines which writes are visible to which reads across threads. Without happens-before edges, CPUs and compilers may reorder or cache values — leading to subtle bugs in double-checked locking, lazy init, and lock-free code.
""") + q(
    "What is happens-before?",
    "Hard", "3 min",
    "Partial ordering guaranteeing visibility — if A happens-before B, B sees A's writes.",
    "Rules: monitor unlock→lock, volatile write→read, thread start/join, `Concurrent` utilities documented edges. Without happens-before, threads may see stale values due to CPU cache and compiler reordering.",
    "JMM defines what reorderings are legal; synchronized/volatile constrain them.",
    followups=["volatile vs synchronized?", "Double-checked locking fix?"],
) + q(
    "What does volatile guarantee?",
    "Medium", "1 min",
    "Visibility and ordering for reads/writes — not atomicity of compound ops like i++.",
    "Volatile read/write establish happens-before. No torn reads/writes for 32/64-bit volatiles on supported platforms. i++ is read-modify-write — use `AtomicInteger` or lock.",
    followups=["Why volatile not enough for i++?"],
) + q(
    "Double-checked locking — why broken and fix?",
    "Hard", "2 min",
    "Without volatile on instance ref, another thread may see partially constructed object due to reordering.",
    "Fix: `private volatile Singleton instance`, holder idiom, or enum singleton. Volatile write establishes happens-before for readers.",
    production="Prefer DI or enum singleton — avoid hand-rolled DCL in new code.",
    mistakes=[
        "DCL without volatile on the instance reference (broken pre-JMM5 pattern).",
        "Using volatile on fields inside the object but not on the publishing reference.",
    ],
    interview_probes=[
        "List three happens-before rules without looking them up.",
        "Why does `Thread.start` establish happens-before?",
        "Safe publication: stack confinement vs volatile vs final fields?",
    ],
    followups=["Safe publication idioms?"],
) + interview_bank("JMM Interview Drill", [
    ("Is `volatile` enough for `count++`?", "No — compound RMW needs atomics or synchronization."),
    ("Does reordering happen on single-threaded code?", "Yes, compiler may reorder if as-if-serial semantics preserved."),
    ("How does `ConcurrentHashMap` relate to JMM?", "Documented happens-before on successful `put` → subsequent `get`."),
])

PAGES["cas-and-lock-free-programming"] = fm(
    "CAS & Lock-Free Programming",
    "Compare-and-swap, ABA problem, AtomicReference, LongAdder vs AtomicLong.",
    "CAS",
    3, "Concurrency", "3.4",
) + page_intro("""
Lock-free code uses **hardware CAS** (compare-and-swap) instead of mutexes for hot counters, queues, and map bins. Interviewers probe CAS mechanics, the **ABA problem**, when to pick `LongAdder`, and how `java.util.concurrent.atomic` maps to CPU instructions.

```mermaid
flowchart LR
    A[Read current V] --> B{V == expected?}
    B -->|yes| C[Write new value atomically]
    B -->|no| D[Retry or fail]
    C --> E[Success]
    D --> A
```
""") + q(
    "What is CAS?",
    "Medium", "1–2 min",
    "Compare-And-Swap atomically updates a memory location **only if** the current value equals an expected value — a hardware primitive (`cmpxchg` on x86).",
    "Java exposes CAS via `sun.misc.Unsafe` (internal) and public APIs: `AtomicInteger.compareAndSet`, `AtomicReference`, `VarHandle` (Java 9+). Lock-free algorithms **retry** when CAS fails due to contention instead of parking threads. `AtomicInteger.incrementAndGet` loops: read, compute, CAS until success. CHM uses CAS on empty bins before escalating to synchronized bin heads.",
    "On x86: `LOCK CMPXCHG`. Contended CAS causes cache-line bouncing — `LongAdder` stripes to reduce this.",
    production="Prefer atomics for metrics and single-word updates; use locks when invariants span multiple fields.",
    mistakes=[
        "Assuming CAS makes `i++` on a plain `int` atomic — need `AtomicInteger` or synchronized.",
        "Spinning forever on hot CAS without backoff or striping.",
    ],
    interview_probes=[
        "Walk through `incrementAndGet` at the CPU level — what happens on failure?",
        "When would you choose a lock over CAS for a counter?",
        "How does CAS relate to optimistic concurrency in databases?",
    ],
    code="""```java
AtomicInteger counter = new AtomicInteger(0);

// incrementAndGet: CAS loop internally
int next = counter.incrementAndGet();

// explicit CAS — returns false if another thread won
boolean ok = counter.compareAndSet(5, 6);
```""",
    followups=["CAS vs lock — when prefer each?", "What is lock-free vs wait-free?"],
) + q(
    "CAS vs synchronized — when prefer each?",
    "Medium", "2 min",
    "CAS for **single-word** optimistic updates under moderate contention; `synchronized`/`Lock` when you must hold **multi-field invariants** or block waiting.",
    "CAS wins for counters, stack heads, and CHM-style structures where failure = retry. Locks win when work inside the critical section is non-trivial, when you need `wait`/`notify`, or when retry storms would waste CPU. `ReentrantLock` with `tryLock` blends both: optimistic attempt, fallback to blocking.",
    production="Micrometer counters: `LongAdder`. Sequence IDs needing strict ordering: `AtomicLong` or DB sequence.",
    mistakes=["Using CAS loops to guard three related fields — use a lock or transactional model."],
    interview_probes=[
        "Design a rate limiter with atomics only — what breaks?",
        "Why can contended CAS be slower than a short lock?",
    ],
) + q(
    "ABA problem?",
    "Hard", "2–3 min",
    "Value changes **A → B → A**; a CAS comparing against expected **A** succeeds even though the structure changed in between.",
    "Classic in lock-free **stacks/queues** that recycle nodes — thread 1 pops A, thread 2 pops/modifies/pushes A back, thread 1's CAS still sees A. Fixes: **versioned references** (`AtomicStampedReference`, `AtomicMarkableReference`), **hazard pointers**, or **epoch-based reclamation** (non-blocking memory management). Java's `ConcurrentLinkedQueue` uses safe algorithms; don't hand-roll lock-free lists without studying reclamation.",
    mistakes=[
        "Ignoring ABA when reusing object pools with CAS-linked structures.",
        "Assuming `AtomicReference` alone prevents ABA — it does not without stamps.",
    ],
    interview_probes=[
        "Why doesn't `AtomicInteger` suffer ABA for a counter?",
        "When would you use `AtomicStampedReference` in production?",
        "How do hazard pointers differ from version stamps?",
    ],
    followups=["Where does ABA matter outside Java?"],
) + q(
    "LongAdder vs AtomicLong?",
    "Medium", "1–2 min",
    "`LongAdder` **stripes** increments across internal cells — lower contention under many writers; `AtomicLong` holds a **single** value with CAS on every update.",
    "`LongAdder.add` spreads writes; `sum()` aggregates cells (not a linearizable snapshot under concurrent adds, but fine for metrics). Use `AtomicLong` when you need **exact current value** on every read, CAS-based sequences, or `getAndIncrement` semantics visible to other threads immediately.",
    production="Request/error counters: `LongAdder`. Global sequence / ledger balance: `AtomicLong` or DB.",
    code="""```java
LongAdder requests = new LongAdder();
requests.increment();
long approx = requests.sum();  // good for dashboards

AtomicLong sequence = new AtomicLong();
long id = sequence.incrementAndGet();  // strict unique ID
```""",
    interview_probes=[
        "Is `sum()` on LongAdder linearizable? When does that matter?",
        "How would you expose LongAdder to Prometheus?",
    ],
    followups=["DoubleAdder vs AtomicDouble?"],
) + q(
    "AtomicReference use cases?",
    "Medium", "1–2 min",
    "Holds a reference updated atomically — lock-free **swap** of immutable snapshots (config, cache entry, state object).",
    "Pattern: keep an **immutable** object; CAS replaces whole reference when config changes. Readers never see torn state. `AtomicReference<Config>` + `compareAndSet(old, new)` after validation. Used in `ConcurrentHashMap` treeify transitions and lazy initialization patterns.",
    code="""```java
AtomicReference<Config> live = new AtomicReference<>(Config.defaults());

void publish(Config next) {
    Config prev;
    do {
        prev = live.get();
        if (!next.isValid()) throw new IllegalArgumentException();
    } while (!live.compareAndSet(prev, next));
}
```""",
    interview_probes=[
        "Why must referenced objects be immutable for safe CAS swap?",
        "AtomicReference vs volatile reference field?",
    ],
) + q(
    "VarHandle vs legacy Atomic*?",
    "Hard", "2 min",
    "`VarHandle` (Java 9+) provides typed CAS/volatile access on fields and arrays — foundation for future intrinsics; `Atomic*` classes are ergonomic wrappers.",
    "VarHandles enable off-heap / array element CAS with fence modes (`plain`, `opaque`, `release`, `acquire`, `volatile`). Library authors use them; application code usually sticks to `AtomicInteger` etc. Conceptually same CAS semantics.",
    interview_probes=[
        "What fence modes does VarHandle expose and why?",
        "How does this relate to `Unsafe` deprecation path?",
    ],
) + q(
    "Lock-free vs wait-free?",
    "Hard", "2 min",
    "**Lock-free:** system-wide progress — some thread completes in finite steps. **Wait-free:** every thread completes in bounded steps regardless of others.",
    "Most `java.util.concurrent.atomic` ops are lock-free (retry under contention). True wait-free structures are rare in JDK — harder to implement. Interview answer: lock-free is practical JDK goal; wait-free is stronger theoretical guarantee.",
    interview_probes=[
        "Is `ConcurrentLinkedQueue.offer` wait-free?",
        "Why do production systems rarely require wait-freedom?",
    ],
) + interview_bank("Rapid-Fire Interview Drill", [
    ("Explain CAS in one sentence to a junior.", "Atomic update if-and-only-if current value matches expected; retry on failure."),
    ("Your metrics spike CPU after switching to AtomicLong — fix?", "Stripe with LongAdder or sample; check cache-line false sharing."),
    ("Can you implement a lock-free stack with only AtomicReference?", "Yes, but address ABA and safe node reclamation."),
    ("When does CHM use CAS vs synchronized bin lock?", "Empty bin CAS install; collision chains synchronize on bin head."),
    ("How do you test lock-free code?", "Stress tests, jcstress, Thread.sleep jitter — not single-threaded unit tests only."),
])

PAGES["threadlocal-internals"] = fm(
    "ThreadLocal Internals",
    "Per-thread storage, ThreadLocalMap, leaks in pooled threads.",
    "ThreadLocal",
    3, "Concurrency", "3.5",
) + page_intro("""
`ThreadLocal` gives each thread its own copy of a variable — common for `SimpleDateFormat`, request context, and tracing IDs. In **pooled threads**, failure to `remove()` causes leaks and cross-request contamination.
""") + q(
    "How does ThreadLocal work internally?",
    "Medium", "2 min",
    "Each `Thread` holds a `ThreadLocalMap` — weak keys (ThreadLocal), strong values.",
    "`ThreadLocal.set` gets current thread's map, creates entry keyed by ThreadLocal identity. `get` looks up same map. Keys are weak — ThreadLocal GC'd when no strong ref, but values linger until next set/remove if key collected.",
    "OpenJDK: `Thread.threadLocals` field.",
    "Always `remove()` in finally for pool threads.",
    followups=["ThreadLocal vs ScopedValue?", "Millions of virtual threads + ThreadLocal?"],
) + q(
    "ThreadLocal memory leak in thread pools?",
    "Medium", "1 min",
    "Pool threads live forever — ThreadLocal values retained until removed.",
    "Request context in ThreadLocal without `remove()` after task leaks prior request data and heap. Critical in Tomcat/executor pools.",
    production="try/finally with remove(); prefer ScopedValue (21+) for virtual threads.",
    interview_probes=[
        "Why are ThreadLocal keys weak but values strong?",
        "What breaks if you use ThreadLocal with 1M virtual threads?",
        "How would you migrate request context to ScopedValue?",
    ],
) + q(
    "ThreadLocal vs ScopedValue (Java 21+)?",
    "Medium", "2 min",
    "`ScopedValue` binds immutable context for a **dynamic scope** — inherited by child threads, no map per thread, better for virtual threads.",
    "ThreadLocal: map on each `Thread`, manual remove. ScopedValue: `ScopedValue.where(KEY, value).run(() -> ...)` — automatic cleanup when scope ends. Preferred for request context in VT-heavy apps.",
    interview_probes=[
        "Can ScopedValue replace all ThreadLocal uses?",
        "How does structured concurrency interact with ScopedValue?",
    ],
) + interview_bank("ThreadLocal Interview Drill", [
    ("Symptom: user A sees user B data in Tomcat — cause?", "ThreadLocal not cleared in pool thread after request."),
    ("Where is ThreadLocalMap stored?", "On the Thread object (`threadLocals` field)."),
])

PAGES["forkjoinpool-internals"] = fm(
    "ForkJoinPool Internals",
    "Work-stealing, common pool, parallel streams, CompletableFuture default executor.",
    "ForkJoinPool",
    3, "Concurrency", "3.6",
) + q(
    "How does ForkJoinPool work-stealing work?",
    "Hard", "2 min",
    "Each worker has deque; pushes own tasks, steals from others' deque tail when idle.",
    "Divide-and-conquer tasks `fork` subtasks, `join` results. Stealing balances load. `commonPool()` shared by parallel streams and default `CompletableFuture` async — risk of starvation.",
    "Not used for virtual thread scheduling.",
    production="Pass explicit Executor to CompletableFuture; don't block inside common pool.",
    interview_probes=[
        "Why is blocking in parallelStream dangerous?",
        "ForkJoinPool common pool parallelism default?",
        "Difference between work-stealing and traditional thread pool queue?",
    ],
    followups=["Parallel stream thread pool?"],
) + q(
    "Parallel streams and common pool pitfalls?",
    "Medium", "2 min",
    "`parallelStream()` uses `ForkJoinPool.commonPool()` — shared globally; blocking or IO inside pipeline starves other users of the pool.",
    "Fix: custom pool via `ForkJoinPool.submit(() -> list.parallelStream()...).get()` or use explicit Executor. CPU-bound, non-blocking transforms only in parallel streams.",
    mistakes=["Calling `parallelStream` on small collections — overhead exceeds benefit."],
    interview_probes=[
        "When is parallelStream actually faster?",
        "How does Spliterator SPLIT_CHARACTERISTICS affect parallelism?",
    ],
) + interview_bank("ForkJoinPool Interview Drill", [
    ("CompletableFuture.supplyAsync with no executor — which pool?", "ForkJoinPool.commonPool()."),
    ("Virtual threads use ForkJoinPool?", "No — carrier pool is separate (ForkJoinPool by default for carriers)."),
])

PAGES["deadlock-detection"] = fm(
    "Deadlock Detection & Prevention",
    "Four conditions, lock ordering, tryLock, thread dump analysis.",
    "Deadlock",
    3, "Concurrency", "3.7",
) + q(
    "Four conditions for deadlock?",
    "Medium", "1 min",
    "Mutual exclusion, hold-and-wait, no preemption, circular wait — break one to prevent.",
    "Prevention: global lock ordering, `tryLock` with backoff, timeouts. Detection: thread dump shows 'Found one Java-level deadlock'.",
    production="jcmd Thread.print / JFR lock events.",
    interview_probes=[
        "Break circular wait without global ordering — possible?",
        "Difference between deadlock and livelock?",
        "How does `ReentrantLock.tryLock` help?",
    ],
    followups=["Live lock vs deadlock?"],
) + q(
    "How do you diagnose deadlock in production?",
    "Medium", "2 min",
    "Thread dump (`jcmd <pid> Thread.print`, `jstack`) shows 'Found one Java-level deadlock' with cycle. JFR `jdk.JavaMonitorEnter` / lock events give timing.",
    "Prevention beats detection: consistent lock order, timeout locks, avoid nested locks across subsystems. Libraries like deadlock detectors in tests (cycle in lock graph).",
    interview_probes=[
        "Can you have deadlock without synchronized?",
        "Database deadlock vs JVM deadlock — same four conditions?",
    ],
) + interview_bank("Deadlock Interview Drill", [
    ("Transfer between two accounts — classic fix?", "Lock accounts in consistent order (e.g. by id)."),
    ("tryLock with timeout — what do you do on failure?", "Backoff, log, fail transaction, or ordered retry."),
])

PAGES["concurrent-collections"] = fm(
    "Concurrent Collections Interview Guide",
    "CHM, CopyOnWrite, BlockingQueue — when to use which.",
    "Concurrent Collections",
    3, "Concurrency", "3.8",
    aliases=["concurrent-collections-interview"],
) + q(
    "CHM vs Collections.synchronizedMap?",
    "Medium", "1 min",
    "CHM: bin-level locking/CAS — better write scalability. synchronizedMap: locks entire map per op.",
    "CHM forbids null keys/values. Weakly consistent iterators.",
    followups=["See ConcurrentHashMap Internals"],
) + q(
    "CopyOnWriteArrayList when?",
    "Medium", "1 min",
    "Read-mostly, rare writes, iterators must not throw ConcurrentModificationException.",
    "Write copies entire array — O(n). Good for listener lists, config snapshots. Bad for write-heavy metrics.",
) + q(
    "BlockingQueue for backpressure?",
    "Easy", "30 sec",
    "Bounded queue blocks producers when full — natural backpressure for thread pools.",
    "`ArrayBlockingQueue` fixed capacity; size from SLA and memory budget.",
)

PAGES["completablefuture-interview-guide"] = fm(
    "CompletableFuture Interview Guide",
    "Composition, executors, timeouts, exception handling.",
    "CompletableFuture",
    3, "Concurrency", "3.10",
    aliases=["async-completablefuture"],
) + q(
    "thenApply vs thenCompose?",
    "Medium", "1 min",
    "`thenApply`: map result to value. `thenCompose`: flatMap — function returns another CompletableFuture.",
    "Nested `get()` blocks — chain with thenCompose. Completion uses CAS on result stack (AltResult for exceptions).",
    production="Always pass explicit Executor for app work — not commonPool().",
    followups=["orTimeout / completeOnTimeout?", "exceptionally vs handle?"],
) + q(
    "CompletableFuture allOf vs anyOf?",
    "Medium", "1 min",
    "`allOf` completes when all complete (void aggregate). `anyOf` completes when first completes.",
    "Use `allOf` then join each future for batch fan-in. `anyOf` for racing redundant calls — cancel losers to avoid waste.",
    production="Set timeouts on each leg; do not block on `get()` without timeout in reactive services.",
    followups=["See [Virtual Threads](/java-engineering/virtual-threads-interview-guide/) for blocking style"],
) + q(
    "exceptionally vs handle?",
    "Medium", "1 min",
    "`exceptionally` only runs on failure and returns recovery value. `handle` runs always with (result, ex) — unified success/failure path.",
    "Prefer `handle` when both branches need same downstream type. `whenComplete` for side effects without transforming result.",
)

PAGES["virtual-threads-interview-guide"] = fm(
    "Virtual Threads Interview Guide",
    "Carriers, pinning, structured concurrency, ScopedValue vs ThreadLocal.",
    "Virtual Threads",
    3, "Concurrency", "3.11",
    aliases=["virtual-threads-structured-concurrency"],
) + q(
    "Platform vs virtual threads?",
    "Medium", "1 min",
    "Platform: 1:1 OS thread, ~MB stack. Virtual: JVM-scheduled, cheap — mount on carrier pool.",
    "Blocking IO on VT releases carrier when unmounted. Massive concurrency for thread-per-request without reactive rewrite.",
    followups=["What is pinning?", "Structured concurrency goal?"],
) + q(
    "What is thread pinning?",
    "Hard", "2 min",
    "Virtual thread blocks carrier when holding synchronized monitor or native code — limits scalability.",
    "ReentrantLock doesn't pin (usually). Monitor pinning improved in newer JDKs — still audit synchronized blocks on hot paths.",
    production="Review JDBC drivers, JNI, synchronized — use jfr pinning events.",
)

# --- JVM ---
PAGES["jvm-memory-gc-oom-guide"] = fm(
    "JVM Memory, GC & OOM Guide",
    "Heap regions, collectors, leaks, OOM types, and diagnosis.",
    "Memory & GC",
    4, "JVM", "4.1",
    aliases=["jvm-memory-and-gc", "memory-leaks-and-oom", "memory-diagram-interview", "gc-summary-interview"],
) + q(
    "Stack vs heap?",
    "Easy", "30 sec",
    "Stack: per-thread frames, primitives and references, automatic lifetime. Heap: shared objects, GC-managed.",
    "References on stack point to heap objects. Static field data lives in heap; class metadata in Metaspace.",
    "See [Memory Diagram Cheat Sheet](/java-engineering/memory-diagram-cheatsheet/).",
    followups=["Where do static fields live?"],
) + q(
    "Minor vs major GC?",
    "Medium", "1 min",
    "Minor: young gen (Eden/Survivor), frequent, usually short STW. Major/old: tenured collection — longer unless concurrent collector.",
    "Generational hypothesis: most objects die young. Promotion when survivors exceed age threshold.",
    "TLAB: per-thread Eden buffers reduce allocation contention.",
    followups=["G1 mixed GC?", "When ZGC over G1?"],
) + q(
    "G1 vs ZGC?",
    "Hard", "2 min",
    "G1: regional, balanced default. ZGC: sub-ms pauses, colored pointers, large heaps, more CPU/barrier cost.",
    "Tune with `-Xlog:gc*` and pause P99. Container: `-XX:MaxRAMPercentage`.",
    production="`-XX:+HeapDumpOnOutOfMemoryError` on persistent volume.",
    followups=["Shenandoah?", "Humongous objects in G1?"],
) + q(
    "Can you leak memory with a GC?",
    "Medium", "1 min",
    "Yes — logical leaks keep strong references (static maps, listeners, ThreadLocal, classloader chains).",
    "OOM types: heap, Metaspace, direct buffer, unable to create native thread.",
    followups=["See Reference Types", "ThreadLocal in pools"],
)

PAGES["jvm-internals"] = fm(
    "JVM Internals Interview Guide",
    "Bytecode pipeline, class loading overview, interpreter vs JIT entry points.",
    "JVM Internals",
    4, "JVM", "4.2",
    aliases=["jvm-internals-quick-ref"],
) + page_intro("""
The JVM loads `.class` files, verifies bytecode, interprets cold code, and **JIT-compiles** hot methods. Senior interviews connect class loading, verification, tiered compilation, and deoptimization.
""") + q(
    "Class loading phases?",
    "Medium", "2 min",
    "**Loading** → **Linking** (verify, prepare, resolve) → **Initialization** (`<clinit>`).",
    "**Loading:** read bytecode, create `Class` object in Metaspace. **Verify:** bytecode safety checks. **Prepare:** allocate static fields (default values). **Resolve:** symbolic references → direct (can be lazy). **Initialize:** run static initializers once per classloader.",
    "Parent loader must be initialized before child. `Class.forName(name, initialize=true, loader)` triggers init.",
    interview_probes=[
        "Can you load a class without initializing it?",
        "What runs first — static field init or static block?",
        "Difference between `ClassLoader.loadClass` and `Class.forName`?",
    ],
    followups=["See [ClassLoader Internals](/java-engineering/classloader-internals/)"],
) + q(
    "Interpreter vs JIT?",
    "Medium", "2 min",
    "Interpreter executes bytecode immediately with no compile wait; **JIT** compiles hot methods to native code for speed.",
    "Startup: interpreter + C1 quick compiles. Hot methods promoted to C2 with inlining, escape analysis, intrinsics. **On-Stack Replacement (OSR)** compiles long-running loops still in interpreter. Cold code stays interpreted — saves compile cost.",
    interview_probes=[
        "Why not JIT everything at startup?",
        "What is OSR and when does it matter?",
        "How would you detect JIT compilation in production?",
    ],
    followups=["See [JIT & Safepoints](/java-engineering/jit-escape-analysis-safepoints/)"],
) + q(
    "What is bytecode verification?",
    "Medium", "1–2 min",
    "Verifier checks class files at **link** time — stack map frames, type safety, valid control flow.",
    "Prevents stack underflow/overflow, illegal casts, and jumping into middle of instructions. Failure: `VerifyError`. Distinct from compile-time `javac` checks — JVM re-verifies untrusted bytecode.",
    mistakes=["Assuming `javac` success means no `VerifyError` at runtime for generated bytecode (agents, ASM)."],
    interview_probes=[
        "Why does Java need a verifier if javac already type-checks?",
        "What changed with stack map frames in Java 6+?",
    ],
) + q(
    "JIT C1 vs C2 compilers?",
    "Hard", "2–3 min",
    "C1 (client) compiles fast with fewer optimizations; C2 (server) compiles hot methods aggressively after profiling.",
    "Tiered compilation uses C1 for quick warmup, promotes to C2 for hot code. `-XX:TieredStopAtLevel` controls depth. **Deoptimization** reverts optimized code when assumptions fail (e.g., monomorphic call site becomes megamorphic).",
    production="Use JVM defaults on JDK 17+; avoid disabling tiered compilation without profiling evidence.",
    mistakes=[
        "Disabling JIT (`-Xint`) in production for debugging and forgetting to remove.",
        "Tuning C2 thresholds without JFR proof of compile storms.",
    ],
    interview_probes=[
        "What triggers deoptimization?",
        "Megamorphic call site — JIT impact?",
        "Difference between `-XX:CompileThreshold` and tiered levels?",
    ],
    followups=["See [JIT & Safepoints](/java-engineering/jit-escape-analysis-safepoints/)"],
) + q(
    "Constant pool and method area?",
    "Medium", "1 min",
    "Constant pool holds literals, class/method/field symbolic refs; lives in Metaspace with class metadata (Java 8+).",
    "String literals interned in pool (JDK 7+ on heap). Understanding pool helps explain `OutOfMemoryError: Metaspace` vs heap OOM.",
    interview_probes=[
        "Where do string literals live in modern JDK?",
        "What is `ldc` bytecode instruction?",
    ],
) + interview_bank("JVM Internals Interview Drill", [
    ("Name the three JVM class loaders in JDK 9+.", "Bootstrap (null), Platform (extension), Application (system)."),
    ("What tool shows compiled methods?", "`jcmd Compiler.queue` / JFR `jdk.CompilerPhase` / `-XX:+PrintCompilation`."),
    ("VerifyError vs NoClassDefFoundError?", "VerifyError: bad bytecode; NoClassDefFoundError: present at compile, missing/failed at runtime init."),
])

PAGES["classloader-internals"] = fm(
    "ClassLoader Internals",
    "Bootstrap, platform, application loaders, delegation model.",
    "ClassLoaders",
    4, "JVM", "4.3",
) + page_intro("""
Class loaders define **namespace boundaries** for classes. The **parent-delegation model** prevents replacing `java.lang.String` from application code and underpins modular isolation in containers and app servers.
""") + q(
    "Class loader delegation — why parent-first?",
    "Medium", "2 min",
    "Security and **single definition** — core JDK classes loaded once by bootstrap/platform loaders; app code cannot spoof `java.*`.",
    "Default: child asks parent to load; parent tries its parent up to bootstrap. Only if parent fails does child load from its own classpath. Tomcat/OSGi use **child-first** for web apps to isolate WAR dependencies.",
    interview_probes=[
        "Who loads `java.lang.Object`?",
        "How do you break parent delegation intentionally?",
        "Module path vs classpath — which loader?",
    ],
    followups=["How break delegation (OSGi, Tomcat)?"],
) + q(
    "Bootstrap vs Platform vs Application loader?",
    "Medium", "1–2 min",
    "**Bootstrap** (null `getClassLoader()`): `java.base` core classes. **Platform** (extension): JDK modules not in base. **Application** (system): application classpath/module path.",
    "JDK 9+ module system: loaders align with module layers. `ClassLoader.getSystemClassLoader()` returns application loader in most apps.",
    interview_probes=[
        "Can you instantiate BootstrapClassLoader?",
        "What loader loads JDBC driver from `META-INF/services`?",
    ],
) + q(
    "Custom classloader use cases?",
    "Hard", "2 min",
    "Hot reload, plugin architectures, bytecode generation (agents), isolating conflicting dependency versions.",
    "Must define `findClass` or delegate properly; leaking custom loaders retains all their classes (Metaspace leak). Always null out refs on undeploy.",
    production="Prefer JPMS layers or container isolation over hand-rolled loaders unless building a plugin platform.",
    interview_probes=[
        "What happens if same class name loaded by two loaders?",
        "How does `instanceof` interact with different loaders?",
    ],
) + interview_bank("ClassLoader Interview Drill", [
    ("Symptom: `ClassCastException` on same class name — cause?", "Same FQCN loaded by two different class loaders — types incompatible."),
    ("`Thread.contextClassLoader` purpose?", "Frameworks set it so libraries load classes from the right module/WAR."),
])

PAGES["classloader-memory-leaks"] = fm(
    "ClassLoader Memory Leaks",
    "WAR redeploy, static refs, Metaspace OOM in containers.",
    "CL Leaks",
    4, "JVM", "4.4",
) + q(
    "Why classloader leaks on WAR redeploy?",
    "Hard", "2 min",
    "Old classloader retained by static refs, ThreadLocal values, or lingering threads — classes not unloaded, Metaspace grows.",
    "Fix: undeploy hooks, remove listeners, clear ThreadLocals, avoid static collections holding app classes.",
    production="Monitor Metaspace in dynamic scripting (Groovy, JSR223).",
)

PAGES["jit-escape-analysis-safepoints"] = fm(
    "JIT, Escape Analysis & Safepoints",
    "C1/C2 tiers, stack allocation, safepoint STW operations.",
    "JIT & Safepoints",
    4, "JVM", "4.5",
) + q(
    "What is escape analysis?",
    "Hard", "2 min",
    "JIT determines if object escapes method/thread — non-escaping objects may be stack-allocated or scalar-replaced.",
    "Not guaranteed observable — don't rely on for correctness. Eliminates allocation for short-lived non-escaping objects.",
    followups=["Scalar replacement?"],
) + q(
    "What is a safepoint?",
    "Medium", "1 min",
    "Point where JVM can safely pause all threads for GC, deopt, JVMTI — not every bytecode instruction.",
    "Long counted loops poll safepoint. STW GC roots scanned at safepoint. Rare infinite loops without poll blocked GC in old bugs.",
)

PAGES["reference-types-interview"] = fm(
    "Reference Types Interview Guide",
    "Soft, weak, phantom references and Cleaner.",
    "References",
    4, "JVM", "4.6",
) + q(
    "Soft vs weak vs phantom?",
    "Medium", "2 min",
    "Soft: cleared before OOM — memory-sensitive cache. Weak: next GC — canonical mappings. Phantom: after finalize/enqueue — post-mortem cleanup.",
    "ReferenceQueue notifies when referent cleared. Prefer `Cleaner` over finalization (deprecated).",
    followups=["WeakHashMap behavior?", "PhantomReference use case?"],
)

# --- Platform ---
PAGES["reflection-interview"] = fm(
    "Reflection Interview Guide",
    "Runtime inspection, annotation retention, modules, performance.",
    "Reflection",
    5, "Platform APIs", "5.1",
    aliases=["reflection-annotations-ref"],
) + q(
    "Annotation retention SOURCE vs CLASS vs RUNTIME?",
    "Easy", "30 sec",
    "SOURCE: compile-only. CLASS: bytecode, not runtime reflection. RUNTIME: visible via reflection.",
    "Framework annotations (JPA, Spring) need RUNTIME. `@Override` is SOURCE.",
    followups=["Module opens for deep reflection?"],
) + q(
    "Reflection cost and mitigation?",
    "Medium", "1 min",
    "Method lookup expensive — cache MethodHandle, use compile-time annotation processing, Spring AOT.",
    "Modules (9+): `opens` package for frameworks. Prefer build-time indexing over classpath scanning.",
)

PAGES["serialization-interview"] = fm(
    "Serialization Interview Guide",
    "Serializable contract, serialVersionUID, safer alternatives.",
    "Serialization",
    5, "Platform APIs", "5.2",
    aliases=["serialization-quick-ref"],
) + q(
    "Why avoid Java serialization in new systems?",
    "Medium", "1 min",
    "Security (gadget chains), brittleness across versions, poor cross-language support.",
    "Prefer JSON, Protobuf, Avro. If required: `serialVersionUID`, whitelist ObjectInputFilter (9+).",
    followups=["Externalizable vs Serializable?"],
)

# --- Cheat sheets ---
PAGES["memory-diagram-cheatsheet"] = fm(
    "Memory Diagram (Cheat Sheet)",
    "One-screen stack, heap, metaspace, and object layout.",
    "Memory Diagram",
    6, "Interview Cheat Sheets", "6.2",
    aliases=["memory-diagram-interview"],
    cheat_sheet=True,
) + """
```mermaid
flowchart TB
  subgraph perThread [Per thread]
    stack[Stack - frames]
    pc[Program Counter]
  end
  subgraph shared [Shared]
    heap[Heap - Young / Old]
    meta[Metaspace]
    code[Code Cache]
  end
  stack --> heap
```

| Region | Stores | GC |
| :--- | :--- | :--- |
| Stack | Locals, refs | Auto on pop |
| Eden | New objects | Minor GC |
| Old | Tenured | Major / mixed |
| Metaspace | Class metadata | Class unloading |
| Direct | NIO buffers | Cleaner |

| Object (64b, compressed oops) | |
| :--- | :--- |
| Mark word | Hash, locks, GC age |
| Klass pointer | Class metadata |
| Fields | + padding |

**Deep dive:** [JVM Memory, GC & OOM Guide](/java-engineering/jvm-memory-gc-oom-guide/)
"""

PAGES["thread-lifecycle-cheatsheet"] = fm(
    "Thread Lifecycle (Cheat Sheet)",
    "Platform thread state diagram and virtual thread notes.",
    "Thread Lifecycle",
    6, "Interview Cheat Sheets", "6.3",
    aliases=["thread-lifecycle-interview"],
    cheat_sheet=True,
) + """
```mermaid
stateDiagram-v2
  [*] --> NEW
  NEW --> RUNNABLE: start
  RUNNABLE --> BLOCKED: monitor lock
  RUNNABLE --> WAITING: wait/join/park
  RUNNABLE --> TIMED_WAITING: sleep/timeout
  BLOCKED --> RUNNABLE: lock acquired
  WAITING --> RUNNABLE: notify/unpark
  TIMED_WAITING --> RUNNABLE: timeout
  RUNNABLE --> TERMINATED: run ends
```

| State | Cause |
| :--- | :--- |
| BLOCKED | Waiting for synchronized monitor |
| WAITING | `wait`, `join`, `park` — no timeout |
| TIMED_WAITING | `sleep`, timed `wait`/`join` |

| Platform vs Virtual | |
| :--- | :--- |
| Cost | ~MB stack vs cheap VT |
| Blocking IO | VT unmounts carrier; pinning if synchronized/native |

**Deep dive:** [Java Threading Interview Guide](/java-engineering/java-threading-interview-guide/)
"""

PAGES["java-version-migration-guide"] = fm(
    "Java Version Migration Guide",
    "LTS matrix, feature deltas, upgrade checkpoints, interview facts.",
    "Version Migration",
    6, "Interview Cheat Sheets", "6.5",
    aliases=["java-lts-release-matrix", "java-recent-features", "java-version-features-interview"],
    cheat_sheet=True,
) + """
| LTS | Headline features |
| :---: | :--- |
| 8 | Lambdas, streams, `Optional`, `java.time` |
| 11 | HTTP client, removed Java EE from JDK |
| 17 | Records, sealed, pattern `instanceof` |
| 21 | Virtual threads, sequenced collections, pattern switch |
| 25 | Current LTS upgrade target |

| Migration | Action |
| :--- | :--- |
| 8 → 11 | JAXB/JAX-WS modules, `jdeps` |
| 11 → 17 | `--add-opens` audit, strong encapsulation |
| 17 → 21 | Virtual threads pilot, pinning review |

| Post-17 adopt | Defer |
| :--- | :--- |
| Records, sealed ADTs | Preview features without flag plan |
| Virtual threads for IO | Foreign API without need |

---

""" + q(
    "Why LTS for enterprises?",
    "Easy", "30 sec",
    "Predictable vendor support, security patches, slower change absorption.",
    "Non-LTS every 6 months — only if you own upgrade cadence.",
)

# Top 100 - abbreviated but complete structure with 100 entries
TOP100_ROWS = [
    ("Why is String immutable?", "Easy", "Strings", "strings-and-enums-interview"),
    ("StringBuilder vs concat in loops?", "Easy", "Strings", "strings-and-enums-interview"),
    ("Enum vs int constants?", "Easy", "Enums", "strings-and-enums-interview"),
    ("Composition over inheritance?", "Medium", "OOP", "oop-interview"),
    ("Record vs class?", "Medium", "OOP", "oop-interview"),
    ("What is PECS?", "Medium", "Generics", "generics-interview"),
    ("Type erasure?", "Medium", "Generics", "generics-interview"),
    ("Checked vs unchecked exceptions?", "Easy", "Exceptions", "exceptions-interview"),
    ("equals/hashCode contract?", "Medium", "Object Contract", "object-contract-interview"),
    ("ArrayList vs LinkedList?", "Easy", "Collections", "collection-selection-matrix"),
    ("When LinkedHashMap?", "Medium", "Collections", "collection-selection-matrix"),
    ("HashMap internal structure?", "Hard", "Collections", "hashmap-internals"),
    ("HashMap vs TreeMap?", "Easy", "Collections", "map-implementations"),
    ("Why ConcurrentHashMap?", "Medium", "Collections", "concurrenthashmap-internals"),
    ("CHM vs synchronized HashMap?", "Medium", "Collections", "concurrent-collections"),
    ("CHM null policy?", "Easy", "Collections", "concurrenthashmap-internals"),
    ("CopyOnWrite when?", "Medium", "Collections", "concurrent-collections"),
    ("BlockingQueue purpose?", "Easy", "Collections", "concurrent-collections"),
    ("Why are streams lazy?", "Medium", "Streams", "streams-collectors-interview-guide"),
    ("Parallel stream when?", "Medium", "Streams", "streams-collectors-interview-guide"),
    ("reduce vs collect?", "Medium", "Streams", "streams-collectors-interview-guide"),
    ("Optional anti-patterns?", "Medium", "Streams", "streams-collectors-interview-guide"),
    ("BLOCKED vs WAITING?", "Medium", "Threading", "java-threading-interview-guide"),
    ("Thread pool sizing?", "Medium", "Threading", "java-threading-interview-guide"),
    ("shutdown vs shutdownNow?", "Easy", "Threading", "java-threading-interview-guide"),
    ("What is happens-before?", "Hard", "JMM", "java-memory-model"),
    ("volatile guarantees?", "Medium", "JMM", "java-memory-model"),
    ("Why volatile not enough for i++?", "Medium", "Concurrency", "locks-and-atomics"),
    ("synchronized vs ReentrantLock?", "Medium", "Concurrency", "locks-and-atomics"),
    ("What is CAS?", "Medium", "Concurrency", "cas-and-lock-free-programming"),
    ("ABA problem?", "Hard", "Concurrency", "cas-and-lock-free-programming"),
    ("LongAdder vs AtomicLong?", "Medium", "Concurrency", "cas-and-lock-free-programming"),
    ("ThreadLocal internals?", "Hard", "Concurrency", "threadlocal-internals"),
    ("ThreadLocal leak in pools?", "Medium", "Concurrency", "threadlocal-internals"),
    ("ForkJoinPool work-stealing?", "Hard", "Concurrency", "forkjoinpool-internals"),
    ("Deadlock four conditions?", "Medium", "Concurrency", "deadlock-detection"),
    ("CountDownLatch vs CyclicBarrier?", "Medium", "Coordination", "concurrent-coordination"),
    ("Semaphore use case?", "Easy", "Coordination", "concurrent-coordination"),
    ("thenApply vs thenCompose?", "Medium", "Async", "completablefuture-interview-guide"),
    ("CompletableFuture executor choice?", "Medium", "Async", "completablefuture-interview-guide"),
    ("Platform vs virtual threads?", "Medium", "Virtual Threads", "virtual-threads-interview-guide"),
    ("What is pinning?", "Hard", "Virtual Threads", "virtual-threads-interview-guide"),
    ("ScopedValue vs ThreadLocal?", "Medium", "Virtual Threads", "virtual-threads-interview-guide"),
    ("Stack vs heap?", "Easy", "JVM", "jvm-memory-gc-oom-guide"),
    ("Minor vs major GC?", "Medium", "JVM", "jvm-memory-gc-oom-guide"),
    ("Generational hypothesis?", "Medium", "JVM", "jvm-memory-gc-oom-guide"),
    ("G1 vs ZGC?", "Hard", "JVM", "jvm-memory-gc-oom-guide"),
    ("Memory leak with GC?", "Medium", "JVM", "jvm-memory-gc-oom-guide"),
    ("Metaspace OOM cause?", "Medium", "JVM", "classloader-memory-leaks"),
    ("Soft vs weak vs phantom?", "Medium", "JVM", "reference-types-interview"),
    ("Class loader delegation?", "Medium", "JVM", "classloader-internals"),
    ("Classloader leak on redeploy?", "Hard", "JVM", "classloader-memory-leaks"),
    ("Escape analysis?", "Hard", "JVM", "jit-escape-analysis-safepoints"),
    ("Safepoint purpose?", "Medium", "JVM", "jit-escape-analysis-safepoints"),
    ("JIT C1 vs C2?", "Medium", "JVM", "jvm-internals"),
    ("TLAB purpose?", "Medium", "JVM", "jvm-memory-gc-oom-guide"),
    ("-XX:MaxRAMPercentage?", "Easy", "JVM Flags", "jvm-flags-and-tuning"),
    ("Heap dump on OOM?", "Easy", "JVM Flags", "jvm-flags-and-tuning"),
    ("GC logging flag (11+)?", "Easy", "JVM Flags", "jvm-flags-and-tuning"),
    ("Reflection performance?", "Medium", "Platform", "reflection-interview"),
    ("Annotation RUNTIME vs SOURCE?", "Easy", "Platform", "reflection-interview"),
    ("Why avoid Java serialization?", "Medium", "Platform", "serialization-interview"),
    ("serialVersionUID purpose?", "Easy", "Platform", "serialization-interview"),
    ("Why LTS?", "Easy", "Versions", "java-version-migration-guide"),
    ("Java 17 headline features?", "Medium", "Versions", "java-version-migration-guide"),
    ("Java 21 headline features?", "Medium", "Versions", "java-version-migration-guide"),
    ("Primitives vs wrappers in hot loops?", "Easy", "Language", "language-fundamentals"),
    ("final on reference?", "Easy", "Language", "language-fundamentals"),
    ("Covariant arrays vs generics?", "Medium", "Language", "language-fundamentals"),
    ("Overloading vs overriding?", "Easy", "OOP", "oop-interview"),
    ("Sealed classes purpose?", "Medium", "OOP", "oop-interview"),
    ("Comparable vs Comparator?", "Easy", "Object Contract", "object-contract-interview"),
    ("HashMap load factor?", "Medium", "Collections", "hashmap-internals"),
    ("HashMap treeify threshold?", "Hard", "Collections", "hashmap-internals"),
    ("CHM sizeCtl?", "Hard", "Collections", "concurrenthashmap-internals"),
    ("WeakHashMap use case?", "Medium", "Collections", "map-implementations"),
    ("IdentityHashMap use case?", "Medium", "Collections", "map-implementations"),
    ("PriorityQueue iterator order?", "Easy", "Collections", "collection-selection-matrix"),
    ("fail-fast vs weakly consistent?", "Medium", "Collections", "concurrent-collections"),
    ("Spliterator characteristics?", "Hard", "Streams", "streams-collectors-interview-guide"),
    ("Collectors.toMap merge function?", "Easy", "Streams", "streams-collectors-interview-guide"),
    ("Effectively final in lambdas?", "Easy", "Streams", "streams-collectors-interview-guide"),
    ("Thread.start happens-before run?", "Easy", "JMM", "java-memory-model"),
    ("Double-checked locking fix?", "Hard", "JMM", "java-memory-model"),
    ("ReadWriteLock when?", "Medium", "Concurrency", "locks-and-atomics"),
    ("StampedLock optimistic read?", "Hard", "Concurrency", "locks-and-atomics"),
    ("False sharing?", "Hard", "Concurrency", "locks-and-atomics"),
    ("VarHandle purpose?", "Hard", "Concurrency", "locks-and-atomics"),
    ("AtomicReference use case?", "Medium", "Concurrency", "cas-and-lock-free-programming"),
    ("Phaser vs CyclicBarrier?", "Hard", "Coordination", "concurrent-coordination"),
    ("CompletableFuture allOf vs anyOf?", "Medium", "Async", "completablefuture-interview-guide"),
    ("Structured concurrency goal?", "Medium", "Virtual Threads", "virtual-threads-interview-guide"),
    ("Object layout mark word?", "Hard", "JVM", "memory-diagram-cheatsheet"),
    ("Compressed oops?", "Medium", "JVM", "memory-diagram-cheatsheet"),
    ("Direct buffer OOM?", "Medium", "JVM", "jvm-memory-gc-oom-guide"),
    ("Card table / remembered set?", "Hard", "JVM", "jvm-memory-gc-oom-guide"),
    ("Humongous object in G1?", "Hard", "JVM", "jvm-memory-gc-oom-guide"),
    ("Shenandoah vs ZGC?", "Hard", "JVM", "jvm-memory-gc-oom-guide"),
    ("Deoptimization in JIT?", "Hard", "JVM", "jvm-internals"),
    ("javac --release vs target?", "Medium", "Versions", "java-version-migration-guide"),
    ("Module opens vs exports?", "Medium", "Platform", "reflection-interview"),
    ("Cleaner vs finalization?", "Medium", "JVM", "reference-types-interview"),
    ("String intern() cost?", "Medium", "Strings", "strings-and-enums-interview"),
    ("Text blocks (15+)?", "Easy", "Strings", "strings-and-enums-interview"),
    ("try-with-resources suppression?", "Medium", "Exceptions", "exceptions-interview"),
    ("Arrays.asList vs List.of?", "Easy", "Collections", "collection-selection-matrix"),
    ("NavigableMap floorKey?", "Medium", "Collections", "map-implementations"),
    ("Record serialization concerns?", "Medium", "OOP", "oop-interview"),
]

top100_body = fm(
    "Top 100 Java Interview Questions",
    "Index of high-signal Java interview questions with difficulty, topic, and deep-dive links.",
    "Top 100",
    6, "Interview Cheat Sheets", "6.1",
) + """
Curated questions for **6+ year** Java engineers. Each links to a detailed interview page.

| # | Question | Difficulty | Topic | Deep Dive |
| --: | :--- | :--- | :--- | :--- |
"""
for i, (question, diff, topic, slug) in enumerate(TOP100_ROWS, 1):
    top100_body += f"| {i} | {question} | {diff} | {topic} | [{slug.replace('-', ' ').title()}](/java-engineering/{slug}/) |\n"

PAGES["top-100-java-interview-questions"] = top100_body


def main() -> None:
    CONTENT.mkdir(parents=True, exist_ok=True)
    for slug, body in PAGES.items():
        path = CONTENT / f"{slug}.md"
        path.write_text(body, encoding="utf-8")
        print(f"Wrote {path.name}")
    print(f"\nGenerated {len(PAGES)} pages.")


if __name__ == "__main__":
    main()
