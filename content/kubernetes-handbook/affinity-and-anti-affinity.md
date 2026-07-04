---
title: "Affinity & Anti-Affinity"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Pod placement rules — node affinity, pod affinity, and topology spread."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Affinity"
module: 5
moduleTitle: "Scheduling & Scaling"
sectionRef: "5.2"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/affinity-and-anti-affinity/"]
---

## Executive Summary

**Affinity** attracts pods to nodes or other pods; **anti-affinity** spreads replicas across hosts/zones. **topologySpreadConstraints** distribute pods evenly.

---

## Commands

### kubectl get pods -o wide (spread check)

**Purpose:** Verify pods distributed across nodes after anti-affinity rules.

**Syntax:**
```bash
kubectl get pods -o wide -l app=NAME -n NS
```

**Example:**
```bash
kubectl get pods -o wide -l app=api -n myapp
```

**Output:**
```
NAME    NODE\napi-0   node-1\napi-1   node-2\napi-2   node-3
```

**Common mistakes:**
- All pods on one node — required anti-affinity missing or soft preference ignored
- Insufficient nodes makes hard anti-affinity leave pods Pending

### kubectl describe pod (scheduling)

**Purpose:** See events when affinity/anti-affinity blocks scheduling.

**Syntax:**
```bash
kubectl describe pod PENDING_POD -n NS
```

**Example:**
```bash
kubectl describe pod api-xyz -n myapp
```

**Output:**
```
0/5 nodes available: 3 node(s) didn't match pod anti-affinity rules
```

**Common mistakes:**
- Soft affinity (`preferredDuringScheduling`) never blocks — check if you needed hard
- Topology key must exist on nodes (`topology.kubernetes.io/zone`)

---

## YAML Snippet

### podAntiAffinity

**Purpose:** Spread replicas across hosts.

**Syntax:**
```yaml
podAntiAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchLabels:
          app: api
      topologyKey: kubernetes.io/hostname
```

**Example:**
```yaml
podAntiAffinity:
  preferredDuringSchedulingIgnoredDuringExecution:
    - weight: 100
      podAffinityTerm:
        labelSelector:
          matchLabels:
            app: api
        topologyKey: topology.kubernetes.io/zone
```

**Common mistakes:**
- `IgnoredDuringExecution` means rules not re-evaluated after schedule
- Mixing required rules too aggressively causes capacity fragmentation

---

## Related Topics

- [Taints & Tolerations](/kubernetes-handbook/taints-and-tolerations/) · [DaemonSets](/kubernetes-handbook/daemonsets/)
