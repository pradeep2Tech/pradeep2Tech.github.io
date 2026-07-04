---
title: "Koko Eating Bananas"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Binary Search on Answer pattern — Koko Eating Bananas."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Koko Eating Bananas"
module: 3
moduleTitle: "Binary Search"
sectionRef: "3.5"
weight: 305
languages: ["java", "golang"]
source: "https://leetcode.com/problems/koko-eating-bananas/"
sourceLabel: "LeetCode 875"
pattern: "Binary Search on Answer"
interviewHandbook: true
---
# Koko Eating Bananas

**Source:** [LeetCode 875](https://leetcode.com/problems/koko-eating-bananas/) · **Pattern:** Binary Search on Answer · **Problem #25**

---

## Problem Statement

Koko has `piles[i]` bananas and must finish all piles within `h` hours. Each hour she picks a pile and eats `k` bananas (or the remainder if fewer remain). Return the **minimum integer `k`** such that she can finish in time.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ piles.length ≤ 10⁴` |
| Pile size | `1 ≤ piles[i] ≤ 10⁹` |
| Hours | `piles.length ≤ h ≤ 10⁹` |

---

## Pattern Recognition

**Canonical pattern:** [Binary Search](/dsa-coding/03-binary-search/) — full framework in module primer.

Minimize the maximum eating speed → monotonic feasibility: if speed `k` works, any `k' > k` also works. Binary search `k` in `[1, max(piles)]`.

### Why this pattern?

Monotone feasibility in speed → binary search on answer.

### Why not another pattern?

Per-speed simulation is check inside BS; greedy speed pick fails.

### What the interviewer expects

Prove if speed k works, k+1 works; find minimum k.

---

## Brute Force

Try every speed from `1` to `max(piles)` and simulate hours — **O(n · max(piles))**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`piles = [3,6,7,11]`, `h = 8`. `k=4` → hours `1+2+2+3=8` ✓. `k=3` → `1+2+3+4=10` ✗. Minimum feasible is **4**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1, high = 0;
        for (int p : piles) {
            high = Math.max(high, p);
        }
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (hoursNeeded(piles, mid) <= h) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private long hoursNeeded(int[] piles, int speed) {
        long hours = 0;
        for (int p : piles) {
            hours += (p + speed - 1L) / speed;
        }
        return hours;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func minEatingSpeed(piles []int, h int) int {
    low, high := 1, 0
    for _, p := range piles {
        if p > high {
            high = p
        }
    }
    for low < high {
        mid := low + (high-low)/2
        if hoursNeeded(piles, mid) <= h {
            high = mid
        } else {
            low = mid + 1
        }
    }
    return low
}

func hoursNeeded(piles []int, speed int) int64 {
    var hours int64
    for _, p := range piles {
        hours += int64((p + speed - 1) / speed)
    }
    return hours
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n log max(piles))
- **Space:** O(1)

---

## Edge Cases

- `h == piles.length` — must eat each pile in one hour → `k = max(piles)`
- Single pile
- Very large pile values — use 64-bit for hour sum

---

## Interview Follow-ups

1. **Why `low < high`?** — Finding minimum feasible — shrink upper bound when mid works.
2. **Ceil division?** — Use `(p + k - 1) / k` to avoid floating point.
3. **Similar problems?** — Capacity to ship, split array largest sum — same BS-on-answer shape.

---

## See Also

- [Previous: Missing Number in Sorted Array](/dsa-coding/03-binary-search/missing-number-in-sorted-array/)
- [Next: Aggressive Cows](/dsa-coding/03-binary-search/aggressive-cows/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
