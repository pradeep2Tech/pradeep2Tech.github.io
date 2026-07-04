---
title: "Valid Parentheses"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Stack / Recursion Thinking pattern — Valid Parentheses."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Valid Parentheses"
module: 4
moduleTitle: "Recursion & Backtracking"
sectionRef: "4.1"
weight: 401
languages: ["java", "golang"]
source: "https://leetcode.com/problems/valid-parentheses/"
sourceLabel: "LeetCode 20"
pattern: "Stack / Recursion Thinking"
interviewHandbook: true
---
# Valid Parentheses

**Source:** [LeetCode 20](https://leetcode.com/problems/valid-parentheses/) · **Pattern:** Stack / Recursion Thinking · **Problem #27**

---

## Problem Statement

Given a string `s` containing `'()'`, `'[]'`, and `'{}'`, determine if the input string is valid: every opening bracket has a matching closing bracket in the correct order.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ s.length ≤ 10⁴` |
| Characters | `'('`, `')'`, `'['`, `']'`, `'{'`, `'}'` only |

---

## Pattern Recognition

**Canonical pattern:** [Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/) — full framework in module primer.

Last opened must close first → LIFO stack. Push openers; on closers, pop and verify type. Empty stack at end means valid.

### Why this pattern?

Last-open must match current close → stack LIFO.

### Why not another pattern?

Counter-only fails on `](` type; recursion works but stack is cleaner.

### What the interviewer expects

Map open→close; early exit on empty stack pop.

---

## Brute Force

Repeatedly remove adjacent pairs `()`, `[]`, `{}` until string empty or stuck — **O(n²)** worst case.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`s = "({[]})"`. Push `(`, `{`, `[`. Pop `[` with `]`, pop `{` with `}`, pop `(` with `)`. Stack empty → **true**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char open = stack.pop();
                if (open == '(' && c != ')'
                        || open == '[' && c != ']'
                        || open == '{' && c != '}') {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func isValid(s string) bool {
    stack := []rune{}
    pairs := map[rune]rune{')': '(', ']': '[', '}': '{'}
    for _, c := range s {
        switch c {
        case '(', '[', '{':
            stack = append(stack, c)
        default:
            if len(stack) == 0 || stack[len(stack)-1] != pairs[c] {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
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

- Closing bracket with empty stack
- Only openers — e.g. `"((("`
- Mismatched type — e.g. `"(]"`

---

## Interview Follow-ups

1. **Generate all valid strings?** — See Generate Parentheses — backtracking with counts.
2. **Longest valid substring?** — Stack storing indices — LC 32 variant.
3. **Recursion instead of stack?** — Same LIFO; explicit stack is clearer in interviews.

---

## See Also

- [Previous: Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/_index/)
- [Next: Subset Sum](/dsa-coding/04-recursion-backtracking/subset-sum-recursion/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
