---
title: "Subdomain Visit Count"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "HashMap pattern — Subdomain Visit Count."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Subdomain Visit Count"
module: 2
moduleTitle: "Sliding Window & Prefix Sum"
sectionRef: "2.8"
weight: 208
languages: ["java", "golang"]
source: "https://leetcode.com/problems/subdomain-visit-count/"
sourceLabel: "LeetCode 811"
pattern: "HashMap"
interviewHandbook: true
---
# Subdomain Visit Count

**Source:** [LeetCode 811](https://leetcode.com/problems/subdomain-visit-count/) · **Pattern:** HashMap · **Problem #20**

---

## Problem Statement

Given visit strings `"count domain"` (e.g. `"900 google.mail.com"`), return all subdomains with total visit counts formatted as `"count subdomain"`.

| Constraint | Value |
| :--- | :--- |
| `n` | `1 ≤ cpdomains.length ≤ 100` |
| Domains | 1–3 labels, lowercase letters |
| Counts | `1 ≤ count ≤ 10⁴` per record |

---

## Pattern Recognition

**Canonical pattern:** [Sliding Window & Prefix Sum](/dsa-coding/02-sliding-window-prefix-sum/) — full framework in module primer.

Split domain on `.`, accumulate counts for every suffix key — trie-like decomposition with a HashMap.

### Why this pattern?

Parse counts + aggregate by subdomain key → HashMap.

### Why not another pattern?

Array structures don't fit hierarchical keys; sorting irrelevant.

### What the interviewer expects

String parsing edge cases; composite keys with dots.

---

## Brute Force

For each record, enumerate all suffix domains — same asymptotics as optimal; HashMap aggregation keeps code simple.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`"900 google.mail.com"` → add 900 to `google.mail.com`, `mail.com`, `com`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> counts = new HashMap<>();
        for (String cp : cpdomains) {
            int space = cp.indexOf(' ');
            int visits = Integer.parseInt(cp.substring(0, space));
            String[] parts = cp.substring(space + 1).split("\\.");
            StringBuilder sb = new StringBuilder();
            for (int i = parts.length - 1; i >= 0; i--) {
                if (sb.length() > 0) sb.insert(0, '.');
                sb.insert(0, parts[i]);
                counts.merge(sb.toString(), visits, Integer::sum);
            }
        }
        List<String> res = new ArrayList<>();
        for (var e : counts.entrySet()) {
            res.add(e.getValue() + " " + e.getKey());
        }
        return res;
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func subdomainVisits(cpdomains []string) []string {
    counts := make(map[string]int)
    for _, cp := range cpdomains {
        parts := strings.SplitN(cp, " ", 2)
        visits, _ := strconv.Atoi(parts[0])
        labels := strings.Split(parts[1], ".")
        domain := ""
        for i := len(labels) - 1; i >= 0; i-- {
            if domain == "" {
                domain = labels[i]
            } else {
                domain = labels[i] + "." + domain
            }
            counts[domain] += visits
        }
    }
    res := make([]string, 0, len(counts))
    for d, c := range counts {
        res = append(res, strconv.Itoa(c)+" "+d)
    }
    return res
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(n · L) — L = labels per domain
- **Space:** O(unique subdomains)

---

## Edge Cases

- Single-label domain `com`
- Multiple records same subdomain — sums merge
- Output order unspecified

---

## Interview Follow-ups

1. **Trie instead of map?** — Same counts; trie enables prefix queries.
2. **Wildcard DNS?** — Out of scope — exact suffix keys only.
3. **Parse without split?** — Manual scan for `.` boundaries.

---

## See Also

- [Previous: Trapping Rain Water](/dsa-coding/02-sliding-window-prefix-sum/trapping-rain-water/)
- [Next: Binary Search](/dsa-coding/03-binary-search/_index/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
