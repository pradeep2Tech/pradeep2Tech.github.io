---
title: "Binary Search Template"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "BS Template"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "BS Template"
module: 9
moduleTitle: "DSA & Coding"
sectionRef: "9.3"
weight: 903
ShowToc: true
interviewHandbook: true
---

# Binary Search Template

> **Canonical theory:** [Module 3](/dsa-coding/03-binary-search/). This page keeps **copy-paste snippets only**.

## Classic — find exact target

```java
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (nums[mid] == target) return mid;
    if (nums[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}
return -1;
```

## Lower bound — first index with `nums[i] >= target`

```java
int lo = 0, hi = n; // half-open [lo, hi)
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (nums[mid] < target) lo = mid + 1;
    else hi = mid;
}
return lo; // insertion point
```

## Binary search on answer space

Monotone predicate `feasible(x)` — find min `x` such that `feasible(x)` is true.

```java
int lo = minAnswer, hi = maxAnswer;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (feasible(mid)) hi = mid;
    else lo = mid + 1;
}
return lo;
```

## Go — lower bound

```go
lo, hi := 0, n
for lo < hi {
    mid := lo + (hi-lo)/2
    if nums[mid] < target {
        lo = mid + 1
    } else {
        hi = mid
    }
}
return lo
```

## When to use which

| Signal | Template |
| :--- | :--- |
| Sorted array lookup | Classic |
| First/last position, insert index | Lower / upper bound |
| Minimize maximum, maximize minimum | Search on answer |
| Rotated / peak array | Modified predicate on `mid` |

---

## See Also

- [Previous: Top 30 Must-Solve](/dsa-coding/09-interview-guide/top-30-must-solve/)
- [Next: Sliding Window Template](/dsa-coding/09-interview-guide/sliding-window-template/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
