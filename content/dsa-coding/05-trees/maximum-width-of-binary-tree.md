---
title: "Maximum Width of Binary Tree"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BFS pattern — Maximum Width of Binary Tree."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Maximum Width of Binary Tree"
module: 5
moduleTitle: "Trees"
sectionRef: "5.6"
weight: 506
languages: ["java", "golang"]
source: "https://leetcode.com/problems/maximum-width-of-binary-tree/"
sourceLabel: "LeetCode 662"
pattern: "BFS"
ShowToc: true
interviewHandbook: true
---
# Maximum Width of Binary Tree

**Source:** [LeetCode 662](https://leetcode.com/problems/maximum-width-of-binary-tree/) · **Pattern:** BFS · **Problem #38**

---

## Problem Statement

Given the `root` of a binary tree, return the **maximum width** among all levels. Width is the count of nodes between the leftmost and rightmost non-null nodes at a level, including the null gaps between them (index-based complete-tree numbering).

| Constraint | Value |
| :--- | :--- |
| Nodes | `1 ≤ tree nodes ≤ 3000` |
| Values | `-100 ≤ Node.val ≤ 100` |

---

## Pattern Recognition

**Canonical pattern:** [Trees](/dsa-coding/05-trees/) — full framework in module primer.

Level width with implicit null slots → BFS assigning index `i` to node, children get `2*i` and `2*i+1`; width = last index − first index + 1 per level.

### Why this pattern?

BFS with index positions — width = rightmost-leftmost+1 per level.

### Why not another pattern?

DFS with index offsets works; sorting nodes per level wasteful.

### What the interviewer expects

Prevent index overflow with relative indexing in production discussion.

---

## Brute Force

Store full indexed level including null placeholders — memory blow-up on sparse wide levels.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

Tree `[1,3,2,5,3,null,9]` — deepest level indices 4..7 → width 4 (includes gap between 5 and 9).

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
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        Deque<TreeNode> nodes = new ArrayDeque<>();
        Deque<Long> indices = new ArrayDeque<>();
        nodes.add(root);
        indices.add(0L);
        int maxWidth = 0;
        while (!nodes.isEmpty()) {
            int size = nodes.size();
            long left = indices.peekFirst();
            long right = left;
            for (int i = 0; i < size; i++) {
                TreeNode node = nodes.removeFirst();
                long idx = indices.removeFirst();
                right = idx;
                if (node.left != null) {
                    nodes.addLast(node.left);
                    indices.addLast(idx * 2);
                }
                if (node.right != null) {
                    nodes.addLast(node.right);
                    indices.addLast(idx * 2 + 1);
                }
            }
            maxWidth = Math.max(maxWidth, (int) (right - left + 1));
        }
        return maxWidth;
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

func widthOfBinaryTree(root *TreeNode) int {
    if root == nil {
        return 0
    }
    type pair struct {
        node *TreeNode
        idx  int
    }
    q := []pair{{root, 0}}
    maxWidth := 0
    for len(q) > 0 {
        size := len(q)
        left := q[0].idx
        right := left
        for i := 0; i < size; i++ {
            cur := q[0]
            q = q[1:]
            right = cur.idx
            if cur.node.Left != nil {
                q = append(q, pair{cur.node.Left, cur.idx * 2})
            }
            if cur.node.Right != nil {
                q = append(q, pair{cur.node.Right, cur.idx*2 + 1})
            }
        }
        if w := right - left + 1; w > maxWidth {
            maxWidth = w
        }
    }
    return maxWidth
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

- Single node — width 1
- Left-only skew — width stays 1 each level
- Wide sparse level — index math needs 64-bit in Java

---

## Interview Follow-ups

1. **Index overflow?** — Normalize by subtracting min index each level before enqueue.
2. **Count nodes only (no null gaps)?** — Different metric — standard level node count.
3. **DFS with index?** — Pass index down; track global min/max per depth.

---

## See Also

- [Previous: Binary Tree Zigzag Level Order Traversal](/dsa-coding/05-trees/binary-tree-zigzag-level-order/)
- [Next: Maximum Level Sum of a Binary Tree](/dsa-coding/05-trees/maximum-level-sum-binary-tree/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
