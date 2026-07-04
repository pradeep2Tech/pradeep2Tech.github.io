---
title: "4Sum"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Two Pointers pattern — 4Sum."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "4Sum"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.9"
weight: 109
languages: ["java", "golang"]
source: "https://leetcode.com/problems/4sum/"
sourceLabel: "LeetCode 18"
pattern: "Two Pointers"
interviewHandbook: true
---
# 4Sum

**Source:** [LeetCode 18](https://leetcode.com/problems/4sum/) · **Pattern:** Two Pointers · **Problem #9**

---

## Problem Statement

Given `nums` and `target`, return all unique quadruplets that sum to `target`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 200` |
| Values | `-10⁹ ≤ nums[i], target ≤ 10⁹` |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Sort + double outer loop fixing `i` and `j`, then two-pointer scan for remaining pair. Duplicate skipping at every level.

### Why this pattern?

Sort + double fixed indices + two pointers — k-sum generalization.

### Why not another pattern?

HashMap for 4 elements is messy; reduce to 2-sum after fixing two indices.

### What the interviewer expects

Mention k-sum extension; skip duplicates on outer loops.

---

## Brute Force

Four nested loops — **O(n⁴)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums=[1,0,-1,0,-2,2]`, `target=0` → quadruplets `[-2,-1,1,2]` and `[-2,0,0,2]`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int l = j + 1, r = n - 1;
                while (l < r) {
                    long sum = (long) nums[i] + nums[j] + nums[l] + nums[r];
                    if (sum == target) {
                        res.add(List.of(nums[i], nums[j], nums[l], nums[r]));
                        while (l < r && nums[l] == nums[l + 1]) l++;
                        while (l < r && nums[r] == nums[r - 1]) r--;
                        l++;
                        r--;
                    } else if (sum < target) l++;
                    else r--;
                }
            }
        }
        return res;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func fourSum(nums []int, target int) [][]int {
    sort.Ints(nums)
    var res [][]int
    n := len(nums)
    for i := 0; i < n-3; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
        for j := i + 1; j < n-2; j++ {
            if j > i+1 && nums[j] == nums[j-1] {
                continue
            }
            l, r := j+1, n-1
            for l < r {
                sum := int64(nums[i]) + int64(nums[j]) + int64(nums[l]) + int64(nums[r])
                if sum == int64(target) {
                    res = append(res, []int{nums[i], nums[j], nums[l], nums[r]})
                    for l < r && nums[l] == nums[l+1] {
                        l++
                    }
                    for l < r && nums[r] == nums[r-1] {
                        r--
                    }
                    l++
                    r--
                } else if sum < int64(target) {
                    l++
                } else {
                    r--
                }
            }
        }
    }
    return res
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n³)
- **Space:** O(1) excluding output

---

## Edge Cases

- Use `long` for sum to avoid overflow
- Fewer than 4 elements → empty result
- Duplicate quadruplets must be skipped

---

## Interview Follow-ups

1. **General k-sum?** — Sort + recurse fixing one value each level.
2. **HashMap 2-sum inner?** — O(n²) space trade for average case.
3. **Target closest 4-sum?** — Track best delta like 3Sum closest.

---

## See Also

- [Previous: 3Sum Closest](/dsa-coding/01-arrays-hashmap-two-pointers/3sum-closest/)
- [Next: Merge Sorted Array](/dsa-coding/01-arrays-hashmap-two-pointers/merge-sorted-array/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
