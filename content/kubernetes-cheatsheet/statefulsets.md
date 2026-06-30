---
title: "StatefulSets"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Stable identity, ordered rollout, and persistent storage for stateful apps."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "StatefulSets"
module: 1
moduleTitle: "Architecture & Workloads"
sectionRef: "1.5"
ShowToc: true
---

## Executive Summary

**StatefulSet** gives pods stable network identity (`pod-0`, `pod-1`), ordered rollout/scale, and per-pod PersistentVolumeClaims via `volumeClaimTemplates`.

---

## Commands

### kubectl get statefulset

**Purpose:** List StatefulSets and ready replicas.

**Syntax:**
```bash
kubectl get sts [-n NAMESPACE]
```

**Example:**
```bash
kubectl get sts -n data
```

**Output:**
```
NAME   READY   AGE\npg     3/3     7d
```

**Common mistakes:**
- Abbreviation `sts` is common
- READY stuck below desired — check PVC binding and pod events

### kubectl scale statefulset

**Purpose:** Scale replicas — pods created/deleted in ordinal order.

**Syntax:**
```bash
kubectl scale sts NAME --replicas=N -n NS
```

**Example:**
```bash
kubectl scale sts pg --replicas=3 -n data
```

**Output:**
```
statefulset.apps/pg scaled
```

**Common mistakes:**
- Scaling down deletes highest ordinal first — data loss risk without backups
- Scale-up is serial by default — can be slow for large counts

### kubectl delete pod (force reschedule)

**Purpose:** Delete a StatefulSet pod — controller recreates with same identity.

**Syntax:**
```bash
kubectl delete pod POD_NAME -n NS
```

**Example:**
```bash
kubectl delete pod pg-1 -n data
```

**Output:**
```
pod "pg-1" deleted
```

**Common mistakes:**
- Do not delete PVCs unless you intend to wipe data
- Pod name is predictable — use for debugging specific shard

---

## Related Topics

- [Persistent Volumes](/kubernetes-cheatsheet/persistent-volumes/) · [Services](/kubernetes-cheatsheet/services/) (headless)
