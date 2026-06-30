---
title: "Troubleshooting"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CrashLoopBackOff, ImagePullBackOff, pending pods, and events."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Troubleshooting"
module: 5
moduleTitle: "Operations & Security"
sectionRef: "5.6"
ShowToc: true
---

## Executive Summary

Systematic debug flow: **events → describe → logs → exec → endpoints → network**. Common failure modes: **CrashLoopBackOff**, **ImagePullBackOff**, **Pending**, **OOMKilled**.

---

## Commands

### Diagnose CrashLoopBackOff

**Purpose:** Get restart reason and previous logs.

**Syntax:**
```bash
kubectl describe pod POD -n NS && kubectl logs POD -n NS --previous
```

**Example:**
```bash
kubectl logs api-0 -n myapp --previous
```

**Output:**
```
Error: main class not found / exit code 1
```

**Common mistakes:**
- Current logs may be empty if container dies instantly
- Check liveness probe killing healthy-but-slow app

### Diagnose ImagePullBackOff

**Purpose:** Verify image name, tag, pull secrets, and registry auth.

**Syntax:**
```bash
kubectl describe pod POD -n NS
```

**Example:**
```bash
kubectl describe pod api-0 -n myapp
```

**Output:**
```
Failed to pull image "myapp:latest": not found
```

**Common mistakes:**
- `:latest` tag not pulled if already cached with old digest
- Private registry needs imagePullSecrets on pod spec

### Diagnose Pending pod

**Purpose:** Find scheduling failures — resources, affinity, taints, PVC.

**Syntax:**
```bash
kubectl describe pod POD -n NS
```

**Example:**
```bash
kubectl describe pod api-0 -n myapp
```

**Output:**
```
0/3 nodes available: insufficient cpu
```

**Common mistakes:**
- Pending without events — check scheduler logs
- PVC unbound blocks WaitForFirstConsumer pods

### kubectl debug (ephemeral container)

**Purpose:** Attach debug container to running pod (K8s 1.23+).

**Syntax:**
```bash
kubectl debug -it POD -n NS --image=busybox --target=CONTAINER
```

**Example:**
```bash
kubectl debug -it api-0 -n myapp --image=busybox --target=api
```

**Output:**
```
Targeting container "api". If you don't see a command prompt, try pressing enter.
```

**Common mistakes:**
- Ephemeral containers need feature gate/enabled on older distros
- Cannot copy files into main container filesystem easily

---

## Related Topics

- [Probes](/kubernetes-cheatsheet/probes/) · [Resource Limits](/kubernetes-cheatsheet/resource-limits/) · [Events & kubectl](/kubernetes-cheatsheet/common-kubectl-commands/)
