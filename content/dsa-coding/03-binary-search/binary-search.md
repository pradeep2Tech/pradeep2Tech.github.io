---
title: "Binary Search"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Classic pattern — Binary Search."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Binary Search"
module: 3
moduleTitle: "Binary Search"
sectionRef: "3.1"
weight: 301
languages: ["java", "golang"]
source: "https://leetcode.com/problems/binary-search/"
sourceLabel: "LeetCode 704"
pattern: "Classic"
interviewHandbook: true
---
# Binary Search

**Source:** [LeetCode 704](https://leetcode.com/problems/binary-search/) · **Pattern:** Classic · **Problem #21**

---

## Problem Statement

Given a sorted array `nums` of distinct integers and a `target`, return the index of `target` if found, otherwise `-1`. You must run in **O(log n)** time.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 10⁴` |
| Values | `-10⁴ ≤ nums[i], target ≤ 10⁴` |
| Array | Sorted ascending, all values unique |

---

## Pattern Recognition

**Canonical pattern:** [Binary Search](/dsa-coding/03-binary-search/) — full framework in module primer.

Sorted array + lookup by value → halve the search space each step. Compare `nums[mid]` with `target` and discard the impossible half.

### Why this pattern?

Sorted array + exact target → inclusive binary search O(log n).

### Why not another pattern?

Linear scan O(n) misses log requirement; HashMap ignores order.

### What the interviewer expects

Mid overflow guard; lo/hi termination; return -1 case.

---

## Brute Force

Linear scan left to right — **O(n)** time, **O(1)** space. Correct but violates the logarithmic requirement.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums = [-1,0,3,5,9,12]`, `target = 9`. `mid=2 → nums[2]=3 < 9` → `low=3`. `mid=4 → nums[4]=9` → return **4**.

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
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
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
        switch {
        case nums[mid] == target:
            return mid
        case nums[mid] < target:
            low = mid + 1
        default:
            high = mid - 1
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

- Target at first or last index
- Target not present — return `-1`
- Single-element array

---

## Interview Follow-ups

1. **Duplicates allowed?** — Use `while (low < high)` left-bias to find first/last occurrence.
2. **Recursive BS?** — Same logic; iterative preferred for stack safety.
3. **Off-by-one bugs?** — Always test `low == high` and empty-range exit.

---

## See Also

- [Previous: Binary Search](/dsa-coding/03-binary-search/_index/)
- [Next: Search in Rotated Sorted Array](/dsa-coding/03-binary-search/search-in-rotated-sorted-array/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
