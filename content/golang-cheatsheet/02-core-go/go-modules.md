---
title: "Go Modules"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "go.mod, go.sum, module path, replace, and workspace mode."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Modules"
module: 2
moduleTitle: "Core Go"
sectionRef: "2.4"
weight: 204
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/go-modules/"
---

## At a Glance

- **Go modules** are the unit of dependency versioning since Go 1.16+. Defined by **`go.mod`** at module root; checksums in **`go.sum`**.

---

## Reference Tables

| File | Role |
| :--- | :--- |
| `go.mod` | Module path, Go version, require/replace/exclude |
| `go.sum` | Cryptographic checksums of module contents |
| `go.work` | Multi-module workspace (local dev) |

| Directive | Purpose |
| :--- | :--- |
| `module` | Import path prefix |
| `require` | Dependencies |
| `replace` | Local fork or vanity redirect |
| `retract` | Withdraw bad versions |

```bash
go mod init example.com/myapp
go mod tidy
go mod verify
go mod graph
```

For **MVS**, `go get`, and vendoring, see [Dependency Management](/golang-cheatsheet/02-core-go/dependency-management/).

---

## Snippets

```go
module github.com/org/project

go 1.22

require (
    github.com/lib/pq v1.10.9
)
```

---

## Internals & Gotchas

- Commit `go.sum` — required for reproducible builds.
- Major version `/v2` in module path for v2+ APIs.
- `replace` in go.mod is local-only — don't rely in published libraries.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

## How do you version Go in go.mod and Docker images consistently?

### Short Answer
go.mod defines module path and requirements; MVS picks minimum compatible versions; commit go.sum for reproducibility.

### Detailed Explanation
Modules replaced GOPATH for dependency management. replace is for local dev; retract withdraws bad versions. Vendoring supports hermetic CI.

### Internal Working
The module graph is resolved with minimal version selection — not latest-wins. Major versions v2+ require /v2 in module path.

### Production Notes
Pin Go toolchain in go.mod and Docker. Use GOPRIVATE for internal modules. Run go mod verify in CI.

### Common Mistakes
Committing replace directives meant for local forks. Using go get -u blindly in libraries. Omitting go.sum from VCS.

### Follow-up Questions
How does MVS behave when two modules require different minimum versions of the same dependency?

---
## What is the policy for retract directives after publishing a bad module version?

### Short Answer
go.mod defines module path and requirements; MVS picks minimum compatible versions; commit go.sum for reproducibility.

### Detailed Explanation
Modules replaced GOPATH for dependency management. replace is for local dev; retract withdraws bad versions. Vendoring supports hermetic CI.

### Internal Working
The module graph is resolved with minimal version selection — not latest-wins. Major versions v2+ require /v2 in module path.

### Production Notes
Pin Go toolchain in go.mod and Docker. Use GOPRIVATE for internal modules. Run go mod verify in CI.

### Common Mistakes
Committing replace directives meant for local forks. Using go get -u blindly in libraries. Omitting go.sum from VCS.

### Follow-up Questions
How does MVS behave when two modules require different minimum versions of the same dependency?

---
<!-- interview-answers:end -->

---

## How do you version Go in go.mod and Docker images consistently?

### Short Answer
The architecturally sound response is go.mod/go.sum, MVS resolution, vendoring, GOPRIVATE — for: How do you version Go in go.mod and Docker images consistently.

### Detailed Explanation
Explain semver import paths (/v2), retract, and verify in CI for: How do you version Go in go.mod and Docker images consistently.

### Internal Working
MVS picks minimum compatible versions across the module graph — internal rule for: How do you version Go in go.mod and Docker images consistently.

### Production Notes
Pin toolchain; never commit local replace forks for: How do you version Go in go.mod and Docker images consistently.

### Common Mistakes
Omitting go.sum or blind `go get -u` in libraries hurts: How do you version Go in go.mod and Docker images consistently.

### Follow-up Questions
How would MVS resolve a conflicting requirement in: How do you version Go in go.mod and Docker images consistently?

---
## What is the policy for retract directives after publishing a bad module version?

### Short Answer
The mechanism-first explanation is go.mod/go.sum, MVS resolution, vendoring, GOPRIVATE — for: What is the policy for retract directives after publishing a bad module version.

### Detailed Explanation
Explain semver import paths (/v2), retract, and verify in CI for: What is the policy for retract directives after publishing a bad module version.

### Internal Working
MVS picks minimum compatible versions across the module graph — internal rule for: What is the policy for retract directives after publishing a bad module version.

### Production Notes
Pin toolchain; never commit local replace forks for: What is the policy for retract directives after publishing a bad module version.

### Common Mistakes
Omitting go.sum or blind `go get -u` in libraries hurts: What is the policy for retract directives after publishing a bad module version.

### Follow-up Questions
How would MVS resolve a conflicting requirement in: What is the policy for retract directives after publishing a bad module version?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Packages](/golang-cheatsheet/02-core-go/packages/)
- [Next: Dependency Management](/golang-cheatsheet/02-core-go/dependency-management/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
