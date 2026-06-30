---
title: "Deployments"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Declarative rollouts, scaling, and rollback for stateless apps."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Deployments"
module: 1
moduleTitle: "Architecture & Workloads"
sectionRef: "1.4"
ShowToc: true
---

## Executive Summary

**Deployment** declares desired state for stateless apps: replica count, pod template, and rolling update strategy. It owns ReplicaSets and supports rollback.

---

## Commands

### kubectl apply -f deployment.yaml

**Purpose:** Create or update a Deployment declaratively.

**Syntax:**
```bash
kubectl apply -f FILE [-n NAMESPACE]
```

**Example:**
```bash
kubectl apply -f deployment.yaml -n myapp
```

**Output:**
```
deployment.apps/myapp configured
```

**Common mistakes:**
- `kubectl apply` merges — accidental field removal may not delete nested keys
- Use `--server-side` for large objects or field manager conflicts

### kubectl rollout status

**Purpose:** Wait until rollout completes successfully.

**Syntax:**
```bash
kubectl rollout status deployment/NAME -n NS
```

**Example:**
```bash
kubectl rollout status deployment/myapp -n myapp
```

**Output:**
```
deployment "myapp" successfully rolled out
```

**Common mistakes:**
- Hangs if new pods never become Ready — check probes and image
- CI pipelines should set a timeout

### kubectl rollout history

**Purpose:** List revision history for rollback.

**Syntax:**
```bash
kubectl rollout history deployment/NAME -n NS [--revision=N]
```

**Example:**
```bash
kubectl rollout history deployment/myapp -n myapp
```

**Output:**
```
REVISION  CHANGE-CAUSE\n1         <none>\n2         kubectl set image ...
```

**Common mistakes:**
- Without `--record` or change-cause annotation, history is sparse
- `--revision` shows manifest diff for that revision

### kubectl rollout undo

**Purpose:** Rollback to previous or specific revision.

**Syntax:**
```bash
kubectl rollout undo deployment/NAME [--to-revision=N] -n NS
```

**Example:**
```bash
kubectl rollout undo deployment/myapp -n myapp
```

**Output:**
```
deployment.apps/myapp rolled back
```

**Common mistakes:**
- Undo only changes pod template — not Service or Ingress
- Test rollback in staging — image tags may have been garbage-collected

### kubectl set image

**Purpose:** Trigger rolling update by changing container image.

**Syntax:**
```bash
kubectl set image deployment/NAME CONTAINER=IMAGE -n NS
```

**Example:**
```bash
kubectl set image deployment/myapp api=myapp:2.0.0 -n myapp
```

**Output:**
```
deployment.apps/myapp image updated
```

**Common mistakes:**
- Wrong container name silently fails or updates wrong container
- Always pin image digest or semver tag in production

---

## Related Topics

- [Rolling Updates](/kubernetes-cheatsheet/rolling-updates/) · [HPA](/kubernetes-cheatsheet/hpa/) · [Probes](/kubernetes-cheatsheet/probes/)
