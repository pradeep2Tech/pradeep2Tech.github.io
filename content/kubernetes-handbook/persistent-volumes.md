---
title: "Persistent Volumes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "PV, PVC, binding, access modes, and reclaim policies."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Persistent Volumes"
module: 3
moduleTitle: "Configuration & Storage"
sectionRef: "3.3"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/persistent-volumes/"]
---

## Executive Summary

**PersistentVolume (PV)** is cluster storage. **PersistentVolumeClaim (PVC)** requests capacity and access mode. Binding is one-to-one for static PVs; StorageClass enables dynamic provisioning.

---

## Commands

### kubectl get pv,pvc

**Purpose:** List volumes and claims with status and capacity.

**Syntax:**
```bash
kubectl get pv,pvc [-n NAMESPACE]
```

**Example:**
```bash
kubectl get pvc -n myapp
```

**Output:**
```
NAME        STATUS   VOLUME     CAPACITY   ACCESS MODES\ndata-pvc    Bound    pv-abc     10Gi       RWO
```

**Common mistakes:**
- Pending PVC — no matching PV or StorageClass provisioner failed
- Released PV needs reclaim policy handled before reuse

### kubectl describe pvc

**Purpose:** See events for provisioning failures and selected StorageClass.

**Syntax:**
```bash
kubectl describe pvc NAME -n NS
```

**Example:**
```bash
kubectl describe pvc data-pvc -n myapp
```

**Output:**
```
Events: Provisioning succeeded...
```

**Common mistakes:**
- Wrong access mode (RWO vs RWM) blocks binding
- Zone mismatch in multi-AZ clusters — check topology

### kubectl delete pvc

**Purpose:** Release claim — PV behavior depends on reclaim policy.

**Syntax:**
```bash
kubectl delete pvc NAME -n NS
```

**Example:**
```bash
kubectl delete pvc data-pvc -n myapp
```

**Output:**
```
persistentvolumeclaim "data-pvc" deleted
```

**Common mistakes:**
- Retain policy leaves PV in Released — manual cleanup needed
- Deleting PVC wipes data on Delete reclaim policy

---

## Related Topics

- [Storage Classes](/kubernetes-handbook/storage-classes/) · [StatefulSets](/kubernetes-handbook/statefulsets/)
