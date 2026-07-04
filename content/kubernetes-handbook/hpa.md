---
title: "HPA"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Horizontal Pod Autoscaler — CPU, memory, and custom metrics scaling."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "HPA"
module: 5
moduleTitle: "Scheduling & Scaling"
sectionRef: "5.5"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/hpa/"]
---

## Executive Summary

**HorizontalPodAutoscaler** scales Deployment/StatefulSet replicas based on metrics (CPU, memory, custom, external). Requires metrics-server or custom metrics adapter.

---

## Commands

### kubectl autoscale

**Purpose:** Create HPA for a deployment quickly.

**Syntax:**
```bash
kubectl autoscale deployment NAME --min=N --max=M --cpu-percent=P -n NS
```

**Example:**
```bash
kubectl autoscale deployment myapp --min=2 --max=10 --cpu-percent=70 -n myapp
```

**Output:**
```
horizontalpodautoscaler.autoscaling/myapp autoscaled
```

**Common mistakes:**
- v2 HPA prefers YAML for memory/custom metrics
- Target % is of requests — missing requests makes HPA ineffective

### kubectl get hpa

**Purpose:** Watch current/desired replicas and metric targets.

**Syntax:**
```bash
kubectl get hpa -n NAMESPACE
```

**Example:**
```bash
kubectl get hpa -n myapp
```

**Output:**
```
NAME    REFERENCE          TARGETS   MINPODS   MAXPODS   REPLICAS\nmyapp   Deployment/myapp   45%/70%   2         10        4
```

**Common mistakes:**
- `<unknown>/70%` means metrics not available
- Rapid flapping — tune behavior stabilization windows in YAML

### kubectl describe hpa

**Purpose:** Debug scaling events and metric resolution failures.

**Syntax:**
```bash
kubectl describe hpa NAME -n NS
```

**Example:**
```bash
kubectl describe hpa myapp -n myapp
```

**Output:**
```
Conditions: AbleToScale True ...
```

**Common mistakes:**
- Custom metrics need prometheus-adapter or equivalent
- Scale-down delay defaults may feel slow during traffic drops

---

## Related Topics

- [Resource Limits](/kubernetes-handbook/resource-limits/) · [Deployments](/kubernetes-handbook/deployments/)
