# Architecture Discovery — Template Selection Guide

**Status:** Phase 6 authoring standard  
**Date:** 2026-08-04

## Select the template by reader outcome

| Template | Use when the reader must | Archetype kind |
|---|---|---|
| Tutorial | Perform a bounded activity and produce a validated output | `architecture-discovery-tutorial` |
| Concept | Understand one architectural question or mental model | `architecture-discovery-concept` |
| Architecture Pattern | Apply a repeatable discovery or governance solution | `architecture-discovery-architecture-pattern` |
| Checklist | Verify readiness, coverage, or completion | `architecture-discovery-checklist` |
| Case Study | Follow an end-to-end enterprise scenario and its decisions | `architecture-discovery-case-study` |
| Decision Record | Record one consequential decision and its evidence | `architecture-discovery-decision-record` |
| Technology Comparison | Evaluate options against a specific enterprise context | `architecture-discovery-technology-comparison` |
| Interview Question | Assess discovery judgment through a scenario and rubric | `architecture-discovery-interview-question` |
| Cheat Sheet | Retrieve essential prompts and quality gates on one page | `architecture-discovery-cheat-sheet` |
| Workshop | Facilitate a timeboxed session that produces a decision or artifact | `architecture-discovery-workshop` |

## Create a page

Use Hugo's archetype kind explicitly:

```powershell
hugo new --kind architecture-discovery-concept content/architecture-discovery/discovery-framework/example-topic.md
```

Keep the generated page as `draft: true` until its evidence, links, Mermaid diagrams, metadata, and review checks pass.

## Shared front matter contract

Every article must define:

- `title`, `date`, `draft`, and `description`
- `tags`, `categories`, and `shortTitle`
- `contentType` matching one template in this guide
- `difficulty` and `estimatedReadingTime`
- `interviewImportance` and `enterpriseImportance`
- `prerequisites` and `dependencies`

Use `cheatSheet: true` only for intentionally flat, scan-first pages. Use `interviewHandbook: true` for interview exercises.

## Shared content contract

Every explanatory article must include or deliberately mark as not applicable:

1. enterprise context or business problem
2. motivation and architectural question
3. model, workflow, or architecture
4. evidence and validation
5. practical enterprise example
6. tradeoffs
7. failure modes or anti-patterns
8. architecture review notes
9. interview questions or assessment prompts
10. summary and contextual cross-references

Templates may rename these sections to suit their reader outcome. Do not append empty boilerplate sections merely to satisfy the list.

## Existing presentation components

Use fenced Mermaid diagrams directly. The site supplies rendering, zoom, and lightbox behavior.

Use existing shortcodes where they improve comprehension:

| Need | Existing shortcode |
|---|---|
| Note, recommendation, or risk | `note`, `tip`, `warning` |
| Decision emphasis | `decision-card` |
| Structured comparison | `comparison-table` |
| Benefits and costs | `pros-cons` |
| Interview response | `interview-answer` |
| Technology suitability | `technology-fit` |

Do not create a new shortcode when a table, Mermaid diagram, or existing component expresses the information clearly.

## Template quality gate

- The chosen template matches the reader's intended outcome.
- The page answers one architectural question.
- Claims are evidence-backed or explicitly labeled assumptions.
- Tables and diagrams clarify real relationships rather than decorate the page.
- Cross-links point to canonical implementation guidance instead of duplicating it.
- Metadata matches the approved content roadmap.
- Empty prompts and template comments are removed before publication.

