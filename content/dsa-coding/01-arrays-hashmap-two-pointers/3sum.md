---
title: "3Sum"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Two Pointers pattern — 3Sum."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "3Sum"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.7"
weight: 107
languages: ["java", "golang"]
source: "https://leetcode.com/problems/3sum/"
sourceLabel: "LeetCode 15"
pattern: "Two Pointers"
ShowToc: true
interviewHandbook: true
---
# 3Sum

**Source:** [LeetCode 15](https://leetcode.com/problems/3sum/) · **Pattern:** Two Pointers · **Problem #7**

---

## Problem Statement

Given integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`.

| Constraint | Value |
| :--- | :--- |
| `n` | `3 ≤ nums.length ≤ 3000` |
| Values | `-10⁵ ≤ nums[i] ≤ 10⁵` |
| Output | No duplicate triplets |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Sort + fix smallest value `nums[i]`, two-pointer scan for `-(nums[i])` on the rest. Skip duplicates at each level.

### Why this pattern?

Sort + fix one index + two pointers — eliminates O(n³) to O(n²) with dedup.

### Why not another pattern?

HashMap for triplets causes duplicate handling pain; sliding window doesn't apply.

### What the interviewer expects

Skip duplicate `i`, `lo`, `hi`; state why sort enables two-pointer scan.

---

## Brute Force

Three nested loops with a set for dedup — **O(n³)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[-1,0,1,2,-1,-4]` → sort → fix `-1`, pointers find `(-1,0,1)` and `(-1,-1,2)`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    res.add(List.of(nums[i], nums[l], nums[r]));
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    l++;
                    r--;
                } else if (sum < 0) l++;
                else r--;
            }
        }
        return res;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    var res [][]int
    for i := 0; i < len(nums)-2; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
        l, r := i+1, len(nums)-1
        for l < r {
            sum := nums[i] + nums[l] + nums[r]
            if sum == 0 {
                res = append(res, []int{nums[i], nums[l], nums[r]})
                for l < r && nums[l] == nums[l+1] {
                    l++
                }
                for l < r && nums[r] == nums[r-1] {
                    r--
                }
                l++
                r--
            } else if sum < 0 {
                l++
            } else {
                r--
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

- **Time:** O(n²)
- **Space:** O(1) excluding output

---

## Edge Cases

- All zeros — single triplet `[0,0,0]` after dedup
- No solution — empty list
- Many duplicates — skip logic essential

---

## Interview Follow-ups

1. **3Sum closest?** — Track best absolute difference instead of collecting zeros.
2. **4Sum?** — Add another outer loop or hash pair complement.
3. **k-Sum?** — Sort + recurse or hash `(k-2)`-sum complements.

---

## See Also

- [Previous: Valid Palindrome](/dsa-coding/01-arrays-hashmap-two-pointers/valid-palindrome/)
- [Next: 3Sum Closest](/dsa-coding/01-arrays-hashmap-two-pointers/3sum-closest/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
