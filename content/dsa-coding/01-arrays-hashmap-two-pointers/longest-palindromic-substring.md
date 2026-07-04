---
title: "Longest Palindromic Substring"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Expand Around Center pattern — Longest Palindromic Substring."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Longest Palindromic Substring"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.12"
weight: 112
languages: ["java", "golang"]
source: "https://leetcode.com/problems/longest-palindromic-substring/"
sourceLabel: "LeetCode 5"
pattern: "Expand Around Center"
interviewHandbook: true
---
# Longest Palindromic Substring

**Source:** [LeetCode 5](https://leetcode.com/problems/longest-palindromic-substring/) · **Pattern:** Expand Around Center · **Problem #12**

---

## Problem Statement

Given string `s`, return the longest palindromic substring in `s`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ s.length ≤ 1000` |
| Charset | Digits and English letters |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Every palindrome expands from a center (one or two chars). Try `2n-1` centers, expand while matching.

### Why this pattern?

Expand around center — O(n²) centers, O(1) space.

### Why not another pattern?

DP O(n²) space acceptable but expand is simpler; Manacher is overkill unless asked.

### What the interviewer expects

Even vs odd centers; early continue on bounds.

---

## Brute Force

Check every substring — **O(n³)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`"babad"` → expand at index 1 (`a`) gives `"bab"` length 3.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public String longestPalindrome(String s) {
        int start = 0, maxLen = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > maxLen) {
                maxLen = len;
                start = i - (len - 1) / 2;
            }
        }
        return s.substring(start, start + maxLen);
    }

    private int expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return r - l - 1;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func longestPalindrome(s string) string {
    start, maxLen := 0, 0
    expand := func(l, r int) int {
        for l >= 0 && r < len(s) && s[l] == s[r] {
            l--
            r++
        }
        return r - l - 1
    }
    for i := 0; i < len(s); i++ {
        len1 := expand(i, i)
        len2 := expand(i, i+1)
        if l := max(len1, len2); l > maxLen {
            maxLen = l
            start = i - (l-1)/2
        }
    }
    return s[start : start+maxLen]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n²)
- **Space:** O(1)

---

## Edge Cases

- Entire string palindrome
- All distinct characters — any single char
- Even-length palindrome center between two chars

---

## Interview Follow-ups

1. **Count palindromic substrings?** — Increment count on each successful expand.
2. **Longest in stream?** — Manacher's algorithm O(n).
3. **DP solution?** — O(n²) time and space table `dp[i][j]`.

---

## See Also

- [Previous: Meeting Schedule](/dsa-coding/01-arrays-hashmap-two-pointers/meeting-schedule/)
- [Next: Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/_index/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
