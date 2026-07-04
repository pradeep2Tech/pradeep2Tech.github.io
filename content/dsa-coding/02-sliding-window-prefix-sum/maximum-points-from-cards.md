---
title: "Maximum Points You Can Obtain from Cards"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Sliding Window pattern — Maximum Points You Can Obtain from Cards."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Maximum Points You Can Obtain from Cards"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.5"
weight: 205
languages: ["java", "golang"]
source: "https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/"
sourceLabel: "LeetCode 1423"
pattern: "Sliding Window"
ShowToc: true
interviewHandbook: true
---
# Maximum Points You Can Obtain from Cards

**Source:** [LeetCode 1423](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) · **Pattern:** Sliding Window · **Problem #17**

---

## Problem Statement

From integer array `cardPoints` and integer `k`, take exactly `k` cards from either end (one per turn). Maximize the sum of taken cards.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ cardPoints.length ≤ 10⁵` |
| `k` | `1 ≤ k ≤ cardPoints.length` |
| Values | `1 ≤ cardPoints[i] ≤ 10⁴` |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Taking `k` from ends ⇔ leaving a contiguous middle subarray of length `n-k`. Minimize middle sum → sliding window complement.

### Why this pattern?

Take k cards from ends = minimize sum of middle subarray of size n-k.

### Why not another pattern?

Greedy from ends wrong; sliding window on middle segment.

### What the interviewer expects

Reframe problem; fixed window size n-k.

---

## Brute Force

Try all `k+1` splits of how many from left vs right — **O(k)**. Sliding-window complement on the middle is **O(n)** and clearer at scale.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[1,2,3,4,5,6,1]`, `k=3` → take `6+1+1=8` or via complement skip middle min sum.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int window = n - k, windowSum = 0, total = 0;
        for (int i = 0; i < n; i++) total += cardPoints[i];
        for (int i = 0; i < window; i++) windowSum += cardPoints[i];
        int minWindow = windowSum;
        for (int i = window; i < n; i++) {
            windowSum += cardPoints[i] - cardPoints[i - window];
            minWindow = Math.min(minWindow, windowSum);
        }
        return total - minWindow;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func maxScore(cardPoints []int, k int) int {
    n := len(cardPoints)
    window := n - k
    total, windowSum := 0, 0
    for _, x := range cardPoints {
        total += x
    }
    for i := 0; i < window; i++ {
        windowSum += cardPoints[i]
    }
    minWindow := windowSum
    for i := window; i < n; i++ {
        windowSum += cardPoints[i] - cardPoints[i-window]
        if windowSum < minWindow {
            minWindow = windowSum
        }
    }
    return total - minWindow
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

- `k == n` — sum entire array
- `k == 1` — max of first and last
- `window == 0` — take all from ends only

---

## Interview Follow-ups

1. **Take at most k?** — Also consider shorter takes — not this problem variant.
2. **Three-end deque?** — Different problem; still greedy or DP.
3. **Why complement works?** — Fixed count taken implies fixed middle length.

---

## See Also

- [Previous: Max Consecutive Ones III](/dsa-coding/02-sliding-window-prefix-sum/max-consecutive-ones-iii/)
- [Next: Equal Left and Right Subarray Sum](/dsa-coding/02-sliding-window-prefix-sum/equal-left-right-subarray-sum/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
