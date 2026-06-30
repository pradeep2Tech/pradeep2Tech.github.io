---
title: "Helm Basics"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Charts, releases, values, and upgrade/rollback workflow."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Helm"
module: 5
moduleTitle: "Operations & Security"
sectionRef: "5.4"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/helm-basics/"]
---

## Executive Summary

**Helm** packages Kubernetes manifests as **charts**. **Releases** are installed chart instances with versioned **values** overrides.

---

## Commands

### helm install

**Purpose:** Deploy a chart release into a namespace.

**Syntax:**
```bash
helm install RELEASE CHART [-n NS] [--create-namespace] [-f values.yaml]
```

**Example:**
```bash
helm install myapp oci://registry.example.com/charts/myapp -n myapp --create-namespace -f prod.yaml
```

**Output:**
```
NAME: myapp\nSTATUS: deployed\nREVISION: 1
```

**Common mistakes:**
- Release name must be unique per namespace
- Wrong values file key silently ignored — validate with `helm template`

### helm upgrade --install

**Purpose:** Idempotent install or upgrade (CI-friendly).

**Syntax:**
```bash
helm upgrade --install RELEASE CHART -n NS -f values.yaml
```

**Example:**
```bash
helm upgrade --install myapp ./chart -n myapp -f prod.yaml
```

**Output:**
```
Release "myapp" has been upgraded. Happy Helming!
```

**Common mistakes:**
- Without `--atomic`, failed upgrade may leave partial resources
- Use `--dry-run` in pipeline before apply

### helm rollback

**Purpose:** Revert release to previous revision.

**Syntax:**
```bash
helm rollback RELEASE REVISION -n NS
```

**Example:**
```bash
helm rollback myapp 3 -n myapp
```

**Output:**
```
Rollback was a success! Happy Helming!
```

**Common mistakes:**
- Revision 1 may reference deleted chart version — keep chart artifacts
- Rollback does not rollback CRDs always — test CRD upgrades

### helm list / history

**Purpose:** List releases and revision history.

**Syntax:**
```bash
helm history RELEASE -n NS
```

**Example:**
```bash
helm history myapp -n myapp
```

**Output:**
```
REVISION  STATUS      CHART\n3         deployed    myapp-1.2.0
```

**Common mistakes:**
- `-a` shows failed/uninstalled releases
- Secrets backend stores release data — protect etcd backups

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)
