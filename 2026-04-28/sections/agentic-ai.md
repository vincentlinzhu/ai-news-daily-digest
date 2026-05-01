# Agentic AI — 2026-04-28

## Top Stories (3–5)

### 1. Google Unveils Gemini Enterprise Agent Platform — A Full-Stack OS for Autonomous Enterprise Agents
**Source:** [SiliconANGLE](https://siliconangle.com/2026/04/22/google-brings-agentic-development-optimization-governance-one-roof-gemini-enterprise-agent-platform/)

Google Cloud announced the **Gemini Enterprise Agent Platform** at Cloud Next 2026 (Las Vegas, April 22), replacing Vertex AI as the company's unified hub for building, scaling, governing, and optimizing AI agents. All future Vertex AI roadmap work will now ship exclusively through this platform, signaling a complete architectural pivot toward agent-native infrastructure. The announcement framed it explicitly as building an "operating system for enterprise AI," where every worker—technical or not—can access autonomous AI capabilities through the companion Gemini Enterprise application.

The platform is organized around four strategic pillars: **Build** (Agent Studio low-code interface + Agent Development Kit with graph-based orchestration), **Scale** (Agent Memory Bank for persistent long-term context, sub-second cold-start Agent Runtime, multiday workflow support), **Govern** (cryptographic Agent Identity, Agent Gateway as policy enforcement air-traffic-control, Agent Registry for approved tool discovery), and **Optimize** (Agent Simulation on synthetic workloads, Agent Evaluation, Agent Observability for visual trace debugging, Agent Optimizer for automated instruction refinement). GE Appliances, an early adopter, deployed 800+ agents using the platform and cut backorders 25% via a Supplier Collaboration Agent managing 600+ vendors.

Why it matters: this is the first time a hyperscaler has shipped a single platform covering the full agent lifecycle—development, runtime, governance, and continuous improvement—in one coherent surface. Competitors must now match all four pillars or cede enterprise platform positioning. The native MCP integration means agents interact with Google Cloud and Workspace services as standardized tools, reducing bespoke integration code.

**Key technical details:**
- Agent Development Kit now uses a **graph-based framework** for organizing sub-agent networks; supports batch and event-driven agents via BigQuery/Pub/Sub integration
- **Agent Memory Bank** dynamically generates long-term memories from conversations; "Memory Profiles" enable low-latency, high-accuracy recall
- **Agent Identity** issues cryptographic IDs per agent, creating auditable trails mapped to authorization policies
- **Agent Gateway** enforces consistent security policies fleet-wide, including prompt injection detection
- Model Garden provides access to 200+ models: Gemini 3.1 Pro/Flash, Gemma 4, Lyria 3, Claude 3.5 Sonnet/Haiku, and third-party options

---

### 2. OpenAI Agents SDK v0.14.0 — Sandbox Agents and Harness Architecture Transform Coding Agents
**Source:** [OpenAI](https://openai.com/index/the-next-evolution-of-the-agents-sdk) | [GitHub v0.14.0](https://github.com/openai/openai-agents-python/releases/tag/v0.14.0)

On April 15, 2026, OpenAI released v0.14.0 of the Agents SDK, the most structurally significant update since the SDK's debut. The headline feature is **Sandbox Agents**: a persistent, isolated execution workspace that gives agents real filesystem access (read/write/navigate), git integration (clone/branch/commit/push), container support (local, Docker, and seven hosted providers), and snapshot/resume capability for checkpoint recovery. Previously, multi-step coding agents required teams to wire up their own file systems, storage, and compute before testing a single agent interaction. The new harness reduces this to a configuration declaration.

The architectural shift is called the **Harness-Compute Separation**: the control plane (orchestration, tool selection, context management) is decoupled from the execution substrate. This allows the same harness to run locally in a `UnixLocalSandboxClient`, in a `DockerSandboxClient`, or hosted on E2B, Modal, Blaxel, Runloop, Daytona, Vercel, or Cloudflare—without changing agent code. The SDK also now supports 100+ LLMs via the Chat Completions API, breaking its previous implicit lock-in to OpenAI models. Native primitives include `apply_patch` for minimal diffs, AGENTS.md for workspace manifests, MCP tool integration, and prompt injection/exfiltration mitigations baked into the harness.

This update elevates the OpenAI Agents SDK from an orchestration library to a complete agent execution environment. Engineering teams that previously built bespoke infrastructure to run coding agents (file systems, git ops, sandboxes, state persistence) can now replace that custom code with framework primitives, drastically compressing time-to-first-production-agent.

**Key technical details:**
- `Sandbox.snapshot()` / `Sandbox.restore()` enables debugging at specific agent steps and parallel branch exploration
- Storage integrations: S3, GCS, Azure Blob Storage, Cloudflare R2 out of the box
- **Codex CLI v0.125.0** (April 24): adds Unix socket transport, plugin management, permission profile persistence, and reasoning-token usage reporting
- AGENTS.md standard for portable workspace manifests—signals intent to standardize cross-tool agent configuration
- Security: prompt injection detection and exfiltration mitigations built into harness (not prompt-layer workarounds)

---

### 3. AWS Bedrock AgentCore — Managed Harness Launches, Collapses Agent Infrastructure to 3 API Calls
**Source:** [AWS Blog](https://aws.amazon.com/blogs/machine-learning/get-to-your-first-working-agent-in-minutes-announcing-new-features-in-amazon-bedrock-agentcore/) | [SiliconANGLE](https://siliconangle.com/2026/04/22/aws-accelerates-ai-agent-development-amazon-bedrock-agentcore/)

AWS announced new AgentCore capabilities on April 22, 2026, centering on the **Managed Agent Harness** (now in preview)—a declarative infrastructure layer that replaces the full agent orchestration boilerplate with three API calls. Developers declare a model, tools, and instructions; AgentCore stitches together compute, tooling, memory, identity, and security to produce a running agent testable within minutes. The harness is powered by **Strands Agents**, AWS's open-source Python/TypeScript SDK (now at v1.36.0), which is already used in production by Amazon Q Developer, AWS Glue, and VPC Reachability Analyzer.

The companion **AgentCore CLI** manages the full lifecycle from prototype to production in a single terminal workflow, supporting CDK and Terraform (coming soon) for IaC-based reproducible deployments. A new **AgentCore Skills** feature delivers curated platform knowledge to coding assistants (Kiro Power built-in; Claude Code, Codex, and Cursor plugins coming by end of April), solving the "stale context" problem where coding agents give outdated API guidance. Framework support includes LangGraph, LlamaIndex, CrewAI, Google ADK, and OpenAI Agents SDK—making AgentCore intentionally framework-neutral.

The Managed Harness directly challenges both Google's ADK and OpenAI's v0.14.0 Sandbox on the same week, creating a three-way infrastructure battle for who owns the agent execution layer. AWS's differentiation is deep IAM integration, microVM isolation per agent, and native IaC deployment—strengths that resonate with enterprises already running critical workloads on AWS.

**Key technical details:**
- **MicroVM isolation** per agent run—stronger security boundary than container-only approaches
- Session state persisted to durable filesystem; agents can suspend mid-task and resume (human-in-the-loop patterns without custom plumbing)
- Framework-neutral: supports LangGraph, LlamaIndex, CrewAI, Google ADK, OpenAI Agents SDK
- Available in 4 regions (preview): US-West-2, US-East-1, EU-Frankfurt, AP-Sydney; CLI in all 14 AgentCore regions
- No additional charge for harness, CLI, or skills; pay only for underlying compute/model usage

---

### 4. Salesforce Agent Fabric Expansion — MCP Bridge, Visual Canvas, and "Guided Determinism" for Enterprise Multi-Agent Control
**Source:** [Salesforce News](https://www.salesforce.com/news/stories/agent-fabric-control-plane-announcement/) | [MuleSoft/SFDC Developers](https://sfdcdevelopers.com/2026/04/16/mulesoft-agent-fabric-multi-agent-orchestration-governance/)

At TrailblazerDX on April 15, 2026, Salesforce announced a major expansion of **Agent Fabric**, its enterprise control plane for multi-agent orchestration (launched September 2025). The centerpiece is the **MCP Bridge**: a gateway that makes existing APIs agent-ready by implementing MCP without requiring code rewrites, applying standardized rate-limiting and security at the gateway layer. Paired with new **Informatica-hosted MCP servers** for data quality and governance, this gives enterprises a path to agent-enable legacy APIs and data pipelines without a full replatform.

Other additions include an **Agent Scanner** for automated discovery of AI tools and agents across Amazon Bedrock, Azure AI Foundry, and GoDaddy; a **Visual Authoring Canvas** with drag-and-drop workflow design and human-in-the-loop checkpoints; **Trusted Agent Identity** with role-based access control and mobile-based authorization for high-risk actions; and an **AI Gateway** providing standardized token management, compliance, and cross-LLM observability. Simultaneously, Salesforce published its integration pattern guide distinguishing when to use API (deterministic CRUD), MCP (dynamic tool exposure), or A2A (peer agent delegation)—a rare vendor-published decision framework.

The "guided determinism" framing signals Salesforce's thesis: enterprise agents should not be fully autonomous; they need governance rails that ensure predictability at scale. With Alcon's 900-siloed-agent cautionary tale circulating widely, Salesforce is positioning Agent Fabric as the control plane that prevents governance debt from accumulating as enterprises scale agent deployments.

**Key technical details:**
- **MCP Bridge**: no code refactor needed to make existing APIs MCP-compliant; gateway-level rate-limiting and security enforced automatically
- **Agent Registry**: central library of approved tools/skills with discovery and access control
- **Trusted Agent Identity**: RBAC for agents, mobile-based step-up authorization for elevated actions
- **AI Gateway**: cross-LLM token tracking, compliance logging, observability dashboard
- Integrates with Amazon Bedrock, Azure AI Foundry, GoDaddy agent ecosystems via Agent Scanner

---

### 5. ServiceNow Goes AI-Native Across All Products — Context Engine and Open Agent Skills Platform
**Source:** [ServiceNow IR](https://investor.servicenow.com/news/news-details/2026/ServiceNow-moves-beyond-the-sidecar-AI-era-giving-customers-a-complete-AI-native-experience-across-all-products-and-packages/default.aspx)

ServiceNow announced on April 9, 2026 that it is embedding AI natively across its entire product portfolio, explicitly declaring the end of the "sidecar AI era"—where AI is bolted on as an optional feature rather than built into the core system of record. The flagship capability is the **Context Engine**: an enterprise-wide knowledge graph that surfaces relationships, policies, decision history, and organizational context to AI agents at inference time. Agents can now make decisions grounded in full enterprise context, not just the immediate conversation or ticket.

The platform also introduces an **open agent skills framework**: developers can build custom agent capabilities from any tool and deploy them natively into ServiceNow, positioning it as a composable agent runtime rather than a closed workflow engine. AI, data, security, and governance are now baked into all product tiers, not available only in premium SKUs—a significant commercialization shift. Combined with SAP SuccessFactors' simultaneous rollout of Joule as an active orchestrator (Payroll Explanation Agent targeting 50% resolution-time reduction), April 2026 marks the week when major enterprise SaaS platforms stopped treating AI as a feature and started treating it as the runtime.

**Key technical details:**
- **Context Engine**: connects agent decisions to enterprise knowledge graph (relationships, policies, decision history)
- Open agent skills platform: any tool → deploy to ServiceNow; breaks proprietary skill lock-in
- AI/data/security/governance built into all packages (not premium-only)
- SAP parallel: Joule evolves from reactive copilot to active workflow orchestrator across SuccessFactors HR suite

---

## Deep Dive: Most Important Item

### Google Gemini Enterprise Agent Platform — The First Full-Stack Agent OS

The Gemini Enterprise Agent Platform is architecturally significant because it is the first offering from a hyperscaler to unify all four dimensions of the production agent problem—**development, runtime, governance, and continuous optimization**—into a single coherent platform. Every prior offering addressed at most two dimensions (e.g., LangGraph handles development + runtime; AWS IAM handles governance). Google's platform is the first to ship all four as an integrated, opinionated system with a unified API surface.

**What the Platform Provides**

1. **Agent Studio** — Low-code visual builder for business users with drag-and-drop agent logic composition
2. **Agent Development Kit (ADK)** — Graph-based framework for code-first agent network construction, with native BigQuery/Pub/Sub batch and event-driven integrations
3. **Agent Runtime** — Sub-second cold-start provisioning; multiday workflow support for autonomous, long-horizon agents
4. **Agent Memory Bank** — Dynamically generated long-term memory with Memory Profiles for low-latency, high-accuracy recall across sessions
5. **Agent Identity** — Cryptographic per-agent IDs, full audit trail, mapped to authorization policies (IAM integration)
6. **Agent Registry** — Central library of approved tools, skills, and agents; controls which assets agents can discover and invoke
7. **Agent Gateway** — Fleet-wide policy enforcement, acts as "air traffic control" for agent interactions
8. **Agent Security Dashboard** — Real-time prompt injection detection and behavioral monitoring
9. **Agent Simulation** — Pre-production testing on synthetic workloads with virtualized tools
10. **Agent Evaluation** — Continuous scoring of live agents against defined objectives
11. **Agent Observability** — Visual trace debugging of complex agent reasoning chains
12. **Agent Optimizer** — Automated system instruction refinement to improve accuracy over time

**Why This Matters**

The governance gap has been the primary barrier to enterprise agent adoption at scale. Alcon's well-publicized mistake—deploying 900 siloed agents without governance, creating security and compliance exposure—is the canonical enterprise cautionary tale of 2026. Agent Fabric (Salesforce), AgentCore (AWS), and now Gemini Enterprise Agent Platform (Google) are all responding to this same gap, but Google ships the most complete answer: a platform that governs agents *by construction* (cryptographic identity, registry-enforced tool access, gateway policy enforcement) rather than relying on prompt-layer guardrails that can be circumvented.

The Memory Bank architecture is also notable: by generating and curating long-term memories dynamically (rather than forcing developers to manage context windows manually), Google is solving one of the most painful production problems—agents that "forget" across sessions and require users to re-establish context. This is the difference between an agent that is a productivity tool and one that functions like a persistent employee with institutional memory.

The integration of Agent Optimizer closes the improvement loop that no other platform ships end-to-end: an agent runs in production, Evaluation continuously scores it, and Optimizer automatically refines its system instructions. This moves the agent from a static deployed artifact to a continuously improving system—a fundamentally different operational model.

**Architectural Significance**

The platform introduces a new primitive: **the Agent as a managed, governed, continuously-optimizing compute unit** rather than a stateless request handler. This is analogous to what Kubernetes did for container workloads—abstracting away the operational complexity of the execution substrate so engineers focus on agent logic, not infrastructure. The cryptographic identity model is particularly forward-looking: it enables compliance audit trails, fine-grained authorization policies, and eventually, federated agent ecosystems where agents from different organizations can interact with verifiable identity.

**Competitive Context**

| Dimension | Google Gemini GEAP | AWS AgentCore | Salesforce Agent Fabric | OpenAI Agents SDK |
|---|---|---|---|---|
| **Build (Low-code)** | Agent Studio ✓ | CLI-based | Visual Canvas ✓ | None |
| **Build (Code-first)** | ADK (graph) ✓ | Strands (model-driven) ✓ | MuleSoft/Apex | SDK (imperative) ✓ |
| **Runtime** | Agent Runtime (sub-second cold start) | MicroVM harness | MuleSoft runtime | Sandbox (v0.14.0) |
| **Memory** | Memory Bank ✓ | Session persistence | Native CRM memory | Configurable |
| **Identity/Governance** | Cryptographic ID + Gateway | IAM + microVM isolation | Trusted Agent Identity + RBAC | Prompt-level |
| **Continuous Optimization** | Optimizer + Evaluator ✓ | Not shipped | Not shipped | Not shipped |
| **Multi-vendor Models** | 200+ (Model Garden) | Any via Strands/LiteLLM | Multi-LLM via Gateway | 100+ via Chat API |
| **Ecosystem Lock-in** | Moderate (GCP services) | Low (framework-neutral) | High (Salesforce CRM) | Moderate (OpenAI preferred) |

Google leads on the Govern and Optimize pillars; AWS leads on framework neutrality and security isolation; OpenAI leads on developer velocity; Salesforce leads on CRM integration depth.

---

## Benchmark Data (SWE-bench, GAIA, AgentBench, etc.)

```json
[
  {
    "benchmark": "SWE-bench Verified",
    "date": "2026-04-28",
    "source": "https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release",
    "results": [
      {"agent": "Claude Opus 4.7", "score": 87.6, "metric": "% resolved"},
      {"agent": "Claude Opus 4.6 (prev)", "score": 80.8, "metric": "% resolved"},
      {"agent": "Gemini 3.1 Pro", "score": 80.6, "metric": "% resolved"}
    ],
    "notes": "Claude Opus 4.7 leads SWE-bench Verified; sharp long-context regression at 256K–1M tokens noted separately"
  },
  {
    "benchmark": "SWE-bench Pro",
    "date": "2026-04-28",
    "source": "https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release",
    "results": [
      {"agent": "Claude Opus 4.7", "score": 64.3, "metric": "% resolved (single-pass)"},
      {"agent": "GPT-5.4", "score": 57.7, "metric": "% resolved"},
      {"agent": "GPT-5.5", "score": 58.6, "metric": "% resolved (single-pass)"},
      {"agent": "Gemini 3.1 Pro", "score": 54.2, "metric": "% resolved"}
    ],
    "notes": "SWE-bench Pro tests harder, multi-file real-world GitHub issues; Opus 4.7 leads"
  },
  {
    "benchmark": "Terminal-Bench 2.0",
    "date": "2026-04-28",
    "source": "https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/",
    "results": [
      {"agent": "GPT-5.5", "score": 82.7, "metric": "% tasks completed"},
      {"agent": "Claude Opus 4.7", "score": 69.4, "metric": "% tasks completed"},
      {"agent": "Gemini 3.1 Pro", "score": 68.5, "metric": "% tasks completed"}
    ],
    "notes": "Terminal-Bench 2.0 tests complex CLI workflows in real terminal environments; GPT-5.5 leads agentic terminal work"
  },
  {
    "benchmark": "GDPval",
    "date": "2026-04-28",
    "source": "https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/",
    "results": [
      {"agent": "GPT-5.5", "score": 84.9, "metric": "% of 44 knowledge-work tasks completed"}
    ],
    "notes": "GDPval measures economically valuable task completion across 44 knowledge work categories in real computer environments"
  },
  {
    "benchmark": "CursorBench (autonomous coding in Cursor)",
    "date": "2026-04-28",
    "source": "https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release",
    "results": [
      {"agent": "Claude Opus 4.7", "score": 70.0, "metric": "% tasks resolved"},
      {"agent": "Claude Opus 4.6 (prev)", "score": 58.0, "metric": "% tasks resolved"}
    ],
    "notes": "CursorBench measures autonomous coding performance within the Cursor IDE environment; 12pp improvement generation-over-generation"
  },
  {
    "benchmark": "Graph Agent Accuracy (production workloads)",
    "date": "2026-04-28",
    "source": "https://dasroot.net/posts/2026/04/agent-architectures-react-plan-execute-graph-agents/",
    "results": [
      {"agent": "Graph Agents (DAG-based)", "score": 95, "metric": "% task accuracy"},
      {"agent": "Plan-and-Execute", "score": 92, "metric": "% task accuracy"},
      {"agent": "ReAct", "score": 85, "metric": "% task accuracy"}
    ],
    "notes": "Architecture comparison on production workloads; Graph Agents also fastest at 800–1400ms; ReAct uses fewest tokens (2K–3K vs 3K–4.5K)"
  }
]
```

---

## Architecture / Pattern Notes

### Dominant Architecture Pattern: Graph-Based Multi-Agent Orchestration

The week's announcements converge on a shared architectural pattern: **directed graph orchestration of specialized sub-agents**, where each node is a purpose-built agent (not a general-purpose model) and edges represent conditional handoffs based on task state. Google's ADK, AWS's Strands, and LangGraph v1.1 all use graph-based primitives as their core execution model. The shift from flat, sequential agent chains to typed, stateful agent graphs is the defining architectural transition of H1 2026.

In a graph-based system, the orchestrator maintains explicit state as a typed schema (LangGraph's approach), or as a model-driven memory profile (Google Memory Bank / Strands). Conditional edges allow the graph to route based on tool output, confidence scores, or intermediate results—enabling multi-step workflows that recover from failures by backtracking to prior nodes rather than restarting from scratch.

### Framework Comparison Table

| Framework | Core Abstraction | Graph Type | Best For | Production Maturity |
|---|---|---|---|---|
| **LangGraph v1.1** | Typed stateful graph with checkpointing | Cyclic (supports loops) | Complex, fault-tolerant, long-horizon agents | High (34.5M monthly PyPI downloads) |
| **CrewAI v1.12** | Role-based crews with declarative tasks | Acyclic + event-driven Flows | Rapid prototyping, role-first business processes | Medium (5.2M monthly PyPI downloads) |
| **OpenAI Agents SDK v0.14** | Imperative harness with sandbox execution | Handoff chains | Coding agents needing real filesystem/git access | High (OpenAI-native) |
| **AWS Strands v1.36** | Model-driven tool list (no explicit graph) | Implicit (model decides) | Framework-agnostic AWS workloads | Medium-High (production in Q/Glue/VPC) |
| **Google ADK** | Graph-based sub-agent networks | Directed graph | Enterprise GCP workloads, multiday workflows | Medium (newly GA) |
| **AutoGen/AG2** | Multi-agent conversations + group chat | Conversational | Research, experimental multi-agent | Low-Medium (research-oriented) |

### Emerging Pattern: Harness-Compute Separation

Both OpenAI (Agents SDK v0.14.0) and AWS (AgentCore Managed Harness) shipped the same architectural insight this week: **the agent harness (orchestration logic) should be decoupled from the compute substrate (where execution happens)**. In practice, this means:

- The harness declares: model, tools, instructions, security policies, memory configuration
- The compute substrate provides: filesystem, git, container isolation, network access
- Switching from local → Docker → cloud hosted = a config change, not a code rewrite

This pattern mirrors how Kubernetes decoupled application definitions from underlying compute. The implication for engineering teams: invest in harness-portable agent code today, because the execution substrate will continue to evolve (edge compute, specialized agent hardware, confidential computing enclaves).

### Emerging Pattern: Governed Discovery (Agent Registry + MCP)

The Agent Registry (Google), Agent Fabric Scanner (Salesforce), and MCP Bridge are converging on a second pattern: **governed tool and agent discovery**. Rather than hardcoding tool URLs into agent prompts, agents query a centralized registry that enforces access control, version pinning, and audit logging. MCP provides the wire protocol; the registry provides the governance layer. This pattern solves the "900 siloed agents" problem by making it structurally impossible for an agent to access an unapproved tool—policy is enforced at discovery time, not runtime.

---

## Analysis & Impact for Agentic Engineers

- **The infrastructure gap is closing fast**: All three major clouds now offer managed agent harnesses (Google ADK/Runtime, AWS AgentCore Harness, and implicitly Azure AI Foundry). Teams that spent Q1 2026 building bespoke orchestration infrastructure should audit whether those investments are now commoditized—the differentiator is shifting to agent logic, prompting strategy, and evaluation pipelines, not orchestration plumbing.

- **Cryptographic agent identity is becoming a baseline expectation**: Google's per-agent cryptographic IDs, Salesforce's Trusted Agent Identity with RBAC, and Oasis AAM's short-lived privilege sessions all point toward a future where "which agent took this action" is as auditable as "which human took this action." Engineers building production systems today should design with IAM-compatible agent identity from the start, not retrofit it later.

- **Benchmark bifurcation by task type**: GPT-5.5 dominates Terminal-Bench 2.0 (82.7%) while Claude Opus 4.7 leads SWE-bench Pro (64.3%); neither leads on both. This isn't noise—it reflects genuine architectural differences in how models handle CLI interaction patterns vs. code comprehension and patch generation. Agentic engineers should benchmark their specific workload rather than relying on headline scores.

- **The observability stack is maturing but fragmented**: LangSmith, Langfuse (now ClickHouse-owned), Arize Phoenix, and Laminar each excel in different dimensions. The practical recommendation for new production systems is to emit OpenTelemetry spans (vendor-neutral) and route to your preferred backend—ensuring you're not locked into an observability vendor as the ecosystem consolidates.

- **CrewAI's rapid-prototyping position is under pressure**: The 18% token overhead penalty documented in migration guides, combined with Google/AWS/OpenAI all shipping low-friction agent builders (Agent Studio, AgentCore CLI, Sandbox Agents), means CrewAI's "lowest friction to MVP" moat is narrowing. Teams using CrewAI for prototyping should plan migration paths to LangGraph for production workloads exceeding 20 agent interactions.

---

## Key Takeaways (TL;DR)

- **Google, AWS, and OpenAI all shipped major agent infrastructure this week**, converging on harness-compute separation and managed execution environments—the "infrastructure gap" in agentic AI is closing rapidly and will be largely commoditized by H2 2026.
- **Cryptographic agent identity is the new governance baseline**: Google GEAP, Salesforce Agent Fabric, and Oasis AAM all independently landed on per-agent identity as the foundation for enterprise-grade governance and auditability.
- **GPT-5.5 owns terminal/CLI tasks (82.7% Terminal-Bench 2.0); Claude Opus 4.7 owns code understanding (87.6% SWE-bench Verified, 64.3% Pro)**—model selection for agentic workloads must be task-specific, not based on headline leaderboard position.
- **Enterprise SaaS platforms (ServiceNow, SAP, Salesforce) are now AI-native at the platform level**—the "sidecar AI" era is officially over; agents are now the primary interaction model for enterprise workflows, not a premium add-on.
- **Graph-based multi-agent orchestration is the dominant production architecture** across Google ADK, LangGraph, and AWS Strands; the shift from flat chains to typed, stateful agent graphs is the defining architectural pattern of H1 2026.
- **MCP + Agent Registry = governed tool discovery**—the combination of MCP as a wire protocol and centralized registries (Google Agent Registry, Salesforce Agent Fabric Scanner) is solving the "900 siloed agents" enterprise governance problem at the infrastructure layer.

---

*Sources:*

- https://siliconangle.com/2026/04/22/google-brings-agentic-development-optimization-governance-one-roof-gemini-enterprise-agent-platform/
- https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-enterprise-agent-platform/
- https://medium.com/google-cloud/what-is-gemini-enterprise-agent-platform-ff621edcbe3d
- https://virtualizationreview.com/articles/2026/04/24/google-cloud-next-26-gemini-enterprise-agent-platform-leads-ai-centric-news.aspx
- https://openai.com/index/the-next-evolution-of-the-agents-sdk
- https://github.com/openai/openai-agents-python/releases/tag/v0.14.0
- https://www.abhs.in/blog/openai-agents-sdk-evolution-sandbox-harness-april-2026
- https://www.idlen.io/news/openai-agents-sdk-sandbox-harness-codex-filesystem-tools-april-2026
- https://developers.openai.com/codex/changelog/
- https://aws.amazon.com/blogs/machine-learning/get-to-your-first-working-agent-in-minutes-announcing-new-features-in-amazon-bedrock-agentcore/
- https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/
- https://siliconangle.com/2026/04/22/aws-accelerates-ai-agent-development-amazon-bedrock-agentcore/
- https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk
- https://strandsagents.com/
- https://www.salesforce.com/news/stories/agent-fabric-control-plane-announcement/
- https://sfdcdevelopers.com/2026/04/16/mulesoft-agent-fabric-multi-agent-orchestration-governance/
- https://www.salesforce.com/blog/agentforce-mcp/
- https://www.salesforce.com/blog/how-to-choose-integration-pattern-for-agentforce/
- https://investor.servicenow.com/news/news-details/2026/ServiceNow-moves-beyond-the-sidecar-AI-era-giving-customers-a-complete-AI-native-experience-across-all-products-and-packages/default.aspx
- https://www.aitechsuite.com/ai-news/sap-unveils-agentic-ai-to-automate-complex-hr-workflows-and-eliminate-administrative-bloat
- https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release
- https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/
- https://www.tbench.ai/leaderboard/terminal-bench/2.0
- https://benchlm.ai/benchmarks/terminalBench2
- https://agentmarketcap.ai/blog/2026/04/12/react-vs-plan-execute-vs-tree-of-thought-production-2026
- https://dasroot.net/posts/2026/04/agent-architectures-react-plan-execute-graph-agents/
- https://tokenmix.ai/blog/agent-frameworks-2026-langgraph-crewai-autogen-openai-sdk
- https://blog.softmaxdata.com/definitive-guide-to-agentic-frameworks-in-2026-langgraph-crewai-ag2-openai-and-more/
- https://tokenmix.ai/blog/crewai-to-langgraph-migration-guide-2026
- https://mcpplaygroundonline.com/blog/mcp-2026-roadmap-whats-changing-for-developers
- https://dev.to/agdex_ai/mcp-vs-a2a-the-two-protocols-every-ai-agent-developer-needs-to-understand-2026-1jn7
- https://oasis.security/blog/introducing-oasis-agentic-access-management
- https://konghq.com/agent-gateway
- https://www.certiv.ai/product/
- https://laminar.sh/article/2026-04-23-top-6-agent-observability-platforms
- https://dev.to/chunxiaoxx/ai-agent-observability-in-2026-openai-agents-sdk-langsmith-and-opentelemetry-3ale
- https://prodsens.live/2026/04/15/17-weeks-running-7-autonomous-ai-agents-in-production-real-lessons-and-real-numbers/
- https://ecommercenews.uk/story/ge-appliances-rolls-out-800-ai-agents-across-operations
- https://autonainews.com/salesforce-oracle-servicenow-bet-big-on-agentic-ai-integrations-this-week/
