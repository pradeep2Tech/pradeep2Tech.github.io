---
title: "How Is the Software Supply Chain Secured?"
date: 2026-07-09T01:40:00+00:00
draft: false
description: "Secure CI/CD architecture across source control, dependencies, build identity, artifact signing, SBOMs, deployment policy, and provenance."
tags: ["security-architecture", "supply-chain", "cicd", "sbom", "artifact-signing", "provenance"]
categories: ["Security Architecture"]
shortTitle: "Supply Chain"
---

## 1. Production Problem

Production security is lost if malicious code enters before runtime. Attackers target dependencies, CI tokens, build runners, package registries, container images, deployment credentials, and release approvals.

## 2. Why Existing Approaches Failed

Manual code review failed to detect dependency substitution and compromised build scripts. Long-lived CI secrets failed because one pipeline leak became production deploy access. Unsigned images failed because clusters could not prove what built them. Scanner-only gates failed because teams ignored noisy results without ownership.

## 3. Architecture Evolution

Secure delivery moved toward least-privilege CI identity, ephemeral build credentials, reproducible builds, dependency pinning, SBOMs, artifact signing, provenance, admission checks, and protected promotion workflows.

```mermaid
flowchart LR
    Code[Source Control] --> Build[Isolated Build Runner]
    Build --> Test[Security and Quality Gates]
    Test --> Sign[Sign Artifact and Generate SBOM]
    Sign --> Registry[Artifact Registry]
    Registry --> Admission[Cluster Admission]
    Admission --> Prod[Production Runtime]
```

## 4. Complete Request Flow

A payment service change is merged. Branch protection requires review and passing checks. CI runs in an isolated runner with short-lived credentials. Dependencies are pinned and scanned. The image is built, signed, and pushed with provenance. Kubernetes admission accepts only signed images from approved registries built by approved pipelines.

## 5. Production Architecture

Separate build, deploy, and runtime permissions. CI can build artifacts; deploy automation can promote approved artifacts; workloads run with separate runtime identities. Protect package registries and base images as production dependencies.

## 6. Kubernetes Implementation

Use admission policy to require signed images, approved registries, immutable tags or digests, vulnerability thresholds, and required metadata. Avoid letting application teams deploy arbitrary images directly to production namespaces.

## 7. Cloud Implementation

Use cloud OIDC federation for CI instead of static deploy keys. Store artifacts in managed registries with immutability and scanning. Log artifact promotion and deployment events. Separate cloud roles for build, deploy, and runtime.

## 8. Production Debugging

For an unknown production image, inspect image digest, signature, provenance, registry event, CI run, source commit, dependency lockfile, and deployment actor. For a dependency incident, identify affected SBOMs, deployed versions, exploitability, reachable services, and rollback/promote path.

## 9. Failure Scenarios

CI token can push directly to production registry and deploy. Base image is compromised and silently inherited by many services. Admission allows unsigned emergency images permanently. Dependency scanner blocks critical releases with noisy false positives and gets disabled.

## 10. Tradeoffs

Strict gates improve assurance but can slow emergency response. Signing and provenance add complexity but make production state explainable. Scanner severity must be paired with reachability and ownership.

## 11. Interview Questions

How do you prove a production image came from approved source?

Why should CI use short-lived cloud credentials?

What is the role of SBOMs during incident response?

How would you design emergency release exceptions safely?

## 12. Common Misconceptions

"Security starts after deployment." Many compromises enter through code and build systems.

"A private registry is enough." You still need identity, signing, provenance, and admission.

"Scanners secure the supply chain." Architecture decides whether findings are enforced and traceable.
