---
title: "N-Queens"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Backtracking pattern — N-Queens."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "N-Queens"
module: 4
moduleTitle: "Recursion & Backtracking"
sectionRef: "4.6"
weight: 406
languages: ["java", "golang"]
source: "https://leetcode.com/problems/n-queens/"
sourceLabel: "LeetCode 51"
pattern: "Backtracking"
interviewHandbook: true
---
# N-Queens

**Source:** [LeetCode 51](https://leetcode.com/problems/n-queens/) · **Pattern:** Backtracking · **Problem #32**

---

## Problem Statement

Place `n` queens on an `n × n` chessboard so no two queens attack each other. Return all distinct board configurations. Each configuration uses `'Q'` and `'.'`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ n ≤ 9` |

---

## Pattern Recognition

**Canonical pattern:** [Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/) — full framework in module primer.

Place one queen per row. Track occupied columns and diagonals (`row±col` constants). Backtrack row by row; skip invalid columns instantly.

### Why this pattern?

Place row by row; track cols and diagonals with sets — prune conflicts early.

### Why not another pattern?

Brute all board layouts exponential without pruning.

### What the interviewer expects

Explain diagonal indexing `row±col`; return all layouts vs count.

---

## Brute Force

Try all `n^n` placements — check attacks each time. Viable only for tiny `n`.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`n = 4`. Row 0 col 1, row 1 col 3, row 2 col 0, row 3 col 2 → `.Q.. / ...Q / Q... / ..Q.` plus symmetric solution — **2** boards total.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        boolean[] cols = new boolean[n];
        boolean[] diag1 = new boolean[2 * n];
        boolean[] diag2 = new boolean[2 * n];
        backtrack(0, n, board, cols, diag1, diag2, result);
        return result;
    }

    private void backtrack(int row, int n, char[][] board,
            boolean[] cols, boolean[] diag1, boolean[] diag2,
            List<List<String>> result) {
        if (row == n) {
            List<String> snapshot = new ArrayList<>(n);
            for (char[] r : board) {
                snapshot.add(new String(r));
            }
            result.add(snapshot);
            return;
        }
        for (int col = 0; col < n; col++) {
            int d1 = row - col + n;
            int d2 = row + col;
            if (cols[col] || diag1[d1] || diag2[d2]) {
                continue;
            }
            board[row][col] = 'Q';
            cols[col] = diag1[d1] = diag2[d2] = true;
            backtrack(row + 1, n, board, cols, diag1, diag2, result);
            board[row][col] = '.';
            cols[col] = diag1[d1] = diag2[d2] = false;
        }
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func solveNQueens(n int) [][]string {
    board := make([][]byte, n)
    for i := range board {
        board[i] = make([]byte, n)
        for j := range board[i] {
            board[i][j] = '.'
        }
    }
    cols := make([]bool, n)
    diag1 := make([]bool, 2*n)
    diag2 := make([]bool, 2*n)
    var result []string
    var dfs func(int)
    dfs = func(row int) {
        if row == n {
            for i := 0; i < n; i++ {
                result = append(result, string(board[i]))
            }
            return
        }
        for col := 0; col < n; col++ {
            d1, d2 := row-col+n, row+col
            if cols[col] || diag1[d1] || diag2[d2] {
                continue
            }
            board[row][col] = 'Q'
            cols[col], diag1[d1], diag2[d2] = true, true, true
            dfs(row + 1)
            board[row][col] = '.'
            cols[col], diag1[d1], diag2[d2] = false, false, false
        }
    }
    dfs(0)
    grouped := make([][]string, 0, len(result)/n)
    for i := 0; i < len(result); i += n {
        grouped = append(grouped, result[i:i+n])
    }
    return grouped
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n!) — heavily pruned
- **Space:** O(n²) board + O(n) tracking arrays

---

## Edge Cases

- `n = 1` → single `Q`
- `n = 2` or `n = 3` → no solution → `[]`
- Symmetry doubles configurations for even `n`

---

## Interview Follow-ups

1. **N-Queens II — count only?** — Same DFS; increment counter instead of recording boards.
2. **Bitmask optimization?** — Represent columns/diags as bits for faster checks.
3. **Placing per column instead of row?** — Equivalent; row-wise is the usual interview template.

---

## See Also

- [Previous: Word Search](/dsa-coding/04-recursion-backtracking/word-search/)
- [Next: Trees](/dsa-coding/05-trees/_index/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
