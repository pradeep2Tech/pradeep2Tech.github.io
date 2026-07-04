---
title: "Sliding Window Template"
date: 2026-07-04T00:00:00+00:00
draft: false
description: "SW Template"
tags: ["dsa-coding", "dsa", "algorithms", "interview"]
categories: ["DSA & Coding"]
shortTitle: "SW Template"
module: 9
moduleTitle: "DSA & Coding"
sectionRef: "9.4"
weight: 904
interviewHandbook: true
---

# Sliding Window Template

> **Canonical theory:** [Module 2](/dsa-coding/02-sliding-window-prefix-sum/). This page keeps **copy-paste snippets only**.

## Fixed window of size `k`

```java
int sum = 0, best = 0;
for (int i = 0; i < nums.length; i++) {
    sum += nums[i];
    if (i >= k) sum -= nums[i - k];
    if (i >= k - 1) best = Math.max(best, sum);
}
```

## Variable window — expand right, shrink left

```java
Map<Character, Integer> freq = new HashMap<>();
int left = 0, best = 0;
for (int right = 0; right < s.length(); right++) {
    // add s[right] to window state
    while (windowInvalid()) {
        // remove s[left], left++
    }
    best = Math.max(best, right - left + 1);
}
```

## Go — variable window

```go
left := 0
best := 0
for right := 0; right < len(s); right++ {
    // expand with s[right]
    for windowInvalid() {
        // shrink s[left]
        left++
    }
    if right-left+1 > best {
        best = right - left + 1
    }
}
```
