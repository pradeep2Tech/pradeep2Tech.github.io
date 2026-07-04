---
title: "Trapping Rain Water"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Prefix/Suffix pattern — Trapping Rain Water."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Trapping Rain Water"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.7"
weight: 207
languages: ["java", "golang"]
source: "https://leetcode.com/problems/trapping-rain-water/"
sourceLabel: "LeetCode 42"
pattern: "Prefix/Suffix"
ShowToc: true
interviewHandbook: true
---
# Trapping Rain Water

**Source:** [LeetCode 42](https://leetcode.com/problems/trapping-rain-water/) · **Pattern:** Prefix/Suffix · **Problem #19**

---

## Problem Statement

Given non-negative elevation map `height`, compute how much water can be trapped after raining.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ height.length ≤ 2·10⁴` |
| Heights | `0 ≤ height[i] ≤ 10⁵` |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Water at `i` is `min(maxLeft, maxRight) - height[i]`. Two pointers or prefix/suffix max arrays.

### Why this pattern?

Prefix max from both sides or two-pointer — each cell bounded by min(leftMax, rightMax).

### Why not another pattern?

Stack/monotonic variant exists but prefix is interview-default.

### What the interviewer expects

Explain water level intuition; O(1) space two-pointer follow-up.

---

## Brute Force

For each bar, scan left/right max — **O(n²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[0,1,0,2,1,0,1,3,2,1,2,1]` → total trapped **6** units.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int trap(int[] height) {
        int l = 0, r = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;
        while (l < r) {
            if (height[l] < height[r]) {
                if (height[l] >= leftMax) leftMax = height[l];
                else water += leftMax - height[l];
                l++;
            } else {
                if (height[r] >= rightMax) rightMax = height[r];
                else water += rightMax - height[r];
                r--;
            }
        }
        return water;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func trap(height []int) int {
    l, r := 0, len(height)-1
    leftMax, rightMax, water := 0, 0, 0
    for l < r {
        if height[l] < height[r] {
            if height[l] >= leftMax {
                leftMax = height[l]
            } else {
                water += leftMax - height[l]
            }
            l++
        } else {
            if height[r] >= rightMax {
                rightMax = height[r]
            } else {
                water += rightMax - height[r]
            }
            r--
        }
    }
    return water
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

- Monotonic increasing — 0 water
- Flat terrain — 0 water
- Single bar — 0 water

---

## Interview Follow-ups

1. **Prefix array version?** — Precompute `leftMax[i]`, `rightMax[i]`.
2. **Trapping with walls at ends?** — Same formula.
3. **Largest rectangle in histogram?** — Different stack problem.

---

## See Also

- [Previous: Equal Left and Right Subarray Sum](/dsa-coding/02-sliding-window-prefix-sum/equal-left-right-subarray-sum/)
- [Next: Subdomain Visit Count](/dsa-coding/02-sliding-window-prefix-sum/subdomain-visit-count/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
