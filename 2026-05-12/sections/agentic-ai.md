# Agentic AI — 2026-05-12

## Top Stories (3-5)

### 1. Claude Managed Agents Gains Multi-Agent Orchestration — Parallel delegation with shared filesystem now in production

**Source:** [Claude Blog](https://claude.com/blog/new-in-claude-managed-agents) | [Anthropic Docs](https://platform.claude.com/docs/en/managed-agents/multi-agent) | [Agentic Blog](https://blog.appxlab.io/2026/04/14/claude-managed-agents-production/)

Claude Managed Agents, which launched in public beta on April 8, 2026, added multi-agent orchestration support in May 2026 — a significant upgrade that moves Anthropic's hosted agentic runtime from single-agent to full multi-agent production deployments. A lead agent can now decompose complex tasks and delegate subtasks to specialist agents running in parallel on a shared filesystem, each with its own model, prompt, and tool configuration. The lead agent accumulates results from all specialists into its overall context before producing a final output.

Three new research preview features shipped alongside orchestration: **Dreaming** (the agent reviews past sessions and memory stores to extract learned patterns for self-improvement), **Outcomes** (agents work toward developer-defined success rubrics with a separate grader agent evaluating outputs, improving task success by up to 10 points in A/B tests), and **Webhooks** (fire-and-forget async operation — submit a task, receive a webhook when it completes). Together these push Claude Managed Agents from "hosted loop runner" to a full agentic platform with self-evaluation and learning capabilities.

**Key technical details:**
- Multi-agent delegation patterns: parallelization (fan-out independent subtasks), specialization (domain-specific routing), escalation (consult more capable model for hard subtasks)
- Shared filesystem enables information passing between specialist agents without custom message-passing code
- Session checkpointing, credential management, scoped permissions, and end-to-end tracing are built-in infrastructure (zero-ops overhead)
- Dreaming and Outcomes are research previews; GA timeline not announced
- Webhook delivery enables asynchronous production integrations

---

### 2. SAP Unveils "Autonomous Enterprise" at Sapphire 2026 — 200+ AI agents targeting end-to-end ERP automation

**Source:** [Forbes](https://www.forbes.com/sites/victordey/2026/05/12/the-end-of-the-erp-era-sap-wants-ai-agents-to-run-your-autonomous-enterprise/) | [SAP News](https://news.sap.com/2026/04/sap-business-ai-release-highlights-q1-2026/) | [Help Net Security](https://www.helpnetsecurity.com/2026/05/12/sap-autonomous-enterprise-business-workflows/)

SAP announced "Autonomous Enterprise" at Sapphire 2026 in Orlando — described by Forbes as "SAP's most aggressive repositioning in a generation." The platform deploys over 50 domain-specific Joule Assistants and more than 200 specialized AI agents operating autonomously across finance, procurement, HR, supply chain, and customer operations. The flagship showcase was the **Autonomous Close Assistant**, which compresses financial close cycles from weeks to days. A €100 million partner fund was simultaneously announced to accelerate customer deployments.

At the technical core is **SAP Knowledge Graph**, a semantic layer that maps relationships between business entities, workflows, and operational systems — providing the business context that SAP CEO Christian Klein argued is the decisive competitive moat in enterprise AI. Klein's thesis: winning enterprise agentic AI requires not just model capability but deep governance infrastructure — the operational rules, compliance context, and process logic that make agents trustworthy for mission-critical decisions. SAP already had this context embedded across 7.3 million data fields in its ERP systems, giving it a structural advantage over pure-play AI vendors entering the enterprise.

**Key technical details:**
- SAP Business AI Platform unifies BTP, SAP Business Data Cloud, and AI services into a single governed environment
- Joule Studio (GA since Q1 2026) enables custom agent development with 2,400 skills and 40+ pre-built agents
- Autonomous financial close, procurement, and supply-chain agents available on Day 1
- SAP Knowledge Graph provides semantic grounding preventing hallucinated business logic
- €100M partner deployment fund for SI ecosystem acceleration

---

### 3. WSO2 Agent Manager Launches as the Only Open-Source Framework-Agnostic Agent Control Plane — GA targeting June 2026

**Source:** [Globe Newswire](https://www.globenewswire.com/news-release/2026/05/05/3287760/0/en/WSO2-Launches-Agent-Manager-to-Bring-Identity-Governance-and-Scale-to-Enterprise-AI-Agents.html) | [WSO2](https://wso2.com/agent-platform/agent-manager/) | [GitHub](https://github.com/wso2/agent-manager)

WSO2 launched Agent Manager in beta on May 5, 2026 under Apache 2.0, filling a critical gap in the agentic stack: a framework-agnostic, open-source control plane that covers identity, governance, and observability for multi-framework agent deployments. Unlike proprietary solutions (LangSmith, Vertex Agent Builder, Bedrock Agents), WSO2 Agent Manager can manage LangChain, CrewAI, OpenAI SDK, and custom agents simultaneously from a single pane of glass, regardless of whether they run on-premise, in AWS Bedrock, or in LangSmith.

The architecture is Kubernetes-native, built on OpenChoreo for internal deployments, and uses OpenTelemetry for zero-code-change instrumentation. Identity is first-class: each agent receives a cryptographic identity with fine-grained access control and instant revocation capability. The platform integrates with existing identity providers (Okta, Entra ID) and observability stacks, and includes policy enforcement with compliance-ready evidence generation for SOC 2, HIPAA, GDPR, and EU AI Act. The GA target is June 2026; latest release is v0.13.1 (April 2026).

**Key technical details:**
- Apache 2.0 license, Go (44.9%) + TypeScript (35%) + Python (15.3%) codebase
- Framework-agnostic: LangChain, CrewAI, OpenAI Agents SDK, custom — any HTTP-based agent
- OpenTelemetry-compatible tracing captures LLM calls, tool invocations, and agent decisions
- MCP and A2A protocol support built in for tool and agent communication layers
- Zero vendor lock-in: uses open standards (MCP, OAuth 2.0, Kubernetes, OpenTelemetry)

---

### 4. OpenAI Agents Python SDK Hits v0.17.x — GPT-5 default, concurrency controls, realtime improvements

**Source:** [GitHub v0.16.0](https://github.com/openai/openai-agents-python/releases/tag/v0.16.0) | [GitHub v0.17.1](https://github.com/openai/openai-agents-python/releases/tag/v0.17.1)

Two rapid releases of the OpenAI Agents Python SDK dropped in the first two weeks of May 2026. v0.16.0 (May 7) made `gpt-5.4-mini` the new default model, replacing `gpt-4.1` — bringing GPT-5 series defaults including `reasoning.effort="none"` and `verbosity="low"` to all new agents. v0.17.0 (May 8) added `gpt-realtime-2` as the default for RealtimeAgent with sandbox security hardening. v0.17.1 (May 11) followed immediately with tracing resilience fixes, session management patches for MongoDB/Redis backends, and realtime audio processing improvements.

The most operationally significant new feature in this release cycle is `ToolExecutionConfig(max_function_tool_concurrency=...)`, which enables fine-grained control over parallel local tool execution. Previously, all function tools in a step ran concurrently with no rate limiting; this config allows teams deploying agents against rate-limited APIs (e.g., calling external services with QPS limits) to throttle concurrency at the tool level without wrapping tools in custom semaphore logic. The `include_server_in_tool_names` flag for MCPConfig addresses a real production pain point: name collisions when agents connect to multiple MCP servers that expose identically named tools.

**Key technical details:**
- Default model: `gpt-5.4-mini` (v0.16.0), RealtimeAgent default: `gpt-realtime-2` (v0.17.0)
- `max_turns=None` option to disable run turn limits for long-horizon tasks
- `ToolExecutionConfig(max_function_tool_concurrency=N)` for API rate-limit-aware tool scheduling
- `include_server_in_tool_names` in MCPConfig prevents tool name collisions across MCP servers
- MongoDB and Redis session backends patched for multi-session reliability

---

### 5. Google ADK Publishes Long-Running Agent Guide — Durable pause/resume for multi-week enterprise workflows

**Source:** [Google Developers Blog](https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/) | [ADK Docs](https://google.github.io/adk-docs/runtime/resume/)

Google published a detailed production guide in May 2026 covering the three architectural patterns that distinguish production agents from demo chatbots when building long-running workflows with the Agent Development Kit. The guide centers on an HR onboarding agent that sends a welcome packet, waits days while employees sign documents, delegates IT provisioning to a sub-agent, tracks hardware delivery, and sends a personalized schedule — all without losing context or requiring the agent to actively poll for state changes.

The three architectural principles the guide formalizes are: (1) **durable memory schemas** over raw JSON in vector DBs, (2) **event-driven dormancy gates** (agents go dormant rather than polling/blocking), and (3) **multi-agent delegation** for handling heterogeneous subtasks. This complements Google Cloud's April 2026 launch of the Gemini Enterprise Agent Platform (evolution of Vertex AI), which provides Agent Studio (low-code), ADK (code-first), and Model Garden access (200+ models) under a unified enterprise governance layer.

**Key technical details:**
- `ResumabilityConfig` on the ADK workflow app enables checkpoint-based resume
- Events + Event Actions log completed workflow steps for incremental resumption
- Sub-agent delegation via multi-agent pattern — IT provisioning agent example
- Known issue: `LongRunningFunctionTool` resume fails with streaming (GitHub issue #5064 open)
- AlphaEvolve (production for 1+ year) is the most mature Gemini-powered agent: recovering 0.7% of Google's global compute, 23% speedup on Gemini training kernels

---

## Deep Dive: Most Important Item

### SAP Autonomous Enterprise: Why Governance Wins in Agentic ERP

**Architectural Significance**

SAP's Sapphire 2026 announcement is the most consequential enterprise agentic AI development of the quarter — not because of model capability, but because it demonstrates the winning architecture for regulated enterprise domains. The platform's core thesis, articulated by CEO Christian Klein, is that the AI agent race in the enterprise is won at the **governance layer**, not the foundation model layer.

The architecture is built around three interlocking components:

1. **SAP Knowledge Graph** — a semantic layer encoding the relationships between business processes, data entities, compliance rules, and operational logic accumulated from SAP's 50+ years as the ERP vendor for the Fortune 500. This graph provides agents with the business context necessary to make decisions that are not just technically correct but operationally valid and legally compliant.

2. **200+ Specialized Domain Agents** — rather than one general-purpose agent attempting all tasks, SAP deploys narrow specialists (financial close agent, procurement agent, HR onboarding agent, supply chain resilience agent) each grounded in domain-specific rules, KPIs, and process flows extracted from the Knowledge Graph. Each Joule Assistant corresponds to a bounded operational domain with clear input/output contracts.

3. **Joule Interface** — a conversational orchestration layer where users specify business outcomes ("close the books by Friday") rather than task sequences. Joule decomposes the goal, dispatches the appropriate specialist agents, monitors execution, and surfaces exceptions requiring human judgment.

**Competitive Context**

The timing of this announcement relative to competitors is deliberate. Salesforce launched Agentforce Operations on April 29 (targeting back-office process automation with claimed 50–70% cycle time reductions). ServiceNow, Workday, and Oracle are all shipping agentic layers on their respective platforms in 2026. The common pattern: every major ERP/SaaS vendor is pivoting from "AI assistant for humans" to "AI agents that autonomously operate the enterprise."

SAP's structural advantage is the depth of business context embedded in its data model — 7.3 million data fields across finance, procurement, HR, and supply chain. Pure-play AI vendors (OpenAI, Anthropic, Google) can provide better foundation models, but they lack the operational context to safely automate decisions like approving a $2M purchase order or closing a financial quarter. SAP's bet is that context + governance will prove more defensible than raw model performance as enterprises move from AI experimentation to AI operation.

The €100M partner fund signals an SI-led deployment model — acknowledging that the bottleneck for enterprise adoption is not capability but organizational change management, process redesign, and integration with legacy systems.

**Open Questions**
- Will SAP's Knowledge Graph remain proprietary, or will it expose APIs for third-party agents (A2A compatibility)?
- How will SAP handle model selection — will customers be able to swap in non-SAP models, or is there lock-in to SAP's model layer?
- The "Autonomous Enterprise" vision requires agents to make binding business decisions (approve POs, execute trades, sign contracts) — what are the audit and liability frameworks?

---

## Benchmark Data (SWE-bench, GAIA, AgentBench, etc.)

```json
[
  {
    "benchmark": "SWE-bench Verified",
    "date": "2026-05-12",
    "source": "https://www.vals.ai/benchmarks/swebench-06-13-2025",
    "results": [
      {"agent": "Claude Opus 4.7", "score": 87.6, "metric": "% resolved"},
      {"agent": "GPT-5.5", "score": 82.6, "metric": "% resolved"},
      {"agent": "Claude Opus 4.7 (alternate run)", "score": 82.0, "metric": "% resolved"},
      {"agent": "Gemini 3.1 Pro Preview", "score": 78.8, "metric": "% resolved"}
    ],
    "notes": "SWE-bench Verified is acknowledged as contaminated; OpenAI stopped self-reporting it. Use SWE-bench Pro for uncontaminated baselines. Claude Opus 4.7 holds the highest published score at 87.6%."
  },
  {
    "benchmark": "Terminal-Bench 2.0",
    "date": "2026-05-12",
    "source": "https://www.tbench.ai/leaderboard/terminal-bench/2.0",
    "results": [
      {"agent": "GPT-5.5", "score": 82.7, "metric": "% tasks completed"},
      {"agent": "Claude Mythos Preview", "score": 82.0, "metric": "% tasks completed"},
      {"agent": "GPT-5.3 Codex", "score": 77.3, "metric": "% tasks completed"}
    ],
    "notes": "Terminal-Bench 2.0 evaluates agents on real-world CLI tasks including software engineering, system administration, and cybersecurity. 124 entries tracked. GPT-5.5 leads by a narrow margin."
  },
  {
    "benchmark": "GDPval (Artificial Analysis)",
    "date": "2026-05-12",
    "source": "https://artificialanalysis.ai/evaluations/gdpval-aa",
    "results": [
      {"agent": "GPT-5.5 (xhigh effort)", "score": 1773, "metric": "GDPval score (higher is better)"},
      {"agent": "GPT-5.5 (high effort)", "score": 1755, "metric": "GDPval score"},
      {"agent": "Claude Opus 4.7 (Adaptive Reasoning, Max Effort)", "score": 1753, "metric": "GDPval score"}
    ],
    "notes": "GDPval tests models on 220 economically valuable tasks across 44 occupations and 9 industries. Agents receive shell + browser access. OpenAI reports GPT-5.5 at 84.9% on GDPval. Top 3 models are within 20 points of each other, indicating convergence at the frontier."
  },
  {
    "benchmark": "GAIA",
    "date": "2026-05-12",
    "source": "https://agentmarketcap.ai/blog/2026/04/11/gaia-benchmark-gold-standard-autonomous-agent-2026",
    "results": [
      {"agent": "Alita system", "score": 87.27, "metric": "pass@3 overall"},
      {"agent": "Claude Sonnet 4.5 (Princeton HAL)", "score": 74.6, "metric": "% overall"},
      {"agent": "Claude Mythos Preview (BenchLM)", "score": 52.3, "metric": "% overall"}
    ],
    "notes": "GAIA tests real-world multi-step workflows requiring tool coordination. Human baseline is ~92%. Best systems have closed the gap from 77 points below human (2023) to under 20 points. Now considered the best predictor of production agent performance."
  },
  {
    "benchmark": "WebArena",
    "date": "2026-05-12",
    "source": "https://decodethefuture.org/en/ai-agent-benchmarks-2026/",
    "results": [
      {"agent": "Claude Mythos Preview", "score": 68.7, "metric": "% tasks completed"},
      {"agent": "GPT-5.4 Pro", "score": 65.8, "metric": "% tasks completed"},
      {"agent": "Claude Opus 4.6", "score": 64.5, "metric": "% tasks completed"}
    ],
    "notes": "WebArena measures multi-step browser navigation tasks on realistic web environments. Plan-and-Execute architecture achieves 57.58% on WebArena-Lite vs. ReAct's lower baseline — architecture matters more than model for long-horizon tasks."
  },
  {
    "benchmark": "AI Agent Framework Scorecard 2026",
    "date": "2026-05-12",
    "source": "https://rapidclaw.dev/blog/ai-agent-benchmarks-2026",
    "results": [
      {"agent": "Overall frontier cluster", "score": 74, "metric": "typical upper range % on easy suites"},
      {"agent": "Benchmark reliability caveat", "score": -15, "metric": "estimated inflation from contamination/scaffolding/single-run reporting"}
    ],
    "notes": "UC Berkeley research (April 2026) showed all 8 major agent benchmarks can be reward-hacked to ~100%. Benchmark inflation of 5-15 points is endemic. GAIA, Terminal-Bench, and GDPval are considered the most contamination-resistant."
  }
]
```

---

## Architecture / Pattern Notes

### Dominant Pattern 1: Hierarchical Multi-Agent (Supervisor-Worker)

```
lead_agent (orchestrator / planner)
  -> decompose task
specialist_agent_1 (domain A — e.g., finance)
  -> execute subtask, write to shared filesystem
specialist_agent_2 (domain B — e.g., procurement)
  -> execute subtask, write to shared filesystem
specialist_agent_N (domain N)
  -> execute subtask, write to shared filesystem
  -> all results merge into lead_agent context
lead_agent
  -> synthesize outputs, apply grader (Outcomes rubric)
  -> produce final result or escalate exception
```

*Used by: Claude Managed Agents multi-agent orchestration, SAP Joule Assistants dispatch, Google ADK multi-agent delegation, LangGraph supervisor pattern*

---

### Dominant Pattern 2: Event-Driven Dormant Agent (Long-Running)

```
agent (active)
  -> complete sync action (e.g., send email, call API)
  -> register dormancy gate (event type + condition)
agent (dormant — zero cost while waiting)
  -> [external event fires: webhook, approval, timer, human input]
agent (active again — resumes from checkpoint)
  -> read durable state from memory schema
  -> continue workflow from last completed step
```

*Used by: Google ADK ResumabilityConfig, Claude Managed Agents session checkpointing, Hermes Agent v0.13.0 heartbeats + retry budgets*

---

### Dominant Pattern 3: SGA-MCTS (System 2 → System 1 Distillation)

```
offline_phase
  -> MCTS explores state-goal-action tree
  -> distills successful trajectories into SGA atoms
  -> stores atoms in retrieval index
online_inference
  -> new task arrives
  -> retrieve relevant SGA atoms from index
  -> compose plan from distilled trajectories (System 1 speed)
  -> execute with full context of validated prior paths
```

*From arXiv 2604.14712. Achieves "System 2 reasoning depth at System 1 inference speeds" — designed for real-time feasibility of complex multi-step tasks.*

---

### Framework Comparison Table

| Framework | Core Abstraction | Graph Type | Best For |
|-----------|-----------------|------------|----------|
| LangGraph | State machine nodes + edges | Explicit DAG / cyclic graph | Production control, deterministic flows, checkpointing |
| OpenAI Agents SDK | Agent + handoffs + tools | Implicit (managed loop) | Rapid deployment on OpenAI stack, realtime agents |
| CrewAI | Role-based agents + tasks | Sequential / hierarchical | Quick prototyping, domain-role assignment |
| AutoGen / AG2 | Conversational agent groups | Dynamic conversation graph | Research workflows, multi-agent dialogue |
| Claude Managed Agents | Hosted sessions + specialists | Managed supervisor-worker | Zero-ops production, Anthropic-native stack |
| Google ADK | Tools + sub-agents + memory | Event-driven DAG | Long-running enterprise workflows, Gemini-native |
| WSO2 Agent Manager | Control plane (identity + govern + trace) | N/A (cross-framework) | Enterprise governance, multi-framework fleet management |
| Hermes Agent | Kanban boards + durable tasks | Goal-directed async | Multi-platform messaging agents, durable task management |

---

## Analysis & Impact for Agentic Engineers

- **Governance is the new moat.** SAP's Autonomous Enterprise launch, WSO2 Agent Manager's GA, and the proliferation of agent security platforms (Okta, Certiv, Nomotic, Thoth) all signal the same message: the production blocker in 2026 is no longer model capability — it's trusted, auditable, compliant agent operation. Engineers building enterprise agents must plan for identity, access control, and audit trails from day one, not as afterthoughts.

- **Claude Managed Agents' Outcomes + Dreaming are a preview of self-improving agents.** The ability for an agent to grade its own outputs against a developer-defined rubric and self-correct (up to +10 points improvement) is architecturally significant. Combined with Dreaming (extracting patterns from past sessions), this is the first commercially available hosted system with explicit self-improvement loops. Watch for this pattern to spread to LangGraph (LangSmith rubric evaluators), OpenAI (evals-as-tool-calls), and Google ADK.

- **Event-driven dormancy is required for enterprise agentic workflows.** Google's ADK guide making this explicit — agents should go dormant waiting for external events rather than polling — reflects a broader shift in how long-running workflows are architectured. Engineers still building polling loops or sleeping threads in production agents are accumulating technical debt; the event-driven dormancy pattern is now the documented best practice across ADK, Claude Managed Agents, and Hermes Agent.

- **Benchmark contamination is accelerating, but GAIA and Terminal-Bench remain reliable.** UC Berkeley's April 2026 finding that all 8 major agent benchmarks can be reward-hacked to ~100% should recalibrate how teams evaluate models for production tasks. GAIA (multi-step tool-use workflows) and Terminal-Bench 2.0 (real CLI tasks) remain the most operationally predictive benchmarks. GDPval (economically-grounded task suite) is the best for evaluating ROI-relevant agent capabilities.

- **The A2A + MCP two-layer protocol stack is solidifying.** With A2A v1.0 backed by AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP, and ServiceNow, and MCP's 2026 roadmap targeting stateless transport for hyperscale by June, the protocol stack is stable enough to build production systems on. Engineers should design agent systems expecting both layers: MCP for agent-tool calls (specific function execution), A2A for agent-agent delegation (multi-turn collaborative tasks).

---

## Key Takeaways (TL;DR)

- **Claude Managed Agents added multi-agent orchestration** (May 2026): parallel specialist agents on shared filesystem, plus Dreaming (self-improvement from past sessions) and Outcomes (grader-based self-correction, +10 points improvement in testing).
- **SAP declared "Autonomous Enterprise"** at Sapphire 2026: 200+ specialized AI agents automating ERP operations, anchored by SAP Knowledge Graph — governance and business context as the defensible moat over foundation model vendors.
- **WSO2 Agent Manager** is the only Apache 2.0, framework-agnostic agent control plane covering identity + governance + observability for multi-framework fleets; GA June 2026.
- **OpenAI Agents SDK v0.17.x** defaults to GPT-5.4-mini, adds `ToolExecutionConfig` for MCP-level tool concurrency control, and fixes Redis/MongoDB session management for production deployments.
- **GAIA and Terminal-Bench 2.0 are the most reliable agentic benchmarks** — UC Berkeley confirmed all 8 major benchmarks are reward-hackable; GPT-5.5 leads Terminal-Bench (82.7%) and GDPval (84.9%), Claude Opus 4.7 leads SWE-bench Verified (87.6%).
- **Event-driven dormant agent architecture** (Google ADK guide, May 2026) is now the documented best practice for enterprise long-running workflows — agents go dormant waiting for external events rather than polling, with durable checkpoint-based resumption.

---

*Sources:*

- https://claude.com/blog/new-in-claude-managed-agents
- https://claude.com/blog/claude-managed-agents
- https://platform.claude.com/docs/en/managed-agents/multi-agent
- https://blog.appxlab.io/2026/04/14/claude-managed-agents-production/
- https://www.forbes.com/sites/victordey/2026/05/12/the-end-of-the-erp-era-sap-wants-ai-agents-to-run-your-autonomous-enterprise/
- https://news.sap.com/2026/04/sap-business-ai-release-highlights-q1-2026/
- https://www.helpnetsecurity.com/2026/05/12/sap-autonomous-enterprise-business-workflows/
- https://www.savictech.com/insights/sap-joule-agentic-platform-40-agents-2026/
- https://www.globenewswire.com/news-release/2026/05/05/3287760/0/en/WSO2-Launches-Agent-Manager-to-Bring-Identity-Governance-and-Scale-to-Enterprise-AI-Agents.html
- https://wso2.com/agent-platform/agent-manager/
- https://github.com/wso2/agent-manager
- https://wso2.github.io/agent-manager/
- https://github.com/openai/openai-agents-python/releases/tag/v0.16.0
- https://github.com/openai/openai-agents-python/releases/tag/v0.17.0
- https://github.com/openai/openai-agents-python/releases/tag/v0.17.1
- https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/
- https://google.github.io/adk-docs/runtime/resume/
- https://deepmind.google/blog/alphaevolve-impact/
- https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
- https://www.tbench.ai/leaderboard/terminal-bench/2.0
- https://artificialanalysis.ai/evaluations/gdpval-aa
- https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/
- https://agentmarketcap.ai/blog/2026/04/11/gaia-benchmark-gold-standard-autonomous-agent-2026
- https://decodethefuture.org/en/ai-agent-benchmarks-2026/
- https://rapidclaw.dev/blog/ai-agent-benchmarks-2026
- https://agentmarketcap.ai/blog/2026/04/11/swe-bench-12-month-progress-report-2025-2026
- https://www.vals.ai/benchmarks/swebench-06-13-2025
- https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/
- https://a2a-protocol.org/v0.2.5/topics/a2a-and-mcp/
- https://tedt.org/MCPs-2026-Roadmap/
- https://mcpblog.dev/blog/2026-03-15-a2a-v1-mcp
- https://www.contextstudios.ai/blog/mcp-v2-beta-what-changes-in-multi-agent-communication
- https://www.salesforce.com/news/stories/agentforce-operations-announcement/
- https://agentmodeai.com/compare/servicenow-now-assist-vs-sap-joule/
- https://agentmarketcap.ai/blog/2026/04/12/react-vs-plan-execute-vs-tree-of-thought-production-2026
- https://arxiv.org/pdf/2604.14712
- https://www.marktechpost.com/2026/04/22/how-to-design-a-production-grade-camel-multi-agent-system-with-planning-tool-use-self-consistency-and-critique-driven-refinement/
- https://www.okta.com/products/govern-ai-agent-identity/
- https://www.certiv.ai/product/
- https://a2a.midlantics.com/
- https://aten.security/thoth
- https://nomotic.ai/
- https://beam.ai/agentic-insights/enterprise-ai-agents-production-2026
- https://www.inventiple.com/blog/agentic-ai-production-cost-analysis
- https://softmaxdata.com/blog/definitive-guide-to-agentic-frameworks-in-2026-langgraph-crewai-ag2-openai-and-more/
- https://pecollective.com/blog/ai-agent-frameworks-compared/
- https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7
