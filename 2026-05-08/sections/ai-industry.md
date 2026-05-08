# AI Industry & General News — 2026-05-08

---

## Top Stories (3–5)

### 1. OpenAI Launches GPT-5.5-Cyber via "Trusted Access for Cyber" Program — Specialized cybersecurity model gates advanced capability behind verified identity
**Source:** [OpenAI Blog](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/) · [Help Net Security](https://www.helpnetsecurity.com/2026/05/08/openai-gpt-5-5-cyber-model/) · [WION News](https://www.wionews.com/technology/openai-launches-gpt-5-5-cyber-key-things-to-know-about-the-new-model-1778240980582)

OpenAI released GPT-5.5-Cyber on May 8, 2026, a specialized variant of GPT-5.5 engineered to be maximally permissive for authorized cybersecurity tasks while maintaining tight safeguards against misuse. The model is not necessarily more powerful than standard GPT-5.5 in general intelligence, but it is "trained to be more permissive on security-related tasks" — enabling vulnerability identification, binary reverse engineering, malware analysis, detection engineering, and patch validation that would be refused by the standard model.

Access is gated through OpenAI's Trusted Access for Cyber (TAC) program, an identity-and-trust-based framework limiting distribution to "critical cyber defenders" responsible for securing critical infrastructure. Major organizations already participating include Bank of America, JPMorgan Chase, Goldman Sachs, Cloudflare, CrowdStrike, and NVIDIA. Beginning June 1, 2026, all individual members accessing the most cyber-capable models must enable phishing-resistant Advanced Account Security.

The timing is notable: the release follows the White House studying an executive order for mandatory pre-deployment AI security reviews — itself triggered by Anthropic's warning that its Claude Mythos model was too dangerous to release publicly. OpenAI's tiered-access model offers a third path between "release everything openly" and "withhold from everyone": graduated trust verification. This architecture — standard model → TAC-enabled → cyber-specialist — could become an industry template for dual-use AI capabilities in security, bio, and other sensitive domains.

**Key details:**
- GPT-5.5-Cyber is in limited preview, rolling out to verified critical infrastructure defenders
- TAC program tiers: standard GPT-5.5 → GPT-5.5 with TAC → GPT-5.5-Cyber (most permissive)
- Advanced Account Security with phishing-resistant MFA mandated from June 1, 2026
- Participating institutions span financial services, cloud platforms, and cybersecurity vendors
- Authorized use cases explicitly include red teaming, penetration testing, and threat intelligence

---

### 2. Sierra Raises $950M at $15B Valuation — Enterprise AI agents scale to Fortune 50, generating $150M ARR in 14 months
**Source:** [TechCrunch](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/) · [SiliconANGLE](https://siliconangle.com/2026/05/04/ai-agent-startup-sierra-valued-15b-new-950m-funding-round/) · [The SaaS News](https://www.thesaasnews.com/news/sierra-raises-950m-at-15b-valuation)

Sierra Technologies, the AI agent platform founded by Bret Taylor (OpenAI board chair) and Clay Bavor (former Google executive), closed a $950 million funding round on May 4, 2026, led by Tiger Global and GV (Google Ventures), pushing its valuation past $15 billion. The company now has more than $1 billion in total capital raised and serves over 40% of the Fortune 50, powering billions of customer interactions across mortgage refinancing, insurance claims, returns management, and fundraising. Revenue exploded from $100M ARR (November 2025) to $150M ARR (February 2026) — a $50M gain in roughly 90 days.

Sierra's differentiation is its platform layer above raw LLMs: enterprises configure branded agents with controlled personas, guardrails, and escalation paths rather than building from scratch. In April 2026, the company launched "Ghostwriter," an agent-as-a-service tool that autonomously builds and deploys specialized AI agents from natural language descriptions — dramatically lowering the build cost for enterprise deployments.

The fundraise demonstrates that the "value layer above LLMs" thesis is proving out at scale. With Tiger Global and Google Ventures backing, Sierra has both growth capital and a strategic signal from two of the largest institutional AI investors. For comparison, eight months prior the company was at a $350M raise — the valuation growth (roughly 5× in less than a year) reflects market conviction that enterprise agent platforms, not model providers, may capture the largest share of AI revenue.

**Key details:**
- $950M raised; $15B+ post-money valuation; >$1B total capital raised to date
- Investors: Tiger Global (lead), GV/Google Ventures; prior backers include Sequoia, Benchmark
- Revenue trajectory: $100M ARR (Nov 2025) → $150M ARR (Feb 2026) → current
- Customer base: >40% of Fortune 50; billions of customer interactions processed
- April 2026 product launch: "Ghostwriter" agent-as-a-service for rapid agent deployment
- Previous round: $350M at undisclosed valuation, ~8 months prior

---

### 3. Anthropic Claude Managed Agents: "Dreaming," Outcomes, and Multiagent Orchestration — Three new features push agentic Claude toward autonomous long-horizon workflows
**Source:** [Claude Blog](https://claude.com/blog/new-in-claude-managed-agents) · [ZDNET](https://www.zdnet.com/article/your-claude-agents-can-dream-now-how-anthropics-new-feature-works/) · [Ars Technica](https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/)

On May 7, 2026, Anthropic shipped three new capabilities for Claude Managed Agents: *Dreaming* (a scheduled memory-review process that surfaces patterns across past sessions), *Outcomes* (defined success criteria that trigger automatic revision loops), and *Multiagent Orchestration* (a lead agent delegating to parallel specialist agents on a shared filesystem). Taken together, these features represent a systematic push toward agents that can execute complex, multi-day tasks with minimal human interruption.

Dreaming is a research preview that runs asynchronously between sessions, reviewing memory stores and extracting recurring mistakes, shared workflows, and team preferences. Users control whether discoveries are applied automatically or require manual review — a meaningful trust-calibration knob. Outcomes adds a separate grader in an isolated context window that evaluates output against a rubric, triggering revision loops until success criteria are met. Internal benchmarks showed +8.4pp on docx generation tasks and +10.1pp on pptx file generation. Netflix is already using multiagent orchestration for platform team workflows, suggesting production-readiness beyond internal tests.

These three features address different bottlenecks in agentic reliability: Dreaming tackles knowledge accumulation over time, Outcomes solves the evaluation-revision loop, and Orchestration handles task decomposition and parallelism. Together they represent Anthropic's architectural response to the key finding in AstaBench Spring 2026 — that only ~3% of hard end-to-end scientific tasks complete perfectly, with workflow coherence as the main constraint. Anthropic is explicitly engineering for the coherence gap.

**Key details:**
- Dreaming: research preview; reviews past sessions to extract patterns, auto-updates memory optionally
- Outcomes: grader in isolated context evaluates output; +8.4pp docx, +10.1pp pptx in internal testing
- Multiagent orchestration: lead agent spawns parallel specialists on shared filesystem with persistent threads
- Netflix cited as early production deployment of orchestration feature
- All features available on Claude Platform; Dreaming in research preview, others generally available

---

### 4. White House Studies Pre-Deployment AI Security Executive Order — Trump administration reverses course, weighing mandatory frontier-model safety reviews
**Source:** [Bloomberg Law](https://news.bloomberglaw.com/artificial-intelligence/white-house-prepares-order-to-boost-ai-security-hassett-says) · [Federal News Network](https://federalnewsnetwork.com/artificial-intelligence/2026/05/wh-studying-ai-security-executive-order/) · [Cybersecurity Dive](https://www.cybersecuritydive.com/news/nist-ai-model-testing-caisi-google-microsoft/819452/)

The White House is actively studying an executive order that would require pre-deployment security reviews of frontier AI models — a significant reversal for the Trump administration, which had previously repealed Biden-era AI safety guardrails in January 2025. National Economic Council Director Kevin Hassett compared the mechanism to FDA drug evaluation: models would need to "go through a process so that they're released to the wild after they've been proven safe." NIST's Center for AI Standards and Innovation (CAISI) would serve as the primary evaluating body, having already completed 40 evaluations and recently signing pre-deployment testing agreements with Google DeepMind, Microsoft, and xAI — joining earlier agreements with Anthropic and OpenAI.

The policy shift was catalyzed by Anthropic's disclosure that Claude Mythos could rapidly find and exploit serious software vulnerabilities, raising concerns that publicly releasing such a model would create unacceptable offensive risk. The administration is simultaneously circulating draft policy language that would limit AI contractors' ability to dictate how government agencies use purchased AI systems — a direct response to Anthropic's objections about using Claude in autonomous weaponry and surveillance contexts.

The practical implication is a possible end to the "release first, patch later" AI model deployment norm. If the executive order is signed, frontier labs would need CAISI clearance before public release — a new institutional bottleneck that could meaningfully slow deployment timelines, change competitive dynamics (well-resourced labs can navigate government review; smaller players may struggle), and create pressure for voluntary pre-release sharing with NIST even before the order takes effect.

**Key details:**
- NEC Director Kevin Hassett confirmed the White House is "studying" the executive order (May 2026)
- CAISI has signed pre-deployment eval agreements with: Anthropic, OpenAI, Google DeepMind, Microsoft, xAI
- Trigger: Anthropic warning about Claude Mythos cybersecurity capabilities and Mythos's limited release
- Separate policy track: limiting contractor authority over government AI usage decisions
- CAISI interagency task force can test models in classified settings
- Mandatory vs. voluntary: current evaluations are voluntary; EO would potentially require them

---

### 5. Gemini 3.1 Flash-Lite Generally Available — Google's fastest, cheapest Gemini 3 model goes GA with 2.5× TTFT improvement and $0.25/1M input pricing
**Source:** [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) · [Google DeepMind](https://deepmind.google/models/gemini/flash-lite) · [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)

Google announced that Gemini 3.1 Flash-Lite is generally available on the Gemini Enterprise Agent Platform via Google Cloud, positioning it as the fastest and most cost-efficient model in the Gemini 3 series. It delivers 2.5× faster Time to First Answer Token and 45% faster output speed versus Gemini 2.5 Flash at comparable or better quality. The model achieves 86.9% on GPQA Diamond and 76.8% on MMMU Pro, with improved instruction following, enhanced audio input capabilities, and expanded thinking support with adjustable reasoning levels. Pricing is $0.25/1M input tokens and $1.50/1M output tokens — aggressively competitive for high-throughput production workloads.

Real-world production results validate the model's economics: Gladly (customer service platform) reports approximately 60% lower costs vs. the prior solution. Early adopters include JetBrains (IDE development tools), Astrocade (game creation with multimodal safety checks), and unnamed partners running content moderation and translation at scale. The model supports multimodal inputs — text, code, images, audio, video — with a 1 million token context window.

The GA timing (one day before GPT-5.5-Cyber, the same week as Mistral Medium 3.5) reflects intensifying competition at the cost-efficient inference tier. Google is explicitly targeting the "high-volume, low-latency" workloads — translation, classification, customer support — where cost-per-call dominates model selection decisions. With 86.9% GPQA Diamond on a sub-$0.50/1M input model, the quality ceiling for budget-tier inference has risen significantly.

**Key details:**
- $0.25/1M input tokens, $1.50/1M output tokens (budget-tier pricing)
- 2.5× faster TTFT, 45% faster output vs. Gemini 2.5 Flash
- 86.9% GPQA Diamond; 76.8% MMMU Pro; 1M context window
- Supports text, code, images, audio, video inputs
- Gladly reports ~60% cost reduction in customer service deployment
- Available on Gemini Enterprise Agent Platform via Google Cloud

---

## Deep Dive: OpenAI's Trusted Access for Cyber — A New Architecture for Dual-Use AI Capabilities

**The strategic turning point in how AI labs handle dangerous capabilities**

### What Exactly Happened

On May 8, 2026, OpenAI launched GPT-5.5-Cyber in limited preview through its Trusted Access for Cyber (TAC) program. Unlike a standard model release, this is not a capability announcement — it is an access architecture announcement. The model itself is a fine-tuned variant of GPT-5.5 that removes certain refusals for security-related tasks while maintaining others, making it the most permissive AI system OpenAI has released. But the mechanism of release — a graduated, verified, identity-gated tiered access system — is the real story.

The Trusted Access for Cyber framework creates three tiers: standard GPT-5.5 with full commercial safeguards; GPT-5.5 with TAC enabled (more precise permissions for verified defensive work); and GPT-5.5-Cyber (maximum permissiveness for specialized cybersecurity workflows). Organizations must pass verification to access each tier, with the most capable tier reserved for "critical cyber defenders" responsible for critical infrastructure. Bank of America, JPMorgan Chase, Goldman Sachs, Cloudflare, CrowdStrike, NVIDIA, and others are already enrolled. From June 1, 2026, Advanced Account Security with phishing-resistant credentials is mandatory for the top tier.

### What Makes This Different From Prior Announcements

Previous AI cybersecurity efforts were largely bolt-on: add safety filters, then try to allow legitimate security researchers to bypass them through prompt engineering. TAC flips this: start with a more capable model and layer verified identity on top of access. The distinction matters because prompt-based safety is always vulnerable to jailbreaks, while identity-gated access is not — an attacker cannot prompt their way to GPT-5.5-Cyber if their account hasn't been verified as a legitimate defender. This is the first major AI lab to operationalize the "security clearance" model for AI access at scale.

### Strategic Motivations and Competitive Implications

OpenAI's timing is clearly calibrated to the regulatory moment. The White House is studying a mandatory pre-deployment review executive order, and the AI security debate has intensified after Anthropic's Claude Mythos disclosure. By releasing GPT-5.5-Cyber with TAC — proactively — OpenAI demonstrates a self-regulatory framework that could preempt heavier-handed government requirements. The implicit argument: "We have built the identity verification, tiered access, and audit infrastructure. You don't need to create an FDA for AI."

There is also a direct commercial opportunity. The security market represents hundreds of billions in annual spending, and AI-augmented security operations (vulnerability scanning, malware analysis, red teaming) is one of the highest-value applied AI use cases. By owning the verified-defender relationship with Bank of America, JPMorgan, Cloudflare, and CrowdStrike, OpenAI acquires both revenue and credibility as a mission-critical security infrastructure provider — not merely a chatbot vendor.

Competitive implications: Anthropic has Claude Mythos Preview (limited), which addresses similar use cases but explicitly chose not to release it broadly due to capability risk. Google has Project Naptime and related security research models. Microsoft's Security Copilot is already enterprise-deployed but built on earlier GPT models. OpenAI's move puts pressure on all three to define their own tiered-access architectures for high-stakes domains — or risk being positioned as either naive (releasing without controls) or overcautious (withholding from legitimate users).

### What to Watch in the Next 30–90 Days

The White House executive order on pre-deployment AI security reviews is the most consequential near-term policy development. If signed, it would institutionalize CAISI as a gatekeeper for frontier model releases — and OpenAI's proactive government partnerships (CAISI already has an agreement with OpenAI) position it well relative to labs that have been more adversarial with regulators. Watch for the EO's scope: will it apply only to general-release models, or also to specialized variants like GPT-5.5-Cyber? The latter would create a dual-track compliance regime that most labs lack infrastructure for today.

The enrollment trajectory of the TAC program matters: if the most critical infrastructure operators (utilities, telecoms, healthcare systems) sign on within 90 days, OpenAI has effectively created a government-adjacent trust network that will be difficult for competitors to replicate. Also watch for the first public disclosure of GPT-5.5-Cyber finding a real zero-day or substantially accelerating incident response — that case study will drive the next wave of enterprise security adoption.

### Impact on Developers and Companies Building on AI

For security product companies, the TAC framework is a forcing function: organizations that want to deploy the most capable AI for defensive security work now need to invest in identity verification infrastructure and meet OpenAI's enrollment requirements. Security AI startups building on the OpenAI API should evaluate whether their use case qualifies them for TAC access — it could unlock substantially more capable assistance for authorized workflows. The mandatory Advanced Account Security requirement from June 1 sets a new baseline for AI vendor identity requirements that other platforms will likely adopt. For non-security AI builders, the TAC architecture is a preview of what capability gating will look like across other sensitive domains: biology, critical infrastructure simulation, and advanced chemistry are likely candidates for similar frameworks over the next 12–24 months.

---

## Data for Visualization

```json
{
  "chart_type": "bar",
  "title": "Hyperscaler AI Capex 2026 vs 2025 (Projected, $B)",
  "subtitle": "Google, Microsoft, Meta, Amazon combined",
  "unit": "$B",
  "data": [
    {"label": "Amazon 2026", "value": 200},
    {"label": "Alphabet 2026", "value": 185},
    {"label": "Microsoft 2026", "value": 190},
    {"label": "Meta 2026", "value": 150},
    {"label": "Total 2026", "value": 725},
    {"label": "Total 2025", "value": 410}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Sierra Technologies ARR Growth ($M)",
  "subtitle": "From founding to May 2026",
  "unit": "$M ARR",
  "data": [
    {"label": "Nov 2025", "value": 100},
    {"label": "Feb 2026", "value": 150},
    {"label": "May 2026 (est.)", "value": 175}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Gemini 3.1 Flash-Lite Pricing vs Competitors (Input, $/1M tokens)",
  "subtitle": "Budget-tier model price comparison, May 2026",
  "unit": "$/1M input tokens",
  "data": [
    {"label": "Gemini 3.1 Flash-Lite", "value": 0.25},
    {"label": "Mistral Medium 3.5", "value": 1.50},
    {"label": "DeepSeek V4-Pro (post-cut)", "value": 0.50},
    {"label": "Kimi K2.6", "value": 0.60},
    {"label": "GPT-5.5 Instant", "value": 2.50}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Major AI Funding Rounds: May 2026 ($M)",
  "subtitle": "Announced or closed in May 2026",
  "unit": "$M",
  "data": [
    {"label": "Sierra (AI agents)", "value": 950},
    {"label": "SAP × Prior Labs (acquisition investment)", "value": 1160},
    {"label": "Zyg (enterprise AI)", "value": 60},
    {"label": "Nova Intelligence (SAP AI)", "value": 31.5}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Mistral Medium 3.5 vs Frontier Models: SWE-Bench Verified (%)",
  "subtitle": "Coding benchmark comparison, May 2026",
  "unit": "%",
  "data": [
    {"label": "Gemini 3.1 Pro Preview", "value": 78.8},
    {"label": "Mistral Medium 3.5", "value": 77.6},
    {"label": "Claude Sonnet 4", "value": 77.2},
    {"label": "DeepSeek V4-Pro", "value": 80.6},
    {"label": "GPT-5.5", "value": 75.0}
  ]
}
```

---

## Analysis & Impact for ML/Agentic Engineers

- **The tiered-access model for dual-use AI is now operational: plan for it.** OpenAI's GPT-5.5-Cyber via TAC is the first production instance of capability gating beyond standard enterprise accounts. If you build security tooling on OpenAI APIs, auditing your organization's eligibility for TAC enrollment should be on your Q3 roadmap — the most powerful assistance for authorized workflows is now behind an identity wall, not a prompt wall.

- **Anthropic's multiagent orchestration with shared filesystem is a production architecture shift.** The Claude Managed Agents update enables parallel specialist sub-agents on a shared filesystem with persistent thread memory. If you are building agentic workflows today and relying on single-context long-chain-of-thought for complex tasks, benchmark against orchestrated multi-specialist architectures — Netflix's adoption suggests real production gains are available now.

- **Budget-tier inference quality has crossed a new threshold: $0.25/1M input tokens for 86.9% GPQA Diamond.** Gemini 3.1 Flash-Lite's GA means that production workloads previously requiring mid-tier models ($1–3/1M input) can be reconsidered at 4–12× lower cost. If you are running high-volume classification, translation, content moderation, or customer support pipelines, re-benchmark on Flash-Lite before your next infrastructure planning cycle.

- **The White House pre-deployment AI security EO, if signed, will affect model release timelines for all frontier labs.** CAISI has agreements with all five major labs; mandatory reviews would add weeks-to-months of institutional latency before public releases. For teams building on cutting-edge model capabilities, this means the gap between private access (enterprise agreements, research partnerships) and public availability could widen substantially. Investment in early lab partnerships — not just API access — will matter more.

- **Enterprise agentic AI revenue is now definitively real, not theoretical.** Sierra's $150M ARR, Anthropic's outcomes improvements (+8–10pp on document tasks), and AWS's SageMaker model customization from months-to-days collectively mark the transition from "AI demo" to "AI revenue line item." If you are deploying agents in production, the competitive pressure from platform-layer players (Sierra, Managed Agents) will intensify — specialized agents built on top of LLM APIs need a clear differentiation story vs. orchestration platforms that abstract away the model layer.

---

## Key Takeaways (TL;DR)

- **OpenAI launched GPT-5.5-Cyber via Trusted Access for Cyber on May 8** — the first production identity-gated AI capability tier, with Bank of America, JPMorgan, CrowdStrike, and NVIDIA already enrolled.
- **Sierra raised $950M at $15B+ valuation** with $150M ARR and 40%+ of Fortune 50 as customers, proving enterprise agent platforms generate real at-scale revenue.
- **Anthropic shipped three new Managed Agents features** (Dreaming, Outcomes, Multiagent Orchestration) with Netflix already in production — directly targeting agentic workflow coherence as the next frontier.
- **The White House is studying a mandatory pre-deployment AI security EO**, a major regulatory reversal catalyzed by Claude Mythos disclosures; CAISI has signed evaluation agreements with all five major labs.
- **Gemini 3.1 Flash-Lite is GA at $0.25/1M input tokens** with 86.9% GPQA Diamond and 2.5× faster TTFT than Gemini 2.5 Flash — the new price-performance benchmark for high-volume production inference.
- **Big Tech 2026 AI capex is now projected at $725B combined** (Google, Microsoft, Meta, Amazon) — up 77% from 2025, with Amazon facing potential negative free cash flow as a result.
- **Mistral Medium 3.5 hit 77.6% SWE-Bench Verified** (highest open-weight score at launch) with 256K context and $1.50/1M input pricing — open-weight models continue closing the gap on closed-source frontier coding performance.

---

*Sources:*

[OpenAI – Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)
[OpenAI – Introducing Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/)
[OpenAI – Trusted Access for the Next Era of Cyber Defense](https://openai.com/index/scaling-trusted-access-for-cyber-defense/)
[Help Net Security – OpenAI tunes GPT-5.5-Cyber for more permissive security workflows](https://www.helpnetsecurity.com/2026/05/08/openai-gpt-5-5-cyber-model/)
[WION News – OpenAI launches GPT-5.5-Cyber: Key things to know](https://www.wionews.com/technology/openai-launches-gpt-5-5-cyber-key-things-to-know-about-the-new-model-1778240980582)
[Technobezz – OpenAI Rolls Out GPT-5.5-Cyber Exclusively to Critical Cyber Defenders](https://www.technobezz.com/news/openai-rolls-out-gpt-55-cyber-exclusively-to-critical-cyber-defenders)
[TechCrunch – Sierra raises $950M as the race to own enterprise AI gets serious](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/)
[SiliconANGLE – AI agent startup Sierra valued at $15B in new $950M funding round](https://siliconangle.com/2026/05/04/ai-agent-startup-sierra-valued-15b-new-950m-funding-round/)
[The AI Insider – Sierra Secures $950M at $15B Valuation](https://theaiinsider.tech/2026/05/05/sierra-secures-950m-at-15b-valuation-to-become-global-standard-for-ai-customer-agents/)
[Seeking Alpha – OpenAI chair's AI startup Sierra raises $950M at over $15B valuation](https://seekingalpha.com/news/4584893-openai-chairs-ai-startup-sierra-raises-950m-at-over-15b-valuation)
[Claude Blog – New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](https://claude.com/blog/new-in-claude-managed-agents)
[ZDNET – Your Claude agents can 'dream' now](https://www.zdnet.com/article/your-claude-agents-can-dream-now-how-anthropics-new-feature-works/)
[Ars Technica – Anthropic's Claude Managed Agents can now "dream," sort of](https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/)
[9to5Mac – Anthropic updates Claude Managed Agents with three new features](https://9to5mac.com/2026/05/07/anthropic-updates-claude-managed-agents-with-three-new-features/)
[Bloomberg Law – White House Prepares Order to Boost AI Security, Hassett Says](https://news.bloomberglaw.com/artificial-intelligence/white-house-prepares-order-to-boost-ai-security-hassett-says)
[Federal News Network – WH 'studying' AI security executive order](https://federalnewsnetwork.com/artificial-intelligence/2026/05/wh-studying-ai-security-executive-order/)
[Cybersecurity Dive – NIST will test three major tech firms' frontier AI models for cybersecurity risks](https://www.cybersecuritydive.com/news/nist-ai-model-testing-caisi-google-microsoft/819452/)
[CSO Online – US government agency to safety test frontier AI models before release](https://www.csoonline.com/article/4168135/us-government-agency-to-safety-test-frontier-ai-models-before-release-2.html)
[Google Cloud Blog – Gemini 3.1 Flash-Lite is now generally available](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available)
[Google DeepMind – Gemini 3.1 Flash-Lite Model Card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite)
[Google Blog – Gemini 3.1 Flash Lite: Our most cost-effective AI model yet](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)
[Tom's Hardware – Google, Microsoft, Meta, and Amazon capex spending to hit $725 billion in 2026](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)
[Fortune – Microsoft, Meta, and Google just announced billions more in AI spending](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/)
[AI News – Big Tech's AI infrastructure spending paid off—and accelerated](https://www.artificialintelligence-news.com/news/big-tech-ai-infrastructure-spending-q1-2026-results/)
[AWS – Announcing Agent Toolkit for AWS](https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/)
[AWS – The AWS MCP Server is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/)
[About Amazon – AWS and OpenAI announce expanded partnership](https://www.aboutamazon.com/news/aws/bedrock-openai-models)
[Microsoft Blog – The next phase of the Microsoft-OpenAI partnership](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
[The Verge – Microsoft and OpenAI's famed AGI agreement is dead](https://www.theverge.com/ai-artificial-intelligence/918981/openai-microsoft-renegotiate-contract)
[The Decoder – Mistral's new flagship Medium 3.5 folds chat, reasoning, and code into one model](https://the-decoder.com/mistrals-new-flagship-medium-3-5-folds-chat-reasoning-and-code-into-one-model/)
[MarkTechPost – Mistral AI Launches Remote Agents in Vibe and Mistral Medium 3.5](https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/)
[TechCrunch – SAP bets $1.16B on 18-month-old German AI lab](https://techcrunch.com/2026/05/05/sap-bets-1-16b-on-18-month-old-german-ai-lab-and-says-yes-to-nemoclaw/)
[Bloomberg – IronSource Founders' AI Startup Zyg Raises at $500 Million Value](https://www.bloomberg.com/news/articles/2026-05-05/ironsource-founders-ai-startup-zyg-raises-at-500-million-value)
[Fortune – Nova Intelligence raises $31.5 million to bring AI to SAP's $89 billion migration wave](https://fortune.com/2026/05/05/exclusive-nova-intelligence-ai-sap-chemistry-emma-qian/)
