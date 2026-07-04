---
title: "Group Anagrams"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "HashMap pattern — Group Anagrams."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Group Anagrams"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.3"
weight: 103
languages: ["java", "golang"]
source: "https://leetcode.com/problems/group-anagrams/"
sourceLabel: "LeetCode 49"
pattern: "HashMap"
interviewHandbook: true
---
# Group Anagrams

**Source:** [LeetCode 49](https://leetcode.com/problems/group-anagrams/) · **Pattern:** HashMap · **Problem #3**

---

## Problem Statement

Given an array of strings, group the anagrams together. Return the groups in any order.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ strs.length ≤ 10⁴` |
| Word length | `0 ≤ strs[i].length ≤ 100` |
| Charset | Lowercase English letters |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Anagrams share the same canonical key — sorted word or 26-char frequency signature. HashMap from key → list of words.

### Why this pattern?

Grouping requires canonical key — sorted string or frequency tuple.

### Why not another pattern?

Pairwise compare is O(n²·k); trie overkill for interview scope.

### What the interviewer expects

Justify key normalization; discuss immutability of tuple keys in Java.

---

## Brute Force

For each string, compare against a representative in each group — **O(n² · L)** where L is word length.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`["eat","tea","tan","ate","nat","bat"]` → keys `aet` and `ant` and `abt` → groups `[[eat,tea,ate],[tan,nat],[bat]]`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(groups.values());
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)
    for _, s := range strs {
        key := []byte(s)
        sort.Slice(key, func(i, j int) bool { return key[i] < key[j] })
        k := string(key)
        groups[k] = append(groups[k], s)
    }
    out := make([][]string, 0, len(groups))
    for _, g := range groups {
        out = append(out, g)
    }
    return out
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n · L log L) — L = max word length
- **Space:** O(n · L)

---

## Edge Cases

- Single-character strings each form their own group
- Empty string groups with other empties
- All words identical → one group

---

## Interview Follow-ups

1. **Avoid sorting keys?** — Use `int[26]` encoded as string key for O(L) per word.
2. **Stream of words?** — Same map; emit groups on flush.
3. **Return indices?** — Store original index alongside each word.

---

## See Also

- [Previous: Valid Anagram](/dsa-coding/01-arrays-hashmap-two-pointers/valid-anagram/)
- [Next: Count Pairs With Absolute Difference K](/dsa-coding/01-arrays-hashmap-two-pointers/count-pairs-absolute-difference-k/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
