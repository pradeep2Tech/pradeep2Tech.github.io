---
title: "Number of Closed Islands"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DFS pattern — Number of Closed Islands."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Number of Closed Islands"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.8"
weight: 608
languages: ["java", "golang"]
source: "https://leetcode.com/problems/number-of-closed-islands/"
sourceLabel: "LeetCode 1254"
pattern: "DFS"
ShowToc: true
interviewHandbook: true
---
# Number of Closed Islands

**Source:** [LeetCode 1254](https://leetcode.com/problems/number-of-closed-islands/) · **Pattern:** DFS · **Problem #47**

---

## Problem Statement

Given an `m x n` grid of `0` (water) and `1` (land), return the number of **closed islands**. A closed island is entirely surrounded by water (no land on the grid border connects to it).

| Constraint | Value |
| :--- | :--- |
| Grid | `1 ≤ m, n ≤ 200` |
| Cells | `0` or `1` |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Islands touching border cannot be closed → first flood-fill border-connected land to water, then count remaining land components.

### Why this pattern?

Flood-fill border-connected water first; count islands fully surrounded.

### Why not another pattern?

Counting all islands overcounts; need boundary classification.

### What the interviewer expects

DFS from border to mark non-closed; then count internal islands.

---

## Brute Force

For each land cell check if path to border exists — repeated BFS per cell, **O((mn)²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

Border land connected to edge is marked 0; interior `1` pockets fully surrounded by `0` are counted.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int closedIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        for (int r = 0; r < m; r++) {
            sink(grid, r, 0);
            sink(grid, r, n - 1);
        }
        for (int c = 0; c < n; c++) {
            sink(grid, 0, c);
            sink(grid, m - 1, c);
        }
        int count = 0;
        for (int r = 1; r < m - 1; r++) {
            for (int c = 1; c < n - 1; c++) {
                if (grid[r][c] == 1) {
                    count++;
                    sinkIsland(grid, r, c);
                }
            }
        }
        return count;
    }

    private void sink(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 0) return;
        grid[r][c] = 0;
        sink(grid, r + 1, c);
        sink(grid, r - 1, c);
        sink(grid, r, c + 1);
        sink(grid, r, c - 1);
    }

    private void sinkIsland(int[][] grid, int r, int c) {
        sink(grid, r, c);
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func closedIsland(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    var flood func(r, c int)
    flood = func(r, c int) {
        if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 {
            return
        }
        grid[r][c] = 0
        flood(r+1, c)
        flood(r-1, c)
        flood(r, c+1)
        flood(r, c-1)
    }
    for r := 0; r < m; r++ {
        flood(r, 0)
        flood(r, n-1)
    }
    for c := 0; c < n; c++ {
        flood(0, c)
        flood(m-1, c)
    }
    count := 0
    for r := 1; r < m-1; r++ {
        for c := 1; c < n-1; c++ {
            if grid[r][c] == 1 {
                count++
                flood(r, c)
            }
        }
    }
    return count
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(mn)
- **Space:** O(mn) recursion worst case

---

## Edge Cases

- All border land — after phase 1 count is 0
- No land → 0
- Single interior land cell — counts as 1 if surrounded

---

## Interview Follow-ups

1. **Return island areas?** — DFS returns size; filter closed in phase 2.
2. **4-direction vs 8?** — Problem uses 4-direction connectivity.
3. **Union-Find alternative?** — Union border lands first, then count components not touching border.

---

## See Also

- [Previous: Time Needed to Inform All Employees](/dsa-coding/06-graphs/time-needed-to-inform-employees/)
- [Next: Advanced Graphs](/dsa-coding/07-advanced-graphs/_index/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
