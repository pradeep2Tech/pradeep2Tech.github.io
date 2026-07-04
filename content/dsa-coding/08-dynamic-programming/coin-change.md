---
title: "Coin Change"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "DP pattern — Coin Change."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Coin Change"
module: 8
moduleTitle: "Dynamic Programming"
sectionRef: "8.5"
weight: 805
languages: ["java", "golang"]
source: "https://leetcode.com/problems/coin-change/"
sourceLabel: "LeetCode 322"
pattern: "DP"
interviewHandbook: true
---
# Coin Change

**Source:** [LeetCode 322](https://leetcode.com/problems/coin-change/) · **Pattern:** DP · **Problem #54**

---

## Problem Statement

Given coin denominations and an amount, return the fewest number of coins needed to make up that amount, or `-1` if impossible.

| Constraint | Value |
| :--- | :--- |
| Coins | `1 ≤ coins.length ≤ 12` |
| Amount | `0 ≤ amount ≤ 10⁴` |
| Values | `1 ≤ coins[i] ≤ 2³¹ - 1` |

---

## Pattern Recognition

**Canonical pattern:** [Dynamic Programming](/dsa-coding/08-dynamic-programming/) — full framework in module primer.

Unbounded knapsack / min-cost: for each amount, try every coin and take minimum. `dp[a] = min(dp[a], 1 + dp[a - coin])`.

### Why this pattern?

Unbounded knapsack — outer amount loop, inner coins; min coins.

### Why not another pattern?

Greedy fails on [1,3,4] target 6; DFS exponential.

### What the interviewer expects

Initialize dp with INF; dp[0]=0; loop direction proves reuse.

---

## Brute Force

Recursive try-all-coins with memo — same complexity as DP but top-down.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`coins = [1,2,5]`, `amount = 11`. Best: `5+5+1` → **3** coins. `dp[11]=min(dp[10]+1, dp[9]+1, dp[6]+1)=3`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int a = 1; a <= amount; a++) {
            for (int c : coins) {
                if (c <= a) {
                    dp[a] = Math.min(dp[a], dp[a - c] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func coinChange(coins []int, amount int) int {
    dp := make([]int, amount+1)
    for i := 1; i <= amount; i++ {
        dp[i] = amount + 1
    }
    for a := 1; a <= amount; a++ {
        for _, c := range coins {
            if c <= a && dp[a-c]+1 < dp[a] {
                dp[a] = dp[a-c] + 1
            }
        }
    }
    if dp[amount] > amount {
        return -1
    }
    return dp[amount]
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(amount · |coins|)
- **Space:** O(amount)

---

## Edge Cases

- `amount = 0` → 0 coins
- No combination possible → -1
- Greedy fails (e.g. coins `[1,3,4]`, amount 6) — must use DP

---

## Interview Follow-ups

1. **Count ways to make amount?** — Sum transitions instead of min.
2. **Bounded coin supply?** — 0/1 knapsack per coin denomination.
3. **BFS on amount graph?** — Also O(amount · |coins|); DP is simpler.

---

## See Also

- [Previous: Unique Paths](/dsa-coding/08-dynamic-programming/unique-paths/)
- [Next: Rod Cutting](/dsa-coding/08-dynamic-programming/rod-cutting/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
