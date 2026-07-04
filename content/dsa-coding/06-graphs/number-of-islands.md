---
title: "Number of Islands"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DFS pattern — Number of Islands."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Number of Islands"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.2"
weight: 602
languages: ["java", "golang"]
source: "https://leetcode.com/problems/number-of-islands/"
sourceLabel: "LeetCode 200"
pattern: "DFS"
interviewHandbook: true
---
# Number of Islands

**Source:** [LeetCode 200](https://leetcode.com/problems/number-of-islands/) · **Pattern:** DFS · **Problem #41**

---

## Problem Statement

Given an `m x n` 2D grid of `'1'` (land) and `'0'` (water), return the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

| Constraint | Value |
| :--- | :--- |
| Grid | `1 ≤ m, n ≤ 300` |
| Cells | `grid[i][j]` is `'0'` or `'1'` |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Count connected components of `'1'` → scan grid; on unseen land, increment count and DFS/BFS to sink the whole island.

### Why this pattern?

Connected components on grid → DFS/BFS flood-fill.

### Why not another pattern?

Union-Find works but DFS in-place mark is standard; BFS for shortest not needed.

### What the interviewer expects

4-direction; mutate grid or visited set tradeoff.

---

## Brute Force

Union-Find connecting adjacent lands — **O(mn α(mn))**; heavier than needed for static grid.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`grid = [["1","1","0"],["0","1","0"],["0","0","1"]]` — three separate land components → `3`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length, count = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    dfs(grid, r, c);
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int r, int c) {
        int m = grid.length, n = grid[0].length;
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func numIslands(grid [][]byte) int {
    m, n := len(grid), len(grid[0])
    var dfs func(r, c int)
    dfs = func(r, c int) {
        if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != '1' {
            return
        }
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    }
    count := 0
    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            if grid[r][c] == '1' {
                count++
                dfs(r, c)
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

- All water → 0
- Single cell land → 1
- Mutating input — clarify with interviewer

---

## Interview Follow-ups

1. **Max island area?** — DFS returning cell count per component.
2. **Distinct island shapes?** — Encode shape as string during DFS.
3. **BFS instead?** — Queue flood fill — same complexity.

---

## See Also

- [Previous: Rotten Oranges](/dsa-coding/06-graphs/rotten-oranges/)
- [Next: Number of Provinces](/dsa-coding/06-graphs/number-of-provinces/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
