---
title: "Maximum Level Sum of a Binary Tree"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BFS pattern — Maximum Level Sum of a Binary Tree."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Maximum Level Sum of a Binary Tree"
module: 5
moduleTitle: "Trees"
sectionRef: "5.7"
weight: 507
languages: ["java", "golang"]
source: "https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/"
sourceLabel: "LeetCode 1161"
pattern: "BFS"
ShowToc: true
interviewHandbook: true
---
# Maximum Level Sum of a Binary Tree

**Source:** [LeetCode 1161](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) · **Pattern:** BFS · **Problem #39**

---

## Problem Statement

Given the `root` of a binary tree, return the **smallest level number** (1-indexed) whose sum of node values is maximal.

| Constraint | Value |
| :--- | :--- |
| Nodes | `1 ≤ tree nodes ≤ 10⁴` |
| Values | `-10⁵ ≤ Node.val ≤ 10⁵` |

---

## Pattern Recognition

**Canonical pattern:** [Trees](/dsa-coding/05-trees/) — full framework in module primer.

Aggregate per level → BFS level-sum loop; track best sum and smallest level on ties.

### Why this pattern?

BFS accumulate sum per level; track max.

### Why not another pattern?

DFS level sums need depth map; brute all paths wrong.

### What the interviewer expects

Tie-breaking smallest level if asked; null-safe sum.

---

## Brute Force

DFS with depth map summing values — same **O(n)** but BFS is more natural for level indexing.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[1,7,0,7,-8,null,null]` — level sums: 1, 7, -1, 7 → max 7 at level 2 (1-indexed).

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
    public int maxLevelSum(TreeNode root) {
        Deque<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int level = 1, bestLevel = 1;
        long maxSum = Long.MIN_VALUE;
        while (!q.isEmpty()) {
            int size = q.size();
            long sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = q.removeFirst();
                sum += node.val;
                if (node.left != null) q.addLast(node.left);
                if (node.right != null) q.addLast(node.right);
            }
            if (sum > maxSum) {
                maxSum = sum;
                bestLevel = level;
            }
            level++;
        }
        return bestLevel;
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

func maxLevelSum(root *TreeNode) int {
    q := []*TreeNode{root}
    level, bestLevel := 1, 1
    maxSum := -1 << 62
    for len(q) > 0 {
        size := len(q)
        sum := 0
        for i := 0; i < size; i++ {
            node := q[0]
            q = q[1:]
            sum += node.Val
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        if sum > maxSum {
            maxSum = sum
            bestLevel = level
        }
        level++
    }
    return bestLevel
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

- Tie on sum — return smallest level number
- Single node — level 1
- All negative values — least negative level wins

---

## Interview Follow-ups

1. **Return the sum too?** — Track `maxSum` alongside `bestLevel`.
2. **K highest level sums?** — Store all level sums then select top K.
3. **DFS level sums?** — HashMap depth → sum, then scan keys.

---

## See Also

- [Previous: Maximum Width of Binary Tree](/dsa-coding/05-trees/maximum-width-of-binary-tree/)
- [Next: Graphs](/dsa-coding/06-graphs/_index/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
