---
title: "Time Needed to Inform All Employees"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BFS/DFS on Tree pattern — Time Needed to Inform All Employees."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Time Needed to Inform All Employees"
module: 6
moduleTitle: "Graphs"
sectionRef: "6.7"
weight: 607
languages: ["java", "golang"]
source: "https://leetcode.com/problems/time-needed-to-inform-all-employees/"
sourceLabel: "LeetCode 1376"
pattern: "BFS/DFS on Tree"
interviewHandbook: true
---
# Time Needed to Inform All Employees

**Source:** [LeetCode 1376](https://leetcode.com/problems/time-needed-to-inform-all-employees/) · **Pattern:** BFS/DFS on Tree · **Problem #46**

---

## Problem Statement

A company has `n` employees (`0..n-1`) with a manager tree (`manager[i]` is manager of `i`, root has `manager[i] = -1`). Each employee `i` needs `informTime[i]` minutes to inform subordinates. Return minutes needed for the head to inform everyone.

| Constraint | Value |
| :--- | :--- |
| Employees | `1 ≤ n ≤ 10⁵` |
| Tree | Valid rooted tree |
| Times | `0 ≤ informTime[i] ≤ 500` |

---

## Pattern Recognition

**Canonical pattern:** [Graphs](/dsa-coding/06-graphs/) — full framework in module primer.

Tree propagation of max child time + edge weight → build adjacency from manager array; DFS postorder or BFS bottom-up from leaves.

### Why this pattern?

Tree BFS/DFS from root — propagate max time down org chart.

### Why not another pattern?

Greedy per node wrong; graph may be tree by problem guarantee.

### What the interviewer expects

Build children adjacency from manager array; return max leaf time.

---

## Brute Force

Simulate minute-by-minute events — wasteful **O(answer)** when answer can be large.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`n=6`, head 2, inform times `[0,0,1,0,0,0]` — leaf chains sum max depth inform delay → `1` minute total for small tree.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < n; i++) {
            if (manager[i] != -1) adj.get(manager[i]).add(i);
        }
        return dfs(headID, adj, informTime);
    }

    private int dfs(int u, List<List<Integer>> adj, int[] informTime) {
        int maxChild = 0;
        for (int v : adj.get(u)) {
            maxChild = Math.max(maxChild, dfs(v, adj, informTime));
        }
        return informTime[u] + maxChild;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
    adj := make([][]int, n)
    for i := 0; i < n; i++ {
        if manager[i] != -1 {
            p := manager[i]
            adj[p] = append(adj[p], i)
        }
    }
    var dfs func(u int) int
    dfs = func(u int) int {
        maxChild := 0
        for _, v := range adj[u] {
            if t := dfs(v); t > maxChild {
                maxChild = t
            }
        }
        return informTime[u] + maxChild
    }
    return dfs(headID)
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## Edge Cases

- Single employee (head only) → 0
- Star graph — head informs all directly
- Deep chain — sum along one path dominates

---

## Interview Follow-ups

1. **BFS topological?** — Process children before parents using reverse adjacency.
2. **Parallel inform?** — Model as longest weighted path in tree.
3. **Fire employee subtree?** — Subtree size queries with DFS order.

---

## See Also

- [Previous: Nearest Exit from Entrance in Maze](/dsa-coding/06-graphs/nearest-exit-from-maze/)
- [Next: Number of Closed Islands](/dsa-coding/06-graphs/number-of-closed-islands/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
