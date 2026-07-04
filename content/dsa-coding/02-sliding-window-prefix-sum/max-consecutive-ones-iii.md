---
title: "Max Consecutive Ones III"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Variable Window pattern — Max Consecutive Ones III."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Max Consecutive Ones III"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.4"
weight: 204
languages: ["java", "golang"]
source: "https://leetcode.com/problems/max-consecutive-ones-iii/"
sourceLabel: "LeetCode 1004"
pattern: "Variable Window"
ShowToc: true
interviewHandbook: true
---
# Max Consecutive Ones III

**Source:** [LeetCode 1004](https://leetcode.com/problems/max-consecutive-ones-iii/) · **Pattern:** Variable Window · **Problem #16**

---

## Problem Statement

Given binary array `nums` and integer `k`, return the maximum number of consecutive 1's if you may flip at most `k` 0's.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 10⁵` |
| `k` | `0 ≤ k ≤ nums.length` |
| Values | `nums[i]` is 0 or 1 |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Longest subarray with at most `k` zeros — variable window counting zeros, shrink when count exceeds `k`.

### Why this pattern?

At most K zeros in window — shrink when zeros > K.

### Why not another pattern?

Prefix sum on binary array possible but window is cleaner O(n).

### What the interviewer expects

Count zeros in window; longest vs shortest invariant.

---

## Brute Force

Try every subarray, count zeros — **O(n²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[1,1,1,0,0,0,1,1,1,1]`, `k=2` → window with two flips gives length **6**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, zeros = 0, best = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > k) {
                if (nums[left++] == 0) zeros--;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func longestOnes(nums []int, k int) int {
    left, zeros, best := 0, 0, 0
    for right, v := range nums {
        if v == 0 {
            zeros++
        }
        for zeros > k {
            if nums[left] == 0 {
                zeros--
            }
            left++
        }
        if right-left+1 > best {
            best = right - left + 1
        }
    }
    return best
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

- `k = 0` — longest existing run of 1s
- All ones — entire array
- `k` >= zero count — whole array

---

## Interview Follow-ups

1. **Max with at most k of any value?** — Generalize zero counter to mismatch count.
2. **Minimum flips to all ones?** — Total zero count in array.
3. **Circular binary array?** — Double array or two-pass trick.

---

## See Also

- [Previous: Longest Substring with At Most K Distinct Characters](/dsa-coding/02-sliding-window-prefix-sum/longest-substring-k-distinct-characters/)
- [Next: Maximum Points You Can Obtain from Cards](/dsa-coding/02-sliding-window-prefix-sum/maximum-points-from-cards/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
