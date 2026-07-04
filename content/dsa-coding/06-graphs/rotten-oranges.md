---
title: "Rotten Oranges"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Multi-Source BFS pattern — Rotten Oranges."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Rotten Oranges"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.1"
weight: 601
languages: ["java", "golang"]
source: "https://leetcode.com/problems/rotten-oranges/"
sourceLabel: "LeetCode 994"
pattern: "Multi-Source BFS"
ShowToc: true
interviewHandbook: true
---
# Rotten Oranges

**Source:** [LeetCode 994](https://leetcode.com/problems/rotten-oranges/) · **Pattern:** Multi-Source BFS · **Problem #40**

---

## Problem Statement

Given an `m x n` grid where `0` = empty, `1` = fresh orange, `2` = rotten orange, every minute rotten oranges rot adjacent fresh cells (4-directionally). Return the minimum minutes until no fresh orange remains, or `-1` if impossible.

| Constraint | Value |
| :--- | :--- |
| Grid | `1 ≤ m, n ≤ 10` |
| Cells | Values in `{0, 1, 2}` |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Simultaneous spread from multiple sources → enqueue all rotten cells at time 0, BFS layer by layer counting minutes.

### Why this pattern?

Multi-source BFS — all rotten oranges enqueue at t=0.

### Why not another pattern?

DFS doesn't yield minimum minutes; single-source BFS misses parallel spread.

### What the interviewer expects

Track fresh count; return -1 if fresh remains.

---

## Brute Force

Repeatedly scan grid each minute for fresh adjacent to rotten — **O((mn)²)** time.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[[2,1,1],[1,1,0],[0,1,1]]` — minute 1: two rot; minute 2: two more; minute 3: last fresh → `4` minutes.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Deque<int[]> q = new ArrayDeque<>();
        int fresh = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 2) q.add(new int[] { r, c });
                else if (grid[r][c] == 1) fresh++;
            }
        }
        if (fresh == 0) return 0;
        int minutes = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty() && fresh > 0) {
            minutes++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cell = q.removeFirst();
                for (int[] d : dirs) {
                    int nr = cell[0] + d[0], nc = cell[1] + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        q.addLast(new int[] { nr, nc });
                    }
                }
            }
        }
        return fresh == 0 ? minutes : -1;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func orangesRotting(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    type cell struct{ r, c int }
    q := []cell{}
    fresh := 0
    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            if grid[r][c] == 2 {
                q = append(q, cell{r, c})
            } else if grid[r][c] == 1 {
                fresh++
            }
        }
    }
    if fresh == 0 {
        return 0
    }
    dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    minutes := 0
    for len(q) > 0 && fresh > 0 {
        minutes++
        size := len(q)
        for i := 0; i < size; i++ {
            cur := q[0]
            q = q[1:]
            for _, d := range dirs {
                nr, nc := cur.r+d[0], cur.c+d[1]
                if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1 {
                    grid[nr][nc] = 2
                    fresh--
                    q = append(q, cell{nr, nc})
                }
            }
        }
    }
    if fresh == 0 {
        return minutes
    }
    return -1
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(mn)
- **Space:** O(mn)

---

## Edge Cases

- No fresh oranges initially → 0
- Fresh unreachable island → -1
- Single rotten spreads to entire grid

---

## Interview Follow-ups

1. **8-directional rot?** — Add diagonal dirs to neighbor loop.
2. **Return order of rot times?** — Store timestamp per cell during BFS.
3. **Why minutes - 1?** — Last layer increments minutes but no new rot that step.

---

## See Also

- [Previous: Graphs](/dsa-coding/06-graphs/_index/)
- [Next: Number of Islands](/dsa-coding/06-graphs/number-of-islands/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
