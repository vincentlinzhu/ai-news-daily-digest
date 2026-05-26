# AI Industry & General News — 2026-05-26

---

## Top Stories (3–5)

### 1. OpenRouter Raises $113M Series B at $1.3B Valuation as Multi-Model Era Arrives — AI gateway hits 100 trillion tokens/month as enterprises abandon single-vendor lock-in

**Source:** [SiliconANGLE](https://siliconangle.com/2026/05/26/openrouter-raises-113m-bring-order-enterprise-ai-inference-routing/) · [TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/) · [Tech Startups](https://techstartups.com/2026/05/26/openrouter-raises-113m-as-ai-token-usage-surges-to-100-trillion-monthly/)

OpenRouter — the NYC-based AI model exchange that lets developers and enterprises route requests across more than 400 AI models through a single API — announced a $113 million Series B today led by CapitalG, Alphabet's independent growth fund. The round values the company at approximately $1.3 billion post-money, more than doubling its $547 million valuation from its Series A just one year ago. Investors include Nvidia's NVentures, ServiceNow Ventures, MongoDB Ventures, Snowflake Ventures, Databricks Ventures, Andreessen Horowitz, and Menlo Ventures — a consortium that reads like a who's-who of the enterprise AI stack.

The velocity behind the raise is striking: OpenRouter now processes 100 trillion tokens per month, or roughly 25 trillion per week — a 5× increase from six months ago. The platform claims 8 million global users. CEO Alex Atallah described the thesis plainly: "The era of picking a single model is over. Success now depends on continuously routing across a changing market." The platform enables per-request cost optimization, latency management, spend visibility, audit-friendly usage reporting, and team-level access controls — precisely what enterprises need as they deploy agents at scale.

The timing and the investor syndicate signal something larger: the AI infrastructure layer is bifurcating between model makers and model routers. The participation of Alphabet/CapitalG (which is financially invested in OpenRouter while Google competes in model-making) alongside Nvidia, Databricks, and ServiceNow suggests these players see the multi-model abstraction layer as neutral, necessary infrastructure — akin to cloud-agnostic orchestration tools. OpenRouter will use the capital to expand routing, governance, and optimization capabilities.

**Key details:**
- $113M Series B led by CapitalG; post-money valuation ~$1.3B (up from $547M one year prior)
- 100 trillion tokens/month processed; 8 million global users; 400+ models available
- 5× token growth in six months signals massive enterprise agent deployment wave
- Investors span Alphabet, Nvidia, Databricks, ServiceNow, Snowflake, MongoDB — entire enterprise stack
- Prior Series A raised $40M in June 2025

---

### 2. Anthropic Signs $45B Compute Deal with SpaceX, Disclosed in SpaceX's Historic IPO Filing — $1.25B/month commitment through 2029 makes Anthropic the anchor tenant of Colossus I and II

**Source:** [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-20/anthropic-to-pay-spacex-nearly-45-billion-for-computing-deal) · [The Verge](https://www.theverge.com/science/935229/spacex-anthropic-ipo-ai-capacity-deal-colossus) · [HotHardware](https://hothardware.com/news/anthropic-inks-spacex-deal-ahead-of-2-trillion-ipo)

Anthropic will pay SpaceX $1.25 billion per month — approximately $15 billion annually and $45 billion over three years — for access to the Colossus I and Colossus II supercomputer clusters in Memphis, Tennessee. The financial terms were disclosed in SpaceX's S-1 registration statement filed with the SEC on May 20, 2026, as SpaceX prepares what may be the largest IPO in capital markets history (targeting a $1.75T valuation and a $75B raise on Nasdaq under ticker SPCX, with a roadshow beginning June 4 and pricing set for June 11). Capacity is ramping in May and June 2026 at a reduced fee, reaching the full monthly rate thereafter. Either party may terminate with 90 days' notice.

The deal gives Anthropic access to over 220,000 Nvidia GPUs and more than 300 megawatts of compute capacity — the original infrastructure built for xAI's Grok chatbot. Anthropic head of product Ami Vora said the deal allows the company to lift rate caps that had frustrated paid subscribers, including those on Pro, Max, Team, and Enterprise plans. As part of the agreement, Anthropic and SpaceX are also exploring orbital AI compute: data centers in space, potentially delivering gigawatts of capacity beyond terrestrial constraints.

For SpaceX, the Anthropic contract transforms the economics of its IPO. SpaceX's AI division ran a $2.5 billion deficit in Q1 2026, contributing to a consolidated net loss of $4.3 billion on $4.7 billion in Q1 revenue. The $15B/year Anthropic commitment converts Colossus from a cost center into a revenue line that could nearly double SpaceX's total 2025 revenues of $18.67 billion. Musk has stated publicly that SpaceX is "offering AI compute as a service at significant scale" to any AI company that wants it. OpenAI and other labs have reportedly expressed interest.

**Key details:**
- $1.25B/month ($15B/year, $45B over 3 years through May 2029) with 90-day termination clause
- 220,000+ Nvidia GPUs; 300+ megawatts at Colossus I and Colossus II, Memphis, TN
- SpaceX S-1 filed May 20; SPCX ticker; ~$1.75T target valuation; ~$75B raise — largest IPO in history if priced
- SpaceX AI division lost $2.5B in Q1 2026; Anthropic contract is key to IPO investment thesis
- Future exploration of orbital AI compute infrastructure

---

### 3. Anthropic Acquires Stainless for ~$300M, Cutting Off OpenAI and Google's SDK Toolchain — Developer infrastructure move reshapes the MCP and agent connectivity layer

**Source:** [Anthropic](https://www.anthropic.com/news/anthropic-acquires-stainless) · [TechCrunch](https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/) · [The New Stack](https://thenewstack.io/anthropic-stainless-sdk-acquisition/)

Anthropic acquired Stainless on May 18, 2026, a New York-based startup founded in 2022 by former Stripe engineer Alex Rattray. Stainless's platform converts OpenAPI specifications into production-grade SDKs (TypeScript, Python, Go, Java, Kotlin), CLIs, documentation, and MCP servers — the exact tooling that turns an API into something AI agents can actually use. The Information reported terms above $300 million; Anthropic did not confirm the price. Stainless was backed by Sequoia Capital and Andreessen Horowitz.

The strategic logic is straightforward but the competitive implications are sharp: Stainless has been the shared SDK factory for Anthropic, OpenAI, Google, Cloudflare, Replicate, and Runway. Anthropic is winding down all hosted Stainless products immediately. OpenAI and Google — which relied on Stainless to generate and maintain their own SDKs — must now build or source equivalent infrastructure independently. Existing Stainless customers retain rights to SDKs they've already generated but lose access to the ongoing update pipeline.

This acquisition is a direct extension of Anthropic's MCP strategy. Anthropic created the Model Context Protocol to standardize how agents connect to external tools. Stainless is the layer that generates those connectors from an API spec. By internalizing Stainless, Anthropic controls the full stack from protocol design (MCP) to SDK and MCP server generation — a structural advantage in the race to make Claude agents the best-connected in the ecosystem. The analogy to Bun (acquired by Anthropic) and Astral (acquired by OpenAI) is apt: AI labs are now hoarding developer infrastructure as a moat.

**Key details:**
- Acquisition price reported above $300M; all hosted Stainless products wound down immediately
- Stainless previously powered SDKs for OpenAI, Google, Cloudflare, Replicate, Runway — all lose shared supplier
- Stainless generated every official Anthropic SDK since the early Claude API days
- Anthropic now controls MCP (protocol) + Stainless (SDK/MCP server generation) — full agent connectivity stack
- Stainless team integrates fully into Anthropic's Claude Platform team

---

### 4. Anthropic's Project Glasswing Discloses 10,000+ Vulnerabilities in First Progress Update — AI-powered security coalition patches zero-days across critical infrastructure in weeks

**Source:** [Anthropic](https://www.anthropic.com/research/glasswing-initial-update) · [Crypto Briefing](https://cryptobriefing.com/anthropic-project-glasswing-software-vulnerabilities/) · [Anthropic Glasswing Page](https://www.anthropic.com/project/glasswing)

On May 22, Anthropic published its first progress update on Project Glasswing — the cybersecurity coalition launched in April 2026 that gives vetted partners access to Claude Mythos Preview (Anthropic's unreleased frontier model with 93.9% SWE-bench Verified) to find and fix software vulnerabilities at AI-accelerated speed. The numbers are staggering: partners have collectively identified over 10,000 high- and critical-severity vulnerabilities, including thousands of zero-days that had been lurking undetected in widely-used systems for years. Claude Opus 4.7 alone has patched over 2,100 vulnerabilities since launch.

The coalition includes AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, Nvidia, and Palo Alto Networks, with over 40 additional participating organizations. Anthropic has committed $100 million in Claude usage credits and $4 million in open-source security enhancements to fund the effort. As of this update, Anthropic is now making Glasswing tools available to qualifying enterprise security teams: custom scanning skills, a codebase-mapping harness with subagent scanning, and a threat model builder that prioritizes attack surface by risk.

The update makes clear why Mythos Preview remains restricted: "No company — including Anthropic — has developed safeguards strong enough to prevent such models from being misused and potentially causing severe harm." But the 10,000+ vulnerability disclosure demonstrates that the same capabilities that make a model dangerous for offense can be pointed defensively at critical infrastructure. This is the most significant public demonstration to date of the dual-use nature of frontier AI in cybersecurity.

**Key details:**
- 10,000+ high/critical severity vulnerabilities identified; thousands classified as zero-days
- Claude Opus 4.7 patched 2,100+ vulnerabilities since project launch in April 2026
- Coalition: AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, Nvidia, PaloAlto + 40 more
- Anthropic committed $100M usage credits + $4M for open-source security
- Claude Mythos Preview priced at $25/$125 per M input/output tokens (restricted access only)
- Tools now released to qualifying enterprise security teams (scanning harness, threat model builder)

---

### 5. Anthropic Deepens Enterprise Push: KPMG Global Alliance, PwC Deployment, and $200M Gates Foundation Partnership — Claude embedded in Big Four client delivery workflows for the first time

**Source:** [Anthropic/KPMG](https://www.anthropic.com/news/anthropic-kpmg) · [KPMG Press Release](https://kpmg.com/us/en/media/news/kpmg-anthropic-global-alliance.html) · [Anthropic/Gates](https://www.anthropic.com/news/gates-foundation-partnership)

Three major Anthropic enterprise announcements landed in the second half of May. First, on May 19, KPMG announced a global alliance embedding Claude inside Digital Gateway — KPMG's flagship client delivery platform — starting with tax and legal workflows. All 276,000 KPMG employees globally gain access to Claude, making KPMG the first Big Four firm to embed frontier AI directly into its core client platform. Anthropic named KPMG its preferred consultant for private equity, and the two firms will co-develop PE-focused products including KPMG Blaze (Claude Code for IT modernization). Second, PwC expanded its Claude alliance to include training 30,000 professionals, a joint Center of Excellence, and a Claude-native "Office of the CFO" finance function. Third, on May 14, Anthropic formalized a $200 million, four-year partnership with the Gates Foundation covering global health, life sciences, education, and economic mobility — the largest AI-philanthropic commitment in either organization's history.

Together, these announcements reflect an acceleration in Anthropic's enterprise go-to-market strategy. The Big Four professional services firms collectively have direct relationships with the C-suite at most of the Fortune 500 — embedding Claude in KPMG and PwC's delivery workflows is a distribution play that could reach enterprise AI deployments faster than any direct sales motion. The Gates Foundation partnership simultaneously positions Anthropic as the AI lab most committed to non-commercial beneficial deployment, differentiating on trust at a moment when the US regulatory environment offers no oversight mechanism.

**Key details:**
- KPMG: 276,000 employees, Claude inside Digital Gateway, KPMG preferred PE consultant, KPMG Blaze product
- PwC: 30,000 professionals trained/certified, Joint CoE, Office of the CFO (finance AI group)
- Gates Foundation: $200M over 4 years in grant funding, Claude credits, and technical support
- Focus areas: global health, life sciences, education, economic mobility
- Anthropic also launched Claude for Small Business (May 13) and AI agents for financial services (May 5)

---

## Deep Dive: The Anthropic–SpaceX $45B Compute Deal and the Coming Infrastructure Consolidation

**What exactly happened**

On May 6, 2026, Anthropic announced a compute partnership with SpaceX, giving it access to Colossus I in Memphis. On May 20, when SpaceX filed its preliminary S-1 with the SEC to pursue what would be the largest IPO in capital markets history, the actual financial terms became public: $1.25 billion per month, ramping over May–June 2026, running through May 2029 — a potential $45 billion commitment over three years. Anthropic subsequently disclosed it was expanding from Colossus I to Colossus II, scaling up Nvidia GB200 capacity. The result: Anthropic has access to 220,000+ Nvidia GPUs, over 300 megawatts of compute, and the infrastructure originally built to power xAI's Grok models.

**What makes this different from prior compute deals**

Most AI lab compute procurement involves long-term cloud commitments with AWS, Azure, or GCP — infrastructure that the hyperscaler operates and that hundreds of other customers share. The Anthropic–SpaceX deal is different in three ways. First, it is purpose-built, dedicated infrastructure: Colossus was built as a supercomputer cluster for frontier AI training, not a shared cloud. Second, the scale is unprecedented — $15 billion annually at a time when OpenAI's entire revenue base is estimated around $10–12 billion annually. Third, the disclosure mechanism was involuntary: the public learned the terms not from a press release but from an IPO filing, which means the S-1 is now a primary source on AI industry economics. Future IPO filings from Anthropic (which has been discussed at a ~$2 trillion potential valuation) will generate similar disclosures.

**Strategic motivations and competitive implications**

For Anthropic, the deal solves an immediate problem: Claude demand is outrunning compute. Rate limits had frustrated enterprise customers on paid plans. The SpaceX compute unlocks capacity to serve this demand while the company explores longer-term orbital infrastructure. For SpaceX, the deal is the difference between an IPO with a compelling AI revenue story and one without. SpaceX's AI division lost $2.5 billion in Q1 2026 alone; the Anthropic contract converts that liability into a $15B/year revenue line. Elon Musk has signaled that SpaceX is now offering "AI compute as a service at significant scale" to all takers — a direct challenge to hyperscalers on price and GPU density.

The competitive implication for OpenAI is notable. OpenAI and Anthropic are both racing to close the gap between demand and supply. OpenAI has its own Azure compute arrangements, but if SpaceX's SPCX stock begins trading and Musk positions Colossus as neutral AI infrastructure, OpenAI (and others) may find themselves in a compute arms race with a new entrant — SpaceX — that has structural cost advantages from building and operating its own data centers and power infrastructure.

**What to watch in the next 30–90 days**

The SpaceX IPO roadshow begins June 4 with pricing on June 11. Market reception will determine whether other AI companies view SpaceX as a viable compute source or a risky single-vendor dependency. Watch for: (1) whether any other AI lab signs a Colossus compute agreement, (2) Anthropic's rate limit changes as GB200 capacity ramps through June, (3) any SEC comment letters on the S-1 that probe the Anthropic contract's termination clause, and (4) the first Anthropic financial disclosures if the company pursues its own IPO — which will likely reveal revenue figures that dwarf what most analysts currently model.

**Impact on developers and companies building on AI**

Rate caps lifting for Claude Pro, Max, Team, and Enterprise is the near-term developer impact. Medium-term, the ability to sustain $15B/year in compute spend suggests Anthropic can compete on model quality at scale — which means the Claude 4.x and forthcoming 5.x generation will have the training runs to stay competitive with GPT-5.x and Gemini 3.x. For companies with multi-year Claude API commitments, this deal substantially reduces the risk of capacity constraints. For companies evaluating whether to build on Claude, Gemini, or GPT, the SpaceX deal is a signal that Anthropic's compute floor just went from uncertain to one of the best-capitalized in the industry.

---

## Data for Visualization

```json
{
  "chart_type": "bar",
  "title": "AI Startup Funding Rounds — May 2026 (Selected)",
  "subtitle": "Announced or closed in the week of May 19–26, 2026",
  "unit": "$M",
  "data": [
    {"label": "OpenRouter (Series B)", "value": 113},
    {"label": "Commure Healthcare AI (Series)", "value": 70},
    {"label": "Dust Enterprise Agents (Series B)", "value": 40},
    {"label": "Perceptic Drug Discovery (Seed)", "value": 12}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Anthropic May 2026 Commitments & Deals ($ billions)",
  "subtitle": "Announced spending obligations and partnership values",
  "unit": "$B",
  "data": [
    {"label": "SpaceX compute deal (3-year total)", "value": 45},
    {"label": "SpaceX compute deal (annual run rate)", "value": 15},
    {"label": "Gates Foundation partnership", "value": 0.2},
    {"label": "Project Glasswing credits committed", "value": 0.1}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "OpenRouter Token Volume Growth (Weekly)",
  "subtitle": "Trillion tokens per week, 6-month comparison",
  "unit": "T tokens/week",
  "data": [
    {"label": "Nov 2025 (6 months ago)", "value": 5},
    {"label": "May 2026 (current)", "value": 25}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Anthropic Enterprise Reach — May 2026 Partnerships",
  "subtitle": "Professionals with access to Claude via new alliances",
  "unit": "thousands of employees",
  "data": [
    {"label": "KPMG global workforce", "value": 276},
    {"label": "PwC trained professionals", "value": 30}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Notable AI Compute Infrastructure Events — May 2026",
  "subtitle": "Announced data center / GPU commitments ($B annual)",
  "unit": "$B/year",
  "data": [
    {"label": "Anthropic → SpaceX Colossus", "value": 15},
    {"label": "Big 4 hyperscaler capex (2026 est., per co.)", "value": 181},
    {"label": "Nvidia Q1 FY27 Data Center Revenue (annualized)", "value": 268}
  ]
}
```

---

## Analysis & Impact for ML/Agentic Engineers

- **The multi-model router is now a funded infrastructure category.** OpenRouter's $1.3B valuation and 5× token growth signal that enterprises deploying agents at scale are not committing to a single provider. If you are building agentic systems for enterprise customers, consider whether your architecture exposes model selection as a runtime decision rather than a compile-time constant — your customers will increasingly demand it, and abstraction layers like OpenRouter (or LiteLLM, which remains open-source) are maturing rapidly.

- **Anthropic's Stainless acquisition changes MCP server development economics.** The shutdown of hosted Stainless products removes the easiest path for OpenAI- and Google-ecosystem developers to generate MCP servers. For teams building MCP connectors today, watch Anthropic's release of internal Stainless tooling — they have committed to making SDK and MCP generation available through the Claude platform. If you are building connectors to third-party APIs and want Claude agents to use them, staying close to Anthropic's developer tooling roadmap is now more important than before.

- **Project Glasswing is the first enterprise-scale demonstration of AI agents autonomously doing security work.** Over 10,000 critical vulnerabilities patched in weeks. If you maintain production software — open-source or proprietary — and have not yet investigated Claude Security (now in public beta for Enterprise customers), this is worth trialing. The tooling (harness + threat model builder + skills) is now being released to qualifying security teams. For teams building AI-augmented security pipelines, Glasswing's public writeup of how Mythos discovers and patches vulnerabilities is the best available documentation of what production-grade AI security agents actually do.

- **The EU AI Act's August 2026 watermarking deadline is still live; the December 2027 deadline is not.** The Digital Omnibus political agreement pushed back Annex III (standalone high-risk AI) and Annex I (AI in regulated products) enforcement, but the Article 50(2) watermarking obligation for AI content providers moved only to December 2, 2026 — not delayed significantly. If your product generates AI content for EU users, watermarking is the nearest live deadline and it is 6 months away. China's intelligent agent framework (May 8 implementation opinions) formally defined "agent" across 19 sectors — if you serve Chinese enterprise customers, agent classification now has regulatory teeth.

- **Compute access is becoming a strategic differentiator at the model provider layer.** Anthropic's $45B SpaceX deal and the subsequent rate limit removals mean Claude's capacity constraints — which frustrated enterprise customers throughout Q1 2026 — are being systematically resolved. For teams that previously rate-limited their Claude API usage or built fallback routing to other providers due to availability, revisit those architectural decisions. The compute ramp through June 2026 is real. Simultaneously, the Anthropic–SpaceX partnership signals that the next frontier training runs will be funded and may produce Claude 5.x-class models faster than analyst estimates have assumed.

---

## Key Takeaways (TL;DR)

- **OpenRouter raises $113M at $1.3B valuation today** as AI token volume hits 100 trillion/month — the multi-model gateway is now a funded enterprise infrastructure category, not a niche tool.
- **Anthropic commits $45B to SpaceX compute** ($1.25B/month through May 2029), revealed in SpaceX's S-1 filing for what will be the largest IPO in history (~$1.75T valuation, June 12 debut).
- **Anthropic acquires Stainless for ~$300M**, shutting down the shared SDK/MCP server generator used by OpenAI, Google, and Cloudflare — and taking full control of the agent connectivity stack.
- **Project Glasswing discloses 10,000+ critical vulnerabilities** patched by AI in weeks; Claude Security tools are now publicly available to Enterprise customers.
- **Anthropic signs KPMG global alliance** (276,000 employees, first Big Four firm to embed frontier AI in client delivery platform) plus PwC and a $200M Gates Foundation partnership in a single week.
- **EU AI Act watermarking deadline is December 2, 2026** — still live despite the Omnibus push-backs on high-risk AI; China's agent framework now formally defines and regulates AI agents across 19 sectors.
- **GPT-5.6 is unconfirmed but signaled**: Polymarket at 80–89% odds for June 30 release; internal Codex log traces and codenames (ember-alpha, beacon-alpha) appeared in developer environments; expect simultaneous June launches from OpenAI, Anthropic (Claude Sonnet 4.8 rumored), and Google (Gemini 3.5 Pro confirmed for next month).

---

*Sources:*

[OpenRouter Series B — SiliconANGLE](https://siliconangle.com/2026/05/26/openrouter-raises-113m-bring-order-enterprise-ai-inference-routing/)
[OpenRouter valuation doubles to $1.3B — TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/)
[OpenRouter 100T tokens/month — Tech Startups](https://techstartups.com/2026/05/26/openrouter-raises-113m-as-ai-token-usage-surges-to-100-trillion-monthly/)
[Anthropic–SpaceX $45B compute deal — Bloomberg](https://www.bloomberg.com/news/articles/2026-05-20/anthropic-to-pay-spacex-nearly-45-billion-for-computing-deal)
[Anthropic $15B/year for SpaceX data centers — The Verge](https://www.theverge.com/science/935229/spacex-anthropic-ipo-ai-capacity-deal-colossus)
[Anthropic–SpaceX compute deal details — HotHardware](https://hothardware.com/news/anthropic-inks-spacex-deal-ahead-of-2-trillion-ipo)
[Anthropic–SpaceX initial deal — Axios](https://www.axios.com/2026/05/06/anthropic-spacex-elon-musk-compute)
[SpaceX $1.25B/month — Billionaires Africa](https://www.billionaires.africa/2026/05/26/elon-musks-spacex-has-a-secret-weapon-anthropic-is-paying-it-1-25-billion-a-month-to-keep-training-its-ai/)
[SpaceX IPO S-1 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm)
[SpaceX IPO $75B raise at $1.75T valuation — Tech Marketer](https://thetechmarketer.com/spacex-ipo-2026-spcx-nasdaq-valuation-starlink/)
[SpaceX IPO tracker — SpaceX IPO Stat](https://spacexipostat.us/)
[Anthropic acquires Stainless — Anthropic](https://www.anthropic.com/news/anthropic-acquires-stainless)
[Anthropic acquires Stainless — TechCrunch](https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/)
[Stainless acquisition impact on OpenAI/Google — The New Stack](https://thenewstack.io/anthropic-stainless-sdk-acquisition/)
[Stainless agent plumbing analysis — Developers Digest](https://www.developersdigest.tech/blog/anthropic-stainless-sdk-agent-plumbing)
[Project Glasswing initial update — Anthropic](https://www.anthropic.com/research/glasswing-initial-update)
[Project Glasswing main page — Anthropic](https://www.anthropic.com/project/glasswing)
[Project Glasswing 10,000+ vulnerabilities — Crypto Briefing](https://cryptobriefing.com/anthropic-project-glasswing-software-vulnerabilities/)
[KPMG–Anthropic global alliance — Anthropic](https://www.anthropic.com/news/anthropic-kpmg)
[KPMG Digital Gateway Powered by Claude — KPMG](https://kpmg.com/us/en/media/news/kpmg-anthropic-global-alliance.html)
[KPMG Claude rollout — Accounting Today](https://www.accountingtoday.com/news/kpmg-enters-alliance-with-anthropic)
[Anthropic–Gates Foundation $200M — Anthropic](https://www.anthropic.com/news/gates-foundation-partnership)
[Commure $70M at $7B valuation — AI Insider](https://theaiinsider.tech/2026/05/26/commure-secures-70m-at-7b-valuation-to-deploy-ai-agents-across-healthcare-administration/)
[Dust $40M Series B — AI Insider](https://theaiinsider.tech/2026/05/25/dust-raises-40m-to-make-ai-multiplayer-inside-the-enterprise/)
[Gemini 3.5 Flash — Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
[Gemini Omni Flash — Google Blog Africa](https://blog.google/intl/en-africa/products/explore-get-answers/gemini-omni/)
[Gemini Omni TechCrunch](https://techcrunch.com/2026/05/19/googles-gemini-omni-turns-images-audio-and-text-into-video-and-thats-just-the-start/)
[Gemini Omni Flash — The Verge](https://www.theverge.com/tech/933552/google-gemini-ai-omni-flash-media-video-io-2026)
[Gemini Omni Flash model card — DeepMind](https://deepmind.google/models/model-cards/gemini-omni-flash/)
[Google Agent Executor runtime — Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime)
[Google Agent Substrate / GKE — Google Cloud](https://cloud.google.com/blog/products/containers-kubernetes/bringing-you-agent-sandbox-on-gke-and-agent-substrate)
[Managed Agents Gemini API — Google](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/)
[GPT-5.6 leak analysis — WaveSpeed](https://wavespeed.ai/blog/posts/gpt-5-6-canary-leak-what-we-know/)
[GPT-5.6 leaks hint at June launch — WinCentral](https://thewincentral.com/gpt-5-6-leaks-suggest-openais-next-big-ai-upgrade-could-arrive-in-june/)
[GPT-5.5 official launch — OpenAI](https://openai.com/index/introducing-gpt-5-5/)
[EU AI Act 2026 compliance map — AISigil](https://aisigil.com/artificial-intelligence-laws-global-compliance-map-2026/)
[EU AI Act high-risk draft rules — AI CERTs](https://www.aicerts.ai/news/eu-ai-act-navigating-new-high-risk-draft-rules/)
[EU AI Act Omnibus reading — DEV Community](https://dev.to/studiomeyer_io/the-eu-ai-act-in-2026-reading-the-law-after-the-omnibus-11b9)
[China intelligent agent definition — Thorsten Jelinek Substack](https://thorstenjelinek.substack.com/p/china-just-defined-the-intelligent)
[China AI regulation vs. US — South China Morning Post](https://www.scmp.com/tech/policy/article/3354925/will-chinas-lead-ai-regulation-force-us-rethink-its-approach-under-trump)
[OpenRouter Series B funding round — Finsmes](https://www.finsmes.com/2026/05/openrouter-raises-113m-in-series-b-funding.html)
[Perceptic drug discovery $12M seed — Fortune](https://fortune.com/2026/05/26/exclusive-perceptic-a-startup-automating-drug-discovery-end-to-end-for-big-pharma-emerges-from-stealth-with-12-million-in-seed-funding/)
