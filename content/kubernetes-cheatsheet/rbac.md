---
title: "RBAC"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Roles, ClusterRoles, bindings, and least-privilege access."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "RBAC"
module: 5
moduleTitle: "Operations & Security"
sectionRef: "5.3"
ShowToc: true
---

## Executive Summary

**RBAC** grants permissions via **Role/ClusterRole** + **RoleBinding/ClusterRoleBinding**. Principle of least privilege — separate CI, dev, and admin roles.

---

## Commands

### kubectl auth can-i

**Purpose:** Check whether current user/service account can perform action.

**Syntax:**
```bash
kubectl auth can-i VERB RESOURCE [--as=USER] -n NS
```

**Example:**
```bash
kubectl auth can-i create deployments -n myapp
```

**Output:**
```
yes
```

**Common mistakes:**
- Use `--as=system:serviceaccount:ns:sa` for SA checks
- Cluster-scoped verbs need omitting `-n` or ClusterRole

### kubectl create rolebinding

**Purpose:** Bind a Role to user/group/service account.

**Syntax:**
```bash
kubectl create rolebinding NAME --role=ROLE --user=USER -n NS
```

**Example:**
```bash
kubectl create rolebinding deployer --role=deployer --user=ci-bot -n myapp
```

**Output:**
```
rolebinding.rbac.authorization.k8s.io/deployer created
```

**Common mistakes:**
- RoleBinding only grants namespace scope — use ClusterRoleBinding for CRDs cluster-wide
- Default SA in namespace often over-permissioned in dev clusters

### kubectl get role,rolebinding

**Purpose:** Audit RBAC objects in namespace.

**Syntax:**
```bash
kubectl get role,rolebinding -n NS
```

**Example:**
```bash
kubectl get role,rolebinding -n myapp
```

**Output:**
```
NAME        CREATED AT\ndeployer    2026-01-01
```

**Common mistakes:**
- Bindings reference role by name — deleting role breaks binding silently
- Use `kubectl who-can` plugins for bulk audits

---

## Related Topics

- [Namespaces](/kubernetes-cheatsheet/namespaces/) · [Production Best Practices](/kubernetes-cheatsheet/production-best-practices/)
