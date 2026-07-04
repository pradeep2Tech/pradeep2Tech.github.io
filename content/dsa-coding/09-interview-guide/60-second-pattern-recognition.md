---
title: "60-Second Pattern Recognition"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "60-Second Cheat Sheet"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "60-Second Cheat Sheet"
module: 9
moduleTitle: "DSA & Coding"
sectionRef: "9.4"
weight: 904
interviewHandbook: true
cheatSheet: true
---

# 60-Second Pattern Recognition

Ultra-condensed triage — read in one minute before interviews.  
Canonical depth: module primers + [Pattern Recognition Table](/dsa-coding/09-interview-guide/pattern-recognition-table/).

| Signal (1 line) | Pattern | Module |
| :--- | :--- | :--- |
| Seen before? / frequency? | HashMap | 1 |
| Sorted pair / triplet? | Two pointers | 1 |
| Fixed window k? | Fixed sliding window | 2 |
| Longest/shortest substring? | Variable window | 2 |
| Subarray sum (negatives OK)? | Prefix + map | 2 |
| Sorted search / first true? | Binary search | 3 |
| Minimize maximum rate? | BS on answer | 3 |
| Generate all combos? | Backtracking | 4 |
| Valid brackets? | Stack | 4 |
| Tree path / BST? | DFS | 5 |
| Level order? | BFS | 5 |
| Islands / flood? | DFS | 6 |
| Shortest grid steps? | BFS | 6 |
| Rotten / multi-source? | Multi-source BFS | 6 |
| Alien order / deps? | Topo sort | 7 |
| Count ways / min cost? | DP | 8 |

---

## 60-Second Flow

1. **Contiguous?** → Module 2  
2. **Tree?** → Module 5  
3. **Grid/graph?** → Module 6/7  
4. **Optimize count/cost?** → Module 8  
5. **Sorted/monotone?** → Module 3  
6. **Else** → Module 1 (HashMap) or Module 4 (search)

---

## Complexity at a Glance

| n | Use |
| :--- | :--- |
| 10⁵+ | O(n) or O(n log n) |
| 10³ | O(n²) maybe |
| tiny | backtracking OK |

[Complexity Decision Framework](/dsa-coding/09-interview-guide/complexity-decision-framework/) · [Pattern Selection Matrix](/dsa-coding/09-interview-guide/pattern-selection-matrix/)
