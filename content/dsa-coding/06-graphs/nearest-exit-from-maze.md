---
title: "Nearest Exit from Entrance in Maze"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BFS pattern — Nearest Exit from Entrance in Maze."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Nearest Exit from Entrance in Maze"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.6"
weight: 606
languages: ["java", "golang"]
source: "https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/"
sourceLabel: "LeetCode 490"
pattern: "BFS"
interviewHandbook: true
---
# Nearest Exit from Entrance in Maze

**Source:** [LeetCode 490](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) · **Pattern:** BFS · **Problem #45**

---

## Problem Statement

Given a maze (`'+'` wall, `'.'` empty) and an entrance `[row, col]`, return the **minimum steps** to reach any border cell that is empty. You cannot walk off the maze or reuse a cell in the same path.

| Constraint | Value |
| :--- | :--- |
| Maze | `1 ≤ m, n ≤ 100` |
| Entrance | Empty cell on border or interior |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Shortest steps in unweighted grid → BFS from entrance; stop at first empty border cell (excluding entrance).

### Why this pattern?

BFS from entrance on boundary — first exit is shortest.

### Why not another pattern?

DFS may find longer path first; treat maze as implicit graph.

### What the interviewer expects

Only step on empty cells; entrance not counted as exit.

---

## Brute Force

DFS all paths tracking min steps — exponential.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

Maze with entrance inside; BFS expands in rings — first border `.` hit gives step count.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length, n = maze[0].length;
        int sr = entrance[0], sc = entrance[1];
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[] { sr, sc, 0 });
        maze[sr][sc] = '+';
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty()) {
            int[] cur = q.removeFirst();
            int r = cur[0], c = cur[1], dist = cur[2];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || maze[nr][nc] == '+') continue;
                if ((nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1)) return dist + 1;
                maze[nr][nc] = '+';
                q.addLast(new int[] { nr, nc, dist + 1 });
            }
        }
        return -1;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func nearestExit(maze [][]byte, entrance []int) int {
    m, n := len(maze), len(maze[0])
    sr, sc := entrance[0], entrance[1]
    type cell struct{ r, c, dist int }
    q := []cell{{sr, sc, 0}}
    maze[sr][sc] = '+'
    dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    for len(q) > 0 {
        cur := q[0]
        q = q[1:]
        for _, d := range dirs {
            nr, nc := cur.r+d[0], cur.c+d[1]
            if nr < 0 || nr >= m || nc < 0 || nc >= n || maze[nr][nc] == '+' {
                continue
            }
            if nr == 0 || nr == m-1 || nc == 0 || nc == n-1 {
                return cur.dist + 1
            }
            maze[nr][nc] = '+'
            q = append(q, cell{nr, nc, cur.dist + 1})
        }
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

- Entrance already on border — must **exit** (step off), not stay
- No reachable border → -1
- Mark visited to prevent cycles

---

## Interview Follow-ups

1. **Return exit coordinates?** — Store parent during BFS.
2. **Multiple exits?** — BFS naturally finds nearest.
3. **Keys and doors?** — State-space BFS with bitmask keys.

---

## See Also

- [Previous: Shortest Path in Binary Matrix](/dsa-coding/06-graphs/shortest-path-in-binary-matrix/)
- [Next: Time Needed to Inform All Employees](/dsa-coding/06-graphs/time-needed-to-inform-employees/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
