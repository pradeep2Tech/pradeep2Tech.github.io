---
title: "Trees"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Trees"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Trees"
module: 5
moduleTitle: "DSA & Coding"
sectionRef: "5.0"
weight: 500
interviewHandbook: true
---

# Trees

> **Canonical home** for tree DFS/BFS, BST properties, and level-order processing.

---

## Overview

Hierarchical data — recurse on children or queue by level.

---

## Recognition Signals

- Path sum / root-to-leaf
- BST validity / LCA on BST
- Level order / zigzag / right-side view / width

---

## When To Use / When NOT To Use

**Use:** explicit tree input. **Not:** arbitrary graph cycles → Module 6.

---

## Problem Solving Framework

DFS for paths and BST bounds; BFS for level metrics. Pass min/max down BST.

---

## Core Algorithms

DFS pre/in/post; BFS with queue size per level.

---

## Complexity Analysis

O(n) time, O(h) stack or O(w) queue.

---

## Common Mistakes

- BST check without min/max range
- Null handling on empty tree

---


---

## Interviewer Perspective

- BST questions require **range propagation** (min/max bounds), not just local `left < root < right`.
- Level-order vs DFS: expect you to pick BFS when **depth/width** matters.
- Follow-up: iterative vs recursive, null handling, skewed tree stack overflow.

---

## Common Failure Modes

| Failure | Symptom | Fix |
| :--- | :--- | :--- |
| BST check local only | Miss invalid deep node | Pass `(min, max)` down |
| Null root | NPE | Guard `if (root == null)` |
| Global variable for path | Fragile recursion | Return value from DFS |
| BFS without level size | Wrong level metrics | Snapshot `queue.size()` per level |
| Confuse tree with graph | Cycle assumptions | Trees have no back-edges |

---

## Architect Notes

- Tree DFS = **hierarchical delegation** — aggregate from leaves (sums, heights).
- BFS = **level-by-level fan-out** — org charts, dependency levels, cache warming by depth.
- BST invariant enables O(h) search — degraded to O(n) when unbalanced; production uses balanced trees.

---

## Representative Problems

[Path Sum](/dsa-coding/05-trees/path-sum/) · [Validate BST](/dsa-coding/05-trees/validate-binary-search-tree/) · [Right Side View](/dsa-coding/05-trees/binary-tree-right-side-view/)

---

## Related Patterns

- [Graphs](/dsa-coding/06-graphs/) for general graphs
- [Tree quick revision](/dsa-coding/11-interview-pattern-cheatsheets/06-tree-cheatsheet/)

---

## Quick Revision Notes

- **DFS:** path, BST, LCA.
- **BFS:** levels, width, zigzag.

## Problems in This Module

| # | Problem | Pattern |
| :---: | :--- | :--- |
| 33 | [Path Sum](/dsa-coding/05-trees/path-sum/) | DFS |
| 34 | [Validate Binary Search Tree](/dsa-coding/05-trees/validate-binary-search-tree/) | DFS |
| 35 | [Lowest Common Ancestor of a BST](/dsa-coding/05-trees/lowest-common-ancestor-bst/) | DFS |
| 36 | [Binary Tree Right Side View](/dsa-coding/05-trees/binary-tree-right-side-view/) | BFS |
| 37 | [Binary Tree Zigzag Level Order Traversal](/dsa-coding/05-trees/binary-tree-zigzag-level-order/) | BFS |
| 38 | [Maximum Width of Binary Tree](/dsa-coding/05-trees/maximum-width-of-binary-tree/) | BFS |
| 39 | [Maximum Level Sum of a Binary Tree](/dsa-coding/05-trees/maximum-level-sum-binary-tree/) | BFS |

---

## See Also

- [Previous: N-Queens](/dsa-coding/04-recursion-backtracking/n-queens/)
- [Next: Path Sum](/dsa-coding/05-trees/path-sum/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
