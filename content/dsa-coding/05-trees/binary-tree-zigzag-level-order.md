---
title: "Binary Tree Zigzag Level Order Traversal"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BFS pattern — Binary Tree Zigzag Level Order Traversal."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Binary Tree Zigzag Level Order Traversal"
module: 5
moduleTitle: "Trees"
sectionRef: "5.5"
weight: 505
languages: ["java", "golang"]
source: "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/"
sourceLabel: "LeetCode 103"
pattern: "BFS"
interviewHandbook: true
---
# Binary Tree Zigzag Level Order Traversal

**Source:** [LeetCode 103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) · **Pattern:** BFS · **Problem #37**

---

## Problem Statement

Given the `root` of a binary tree, return the zigzag level order traversal (alternate left-to-right and right-to-left per level).

| Constraint | Value |
| :--- | :--- |
| Nodes | `0 ≤ tree nodes ≤ 2000` |
| Values | `-100 ≤ Node.val ≤ 100` |

---

## Pattern Recognition

**Canonical pattern:** [Trees](/dsa-coding/05-trees/) — full framework in module primer.

Level-order with per-level direction flip → standard BFS + reverse every odd level, or add children to deque front/back alternately.

### Why this pattern?

BFS with level parity toggling deque direction.

### Why not another pattern?

DFS zigzag is painful; recursion depth vs width.

### What the interviewer expects

Reverse every other level or use double-ended processing.

---

## Brute Force

BFS collect levels, reverse alternate indices — clear and **O(n)** with small reversal cost per level.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[3,9,20,null,null,15,7]` → level 0 `[3]`, level 1 `[20,9]`, level 2 `[15,7]`.

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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        boolean leftToRight = true;
        while (!q.isEmpty()) {
            int size = q.size();
            LinkedList<Integer> level = new LinkedList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.removeFirst();
                if (leftToRight) level.addLast(node.val);
                else level.addFirst(node.val);
                if (node.left != null) q.addLast(node.left);
                if (node.right != null) q.addLast(node.right);
            }
            res.add(level);
            leftToRight = !leftToRight;
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

func zigzagLevelOrder(root *TreeNode) [][]int {
    if root == nil {
        return nil
    }
    res := [][]int{}
    q := []*TreeNode{root}
    leftToRight := true
    for len(q) > 0 {
        size := len(q)
        level := make([]int, 0, size)
        for i := 0; i < size; i++ {
            node := q[0]
            q = q[1:]
            if leftToRight {
                level = append(level, node.Val)
            } else {
                level = append([]int{node.Val}, level...)
            }
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        res = append(res, level)
        leftToRight = !leftToRight
    }
    return res
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(w)

---

## Edge Cases

- Single node — one level `[root.val]`
- Skewed tree — many single-node levels
- Empty tree → `[]`

---

## Interview Follow-ups

1. **Zigzag without addFirst O(n) per level?** — Collect normally then reverse odd levels.
2. **N-ary tree zigzag?** — Same BFS; enqueue all children.
3. **Vertical order?** — Different coordinate system — BFS with column index.

---

## See Also

- [Previous: Binary Tree Right Side View](/dsa-coding/05-trees/binary-tree-right-side-view/)
- [Next: Maximum Width of Binary Tree](/dsa-coding/05-trees/maximum-width-of-binary-tree/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
