---
title: "Namespaces"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Logical isolation, quotas, and multi-tenant boundaries."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Namespaces"
module: 3
moduleTitle: "Configuration & Storage"
sectionRef: "3.5"
ShowToc: true
---

## Executive Summary

**Namespace** scopes names for objects and pairs with RBAC, quotas, and network policies for multi-tenant isolation.

---

## Commands

### kubectl create namespace

**Purpose:** Create a new namespace.

**Syntax:**
```bash
kubectl create namespace NAME
```

**Example:**
```bash
kubectl create namespace myapp
```

**Output:**
```
namespace/myapp created
```

**Common mistakes:**
- Namespace names cannot be changed — plan env prefix (`myapp-prod`)
- Deleting namespace deletes all objects inside — irreversible

### kubectl config set-context --namespace

**Purpose:** Set default namespace for current context.

**Syntax:**
```bash
kubectl config set-context --current --namespace=NS
```

**Example:**
```bash
kubectl config set-context --current --namespace=myapp
```

**Output:**
```
Context "prod" modified.
```

**Common mistakes:**
- Easy to forget and run commands in wrong namespace
- CI should pass `-n` explicitly instead of relying on context

### kubectl get all -n

**Purpose:** List common namespaced resources in one namespace.

**Syntax:**
```bash
kubectl get all -n NAMESPACE
```

**Example:**
```bash
kubectl get all -n myapp
```

**Output:**
```
pod/... service/... deployment/...
```

**Common mistakes:**
- `kubectl get all` omits Ingress, PVC, HPA — not literally everything
- Cluster-scoped resources (PV, SC) not shown

### kubectl get resourcequota

**Purpose:** Check namespace quota usage.

**Syntax:**
```bash
kubectl get resourcequota -n NS
```

**Example:**
```bash
kubectl get resourcequota -n myapp
```

**Output:**
```
NAME    AGE   REQUESTS.CPU   LIMITS.MEMORY\nquota   30d   2/4            8Gi/16Gi
```

**Common mistakes:**
- Quota enforced at admission — pods rejected without clear pod events sometimes
- LimitRange defaults apply per-container

---

## Related Topics

- [RBAC](/kubernetes-cheatsheet/rbac/) · [Resource Limits](/kubernetes-cheatsheet/resource-limits/)
