---
title: "Shortest Path in Binary Matrix"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BFS pattern — Shortest Path in Binary Matrix."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Shortest Path in Binary Matrix"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.5"
weight: 605
languages: ["java", "golang"]
source: "https://leetcode.com/problems/shortest-path-in-binary-matrix/"
sourceLabel: "LeetCode 1091"
pattern: "BFS"
ShowToc: true
interviewHandbook: true
---
# Shortest Path in Binary Matrix

**Source:** [LeetCode 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) · **Pattern:** BFS · **Problem #44**

---

## Problem Statement

Given an `n x n` binary matrix `grid`, return the length of the shortest **clear path** from top-left `(0,0)` to bottom-right `(n-1,n-1)`. Move 8-directionally through cells with value `0`. Path length counts cells including start and end. Return `-1` if no path.

| Constraint | Value |
| :--- | :--- |
| Grid | `n == grid.length` |
| Size | `1 ≤ n ≤ 100` |
| Cells | `0` or `1` |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Unweighted shortest path on grid → BFS from start; 8 neighbors; first time reaching target is optimal.

### Why this pattern?

Unweighted shortest path → BFS with 8 directions.

### Why not another pattern?

DFS doesn't guarantee shortest; Dijkstra overkill.

### What the interviewer expects

Mark visited on enqueue; block (0,0) if cell is 1.

---

## Brute Force

DFS enumerating all paths tracking min length — exponential.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[[0,1],[1,0]]` — direct paths blocked; diagonal 0→(1,1) length 2 if open; classic `[0,0]→[1,1]` via diagonal when allowed.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        if (n == 1) return 1;
        int[][] dirs = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[] {0, 0, 1});
        grid[0][0] = 1;
        while (!q.isEmpty()) {
            int[] cur = q.removeFirst();
            int r = cur[0], c = cur[1], dist = cur[2];
            if (r == n - 1 && c == n - 1) return dist;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    q.addLast(new int[] { nr, nc, dist + 1 });
                }
            }
        }
        return -1;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func shortestPathBinaryMatrix(grid [][]int) int {
    n := len(grid)
    if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
        return -1
    }
    if n == 1 {
        return 1
    }
    dirs := [8][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
    type cell struct{ r, c, dist int }
    q := []cell{{0, 0, 1}}
    grid[0][0] = 1
    for len(q) > 0 {
        cur := q[0]
        q = q[1:]
        if cur.r == n-1 && cur.c == n-1 {
            return cur.dist
        }
        for _, d := range dirs {
            nr, nc := cur.r+d[0], cur.c+d[1]
            if nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 {
                grid[nr][nc] = 1
                q = append(q, cell{nr, nc, cur.dist + 1})
            }
        }
    }
    return -1
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n²)
- **Space:** O(n²)

---

## Edge Cases

- Start or end blocked → -1
- 1x1 grid with 0 → 1
- Mark visited on enqueue to avoid duplicate queue entries

---

## Interview Follow-ups

1. **4-direction only?** — Drop diagonal dirs from neighbor list.
2. **Return path coordinates?** — Store parent map during BFS, backtrack.
3. **Weighted cells?** — Dijkstra — not pure BFS.

---

## See Also

- [Previous: Graph Valid Tree](/dsa-coding/06-graphs/graph-valid-tree/)
- [Next: Nearest Exit from Entrance in Maze](/dsa-coding/06-graphs/nearest-exit-from-maze/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
