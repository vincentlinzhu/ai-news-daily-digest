# AI Industry & General News — 2026-05-29

---

## Top Stories (5)

### 1. Anthropic Raises $65B at $965B Valuation, Surpasses OpenAI as World's Most Valuable AI Startup

**Source:** [TechCrunch](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-28/anthropic-raises-at-965-billion-valuation-eclipsing-openai) · [CNBC](https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html) · [PitchBook](https://pitchbook.com/news/articles/anthropic-bests-openai-in-valuation-race-hitting-965b-with-series-h)

Anthropic has closed a $65 billion Series H funding round at a $965 billion post-money valuation, officially surpassing OpenAI's $852 billion valuation (from its March $122B Series F) to become the world's most valuable private AI company. The round was co-led by Altimeter Capital, Dragoneer, Greenoaks, and Sequoia Capital, with co-investors including Capital Group, Coatue, D1 Capital Partners, GIC, ICONIQ, and nearly every major institutional player in tech—Blackstone, Brookfield, D.E. Shaw, DST Global, Fidelity, General Catalyst, Insight Partners, Jane Street, Lightspeed, Temasek, and T. Rowe Price. The $65B figure includes $15B in previously committed hyperscaler capital (primarily $5B from Amazon), and strategic chip-infrastructure partners Samsung, SK Hynix, and Micron also joined the round.

The fundraise was accompanied by a landmark revenue disclosure: Anthropic's annualized run-rate revenue crossed $47 billion in May 2026—up from $14 billion in February and $9 billion at end-2025—driven primarily by Claude Code enterprise adoption. The company projects a 130% revenue surge that would yield its first operating profit. The Wall Street Journal reported gross margins exceeding 70%. With 500+ customers spending $1M+/year and 8 of 10 Fortune 10 companies on the platform, the valuation is now grounded in verifiable unit economics rather than speculation.

The capital will be deployed toward safety research, expanded compute infrastructure, and scaling Claude's enterprise products. Anthropic has also assembled more than $200B in multi-year compute commitments across Amazon (5 GW), Google/Broadcom (5 GW TPU), Microsoft/NVIDIA ($30B Azure), SpaceX Colossus 1 (300MW+), and Fluidstack ($50B). IPO timing remains fluid—The Information previously reported October 2026, CNBC confirmed Anthropic is preparing its IPO "behind the scenes"—while rival OpenAI is moving to file its confidential S-1 within weeks targeting a September listing.

**Key details:**
- $65B Series H at $965B post-money; OpenAI was at $852B after a larger $122B raise in March
- Annualized revenue: $47B (May 2026) vs. ~$25–30B at OpenAI; 3× in 90 days
- 10+ GW compute pipeline; SpaceX Colossus 1 (220K+ NVIDIA GPUs) already active, doubling Claude Code rate limits
- IPO target: October 2026 (The Information); no S-1 filed; revenue expected to hit ~$50B run-rate by June
- Valuation went from $380B (Feb 2026 Series G) to $965B in roughly 90 days

---

### 2. Anthropic Launches Claude Opus 4.8 with Dynamic Workflow and Claude Mythos Confirmed for June

**Source:** [American Bazaar](https://americanbazaaronline.com/2026/05/29/anthropic-launches-claude-opus-4-8-with-stronger-coding-481789/) · [Crypto Briefing](https://cryptobriefing.com/anthropic-opus-4-8-dynamic-workflow-claude-code/) · [SQ Magazine](https://sqmagazine.co.uk/claude-mythos-public-release-safety-tests/) · [AI Insider](https://theaiinsider.tech/2026/05/29/anthropic-announces-65b-funding-round-at-965b-valuation-in-landmark-series-h-as-opus-4-8-and-compute-deal-land-on-same-day/)

Anthropic released Claude Opus 4.8 today alongside its Series H announcement, making the dual news day a defining moment for the company's enterprise positioning. The headline feature is **Dynamic Workflow**—a research preview capability for Claude Code that allows the system to autonomously plan a complex task, spawn hundreds of parallel subagents, verify its own outputs, and deliver finished results in a single session. Anthropic demonstrated a real-world case: migrating a 750,000-line codebase in 11 days with a 99.8% test pass rate using coordinated subagents—a benchmark that would have required months of manual engineering work.

Beyond Dynamic Workflow, Opus 4.8 introduces faster processing modes, adjustable effort settings that let enterprise customers balance cost/speed/reasoning depth, and improved performance on computer-use, financial analysis, and long-form research evaluations. Pricing is unchanged from Opus 4.7: $5/M input tokens, $25/M output tokens—a deliberate hold against GPT-5.5's $5/$30 and Claude Opus 4.7's $15/$75 pricing. The model is available immediately on Max, Team, and Enterprise plans, and via the Claude API, Amazon Bedrock, and Google Vertex AI.

In the same announcement, Anthropic confirmed that **Claude Mythos**—its restricted-access, frontier cybersecurity-focused model family—will reach all customers "in the coming weeks" following safety evaluations. Through Project Glasswing, Mythos has already identified 23,000+ software vulnerabilities in partnership with AWS, Apple, Broadcom, Cisco, CrowdStrike, and Google. Mythos will effectively be the first model in history released with an explicit cybersecurity capability declaration, with safeguards still being finalized. Its public launch is expected in June.

**Key details:**
- Dynamic Workflow: hundreds of parallel subagents coordinated within one Claude Code session; 750K-line migration in 11 days / 99.8% test pass rate
- Pricing held flat at $5/$25 per M tokens; lower-cost "effort-scaled" mode added for cost-sensitive workloads
- Opus 4.8 available: API, Bedrock, Vertex AI, Max/Team/Enterprise plans
- Claude Mythos: 23,000+ CVEs identified in Project Glasswing; public release "in coming weeks" (June)
- Also: Claude for Small Business (launched May 13) integrates QuickBooks, PayPal, HubSpot, Canva, DocuSign, G Suite, M365, Square, Stripe, Slack, Webflow—15 prebuilt agentic workflows for SMBs

---

### 3. Google I/O 2026: Gemini 3.5 Flash, Antigravity 2.0, Gemini Embedding 2, and Gemini Spark Define the "Agentic Gemini Era"

**Source:** [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/) · [Google Developers Blog](https://developers.googleblog.com/en/all-the-news-from-the-google-io-2026-developer-keynote/) · [CRN](https://www.crn.com/news/cloud/2026/google-ceo-explains-6-big-ai-and-gemini-launches-at-google-i-o-keynote) · [EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/google-deepmind-puts-gemini-embedding-2-into-the-race-for-multimodal-ai-search)

Google used I/O 2026 (held May 19–20) to declare what CEO Sundar Pichai called "the agentic Gemini era," anchored by two major new model families and a redesigned developer platform. **Gemini 3.5 Flash**—the first in the Gemini 3.5 series—is Google's fastest frontier model, 4× faster than prior frontier models by standard benchmarks and 12× faster in an optimized variant. It outperforms Gemini 3.1 Pro on nearly every benchmark while running at Flash speeds, making it the default model for the Gemini app globally, AI Mode in Google Search, and the new Gemini Enterprise Agent Platform. Google 3.5 Pro is already in internal testing, expected June. The companion release, **Gemini Omni Flash**, adds native video generation to the Gemini family—previously reported; continuing rollout to API/enterprise this week.

**Google Antigravity 2.0** is the reorganized developer platform, replacing Vertex AI as the canonical way to build, deploy, and govern agents. It ships with: a standalone desktop app for orchestrating multiple agents in parallel; an Antigravity CLI for terminal-native agent creation; an Antigravity SDK for self-hosted deployment; and **Managed Agents** in the Gemini API—a single API call that provisions a fully sandboxed Linux agent (with web browsing, code execution, and file management) powered by the Antigravity harness. Google processed 3 trillion tokens/day internally on Antigravity tools in May, up from 500 billion in March—6× in ~60 days. **Gemini Spark**, a 24/7 personal AI agent integrated with Gmail/Docs/Calendar/Drive, launched to Ultra subscribers in the US this week.

Today (May 29), Google DeepMind separately released **Gemini Embedding 2**, a native multimodal embedding model mapping text, images, video, audio, documents, and code into a unified vector space. Key benchmarks: 62.9 Recall@1 (MSCOCO text-to-image), 68.8 NDCG@10 (Vatex text-to-video), 69.9 MTEB multilingual, 84.0 MTEB Code. Available now in public preview via Gemini API and Google Cloud Vertex AI (model ID: `gemini-embedding-2`), with scalable output dimensions from 128 to 3,072 via Matryoshka Representation Learning. On the enterprise cloud side, **Nano Banana 2** (Gemini 3.1 Flash Image) and **Nano Banana Pro** (Gemini 3 Pro Image) also reached GA on May 28 via the Gemini Enterprise Agent Platform, now supporting video as an input modality.

**Key details:**
- Gemini 3.5 Flash: default in Gemini app + Search globally; 4–12× faster than prior frontier; outperforms Gemini 3.1 Pro across benchmarks
- Gemini 3.5 Pro: internal testing, June release
- Antigravity 2.0: orchestrate multi-agent workflows; Managed Agents = single-API sandboxed agent (no infra setup)
- Gemini Embedding 2 (GA today): 6-modality unified embedding space; Matryoshka 128–3072 dims
- Gemini Spark: 24/7 personal agent, US Ultra subscribers; macOS app coming summer 2026
- Google processing 3T tokens/day internally on Antigravity (6× growth in 60 days)

---

### 4. Meta Raises 2026 AI Capex to $145B, Launches Meta Compute Initiative, Eyes Cloud Entry

**Source:** [Fortune](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/) · [Implicator](https://www.implicator.ai/zuckerberg-offers-wall-street-a-cloud-answer-for-ai-spending/) · [MarketPulse](https://market-pulse.co/article/20785/meta-eyes-cloud-market-entry-as-ai-spending-surges-to-145b) · [Mark Zuckerberg/Facebook](https://www.facebook.com/zuck/posts/today-were-establishing-a-new-top-level-initiative-called-meta-compute-meta-is-p/10117230523669241/)

Meta has raised its 2026 capex guidance to $125–$145 billion (up from $115–$135B), and CEO Mark Zuckerberg told shareholders that entering the cloud computing market is "definitely on the table" if the company overbuilds data center capacity. This marks the first time a hyperscaler-scale AI investor has explicitly flagged commercializing surplus compute rather than just absorbing it internally. The announcement came alongside the formal creation of **Meta Compute**, a new top-level organizational initiative led by Santosh Janardhan (global infrastructure) and Daniel Gross (long-term capacity strategy), with Dina Powell McCormick (former US Deputy National Security Advisor, newly appointed Meta President) heading government and sovereign infrastructure partnerships.

Meta's compute ambitions are multi-decade in scope. Zuckerberg's post described plans for "tens of gigawatts this decade" and "hundreds of gigawatts or more over time," backed by nuclear energy agreements with TerraPower, Oklo, Vistra, and Constellation Energy targeting 6.6 GW of new and existing US electricity capacity by 2035. The Prometheus AI supercluster in Ohio is the current flagship. Combined with OpenAI's ~$500B Stargate commitment, Microsoft's $80B data center build, Amazon's $150B cloud expansion, Google's undisclosed but multi-hundred-billion infrastructure spend, and Anthropic's $200B+ compute contracts—the combined six-hyperscaler-equivalent AI capex for 2026 now exceeds $700B. This is the largest concentrated infrastructure build-out in human history.

The cloud-entry signal is strategically significant: AWS, Azure, and Google Cloud have built their enterprises over decades of customer relationships Meta does not have. But the direction of travel—AI-first compute companies generating their own cloud products—points to a fundamental restructuring of the cloud market by 2028–2030. Meta also confirmed it will test paid AI subscription tiers (at $7.99 and $19.99/month) in Singapore, Guatemala, and Bolivia next month, the first step toward monetizing its AI investments at consumer scale.

**Key details:**
- Meta 2026 capex: $125–145B (prior guidance: $115–135B); up ~$10B at midpoint
- Meta Compute org: Janardhan (infra), Gross (capacity strategy), Powell McCormick (gov't partnerships)
- Nuclear energy: 6.6 GW US capacity by 2035 (TerraPower, Oklo, Vistra, Constellation)
- Cloud ambition: "definitely on the table" if Meta overbuild; no contracts, customers, or timeline yet
- AI subscription test: $7.99/$19.99/month in Singapore, Guatemala, Bolivia next month

---

### 5. OpenAI Codex Expands to Windows with Computer Use; GPT-5.5 API Now Fully Live

**Source:** [9to5Mac](https://9to5mac.com/2026/05/29/chatgpt-for-ios-can-now-start-codex-work-on-windows/) · [OpenAI](https://openai.com/index/introducing-gpt-5-5/) · [Tech Insider](https://tech-insider.org/gpt-5-5-launch-openai-april-23-terminal-bench-2026/)

OpenAI today shipped major Codex platform expansions: **Computer Use now works on Windows**, and **remote control for Codex on Windows** extends to ChatGPT on iOS/Android and Codex on Mac. Previously, Computer Use and remote control were Mac-only; Windows users can now have Codex see, click, and type across desktop apps in the foreground while it works. ChatGPT on iOS and Android can initiate Codex tasks on a remote Windows machine and monitor their progress, bringing cross-platform agentic computing to OpenAI's full user base. The release also added profile details, usage stats, and token activity to the Codex desktop app.

In context, this week marked the first full API deployment cycle for **GPT-5.5**, which launched to ChatGPT users on April 23 and hit the API on April 24. GPT-5.5 sits at 82.7% on Terminal-Bench 2.0, 84.9% on GDPval, and 58.6% on SWE-Bench Pro—the three benchmarks OpenAI has prioritized as replacements for saturated academic tests. Standard API pricing is $5/$30 per million tokens (1M context), while GPT-5.5 Pro (for long-horizon research and codebase-wide refactors) is $30/$180. Notably, GPT-5.5's $5 input pricing matches Claude Opus 4.8's newly held pricing, with OpenAI undercutting Claude Opus 4.7's former $15 input cost significantly. OpenAI is now underpricing its closest competitor at comparable benchmark performance.

Looking ahead, OpenAI is preparing a confidential IPO S-1 filing targeting a September 2026 listing at a rumored $2T valuation—which would be larger than SpaceX's pending IPO and among the largest in US history. Internal tensions have emerged: CFO Sarah Friar has reportedly expressed concerns about IPO timing and has been excluded from key meetings (Business Insider). The company also made headlines this week for a separate claim that a general-purpose reasoning model (not a specialized theorem prover) appears to have solved an 80-year-old Erdős conjecture in geometry—backed by commentary from mathematicians Noga Alon, Melanie Wood, and Thomas Bloom, though peer verification remains pending.

**Key details:**
- Codex for Windows: Computer Use + remote control from iOS/Android + cross-Mac/PC control (May 29)
- GPT-5.5: 82.7% Terminal-Bench, 84.9% GDPval, 58.6% SWE-Bench Pro; API at $5/$30 per M tokens
- GPT-5.5 Pro: $30/$180 per M tokens for Pro/Business/Enterprise
- OpenAI IPO: S-1 filing imminent; September 2026 target; ~$2T implied valuation; CFO friction reported
- Math claim: general-purpose model reportedly proves 80-year Erdős geometry conjecture; peer review pending

---

## Deep Dive: Anthropic's $965B Moment — Revenue, Infrastructure, and the IPO Race

Anthropic's Series H is the clearest expression yet of how AI's economics have changed. Just 90 days ago, the company was worth $380 billion. Today it is at $965 billion—nearly tripling in a quarter—and the move is not purely speculative. The revenue trajectory underpins it: $9B annualized at end-2025, $14B by mid-February, $30B by early April, $47B in May. The acceleration is driven almost entirely by Claude Code enterprise adoption. With 500+ customers spending $1M+/year and 8 of 10 Fortune 10 companies on the platform, Anthropic has crossed from developer adoption into enterprise lock-in.

The structural element that makes this round unusual is the compute pipeline attached to it. Anthropic has $200B+ in multi-year compute contracts: 5 GW from Amazon (1 GW online by year-end), 5 GW from Google/Broadcom (TPU, starting 2027), $30B Azure from Microsoft/NVIDIA, SpaceX Colossus 1 (220K+ NVIDIA GPUs, already live), and Fluidstack ($50B). When the SpaceX deal came online in early May, Claude Code 5-hour rate limits immediately doubled for Pro/Max/Team/Enterprise, and Tier 1 API input limits for Opus jumped 1,500%. The pattern is direct: more compute → higher rate limits → more enterprise feasibility for large agentic workloads → more revenue. Investors are therefore pricing not just current ARR but the infrastructure locked into the growth path.

The competitive dynamics with OpenAI are now multi-dimensional. On revenue, Anthropic ($47B ARR) has overtaken OpenAI (~$25–30B ARR). On valuation, Anthropic ($965B) has overtaken OpenAI ($852B). On model pricing, Anthropic held Opus 4.8 at $5/$25 while OpenAI's GPT-5.5 sits at $5/$30—meaning the same input price for roughly equivalent coding performance, with Anthropic's Pro model now cheaper on output. The one area where OpenAI retains an edge is consumer distribution: ChatGPT has hundreds of millions of active users; Anthropic's claude.ai user count is not publicly disclosed but is estimated at a fraction of that.

The IPO race adds time pressure. OpenAI is reported to be filing its confidential S-1 within weeks for a September 2026 listing. Anthropic's October 2026 target means the two most valuable AI companies will attempt to go public within the same 8-week window—a coincidence that will test institutional investor appetite, lock-up structures, and market timing in a way that has no modern precedent. The SpaceX IPO, previously expected in June, adds a third mega-listing. Anthropic's Public Benefit Corporation structure and Dario Amodei's maintained voting control are expected to be key differentiators in the S-1 narrative; the company can argue it has aligned financial and safety incentives in a way a Delaware C-Corp cannot.

Claude Mythos arriving in June adds another dimension: it is the first model class explicitly positioned as a cybersecurity AI, with documented identification of 23,000+ vulnerabilities through Project Glasswing. If Mythos deploys without misuse incidents, it validates Anthropic's safety-first commercialization thesis at a critical pre-IPO moment. If misuse occurs, it creates exactly the kind of headline risk that could affect investor sentiment. Anthropic knows this—the company delayed Mythos specifically because its cybersecurity capabilities exceeded existing safeguard frameworks. The decision to release it weeks before the IPO preparation window is a calculated bet on the strength of its safety infrastructure.

The broader implication for the AI industry: the "last private round" framing from TechCrunch reflects a genuine structural shift. At $965B, Anthropic is already larger than all but 8–10 public companies. The private market premium over public comps has inverted—investors now pay more to be in pre-IPO, not less. This dynamic, which also characterized OpenAI's March round, signals that AI model companies have become an entirely new asset class where traditional VC valuation frameworks no longer apply.

---

## Data for Visualization

```json
{
  "chart_type": "bar",
  "title": "Top AI Startup Valuations (May 2026)",
  "unit": "$B",
  "data": [
    {"label": "Anthropic", "value": 965},
    {"label": "OpenAI", "value": 852},
    {"label": "xAI (SpaceX-merged)", "value": 1250},
    {"label": "Databricks", "value": 62},
    {"label": "Mistral", "value": 6}
  ]
}
```

```json
{
  "chart_type": "line",
  "title": "Anthropic Annualized Revenue Run-Rate (2025–2026)",
  "unit": "$B",
  "data": [
    {"label": "Dec 2025", "value": 9},
    {"label": "Feb 2026", "value": 14},
    {"label": "Apr 2026", "value": 30},
    {"label": "May 2026", "value": 47}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "2026 AI Capex Commitments by Company",
  "unit": "$B",
  "data": [
    {"label": "Meta", "value": 145},
    {"label": "Amazon (AWS)", "value": 150},
    {"label": "Microsoft", "value": 80},
    {"label": "Alphabet/Google", "value": 75},
    {"label": "Anthropic (compute contracts)", "value": 200},
    {"label": "OpenAI (Stargate)", "value": 500}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Frontier Model API Pricing Comparison (May 2026)",
  "unit": "$/M tokens (output)",
  "data": [
    {"label": "Claude Opus 4.8 ($5 in)", "value": 25},
    {"label": "GPT-5.5 ($5 in)", "value": 30},
    {"label": "Claude Opus 4.7 ($15 in)", "value": 75},
    {"label": "GPT-5.5 Pro ($30 in)", "value": 180}
  ]
}
```

```json
{
  "chart_type": "bar",
  "title": "Anthropic Compute Pipeline (Gigawatts Committed)",
  "unit": "GW",
  "data": [
    {"label": "Amazon (by end 2026)", "value": 1},
    {"label": "Amazon (full contract)", "value": 5},
    {"label": "Google/Broadcom (2027+)", "value": 5},
    {"label": "SpaceX Colossus 1 (online)", "value": 0.3},
    {"label": "Fluidstack", "value": 1}
  ]
}
```

---

## Analysis & Impact for ML/Agentic Engineers

- **Dynamic Workflow is the most consequential Claude Code feature since its launch.** The ability to orchestrate hundreds of parallel subagents within a single session—with self-verification loops—changes the economics of large-scale software engineering tasks. The 750K-line codebase migration benchmark (11 days, 99.8% test pass) is a credible, production-scale demonstration. Engineers building agentic coding systems should evaluate Dynamic Workflow for tasks they currently decompose manually across multiple sequential runs. The practical ceiling on parallel subagent count and session duration has not been publicly disclosed; expect rate-limit expansions as Anthropic's compute pipeline (Amazon 1 GW online by year-end) comes online.

- **Gemini Embedding 2's unified multimodal embedding space is immediately useful for RAG pipelines.** The ability to embed text, images, video, audio, documents, and code into a single comparable vector space removes a major architectural seam in multimodal retrieval systems. Previously, multi-modal RAG required separate embedding models with heterogeneous vector spaces and complex cross-modal fusion logic. Gemini Embedding 2's Matryoshka scaling (128–3,072 dimensions) allows engineers to trade storage cost against retrieval quality without retraining. For teams building agents that need to reason across document, image, and video corpora simultaneously, this is a meaningful infrastructure simplification.

- **Antigravity's Managed Agents API is Google's answer to Claude Code's parallel subagents.** A single API call that provisions a sandboxed Linux agent with web browsing, code execution, and file management abstracts away all infrastructure setup. For engineers who want the capabilities of a full-environment coding agent without managing container orchestration, this is a significant DX improvement. The key limitation is lock-in: agents running in the Antigravity harness are Google-infrastructure-native. Compare this to OpenCode or Claude Code, which can run against any provider. The tradeoff is convenience vs. portability.

- **The pricing war between Anthropic and OpenAI has reached parity at the frontier.** Claude Opus 4.8 and GPT-5.5 are now priced identically on input ($5/M tokens) with Anthropic cheaper on output ($25 vs. $30/M). For teams that were paying $15/M for Claude Opus 4.7 and considering switching to GPT-5.5, Opus 4.8 removes the cost argument. The competitive moat has shifted entirely to capability and ecosystem integration. Engineers should re-benchmark their workloads against both models at current pricing; the conclusions from Q1 2026 cost analyses are likely stale.

- **EU AI Act compliance clock is real and imminent for high-risk AI deployments.** The August 2, 2026 deadline for high-risk AI system obligations under Annex III remains technically operative—the Digital Omnibus provisional agreement (May 7) that would defer to December 2027 has not been formally adopted and could fail. Any ML team with EU customers deploying AI in employment, credit, healthcare, education, biometric, law enforcement, or immigration contexts needs to have its conformity assessment, technical documentation, risk management system, and transparency obligations either complete or provably underway. Do not assume the Omnibus extension. The US Senate's 99–1 vote to preserve 149+ state AI laws also signals that American compliance complexity will continue to compound.

---

## Key Takeaways (TL;DR)

- **Anthropic is now worth more than OpenAI** ($965B vs $852B) after a $65B Series H, with $47B annualized revenue and 10+ GW compute pipeline—the largest private AI fundraise in history.
- **Claude Opus 4.8 launched today** with Dynamic Workflow (hundreds of parallel subagents per session); priced flat at $5/$25/M tokens, making it cost-competitive with GPT-5.5.
- **Claude Mythos arrives in June**—23,000+ CVEs identified in Project Glasswing; first explicitly cybersecurity-positioned frontier model; Anthropic deploying it weeks before IPO prep window.
- **Google's Gemini 3.5 Flash + Antigravity 2.0** (from I/O 2026 two weeks ago) are now in broad GA; today's Gemini Embedding 2 release adds native 6-modality unified vector embeddings for RAG/search.
- **OpenAI expanded Codex to Windows** (Computer Use + remote control) while GPT-5.5 ($5/$30) hits full API availability—prices converge with Anthropic, shifting competition to pure capability.
- **Meta's $125–145B capex and Meta Compute initiative** signal a potential cloud market entry if excess data center capacity is built; nuclear energy contracts for 6.6 GW by 2035.
- **EU AI Act August 2 deadline is real**—Omnibus deferral to Dec 2027 not yet formally adopted; US federal AI moratorium killed 99-1, preserving 149+ state-level AI laws.

---

*Sources:*
- https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/
- https://www.bloomberg.com/news/articles/2026-05-28/anthropic-raises-at-965-billion-valuation-eclipsing-openai
- https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html
- https://pitchbook.com/news/articles/anthropic-bests-openai-in-valuation-race-hitting-965b-with-series-h
- https://byteiota.com/anthropic-series-h-965-billion-valuation/
- https://americanbazaaronline.com/2026/05/29/anthropic-launches-claude-opus-4-8-with-stronger-coding-481789/
- https://cryptobriefing.com/anthropic-opus-4-8-dynamic-workflow-claude-code/
- https://sqmagazine.co.uk/claude-mythos-public-release-safety-tests/
- https://theaiinsider.tech/2026/05/29/anthropic-announces-65b-funding-round-at-965b-valuation-in-landmark-series-h-as-opus-4-8-and-compute-deal-land-on-same-day/
- https://www.anthropic.com/news/claude-for-small-business
- https://www.anthropic.com/news/google-broadcom-partnership-compute
- https://www.anthropic.com/news/higher-limits-spacex
- https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- https://developers.googleblog.com/en/all-the-news-from-the-google-io-2026-developer-keynote/
- https://www.crn.com/news/cloud/2026/google-ceo-explains-6-big-ai-and-gemini-launches-at-google-i-o-keynote
- https://www.edtechinnovationhub.com/news/google-deepmind-puts-gemini-embedding-2-into-the-race-for-multimodal-ai-search
- https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-and-nano-banana-pro-are-generally-available
- https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/
- https://9to5mac.com/2026/05/29/chatgpt-for-ios-can-now-start-codex-work-on-windows/
- https://openai.com/index/introducing-gpt-5-5/
- https://tech-insider.org/gpt-5-5-launch-openai-april-23-terminal-bench-2026/
- https://www.mitsloanme.com/article/openai-claims-general-purpose-ai-solved-an-80-year-mathematical-problem/
- https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/
- https://www.implicator.ai/zuckerberg-offers-wall-street-a-cloud-answer-for-ai-spending/
- https://www.facebook.com/zuck/posts/today-were-establishing-a-new-top-level-initiative-called-meta-compute-meta-is-p/10117230523669241/
- https://market-pulse.co/article/20785/meta-eyes-cloud-market-entry-as-ai-spending-surges-to-145b
- https://algeriatech.news/global-ai-regulation-divergence-us-eu-china-three-rulebooks-cto-strategy-2026/
- https://informedclearly.com/en/ai/53075/ai-regulatory-divergence-systemic-risk-2026
- https://techne.ai/insights/eu-ai-act-for-us-boards/
- https://matthewbertram.com/blog/eu-ai-act-what-us-businesses-need-to-know/
- https://press.aboutamazon.com/2026/5/snowflake-expands-aws-collaboration-with-6b-commitment-to-accelerate-enterprise-agentic-ai-adoption
- https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development
- https://www.marketingprofs.com/opinions/2026/54875/ai-update-may-29-2026-ai-news-and-views-from-the-past-week
- https://www.tradingkey.com/analysis/stocks/us-stocks/261935293-anthropic-ipo-openai-claude-code-tradingkey
