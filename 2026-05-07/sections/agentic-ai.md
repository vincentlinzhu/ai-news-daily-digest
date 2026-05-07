# Agentic AI — 2026-05-07

*Research by: research-agentic · Coverage window: ~2026-04-30 to 2026-05-07*

---

## Top Stories

### 1. Twilio SIGNAL 2026: A New Conversation Infrastructure Layer for the Agentic Era

On May 6, 2026, Twilio's annual SIGNAL conference delivered a comprehensive platform overhaul squarely aimed at the multi-agent era. The centerpiece is a new **Conversation Layer** comprising three GA products and a new open-source SDK:

- **Conversation Memory** — An identity-resolved, LLM-optimized customer profile store that surfaces only the most relevant context per turn, reducing token usage and latency. Backed by a new Enterprise Knowledge API for grounding interactions in business documents, FAQs, and policies.
- **Conversation Orchestrator** — Multi-channel, multi-agent routing and coordination. Connects interactions across voice, SMS, messaging, and email into a single thread; manages human↔AI handoffs with full transcript continuity.
- **Conversation Intelligence** — Real-time LLM-based operators that detect sentiment shifts, flag escalation risk, and trigger actions *during* a conversation (not only post-hoc).
- **Twilio Agent Connect (GA)** — An open-source, self-hosted orchestration SDK that bridges any AI runtime (OpenAI, Azure, Amazon Bedrock, Anthropic, LangChain/LangGraph, or in-house) to Twilio's production voice and messaging channels. Handles low-latency streaming, turn-taking, session/identity management, and AI-to-human handoff. Model-agnostic and self-hosted by design.

Early production deployments: Car Finance 247 (UK) uses Conversation Memory + Orchestrator + Flex to recover stalled loan applications across voice, SMS, and RCS; Centerfield uses real-time conversation data to standardize agent performance at scale; Constellation Dealerships went from evaluation to measurable outcomes in days.

**Why it matters:** Twilio is positioning itself as the neutral communications infrastructure layer for the agentic era — the entity that handles the hard real-time I/O (voice, messaging, streaming, barge-in, HIPAA/PCI compliance) while leaving model and orchestration choices entirely to the developer. If A2A is the inter-agent wire protocol, Twilio is bidding to own the customer-facing I/O plane.

**Sources:** [Twilio SIGNAL 2026 announcements](https://www.twilio.com/en-us/blog/products/signal-2026-product-announcements) · [Agent Connect launch blog](https://www.twilio.com/en-us/blog/products/launches/agent-connect) · [Press release](https://www.twilio.com/en-us/press/releases/twilio-s-next-generation-platform--an-infrastructure-layer-for-e)

---

### 2. AWS Launches Agent Toolkit for AWS: 40+ Validated Skills + Managed MCP Server

On May 6, 2026, AWS shipped the **Agent Toolkit for AWS**, its successor to the scattered MCP servers and plugins previously hosted on AWS Labs. The toolkit addresses three pain points teams report when using coding agents on AWS: agents improvising from stale knowledge, difficulty governing agent actions, and multi-service workflows that fail in production.

**Three-layer architecture:**

- **Agent Skills (40+ at launch):** Validated, step-by-step procedures for CloudFormation authoring, S3/data pipeline configuration, serverless deploys, container workloads, and AI service integration. Skills enforce best practices rather than letting agents hallucinate API shapes. More skills coming for databases, networking, and IAM.
- **AWS MCP Server (GA):** A fully-managed MCP server giving coding agents access to any AWS service. Features IAM-based action guardrails, CloudWatch/CloudTrail observability, sandboxed code execution for multi-step operations, and live documentation retrieval so agents always have current API knowledge.
- **Agent Plugins (3 at launch):** Bundles of MCP server + curated skills — *AWS Core* (full-stack app dev), *AWS Data Analytics* (data pipelines and BI), and *AWS Agents* (production agent builds on Bedrock AgentCore).

Compatible coding agents: Claude Code, Kiro, GitHub Copilot. Installs in any IDE. No additional charge; pay only for AWS resources consumed. Available in US East (N. Virginia) and Europe (Frankfurt).

**Companion: Bedrock AgentCore regional expansion** — AgentCore (the runtime/gateway/identity/observability platform for deploying agents at scale) reached AWS GovCloud (US-West) on May 5 and South America (São Paulo) on May 1, enabling government and LatAm deployments with data residency compliance.

**Sources:** [AWS What's New — Agent Toolkit](https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/) · [Bedrock AgentCore GovCloud](https://aws.amazon.com/about-aws/whats-new/2026/05/bedrock-agentcore-launch-aws-govcloud-us/) · [AgentCore São Paulo](https://aws.amazon.com/about-aws/whats-new/2026/05/agentcore-sao-paulo-region/)

---

### 3. Coder Agents Beta: Self-Hosted, Model-Agnostic Coding Agent Platform

Also on May 6, 2026, Coder launched **Coder Agents** in public beta — a centralized, infrastructure-level orchestration platform for coding agents that runs entirely on self-hosted infrastructure. Unlike SaaS coding tools, Coder Agents runs through the Coder control plane with organization-wide governance over models, prompts, MCP tools, and network-isolated workspaces.

**Key design decisions:**

- **Model-agnostic by design:** Supports Anthropic, OpenAI, Google, Amazon Bedrock, and OpenAI-compatible self-hosted endpoints. Intelligence comes from the model; execution infrastructure is standardized.
- **Centralized controls:** Platform teams define which models, system prompts, and MCP servers are available. Developers consume agents through a conversational UI or API without managing the runtime themselves.
- **Sub-agent + skills support:** Agents can spawn sub-agents and execute extensible multi-step workflows via skills and MCP integration.
- **CI/CD integration:** The Coder Agents API can be triggered from GitHub Actions, Slack, or any pipeline.
- **Replaces Coder Tasks:** Coder Agents is the long-term replacement for Coder Tasks (migration path to be announced separately).

**Introductory offer:** Full Premium features with no usage-based limits through September 2026.

**Why it matters:** Coder Agents is the enterprise answer for regulated industries and air-gapped environments that cannot use SaaS coding tools. It separates *how* agents run (infrastructure, governance, observability) from *which model* they use — a principled architecture for organizations that need auditability and policy enforcement over agent behavior.

**Sources:** [Coder blog — Introducing Coder Agents](https://coder.com/blog/introducing-coder-agents) · [Coder Agents self-hosted announcement](https://coder.com/blog/self-hosted-ai-model-agnostic-coder-agents)

---

### 4. Google Gemini Enterprise Agent Platform: Vertex AI Evolves into Full Agent OS

On April 22, 2026 (continuing to generate production signals through early May), Google launched the **Gemini Enterprise Agent Platform** — the most comprehensive single vendor offering to date for building, scaling, governing, and optimizing agent fleets. Going forward, all Vertex AI services and roadmap updates ship exclusively through this platform.

**Build:**
- Upgraded **Agent Development Kit (ADK)** with graph-based multi-agent orchestration, 6T+ monthly tokens processed. New Agent Studio provides low-code→ADK export path.
- **Agent Sandbox** (hardened micro-VM environment for bash/file operations, isolated from host systems).
- **Agent Garden:** Curated templates for code modernization, financial analysis, invoice processing, etc.
- Programmatic interface for coding agents to build, eval, and deploy other agents on the platform.

**Scale:**
- **Agent Runtime** rebuilt for sub-second cold starts; long-running agents can persist state for *days* (supporting multi-day sales sequences, compliance workflows, etc.).
- **Agent Memory Bank** with Memory Profiles for low-latency, high-accuracy long-term context recall across sessions.
- **Custom Session IDs** map agent sessions directly to CRM/database records.
- Bidirectional WebSocket streaming for real-time audio/video (live customer interactions).

**Govern:**
- **Agent Identity:** Each agent receives a unique cryptographic ID with auditable action trail mapped to authorization policies.
- **Agent Registry:** Single source of truth for all enterprise agents, tools, and skills.
- **Agent Gateway:** Air-traffic-control for agent↔tool connections; enforces Model Armor (anti-prompt-injection, anti-data-leakage) across the fleet.
- **Agent Anomaly Detection + Threat Detection:** Statistical + LLM-as-judge behavioral monitoring; flags suspicious reasoning and malicious activity (reverse shells, known-bad IPs).

**Optimize:**
- **Agent Simulation:** Synthetic user interactions + virtualized tools for pre-ship testing.
- **Agent Evaluation:** Live traffic scoring with multi-turn autoraters.
- **Agent Optimizer:** Automatically clusters real-world failures and suggests refined system instructions.

**Production deployments at launch:** Comcast Xfinity Assistant (ADK, multi-agent, digital containment ↑), L'Oréal proprietary Beauty Tech Agentic Platform (ADK + MCP), PayPal (agent payment mandate visualization via AP2), Payhawk Financial Controller Agent (Memory Bank → 50%+ expense submission time reduction), Color Health Virtual Cancer Clinic (patient screening + scheduling).

**Sources:** [Google Cloud Blog — Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) · [Gemini Enterprise app updates](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise)

---

### 5. OpenAI Agents SDK Evolution: Native Sandbox Execution + Model-Native Harness

In mid-April 2026 (April 15), OpenAI released the **next evolution of the Agents SDK** (Python v0.14.0+), introducing a model-native agent harness with native sandbox execution — closing the gap between prototype and production agent infrastructure.

**Harness additions:**
- Configurable memory and sandbox-aware orchestration
- Codex-like filesystem tools (inspect files, run commands, write code)
- Standardized integrations: MCP tool use, Skills (`agentskills.io`), `AGENTS.md` custom instructions, `shell` tool, `apply_patch` tool
- Designed to align execution with how frontier models naturally perform best (e.g., GPT-5.4/5.5's tool call behavior)

**Sandbox execution:**
- Agents get a controlled workspace with files, dependencies, and tools; harness and compute are separated so model-generated code never touches production credentials
- Durable execution: state externalized so a lost sandbox container doesn't kill the run — built-in snapshot/rehydrate resumes from last checkpoint
- Parallel execution: subagents can be routed to isolated sandboxes and work concurrently
- Built-in support for: Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel
- **Manifest abstraction** for portable workspace description: local files, output dirs, AWS S3/GCS/Azure Blob/Cloudflare R2

**Real-world validation:** Oscar Health using it to automate clinical records workflows that prior approaches couldn't handle reliably enough (complex encounter boundary detection in long records).

TypeScript support planned. Code mode and subagents coming to both Python and TypeScript.

**Sources:** [OpenAI — Next evolution of Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk) · [Agents SDK Sandbox April 2026 update](https://open-techstack.com/blog/openai-agents-sdk-sandbox-agents-april-2026/)

---

## Deep Dive: Agent Governance — Identity, Payments, and the Trust Stack

Three independent threads converged this week into a coherent picture of how the industry is solving agent authorization:

### A2A Protocol — Governance Metadata Proposal

Following the March 2026 v1.0 release (which introduced Signed Agent Cards for cryptographic identity), the A2A community is now working on extending Agent Cards with governance metadata (Issue #1717, April 5, 2026):

- **Trust scores** indicating governance compliance level
- **Capability manifests** listing permitted actions
- **Policy compliance references** (ATF, OWASP)
- **Audit trail references** for tamper-evident chains

Separately, PR #1696 (March 2026) formalized a "Verifying Agent Identity" section in the discovery docs, using JWS (RFC 7515) + JSON canonicalization to layer cryptographic verification on top of A2A's transport security.

### Agent Payments Protocol (AP2)

AP2 is an open extension to A2A + MCP developed by Google with PayPal, Mastercard, American Express, Coinbase, Etsy, and 60+ partners. It solves agent commerce authorization via **cryptographically-signed Mandates**:

- **Cart Mandate** — real-time purchase with user present
- **Intent Mandate** — pre-approved delegated purchase (user not present)
- **Payment Mandate** — signals agent involvement to payment networks for fraud/liability routing

PayPal is already live in production with OpenAI, Perplexity, and Microsoft on agentic commerce implementations. Comcast's Xfinity Assistant and PayPal's own checkout flow both use AP2 on the Google Agent Platform.

### Microsoft Agent Framework 1.4 — CodeAct via Hyperlight

Released May 5, Microsoft's Agent Framework .NET 1.4.0 added the `Microsoft.Agents.AI.Hyperlight` package. **CodeAct** collapses multi-step tool calls into a single model-generated code block, reducing end-to-end latency ~50% and token usage ~60%. Each code block runs in a fresh, locally-isolated **Hyperlight micro-VM** — a hardware-level sandbox providing isolation without full container overhead. The `HyperlightCodeActProvider` injects an `execute_code` tool and CodeAct guidance into every invocation, with approval modes (`AlwaysRequire` / `NeverRequire`) and CRUD operations for tools, file mounts, and domain allow-lists.

**The emerging trust stack pattern:**
```
User Intent → Mandate/Credential (cryptographic, verifiable)
    ↓
Agent Card (signed, with governance metadata)
    ↓
Agent Gateway / Registry (policy enforcement, anomaly detection)
    ↓
Sandboxed Execution (Hyperlight micro-VM / Agent Sandbox / E2B)
    ↓
Auditable Action Trail (CloudTrail / Agent Identity / AP2 Payment Mandate)
```

---

## Benchmark Data

### AstaBench Spring 2026 Results (April 30, 2026 — Ai2)

Scientific agent research benchmark: 2,400+ problems across Literature Search, Code & Execution, Data Analysis, End-to-End Discovery.

```json
{
  "benchmark": "AstaBench",
  "date": "2026-04-30",
  "source": "https://allenai.org/blog/astabench-update-spring-2026",
  "leaderboard": [
    {
      "agent": "Claude Opus 4.7 (ReAct, extended thinking)",
      "overall_score_pct": 58.0,
      "cost_per_problem_usd": 3.54,
      "notes": "Leads End-to-End Discovery (+10.2 pts vs Opus 4.6); loses slightly to 4.6 on Code & Execution"
    },
    {
      "agent": "Claude Opus 4.6 (ReAct, extended thinking)",
      "overall_score_pct": 55.3,
      "cost_per_problem_usd": 2.18,
      "notes": "Strong Code & Execution; 62% cheaper than Opus 4.7 overall"
    },
    {
      "agent": "Asta v0 (specialist multi-agent router)",
      "overall_score_pct": 53.0,
      "cost_per_problem_usd": null,
      "notes": "Original benchmark top agent; still competitive"
    },
    {
      "agent": "GPT-5.5 (xhigh reasoning)",
      "overall_score_pct": 52.9,
      "cost_per_problem_usd": 1.61,
      "notes": "Leads Code & Execution and Data Analysis; best non-Claude frontier run; weakest on E2E Discovery"
    },
    {
      "agent": "Claude Sonnet 4.6 (ReAct, extended thinking)",
      "overall_score_pct": 54.5,
      "cost_per_problem_usd": null,
      "notes": "Competitive mid-tier"
    },
    {
      "agent": "Gemini 3.1 Pro Preview (high thinking)",
      "overall_score_pct": 49.6,
      "cost_per_problem_usd": null,
      "notes": ""
    },
    {
      "agent": "GPT-5.4 (xhigh reasoning)",
      "overall_score_pct": 46.5,
      "cost_per_problem_usd": null,
      "notes": ""
    }
  ],
  "key_findings": {
    "e2e_discovery_hard_perfect_completion": "~3%",
    "e2e_discovery_partial_completion": "60-70% of steps (best agents)",
    "fastest_improving_category": "Code & Execution + End-to-End Discovery",
    "slowest_improving_category": "Literature Understanding",
    "industry_adoption": ["UK AISI Inspect Evals", "Elicit", "SciSpace", "Distyl AI", "EvoScientist", "General Reasoning OpenReward"]
  }
}
```

### SWE-bench Context (current state, not new results today)

| Model | SWE-bench Verified | SWE-bench Pro | Notes |
|---|---|---|---|
| Claude Mythos Preview | 93.9% | 77.8% | Restricted release (Glasswing only) |
| Claude Opus 4.7 | 87.6% | 64.3% | Best public model |
| GPT-5.5 | TBD on Pro | — | Strong on Terminal-Bench 82.7% |

*No new SWE-bench results published this week.*

### Multi-Agent Production Adoption Metrics (aggregated, Q4 2025 data)

```json
{
  "enterprises_with_multiagent_in_production": "57%",
  "up_from_2024": "12%",
  "average_agents_deployed_per_org": 12,
  "projected_growth_2_years": "67%",
  "pilot_failure_rate_within_6_months": "40%",
  "performance_gains_vs_single_agent": {
    "task_resolution_speed": "+45%",
    "accuracy_complex_multistep": "+60%"
  },
  "coordination_overhead_example": "950ms for 4-agent fan-out vs 500ms actual processing",
  "sources": ["beam.ai/agentic-insights", "ajentik.com/insights"]
}
```

---

## Architecture / Pattern Notes

### The 2026 Agent Infrastructure Stack

Three dominant multi-agent patterns have crystallized in enterprise production this week:

**1. Hierarchical Orchestrator-Worker (most common)**
Single orchestrator decomposes task → delegates to specialists → aggregates. Used by Wells Fargo (35K bankers, 1,700 procedures), Comcast Xfinity, and most Google ADK deployments. Cost reduction 40-60% vs monolithic agents. Main failure: orchestrator context bloat and task misclassification.

**2. Fan-Out / Fan-In (emerging)**
Parallel independent agents on task shards → aggregation. Used in Anthropic Multiagent Orchestration (shared filesystem + lead agent) and OpenAI multi-sandbox subagent routing. Requires strong result deduplication and conflict resolution at merge.

**3. Event-Driven / Batch+Event Hybrid (new)**
Google Agent Platform's BigQuery + Pub/Sub batch/event agents enable massive asynchronous background tasks (content evaluation, data analysis) without blocking synchronous user paths. Separates "human-speed" conversations from "compute-speed" batch work.

### Agent Memory Architecture Patterns

Research from 2025-2026 identifies five mechanism families now converging in production:

| Mechanism | Example | Use Case |
|---|---|---|
| Context-resident compression | Summary rolling window | Short-session assistants |
| Retrieval-augmented stores | Pinecone/Memory Bank | Long-term user preferences |
| Reflective self-improvement | Claude Dreaming | Cross-session workflow optimization |
| Hierarchical virtual context | EverMemOS MemScenes | Scientific research agents |
| Policy-learned management | AgeMem (RL-trained) | Autonomous memory curation |

The Google Memory Bank "Memory Profiles" feature (launched April 22) is the first enterprise-grade managed service combining retrieval-augmented + reflective patterns with low-latency production SLAs.

### CodeAct: A Latency Architecture Shift

Microsoft's Hyperlight CodeAct integration signals a broader pattern shift: instead of the agent loop making N sequential tool calls (each with model→tool→model round trip), CodeAct lets the model emit a *code block* that batches all tool invocations into one execution. The Hyperlight micro-VM provides isolation equivalent to a container but with near-zero startup overhead. **~50% latency reduction, ~60% token reduction** in representative workloads. Expect other frameworks to adopt this pattern.

---

## Analysis & Impact

**The Twilio moment:** For years, enterprise AI builders have had to either (a) use a SaaS AI platform that owns the customer channel or (b) bolt together telephony APIs with agent frameworks themselves. Twilio Agent Connect + the new Conversation Layer offers a third option: bring your own model and framework, Twilio owns the hard real-time I/O. This is a meaningful architectural unlock for regulated industries (PCI, HIPAA) where SaaS data paths are a blocker.

**AWS is playing catch-up at the tooling layer:** The Agent Toolkit for AWS launch reflects a real pain point — coding agents building AWS infrastructure routinely hallucinate API shapes and get multi-service workflows wrong. By baking validated Skills into the MCP layer (with IAM guardrails), AWS converts the MCP server from "docs retrieval + API calls" to "validated procedure execution." This is a meaningful reliability improvement for production infra-as-code workflows.

**Self-hosted coding agents are a real product category:** Both Coder Agents and the OpenAI Agents SDK sandbox separation reflect the same enterprise insight: regulated industries (healthcare, finance, government) cannot run coding agents on SaaS where code and data leave the perimeter. The Coder/OpenAI approach of "harness in cloud, execution in your sandbox" is emerging as the canonical architecture.

**Google's Agent Platform is the most complete end-to-end offer:** No other vendor yet has a single platform covering Build (ADK+Studio), Scale (Runtime+Memory Bank+Sessions), Govern (Identity+Registry+Gateway+Anomaly Detection), and Optimize (Simulation+Evaluation+Optimizer). The gap between Google and others is now more about vendor trust and lock-in concerns than capability.

**AstaBench reveals a persistent End-to-End gap:** The most important data point from the Ai2 update: the best agent (Claude Opus 4.7) completes only ~3% of hard end-to-end scientific discovery tasks perfectly, despite getting 60-70% of individual steps right. This is a qualitative ceiling on current agentic systems — they can sequence steps but fail to synthesize a complete workflow. The next architecture frontier is *workflow coherence*, not individual capability.

**Agent payments are moving from experiment to infrastructure:** AP2's production deployments (OpenAI, Perplexity, Microsoft, PayPal checkout) signal that agent commerce is no longer theoretical. The cryptographic mandate model (Cart/Intent/Payment Mandate) is the first serious attempt at making agent-initiated payments auditable and legally attributable. Expect this to become a regulatory focus in H2 2026.

---

## Key Takeaways TL;DR

1. **Twilio SIGNAL 2026** delivered a full Conversation Layer (Memory + Orchestrator + Intelligence) plus Agent Connect SDK — positioning Twilio as the neutral customer-I/O plane for multi-agent architectures.
2. **AWS Agent Toolkit** (May 6) ships 40+ validated agent Skills + managed MCP server with IAM guardrails — making coding agents more reliable for multi-service AWS workflows.
3. **Coder Agents beta** (May 6) is the self-hosted, model-agnostic answer for regulated enterprises that can't use SaaS coding tools — governance over models/prompts/workspaces from a central control plane.
4. **Google Gemini Enterprise Agent Platform** (April 22) is the most complete agent OS to date: Build→Scale→Govern→Optimize in a single platform, with cryptographic Agent Identity and anomaly detection now in production at Comcast, L'Oréal, PayPal, and others.
5. **OpenAI Agents SDK** (April 15) adds native sandbox execution with a separated harness/compute model, durable state, and portable Manifest abstraction — production-grade infrastructure for long-running coding agents.
6. **AstaBench Spring 2026** (April 30): Claude Opus 4.7 leads at 58.0%; GPT-5.5 is the best-value non-Claude model at 52.9% and $1.61/problem; end-to-end scientific discovery remains stubbornly hard (~3% perfect completion).
7. **Microsoft Agent Framework 1.4** (May 5) ships CodeAct via Hyperlight micro-VMs — ~50% latency / ~60% token reduction by batching tool calls into model-generated code blocks.
8. **AP2 Agent Payments Protocol** is live in production at PayPal, OpenAI, and Microsoft — cryptographic mandates for agent-initiated purchases are the emerging legal/technical standard for agentic commerce.

---

## Sources

| # | Source | URL |
|---|---|---|
| 1 | Twilio SIGNAL 2026 announcements | https://www.twilio.com/en-us/blog/products/signal-2026-product-announcements |
| 2 | Twilio Agent Connect launch | https://www.twilio.com/en-us/blog/products/launches/agent-connect |
| 3 | Twilio press release | https://www.twilio.com/en-us/press/releases/twilio-s-next-generation-platform--an-infrastructure-layer-for-e |
| 4 | AWS Agent Toolkit for AWS | https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/ |
| 5 | Bedrock AgentCore GovCloud | https://aws.amazon.com/about-aws/whats-new/2026/05/bedrock-agentcore-launch-aws-govcloud-us/ |
| 6 | Bedrock AgentCore São Paulo | https://aws.amazon.com/about-aws/whats-new/2026/05/agentcore-sao-paulo-region/ |
| 7 | Coder Agents — Introducing Coder Agents | https://coder.com/blog/introducing-coder-agents |
| 8 | Coder self-hosted model-agnostic agents | https://coder.com/blog/self-hosted-ai-model-agnostic-coder-agents |
| 9 | Google Cloud — Gemini Enterprise Agent Platform | https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform |
| 10 | Gemini Enterprise app updates | https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise |
| 11 | OpenAI — Next evolution of Agents SDK | https://openai.com/index/the-next-evolution-of-the-agents-sdk |
| 12 | OpenAI Agents SDK Sandbox (April 2026) | https://open-techstack.com/blog/openai-agents-sdk-sandbox-agents-april-2026/ |
| 13 | Ai2 — AstaBench Spring 2026 update | https://allenai.org/blog/astabench-update-spring-2026 |
| 14 | Microsoft Agent Framework dotnet-1.4.0 | https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.4.0 |
| 15 | Microsoft CodeAct + Hyperlight | https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/ |
| 16 | A2A governance metadata proposal (Issue #1717) | https://github.com/a2aproject/A2A/issues/1717 |
| 17 | A2A identity verification PR #1696 | https://github.com/a2aproject/A2A/pull/1696 |
| 18 | Agent Payments Protocol (AP2) — Google | https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol |
| 19 | PayPal AP2 community blog | https://developer.paypal.com/community/blog/PayPal-Agent-Payments-Protocol/ |
| 20 | Amazon SageMaker AI agent model customization | https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-sagemaker-ai-ai/ |
| 21 | Beam.ai — Multi-agent orchestration patterns | https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production |
| 22 | Ajentik — Multi-agent systems in production 2026 | https://www.ajentik.com/insights/multi-agent-systems-production-guide |
| 23 | Gemini Deep Research Max launch | https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/ |
