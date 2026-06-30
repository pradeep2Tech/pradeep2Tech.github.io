---
title: "Memory Diagram (Interview)"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Stack, heap, metaspace, TLAB, and object layout talking points."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Memory Diagram"
module: 11
moduleTitle: "Interview Cheat Sheets"
sectionRef: "11.6"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Stack: frames, locals, operand stack per thread.
- Heap: objects, arrays — shared across threads.
- Metaspace: class metadata (post-8).
- Off-heap: direct buffers, mapped files.

---

## Reference Tables

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

---

## Snippets

```java
// stack: primitives and references
// heap: new Object()
Object o = new Object();
```

---

## Internals & Gotchas

- TLAB allocation in Eden reduces contention.
- Escape analysis may scalar-replace — not guaranteed observable.
- `-XX:+UseCompressedOops` default on 64-bit heaps <32GB.

---

## Production Notes

- Thread stack size `-Xss` matters at thousands of platform threads — not virtual threads.
- Monitor Metaspace in dynamic class loaders (Groovy, JSR223).

---

## Interview Probes


{< interview-answer >}
**Q:** Stack vs heap?

**A:** Stack: thread-local frames, automatic lifetime. Heap: shared objects, GC-managed — references on stack point to heap objects.
{< /interview-answer >}

{< interview-answer >}
**Q:** Where do static fields live?

**A:** Field data in heap inside class mirror; metadata in Metaspace — static references are heap objects.
{< /interview-answer >}

---

## See Also

- [Previous: Version Features](/java-engineering/java-version-features-interview/)
- [Next: Thread Lifecycle](/java-engineering/thread-lifecycle-interview/)
- [Java Engineering Handbook Index](/java-engineering/)
