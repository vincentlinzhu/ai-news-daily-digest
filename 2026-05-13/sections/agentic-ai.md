# Agentic AI — 2026-05-13

## Top Stories (3-5)

### 1. Pydantic AI v1.95.0 Ships Native Tool Search and Instrumentation Capability — Production-grade framework adds provider-agnostic tool routing with Gemini 3 support

**Source:** [GitHub Release](https://github.com/pydantic/pydantic-ai/releases/tag/v1.95.0) | [Pydantic AI Changelog](https://ai.pydantic.dev/changelog.html)

Released on May 13, 2026, Pydantic AI v1.95.0 introduces **Native Tool Search** as a first-class feature on Anthropic and OpenAI, with custom search strategies available on any provider. This enables agents to discover and invoke the right tool at runtime rather than relying on exhaustive enumeration — a critical capability when tool registries grow beyond a few dozen entries. The release also deprecates the `Agent(instrument=...)` parameter in favor of a new `Instrumentation` capability, signaling a cleaner separation between agent configuration and observability concerns.

Also notable is the addition of structured output combined with tool support for Google's **Gemini 3** model — pydantic-ai now provides a consistent abstraction layer across all three frontier providers for tool-augmented structured generation. The v1.94.0 release the same day also reinstated the `mistral` dependency as a default (excluding the compromised version 2.4.6), resolving a supply-chain security concern that had blocked production deployments on Mistral-backed agents.

Preparing for a v2 release expected in June, the release renames "built-in tools" to "native tools" and introduces a `local=` opt-in parameter for provider-adaptive capability fallback, deprecating the silent automatic-fallback behavior that caused subtle correctness bugs. Agentic engineers using pydantic-ai should audit their `instrument=` usage and plan migration before v2 lands.

**Key technical details:**
- Native Tool Search on Anthropic and OpenAI; custom strategies via `capabilities=[NativeTool(...)]` on any provider
- New `Instrumentation` capability replaces deprecated `Agent(instrument=...)` — affects all observability integrations
- Structured output + tool use now supported on Gemini 3, completing parity across OpenAI / Anthropic / Google
- `local=` parameter for explicit provider-adaptive fallback; silent fallback removed (breaking change in June v2)
- Bedrock client runtime fix and model ID normalization for capability profiles; Vercel AI event emission fix
- Mistral 2.4.6 excluded by pinning; security implications for pipelines that auto-upgrade mistral

---

### 2. ServiceNow Build Agent Goes Cross-IDE with Governance by Default — Cursor, Windsurf, Claude Code, and GitHub Copilot now deploy production ServiceNow apps with native governance

**Source:** [BusinessWire](https://www.businesswire.com/news/home/20260506008934/en/ServiceNow-Build-Agent-now-works-inside-every-major-AI-coding-tool-governed-by-default) | [ServiceNow Community](https://www.servicenow.com/community/product-launch-blogs/build-anywhere-run-on-servicenow-deploying-from-external-ides/ba-p/3522466) | [May Update Notes](https://www.servicenow.com/community/now-assist-for-creator-articles/what-s-new-in-may-for-build-agent/ta-p/3535155)

ServiceNow made its **Build Agent** generally available on May 6, 2026, with a headline feature: agents now operate natively within Cursor, Windsurf, Claude Code, and GitHub Copilot. Developers can generate production-ready ServiceNow apps and flows using natural language prompts in their IDE of choice, and the resulting apps receive automatic governance — security roles, data models, and App Engine Management Center checks — before deployment. This "build anywhere, governed everywhere" model directly addresses the enterprise AI coding dilemma: developer velocity versus compliance.

The May 2026 feature drop also adds **In-App Agents** — agents embedded within custom ServiceNow applications that read app metadata, data, workflows, and business logic to give domain-specific recommendations. This is a meaningful architectural shift: rather than a single Build Agent knowing about ServiceNow in general, each deployed app can carry a specialized agent that understands only its bounded context. For enterprise builders, this reduces hallucination risk and compliance surface compared to a single omniscient coding agent.

The integration uses the ServiceNow SDK, which enables external coding agents to create apps using ServiceNow best practices without requiring browser access to a ServiceNow instance — reducing session management overhead and enabling headless CI/CD pipelines. This pattern (SDK-mediated agent-platform integration with mandatory governance at the export boundary) is likely to become a template for other enterprise platform vendors.

**Key technical details:**
- GA in ServiceNow Studio plus extensions for Cursor, Windsurf, Claude Code, GitHub Copilot
- ServiceNow SDK enables agent code generation without browser session; governance applied at export
- Free App Engine Management Center access governs every app before deployment — zero opt-out
- In-App Agents added: conversational agent construction scoped to a specific deployed application's context
- Apps built outside Studio receive the same governance pipeline (security roles, data models, ACLs)
- All builds are auditable via existing ServiceNow audit logs; no separate compliance tooling required

---

### 3. Cognizant OneCognizant: 350,000-Employee Multi-Agent AI Hits 50% Efficiency Gains — Largest verified enterprise multi-agent deployment shows production viability at global scale

**Source:** [Cognizant Blog](https://www.cognizant.com/us/en/insights/insights-blog/enterprise-multi-agent-ai-systems-transform-digital-workplace) | [Enterprise AI Executive](https://enterpriseaiexecutive.ai/p/cognizant-s-350-000-employee-multi-agent-ai) | [Microsoft AI First Movers](https://www.microsoft.com/en-in/aifirstmovers/FY26Cognizant)

Cognizant's **OneCognizant (1C)** platform has emerged as the largest verified enterprise multi-agent AI deployment in the industry. Five months after its July 2025 rollout, the system now serves over 70% of Cognizant's 350,000 associates across 50+ countries, orchestrating more than 80 enterprise agents and 6,000 daily digital interactions through a single web and mobile interface. Reported outcomes: 50% improvement in operational efficiency, ~50% reduction in support ticket volumes, and 35% rise in employee engagement with 10,000 average daily users. This is the most significant production data point published for enterprise multi-agent orchestration at scale.

Built using Cognizant's own **Neuro AI Multi-Agent Accelerator**, 1C integrates hundreds of enterprise applications — ServiceNow ticketing, HR systems, facilities booking, IT provisioning — into a single agentic layer. Employees compose multi-step requests ("book a seat and raise an IT ticket") in a single interaction, with the orchestration layer routing to the appropriate specialized agents. The platform demonstrates that agent orchestration is tractable at scale when backed by: (1) a unified data model, (2) bounded specialized agents rather than one general agent, and (3) a thin coordination layer over existing enterprise SaaS.

The case is significant beyond the headline metrics. It demonstrates that multi-agent systems can deliver positive ROI without requiring a ground-up data re-architecture — 1C runs on top of existing enterprise SaaS subscriptions, not a rip-and-replace. For agentic engineers, the architectural lesson is clear: specialized agents with narrow context windows and clear API contracts outperform monolithic agents with broad access, especially in environments where audit and explainability matter.

**Key technical details:**
- 80+ specialized enterprise agents; 6,000+ daily digital interactions orchestrated through 1C
- Built on Cognizant Neuro® AI Multi-Agent Accelerator; integrates ServiceNow, HR, facilities, and IT systems
- Multi-step agentic requests (e.g., combine leave + IT ticket) fulfilled in a single user interaction
- 50% operational efficiency gain, ~50% reduction in support ticket volumes, 35% rise in engagement
- Deployed to 70%+ of 350,000 employees across 50+ countries within 5 months
- Governance via existing enterprise SaaS permissions — no new IAM infrastructure required at platform level

---

### 4. AWS MCP Server Generally Available — Fully managed MCP with IAM guardrails and CloudTrail audit brings enterprise governance to agent-tool connections

**Source:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) | [AWS MCP Docs](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html) | [IAM for MCP](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_service-with-iam.html)

Amazon Web Services announced the **general availability of the AWS MCP Server** on May 6, 2026, as part of the broader Agent Toolkit for AWS. It is a fully managed Model Context Protocol server that grants AI coding agents secure, auditable access to AWS services — available at no additional charge in us-east-1 and eu-central-1. The server supports identity-based IAM policies, temporary credentials, service roles, and policy condition keys, providing granular least-privilege access. All API calls are logged to CloudTrail, and operational metrics are available via CloudWatch.

Since its preview, AWS has added three production features: (1) a single tool capable of calling **any AWS API** — eliminating the need to pre-enumerate tool schemas for each service; (2) sandboxed script execution for multi-step Python operations against AWS resources; and (3) **agent skills** — curated, reusable procedure libraries covering IaC, storage, analytics, and serverless. The skill library addresses a critical gap in raw MCP: knowing that a tool exists does not mean the agent knows the idiomatic sequence to use it correctly.

The IAM integration is architecturally significant: it makes MCP a first-class citizen of the AWS identity model, meaning existing IAM policies, SCPs, and permission boundaries apply to agent-to-service calls without additional tooling. For teams already using AWS Organizations or AWS Control Tower, this provides immediate governance coverage for agents without a separate agent-IAM layer. This contrasts with many MCP deployments where tool permissions are managed outside the enterprise identity fabric.

**Key technical details:**
- Fully managed MCP server; no additional charge; GA in us-east-1 and eu-central-1
- IAM: identity-based policies, service roles, temporary credentials, ABAC (partial), policy condition keys
- CloudTrail audit logs all API calls; CloudWatch for operational metrics
- Single universal tool for any AWS API — no per-service schema enumeration needed
- Sandboxed Python execution for multi-step operations; agent skills library (IaC, storage, analytics, serverless)
- Agents authenticate via existing IAM credentials; no new credential management plane required

---

### 5. A2A Protocol Reaches v1.0 with Signed Agent Cards and Linux Foundation Governance — Multi-cloud adoption at 150+ organizations as enterprise standard solidifies

**Source:** [A2A Changelog](https://github.com/google/A2A/blob/7b900e77/CHANGELOG.md) | [AgentMarketCap Analysis](https://agentmarketcap.ai/blog/2026/04/12/google-a2a-protocol-state-2026-adoption-enterprise) | [Stellagent Overview](https://stellagent.ai/insights/a2a-protocol-google-agent-to-agent)

The A2A (Agent-to-Agent) Protocol reached **v1.0 on March 12, 2026**, and by April 2026 had grown to 150+ supporting organizations (up from 50 at launch) with 22,000+ GitHub stars. Most significantly, the protocol was donated to the **Linux Foundation** in December 2025, where it now operates under neutral governance alongside Anthropic's Model Context Protocol — both protocols now share a neutral standards body, reducing single-vendor lock-in concerns for enterprise adopters. Native A2A support is now available in Azure AI Foundry, Amazon Bedrock, and Google Vertex AI.

v1.0 introduced **Signed Agent Cards** — cryptographic signing that enables enterprise systems to verify agent identity before delegating tasks — addressing a core trust gap in early agent-to-agent communication. The release also formalized multi-tenant architecture, streamable HTTP transport for long-running workflows, and backward-compatible version negotiation via Agent Card metadata. Breaking changes include modernized OAuth 2.0 flows (removing implicit/password grant, adding device code and PKCE), standardized American spelling across the spec, and removal of deprecated fields.

The combination of Linux Foundation governance and major hyperscaler native support makes A2A the most broadly adopted inter-agent communication standard as of mid-2026. For teams building multi-agent architectures that span cloud providers, A2A is now the lowest-risk choice for agent-to-agent task delegation — the alternative (proprietary orchestration APIs) requires custom adapters for every cross-vendor boundary.

**Key technical details:**
- v1.0 stable; breaking changes: OAuth 2.0 modernized (PKCE, device code; no implicit/password), ID standardization, deprecated fields removed
- Signed Agent Cards: cryptographic identity verification before task delegation — replaces implicit trust
- Streamable HTTP transport replaces synchronous request/response for long-running agent workflows
- Backward-compatible version negotiation: Agent Cards advertise supported protocol versions
- Linux Foundation neutral governance since December 2025; 150+ orgs including Azure, Bedrock, Vertex AI
- Combined notification configs, non-complex IDs, and LF package prefix are now mandatory

---

## Deep Dive: Most Important Item

### ServiceNow Build Agent + Cross-IDE Governance: The "Build Anywhere, Governed Everywhere" Pattern

ServiceNow's Build Agent GA represents the most architecturally significant development this week because it operationalizes a governance pattern that the industry has been debating since agentic coding became mainstream: how do you let developers use frontier AI coding agents while ensuring that the resulting deployments satisfy enterprise compliance requirements? The ServiceNow answer — mandate governance at the **export boundary** rather than at the IDE or agent level — is a deployable, auditable solution to a problem that has blocked enterprise adoption of agentic coding at scale.

**What the Platform Provides**

1. **Cross-IDE MCP-style integration**: The ServiceNow SDK installs as a plugin in Cursor, Windsurf, Claude Code, and GitHub Copilot, giving the coding agent full knowledge of the target ServiceNow environment (data model, workflows, business logic) without requiring a live browser session.

2. **Governance at export**: Apps generated in any external IDE are automatically submitted to App Engine Management Center (AEMC) before deployment. AEMC applies security roles, data model validation, ACL checks, and policy controls — the developer cannot bypass this step.

3. **In-App Agents for bounded context**: Each deployed custom application can host a specialized agent scoped to that app's metadata, workflows, and data. This prevents the "oracle agent" anti-pattern where a single agent has broad read access to the entire platform.

4. **Conversational app construction**: Build Agent accepts natural language prompts within the IDE to generate complete ServiceNow application scaffolding, flows, and agent skills — reducing time from spec to deployable app.

5. **Audit log continuity**: All agent-generated code passes through the same audit pipeline as human-written code. There is no separate compliance check for "AI-generated" apps — governance is uniform.

**Why This Matters**

The governance gap is the primary blocker to enterprise AI coding agent adoption. Individual developers can use Cursor or Claude Code freely, but IT and security teams cannot approve unrestricted agent-generated code at scale. The standard mitigation — code review — does not scale when coding agents can produce 10,000 lines of production logic in minutes. ServiceNow's approach sidesteps the review problem by constraining the output space: agents can only generate code that the platform can validate against its known schema and policy model.

This pattern is reproducible. Any enterprise platform with a formal data model (Salesforce, SAP, Workday, Microsoft Dynamics) can implement the same architecture: SDK-mediated agent integration + mandatory governance gate at the export boundary. The critical enabler is the **platform schema as guardrail** — the agent cannot generate code that violates the platform's type system because the SDK enforces types at generation time. This is a qualitatively different governance model than post-hoc code review or prompt filtering.

For production teams, the In-App Agents feature is the more durable architectural investment. By scoping each agent to the bounded context of a single application, ServiceNow avoids the "context window as attack surface" problem: a compromised or misbehaving agent in App A cannot read data from App B. This locality principle — one agent per bounded context, one bounded context per agent — is becoming the production consensus for secure enterprise agent deployment.

**Architectural Significance**

The pattern introduces a new primitive: the **governed agent sandbox**. Unlike a general-purpose agent with broad API access, a governed agent sandbox:
- Has a predefined schema contract (knows only the platform API, not arbitrary external services)
- Exports artifacts that are validated against the platform's policy model before execution
- Maintains audit continuity with human-authored code — no special treatment for AI-generated outputs
- Supports specialization (In-App Agents) without requiring explicit permission management per agent

This is distinct from agent isolation (sandboxing for security) and agent orchestration (coordinating multiple agents). It is governance-by-construction: the agent's action space is constrained so that invalid or non-compliant outputs are structurally impossible, not just detected after the fact.

**Competitive Context**

Salesforce Agentforce uses a similar bounded approach — agents operate within the Salesforce data model and are constrained by Salesforce permissions — but Agentforce currently requires development to happen within the Salesforce ecosystem. ServiceNow's cross-IDE support allows developers to stay in their preferred tools (Cursor, VS Code) while still meeting enterprise governance requirements. SAP's Joule agents are deeply integrated with SAP's business process graph, providing similar schema-guardrail governance, but have not yet published cross-IDE development support. The Google/Microsoft approach (Vertex AI Agent Builder, Azure AI Foundry) provides governance through IAM and platform-level controls, but governance is applied to the runtime rather than the build-time export boundary — a later, weaker control point.

---

## Benchmark Data (SWE-bench, GAIA, AgentBench, etc.)

```json
[
  {
    "benchmark": "SWE-bench Pro",
    "date": "2026-05-12",
    "source": "https://benchlm.ai/benchmarks/swePro",
    "results": [
      {"agent": "Claude Mythos Preview", "score": 77.8, "metric": "% resolved"},
      {"agent": "Claude Opus 4.7 (Adaptive)", "score": 64.3, "metric": "% resolved"},
      {"agent": "GPT-5.5", "score": 58.6, "metric": "% resolved"}
    ],
    "notes": "30 models evaluated. More challenging than SWE-bench Verified; designed to differentiate frontier coding agents. Public dataset top scores around 23%, private/frontier track shows 70%+ gap."
  },
  {
    "benchmark": "SWE-bench Verified",
    "date": "2026-04-30",
    "source": "https://www.vals.ai/benchmarks/swebench-06-13-2025",
    "results": [
      {"agent": "GPT-5.5", "score": 82.60, "metric": "% resolved"},
      {"agent": "Claude Opus 4.7", "score": 82.00, "metric": "% resolved"},
      {"agent": "Gemini 3.1 Pro Preview", "score": 78.80, "metric": "% resolved"}
    ],
    "notes": "Performance varies strongly by task difficulty: <15-min tasks resolve at 85-92%; >4-hour tasks resolve at 0-67%. Single-agent, unassisted setting."
  },
  {
    "benchmark": "Terminal-Bench 2.0",
    "date": "2026-04-01",
    "source": "https://www.tbench.ai/leaderboard/terminal-bench/2.0",
    "results": [
      {"agent": "Codex CLI + GPT-5.5", "score": 82.0, "metric": "% tasks completed"},
      {"agent": "ForgeCode + GPT-5.4", "score": 81.8, "metric": "% tasks completed"},
      {"agent": "TongAgents + Gemini 3.1 Pro", "score": 80.2, "metric": "% tasks completed"},
      {"agent": "MiMo V2.5-Pro (open-source SOTA)", "score": 68.4, "metric": "% tasks completed"}
    ],
    "notes": "124 leaderboard entries. Evaluates agents on terminal/CLI task execution. Current overall state-of-the-art is 82.7% (GPT-5.5). Best open-source model is MiMo V2.5-Pro at 68.4%."
  },
  {
    "benchmark": "GAIA (Real-World General Assistant)",
    "date": "2026-04-01",
    "source": "https://rapidclaw.dev/blog/ai-agent-benchmarks-2026",
    "results": [
      {"agent": "Claude Sonnet 4.5 (Princeton HAL)", "score": 74.6, "metric": "% tasks correct"},
      {"agent": "Claude Mythos Preview", "score": 52.3, "metric": "% tasks correct"}
    ],
    "notes": "Measures real-world task performance: reasoning, multimodal understanding, web browsing, tool use. Three difficulty levels. Anthropic models sweep top 6 spots as of April 2026. Requires Hugging Face account for full dataset access."
  },
  {
    "benchmark": "SWE-bench Pro (Public Dataset)",
    "date": "2026-04-01",
    "source": "https://scale.com/leaderboard/swe%5Fbench%5Fpro%5Fpublic",
    "results": [
      {"agent": "Top public model (approx.)", "score": 23.0, "metric": "% resolved (public subset)"}
    ],
    "notes": "Public dataset subset of SWE-bench Pro. The 23% vs 77.8% (Mythos, private) gap illustrates the frontier access disparity. Scale AI hosts and scores submissions."
  }
]
```

---

## Architecture / Pattern Notes

### Governed Agent Sandbox Pattern

The most prominent emerging architecture pattern this week is the **Governed Agent Sandbox**: a constrained agent deployment model where the agent's output space is bounded by the target platform's schema and policy model at build time, not just monitored at runtime.

```
[Developer IDE] (Cursor / Windsurf / Claude Code / GitHub Copilot)
  -> [generates code via]
[SDK-Mediated Agent] (knows target platform schema, data model, permissions)
  -> [exports artifact to]
[Governance Gate] (schema validation, policy check, ACL enforcement)
  -> [deploys to]
[Target Platform Runtime] (ServiceNow / Salesforce / SAP / Workday)
  -> [logs to]
[Unified Audit Trail] (same pipeline as human-authored code)
```

**Mermaid diagram (for downstream renderer):**
- developer_ide -> sdk_agent (edge: natural language prompt)
- sdk_agent -> governance_gate (edge: export artifact)
- governance_gate -> platform_runtime (edge: validated deployment)
- platform_runtime -> audit_trail (edge: all interactions logged)
- sdk_agent -> platform_schema (edge: reads for context)
- platform_schema -> sdk_agent (edge: constrains output space)

---

### Framework Comparison Table

| Framework | Core Abstraction | Graph Type | Best For |
|-----------|-----------------|------------|----------|
| LangGraph 0.2.x | Stateful directed graph (nodes = functions, edges = transitions) | Cyclic / DAG | Complex stateful workflows, production reliability, HITL |
| CrewAI 0.100+ | Role-based agent teams with task delegation | Sequential / hierarchical | Multi-agent prototyping, role-defined specialist teams |
| AutoGen 0.4.x (AG2) | Conversational actors with message passing | Dynamic conversation loop | Conversational multi-agent, research orchestration |
| Pydantic AI 1.95.0 | Typed agent + tool schemas with provider abstraction | Single-agent, composable | Type-safe production agents across multiple LLM providers |
| OpenAI Agents SDK 0.16.x | Agent + handoff + tool + guardrail primitives | DAG with handoffs | OpenAI-native multi-agent with sandbox execution |
| ServiceNow Build Agent | Governed artifact generation with platform schema | Schema-constrained code generation | Enterprise platform development with mandatory governance |

---

### Emerging Pattern: Bounded Context Agents (BCA)

Enterprise deployments in 2026 are converging on a pattern called **Bounded Context Agents** (BCA), borrowed from Domain-Driven Design. Rather than a single powerful agent with broad API access, BCA deploys one specialized agent per domain boundary — each agent reads only the data models, workflows, and tools within its bounded context.

**Why it emerges:** The Cognizant OneCognizant deployment (80 specialized agents vs. one general agent) and ServiceNow's In-App Agents (one agent per custom app) both implement BCA independently. The drivers are: (1) smaller context windows reduce hallucination in domain-specific tasks, (2) per-agent permission scoping limits blast radius of a compromised or misbehaving agent, and (3) specialized agents are faster and cheaper to run than a general agent with a 1M-token context. Production deployments show that BCA outperforms general agents in structured enterprise workflows where the action space is enumerable and auditable. The tradeoff is orchestration complexity — you need a routing layer that decides which bounded-context agent to invoke.

**Concrete example:** In OneCognizant, a user says "Book a seat and submit an IT ticket." The orchestration layer decomposes this into two subtasks, routes to the Facilities Agent and the IT Agent separately, collects both results, and returns a unified response. Neither agent sees data from the other's domain. This is BCA in production at 350,000-user scale.

---

## Analysis & Impact for Agentic Engineers

- **Adopt pydantic-ai's Native Tool Search now if your agents use more than 10 tools.** As registries grow, exhaustive enumeration at every invocation becomes a latency and cost bottleneck. Native Tool Search introduces semantic routing at the framework level — validate it against your current tool inventory before the v2 migration lands in June 2026, since the capability registration API is changing (from `instrument=` to `capabilities=`).

- **If you are building on enterprise platforms (Salesforce, ServiceNow, SAP), implement the export-boundary governance pattern.** Don't try to solve AI coding governance with post-hoc code review — it doesn't scale. ServiceNow's Build Agent demonstrates the production-viable alternative: constrain the agent's output space via the platform schema at generation time, then validate at export. If your platform has a formal schema (it probably does), this pattern is directly applicable.

- **Use A2A v1.0 for any cross-vendor agent-to-agent communication.** With Linux Foundation governance and native support in Azure AI Foundry, Amazon Bedrock, and Google Vertex AI, A2A is now the lowest-risk standard for inter-agent protocols. Implement Signed Agent Cards from day one — cryptographic agent identity is cheaper to add at the beginning than retroactively. Avoid building proprietary task-delegation protocols.

- **Deploy Bounded Context Agents instead of monolithic general agents for structured enterprise workflows.** The Cognizant and ServiceNow case studies confirm that 80 specialized agents with narrow context outperforms one general agent with broad context in high-volume, auditable enterprise environments. The tradeoff is orchestration complexity, but both cases show that a simple routing layer (task decomposition + domain classification) is sufficient. Start with 5-10 bounded agents and grow the registry incrementally.

- **Prioritize the AWS MCP Server for AWS-heavy stacks — the IAM integration is a governance upgrade, not just a convenience.** Most MCP deployments today have their own credential management plane that sits outside the enterprise identity model. AWS MCP Server's IAM-native approach means existing SCPs, permission boundaries, and CloudTrail audit coverage apply automatically to agent-to-service calls. This halves the compliance work for teams operating in regulated industries (finance, healthcare, government) on AWS.

---

## Key Takeaways (TL;DR)

- **Pydantic AI v1.95.0** ships Native Tool Search and the Instrumentation capability — migrate before v2 in June since `instrument=` is deprecated and tool registration APIs are changing.
- **ServiceNow Build Agent GA** establishes "export-boundary governance" as the production standard for enterprise AI coding agents — governance at the artifact export step, not the IDE or runtime.
- **Cognizant OneCognizant** validates multi-agent architectures at 350,000-employee scale: 50% efficiency gains, 50% ticket reduction, 80 specialized bounded-context agents over one general agent.
- **AWS MCP Server GA** brings IAM-native, CloudTrail-audited, least-privilege access to AI agent-tool connections — the first fully managed MCP with enterprise-grade identity integration.
- **A2A v1.0** under Linux Foundation governance with hyperscaler native support is now the de-facto standard for cross-vendor agent-to-agent communication — adopt Signed Agent Cards from day one.
- **Benchmark reality check**: UC Berkeley showed all 8 major agent benchmarks can be reward-hacked to ~100% — distrust leaderboard positions and weight production deployment metrics (Cognizant, Tata Steel) alongside benchmark scores.

---

*Sources:*
- https://github.com/pydantic/pydantic-ai/releases/tag/v1.95.0
- https://github.com/pydantic/pydantic-ai/releases/tag/v1.94.0
- https://ai.pydantic.dev/changelog.html
- https://www.businesswire.com/news/home/20260506008934/en/ServiceNow-Build-Agent-now-works-inside-every-major-AI-coding-tool-governed-by-default
- https://www.servicenow.com/community/product-launch-blogs/build-anywhere-run-on-servicenow-deploying-from-external-ides/ba-p/3522466
- https://www.servicenow.com/community/now-assist-for-creator-articles/what-s-new-in-may-for-build-agent/ta-p/3535155
- https://www.cognizant.com/us/en/insights/insights-blog/enterprise-multi-agent-ai-systems-transform-digital-workplace
- https://enterpriseaiexecutive.ai/p/cognizant-s-350-000-employee-multi-agent-ai
- https://www.microsoft.com/en-in/aifirstmovers/FY26Cognizant
- https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/
- https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html
- https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security_iam_service-with-iam.html
- https://github.com/google/A2A/blob/7b900e77/CHANGELOG.md
- https://agentmarketcap.ai/blog/2026/04/12/google-a2a-protocol-state-2026-adoption-enterprise
- https://stellagent.ai/insights/a2a-protocol-google-agent-to-agent
- https://github.com/openai/openai-agents-python/releases/tag/v0.16.0
- https://github.com/openai/openai-agents-python/releases/tag/v0.16.1
- https://benchlm.ai/benchmarks/swePro
- https://www.vals.ai/benchmarks/swebench-06-13-2025
- https://scale.com/leaderboard/swe%5Fbench%5Fpro%5Fpublic
- https://www.tbench.ai/leaderboard/terminal-bench/2.0
- https://llm-registry.com/benchmark/terminal-bench
- https://rapidclaw.dev/blog/ai-agent-benchmarks-2026
- https://pecollective.com/blog/ai-agent-frameworks-compared/
- https://agentmarketcap.ai/blog/2026/04/11/langgraph-autogen-crewai-dspy-multi-agent-orchestration-2026
- https://www.certiv.ai/product/
- https://www.okta.com/products/govern-ai-agent-identity/
- https://oasis.security/blog/introducing-oasis-agentic-access-management
- https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-agent-id
- https://www.salesforce.com/news/stories/agentforce-operations-announcement/
- https://www.crnasia.com/india/news/2026/tata-steel-deploys-over-300-ai-agents-in-nine-months-with-google-cloud
- https://usewire.io/blog/mcp-2026-roadmap-context-delivery-infrastructure/
- https://contextstudios.ai/blog/mcp-v2-beta-what-changes-in-multi-agent-communication
