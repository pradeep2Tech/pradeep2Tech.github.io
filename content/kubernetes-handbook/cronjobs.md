---
title: "CronJobs"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Scheduled Jobs with cron syntax and concurrency policies."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "CronJobs"
module: 2
moduleTitle: "Architecture & Workloads"
sectionRef: "2.8"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/cronjobs/"]
---

## Executive Summary

**CronJob** creates Jobs on a cron schedule. Control concurrency (`Allow`, `Forbid`, `Replace`) and history limits for completed/failed jobs.

---

## Commands

### kubectl create cronjob

**Purpose:** Schedule a recurring Job from an image.

**Syntax:**
```bash
kubectl create cronjob NAME --image=IMAGE --schedule='CRON' -n NS
```

**Example:**
```bash
kubectl create cronjob backup --image=backup:1.0 --schedule='0 2 * * *' -n ops
```

**Output:**
```
cronjob.batch/backup created
```

**Common mistakes:**
- Cron uses controller timezone (usually UTC) — document timezone
- Standard cron has 5 fields; some docs show 6-field seconds variant

### kubectl get cronjobs

**Purpose:** List schedules, last schedule time, and active jobs.

**Syntax:**
```bash
kubectl get cronjobs -n NAMESPACE
```

**Example:**
```bash
kubectl get cronjobs -n ops
```

**Output:**
```
NAME     SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE\nbackup   0 2 * * *   False     0        8h              30d
```

**Common mistakes:**
- SUSPEND True means schedule paused — easy to forget after debug
- ACTIVE > 1 may indicate Forbid policy not set and overlap

### kubectl delete jobs by label

**Purpose:** Clean up finished Job pods created by CronJob.

**Syntax:**
```bash
kubectl delete jobs -l cronjob-name=NAME -n NS
```

**Example:**
```bash
kubectl delete jobs -l cronjob-name=backup -n ops
```

**Output:**
```
job.batch "backup-29223480" deleted
```

**Common mistakes:**
- Deleting CronJob does not delete active Jobs unless cascade set
- Set `successfulJobsHistoryLimit` to auto-prune

---

## Related Topics

- [Jobs](/kubernetes-handbook/jobs/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/)
