---
title: "Labels & Selectors"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Key-value metadata for grouping, selection, and service routing."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Labels & Selectors"
module: 4
moduleTitle: "Scheduling & Scaling"
sectionRef: "4.1"
ShowToc: true
---

## Executive Summary

**Labels** are arbitrary key/value metadata on objects. **Selectors** filter resources — equality (`app=api`) or set-based (`env in (prod,staging)`).

---

## Commands

### kubectl get pods -l

**Purpose:** Filter pods by label selector.

**Syntax:**
```bash
kubectl get pods -l KEY=VALUE [-n NS]
```

**Example:**
```bash
kubectl get pods -l app=api,tier=frontend -n myapp
```

**Output:**
```
NAME           READY   STATUS\napi-7f8b9c-xyz  1/1     Running
```

**Common mistakes:**
- Comma is AND — use `-l 'env in (prod)'` for OR/set syntax
- Typos in labels return empty list — verify with `--show-labels`

### kubectl label

**Purpose:** Add or update labels on resources.

**Syntax:**
```bash
kubectl label RESOURCE NAME KEY=VALUE [--overwrite] -n NS
```

**Example:**
```bash
kubectl label pod api-7f8b9c-xyz version=2.0.0 -n myapp
```

**Output:**
```
pod/api-7f8b9c-xyz labeled
```

**Common mistakes:**
- Changing labels breaks Service/Deployment selectors if inconsistent
- Immutable label keys on some controllers — check webhook errors

### kubectl get pods --show-labels

**Purpose:** Display all labels for troubleshooting selector mismatches.

**Syntax:**
```bash
kubectl get pods --show-labels -n NS
```

**Example:**
```bash
kubectl get pods --show-labels -n myapp
```

**Output:**
```
NAME    ...   LABELS\napi-...       app=api,tier=frontend
```

**Common mistakes:**
- Label values appear in metrics cardinality — avoid high-cardinality values
- Recommended labels: app.kubernetes.io/name, instance, version

---

## Related Topics

- [Services](/kubernetes-cheatsheet/services/) · [Deployments](/kubernetes-cheatsheet/deployments/)
