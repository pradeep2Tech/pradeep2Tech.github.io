---
title: "3Sum Closest"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Two Pointers pattern — 3Sum Closest."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "3Sum Closest"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.8"
weight: 108
languages: ["java", "golang"]
source: "https://leetcode.com/problems/3sum-closest/"
sourceLabel: "LeetCode 16"
pattern: "Two Pointers"
interviewHandbook: true
---
# 3Sum Closest

**Source:** [LeetCode 16](https://leetcode.com/problems/3sum-closest/) · **Pattern:** Two Pointers · **Problem #8**

---

## Problem Statement

Given integer array `nums` and integer `target`, find three integers such that the sum is closest to `target`. Return that sum.

| Constraint | Value |
| :--- | :--- |
| `n` | `3 ≤ nums.length ≤ 1000` |
| Values | `-1000 ≤ nums[i] ≤ 1000` |
| `-10⁴ ≤ target ≤ 10⁴` | Guaranteed unique closest sum |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Same skeleton as 3Sum: sort, fix `i`, two pointers — but track minimum `|sum - target|` instead of collecting triplets.

### Why this pattern?

Same skeleton as 3Sum but track min |sum-target| instead of collecting triplets.

### Why not another pattern?

Ternary search unreliable with duplicates; brute force too slow.

### What the interviewer expects

Clarify you still sort once; update closest inside two-pointer loop.

---

## Brute Force

Try every triplet — **O(n³)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums=[-1,2,1,-4]`, `target=1` → best triplet sum **2** (`-1+2+1`).

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.length - 2; i++) {
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (Math.abs(sum - target) < Math.abs(closest - target)) {
                    closest = sum;
                }
                if (sum < target) l++;
                else if (sum > target) r--;
                else return sum;
            }
        }
        return closest;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func threeSumClosest(nums []int, target int) int {
    sort.Ints(nums)
    closest := nums[0] + nums[1] + nums[2]
    for i := 0; i < len(nums)-2; i++ {
        l, r := i+1, len(nums)-1
        for l < r {
            sum := nums[i] + nums[l] + nums[r]
            if abs(sum-target) < abs(closest-target) {
                closest = sum
            }
            if sum < target {
                l++
            } else if sum > target {
                r--
            } else {
                return sum
            }
        }
    }
    return closest
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n²)
- **Space:** O(1)

---

## Edge Cases

- Exact match early exit
- Negative-heavy arrays
- Length 3 — only one triplet

---

## Interview Follow-ups

1. **Return indices?** — Store best `(i,l,r)` while tracking closest.
2. **k-sum closest?** — Generalize with recursion + two-pointer base.
3. **Why sort?** — Enables monotone pointer moves toward target.

---

## See Also

- [Previous: 3Sum](/dsa-coding/01-arrays-hashmap-two-pointers/3sum/)
- [Next: 4Sum](/dsa-coding/01-arrays-hashmap-two-pointers/4sum/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
