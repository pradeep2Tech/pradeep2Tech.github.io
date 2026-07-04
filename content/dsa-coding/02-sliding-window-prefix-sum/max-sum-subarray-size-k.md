---
title: "Max Sum Subarray of Size K"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Fixed Window pattern — Max Sum Subarray of Size K."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Max Sum Subarray of Size K"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.1"
weight: 201
languages: ["java", "golang"]
source: "https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1"
sourceLabel: "GFG"
pattern: "Fixed Window"
interviewHandbook: true
---
# Max Sum Subarray of Size K

**Source:** [GFG](https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1) · **Pattern:** Fixed Window · **Problem #13**

---

## Problem Statement

Given an array of integers and integer `k`, find the maximum sum of any contiguous subarray of length exactly `k`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ n ≤ 10⁵` |
| `k` | `1 ≤ k ≤ n` |
| Values | Integer array elements |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Fixed window size → add entering element, subtract leaving element when `i >= k`. Track running max.

### Why this pattern?

Fixed window k — add right, drop left incrementally.

### Why not another pattern?

Prefix sum alone doesn't exploit fixed k; variable window unnecessary.

### What the interviewer expects

O(n) single pass; initialize first window before sliding.

---

## Brute Force

Sum every window of length `k` — **O(n · k)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums=[2,1,5,1,3,2]`, `k=3` → windows `8, 7, 9, 6` → max **9**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int maxSumSubarray(int[] nums, int k) {
        int windowSum = 0, maxSum = 0;
        for (int i = 0; i < nums.length; i++) {
            windowSum += nums[i];
            if (i >= k) windowSum -= nums[i - k];
            if (i >= k - 1) maxSum = Math.max(maxSum, windowSum);
        }
        return maxSum;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func maxSumSubarray(nums []int, k int) int {
    windowSum, maxSum := 0, 0
    for i, x := range nums {
        windowSum += x
        if i >= k {
            windowSum -= nums[i-k]
        }
        if i >= k-1 && windowSum > maxSum {
            maxSum = windowSum
        }
    }
    return maxSum
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

- `k == n` — whole array is the window
- `k == 1` — max element
- All negative numbers — least negative window

---

## Interview Follow-ups

1. **Variable window max sum?** — Kadane's algorithm.
2. **Average of size-k windows?** — Same template, divide at end.
3. **Circular array?** — Duplicate array or modulo indexing.

---

## See Also

- [Previous: Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/_index/)
- [Next: Longest Substring Without Repeating Characters](/dsa-coding/02-sliding-window-prefix-sum/longest-substring-without-repeating-characters/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
