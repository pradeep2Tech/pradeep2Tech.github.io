---
title: "Subset Sum"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Recursion pattern — Subset Sum."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Subset Sum"
module: 4
moduleTitle: "Recursion & Backtracking"
sectionRef: "4.2"
weight: 402
languages: ["java", "golang"]
source: "https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1"
sourceLabel: "GFG"
pattern: "Recursion"
ShowToc: true
interviewHandbook: true
---
# Subset Sum

**Source:** [GFG](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1) · **Pattern:** Recursion · **Problem #28**

---

## Problem Statement

Given a non-empty array `arr` of non-negative integers and a target `sum`, return `true` if some subset of elements adds exactly to `sum`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ arr.length ≤ 200` |
| Values | `0 ≤ arr[i] ≤ 10³` |
| Target | `0 ≤ sum ≤ 10³` |

---

## Pattern Recognition

**Canonical pattern:** [Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/) — full framework in module primer.

Each element: include or exclude. Recursion tree has two branches per index. Base cases: `sum == 0` → true; index exhausted → false.

### Why this pattern?

Include/exclude decision tree — explore with backtracking before DP optimization.

### Why not another pattern?

Greedy fails; HashMap doesn't enumerate subsets.

### What the interviewer expects

State recursion depth; mention DP follow-up when subproblems overlap.

---

## Brute Force

Generate all `2^n` subsets and check sums — **O(2^n · n)** time.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`arr = [3, 34, 4, 12, 5, 2]`, `sum = 9`. Pick 3 → need 6; pick 4 → need 2; pick 2 → need 0 → **true**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean subsetSum(int[] arr, int sum) {
        return dfs(arr, 0, sum);
    }

    private boolean dfs(int[] arr, int index, int remaining) {
        if (remaining == 0) {
            return true;
        }
        if (index == arr.length || remaining < 0) {
            return false;
        }
        return dfs(arr, index + 1, remaining - arr[index])
                || dfs(arr, index + 1, remaining);
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func subsetSum(arr []int, sum int) bool {
    var dfs func(int, int) bool
    dfs = func(index, remaining int) bool {
        if remaining == 0 {
            return true
        }
        if index == len(arr) || remaining < 0 {
            return false
        }
        return dfs(index+1, remaining-arr[index]) || dfs(index+1, remaining)
    }
    return dfs(0, sum)
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(2^n) worst case
- **Space:** O(n) recursion stack

---

## Edge Cases

- `sum == 0` — empty subset always works
- Single element equals target
- No subset sums to target

---

## Interview Follow-ups

1. **Memoization / DP?** — `dp[i][s]` — reduces to O(n · sum) pseudo-polynomial.
2. **Print the subset?** — Track chosen indices during recursion.
3. **Count subsets?** — Same tree; add counts from include + exclude branches.

---

## See Also

- [Previous: Valid Parentheses](/dsa-coding/04-recursion-backtracking/valid-parentheses/)
- [Next: Letter Combinations of a Phone Number](/dsa-coding/04-recursion-backtracking/letter-combinations-of-phone-number/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
