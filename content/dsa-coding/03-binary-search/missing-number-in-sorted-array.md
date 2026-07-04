---
title: "Missing Number in Sorted Array"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Binary Search pattern — Missing Number in Sorted Array."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Missing Number in Sorted Array"
module: 3
moduleTitle: "Binary Search"
sectionRef: "3.4"
weight: 304
languages: ["java", "golang"]
source: "https://leetcode.com/problems/missing-number/"
sourceLabel: "LeetCode 268"
pattern: "Binary Search"
interviewHandbook: true
---
# Missing Number in Sorted Array

**Source:** [LeetCode 268](https://leetcode.com/problems/missing-number/) · **Pattern:** Binary Search · **Problem #24**

---

## Problem Statement

An array `nums` contains `n` distinct numbers in the range `[0, n]`. Exactly one number in that range is missing. Return it.

| Constraint | Value |
| :--- | :--- |
| `n` | `nums.length == n` |
| Values | `0 ≤ nums[i] ≤ n` |
| Uniqueness | All elements distinct |

---

## Pattern Recognition

**Canonical pattern:** [Binary Search](/dsa-coding/03-binary-search/) — full framework in module primer.

XOR of `0..n` with all elements cancels pairs and leaves the missing value — works on **unsorted** input in O(n). If the array were sorted, index mismatch `nums[i] != i` is a BS signal.

### Why this pattern?

Sorted with one missing — BS for first index where `nums[i] != i` (or variant).

### Why not another pattern?

Sum formula works only for specific ranges; HashMap O(n) space.

### What the interviewer expects

Predicate: `nums[mid] >= mid` style boundary search.

---

## Brute Force

Sort and scan for first `nums[i] != i`, or use a boolean array — **O(n log n)** or **O(n)** extra space.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums = [3,0,1]`, `n = 3`. XOR indices `0^1^2^3 = 0`. XOR values `3^0^1 = 2`. Result `0^2 = **2**`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int missingNumber(int[] nums) {
        int missing = nums.length;
        for (int i = 0; i < nums.length; i++) {
            missing ^= i ^ nums[i];
        }
        return missing;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func missingNumber(nums []int) int {
    missing := len(nums)
    for i, v := range nums {
        missing ^= i ^ v
    }
    return missing
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

- Missing `0` — e.g. `[1]`
- Missing `n` — e.g. `[0,1,2]`
- Single element `[0]` → answer `1`

---

## Interview Follow-ups

1. **Sorted array follow-up?** — BS on first index where `nums[i] != i`; answer is that index.
2. **Gauss sum?** — `n*(n+1)/2 - sum(nums)` — watch integer overflow on large n.
3. **Multiple missing numbers?** — Different problem — use set or bit tricks.

---

## See Also

- [Previous: Search a 2D Matrix](/dsa-coding/03-binary-search/search-a-2d-matrix/)
- [Next: Koko Eating Bananas](/dsa-coding/03-binary-search/koko-eating-bananas/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
