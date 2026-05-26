# Best Models & Benchmarks — 2026-05-26

## Top Model News (5)

### 1. Gemini Omni Flash — Google's First Native Video Generation Model Ships to Users Today

**Source:** [Google Blog](https://blog.google/intl/en-africa/products/explore-get-answers/gemini-omni/) | [Google DeepMind Model Card](https://deepmind.google/models/model-cards/gemini-omni-flash/) | [TechCrunch](https://techcrunch.com/2026/05/19/googles-gemini-omni-turns-images-audio-and-text-into-video-and-thats-just-the-start/) | [Let's Data Science](https://letsdatascience.com/news/google-launches-gemini-omni-flash-video-model-2cd9175a)

Announced at Google I/O (May 19) and now rolling out broadly to subscribers as of May 26, Gemini Omni Flash is the first model in Google's new Omni family — a transformer-based multimodal system that combines Gemini's language and reasoning backbone with generative media capabilities. The key breakthrough is *native* multimodal I/O: the model accepts arbitrary combinations of text, image, audio, and video as input and produces high-quality video output, grounded in Gemini's world knowledge. Users can describe, reference, and conversationally edit scenes without leaving the Gemini app or Google Flow. Every piece of generated content carries an imperceptible digital watermark and was shipped after automated plus human red-team safety evaluation.

The consumer roll-out is live today (May 26) for Google AI Plus, Pro, and Ultra subscribers globally via the Gemini app and Google Flow. YouTube Shorts and the YouTube Create app receive free access this week. The Omni Pro variant (higher fidelity, longer clips) is in development with no fixed launch date; Google has said it will ship "when we feel like we're at a step change above Flash." Developer and enterprise API access with pricing is expected in the coming weeks — benchmarks for T2VA, I2VA, R2VA, and video editing will be disclosed at that time.

**Key specs:** Not yet API-available | Text + Image + Audio + Video → Video (+ image/audio planned) | Consumer: included in Google AI subscription tiers; API pricing TBD | Proprietary | Rolling out now (consumer), API: weeks away

---

### 2. Qwen 3.7 Max — Alibaba's Highest-Benchmark Chinese Model Claims #1 on SWE-Bench Pro

**Source:** [DataCamp](https://www.datacamp.com/blog/qwen3-7-max) | [CryptoBriefing](https://cryptobriefing.com/alibaba-qwen3-7-max-ai-agent-model/) | [Digital Applied](https://www.digitalapplied.com/blog/qwen-3-7-max-alibaba-flagship-ai-model-2026) | [AI Hub](https://overchat.ai/ai-hub/qwen-3-7-max)

Qwen 3.7 Max, formally announced at the 2026 Alibaba Cloud Summit in Hangzhou on May 20, is Alibaba's closed-weight flagship designed explicitly for long-horizon agentic tasks. The headline demonstration: an autonomous 35-hour kernel optimization run that made 1,158 tool calls and achieved a 10× geometric mean speedup over the Triton reference implementation — a dramatic illustration of sustained agent coherence that most frontier models cannot match. On SWE-Bench Pro (the harder, 1,865-task, multi-language successor to SWE-Bench Verified), Qwen 3.7 Max posts 60.6%, the highest score publicly reported, edging Kimi K2.6 Thinking (59.5%) and DeepSeek V4-Pro Max (59.0%). It also leads on GPQA Diamond at 92.4% and the Apex reasoning benchmark at 44.5.

Pricing is $2.50 input / $7.50 output per 1M tokens — roughly half the cost of Claude Opus 4.7 ($5/$25) for comparable frontier-tier output. A 90% cache discount on input tokens is particularly favorable for long-context agentic workloads that repeatedly reference the same system prompt or document. The model is already live on Alibaba Cloud Model Studio, OpenRouter, Together AI, and Qubrid AI. It is closed-weight and proprietary; no open-source release is planned.

**Key specs:** 1M token context | Text + Vision | $2.50 input / $7.50 output per 1M tokens ($0.25/M cached input) | Proprietary (closed-weight) | Available now on Alibaba Cloud Model Studio, OpenRouter, Together AI

---

### 3. GLM-5.1 Highspeed — Zhipu AI Breaks the 400 Tokens/s API Speed Record

**Source:** [CnTechPost](https://cntechpost.com/2026/05/22/chinese-ai-startup-zhipu-rolls-out-ultra-fast-version-flagship-model/) | [AIBase](https://news.aibase.com/news/28235) | [Pandaily](https://pandaily.com/zhipu-ai-glm-5.1-high-speed-api-400-tokens-s-may2026) | [xix.ai](https://xix.ai/ainews/zhipu-glm51-launches-with-longcontext-performance-surpassing-opus-46.html)

On May 22, Zhipu AI launched GLM-5.1-highspeed — a production-serving variant of its flagship GLM-5.1 model (744B total / 40B active, MoE, MIT-licensed) achieving 400 tokens/s output through a co-developed inference stack with TileRT. This breaks a longstanding industry assumption: that flagship-tier models inherently carry high latency. At 400 t/s, GLM-5.1-highspeed is faster than Gemini 3.5 Flash's 289 t/s and approximately 6× faster than Claude Opus 4.7 (67 t/s) or GPT-5.5 (71 t/s). Zhipu's stock surged 22% intraday on the announcement, pushing its market cap above HKD 450 billion.

The underlying GLM-5.1 base model (open-sourced in April 2026) scored 58.4% on SWE-Bench Pro when released — at that time the first Chinese model to surpass the leading overseas model on that benchmark. It features an 8-hour autonomous execution loop, 202K token context, and dynamic sparse attention for codebase coherence across thousands of tool calls. The highspeed API is currently in selective enterprise access on the Zhipu MaaS platform, targeting AI coding, real-time interaction, business decision-making, and voice applications.

**Key specs:** 202K token context | Text + Code + Vision | Pricing aligned with Anthropic tier (raised 10% at open-source release) | MIT (base weights); proprietary highspeed API | Selective enterprise access now

---

### 4. DeepSeek V4-Pro — Open-Weight Coding Titan Holds the Top Open-Source SWE-Bench Verified Score

**Source:** [QubitTool](https://qubittool.com/blog/llm-landscape-may-2026-deepseek-qwen-llama-comparison) | [Callsphere AI](https://callsphere.ai/blog/llm-comparison-multi-step-research-agent-open-vs-open-may-2026.md) | [Presenc AI](https://presenc.ai/compare/deepseek-v4-vs-qwen-3-5-vs-llama-4-2026)

Released in April 2026 under the MIT license, DeepSeek V4-Pro (1.6 trillion total parameters / 49B active, sparse MoE + Multi-head Latent Attention) remains the dominant open-weight coding and reasoning model as of late May 2026. It posts 83.7% on SWE-Bench Verified — the highest score among openly available models — and holds 90.1% on GPQA Diamond and 87.5 on MMLU-Pro. Available via hosted APIs at $0.55/$0.87 per 1M tokens (input/output), it delivers 10–13× cost efficiency versus GPT-5.5 on equivalent coding tasks. The companion DeepSeek V4-Flash (284B / 13B active) is available at a remarkable $0.14/$0.28 — effectively free-tier for most workloads.

The model's MIT license is the critical differentiator: no usage caps, no MAU clauses, no attribution requirements. Combined with support for vLLM, TGI, SGLang, and Ollama, V4-Pro is the leading choice for teams that need frontier-class coding performance with full deployment control. On the LMSys Arena, DeepSeek V4-Pro holds a 1,462 Elo (April 2026 snapshot) — within striking distance of closed-source frontier models at a fraction of the cost.

**Key specs:** 1M token context | Text + Code | $0.55 input / $0.87 output per 1M (hosted); self-hostable | MIT license | Available on DeepSeek API, Together AI, Fireworks AI, and others

---

### 5. Update on Gemini 3.5 Flash — New SWE-Bench Pro Analysis and Agentic Benchmark Caveats Emerge

**Source:** [Awesome Agents](https://awesomeagents.ai/news/gemini-3-5-flash-agent-benchmarks/) | [Google DeepMind](https://deepmind.google/models/gemini/) | [HouseofMVPs](https://houseofmvps.com/blog/ai-agents/claude-opus-4-7-vs-gpt-5-5-vs-gemini-3-1-pro-for-ai-mvps-2026)

Since the Gemini 3.5 Flash launch (May 19, covered in the prior digest), independent analysts have published a more nuanced performance breakdown that developers should be aware of. On SWE-Bench Pro, Google's 55.1% places it third among closed frontier models — behind Claude Opus 4.7 (64.3%) and GPT-5.5 (58.6%). The 1M-token context window also shows significant degradation: 77.3% accuracy at 128K tokens drops to 26.6% at the full 1M, on par with other frontier models at that scale but well below GPT-5.5's 74% MRCR-v2 retrieval at 512K–1M. Despite these caveats, Gemini 3.5 Flash's combination of 289 tokens/s throughput, 83.6% MCP Atlas (best in class), $1.50/$9.00 pricing, and Finance Agent v2 leadership (57.9%) makes it the clear pick for high-volume agentic pipelines where cost and throughput dominate.

**Key specs:** 1M token context (degraded beyond 128K) | Text + Vision + Code | $1.50 input / $9.00 output per 1M | Proprietary | GA globally via Gemini API, AI Studio, Android Studio, Google Antigravity

---

## Deep Dive: Most Important Release — Gemini Omni Flash (May 26, 2026)

Today's most defining model event is the consumer roll-out of Gemini Omni Flash — not because it tops a code or reasoning leaderboard, but because it represents the first time a frontier-grade intelligence model natively generates and conversationally edits video from any combination of multimodal inputs at mass consumer scale. Where Sora (OpenAI) and Veo (Google) were single-modality text-to-video generation systems accessible mainly to creative professionals, Gemini Omni Flash embeds world-knowledge-grounded video synthesis directly into the apps that more than a billion users already use daily: the Gemini app, Google Flow, and YouTube Shorts.

### What It Can Do

Gemini Omni Flash accepts text, images, audio, and video in any combination as input and generates high-quality, physics-grounded video output. Users can describe a scene in natural language, reference an uploaded image of a location or person, and the model maintains character consistency and scene continuity across a multi-turn conversational editing session — asking "make the lighting warmer" or "have the character turn left" without re-generating from scratch. The model includes imperceptible SynthID digital watermarks on every output and was shipped after systematic red-team safety testing. It renders 10-second clips in the current Flash variant; longer durations are planned. Output quality is strong for simple scenes (travel, action) and shows artifacts on complex motion or dense crowds — typical for the current generation of video diffusion systems.

### Benchmark Highlights

Google has not yet disclosed formal benchmarks for Gemini Omni Flash, stating evaluations for T2VA, I2VA, R2VA, video editing, and image generation will be released when the developer/enterprise API becomes available. The following table covers the underlying Gemini 3.5 Flash reasoning model from which Omni derives its world understanding:

| Benchmark | Gemini 3.5 Flash | Previous Best (at launch) |
|---|---|---|
| MCP Atlas (agentic tool use) | 83.6% | Gemini 3.1 Pro — 78.2% |
| Terminal-Bench 2.1 (agentic coding) | 76.2% | Gemini 3.1 Pro — 70.3% |
| Finance Agent v2 | 57.9% | Gemini 3.1 Pro — 43.0% |
| CharXiv Reasoning (chart understanding) | 84.2% | Gemini 3.1 Pro — not published |
| GDPval-AA Elo (economically valuable work) | 1,656 | Gemini 3.1 Pro — 1,314 |
| SWE-Bench Pro (diverse agentic coding) | 55.1% | Claude Opus 4.7 — 64.3% |
| MMMU-Pro (multimodal understanding) | 83.6% | GPT-5.5 — 81.2% |
| ARC-AGI-2 | 72.1% | GPT-5.5 — 85.0% |
| Throughput (tokens/s) | 289 t/s | GPT-5.5 — 71 t/s |

### Architecture (known)

Gemini Omni Flash is a transformer-based model (Vaswani et al., 2017) with native multimodal support for text, vision, video, and audio inputs and outputs. It was trained on audio, video, image, and text data with text captions at multiple levels of detail. It integrates Gemini 3.5 Flash's reasoning backbone with Google's generative media models (Veo and related systems) into a single end-to-end architecture. The exact parameter count and MoE configuration are not disclosed. SynthID watermarking is built into the generation pipeline natively.

### Pricing & Availability

- **Today (May 26):** Consumer roll-out to all Google AI Plus, Pro, and Ultra subscribers globally via Gemini app and Google Flow; free access on YouTube Shorts and YouTube Create app (ages 18+)
- **API (coming weeks):** Developer and enterprise access via Google AI Studio and Vertex AI — pricing not yet disclosed
- **Context:** Not applicable in the traditional sense — video generation is clip-based (10-second clips, Flash variant)
- **Omni Pro:** Under development, no confirmed launch date

### Strategic Significance

Gemini Omni Flash collapses the gap between "AI assistant" and "AI creative studio" for more than a billion Google users in a single roll-out. By embedding world-knowledge-grounded video generation into the Gemini app rather than shipping it as a separate product, Google is making the argument that multimodal creation is a *feature* of a general-purpose AI, not a standalone tool. This is the same playbook Google used with Gemini 3.5 Flash's integration into Search — commoditize an expensive capability by embedding it at the platform level.

The competitive implication is stark: OpenAI's Sora is a standalone product; Meta's Movie Gen has been research-only; Runway and Pika are independent startups. None of them have the distribution channel that Google has with YouTube Shorts alone, which sees 100 billion daily video views. If Omni Flash's quality is "good enough" for the vast majority of user-generated content, the creative AI tooling market faces serious disruption from a free-at-the-margin incumbent.

The synthetic media governance challenge is equally significant. Google shipping SynthID watermarks natively is a positive step, but watermarks can be stripped, and 400M+ YouTube Shorts creators gaining free AI video synthesis means the volume of AI-generated video content will accelerate sharply in coming weeks. Detection infrastructure, platform policy enforcement, and regulatory frameworks are not prepared for this scale.

### Competitive Context

On video generation quality, Gemini Omni Flash is entering a field where OpenAI's Sora, Google's own Veo 3, and Runway Gen-4 have established reference points. The "conversational editing" feature is differentiated — Sora and Veo require re-prompting from scratch for edits. On raw quality at the top end, The Verge's hands-on review noted Omni Flash is strong on simple scenes but shows artifacts on complex motion — suggesting Veo 3 and Sora Pro still hold quality advantages for production use cases. The key differentiator is access: free on YouTube, included in Gemini subscriptions, with an enterprise API coming. No competitor has this distribution breadth at these economics.

---

## Benchmark Comparison Data

```json
{"benchmark": "SWE-Bench Pro (agentic coding, 1865 tasks, multi-language)", "results": [{"model": "Claude Opus 4.7", "score": 64.3}, {"model": "Qwen 3.7 Max", "score": 60.6}, {"model": "GPT-5.5", "score": 58.6}, {"model": "GLM-5.1", "score": 58.4}, {"model": "Kimi K2.6 Thinking", "score": 59.5}, {"model": "DeepSeek V4-Pro Max", "score": 59.0}, {"model": "Gemini 3.5 Flash", "score": 55.1}, {"model": "Gemini 3.1 Pro", "score": 54.2}, {"model": "DeepSeek V4-Pro", "score": 55.4}, {"model": "Mistral Medium 3.5", "score": 31.0}]}
```

```json
{"benchmark": "SWE-Bench Verified (Python, 500 tasks)", "results": [{"model": "Claude Opus 4.7", "score": 87.6}, {"model": "GPT-5.5", "score": 88.7}, {"model": "DeepSeek V4-Pro", "score": 83.7}, {"model": "Qwen 3.7 Max", "score": 80.4}, {"model": "Kimi K2.6", "score": 82.0}, {"model": "GLM-5.1", "score": 58.4}, {"model": "Gemini 3.5 Flash", "score": 55.1}, {"model": "Gemini 3.1 Pro", "score": 80.6}, {"model": "Mistral Medium 3.5", "score": 77.6}]}
```

```json
{"benchmark": "GPQA Diamond (PhD-level science)", "results": [{"model": "Claude Opus 4.7", "score": 94.2}, {"model": "GPT-5.5 (Pro tier)", "score": 94.4}, {"model": "Gemini 3.1 Pro", "score": 94.3}, {"model": "Qwen 3.7 Max", "score": 92.4}, {"model": "GLM-5.1", "score": 94.6}, {"model": "DeepSeek V4-Pro", "score": 88.8}, {"model": "Qwen 3.5", "score": 88.4}, {"model": "Kimi K2.6 Thinking", "score": 90.5}]}
```

```json
{"benchmark": "ARC-AGI-2 (abstract reasoning puzzles, human avg 66%)", "results": [{"model": "GPT-5.5", "score": 85.0}, {"model": "GPT-5.4 Pro", "score": 83.3}, {"model": "Gemini 3.1 Deep Think", "score": 84.6}, {"model": "Gemini 3.1 Pro", "score": 77.1}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8}, {"model": "Gemini 3.5 Flash", "score": 72.1}, {"model": "GPT-5.4", "score": 73.3}, {"model": "Claude Opus 4.6", "score": 68.8}, {"model": "Grok 4.20", "score": 53.3}]}
```

```json
{"benchmark": "LMSys Chatbot Arena — Overall ELO (May 14, 2026)", "results": [{"model": "claude-opus-4-6-thinking", "score": 1502}, {"model": "claude-opus-4-7-thinking", "score": 1501}, {"model": "claude-opus-4-6", "score": 1498}, {"model": "claude-opus-4-7", "score": 1492}, {"model": "muse-spark (Meta)", "score": 1491}, {"model": "gemini-3.1-pro-preview", "score": 1490}, {"model": "gemini-3-pro", "score": 1486}, {"model": "gpt-5.5-high", "score": 1484}, {"model": "grok-4.20-beta1", "score": 1479}, {"model": "gpt-5.4-high", "score": 1479}, {"model": "gpt-5.5", "score": 1476}, {"model": "gemini-3-flash", "score": 1474}, {"model": "ernie-5.1 (Baidu)", "score": 1473}, {"model": "glm-5.1 (Zhipu)", "score": 1471}, {"model": "qwen3.5-max-preview", "score": 1465}]}
```

```json
{"benchmark": "Terminal-Bench 2.1 (agentic terminal coding)", "results": [{"model": "GPT-5.5", "score": 82.7}, {"model": "Gemini 3.5 Flash", "score": 76.2}, {"model": "Gemini 3.1 Pro", "score": 70.3}, {"model": "Claude Opus 4.7", "score": 66.1}, {"model": "Qwen 3.7 Max (TB 2.0)", "score": 69.7}, {"model": "GLM-5.1 (TB 2.0)", "score": 63.5}]}
```

```json
{"benchmark": "LiveCodeBench (code on unseen problems)", "results": [{"model": "DeepSeek V4-Pro", "score": 93.5}, {"model": "Qwen 3.7 Max", "score": 91.6}, {"model": "GLM-5.1", "score": 68.0}]}
```

```json
{"benchmark": "MCP Atlas (multi-step tool-use workflows)", "results": [{"model": "Gemini 3.5 Flash", "score": 83.6}, {"model": "Claude Opus 4.7", "score": 79.1}, {"model": "Gemini 3.1 Pro", "score": 78.2}, {"model": "Qwen 3.7 Max", "score": 76.4}, {"model": "GPT-5.5", "score": 75.3}, {"model": "Claude Sonnet 4.6", "score": 69.5}]}
```

```json
{"benchmark": "Humanity's Last Exam (HLE, no tools)", "results": [{"model": "Claude Opus 4.7", "score": 46.9}, {"model": "Gemini 3.1 Pro", "score": 44.4}, {"model": "Qwen 3.7 Max", "score": 41.4}, {"model": "GPT-5.5", "score": 41.4}, {"model": "Gemini 3.5 Flash", "score": 40.2}, {"model": "Kimi K2.6", "score": 54.0}]}
```

```json
{"benchmark": "GDPval-AA Elo (economically valuable knowledge work)", "results": [{"model": "GPT-5.5", "score": 1769}, {"model": "Claude Opus 4.7", "score": 1753}, {"model": "Gemini 3.1 Pro", "score": 1676}, {"model": "Gemini 3.5 Flash", "score": 1656}, {"model": "Gemini 3.0 Flash (prior)", "score": 1204}]}
```

```json
{"benchmark": "MMMU-Pro (multimodal understanding, no tools)", "results": [{"model": "Gemini 3.5 Flash", "score": 83.6}, {"model": "Gemini 3.1 Pro", "score": 80.5}, {"model": "GPT-5.5", "score": 81.2}, {"model": "Claude Opus 4.7", "score": 75.2}]}
```

```json
{"benchmark": "Apex (advanced reasoning, vendor-reported)", "results": [{"model": "Qwen 3.7 Max", "score": 44.5}, {"model": "DeepSeek V4-Pro Max", "score": 38.3}, {"model": "Claude Opus 4.6 Max", "score": 34.5}]}
```

```json
{"benchmark": "GPQA Diamond — Open-Weight Only", "results": [{"model": "Qwen 3.5 (open)", "score": 88.4}, {"model": "DeepSeek V4-Pro (open)", "score": 88.8}, {"model": "Kimi K2.6 Thinking (Modified MIT)", "score": 90.5}, {"model": "GLM-5.1 (MIT)", "score": 94.6}]}
```

```json
{"benchmark": "Artificial Analysis Intelligence Index v4.0 (overall)", "results": [{"model": "GPT-5.5", "score": 60.2}, {"model": "Claude Opus 4.7", "score": 57.3}, {"model": "Qwen 3.7 Max", "score": 56.6}, {"model": "DeepSeek V4-Pro", "score": 55.5}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Opus 4.7 | Anthropic | 1M | $5.00 | $25.00 | Text, Vision, Code |
| GPT-5.5 | OpenAI | 1M (400K in Codex) | $5.00 | $30.00 | Text, Vision, Code, Audio |
| GPT-5.5 Pro | OpenAI | 1M | $30.00 | $180.00 | Text, Vision, Code, Audio |
| Gemini 3.1 Pro | Google | 2M | $2.00 (≤200K) | $12.00 (≤200K) | Text, Vision, Code, Audio, Video |
| Gemini 3.5 Flash | Google | 1M | $1.50 | $9.00 | Text, Vision, Code, Audio |
| Gemini Omni Flash | Google | N/A (clip-based) | TBD (API) | TBD (API) | Text + Image + Audio + Video → Video |
| Qwen 3.7 Max | Alibaba | 1M | $2.50 | $7.50 | Text, Vision, Code |
| DeepSeek V4-Pro | DeepSeek | 1M | $0.55 (hosted) | $0.87 (hosted) | Text, Code |
| DeepSeek V4-Flash | DeepSeek | 1M | $0.14 (hosted) | $0.28 (hosted) | Text, Code |
| Kimi K2.6 | MoonShot AI | 1M | $0.95 | $4.00 | Text, Code, Vision |
| GLM-5.1 | Zhipu AI | 202K | Aligned w/ Anthropic | Aligned w/ Anthropic | Text, Code, Vision |
| Grok 4.20 | xAI | 256K | $5.00 | $15.00 | Text, Vision, Code |
| Llama 4 Scout | Meta | 10M | ~$0.10 (hosted) | ~$0.40 (hosted) | Text, Vision |
| Llama 4 Maverick | Meta | 1M | ~$0.15 (hosted) | ~$0.60 (hosted) | Text, Vision |
| Qwen 3.5 (397B) | Alibaba | 256K | ~$0.40 (hosted) | ~$1.20 (hosted) | Text, Code |
| Mistral Large 3 | Mistral | 256K | $3.00 | $9.00 | Text, Code |
| Mistral Medium 3.5 | Mistral | 128K | ~$1.00 | ~$3.00 | Text, Code |

---

## Analysis & Impact

- **For software engineering / coding:** Claude Opus 4.7 remains the accessible frontier ceiling for real-world code changes, with 64.3% on SWE-Bench Pro. However, Qwen 3.7 Max (60.6% SWE-Pro at $2.50/$7.50) now offers compelling cost efficiency for teams willing to use an Alibaba-hosted API. DeepSeek V4-Pro (83.7% SWE-Verified, MIT, $0.55/$0.87 hosted) is the undisputed choice for open-source deployments — it costs 10–13× less than GPT-5.5 on equivalent coding tasks. The new SWE-Bench Verified vs. Pro disparity (models scoring 70%+ Verified often fall to 20–30% Pro) means teams should validate benchmarks against SWE-Bench Pro for realistic multi-file, multi-language expectations.

- **For frontier reasoning / math / science:** GPT-5.5 leads ARC-AGI-2 (85%) and shares the GPQA Diamond crown with Claude Opus 4.7 (94.2–94.4%). Qwen 3.7 Max's 44.5 on Apex and 92.4 on GPQA Diamond represent a new high-water mark from a Chinese lab, at half the proprietary frontier price. GLM-5.1 (MIT, open-weights) posts a surprising 94.6 GPQA Diamond, challenging the assumption that frontier reasoning requires closed-source access.

- **For multimodal / video / audio work:** Gemini Omni Flash's consumer launch today is the defining event in this category. Native multimodal I/O with conversational video editing, physics-grounded generation, and SynthID watermarking — all free on YouTube Shorts — fundamentally changes the accessible ceiling for multimodal creation. Gemini 3.5 Flash leads CharXiv Reasoning (84.2%) and MMMU-Pro (83.6%), making it the strongest vision-reasoning choice among fast models. Gemini 3.1 Pro (2M context, $2/$12) remains the best value for multimodal enterprise workloads at scale.

- **For cost-sensitive or open-source deployments:** DeepSeek V4-Flash ($0.14/$0.28, MIT) is now the go-to for high-volume inference where quality doesn't need to be frontier. DeepSeek V4-Pro ($0.55/$0.87, MIT) provides frontier-tier coding at 10×+ cost advantage over GPT-5.5. Llama 4 Scout (10M token context, Llama community license) is unmatched for long-document workloads. GLM-5.1 (MIT, 58.4% SWE-Pro, 8-hour autonomous loop) is now a serious alternative to proprietary models for agentic engineering pipelines — especially at GLM-5.1-highspeed's 400 t/s throughput.

- **Sustained agentic coherence is now the benchmark:** The arms race has shifted from static accuracy benchmarks to autonomous multi-hour execution. GLM-5.1 frames "8-hour work mode" as the new AGI metric. Qwen 3.7 Max validated 35 hours and 1,158 tool calls. Claude Mythos Preview showed 93.9% SWE-bench Verified under autonomous conditions. The capability floor for "production AI agents" is rising — and the constraint is no longer intelligence per se, but context coherence, tool reliability, and error recovery across thousands of sequential steps.

---

## Key Takeaways (TL;DR)

- Gemini Omni Flash rolls out to consumers globally today (May 26), making world-knowledge-grounded, conversationally editable video synthesis free on YouTube Shorts — the first native video generation model embedded in a platform with 100B+ daily video views.
- Qwen 3.7 Max (Alibaba) posts the top SWE-Bench Pro score of 60.6% and leads on the Apex reasoning benchmark at 44.5, at $2.50/$7.50 — half the cost of Claude Opus 4.7 — making it the most cost-efficient frontier reasoning model from any lab.
- Zhipu's GLM-5.1-highspeed sets a new global API speed record at 400 tokens/s — 6× faster than Claude Opus 4.7 — while maintaining flagship-tier capability (94.6% GPQA Diamond), exploding the assumed latency-quality tradeoff.
- GPT-5.5 leads ARC-AGI-2 at 85% (the grand-prize threshold), while Claude Opus 4.7 leads SWE-Bench Pro at 64.3% — the frontier is now benchmark-dependent with no single model dominating every dimension.
- DeepSeek V4-Pro (MIT, 1.6T/49B MoE, $0.55/$0.87 hosted) continues to widen the open-vs-closed cost gap: 10–13× cheaper than GPT-5.5 on coding tasks with comparable performance, removing the economic argument for proprietary models in most code generation workflows.

---

*Sources:*
- https://blog.google/intl/en-africa/products/explore-get-answers/gemini-omni/
- https://deepmind.google/models/model-cards/gemini-omni-flash/
- https://techcrunch.com/2026/05/19/googles-gemini-omni-turns-images-audio-and-text-into-video-and-thats-just-the-start/
- https://letsdatascience.com/news/google-launches-gemini-omni-flash-video-model-2cd9175a
- https://dev.to/jenueldev/gemini-omni-makes-video-generation-feel-more-like-editing-3434
- https://deepmind.google/models/gemini/
- https://awesomeagents.ai/news/gemini-3-5-flash-agent-benchmarks/
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/
- https://generativeai.pub/the-code-of-reality-how-google-i-o-2026-just-redefined-the-human-ai-interface-41be32989b34
- https://www.datacamp.com/blog/qwen3-7-max
- https://cryptobriefing.com/alibaba-qwen3-7-max-ai-agent-model/
- https://www.digitalapplied.com/blog/qwen-3-7-max-alibaba-flagship-ai-model-2026
- https://overchat.ai/ai-hub/qwen-3-7-max
- https://www.naturalnews.com/2026-05-26-qwen-new-ai-model-designed-autonomous-tasks.html
- https://cntechpost.com/2026/05/22/chinese-ai-startup-zhipu-rolls-out-ultra-fast-version-flagship-model/
- https://news.aibase.com/news/28235
- https://pandaily.com/zhipu-ai-glm-5.1-high-speed-api-400-tokens-s-may2026
- https://xix.ai/ainews/zhipu-glm51-launches-with-longcontext-performance-surpassing-opus-46.html
- https://automatio.ai/models/glm-5-1
- https://qubittool.com/blog/llm-landscape-may-2026-deepseek-qwen-llama-comparison
- https://presenc.ai/compare/deepseek-v4-vs-qwen-3-5-vs-llama-4-2026
- https://callsphere.ai/blog/llm-comparison-multi-step-research-agent-open-vs-open-may-2026.md
- https://opentools.ai/compare/llms/claude-opus-47-vs-gpt-55
- https://www.digitalapplied.com/blog/gpt-5-5-vs-claude-opus-4-7-frontier-comparison
- https://www.buildthisnow.com/blog/models/claude-opus-4-7-vs-gpt-5-5
- https://houseofmvps.com/blog/ai-agents/claude-opus-4-7-vs-gpt-5-5-vs-gemini-3-1-pro-for-ai-mvps-2026
- https://lushbinary.com/blog/gpt-5-5-vs-claude-opus-4-7-comparison-benchmarks-pricing/
- https://presenc.ai/research/lmsys-chatbot-arena-elo-rankings-may-2026
- https://www.swfte.com/blog/lmsys-arena-leaderboard-may-2026
- https://www.swfte.com/lmarena
- https://benchlm.ai/benchmarks/arcAgi2
- https://benchlm.ai/blog/posts/arc-agi-2-explained
- https://thewincentral.com/gpt-5-6-leaks-suggest-openais-next-big-ai-upgrade-could-arrive-in-june/
- https://perplexityaimagazine.com/ai-news/gpt-56-release-date-features-leaks-openai-2026/
- https://www.miniloop.ai/blog/best-open-source-llms-2026
- https://codersera.com/blog/open-source-llms-landscape-2026/
