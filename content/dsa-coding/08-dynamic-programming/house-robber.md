---
title: "House Robber"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Include/Exclude pattern — House Robber."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "House Robber"
module: 8
moduleTitle: "Dynamic Programming"
sectionRef: "8.2"
weight: 802
languages: ["java", "golang"]
source: "https://leetcode.com/problems/house-robber/"
sourceLabel: "LeetCode 198"
pattern: "Include/Exclude"
interviewHandbook: true
---
# House Robber

**Source:** [LeetCode 198](https://leetcode.com/problems/house-robber/) · **Pattern:** Include/Exclude · **Problem #51**

---

## Problem Statement

Given non-negative integers representing money in each house, return the maximum amount you can rob without robbing two adjacent houses.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 100` |
| Values | `0 ≤ nums[i] ≤ 400` |

---

## Pattern Recognition

**Canonical pattern:** [Dynamic Programming](/dsa-coding/08-dynamic-programming/) — full framework in module primer.

At each house: rob it (+ best up to i-2) or skip it (best up to i-1). Linear include/exclude DP — adjacent constraint on a sequence.

### Why this pattern?

Include/exclude adjacent constraint — dp[i] = max(rob i + dp[i-2], dp[i-1]).

### Why not another pattern?

Greedy on max value fails on [2,1,1,2]; backtracking slow.

### What the interviewer expects

Two-variable rolling DP; explain why adjacent ban matters.

---

## Brute Force

Try all 2ⁿ subsets, reject adjacent pairs — **O(2ⁿ)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums = [2,7,9,3,1]`. Best: rob 2+9+1=12 (indices 0,2,4). DP: at index 2 max is 11 (2+9), at index 4 max is 12.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int rob(int[] nums) {
        int prevTake = 0, prevSkip = 0;
        for (int x : nums) {
            int take = x + prevSkip;
            int skip = Math.max(prevTake, prevSkip);
            prevTake = take;
            prevSkip = skip;
        }
        return Math.max(prevTake, prevSkip);
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func rob(nums []int) int {
    prevTake, prevSkip := 0, 0
    for _, x := range nums {
        take := x + prevSkip
        skip := prevTake
        if prevSkip > prevTake {
            skip = prevSkip
        }
        prevTake, prevSkip = take, skip
    }
    if prevTake > prevSkip {
        return prevTake
    }
    return prevSkip
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## Edge Cases

- Single house — return its value
- All zeros — return 0
- Alternating high values — skip optimally

---

## Interview Follow-ups

1. **Houses in a circle?** — Run linear robber on `0..n-2` and `1..n-1`, take max.
2. **Tree of houses?** — Tree DP — post-order include/exclude per node.
3. **Return which houses?** — Backtrack from DP table.

---

## See Also

- [Previous: Climbing Stairs](/dsa-coding/08-dynamic-programming/climbing-stairs/)
- [Next: Subset Sum](/dsa-coding/08-dynamic-programming/subset-sum-dp/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
