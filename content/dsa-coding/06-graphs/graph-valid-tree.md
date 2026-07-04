---
title: "Graph Valid Tree"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DFS/BFS pattern — Graph Valid Tree."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Graph Valid Tree"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.4"
weight: 604
languages: ["java", "golang"]
source: "https://leetcode.com/problems/graph-valid-tree/"
sourceLabel: "LeetCode 261"
pattern: "DFS/BFS"
interviewHandbook: true
---
# Graph Valid Tree

**Source:** [LeetCode 261](https://leetcode.com/problems/graph-valid-tree/) · **Pattern:** DFS/BFS · **Problem #43**

---

## Problem Statement

Given `n` nodes labeled `0..n-1` and an edge list, determine if the edges form a **valid tree**: connected and acyclic (exactly `n-1` edges with no cycles).

| Constraint | Value |
| :--- | :--- |
| Nodes | `1 ≤ n ≤ 2000` |
| Edges | `0 ≤ edges.length ≤ 5000` |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Tree ⇔ connected + `|E| = n-1` + no cycle. Build adjacency list; DFS/BFS or Union-Find detecting cycle.

### Why this pattern?

Tree = connected + exactly n-1 edges — DFS cycle detection or Union-Find.

### Why not another pattern?

Pure edge count without connectivity check fails.

### What the interviewer expects

Mention single component + no cycle; undirected edge handling.

---

## Brute Force

Check `|E| == n-1` then verify connectivity with DFS — already optimal structure.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`n=5, edges=[[0,1],[0,2],[0,3],[1,4]]` — 4 edges, all nodes reachable, no cycle → `true`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        boolean[] seen = new boolean[n];
        Deque<Integer> q = new ArrayDeque<>();
        q.add(0);
        seen[0] = true;
        int visited = 0;
        while (!q.isEmpty()) {
            int u = q.removeFirst();
            visited++;
            for (int v : adj.get(u)) {
                if (!seen[v]) {
                    seen[v] = true;
                    q.addLast(v);
                }
            }
        }
        return visited == n;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func validTree(n int, edges [][]int) bool {
    if len(edges) != n-1 {
        return false
    }
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }
    seen := make([]bool, n)
    q := []int{0}
    seen[0] = true
    visited := 0
    for len(q) > 0 {
        u := q[0]
        q = q[1:]
        visited++
        for _, v := range adj[u] {
            if !seen[v] {
                seen[v] = true
                q = append(q, v)
            }
        }
    }
    return visited == n
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n + e)
- **Space:** O(n + e)

---

## Edge Cases

- n=1, no edges — valid tree (single node)
- Disconnected with n-1 edges — false (forest)
- Cycle with n edges — false immediately

---

## Interview Follow-ups

1. **Detect cycle explicitly?** — DFS with parent pointer or Union-Find on add edge.
2. **Directed tree?** — Need exactly one root with in-degree 0 for all reachability.
3. **Build the tree root?** — Pick any node BFS — parent map gives rooted tree.

---

## See Also

- [Previous: Number of Provinces](/dsa-coding/06-graphs/number-of-provinces/)
- [Next: Shortest Path in Binary Matrix](/dsa-coding/06-graphs/shortest-path-in-binary-matrix/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
