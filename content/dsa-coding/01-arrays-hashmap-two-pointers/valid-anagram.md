---
title: "Valid Anagram"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "HashMap pattern — Valid Anagram."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Valid Anagram"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.2"
weight: 102
languages: ["java", "golang"]
source: "https://leetcode.com/problems/valid-anagram/"
sourceLabel: "LeetCode 242"
pattern: "HashMap"
interviewHandbook: true
---
# Valid Anagram

**Source:** [LeetCode 242](https://leetcode.com/problems/valid-anagram/) · **Pattern:** HashMap · **Problem #2**

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s` (same characters, same counts, different order allowed).

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ s.length, t.length ≤ 5·10⁴` |
| Charset | Lowercase English letters |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Anagram ⇔ identical character frequencies. Use a 26-slot frequency array or HashMap; increment for `s`, decrement for `t`.

### Why this pattern?

Character frequency is the invariant → count array or HashMap.

### Why not another pattern?

Sorting works but O(n log n); two pointers only after sort and doesn't generalize to unicode counts easily.

### What the interviewer expects

O(26) vs O(n) space choice; mention early exit on length mismatch.

---

## Brute Force

Sort both strings and compare — **O(n log n)** time, **O(n)** space for copies.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`s = "anagram"`, `t = "nagaram"` — all letter counts match after increment/decrement.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
            freq[t.charAt(i) - 'a']--;
        }
        for (int c : freq) if (c != 0) return false;
        return true;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func isAnagram(s, t string) bool {
    if len(s) != len(t) {
        return false
    }
    var freq [26]int
    for i := 0; i < len(s); i++ {
        freq[s[i]-'a']++
        freq[t[i]-'a']--
    }
    for _, c := range freq {
        if c != 0 {
            return false
        }
    }
    return true
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(1) — 26 counters

---

## Edge Cases

- Different lengths → immediate false
- Unicode beyond `a-z` would need a map instead of array
- Empty strings — equal, return true

---

## Interview Follow-ups

1. **Unicode?** — Use `HashMap<Character,Integer>` instead of fixed array.
2. **Follow-up: group anagrams?** — Key = sorted string or 26-char signature.
3. **Sort vs count?** — Count is O(n); sort is O(n log n) but simpler to code.

---

## See Also

- [Previous: Two Sum](/dsa-coding/01-arrays-hashmap-two-pointers/two-sum/)
- [Next: Group Anagrams](/dsa-coding/01-arrays-hashmap-two-pointers/group-anagrams/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
