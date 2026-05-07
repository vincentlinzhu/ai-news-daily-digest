# Best Models — AI News Digest: 2026-05-07

> **Coverage window:** ~2026-05-03 through 2026-05-07. Stories already covered in the 2026-05-06 digest are excluded unless there is materially new information.

---

## Top Stories

### 1. GPT-5.5 Instant Becomes ChatGPT's Default Model (May 5, 2026)
OpenAI replaced GPT-5.3 Instant with **GPT-5.5 Instant** as the default model for all ChatGPT users on May 5, 2026. The headline claim: **52.5% fewer hallucinated claims** than GPT-5.3 Instant on high-stakes medical, legal, and financial prompts, and a **37.3% reduction** in factual errors on conversations users had previously flagged. Beyond factuality, GPT-5.5 Instant is a generally stronger model across STEM, visual reasoning, and context-aware personalization. It also delivers shorter, less verbose responses: in internal comparisons it used 30% fewer words without losing substance. OpenAI simultaneously announced memory sources — visible, deletable citations of which past chats and saved memories shaped a response — rolling out across consumer plans.

GPT-5.5 Instant is now also available in the API as `chat-latest`. GPT-5.3 Instant remains available to paid users for three months before retirement.

**Source:** [openai.com/index/gpt-5-5-instant](https://openai.com/index/gpt-5-5-instant/) · May 5, 2026

---

### 2. OpenAI Ships Three New Realtime Voice Models (May 7, 2026 — Today)
OpenAI launched a new generation of realtime audio models in the API today:

- **GPT-Realtime-2** — GPT-5-class reasoning in a live voice interface. Context window expands from 32K → **128K tokens**. Supports parallel tool calls, preambles ("let me check that…"), adjustable reasoning effort (minimal → xhigh), and tone control. On **Big Bench Audio** it scores **96.6%** vs. 81.4% for GPT-Realtime-1.5 (+15.2 pp). On **Audio MultiChallenge** (multi-turn instruction following): **48.5%** vs. 34.7% (+13.8 pp). Zillow reports a **26-point lift in call success rate** (95% vs. 69%) on adversarial benchmarks after prompt optimization.
- **GPT-Realtime-Translate** — Live speech-to-speech translation supporting **70+ input languages → 13 output languages** at natural conversational pace. BolnaAI reports **12.5% lower word error rates** across Hindi, Tamil, and Telugu vs. prior best.
- **GPT-Realtime-Whisper** — Streaming speech-to-text (STT) for low-latency transcription, live captions, and meeting notes.

**Pricing:** GPT-Realtime-2 at $32/$64 per million audio input/output tokens; Translate at $0.034/min; Whisper at $0.017/min.

**Source:** [openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) · May 7, 2026

---

### 3. Kimi K2.6 Wins Live Coding Tournament Over GPT-5.5 and Claude Opus 4.7 (May 3, 2026)
*Update on Kimi K2.6 — new competitive result since the 2026-05-06 digest.*

Moonshot AI's **Kimi K2.6** (1T params, 32B active, released April 20) won the "Word Gem Puzzle" AI Coding Contest on May 3. Final standings in the head-to-head competition:

| Rank | Model | Points | Record |
|------|-------|--------|--------|
| 1 | **Kimi K2.6** | 22 | 7-1-0 |
| 2 | MiMo V2-Pro (Xiaomi) | 20 | — |
| 3 | GPT-5.5 | 16 | — |
| 4 | GLM 5.1 (Zhipu AI) | 15 | — |
| 5 | Claude Opus 4.7 | 12 | — |

This follows Kimi K2.6 already topping the SWE-bench Pro public dataset at 58.6% among open-weight models. The contest win — while a single data point — reinforces its practical coding edge at just $0.60/$2.50 per million tokens (roughly 1/25th the cost of Claude Opus 4.7). The Hacker News thread reached 311 upvotes and 172 comments.

**Sources:** [buildfastwithai.com/blogs/kimi-k2-6-review-benchmarks](https://www.buildfastwithai.com/blogs/kimi-k2-6-review-benchmarks) · [moony01.com/ai/2026/05/03/kimi-k26-coding-test](https://moony01.com/ai/2026/05/03/kimi-k26-coding-test.html)

---

### 4. Mistral Medium 3.5: Best Publicly Available Open-Weight Coding Model (April 29, 2026)
Mistral released **Mistral Medium 3.5** on April 29 — a 128B dense open-weight model that consolidates Mistral Medium 3.1, Magistral, and Devstral 2 into a single architecture covering instruction-following, reasoning, and coding. It scores **77.6% on SWE-bench Verified**, making it the highest open-weight result on that benchmark (edging Claude Sonnet 4 at 77.2% and placing just below Gemini 3.1 Pro Preview at 78.8%). On the τ³-Telecom agentic benchmark: **91.4%**.

Self-hosting requires ~4× H100/H200 GPUs (128GB VRAM, FP8). API pricing: $1.50/$7.50 per million input/output tokens. License: modified MIT on Hugging Face.

**Sources:** [benchlm.ai/models/mistral-medium-3-5-128b](https://benchlm.ai/models/mistral-medium-3-5-128b) · [i-scoop.eu/mistral-medium-3-5](https://www.i-scoop.eu/mistral-medium-3-5/)

---

### 5. BenchLM Coding Leaderboard Update: May 7, 2026 Snapshot
The BenchLM.ai coding leaderboard updated today. Key changes vs. last week:
- **GPT-5.3 Codex** jumped to #2 on SWE-bench Pro with a **77.3%** score — the highest open-weight coding result ever recorded on that benchmark.
- **Claude Mythos Preview** remains #1 overall (100.0 weighted; 93.9% SWE-bench Verified / 77.8% SWE-bench Pro) but is still restricted (Glasswing-only access).
- **DeepSeek V4 Pro (Max)** holds the #4 spot with a 88/100 weighted score and **80.6% SWE-bench Verified** / **55.4% SWE-bench Pro** at $1.74/$3.48 per million tokens.

**Source:** [benchlm.ai/coding](https://benchlm.ai/coding) · Updated May 7, 2026

---

## Deep Dive: GPT-5.5 Instant — What Actually Changed

### The Hallucination Story
OpenAI published a detailed system card for GPT-5.5 Instant's hallucination improvements. The 52.5% reduction vs. GPT-5.3 Instant is measured on *high-stakes prompts* — medicine, law, finance — where accuracy failures have real-world cost. The 37.3% reduction on "especially challenging conversations users flagged" addresses a specific feedback loop from production ChatGPT usage. Neither figure is measured against GPT-5.5 (the heavy model) — this is purely a Instant-tier upgrade story.

Internal examples from the blog post illustrate the change: GPT-5.3 Instant catches that x=3 fails the original equation but incorrectly concludes "no real solution." GPT-5.5 Instant recovers, identifies the algebraic error, re-solves correctly using the quadratic formula, and arrives at (3+√33)/2. This is a qualitatively different failure mode — recovery from initial error — not just fewer surface hallucinations.

### Reasoning & Multimodal Gains

```json
{
  "model": "GPT-5.5 Instant",
  "vs_baseline": "GPT-5.3 Instant",
  "benchmarks": {
    "AIME_2025": { "new": 81.2, "old": 65.4, "delta": "+15.8pp" },
    "GPQA_Diamond": { "new": 85.6, "old": 78.5, "delta": "+7.1pp" },
    "CharXiv_ScientificCharts": { "new": 81.6, "old": 75.0, "delta": "+6.6pp" },
    "MMMU_Pro": { "new": 76.0, "old": 69.2, "delta": "+6.8pp" },
    "OmniDocBench_error_rate": { "new": 12.5, "old": 14.6, "delta": "-2.1pp (lower is better)" }
  },
  "note": "All vs GPT-5.3 Instant, not the full GPT-5.5 heavy model"
}
```

### Personalization
GPT-5.5 Instant introduces "memory sources" — explicit citations of which past chats, saved memories, and connected data (Gmail if authorized) shaped a given response. Unlike prior black-box personalization, the user can inspect, delete, and correct the sources. This is an important UX affordance for trust in daily-driver AI.

---

## Deep Dive: Realtime Voice — GPT-Realtime-2 Architecture Notes

GPT-Realtime-2 is the first OpenAI voice model described as having "GPT-5-class reasoning." Prior Realtime models used lighter reasoning pipelines to keep latency low. The new model adds:

1. **Parallel tool calls in the audio stream** — the model can fan out tool invocations while narrating ("checking your calendar…") without blocking the conversation.
2. **Reasoning effort ladder** — minimal/low/medium/high/xhigh, letting developers trade latency for accuracy per call.
3. **Preambles** — filling the natural response delay with appropriate verbal acknowledgment rather than silence. This is a small UX detail with large perceived-quality impact.
4. **Context: 32K → 128K** — enables coherent multi-task voice sessions and longer conversations.

The two benchmark improvements (+15.2 pp on Big Bench Audio, +13.8 pp on Audio MultiChallenge) translate directly into real call success rate gains: Zillow's 26-point lift (95% vs. 69%) is the most concrete production evidence.

**Pattern note:** The three-model split (reason/translate/transcribe) mirrors OpenAI's earlier text-model unbundling strategy. Different use-cases get purpose-built models rather than one over-engineered model. This keeps per-use-case cost and latency optimal.

---

## Benchmark / Data JSON Blocks

### Coding Leaderboard (SWE-bench Pro — May 7, 2026)
```json
{
  "source": "benchlm.ai/coding",
  "updated": "2026-05-07",
  "metric": "SWE-bench Pro (% resolved)",
  "top_models": [
    { "rank": 1, "model": "Claude Mythos Preview", "type": "closed", "swe_pro": 77.8, "swe_verified": 93.9, "price_per_1M": "$25/$125", "access": "restricted (Glasswing only)" },
    { "rank": 2, "model": "GPT-5.3 Codex", "type": "open-weight", "swe_pro": 77.3, "swe_verified": 85.0, "note": "highest open-weight SWE-Pro ever" },
    { "rank": 3, "model": "Kimi K2.6", "type": "open-weight", "swe_pro": 58.6, "swe_verified": 76.8, "price_per_1M": "$0.60/$2.50", "context": "256K" },
    { "rank": 4, "model": "GPT-5.5", "type": "closed", "swe_pro": 56.8, "swe_verified": 88.7, "price_per_1M": "$5/$30", "context": "400K" },
    { "rank": 5, "model": "Claude Opus 4.7 (Adaptive)", "type": "closed", "swe_pro": 64.3, "swe_verified": 87.6, "price_per_1M": "$5/$25", "context": "1M" },
    { "rank": 6, "model": "DeepSeek V4 Pro (Max)", "type": "open-weight", "swe_pro": 55.4, "swe_verified": 80.6, "price_per_1M": "$1.74/$3.48", "context": "1M" },
    { "rank": 7, "model": "Mistral Medium 3.5", "type": "open-weight", "swe_verified": 77.6, "price_per_1M": "$1.50/$7.50", "context": "256K", "hosting": "4×H100 FP8" }
  ]
}
```

### Reasoning & General Intelligence (May 2026)
```json
{
  "source": "benchlm.ai + awesomeagents.ai",
  "updated": "2026-05",
  "GPQA_Diamond": [
    { "model": "Claude Mythos Preview", "score": 94.5 },
    { "model": "Gemini 3.1 Pro", "score": 94.3 },
    { "model": "Claude Opus 4.7 (Adaptive)", "score": 94.2 },
    { "model": "GPT-5.5", "score": 93.6 }
  ],
  "AIME_2025": [
    { "model": "GPT-5.2 Pro", "score": 100.0, "note": "IMO-qualifying level" },
    { "model": "Grok 4 Heavy", "score": 96.7 },
    { "model": "DeepSeek V3.2-Speciale", "score": 96.7 },
    { "model": "Claude Opus 4.6", "score": 93.3 }
  ],
  "note": "GPQA is near saturation for frontier models — <1pp separates top 4"
}
```

### LMSys Chatbot Arena (Human Preference, April 2026)
```json
{
  "source": "lmarena.ai",
  "updated": "2026-04",
  "metric": "Elo (Bradley-Terry, 5.8M votes, 635 models)",
  "top_5": [
    { "rank": 1, "model": "Claude Opus 4.7 Thinking", "elo": 1505 },
    { "rank": 2, "model": "Claude Opus 4.6 Thinking", "elo": 1503 },
    { "rank": 3, "model": "Claude Opus 4.7", "elo": 1498 },
    { "rank": 4, "model": "Claude Opus 4.6", "elo": 1497 },
    { "rank": 5, "model": "Muse Spark (Meta)", "elo": 1496 }
  ]
}
```

### Realtime Voice Models (May 7, 2026)
```json
{
  "source": "openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api",
  "date": "2026-05-07",
  "models": [
    {
      "name": "GPT-Realtime-2",
      "context_tokens": 128000,
      "reasoning_effort": ["minimal","low","medium","high","xhigh"],
      "Big_Bench_Audio": { "new": 96.6, "old": 81.4, "delta": "+15.2pp" },
      "Audio_MultiChallenge": { "new": 48.5, "old": 34.7, "delta": "+13.8pp" },
      "price": { "audio_input": "$32/1M", "cached_input": "$0.40/1M", "audio_output": "$64/1M" },
      "features": ["parallel_tool_calls","preambles","tone_control","domain_vocabulary"]
    },
    {
      "name": "GPT-Realtime-Translate",
      "input_languages": 70,
      "output_languages": 13,
      "price": "$0.034/min"
    },
    {
      "name": "GPT-Realtime-Whisper",
      "type": "streaming_STT",
      "price": "$0.017/min"
    }
  ]
}
```

### GPT-5.5 Instant Benchmark Gains
```json
{
  "source": "openai.com/index/gpt-5-5-instant",
  "date": "2026-05-05",
  "model": "GPT-5.5 Instant",
  "baseline": "GPT-5.3 Instant",
  "hallucination": {
    "high_stakes_reduction": "52.5%",
    "flagged_conversations_reduction": "37.3%"
  },
  "benchmark_gains": {
    "AIME_2025": "+15.8pp (65.4 → 81.2)",
    "GPQA": "+7.1pp (78.5 → 85.6)",
    "CharXiv": "+6.6pp (75.0 → 81.6)",
    "MMMU_Pro": "+6.8pp (69.2 → 76.0)",
    "OmniDocBench_error": "-2.1pp (14.6 → 12.5, lower better)"
  },
  "availability": "default ChatGPT model (all tiers); API as chat-latest"
}
```

---

## Architecture / Pattern Notes

### MoE Dominates Open-Weight Frontier
Both Kimi K2.6 (1T params, 32B active) and Llama 4 Scout/Maverick (17B active / 109–400B total) use Mixture-of-Experts. This is now the standard architecture for open-weight models that need to be locally deployable while matching closed-model performance. Dense models like Mistral Medium 3.5 (128B, no MoE) still exist but require substantially more VRAM.

### Reasoning Effort as a Dial
OpenAI has now exposed tunable reasoning effort across multiple product lines: GPT-5.5 and GPT-5.5 Instant (xhigh), GPT-Realtime-2 (minimal→xhigh). This pattern — one model, multiple quality/latency tiers set at inference time — is becoming standard and eliminates the need for separate "thinking" vs. "non-thinking" model variants.

### Voice-as-an-Interface Unbundling
GPT-Realtime-2/Translate/Whisper demonstrates purposeful model splitting: rather than one voice model handling all tasks, OpenAI deploys specialized sub-models for reasoning dialogue, real-time translation, and transcription. Each is priced and tuned independently. This should push competitors (Google, Anthropic) toward similar architectural splits in voice offerings.

### Open-Weight Frontier Has Converged (For Coding)
Five frontier-class open-weight models shipped in April–May 2026: Kimi K2.6, Mistral Medium 3.5, Llama 4 Scout/Maverick, DeepSeek V4 Pro, and Qwen 3.5/3.6. Kimi K2.6 and Mistral Medium 3.5 now exceed several closed frontier models on specific coding benchmarks. The open-to-closed capability gap is narrowing faster than the safety/alignment gap.

---

## Analysis & Impact

### GPT-5.5 Instant: What "Daily Driver" AI Means Now
ChatGPT's default model reaching 81.2% AIME 2025 accuracy (a score that would qualify a human for IMO consideration in many countries) as a *background* quality improvement — not a headline launch — is remarkable. Hundreds of millions of users now interact daily with a model that outperforms PhD-level humans on graduate-level science (85.6% GPQA), with 52.5% fewer hallucinations than its predecessor. The memory sources feature is the more strategically important addition: explicit, user-controllable personalization builds the kind of long-term contextual relationship that increases stickiness and differentiation vs. competitors.

### Voice AI Enters Production-Grade Agentic Phase
GPT-Realtime-2's 26-point call success lift at Zillow, BolnaAI's 12.5% WER improvement in Hindi/Tamil/Telugu, and Deutsche Telekom's multilingual deployment signal that real-time voice AI has crossed the production threshold. The pattern of "voice-to-action, systems-to-voice, voice-to-voice" that OpenAI outlined is a design language that will likely shape how the industry talks about voice AI use cases for the next year. Notably, none of the announced partners are purely AI-native — they're established businesses integrating voice AI into existing workflows.

### Kimi K2.6: The Chinese Open-Weight Moment
Kimi K2.6 defeating GPT-5.5 and Claude Opus 4.7 in a live coding tournament at 1/25th the cost of Opus 4.7 is a milestone that will accelerate enterprise experimentation with non-Western open-weight models. The model is already OpenAI and Anthropic SDK-compatible. The risk for Western API providers: cost-sensitive coding workloads may shift to Kimi K2.6 or DeepSeek V4 equivalents, eroding the mid-tier pricing tier just as GPT-5.5 pressures the high tier from above.

### GPQA Near Saturation — What Comes Next?
All four top frontier models (Mythos, Gemini 3.1 Pro, Opus 4.7, GPT-5.5) cluster within 1 percentage point on GPQA Diamond. The benchmark is functionally saturated for differentiation. The field is shifting toward harder targets: Humanity's Last Exam, SWE-bench Pro (still <80% for all models), MultiHaystack (where retrieval accuracy drops models to ~51%), and terminal/agentic benchmarks. Organizations relying on GPQA as a procurement signal should update their evaluation stack.

### Long-Context Retrieval Remains an Unsolved Problem
The MultiHaystack paper (arXiv:2603.05697) shows GPT-5's reasoning accuracy dropping from **80.86% with provided evidence** to **51.4% under top-5 retrieval from a 46K-item multimodal corpus**. A ~30-point performance cliff on retrieval-augmented tasks means RAG pipelines relying on model-side retrieval are substantially more error-prone than controlled benchmarks suggest. This has direct product implications for long-context enterprise deployments.

---

## Open-Weight Models Worth Running Locally

| Model | Params (Active) | Context | Highlight | Hardware | Recommended For |
|-------|----------------|---------|-----------|----------|-----------------|
| **Kimi K2.6** | 32B (1T total) | 256K | Best open SWE-bench Pro (58.6%); tournament winner | Cluster | Coding agents, cost-sensitive SWE work |
| **Mistral Medium 3.5** | 128B (dense) | 256K | Best open SWE-bench Verified (77.6%); multimodal | 4×H100 FP8 | Production coding + vision tasks |
| **Llama 4 Scout** | 17B (109B total) | 10M | Single H100; 10M context; multimodal | 1×H100 | Long-context, RAG, multimodal on single node |
| **DeepSeek V4 Pro (Max)** | ~37B active | 1M | Best open overall on BenchLM coding (88/100) | Cluster | General reasoning + coding |
| **DeepSeek V4 Flash** | 13B active | 1M | $0.14/$0.28 via API; reasoning-capable | Single GPU (via API) | Budget agentic tasks |
| **Qwen 3.6 35B-A3B** | 3B active | 262K | $0.00 via API; competitive with GPT-4-class | Single GPU | Free-tier coding and reasoning |
| **Gemma 4 26B** | 26B | 262K | Free, Google-backed; strong on benchmarks | Consumer GPU (quantized) | Local experimentation |

---

## Key Takeaways TL;DR

1. **GPT-5.5 Instant (May 5)** is now ChatGPT's default model: 52.5% fewer hallucinations, +15.8pp AIME, +7.1pp GPQA vs. its predecessor — the biggest Instant-tier jump in ChatGPT history.
2. **GPT-Realtime-2 (May 7, today)** is the first voice model with GPT-5-class reasoning: +15pp Big Bench Audio, 128K context, parallel tool calls — voice AI enters true agentic territory.
3. **Kimi K2.6 won a live coding contest** over GPT-5.5 and Claude Opus 4.7 on May 3, reinforcing that the best open-weight coder is now competitive with closed frontier models at 1/25th the price.
4. **GPT-5.3 Codex** is now #2 on SWE-bench Pro with 77.3% — the highest open-weight coding score ever; the open/closed gap on coding is narrowing fast.
5. **GPQA Diamond is functionally saturated** (<1pp separates the top 4 frontier models); meaningful differentiation now requires harder benchmarks (SWE-bench Pro, MultiHaystack, Terminal-Bench).
6. **Long-context retrieval is still broken**: MultiHaystack shows a ~30pp accuracy cliff when models must retrieve from large corpora vs. being handed evidence — critical signal for RAG-reliant products.
7. **Open-weight frontier landscape (April–May 2026):** Kimi K2.6, Mistral Medium 3.5, Llama 4, DeepSeek V4, Qwen 3.5/3.6 — five credible frontier-class open models in one month.

---

## Sources

| # | Title | URL | Date |
|---|-------|-----|------|
| 1 | GPT-5.5 Instant: smarter, clearer, and more personalized | https://openai.com/index/gpt-5-5-instant/ | 2026-05-05 |
| 2 | Advancing voice intelligence with new models in the API | https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/ | 2026-05-07 |
| 3 | OpenAI claims ChatGPT's new default model hallucinates way less | https://www.theverge.com/ai-artificial-intelligence/924225/openai-chatgpt-default-model-gpt-5-5-instant | 2026-05-05 |
| 4 | Kimi K2.6: Open-Source Just Beat GPT-5.5 at Coding | https://www.buildfastwithai.com/blogs/kimi-k2-6-review-benchmarks | 2026-05 |
| 5 | Kimi K2-6 Just Beat GPT-5-5 and Claude in a Viral Coding Test | https://moony01.com/ai/2026/05/03/kimi-k26-coding-test.html | 2026-05-03 |
| 6 | BenchLM AI Coding Leaderboard | https://benchlm.ai/coding | Updated 2026-05-07 |
| 7 | Mistral Medium 3.5 brings reasoning, coding and vision into one open model | https://www.i-scoop.eu/mistral-medium-3-5/ | 2026-04-29 |
| 8 | Mistral Medium 3.5 Benchmarks | https://benchlm.ai/models/mistral-medium-3-5-128b | 2026 |
| 9 | GPT-5.5 Instant System Card — Hallucinations | https://deploymentsafety.openai.com/gpt-5-5-instant/hallucinations | 2026-05-05 |
| 10 | GPQA Benchmark 2026: 46 LLM scores | https://benchlm.ai/benchmarks/gpqa | 2026-05 |
| 11 | Reasoning Benchmarks: GPQA, AIME, and Humanity's Last Exam | https://awesomeagents.ai/leaderboards/reasoning-benchmarks-leaderboard/ | 2026-05 |
| 12 | LMSys Arena Leaderboard | https://lmarena.ai/leaderboard/ | 2026-04 |
| 13 | LongBench v2 Benchmark 2026 | https://benchlm.ai/benchmarks/longBenchV2 | 2026-05 |
| 14 | MultiHaystack: Benchmarking Multimodal Retrieval | https://arxiv.org/abs/2603.05697v1 | 2026-03 |
| 15 | Best Open-Source LLM May 2026 | https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/ | 2026-05 |
| 16 | OpenAI unveils trio of realtime audio models | https://www.neowin.net/news/openai-unveils-trio-of-realtime-audio-models-to-power-next-gen-voice-agents/ | 2026-05-07 |
| 17 | AI API Pricing Comparison 2026 | https://www.aipricing.guru/blog/ai-api-pricing-comparison-2026/ | 2026 |
| 18 | LLM API Pricing Comparison 2026 | https://benchlm.ai/pricing | 2026-05 |
