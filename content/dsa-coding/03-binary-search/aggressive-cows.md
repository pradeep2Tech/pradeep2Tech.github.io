---
title: "Aggressive Cows"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Binary Search on Answer pattern — Aggressive Cows."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Aggressive Cows"
module: 3
moduleTitle: "Binary Search"
sectionRef: "3.6"
weight: 306
languages: ["java", "golang"]
source: "https://www.geeksforgeeks.org/problems/aggressive-cows/1"
sourceLabel: "GFG"
pattern: "Binary Search on Answer"
interviewHandbook: true
---
# Aggressive Cows

**Source:** [GFG](https://www.geeksforgeeks.org/problems/aggressive-cows/1) · **Pattern:** Binary Search on Answer · **Problem #26**

---

## Problem Statement

Given `N` stalls at positions `stalls[i]` and `C` cows, assign cows to stalls so that the **minimum distance between any two cows is as large as possible**. Return that maximum minimum distance.

| Constraint | Value |
| :--- | :--- |
| `N` | `2 ≤ N ≤ 10⁵` |
| `C` | `2 ≤ C ≤ N` |
| Positions | `0 ≤ stalls[i] ≤ 10⁹`, unsorted |

---

## Pattern Recognition

**Canonical pattern:** [Binary Search](/dsa-coding/03-binary-search/) — full framework in module primer.

Maximize the minimum gap → if distance `d` is feasible, any `d' < d` is also feasible. Sort stalls, BS on distance, greedily place cows left-to-right.

### Why this pattern?

Maximize minimum distance → BS on distance with feasibility placement check.

### Why not another pattern?

Sort stalls first; brute distance enumeration too slow.

### What the interviewer expects

Feasibility greedy: place cows at min distance; classic interview capstone.

---

## Brute Force

Try every possible minimum distance from `1` to `max gap` — **O(N²)** or worse with naive placement.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`stalls = [1,2,4,8,9]`, `C = 3`. `d=3`: cows at 1, 4, 8 → 3 cows ✓. `d=4`: only 1 and 8 (next would need 12) → ✗. Answer **3**.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
import java.util.Arrays;

class Solution {
    public int aggressiveCows(int[] stalls, int cows) {
        Arrays.sort(stalls);
        int low = 1, high = stalls[stalls.length - 1] - stalls[0];
        int best = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canPlace(stalls, cows, mid)) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return best;
    }

    private boolean canPlace(int[] stalls, int cows, int dist) {
        int count = 1;
        int last = stalls[0];
        for (int i = 1; i < stalls.length; i++) {
            if (stalls[i] - last >= dist) {
                count++;
                last = stalls[i];
                if (count >= cows) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
import "sort"

func aggressiveCows(stalls []int, cows int) int {
    sort.Ints(stalls)
    low, high := 1, stalls[len(stalls)-1]-stalls[0]
    best := 0
    for low <= high {
        mid := low + (high-low)/2
        if canPlace(stalls, cows, mid) {
            best = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return best
}

func canPlace(stalls []int, cows, dist int) bool {
    count, last := 1, stalls[0]
    for i := 1; i < len(stalls); i++ {
        if stalls[i]-last >= dist {
            count++
            last = stalls[i]
            if count >= cows {
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

- **Time:** O(N log N + N log G) — G = coordinate span
- **Space:** O(1) excluding sort

---

## Edge Cases

- `C == 2` — answer is max span
- All stalls adjacent — answer may be `1`
- Duplicate stall coordinates — sort keeps them; distance 0 blocks second cow at same spot

---

## Interview Follow-ups

1. **Book allocation / painters partition?** — Same maximize-minimum BS template.
2. **Why sort first?** — Greedy placement only works on ordered positions.
3. **Floating-point distances?** — Integer stalls → integer answer; no precision issues.

---

## See Also

- [Previous: Koko Eating Bananas](/dsa-coding/03-binary-search/koko-eating-bananas/)
- [Next: Recursion & Backtracking](/dsa-coding/04-recursion-backtracking/_index/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
