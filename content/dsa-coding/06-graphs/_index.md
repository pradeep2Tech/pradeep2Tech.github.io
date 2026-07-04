---
title: "Graphs"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Graphs"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Graphs"
module: 6
moduleTitle: "DSA & Coding"
sectionRef: "6.0"
weight: 600
ShowToc: true
interviewHandbook: true
---

# Graphs

> **Canonical home** for grid/graph DFS, BFS shortest path, multi-source BFS, union-find style connectivity.

---

## Overview

Nodes and edges — flood-fill, level BFS, or disjoint connectivity.

---

## Recognition Signals

- Islands, provinces, closed islands
- Shortest steps in unweighted grid
- Multi-source spread (rotten oranges)
- Maze exit

---

## When To Use / When NOT To Use

**Use:** adjacency or implicit grid graph. **Not:** weighted shortest path (Dijkstra — outside scope); tree-only → Module 5.

---

## Problem Solving Framework

| Goal | Technique |
| :--- | :--- |
| Components | DFS flood-fill |
| Shortest path | BFS |
| Multi-source | enqueue all sources |

---

## Complexity Analysis

O(V+E) or O(mn) on grid.

---

## Common Mistakes

- DFS for shortest path
- Not marking visited before enqueue

---


---

## Interviewer Perspective

- **DFS vs BFS** must be justified: components vs shortest unweighted path.
- Multi-source BFS (rotten oranges) — expect enqueue **all sources** at t=0.
- Grid problems: 4 vs 8 directions, in-place marking vs visited set.

---

## Common Failure Modes

| Failure | Symptom | Fix |
| :--- | :--- | :--- |
| DFS for shortest path | Wrong step count | BFS on unweighted graph |
| Visit after dequeue | Duplicate processing | Mark visited **before** enqueue |
| Not clone grid | Corrupts input | Copy or restore marks |
| Miss multi-source init | Off-by-one rounds | Seed queue with all sources |
| Islands count wrong | Double count | Flood-fill entire component once |

---

## Architect Notes

- Flood-fill = **reachability analysis** — network zones, permission propagation, image regions.
- BFS layers = **synchronous rounds** — gossip protocols, epidemic spread (rotten oranges).
- Union-Find alternative for dynamic connectivity — not in problem set but worth mentioning in discussion.

---

## Representative Problems

[Number of Islands](/dsa-coding/06-graphs/number-of-islands/) · [Rotten Oranges](/dsa-coding/06-graphs/rotten-oranges/) · [Shortest Path Binary Matrix](/dsa-coding/06-graphs/shortest-path-in-binary-matrix/)

---

## Related Patterns

- [Advanced graphs](/dsa-coding/07-advanced-graphs/) for topo sort
- [Graph quick revision](/dsa-coding/11-interview-pattern-cheatsheets/07-graph-cheatsheet/)

---

## Quick Revision Notes

- **Connected:** DFS.
- **Shortest unweighted:** BFS.
- **Multi-source:** BFS from all seeds.

## Problems in This Module

| # | Problem | Pattern |
| :---: | :--- | :--- |
| 40 | [Rotten Oranges](/dsa-coding/06-graphs/rotten-oranges/) | Multi-Source BFS |
| 41 | [Number of Islands](/dsa-coding/06-graphs/number-of-islands/) | DFS |
| 42 | [Number of Provinces](/dsa-coding/06-graphs/number-of-provinces/) | DFS |
| 43 | [Graph Valid Tree](/dsa-coding/06-graphs/graph-valid-tree/) | DFS/BFS |
| 44 | [Shortest Path in Binary Matrix](/dsa-coding/06-graphs/shortest-path-in-binary-matrix/) | BFS |
| 45 | [Nearest Exit from Entrance in Maze](/dsa-coding/06-graphs/nearest-exit-from-maze/) | BFS |
| 46 | [Time Needed to Inform All Employees](/dsa-coding/06-graphs/time-needed-to-inform-employees/) | BFS/DFS on Tree |
| 47 | [Number of Closed Islands](/dsa-coding/06-graphs/number-of-closed-islands/) | DFS |

---

## See Also

- [Previous: Maximum Level Sum of a Binary Tree](/dsa-coding/05-trees/maximum-level-sum-binary-tree/)
- [Next: Rotten Oranges](/dsa-coding/06-graphs/rotten-oranges/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
