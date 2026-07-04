---
title: "Advanced Graphs"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Adv. Graphs"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Adv. Graphs"
module: 7
moduleTitle: "DSA & Coding"
sectionRef: "7.0"
weight: 700
interviewHandbook: true
---

# Advanced Graphs

> **Canonical home** for topological order and graph modeling from trees (distance K).

---

## Overview

Ordering with dependencies; treat tree as graph when parent links insufficient.

---

## Recognition Signals

- Alien dictionary / course schedule style ordering
- Distance K from target in tree → build parent graph + BFS

---

## Core Algorithms

Kahn's algorithm or DFS post-order for topo. Tree: hash parents then BFS from source.

---


---

## Interviewer Perspective

- Topological sort: detect **cycle** — if indegree queue empties before all nodes processed, no valid order.
- Alien dictionary: build graph from **adjacent character pairs**, not full lex sort.
- Tree distance K: expect **parent map + BFS**, not only child pointers.

---

## Common Failure Modes

| Failure | Symptom | Fix |
| :--- | :--- | :--- |
| Cycle undetected | Partial topo order | Track processed count vs n |
| Wrong edge direction | Invalid order | First differing char defines edge |
| BFS from wrong node | Miss distance K | Build undirected parent graph first |
| Overbuild graph | Too many edges | Only compare adjacent words |

---

## Architect Notes

- Topo sort = **build/deployment ordering** — tasks with dependencies (CI pipelines, migrations).
- Character precedence graph models **partial orders** — weaker than full sort, stronger than equality.
- Treating trees as graphs unifies **bidirectional traversal** when parent links are missing.

---

## Representative Problems

[Alien Dictionary](/dsa-coding/07-advanced-graphs/alien-dictionary/) · [All Nodes Distance K](/dsa-coding/07-advanced-graphs/all-nodes-distance-k-in-binary-tree/)

---

## Quick Revision Notes

- **Topo:** indegree queue or DFS finish times.
- **Tree as graph:** parent map + BFS.

## Problems in This Module

| # | Problem | Pattern |
| :---: | :--- | :--- |
| 48 | [Alien Dictionary](/dsa-coding/07-advanced-graphs/alien-dictionary/) | Topological Sort |
| 49 | [All Nodes Distance K in Binary Tree](/dsa-coding/07-advanced-graphs/all-nodes-distance-k-in-binary-tree/) | Graph + BFS |

---

## See Also

- [Previous: Number of Closed Islands](/dsa-coding/06-graphs/number-of-closed-islands/)
- [Next: Alien Dictionary](/dsa-coding/07-advanced-graphs/alien-dictionary/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
