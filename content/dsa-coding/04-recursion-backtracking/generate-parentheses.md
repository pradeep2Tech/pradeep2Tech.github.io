---
title: "Generate Parentheses"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Backtracking pattern — Generate Parentheses."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Generate Parentheses"
module: 4
moduleTitle: "Recursion & Backtracking"
sectionRef: "4.4"
weight: 404
languages: ["java", "golang"]
source: "https://leetcode.com/problems/generate-parentheses/"
sourceLabel: "LeetCode 22"
pattern: "Backtracking"
interviewHandbook: true
---
# Generate Parentheses

**Source:** [LeetCode 22](https://leetcode.com/problems/generate-parentheses/) · **Pattern:** Backtracking · **Problem #30**

---

## Problem Statement

Given `n` pairs of parentheses, generate all combinations of well-formed parentheses strings.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ n ≤ 8` |

---

## Pattern Recognition

**Canonical pattern:** [Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/) — full framework in module primer.

Track open and close counts. Add `'('` if `open < n`; add `')'` only if `close < open`. Prune invalid branches early.

### Why this pattern?

Constraint tracking: open < n, close < open — prune invalid branches.

### Why not another pattern?

Brute all 2^(2n) strings then filter wasteful.

### What the interviewer expects

Narrate pruning; O(4^n/sqrt(n)) Catalan output size awareness.

---

## Brute Force

Generate all `2^(2n)` binary strings of parentheses, filter valid — exponential with heavy waste.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`n = 3`. Start `(`. Valid extensions maintain `close ≤ open`. Yields **5** strings: `((()))`, `(()())`, `(())()`, `()(())`, `()()()`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(n, 0, 0, new StringBuilder(), result);
        return result;
    }

    private void backtrack(int n, int open, int close, StringBuilder path, List<String> result) {
        if (path.length() == 2 * n) {
            result.add(path.toString());
            return;
        }
        if (open < n) {
            path.append('(');
            backtrack(n, open + 1, close, path, result);
            path.deleteCharAt(path.length() - 1);
        }
        if (close < open) {
            path.append(')');
            backtrack(n, open, close + 1, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func generateParenthesis(n int) []string {
    var result []string
    var path []byte
    var dfs func(open, close int)
    dfs = func(open, close int) {
        if len(path) == 2*n {
            result = append(result, string(path))
            return
        }
        if open < n {
            path = append(path, '(')
            dfs(open+1, close)
            path = path[:len(path)-1]
        }
        if close < open {
            path = append(path, ')')
            dfs(open, close+1)
            path = path[:len(path)-1]
        }
    }
    dfs(0, 0)
    return result
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(4^n / √n) — Catalan output
- **Space:** O(n) recursion depth

---

## Edge Cases

- `n = 1` → `["()"]`
- `n = 2` → `["(())","()()"]`
- Never allow `close > open`

---

## Interview Follow-ups

1. **Count only?** — Nth Catalan number — DP or direct formula.
2. **Print one valid string?** — Fill n open then n close — no backtracking needed.
3. **With other brackets?** — Stack validity check per generated string or tighter rules.

---

## See Also

- [Previous: Letter Combinations of a Phone Number](/dsa-coding/04-recursion-backtracking/letter-combinations-of-phone-number/)
- [Next: Word Search](/dsa-coding/04-recursion-backtracking/word-search/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
