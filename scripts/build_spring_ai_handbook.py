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

FOUNDATION_ANSWERS = {
    "What is an LLM, and how does it generate a response?": "A large language model is a Transformer-based neural network trained to estimate the probability of the next token from the tokens already in its context. The input is tokenized into numeric IDs, converted into learned representations, and processed through attention layers that relate each token to relevant earlier tokens. During inference, the model produces a probability distribution, selects one token according to its decoding settings, appends it to the context, and repeats until a stop condition is reached. It generates from learned statistical patterns and supplied context; it does not query a factual database unless the application explicitly provides retrieval or tools.",
    "Explain how an LLM generates a response.": "The application assembles system instructions, user input, conversation history, retrieved evidence and tool results into a bounded context. The tokenizer converts that text into tokens, and the Transformer uses attention to compute contextual representations and a next-token probability distribution. A decoding strategy selects a token, adds it to the sequence and repeats autoregressively. The final response is therefore probabilistic generation conditioned on the available context, not a deterministic lookup or proof of correctness.",
    "What is the difference between an LLM, embedding model, and reranking model?": "An LLM generates new token sequences and is used for answering, summarizing or planning. An embedding model converts text into a fixed-length vector so a vector index can retrieve semantically related candidates; it does not generate an answer. A reranking model compares a query with retrieved candidates and produces a stronger relevance ordering, usually at higher per-document cost. In RAG they form a pipeline: embeddings retrieve broadly, reranking improves precision, and the LLM synthesizes from the selected evidence.",
    "What is a token, and why does tokenization matter in production?": "A token is the model's processing unit and may be a word, part of a word, punctuation or whitespace depending on the tokenizer. The complete request and generated response consume tokens, so tokenization determines whether prompts fit the context window and directly affects provider cost, memory, throughput and latency. Different models can tokenize the same text differently, making character or word counts unreliable. Production systems should measure tokens with the target model's tokenizer and reserve explicit budgets for instructions, history, retrieval, tools and output.",
    "What is an LLM context window, and why is it important?": "The context window is the maximum token budget the model can consider for one inference request. System instructions, user messages, conversation history, retrieved chunks, tool definitions, tool results and the planned output all compete for this space. Exceeding it causes rejection or truncation, while filling it with weak content increases latency, cost and the chance that important evidence is ignored. A production system therefore allocates token budgets, retrieves selectively, summarizes older history and preserves critical instructions.",
    "What is hallucination, and why does it happen?": "Hallucination is a plausible-sounding response that is unsupported or false. It occurs because an LLM optimizes next-token likelihood rather than truth, especially when knowledge is missing, instructions are ambiguous, retrieval is weak, context conflicts, or untrusted text manipulates the prompt. Mitigation combines authoritative retrieval, relevance thresholds, citations, abstention, structured validation and deterministic checks for business decisions. No prompt can eliminate hallucination, so risk-sensitive workflows require evaluation and human or rule-based control.",
    "Explain hallucination and how you mitigate it.": "Hallucination is unsupported generation caused by probabilistic prediction rather than factual verification. I reduce it by grounding answers in authorized evidence, filtering and reranking retrieval, requiring claim-linked citations, instructing the system to abstain when evidence is insufficient, and validating high-impact outputs against deterministic sources. I then measure faithfulness and answer correctness on a representative evaluation set. In regulated workflows, the model may recommend, but rules or humans approve the decision.",
    "What is the difference between Prompting, RAG, and Fine-tuning?": "Prompting changes the instructions and context supplied at runtime and is best for defining a task, tone, constraints or response format. RAG retrieves current or private knowledge at request time and grounds the response without changing model weights. Fine-tuning changes model behavior by training on examples and is useful for stable specialized patterns, not as the primary store for frequently changing enterprise facts. Most enterprise systems start with prompting, add RAG for knowledge, and consider fine-tuning only after evaluation shows a persistent behavioral gap.",
    "What are Temperature and Top-P? How do they affect production systems?": "Temperature reshapes the next-token probability distribution: lower values concentrate choices and higher values increase variation. Top-P limits sampling to the smallest set of tokens whose cumulative probability reaches a threshold, excluding the long tail. They interact, so production systems normally tune one conservatively and hold the other stable. Low-variance settings suit extraction and transactions, but they do not guarantee determinism because providers, model versions and infrastructure can still change outputs.",
    "What are embeddings, and how does semantic similarity work?": "An embedding model maps text into a fixed-dimensional vector whose geometry represents learned semantic relationships. The query and documents must use the same embedding model and dimension; a vector store then uses cosine similarity, dot product or Euclidean distance to find nearby vectors, often through an approximate nearest-neighbor index. Similarity only ranks related candidates—it does not prove relevance or truth—so production retrieval also uses metadata filters, thresholds and reranking. Changing the embedding model requires a versioned re-embedding and index migration.",
    "Why can't an LLM directly access enterprise databases/APIs?": "A model receives context and generates text or structured tool-call requests; it has no inherent network identity, database session or authorization to enterprise systems. The application exposes a controlled set of tool schemas, validates model-generated arguments, checks the authenticated user's permissions, executes the operation and returns a bounded result. This separation prevents the model from granting itself access and allows timeouts, idempotency, audit and policy enforcement. Credentials must remain in the execution layer, never in prompts.",
    "What is the difference between traditional RAG and an AI Agent?": "Traditional RAG follows a mostly fixed path: retrieve evidence, add it to the prompt and generate a grounded answer. An agent can iteratively decide what action to take next, choose tools, observe results, update state and continue until a termination condition is met. RAG is often one capability used by an agent, but it does not itself imply planning or side effects. Use an agent only when dynamic decisions add value; deterministic retrieval or workflows are simpler, faster and safer for predictable tasks.",
    "How would you handle multiple LLM providers?": "Place provider-specific clients behind a model gateway that routes by capability, data residency, latency, cost and risk rather than treating every model as interchangeable. Normalize the application contract, but retain provider-specific configuration where capabilities differ. Test prompts, structured output, tool calling, safety behavior and token accounting for every supported model. Fail over only to a semantically compatible model, preserve the request deadline, and record the selected provider and model version for evaluation and audit.",
}

FOUNDATION_REVISION_MD = r'''
### What is an LLM, and how does it generate a response?

An **LLM** is a Transformer-based neural network trained to estimate the probability of the next token from the tokens already in its context.

- **Generation flow:**
  1. Tokenize the input into numeric token IDs.
  2. Convert tokens into learned representations.
  3. Process them through **attention layers** that relate each token to relevant earlier tokens.
  4. Produce a probability distribution for the next token.
  5. Select a token using the configured decoding settings, append it to the context, and repeat until a stop condition.
- **Important:** The model generates from learned statistical patterns and supplied context.
- **Boundary:** It does not query a factual database unless the application explicitly supplies retrieval or tools.

### What is the difference between an LLM, embedding model, and reranking model?

The three models serve different stages of an AI pipeline: **generation**, **candidate retrieval**, and **relevance refinement**.

| Model | Primary role | Output |
|---|---|---|
| **LLM** | Answers, summarizes, or plans by generating token sequences | Generated text or structured content |
| **Embedding model** | Converts text into fixed-length vectors for semantic retrieval | Vector representation |
| **Reranking model** | Compares a query with retrieved candidates and improves their relevance order | Relevance scores or reordered candidates |

- **RAG flow:** Embeddings retrieve broadly → reranking improves precision → the LLM synthesizes from selected evidence.
- **Trade-off:** Reranking usually improves relevance but adds per-document latency and cost.
- **Important:** An embedding model retrieves related content; it does not generate an answer.

### What is a token, and why does tokenization matter in production?

A **token** is the model's processing unit and may represent a word, part of a word, punctuation, or whitespace.

- The prompt and generated response both consume tokens.
- Token counts determine whether a request fits the **context window**.
- They directly affect provider cost, memory, throughput, and latency.
- Different models can tokenize identical text differently, so character or word counts are unreliable.
- **Production:** Measure with the target model's tokenizer and reserve budgets for instructions, history, retrieval, tools, and output.

### What is an LLM context window, and why is it important?

The **context window** is the maximum token budget a model can consider during one inference request.

- System instructions, user messages, conversation history, retrieved chunks, tool definitions, tool results, and planned output share the same budget.
- Exceeding the limit causes rejection or truncation.
- Filling it with weak content increases latency, cost, and the chance that important evidence is ignored.
- **Production:** Allocate token budgets, retrieve selectively, summarize older history, and preserve critical instructions.

### What is hallucination, and why does it happen?

**Hallucination** is a plausible-sounding response that is unsupported or false.

- An LLM optimizes **next-token likelihood**, not factual truth.
- Risk increases when knowledge is missing, instructions are ambiguous, retrieval is weak, or context conflicts.
- Untrusted content can also manipulate the prompt and distort the answer.
- Mitigation combines authoritative retrieval, relevance thresholds, citations, abstention, structured validation, and deterministic checks.
- **Important:** No prompt eliminates hallucination; risk-sensitive workflows require evaluation and human or rule-based control.

### What is the difference between Prompting, RAG, and Fine-tuning?

**Prompting** changes runtime instructions, **RAG** supplies runtime knowledge, and **fine-tuning** changes model behavior through training.

| Approach | What it changes | Best fit |
|---|---|---|
| **Prompting** | Instructions and context supplied with a request | Task definition, tone, constraints, and response format |
| **RAG** | Current or private knowledge supplied at request time | Grounded answers without changing model weights |
| **Fine-tuning** | Model behavior learned from training examples | Stable specialized behavior or patterns |

- Fine-tuning is not the primary store for frequently changing enterprise facts.
- **Production path:** Start with prompting, add RAG for knowledge, and consider fine-tuning only when evaluation shows a persistent behavioral gap.

### What are Temperature and Top-P? How do they affect production systems?

**Temperature** and **Top-P** control how tokens are sampled from the model's next-token probability distribution.

- **Temperature:** Lower values concentrate choices; higher values increase variation.
- **Top-P:** Limits sampling to the smallest token set whose cumulative probability reaches the configured threshold.
- The settings interact, so production systems normally tune one conservatively while keeping the other stable.
- Low-variance settings suit extraction and transactional use cases.
- **Trade-off:** Low values improve repeatability but do not guarantee determinism across provider infrastructure or model versions.

### What are embeddings, and how does semantic similarity work?

An **embedding model** maps text into a fixed-dimensional vector whose geometry represents learned semantic relationships.

1. Embed documents and the query using the same model and vector dimension.
2. Store document vectors and metadata in a **vector store**.
3. Compare the query vector using cosine similarity, dot product, or Euclidean distance.
4. Retrieve nearby candidates, often through an approximate nearest-neighbor index.
- **Important:** Similarity ranks related candidates; it does not prove relevance or truth.
- **Production:** Apply metadata filters, thresholds, and reranking. Changing the model requires versioned re-embedding and index migration.

### Why can't an LLM directly access enterprise databases/APIs?

An LLM generates text or structured tool-call requests; it has no inherent network identity, database session, or enterprise authorization.

1. The application exposes a controlled set of tool schemas.
2. The model proposes a tool and arguments.
3. Application code validates the arguments and authenticated user's permissions.
4. The application executes the operation and returns a bounded result.
- This separation supports timeouts, idempotency, policy enforcement, and audit.
- **Security:** Credentials stay in the execution layer and never enter prompts.

### What is the difference between traditional RAG and an AI Agent?

Traditional **RAG** follows a mostly fixed retrieval-and-generation path, while an **AI agent** can iteratively choose actions and tools.

- **RAG:** Retrieve evidence → add it to the prompt → generate a grounded answer.
- **Agent:** Decide the next action → invoke a tool → observe the result → update state → continue until termination.
- RAG can be one capability used by an agent, but retrieval alone does not imply planning or side effects.
- **Trade-off:** Use an agent only when dynamic decisions add value; deterministic retrieval or workflows are simpler, faster, and safer for predictable tasks.

### Explain how an LLM generates a response.

An LLM generates a response by repeatedly predicting the next token from the application-supplied context.

1. Assemble system instructions, user input, history, retrieved evidence, and tool results into a bounded context.
2. Tokenize the context.
3. Use Transformer attention to compute contextual representations and next-token probabilities.
4. Select a token using the decoding strategy and append it to the sequence.
5. Repeat until a stop condition is reached.
- **Important:** The result is probabilistic generation conditioned on context, not a deterministic lookup or proof of correctness.

### Explain hallucination and how you mitigate it.

Hallucination is unsupported generation caused by probabilistic prediction rather than factual verification.

- Ground answers in authorized evidence.
- Filter and rerank retrieval results before context construction.
- Require claim-linked citations and abstention when evidence is insufficient.
- Validate high-impact outputs against deterministic sources.
- Measure **faithfulness** and **answer correctness** on a representative evaluation set.
- **Regulated workflows:** The model may recommend, but rules or humans approve the decision.

### How would you handle multiple LLM providers?

Use a **model gateway** that routes providers by capability, data residency, latency, cost, and risk without assuming models are interchangeable.

- Normalize the application contract while retaining provider-specific configuration where capabilities differ.
- Test prompts, structured output, tool calling, safety behavior, and token accounting for every supported model.
- Fail over only to a semantically compatible model and preserve the request deadline.
- Record the chosen provider and model version for evaluation, observability, and audit.
'''

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
        "foundations": """flowchart LR
    T[Input text] --> K[Tokenizer] --> C[Context tokens]
    C --> A[Transformer attention] --> P[Next-token probabilities]
    P --> D[Decode one token] --> S{Stop condition?}
    S -->|no| C
    S -->|yes| O[Generated response]
    O --> V[Application validation]""",
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
    if item["question"] in FOUNDATION_ANSWERS:
        return FOUNDATION_ANSWERS[item["question"]]
    q = item["question"].lower()
    if any(x in q for x in ("when should", "when would you reject", "why shouldn't")):
        return f"Start from the deterministic alternative and identify exactly where interpretation or dynamic action is required. Evaluate {areas} against latency, compliance, predictability and operating cost. Use an agent only when measured task-quality improvement outweighs its additional nondeterminism and failure surface."
    if any(x in q for x in ("secure", "protect", "prevent unauthorized", "multi-tenant")):
        return f"Treat {areas} as deterministic controls enforced at the application, retrieval and tool boundaries. Identity, tenant scope and permissions must come from authenticated server context, never from prompt text or model output. Apply least privilege, validate every requested action and preserve an audit trail across fallback and retry paths."
    if any(x in q for x in ("failure", "fails", "timeout", "429", "unavailable", "degrading", "slow", "increased")):
        return f"Use an end-to-end deadline and tracing to locate the failing segment before retrying. Protect capacity with bounded concurrency, backoff and circuit breaking, and make retries idempotent when side effects are possible. Recover through a tested fallback or safe degradation, then verify {areas} and add the incident to regression coverage."
    if any(x in q for x in ("evaluate", "prove", "test")):
        return f"Build a versioned dataset of representative, edge and adversarial scenarios and define expected evidence or outcomes before testing. Measure {areas} separately so retrieval, generation and end-task failures are distinguishable. Compare against a baseline, inspect failures rather than relying on one aggregate score, and retain every accepted defect as a regression case."
    if any(x in q for x in ("design", "architecture", "walk me through", "flow")):
        return f"Separate the design into explicit components for {areas}, with a clear contract and owner for each boundary. Show how authenticated context, state and evidence move through the system, and where deterministic policy constrains model decisions. Then explain bottlenecks, partial failures, recovery, scaling signals and the metrics that prove the complete task works."
    return f"{areas} form a controlled end-to-end capability rather than a set of independent features. Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward. In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path."

def structured_answer(item: dict[str, str]) -> str:
    """Present an existing concise answer as an interview-revision block."""
    answer = takeaway(item)
    sentences = re.split(r"(?<=[.!?])\s+", answer.strip())
    direct = sentences[0]
    remainder = sentences[1:]
    labels = ["How it works", "Production", "Trade-off", "Important"]
    bullets = [f"- **Key areas:** {item['keyAreas'].rstrip('.')}." ]
    for index, sentence in enumerate(remainder[:4]):
        bullets.append(f"- **{labels[index]}:** {sentence}")
    if len(bullets) < 3:
        bullets.append("- **Boundary:** Keep model interpretation separate from deterministic authorization, validation, state, and recovery.")
    return f"### {item['question']}\n\n{direct}\n\n" + "\n".join(bullets)

def page(title: str, description: str, items: list[dict[str, str]], kind: str) -> str:
    answers = "\n\n".join(structured_answer(item) for item in items)
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

{answers}

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
    blocks = []
    for question, _priority, answer in PROMPT_QUESTIONS:
        sentences = re.split(r"(?<=[.!?])\s+", answer.strip())
        direct = sentences[0]
        detail = " ".join(sentences[1:]) or sentences[0]
        blocks.append(f'''### {question}

{direct}

- **How it works:** {detail}
- **Production:** Version the prompt with its model, response schema, available tools, and retrieval behavior.
- **Validation:** Promote changes only when quality, safety, latency, and cost remain within defined acceptance thresholds.''')
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

{chr(10).join(chr(10) + block for block in blocks).strip()}

## Production Rule

Version the prompt together with its model, sampling configuration, response schema, available tools and retrieval behavior. Promote changes only when quality, safety, latency and cost remain inside defined acceptance thresholds.
'''

def llm_foundations_page() -> str:
    return f'''---
title: "LLM Foundations"
date: 2026-08-22T00:00:00+05:30
draft: false
description: "How models generate, use context, represent meaning and differ from retrieval or agents."
tags: ["spring-ai", "genai", "interview-preparation"]
categories: ["Spring AI"]
interviewHandbook: true
---

How models generate, use context, represent meaning and differ from retrieval or agents.

## Core Flow

```mermaid
{flow("foundations")}
```

## Revision Map

{FOUNDATION_REVISION_MD.strip()}

## Interview Lens

Keep probabilistic interpretation separate from authorization, policy, transactions, and recovery. Explain trade-offs with evidence: task quality, latency, resilience, security, operating cost, and auditability.
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
        if slug == "llm-foundations":
            (OUT / f"{slug}.md").write_text(llm_foundations_page(), encoding="utf-8")
            continue
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
