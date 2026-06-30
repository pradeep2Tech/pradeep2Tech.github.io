---
title: "ReplicaSets"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Replica count enforcement and pod template matching."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "ReplicaSets"
module: 1
moduleTitle: "Architecture & Workloads"
sectionRef: "1.3"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/replicasets/"]
---

## Executive Summary

**ReplicaSet** maintains a stable set of pod replicas matching a label selector. Deployments manage ReplicaSets — you rarely create ReplicaSets directly.

---

## Commands

### kubectl get rs

**Purpose:** List ReplicaSets and desired/current/ready replica counts.

**Syntax:**
```bash
kubectl get rs -n NAMESPACE
```

**Example:**
```bash
kubectl get rs -n myapp
```

**Output:**
```
NAME             DESIRED   CURRENT   READY   AGE\nmyapp-6d4f8b9c7d   3         3         3       2d
```

**Common mistakes:**
- Old ReplicaSets with DESIRED=0 are normal after rolling update
- READY < DESIRED indicates failing readiness probes

### kubectl describe rs

**Purpose:** Inspect selector, pod template, and events for a ReplicaSet.

**Syntax:**
```bash
kubectl describe rs RS_NAME -n NAMESPACE
```

**Example:**
```bash
kubectl describe rs myapp-6d4f8b9c7d -n myapp
```

**Output:**
```
Replicas: 3 current / 3 desired\nPods Status: 3 Running / 0 Waiting / 0 Succeeded / 0 Failed
```

**Common mistakes:**
- ReplicaSet name hash changes on pod template change
- Events may reference Deployment as owner — follow ownerReferences

### kubectl scale (via deployment)

**Purpose:** Change replica count — Deployment updates underlying ReplicaSet.

**Syntax:**
```bash
kubectl scale deployment NAME --replicas=N -n NS
```

**Example:**
```bash
kubectl scale deployment myapp --replicas=5 -n myapp
```

**Output:**
```
deployment.apps/myapp scaled
```

**Common mistakes:**
- Scaling ReplicaSet directly is overwritten by Deployment controller
- HPA may scale back if CPU/memory targets differ

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Labels & Selectors](/kubernetes-handbook/labels-and-selectors/)
