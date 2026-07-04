---
title: "Validate Binary Search Tree"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DFS pattern — Validate Binary Search Tree."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Validate Binary Search Tree"
module: 5
moduleTitle: "Trees"
sectionRef: "5.2"
weight: 502
languages: ["java", "golang"]
source: "https://leetcode.com/problems/validate-binary-search-tree/"
sourceLabel: "LeetCode 98"
pattern: "DFS"
interviewHandbook: true
---
# Validate Binary Search Tree

**Source:** [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/) · **Pattern:** DFS · **Problem #34**

---

## Problem Statement

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST). For every node, all values in its left subtree are **strictly less** and all values in its right subtree are **strictly greater** than the node's value.

| Constraint | Value |
| :--- | :--- |
| Nodes | `1 ≤ tree nodes ≤ 10⁴` |
| Values | `-2³¹ ≤ Node.val ≤ 2³¹ - 1` |

---

## Pattern Recognition

**Canonical pattern:** [Trees](/dsa-coding/05-trees/) — full framework in module primer.

BST validity is a global ordering constraint, not local parent-child checks only. Pass `(min, max)` bounds down the tree or verify strictly increasing inorder traversal.

### Why this pattern?

BST = bounded range per node — pass (min, max) down.

### Why not another pattern?

Inorder compare only catches some errors; local parent check insufficient.

### What the interviewer expects

Use long bounds; null children inherit parent bound.

---

## Brute Force

For each node, verify entire left subtree max < node and right subtree min > node — **O(n²)** time on skewed trees.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[2,1,3]` — node 2 allows left in (-∞,2) and right in (2,∞); children 1 and 3 satisfy → `true`. `[5,1,4,null,null,3,6]` — node 5's right subtree contains 3 < 5 → `false`.

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
    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }

    private boolean validate(TreeNode node, Integer lo, Integer hi) {
        if (node == null) return true;
        if (lo != null && node.val <= lo) return false;
        if (hi != null && node.val >= hi) return false;
        return validate(node.left, lo, node.val)
            && validate(node.right, node.val, hi);
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

func isValidBST(root *TreeNode) bool {
    var validate func(node *TreeNode, lo, hi *int) bool
    validate = func(node *TreeNode, lo, hi *int) bool {
        if node == nil {
            return true
        }
        if lo != nil && node.Val <= *lo {
            return false
        }
        if hi != nil && node.Val >= *hi {
            return false
        }
        return validate(node.Left, lo, &node.Val) && validate(node.Right, &node.Val, hi)
    }
    return validate(root, nil, nil)
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(h)

---

## Edge Cases

- Duplicate values anywhere — invalid BST (strict inequality)
- Single node — valid
- Integer.MIN_VALUE / MAX_VALUE at boundaries

---

## Interview Follow-ups

1. **Inorder approach?** — Track previous inorder value; must strictly increase.
2. **BST with duplicates allowed?** — Relax to ≤ on left or ≥ on right per problem variant.
3. **Recover BST with two swapped nodes?** — Inorder finds out-of-order pair.

---

## See Also

- [Previous: Path Sum](/dsa-coding/05-trees/path-sum/)
- [Next: Lowest Common Ancestor of a BST](/dsa-coding/05-trees/lowest-common-ancestor-bst/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
