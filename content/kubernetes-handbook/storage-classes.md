---
title: "Storage Classes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Dynamic provisioning, provisioners, and volume parameters."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Storage Classes"
module: 4
moduleTitle: "Configuration & Storage"
sectionRef: "4.4"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/storage-classes/"]
---

## Executive Summary

**StorageClass** defines provisioner, parameters, reclaim policy, and volume binding mode (`Immediate` vs `WaitForFirstConsumer`).

---

## Commands

### kubectl get storageclass

**Purpose:** List available classes and default annotation.

**Syntax:**
```bash
kubectl get sc
```

**Example:**
```bash
kubectl get sc
```

**Output:**
```
NAME                 PROVISIONER             RECLAIMPOLICY\nstandard (default)   kubernetes.io/gce-pd   Delete
```

**Common mistakes:**
- No default SC causes PVC to stay Pending without explicit className
- Cloud provisioner name differs per platform

### kubectl describe storageclass

**Purpose:** Inspect provisioner parameters and binding mode.

**Syntax:**
```bash
kubectl describe sc NAME
```

**Example:**
```bash
kubectl describe sc fast-ssd
```

**Output:**
```
Parameters: type=pd-ssd\nVolumeBindingMode: WaitForFirstConsumer
```

**Common mistakes:**
- WaitForFirstConsumer delays binding until pod scheduled — normal
- Wrong parameter keys silently fail on some provisioners

---

## Related Topics

- [Persistent Volumes](/kubernetes-handbook/persistent-volumes/) · [Affinity](/kubernetes-handbook/affinity-and-anti-affinity/) (zones)
