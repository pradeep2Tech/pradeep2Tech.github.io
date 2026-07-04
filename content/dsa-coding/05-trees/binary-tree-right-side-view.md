---
title: "Binary Tree Right Side View"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BFS pattern — Binary Tree Right Side View."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Binary Tree Right Side View"
module: 5
moduleTitle: "Trees"
sectionRef: "5.4"
weight: 504
languages: ["java", "golang"]
source: "https://leetcode.com/problems/binary-tree-right-side-view/"
sourceLabel: "LeetCode 199"
pattern: "BFS"
interviewHandbook: true
---
# Binary Tree Right Side View

**Source:** [LeetCode 199](https://leetcode.com/problems/binary-tree-right-side-view/) · **Pattern:** BFS · **Problem #36**

---

## Problem Statement

Given the `root` of a binary tree, return the values of nodes you can see ordered from top to bottom when standing on the **right side** of the tree.

| Constraint | Value |
| :--- | :--- |
| Nodes | `0 ≤ tree nodes ≤ 100` |
| Values | `-100 ≤ Node.val ≤ 100` |

---

## Pattern Recognition

**Canonical pattern:** [Trees](/dsa-coding/05-trees/) — full framework in module primer.

Rightmost node per level → level-order BFS; capture the last node processed in each level. Equivalent DFS: visit right child before left, record first node at each depth.

### Why this pattern?

BFS level order — last node per level visible.

### Why not another pattern?

DFS with depth tracking works; right-first DFS also valid.

### What the interviewer expects

Queue size per level; empty tree edge case.

---

## Brute Force

BFS storing entire level lists, take last element each time — same complexity but extra list churn.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[1,2,3,null,5,null,4]` — level 0: `[1]`, level 1: `[3]` (right wins over 2), level 2: `[4]` → `[1,3,4]`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.removeFirst();
                if (node.left != null) q.addLast(node.left);
                if (node.right != null) q.addLast(node.right);
                if (i == size - 1) res.add(node.val);
            }
        }
        return res;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
    if root == nil {
        return nil
    }
    res := []int{}
    q := []*TreeNode{root}
    for len(q) > 0 {
        size := len(q)
        for i := 0; i < size; i++ {
            node := q[0]
            q = q[1:]
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
            if i == size-1 {
                res = append(res, node.Val)
            }
        }
    }
    return res
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(w) queue width

---

## Edge Cases

- Empty tree → empty list
- Only left children — right view is left spine
- Complete tree — all level rightmost nodes

---

## Interview Follow-ups

1. **Left side view?** — Capture first node in each BFS level.
2. **Top view?** — Track horizontal distance with map.
3. **DFS variant?** — Preorder right-first with depth tracking.

---

## See Also

- [Previous: Lowest Common Ancestor of a BST](/dsa-coding/05-trees/lowest-common-ancestor-bst/)
- [Next: Binary Tree Zigzag Level Order Traversal](/dsa-coding/05-trees/binary-tree-zigzag-level-order/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
