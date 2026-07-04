---
title: "Alien Dictionary"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "Topological Sort pattern — Alien Dictionary."
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "Alien Dictionary"
module: 7
moduleTitle: "Advanced Graphs"
sectionRef: "7.1"
weight: 701
languages: ["java", "golang"]
source: "https://leetcode.com/problems/alien-dictionary/"
sourceLabel: "LeetCode 269"
pattern: "Topological Sort"
ShowToc: true
interviewHandbook: true
---
# Alien Dictionary

**Source:** [LeetCode 269](https://leetcode.com/problems/alien-dictionary/) · **Pattern:** Topological Sort · **Problem #48**

---

## Problem Statement

A new alien language uses a sorted list of words. Derive the character order. Return any valid ordering of unique letters, or `""` if no valid order exists (cycle detected).

| Constraint | Value |
| :--- | :--- |
| `words` | `1 ≤ words.length ≤ 10²` |
| Word length | `1 ≤ words[i].length ≤ 10²` |
| Letters | Lowercase English; all words non-empty |

---

## Pattern Recognition

**Canonical pattern:** [Advanced Graphs](/dsa-coding/07-advanced-graphs/) — full framework in module primer.

Adjacent words reveal the first differing character's precedence — build directed edges `u → v`. Ordering exists iff the graph is a DAG → topological sort (Kahn's BFS or DFS post-order).

### Why this pattern?

Build char graph from adjacent word pairs; topo sort for order.

### Why not another pattern?

Lex sort of all chars wrong; HashMap alone doesn't encode precedence.

### What the interviewer expects

Cycle detection; invalid input when prefix longer than word.

---

## Brute Force

Try all permutations of unique letters and validate against every adjacent pair — **O(U! · W)** where U = unique letters, W = word count. Impossible at interview scale.

---

## Optimal Solution

Invariant is under Pattern Recognition — see implementation below.

---

## Walkthrough

`words = ["wrt","wrf","er","ett","rftt"]`. From `wrt` vs `wrf` → `t` before `f`; `wrt` vs `er` → `w` before `e`; `er` vs `ett` → `r` before `t`; `ett` vs `rftt` → `e` before `r`. Topological order: `w → e → r → t → f`.

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
class Solution {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> adj = new HashMap<>();
        Map<Character, Integer> indeg = new HashMap<>();
        for (String w : words) {
            for (char c : w.toCharArray()) {
                adj.putIfAbsent(c, new HashSet<>());
                indeg.putIfAbsent(c, 0);
            }
        }
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i + 1];
            if (w1.length() > w2.length() && w1.startsWith(w2)) return "";
            for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
                char u = w1.charAt(j), v = w2.charAt(j);
                if (u != v) {
                    if (!adj.get(u).contains(v)) {
                        adj.get(u).add(v);
                        indeg.put(v, indeg.get(v) + 1);
                    }
                    break;
                }
            }
        }
        Queue<Character> q = new ArrayDeque<>();
        for (char c : indeg.keySet()) {
            if (indeg.get(c) == 0) q.offer(c);
        }
        StringBuilder order = new StringBuilder();
        while (!q.isEmpty()) {
            char c = q.poll();
            order.append(c);
            for (char nei : adj.get(c)) {
                indeg.put(nei, indeg.get(nei) - 1);
                if (indeg.get(nei) == 0) q.offer(nei);
            }
        }
        return order.length() == indeg.size() ? order.toString() : "";
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
func alienOrder(words []string) string {
    adj := make(map[byte]map[byte]struct{})
    indeg := make(map[byte]int)
    addChar := func(c byte) {
        if _, ok := adj[c]; !ok {
            adj[c] = make(map[byte]struct{})
            indeg[c] = 0
        }
    }
    for _, w := range words {
        for i := 0; i < len(w); i++ {
            addChar(w[i])
        }
    }
    for i := 0; i < len(words)-1; i++ {
        w1, w2 := words[i], words[i+1]
        if len(w1) > len(w2) && strings.HasPrefix(w1, w2) {
            return ""
        }
        lim := len(w1)
        if len(w2) < lim {
            lim = len(w2)
        }
        for j := 0; j < lim; j++ {
            if w1[j] != w2[j] {
                u, v := w1[j], w2[j]
                if _, seen := adj[u][v]; !seen {
                    adj[u][v] = struct{}{}
                    indeg[v]++
                }
                break
            }
        }
    }
    q := make([]byte, 0)
    for c, d := range indeg {
        if d == 0 {
            q = append(q, c)
        }
    }
    var order []byte
    for len(q) > 0 {
        c := q[0]
        q = q[1:]
        order = append(order, c)
        for nei := range adj[c] {
            indeg[nei]--
            if indeg[nei] == 0 {
                q = append(q, nei)
            }
        }
    }
    if len(order) != len(indeg) {
        return ""
    }
    return string(order)
}
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

## Complexity

- **Time:** O(C + V + E) — C = total characters across words
- **Space:** O(V + E)

---

## Edge Cases

- Single word — return its unique letters in any order
- Invalid prefix: `["abc", "ab"]` → `""`
- Cycle in constraints → `""`
- Duplicate edges from multiple word pairs — dedupe

---

## Interview Follow-ups

1. **DFS topo sort instead of Kahn?** — Post-order stack works; detect back-edge for cycle.
2. **Multiple valid orders?** — Any topological ordering is accepted.
3. **Related: Course Schedule?** — Same DAG + topo pattern; build edges from prerequisites.

---

## See Also

- [Previous: Advanced Graphs](/dsa-coding/07-advanced-graphs/_index/)
- [Next: All Nodes Distance K in Binary Tree](/dsa-coding/07-advanced-graphs/all-nodes-distance-k-in-binary-tree/)
- [DSA & Coding Index](/dsa-coding/)
- [Java Engineering](/java-engineering/)
- [Design Patterns](/design-patterns/)
