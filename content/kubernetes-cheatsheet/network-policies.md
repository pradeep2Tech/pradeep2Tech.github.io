---
title: "Network Policies"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Pod-level firewall rules for ingress and egress traffic."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Network Policies"
module: 2
moduleTitle: "Networking & Exposure"
sectionRef: "2.3"
ShowToc: true
---

## Executive Summary

**NetworkPolicy** filters pod ingress/egress by namespace, pod labels, IP blocks, and ports. Requires a CNI that enforces policies (Calico, Cilium, etc.).

---

## Commands

### kubectl get networkpolicies

**Purpose:** List policies and which pods they may affect.

**Syntax:**
```bash
kubectl get networkpolicies -n NAMESPACE
```

**Example:**
```bash
kubectl get netpol -n myapp
```

**Output:**
```
NAME           POD-SELECTOR   AGE\napi-allow-db   app=api        5d
```

**Common mistakes:**
- No policies often means allow-all — verify CNI default
- Policy only selects pods listed in `podSelector` — empty selects all in namespace

### kubectl describe networkpolicy

**Purpose:** Inspect ingress/egress rules and peers.

**Syntax:**
```bash
kubectl describe netpol NAME -n NS
```

**Example:**
```bash
kubectl describe netpol api-allow-db -n myapp
```

**Output:**
```
Policy Types: Ingress\nAllowed Ingress: ...
```

**Common mistakes:**
- Egress denied by default only if policy types include Egress
- Cross-namespace rules need namespaceSelector labels

### kubectl run netshoot (debug)

**Purpose:** Test connectivity from a pod with shell and network tools.

**Syntax:**
```bash
kubectl run netshoot --rm -it --image=nicolaka/netshoot -- bash
```

**Example:**
```bash
kubectl run netshoot --rm -it --image=nicolaka/netshoot -n myapp -- curl -v telnet://db:5432
```

**Output:**
```
Connected to db.myapp.svc.cluster.local
```

**Common mistakes:**
- Debug pod must match policy labels to simulate real workload
- DNS egress may need explicit allow rule

---

## Related Topics

- [Services](/kubernetes-cheatsheet/services/) · [Namespaces](/kubernetes-cheatsheet/namespaces/)
