# Best Models & Benchmarks — 2026-05-19

## Top Model News (3-5)

### 1. Gemini 3.5 Flash — Google's Fastest Frontier Model Launches at Google I/O 2026
**Source:** [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) | [TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/) | [Neowin](https://www.neowin.net/news/google-announces-gemini-35-flash-its-strongest-coding-model-yet/)

Google released Gemini 3.5 Flash today at Google I/O 2026, kicking off the Gemini 3.5 model family with a bold pivot: this is explicitly designed not as a chatbot but as an agent runtime. The model outperforms the much larger Gemini 3.1 Pro on agentic and coding benchmarks while running at over 280 output tokens per second — approximately 4x faster than comparable frontier models. Google's CTO Koray Kavukcuoglu and Chief Scientist Jeff Dean co-authored the announcement, signaling executive-level commitment to the agentic direction.

The model is designed to execute long-horizon tasks — multi-week workflows that would take human auditors days are now completed by 3.5 Flash in hours. Coupled with the updated Antigravity harness (Google's agent-first development platform), it can orchestrate collaborative subagents for complex pipelines: enterprise demos showed Salesforce using it in Agentforce, Shopify running parallel subagents for merchant forecasting, and Macquarie Bank reasoning over 100+ page documents for customer onboarding. Google also announced Gemini Spark, a 24/7 personal AI agent powered by 3.5 Flash, rolling out to trusted testers immediately with beta for AI Ultra subscribers next week.

Gemini 3.5 Flash lands in the top-right quadrant of the Artificial Analysis intelligence index — frontier-level quality at exceptional speed. It already exceeds Gemini 3.1 Pro on Terminal-Bench 2.1 (76.2% vs prior best), GDPval-AA (Elo 1656), MCP Atlas (83.6%), and CharXiv Reasoning (84.2% multimodal). The 3.5 Pro orchestrator is being used internally at Google and is expected to roll out next month.

**Key specs:** 1M token context window | 65K max output tokens | Text, image, video, audio | $1.50/$9.00 per 1M input/output tokens | Proprietary | Generally available via Gemini API, AI Studio, Gemini Enterprise Agent Platform, and globally in the Gemini app and AI Mode in Search

---

### 2. GPT-5.5 Instant — OpenAI Refreshes Default ChatGPT Model With Major Factuality Gains
**Source:** [OpenAI Blog](https://openai.com/index/gpt-5-5-instant/) | [LLM Reference](https://www.llmreference.com/model/gpt-5.5-instant) | [LLM Stats](https://llm-stats.com/models/gpt-5.5-instant)

OpenAI shipped GPT-5.5 Instant on May 5, 2026, replacing GPT-5.3 Instant as the default model for all ChatGPT users — hundreds of millions of daily drivers. The update's headline metric is factuality: 52.5% fewer hallucinated claims on high-stakes prompts covering medicine, law, and finance compared to GPT-5.3 Instant, and 37.3% fewer inaccurate claims on conversations specifically flagged for factual errors. OpenAI published detailed side-by-side comparisons showing the model self-correcting algebraic errors that the prior version left undetected, a meaningful improvement for educational and technical use.

Beyond accuracy, GPT-5.5 Instant is the first default ChatGPT model to offer robust personalization from past chats, connected Gmail data, and saved memories — with new "memory sources" transparency controls that let users see exactly what context shaped a response and delete it if outdated. The model produces 30% fewer words per response on average while maintaining substance, reducing the overformatting and unnecessary follow-up questions that characterized 5.3. API availability is immediate as `chat-latest`; GPT-5.3 Instant remains available for paid users for three months before retirement.

This is architecturally notable as a "decoder-only" model with a 400K context window (up from prior generation), 128K max output, and multimodal support for text and image input. The pricing increase reflects the quality step-up: $5.00/$30.00 per 1M tokens puts it at the premium tier alongside Claude Opus 4.6. Enhanced personalization from past chats and Gmail is rolling out to Plus/Pro on web first, with Free/Business/Enterprise to follow.

**Key specs:** 400K context window | Text + image input | $5.00/$30.00 per 1M input/output tokens | Proprietary | Available as `chat-latest` in the API and as default ChatGPT model

---

### 3. Qwen3.6-27B — Alibaba's 27B Dense Model Beats 397B MoE Predecessor on All Coding Benchmarks
**Source:** [Alibaba Cloud Blog](https://www.alibabacloud.com/blog/qwen3-6-27b-flagship-level-coding-in-a-27b-dense-model_603063) | [GitHub](https://github.com/QwenLM/Qwen3.6/blob/main/README.md) | [BenchLM.ai](https://benchlm.ai/models/qwen3-6-27b)

Alibaba open-sourced Qwen3.6-27B on April 22, 2026 — a 27.8B parameter dense multimodal model that outperforms Qwen3.5-397B-A17B (15x larger) across every major coding benchmark. The efficiency story here is remarkable: by trading MoE breadth for dense architecture quality, Alibaba achieved 77.2% on SWE-bench Verified (vs. 76.2% for the 397B model), 87.8% on GPQA Diamond, and 94.1% on AIME 2026. This is a direct challenge to the assumption that larger parameter counts always yield better capabilities.

The model is fully open-source under Apache 2.0, available on Hugging Face and ModelScope, with weights deployable on a single 8×H100 node. It supports a 262K native context window extensible to 1M via YaRN, natively processes text, images, and video, and handles 201 languages. Both thinking and non-thinking inference modes are supported, allowing users to trade reasoning depth for latency. Qwen Code integration shipped the same week, giving developers immediate access via the CLI coding agent.

Qwen3.6-27B is strategically significant because it brings frontier-competitive coding performance within reach of enterprise self-hosting. At 27B parameters, organizations can run this model on on-premise GPU clusters without cloud API dependency — a critical requirement for regulated industries. Its 59.3% Terminal-Bench 2.0 score matches Claude Opus 4.6 directly, making it the first open-weight model to reach that tier.

**Key specs:** 262K native / 1M extended context | Text, image, video input | Free via Qwen Studio API; open weights on HuggingFace | Apache 2.0 license | Generally available since April 22, 2026

---

### 4. OpenAI Realtime Voice API — GPT-Realtime-2 Brings GPT-5-Class Reasoning to Live Voice
**Source:** [OpenAI Blog](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) | [The Decoder](https://the-decoder.com/openais-new-voice-model-brings-gpt-5-level-reasoning-to-real-time-conversations/) | [The Next Web](https://thenextweb.com/news/openai-gpt-realtime-2-voice-models)

On May 7, 2026, OpenAI released three new Realtime voice models: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper. The headline model, GPT-Realtime-2, brings GPT-5-level reasoning into live audio conversations — it can call tools mid-conversation, handle interruptions gracefully, and reason at adjustable effort levels (minimal through xhigh) while maintaining natural response cadence. Context window expanded to 128K (from 32K prior generation) and parallel tool calling is now supported.

GPT-Realtime-Translate handles end-to-end audio translation without converting to intermediate text, preserving speaker tone and emotion across 70+ input languages and 13 output languages. GPT-Realtime-Whisper provides streaming ASR that transcribes live speech as it occurs. Together, the three models cover the three core voice interaction patterns: voice-to-action, systems-to-voice, and voice-to-voice. This positions OpenAI's API as the infrastructure layer for voice-enabled agentic applications — customer service automation, real-time meeting assistance, multilingual communications.

Pricing is audio-native: GPT-Realtime-2 at $32/$64 per 1M audio input/output tokens, with a 90%+ discount for cached audio input at $0.40/1M. Translate and Whisper are priced per-minute ($0.034 and $0.017 respectively), making them cost-effective for high-volume transcription pipelines. These models are available immediately through the OpenAI API.

**Key specs:** 128K context window | Audio input/output (text also supported) | $32/$64 per 1M audio tokens (Realtime-2) | Proprietary | Available via OpenAI API

---

### 5. Claude Mythos Preview — Anthropic's Most Capable Model Withheld Due to Cybersecurity Risk
**Source:** [Built In](https://cdn.builtin.com/articles/anthropic-claude-mythos) | [Build Fast with AI](https://www.buildfastwithai.com/blogs/claude-mythos-release-date-access-2026) | [Appwrite](https://appwrite.io/blog/post/claude-mythos-preview)

Anthropic announced Claude Mythos Preview on April 7, 2026, following an accidental API leak on March 26. The model sits above the Opus tier in capability — achieving 93.9% on SWE-bench Verified (the current public leader) and 97.6% on USAMO 2026 math — but Anthropic has explicitly chosen not to release it publicly. The reason: Mythos autonomously discovered thousands of zero-day vulnerabilities across all major operating systems and browsers, including a 27-year-old OpenBSD bug and long-standing Firefox vulnerabilities, making it what Anthropic describes as "a potential existential threat to current cybersecurity software."

Instead of a public launch, Anthropic channeled Mythos into Project Glasswing, a defensive cybersecurity initiative with $100 million in model usage credits. Access is restricted to ~50 vetted organizations: AWS, Apple, Microsoft, Google, NVIDIA, CrowdStrike, the Linux Foundation, and other critical infrastructure operators. The model is being used offensively-defensively — running continuous zero-day discovery on production systems to find and patch vulnerabilities before adversaries can exploit them.

This is a landmark decision in AI safety governance: a leading lab voluntarily withholding its most capable model from commercial release. It establishes a precedent that capability evaluations should trigger deployment restrictions, not just liability disclosures. The event also sets a new public benchmark ceiling — 93.9% SWE-bench Verified — against which all public models will be compared, even though Mythos itself remains out of reach.

**Key specs:** Not publicly available | Access restricted to ~50 vetted organizations via Project Glasswing | 93.9% SWE-bench Verified, 97.6% USAMO 2026 | Proprietary, no public API or pricing

---

## Deep Dive: Most Important Release — Gemini 3.5 Flash (May 19, 2026)

Google's release of Gemini 3.5 Flash today at Google I/O 2026 is the defining model event of this news cycle because it represents the clearest bet yet by a top-3 AI lab that the next competitive frontier is not raw intelligence but agentic throughput — the ability to execute complex, multi-step workflows autonomously at scale and speed. It is the first Flash-tier model to outperform a larger flagship (Gemini 3.1 Pro) on coding and agentic benchmarks, shattering the convention that cheap/fast models must sacrifice quality.

### What It Can Do

Gemini 3.5 Flash processes multi-turn agentic tasks with a 1M token context window, sustaining coherent plan-execute cycles across hours-long workflows without losing context. It orchestrates parallel subagents via the Antigravity harness, enabling divide-and-conquer on large codebases, financial documents, and research projects. Its multimodal understanding covers text, images, video, and audio — it can generate interactive web UIs, analyze complex invoices, and reason over 100+ page documents in a single pass. On coding, it achieved 76.2% on Terminal-Bench 2.1, 55.1% on SWE-Bench Pro, and 83.6% on MCP Atlas (multi-step tool-calling workflows). At 280+ output tokens per second, it is the fastest frontier-quality model available today.

### Benchmark Highlights

| Benchmark | Gemini 3.5 Flash | Previous Best |
|---|---|---|
| Terminal-Bench 2.1 | 76.2% | Gemini 3.1 Pro (prior holder) |
| GDPval-AA (Elo) | 1656 | Gemini 3.1 Pro |
| MCP Atlas | 83.6% | Gemini 3.1 Pro |
| SWE-Bench Pro | 55.1% | Claude Opus 4.7 (64.3%) |
| OSWorld-Verified (computer use) | 78.4% | GPT-5.5 (78.7%) |
| CharXiv Reasoning (multimodal) | 84.2% | Prior Gemini |
| MMMU-Pro (multimodal) | 83.6% | Competitive with Gemini 3.1 Pro |
| Output tokens/sec | 280+ | ~70 (comparable frontier models) |

### Architecture (known)

Gemini 3.5 Flash is a multimodal Transformer trained natively on text, images, audio, and video. Google has not published a model card or architecture paper for 3.5 Flash as of today's announcement, but it continues the Gemini 3.x lineage with Antigravity integration for multi-agent coordination. The model uses an extended thinking mode (default "medium" effort rather than "high" as in previous Flash generations) to balance quality, latency, and cost. The 90% cache discount on input tokens signals optimized KV-cache architecture for long-context agentic loops.

### Pricing & Availability

- **Standard pricing:** $1.50 per 1M input tokens / $9.00 per 1M output tokens
- **Cached input:** 90% discount (≈$0.15 per 1M cached tokens)
- **3x cost increase** over Gemini 3 Flash ($0.50/$3.00), reflecting the quality jump
- **Context window:** 1M tokens input / 65K max output
- **API model ID:** `gemini-3.5-flash`
- **Available immediately:** Gemini API, Google AI Studio, Android Studio, Gemini Enterprise Agent Platform, Gemini Enterprise, Gemini app (global default), AI Mode in Search

### Strategic Significance

The timing — Google I/O 2026, the company's flagship developer conference — sends an unmistakable signal: Google is repositioning itself as the infrastructure provider for agentic AI, not just a competitive chatbot. By making 3.5 Flash the default in the Gemini app, AI Mode in Search, and enterprise platforms simultaneously, Google is ensuring that its most capable agentic model is also its most widely deployed. The Antigravity 2.0 desktop application, also announced today, creates a developer ecosystem built around agent-first workflows with 3.5 Flash as the engine.

The cost story is equally significant. Google claims 3.5 Flash can complete tasks "at less than half the cost of other frontier models" for long-horizon agentic work — partly due to its speed (fewer wall-clock seconds of API time) and partly due to more efficient token usage in multi-turn contexts. Shopify and Ramp are already in production, and Macquarie Bank and Xero are in pilots, validating enterprise readiness at launch.

The strategic gap between 3.5 Flash and 3.5 Pro is deliberate: Pro is positioned as the orchestrator model for the highest-stakes enterprise workflows, while Flash serves as the workhorse subagent. This mirrors the OpenAI o3/GPT-5.5 dual-tier approach and establishes that the future production architecture is a two-tier agent stack: a heavy thinker for planning, a fast executor for action.

### Competitive Context

Gemini 3.5 Flash's 76.2% Terminal-Bench 2.1 score places it above GPT-5.5 (82.7% on Terminal-Bench 2.0, different version) but direct comparison is complicated by benchmark version differences. On GDPval-AA (1656 Elo) it trails GPT-5.5's GDPval score of 84.9% (different scale). OSWorld-Verified computer use (78.4%) is nearly identical to GPT-5.5's 78.7%. The clearest competitive advantage is speed: at 280 tokens/sec it is approximately 4x faster than GPT-5.5 or Claude Opus 4.x at comparable quality, making it the default choice for cost-sensitive agentic deployments where throughput matters more than peak accuracy.

---

## Benchmark Comparison Data

```json
{"benchmark": "SWE-bench Verified", "results": [{"model": "Claude Mythos Preview", "score": 0.939}, {"model": "Claude Opus 4.7", "score": 0.876}, {"model": "GPT-5.3-Codex", "score": 0.850}, {"model": "Qwen3.6-27B", "score": 0.772}, {"model": "DeepSeek V4 Pro Max", "score": 0.806}, {"model": "Gemini 3.1 Pro", "score": 0.806}, {"model": "Kimi K2.6", "score": 0.802}, {"model": "MiniMax M2.5", "score": 0.802}, {"model": "GPT-5.2", "score": 0.800}]}
```

```json
{"benchmark": "SWE-bench Pro", "results": [{"model": "Claude Opus 4.7", "score": 0.643}, {"model": "Gemini 3.5 Flash", "score": 0.551}, {"model": "Qwen3.6-27B", "score": 0.535}, {"model": "Qwen3.5-397B-A17B", "score": 0.509}]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [{"model": "GPT-5.5", "score": 0.827}, {"model": "Qwen3.6-27B", "score": 0.593}, {"model": "Claude Opus 4.6", "score": 0.593}]}
```

```json
{"benchmark": "Terminal-Bench 2.1", "results": [{"model": "Gemini 3.5 Flash", "score": 0.762}]}
```

```json
{"benchmark": "GDPval", "results": [{"model": "GPT-5.5", "score": 0.849}]}
```

```json
{"benchmark": "GDPval-AA (Elo)", "results": [{"model": "Gemini 3.5 Flash", "score": 1656}]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [{"model": "GPT-5.5", "score": 0.85}, {"model": "Gemini 3.1 Deep Think", "score": 0.846}, {"model": "GPT-5.4 Pro", "score": 0.83}, {"model": "Gemini 3.1 Pro", "score": 0.771}, {"model": "Claude Opus 4.6", "score": 0.69}, {"model": "Grok 4", "score": 0.16}, {"model": "DeepSeek V3.2", "score": 0.04}]}
```

```json
{"benchmark": "GPQA Diamond", "results": [{"model": "Gemini 3.1 Pro", "score": 0.943}, {"model": "Claude Opus 4.7 Adaptive", "score": 0.942}, {"model": "GPT-5.5", "score": 0.936}, {"model": "GPT-5.4", "score": 0.885}, {"model": "Claude Opus 4.6", "score": 0.884}, {"model": "Qwen3.6-27B", "score": 0.878}]}
```

```json
{"benchmark": "AIME 2026", "results": [{"model": "Qwen3.6-27B", "score": 0.941}]}
```

```json
{"benchmark": "LiveCodeBench", "results": [{"model": "DeepSeek-V4-Pro (Max)", "score": 0.935}, {"model": "Gemini 3.0 Pro Preview", "score": 0.920}, {"model": "DeepSeek-V4-Flash (Max)", "score": 0.916}, {"model": "Gemini 3.1 Pro Preview", "score": 0.917}, {"model": "DeepSeek-V4-Pro (High)", "score": 0.898}, {"model": "Kimi K2.6", "score": 0.896}]}
```

```json
{"benchmark": "LMSys Arena Overall ELO (April 2026)", "results": [{"model": "Claude Opus 4.6 Thinking", "score": 1504}, {"model": "Gemini 3.1 Pro Preview", "score": 1493}, {"model": "GPT-5.4 High", "score": 1484}, {"model": "Grok 4.20", "score": 1471}, {"model": "DeepSeek V4 Pro", "score": 1462}, {"model": "Claude Sonnet 4.6", "score": 1458}, {"model": "GPT-5.4 Standard", "score": 1455}, {"model": "Gemini 3.0 Pro", "score": 1449}, {"model": "Qwen 3.6-Plus", "score": 1447}, {"model": "Meta Muse Spark", "score": 1441}]}
```

```json
{"benchmark": "OSWorld-Verified (computer use)", "results": [{"model": "GPT-5.5", "score": 0.787}, {"model": "Gemini 3.5 Flash", "score": 0.784}]}
```

```json
{"benchmark": "MCP Atlas (multi-step workflows)", "results": [{"model": "Gemini 3.5 Flash", "score": 0.836}]}
```

```json
{"benchmark": "CharXiv Reasoning (multimodal)", "results": [{"model": "Gemini 3.5 Flash", "score": 0.842}]}
```

```json
{"benchmark": "BrowseComp", "results": [{"model": "GPT-5.5", "score": 0.844}]}
```

```json
{"benchmark": "FrontierMath Tier 1-3", "results": [{"model": "GPT-5.5", "score": 0.517}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Gemini 3.5 Flash | Google | 1M tokens | $1.50 | $9.00 | Text, Image, Video, Audio |
| GPT-5.5 Instant | OpenAI | 400K tokens | $5.00 | $30.00 | Text, Image |
| GPT-5.5 | OpenAI | 1M tokens | $5.00 (≤272K) / $10.00 (>272K) | $30.00 / $45.00 | Text, Image, Computer Use |
| GPT-5.4 | OpenAI | 1M tokens | $2.50 | $15.00 | Text, Image |
| Claude Opus 4.7 | Anthropic | 1M tokens (beta) | $5.00 | $25.00 | Text, Image |
| Claude Opus 4.6 | Anthropic | 1M tokens | $5.00 | $25.00 | Text, Image |
| Claude Sonnet 4.6 | Anthropic | 1M tokens | $3.00 | $15.00 | Text, Image |
| Gemini 3.1 Pro | Google | 1M tokens | $2.00 | $12.00 | Text, Image, Video, Audio |
| Gemini 3.1 Flash-Lite | Google | 1M tokens | $0.25 | $1.50 | Text, Image |
| DeepSeek V4 Pro | DeepSeek | 1M tokens | $1.74 | $3.48 | Text, Image |
| DeepSeek V4 Flash | DeepSeek | 1M tokens | ~$0.27 | ~$1.10 | Text, Image |
| Qwen3.6-27B | Alibaba | 262K / 1M (YaRN) | Open weights / Qwen Studio API | — | Text, Image, Video |
| GPT-Realtime-2 | OpenAI | 128K tokens | $32.00 (audio) | $64.00 (audio) | Audio, Text |
| Kimi K2.6 | Moonshot AI | 1M tokens | ~$0.60 | ~$2.50 | Text, Image |
| Meta Muse Spark | Meta | 512K tokens | — (API pricing TBD) | — | Text, Image |

---

## Analysis & Impact

- **For software engineering / coding:** Gemini 3.5 Flash at 76.2% Terminal-Bench 2.1 and Qwen3.6-27B at 77.2% SWE-bench Verified now offer frontier coding quality at substantially lower cost than Claude Opus 4.7 ($5/$25) — teams building autonomous coding pipelines should benchmark 3.5 Flash at $1.50/$9.00 before defaulting to Anthropic or OpenAI flagship models, as the 4x speed advantage compounds significantly in agentic loops with dozens of API calls.

- **For frontier reasoning / math / science:** The ARC-AGI-2 leaderboard now shows GPT-5.5 at 85% and Gemini 3.1 Deep Think at 84.6% — both above the 66% human average — representing genuine progress in fluid intelligence. For PhD-level scientific reasoning, GPQA Diamond is near-saturated at the top (Gemini 3.1 Pro 94.3%, Claude Opus 4.7 94.2%, GPT-5.5 93.6%), meaning GPQA Diamond alone is no longer sufficient to differentiate frontier models; FrontierMath and USAMO-class benchmarks are needed for discrimination.

- **For multimodal / video / audio work:** OpenAI's GPT-Realtime-2 (128K context, adjustable reasoning effort, parallel tool calling) now makes real-time voice-reasoning pipelines production-viable; GPT-Realtime-Translate covers 70+ languages end-to-end without text intermediation. Gemini 3.5 Flash's 84.2% CharXiv Reasoning and 83.6% MMMU-Pro make it the leading model for visual document understanding at Flash-tier pricing.

- **For cost-sensitive or open-source deployments:** Qwen3.6-27B under Apache 2.0 is the clearest efficiency breakthrough of the month — 77.2% SWE-bench Verified from a 27B dense model that runs on a single 8×H100 node rivals proprietary APIs at zero per-token cost. DeepSeek V4 Pro ($1.74/$3.48, MIT license, 93.5% LiveCodeBench) remains the best open-weight model for pure coding throughput, making Chinese open-source labs collectively the cost-performance leaders in the open ecosystem.

- **The agent-first architecture is now table stakes:** Every major lab announcement this cycle — Gemini 3.5 Flash with Antigravity, GPT-5.5 with computer use, OpenAI Realtime with tool-calling voice, Qwen3.6 with Qwen Code — is framed around agentic workflows, not chatbot quality. The question is no longer whether a model can reason, but whether it can execute: long-horizon task completion, subagent coordination, and multi-tool orchestration are now the primary differentiators at the frontier.

---

## Key Takeaways (TL;DR)

- Gemini 3.5 Flash launches today at Google I/O with 280+ tokens/sec throughput, surpassing Gemini 3.1 Pro on Terminal-Bench 2.1 (76.2%), MCP Atlas (83.6%), and OSWorld-Verified (78.4%) at $1.50/$9.00 per 1M tokens.
- GPT-5.5 Instant (May 5) cut hallucinated claims by 52.5% and reduces inaccurate responses by 37.3% over GPT-5.3 Instant, now serving as the default model for hundreds of millions of ChatGPT users.
- Qwen3.6-27B (Apache 2.0) outperforms the 15x-larger Qwen3.5-397B-A17B on all coding benchmarks with 77.2% SWE-bench Verified and 94.1% AIME 2026 from a 27B dense model.
- Claude Mythos Preview achieves 93.9% SWE-bench Verified and 97.6% USAMO 2026 — the highest scores recorded — but Anthropic withheld it from public release due to autonomous zero-day vulnerability discovery capabilities.
- ARC-AGI-2's top tier (GPT-5.5 85%, Gemini 3.1 Deep Think 84.6%) has crossed the human average of 66% for the first time, marking a genuine milestone in fluid reasoning benchmarks.

---

*Sources:*
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/
- https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/
- https://www.neowin.net/news/google-announces-gemini-35-flash-its-strongest-coding-model-yet/
- https://www.moneycontrol.com/technology/google-announces-gemini-3-5-update-with-agentic-ai-features-coding-upgrades-and-faster-performance-article-13924397.html
- https://timesofindia.indiatimes.com/technology/tech-news/google-i/o-2026-googles-most-powerful-model-to-date-gemini-flash-3-5-launched/articleshow/131209296.cms
- https://deepmind.google/en/models/gemini/flash/
- https://dev.to/googleai/gemini-35-flash-developer-guide-1i46
- https://www.linkedin.com/pulse/google-has-released-gemini-35-flash-artificial-analysis-nvbjc
- https://openai.com/index/gpt-5-5-instant/
- https://www.llmreference.com/model/gpt-5.5-instant
- https://llm-stats.com/models/gpt-5.5-instant
- https://developers.openai.com/api/docs/models/gpt-5.5
- https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- https://the-decoder.com/openais-new-voice-model-brings-gpt-5-level-reasoning-to-real-time-conversations/
- https://thenextweb.com/news/openai-gpt-realtime-2-voice-models
- https://www.alibabacloud.com/blog/qwen3-6-27b-flagship-level-coding-in-a-27b-dense-model_603063
- https://github.com/QwenLM/Qwen3.6/blob/main/README.md
- https://benchlm.ai/models/qwen3-6-27b
- https://toknow.ai/posts/qwen36-deepseek-v4-china-open-weight-frontier-models/
- https://cdn.builtin.com/articles/anthropic-claude-mythos
- https://www.buildfastwithai.com/blogs/claude-mythos-release-date-access-2026
- https://appwrite.io/blog/post/claude-mythos-preview
- https://awesomeagents.ai/models/claude-mythos-preview/
- https://deepseekai.guide/models/deepseek-v4-pro/
- https://felloai.com/deepseek-v4/
- https://www.swfte.com/blog/lmsys-arena-leaderboard-may-2026
- https://llm-registry.com/benchmark/arc-agi-2
- https://agentmarketcap.ai/blog/2026/04/08/arc-agi-2-leaderboard-2026-gemini-abstract-reasoning-benchmark
- https://llm-registry.com/benchmark/gpqa-diamond
- https://benchlm.ai/benchmarks/gpqaDiamond
- https://www.marc0.dev/en/leaderboard
- https://benchlm.ai/benchmarks/sweVerified
- https://llm-registry.com/benchmark/livecodebench-v6
- https://benchlm.ai/benchmarks/liveCodeBench
- https://www.scriptbyai.com/gpt-gemini-claude-pricing/
- https://aicostcheck.com/pricing
- https://www.clawrouters.com/blog/llm-api-pricing-guide-2026
