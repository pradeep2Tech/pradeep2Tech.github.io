---
title: "Java Engineering Handbook"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Interview-focused Java handbook for senior engineers — collections internals, concurrency, JVM/GC, and Top 100 questions. Java 8–25."
tags: ["java", "java-engineering", "handbook", "interview", "jvm"]
categories: ["Java Engineering Handbook"]
ShowPageNums: true
---

Dense **interview handbook** for senior engineers, leads, and architects — not a beginner tutorial. Questions first, production notes included, duplicate cheat sheets removed.

**36 pages** · **6 modules** · Target JDK **8 → 25**

---

## Who This Is For

| You are… | Start here |
| :--- | :--- |
| **Interview prep (6+ years)** | [Top 100 Questions](/java-engineering/top-100-java-interview-questions/) |
| **Interview prep (coding)** | [DSA & Coding](/dsa-coding/) → [Top 30 Must-Solve](/dsa-coding/09-interview-guide/top-30-must-solve/) → [Pattern Cheat Sheets](/dsa-coding/11-interview-pattern-cheatsheets/01-two-pointers-cheatsheet/) |
| **Staff engineer / architect** | [HashMap Internals](/java-engineering/hashmap-internals/) → [JVM Memory & GC](/java-engineering/jvm-memory-gc-oom-guide/) → [JVM Flags](/java-engineering/jvm-flags-and-tuning/) |
| **Concurrency deep dive** | [Java Threading](/java-engineering/java-threading-interview-guide/) → [JMM](/java-engineering/java-memory-model/) → [Virtual Threads](/java-engineering/virtual-threads-interview-guide/) |
| **Quick revision** | [Memory Diagram](/java-engineering/memory-diagram-cheatsheet/) · [Thread Lifecycle](/java-engineering/thread-lifecycle-cheatsheet/) · [Collections Big-O](/java-engineering/collections-complexity/) |

{{% note %}}
Spring Boot and design patterns live in **other handbook sections** — this track is **Java language + JVM platform**. For coding interview patterns (HashMap, two pointers, DP), see [DSA & Coding](/dsa-coding/).
{{% /note %}}

---

## Module Map

| # | Module | Pages | Focus |
| :--: | :--- | :---: | :--- |
| 1 | Language Fundamentals | 7 | Primitives, strings, OOP, generics, exceptions, streams |
| 2 | Collections | 4 | Selection matrix, HashMap/CHM internals, maps |
| 3 | Concurrency | 11 | Threading, JMM, CAS, coordination, CF, virtual threads |
| 4 | JVM | 7 | Memory/GC/OOM, class loaders, JIT, references, flags |
| 5 | Platform APIs | 2 | Reflection, serialization |
| 6 | Interview Cheat Sheets | 5 | Top 100, diagrams, Big-O, version migration |

---

## Page Format

Depth pages use a consistent interview structure:

**Question** → **Short Answer** → **Detailed Explanation** → **Internal Working** → **Production Notes** → **Common Mistakes** → **Follow-up Questions**

Difficulty and answer time are on the [Top 100 index](/java-engineering/top-100-java-interview-questions/) only.

Cheat sheets are one-screen tables and diagrams with links to depth pages.

---

## LTS at a Glance

| LTS | Why it still matters |
| :---: | :--- |
| **8** | Largest legacy bytecode base; lambda baseline |
| **11** | HTTP client; dropped Java EE from JDK |
| **17** | Records, sealed classes, strong encapsulation |
| **21** | Virtual threads — changes default concurrency model |
| **25** | Current long-term upgrade target |

Full guide: [Java Version Migration](/java-engineering/java-version-migration-guide/)

---

Browse the **Table of Contents** below for all pages with section numbers.
