---
title: "Longest Substring with At Most K Distinct Characters"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Variable Window pattern — Longest Substring with At Most K Distinct Characters."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Longest Substring with At Most K Distinc"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.3"
weight: 203
languages: ["java", "golang"]
source: "https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/"
sourceLabel: "LeetCode 340"
pattern: "Variable Window"
interviewHandbook: true
---
# Longest Substring with At Most K Distinct Characters

**Source:** [LeetCode 340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) · **Pattern:** Variable Window · **Problem #15**

---

## Problem Statement

Given string `s` and integer `k`, return the length of the longest substring containing at most `k` distinct characters.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ s.length ≤ 5·10⁴` |
| `k` | `1 ≤ k ≤ 50` |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Variable window with frequency map — expand right, while `distinct > k` shrink left decrementing counts.

### Why this pattern?

Variable window + frequency map; shrink when distinct > k.

### Why not another pattern?

Fixed window wrong size; prefix sum doesn't count distinct chars.

### What the interviewer expects

Remove map entry at freq 0; at-most-k vs exactly-k distinction.

---

## Brute Force

Enumerate all substrings, count distinct — **O(n²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`s="eceba"`, `k=2` → longest `"ece"` or `"eba"` → length **3**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> freq = new HashMap<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            freq.merge(c, 1, Integer::sum);
            while (freq.size() > k) {
                char drop = s.charAt(left++);
                int n = freq.merge(drop, -1, Integer::sum);
                if (n == 0) freq.remove(drop);
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func lengthOfLongestSubstringKDistinct(s string, k int) int {
    freq := make(map[byte]int)
    left, best := 0, 0
    for right := 0; right < len(s); right++ {
        freq[s[right]]++
        for len(freq) > k {
            drop := s[left]
            freq[drop]--
            if freq[drop] == 0 {
                delete(freq, drop)
            }
            left++
        }
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
- **Space:** O(k)

---

## Edge Cases

- `k` equals alphabet size — whole string
- `k = 1` — longest run of one char
- All distinct with small `k` — window size `k`

---

## Interview Follow-ups

1. **Exactly k distinct?** — At-most-k minus at-most-(k-1).
2. **Case-sensitive?** — Same algorithm; normalize if needed.
3. **Stream?** — Same window; output best on each char.

---

## See Also

- [Previous: Longest Substring Without Repeating Characters](/dsa-coding/02-sliding-window-prefix-sum/longest-substring-without-repeating-characters/)
- [Next: Max Consecutive Ones III](/dsa-coding/02-sliding-window-prefix-sum/max-consecutive-ones-iii/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
