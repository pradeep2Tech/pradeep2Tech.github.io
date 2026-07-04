---
title: "ConfigMaps"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Non-sensitive configuration as env vars or mounted files."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "ConfigMaps"
module: 4
moduleTitle: "Configuration & Storage"
sectionRef: "4.1"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/configmaps/"]
---

## Executive Summary

**ConfigMap** stores non-sensitive config as key-value pairs or file snippets. Inject via env vars, envFrom, or volume mounts.

---

## Commands

### kubectl create configmap

**Purpose:** Create from literals or files.

**Syntax:**
```bash
kubectl create configmap NAME --from-literal=k=v [--from-file=path] -n NS
```

**Example:**
```bash
kubectl create configmap myapp-config --from-literal=LOG_LEVEL=info -n myapp
```

**Output:**
```
configmap/myapp-config created
```

**Common mistakes:**
- `--from-env-file` expects KEY=VALUE lines
- Large ConfigMaps hit 1Mi etcd object limit — split or use volumes

### kubectl get configmap -o yaml

**Purpose:** Export ConfigMap for review or GitOps.

**Syntax:**
```bash
kubectl get configmap NAME -o yaml -n NS
```

**Example:**
```bash
kubectl get configmap myapp-config -o yaml -n myapp
```

**Output:**
```
apiVersion: v1\nkind: ConfigMap\ndata:\n  LOG_LEVEL: info
```

**Common mistakes:**
- Editing live ConfigMap does not restart pods using envFrom — remount or rollout
- Binary data belongs in Secrets or external store

### kubectl rollout restart

**Purpose:** Restart pods to pick up mounted ConfigMap changes.

**Syntax:**
```bash
kubectl rollout restart deployment/NAME -n NS
```

**Example:**
```bash
kubectl rollout restart deployment/myapp -n myapp
```

**Output:**
```
deployment.apps/myapp restarted
```

**Common mistakes:**
- Env var injection is immutable at pod start — restart required
- SubPath volume mounts do not auto-update — avoid subPath for hot reload

---

## Related Topics

- [Secrets](/kubernetes-handbook/secrets/) · [Deployments](/kubernetes-handbook/deployments/)
