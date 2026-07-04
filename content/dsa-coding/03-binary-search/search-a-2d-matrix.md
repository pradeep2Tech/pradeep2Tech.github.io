---
title: "Search a 2D Matrix"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Matrix Binary Search pattern — Search a 2D Matrix."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Search a 2D Matrix"
module: 3
moduleTitle: "Binary Search"
sectionRef: "3.3"
weight: 303
languages: ["java", "golang"]
source: "https://leetcode.com/problems/search-a-2d-matrix/"
sourceLabel: "LeetCode 74"
pattern: "Matrix Binary Search"
ShowToc: true
interviewHandbook: true
---
# Search a 2D Matrix

**Source:** [LeetCode 74](https://leetcode.com/problems/search-a-2d-matrix/) · **Pattern:** Matrix Binary Search · **Problem #23**

---

## Problem Statement

Given an `m × n` matrix where each row is sorted left-to-right and the first element of each row is greater than the last element of the previous row, return `true` if `target` exists in the matrix.

| Constraint | Value |
| :--- | :--- |
| Dimensions | `m, n ≥ 1` |
| Values | `-10⁴ ≤ matrix[i][j], target ≤ 10⁴` |
| Structure | Full matrix is one sorted sequence in row-major order |

---

## Pattern Recognition

**Canonical pattern:** [Binary Search](/dsa-coding/03-binary-search/) — full framework in module primer.

Row-major order equals a sorted 1D array of length `m·n`. Map flat index `k` to `(k/n, k%n)` and run classic BS.

### Why this pattern?

Treat as 1D sorted array or BS on row then column.

### Why not another pattern?

DFS/BFS wrong paradigm; HashMap ignores global order.

### What the interviewer expects

Flatten index `mid → (mid/cols, mid%cols)` trick.

---

## Brute Force

Scan every cell — **O(m·n)** time, **O(1)** space.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]`, `target = 3`. Flat search on 12 elements: `mid=5 → 11 > 3` → left; eventually `mid=1 → 3` → **true**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int low = 0, high = m * n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) {
                return true;
            }
            if (val < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func searchMatrix(matrix [][]int, target int) bool {
    m, n := len(matrix), len(matrix[0])
    low, high := 0, m*n-1
    for low <= high {
        mid := low + (high-low)/2
        val := matrix[mid/n][mid%n]
        switch {
        case val == target:
            return true
        case val < target:
            low = mid + 1
        default:
            high = mid - 1
        }
    }
    return false
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(log(m·n))
- **Space:** O(1)

---

## Edge Cases

- Target smaller than top-left or larger than bottom-right
- Single row or single column matrix
- Target equals corner cells

---

## Interview Follow-ups

1. **Each row sorted, columns not globally?** — Start from top-right, staircase search O(m+n).
2. **Search row then column?** — Two BS passes — only if row boundaries hold per row.
3. **Count occurrences?** — Find leftmost then rightmost with BS variants.

---

## See Also

- [Previous: Search in Rotated Sorted Array](/dsa-coding/03-binary-search/search-in-rotated-sorted-array/)
- [Next: Missing Number in Sorted Array](/dsa-coding/03-binary-search/missing-number-in-sorted-array/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
