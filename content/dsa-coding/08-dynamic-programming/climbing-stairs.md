---
title: "Climbing Stairs"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Fibonacci DP pattern — Climbing Stairs."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Climbing Stairs"
module: 8
moduleTitle: "Dynamic Programming"
sectionRef: "8.1"
weight: 801
languages: ["java", "golang"]
source: "https://leetcode.com/problems/climbing-stairs/"
sourceLabel: "LeetCode 70"
pattern: "Fibonacci DP"
interviewHandbook: true
---
# Climbing Stairs

**Source:** [LeetCode 70](https://leetcode.com/problems/climbing-stairs/) · **Pattern:** Fibonacci DP · **Problem #50**

---

## Problem Statement

You climb a staircase with `n` steps. Each time you can take 1 or 2 steps. Return how many distinct ways to reach the top.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ n ≤ 45` |

---

## Pattern Recognition

**Canonical pattern:** [Dynamic Programming](/dsa-coding/08-dynamic-programming/) — full framework in module primer.

Ways to reach step `i` = ways to `i-1` + ways to `i-2` — classic Fibonacci recurrence. Signals: counting paths with fixed step sizes, only last two states matter.

### Why this pattern?

Fibonacci recurrence — ways(n) = ways(n-1) + ways(n-2).

### Why not another pattern?

Brute recursion exponential; greedy doesn't exist.

### What the interviewer expects

O(1) space rolling vars; connect to Fibonacci without jargon overload.

---

## Brute Force

Recursive enumeration of all 1/2 step sequences — **O(2ⁿ)** without memo.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`n = 3`. Ways: `1+1+1`, `1+2`, `2+1` → **3**. Matches `dp[3]=dp[2]+dp[1]=2+1`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int prev2 = 1, prev1 = 2;
        for (int i = 3; i <= n; i++) {
            int cur = prev1 + prev2;
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func climbStairs(n int) int {
    if n <= 2 {
        return n
    }
    prev2, prev1 := 1, 2
    for i := 3; i <= n; i++ {
        cur := prev1 + prev2
        prev2, prev1 = prev1, cur
    }
    return prev1
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

- `n = 1` → 1 way
- `n = 2` → 2 ways
- Large `n` fits in 32-bit int for given constraints

---

## Interview Follow-ups

1. **Steps 1, 2, or 3?** — Tribonacci recurrence `dp[i]=dp[i-1]+dp[i-2]+dp[i-3]`.
2. **Min cost per step?** — Min-path DP, not counting.
3. **Matrix exponentiation?** — O(log n) for huge n.

---

## See Also

- [Previous: Dynamic Programming](/dsa-coding/08-dynamic-programming/_index/)
- [Next: House Robber](/dsa-coding/08-dynamic-programming/house-robber/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
