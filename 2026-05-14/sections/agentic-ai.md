# Agentic AI — 2026-05-14

## Top Stories (3-5)

### 1. Anthropic Claude Managed Agents: Dreaming, Outcomes, and Multiagent Orchestration — Self-improving agents with rubric-based grading and parallel specialist delegation now in public beta

**Source:** [Anthropic Claude Blog](https://claude.com/blog/new-in-claude-managed-agents) | [Claude Platform Docs](https://platform.claude.com/docs/en/managed-agents/overview) | [Multiagent Sessions Docs](https://platform.claude.com/docs/en/managed-agents/multi-agent)

Anthropic launched three major additions to Claude Managed Agents on May 6, 2026, fundamentally elevating what hosted agents can do autonomously. **Dreaming** (research preview) is a scheduled background process that reviews past agent sessions, extracts recurring patterns, and curates the agent's memory store without human intervention—enabling genuine session-over-session self-improvement. **Outcomes** (public beta) lets developers write a rubric describing what "good" looks like; a separate grader evaluates outputs in its own context window (isolated from the agent's reasoning) and triggers an automatic re-attempt until the rubric is satisfied. Internal benchmarks show up to +10 points task-success improvement over standard prompting loops, with +8.4% on `.docx` generation and +10.1% on `.pptx`. **Multiagent orchestration** (public beta) allows a coordinator agent running on Claude Opus 4.7 to delegate to parallel specialist sub-agents, each with independent models, system prompts, tools, and isolated session threads—while sharing a common filesystem.

Real deployments are already demonstrating impact at scale: Harvey (legal AI) reported ~6× completion rate improvement using dreaming for cross-session memory; Netflix's platform team uses multiagent orchestration to analyze hundreds of build logs in parallel and surface only recurring failure patterns; Wisedocs cut document review time 50% while enforcing quality rubrics via outcomes. All three features work together—dreaming refines memory between sessions, outcomes enforces quality gates within sessions, and multiagent orchestration fans out the work. The `managed-agents-2026-04-01` beta header is required for all API calls, and developers can trace every delegation step in the Claude Console.

For agentic engineers, this is the clearest signal yet that hosted orchestration is maturing into production infrastructure. Rather than building your own memory management, grading harnesses, and agent-spawning logic, Managed Agents now provides all three as platform primitives with observable audit trails. The closed-loop self-improvement via dreaming is architecturally novel: it addresses the long-standing problem of agents that plateau after initial deployment by periodically distilling cross-session learnings into durable memory.

**Key technical details:**
- Dreaming reviews all sessions in a memory store, extracts patterns (recurring mistakes, convergent workflows, shared preferences), and restructures memory to stay high-signal—automatically or with human review gating
- Outcomes grader runs in a separate context window from the agent to avoid reasoning contamination; rubric can be quantitative (requirements met) or qualitative (brand voice, visual guidelines)
- Multiagent: coordinator + up to 20 specialist agents per orchestration; agents share filesystem but not session history; events are persistent; full delegation trace in Claude Console
- Webhooks allow async notification on task completion, enabling callback-driven pipeline architectures
- Dreaming requires access request; outcomes, multiagent, memory are public beta at `platform.claude.com`

---

### 2. AWS Agent Toolkit and MCP Server Go Generally Available — 40+ agent skills, authenticated AWS API access, and sandboxed Python execution via MCP

**Source:** [AWS News Blog](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/) | [AWS What's New: MCP Server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) | [AWS What's New: Agent Toolkit](https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/) | [GitHub](https://github.com/aws/agent-toolkit-for-aws)

AWS announced the general availability of the AWS MCP Server and the broader Agent Toolkit for AWS on May 6, 2026—the same day as Anthropic's Managed Agents update. The AWS MCP Server is a managed remote MCP server that solves a critical gap: AI coding agents working with AWS relied on training data that was months stale and would reach for AWS CLI rather than CDK/CloudFormation, producing over-permissioned IAM policies. The server provides three core tools: `call_aws` (executes any of 15,000+ AWS API operations using existing IAM credentials, with new APIs supported within days of launch), `search_documentation`/`read_documentation` (retrieves current AWS docs at query time, no authentication required), and `run_script` (executes Python server-side in a sandboxed environment that inherits IAM permissions but has no network or filesystem access—enabling multi-API aggregation in a single round-trip).

New at GA: IAM context key support eliminates the need for a separate permission to use the server; token requirements per interaction are reduced; CloudWatch metrics under `AWS-MCP` namespace separate agent calls from human calls for compliance audit trails; CloudTrail captures all API activity. The broader Agent Toolkit includes 40+ curated agent skills contributed and maintained by AWS service teams—replacing the previous "Agent SOPs" with structured best practices for infrastructure-as-code, storage, analytics, serverless, containers, and AI services. Three agent plugins (AWS Core, AWS Data Analytics, AWS Agents) are available for Claude Code, Cursor, Kiro, and Codex.

For agentic engineers building on AWS, this removes the painful impedance mismatch between agents and cloud infrastructure. The `run_script` tool is particularly significant: it enables agents to chain 10+ API calls, filter responses, and compute derived results in one round-trip rather than burning context with sequential tool calls. The Skills layer creates a new pattern—platform-maintained, continuously updated procedural knowledge that agents consult rather than hallucinating from stale training data.

**Key technical details:**
- Available in US East (N. Virginia) and Europe (Frankfurt); can make API calls to any region
- No additional cost; pay only for AWS resources created
- Authentication via IAM + SigV4; bridges to MCP's OAuth 2.1 via the open-source `mcp-proxy-for-aws` proxy
- Compatible with Claude Code, Kiro, Cursor, Codex, and any MCP-compatible client
- CloudWatch namespace `AWS-MCP` enables per-agent observability separate from human actions
- Skills are service-team-maintained, keeping tool count low and reducing hallucination risk

---

### 3. SAP Autonomous Enterprise + Anthropic Partnership at Sapphire 2026 — 200+ domain-specific agents embedded in ERP with Claude as primary reasoning engine

**Source:** [SAP News Center](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/) | [SAP-Anthropic Partnership](https://news.sap.com/2026/05/sap-anthropic-to-bring-claude-sap-business-ai-platform/) | [SAP Business AI Platform](https://news.sap.com/2026/05/sap-sapphire-keynote-business-ai-platform-power-autonomous-enterprise/) | [TechTarget Analysis](https://www.techtarget.com/searcherp/news/366642887/The-AI-technology-behind-SAPs-Autonomous-Enterprise-pitch)

At SAP Sapphire 2026 in May, SAP unveiled the **Autonomous Enterprise** vision backed by the new **SAP Business AI Platform**—a unified layer that combines SAP Knowledge Graph (structured maps of business entities and processes derived from 7 million+ ERP data fields), Joule Studio (no-code/pro-code/AI agent builder), and deep integration with SAP S/4HANA, SuccessFactors, and Ariba. The flagship deployment is the **SAP Autonomous Suite**, which orchestrates over 200 specialized Joule agents across finance (compressing financial close from weeks to days), supply chain, procurement, HR, and customer experience. Simultaneously, SAP and Anthropic announced a partnership to embed Claude as the primary reasoning engine across SAP's AI portfolio—with the explicit governance constraint that Claude operates within SAP's business rules, security, and compliance frameworks.

SAP's approach is architecturally the most restrictive of the enterprise ERP vendors: in April 2026, SAP updated API policies to prohibit third-party AI agents from interacting with SAP systems outside SAP-endorsed architectures. This creates a walled garden where Anthropic's Claude is the privileged insider while other AI agents are locked out. The Joule Studio builder follows a pattern of providing a governed, low-code entry point for business users to build domain agents that access ERP data, while keeping raw API access tightly controlled. SAP CEO Christian Klein's framing is direct: "almost right" accuracy is unacceptable for mission-critical business processes.

For agentic engineers in enterprise contexts, SAP's move signals that large ERP vendors will increasingly control the governance layer for agents touching business data. If you're building on SAP infrastructure, the path of least resistance is through the Joule framework and the Anthropic partnership—direct API scraping or third-party agent orchestration will face policy barriers. This also makes SAP's governance model a reference implementation for how industrial-scale agent deployments handle compliance: data grounding in a Knowledge Graph, workflow execution via approved action surfaces, and human oversight gates on mutations.

**Key technical details:**
- SAP Knowledge Graph covers 7M+ ERP data fields, providing structured context for agents on business entities, processes, and relationships
- Joule Studio supports no-code, pro-code, and AI-native agent authoring within the SAP ecosystem
- 50+ domain-specific Joule Assistants orchestrating 200+ specialized agents in GA
- Anthropic Claude embedded as primary reasoning engine; partnership emphasizes governance and business-context grounding
- SAP API policy update (April 2026): third-party agents prohibited outside SAP-endorsed architectures
- Integration targets: SAP S/4HANA, SuccessFactors, Ariba

---

### 4. ServiceNow Action Fabric Launches at Knowledge 2026 — Metered integration layer opening enterprise workflows to any external AI agent via MCP

**Source:** [NowBen](https://nowben.com/servicenow-launches-action-fabric-to-open-full-system-of-action-to-any-ai-agent/) | [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/servicenow-sap-and-workday-make-ai-agents-pay-to-play/) | [Reworked](https://www.reworked.co/digital-workplace/servicenow-launches-action-fabric-major-overhaul-of-ai-control-tower/) | [CIO](https://www.cio.com/article/4169954/servicenows-ai-control-tower-offers-hazy-view-of-spend.html)

ServiceNow announced **Action Fabric** at Knowledge 2026, a metered integration layer that exposes ServiceNow's full "system of action"—workflows, playbooks, approval chains, service catalog actions, and business rules—to any external AI agent (Claude, Copilot, custom-built agents) through a ServiceNow MCP Server. Anthropic's Claude is the launch partner. Action Fabric is ServiceNow's strategic bet to become the universal control plane for enterprise agentic workflows, positioned as the governance and execution layer that any agent must pass through to touch ServiceNow data and trigger business processes. Unlike SAP's closed approach, ServiceNow is explicitly opening its platform to external agents—but on metered, action-based pricing terms.

The pricing model is architecturally significant and concerning for budget predictability. Customers receive a baseline of "assists" bundled with their subscription and pay per additional operation. Because the number of assists consumed per agentic interaction varies based on task complexity and tool use patterns—especially in retry loops when tasks fail—CFOs face unpredictable monthly exposure. This mirrors SAP and Salesforce's shift toward usage-based agent pricing, a trend that will reshape enterprise software economics in 2026-2027. The CIO community has noted that the "AI control tower" visibility into spend remains limited.

For agentic engineers deploying in ServiceNow environments, Action Fabric creates a clear integration pattern: register your agent against the ServiceNow MCP Server, route enterprise workflow executions through it rather than calling ServiceNow APIs directly, and accept the metered pricing in exchange for governed access to approval chains and business rules your agent couldn't otherwise touch safely. The governance tradeoff is real—Action Fabric gives you audit trails and policy enforcement at the action boundary, but at per-operation cost.

**Key technical details:**
- ServiceNow MCP Server exposes workflows, playbooks, approval chains, and service catalog actions to external agents
- Pricing: action-based (per-operation), variable consumption per agentic session, bundled assists + overage
- Launch partner: Anthropic Claude (Claude Cowork integration)
- Surfaces: workflows, playbooks, approval chains, service catalog, business rules
- Key risk: variable consumption in retry loops creates unpredictable billing; no hard spend caps reported at launch

---

### 5. Google ADK Long-Running Agent Pattern — Pause/resume with durable memory schemas and event-driven dormancy published May 12, 2026

**Source:** [Google Developers Blog](https://developers.googleblog.com/en/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/) | [Google ADK Interactions API](https://developers.googleblog.com/en/building-agents-with-the-adk-and-the-new-interactions-api/) | [Redis ADK Memory](https://redis.io/blog/build-google-adk-agents-with-persistent-real-time-memory-on-redis/)

On May 12, 2026, Google published production guidance for building long-running AI agents with the Agent Development Kit (ADK)—agents that pause for days, resume when triggered, and maintain coherent context across weeks of real-world time. The guidance tackles three failure modes of naive stateless agents: **prompt context pollution** (hundreds of conversation turns fill history with irrelevant noise), **token cost explosion** (replaying full history on every call), and **reasoning hallucinations** (agents hallucinating steps that never occurred after long pauses). The solution involves three architectural primitives: durable memory schemas (structured rather than raw JSON vector storage), event-driven dormancy gates (replacing active polling with event triggers), and multi-agent delegation (routing idle-time subtasks to specialized sub-agents).

Google demonstrated the pattern with a New Hire Onboarding Coordinator Agent that sends welcome packets, pauses while documents are signed (potentially days), delegates IT provisioning to sub-agents, waits for hardware delivery confirmation, then sends personalized day-one schedules—all without losing context or burning tokens during idle periods. The new **Interactions API** provides a conversation interface for agents that need to interact with multiple users or systems over time, complementing the dormancy model. Redis is supported as a persistent memory backend for real-time state across agent restarts. Full source code is available on GitHub.

For agentic engineers, this is the definitive public reference for production long-running agent architecture. The event-driven dormancy gate pattern—replacing `sleep` polling with event queue consumption—is directly applicable to any agent framework and significantly reduces compute cost for agents that spend most of their time waiting for human or system responses. The structured durable memory schema approach (preventing context accumulation) is a best practice that applies regardless of whether you're on ADK, LangGraph, or a custom stack.

**Key technical details:**
- ADK v2.0.0-alpha includes graph-based workflow runtime for long-running orchestration
- Event-driven dormancy gates replace polling loops; agents wake on external events (webhook, queue message, cron)
- Durable memory schema: structured object storage vs. raw JSON in vector DB; prevents context accumulation
- Interactions API: multi-user/multi-system conversation threading for long-running agents
- Redis backend: persistent real-time memory across agent restarts and deployments
- Full open-source example: New Hire Onboarding Coordinator Agent on GitHub

---

## Deep Dive: Most Important Item

### Claude Managed Agents: Dreaming, Outcomes, and Multiagent Orchestration

This is the most architecturally significant release of the week because it introduces three production primitives—self-improvement, self-evaluation, and parallel delegation—as a managed platform service, collapsing what previously required custom infrastructure into first-class API features. For the first time, a hosted agent platform provides closed-loop quality control (outcomes grader), cross-session learning (dreaming), and governed parallel execution (multiagent) within a single auditable system.

**What the Platform Provides**

1. **Dreaming (Research Preview):** A scheduled background process that reviews past sessions in the agent's memory store, extracts recurring patterns (mistakes, convergent workflows, team-shared preferences), curates and restructures memory for signal quality, and optionally requires human approval before persisting changes. Runs independently of active sessions.

2. **Outcomes (Public Beta):** A rubric-based self-evaluation system where a separate grader agent—running in an isolated context window to prevent contamination—evaluates task outputs against developer-defined success criteria (quantitative or qualitative) and triggers automatic re-attempts with targeted feedback until the bar is cleared. Measured +8.4% to +10.1% improvement on document generation tasks.

3. **Multiagent Orchestration (Public Beta):** A coordinator agent (configured with `multiagent.type: "coordinator"`) delegates tasks to up to 20 registered specialist agents. Each specialist has independent model selection, system prompt, tools, and session thread. Agents run in parallel on a shared filesystem; events are persistent; full delegation trace visible in Claude Console.

4. **Webhooks:** Async callbacks on task completion, enabling agents to run fire-and-forget with results delivered via HTTP POST to developer-controlled endpoints.

5. **Memory System:** Persistent memory store shared across sessions; dreaming refines and restructures this store between sessions; individual agents write learnings during active work.

**Why This Matters**

The outcomes grader architecture solves a fundamental agentic quality problem: when an agent evaluates its own output, the grader is influenced by the same reasoning chain that produced the output—a form of confirmation bias. By isolating the grader in a separate context window, Anthropic implements an adversarial evaluation loop that more reliably detects quality failures. The +10-point improvement on hard tasks confirms that rubric-based self-correction outperforms prompting-only approaches for complex, multi-step outputs.

Dreaming addresses the equally fundamental problem of agent stagnation. Most production agents plateau after initial deployment because they lack a mechanism to generalize learnings across sessions. Dreaming's cross-session pattern extraction creates a genuine feedback loop between production usage and agent capability—without requiring retraining or model updates. The human-in-the-loop approval gate for memory updates is a well-designed governance control that prevents runaway self-modification while still enabling automated improvement.

For enterprise teams, the combination of all three features changes the ROI calculation for hosted agents. Previously, self-improvement required custom memory pipelines; self-evaluation required custom grading harnesses; parallel delegation required custom orchestration frameworks—each adding engineering cost and operational complexity. Managed Agents now provides all three, with Claude Console traceability satisfying audit requirements.

**Architectural Significance**

This release introduces a new primitive: **the self-correcting, self-improving agent cluster**. The pattern is:
- `Coordinator` assigns subtasks to specialists and synthesizes results
- `Outcomes Grader` evaluates each output against rubric in isolated context
- `Dreaming Process` refines cross-session memory between runs
- `Webhook Sink` decouples task completion from caller wait time

This is a shift from single-turn or multi-turn agents toward persistent, evolving agent systems that accumulate organizational knowledge over time. The implications for multi-tenant enterprise deployments (where dreaming can learn across thousands of user sessions) are significant.

**Competitive Context**

OpenAI's Agents SDK (v0.13) provides handoffs and guardrails but lacks a native outcomes grader or dreaming equivalent—self-improvement must be custom-built. LangGraph (v1.1.4) provides best-in-class state persistence and error recovery but requires developers to implement all evaluation and memory refinement logic. Google ADK v2.0.0-alpha provides long-running agent infrastructure and event-driven dormancy but no hosted self-evaluation primitive. Microsoft Agent Framework 1.0 covers graph-based orchestration in .NET/Python but no managed memory evolution. Anthropic's Managed Agents is currently the only platform offering all three (self-evaluation, self-improvement, parallel delegation) as managed, observable platform services.

---

## Benchmark Data (SWE-bench, GAIA, AgentBench, etc.)

```json
[
  {
    "benchmark": "SWE-bench Verified",
    "date": "2026-05-14",
    "source": "https://rapidclaw.dev/blog/ai-agent-benchmarks-2026",
    "results": [
      {"agent": "Claude Opus 4.7", "score": 87.6, "metric": "% resolved"},
      {"agent": "GPT-5.3 Codex", "score": 85.0, "metric": "% resolved"},
      {"agent": "Claude Opus 4.5", "score": 80.9, "metric": "% resolved"},
      {"agent": "Average (83 models)", "score": 63.4, "metric": "% resolved"}
    ],
    "notes": "500 human-validated GitHub issue instances. OpenAI stopped self-reporting scores after confirmed evaluation-set leakage (per UC Berkeley research, April 2026). Prefer third-party scores. Note: GPT-5.5 Instant reported 88.7% on SWE-bench Verified in prior digest (2026-05-13)."
  },
  {
    "benchmark": "GAIA (Princeton HAL)",
    "date": "2026-05-14",
    "source": "https://rapidclaw.dev/blog/ai-agent-benchmarks-2026",
    "results": [
      {"agent": "Claude Sonnet 4.5", "score": 74.6, "metric": "% correct"},
      {"agent": "Claude Mythos Preview", "score": 52.3, "metric": "% correct (BenchLM)"}
    ],
    "notes": "Anthropic sweeps top six HAL leaderboard spots. GAIA tests real-world tool use: web search, file handling, multi-step reasoning across modalities."
  },
  {
    "benchmark": "WebArena-Lite (Plan-and-Execute with dynamic replanning)",
    "date": "2026-04-12",
    "source": "https://agentmarketcap.ai/blog/2026/04/12/react-vs-plan-execute-vs-tree-of-thought-production-2026",
    "results": [
      {"agent": "Plan-and-Execute with dynamic replanning", "score": 57.58, "metric": "% task success"}
    ],
    "notes": "Benchmark for web navigation agents. Plan-and-Execute consistently outperforms ReAct on long-horizon tasks (>10 steps). ReAct remains superior for short-horizon tasks (1-5 tool calls)."
  },
  {
    "benchmark": "AgentBench",
    "date": "2026-05-14",
    "source": "https://agentsindex.ai/compare/agentbench-vs-swe-bench",
    "results": [],
    "notes": "Maintained by Tsinghua THUDM. Evaluates agents across 8 environments (OS, database, web, KG, lateral thinking, house-keeping, web shopping, mind2web). Open-source Apache 2.0, accepted ICLR 2024. No updated leaderboard scores available for May 2026 reporting period."
  },
  {
    "benchmark": "Claude Managed Agents Outcomes Internal",
    "date": "2026-05-06",
    "source": "https://claude.com/blog/new-in-claude-managed-agents",
    "results": [
      {"agent": "Claude Managed Agents with Outcomes", "score": 10, "metric": "points improvement over standard prompting loop (max gains on hardest tasks)"},
      {"agent": "Outcomes on .docx generation", "score": 8.4, "metric": "% task success improvement"},
      {"agent": "Outcomes on .pptx generation", "score": 10.1, "metric": "% task success improvement"}
    ],
    "notes": "Internal Anthropic benchmark. Outcomes grader runs in isolated context window. Harvey (legal AI) reported ~6x completion rate improvement using dreaming + outcomes in production."
  },
  {
    "benchmark": "Benchmark Trustworthiness Warning",
    "date": "2026-04-12",
    "source": "https://rapidclaw.dev/blog/ai-agent-benchmarks-2026",
    "results": [],
    "notes": "UC Berkeley research (April 12, 2026) demonstrated all 8 major agent benchmarks can be reward-hacked to ~100%. Recommendation: prefer third-party evaluation scores; run held-out private evaluations for production decisions. OpenAI stopped reporting SWE-bench Verified self-scores after evaluation-set leakage confirmed."
  }
]
```

---

## Architecture / Pattern Notes

### Self-Correcting Multi-Agent Loop (Dominant Production Pattern, May 2026)

The dominant emerging architecture combines parallel delegation with isolated self-evaluation and cross-session memory refinement. Rather than a single agent that prompts itself to self-critique, the pattern uses structurally separated roles: a coordinator delegates, specialists execute, an isolated grader evaluates, and a background dreamer refines memory between runs.

```
[Coordinator Agent] (orchestration, task decomposition)
  ↓ delegate subtask
[Specialist Agent A] (domain: legal, code, data)
  ↓ output
[Outcomes Grader] (isolated context window, rubric evaluation)
  ↓ pass/fail + targeted feedback
[Specialist Agent A] (re-attempt if fail)
  ↓ accepted output
[Coordinator Agent] (synthesize results)
  ↓ session complete
[Dreaming Process] (background, cross-session pattern extraction)
  ↓ memory update
[Shared Memory Store] (structured, evolving)
  ↑ context inject
[Coordinator Agent] (next session starts with refined memory)
```

**Mermaid diagram (for downstream renderer):**
- `coordinator` → `specialist_a` (edge: delegate subtask)
- `coordinator` → `specialist_b` (edge: delegate subtask)
- `specialist_a` → `grader` (edge: output for evaluation)
- `specialist_b` → `grader` (edge: output for evaluation)
- `grader` → `specialist_a` (edge: fail + feedback)
- `grader` → `coordinator` (edge: pass → synthesize)
- `coordinator` → `webhook_sink` (edge: task complete notification)
- `dreaming_process` → `memory_store` (edge: curate and restructure)
- `memory_store` → `coordinator` (edge: inject context at session start)

### Framework Comparison Table

| Framework | Core Abstraction | Graph Type | Best For |
|-----------|-----------------|------------|----------|
| Claude Managed Agents | Coordinator + Specialist + Grader + Memory | Managed hosted DAG | Self-improving agents needing outcomes grading; production with audit requirements |
| LangGraph v1.1.4 | State machine with checkpointed nodes | Cyclic graph with persistence | Complex stateful workflows; best error recovery (41/47 failures); production Python/JS |
| CrewAI v1.12 | Crew of role-playing agents with tasks | Sequential + parallel | Fastest prototyping; no-code + pro-code; OpenAI-compatible providers |
| AutoGen AG2 Beta | Event-driven actor model | Streaming multi-agent graph | Research and complex reasoning; multi-provider LLM; non-OpenAI backends |
| OpenAI Agents SDK v0.13 | Agent handoffs + guardrails | Handoff graph (flat) | OpenAI-native apps; fast integration; session persistence; MCP resource support |
| Google ADK v2.0.0-alpha | Long-running sessions + event dormancy | Graph-based workflow runtime | Pause/resume agents; multi-day workflows; Vertex AI ecosystem |
| Microsoft Agent Framework 1.0 | Graph-based orchestration | Single/multi-agent graph | .NET and Python enterprise; Microsoft 365 integration; Entra Agent ID governance |
| Pydantic AI v1.71 | Composable typed agents | Flat + composable | Type-safe agent pipelines; Pythonic API; easy LLM provider switching |

### Event-Driven Dormancy Gate Pattern

The event-driven dormancy gate replaces the anti-pattern of agents that `sleep()` and poll for task completion. Instead of blocking a thread or process, the agent serializes its full state to durable storage, unregisters from the execution runtime, and resumes only when an external event (webhook, queue message, cron trigger, or human callback) delivers a wake signal. This has three engineering advantages:

1. **Zero compute cost during wait:** An agent waiting for a document to be signed (potentially days) consumes no compute resources between the signature event and its wake.
2. **Horizontal scalability:** Dormant agent state is just a blob in a database; thousands of concurrent long-running agents impose no active compute load.
3. **Reliability:** If the execution runtime restarts (deploy, crash), dormant agents resume from persisted state on next wake event—they do not lose progress.

Google ADK's May 2026 guidance formalizes this pattern with `dormancy gates` as a named primitive. The OMAR system used in this research pipeline uses the same pattern. The practical implication: any agent that blocks on human input, external API polling, or multi-day task horizons should use this pattern rather than occupying a live thread.

---

## Analysis & Impact for Agentic Engineers

- **Adopt Outcomes-graded evaluation before deploying agents to production.** The Claude Managed Agents outcomes grader—or an equivalent isolated-context evaluation loop—is now a measurable best practice, with up to +10 points task-success improvement on hard tasks. If you're not running a rubric-based eval at task completion, your agents are shipping untested outputs at production scale. The isolation of the grader from the agent's reasoning context is the key architectural detail: a same-context self-critic is unreliable.

- **Enterprise agentic deployments in SAP, ServiceNow, or Workday environments must budget for per-action pricing.** ServiceNow's Action Fabric and SAP's Autonomous Suite have both shifted to metered, action-based pricing. If you're building agents that interact with these platforms, model your expected monthly action volume (including retry loops) before committing to an architecture—variable consumption in failed workflows can create orders-of-magnitude billing surprises. Request spend caps where available.

- **Use event-driven dormancy gates instead of polling for any agent with wait times over 30 seconds.** The Google ADK long-running agent pattern (published May 12, 2026) is the public reference implementation. If you are building on LangGraph, the equivalent is checkpointed nodes with external event triggers; on OpenAI Agents SDK, use session persistence + webhook callbacks. The engineering investment is upfront but dramatically reduces both compute cost and failure surface for multi-day agent tasks.

- **Register your agent infrastructure with a dedicated identity provider before connecting to enterprise data.** Microsoft Entra Agent ID (public preview) and Okta for AI Agents both provide agent-first identity management with conditional access, privilege management, and audit logging. The 88% enterprise security incident rate reported by Okta is not theoretical—prompt injection targeting credential theft is a documented attack vector against agents with persistent tool access. Treat every agent as a non-human identity with the same lifecycle governance you apply to service accounts.

- **If building on AWS, configure the AWS MCP Server before writing any custom AWS integration tooling.** The GA of the AWS MCP Server eliminates the need to maintain bespoke IAM credential handling, documentation retrieval, and sandboxed script execution in your agent stack. The `run_script` tool's single-round-trip multi-API aggregation is a concrete performance win for infrastructure agents that previously issued 10+ sequential `call_aws` operations. Start with the `mcp-proxy-for-aws` pattern and restrict IAM scope to the minimum required for your agent's tasks.

---

## Key Takeaways (TL;DR)

- Anthropic's Claude Managed Agents now offers dreaming (cross-session self-improvement), outcomes (isolated rubric grading), and multiagent orchestration (parallel specialist delegation) as managed platform primitives—collapsing months of custom infrastructure work into API calls.
- AWS's Agent Toolkit MCP Server is GA: 15,000+ AWS API operations, current documentation retrieval, and sandboxed Python execution in a single MCP server compatible with all major agent IDEs.
- SAP's Autonomous Enterprise deploys 200+ Joule agents across its ERP suite with Claude as the primary reasoning engine, and explicitly prohibits third-party agents outside SAP-endorsed architectures—a governance model that will define ERP agent integration patterns for years.
- ServiceNow Action Fabric opens enterprise workflows to any external AI agent via MCP, but introduces metered per-action pricing that creates billing unpredictability for agentic retry loops.
- The event-driven dormancy gate is the production standard for long-running agents—formalized in Google ADK's May 2026 guidance—replacing polling with state serialization and external event wakeups for zero-cost idle periods.
- UC Berkeley confirmed all 8 major agent benchmarks can be reward-hacked to ~100%; production benchmark selection should favor third-party evaluations and private held-out test sets.

---

*Sources:*

- https://claude.com/blog/new-in-claude-managed-agents
- https://platform.claude.com/docs/en/managed-agents/overview
- https://platform.claude.com/docs/en/managed-agents/multi-agent
- https://platform.claude.com/docs/en/managed-agents/agent-setup
- https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/
- https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/
- https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/
- https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html
- https://github.com/aws/agent-toolkit-for-aws
- https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/
- https://news.sap.com/2026/05/sap-anthropic-to-bring-claude-sap-business-ai-platform/
- https://news.sap.com/2026/05/sap-sapphire-keynote-business-ai-platform-power-autonomous-enterprise/
- https://www.techtarget.com/searcherp/news/366642887/The-AI-technology-behind-SAPs-Autonomous-Enterprise-pitch
- https://www.techtarget.com/searcherp/news/366642871/SAP-unveils-agentic-AI-tools-to-partially-automate-ERP-suite
- https://nowben.com/servicenow-launches-action-fabric-to-open-full-system-of-action-to-any-ai-agent/
- https://www.pymnts.com/artificial-intelligence-2/2026/servicenow-sap-and-workday-make-ai-agents-pay-to-play/
- https://www.reworked.co/digital-workplace/servicenow-launches-action-fabric-major-overhaul-of-ai-control-tower/
- https://www.cio.com/article/4169954/servicenows-ai-control-tower-offers-hazy-view-of-spend.html
- https://developers.googleblog.com/en/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/
- https://developers.googleblog.com/en/building-agents-with-the-adk-and-the-new-interactions-api/
- https://redis.io/blog/build-google-adk-agents-with-persistent-real-time-memory-on-redis/
- https://claudeapi.com/en/blog/news/code-with-claude-conference/
- https://laravel-news.com/laravels-ai-sdk-adds-sub-agents
- https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/
- https://rapidclaw.dev/blog/ai-agent-benchmarks-2026
- https://agentsindex.ai/compare/agentbench-vs-swe-bench
- https://agentmarketcap.ai/blog/2026/04/12/react-vs-plan-execute-vs-tree-of-thought-production-2026
- https://www.digitalapplied.com/blog/agent-architecture-patterns-taxonomy-2026
- https://openclaw-ai.net/en/blog/ai-agent-architecture-patterns-2026
- https://www.microsoft.com/en-gb/security/business/identity-access/microsoft-entra-agent-id
- https://www.okta.com/en-in/products/govern-ai-agent-identity/
- https://www.certiv.ai/product/
- https://www.zenity.io/platform/ai-observability-platform
- https://www.ibm.com/solutions/agentic-ai-identity-management
- https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
- https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/
- https://joshbersin.com/2026/04/the-reinvention-of-workday-from-system-of-record-to-platform-of-agents/
- https://pecollective.com/blog/ai-agent-frameworks-compared/
- https://softmaxdata.com/blog/definitive-guide-to-agentic-frameworks-in-2026-langgraph-crewai-ag2-openai-and-more/
- https://mcpblog.dev/blog/2026-03-15-a2a-v1-mcp
- https://agentmarketcap.ai/blog/2026/04/11/a2a-vs-mcp-agent-protocol-war-2026
- https://thenextweb.com/news/sap-autonomous-enterprise-ai-agents-sapphire
