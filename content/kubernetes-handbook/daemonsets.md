---
title: "DaemonSets"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Run one pod per node — agents, log collectors, CNI plugins."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "DaemonSets"
module: 2
moduleTitle: "Architecture & Workloads"
sectionRef: "2.6"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/daemonsets/"]
---

## Executive Summary

**DaemonSet** ensures one pod copy runs on every (or selected) node — typical for node agents, log shippers, and CNI plugins.

---

## Commands

### kubectl get daemonset

**Purpose:** Show desired, current, ready, and available pod counts per DaemonSet.

**Syntax:**
```bash
kubectl get ds [-n NAMESPACE]
```

**Example:**
```bash
kubectl get ds -n kube-system
```

**Output:**
```
NAME         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE\nfluent-bit   5         5         5       5            5
```

**Common mistakes:**
- DESIRED equals eligible node count — taints reduce eligible nodes
- Not Ready on upgraded nodes often means rolling update in progress

### kubectl rollout status daemonset

**Purpose:** Wait for DaemonSet rollout to complete on all nodes.

**Syntax:**
```bash
kubectl rollout status ds/NAME -n NS
```

**Example:**
```bash
kubectl rollout status ds/fluent-bit -n logging
```

**Output:**
```
daemon set "fluent-bit" successfully rolled out
```

**Common mistakes:**
- Node cordon/drain reduces AVAILABLE temporarily
- MaxUnavailable in updateStrategy affects rollout speed

---

## Related Topics

- [Taints & Tolerations](/kubernetes-handbook/taints-and-tolerations/) · [Node affinity](/kubernetes-handbook/affinity-and-anti-affinity/)
