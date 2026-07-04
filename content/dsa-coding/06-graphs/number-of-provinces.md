---
title: "Number of Provinces"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DFS pattern — Number of Provinces."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Number of Provinces"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.3"
weight: 603
languages: ["java", "golang"]
source: "https://leetcode.com/problems/number-of-provinces/"
sourceLabel: "LeetCode 547"
pattern: "DFS"
ShowToc: true
interviewHandbook: true
---
# Number of Provinces

**Source:** [LeetCode 547](https://leetcode.com/problems/number-of-provinces/) · **Pattern:** DFS · **Problem #42**

---

## Problem Statement

There are `n` cities connected by undirected roads. `isConnected[i][j] = 1` if cities `i` and `j` are directly connected. A **province** is a group of directly or indirectly connected cities. Return the total number of provinces.

| Constraint | Value |
| :--- | :--- |
| Cities | `1 ≤ n ≤ 200` |
| Matrix | `n x n` symmetric, `isConnected[i][i] = 1` |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Connected components in adjacency matrix → for each unvisited city, DFS/BFS all reachable nodes.

### Why this pattern?

Adjacency matrix connectivity — DFS from each unvisited node.

### Why not another pattern?

BFS equivalent; HashMap irrelevant.

### What the interviewer expects

Count components; O(n²) scan acceptable for dense matrix.

---

## Brute Force

Floyd-Warshall then count components — **O(n³)** overkill.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`isConnected = [[1,1,0],[1,1,0],[0,0,1]]` — cities {0,1} one province, city {2} alone → `2`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] seen = new boolean[n];
        int provinces = 0;
        for (int i = 0; i < n; i++) {
            if (!seen[i]) {
                provinces++;
                dfs(isConnected, seen, i);
            }
        }
        return provinces;
    }

    private void dfs(int[][] g, boolean[] seen, int u) {
        seen[u] = true;
        for (int v = 0; v < g.length; v++) {
            if (g[u][v] == 1 && !seen[v]) dfs(g, seen, v);
        }
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func findCircleNum(isConnected [][]int) int {
    n := len(isConnected)
    seen := make([]bool, n)
    var dfs func(u int)
    dfs = func(u int) {
        seen[u] = true
        for v := 0; v < n; v++ {
            if isConnected[u][v] == 1 && !seen[v] {
                dfs(v)
            }
        }
    }
    provinces := 0
    for i := 0; i < n; i++ {
        if !seen[i] {
            provinces++
            dfs(i)
        }
    }
    return provinces
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n²)
- **Space:** O(n)

---

## Edge Cases

- Single city → 1 province
- Fully connected → 1 province
- No edges off diagonal → n provinces

---

## Interview Follow-ups

1. **Edge list input?** — Build adjacency list then same DFS.
2. **Union-Find?** — Union pairs where matrix is 1; count distinct roots.
3. **Directed graph?** — Need Kosaraju/Tarjan for SCCs — different problem.

---

## See Also

- [Previous: Number of Islands](/dsa-coding/06-graphs/number-of-islands/)
- [Next: Graph Valid Tree](/dsa-coding/06-graphs/graph-valid-tree/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
