---
title: "Letter Combinations of a Phone Number"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Backtracking pattern — Letter Combinations of a Phone Number."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Letter Combinations of a Phone Number"
module: 4
moduleTitle: "Recursion & Backtracking"
sectionRef: "4.3"
weight: 403
languages: ["java", "golang"]
source: "https://leetcode.com/problems/letter-combinations-of-a-phone-number/"
sourceLabel: "LeetCode 17"
pattern: "Backtracking"
interviewHandbook: true
---
# Letter Combinations of a Phone Number

**Source:** [LeetCode 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) · **Pattern:** Backtracking · **Problem #29**

---

## Problem Statement

Given a string `digits` containing digits `2–9`, return all possible letter combinations that the number could represent (phone keypad mapping). Return empty list for empty input.

| Constraint | Value |
| :--- | :--- |
| `n` | `0 ≤ digits.length ≤ 4` |
| Digits | `2–9` only (no 0/1) |

---

## Pattern Recognition

**Canonical pattern:** [Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/) — full framework in module primer.

Fixed-length combinations from independent choice sets → backtrack one digit at a time, append each mapped letter, recurse, then backtrack length.

### Why this pattern?

Cartesian product via backtracking — build string digit by digit.

### Why not another pattern?

Iterative queue works but backtracking is natural; HashMap only for digit map.

### What the interviewer expects

Base case empty digits; undo by popping char.

---

## Brute Force

Nested loops per digit — works for max length 4 but does not generalize; equivalent to hard-coded backtracking.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`digits = "23"`. Digit 2 → `a,b,c`; from `a` digit 3 → `ad,ae,af`; … Total **9** strings: `ad,ae,af,bd,be,bf,cd,ce,cf`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final String[] MAP = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) {
            return result;
        }
        backtrack(digits, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(String digits, int i, StringBuilder path, List<String> result) {
        if (i == digits.length()) {
            result.add(path.toString());
            return;
        }
        for (char c : MAP[digits.charAt(i) - '0'].toCharArray()) {
            path.append(c);
            backtrack(digits, i + 1, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
var keypad = []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

func letterCombinations(digits string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    var result []string
    var path []byte
    var dfs func(int)
    dfs = func(i int) {
        if i == len(digits) {
            result = append(result, string(path))
            return
        }
        for _, c := range keypad[digits[i]-'0'] {
            path = append(path, byte(c))
            dfs(i + 1)
            path = path[:len(path)-1]
        }
    }
    dfs(0)
    return result
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(4^n · n) — n = digits length
- **Space:** O(n) recursion excluding output

---

## Edge Cases

- Empty `digits` → `[]`
- Single digit → 3 or 4 letters
- Digit 7 or 9 has four letters

---

## Interview Follow-ups

1. **Iterative BFS/queue?** — Enqueue partial strings per digit — same complexity.
2. **Combination Sum style?** — Digits fixed length; no reuse or sorting needed.
3. **Return count only?** — `product of keypad sizes` without building strings.

---

## See Also

- [Previous: Subset Sum](/dsa-coding/04-recursion-backtracking/subset-sum-recursion/)
- [Next: Generate Parentheses](/dsa-coding/04-recursion-backtracking/generate-parentheses/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
