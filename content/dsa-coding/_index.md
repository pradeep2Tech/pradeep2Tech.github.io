---
title: "DSA & Coding"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "55 canonical coding interview problems — HashMap, sliding window, binary search, trees, graphs, and DP. Java and Go solutions."
tags: ["dsa", "algorithms", "coding-interview"]
ShowPageNums: true
---

Interview-focused DSA curriculum — **55 problems** across **8 pattern modules**, with Java and Go implementations. Pairs with [Java Engineering](/java-engineering/) (collections complexity) and [Design Patterns](/design-patterns/) (LLD).

**Status:** Published — 82 topics (55 problems + guides + cheat sheets). Content consolidated with canonical module primers.

---

## Start Here (Senior Engineers)

| Resource | Purpose |
| :--- | :--- |
| [Interview Problem-Solving Framework](/dsa-coding/09-interview-guide/interview-problem-solving-framework/) | 11-step interview flow |
| [Pattern Recognition Table](/dsa-coding/09-interview-guide/pattern-recognition-table/) | Signal → pattern → module routing |
| [Pattern Selection Matrix](/dsa-coding/09-interview-guide/pattern-selection-matrix/) | Problem type → pattern decision grid |
| [Complexity Decision Framework](/dsa-coding/09-interview-guide/complexity-decision-framework/) | Constraint → target complexity |
| [60-Second Pattern Recognition](/dsa-coding/09-interview-guide/60-second-pattern-recognition/) | Final cram sheet before interviews |

---

## Module Map

| # | Module | Problems | Focus |
| :---: | :--- | :---: | :--- |
| 1 | [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) | 12 | HashMap, two pointers, palindrome expand |
| 2 | [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) | 8 | Fixed/variable window, prefix arrays |
| 3 | [Binary Search](/dsa-coding/03-binary-search/) | 6 | Classic, rotated, search on answer |
| 4 | [Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/) | 6 | Subsets, combinations, grid search |
| 5 | [Trees](/dsa-coding/05-trees/) | 7 | DFS, BFS, BST |
| 6 | [Graphs](/dsa-coding/06-graphs/) | 8 | Islands, BFS shortest path |
| 7 | [Advanced Graphs](/dsa-coding/07-advanced-graphs/) | 2 | Topological sort, tree-as-graph |
| 8 | [Dynamic Programming](/dsa-coding/08-dynamic-programming/) | 6 | 1D, grid, unbounded knapsack |
| 9 | [Interview Guide](/dsa-coding/09-interview-guide/interview-problem-solving-framework/) | — | Framework, recognition table, templates |
| 10 | [Learning Paths](/dsa-coding/10-learning-paths/dsa-senior-engineer-path/) | — | Senior + 48h revision paths |
| 11 | [Pattern Cheat Sheets](/dsa-coding/11-interview-pattern-cheatsheets/01-two-pointers-cheatsheet/) | 8 | Quick revision — links to module primers |

---

## Pattern Cheat Sheets (Module 11)

Quick revision only — full theory in module primers (Modules 1–8):

| Sheet | Focus |
| :--- | :--- |
| [Two Pointers](/dsa-coding/11-interview-pattern-cheatsheets/01-two-pointers-cheatsheet/) | Sorted pairs, palindrome scan |
| [Sliding Window](/dsa-coding/11-interview-pattern-cheatsheets/02-sliding-window-cheatsheet/) | Fixed & variable window |
| [Prefix Sum](/dsa-coding/11-interview-pattern-cheatsheets/03-prefix-sum-cheatsheet/) | Range sums, pivot |
| [Binary Search](/dsa-coding/11-interview-pattern-cheatsheets/04-binary-search-cheatsheet/) | Classic & answer space |
| [Backtracking](/dsa-coding/11-interview-pattern-cheatsheets/05-backtracking-cheatsheet/) | Choose / recurse / undo |
| [Trees](/dsa-coding/11-interview-pattern-cheatsheets/06-tree-cheatsheet/) | DFS & BFS |
| [Graphs](/dsa-coding/11-interview-pattern-cheatsheets/07-graph-cheatsheet/) | Flood-fill & shortest path |
| [DP](/dsa-coding/11-interview-pattern-cheatsheets/08-dp-cheatsheet/) | 1D, grid, knapsack |

---

## Quick Start

| Goal | Start here |
| :--- | :--- |
| **Interview flow** | [Problem-Solving Framework](/dsa-coding/09-interview-guide/interview-problem-solving-framework/) |
| **Pattern triage** | [Pattern Recognition Table](/dsa-coding/09-interview-guide/pattern-recognition-table/) |
| **Pattern cram** | [Two Sum](/dsa-coding/01-arrays-hashmap-two-pointers/two-sum/) → [3Sum](/dsa-coding/01-arrays-hashmap-two-pointers/3sum/) |
| **Sliding window** | [Longest Substring Without Repeating](/dsa-coding/02-sliding-window-prefix-sum/longest-substring-without-repeating-characters/) |
| **48-hour revision** | [Interview Revision Path](/dsa-coding/10-learning-paths/dsa-interview-revision-path/) |
| **Full bank** | [Top 55 Interview Questions](/dsa-coding/09-interview-guide/top-55-interview-questions/) |

---

## Page Format

| Section | Purpose |
| :--- | :--- |
| **Problem Statement** | Restated with constraints |
| **Pattern** | Technique selection rationale |
| **Approach** | Brute force → optimal |
| **Implementation** | Java + Go (`impl-tabs`) |
| **Complexity** | Time and space |
| **Edge Cases** | What breaks naive code |
| **Follow-up Questions** | Next interviewer probes |

---

## Regenerate

```bash
python scripts/build_dsa_coding_handbook.py   # sync yaml registry + prune orphans
hugo --minify
```

---

## See Also

- [Java Engineering](/java-engineering/) — HashMap, streams, concurrency
- [Design Patterns](/design-patterns/) — LLD and GoF patterns
- [Interview Prep](/interview-prep/) — cross-domain question banks
