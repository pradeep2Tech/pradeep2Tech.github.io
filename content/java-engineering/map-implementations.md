---
title: "Map Implementations Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "HashMap, LinkedHashMap, TreeMap, CHM selection — when to use which."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Maps"
module: 2
moduleTitle: "Collections"
sectionRef: "2.4"
interviewHandbook: true
aliases:
  - map-implementations-ref
---

## HashMap vs TreeMap?

**Difficulty:** Easy · **Time:** 30 sec

### Short Answer

HashMap: O(1) avg, unordered. TreeMap: O(log n), sorted, `NavigableMap` range ops.

### Detailed Explanation

TreeMap needs `Comparable` keys or Comparator. No null keys in TreeMap (usually).

### Interview Questions

1. NavigableMap floor/ceiling use cases?

### Follow-up Questions

- NavigableMap floor/ceiling use cases?

---
## WeakHashMap vs HashMap?

**Difficulty:** Medium · **Time:** 1 min

### Short Answer

WeakHashMap keys are weak references — entries removed when key only weakly reachable.

### Detailed Explanation

Use for listener registries or caches where keys should GC independently. Values need strong refs elsewhere or they disappear too.

### Interview Questions

1. IdentityHashMap use case?

### Follow-up Questions

- IdentityHashMap use case?

---
