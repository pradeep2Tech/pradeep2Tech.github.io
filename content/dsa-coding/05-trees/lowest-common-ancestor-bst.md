---
title: "Lowest Common Ancestor of a BST"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DFS pattern — Lowest Common Ancestor of a BST."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Lowest Common Ancestor of a BST"
module: 5
moduleTitle: "Trees"
sectionRef: "5.3"
weight: 503
languages: ["java", "golang"]
source: "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/"
sourceLabel: "LeetCode 235"
pattern: "DFS"
ShowToc: true
interviewHandbook: true
---
# Lowest Common Ancestor of a BST

**Source:** [LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · **Pattern:** DFS · **Problem #35**

---

## Problem Statement

Given a BST `root` and two nodes `p` and `q`, return the lowest common ancestor (LCA) — the lowest node that has both `p` and `q` as descendants (a node can be its own descendant).

| Constraint | Value |
| :--- | :--- |
| Nodes | `2 ≤ tree nodes ≤ 10⁵` |
| Values | Unique; `-10⁹ ≤ Node.val ≤ 10⁹` |
| Guarantee | `p` and `q` exist in the BST |

---

## Pattern Recognition

**Canonical pattern:** [Trees](/dsa-coding/05-trees/) — full framework in module primer.

BST ordering lets you decide direction without searching both subtrees: if both targets are smaller, go left; both larger, go right; otherwise current node is the split point (LCA).

### Why this pattern?

BST ordering routes search — split when p and q on different sides.

### Why not another pattern?

Generic tree LCA uses parent pointers; brute path lists O(n) space.

### What the interviewer expects

O(h) iterative descent; exploit BST property explicitly.

---

## Brute Force

Store paths from root to `p` and `q`, compare prefix — **O(h)** time and space but extra path storage.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

BST `[6,2,8,0,4,7,9,null,null,3,5]`, `p=2`, `q=8`. At 6 both are on different sides → LCA is 6. For `p=2`, `q=4`: at 6 go left; at 2 one equals root → LCA is 2.

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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int pv = p.val, qv = q.val;
        while (root != null) {
            if (pv < root.val && qv < root.val) {
                root = root.left;
            } else if (pv > root.val && qv > root.val) {
                root = root.right;
            } else {
                return root;
            }
        }
        return null;
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

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    pv, qv := p.Val, q.Val
    for root != nil {
        if pv < root.Val && qv < root.Val {
            root = root.Left
        } else if pv > root.Val && qv > root.Val {
            root = root.Right
        } else {
            return root
        }
    }
    return nil
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(h)
- **Space:** O(1)

---

## Edge Cases

- One node is ancestor of the other — that node is the LCA
- Adjacent parent-child pair
- Deep skewed tree — still O(h)

---

## Interview Follow-ups

1. **General binary tree LCA?** — Postorder DFS or parent-pointer + set intersection.
2. **Multiple queries on same tree?** — Euler tour + RMQ preprocessing.
3. **Return path to LCA?** — Record directions during the walk.

---

## See Also

- [Previous: Validate Binary Search Tree](/dsa-coding/05-trees/validate-binary-search-tree/)
- [Next: Binary Tree Right Side View](/dsa-coding/05-trees/binary-tree-right-side-view/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
