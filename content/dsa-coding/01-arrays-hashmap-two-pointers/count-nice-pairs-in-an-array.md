---
title: "Count Nice Pairs in an Array"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "HashMap pattern — Count Nice Pairs in an Array."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Count Nice Pairs in an Array"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.5"
weight: 105
languages: ["java", "golang"]
source: "https://leetcode.com/problems/count-nice-pairs-in-an-array/"
sourceLabel: "LeetCode 1814"
pattern: "HashMap"
ShowToc: true
interviewHandbook: true
---
# Count Nice Pairs in an Array

**Source:** [LeetCode 1814](https://leetcode.com/problems/count-nice-pairs-in-an-array/) · **Pattern:** HashMap · **Problem #5**

---

## Problem Statement

A **nice pair** `(i, j)` satisfies `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])` with `i < j`. Return the count modulo `10⁹ + 7`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ nums.length ≤ 10⁵` |
| Values | `0 ≤ nums[i] ≤ 10⁹` |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Rearrange: `nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])`. Count equal transformed values with a frequency map — same trick as anagram keys.

### Why this pattern?

Transform `rev(j)-j` as key; count prior equal keys → HashMap.

### Why not another pattern?

O(n²) pair scan fails scale; sorting destroys index pairing need.

### What the interviewer expects

Explain rev() definition; combine math transform + frequency pattern.

---

## Brute Force

Check all pairs and compare the nice condition — **O(n²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`nums=[42,11,1,42]` → transforms `[24, -8, 0, 24]` → two 24s form one pair → **1**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
  private static final int MOD = 1_000_000_007;

  public int countNicePairs(int[] nums) {
    Map<Integer, Integer> freq = new HashMap<>();
    long count = 0;
    for (int x : nums) {
      int key = x - rev(x);
      count += freq.getOrDefault(key, 0);
      freq.merge(key, 1, Integer::sum);
    }
    return (int) (count % MOD);
  }

  private int rev(int x) {
    int r = 0;
    while (x > 0) {
      r = r * 10 + x % 10;
      x /= 10;
    }
    return r;
  }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func countNicePairs(nums []int) int {
    const mod = 1_000_000_007
    freq := make(map[int]int)
    count := 0
    for _, x := range nums {
        key := x - rev(x)
        count = (count + freq[key]) % mod
        freq[key]++
    }
    return count
}

func rev(x int) int {
    r := 0
    for x > 0 {
        r = r*10 + x%10
        x /= 10
    }
    return r
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n · log₁₀ max(nums))
- **Space:** O(n)

---

## Edge Cases

- Single element → 0 pairs
- All transforms unique → 0
- Apply modulo on accumulated count

---

## Interview Follow-ups

1. **Why subtract rev?** — Algebra cancels cross terms so only per-index signature matters.
2. **Leading zeros in rev?** — Integer reversal ignores leading zeros by definition.
3. **Overflow?** — Use `long` for running count before modulo.

---

## See Also

- [Previous: Count Pairs With Absolute Difference K](/dsa-coding/01-arrays-hashmap-two-pointers/count-pairs-absolute-difference-k/)
- [Next: Valid Palindrome](/dsa-coding/01-arrays-hashmap-two-pointers/valid-palindrome/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
