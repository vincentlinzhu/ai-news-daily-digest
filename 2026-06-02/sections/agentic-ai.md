# Agentic AI — 2026-06-02

## Top Stories (3-5)

### 1. OpenAI Ships "Next Evolution" of Agents SDK — Sandbox Agents Now GA — Model-Native Harness for Long-Horizon Work

**Source:** [OpenAI Blog](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) | [OpenAI Developer Community](https://community.openai.com/t/the-next-evolution-of-the-agents-sdk/1379072) | [OpenAI API Docs](https://developers.openai.com/api/docs/guides/agents/sandboxes)

Today (June 2, 2026), OpenAI officially announced the general availability of the "next evolution" of the Agents SDK, which consolidates a series of capabilities that began shipping in April 2026 into a production-ready surface. The centrepiece is **Sandbox Agents** — a first-class SDK primitive that gives agents a persistent, isolated workspace with a real filesystem, shell access, and configurable network egress. Sandbox Agents landed in Python (v0.14.0, April 15), with TypeScript support marked as "coming soon" in the latest announcement. As of this writing the SDK is at v0.17.4 (released May 26), with 26,000+ GitHub stars and 280 contributors.

The architectural story is a clean separation between the **harness** (orchestration: instructions, tool dispatch, handoffs, approval gates, tracing) and the **sandbox** (compute: files, commands, packages, ports, provider-specific isolation). The two layers can run on the same machine or separately, which keeps model-generated code execution away from orchestration credentials and secrets. A `Manifest` abstraction makes workspaces portable across providers — local Unix, local Docker, hosted Modal, or E2B — with cloud storage mounts from S3, GCS, Azure Blob, and Cloudflare R2. The SDK also ships snapshotting and rehydration so a long-running agent can survive sandbox expiry or crash without restarting from scratch.

This matters for agentic engineers because it closes the infrastructure gap between "demo-grade" tool-calling agents and "production-grade" systems that need to inspect real repos, run CI pipelines, patch code across files, and carry workspace state across sessions. Previously, teams had to build their own sandboxing layer (Docker + volume mounts + restart logic). OpenAI now provides that as a first-class, versioned, SLA-backed primitive with consistent API semantics across providers.

**Key technical details:**
- `SandboxAgent` is a subclass of `Agent`; existing code migrates by swapping `Agent` → `SandboxAgent` and adding a `SandboxRunConfig` with a chosen client
- Supported sandbox clients: `UnixLocalSandboxClient`, `DockerSandboxClient`, hosted providers (Modal, E2B)
- Hosted Shell tool: CLI-grade task execution inside an isolated container via the Responses API (build/test/lint steps)
- Skills API: package reusable, versioned workflows as "skills" agents can mount via a manifest file
- Network-enabled containers: explicit opt-in outbound network access per container
- Snapshotting: `RunState` serialization lets a runner resume from last saved sandbox state on a fresh container
- Security: artifact sources constrained to base directory (v0.17.0 fix); Unix filesystem permissions map to model read/write rings
- Pricing: standard token + tool-use API pricing; no additional sandbox surcharge

---

### 2. Microsoft Build 2026: Windows Becomes an Agent Runtime — Agent Framework 1.0 GA + Agent 365 + Agent Governance Toolkit

**Source:** [Microsoft Build Coverage (byteiota)](https://byteiota.com/microsoft-build-2026-windows-is-now-an-agent-platform/) | [Agent Framework 1.0 Announcement](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) | [Agent 365 GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) | [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) | [MAF .NET Blog](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/)

Microsoft Build 2026 (June 2–3, Fort Mason, San Francisco) is anchored on a single architectural thesis: Windows is now a runtime for registering, orchestrating, and deploying persistent AI agents. Three distinct but interlocking products underpin this: the **Microsoft Agent Framework (MAF) 1.0** (unified AutoGen + Semantic Kernel SDK, GA April 2026), **Agent 365** (enterprise observability and governance control plane, GA May 1), and the **Agent Governance Toolkit** (runtime policy enforcement, v4.0.0 released June 1, 2026). Together, they represent the most comprehensive enterprise-facing agentic stack any hyperscaler has shipped, covering the full spectrum from developer SDK to OS-level runtime to security governance.

MAF 1.0 unifies the two most widely used Microsoft agent projects — AutoGen (multi-agent orchestration research) and Semantic Kernel (enterprise memory and plugin architecture) — into a single, commercially supported SDK for .NET (C# primary) and Python. The core programming model exposes four primitives: Agent definitions, Workflows (graph-based executor supporting sequential, concurrent, handoff, group-chat, and Magentic-One patterns), Memory (persistent storage backed by Azure Cosmos DB or Redis), and Connectors (Azure OpenAI, standard OpenAI, GitHub Copilot SDK). Long-running workflows support checkpointing and hydration, human-in-the-loop approval gates, streaming, and pause/resume. The NuGet package is `Microsoft.Agents.AI` (v1.7.0 at Build); the Python equivalent via pip. All patterns support streaming, and the framework natively bridges A2A (Agent-to-Agent protocol) and MCP for inter-agent and tool interoperability.

Agent 365 ($15/user/month) provides a cross-vendor control plane for observing, governing, and securing agents regardless of what framework or cloud they are built on. Starting June 2026, Microsoft Defender adds **asset context mapping** for each agent: which devices it runs on, which MCP servers are configured for it, what identities are associated with it, and what cloud resources those identities can reach. Policy-based controls and runtime blocking/alerting via Intune and Defender enter public preview this month. Ecosystem partners whose agents are now fully manageable via Agent 365 include Genspark, Zensai, Egnyte, Zendesk, Kasisto, Kore, and n8n. The **Agent Governance Toolkit** (open source, MIT) covers all 10 OWASP Agentic Top 10 risks, with 9,500+ tests and five SDK distributions (Python, TypeScript, .NET, Rust, Go). Policy evaluation runs in under 0.1ms and supports YAML, Rego (OPA), and Cedar policy languages.

**Key technical details:**
- MAF 1.0 installs via `pip install microsoft-agents-ai` or NuGet `Microsoft.Agents.AI` v1.7.0
- Orchestration patterns: sequential, concurrent, handoff, group-chat, Magentic-One — all stable in v1.0 GA
- Memory: built-in persistent memory backed by Azure Cosmos DB or Redis with circuit breakers
- Agent Governance Toolkit packages: `agent-governance-toolkit-core`, `-runtime`, `-sre`, `-cli` (or `[full]`)
- AGT covers: deterministic policy enforcement at action layer, Ed25519 cryptographic identity, SPIFFE/SVID trust credentials, 4-tier privilege rings, saga orchestration, kill switch, SLOs + chaos engineering
- Agent 365 Defender integration: MCP server mapping per agent + blast-radius analysis entering public preview June 2026
- Windows Agent Runtime: gRPC-based Cross-Agent Communication Bus; Declarative Agent Manifest (`agent.json`); Agent Registration Service daemon
- Framework interop: A2A + MCP bridges built into AGT core; works across 20+ third-party frameworks

---

### 3. NVIDIA Releases Open-Source Physical AI Agent Toolkit at GTC Taipei — Cosmos 3 Omni-Model Ships

**Source:** [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-releases-major-collection-of-open-source-agent-tools-and-skills-for-physical-ai) | [NVIDIA Investor](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Releases-Major-Collection-of-Open-Source-Agent-Tools-and-Skills-for-Physical-AI/default.aspx) | [Hugging Face / Cosmos 3](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai) | [NVIDIA/skills GitHub](https://github.com/nvidia/skills/)

At GTC Taipei (June 1–2, 2026), NVIDIA announced a major open-source collection of **physical AI agent skills and tools** spanning its entire physical AI stack: Cosmos (world foundation models), Omniverse (simulation and digital twins), Isaac (robotics), Metropolis (vision AI), Alpamayo (autonomous driving), and Jetson (edge AI). All skills are available on GitHub and the `skills.sh` marketplace for use with any coding agent — Claude Code, Cursor, Copilot, Gemini CLI. Simultaneously, **NVIDIA Cosmos 3** launched on Hugging Face as the first open omni-model combining world generation, physical reasoning, and action generation in a single architecture. Two variants ship: Cosmos 3 Nano (16B params, 8B reasoner + 8B generator, RTX PRO 6000-class hardware) and Cosmos 3 Super (64B params, Hopper/Blackwell GPUs for large-scale SDG).

The architectural significance is that NVIDIA is converting its entire library ecosystem — previously requiring expert configuration per tool — into **agent-callable, reproducible skill files** that any coding agent can execute without human guidance. The `NVIDIA/skills` GitHub repo is a daily-synced catalog of skills from product repos, each structured as a `SKILL.md` + `skills.sh.json` sidecar for marketplace metadata. This creates a new distribution model: instead of documentation, complex NVIDIA pipelines are delivered as agent-readable instruction sets that specify which tools to call, what outputs to produce, and how to validate results. Physical AI Launchables on NVIDIA Brev offer instant, pre-configured skill execution environments for synthetic data generation workflows (Neural Reconstruction, Video Augmentation, Defect Image Generation).

This is the most concrete example to date of a hardware/platform vendor rethinking their SDK as an agentic primitive rather than a human-readable API. It signals an emerging pattern: major platform vendors publishing "agent skills" as the primary interface for their tooling, effectively making agent-readiness a first-class product requirement. Microsoft (Azure), CoreWeave, and Nebius are integrating these skills into their cloud services for scaled synthetic data generation.

**Key technical details:**
- Cosmos 3 Nano: 16B params (8B reasoner + 8B generator), targets RTX PRO 6000, available at `nvidia/Cosmos3-Nano` on HuggingFace
- Cosmos 3 Super: 64B params (32B reasoner + 32B generator), Hopper/Blackwell, available at `nvidia/Cosmos3-Super`
- Cosmos 3 integrates with HuggingFace Diffusers via `Cosmos3OmniPipeline`
- Skills distributed as `SKILL.md` files (compatible with Claude Code, Cursor, Gemini CLI skill systems)
- Skills catalog: `omniverse-cad-to-simready`, `physical-ai-neural-reconstruction`, `physical-ai-defect-image-generation`, `physical-ai-video-data-augmentation`, and more
- Trust: each skill signed with OMS; trust anchor at `nv-agent-root-cert.pem`
- Brev Launchables: pre-configured environments for instant execution of SDG skills; no local GPU required

---

### 4. Google ADK 2.0 GA — Graph-Based Workflows + Collaborative Agents + Kotlin/Android Support

**Source:** [ADK 2.0.0 Release](https://github.com/google/adk-python/releases/tag/v2.0.0) | [ADK 2.1.0 Release](https://github.com/google/adk-python/releases/tag/v2.1.0) | [Google Cloud Blog — I/O '26](https://cloud.google.com/blog/topics/developers-practitioners/io26-news-for-agent-developers-on-google-cloud)

Google's Agent Development Kit (ADK) reached General Availability with `v2.0.0` on May 19, 2026, followed by `v2.1.0` on May 23. The GA release introduces two major architectural primitives: **graph-based workflows** (deterministic directed-graph execution replacing purely prompt-driven orchestration) and **collaborative agents** (coordinator/subagent task delegation with three explicit operating modes). ADK Kotlin (beta) launched simultaneously, enabling on-device mobile agents using Gemini Nano with hybrid offload to cloud Python agents. A new **Agents CLI** packages Google's expert knowledge for ADK — turning any AI coding agent into an expert at the Google Cloud agent stack, including eval, deploy, observability, and publishing workflows.

Graph-based workflows in ADK 2.0 define agent logic as directed graphs of execution nodes (code functions, AI agents, tools, human input gates) and edges. Developers can mix graph-mode (deterministic, code-defined routing) with dynamic-mode (full programming language control for loops, branching) within the same system. Collaborative workflows use a coordinator agent that delegates to subagents via explicit modes: `chat` (full multi-turn conversation, "you are sub-agents"), `task` (clarification loop with automatic return), and `single-turn` (parallel "agent as tool" execution). The v2.1.0 release added chart generation for data agents, template/snapshot-based sandbox creation, and improved telemetry with `user.id` in gen_ai log records.

**Key technical details:**
- Install: `pip install google-adk==2.0.0` (v2.0.0 is GA for Python; earlier versions remain available)
- Graph-based workflows: fan-out/fan-in parallel tasks, nested reusable workflows, `FanIn` node for collecting parallel outputs
- Collaborative agents: three delegation modes — `chat`, `task`, `single-turn`; context variable propagation across agent boundaries
- ADK Kotlin (beta): on-device mobile agents, Gemini Nano hybrid orchestration
- Agents CLI: converts any AI coding agent into an ADK expert (eval, deploy, observability, publish)
- Managed Agents API: one-command deployment to Google-hosted environments
- Telemetry: `user.id` enrichment in gen_ai log records (v2.1.0); MCP tool error handling improved

---

### 5. MCP 2026-07-28 Release Candidate: Protocol Goes Fully Stateless — 10-Week Validation Window Open

**Source:** [MCP Blog RC Announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) | [byteiota Breakdown](https://byteiota.com/mcp-goes-stateless-what-the-july-28-spec-rc-breaks/) | [DEV Community Migration Guide](https://dev.to/akaranjkar08/mcp-spec-ships-july-28-every-breaking-change-and-how-to-migrate-4co8) | [MCP.Directory Explainer](https://mcp.directory/blog/mcp-2026-07-28-release-candidate)

The MCP `2026-07-28` Release Candidate — the largest revision of Model Context Protocol since its November 2024 launch — locked on May 21, 2026, opening a 10-week validation window. The headline change is the removal of protocol-level sessions: the `initialize`/`initialized` handshake (SEP-2575) and `Mcp-Session-Id` header (SEP-2567) are both eliminated. Protocol version, client info, and capabilities that previously required a one-time handshake now travel in `_meta` on every request, enabling any request to land on any server instance with no sticky session requirements. This is a stateless-first architecture compatible with ordinary load balancers and commodity HTTP infrastructure.

Beyond sessions, the RC introduces a required operability layer for Streamable HTTP transport: every request must now include `Mcp-Method` (the operation, e.g. `tools/call`) and `Mcp-Name` (the tool or resource name) headers. Servers must reject requests where headers disagree with the body. This makes header-based routing and rate-limiting at the API gateway level possible without body inspection — a significant operational improvement for high-volume deployments. The RC also introduces HTTP-style caching metadata (SEP-2549) and W3C Trace Context propagation (SEP-414) for distributed tracing. Three primitives (Roots, Sampling, Logging) are officially deprecated but guaranteed to remain functional for at least 12 months under the new formal deprecation lifecycle (SEP-2577 + SEP-2596). Tasks and MCP Apps graduate to the new formal Extensions framework.

**Key technical details:**
- RC locked May 21, 2026; final spec publishes July 28, 2026
- Breaking: `initialize`/`initialized` handshake removed; `Mcp-Session-Id` header removed
- Breaking: `Mcp-Method` and `Mcp-Name` headers now required on all Streamable HTTP requests; servers must reject mismatches
- `server/discover` method allows clients to fetch server capabilities on demand (replaces session initialization)
- Deprecated (12-month removal guarantee): Roots, Sampling, Logging
- Extensions framework: reverse-DNS-identified extensions negotiated via capability maps; Tasks + MCP Apps are first two official extensions
- Authorization: hardened OAuth 2.1 + OIDC alignment, Dynamic Client Registration, step-up auth, RFC 9207 compliance
- Tier 1 SDKs (official TypeScript + Python) expected to ship support within the 10-week window
- Migration risk profile: local STDIO users largely unaffected; remote server operators with sticky routing, Redis session stores, or SSE for list-change detection must adapt before July 28

---

## Deep Dive: Most Important Item

### Microsoft's Tripartite Agentic Stack: Agent Framework 1.0 + Agent 365 + Agent Governance Toolkit

The convergence of the Microsoft Agent Framework 1.0 (developer SDK), Agent 365 (enterprise control plane), and the Agent Governance Toolkit (runtime policy enforcement) represents the most architecturally complete agentic production stack announced by any major vendor to date. Unlike Google (ADK, model-native), OpenAI (Agents SDK, API-native), or Anthropic (Claude Agent SDK, opinionated harness), Microsoft is targeting enterprise IT departments who need to govern agents they did not build, running on infrastructure they do not own. This tripartite structure — SDK → control plane → governance — mirrors how Microsoft won enterprise cloud: Azure (IaaS), Azure AD/Entra (identity), Defender (security), and it is a deliberate replication of that playbook for the agentic layer.

**What the Platform Provides**

1. **Microsoft Agent Framework 1.0 (SDK Layer):** Open-source, MIT licensed, .NET and Python. Unifies AutoGen's multi-agent orchestration (sequential, concurrent, group-chat, Magentic-One patterns) with Semantic Kernel's enterprise memory (Cosmos DB/Redis), plugin architecture, and connector ecosystem. Key primitives: `Agent`, `Workflow`, `Memory`, `Connector`. Graph-based execution with checkpointing. Human-in-the-loop approval gates. Streaming throughout. A2A + MCP bridges built-in. Install: `pip install microsoft-agents-ai` or `Microsoft.Agents.AI` NuGet v1.7.0.

2. **Windows Agent Runtime (OS Layer):** Announced at Build 2026 as the OS mechanism for treating agents as persistent first-class entities. Components: Agent Registration Service daemon, Declarative Agent Manifest (`agent.json` schema versioned in Git), Cross-Agent Communication Bus (gRPC pub/sub), Memory Service (encrypted, user-controllable conversational context cache). This moves agent lifecycle management from application code into the operating system.

3. **Agent 365 (Control Plane Layer):** $15/user/month cross-vendor observability and governance. Discovers shadow AI agents, maps asset context (devices, MCP servers, identities, cloud resources) per agent, enforces policy-based controls via Intune, provides runtime blocking and alerting via Defender. GA partners: Genspark, Zensai, Egnyte, Zendesk, Kasisto, Kore, n8n. No integration work required by IT.

4. **Agent Governance Toolkit v4.0.0 (Policy Layer):** Open-source, MIT. 9,500+ tests. Covers all 10 OWASP Agentic Top 10 risks. Five SDK distributions (Python, TypeScript, .NET, Rust, Go). Modules: Agent OS (stateless policy engine, YAML/Rego/Cedar, <0.1ms evaluation), AgentMesh (Ed25519 identity, SPIFFE/SVID, 0–1000 trust scores), Agent Runtime (4-tier privilege rings, saga orchestration, termination control, append-only audit log), Agent SRE (SLOs, error budgets, chaos engineering, circuit breakers). Works across 20+ third-party frameworks; not locked to MAF.

5. **Agents CLI:** Expert tooling that turns any AI coding agent (Claude Code, Cursor, Gemini CLI, Copilot) into a MAF expert, covering ADK eval, deploy, observability, and publishing workflows.

**Why This Matters**

The enterprise governance gap for agentic AI has been the dominant unsolved problem since agents moved into production in late 2025. Most governance tooling has been ad-hoc: custom audit logs, per-framework policy middleware, and manual identity assignment. The Agent Governance Toolkit formalizes what deterministic enforcement looks like at the action layer — policies evaluated before execution, cryptographic accountability on every inter-agent delegation, privilege rings that constrain what model-generated code can actually do on the underlying system. At <0.1ms policy evaluation time, this is not a meaningful runtime overhead.

The Agent 365 + Defender integration entering public preview this month is the key piece for large enterprise IT. Starting June 2026, security teams will have the same asset-context view for agents that they have had for endpoints since Defender ATP launched: device linkage, identity mapping, blast-radius assessment, behavioral anomaly detection. This matters because the dominant enterprise concern with agentic AI is not model quality — it is the "what can this agent actually do and to what?" question, which is an identity and access management problem first and a model problem second. Orchid Security's simultaneous announcement (May 28) of delegation-aware identity enrichment for AI agents highlights the same gap from the IAM vendor side: the "Agent AI Authority Gap" is an industry-recognized problem with commercial solutions now available.

**Architectural Significance**

Microsoft is introducing a new pattern: **OS-mediated agent lifecycle management**. Previous frameworks treated agents as application-level constructs (processes, goroutines, async tasks) that lived and died within the application boundary. The Windows Agent Runtime treats agents as OS-registered entities with persistent identities, health monitoring, versioning, and a gRPC-based communication bus — analogous to how Windows Services work for long-running processes. This is a meaningful primitive shift: it means agent identity, lifecycle, and inter-agent communication move below the application framework layer into the operating system, making agents first-class citizens of the computing environment rather than orchestrated application threads.

**Competitive Context**

- **OpenAI Agents SDK** is provider-native (OpenAI models preferred) and application-layer only; no governance or control plane
- **Google ADK 2.0** provides strong graph-based orchestration with Managed Agents API for hosted deployment, but governance is left to application developers
- **LangGraph** is the production default for stateful graph orchestration but provides no governance, identity, or OS-level runtime
- **Anthropic Claude Agent SDK** powers Claude Code internally but is not yet a public enterprise governance platform
- Microsoft is the only major vendor shipping OS-level agent runtime + cross-vendor control plane + open-source governance toolkit simultaneously — positioning for IT department buyer, not developer buyer

---

## Benchmark Data (SWE-bench, GAIA, AgentBench, etc.)

```json
[
  {
    "benchmark": "SWE-bench Verified",
    "date": "2026-06-02",
    "source": "https://presenc.ai/research/ai-agent-capability-benchmarks-2026",
    "results": [
      {"agent": "Claude Code (Opus 4.7)", "score": 0.77, "metric": "task completion rate"},
      {"agent": "OpenAI Codex agent (GPT-5 Pro)", "score": 0.75, "metric": "task completion rate"},
      {"agent": "Cursor Agent (Sonnet 4.6)", "score": 0.65, "metric": "task completion rate"},
      {"agent": "Aider (Sonnet 4.6)", "score": 0.60, "metric": "task completion rate"},
      {"agent": "Devin (Cognition AI)", "score": 0.55, "metric": "task completion rate"},
      {"agent": "Cline (open-weight)", "score": 0.41, "metric": "task completion rate"},
      {"agent": "Open-source agent + Llama 4 70B", "score": 0.28, "metric": "task completion rate"}
    ],
    "notes": "May 2026 snapshot. Scores are reported as mid-point of published ranges. NOTE: SWE-bench Verified is now widely considered contaminated — Berkeley RDI audit found all 500 Verified instances exploitable to achieve 100% with zero tasks solved. OpenAI has stopped reporting Verified scores internally. Use SWE-bench Pro (SEAL) or FeatureBench for procurement decisions."
  },
  {
    "benchmark": "SWE-bench Pro (SEAL Leaderboard)",
    "date": "2026-06-02",
    "source": "https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough",
    "results": [
      {"agent": "Claude Opus 4.5", "score": 0.459, "metric": "resolve rate"},
      {"agent": "Claude Opus 4.5 (SWE-bench Verified same model)", "score": 0.809, "metric": "resolve rate (Verified — for comparison)"}
    ],
    "notes": "1,865 multi-language tasks, 107 lines avg across 4.1 files, 250-turn limit, identical tooling for all models. The 35-point collapse from Verified to Pro score on the same model illustrates benchmark contamination magnitude. Contamination-resistant design. Scale AI SEAL leaderboard runs all models through standardized harness."
  },
  {
    "benchmark": "FeatureBench (ICLR 2026)",
    "date": "2026-06-02",
    "source": "https://agentmarketcap.ai/blog/2026/06/24/featurebench-63-point-cliff-feature-delivery-frontier-coding-agents",
    "results": [
      {"agent": "Claude Opus 4.5", "score": 0.110, "metric": "feature resolve rate"},
      {"agent": "GPT-5.1-Codex (medium reasoning)", "score": 0.125, "metric": "feature resolve rate"},
      {"agent": "Claude Opus 4.5 (SWE-bench Verified — same model, same week)", "score": 0.744, "metric": "resolve rate — for comparison"}
    ],
    "notes": "ICLR 2026 paper. Measures feature delivery (multi-file architectural changes, not single-file bug patches). Same open-source Python repos as SWE-bench Verified. The 63.4-point cliff between Verified and FeatureBench scores for the same model demonstrates that SWE-bench Verified predicts almost nothing about real feature delivery capability. Frontier labs have not yet trained against FeatureBench task distribution."
  },
  {
    "benchmark": "GAIA (General AI Assistants)",
    "date": "2026-06-02",
    "source": "https://presenc.ai/research/ai-agent-capability-benchmarks-2026",
    "results": [
      {"agent": "Top frontier agent (Anthropic/OpenAI)", "score": 0.65, "metric": "overall (avg L1/L2/L3)"},
      {"agent": "Top frontier agent — Level 1", "score": 0.80, "metric": "Level 1 task completion"},
      {"agent": "Top frontier agent — Level 2", "score": 0.64, "metric": "Level 2 task completion"},
      {"agent": "Top frontier agent — Level 3", "score": 0.40, "metric": "Level 3 task completion"},
      {"agent": "Mid-tier production agent", "score": 0.51, "metric": "overall"},
      {"agent": "Open-source agent (Llama 4)", "score": 0.36, "metric": "overall"},
      {"agent": "Human baseline", "score": 0.92, "metric": "overall"}
    ],
    "notes": "466 questions chaining web browsing, file parsing, multi-document reasoning. NOTE: Berkeley RDI audit found ~98% of GAIA validation questions exploitable via public answer lookups + normalization collisions. The 7-point gap between same model in different orchestration frameworks (64.9% vs 57.6% for Claude Opus 4) shows scaffold quality dominates model quality. Level 3 tasks (35-45%) represent the hardest unsolved agentic gap vs 92% human baseline."
  },
  {
    "benchmark": "Terminal-Bench 2.0",
    "date": "2026-06-02",
    "source": "https://www.digitalapplied.com/blog/llm-benchmark-methodology-2026-contamination-leaderboard-guide",
    "results": [],
    "notes": "Released January 2026. 89 realistic terminal tasks — file manipulation, system administration, debugging, re-implementing research code. Deliberately chosen as work professionals are paid to do. Berkeley RDI audit found 100% of tasks exploitable via binary wrapper trojans. No current public leaderboard results for June 2 — benchmark considered compromised at static evaluation level."
  },
  {
    "benchmark": "WebArena",
    "date": "2026-06-02",
    "source": "https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough",
    "results": [
      {"agent": "Original GPT-4-based agent (baseline)", "score": 0.1441, "metric": "end-to-end task success"},
      {"agent": "Human baseline", "score": 0.7824, "metric": "end-to-end task success"}
    ],
    "notes": "812 scenarios in live e-commerce, forum, and CMS web environments. Long-horizon browser task benchmark. Berkeley RDI found ~100% exploitable via config leakage + DOM injection + prompt injection. Human/model gap remains substantial even for frontier agents."
  },
  {
    "benchmark": "Benchmark Integrity Warning — Berkeley RDI Audit",
    "date": "2026-06-02",
    "source": "https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/",
    "results": [
      {"agent": "Automated exploitation agent", "score": 1.00, "metric": "SWE-bench Verified — 500/500 tasks (exploit, 0 solved)"},
      {"agent": "Automated exploitation agent", "score": 1.00, "metric": "SWE-bench Pro — 731/731 tasks (exploit, 0 solved)"},
      {"agent": "Automated exploitation agent", "score": 1.00, "metric": "Terminal-Bench — 89/89 tasks (exploit)"},
      {"agent": "Automated exploitation agent", "score": 0.98, "metric": "GAIA — ~98% (public answer lookup)"},
      {"agent": "Automated exploitation agent", "score": 0.73, "metric": "OSWorld — 73% (VM state manipulation)"}
    ],
    "notes": "Berkeley RDI built an automated scanning agent that found every major benchmark exploitable to near-perfect scores without solving any tasks. SWE-bench: pytest hooks force all tests to pass. GAIA: answers are public on HuggingFace. Terminal-Bench: binary wrapper trojans. WebArena: DOM injection. This finding does not invalidate all benchmark results — legitimate agent runs still show real capability ordering — but it means any submitted score can now be gamed. Industry is moving toward trajectory-aware, human-verified evaluation (Claw-Eval pattern)."
  }
]
```

---

## Architecture / Pattern Notes

### Sandbox-First Agent Architecture (Dominant Emerging Pattern)

The most significant architectural shift this week is the convergence across all major frameworks on **sandbox-first agent design** — where the agent's compute environment (filesystem, shell, packages, network) is a first-class, versioned, provider-abstracted primitive rather than a side-channel concern. OpenAI's `SandboxAgent`, Google ADK's sandbox-from-template feature (v2.1.0), and Microsoft MAF's execution sandboxing (Agent Runtime privilege rings) all instantiate this same pattern from different entry points.

```
[Structured text for mermaid diagram conversion:]

[Orchestration Layer] (harness: instructions, tool dispatch, handoffs, approval gates, tracing)
  ↓ creates / resumes via Manifest
[Sandbox Session] (compute: filesystem, shell, packages, ports, network egress controls)
  ↓ executes tools in
[Privilege Ring] (model-generated code runs as constrained user with filesystem permissions)
  ↓ artifacts persisted to
[Snapshot Store] (serialized workspace state for resume across restarts)
  ↓ audit events flow to
[Policy Engine] (YAML/Rego/Cedar policy evaluated <0.1ms before each action)
  ↓ compliance events sent to
[Control Plane] (Agent 365 / LangSmith / Datadog — observability, alerting, blocking)
```

**Mermaid diagram (for downstream renderer):**
- `orchestration_layer` → `sandbox_session` (edge: Manifest + SandboxRunConfig)
- `sandbox_session` → `privilege_ring` (edge: model executes tools as constrained user)
- `privilege_ring` → `snapshot_store` (edge: workspace state persisted for resume)
- `snapshot_store` → `orchestration_layer` (edge: rehydrate on restart/crash)
- `privilege_ring` → `policy_engine` (edge: every action pre-evaluated)
- `policy_engine` → `control_plane` (edge: compliance events + blocking signals)
- `control_plane` → `orchestration_layer` (edge: runtime kill-switch / step-up auth)

### Framework Comparison Table

| Framework | Core Abstraction | Graph Type | Sandbox Support | Governance | Best For |
|-----------|-----------------|------------|-----------------|------------|----------|
| LangGraph | State machine nodes + reducers | Directed cyclic graph | Via third-party (E2B, Modal) | LangSmith tracing only | Complex stateful multi-agent workflows in production |
| CrewAI | Role-based agents + Tasks | Linear DAG (hierarchical option) | Via tools | Minimal | Fast prototyping, role-based business automation |
| Microsoft Agent Framework 1.0 | Agent + Workflow + Memory | Directed graph (sequential, concurrent, group-chat) | 4-tier privilege rings (AGT Runtime) | Agent Governance Toolkit (full OWASP coverage) | Enterprise .NET/Python production at scale |
| OpenAI Agents SDK (v0.17.4) | Agent + Runner + SandboxAgent | Implicit (handoffs) | Native SandboxAgent + Manifest | None (app-layer) | OpenAI-native agents, Codex-style filesystem tasks |
| Google ADK 2.0 | WorkflowGraph + CollaborativeAgent | Directed graph + dynamic mode | Template/snapshot sandboxes (v2.1.0) | Managed Agents API | Gemini-native agents, on-device Kotlin agents |
| AutoGen / AG2 | Conversational agents (group chat) | Conversation graph | None built-in | None | Research, complex multi-agent dialogue experiments |

### Emerging Pattern: Agent Skill Marketplaces as First-Class Distribution

NVIDIA's `skills.sh` catalog and GitHub `NVIDIA/skills` repo introduce a new software distribution primitive: the **agent skill file** — a structured `SKILL.md` that encodes domain expertise (which APIs to call, how to validate outputs, error recovery patterns) in a format any coding agent can consume at runtime. This is distinct from documentation (human-readable) or code libraries (requires import and integration). Skills are:

1. **Agent-readable at task time** — no import required; agent reads the skill and applies it contextually
2. **Versioned and signed** — each skill has metadata sidecar (`skills.sh.json`) and is signed with OMS for provenance
3. **Framework-agnostic** — same `SKILL.md` works with Claude Code, Cursor, Gemini CLI, Copilot, or any other coding agent
4. **Marketplace-distributed** — `skills.sh` enables discovery and installation similar to npm/pip but for agent capabilities

The concrete implication: NVIDIA has effectively turned its entire SDK documentation into a form that a coding agent can act on without human mediation. This pattern will likely propagate to other major platform vendors (AWS, Azure, GCP) as the standard interface between platform tooling and AI-assisted development.

---

## Analysis & Impact for Agentic Engineers

- **If you are building production agents on .NET or Python and need enterprise governance, adopt Microsoft Agent Framework 1.0 today.** The v1.0 GA means stable APIs with LTS commitment; the accompanying Agent Governance Toolkit covers the full OWASP Agentic Top 10 with <0.1ms policy evaluation, making it additive without meaningful performance penalty. The AGT works across 20+ frameworks, so you can adopt the governance layer independently of MAF itself — install `agent-governance-toolkit[full]` and wrap your existing LangGraph or CrewAI agents.

- **If you are using SWE-bench Verified as a procurement criterion for coding agents, stop immediately.** The Berkeley RDI audit (June 2026) demonstrated that all 500 Verified tasks are exploitable to achieve 100% with zero tasks actually solved. Use FeatureBench (ICLR 2026, <15% for all frontier models on feature delivery) or SWE-bench Pro (SEAL, 250-turn, identical tooling) instead. These scores better predict whether an agent can ship a real feature versus patch a single-file bug.

- **If you are building long-horizon agents (>10 minutes of wall-clock execution, filesystem operations, command execution), adopt the Sandbox-First architecture.** OpenAI's `SandboxAgent` (v0.14+) and Google ADK's sandbox template support (v2.1.0) both provide the Manifest abstraction for workspace portability. The key design decision is separating harness credentials from sandbox credentials: credentials and orchestration logic should never co-reside with model-generated code execution. The 4-tier privilege ring model from Microsoft AGT provides the right conceptual framework even if you are using OpenAI's sandbox infrastructure.

- **If you are operating remote MCP servers in production, the July 28 migration deadline is real and 10 weeks is now.** The `2026-07-28` RC is locked; Tier 1 SDKs ship within the validation window. Audit your server now for: sticky session dependencies, Redis session stores, SSE-based list-change subscriptions (all eliminated by the stateless core), and missing `Mcp-Method`/`Mcp-Name` headers (now required on every Streamable HTTP request). Local STDIO deployments are minimally affected.

- **If you are building physical AI pipelines (robotics, AV, simulation), NVIDIA's Agent Toolkit skills on `skills.sh` represent the lowest-friction path to agent-driving Cosmos/Omniverse/Isaac workflows.** The Brev Launchables provide pre-configured execution environments so you can evaluate whether agent-driven synthetic data generation is viable for your domain before committing to infrastructure setup. Cosmos 3 Nano (16B params) running on RTX PRO 6000-class hardware is the first open omni-model combining reasoning + generation for physical environments — evaluate it for closed-loop training data quality before the Super (64B) variant if you have workstation-grade compute.

---

## Key Takeaways (TL;DR)

- **Microsoft shipped the most complete enterprise agentic stack at Build 2026** — MAF 1.0 SDK + Windows Agent Runtime + Agent 365 control plane + Agent Governance Toolkit v4.0.0 — targeting IT governance buyers that other vendors are ignoring.
- **OpenAI's Sandbox Agents are now GA**, providing a first-class `SandboxAgent` primitive with Manifest portability, snapshotting, and provider abstraction — eliminating the need for custom Docker/volume-mount sandboxing infrastructure.
- **Every major agentic benchmark is now demonstrably exploitable** (Berkeley RDI audit); FeatureBench (11% frontier scores) and SWE-bench Pro are the only current alternatives with meaningful resistance to gaming.
- **MCP goes fully stateless on July 28** — remote server operators have 10 weeks to eliminate session dependencies, Redis stores, and SSE subscriptions; the `Mcp-Method`/`Mcp-Name` headers are now required on every request.
- **NVIDIA made its entire physical AI stack agent-callable** via open-source `SKILL.md` files on `skills.sh`, with Cosmos 3 shipping as the first open omni-model for physical world reasoning and action generation.
- **Google ADK 2.0 GA** introduces graph-based workflows + collaborative agent modes + Kotlin/Android on-device support, establishing the framework as a credible non-Microsoft/non-OpenAI production option with a clear hybrid edge-to-cloud story.

---

*Sources:*

- https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- https://community.openai.com/t/the-next-evolution-of-the-agents-sdk/1379072
- https://developers.openai.com/api/docs/guides/agents/sandboxes
- https://openai.github.io/openai-agents-python/sandbox/guide/
- https://github.com/openai/openai-agents-python/releases/tag/v0.17.0
- https://pypi.org/project/openai-agents/
- https://byteiota.com/microsoft-build-2026-windows-is-now-an-agent-platform/
- https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/
- https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/
- https://techcommunity.microsoft.com/discussions/agent-365-discussions/agent-365-will-be-generally-available-on-may-1-2026/4500380
- https://github.com/microsoft/agent-governance-toolkit
- https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/
- https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/
- https://wowhow.cloud/blogs/microsoft-build-2026-windows-agent-runtime-copilot-developer-guide-2026
- https://techcommunity.microsoft.com/blog/azuredevcommunityblog/the-future-of-agentic-ai-inside-microsoft-agent-framework-1-0/4510698
- https://nvidianews.nvidia.com/news/nvidia-releases-major-collection-of-open-source-agent-tools-and-skills-for-physical-ai
- https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Releases-Major-Collection-of-Open-Source-Agent-Tools-and-Skills-for-Physical-AI/default.aspx
- https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai
- https://github.com/nvidia/skills/
- https://techintelpro.com/news/nvidia-releases-open-source-physical-ai-agent-tools
- https://github.com/google/adk-python/releases/tag/v2.0.0
- https://github.com/google/adk-python/releases/tag/v2.1.0
- https://cloud.google.com/blog/topics/developers-practitioners/io26-news-for-agent-developers-on-google-cloud
- https://github.com/google/adk-docs/blob/main/docs/workflows/graph-routes.md
- https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- https://byteiota.com/mcp-goes-stateless-what-the-july-28-spec-rc-breaks/
- https://jigarjoshi.in/blog/mcp-stateless-spec-release-candidate/
- https://dev.to/akaranjkar08/mcp-spec-ships-july-28-every-breaking-change-and-how-to-migrate-4co8
- https://mcp.directory/blog/mcp-2026-07-28-release-candidate
- https://presenc.ai/research/ai-agent-capability-benchmarks-2026
- https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough
- https://www.digitalapplied.com/blog/llm-benchmark-methodology-2026-contamination-leaderboard-guide
- https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/
- https://agentmarketcap.ai/blog/2026/06/24/featurebench-63-point-cliff-feature-delivery-frontier-coding-agents
- https://pooyagolchian.com/blog/crewai-vs-langgraph-autogen-comparison-2026/
- https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026
- https://dev.to/cristian_iridon_286794874/langgraph-vs-crewai-vs-autogen-in-2026-pick-the-right-ai-agent-framework-or-skip-frameworks-4m2c
- https://www.globenewswire.com/news-release/2026/05/28/3302914/0/en/Orchid-Extends-Industry-First-Identity-Control-Plane-in-Response-to-Agentic-Dark-Matter-Breaking-the-Established-IAM-Paradigm.html
- https://github.com/Abhi-mishra998/aegis
- https://medium.com/@atnoforgenai/10-ai-agent-frameworks-you-should-know-in-2026-langgraph-crewai-autogen-more-2e0be4055556
