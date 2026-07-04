---
title: "Subset Sum"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DP pattern — Subset Sum."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Subset Sum"
module: 8
moduleTitle: "Dynamic Programming"
sectionRef: "8.3"
weight: 803
languages: ["java", "golang"]
source: "https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1"
sourceLabel: "GFG"
pattern: "DP"
interviewHandbook: true
---
# Subset Sum

**Source:** [GFG](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1) · **Pattern:** DP · **Problem #52**

---

## Problem Statement

Given an array of non-negative integers and a target `sum`, determine whether any subset of the array adds up to exactly `sum`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ arr.length ≤ 200` |
| Values / sum | `0 ≤ arr[i], sum ≤ 10⁴` |

---

## Pattern Recognition

**Canonical pattern:** [Dynamic Programming](/dsa-coding/08-dynamic-programming/) — full framework in module primer.

Decision knapsack: `dp[i][t]` = can we make target `t` using first `i` elements? Transition: skip `arr[i-1]` or take it if `t ≥ arr[i-1]`. Same problem as 0/1 knapsack with boolean states.

### Why this pattern?

Boolean knapsack — dp[sum] |= dp[sum-num] iterating nums.

### Why not another pattern?

Recursion without memo TLE; greedy fails arbitrary values.

### What the interviewer expects

Contrast with Module 4 recursion; iteration order for 0/1 reuse.

---

## Brute Force

Enumerate all 2ⁿ subsets — **O(2ⁿ)**. See the recursion-first walkthrough on [Subset Sum (Recursion)](/dsa-coding/04-recursion-backtracking/subset-sum-recursion/).

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`arr = [3, 34, 4, 12, 5, 2]`, `sum = 9`. Subset `{4,5}` works → return `true`. DP builds reachable sums `{0,2,3,4,5,7,9,...}`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean subsetSum(int[] arr, int sum) {
        boolean[] dp = new boolean[sum + 1];
        dp[0] = true;
        for (int num : arr) {
            for (int t = sum; t >= num; t--) {
                dp[t] = dp[t] || dp[t - num];
            }
        }
        return dp[sum];
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func subsetSum(arr []int, sum int) bool {
    dp := make([]bool, sum+1)
    dp[0] = true
    for _, num := range arr {
        for t := sum; t >= num; t-- {
            dp[t] = dp[t] || dp[t-num]
        }
    }
    return dp[sum]
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n · sum)
- **Space:** O(sum)

---

## Edge Cases

- `sum = 0` — always true (empty subset)
- Empty array with `sum > 0` — false
- Duplicate values — still works; each index used at most once

---

## Interview Follow-ups

1. **Recursion vs DP?** — Same state space; memoized recursion is the top-down view — compare with [Subset Sum (Recursion)](/dsa-coding/04-recursion-backtracking/subset-sum-recursion/).
2. **Count subsets with given sum?** — Use integer DP counts instead of boolean.
3. **Partition equal subset sum?** — Check subset sum for `total/2`.

---

## See Also

- [Previous: House Robber](/dsa-coding/08-dynamic-programming/house-robber/)
- [Next: Unique Paths](/dsa-coding/08-dynamic-programming/unique-paths/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
