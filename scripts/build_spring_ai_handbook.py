"""Build the compact Spring AI interview handbook from the source XLSX."""

from __future__ import annotations

import json
import re
import shutil
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"C:\Users\maggi\Downloads\spring_ai.xlsx")
OUT = (ROOT / "content" / "spring-ai").resolve()

SOURCE_GROUPS = [
    ("llm", 10), ("rag", 20), ("spring", 20), ("agent", 25),
    ("safety", 25), ("multi", 20), ("enterprise", 20), ("interview", 30),
]

TOPICS = [
    ("llm-foundations", "LLM Foundations", "How models generate, use context, represent meaning and differ from retrieval or agents.", ["llm"], "foundations"),
    ("production-prompt-engineering", "Production Prompt Engineering", "Prompt design as a versioned, testable engineering discipline rather than ad hoc wording.", [], "prompting"),
    ("rag-pipeline", "RAG Pipeline", "Ingestion, parsing, chunking, embeddings, retrieval, grounding and citations.", ["rag"], "pipeline"),
    ("retrieval-quality-lifecycle", "Retrieval Quality & Lifecycle", "Search quality, metadata, reranking, evaluation, updates, deletion and tenant isolation.", ["rag"], "retrieval"),
    ("spring-ai-core", "Spring AI Core", "Portable model access, Advisors, memory, structured output, streaming and provider integration.", ["spring"], "spring"),
    ("tools-and-agents", "Tools & Agent Execution", "Tool selection, controlled execution, agent loops and the boundary between agents and workflows.", ["agent", "spring"], "tools"),
    ("agent-state-and-reliability", "Agent State & Reliability", "State, idempotency, timeouts, termination, recovery, testing and debugging.", ["agent"], "reliability"),
    ("security-and-guardrails", "Security & Guardrails", "Prompt injection, data protection, authorization, grounding and safe business actions.", ["safety"], "security"),
    ("production-operations", "Production Operations", "Resilience, observability, evaluation, latency, rate limits, provider changes and cost.", ["safety", "enterprise"], "operations"),
    ("multi-agent-systems", "Multi-Agent Systems", "Coordination patterns, communication, memory boundaries, conflict and complexity trade-offs.", ["multi"], "multi"),
    ("enterprise-platform", "Enterprise Agentic AI Platform", "A scalable, governed platform combining IAM, model routing, RAG, tools, state and recovery.", ["enterprise"], "platform"),
    ("production-use-cases", "Production Agentic AI Use Cases", "Ten production use cases showing where agents add value, how they are controlled, and how success is measured.", [], "use-cases"),
]

USE_CASES = [
    {
        "title": "Enterprise Knowledge Agent",
        "problem": "Employees lose time searching fragmented policies, procedures and technical knowledge.",
        "why": "The request often requires clarification, retrieval across sources and synthesis; use plain RAG when no action or iterative search is needed.",
        "architecture": "User --> API/IAM --> Agent --> Authorized retrieval --> Model --> Cited answer",
        "rag": "Hybrid retrieval over versioned chunks with mandatory tenant/ACL filters, reranking and claim-level citations.",
        "tools": "Search, document metadata, source preview and access-request workflow; keep write tools out by default.",
        "execution": "Classify intent, derive security scope, retrieve, rerank, answer only from evidence and return citations or abstain.",
        "failure": "On weak retrieval, ask a clarifying question or abstain; preserve the source/index version for diagnosis.",
        "security": "Document ACLs are enforced during retrieval; prompt-provided identity or tenant values are ignored.",
        "observability": "Trace parsing, retrieval, reranking and generation; record scores, citations, latency and token usage without logging sensitive content.",
        "evaluation": "Retrieval recall, citation correctness, faithfulness, answer correctness, abstention quality and search-time reduction.",
        "challenges": "Stale documents, inconsistent permissions, duplicate content, poor scans and answers synthesized from conflicting policies.",
    },
    {
        "title": "IT / Developer Agent",
        "problem": "Engineering work is distributed across tickets, repositories, documentation, CI systems and operational tools.",
        "why": "Multi-step investigation and bounded actions benefit from tool selection; deterministic automation remains preferable for known runbooks.",
        "architecture": "Developer --> Agent --> Jira/Confluence retrieval --> Git/CI tools --> Review or action",
        "rag": "Index architecture docs, runbooks and resolved incidents with repository, service, branch and permission metadata.",
        "tools": "Jira, Git, Confluence, code search, build and CI status; mutations require scoped credentials and confirmation.",
        "execution": "Build an evidence set, propose a plan, invoke read tools, generate a patch or ticket update, then require review before mutation.",
        "failure": "Sandbox builds, cap iterations, retain tool output and distinguish failed execution from an unknown mutation outcome.",
        "security": "Use short-lived user-delegated credentials, repository allow-lists, branch protection, secret scanning and approval gates.",
        "observability": "Correlate model decisions, queries, diffs, build results and approvals using one task ID.",
        "evaluation": "Issue-resolution rate, accepted suggestions, build/test pass rate, unsafe-action rate, latency and engineer time saved.",
        "challenges": "Large repositories, stale documentation, generated insecure code, excessive permissions and non-reproducible tool environments.",
    },
    {
        "title": "Incident / Operations Agent",
        "problem": "Responders must correlate alerts, telemetry, deployments and runbooks under severe time pressure.",
        "why": "Iterative hypothesis testing across tools adds value, but remediation should remain policy-controlled and deterministic.",
        "architecture": "Alert --> Incident state --> Telemetry tools --> Hypothesis loop --> Approved remediation",
        "rag": "Retrieve service topology, runbooks, past incidents and change records scoped to the affected environment.",
        "tools": "Logs, metrics, traces, deployment history, feature flags and remediation workflows; begin read-only.",
        "execution": "Create an incident timeline, test ranked hypotheses, recommend a runbook step and execute only pre-approved bounded actions.",
        "failure": "Stop on conflicting evidence, missing telemetry or tool timeout; preserve state and escalate to the incident commander.",
        "security": "Separate diagnosis from remediation roles, use break-glass approval and prohibit free-form shell execution.",
        "observability": "Record every query, hypothesis, evidence link, proposed action, approval and resulting system signal.",
        "evaluation": "Diagnosis accuracy, false-action rate, MTTA/MTTR, escalation quality and percentage of recommendations accepted.",
        "challenges": "Noisy alerts, partial telemetry, cascading failures, stale runbooks and the high cost of a confident wrong action.",
    },
    {
        "title": "Customer Support Agent",
        "problem": "Support teams need consistent answers plus customer-specific context and ticket actions.",
        "why": "The agent can combine grounded knowledge with authorized customer APIs and choose the next support action.",
        "architecture": "Customer --> Support API --> Knowledge RAG + Customer API --> Ticket tools --> Response",
        "rag": "Retrieve approved product documentation, policies and known issues with product/version/locale filters and citations.",
        "tools": "Customer profile, order/subscription status, ticket creation, escalation and approved remediation actions.",
        "execution": "Authenticate, classify intent, retrieve policy, fetch minimum customer data, propose or perform an allowed action and update the ticket.",
        "failure": "Do not guess account facts; degrade to general guidance or human handoff while carrying evidence and conversation state.",
        "security": "Apply customer-resource authorization, PII minimization, redacted telemetry and separate permissions for refunds or account changes.",
        "observability": "Measure retrieval, API/tool latency, handoffs, policy citations, mutations and customer-visible failures.",
        "evaluation": "Resolution rate, answer correctness, containment, CSAT, policy compliance, escalation precision and unsafe-action rate.",
        "challenges": "Identity verification, emotional users, policy changes, multilingual content and adversarial attempts to obtain account data.",
    },
    {
        "title": "Requirement / BRD Agent",
        "problem": "Business requirements arrive as incomplete, inconsistent documents and conversations.",
        "why": "Iterative clarification and synthesis help, while the final artifact needs a deterministic schema and human ownership.",
        "architecture": "Sources --> Extraction/RAG --> Clarification agent --> Structured BRD --> Validation/review",
        "rag": "Retrieve domain standards, existing capabilities, glossary terms and prior approved requirements with provenance.",
        "tools": "Document ingestion, stakeholder directory, requirement repository, glossary and review workflow.",
        "execution": "Extract facts, identify gaps/conflicts, ask targeted questions, generate structured requirements and run rule-based validation.",
        "failure": "Mark unsupported assumptions, retain unresolved conflicts and block publication when mandatory sections or approvals are missing.",
        "security": "Respect project confidentiality, stakeholder access and retention rules; isolate customer and program data.",
        "observability": "Track source-to-requirement lineage, clarification cycles, validation failures and reviewer edits.",
        "evaluation": "Completeness, ambiguity and conflict rates, traceability coverage, reviewer acceptance and downstream change requests.",
        "challenges": "Tacit knowledge, contradictory stakeholders, false precision and treating generated text as approved scope.",
    },
    {
        "title": "Contract Intelligence Agent",
        "problem": "Legal and procurement teams must locate clauses, compare obligations and identify risk across heterogeneous contracts.",
        "why": "The work combines extraction, retrieval and bounded analysis, but legal conclusions require expert review.",
        "architecture": "Contract --> OCR/layout extraction --> Clause index --> Analysis agent --> Legal review",
        "rag": "Use layout-aware clause chunks, document/version/page metadata, approved playbooks and exact citation spans.",
        "tools": "OCR, document parser, clause classifier, comparison engine, obligation register and review workflow.",
        "execution": "Validate extraction quality, classify clauses, retrieve policy, compare deviations, cite text and route material risks to counsel.",
        "failure": "Surface unreadable pages and low-confidence extraction; never silently analyze missing schedules or signatures.",
        "security": "Encrypt documents, enforce matter-level access, restrict provider retention and maintain immutable access/audit records.",
        "observability": "Trace page extraction, clause boundaries, evidence, policy versions, reviewer overrides and export actions.",
        "evaluation": "Clause extraction recall, citation accuracy, deviation precision/recall, missed-risk rate and reviewer agreement.",
        "challenges": "Scans, tables, cross-references, amendments, jurisdiction differences and unauthorized-legal-advice risk.",
    },
    {
        "title": "Data / SQL Agent",
        "problem": "Users need governed access to analytical data without manually writing SQL.",
        "why": "The model can interpret intent and select datasets, but SQL execution must pass deterministic controls.",
        "architecture": "Question --> Semantic catalog --> SQL generation --> Policy/SQL validation --> Read replica --> Result",
        "rag": "Retrieve schema, metric definitions, join rules, ownership and approved query patterns rather than raw business rows.",
        "tools": "Catalog search, SQL parser, query planner/cost estimator, read-only database executor and visualization service.",
        "execution": "Resolve metrics, generate SQL, parse and authorize every relation/column, estimate cost, execute with limits and summarize results.",
        "failure": "Reject ambiguous metrics, unsafe SQL or excessive plans; cancel on deadline and expose validation errors for correction.",
        "security": "Use read-only identities, row/column policies, tenant predicates, query allow-lists, masking and result-size limits.",
        "observability": "Capture normalized SQL fingerprints, datasets, policy decisions, query cost, latency and result cardinality—not sensitive row data.",
        "evaluation": "SQL execution accuracy, metric correctness, policy violations, query cost, clarification rate and analyst acceptance.",
        "challenges": "Semantic ambiguity, schema drift, expensive queries, inference attacks and convincing summaries of incorrect aggregates.",
    },
    {
        "title": "Enterprise Workflow Agent",
        "problem": "Knowledge-heavy processes need flexible interpretation but dependable execution and audit.",
        "why": "Use the agent for classification and next-best-action proposals; use a workflow engine for durable deterministic transitions.",
        "architecture": "Request --> Agent decision --> Policy gate --> Workflow engine --> Tasks/events --> Agent",
        "rag": "Retrieve policies, case history and task instructions using case and tenant authorization.",
        "tools": "Workflow start/signal, task lookup, document service, notification and human-approval queue.",
        "execution": "The agent proposes a typed command; policy validates it; the workflow executes, checkpoints and returns events for the next decision.",
        "failure": "Workflow retries and compensation own operational recovery; the agent must not improvise transaction semantics.",
        "security": "Authorize every workflow command, bind it to case state and principal, and require approval for sensitive transitions.",
        "observability": "Link model/tool spans to workflow instance, state transitions, timers, retries, compensation and approvals.",
        "evaluation": "Completion rate, exception/escalation rate, invalid transition attempts, cycle time and human rework.",
        "challenges": "Long-running state, version migrations, duplicate events, human delays and unclear ownership between agent and workflow.",
    },
    {
        "title": "Transaction Agent",
        "problem": "Users want conversational initiation of high-value business operations such as payments, refunds or orders.",
        "why": "The agent may gather intent and required fields, but authorization and transaction execution must be deterministic.",
        "architecture": "Intent --> Agent proposal --> Validation/IAM --> Approval --> Idempotent transaction API --> Receipt",
        "rag": "Retrieve product rules and policies only; authoritative balances, limits and transaction state come from APIs.",
        "tools": "Quote/preview, beneficiary or order lookup, approval, transaction submission, status and reconciliation.",
        "execution": "Resolve intent, produce a preview, validate limits and authorization, obtain confirmation/approval, execute once and reconcile outcome.",
        "failure": "Treat timeout after submission as unknown state; query by idempotency key before retrying and escalate unresolved outcomes.",
        "security": "Use step-up authentication, segregation of duties, transaction signing, amount/resource policies and immutable audit.",
        "observability": "Record proposal, policy decision, confirmation, idempotency key, API result and reconciliation without exposing secrets.",
        "evaluation": "Successful authorized completion, duplicate rate, fraud/policy violations, abandonment, reconciliation time and false declines.",
        "challenges": "Ambiguous intent, social engineering, irreversible side effects, regulatory evidence and provider/tool partial failure.",
    },
    {
        "title": "Multi-Agent Research Agent",
        "problem": "Complex research requires independent collection, analysis and critique across domains or data sources.",
        "why": "Specialists can work in parallel when tasks are genuinely separable; a single agent is cheaper for tightly coupled research.",
        "architecture": "Research question --> Supervisor --> Parallel specialists --> Evidence store --> Aggregator/critic",
        "rag": "Each specialist retrieves from an authorized domain corpus; evidence retains source, time, scope and confidence metadata.",
        "tools": "Search, data-source connectors, document readers, calculators and citation validator with per-agent allow-lists.",
        "execution": "Supervisor creates bounded tasks, specialists return structured claims/evidence, a critic checks conflicts and aggregation produces the report.",
        "failure": "Cap fan-out/hops, tolerate partial results, detect circular delegation and escalate unresolved evidence conflicts.",
        "security": "Give each agent its own identity and least-privilege tools; do not expose shared memory across tenants or incompatible domains.",
        "observability": "Trace the task graph, messages, retrieval, tools, tokens, evidence lineage, conflicts and aggregation decisions.",
        "evaluation": "Evidence coverage, citation/claim correctness, contradiction detection, task success, latency and cost versus a single-agent baseline.",
        "challenges": "Coordination overhead, duplicated work, context pollution, nondeterministic synthesis and cost without quality gain.",
    },
]

PROMPT_QUESTIONS = [
    ("How do you structure a production system prompt?", "Critical", "Define role and objective, non-negotiable policy, allowed data and tools, response contract, abstention rules and conflict handling. Keep stable policy separate from request-specific content."),
    ("How do system, user, retrieved context and tool instructions differ?", "Critical", "System instructions define application policy; user content expresses intent; retrieved content is untrusted evidence; tool descriptions define capabilities, not authorization. Preserve this precedence in prompt assembly and execution."),
    ("How do you prevent retrieved content from overriding system instructions?", "Critical", "Delimit and label retrieved text as data, strip active markup where practical, instruct the model not to execute embedded directions, minimize exposed tools and enforce authorization outside the model."),
    ("How do you design prompts for structured output?", "Critical", "Use a narrow typed schema with field semantics and constraints, request no extra prose, then parse and validate the result as untrusted input. Retry only bounded correctable failures."),
    ("When should you use few-shot versus zero-shot prompting?", "Medium", "Start zero-shot when instructions and schema are sufficient. Add a small representative set of examples when format, classification boundaries or edge-case behavior remain ambiguous; measure the token and anchoring cost."),
    ("How do you version and test prompts?", "Critical", "Store prompts as reviewed artifacts with semantic versions and dependencies on model, tools, schema and retrieval strategy. Run unit checks, golden scenarios, adversarial cases and online canaries before promotion."),
    ("How do you prevent prompt drift during model upgrades?", "Critical", "Pin prompt-model combinations, compare old and new behavior on a frozen evaluation set, inspect tool and structured-output compatibility, canary by risk tier and retain immediate rollback."),
    ("How do you optimize a prompt without degrading quality?", "Critical", "Establish a quality and safety baseline first, remove redundant tokens incrementally, evaluate each change across representative and adversarial cases, and optimize cost or latency only within explicit quality guardrails."),
]

def workbook_rows(path: Path) -> list[dict[str, str]]:
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rel_ns = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    with zipfile.ZipFile(path) as z:
        workbook = ET.fromstring(z.read("xl/workbook.xml"))
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels}
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            strings = ET.fromstring(z.read("xl/sharedStrings.xml"))
            shared = ["".join(t.text or "" for t in si.findall(".//m:t", ns)) for si in strings.findall("m:si", ns)]
        sheet = next(iter(workbook.find("m:sheets", ns)))
        target = targets[sheet.attrib[f"{{{rel_ns}}}id"]]
        target = target if target.startswith("xl/") else "xl/" + target.lstrip("/")
        xml = ET.fromstring(z.read(target))
        rows = []
        for row in xml.findall(".//m:sheetData/m:row", ns):
            values = {}
            for cell in row.findall("m:c", ns):
                col = re.match(r"[A-Z]+", cell.attrib["r"]).group()
                inline, value = cell.find("m:is", ns), cell.find("m:v", ns)
                if inline is not None:
                    text = "".join(t.text or "" for t in inline.findall(".//m:t", ns))
                elif value is None:
                    text = ""
                elif cell.attrib.get("t") == "s":
                    text = shared[int(value.text)]
                else:
                    text = value.text or ""
                values[col] = text.strip()
            rows.append(values)
        return rows

def parse_items(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    headers = [i for i, row in enumerate(rows) if row.get("A") == "#"]
    items = []
    for index, (source_group, expected) in enumerate(SOURCE_GROUPS):
        start = headers[index] + 1
        end = headers[index + 1] if index + 1 < len(headers) else len(rows)
        numbered, followups = [], []
        for row in rows[start:end]:
            if source_group == "interview" and row.get("A", "").isdigit():
                numbered.append((row["A"], row.get("C", ""), row.get("D", ""), row.get("E", "")))
            elif source_group != "interview" and row.get("A", "").isdigit():
                numbered.append((row["A"], row.get("B", ""), row.get("C", ""), row.get("D", "")))
            elif source_group != "interview" and row.get("B") and row.get("C") and row.get("B") != "Area":
                followups.append((f"F{len(followups)+1}", row["C"], row["B"], "Follow-up"))
        if len(numbered) != expected:
            raise ValueError(f"{source_group}: expected {expected}, found {len(numbered)}")
        for kind, records in (("numbered", numbered), ("follow-up", followups)):
            for number, question, areas, priority in records:
                items.append({
                    "sourceGroup": source_group,
                    "sourceType": kind,
                    "sourceNumber": number,
                    "question": question,
                    "keyAreas": areas,
                    "priority": priority.replace("🔴 ", "").replace("🟡 ", ""),
                })
    if len(items) != 190:
        raise ValueError(f"Expected 190 prompts, found {len(items)}")
    return items

def select_topic(item: dict[str, str]) -> str:
    group = item["sourceGroup"]
    text = (item["question"] + " " + item["keyAreas"]).lower()
    if group == "rag":
        return "retrieval-quality-lifecycle" if any(x in text for x in ("quality", "top-k", "metadata", "rerank", "hybrid", "update", "deletion", "tenant", "evaluate", "failure", "monitor", "latency")) else "rag-pipeline"
    if group == "spring":
        return "tools-and-agents" if "tool" in item["question"].lower() else "spring-ai-core"
    if group == "agent":
        return "agent-state-and-reliability" if any(x in text for x in ("fail", "timeout", "loop", "duplicate", "state", "observe", "test", "cost", "provider")) else "tools-and-agents"
    if group == "safety":
        return "production-operations" if any(x in text for x in ("provider", "rate", "timeout", "observ", "evaluate", "cost", "version", "degrading")) else "security-and-guardrails"
    if group == "enterprise":
        return "production-operations" if any(x in text for x in ("scale", "long-running", "observ", "debug", "cost", "deploy", "disaster")) else "enterprise-platform"
    if group == "interview":
        if any(x in text for x in ("rag", "chunk", "retrieval", "document", "vector")):
            return "retrieval-quality-lifecycle"
        if "spring ai" in text:
            return "spring-ai-core"
        if any(x in text for x in ("multi-agent", "supervisor")):
            return "multi-agent-systems"
        if any(x in text for x in ("tool", "agent execution", "infinite agent")):
            return "agent-state-and-reliability" if any(x in text for x in ("timeout", "invalid", "infinite")) else "tools-and-agents"
        if any(x in text for x in ("prompt injection", "sensitive", "hallucinated business", "protect")):
            return "security-and-guardrails"
        if any(x in text for x in ("429", "unavailable", "latency", "cost", "fallback")):
            return "production-operations"
        if any(x in text for x in ("platform", "concurrent", "architecture", "conventional software")):
            return "enterprise-platform"
        return "llm-foundations"
    return {"llm": "llm-foundations", "multi": "multi-agent-systems"}[group]

def flow(kind: str) -> str:
    diagrams = {
        "pipeline": """flowchart LR
    S[Sources] --> P[Parse and chunk] --> E[Embed] --> V[(Vector index)]
    Q[Question] --> R[Authorized retrieval] --> C[Grounded context] --> M[Model] --> A[Cited answer]
    V --> R""",
        "retrieval": """flowchart LR
    Q[Query] --> H[Hybrid retrieval] --> F[Security filters] --> K[Candidate set]
    K --> RR[Rerank] --> T{Relevant?}
    T -->|yes| C[Bounded context]
    T -->|no| N[Abstain or clarify]""",
        "spring": """flowchart LR
    API[API] --> S[Application service] --> C[ChatClient]
    C --> A[Advisors] --> M[ChatModel]
    A --> V[VectorStore]
    A --> MEM[Chat memory]
    M --> O[Validated response]""",
        "tools": """flowchart LR
    U[Request] --> O[Orchestrator] --> L[Model chooses action]
    L --> G{Authorize and validate}
    G -->|allow| T[Execute tool]
    G -->|deny| X[Stop safely]
    T --> R[Record result] --> O""",
        "reliability": """flowchart LR
    R[Request] --> B[Load state and budgets] --> A[Next action]
    A --> D{Duplicate or over budget?}
    D -->|yes| S[Terminate or escalate]
    D -->|no| E[Idempotent execution] --> C[(Checkpoint)] --> A""",
        "security": """flowchart LR
    I[Untrusted input] --> IG[Input policy] --> R[Authorized retrieval]
    R --> M[Model]
    M --> OG[Output validation]
    M --> TG[Tool authorization]
    TG --> T[Audited action]""",
        "operations": """flowchart LR
    A[Admission control] --> O[Orchestration] --> G[Model gateway]
    G --> P[Primary provider]
    G --> F[Compatible fallback]
    O -. traces and metrics .-> OT[OpenTelemetry]
    OT --> E[Quality and cost evaluation]""",
        "multi": """flowchart TD
    Q[Task] --> S[Supervisor]
    S --> A[Specialist A]
    S --> B[Specialist B]
    A --> R[(Scoped state)]
    B --> R
    R --> D[Deterministic aggregation] --> O[Result]""",
        "platform": """flowchart LR
    API[API, IAM and quotas] --> OR[Orchestration]
    OR --> MG[Model gateway]
    OR --> RAG[RAG with tenant filters]
    OR --> T[Authorized tools]
    OR --> S[(Workflow state)]
    OR -. telemetry .-> EV[Evaluation and governance]""",
        "architecture": """flowchart TD
    B[Business outcome] --> T[Trust boundaries] --> C[Component decisions]
    C --> F[Failure and recovery] --> S[Scale and operations]
    S --> E[Evidence: SLO, quality, cost and audit]""",
        "incidents": """flowchart LR
    D[Detect] --> C[Classify failing segment] --> P[Protect capacity]
    P --> R[Recover with tested path] --> X[Reconcile state]
    X --> L[Add regression and runbook]""",
    }
    return diagrams.get(kind, "flowchart LR\n    I[Input] --> C[Controlled processing] --> O[Validated output]")

def takeaway(item: dict[str, str]) -> str:
    areas = item["keyAreas"].rstrip(".")
    q = item["question"].lower()
    if any(x in q for x in ("when should", "when would you reject", "why shouldn't")):
        return f"Choose the simpler deterministic design unless {areas} provide measurable value that justifies AI risk and operating cost."
    if any(x in q for x in ("secure", "protect", "prevent unauthorized", "multi-tenant")):
        return f"Enforce {areas} in deterministic application and data boundaries; never trust the prompt or model to supply security context."
    if any(x in q for x in ("failure", "fails", "timeout", "429", "unavailable", "degrading", "slow", "increased")):
        return f"Bound, observe and classify the failure; protect capacity, recover through an idempotent tested path, then verify {areas}."
    if any(x in q for x in ("evaluate", "prove", "test")):
        return f"Use versioned representative scenarios and measure {areas}; compare against a baseline and retain failures as regressions."
    if any(x in q for x in ("design", "architecture", "walk me through", "flow")):
        return f"Make {areas} explicit as independently observable components with clear trust, state and failure boundaries."
    return f"Connect {areas}; define the contract, limits, measurement and safe failure behavior for the complete path."

def page(title: str, description: str, items: list[dict[str, str]], kind: str) -> str:
    rows = []
    for item in items:
        label = "Follow-up" if item["sourceType"] == "follow-up" else item["priority"]
        rows.append(f"| {item['question'].replace('|', '\\|')} | {takeaway(item).replace('|', '\\|')} | {label} |")
    return f'''---
title: {json.dumps(title)}
date: 2026-08-22T00:00:00+05:30
draft: false
description: {json.dumps(description)}
tags: ["spring-ai", "genai", "interview-preparation"]
categories: ["Spring AI"]
interviewHandbook: true
---

{description}

## Core Flow

```mermaid
{flow(kind)}
```

## Revision Map

| Question | What a strong answer should establish | Priority |
|---|---|---|
{chr(10).join(rows)}

## Interview Lens

Keep probabilistic interpretation separate from authorization, policy, transactions and recovery. Explain trade-offs with evidence: task quality, latency, resilience, security, operating cost and auditability.
'''

def use_case_page() -> str:
    sections = []
    for index, case in enumerate(USE_CASES, 1):
        nodes = [part.strip() for part in case["architecture"].split("-->")]
        graph = ["flowchart LR"]
        for node_index, label in enumerate(nodes):
            safe = label.replace('"', "'")
            graph.append(f'    N{node_index}["{safe}"]')
            if node_index:
                graph.append(f"    N{node_index-1} --> N{node_index}")
        rows = [
            ("Business problem", case["problem"]),
            ("Why an agent?", case["why"]),
            ("RAG", case["rag"]),
            ("Tools", case["tools"]),
            ("Agent execution", case["execution"]),
            ("Failure handling", case["failure"]),
            ("Security", case["security"]),
            ("Observability", case["observability"]),
            ("Evaluation", case["evaluation"]),
            ("Production challenges", case["challenges"]),
        ]
        table = "\n".join(f"| **{label}** | {value} |" for label, value in rows)
        sections.append(f'''## {index}. {case["title"]}

```mermaid
{chr(10).join(graph)}
```

| Dimension | Production design |
|---|---|
{table}
''')
    return f'''---
title: "Production Agentic AI Use Cases"
date: 2026-08-22T00:00:00+05:30
draft: false
description: "Ten production use cases showing where agents add value, how they are controlled, and how success is measured."
tags: ["spring-ai", "agentic-ai", "production-architecture", "use-cases"]
categories: ["Spring AI"]
interviewHandbook: true
---

Use an agent only where interpretation, iterative evidence gathering or dynamic tool selection adds measurable value. Keep authorization, policy, transactions, approvals and recovery deterministic.

{chr(10).join(sections)}
'''

def prompt_engineering_page() -> str:
    rows = "\n".join(f"| {question} | {answer} | {priority} |" for question, priority, answer in PROMPT_QUESTIONS)
    return f'''---
title: "Production Prompt Engineering"
date: 2026-08-22T00:00:00+05:30
draft: false
description: "Prompt design as a versioned, testable engineering discipline rather than ad hoc wording."
tags: ["spring-ai", "prompt-engineering", "llm", "production"]
categories: ["Spring AI"]
interviewHandbook: true
---

Production prompts are application artifacts with contracts, dependencies and regression risk. Prompt wording cannot replace authorization, policy enforcement, schema validation or tool controls.

## Prompt Lifecycle

```mermaid
flowchart LR
    P[System policy] --> A[Prompt assembly]
    U[User intent] --> A
    R[Untrusted retrieved evidence] --> A
    T[Tool capability descriptions] --> A
    A --> M[Versioned model call] --> V[Parse and validate]
    V --> E[Offline evaluation] --> C[Canary] --> O[Observe and promote or roll back]
```

## Revision Map

| Question | What a strong answer should establish | Priority |
|---|---|---|
{rows}

## Production Rule

Version the prompt together with its model, sampling configuration, response schema, available tools and retrieval behavior. Promote changes only when quality, safety, latency and cost remain inside defined acceptance thresholds.
'''

def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(SOURCE)
    if ROOT not in OUT.parents or OUT.name != "spring-ai":
        raise RuntimeError(f"Refusing to replace unexpected path: {OUT}")
    items = parse_items(workbook_rows(SOURCE))
    for item in items:
        item["topic"] = select_topic(item)

    # This directory contains only generated handbook content.
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    topic_map = {slug: (title, description, kind) for slug, title, description, _, kind in TOPICS}
    for slug, title, description, _, kind in TOPICS:
        if slug == "production-use-cases":
            (OUT / f"{slug}.md").write_text(use_case_page(), encoding="utf-8")
            continue
        if slug == "production-prompt-engineering":
            (OUT / f"{slug}.md").write_text(prompt_engineering_page(), encoding="utf-8")
            continue
        # Workbook follow-up prompts overlap the numbered curriculum. Keep them
        # in the audit manifest, but do not repeat them as visible questions.
        selected = [item for item in items if item["topic"] == slug and item["sourceType"] == "numbered"]
        (OUT / f"{slug}.md").write_text(page(title, description, selected, kind), encoding="utf-8")

    (OUT / "_index.md").write_text('''---
title: "Spring AI & Agentic AI Interview Handbook"
date: 2026-08-22T00:00:00+05:30
draft: false
description: "A concise, flow-oriented revision handbook for Spring AI, RAG, agents and production architecture."
tags: ["spring-ai", "genai", "rag", "agentic-ai", "interview-preparation"]
categories: ["Spring AI"]
ShowPageNums: true
---

A compact architect-level handbook organized by topic rather than learning stage. Related interview prompts are consolidated into revision maps, while major execution and architecture ideas are shown as flows.
''', encoding="utf-8")

    module_groups = [
        (1, "Models & Retrieval", ["llm-foundations", "production-prompt-engineering", "rag-pipeline", "retrieval-quality-lifecycle"]),
        (2, "Spring AI & Agents", ["spring-ai-core", "tools-and-agents", "agent-state-and-reliability"]),
        (3, "Production Architecture", ["security-and-guardrails", "production-operations", "multi-agent-systems", "enterprise-platform", "production-use-cases"]),
    ]
    module_lines = ["modules:"]
    order = []
    for module_id, focus, topics in module_groups:
        module_lines += [f"  - id: {module_id}", f"    focus: {json.dumps(focus)}", "    topics:"]
        module_lines += [f"      - {topic}" for topic in topics]
        order.extend(topics)
    (ROOT / "data" / "spring_ai_modules.yaml").write_text("\n".join(module_lines) + "\n", encoding="utf-8")
    (ROOT / "data" / "spring_ai_order.yaml").write_text("topics:\n" + "\n".join(f"  - {topic}" for topic in order) + "\n", encoding="utf-8")
    (ROOT / "data" / "spring_ai_questions.json").write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts = Counter(item["topic"] for item in items)
    report = [
        "SPRING AI HANDBOOK VALIDATION", "", "Source prompts represented: 190/190",
        "Visible numbered questions: 170/170", "Supplemental workbook prompts absorbed into related topics: 20/20",
        f"Consolidated topic pages: {len(TOPICS)}", "Missing prompts: 0", "Accidental duplicate mappings: 0", "",
    ]
    report += [f"{topic_map[slug][0]}: {sum(1 for item in items if item['topic'] == slug and item['sourceType'] == 'numbered')} visible questions" for slug, *_ in TOPICS if slug not in ("production-use-cases", "production-prompt-engineering")]
    report += ["Production Prompt Engineering: 8/8"]
    report += ["Production Agentic AI Use Cases: 10/10"]
    report += ["", "Every source row maps to exactly one topic through data/spring_ai_questions.json; supplemental prompts are not repeated in the visible revision maps."]
    (ROOT / "docs" / "spring-ai-handbook-validation.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Generated {len(TOPICS)} compact topic pages covering {len(items)} source prompts.")

if __name__ == "__main__":
    main()
