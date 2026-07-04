---
title: "Path Sum"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DFS pattern — Path Sum."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Path Sum"
module: 5
moduleTitle: "Trees"
sectionRef: "5.1"
weight: 501
languages: ["java", "golang"]
source: "https://leetcode.com/problems/path-sum/"
sourceLabel: "LeetCode 112"
pattern: "DFS"
interviewHandbook: true
---
# Path Sum

**Source:** [LeetCode 112](https://leetcode.com/problems/path-sum/) · **Pattern:** DFS · **Problem #33**

---

## Problem Statement

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that the sum of node values along the path equals `targetSum`. A leaf is a node with no children.

| Constraint | Value |
| :--- | :--- |
| Nodes | `0 ≤ tree nodes ≤ 5000` |
| Values | `-1000 ≤ Node.val ≤ 1000` |
| Target | `-1000 ≤ targetSum ≤ 1000` |

---

## Pattern Recognition

**Canonical pattern:** [Trees](/dsa-coding/05-trees/) — full framework in module primer.

Root-to-leaf decision on a tree → DFS carrying a running remainder. At each node subtract `val` from the target; at a leaf check if remainder is zero.

### Why this pattern?

Root-to-leaf DFS with running sum — subtract at each node.

### Why not another pattern?

BFS works but DFS is simpler; HashMap prefix on tree is follow-up.

### What the interviewer expects

Leaf check includes `left==null && right==null`; short-circuit on first hit if any path.

---

## Brute Force

Collect all root-to-leaf paths (DFS backtracking), sum each path, compare to target — **O(n)** paths in worst case skewed tree, **O(h)** space per path.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

Tree `[5,4,8,11,null,13,4,7,2,null,null,null,1]`, `targetSum = 22`. Path 5→4→11→2 sums to 22 → return `true`.

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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) {
            return targetSum == root.val;
        }
        int need = targetSum - root.val;
        return hasPathSum(root.left, need) || hasPathSum(root.right, need);
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

func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil {
        return false
    }
    if root.Left == nil && root.Right == nil {
        return targetSum == root.Val
    }
    need := targetSum - root.Val
    return hasPathSum(root.Left, need) || hasPathSum(root.Right, need)
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(h) recursion stack

---

## Edge Cases

- Empty tree (`root = null`) → false
- Single-node tree — leaf check only
- Negative node values — subtraction still valid

---

## Interview Follow-ups

1. **Return all path sums?** — Backtrack storing current path; collect at leaves.
2. **Path Sum II — return paths?** — DFS backtracking with path list.
3. **Any path (not root-to-leaf)?** — Use prefix sums on tree or convert to graph.

---

## See Also

- [Previous: Trees](/dsa-coding/05-trees/_index/)
- [Next: Validate Binary Search Tree](/dsa-coding/05-trees/validate-binary-search-tree/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
