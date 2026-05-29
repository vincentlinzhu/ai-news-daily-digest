# Best Models & Benchmarks — 2026-05-29

## Top Model News (3-5)

### 1. Claude Opus 4.8 — Anthropic ships new flagship with Dynamic Workflows and fast mode
**Source:** [Anthropic Blog](https://www.anthropic.com/news/claude-opus-4-8) | [llm-stats.com deep dive](https://llm-stats.com/blog/research/claude-opus-4-8-launch) | [ChatForest review](https://chatforest.com/reviews/anthropic-claude-opus-4-8-dynamic-workflows-effort-control-review/)

Released May 28, 2026 — just 43 days after Opus 4.7 — Claude Opus 4.8 is Anthropic's new highest-general-access model. It posts 88.6% on SWE-bench Verified (up 1pp from 4.7's 87.6%), 74.6% on Terminal-Bench 2.1 (replacing 2.0 as the new terminal-agent standard), 93.6% on GPQA Diamond, and 1,890 Elo on GDPval-AA — the last of which is a meaningful reversal from where Opus 4.7 trailed GPT-5.5 by 18 points; 4.8 now leads GPT-5.5 by 121 points on OpenAI's own economic-value benchmark. On SWE-bench Pro (the contamination-resistant variant), Opus 4.8 posts 69.2%, compared to 64.3% on 4.7.

The headline new capability is **Dynamic Workflows** for Claude Code: Opus 4.8 can now plan a codebase-scale task, spin up hundreds of parallel subagents to execute it, verify its own outputs, and deliver finished work in a single session. Anthropic demonstrated this with a 750,000-line codebase migrated in 11 days at a 99.8% test pass rate. Mid-task system messages are now supported on the Messages API — a long-requested feature that allows agent orchestrators to inject guidance without restarting a context. An optional **fast mode** provides ~2.5× throughput at $10/$50 per million tokens (vs. $5/$25 standard). Honesty and calibration improvements are noted in the alignment assessment, described as "measurable" though not yet quantified publicly.

Anthropic simultaneously confirmed in the release notes that a **Mythos-class model** will reach broad availability "in the coming weeks" — framing Opus 4.8 as an acknowledged bridge release. The model is generally available on Claude.ai, the Claude API (`claude-opus-4-8`), Amazon Bedrock, Google Vertex AI, and Microsoft Foundry. Effort levels default to `high`, with `xhigh` and `max` available for harder problems.

**Key specs:** 1M input / 128K output tokens | Text + vision input, text output | $5/$25 per 1M tokens (standard), $10/$50 (fast mode) | Proprietary | Generally available

---

### 2. Gemini 3.5 Flash — Google I/O flagship Flash that surpasses Gemini 3.1 Pro
**Source:** [Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash) | [Google Blog](https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/) | [byteiota review](https://byteiota.com/gemini-35-flash-benchmarks-pricing-agentic-developer-guide/)

Released May 19, 2026 at Google I/O, Gemini 3.5 Flash is the first model in Google's new 3.5 generation. Positioned as an agentic/coding specialist, it has already displaced Gemini 3.1 Pro as the default model in the Gemini consumer app, Google Search's AI Mode (1B+ users), and the Gemini API. Its headline benchmark result is 76.2% on Terminal-Bench 2.1 — surpassing Gemini 3.1 Pro's 68.5% — and 83.6% on MCP Atlas tool-use, which leads the entire field including Claude Opus 4.7 and GPT-5.5. It also posts 55.1% on SWE-bench Pro (above GPT-5.5's 58.6% but below Claude Opus 4.7's 64.3%), 84.2% on CharXiv Reasoning, and 72.1% on ARC-AGI-2. On the Artificial Analysis Intelligence Index, Gemini 3.5 Flash scores **55**, up 9 points from Gemini 3 Flash and placing it firmly among the tier-two-frontier models.

The value proposition is price and speed: at $1.50 / $9.00 per million tokens and ~289 output tokens/second, Flash is 40% cheaper and 4× faster than Gemini 3.1 Pro ($2.00/$12.00, ~122 tok/s). Cached-input pricing drops to $0.15/M (90% discount). Dynamic thinking is on by default with configurable levels (Low/Medium/High). The model also introduces the **Gemini Spark** personal agent surface, rolling out to AI Ultra ($100/mo) subscribers, built on top of 3.5 Flash. Thinking mode is supported; computer use is not yet available on Flash (expected in Pro). Knowledge cutoff is January 2026.

Gemini **3.5 Pro** was announced alongside Flash at I/O but is not yet publicly available — currently in internal testing at Google, with Sundar Pichai confirming on stage: "Give us until next month." June 2026 is the expected window. No benchmarks, pricing, or model card have been disclosed for Pro, though it targets the same frontier coding/reasoning/long-context segment as Gemini 3.1 Pro with a reported 2M-token context window.

**Key specs:** 1,048,576 input / 65,536 output tokens | Text, image, audio, video, PDF input; text output | $1.50/$9.00 per 1M tokens (Standard); $0.75/$4.50 (Batch); $0.15/M cached input | Proprietary | Generally available via Gemini app, AI Studio, Vertex AI, Gemini API

---

### 3. Claude Mythos Preview — Near-100% SWE-bench Verified, gated cybersecurity model nearing general release
**Source:** [Amazon Bedrock model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-mythos-preview.html) | [MindStudio benchmarks](https://www.mindstudio.ai/blog/claude-mythos-benchmark-results-swe-bench-agentic-coding) | [AndroidHeadlines](https://www.androidheadlines.com/2026/05/anthropic-claude-mythos-ai-model-public-release-cybersecurity.html)

Claude Mythos Preview was first released in a gated research preview on April 7, 2026, with access restricted to Project Glasswing participants (defensive cybersecurity teams at Apple, Microsoft, and select enterprises). As of May 2026 it holds the top position on SWE-bench Verified at **93.9%** — the first model to cross 90% on that benchmark — along with GPQA Diamond at **94.6%** and Humanity's Last Exam at **64.7%**, both best-in-class. On the Steel.dev and BenchLM leaderboards it leads every coding-agent benchmark where it has been evaluated.

The model is a distinct class above the Opus 4.x series, described by Anthropic as "a new class of intelligence built for ambitious projects focusing on cybersecurity, autonomous coding, and long-running agents." During restricted testing it autonomously identified hundreds of critical vulnerabilities in Firefox and Apple's M5 chips. The model uses Anthropic's Adaptive Thinking mode (continuous-depth reasoning) rather than a fixed thinking budget. Context window is 1M tokens / 128K output; knowledge cutoff December 2025. Access is currently via a `bedrock-mantle` endpoint (model ID `anthropic.claude-mythos-preview`).

With the Opus 4.8 release notes confirming broad availability "in the coming weeks," a general release is now the dominant expectation in the developer community. Debate continues about the appropriate safety envelope: OpenAI CEO Sam Altman publicly called the gating strategy "fear-based marketing" during a podcast appearance, while Anthropic maintains that finalized defensive safeguards must precede the general rollout.

**Key specs:** 1M input / 128K output tokens | Text + vision | Pricing TBD for general release | Proprietary | Gated preview only (Bedrock `bedrock-mantle` endpoint)

---

### 4. DeepSeek V4 — Open-weight frontier MoE at 30× cost reduction
**Source:** [Hugging Face blog](https://huggingface.co/blog/deepseekv4) | [DeepSeek V4 guide](https://deepseekai.guide/models/deepseek-v4/) | [CodersEra review](https://ghost.codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/)

DeepSeek V4 launched April 24, 2026 as a two-tier open-weight MoE family. The flagship V4-Pro (1.6T total / 49B active parameters, MIT license) matches Claude Opus 4.6 and Gemini 3.1 Pro on SWE-bench Verified (80.6%) while undercutting them at $0.435/$0.87 per million tokens — approximately 11× cheaper on input, 29× cheaper on output than Claude Opus 4.7. V4-Flash (284B total / 13B active) offers the same 1M context at $0.14/$0.28, the cheapest frontier-adjacent inference available.

V4-Pro leads the field on LiveCodeBench (93.5% vs. Claude Opus 4.6's ~89%), Terminal-Bench 2.0 (67.9% vs. Claude's 65.4%), and Codeforces rating (3,206 — approximately 23rd human rank globally). On HLE without tools, it trails GPT-5.4 and Claude (37.7% vs. ~40% for the leaders). Long-context retrieval is genuinely competitive: 94% MRCR accuracy to 128K, 82% at 512K, 59% at 1M — meaningfully ahead of Gemini 3.1 Pro (76.3% MRCR). An 85-person internal developer survey found 52% of respondents calling V4-Pro "ready to replace their current primary coding model."

The architecture ships three reasoning modes (non-thinking / high / max) selectable as API parameters, not separate endpoints — a UX improvement over the mode fragmentation common in competing thinking-model families. A community survey among 85 developers using V4-Pro as their daily driver found 52% saying it was ready to replace their primary model and 39% leaning toward yes.

**Key specs:** 1M input / 384K output tokens | Text | $0.435/$0.87 per 1M tokens (Pro), $0.14/$0.28 (Flash) | MIT License (open weights on Hugging Face) | API + self-host

---

### 5. GPT-5.6 Emerging in Internal Testing — June release expected at 1.5M context
**Source:** [Perplexity AI Magazine](https://perplexityaimagazine.com/ai-news/gpt-56-release-date-features-leaks-openai-2026/) | [WaveSpeed Blog](https://wavespeed.ai/blog/posts/gpt-5-6-canary-leak-what-we-know/) | [AIBase](https://news.aibase.com/news/28320)

GPT-5.6 has not been officially announced as of May 29, 2026, but multiple independent signals confirm active internal testing. The identifier `gpt-5.6` surfaced in OpenAI Codex backend logs on approximately May 13, followed by reports of ChatGPT Pro users experiencing context windows consistent with a 1.5M-token limit — 43% above GPT-5.5's documented 1M limit. Internal codenames `ember-alpha`, `beacon-alpha`, and `iris-alpha` have appeared in developer environment logs, consistent with multi-variant canary testing. Prediction markets at Polymarket and Manifold are pricing 80–89% probability of a public release by June 30, 2026.

The structural logic supports the timeline: GPT-5.4 launched March 5, GPT-5.5 launched April 23, and GPT-5.5 Instant became the default on May 5. The sub-60-day major-version cycle is now a documented pattern. If GPT-5.6 lands in early June as expected, it would coincide with Anthropic's anticipated Mythos general release and Google's Gemini 3.5 Pro launch — potentially the most model-dense single month in AI history.

No architecture, benchmark, or pricing details have been confirmed. A 1.5M context window, if verified, would put GPT-5.6 at the largest commercially deployed context window (surpassing Gemini 3.1 Pro's 2M only in API-deployed models where Claude and GPT currently max at 1M). A reasoning-specialized `GPT-5.6 Pro` variant targeting advanced agentic workflows is also rumored but unconfirmed.

**Key specs:** Unconfirmed | Expected: text + vision, possible extended multimodal | Pricing TBD (GPT-5.5 is $5/$30 per 1M) | Proprietary | Not released

---

## Deep Dive: Most Important Release — Claude Opus 4.8 (May 28, 2026)

### What It Can Do

Claude Opus 4.8 introduces Dynamic Workflows in Claude Code, a capability that transforms it from a single-agent coding assistant into a parallelized multi-agent orchestrator. In a single Claude Code session, the model can: (1) ingest and plan a codebase-scale task; (2) spawn hundreds of specialized subagents to execute work simultaneously; (3) verify each subagent's output against tests; and (4) consolidate results into a finished, verified deliverable. The 750,000-line migration demo — 11 days, 99.8% test pass rate — is the most concrete public demonstration of this capability at scale.

Beyond Dynamic Workflows, mid-task system messages via the Messages API allow orchestrators to inject guidance, constraints, or updated context into an active generation without restarting the conversation. This directly addresses a long-standing pain point for developers building multi-turn agentic pipelines. The optional fast mode (~2.5× throughput at 2× cost) enables latency-sensitive applications to opt into higher speed without a separate model ID. Effort control is now explicit: `high` (default), `xhigh`, and `max` effort levels allow callers to trade compute for quality on a per-request basis.

### Benchmark Highlights

| Benchmark | Claude Opus 4.8 | Claude Opus 4.7 | Previous Best (non-Anthropic) |
|---|---|---|---|
| SWE-bench Verified | **88.6%** | 87.6% | GPT-5.5: 88.7% |
| SWE-bench Pro | **69.2%** | 64.3% | GPT-5.5: 58.6% |
| Terminal-Bench 2.1 | **74.6%** | — (2.0: 69.4%) | Gemini 3.5 Flash: 76.2% |
| GPQA Diamond | **93.6%** | 94.2% | Claude Mythos Preview: 94.6% |
| GDPval-AA (Elo) | **1,890** | ~1,769 | GPT-5.5: ~1,769 |
| Humanity's Last Exam (w/ tools) | **57.9%** | — | Muse Spark: ~58% |
| LM Arena Elo | Expected top-5 | 1,492–1,505 | GPT-5.5-high: 1,484 |

### Architecture (known)

Anthropic has not disclosed architecture details for Opus 4.8. The model uses Adaptive Thinking, Anthropic's continuous-depth reasoning implementation that adjusts compute based on problem complexity. The fast mode suggests a separate inference path (likely reduced thinking budget or distillation) rather than a separate model checkpoint. Model ID is `claude-opus-4-8` on the Claude API.

### Pricing & Availability

| Mode | Input $/1M | Output $/1M | Use Case |
|---|---|---|---|
| Standard | $5.00 | $25.00 | Default agentic/coding workloads |
| Fast Mode | $10.00 | $50.00 | Latency-sensitive applications |

Available: Claude.ai (Max, Team, Enterprise plans), Claude API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry. Generally available as of May 28, 2026.

### Strategic Significance

Opus 4.8 is the clearest public signal yet that Anthropic's primary competitive axis in mid-2026 is **coding at enterprise scale** — not chat quality or consumer features. Dynamic Workflows directly targets the enterprise CTO procurement conversation (large-scale codebase migrations, automated refactoring, CI-integrated agentic loops). The GDPval-AA reversal — from trailing GPT-5.5 to leading it by 121 Elo points on OpenAI's own economic-value benchmark — is a pointed message about production ROI that sales teams can quote directly.

### Competitive Context

Opus 4.8 surpasses GPT-5.5 on SWE-bench Pro (69.2% vs. 58.6%), GDPval (Elo lead), and Humanity's Last Exam with tools (57.9% vs. ~57.2% for GPT-5.5 Pro). GPT-5.5 retains the lead on Terminal-Bench 2.0 (82.7% vs. Opus 4.8's 74.6%) and ARC-AGI-2 (85% vs. Anthropic's unreported Opus 4.8 score). Gemini 3.5 Flash leads on MCP Atlas (83.6%) and matches or exceeds on coding throughput. The net result is a genuine three-way split at the frontier: Anthropic owns agentic coding quality (SWE-bench Pro, GDPval), OpenAI owns reasoning and terminal-agent tasks (ARC-AGI-2, Terminal-Bench), and Google owns tool-use throughput and cost-efficiency at scale.

---

## Benchmark Comparison Data

```json
{"benchmark": "LM Arena Overall Elo (May 2026)", "results": [
  {"model": "GPT-5.5-high", "score": 1506},
  {"model": "Claude Opus 4.7 Thinking", "score": 1505},
  {"model": "Claude Opus 4.7", "score": 1503},
  {"model": "Claude Opus 4.6 Thinking", "score": 1502},
  {"model": "Claude Opus 4.6", "score": 1498},
  {"model": "Gemini 3.1 Pro Preview", "score": 1490},
  {"model": "Gemini 3.0 Pro", "score": 1486},
  {"model": "GPT-5.5 Standard", "score": 1476},
  {"model": "Grok 4.20 Beta", "score": 1479},
  {"model": "GPT-5.4 High", "score": 1479},
  {"model": "Meta Muse Spark", "score": 1491}
]}
```

```json
{"benchmark": "SWE-bench Verified (May 28, 2026)", "results": [
  {"model": "Claude Mythos Preview", "score": 93.9},
  {"model": "Claude Opus 4.8", "score": 88.6},
  {"model": "GPT-5.5 (OpenAI-reported)", "score": 88.7},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 87.6},
  {"model": "GPT-5.3 Codex", "score": 85.0},
  {"model": "Claude Opus 4.5", "score": 80.9},
  {"model": "Claude Opus 4.6", "score": 80.8},
  {"model": "Gemini 3.1 Pro", "score": 80.6},
  {"model": "DeepSeek V4-Pro-Max", "score": 80.6},
  {"model": "MiniMax M2.5", "score": 80.2},
  {"model": "GPT-5.2", "score": 80.0},
  {"model": "Claude Sonnet 4.6", "score": 79.6},
  {"model": "DeepSeek V4-Flash-Max", "score": 79.0},
  {"model": "Mistral Medium 3.5", "score": 77.6},
  {"model": "Kimi K2.6", "score": 80.2}
]}
```

```json
{"benchmark": "SWE-bench Pro (May 2026)", "results": [
  {"model": "Claude Mythos Preview", "score": 77.8},
  {"model": "Claude Opus 4.8", "score": 69.2},
  {"model": "Claude Opus 4.7", "score": 64.3},
  {"model": "GPT-5.5", "score": 58.6},
  {"model": "Gemini 3.5 Flash", "score": 55.1},
  {"model": "Claude Opus 4.5", "score": 45.9}
]}
```

```json
{"benchmark": "ARC-AGI-2 (May 20, 2026)", "results": [
  {"model": "GPT-5.5", "score": 85.0},
  {"model": "GPT-5.4 Pro", "score": 83.3},
  {"model": "Gemini 3.1 Pro", "score": 77.1},
  {"model": "Gemini 3.5 Flash", "score": 72.1},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8},
  {"model": "GPT-5.4", "score": 73.3},
  {"model": "Claude Opus 4.6", "score": 68.8},
  {"model": "Claude Sonnet 4.6", "score": 59.0},
  {"model": "Grok 4.20", "score": 53.3},
  {"model": "GPT-5.2", "score": 52.9},
  {"model": "Meta Muse Spark", "score": 42.5}
]}
```

```json
{"benchmark": "GPQA Diamond (May 2026)", "results": [
  {"model": "Claude Mythos Preview", "score": 94.6},
  {"model": "Gemini 3.1 Pro Preview (Vals)", "score": 95.45},
  {"model": "Gemini 3.1 Pro (codersera)", "score": 94.3},
  {"model": "Claude Opus 4.8", "score": 93.6},
  {"model": "Claude Opus 4.7", "score": 94.2},
  {"model": "GPT-5.5", "score": 93.5},
  {"model": "Gemini 3.5 Flash", "score": 92.68},
  {"model": "GPT-5.4", "score": 92.0},
  {"model": "Qwen 3.7 Max", "score": 92.3},
  {"model": "Meta Muse Spark", "score": 89.5}
]}
```

```json
{"benchmark": "Terminal-Bench 2.0/2.1 (May 28, 2026)", "results": [
  {"model": "GPT-5.5 (TB 2.0)", "score": 82.0},
  {"model": "Gemini 3.5 Flash (TB 2.1)", "score": 76.2},
  {"model": "Claude Opus 4.8 (TB 2.1)", "score": 74.6},
  {"model": "Qwen 3.6 Max (TB 2.0)", "score": 69.7},
  {"model": "Claude Opus 4.7 Adaptive (TB 2.0)", "score": 69.4},
  {"model": "Gemini 3.5 Flash (TB 2.0)", "score": 69.3},
  {"model": "GPT-5.4 xHigh (TB 2.0)", "score": 75.1},
  {"model": "DeepSeek V4-Pro-Max (TB 2.0)", "score": 67.9},
  {"model": "Kimi K2.6 (TB 2.0)", "score": 66.7}
]}
```

```json
{"benchmark": "Humanity's Last Exam (HLE, with tools, May 2026)", "results": [
  {"model": "Claude Mythos Preview", "score": 64.7},
  {"model": "Muse Spark (Contemplating)", "score": 58.0},
  {"model": "GPT-5.5 Pro", "score": 57.2},
  {"model": "Claude Opus 4.8", "score": 57.9},
  {"model": "Gemini 3.1 Pro Preview", "score": 48.0},
  {"model": "Claude Opus 4.7", "score": 46.0},
  {"model": "Gemini 3.5 Flash", "score": 40.2}
]}
```

```json
{"benchmark": "AIME 2026 (math olympiad, May 2026)", "results": [
  {"model": "GPT-5 (best-in-class)", "score": 100},
  {"model": "GPT-5.4", "score": 95},
  {"model": "Gemini 3.1 Pro", "score": 95},
  {"model": "Grok 4.2", "score": 93},
  {"model": "DeepSeek V3.2", "score": 88},
  {"model": "Claude Opus 4.6", "score": 85},
  {"model": "Llama 4 Scout", "score": 80}
]}
```

```json
{"benchmark": "LiveCodeBench (coding contest, May 2026)", "results": [
  {"model": "DeepSeek V4-Pro (Max)", "score": 93.5},
  {"model": "Claude Opus 4.7", "score": 89.0},
  {"model": "Claude Opus 4.6", "score": 88.8},
  {"model": "GPT-5.5", "score": 86.0},
  {"model": "Gemini 3.1 Pro", "score": 84.0}
]}
```

```json
{"benchmark": "MCP Atlas Tool-Use (May 2026)", "results": [
  {"model": "Gemini 3.5 Flash", "score": 83.6},
  {"model": "Claude Opus 4.6", "score": 73.8},
  {"model": "DeepSeek V4-Pro-Max", "score": 73.6},
  {"model": "Claude Opus 4.7", "score": 79.1},
  {"model": "GPT-5.5", "score": 72.0},
  {"model": "Gemini 3.1 Pro", "score": 78.2}
]}
```

```json
{"benchmark": "Artificial Analysis Intelligence Index v4 (May 2026)", "results": [
  {"model": "GPT-5.5", "score": 60},
  {"model": "Gemini 3.1 Pro Preview", "score": 57},
  {"model": "GPT-5.4", "score": 57},
  {"model": "Claude Opus 4.7", "score": 57},
  {"model": "Claude Opus 4.6", "score": 53},
  {"model": "Kimi K2.6 (open-weight)", "score": 54},
  {"model": "MiMo-V2.5-Pro (open-weight)", "score": 54},
  {"model": "Meta Muse Spark", "score": 52},
  {"model": "DeepSeek V4-Pro (open-weight)", "score": 52},
  {"model": "Gemini 3.5 Flash", "score": 55}
]}
```

```json
{"benchmark": "GDPval-AA Elo (economic value, May 2026)", "results": [
  {"model": "Claude Opus 4.8", "score": 1890},
  {"model": "Claude Opus 4.7", "score": 1769},
  {"model": "GPT-5.5", "score": 1769},
  {"model": "Gemini 3.5 Flash", "score": 1656},
  {"model": "Claude Opus 4.6", "score": 1619},
  {"model": "Claude Sonnet 4.6", "score": 1554},
  {"model": "DeepSeek V4-Pro-Max", "score": 1482},
  {"model": "GPT-5.2", "score": 1535}
]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Opus 4.8 | Anthropic | 1M in / 128K out | $5.00 | $25.00 | Text + vision → text |
| Claude Opus 4.8 (Fast) | Anthropic | 1M in / 128K out | $10.00 | $50.00 | Text + vision → text |
| Claude Mythos Preview | Anthropic | 1M in / 128K out | TBD (gated) | TBD | Text + vision → text |
| Claude Sonnet 4.6 | Anthropic | 500K | $3.00 | $15.00 | Text + vision → text |
| GPT-5.5 | OpenAI | 1M | $5.00 | $30.00 | Text + vision → text |
| GPT-5.5 Pro | OpenAI | 1M | $30.00 | $180.00 | Text + vision → text |
| Gemini 3.5 Flash | Google | 1,048,576 in / 65,536 out | $1.50 | $9.00 | Text, image, audio, video → text |
| Gemini 3.1 Pro Preview | Google | 2M | $2.00 | $12.00 | Text, image, audio, video → text |
| GPT-5.4 High | OpenAI | 1,050,000 | $12.50 | $50.00 | Text + vision → text |
| Grok 4.20 | xAI | 256K | $5.00 | $15.00 | Text + vision → text |
| Meta Muse Spark | Meta | 262K | API preview (invite) | API preview | Text, image, voice → text |
| DeepSeek V4-Pro | DeepSeek | 1M in / 384K out | $0.435 | $0.87 | Text → text |
| DeepSeek V4-Flash | DeepSeek | 1M in / 384K out | $0.14 | $0.28 | Text → text |
| Kimi K2.6 | Moonshot AI | 256K | ~$0.60 | ~$3.00 | Text + vision → text |
| Qwen 3.6-Plus | Alibaba | 1M | ~$0.29 | ~$1.65 | Text → text |
| MiniMax M2.5 | MiniMax | 1M | ~$0.30 | ~$1.20 | Text → text |
| Mistral Medium 3.5 128B | Mistral | 256K | $1.50 | $7.50 | Text → text |
| Qwen 3.6-27B | Alibaba (open) | 262K | Free (self-host) | Free | Text → text |
| Qwen 3.6-35B-A3B | Alibaba (open) | 262K | Free (self-host) | Free | Text → text |

---

## Analysis & Impact

- **Enterprise agentic coding has a new top tier.** Claude Opus 4.8's Dynamic Workflows, combined with Mythos Preview's 93.9% SWE-bench Verified, establishes Anthropic as the clear leader for large-scale automated software engineering tasks. For CTOs evaluating multi-week codebase migrations, both models present credible SoW replacements for human dev time that GPT-5.5 and Gemini 3.1 Pro cannot yet match on a quality-first selection.

- **Cost-performance at the open-weight frontier is compressing the premium.** DeepSeek V4-Pro at $0.435/$0.87 and Kimi K2.6 at $0.60/$3.00 score within 1–2 points of Claude Opus 4.6 and Gemini 3.1 Pro on SWE-bench Verified, while costing 10–30× less per token. For cost-sensitive agentic pipelines invoking models thousands of times per session, the business case for proprietary frontier models now requires explicit quality justification — not just brand or integration inertia.

- **Benchmark leadership is fragmented by category.** No single model dominates: GPT-5.5 leads ARC-AGI-2 (85%) and Terminal-Bench 2.0 (82%); Claude Mythos leads SWE-bench (93.9%), GPQA Diamond (94.6%), and HLE (64.7%); Gemini 3.5 Flash leads MCP Atlas (83.6%) and price-performance at the frontier tier; DeepSeek V4-Pro leads LiveCodeBench (93.5%) and Codeforces rating. Developers should run their specific-task evals rather than relying on any single leaderboard position.

- **June 2026 is shaping up as the most contested single month in AI history.** GPT-5.6 (Polymarket: 80–89% by June 30), Gemini 3.5 Pro (Pichai confirmed "next month"), and Claude Mythos general release (Anthropic: "coming weeks") are all expected to land simultaneously. The June window will likely resolve which lab holds the defensible frontier position through Q3 2026 and directly affect enterprise procurement decisions tied to annual AI budget cycles.

- **Medical reasoning emerges as a differentiated capability dimension.** Meta Muse Spark's 42.8% on HealthBench Hard — outperforming GPT-5.4 (40.1%) and Claude Opus 4.6 (14.8%) — signals that specialized training data (1,000+ physicians contributed) can produce category-specific gains that general intelligence benchmarks miss entirely. For healthcare AI procurement, HealthBench Hard is now the most informative single benchmark, and Muse Spark is the model to beat despite trailing on overall intelligence indices.

---

## Key Takeaways (TL;DR)

- **Claude Opus 4.8** (released May 28) advances Anthropic's agentic coding lead with Dynamic Workflows for large-scale parallel subagent execution; 88.6% SWE-bench Verified and a new GDPval-AA record (1,890 Elo) position it as the top general-access coding model while Mythos general release approaches.
- **Gemini 3.5 Flash** (released May 19) is a rare Flash-tier model that outperforms the previous premium tier (3.1 Pro) on coding and agentic benchmarks at 40% lower cost and 4× higher throughput; Gemini 3.5 Pro confirmed for June 2026.
- **Claude Mythos Preview** holds the SWE-bench Verified record at 93.9%, best-in-class GPQA Diamond (94.6%) and HLE (64.7%), and a broad public release is imminent per Anthropic's own release notes.
- **GPT-5.6** is in active internal testing with canary log signals and a probable 1.5M-token context window; Polymarket at 80–89% odds for a June 30 public release, converging with Mythos and Gemini 3.5 Pro for a potential three-way simultaneous launch.
- **Open-weight models** (DeepSeek V4-Pro, Kimi K2.6, Qwen 3.6) have closed to within 1–2 benchmark points of $5+/M proprietary models at 10–30× lower API cost, fundamentally changing the "default to closed-source" assumption for budget-conscious production deployments.

---

*Sources:*
- [Claude Opus 4.8 — llm-stats.com](https://llm-stats.com/blog/research/claude-opus-4-8-launch)
- [Claude Opus 4.8 — ChatForest review](https://chatforest.com/reviews/anthropic-claude-opus-4-8-dynamic-workflows-effort-control-review/)
- [Claude Opus 4.8 — CryptoBriefing](https://cryptobriefing.com/anthropic-opus-4-8-dynamic-workflow-claude-code/)
- [Claude Mythos Preview — Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-mythos-preview.html)
- [Claude Mythos — AndroidHeadlines](https://www.androidheadlines.com/2026/05/anthropic-claude-mythos-ai-model-public-release-cybersecurity.html)
- [LMSys Chatbot Arena May 2026 — Presenc AI](https://presenc.ai/research/lmsys-chatbot-arena-elo-rankings-may-2026)
- [LMSys Leaderboard — Swfte AI](https://www.swfte.com/blog/lmsys-arena-leaderboard-may-2026)
- [LMSys Chatbot Arena+ — OpenLM.ai](https://openlm.ai/chatbot-arena/)
- [LLM Leaderboard April 2026 — oFox AI](https://ofox.ai/blog/llm-leaderboard-best-ai-models-ranked-2026/)
- [SWE-bench Verified Leaderboard — BenchLM.ai](https://benchlm.ai/benchmarks/sweVerified)
- [SWE-bench Verified — Steel.dev](https://leaderboard.steel.dev/leaderboards/swe-bench-verified/)
- [SWE-bench Leaderboard 2026 — CodeAnt](https://www.codeant.ai/blogs/swe-bench-scores)
- [May 2026 Coding Agent Leaderboard — AITechConnect](https://aitechconnect.in/news/coding-agent-leaderboard-may-2026-claude-mythos-gpt55)
- [ARC-AGI-2 Leaderboard — BenchLM.ai](https://benchlm.ai/benchmarks/arcAgi2)
- [ARC-AGI-2 Explained — BenchLM.ai](https://benchlm.ai/blog/posts/arc-agi-2-explained)
- [ARC Prize — arcprize.org](https://arcprize.org/)
- [Terminal-Bench 2.0 Leaderboard — BenchLM.ai](https://benchlm.ai/benchmarks/terminalBench2)
- [AI Agent Benchmark Roundup May 2026 — CodersEra](https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/)
- [GPQA Leaderboard May 2026 — PricePerToken](https://pricepertoken.com/leaderboards/benchmark/gpqa)
- [Vals GPQA Diamond Mirror — BenchLM.ai](https://benchlm.ai/benchmarks/valsGpqaDiamond)
- [Gemini 3.5 Flash — Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash)
- [Gemini 3.5 — Google Blog](https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/)
- [Gemini 3.5 Flash Benchmarks — o-mega.ai](https://o-mega.ai/articles/gemini-3-5-flash-benchmarks-cost-and-guide)
- [Gemini 3.5 Flash Developer Guide — byteiota](https://byteiota.com/gemini-35-flash-benchmarks-pricing-agentic-developer-guide/)
- [Gemini 3.5 Complete Guide — CodersEra](https://codersera.com/blog/gemini-3-5-complete-guide-2026/)
- [Gemini 3.5 Pro Coming — WaveSpeed Blog](https://wavespeed.ai/blog/posts/gemini-3-5-pro-coming-next-month/)
- [GPT-5.6 Leak Analysis — Perplexity AI Magazine](https://perplexityaimagazine.com/ai-news/gpt-56-release-date-features-leaks-openai-2026/)
- [GPT-5.6 Codex Logs — WaveSpeed Blog](https://wavespeed.ai/blog/posts/gpt-5-6-canary-leak-what-we-know/)
- [GPT-5.6 1.5M Context — AIBase](https://news.aibase.com/news/28320)
- [GPT-5.5 Release — OpenAI](https://openai.com/index/introducing-gpt-5-5/)
- [Meta Muse Spark — Meta AI Blog](https://web.archive.org/web/20260509102400/https:/ai.meta.com/blog/introducing-muse-spark-msl/)
- [Muse Spark Analysis — WhatLLM.org](https://whatllm.org/blog/meta-is-back-muse-spark)
- [Muse Spark — Fortune](https://fortune.com/2026/04/08/meta-unveils-muse-spark-mark-zuckerberg-ai-push/)
- [Muse Spark Explained — AI Agents Arena](https://aiagentsarena.com/meta-muse-spark-explained-what-it-is-and-why-it-changes-everything/)
- [DeepSeek V4 — Hugging Face Blog](https://huggingface.co/blog/deepseekv4)
- [DeepSeek V4 Release — DeepSeek AI Guide](https://deepseekai.guide/news/deepseek-v4-release-date/)
- [DeepSeek V4 Review — CodersEra](https://ghost.codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/)
- [DeepSeek-V4-Pro — Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [Qwen 3.6 vs Kimi K2.6 — Lushbinary](https://lushbinary.com/blog/qwen-3-6-max-preview-vs-plus-vs-kimi-k2-6-comparison/)
- [Qwen 3.6 Reviewed — Towards AI](https://medium.com/@arvisionlab/qwen-3-6-reviewed-the-open-weight-coder-that-just-crashed-the-frontier-party-3b2e3e37ba34)
- [Chinese AI Models — TechTimes](http://www.techtimes.com/articles/317352/20260529/chinese-ai-models-lead-openrouter-traffic-coding-gains-come-china-data-risk.htm)
- [HLE Benchmark — lastexam.ai](https://lastexam.ai/)
- [Humanity's Last Exam Leaderboard — Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
