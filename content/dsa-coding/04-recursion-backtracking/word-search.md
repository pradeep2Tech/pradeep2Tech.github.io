---
title: "Word Search"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Backtracking pattern — Word Search."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Word Search"
module: 4
moduleTitle: "Recursion & Backtracking"
sectionRef: "4.5"
weight: 405
languages: ["java", "golang"]
source: "https://leetcode.com/problems/word-search/"
sourceLabel: "LeetCode 79"
pattern: "Backtracking"
interviewHandbook: true
---
# Word Search

**Source:** [LeetCode 79](https://leetcode.com/problems/word-search/) · **Pattern:** Backtracking · **Problem #31**

---

## Problem Statement

Given an `m × n` board of characters and a string `word`, return `true` if `word` exists in the grid. Letters must be adjacent horizontally or vertically; the same cell may not be used twice in one path.

| Constraint | Value |
| :--- | :--- |
| Board | `1 ≤ m, n ≤ 6` |
| Word length | `1 ≤ word.length ≤ 15` |
| Letters | Uppercase and lowercase English letters |

---

## Pattern Recognition

**Canonical pattern:** [Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/) — full framework in module primer.

Grid DFS from each matching start cell. Mark visited, explore 4 neighbors, unmark on return. Classic backtracking with in-place state.

### Why this pattern?

Grid DFS with mark/unmark — backtracking on path.

### Why not another pattern?

BFS finds path but not all paths; DP doesn't apply without overlap structure.

### What the interviewer expects

In-place mark visited; restore cell after recurse.

---

## Brute Force

Same DFS without early exit optimizations — still exponential but acceptable at these bounds.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

Board `ABCE / SFCS / ADEE`, `word = "ABCCED"`. Start `(0,0) A → B → C → C → E → D` via DFS without reusing cells → **true**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length, n = board[0].length;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (dfs(board, word, 0, r, c)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int k, int r, int c) {
        if (k == word.length()) {
            return true;
        }
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length) {
            return false;
        }
        if (board[r][c] != word.charAt(k)) {
            return false;
        }
        char saved = board[r][c];
        board[r][c] = '#';
        boolean found = dfs(board, word, k + 1, r + 1, c)
                || dfs(board, word, k + 1, r - 1, c)
                || dfs(board, word, k + 1, r, c + 1)
                || dfs(board, word, k + 1, r, c - 1);
        board[r][c] = saved;
        return found;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func exist(board [][]byte, word string) bool {
    m, n := len(board), len(board[0])
    var dfs func(int, int, int) bool
    dfs = func(r, c, k int) bool {
        if k == len(word) {
            return true
        }
        if r < 0 || c < 0 || r >= m || c >= n || board[r][c] != word[k] {
            return false
        }
        saved := board[r][c]
        board[r][c] = '#'
        found := dfs(r+1, c, k+1) || dfs(r-1, c, k+1) ||
            dfs(r, c+1, k+1) || dfs(r, c-1, k+1)
        board[r][c] = saved
        return found
    }
    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            if dfs(r, c, 0) {
                return true
            }
        }
    }
    return false
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(m · n · 4^L) — L = word length
- **Space:** O(L) recursion stack

---

## Edge Cases

- Word longer than cell count
- Single cell board matching / not matching
- Repeated letters require separate visits

---

## Interview Follow-ups

1. **Word Search II (many words)?** — Trie + DFS from each cell — prune by prefix.
2. **8-direction adjacency?** — Add four diagonal moves in DFS.
3. **Count paths?** — Sum DFS returns instead of short-circuit on first hit.

---

## See Also

- [Previous: Generate Parentheses](/dsa-coding/04-recursion-backtracking/generate-parentheses/)
- [Next: N-Queens](/dsa-coding/04-recursion-backtracking/n-queens/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
