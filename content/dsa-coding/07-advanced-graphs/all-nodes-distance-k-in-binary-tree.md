---
title: "All Nodes Distance K in Binary Tree"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Graph + BFS pattern — All Nodes Distance K in Binary Tree."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "All Nodes Distance K in Binary Tree"
module: 7
moduleTitle: "Advanced Graphs"
sectionRef: "7.2"
weight: 702
languages: ["java", "golang"]
source: "https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/"
sourceLabel: "LeetCode 863"
pattern: "Graph + BFS"
ShowToc: true
interviewHandbook: true
---
# All Nodes Distance K in Binary Tree

**Source:** [LeetCode 863](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) · **Pattern:** Graph + BFS · **Problem #49**

---

## Problem Statement

Given the `root` of a binary tree, a `target` node `val`, and integer `k`, return the values of all nodes at distance exactly `k` from the target.

| Constraint | Value |
| :--- | :--- |
| Nodes | `1 ≤ number of nodes ≤ 500` |
| Values | `0 ≤ Node.val ≤ 500` |
| `k` | `0 ≤ k ≤ 1000` |
| Target | Guaranteed to exist in the tree |

---

## Pattern Recognition

**Canonical pattern:** [Advanced Graphs](/dsa-coding/07-advanced-graphs/) — full framework in module primer.

Tree edges are one-way parent→child only. Distance `k` may require going up to a parent — model the tree as an undirected adjacency graph, locate target, BFS exactly `k` levels.

### Why this pattern?

Tree lacks parent links → build parent map, BFS from target distance K.

### Why not another pattern?

Pure child DFS can't go upward; one-pass subtree size overkill.

### What the interviewer expects

Undirected graph view of tree; visited set for BFS.

---

## Brute Force

For each node, find path to target (DFS), compute distance — **O(n²)** in worst case.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

Tree `[3,5,1,6,2,0,8,null,null,7,4]`, `target = 5`, `k = 2`. Nodes at distance 2: `7`, `4`, `1` (via parent `3` and child `2`).

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        dfs(root, null, parent);
        Queue<TreeNode> q = new ArrayDeque<>();
        Set<TreeNode> seen = new HashSet<>();
        q.offer(target);
        seen.add(target);
        int dist = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            if (dist == k) {
                List<Integer> res = new ArrayList<>();
                for (TreeNode n : q) res.add(n.val);
                return res;
            }
            for (int i = 0; i < size; i++) {
                TreeNode cur = q.poll();
                for (TreeNode nei : neighbors(cur, parent)) {
                    if (!seen.contains(nei)) {
                        seen.add(nei);
                        q.offer(nei);
                    }
                }
            }
            dist++;
        }
        return List.of();
    }

    private void dfs(TreeNode node, TreeNode par, Map<TreeNode, TreeNode> parent) {
        if (node == null) return;
        parent.put(node, par);
        dfs(node.left, node, parent);
        dfs(node.right, node, parent);
    }

    private List<TreeNode> neighbors(TreeNode node, Map<TreeNode, TreeNode> parent) {
        List<TreeNode> list = new ArrayList<>();
        if (node.left != null) list.add(node.left);
        if (node.right != null) list.add(node.right);
        if (parent.get(node) != null) list.add(parent.get(node));
        return list;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func distanceK(root *TreeNode, target *TreeNode, k int) []int {
    parent := make(map[*TreeNode]*TreeNode)
    var build func(*TreeNode, *TreeNode)
    build = func(node, par *TreeNode) {
        if node == nil {
            return
        }
        parent[node] = par
        build(node.Left, node)
        build(node.Right, node)
    }
    build(root, nil)

    q := []*TreeNode{target}
    seen := map[*TreeNode]bool{target: true}
    dist := 0
    for len(q) > 0 {
        if dist == k {
            res := make([]int, len(q))
            for i, n := range q {
                res[i] = n.Val
            }
            return res
        }
        next := make([]*TreeNode, 0)
        for _, cur := range q {
            for _, nei := range neighbors(cur, parent) {
                if !seen[nei] {
                    seen[nei] = true
                    next = append(next, nei)
                }
            }
        }
        q = next
        dist++
    }
    return nil
}

func neighbors(node *TreeNode, parent map[*TreeNode]*TreeNode) []*TreeNode {
    res := make([]*TreeNode, 0, 3)
    if node.Left != nil {
        res = append(res, node.Left)
    }
    if node.Right != nil {
        res = append(res, node.Right)
    }
    if p := parent[node]; p != nil {
        res = append(res, p)
    }
    return res
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

- `k = 0` — return `[target.val]` only
- Target is leaf — must traverse via parent
- Target is root — no parent neighbor
- `k` larger than max distance — return empty list

---

## Interview Follow-ups

1. **Avoid explicit graph?** — Single DFS from target with distance bookkeeping is harder; graph BFS is cleaner.
2. **Return nodes sorted by value?** — Sort result if required — BFS order is not sorted.
3. **Repeated queries on same tree?** — Precompute parent map once.

---

## See Also

- [Previous: Alien Dictionary](/dsa-coding/07-advanced-graphs/alien-dictionary/)
- [Next: Dynamic Programming](/dsa-coding/08-dynamic-programming/_index/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
