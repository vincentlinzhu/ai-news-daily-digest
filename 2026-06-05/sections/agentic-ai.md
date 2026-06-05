# Agentic AI — 2026-06-05

## Top Stories (3-5)

### 1. Claude Code Dynamic Workflows Ship to Research Preview — Claude Can Now Write Its Own Multi-Agent Harness
**Source:** [Anthropic Blog](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | [Claude Code Docs](https://code.claude.com/docs/en/workflows) | [The Neuron](https://www.theneuron.ai/explainer-articles/claude-code-dynamic-workflows-explained-claude-can-now-build-its-own-workflow-around-a-task/)

Claude Code v2.1.154+ ships a research-preview feature that fundamentally rethinks what a coding agent session means. When you ask Claude to "create a workflow" or invoke the new `ultracode` trigger word, Claude writes a JavaScript orchestration script that fans work across up to 16 concurrent subagents (up to 1,000 total per run), each in its own isolated context window. The script—not the conversation—holds intermediate results, which means even a 500-file migration never bleeds into your working session context.

The key architectural shift is that Claude moves from being the executor to being the *planner*. The harness (the coordination layer) becomes code: inspectable, sharable as a `/skill`, and repeatable via `/workflows`. Common patterns that emerge include fan-out-and-synthesize (split tasks, run in parallel, fold answers back in), adversarial verification (one agent challenges another agent's output), loop-until-done (iterate until a convergence test passes), and classify-and-act (route subtasks to specialist subagents). Dynamic workflows also let Claude select different models per subagent—routing cheaper models to boilerplate steps and frontier models to reasoning-heavy ones.

This matters for agentic engineers because it closes the gap between the bespoke orchestration systems teams have been building on top of LangGraph/CrewAI and the default single-agent loop. The feature is available on Max, Team, and API plans by default; Enterprise requires admin opt-in. It runs on Claude API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry, making it cloud-agnostic.

**Key technical details:**
- Trigger: include `workflow` in prompt, or `/effort ultracode` for automatic workflow planning on every substantive task
- Cap: 16 concurrent agents, 1,000 total agents per run; prevents runaway loops
- Model routing: each subagent can be assigned a different Claude model (Haiku for bulk steps, Opus 4.8 for reasoning-heavy stages)
- Isolation: subagents optionally run in their own git worktree for filesystem isolation
- Reuse: workflows are saved to `~/.claude/workflows/` and can be shared as slash commands
- No user input mid-run; split multi-checkpoint workflows into separate runs to add human-in-the-loop gates

---

### 2. NVIDIA Agent Toolkit + Nemotron 3 Ultra Launch for Always-On Agents
**Source:** [NVIDIA Investor](https://investor.nvidia.com/news/press-release-details/2026/Enterprise-Software-Leaders-Build-AI-Agents-With-NVIDIA/default.aspx) | [NemoClaw Docs](https://docs.nvidia.com/nemoclaw/latest/) | [NemoClaw GitHub](https://github.com/NVIDIA/NemoClaw/blob/main/README.md)

NVIDIA used GTC Taipei (June 1) to announce the NVIDIA Agent Toolkit, an open-source stack combining three components for enterprises building always-on agents: NemoClaw (reference deployment stack), OpenShell (secure runtime with policy-based guardrails), and CUDA-X libraries exposed as agent-callable skills. The flagship model dropping alongside the toolkit is Nemotron 3 Ultra, a 550-billion-parameter mixture-of-experts model designed for long-running agentic workloads—up to 5× faster inference and 30% lower cost than comparable open frontier models.

NemoClaw, now in early preview, installs via `curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash` and provisions the OpenShell runtime, configures a sandboxed agent environment, and sets up inference routing in a single guided wizard. The separation of concern is explicit: NemoClaw handles lifecycle and onboarding, OpenShell enforces kernel-level isolation and policy compliance, and Nemotron 3 Ultra handles reasoning. This mirrors the harness/sandbox split OpenAI introduced in April with its Agents SDK update.

For enterprises currently stitching together Docker + secrets management + model routing + audit logging by hand, this represents a production-grade opinionated stack with a one-command setup. The Nemotron 3 Ultra model arrives June 4 on Hugging Face, ModelScope, OpenRouter, and `build.nvidia.com` as NVIDIA NIM microservices.

**Key technical details:**
- Nemotron 3 Ultra: 550B MoE, 5× faster inference vs. comparable open frontiers, 30% lower cost, optimized for coding/research/enterprise long-running tasks
- OpenShell: policy-based privacy and security guardrails (configurable network, file, credential access), runs on RTX PCs, DGX Station, DGX Spark, and cloud
- NemoClaw: single-command setup, open-source (GitHub), early preview; NOT production-ready per NVIDIA's own alpha classification
- CUDA-X libraries are exposed as agent-callable skills, enabling GPU-accelerated computation directly from agent tool calls
- Inference routing via privacy router allows agents to use local Nemotron models OR cloud frontier models under unified policy enforcement

---

### 3. OWASP Enterprise Adoption Maturity Model for Agentic AI Released at InfoSecurity Europe
**Source:** [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/owasp-agentic-ai-security-maturity/) | [OWASP GenAI](https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/) | [AIUC-1 Crosswalk](https://genai.owasp.org/resource/aiuc-1-crosswalks-owasp-top-10-for-agentic-applications/)

OWASP's GenAI Security Project published "State of Agentic AI Security and Governance v2.01" on June 1 and debuted the framework's new *Enterprise Adoption Maturity Model (EAMM)* at the OWASP GenAI Security Summit at InfoSecurity Europe on June 4. Unlike a catalog of rules, EAMM functions as a two-axis diagnostic (deployment scope × governance maturity), landing organizations at one of four levels and prescribing the minimum controls required before advancing.

The four EAMM levels: **Level 0** (Unaware/Ad Hoc — pilots running without any agentic-specific governance); **Level 1** (Experimentation without guardrails — single-agent workflows with generic AI policies and occasional red-teaming, no autonomy limits); **Level 2** (Policy-defined, human-in-the-loop — formal policies mapped to regulations like the EU AI Act/GDPR, mandatory HITL for high-impact decisions, AI-SBOM established, named CAIO accountability); **Level 3** (Integrated, continuous oversight — real-time drift/anomaly dashboards, kill switches, governance-as-code with machine-readable policies, risk-tiered autonomy ladders). The framework also cross-maps to the OWASP Top 10 for Agentic Applications 2026, and the newly published AIUC-1 Crosswalk (May 25) provides bidirectional mapping to the AIUC-1 controls standard, identifying eight gap areas: agent identity, runtime containment, architectural monitoring, supply chain attestation, and schema controls.

**Key technical details:**
- EAMM is published as part of State of Agentic AI Security and Governance v2.01 (June 1, 2026)
- OWASP Top 10 for Agentic Applications 2026 covers: agent goal hijacking, tool misuse, identity/privilege abuse, memory poisoning, insecure inter-agent communication, cascading failures, trust exploitation, rogue agents
- The framework prescribes two responses when governance is insufficient: invest in agentic-specific controls OR reduce agent permissions/autonomy until existing controls suffice
- Practical requirements at Level 3: live behavioral baselines, real-time containment mechanisms, stop mechanisms (kill switches), joint incident response across safety and security teams, ephemeral credentials, cryptographic attestation per action
- AIUC-1 Crosswalk (May 25) identifies 8 priority gap areas where AIUC-1 needs new or expanded requirements for agentic deployments

---

### 4. A2A Protocol v1.0.1 Hits Production, 150+ Organizations Live Including Salesforce, SAP, ServiceNow
**Source:** [A2A GitHub](https://github.com/google/A2A) | [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) | [CommBank Perspective](https://www.commbank.com.au/business/brighter-perspectives/unlocking-the-agent-to-agent-ai-opportunity.html)

The Agent2Agent (A2A) protocol, contributed to the Linux Foundation by Google in June 2025 and now governed multi-vendor, released v1.0.1 on May 28, 2026—the first stable minor bump since v1.0 GA. With 150+ organizations supporting A2A including Microsoft, AWS, Salesforce, SAP, ServiceNow, and Workday, the protocol has crossed from standards experiment to enterprise reality. Azure AI Foundry, Amazon Bedrock AgentCore, and Google Cloud have all integrated A2A natively.

A2A uses JSON-RPC 2.0 over HTTP(S)/SSE for transport and Agent Cards for capability advertisement—the "business card" an agent publishes so remote orchestrators can discover what it can do, what inputs it accepts, and what auth flows it requires. The protocol is deliberately opaque about agent internals: neither agent needs to expose its memory, model, or reasoning implementation. Roadmap items for upcoming releases include a `QuerySkill()` method for dynamic capability probing, dynamic UX negotiation mid-task (adding audio/video to a running conversation), and improved streaming reliability. The MCP+A2A stack is now the de-facto interoperability layer: MCP handles agent-to-tool access, A2A handles agent-to-agent orchestration.

**Key technical details:**
- Transport: JSON-RPC 2.0 over HTTP(S) + Server-Sent Events for streaming; gRPC support added in earlier build
- Agent Cards: structured capability advertisement (inputs, outputs, auth schemes, skills); roadmap adds optional credential embedding in Agent Cards
- v1.0.1 (May 28): bug fixes to OSPO action references; stable API surface for enterprise builds
- MCP integration: MAF 1.0 (Microsoft Agent Framework, GA April 3) ships with MCP native support and has A2A support "imminent"
- Governance: Linux Foundation, Apache 2.0 license, 150 contributors, 24K GitHub stars
- Next: `QuerySkill()` for runtime capability introspection, dynamic mid-task UX negotiation

---

### 5. Enterprise SaaS Pivots to Consumption Pricing as Agentic AI Disrupts Per-Seat Models
**Source:** [VaaSBlock Analysis](https://www.vaasblock.com/news/enterprise-saas-agentic-ai-salesforce-servicenow-workday-2026/) | [Salesforce Agentforce](https://www.salesforce.com/blog/agentforce-coworker-salesforce-ai-teammate/) | [Planetary Labour](https://planetarylabour.com/articles/agentic-ai-enterprise)

The biggest structural shift in enterprise software in a decade is accelerating: Salesforce, ServiceNow, Workday, and SAP are all transitioning from per-seat licensing to consumption or outcome-based models as agentic AI displaces human-seat usage. Salesforce's Agentforce now serves 8,000+ customers with $900M in AI and Data Cloud revenue in its first six months; its action-based pricing is $0.10 per action. The new "Agentforce Coworker" launch (currently in beta) ships as a headless-first AI teammate that appears inside Salesforce, Slack, Microsoft Teams, ChatGPT, and Claude from a single business-context-aware identity.

ServiceNow targets $1B in AI-specific revenue by 2026, positioning its Now Platform as the workflow substrate agents run *on top of*, with AI Agent Orchestrator providing governance across first- and third-party agents. Workday's Agent System of Record (ASOR) provides an HR/finance-domain governance layer for digital workforces, and Workday Flex Credits operationalize consumption billing. The structural threat: Deloitte estimates 75% of companies will be investing in agentic AI by 2026, but per-seat SaaS seat counts are declining as AI agents do the work previously done by named human users.

**Key technical details:**
- Salesforce Agentforce Coworker: headless-first, multi-surface deployment (Salesforce, Slack, Teams, ChatGPT, Claude), beta now, additional surfaces later 2026
- Agentforce pricing: $0.10/action; targets outcome-based billing to capture agent-driven value without seat counts
- ServiceNow: AI Agent Orchestrator governs agents via MCP; targets $1B AI-specific ARR in 2026
- Workday ASOR: cross-vendor agent governance layer for regulated HR/finance workflows; Flex Credits = consumption billing
- Market sizing: enterprise AI agents market growing from $7.92B in 2025 to $236B by 2034 at 45.8% CAGR
- Risk: agents don't consume software like humans—CFOs are renegotiating contracts around outcomes rather than seat counts

---

## Deep Dive: Most Important Item

### Claude Code Dynamic Workflows — When the Agent Writes the Orchestrator

This is the most architecturally significant development this week because it collapses the distinction between "agentic framework" and "AI assistant." Previously, orchestration frameworks like LangGraph or CrewAI lived *outside* the model: engineers wrote the graph, assigned nodes, configured edges, and handed the scaffolding to the LLM to execute inside. Dynamic Workflows inverts this—Claude *writes* the orchestration script itself, in JavaScript, as an artifact of the task. The harness becomes a first-class product of the AI, not a prerequisite authored by engineers.

**What the Platform Provides**

1. **Script-based orchestration runtime**: The workflow is a JavaScript file with special APIs (`spawnAgent()`, `collectResults()`, `routeByModel()`) executed by a Claude Code runtime, not inside the LLM's context. The LLM writes it; a separate runtime runs it.
2. **Parallel subagent spawning**: Up to 16 concurrent agents per step, 1,000 total per run. Each agent has its own context window, file system access, and tool permissions.
3. **Model-per-step routing**: Different Claude model tiers can be assigned to different workflow stages. Reasoning-heavy steps → Opus 4.8; bulk file scans → Haiku.
4. **Worktree isolation**: Subagents optionally run in isolated git worktrees, preventing cross-contamination of file system state.
5. **Adversarial verification**: The workflow script can spin up a "challenger" agent to refute the output of a "solver" agent, running until outputs converge.
6. **Workflow persistence and reuse**: Successful workflow scripts are saved to `~/.claude/workflows/` and exposed as slash commands or skills shareable across teams.
7. **`ultracode` mode**: A session-level setting (`/effort ultracode`) that combines `xhigh` reasoning effort with automatic workflow planning—Claude decides when to invoke a workflow without being asked.

**Why This Matters**

The practical impact for engineering teams is that the orchestration expertise required to use multi-agent patterns drops dramatically. A senior engineer at a mid-size company previously needed to architect a LangGraph workflow, write node functions, configure state schemas, set up checkpointing, and wire observability—weeks of work. With Dynamic Workflows, you describe the task, Claude emits a JavaScript orchestration script that *encodes the architecture*, and the runtime handles execution. The script remains human-inspectable and can be edited or versioned.

The governance implications are double-edged. On one hand, codifying the orchestration as a runnable script creates auditability—you can read exactly what the agent planned to do. On the other hand, Claude-generated orchestration scripts can spawn hundreds of subagents, invoke tools at scale, and consume substantial tokens without human checkpoints mid-run (user input is disabled during execution). Organizations running Claude Code on Enterprise plans should audit workflow scripts before allowing broad use, implement token budget guardrails, and ensure sensitive filesystem paths are out of scope.

The competitive implication is that Anthropic now has the strongest "agent-writes-the-agent-framework" story in the market—more opinionated than OpenAI Sandbox Agents (which require engineers to write the `SandboxAgent` and `Manifest`), and more AI-native than LangGraph (where the developer writes the graph).

**Architectural Significance**

Dynamic Workflows introduce a new primitive: the *meta-harness*—an AI-generated orchestration layer that sits between the user's intent and the subagents executing work. This is architecturally distinct from both static RAG pipelines and hand-authored multi-agent graphs. The closest prior art is AutoGen's code-execution loop and early LangGraph "plan-and-execute" patterns, but both required significant human scaffolding. The new primitive is: **intent → AI-generated orchestration script → runtime-executed parallel subagents → synthesized result**. The script is the new unit of agentic work product.

**Competitive Context**

- **OpenAI Sandbox Agents (GA)**: Engineers write `SandboxAgent` + `Manifest`; agent gets a controlled compute environment. Harness is human-authored. Strong sandbox isolation, weak meta-orchestration.
- **LangGraph**: Engineers write stateful graphs with explicit checkpointing; strong production durability and observability (LangSmith). Harness is human-authored. No AI-generated orchestration.
- **Microsoft Agent Framework (MAF) 1.0**: Engineers use MAF's `GraphFlow`/`SequentialBuilder`; unified across .NET and Python. Harness is human-authored. Strong Azure/M365 integration.
- **Claude Dynamic Workflows**: *AI-generated* harness; JavaScript runtime; model-routing per step; adversarial verification built in. Weaker external observability than LangSmith. Weakest for enterprises requiring deterministic, audited multi-step human approval gates.

---

## Benchmark Data (SWE-bench, GAIA, AgentBench, etc.)

```json
[
  {
    "benchmark": "SWE-bench Verified",
    "date": "2026-06-02",
    "source": "https://benchlm.ai/benchmarks/sweVerified",
    "results": [
      {"agent": "Claude Mythos Preview", "score": 0.939, "metric": "task resolution rate"},
      {"agent": "Claude Opus 4.8", "score": 0.886, "metric": "task resolution rate"},
      {"agent": "Claude Opus 4.7 (Adaptive)", "score": 0.876, "metric": "task resolution rate"}
    ],
    "notes": "BenchLM.ai leaderboard as of June 2, 2026. Uses standardized harness across all models. 49 models evaluated. Note: Berkeley RDI April 2026 audit showed SWE-bench Verified is gameable to near-100% with harness-aware optimizations—use SWE-bench Pro for production evaluations."
  },
  {
    "benchmark": "SWE-bench Verified (vals.ai minimal harness)",
    "date": "2026-05-28",
    "source": "https://vals.ai/benchmarks/swebench",
    "results": [
      {"agent": "GPT 5.5", "score": 0.826, "metric": "task resolution rate"},
      {"agent": "Claude Opus 4.7", "score": 0.820, "metric": "task resolution rate"},
      {"agent": "Gemini 3.1 Pro Preview", "score": 0.788, "metric": "task resolution rate"},
      {"agent": "GPT 5.4", "score": 0.782, "metric": "task resolution rate"},
      {"agent": "GPT 5.3 Codex", "score": 0.780, "metric": "task resolution rate"}
    ],
    "notes": "vals.ai uses a bash-tool-only minimal harness (no scaffolding advantage). Puts evaluation burden on the model, not the harness. 500 human-verified tasks. More conservative and reproducible than lab-reported numbers."
  },
  {
    "benchmark": "SWE-bench Verified (Presenc AI production agents, May 2026 snapshot)",
    "date": "2026-05-01",
    "source": "https://presenc.ai/research/ai-agent-capability-benchmarks-2026",
    "results": [
      {"agent": "Claude Code (Opus 4.7)", "score": 0.77, "metric": "task resolution rate (midpoint of 76-78% range)"},
      {"agent": "OpenAI Codex agent (GPT-5 Pro)", "score": 0.75, "metric": "task resolution rate (midpoint of 74-76% range)"},
      {"agent": "Cursor Agent (Sonnet 4.6)", "score": 0.65, "metric": "task resolution rate (midpoint of 63-67% range)"},
      {"agent": "Devin (Cognition AI)", "score": 0.55, "metric": "task resolution rate (midpoint of 52-58% range)"},
      {"agent": "Open-source agent + Llama 4 70B", "score": 0.285, "metric": "task resolution rate (midpoint of 25-32% range)"}
    ],
    "notes": "Production agent harnesses (not minimal). Reflects real-world scaffolding. Frontier agents cluster 70-78%. Up from 13% in early 2024, 49% in early 2025."
  },
  {
    "benchmark": "GAIA (Princeton HAL, April 2026 snapshot)",
    "date": "2026-04-01",
    "source": "https://rapidclaw.dev/blog/ai-agent-benchmarks-2026",
    "results": [
      {"agent": "Claude Sonnet 4.5 (HAL scaffold)", "score": 0.746, "metric": "overall accuracy"},
      {"agent": "Claude Opus 4.5 (HAL scaffold)", "score": 0.732, "metric": "overall accuracy"},
      {"agent": "OWL (open-source, HAL scaffold)", "score": 0.691, "metric": "overall accuracy (best open-source)"}
    ],
    "notes": "Princeton HAL provides a specialized multi-model scaffold. Anthropic models sweep all top 6 HAL spots. Scores not directly comparable to bare-model GAIA results. Leaderboard last updated April 2026."
  },
  {
    "benchmark": "GAIA Official Leaderboard (HuggingFace, April 16, 2026)",
    "date": "2026-04-16",
    "source": "https://leaderboard.steel.dev/leaderboards/gaia/",
    "results": [
      {"agent": "OPS-Agentic-Search (Alibaba Cloud multi-model ensemble)", "score": 0.9236, "metric": "overall accuracy across 466 questions"},
      {"agent": "openJiuwen-deepagent (Suzhou AI Lab)", "score": 0.9236, "metric": "overall accuracy"},
      {"agent": "JoinAI V2.2 (JoinAI-CMCC multi-model)", "score": 0.907, "metric": "overall accuracy"},
      {"agent": "Nemotron-ToolOrchestra (NVIDIA)", "score": 0.9037, "metric": "overall accuracy"}
    ],
    "notes": "Official GAIA leaderboard is dominated by multi-model ensemble systems (Qwen + Claude + GPT-5 + DeepSeek + Gemini mixtures). Not representative of single-model capability. NVIDIA's Nemotron-ToolOrchestra (8B routing model) reaching 90%+ is notable. Use for enterprise orchestration architecture research, not model comparison."
  },
  {
    "benchmark": "GAIA (BenchLM snapshot, bare model)",
    "date": "2026-06-02",
    "source": "https://rapidclaw.dev/blog/ai-agent-benchmarks-2026",
    "results": [
      {"agent": "Claude Mythos Preview", "score": 0.523, "metric": "overall accuracy (bare model, no custom scaffold)"},
      {"agent": "GPT-5.4 Pro", "score": 0.505, "metric": "overall accuracy"},
      {"agent": "GPT-5.4", "score": 0.482, "metric": "overall accuracy"}
    ],
    "notes": "Bare model (no custom scaffold) GAIA scores are dramatically lower than HAL/ensemble systems. The 40-point gap between bare model and HAL scaffold demonstrates that GAIA measures the scaffold as much as the model. Context: GAIA Level 3 (hardest) sits at 35-45% for frontier agents vs. ~92% human baseline."
  }
]
```

---

## Architecture / Pattern Notes

### Dominant Architecture Pattern: Meta-Harness Orchestration (AI-Generated Workflow Scripts)

The most significant new architectural pattern this week is the *meta-harness*: an AI model outputs an orchestration script as a task artifact, and a separate runtime executes that script to coordinate parallel subagents. This is distinct from static multi-agent graphs (where humans write the graph) and from single-agent agentic loops (where one model holds all context).

```
[Structured text for mermaid diagram conversion:]
[user_intent] (natural language task description)
  ↓ "write workflow"
[claude_opus_4_8] (meta-planner: generates JavaScript orchestration script)
  ↓ "execute script"
[workflow_runtime] (JavaScript runtime with special agent APIs)
  ↓ "spawn" (up to 16 concurrent)
[subagent_pool] (isolated subagents, each with own context window)
  ↓ "fan-out tasks"
[specialized_subagents] (solver, verifier, challenger, synthesizer roles)
  ↓ "collect results"
[synthesizer_agent] (aggregates, cross-checks, resolves conflicts)
  ↓ "return"
[user] (single coordinated answer, no intermediate clutter)
```

**Mermaid diagram (for downstream renderer):**
- `user_intent` → `meta_planner` (edge: describe task)
- `meta_planner` → `workflow_script` (edge: generates JS)
- `workflow_script` → `runtime` (edge: submitted for execution)
- `runtime` → `subagent_pool` (edge: spawn up to 16 concurrent)
- `subagent_pool` → `solver` (edge: fan-out subtask)
- `subagent_pool` → `verifier` (edge: fan-out adversarial check)
- `solver` → `synthesizer` (edge: report result)
- `verifier` → `synthesizer` (edge: challenge/confirm)
- `synthesizer` → `user` (edge: unified answer)

### Framework Comparison Table

| Framework | Core Abstraction | Graph Type | Best For |
|-----------|-----------------|------------|----------|
| LangGraph | Stateful graph nodes with typed state | Directed cyclic graph with checkpointing | Production systems requiring deterministic state, HITL, observability (LangSmith) |
| CrewAI | Role-based agents (Crew + Task + Agent) | Sequential/hierarchical, SQLite-backed (April 2026) | Rapid prototyping, linear business automation, role-based collaboration |
| Microsoft Agent Framework 1.0 | WorkflowBuilder / GraphFlow (unified AutoGen + Semantic Kernel) | Explicit workflow DAG, persistent AgentSession | Azure-native, .NET + Python, MCP-native, enterprise governance |
| Claude Dynamic Workflows | AI-generated JavaScript orchestration script | AI-planned DAG with adversarial verification loops | Tasks where orchestration architecture itself is unknown upfront; token-budget-tolerant workloads |
| OpenAI Sandbox Agents | SandboxAgent + Manifest + provider-abstracted compute | Single durable agent with snapshotting | Long-running agents requiring durable state, multi-cloud compute portability |

### Emerging Pattern: Ephemeral Credential Brokering for Agent Identity

As multi-agent systems mature, a clear pattern is crystallizing around agent identity: **ephemeral, task-scoped credentials issued by a broker at spawn time** replace persistent API keys. The Cloud Security Alliance's Agentic IAM framework and OWASP EAMM Level 3 both require this pattern as table stakes for production.

In the canonical implementation: an orchestrator spawns an agent and immediately requests a credential from an access broker (e.g., Ephyr, Strata Maverics, or Workday ASOR). The broker validates the request against the application's permission ceiling and issues a token scoped to exactly that task—no broader scope, no longer TTL than necessary (5-minute defaults for SSH certificates are becoming standard). The token is cryptographically bound to a private key the agent holds, so stealing the JWT without the key is useless. Each delegation hop to a subagent can only *narrow* scope, never expand it. All credential operations—issuance, renewal, revocation, denial—are written to a hash-chained, SIEM-ready audit log.

Concrete tools implementing this pattern: **Ephyr** (open-source, Ed25519 CA, ULID correlation, MCP endpoint), **Strata Maverics** (MCP Proxy with DPoP/OBO delegation chains), **Agent Passport System / Termo** (Ed25519 passports with delegation chains and Merkle contribution proofs). The Cloud Security Alliance published formal guidance in May 2026; NIST's AI Agent Standards Initiative (launched February 2026) is moving toward regulatory codification of these requirements.

---

## Analysis & Impact for Agentic Engineers

- **Adopt Claude Code Dynamic Workflows for complex, token-budget-tolerant tasks, but audit every generated script before production use.** The AI-generated harness pattern is powerful but opaque by default—CI pipelines should require human review of workflow scripts before they can be scheduled as repeating jobs. Token consumption can be 10–50× a standard session for large workflows. Start with scoped, bounded tasks (e.g., a single module migration) before applying to whole-codebases.

- **If you are building multi-agent systems for enterprise, implement ephemeral credential brokering now, not later.** OWASP EAMM Level 2 requires it, regulators are moving toward mandating it, and the CSA published the canonical pattern in May 2026. The incremental cost of switching from persistent API keys to a broker like Ephyr is low compared to the blast radius of a compromised persistent key used across hundreds of agent invocations. Every agent spawn should be a credential issuance event.

- **Use SWE-bench Verified via vals.ai's minimal bash-only harness for fair model comparisons, and use SWE-bench Pro or FeatureBench for production benchmarking.** The gap between Berkeley-RDI's warning (April 2026: all major benchmarks gameable to ~100%) and the vals.ai minimal harness results is meaningful—GPT 5.5 at 82.6% and Claude Opus 4.7 at 82% with a bash-only harness vs. 93.9% claimed by Claude Mythos Preview with a full scaffold. Your production agent performance will resemble the minimal harness numbers, not the scaffold-assisted numbers.

- **If you are running LangGraph in production, the Microsoft Agent Framework 1.0 GA (April 3) is worth evaluating as a migration path if your stack is Azure-native or requires .NET support.** MAF unifies AutoGen and Semantic Kernel under one SDK, adds MCP native integration, and has a documented migration guide from AutoGen v0.2 abstractions. AutoGen standalone is now in maintenance mode. LangGraph remains the stronger choice for non-Azure environments requiring complex stateful graphs and LangSmith observability.

- **Enterprise SaaS procurement teams should immediately renegotiate contracts with Salesforce, ServiceNow, and Workday around outcome-based or consumption pricing.** Per-seat models are structurally misaligned with agentic workflows—you are increasingly paying for seat licenses while agents do the work. Salesforce's $0.10/action pricing and Workday Flex Credits are the new baseline; vendors still quoting per-seat for AI-assisted workflows are extracting misaligned value. Define what "action" means in your contract before signing.

---

## Key Takeaways (TL;DR)

- Claude Code Dynamic Workflows (research preview) let Claude write its own JavaScript orchestration harness—up to 16 concurrent subagents, model-routing per step, adversarial verification loops, and saveable workflow scripts that become reusable slash commands.
- NVIDIA launched Nemotron 3 Ultra (550B MoE, 5× faster, 30% cheaper than comparable open models) alongside NemoClaw/OpenShell as a one-command secure agent runtime stack—early preview, not production-ready.
- OWASP published the Enterprise Adoption Maturity Model (4 levels) for agentic AI governance, with Level 3 requiring real-time behavioral monitoring, kill switches, governance-as-code, ephemeral credentials, and cryptographic attestation.
- A2A protocol v1.0.1 is in production with 150+ organizations (Salesforce, SAP, ServiceNow, Workday, Microsoft, AWS); MCP+A2A is now the de-facto agent interoperability stack.
- AutoGen is in maintenance mode as of April 2026—Microsoft shipped MAF 1.0 (AutoGen + Semantic Kernel merged) as the official successor; new projects should use LangGraph (complex stateful), CrewAI (rapid prototyping), or MAF (Azure-native).
- The GAIA official leaderboard (92%+ by multi-model ensembles) and SWE-bench Verified (93.9% with full scaffold) are measuring harness sophistication as much as model quality—use vals.ai's bash-only harness or SWE-bench Pro for production-predictive numbers.

---

*Sources:*
- https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
- https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
- https://code.claude.com/docs/en/workflows
- https://www.theneuron.ai/explainer-articles/claude-code-dynamic-workflows-explained-claude-can-now-build-its-own-workflow-around-a-task/
- https://claudelab.net/en/articles/claude-code/claude-code-dynamic-workflow-hands-on
- https://investor.nvidia.com/news/press-release-details/2026/Enterprise-Software-Leaders-Build-AI-Agents-With-NVIDIA/default.aspx
- https://docs.nvidia.com/nemoclaw/latest/
- https://github.com/NVIDIA/NemoClaw/blob/main/README.md
- https://build.nvidia.com/nemoclaw
- https://nvidianews.nvidia.com/news/nvidia-announces-nemoclaw
- https://pub.towardsai.net/nvidia-nemoclaw-openshell-fastest-way-to-install-bbfb82b08ea7
- https://www.infosecurity-magazine.com/news/owasp-agentic-ai-security-maturity/
- https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/
- https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- https://genai.owasp.org/resource/aiuc-1-crosswalks-owasp-top-10-for-agentic-applications/
- https://github.com/google/A2A
- https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade
- https://www.commbank.com.au/business/brighter-perspectives/unlocking-the-agent-to-agent-ai-opportunity.html
- https://atlan.com/know/google-a2a-protocol/
- https://www.salesforce.com/blog/agentforce-coworker-salesforce-ai-teammate/
- https://www.vaasblock.com/news/enterprise-saas-agentic-ai-salesforce-servicenow-workday-2026/
- https://planetarylabour.com/articles/agentic-ai-enterprise
- https://www.linkedin.com/pulse/usage-based-chaos-agentic-ai-breaking-saas-pricing-models-prasad-juyoe
- https://www.moxo.com/blog/agentic-ai-pricing
- https://benchlm.ai/benchmarks/sweVerified
- https://vals.ai/benchmarks/swebench
- https://rapidclaw.dev/blog/ai-agent-benchmarks-2026
- https://presenc.ai/research/ai-agent-capability-benchmarks-2026
- https://leaderboard.steel.dev/leaderboards/gaia/
- https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- https://www.polarpoint.io/blog/2026/05/26/mcp-goes-stateless-what-the-2026-07-28-rc-actually-changes/
- https://sdd.sh/2026/03/mcps-2026-roadmap-from-prototype-protocol-to-production-standard/
- https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026
- https://devblogs.microsoft.com/foundry/agent-service-build2026/
- https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/
- https://developers.openai.com/api/docs/guides/agents/sandboxes
- https://dev.to/cristian_iridon_286794874/langgraph-vs-crewai-vs-autogen-in-2026-pick-the-right-ai-agent-framework-or-skip-frameworks-4m2c
- https://automationswitch.com/ai-workflows/langchain-vs-crewai-vs-autogen-vs-langgraph
- https://turion.ai/blog/langgraph-vs-crewai-vs-autogen-comparison-2026/
- https://pub.towardsai.net/langgraph-vs-crewai-vs-autogen-which-ai-agent-framework-should-your-enterprise-use-in-2026-3a9ebb407b09
- https://github.com/EphyrAI/Ephyr
- https://cloudsecurityalliance.org/blog/2026/05/08/ai-agent-identity-is-being-solved-backwards-and-the-window-to-fix-it-is-now
- https://www.strata.io/blog/agentic-identity/agentic-ai-governance-how-to-approach-it/
- https://termo.ai/skills/agent-passport-system
- https://christian-schneider.net/blog/non-human-identity-governance-gap-ai-agents/
- https://massivescale-ai/agentic-trust-framework (GitHub)
