---
title: "Rod Cutting"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Unbounded Knapsack pattern — Rod Cutting."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Rod Cutting"
module: 8
moduleTitle: "Dynamic Programming"
sectionRef: "8.6"
weight: 806
languages: ["java", "golang"]
source: "https://www.geeksforgeeks.org/problems/rod-cutting0840/1"
sourceLabel: "GFG"
pattern: "Unbounded Knapsack"
ShowToc: true
interviewHandbook: true
---
# Rod Cutting

**Source:** [GFG](https://www.geeksforgeeks.org/problems/rod-cutting0840/1) · **Pattern:** Unbounded Knapsack · **Problem #55**

---

## Problem Statement

Given a rod of length `n` and an array `price[i]` for a piece of length `i+1`, maximize total revenue by cutting the rod (pieces may be reused in length decomposition).

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ n ≤ 10³` |
| Prices | Non-negative integers |

---

## Pattern Recognition

**Canonical pattern:** [Dynamic Programming](/dsa-coding/08-dynamic-programming/) — full framework in module primer.

Unbounded knapsack maximize: for each length `L`, try every cut length `i` with price `price[i-1]` and reuse remainder — mirror of Coin Change but maximize profit.

### Why this pattern?

Unbounded knapsack maximize price — same loop order as coin change.

### Why not another pattern?

Greedy by price/length ratio fails; recursion needs memo.

### What the interviewer expects

Cut vs no-cut at each length; parallel to coin change framing.

---

## Brute Force

Try all compositions of lengths summing to `n` — exponential.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`n=8`, prices `[1,5,8,9,10,17,17,20]`. Best: cut lengths 2 and 6 → `5 + 17 = 22` (beats a single length-8 piece worth `20`).

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int cutRod(int n, int[] price) {
        int[] dp = new int[n + 1];
        for (int len = 1; len <= n; len++) {
            for (int cut = 1; cut <= len; cut++) {
                dp[len] = Math.max(dp[len], price[cut - 1] + dp[len - cut]);
            }
        }
        return dp[n];
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func cutRod(n int, price []int) int {
    dp := make([]int, n+1)
    for length := 1; length <= n; length++ {
        for cut := 1; cut <= length; cut++ {
            val := price[cut-1] + dp[length-cut]
            if val > dp[length] {
                dp[length] = val
            }
        }
    }
    return dp[n]
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n²)
- **Space:** O(n)

---

## Edge Cases

- All zero prices → 0 revenue
- Single piece best — no cut
- Uniform price per unit — cut all length-1

---

## Interview Follow-ups

1. **Print cuts not just value?** — Backtrack from DP table.
2. **Limited supply per length?** — Becomes 0/1 knapsack.
3. **Relation to Coin Change?** — Min coins vs max price — same unbounded structure.

---

## See Also

- [Previous: Coin Change](/dsa-coding/08-dynamic-programming/coin-change/)
- [Next: Top 55 Interview Questions](/dsa-coding/09-interview-guide/top-55-interview-questions/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
