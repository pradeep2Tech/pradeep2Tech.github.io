---
title: "Equal Left and Right Subarray Sum"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Prefix Sum pattern — Equal Left and Right Subarray Sum."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Equal Left and Right Subarray Sum"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.6"
weight: 206
languages: ["java", "golang"]
source: "https://leetcode.com/problems/find-pivot-index/"
sourceLabel: "LeetCode 724"
pattern: "Prefix Sum"
interviewHandbook: true
---
# Equal Left and Right Subarray Sum

**Source:** [LeetCode 724](https://leetcode.com/problems/find-pivot-index/) · **Pattern:** Prefix Sum · **Problem #18**

---

## Problem Statement

Return the **pivot index** where sum of numbers to the left equals sum to the right. If none exists, return `-1`. The pivot is excluded from both sides.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 10⁴` |
| Values | `-1000 ≤ nums[i] ≤ 1000` |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Prefix sum pivot — track `leftSum` while iterating; `rightSum = total - leftSum - nums[i]`.

### Why this pattern?

Prefix sum — pivot where left sum equals right sum.

### Why not another pattern?

Two pointers don't give range sums; HashMap overkill.

### What the interviewer expects

O(n) prefix build; exclude pivot from both sides.

---

## Brute Force

For each index, rescan left and right — **O(n²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[1,7,3,6,5,6]` → at index 3, left `1+7+3=11`, right `5+6=11` → return **3**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        int left = 0;
        for (int i = 0; i < nums.length; i++) {
            int right = total - left - nums[i];
            if (left == right) return i;
            left += nums[i];
        }
        return -1;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func pivotIndex(nums []int) int {
    total := 0
    for _, x := range nums {
        total += x
    }
    left := 0
    for i, x := range nums {
        if left == total-left-x {
            return i
        }
        left += x
    }
    return -1
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

- Pivot at index 0 — left sum empty (0)
- Pivot at last index — right sum empty (0)
- No pivot → -1

---

## Interview Follow-ups

1. **Multiple pivots?** — Return first per problem spec.
2. **2D matrix pivot?** — Prefix sums per row/column.
3. **Product instead of sum?** — Track prefix products with division checks.

---

## See Also

- [Previous: Maximum Points You Can Obtain from Cards](/dsa-coding/02-sliding-window-prefix-sum/maximum-points-from-cards/)
- [Next: Trapping Rain Water](/dsa-coding/02-sliding-window-prefix-sum/trapping-rain-water/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
