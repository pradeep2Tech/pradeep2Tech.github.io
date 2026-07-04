---
title: "Two Sum"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "HashMap pattern — Two Sum."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Two Sum"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.1"
weight: 101
languages: ["java", "golang"]
source: "https://leetcode.com/problems/two-sum/"
sourceLabel: "LeetCode 1"
pattern: "HashMap"
interviewHandbook: true
---
# Two Sum

**Source:** [LeetCode 1](https://leetcode.com/problems/two-sum/) · **Pattern:** HashMap · **Problem #1**

---

## Problem Statement

Given an integer array `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. Exactly one solution exists and you may not use the same element twice.

| Constraint | Value |
| :--- | :--- |
| `n` | `2 ≤ nums.length ≤ 10⁴` |
| Values | `-10⁹ ≤ nums[i] ≤ 10⁹` |
| Answer | Exactly one valid pair; return indices in any order |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Unsorted array + need complement lookup in O(1) → HashMap from value to index. Single pass: check if `target - nums[i]` was seen before storing `nums[i]`.

### Why this pattern?

Unsorted array + pair by complement → single-pass HashMap with O(1) lookup.

### Why not another pattern?

Two pointers need sorted order (extra O(n log n)); sliding window needs contiguous subarray.

### What the interviewer expects

O(n) time/space tradeoff stated upfront; query complement before insert; sorted follow-up → two pointers.

---

## Brute Force

Check every pair `(i, j)` with nested loops — **O(n²)** time, **O(1)** space. Fine for tiny inputs but fails interview scale.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums = [2,7,11,15]`, `target = 9`. At index 0 store `{2:0}`. At index 1, `9-7=2` is in the map → return `[0,1]`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int need = target - nums[i];
            if (seen.containsKey(need)) {
                return new int[] { seen.get(need), i };
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for i, x := range nums {
        if j, ok := seen[target-x]; ok {
            return []int{j, i}
        }
        seen[x] = i
    }
    return nil
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## Edge Cases

- Negative numbers and zero as valid values
- Duplicate values — map stores latest index; complement lookup still correct
- Minimum length 2 — always exactly one answer

---

## Interview Follow-ups

1. **Return all pairs?** — Use multimap or sort + two pointers; dedupe triplets if needed.
2. **Sorted array?** — Two pointers from both ends in O(n) time, O(1) space.
3. **3Sum?** — Sort + fix one index + two-pointer scan for the remaining pair.

---

## See Also

- [Previous: Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/_index/)
- [Next: Valid Anagram](/dsa-coding/01-arrays-hashmap-two-pointers/valid-anagram/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
