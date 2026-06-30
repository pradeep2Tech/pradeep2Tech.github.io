---
title: "Java Engineering Handbook"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Architect-grade Java quick reference — collections internals, concurrency, JVM/GC, LTS matrix, and interview one-pagers. Java 8–25."
tags: ["java", "java-engineering", "handbook", "jvm", "cheat-sheet"]
categories: ["Java Engineering Handbook"]
ShowPageNums: true
---

Dense **cheat sheets** for senior engineers and architects — not a language tutorial. Basics are **clubbed** into one-pagers; depth sits where production decisions happen: **collections internals**, **concurrency**, **memory/GC**, **JVM flags**, and **LTS upgrades**.

**35 pages** · **11 modules** · Target JDK **8 → 25**

---

## Who This Is For

| You are… | Start here |
| :--- | :--- |
| **Architect / 15+ years** | [Collections Decision Matrix](/java-engineering/collections-decision-matrix/) → [JVM Flags](/java-engineering/jvm-flags-and-tuning/) → [LTS Matrix](/java-engineering/java-lts-release-matrix/) |
| **Staff engineer in review** | [HashMap Internals](/java-engineering/hashmap-internals/) · [Virtual Threads](/java-engineering/virtual-threads-structured-concurrency/) · [CHM Internals](/java-engineering/concurrenthashmap-internals/) |
| **Interview prep (no coding)** | Module 11 — [Collections Complexity](/java-engineering/collections-complexity/) and siblings |

{{% note %}}
Spring, Hibernate, Maven, design patterns, and DSA live in **other handbook sections** — this is **Java language + JVM platform** only.
{{% /note %}}

---

## Module Map

| # | Module | Pages | Focus |
| :--: | :--- | :---: | :--- |
| 1 | Language Essentials | 2 | Types, control flow, strings, enums — **clubbed basics** |
| 2 | OOP | 2 | Inheritance, records/sealed, `equals`/`hashCode` contract |
| 3 | Collections | 6 | Decision matrices + **HashMap / CHM internals** |
| 4 | Exceptions & Generics | 2 | Checked vs unchecked, PECS, erasure gotchas |
| 5 | Functional & Streams | 2 | Lambdas, collectors, parallel stream caveats |
| 6 | Concurrency | 5 | Executors, locks, coordination, **virtual threads** |
| 7 | Memory & GC | 2 | Generations, collectors, OOM, leaks |
| 8 | JVM | 2 | Class loading, JIT, **startup flags & tuning** |
| 9 | Modern Java | 2 | **LTS matrix** + recent non-LTS rollup |
| 10 | Platform APIs | 3 | NIO, reflection, serialization (when to avoid Java ser) |
| 11 | Interview Cheat Sheets | 7 | One-screen tables — complexity, GC, thread states |

---

## Page Format

Every sheet uses the same scan-friendly layout:

**At a Glance** → **Reference Tables** → **Snippets** → **Internals & Gotchas** → **Production Notes** → **Interview Probes** → **See Also**

No long tutorials. Tables and decision matrices first.

---

## JDK vs JRE vs JVM

| Term | Architect takeaway |
| :--- | :--- |
| **JVM** | Runs bytecode; owns GC, JIT, threads — tune here |
| **JDK** | Compiler + tools + runtime — what CI and dev machines install |
| **JRE** | Legacy term; use **jlink** images or full JDK in containers |

---

## LTS at a Glance

| LTS | Why it still matters |
| :---: | :--- |
| **8** | Largest legacy bytecode base; lambda baseline |
| **11** | HTTP client; dropped Java EE from JDK |
| **17** | Records, sealed classes, strong encapsulation |
| **21** | Virtual threads — changes default concurrency model |
| **25** | Current long-term upgrade target |

Full matrix: [Java LTS Release Matrix](/java-engineering/java-lts-release-matrix/)

---

Browse the **Table of Contents** below for all pages with section numbers.
