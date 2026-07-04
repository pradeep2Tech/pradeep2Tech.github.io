---
title: "Taints & Tolerations"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Repel pods from nodes unless they tolerate specific taints."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Taints"
module: 5
moduleTitle: "Scheduling & Scaling"
sectionRef: "5.3"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/taints-and-tolerations/"]
---

## Executive Summary

**Taints** repel pods from nodes unless pods have matching **tolerations**. Used for dedicated nodes, GPU pools, and control-plane isolation.

---

## Commands

### kubectl taint nodes

**Purpose:** Add or remove taints on a node.

**Syntax:**
```bash
kubectl taint nodes NODE KEY=VALUE:Effect
```

**Example:**
```bash
kubectl taint nodes node-2 dedicated=gpu:NoSchedule
```

**Output:**
```
node/node-2 tainted
```

**Common mistakes:**
- Effect NoExecute evicts existing pods without toleration
- Removing taint requires `-` suffix: `dedicated=gpu:NoSchedule-`

### kubectl describe node

**Purpose:** View taints and allocated resources on a node.

**Syntax:**
```bash
kubectl describe node NODE
```

**Example:**
```bash
kubectl describe node node-2
```

**Output:**
```
Taints: dedicated=gpu:NoSchedule
```

**Common mistakes:**
- Cordon (`SchedulingDisabled`) is not a taint — different mechanism
- NotReady nodes retain taints — drain before maintenance

### kubectl drain

**Purpose:** Evict pods and mark node unschedulable for maintenance.

**Syntax:**
```bash
kubectl drain NODE --ignore-daemonsets --delete-emptydir-data
```

**Example:**
```bash
kubectl drain node-2 --ignore-daemonsets --delete-emptydir-data
```

**Output:**
```
node/node-2 cordoned\n... evicted
```

**Common mistakes:**
- Without `--ignore-daemonsets` drain hangs on DaemonSet pods
- Pods with local storage need `--delete-emptydir-data` or manual handling

---

## Related Topics

- [Affinity](/kubernetes-handbook/affinity-and-anti-affinity/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)
