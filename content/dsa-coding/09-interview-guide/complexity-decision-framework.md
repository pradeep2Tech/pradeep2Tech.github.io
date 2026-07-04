---
title: "Complexity Decision Framework"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Complexity Framework"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Complexity Framework"
module: 9
moduleTitle: "DSA & Coding"
sectionRef: "9.3"
weight: 903
interviewHandbook: true
cheatSheet: true
---

# Complexity Decision Framework

Derive your **complexity budget from constraints** before choosing a pattern. Architects state this aloud in interviews.

---

## Constraint → Target Complexity

| `n` (typical) | Safe target | Patterns in range |
| :--- | :--- | :--- |
| ≤ 20 | O(n!), O(2^n) | Backtracking with pruning |
| ≤ 200 | O(n³) | Triple loops, dense DP tables |
| ≤ 2,000 | O(n²) | Nested loops, 2D DP |
| ≤ 10⁵ | O(n log n) | Sort + scan, heap, BS on answer with O(n) check |
| ≤ 10⁶ | O(n) | HashMap, sliding window, BFS/DFS linear |
| ≤ 10⁷ | O(n) or O(n log n) tight | Avoid hidden constants, large maps |

---

## Space Tradeoffs

| Pattern | Extra space | When worth it |
| :--- | :--- | :--- |
| HashMap | O(n) | Cuts time from O(n²) to O(n) |
| Prefix + map | O(n) | Subarray sum with negatives |
| DP table | O(n) – O(n²) | Overlapping subproblems |
| Recursion stack | O(h) – O(n) | Trees/graphs depth |
| In-place pointers | O(1) | Sorted arrays, swap-based |

---

## Decision Checklist

1. **Multiply dimensions** — grid `m×n` → treat as N = m·n for BFS/DFS.
2. **Hidden log** — sort O(n log n); BS on answer O(n log R) with O(n) feasibility.
3. **Output size** — generating all subsets is O(2^n); interviewer may accept only count.
4. **Amortized** — sliding window two pointers: each index moves O(1) times total.

---

## Interview Script

> "With n up to 10⁵, I need about O(n) or O(n log n). Brute force is O(n²), so I'll use a HashMap / window / sort+two pointers."

---

## Related

- [Pattern Selection Matrix](/dsa-coding/09-interview-guide/pattern-selection-matrix/)
- [60-Second Pattern Recognition](/dsa-coding/09-interview-guide/60-second-pattern-recognition/)
