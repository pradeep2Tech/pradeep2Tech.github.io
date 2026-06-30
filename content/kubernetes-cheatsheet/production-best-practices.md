---
title: "Production Best Practices"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Security, reliability, observability, and cluster hygiene checklist."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Production"
module: 5
moduleTitle: "Operations & Security"
sectionRef: "5.7"
ShowToc: true
---

## Executive Summary

Production checklist: **RBAC least privilege**, **resource requests/limits**, **PDBs**, **network policies**, **no `:latest`**, **GitOps**, **backup etcd/PV**, **ingress TLS**, **monitoring & alerts**.

---

## Commands

### kubectl create poddisruptionbudget

**Purpose:** Ensure minimum availability during voluntary disruptions.

**Syntax:**
```bash
kubectl create poddisruptionbudget NAME --selector=LABEL=VALUE --min-available=N -n NS
```

**Example:**
```bash
kubectl create pdb api-pdb --selector=app=api --min-available=2 -n myapp
```

**Output:**
```
poddisruptionbudget.policy/api-pdb created
```

**Common mistakes:**
- maxUnavailable and minAvailable conflict — set only one
- PDB ignored for single-replica deployments — still allows drain issues

### kubectl cordon / uncordon

**Purpose:** Prevent new schedules without evicting (cordon).

**Syntax:**
```bash
kubectl cordon NODE && kubectl uncordon NODE
```

**Example:**
```bash
kubectl cordon node-3
```

**Output:**
```
node/node-3 cordoned
```

**Common mistakes:**
- Cordon alone does not migrate workloads — pair with drain
- Forgotten cordon reduces cluster capacity silently

### kubectl get pdb,hpa,netpol

**Purpose:** Audit resilience objects in namespace.

**Syntax:**
```bash
kubectl get pdb,hpa,networkpolicies -n NS
```

**Example:**
```bash
kubectl get pdb,hpa,netpol -n myapp
```

**Output:**
```
NAME      MIN AVAILABLE   ALLOWED DISRUPTIONS\napi-pdb   2               1
```

**Common mistakes:**
- Missing netpol in multi-tenant cluster is a security gap
- Review Helm values for production overrides in CI

---

## Related Topics

- [RBAC](/kubernetes-cheatsheet/rbac/) · [Network Policies](/kubernetes-cheatsheet/network-policies/) · [HPA](/kubernetes-cheatsheet/hpa/) · [Microservices — Zero-Downtime Deployment](/microservices/zero-downtime-deployment-topologies/)
