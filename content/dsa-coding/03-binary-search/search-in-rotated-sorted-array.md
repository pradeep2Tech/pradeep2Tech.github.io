---
title: "Search in Rotated Sorted Array"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Modified Binary Search pattern — Search in Rotated Sorted Array."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Search in Rotated Sorted Array"
module: 3
moduleTitle: "Binary Search"
sectionRef: "3.2"
weight: 302
languages: ["java", "golang"]
source: "https://leetcode.com/problems/search-in-rotated-sorted-array/"
sourceLabel: "LeetCode 33"
pattern: "Modified Binary Search"
ShowToc: true
interviewHandbook: true
---
# Search in Rotated Sorted Array

**Source:** [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) · **Pattern:** Modified Binary Search · **Problem #22**

---

## Problem Statement

An array sorted in ascending order was rotated at an unknown pivot. Given `nums` and `target`, return the index of `target` or `-1`. Assume no duplicates.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 5000` |
| Values | `-10⁴ ≤ nums[i], target ≤ 10⁴` |
| Array | Originally sorted, rotated, all unique |

---

## Pattern Recognition

**Canonical pattern:** [Binary Search](/dsa-coding/03-binary-search/) — full framework in module primer.

At any `mid`, one half `[low..mid]` or `[mid..high]` is fully sorted. Check which half is sorted, then decide if `target` lies inside it.

### Why this pattern?

One half always sorted — discard the other.

### Why not another pattern?

Plain BS on unsorted half fails; two pointers don't apply.

### What the interviewer expects

Identify sorted half with `nums[left] <= nums[mid]`; compare target to sorted range.

---

## Brute Force

Scan the array linearly — **O(n)**. Works but ignores rotation structure.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums = [4,5,6,7,0,1,2]`, `target = 0`. `mid=3, nums[3]=7`; left `[4,5,6,7]` sorted. `0` not in `[4,7]` → `low=4`. `mid=5, nums[5]=1`; right sorted; `0` in `[0,2]` → `high=4`. `mid=4, nums[4]=0` → return **4**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func search(nums []int, target int) int {
    low, high := 0, len(nums)-1
    for low <= high {
        mid := low + (high-low)/2
        if nums[mid] == target {
            return mid
        }
        if nums[low] <= nums[mid] {
            if nums[low] <= target && target < nums[mid] {
                high = mid - 1
            } else {
                low = mid + 1
            }
        } else {
            if nums[mid] < target && target <= nums[high] {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
    }
    return -1
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(log n)
- **Space:** O(1)

---

## Edge Cases

- Array not rotated (pivot at 0)
- Target at pivot index
- Two-element rotation `[1,3]`

---

## Interview Follow-ups

1. **With duplicates?** — When `nums[low]==nums[mid]==nums[high]`, shrink bounds — worst O(n).
2. **Find minimum element?** — BS variant: move toward unsorted half.
3. **Find rotation count?** — Index of minimum equals rotation offset.

---

## See Also

- [Previous: Binary Search](/dsa-coding/03-binary-search/binary-search/)
- [Next: Search a 2D Matrix](/dsa-coding/03-binary-search/search-a-2d-matrix/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
