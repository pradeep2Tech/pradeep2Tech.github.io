---
title: "Unique Paths"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Grid DP pattern — Unique Paths."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Unique Paths"
module: 8
moduleTitle: "Dynamic Programming"
sectionRef: "8.4"
weight: 804
languages: ["java", "golang"]
source: "https://leetcode.com/problems/unique-paths/"
sourceLabel: "LeetCode 62"
pattern: "Grid DP"
interviewHandbook: true
---
# Unique Paths

**Source:** [LeetCode 62](https://leetcode.com/problems/unique-paths/) · **Pattern:** Grid DP · **Problem #53**

---

## Problem Statement

A robot on an `m × n` grid starts at top-left and can only move right or down. Return the number of unique paths to the bottom-right corner.

| Constraint | Value |
| :--- | :--- |
| Grid | `1 ≤ m, n ≤ 100` |

---

## Pattern Recognition

**Canonical pattern:** [Dynamic Programming](/dsa-coding/08-dynamic-programming/) — full framework in module primer.

Paths to `(i,j)` = paths from above + paths from left. First row/column are all 1s — 2D grid DP collapses to 1D row.

### Why this pattern?

Grid DP — paths(i,j) = paths(i-1,j) + paths(i,j-1).

### Why not another pattern?

Combinatorics formula possible but DP generalizes with obstacles follow-up.

### What the interviewer expects

First row/column base cases; O(mn) time, O(n) space compression.

---

## Brute Force

DFS all right/down paths — exponential in `m+n`.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`m=3, n=2`. Paths: RRD, RDR, DRR → **3**. First row `[1,1]`; second row `[1,2]`; third `[1,3]`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func uniquePaths(m, n int) int {
    dp := make([]int, n)
    for j := range dp {
        dp[j] = 1
    }
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            dp[j] += dp[j-1]
        }
    }
    return dp[n-1]
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(m · n)
- **Space:** O(n)

---

## Edge Cases

- `m = 1` or `n = 1` — exactly one path
- Small grid `1×1` → 1
- Combinatorics formula C(m+n-2, m-1) also works

---

## Interview Follow-ups

1. **Obstacles in grid?** — DP with blocked cells set to 0.
2. **Min path sum?** — Grid DP storing min not count.
3. **Modulo large answer?** — Use combinatorics with mod at each multiply.

---

## See Also

- [Previous: Subset Sum](/dsa-coding/08-dynamic-programming/subset-sum-dp/)
- [Next: Coin Change](/dsa-coding/08-dynamic-programming/coin-change/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
