---
title: "Resource Limits"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "CPU/memory requests and limits, QoS classes, and LimitRange."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Resource Limits"
module: 4
moduleTitle: "Scheduling & Scaling"
sectionRef: "4.4"
ShowToc: true
---

## Executive Summary

**requests** reserve schedulable capacity; **limits** cap usage. QoS classes: **Guaranteed**, **Burstable**, **BestEffort**. Set JVM/Go runtime flags to respect container limits.

---

## Commands

### kubectl top pods

**Purpose:** Show live CPU/memory usage (requires metrics-server).

**Syntax:**
```bash
kubectl top pods -n NAMESPACE
```

**Example:**
```bash
kubectl top pods -n myapp
```

**Output:**
```
NAME    CPU(cores)   MEMORY(bytes)\napi-0   120m         512Mi
```

**Common mistakes:**
- Metrics absent if metrics-server not installed
- Usage near limit triggers CPU throttle or OOMKill

### kubectl describe pod (QoS)

**Purpose:** Inspect QoS class and resource fields.

**Syntax:**
```bash
kubectl describe pod NAME -n NS
```

**Example:**
```bash
kubectl describe pod api-0 -n myapp
```

**Output:**
```
QoS Class: Burstable\nLimits: cpu 500m, memory 512Mi
```

**Common mistakes:**
- Limits without requests get request=limit for CPU/memory
- BestEffort pods evicted first under node pressure

### kubectl get limitrange

**Purpose:** View default/min/max container resources per namespace.

**Syntax:**
```bash
kubectl get limitrange -n NS
```

**Example:**
```bash
kubectl get limitrange -n myapp
```

**Output:**
```
NAME    CREATED AT\nlimits  2026-01-01
```

**Common mistakes:**
- Pods without resources inherit LimitRange defaults at admission
- ResourceQuota caps namespace totals — different from LimitRange

---

## Related Topics

- [HPA](/kubernetes-cheatsheet/hpa/) · [Production Best Practices](/kubernetes-cheatsheet/production-best-practices/)
