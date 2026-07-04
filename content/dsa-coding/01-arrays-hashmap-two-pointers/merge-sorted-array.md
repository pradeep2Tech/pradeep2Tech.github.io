---
title: "Merge Sorted Array"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Two Pointers pattern — Merge Sorted Array."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Merge Sorted Array"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.10"
weight: 110
languages: ["java", "golang"]
source: "https://leetcode.com/problems/merge-sorted-array/"
sourceLabel: "LeetCode 88"
pattern: "Two Pointers"
interviewHandbook: true
---
# Merge Sorted Array

**Source:** [LeetCode 88](https://leetcode.com/problems/merge-sorted-array/) · **Pattern:** Two Pointers · **Problem #10**

---

## Problem Statement

Merge two sorted arrays `nums1` (length `m+n` with first `m` elements valid) and `nums2` (length `n`) into `nums1` in non-decreasing order **in-place**.

| Constraint | Value |
| :--- | :--- |
| `m, n` | `0 ≤ m, n ≤ 200` |
| Values | `-10⁹ ≤ nums[i] ≤ 10⁹` |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Merge from the **end** — largest elements land in unused tail of `nums1`, avoiding overwrite of unmerged values.

### Why this pattern?

Merge from end with two pointers — O(1) extra space in-place.

### Why not another pattern?

New array merge is O(n) space; HashMap not applicable.

### What the interviewer expects

Why fill from rear (avoid overwrite); stable merge invariant.

---

## Brute Force

Copy `nums2`, sort tail — **O((m+n) log(m+n))**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums1=[1,2,3,0,0,0]`, `m=3`, `nums2=[2,5,6]`, `n=3` → fill from back → `[1,2,2,3,5,6]`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func merge(nums1 []int, m int, nums2 []int, n int) {
    i, j, k := m-1, n-1, m+n-1
    for j >= 0 {
        if i >= 0 && nums1[i] > nums2[j] {
            nums1[k] = nums1[i]
            i--
        } else {
            nums1[k] = nums2[j]
            j--
        }
        k--
    }
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(m + n)
- **Space:** O(1)

---

## Edge Cases

- `n = 0` — nothing to merge
- `m = 0` — copy all of `nums2`
- All `nums2` elements smaller — copy from back still works

---

## Interview Follow-ups

1. **Merge from front?** — Need extra buffer or shift — backward is simpler.
2. **Linked lists?** — Dummy head forward merge.
3. **k sorted arrays?** — Min-heap merge.

---

## See Also

- [Previous: 4Sum](/dsa-coding/01-arrays-hashmap-two-pointers/4sum/)
- [Next: Meeting Schedule](/dsa-coding/01-arrays-hashmap-two-pointers/meeting-schedule/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
