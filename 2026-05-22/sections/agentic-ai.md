# Agentic AI — 2026-05-22

## Top Stories (3-5)

### 1. MCP 2026-07-28 Release Candidate Drops — Biggest Protocol Revision Since Launch, Goes Fully Stateless

**Source:** [MCP Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) | [MCP Tasks Docs](https://modelcontextprotocol.io/extensions/tasks/overview) | [SEP-2663 PR](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663)

The Model Context Protocol released its 2026-07-28 Release Candidate on May 21, 2026 — the largest revision to the protocol since its launch. The headline change: MCP is now **stateless at the protocol layer**, allowing servers to run behind ordinary load balancers without sticky routing. Six Specification Enhancement Proposals (SEPs) collaborate to remove session state from the core, making horizontal scale-out a first-class property of any compliant MCP deployment. The `initialize`/`initialized` handshake is removed; client capabilities now travel in `_meta` fields on every request.

The Tasks extension has been **graduated out of the core spec into an official extension** and completely redesigned for statelessness. Servers return a task handle from `tools/call`; clients drive the lifecycle via `tasks/get`, `tasks/update`, and `tasks/cancel`. The previously-included `tasks/list` method is removed because it cannot be scoped safely without session identity. This architectural split means the core protocol finalizes stability while extensions like Tasks and MCP Apps (server-rendered UIs) evolve on independent timelines. The release candidate is locked as of May 21; the final specification ships July 28, 2026.

For agentic engineers, this is a breaking change with a 10-week migration window. Tier 1 SDKs (C#, Python, TypeScript) are expected to ship support before July 28. The shift to stateless MCP unlocks true cloud-native deployments: MCP servers can now run as ephemeral containers behind round-robin load balancers, enabling cost-effective autoscaling for high-traffic agent tool deployments. Teams relying on `Mcp-Session-Id` sticky routing must refactor before upgrading.

**Key technical details:**
- `initialize`/`initialized` handshake removed (SEP-2575); client info and capabilities travel in `_meta` on each request
- `Mcp-Session-Id` header removed; stateless HTTP now the canonical transport model
- Tasks redesigned as an extension (`io.modelcontextprotocol/tasks`): `tools/call` returns `CreateTaskResult` with `taskId`, TTL, and `pollIntervalMs`; lifecycle driven by `tasks/get`, `tasks/update`, `tasks/cancel`
- `tasks/list` removed for safety reasons (no session scope)
- New MCP Apps extension (SEP-1865) allows servers to return interactive React-based UI components inside supporting host applications
- A formal deprecation policy is introduced: breaking changes must graduate through extensions before touching core
- Authorization redesigned to align more closely with OAuth 2.0 / OpenID Connect deployments
- Tier 1 SDK maintainers have 10-week window (until July 28) to ship support

---

### 2. Google Agent Infrastructure Stack Goes GA — Agent Executor, Agent Sandbox GKE, and Agent Substrate Released Together

**Source:** [Agent Executor Blog](https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime) | [GKE Agent Sandbox Blog](https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate) | [Agent Substrate GitHub](https://github.com/agent-substrate/substrate)

Google announced a three-layer agentic infrastructure stack in the week of May 19-22, 2026, completing the "execution plane" for its broader agentic enterprise platform. **GKE Agent Sandbox** went generally available on May 20, providing secure, stateful, single-replica workloads for executing untrusted LLM-generated code via gVisor isolation. Built as a managed GKE add-on with a Python SDK, it supports warm pools and pod snapshotting for fast startup. Google confirmed working integrations with LangChain, Lovable, and Vertex AI Agentic SDK.

**Agent Executor** (preview, May 20) is Google's open-source distributed agent runtime standard for execution, resumption, and distributed deployment. It is designed to be harness-agnostic and explicitly supports agents built on LangChain/LangGraph, ADK, and any agent using the Agent-to-Agent (A2A) protocol. **Agent Substrate** (open source, Apache 2.0, May 13-22) is the most architecturally novel piece: a new Kubernetes abstraction layer specifically designed for millions of sub-second tool calls. Standard Kubernetes optimizes for thousands of long-running services; Agent Substrate bypasses control-plane limitations for the "chatter" of ultra-dense, short-lived agent workloads at hundreds of millions of registered agents scale.

Together these three layers provide a complete execution stack: Agent Substrate handles scheduling and compute density, Agent Sandbox provides kernel-level isolation and snapshotting, and Agent Executor provides the application-level execution standard with resumption. This is the first production-grade open-source stack that separates these three concerns cleanly, and it explicitly targets the density challenge that has made running millions of simultaneous agents economically impractical on standard cloud infrastructure.

**Key technical details:**
- GKE Agent Sandbox GA: gVisor isolation, pod snapshotting, warm pools, Python SDK (`com.google.adk:google-adk-kotlin-core-android:0.1.0`)
- Agent Substrate: Go-based (78.5%), Apache 2.0, minimal Kubernetes control plane bypass for sub-second tool call chatter
- Agent Substrate supports: ADK session identity, LangChain stateful agents, Claude Code + CodeX multiplex, MCP servers as Substrate Actors
- Agent Executor: preview, integrates with A2A protocol, LangChain/LangGraph, and ADK 2.0
- Agent Substrate v0.0.0 released May 19; GitHub active with 169 stars and 20 contributors as of May 22

---

### 3. Google ADK 2.0 GA + Kotlin/Android 0.1.0 — Graph-Based Multi-Agent Engine Replaces Hierarchical Executor

**Source:** [ADK 2.0 Release](https://github.com/google/adk-python/releases/tag/v2.0.0) | [ADK 2.0 Docs](https://adk.dev/2.0/) | [ADK Kotlin Blog](https://developers.googleblog.com/en/adk-kotlin-android-building-ai-agents/) | [Virtualization Review](https://virtualizationreview.com/articles/2026/05/19/google-io-26-fills-out-enterprise-agent-stack-with-managed-agents-adk-2,-d-,0.aspx)

Google Agent Development Kit 2.0 reached general availability on May 19, 2026, introducing a **breaking architectural change**: `BaseAgent` now subclasses `BaseNode`, and agents execute as nodes within a graph-based Workflow Runtime rather than as standalone hierarchical executors. This is a fundamental shift from ADK 1.x — the framework transitions from an executor model to a directed graph model, enabling non-linear conditional workflows, iterative loops, and explicit branching alongside the previous hierarchical patterns. ADK 2.0 supports three collaborative workflow modes: chat (full user-interaction handoff to subagents), task (collaborative with clarification and auto-return), and single-turn (parallel, no user interaction).

On May 21, Google also released **ADK for Kotlin 0.1.0** and **ADK for Android 0.1.0** (experimental), bringing agentic workflows to JVM backends and Android on-device LLM deployments. ADK now spans Python, Go, Java, Kotlin, TypeScript, and Android — making it the broadest cross-platform agent framework in the ecosystem. The Android variant supports local on-device LLMs via ML Kit GenAI APIs with transparent cloud bridge to Gemini.

ADK 2.0 is positioned as Google's "code-first" rung in a four-tier agent development ladder: Agent Studio (low-code), Managed Agents API (hosted runtime), Antigravity (coding/orchestration surface), and ADK 2.0 (custom agent meshes). All four tiers are connected by the A2A protocol, so an agent built at any tier can be called as a subagent by agents at any other tier. For teams upgrading from ADK 1.x, the `BaseAgent` → `BaseNode` migration is a breaking change requiring workflow graph refactoring.

**Key technical details:**
- `BaseAgent` now subclasses `BaseNode`; all agents evaluated as graph nodes in Workflow Runtime
- Graph execution supports: conditional branching, iterative loops, parallel fan-out, hierarchical team structures
- `A2aAgentExecutor` factory available via `to_a2a()` function (ADK v1.34.0+); A2A persistent task stores now supported
- Collaborative modes: `chat`, `task`, `single_turn` with explicit context propagation across subagent flows
- ADK for Kotlin/Android: `implementation("com.google.adk:google-adk-kotlin-core-android:0.1.0")`
- GCPSkillRegistry and Skill Registry implemented in ADK for composable, reusable agent capabilities
- OAuth PKCE support added to McpToolset in ADK v1.34.0
- 20K GitHub stars on adk-python

---

### 4. Red Hat AI 3.4 + Microsoft Agent 365 — Enterprise AgentOps and Governance Control Planes Arrive

**Source:** [Red Hat AI 3.4](https://datacenternews.asia/story/red-hat-ai-3-4-adds-governance-for-agentic-systems) | [Microsoft Agent 365](https://www.hitechies.com/microsoft-agent-365-autonomous-ai-enterprise-governance-2026/) | [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/) | [MCP .NET Governance](https://devblogs.microsoft.com/dotnet/announcing-agent-governance-toolkit-mcp-extensions-for-dotnet/)

Red Hat AI 3.4 (May 15, 2026) added a dedicated **AgentOps** layer with tracing, observability, identity controls (SPIFFE/SPIRE-based cryptographic workload identity), and lifecycle management for autonomous agents. The platform now includes automated safety testing via Chatterbox Labs and Garak for jailbreak/prompt-injection/bias scanning, with NVIDIA NeMo Guardrails providing runtime safety controls. This positions Red Hat AI as an enterprise-grade AgentOps platform for organizations running hybrid-cloud agent deployments with strict compliance requirements.

Microsoft Agent 365 went live May 1, 2026 as a dedicated governance control plane for enterprise AI agents operating on Microsoft Foundry, Copilot Studio, and third-party platforms. Each agent receives a documented identity, scoped access permissions, and auditable output logs. The companion **Microsoft.AgentGovernance.Extensions.ModelContextProtocol** package (Public Preview) adds one-call governance to any .NET MCP server via `.WithGovernance(...)`, including policy enforcement, startup scanning, runtime tool-call governance, and response sanitization with DID-based agent identity (`did:mcp:anonymous` fallback).

The governance gap is severe: per an April 2026 OutSystems survey, only 12% of enterprises have centralized governance over their agents, while 88% reported confirmed or suspected AI agent security incidents in the past year (Gravitee 2026 survey). A May 2026 CSA research note documented **sub-4-hour weaponization** of a PraisonAI auth-by-default vulnerability (CVE-2026-44338), with scan-to-probe windows compressed to under 4 hours — a new planning baseline for AI infrastructure patch management.

**Key technical details:**
- Red Hat AI 3.4 AgentOps: tracing, observability, SPIFFE/SPIRE identity, lifecycle management; Garak + Chatterbox Labs adversarial scanning
- Microsoft Agent 365: per-agent identity + scoped permissions + audit logs; manages agents across Foundry, Copilot Studio, and third-party platforms
- `Microsoft.AgentGovernance.Extensions.ModelContextProtocol` (Public Preview, .NET 8+): `WithGovernance(...)` on `IMcpServerBuilder`; DID-based agent identity, response sanitization, policy file-based enforcement
- CVE-2026-44338 (PraisonAI): sub-4-hour weaponization window documented by CSA; CSA AICM control baseline recommended
- CSA Agentic AI Red Teaming Guide covers unauthenticated API access, workflow injection, and unauthorized task triggering
- 88% of orgs report AI agent security incidents (Gravitee 2026); only 12% have centralized governance (OutSystems April 2026)

---

### 5. Salesforce Summer '26 Multi-Agent Orchestration + ServiceNow Build Agent in Cursor/Claude Code — Enterprise Platforms Add Production Agentic Depth

**Source:** [Salesforce Summer 2026](https://www.salesforce.com/news/stories/summer-2026-product-release-announcement/) | [Salesforce London Campus](https://www.cxtoday.com/crm/salesforce-expands-london-ai-campus-as-agentforce-adoption-moves-beyond-pilots/) | [ServiceNow Build Agent](https://www.businesswire.com/news/home/20260506008934/en/ServiceNow-Build-Agent-now-works-inside-every-major-AI-coding-tool-governed-by-default)

Salesforce announced its Summer '26 Release (GA June 15, 2026), with the flagship feature being **Multi-Agent Orchestration in Agentforce** — enabling multiple agents to work as a unified team on complex end-to-end workflows with shared context across all channels. The release also includes a new **Help Agent** for Agentforce Self-Service, set up in 6 clicks or fewer via a new conversational Portal UI. Salesforce reports Agentforce is now deployed by 23,000+ customers globally, with the UK alone including Heathrow Airport, NHS Shared Business Services, the National Trust, and multiple police forces. The company is calling this the transition from "pilots to production."

ServiceNow announced at Knowledge 2026 (May 6) that **Build Agent** is now generally available in ServiceNow Studio, with core skills extended into Cursor, Windsurf, Claude Code, and GitHub Copilot — enabling developers to build within any coding environment with full ServiceNow platform context. The App Engine Management Center (AEMC) is now free for all ServiceNow customers, providing deployment approvals, release management, and application lifecycle governance from AI-assisted development to governed deployment. A reimagined AI Agent Studio with guided conversational creation is expected in Q2 2026.

**Key technical details:**
- Salesforce Multi-Agent Orchestration: single customer touchpoint with shared cross-agent context; agents work as unified team on complex workflows
- Agentforce now in 25+ languages for Voice; Hindi launch announced May 19 with deterministic guardrails for action control
- ServiceNow Build Agent GA in Studio (all application scopes); skills available in Cursor, Windsurf, Claude Code, GitHub Copilot
- AEMC freemium tier (deployment approvals, release management) available to all customers
- Build Agent MCP Client and ecosystem integrations expected Q2 2026
- Reimagined AI Agent Studio (guided conversational creation) expected Q2 2026

---

## Deep Dive: Most Important Item

### MCP 2026-07-28 Release Candidate: Stateless Core Changes Everything About How You Deploy Tool Servers

The MCP 2026-07-28 RC is the most architecturally significant protocol event in the agentic stack since MCP's original launch. The shift to a stateless core is not an incremental improvement — it changes the entire operational model for MCP server deployments, eliminating the fundamental constraint that made production scale-out difficult and expensive. Every team running or planning to run MCP servers needs to understand the migration timeline and what it enables.

**What the Protocol Provides**

1. **Stateless core transport** — MCP sessions are eliminated at the protocol layer. Any MCP 2026-07-28 compliant server can be deployed behind a standard load balancer without sticky routing. Client capabilities and identity travel in `_meta` fields on each request.

2. **Tasks as an official extension** — Long-running work is moved from core to an extension (`io.modelcontextprotocol/tasks`). Servers advertise support via `server/discover` capabilities. When a tool call should be long-running, the server returns `CreateTaskResult` with a `taskId`, `ttlMs`, and suggested `pollIntervalMs`. Clients drive via `tasks/get`, `tasks/update`, and `tasks/cancel`.

3. **MCP Apps extension (SEP-1865)** — Servers can now return interactive React-based UI components (dashboards, forms, data visualizations) directly within the conversation window of host applications like Claude Desktop. This unlocks rich tool UIs without separate web deployments.

4. **Authorization aligned with OAuth/OIDC** — The auth model is redesigned to fit standard OAuth 2.0 / OpenID Connect deployments rather than custom MCP session-based auth, making enterprise SSO integration tractable.

5. **Formal deprecation policy** — Breaking changes must graduate through extensions before touching core. Implementers can build on `2026-07-28` with a contractual guarantee that stable features will remain stable.

6. **Tier 1 SDK timeline** — C#, Python, and TypeScript SDKs are expected to ship compliance within the 10-week window before July 28. The `Microsoft.AgentGovernance.Extensions.ModelContextProtocol` package for .NET already supports stateless operation (`WithHttpTransport(o => o.Stateless = true)`).

7. **`tasks/list` removed** — Not safely scopable without session identity. Teams relying on client-initiated task enumeration must redesign to server-directed task creation.

**Why This Matters**

The previous MCP session model required `Mcp-Session-Id` sticky routing, which meant MCP servers could not be horizontally scaled behind standard cloud load balancers. In practice, this forced engineering teams to either run single-instance MCP servers (creating availability and scale bottlenecks) or build custom session affinity infrastructure. The stateless RC eliminates this entirely — a 2026-07-28 MCP server is just an HTTP service, deployable on any cloud infrastructure that handles ordinary web traffic, including serverless functions, container fleets, and CDN edge workers.

This unblocks a class of high-scale production deployments that were previously economically impractical. Consider an enterprise MCP tool server for a document retrieval system serving 50,000 daily active users of an agentic assistant: the old model required stateful session management at scale; the new model allows the tool server to be deployed as a standard autoscaling HTTP service. The Tasks extension handles the "long-running" exception (e.g., background document indexing) without requiring core session state.

The governance implications are also significant. The alignment of MCP authorization with OAuth 2.0/OIDC means enterprises can use their existing identity providers (Okta, Azure AD, etc.) to govern which agents have access to which tool servers, using standard OIDC claims and scopes rather than custom MCP session credentials. Combined with the `.WithGovernance()` tooling in the .NET SDK, this provides a compliance-ready path for regulated industries.

**Architectural Significance**

The 2026-07-28 RC introduces a key architectural primitive: **session-free tool invocation as the default, long-running work as an opt-in extension**. This inverts the previous design where statefulness was embedded in the transport and long-running work was handled by keeping sessions alive. The new pattern separates concerns cleanly: the core protocol handles synchronous tool invocation at cloud scale; the Tasks extension handles asynchronous work via a polling contract; MCP Apps handles UI surfaces via a separate extension. This is the same separation-of-concerns pattern that made REST APIs scalable after the SOAP/session era.

**Competitive Context**

OpenAI's Responses API and Assistants API provide analogous long-running tool execution via `run` objects with polling, but within a proprietary API envelope. The MCP Tasks extension achieves similar semantics with an open, multi-vendor protocol. Google's ADK integrates with both MCP (via McpToolset) and A2A, but A2A is a higher-level agent-to-agent protocol rather than a tool protocol. The stateless MCP RC positions MCP as the dominant open standard for the tool layer of agentic stacks, while A2A operates at the agent coordination layer above it.

---

## Benchmark Data (SWE-bench, GAIA, AgentBench, etc.)

```json
[
  {
    "benchmark": "SWE-bench Verified",
    "date": "2026-05-21",
    "source": "https://benchlm.ai/benchmarks/sweVerified",
    "results": [
      {"agent": "Claude Mythos Preview", "score": 0.939, "metric": "% resolved (500 tasks)"},
      {"agent": "Claude Opus 4.7 (Adaptive)", "score": 0.876, "metric": "% resolved (500 tasks)"},
      {"agent": "GPT-5.3 Codex", "score": 0.850, "metric": "% resolved (500 tasks)"},
      {"agent": "Claude Opus 4.6 (Claude Code)", "score": 0.808, "metric": "% resolved (500 tasks)"},
      {"agent": "Claude Opus 4.5 (Cursor)", "score": 0.809, "metric": "% resolved (500 tasks)"}
    ],
    "notes": "Claude Mythos Preview leads at 93.9% but was withheld from public release (autonomous zero-day discovery). 47 models evaluated as of May 21, 2026. Human-filtered 500-task subset. Claude Opus 4.7 Adaptive at 87.6% is highest publicly available model."
  },
  {
    "benchmark": "SWE-bench Verified* (mini-swe-agent-v2 harness)",
    "date": "2026-05-20",
    "source": "https://benchlm.ai/benchmarks/sweVerifiedArcee",
    "results": [
      {"agent": "Claude Opus 4.6", "score": 0.756, "metric": "% resolved"},
      {"agent": "MiniMax M2.7", "score": 0.754, "metric": "% resolved"},
      {"agent": "GLM-5", "score": 0.728, "metric": "% resolved"},
      {"agent": "Moonshot AI (Kimi)", "score": 0.708, "metric": "% resolved"},
      {"agent": "Arcee AI Trinity-Large-Thinking", "score": 0.632, "metric": "% resolved"}
    ],
    "notes": "Alternative harness (mini-swe-agent-v2) used by Arcee AI for Trinity-Large-Thinking comparison. 5 models evaluated. Reference/display view only on BenchLM. Top-10 spread is 12.4 points."
  },
  {
    "benchmark": "SWE-bench Pro",
    "date": "2026-05-07",
    "source": "https://particula.tech/blog/swe-bench-pro-multi-file-coding-collapse",
    "results": [
      {"agent": "Claude Opus 4.6 (Claude Code)", "score": 0.555, "metric": "% resolved (multi-file PRs)"},
      {"agent": "Claude Opus 4.5 (Cursor)", "score": 0.502, "metric": "% resolved"},
      {"agent": "Claude Opus 4.5 (Auggie)", "score": 0.518, "metric": "% resolved"},
      {"agent": "Claude Opus 4.5 (SEAL)", "score": 0.459, "metric": "% resolved"},
      {"agent": "Gemini 3.1 Pro (stock)", "score": 0.375, "metric": "% resolved"},
      {"agent": "GPT-5.4 (stock)", "score": 0.415, "metric": "% resolved"},
      {"agent": "Mid-tier open-weight models", "score": 0.275, "metric": "% resolved (range 23-32%)"}
    ],
    "notes": "SWE-bench Pro averages 4.1 modified files per task vs. ~1.2 for Verified. Contractor-curated GitHub PRs including cross-file dependency changes, schema migrations. Models that score 80% on Verified collapse to 23-57% on Pro. Harness choice accounts for ~9.5pp swing on a single model."
  },
  {
    "benchmark": "Terminal-Bench 2.0",
    "date": "2026-01",
    "source": "https://arxiv.org/html/2601.11868v1",
    "results": [
      {"agent": "Frontier models/agents (all)", "score": 0.65, "metric": "max observed (89 tasks, CLI environments)"}
    ],
    "notes": "89 containerized CLI tasks inspired by real workflows. Tasks require configuring legacy systems, reimplementing research papers, general software engineering. Each task has containerized environment, instruction, test suite, and reference solution. All frontier models score under 65%. Official evaluation harness: Harbor (harbor-framework/harbor v0.7.1). Published at ICLR 2026."
  },
  {
    "benchmark": "SWE-bench Verified (production coding agents, May 2026 snapshot)",
    "date": "2026-05-22",
    "source": "https://presenc.ai/research/ai-agent-capability-benchmarks-2026",
    "results": [
      {"agent": "Claude Code (Opus 4.7)", "score": 0.77, "metric": "% resolved (approximate)"},
      {"agent": "OpenAI Codex agent (GPT-5 Pro)", "score": 0.75, "metric": "% resolved (approximate)"},
      {"agent": "Cursor Agent (Sonnet 4.6)", "score": 0.65, "metric": "% resolved (approximate)"},
      {"agent": "Aider (Sonnet 4.6)", "score": 0.605, "metric": "% resolved (approximate)"},
      {"agent": "Devin (Cognition AI)", "score": 0.55, "metric": "% resolved (approximate)"},
      {"agent": "Cline (open-weight backed)", "score": 0.415, "metric": "% resolved (approximate)"},
      {"agent": "Open-source agent + Llama 4 70B", "score": 0.285, "metric": "% resolved (approximate)"}
    ],
    "notes": "Snapshot from Presenc AI research synthesis; figures approximate ±3-5pp. Historical comparison: 13% (early 2024) → 49% (early 2025) → 74-78% (May 2026). Frontier coding agents have climbed 5× in 2.5 years. Relative ranking more reliable than absolute scores."
  }
]
```

---

## Architecture / Pattern Notes

### Recursive Self-Delegation (Divide-and-Conquer Agent Architecture)

The newly published **Recursive Agent Optimization (RAO)** paper from CMU and Amazon AGI Labs (arXiv 2605.06639) formalizes a pattern where a *single* LLM policy — with the same weights at every node — recursively spawns instances of itself to handle sub-tasks. Unlike multi-agent systems with specialized sub-agents, RAO trains the delegation strategy via reinforcement learning, teaching the model *when to delegate* and *how to formulate sub-tasks*. The key primitive is a **delegation policy** learned via RL that balances coordination overhead against direct-solve cost, uses depth-level inverse-frequency weighting to prevent over-optimization at shallow recursion levels, and enables up to 10 levels of recursive delegation.

```
[root_agent] (receives task, decides: solve or delegate)
  ↓ delegate (when task is divisible/exceeds context)
[child_agent_1..N] (same weights as root; each receives sub-task)
  ↓ results
[root_agent] (aggregates sub-results, synthesizes final answer)
  ↓ returns
[caller]

Key properties:
- Same policy weights at every recursion level (not specialized sub-agents)
- RL-trained delegation: learns WHEN to delegate, not just HOW
- Depth-level inverse-frequency weighting prevents gradient domination from over-represented depths
- Up to 2.5× wall-clock reduction on parallelizable tasks
- Generalizes to tasks 10× harder than training distribution
- Overcomes context window limits via recursive divide-and-conquer
```

**Mermaid diagram (for downstream renderer):**
- `root` → `delegation_decision` (edge: analyze task complexity)
- `delegation_decision` → `direct_solve` (edge: task fits context, not parallelizable)
- `delegation_decision` → `spawn_children` (edge: task too large or parallelizable)
- `spawn_children` → `child_1..N` (edge: formulate sub-tasks with context)
- `child_1..N` → `root` (edge: return sub-results)
- `root` → `aggregate` (edge: synthesize results from all children)
- `aggregate` → `caller` (edge: final answer)

### Framework Comparison Table

| Framework | Core Abstraction | Graph Type | Best For |
|-----------|-----------------|------------|----------|
| Google ADK 2.0 | `BaseNode` (Agents, Tools, Functions as graph nodes) | Directed graph with conditional/cyclical edges | Multi-model agent meshes, A2A interop, hybrid cloud |
| LangGraph | StateGraph with typed state + checkpointing | Cyclic directed graph | Complex stateful workflows, durable error recovery |
| OpenAI Agents SDK v0.17 | Agent + Tools + Handoff rules | Implicit loop (no explicit graph) | OpenAI-native, rapid prototyping, realtime agents |
| CrewAI | Role-based Crew (agents with roles and goals) | Sequential / hierarchical (configurable) | Role-first prototyping, fast time-to-MVP |
| AutoGen / AG2 | Multi-agent group chat with structured conversation | Conversation graph | Research, multi-model debate, experimental patterns |
| Google Agent Executor | Execution + resumption unit (any A2A/ADK agent) | Distributed execution DAG | Scalable production deployments on GKE/Agent Substrate |

### Stateless-by-Default MCP Server Pattern

The MCP 2026-07-28 RC enables a new **stateless MCP server** deployment pattern that eliminates session-affinity infrastructure. Key implementation elements: (1) no session state stored server-side between requests, (2) client sends full capability context in `_meta` on every request, (3) long-running operations return `taskId` handles for polling rather than holding open connections, (4) server deployed as standard autoscaling HTTP service. This makes MCP servers operationally identical to REST APIs, enabling deployment on serverless platforms (Lambda, Cloud Run, Azure Functions) without sticky routing.

```
[mcp_client] (sends request with capabilities in _meta)
  ↓ HTTP POST (stateless, any backend instance)
[load_balancer] (round-robin, no session affinity)
  ↓ routes to any instance
[mcp_server_instance_N] (stateless; no session store)
  ↓ synchronous: immediate result
[mcp_client] (receives tool result)
  ↓ async: returns CreateTaskResult{taskId, ttlMs, pollIntervalMs}
[mcp_client] (polls tasks/get until complete)
```

---

## Analysis & Impact for Agentic Engineers

- **Adopt MCP 2026-07-28 RC now for new deployments, but plan a migration sprint for existing servers.** The stateless transport is a breaking change (`Mcp-Session-Id` removed, `initialize`/`initialized` handshake removed). Teams with existing MCP servers should audit session usage immediately and begin migration planning. The 10-week window before July 28 is tight for large implementations. However, new deployments should target the RC from day one — stateless HTTP servers are architecturally superior for production scale.

- **Use SWE-bench Pro as your primary benchmark signal for production coding agent selection, not SWE-bench Verified.** Models that score 80% on Verified collapse to 23-57% on Pro depending on harness quality. The 9.5pp intra-model swing from harness choice means that scaffold engineering matters more than model selection in the 50-60% Pro score range. If you are building a coding agent for production refactors involving multiple files, budget for harness engineering rather than defaulting to the most expensive model.

- **If you are deploying MCP servers in regulated environments, implement governance before July 28.** The Microsoft Agent Governance Toolkit for .NET (`Microsoft.AgentGovernance.Extensions.ModelContextProtocol`) provides DID-based agent identity, response sanitization, and policy-file enforcement with a one-call integration. The CSA CVE-2026-44338 incident documents a sub-4-hour scan-to-probe window — treat unpatched AI framework dependencies as equivalent in urgency to critical web framework CVEs.

- **For teams on Google Cloud, the ADK 2.0 + Agent Executor + Agent Substrate stack is now the production-grade path for large-scale agent deployments.** ADK 2.0's graph-based execution engine (breaking change from ADK 1.x) and native A2A interop are mature enough for production use. Teams upgrading from ADK 1.x must refactor `BaseAgent` to `BaseNode`. Teams running millions of agents should evaluate Agent Substrate for the control-plane density benefits vs. standard Kubernetes.

- **Recursive Agent Optimization (RAO) is the most architecturally significant research contribution this week for teams building long-horizon agents.** The key insight: RL-trained delegation policies significantly outperform prompt-engineered delegation heuristics, enabling up to 10 levels of recursive sub-agent spawning with up to 2.5× wall-clock reduction on parallelizable tasks. If you are building agents that process large documents, long code repositories, or multi-step research tasks, the RAO approach (training delegation strategy end-to-end) is worth evaluating — the CMU/Amazon authors report generalization to tasks 10× harder than training distribution.

---

## Key Takeaways (TL;DR)

- **MCP goes fully stateless on May 21:** The 2026-07-28 RC removes sessions, enables load-balancer-transparent horizontal scale, and graduates Tasks to a standalone extension — the biggest protocol change since MCP launched.
- **Google's three-layer infra stack (Agent Sandbox GA + Agent Executor preview + Agent Substrate) provides the first open-source production stack for running millions of simultaneous agents at density.**
- **ADK 2.0 GA (May 19) is a breaking change:** `BaseAgent` is now a graph node; teams on ADK 1.x must migrate; the new graph execution engine enables non-linear, conditional multi-agent workflows natively.
- **SWE-bench Pro is the correct benchmark for production coding agents:** frontier models collapse from ~80% (Verified) to 23-57% (Pro) on realistic multi-file tasks — scaffold quality now matters more than model selection.
- **Agent governance has a critical adoption gap:** only 12% of enterprises have centralized agent governance while CVE-2026-44338 proved AI framework vulnerabilities can be weaponized in under 4 hours.
- **RAO (arXiv 2605.06639, CMU + Amazon) formalizes recursive self-delegation as a trainable strategy:** a single RL-trained policy can divide-and-conquer tasks beyond its context window with up to 2.5× wall-clock improvement over single-agent baselines.

---

*Sources:*
- https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- https://modelcontextprotocol.io/extensions/tasks/overview
- https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663
- https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime
- https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate
- https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox
- https://github.com/agent-substrate/substrate
- https://github.com/google/adk-python/releases/tag/v2.0.0
- https://adk.dev/2.0/
- https://developers.googleblog.com/en/adk-kotlin-android-building-ai-agents/
- https://virtualizationreview.com/articles/2026/05/19/google-io-26-fills-out-enterprise-agent-stack-with-managed-agents-adk-2,-d-,0.aspx
- https://datacenternews.asia/story/red-hat-ai-3-4-adds-governance-for-agentic-systems
- https://www.hitechies.com/microsoft-agent-365-autonomous-ai-enterprise-governance-2026/
- https://devblogs.microsoft.com/dotnet/announcing-agent-governance-toolkit-mcp-extensions-for-dotnet/
- https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/
- https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_research_note_agentic_framework_rapid_exploitation_20260515-csa-styled.pdf
- https://www.salesforce.com/news/stories/summer-2026-product-release-announcement/
- https://www.cxtoday.com/crm/salesforce-expands-london-ai-campus-as-agentforce-adoption-moves-beyond-pilots/
- https://www.businesswire.com/news/home/20260506008934/en/ServiceNow-Build-Agent-now-works-inside-every-major-AI-coding-tool-governed-by-default
- https://arxiv.org/abs/2605.06639
- https://arxiv.org/abs/2605.07728
- https://arxiv.org/html/2605.15871v1
- https://benchlm.ai/benchmarks/sweVerified
- https://benchlm.ai/benchmarks/sweVerifiedArcee
- https://presenc.ai/research/ai-agent-capability-benchmarks-2026
- https://particula.tech/blog/swe-bench-pro-multi-file-coding-collapse
- https://arxiv.org/html/2601.11868v1
- https://github.com/harbor-framework/harbor
- https://github.com/google/adk-python/releases/tag/v0.17.0
- https://github.com/openai/openai-agents-python/releases/tag/v0.17.0
- https://github.com/openai/openai-agents-python/releases/tag/v0.16.0
- https://venturebeat.com/technology/kore-ai-launches-artemis-ai-agent-platform-expands-challenge-to-microsoft-and-salesforce
- https://tokenmix.ai/blog/agent-frameworks-2026-langgraph-crewai-autogen-openai-sdk
