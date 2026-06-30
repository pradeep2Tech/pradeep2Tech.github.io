---
title: "Go Cheat Sheet"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Go language quick reference — syntax, types, concurrency, sync primitives, modules, and interview probes."
tags: ["golang", "go", "golang-cheatsheet", "handbook", "cheat-sheet"]
categories: ["Go Cheat Sheet"]
ShowPageNums: true
---

Dense **cheat sheets** for engineers who already know Go — syntax recap, copy-paste snippets, and concurrency gotchas. Pairs with [Design Patterns](/design-patterns/) for Go implementations and [Microservices](/microservices/) for distributed service patterns.

**25 pages** · **10 modules** · Target Go **1.22+**

Start with [Language Basics](/golang-cheatsheet/language-basics/) — syntax, types, zero values, and variables on one page.

---

## Who This Is For

| You are… | Start here |
| :--- | :--- |
| **Backend engineer** | [Language Basics](/golang-cheatsheet/language-basics/) → [Error Handling](/golang-cheatsheet/error-handling/) → [Goroutines](/golang-cheatsheet/goroutines/) |
| **Java/Kotlin dev learning Go** | [Interfaces](/golang-cheatsheet/interfaces/) · [Slices](/golang-cheatsheet/slices/) · [Pointers](/golang-cheatsheet/pointers/) |
| **Interview prep** | [Interview Questions](/golang-cheatsheet/interview-questions/) + Module 5–6 concurrency |

{{% note %}}
Spring Boot, Kubernetes, and system design case studies live in **other handbook sections** — this is **Go language + runtime** only.
{{% /note %}}

---

## Module Map

| # | Module | Pages | Focus |
| :--: | :--- | :---: | :--- |
| 1 | Language Basics | 2 | Language basics (clubbed), functions |
| 2 | Types & Structs | 4 | Structs, interfaces, pointers, methods |
| 3 | Packages & Errors | 2 | Layout, exports, `error` idioms |
| 4 | Collections | 3 | Slices, arrays, maps |
| 5 | Concurrency | 4 | Goroutines, channels, select, context |
| 6 | Synchronization | 3 | Mutex, RWMutex, sync package |
| 7 | Testing & Reflection | 2 | Table tests, benchmarks, reflect |
| 8 | Runtime | 2 | Memory model, GC |
| 9 | Modules & Tooling | 2 | go.mod, dependency management |
| 10 | Interview | 1 | High-signal probes |

---

## Page Format

Every sheet uses the same scan-friendly layout:

| # | Section |
| :---: | :--- |
| 1 | At a Glance |
| 2 | Reference Tables |
| 3 | Snippets |
| 4 | Internals & Gotchas |
| 5 | Production Notes |
| 6 | See Also |

**Executive Summary** → **Core Concepts** → **Quick Reference** → **Snippets** → **Common Gotchas** → **Related Topics**

No long tutorials. Tables and code blocks first.

---

## Regenerate

```bash
python scripts/build_golang_cheatsheet.py
```

Module structure lives in `data/golang_cheatsheet_modules.yaml`. Page bodies are in `PAGE_BODIES` inside the build script unless you hand-edit markdown (hand edits overwritten on regen).
