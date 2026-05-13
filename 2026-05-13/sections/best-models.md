# Best Models & Benchmarks — 2026-05-13

## Top Model News (3-5)

### 1. GPT-5.5 Instant — OpenAI's New Default ChatGPT Model with Massive Hallucination Reduction
**Source:** [OpenAI Blog](https://openai.com/index/gpt-5-5-instant/) | [TechCrunch](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/) | [System Card](https://openai.com/index/gpt-5-5-instant-system-card/)

Released on May 5, 2026, GPT-5.5 Instant is now the default ChatGPT model for all users. It delivers the most significant hallucination reduction of any OpenAI model to date: 52.5% fewer hallucinated claims on high-stakes prompts in medicine, law, and finance compared to its predecessor GPT-5.3 Instant. The model also shows a 37.3% reduction in factual inaccuracies on challenging multi-turn conversations — directly addressing one of the most persistent pain points of large language models.

Beyond accuracy, GPT-5.5 Instant extends the context window to 1,050,000 tokens (over 1 million) and notably scores 81.2 on AIME 2025 (vs. 65.4 for its predecessor) and 76 on MMMU-Pro multimodal reasoning (vs. 69.2). It is the first Instant-tier model classified as "High Capability" in OpenAI's cybersecurity and biological/chemical preparedness risk categories, signaling its step-up in frontier power. The model supports web search, file search, code interpreter, computer use, streaming, function calling, and structured outputs.

GPT-5.5 Instant also earns a top-3 spot on SWE-bench Verified at 88.7%, edging out Claude Opus 4.7 (87.6%) and GPT-5.3-Codex (85.0%) — the first time a general-purpose conversational model has topped the coding leaderboard. This makes it the single model that most broadly advances the frontier across accuracy, reasoning, coding, and multimodal capability in early May 2026.

**Key specs:** 1,050,000-token context window | Text + image input | $5.00/$30.00 per 1M input/output tokens | Proprietary | Generally available via ChatGPT (default) and API (`chat-latest`)

---

### 2. OpenAI GPT-Realtime-2 + Voice Suite — Real-Time Voice Intelligence with GPT-5-Class Reasoning
**Source:** [OpenAI Blog](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) | [The Next Web](https://thenextweb.com/news/openai-gpt-realtime-2-voice-models) | [AI News](https://news.smol.ai/issues/26-05-07-gpt-realtime-2/)

On May 7, 2026, OpenAI released a three-model voice suite that fundamentally upgrades real-time audio intelligence. GPT-Realtime-2 is the flagship: it brings GPT-5-class reasoning into voice interactions, supports a 128K context window (quadrupling the prior 32K), and allows configurable reasoning effort levels from minimal to xhigh — enabling developers to tradeoff cost and accuracy based on task complexity. The model supports text, audio, and image inputs with speech-to-speech output.

Benchmark results are compelling. GPT-Realtime-2 scores 96.6% on Big Bench Audio in High mode (vs. 81.4% for GPT-Realtime-1.5 — a +15.2pp gain) and 48.5% on Audio MultiChallenge in Xhigh mode (vs. 34.7% — a +13.8pp gain). Real-world deployment data reinforces these numbers: Zillow reports a 26-point lift in call success rate (69% → 95%), and BolnaAI achieved 12.5% lower word error rates on Hindi, Tamil, and Telugu — highlighting the model's multilinguality.

The companion models complete a full voice stack: GPT-Realtime-Translate enables live translation across 70+ input languages to 13 output languages at $0.034/minute; GPT-Realtime-Whisper provides streaming speech-to-text at $0.017/minute for low-latency transcription pipelines. Together, these three models give developers a complete real-time audio infrastructure built on frontier intelligence.

**Key specs:** 128K context window | Audio + text + image input, speech output | GPT-Realtime-2: $32/$64 per 1M audio input/output tokens | Translate: $0.034/min | Whisper: $0.017/min | Proprietary | Available via OpenAI API

---

### 3. Anthropic Claude for Small Business — 15 Agentic Workflows Integrated Into SMB Tools
**Source:** [Anthropic Blog](https://www.anthropic.com/news/claude-for-small-business) | [Rolling Out](https://rollingout.com/2026/05/13/claude-for-small-business-15-new/) | [Crypto Briefing](https://cryptobriefing.com/claude-for-small-business-ai-integration/)

Launched on May 13, 2026, Claude for Small Business is Anthropic's bid to bring its most capable AI infrastructure to the 44% of U.S. GDP accounted for by small and mid-size businesses. Rather than releasing a new model, Anthropic has bundled Claude's existing capabilities — running on Claude Opus 4.7 — into 15 pre-built agentic workflows across finance, operations, sales, marketing, HR, and customer service. These workflows install as a toggle inside Claude Cowork and require no additional charge beyond existing Claude licenses and partner tool subscriptions.

The integration footprint is substantial: QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365, Slack, Square, Stripe, and Webflow. Representative workflows include forecasting cash position, reconciling monthly books, running sales campaigns, chasing invoices, analyzing margins, and reviewing contracts. A partnership with PayPal adds an "AI Fluency for Small Business" education course, and Anthropic is launching a 10-city SMB Tour starting May 14 in Chicago — an unusually aggressive go-to-market for an AI lab.

While not a model release, this is a significant deployment milestone. It marks the moment frontier AI (Opus 4.7 quality) becomes turnkey for non-technical users, removing the integration burden that has historically kept SMBs from capturing AI value. It also signals Anthropic's vertical bundling strategy: competing on workflow productivity rather than raw benchmark numbers, creating stickiness that API-only providers cannot easily replicate.

**Key specs:** Powered by Claude Opus 4.7 | 1M context window | Text + vision | $5/$25 per 1M input/output tokens (underlying model) | Proprietary | Available via Claude Cowork (May 13, 2026)

---

### 4. Google DeepMind Magic Pointer — AI-Native Cursor Powered by Gemini Comes to Chrome
**Source:** [Google DeepMind Blog](https://deepmind.google/blog/ai-pointer/) | [9to5Google](https://9to5google.com/2026/05/12/deepmind-googlebook-magic-pointer/) | [MarkTechPost](https://www.marktechpost.com/2026/05/13/google-deepmind-introduces-an-ai-enabled-mouse-pointer-powered-by-gemini-that-captures-visual-and-semantic-context-around-the-cursor/)

Announced on May 12–13, 2026, Google DeepMind's Magic Pointer is the most interface-level AI innovation since the launch of multi-modal chatbots. It reimagines the mouse cursor as a Gemini-powered semantic agent: rather than tracking only pixel coordinates, it continuously captures visual and semantic context around the cursor, understanding not just _where_ the user points but _what_ they mean. Hovering over a PDF, a table, a date, or a video frame automatically registers that element as an addressable semantic object.

The design philosophy — articulated as four principles: "Maintain the flow," "Show and tell," "This and That," and "Pixels into entities" — eliminates the need for users to copy-paste, retype, or context-switch into a separate AI window. Users can say "Fix this" while hovering over broken code, "Turn this into a chart" while hovering over statistics, or "Book this place" while pausing a travel video, and Gemini acts on those implicit references. Interactive demos are live in Google AI Studio for image editing and map-finding tasks.

Magic Pointer is rolling out to Gemini in Chrome and to the new Googlebook laptops. This is not a standalone model release but a new interaction modality layered on top of Gemini 3.1, and it represents Google's clearest statement yet about how AI should be embedded in the operating system layer rather than accessed as a separate application. The downstream implications for accessibility and professional productivity workflows are substantial.

**Key specs:** Powered by Gemini 3.1 | Visual + semantic cursor context | No separate pricing (Chrome / Googlebook integration) | Proprietary | Demo live in Google AI Studio; Chrome and Googlebook rollout May 2026

---

### 5. GPT-5.5 Tops ARC-AGI-2 at 85% — Abstract Reasoning Now Exceeds Human Baseline
**Source:** [ARC Prize Leaderboard](https://arcprize.org/leaderboard) | [BenchLM](https://benchlm.ai/benchmarks/arcAgi2) | [Agent Market Cap](https://agentmarketcap.ai/blog/2026/04/08/arc-agi-2-leaderboard-2026-gemini-abstract-reasoning-benchmark)

The ARC-AGI-2 leaderboard has crossed a symbolic threshold as of May 2026: GPT-5.5 has reached 85%, surpassing the average human baseline of 66% by 19 percentage points and marking the first time a broadly available AI system definitively exceeds human performance on this benchmark of fluid abstract reasoning. GPT-5.4 Pro sits at 83.3%, Gemini 3.1 Pro at 77.1%, and Claude Opus 4.7 at 75.8%. The four leading models are clustered within a 9.2-point band, suggesting convergent progress at the abstract reasoning frontier.

ARC-AGI-2 measures genuine generalization from sparse examples using novel visual grid puzzles that cannot be solved through pattern memorization. Earlier this year, Gemini 3.1 Deep Think reached 84.6% but at a cost of ~$77 per task — cost-prohibitive for production use. GPT-5.5's 85% at standard model pricing represents a breakthrough in economically viable abstract reasoning. The gap below the top tier remains dramatic: Grok 4 scores 15.9%, DeepSeek V3.2 at 4%, and Llama 4 / Qwen 3 at near-zero.

This result matters beyond the benchmark. ARC-AGI-2 was designed specifically to resist the kind of statistical interpolation that inflates scores on saturated benchmarks like MMLU. GPT-5.5 at 85% is the strongest evidence yet that frontier models are developing genuine compositional generalization — a capability that directly enables harder planning, tool-use, and novel problem-solving in agentic deployments.

**Key specs:** GPT-5.5 | $5/$30 per 1M input/output tokens | 1,050,000-token context | Proprietary | Available via ChatGPT and OpenAI API

---

## Deep Dive: Most Important Release — GPT-5.5 Instant (May 5, 2026)

GPT-5.5 Instant is the defining model event of this week because it simultaneously advances in accuracy, reasoning, coding, abstract reasoning, and multimodality — and it does so as the default ChatGPT model, meaning these improvements are immediately in the hands of hundreds of millions of users. Where previous model releases improved one or two dimensions, GPT-5.5 Instant tops SWE-bench Verified (88.7%), exceeds the human ARC-AGI-2 baseline (85%), posts the largest hallucination reduction of any OpenAI release (52.5%), and extends the context window to over 1 million tokens. It is the first time an OpenAI general-purpose model — not a specialized Codex variant — leads the coding leaderboard.

### What It Can Do

GPT-5.5 Instant processes text and images in a 1,050,000-token context window, enabling in-context analysis of book-length documents, code repositories, and multi-document research tasks. Its hallucination reduction (52.5% on high-stakes medicine/law/finance queries) makes it materially more deployable for regulated-industry applications. On ARC-AGI-2, it scores 85%, exceeding human average (66%) and demonstrating fluid abstract reasoning. For coding, it achieves 88.7% on SWE-bench Verified — outperforming specialized Codex variants — and 82.7% on Terminal-Bench 2.0, the highest of any model. It supports parallel tool calls, structured outputs, computer use, code interpreter, and web search, making it a complete agentic backbone.

### Benchmark Highlights

| Benchmark | GPT-5.5 Instant | Previous Best |
|---|---|---|
| SWE-bench Verified | 88.7% | Claude Opus 4.7 — 87.6% |
| ARC-AGI-2 | 85.0% | GPT-5.4 Pro — 83.3% |
| Terminal-Bench 2.0 | 82.7% | Claude Mythos Preview — 82.0% |
| GPQA Diamond | 93.6% | Gemini 3.1 Pro — 94.3% |
| AIME 2025 | 81.2 | GPT-5.3 Instant — 65.4 |
| MMMU-Pro | 76.0 | GPT-5.3 Instant — 69.2 |
| LMSys Arena Overall ELO | ~1490 | Claude Opus 4.6 Thinking — 1504 |
| Hallucination (high-stakes) | 52.5% reduction vs. predecessor | — |

### Architecture (known)

OpenAI has not publicly disclosed the detailed architecture of GPT-5.5 Instant. Based on the system card and deployment safety hub, it is a dense transformer trained with reinforcement learning from human feedback (RLHF) and classified as "High Capability" in cybersecurity and bio/chem preparedness risk categories — the first Instant-tier model to receive this classification. The 1,050,000-token context window suggests advances in attention efficiency or key-value cache management over previous Instant models. No MoE or SSM disclosures have been made.

### Pricing & Availability

- **Standard API:** $5.00 / 1M input tokens, $30.00 / 1M output tokens
- **Context window:** 1,050,000 tokens input; 128,000 max output tokens
- **Knowledge cutoff:** December 1, 2025
- **API identifier:** `gpt-5.5-instant`, also accessible via `chat-latest` alias
- **ChatGPT:** Default model for all users (Free, Plus, Pro, Team, Enterprise tiers)
- **Modalities:** Text + image input; text output
- **Features:** Web search, file search, code interpreter, computer use, streaming, function calling, structured outputs

### Strategic Significance

GPT-5.5 Instant's release at the top of every major benchmark — while serving as the default model for all ChatGPT users — is the clearest example yet of OpenAI closing the gap between frontier lab research and mass-market deployment. Historically, the most capable models were gated behind premium APIs or restricted access programs. GPT-5.5 Instant makes 88.7% SWE-bench performance and human-surpassing ARC-AGI-2 reasoning available to any ChatGPT user without additional cost.

The 52.5% hallucination reduction on high-stakes domains is strategically significant beyond the benchmark: it directly addresses the regulatory and liability concerns that have slowed AI adoption in healthcare, legal, and financial services. Combined with the "High Capability" safety classification and Trusted Access for Cyber variant (released simultaneously), this positions GPT-5.5 as OpenAI's entry point into regulated enterprise markets where accuracy guarantees matter.

Finally, the fact that a general-purpose model now leads the SWE-bench coding leaderboard — ahead of specialized Codex variants — signals that the era of task-specific model specialization may be plateauing. GPT-5.5 Instant suggests that general reasoning trained at sufficient scale now encompasses coding ability, not the other way around.

### Competitive Context

GPT-5.5 Instant leads SWE-bench Verified at 88.7% compared to Claude Opus 4.7 at 87.6% (a 1.1pp gap) and Claude Mythos Preview at 93.9% (restricted to 52 vetted partners — not publicly available). On ARC-AGI-2, GPT-5.5's 85% exceeds Gemini 3.1 Pro (77.1%) and Claude Opus 4.7 (75.8%) by 8-9 points. On Terminal-Bench 2.0, GPT-5.5 (82.7%) marginally edges Claude Mythos Preview (82.0%) and leads GPT-5.3-Codex (77.3%) by 5.4pp. In LMSys Arena, GPT-5.5 is estimated at ~1490 ELO, trailing Claude Opus 4.6 Thinking (1504 ELO) — meaning it does not yet lead on human preference scores, even while topping objective benchmarks. DeepSeek V4 Pro remains the open-weight leader at 80.6% SWE-bench Verified, still 8.1 points behind GPT-5.5.

---

## Benchmark Comparison Data

```json
{"benchmark": "SWE-bench Verified", "results": [{"model": "Claude Mythos Preview", "score": 93.9}, {"model": "GPT-5.5 Instant", "score": 88.7}, {"model": "Claude Opus 4.7", "score": 87.6}, {"model": "GPT-5.3-Codex", "score": 85.0}, {"model": "DeepSeek V4 Pro", "score": 80.6}, {"model": "Gemini 3.1 Pro", "score": 80.6}, {"model": "Kimi K2.6", "score": 80.2}, {"model": "MiniMax M2.5", "score": 80.2}, {"model": "Claude Sonnet 4.6", "score": 79.6}, {"model": "Qwen 3.6 Plus", "score": 78.8}, {"model": "Mistral Medium 3.5", "score": 77.6}]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [{"model": "GPT-5.5", "score": 85.0}, {"model": "GPT-5.4 Pro", "score": 83.3}, {"model": "Gemini 3.1 Deep Think", "score": 84.6}, {"model": "Gemini 3.1 Pro", "score": 77.1}, {"model": "Claude Opus 4.7", "score": 75.8}, {"model": "Grok 4.20", "score": 16.0}, {"model": "DeepSeek V3.2", "score": 4.0}, {"model": "Qwen 3", "score": 1.0}, {"model": "Llama 4 Maverick", "score": 0.0}, {"model": "Human Average", "score": 66.0}]}
```

```json
{"benchmark": "GPQA Diamond", "results": [{"model": "Gemini 3.1 Pro", "score": 94.3}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 94.2}, {"model": "GPT-5.5", "score": 93.6}, {"model": "GPT-5.4", "score": 92.8}, {"model": "Moonshot AI", "score": 90.5}, {"model": "DeepSeek V4 Pro", "score": 90.1}, {"model": "Qwen 3.6 Plus", "score": 88.2}, {"model": "Grok 4.20", "score": 88.4}]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [{"model": "GPT-5.5", "score": 82.7}, {"model": "Claude Mythos Preview", "score": 82.0}, {"model": "GPT-5.3-Codex", "score": 77.3}, {"model": "Qwen 3.6 Plus", "score": 61.6}, {"model": "GPT-5.3-Codex-Spark", "score": 58.4}, {"model": "GPT-5.1-Codex-mini", "score": 46.1}]}
```

```json
{"benchmark": "LiveCodeBench", "results": [{"model": "DeepSeek V4 Pro (Max)", "score": 93.5}, {"model": "DeepSeek V4 Flash (Max)", "score": 91.6}, {"model": "Gemini 3 Pro Preview", "score": 91.7}, {"model": "Gemini 3 Flash Preview Thinking", "score": 90.8}, {"model": "DeepSeek V4 Pro (High)", "score": 89.8}, {"model": "Grok 4.20", "score": 79.0}]}
```

```json
{"benchmark": "LMSys Chatbot Arena Overall ELO", "results": [{"model": "Claude Opus 4.6 Thinking", "score": 1504}, {"model": "Gemini 3.1 Pro Preview", "score": 1493}, {"model": "GPT-5.4 High", "score": 1484}, {"model": "Grok 4.20", "score": 1471}, {"model": "DeepSeek V4 Pro", "score": 1462}, {"model": "Claude Sonnet 4.6", "score": 1458}, {"model": "GPT-5.4 Standard", "score": 1455}, {"model": "Gemini 3.0 Pro", "score": 1449}, {"model": "Qwen 3.6-Plus", "score": 1447}, {"model": "Meta Muse Spark", "score": 1441}]}
```

```json
{"benchmark": "AIME 2025", "results": [{"model": "Grok 4 Heavy", "score": 100.0}, {"model": "Grok 4 Standard", "score": 91.7}, {"model": "GPT-5.5 Instant", "score": 81.2}, {"model": "GPT-5.3 Instant", "score": 65.4}]}
```

```json
{"benchmark": "MMMU-Pro (Multimodal)", "results": [{"model": "Gemini 3.1 Pro Preview", "score": 82.4}, {"model": "Meta Muse Spark", "score": 80.5}, {"model": "GPT-5.5 Instant", "score": 76.0}, {"model": "GPT-5.3 Instant", "score": 69.2}]}
```

```json
{"benchmark": "Big Bench Audio", "results": [{"model": "GPT-Realtime-2 (High)", "score": 96.6}, {"model": "GPT-Realtime-1.5", "score": 81.4}]}
```

```json
{"benchmark": "Audio MultiChallenge", "results": [{"model": "GPT-Realtime-2 (Xhigh)", "score": 48.5}, {"model": "GPT-Realtime-1.5", "score": 34.7}]}
```

```json
{"benchmark": "Humanity's Last Exam (HLE)", "results": [{"model": "Grok 4 Heavy", "score": 50.0}, {"model": "Gemini 3.1 Pro Preview", "score": 44.7}, {"model": "GPT-5.4", "score": 41.6}, {"model": "Meta Muse Spark (Contemplating)", "score": 58.0}, {"model": "Meta Muse Spark (Standard)", "score": 39.9}]}
```

```json
{"benchmark": "Artificial Analysis Intelligence Index", "results": [{"model": "Grok 4.3", "score": 53.2}, {"model": "Meta Muse Spark", "score": 52.0}, {"model": "Gemini 3.1 Pro Preview", "score": 51.5}, {"model": "GPT-5.4", "score": 51.0}, {"model": "Claude Opus 4.6", "score": 49.5}, {"model": "Ling 2.6 Flash", "score": 26.0}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| GPT-5.5 Instant | OpenAI | 1,050,000 tokens | $5.00 | $30.00 | Text, Image |
| GPT-5.4 | OpenAI | 400K+ tokens | $2.50 | $15.00 | Text, Image |
| GPT-Realtime-2 | OpenAI | 128,000 tokens | $32.00 (audio) | $64.00 (audio) | Audio, Text, Image |
| Claude Opus 4.7 | Anthropic | 1,000,000 tokens | $5.00 | $25.00 | Text, Image, Video |
| Claude Sonnet 4.6 | Anthropic | 1,000,000 tokens | $3.00 | $15.00 | Text, Image |
| Gemini 3.1 Pro Preview | Google | 2,000,000 tokens | $3.50 | $10.50 | Text, Image, Audio, Video, Code |
| Grok 4.20 | xAI | 256,000 tokens (API) / 1M (app) | $3.00 | $15.00 | Text, Image |
| DeepSeek V4 Pro | DeepSeek | 1,000,000 tokens | $1.74 | $3.48 | Text, Image (open weights, MIT) |
| Qwen 3.6 Plus | Alibaba | 1,000,000 tokens | $0.33–$0.50 | $1.95–$3.00 | Text, Image, Video |
| Meta Muse Spark | Meta | Not disclosed | Not public | Not public | Text, Image, Voice |
| Mistral Medium 3.5 | Mistral | 128,000 tokens | ~$0.40 | ~$2.00 | Text |
| Perceptron Mk1 | Perceptron | 32,000 tokens | $0.15 | $1.50 | Video, Image, Text |
| GPT-5.3-Codex-Spark | OpenAI | 256,000 tokens | Not disclosed | Not disclosed | Text (>1,000 tok/s) |
| Llama 4 Scout | Meta | 10,000,000 tokens | Open weight | Open weight | Text, Image (Apache 2.0) |
| DeepSeek V4 Flash | DeepSeek | 1,000,000 tokens | $0.87 | $1.74 | Text, Image (open weights, MIT) |

---

## Analysis & Impact

- **For software engineering / coding:** GPT-5.5 Instant now leads SWE-bench Verified at 88.7% — the first time a general-purpose model beats specialized Codex variants — while DeepSeek V4 Pro remains the best open-weight option at 80.6%. The 8.1pp gap between open and closed-weight leaders is the smallest it has ever been. For terminal/agentic coding, GPT-5.5 also leads Terminal-Bench 2.0 at 82.7%, giving engineering teams a single model that dominates across both benchmark types.

- **For frontier reasoning / math / science:** ARC-AGI-2 has been cracked: GPT-5.5 hits 85% vs. the 66% human average, with Gemini 3.1 Pro at 77.1% close behind. On GPQA Diamond (graduate science), the top three models (Gemini 3.1 Pro 94.3%, Claude Opus 4.7 94.2%, GPT-5.5 93.6%) are within 0.7pp of each other — GPQA Diamond is effectively saturated at the frontier. For math reasoning, Grok 4 Heavy's 100% AIME 2025 and 50%+ HLE remain the marks to beat, but only the Heavy (multi-agent) variant achieves them.

- **For multimodal / video / audio work:** The Magic Pointer from Google DeepMind introduces a new interaction paradigm — Gemini as a semantic cursor across all applications — which will compound value as it rolls out to Chrome and Googlebook laptops. For audio, GPT-Realtime-2's +15.2pp gain on Big Bench Audio and support for 70+ languages (via GPT-Realtime-Translate) makes real-time voice agents commercially viable for global deployments. Perceptron Mk1 remains the most cost-efficient video model at $0.15/$1.50 per 1M tokens, 80–90% cheaper than GPT-5.5 or Gemini for pure video workloads.

- **For cost-sensitive or open-source deployments:** DeepSeek V4 Pro (MIT license, $1.74 input) delivers 80.6% SWE-bench and 90.1% GPQA Diamond — competitive with models costing 17× more. Qwen 3.6 Plus ($0.33–$0.50 input) offers enterprise-grade agentic coding and 1M context for a fraction of frontier model pricing. Llama 4 Scout's 10M context window under Apache 2.0 remains the most accessible long-context open-weight option. The open-closed frontier gap is now measurable in single-digit benchmark percentage points, not double digits.

- **Agentic AI integration is now table stakes:** Claude for Small Business (15 pre-built workflows across 10+ SMB tools), GPT-5.5's full agentic feature set (computer use, parallel tool calls, code interpreter), and Gemini's Magic Pointer (operating system-level AI pointer) collectively signal that model releases without deep integration stories are no longer competitively sufficient. The battleground has shifted from benchmark performance to deployment breadth and workflow stickiness.

---

## Key Takeaways (TL;DR)

- **GPT-5.5 Instant tops SWE-bench Verified at 88.7%** and ARC-AGI-2 at 85% (beating human average), becoming the first general-purpose model to lead both the coding and abstract reasoning leaderboards simultaneously.
- **GPT-Realtime-2 achieves 96.6% on Big Bench Audio** (+15.2pp over its predecessor), with a 4× context expansion to 128K and configurable reasoning effort — turning voice AI into a frontier-class capability.
- **ARC-AGI-2 has crossed the human threshold**: GPT-5.5 at 85% exceeds the 66% human average by 19 points, marking the first broadly available model to achieve this on the benchmark designed to resist memorization.
- **Anthropic deployed 15 SMB agentic workflows** into QuickBooks, PayPal, HubSpot, and 10 other platforms on May 13 — a sign that frontier model labs are competing on deployment breadth as much as benchmark numbers.
- **The open-weight frontier gap is now 8.1pp** on SWE-bench Verified (DeepSeek V4 Pro 80.6% vs. GPT-5.5 88.7%) — with DeepSeek V4 Pro available at $1.74/M input under MIT license, the cost-capability tradeoff for open-source has never been more favorable.

---

*Sources:*

- https://openai.com/index/gpt-5-5-instant/
- https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/
- https://openai.com/index/gpt-5-5-instant-system-card/
- https://developers.openai.com/api/docs/models/gpt-5.5
- https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- https://thenextweb.com/news/openai-gpt-realtime-2-voice-models
- https://news.smol.ai/issues/26-05-07-gpt-realtime-2/
- https://developers.openai.com/api/docs/models/gpt-realtime-2
- https://windowsreport.com/openai-launches-gpt-realtime-2-real-time-translation-and-whisper-audio-apis/
- https://www.anthropic.com/news/claude-for-small-business
- https://rollingout.com/2026/05/13/claude-for-small-business-15-new/
- https://cryptobriefing.com/claude-for-small-business-ai-integration/
- https://deepmind.google/blog/ai-pointer/
- https://9to5google.com/2026/05/12/deepmind-googlebook-magic-pointer/
- https://www.marktechpost.com/2026/05/13/google-deepmind-introduces-an-ai-enabled-mouse-pointer-powered-by-gemini-that-captures-visual-and-semantic-context-around-the-cursor/
- https://arcprize.org/leaderboard
- https://benchlm.ai/benchmarks/arcAgi2
- https://agentmarketcap.ai/blog/2026/04/08/arc-agi-2-leaderboard-2026-gemini-abstract-reasoning-benchmark
- https://benchlm.ai/benchmarks/sweVerified
- https://leaderboard.steel.dev/leaderboards/swe-bench-verified/
- https://www.swfte.com/blog/lmsys-arena-leaderboard-may-2026
- https://benchlm.ai/benchmarks/gpqaDiamond
- https://benchlm.ai/benchmarks/liveCodeBench
- https://www.tbench.ai/leaderboard/terminal-bench/2.0
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/
- https://deepmind.google/models/model-cards/gemini-3-1-pro/
- https://www.swfte.com/research/gemini-3-1-pro
- https://benchgecko.ai/model/qwen3-6-plus
- https://benchlm.ai/models/qwen3-6-plus
- https://awesomeagents.ai/news/alibaba-qwen3-6-plus-enterprise-agentic-ai/
- https://deepseekai.guide/models/deepseek-v4/
- https://www.buildthisnow.com/blog/models/2026-04-24-deepseek-v4
- https://artificialanalysis.ai/leaderboards/models
- https://ai.meta.com/blog/introducing-muse-spark-msl/
- https://artificialanalysis.ai/articles/muse-spark-everything-you-need-to-know
- https://www.aiwiremedia.com/news/models/openai-launches-gpt-5-3-codex-spark-a-real-time-coding-model-running-on-cerebras-chips
- https://platform.claude.com/docs/en/build-with-claude/fast-mode
- https://www.anthropic.com/news/claude-opus-4-7
- https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/
- https://awesomeagents.ai/models/grok-4/
- https://aiprixa.com/grok-4-is-here-the-release-facts-benchmarks/
- https://crazyrouter.com/en/blog/ai-api-pricing-comparison-may-2026-developer-guide
- https://www.digitalapplied.com/blog/ai-model-api-pricing-tracker-q2-2026-data-points
