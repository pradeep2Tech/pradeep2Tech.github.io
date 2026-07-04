---
title: "Valid Palindrome"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Two Pointers pattern — Valid Palindrome."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Valid Palindrome"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.6"
weight: 106
languages: ["java", "golang"]
source: "https://leetcode.com/problems/valid-palindrome/"
sourceLabel: "LeetCode 125"
pattern: "Two Pointers"
interviewHandbook: true
---
# Valid Palindrome

**Source:** [LeetCode 125](https://leetcode.com/problems/valid-palindrome/) · **Pattern:** Two Pointers · **Problem #6**

---

## Problem Statement

Given a string `s`, return `true` if it is a palindrome after converting to lowercase and removing non-alphanumeric characters.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ s.length ≤ 2·10⁵` |
| Charset | Printable ASCII |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Symmetric scan from both ends — skip invalid chars, compare lowercase letters. Two pointers converge in O(n).

### Why this pattern?

Two pointers from ends — skip non-alphanumeric in O(n).

### Why not another pattern?

Stack/reverse string wastes O(n) space; HashMap irrelevant.

### What the interviewer expects

In-place scan; case folding; don't allocate reversed copy unless asked.

---

## Brute Force

Filter string, reverse copy, compare — **O(n)** time but extra **O(n)** space.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`"A man, a plan, a canal: Panama"` → compare `a/p`, `m/a`, … → all match → **true**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func isPalindrome(s string) bool {
    l, r := 0, len(s)-1
    for l < r {
        for l < r && !isAlnum(s[l]) {
            l++
        }
        for l < r && !isAlnum(s[r]) {
            r--
        }
        if toLower(s[l]) != toLower(s[r]) {
            return false
        }
        l++
        r--
    }
    return true
}

func isAlnum(b byte) bool {
    return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9')
}

func toLower(b byte) byte {
    if b >= 'A' && b <= 'Z' {
        return b + 32
    }
    return b
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## Edge Cases

- Empty after filtering — vacuously true
- Only punctuation
- Mixed case and digits

---

## Interview Follow-ups

1. **Allow at most one deletion?** — Two-pointer with skip-left or skip-right variant.
2. **Unicode letters?** — Use code points and `Character.isLetter` equivalents.
3. **Recursive?** — Same logic; watch stack depth on long strings.

---

## See Also

- [Previous: Count Nice Pairs in an Array](/dsa-coding/01-arrays-hashmap-two-pointers/count-nice-pairs-in-an-array/)
- [Next: 3Sum](/dsa-coding/01-arrays-hashmap-two-pointers/3sum/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
