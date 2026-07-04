---
title: "Longest Substring Without Repeating Characters"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Variable Window pattern — Longest Substring Without Repeating Characters."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Longest Substring Without Repeating Char"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.2"
weight: 202
languages: ["java", "golang"]
source: "https://leetcode.com/problems/longest-substring-without-repeating-characters/"
sourceLabel: "LeetCode 3"
pattern: "Variable Window"
ShowToc: true
interviewHandbook: true
---
# Longest Substring Without Repeating Characters

**Source:** [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · **Pattern:** Variable Window · **Problem #14**

---

## Problem Statement

Given string `s`, find the length of the longest substring without repeating characters.

| Constraint | Value |
| :--- | :--- |
| `n` | `0 ≤ s.length ≤ 5·10⁴` |
| Charset | ASCII including spaces and symbols |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Variable window — expand right, shrink left while duplicate exists. Map stores last index of each character.

### Why this pattern?

Variable window — expand until duplicate, shrink from left.

### Why not another pattern?

HashMap of last index beats set for O(1) jumps; brute substring generation O(n³).

### What the interviewer expects

Longest invariant: max **after** window valid; state charset map choice.

---

## Brute Force

Check every substring for uniqueness — **O(n³)** or **O(n²)** with a set.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`"abcabcbb"` → window grows to `"abc"` (len 3), shrinks on repeat → max **3**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> last = new HashMap<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (last.containsKey(c)) {
                left = Math.max(left, last.get(c) + 1);
            }
            last.put(c, right);
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func lengthOfLongestSubstring(s string) int {
    last := make(map[byte]int)
    left, best := 0, 0
    for right := 0; right < len(s); right++ {
        c := s[right]
        if idx, ok := last[c]; ok && idx >= left {
            left = idx + 1
        }
        last[c] = right
        if right-left+1 > best {
            best = right - left + 1
        }
    }
    return best
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(min(n, |Σ|))

---

## Edge Cases

- Empty string → 0
- All same character → 1
- No repeats → full length

---

## Interview Follow-ups

1. **At most k distinct?** — Count map + shrink when distinct > k.
2. **At most k replacements?** — Track mismatch count in window.
3. **Return substring itself?** — Track `(start, bestLen)`.

---

## See Also

- [Previous: Max Sum Subarray of Size K](/dsa-coding/02-sliding-window-prefix-sum/max-sum-subarray-size-k/)
- [Next: Longest Substring with At Most K Distinct Characters](/dsa-coding/02-sliding-window-prefix-sum/longest-substring-k-distinct-characters/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
