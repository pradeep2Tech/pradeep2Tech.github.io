---
title: "Meeting Schedule"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Two Arrays + Sorting pattern — Meeting Schedule."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Meeting Schedule"
module: 1
moduleTitle: "Arrays, HashMap & Two Pointers"
sectionRef: "1.11"
weight: 111
languages: ["java", "golang"]
source: "https://leetcode.com/problems/meeting-rooms/"
sourceLabel: "LeetCode 252"
pattern: "Two Arrays + Sorting"
interviewHandbook: true
---
# Meeting Schedule

**Source:** [LeetCode 252](https://leetcode.com/problems/meeting-rooms/) · **Pattern:** Two Arrays + Sorting · **Problem #11**

---

## Problem Statement

Given an array of meeting time intervals `[start, end]`, determine if a person can attend all meetings (no overlaps).

| Constraint | Value |
| :--- | :--- |
| `n` | `0 ≤ intervals.length ≤ 10⁴` |
| Times | `0 ≤ start < end ≤ 10⁶` |

---

## Pattern Recognition

**Canonical pattern:** [Arrays, HashMap & Two Pointers](/dsa-coding/01-arrays-hashmap-two-pointers/) — full framework in module primer.

Overlap detection on intervals → sort by start time, check if any `start < previous end`.

### Why this pattern?

Sort intervals by start; overlap check is O(n) after sort.

### Why not another pattern?

HashMap doesn't model intervals; brute compare all pairs O(n²).

### What the interviewer expects

Sort justification; edge case single meeting, adjacent non-overlap.

---

## Brute Force

Compare every pair of intervals — **O(n²)**.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`[[0,30],[5,10],[15,20]]` → after sort, `5 < 30` → **false**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }
        return true;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func canAttendMeetings(intervals [][]int) bool {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] < intervals[i-1][1] {
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

- **Time:** O(n log n)
- **Space:** O(1) excluding sort

---

## Edge Cases

- Empty schedule → true
- Single meeting → true
- Touching endpoints `[1,2],[2,3]` — non-overlapping if end exclusive

---

## Interview Follow-ups

1. **Minimum rooms?** — Sort starts/ends; sweep line count.
2. **Insert new meeting?** — Binary search slot or reuse room heap.
3. **Merge intervals?** — Sort + accumulate merged range.

---

## See Also

- [Previous: Merge Sorted Array](/dsa-coding/01-arrays-hashmap-two-pointers/merge-sorted-array/)
- [Next: Longest Palindromic Substring](/dsa-coding/01-arrays-hashmap-two-pointers/longest-palindromic-substring/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
