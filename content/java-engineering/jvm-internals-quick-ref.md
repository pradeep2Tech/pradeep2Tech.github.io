---
title: "JVM Internals Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Class loaders, JIT tiers, bytecode pipeline, and safepoints."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "JVM Internals"
module: 8
moduleTitle: "JVM"
sectionRef: "8.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Load → Link (verify, prepare, resolve) → Initialize.
- Bootstrap → Platform → Application class loaders delegation model.
- JIT: C1 (fast compile) → C2 (aggressive opt) — tiered compilation.
- Safepoints: STW operations (GC, deopt, JVMTI) — not every bytecode.

---

## Reference Tables

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

---

## Snippets

```bash
java -XX:+PrintCompilation -jar app.jar   # legacy style
java -XX:StartFlightRecording=settings=profile -jar app.jar
```

---

## Internals & Gotchas

- Escape analysis may stack-allocate non-escaping objects (not guaranteed).
- Inlining driven by hotness — `-XX:MaxInlineLevel`.
- Deoptimization on invalidated assumptions (e.g. monomorphic call site becomes megamorphic).

---

## Production Notes

- Avoid giant class loaders reloading same classes — Metaspace churn.
- Warm up JIT before latency benchmarks.
- Module path (9+) reduces illegal reflective access — plan opens for frameworks.

---

## Interview Probes


{< interview-answer >}
**Q:** Class loader delegation why?

**A:** Parent-first prevents core class spoofing; child sees parent definitions — security + single definition principle.
{< /interview-answer >}

{< interview-answer >}
**Q:** Safepoint bias?

**A:** Long counted loops may poll safepoint — rare infinite loop without safepoint blocks GC in old JDK bugs; know `CompileCommand` escape hatches.
{< /interview-answer >}

---

## See Also

- [Previous: Leaks & OOM](/java-engineering/memory-leaks-and-oom/)
- [Next: JVM Flags](/java-engineering/jvm-flags-and-tuning/)
- [Java Engineering Handbook Index](/java-engineering/)
