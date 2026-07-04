---
title: "Count Pairs With Absolute Difference K"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "HashMap pattern — Count Pairs With Absolute Difference K."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Count Pairs With Absolute Difference K"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.4"
weight: 104
languages: ["java", "golang"]
source: "https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/"
sourceLabel: "LeetCode 2006"
pattern: "HashMap"
ShowToc: true
interviewHandbook: true
---
# Count Pairs With Absolute Difference K

**Source:** [LeetCode 2006](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) · **Pattern:** HashMap · **Problem #4**

---

## Problem Statement

Given integer array `nums` and integer `k`, count pairs `(i, j)` with `i < j` and `|nums[i] - nums[j]| == k`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 200` |
| `k` | `0 ≤ k ≤ 100` |
| Values | `1 ≤ nums[i] ≤ 100` |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

For each value `x`, partners are `x + k` and `x - k` already seen. Frequency map counts prior occurrences — classic complement counting.

### Why this pattern?

For each `x`, count `x+k` and `x-k` seen → frequency map.

### Why not another pattern?

Brute pair enumeration O(n²); sorting doesn't help count pairs directly.

### What the interviewer expects

Watch double-counting; clarify ordered vs unordered pairs per problem statement.

---

## Brute Force

All pairs `(i,j)` — **O(n²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums=[1,2,2,1]`, `k=1` → pairs (0,1),(0,2),(1,3),(2,3) → **4**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int countKDifference(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        int count = 0;
        for (int x : nums) {
            if (k == 0) {
                count += freq.getOrDefault(x, 0);
            } else {
                count += freq.getOrDefault(x + k, 0);
                count += freq.getOrDefault(x - k, 0);
            }
            freq.merge(x, 1, Integer::sum);
        }
        return count;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func countKDifference(nums []int, k int) int {
    freq := make(map[int]int)
    count := 0
    for _, x := range nums {
        if k == 0 {
            count += freq[x]
        } else {
            count += freq[x+k] + freq[x-k]
        }
        freq[x]++
    }
    return count
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

- `k = 0` — count pairs of equal values only
- No matching pairs → return 0
- All elements equal with `k > 0` → 0

---

## Interview Follow-ups

1. **Count pairs with difference ≤ k?** — Sort + two pointers or merge counts.
2. **Distinct pairs only?** — Same formula; ensure `i < j` by processing left to right.
3. **Large value range?** — HashMap still works; array indexing if bounded.

---

## See Also

- [Previous: Group Anagrams](/dsa-coding/01-arrays-hashmap-two-pointers/group-anagrams/)
- [Next: Count Nice Pairs in an Array](/dsa-coding/01-arrays-hashmap-two-pointers/count-nice-pairs-in-an-array/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
