# Best Models & Benchmarks — 2026-05-08

## Top Model News (5)

### 1. DeepSeek V4 — 1.6T-Parameter MoE at 1/7th the Cost of Opus 4.7, Leads LiveCodeBench

**Source:** [Morph LLM Guide](https://www.morphllm.com/deepseek-v4) | [Awesome Agents Review](https://awesomeagents.ai/models/deepseek-v4/) | [NVIDIA Dev Blog](https://developer.nvidia.com/blog/build-with-deepseek-v4-using-nvidia-blackwell-and-gpu-accelerated-endpoints) | [Benchmarks](https://deepseekai.guide/news/deepseek-benchmarks-2026/)

DeepSeek V4 launched April 24, 2026 as a pair of MIT-licensed Mixture-of-Experts models: V4-Pro (1.6T total / 49B active parameters) and V4-Flash (284B total / 13B active). Both support 1M-token context windows and are released under MIT license. The flagship V4-Pro scores 93.5% on LiveCodeBench in max reasoning mode — the highest of any model tested on that benchmark — while matching or exceeding Gemini 3.1 Pro and Claude Opus 4.6 on SWE-bench Verified (80.6%) at a fraction of the price.

The architectural innovation driving this efficiency is a novel hybrid attention mechanism combining Compressed Sparse Attention (CSA) with Heavily Compressed Attention (HCA), achieving 27% of V3.2's inference FLOPs and only 10% of its KV cache at 1M-token context. The model also introduces Manifold-Constrained Hyper-Connections (mHC) replacing standard residual connections, and uses FP4 quantization for MoE expert weights with FP8 elsewhere. Training employed the Muon optimizer for faster convergence.

At $1.74/$3.48 per million input/output tokens for V4-Pro (and just $0.14/$0.28 for V4-Flash), DeepSeek continues to reset expectations for price-performance. V4-Pro delivers comparable coding benchmark scores to Claude Opus 4.7 ($5/$25 per M tokens) at ~7× lower cost, representing a major challenge to closed-source model monetization strategies.

**Key specs:** 1M token context | Text + code | V4-Pro: $1.74/$3.48 per 1M tokens; V4-Flash: $0.14/$0.28 per 1M tokens | MIT license | Available via API and open weights on Hugging Face

---

### 2. Claude Mythos Preview — Anthropic's Unreleased Research Frontier Sets New Ceiling on SWE-bench

**Source:** [Anthropic Red Team](https://red.anthropic.com/2026/mythos-preview/) | [RD World Online](https://www.rdworldonline.com/claude-mythos-leads-17-of-18-benchmarks-anthropic-measured-muse-spark-put-meta-back-in-the-frontier-club-and-openais-spud-model-is-reportedly-near-launch/) | [BenchLM](https://benchlm.ai/models/claude-mythos-preview)

Claude Mythos Preview, announced April 7, 2026, is Anthropic's most capable model to date but is being held back from public release due to safety concerns — specifically, it can autonomously find zero-day vulnerabilities in both open-source and closed-source software and develop proof-of-concept exploits with minimal human steering. It leads 17 of 18 benchmarks Anthropic measured, with a 93.9% SWE-bench Verified score (vs. 80.8% for Opus 4.6) and 97.6% on USAMO 2026 mathematics (vs. 42.3% for Opus 4.6 — a 2.3× leap). Cybench is fully saturated at 100%.

The model's release strategy reflects Anthropic's ASL-4 safety framework kicking in for the first time in practice. The capability jump from Opus 4.6 to Mythos is described internally as larger than the jump from Claude 2 to Claude 3 Opus. While pricing ($25/$125 per M tokens) is published, access remains limited to red-teamers and selected research partners as of today.

The significance of Mythos extends beyond benchmarks: it signals that the next capability frontier is primarily gated by safety evaluation timelines rather than training compute. This previews a world where the most capable model is not the one in production, and the gap between frontier and deployed models will widen as labs apply more rigorous safety thresholds before general availability.

**Key specs:** 1M token context | Text + multimodal | $25/$125 per 1M tokens | Research preview only; no public API | #1 on BenchLM provisional leaderboard (99/100)

---

### 3. GPT-5.5 — OpenAI's First Full Retrain Since GPT-4.5 Leads Terminal-Bench and SWE-bench

**Source:** [OpenAI Blog](https://openai.com/index/introducing-gpt-5-5/) | [BenchLM](https://benchlm.ai/models/gpt-5-5) | [Enter.Pro](https://enter.pro/page/en-US/news/gpt-5-5-benchmarks-swe-bench-hallucination-drop)

GPT-5.5, released April 23, 2026, is OpenAI's first fully retrained base model since GPT-4.5, designed to push the frontier across agentic coding, computer use, and scientific research. It achieves 88.7% on SWE-bench Verified, 82.7% on Terminal-Bench 2.0 (leading all public models), and 93.6% on GPQA Diamond. Critically, it cuts hallucination rate by 60% relative to GPT-5.4 and uses approximately 40% fewer output tokens on equivalent tasks — making it meaningfully more cost-efficient at equivalent quality.

The model features a 1.05M-token context window and native multimodal support across text, images, audio, and video. It excels particularly in agentic tasks (98.2/100 on BenchLM's agentic score) and reasoning (96.5/100), and achieves 78.7% on OSWorld-Verified for computer-use tasks. It is currently available to Plus, Pro, Business, and Enterprise ChatGPT users and in Codex, with API deployment rolled out as of late April.

At $5/$30 per million input/output tokens, GPT-5.5 is priced identically to Claude Opus 4.7 on input but meaningfully more expensive on output. The 40% token efficiency gain partially offsets the sticker price. The Arena Elo of ~1,475 places it in the mid-tier of the current leaderboard — behind Claude Opus 4.7 Thinking (~1,505) but ahead of most open-weight competitors.

**Key specs:** 1,050,000 token context | Text, image, audio, video | $5.00/$30.00 per 1M tokens (cached: $0.50) | Proprietary | Available in ChatGPT and API

---

### 4. Meta Muse Spark — Meta's First Closed Frontier Model Rejoins Top-5

**Source:** [Meta AI Blog](https://ai.meta.com/blog/introducing-muse-spark-1-msl/) | [Artificial Analysis](https://artificialanalysis.ai/articles/muse-spark-everything-you-need-to-know) | [The Decoder](https://the-decoder.com/metas-muse-spark-is-its-first-frontier-model-and-its-first-without-open-weights/)

Released April 8, 2026 by Meta Superintelligence Labs, Muse Spark marks Meta's return to the frontier tier after roughly a year of open-weight-focused work post-Llama 4. The model scores 52 on the Artificial Analysis Intelligence Index (placing 4th), leads all models on HealthBench Hard (42.8 vs. GPT-5.4's 40.1), and achieves 50.2% on Humanity's Last Exam in "Contemplating" mode — a multi-agent orchestration approach that runs parallel reasoning chains. On MMMU-Pro (multimodal reasoning), it scores 80.5%, second only to Gemini 3.1 Pro.

In a pivotal strategic shift, Muse Spark is Meta's first model released without open weights — a break from the Llama tradition. The move signals that Meta's Superintelligence Labs is prioritizing frontier capability and commercial deployment over the open-source ecosystem that Llama built. The model is currently free at meta.ai with a 262K token context window, with API access in private preview only.

The "Contemplating" multi-agent mode, which orchestrates multiple parallel agents to tackle complex tasks, achieved 58% on FrontierScience Research — suggesting Meta is investing in test-time compute scaling rather than just larger base models. However, the lack of SWE-bench scores and the closed-API status makes direct coding comparisons difficult for now.

**Key specs:** 262K token context | Text + multimodal (visual chain of thought) | Free (meta.ai); API in private preview | Proprietary, no open weights | Released April 8, 2026

---

### 5. Gemini 3.1 Flash-Lite GA — Google's Fastest Production Model Now Generally Available

**Source:** [Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) | [Google DeepMind Model Card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite) | [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)

Gemini 3.1 Flash-Lite reached general availability on May 7, 2026 (the day before this digest), completing Google's Flash-Lite preview rollout that began March 3, 2026. The model delivers 2.5× faster time-to-first-token and 45% higher output throughput compared to Gemini 2.5 Flash, at $0.25/$1.50 per million tokens — making it Google's most cost-effective production-ready model. Despite the speed and cost focus, it achieves 86.9% on GPQA Diamond and 76.8% on MMMU-Pro, outperforming many larger models.

The model supports up to 1M-token context windows with full multimodal inputs: text, code, images (up to 3,000 per prompt), video (up to ~45 minutes with audio), audio (up to 8.4 hours), and PDFs. It includes flexible reasoning levels (minimal, low, medium, high) for dynamic quality-latency tradeoffs, making it ideal as an orchestration backbone in multi-agent systems where sub-second responsiveness matters more than peak accuracy.

As the GA release of an already-previewed model, Flash-Lite's importance is operational: enterprises can now commit production workloads to it with SLA guarantees. Google's strategy of tiering Flash-Lite (speed/cost), Flash (balanced), and Pro (frontier) gives developers a clear path to optimize each call in an agentic pipeline independently — a model-routing architecture that aligns well with how production AI systems are actually built in 2026.

**Key specs:** 1M token input / 64K token output context | Text, images, audio, video, PDF, code | $0.25/$1.50 per 1M tokens | Proprietary | Generally available on Gemini API, Vertex AI, Google AI Studio

---

## Deep Dive: Most Important Release — DeepSeek V4 (April 24, 2026)

DeepSeek V4 is the defining model event of the current moment because it simultaneously sets the new high-water mark for coding benchmarks (93.5% LiveCodeBench), demonstrates that a fully open-weight MIT-licensed model can match frontier closed models on SWE-bench at 80.6%, and undercuts the nearest proprietary competitor (Claude Opus 4.7) by ~7× on price for comparable coding performance. In an era where the frontier was thought to require closed-model pricing to sustain, V4 challenges that assumption at scale.

### What It Can Do

DeepSeek V4-Pro handles agentic software engineering tasks end-to-end, including multi-file repository edits, terminal command execution, and test-driven debugging loops. Its 1M-token context allows it to ingest entire codebases without chunking. In max reasoning mode, it achieves 90.1% on GPQA Diamond (rivaling proprietary models on expert-level science questions), 93.5% LiveCodeBench, and 80.6% SWE-bench Verified. The V4-Flash variant at $0.14/$0.28 per M tokens delivers 91.6% LiveCodeBench — a score that would have been frontier-class just 90 days ago — at essentially commodity pricing.

### Benchmark Highlights

| Benchmark | DeepSeek V4-Pro | Previous Best (Public) |
|---|---|---|
| LiveCodeBench | **93.5%** | DeepSeek V3.2: ~89.6% |
| GPQA Diamond | 90.1% | Claude Opus 4.7: 94.2% |
| SWE-bench Verified | 80.6% | Claude Opus 4.6: 80.8% |
| AIME 2026 (est.) | ~92% | Kimi K2.6: 96.4% |
| Terminal-Bench 2.0 | 67.9% | GPT-5.5: 82.7% |
| Intelligence Index | 51.5 | Claude Opus 4.7: 57.3 |

### Architecture (known)

DeepSeek V4-Pro is a 1.6-trillion-parameter Mixture-of-Experts model with 49B active parameters per token, organized across 61 transformer layers with 384 total experts (up from 256 in V3) selecting 6 per token. The first 3 layers use hash-based routing; subsequent layers use standard top-k routed MoE with the `noaux_tc` auxiliary-loss-free load balancing and `sqrtsoftplus` scoring. The attention architecture is a three-way hybrid: sliding-window attention for local context, Compressed Sparse Attention (CSA, m=4) for medium range, and Heavily Compressed Attention (HCA, m'=128) for ultra-long-range dependencies — together achieving 27% of V3.2's per-token FLOPs and 10% of its KV cache at 1M-token context. Residual connections are replaced by Manifold-Constrained Hyper-Connections (mHC) using Sinkhorn-Knopp iterations. Training used the Muon optimizer with FP4 quantization for MoE experts and FP8 elsewhere. Pre-training dataset: 32+ trillion tokens. Post-training: two-stage domain-specific expert cultivation followed by on-policy distillation.

### Pricing & Availability

| Variant | Input | Output | Context |
|---|---|---|---|
| V4-Pro | $1.74/1M | $3.48/1M | 1M tokens |
| V4-Flash | $0.14/1M | $0.28/1M | 1M tokens |

Both models are MIT-licensed and available as open weights on Hugging Face, and via the DeepSeek API. NVIDIA Blackwell-optimized endpoints are available through NVIDIA's GPU-accelerated inference infrastructure.

### Strategic Significance

DeepSeek V4 represents the clearest evidence yet that the open-weight frontier is closing the gap with closed models on tasks that matter commercially. Its MIT license means any company can self-host it, fine-tune it, and deploy it without API dependency — a critical consideration for enterprises concerned about data privacy, latency SLAs, or cost predictability at scale. The V4-Flash variant at $0.14/$0.28 is particularly significant: it allows developers to route the majority of coding calls to a near-frontier model at 3–4% of Opus 4.7's cost, reserving expensive models for only the most complex tasks.

The architectural choices also matter beyond benchmarks. The 10% KV cache footprint of V4-Pro vs. V3.2 means dramatically reduced memory pressure at long context, enabling inference on GPU configurations that could not previously serve 1M-token models economically. Combined with the 27% FLOP reduction, V4-Pro is likely to see rapid adoption on third-party inference providers (Together AI, Fireworks, DigitalOcean, Groq) that compete on throughput efficiency.

The strategic challenge for OpenAI and Anthropic is stark: GPT-5.5 and Claude Opus 4.7 remain ahead on most benchmarks, but the gap is now measured in single-digit percentage points on key metrics while the price gap is measured in multiples of 5–10×. The question for the next 6 months is whether closed-model providers can differentiate on safety guarantees, reliability, multimodal depth, or agentic integrations — because raw benchmark performance is no longer a sufficient moat.

### Competitive Context

On LiveCodeBench, V4-Pro's 93.5% leads all models including Claude Opus 4.7 (78.5%), GPT-5.5 (est. ~84%), and Gemini 3.1 Pro. On SWE-bench Verified, V4-Pro (80.6%) is essentially tied with Claude Opus 4.6 (80.8%) and Gemini 3.1 Pro (80.6%), with only Claude Opus 4.7 (87.6%) and Claude Mythos Preview (93.9%, not publicly available) ahead. On GPQA Diamond, V4-Pro (90.1%) trails Gemini 3.1 Pro (94.3%), Claude Opus 4.7 (94.2%), and GPT-5.5 (93.6%) — scientific reasoning remains a relative weakness. On Terminal-Bench 2.0, V4-Pro (67.9%) lags GPT-5.5 (82.7%) and Claude Opus 4.7 (69.4%) — agentic terminal tasks favor models with more extensive RLHF on tool use. The V4-Flash at $0.14/$0.28 with 91.6% LiveCodeBench has no close competitor in its price tier.

---

## Benchmark Comparison Data

```json
{"benchmark": "Intelligence Index (Artificial Analysis)", "date": "2026-05-07", "results": [{"model": "Claude Opus 4.7", "score": 57.3}, {"model": "Gemini 3.1 Pro", "score": 57.2}, {"model": "GPT-5.4", "score": 56.8}, {"model": "GPT-5.5 (xhigh)", "score": 60.0}, {"model": "MiMo-V2.5-Pro", "score": 53.8}, {"model": "GPT-5.3 Codex", "score": 53.6}, {"model": "Muse Spark", "score": 52.0}, {"model": "DeepSeek V4 Pro", "score": 51.5}, {"model": "GLM-5.1", "score": 51.4}, {"model": "Qwen3.6 Plus", "score": 50.0}]}
```

```json
{"benchmark": "GPQA Diamond", "date": "2026-04-28", "results": [{"model": "Claude Mythos Preview", "score": 94.5}, {"model": "Gemini 3.1 Pro", "score": 94.3}, {"model": "Claude Opus 4.7", "score": 94.2}, {"model": "GPT-5.5", "score": 93.6}, {"model": "GPT-5.4", "score": 92.8}, {"model": "Claude Opus 4.6", "score": 91.3}, {"model": "Gemini 3 Pro", "score": 91.9}, {"model": "Kimi K2.6", "score": 90.5}, {"model": "DeepSeek V4 Pro", "score": 90.1}, {"model": "DeepSeek V4 Flash", "score": 88.1}, {"model": "Muse Spark", "score": 88.4}, {"model": "Gemini 3.1 Flash-Lite", "score": 86.9}, {"model": "Qwen3.6-35B-A3B", "score": 86.0}]}
```

```json
{"benchmark": "SWE-bench Verified", "date": "2026-05-07", "results": [{"model": "Claude Mythos Preview", "score": 93.9}, {"model": "GPT-5.5", "score": 88.7}, {"model": "Claude Opus 4.7", "score": 87.6}, {"model": "GPT-5.3 Codex", "score": 85.0}, {"model": "Claude Opus 4.5", "score": 80.9}, {"model": "Claude Opus 4.6", "score": 80.8}, {"model": "Gemini 3.1 Pro", "score": 80.6}, {"model": "DeepSeek V4 Pro", "score": 80.6}, {"model": "MiniMax M2.5", "score": 80.5}, {"model": "Qwen3.6-35B-A3B", "score": 73.4}]}
```

```json
{"benchmark": "LiveCodeBench", "date": "2026-05-07", "results": [{"model": "DeepSeek V4 Pro (Max)", "score": 93.5}, {"model": "DeepSeek V4 Flash (Max)", "score": 91.6}, {"model": "Gemini 3 Pro Preview", "score": 91.7}, {"model": "Gemini 3 Flash Preview (Reasoning)", "score": 90.8}, {"model": "DeepSeek V3.2 Speciale", "score": 89.6}, {"model": "DeepSeek V4 Pro (High)", "score": 89.8}, {"model": "Claude Opus 4.7", "score": 78.5}, {"model": "Kimi K2.6", "score": 78.2}, {"model": "Gemma 4 26B (Thinking)", "score": 77.1}]}
```

```json
{"benchmark": "AIME 2026", "date": "2026-04-28", "results": [{"model": "Kimi K2.6", "score": 96.4}, {"model": "GLM-5", "score": 95.8}, {"model": "Kimi K2.5", "score": 95.8}, {"model": "GLM 5.1 (Thinking)", "score": 95.3}, {"model": "Qwen 3.6 Plus Preview (Thinking)", "score": 95.3}, {"model": "Claude Opus 4.5 (Thinking)", "score": 93.3}, {"model": "GLM-4.7 (Thinking)", "score": 92.9}, {"model": "DeepSeek V3.2 (Thinking)", "score": 92.7}, {"model": "Qwen3.5-397B-A17B (Thinking)", "score": 91.3}, {"model": "Gemma 4 26B (Thinking)", "score": 88.3}]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "date": "2026-05-07", "results": [{"model": "GPT-5.5", "score": 82.7}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 69.4}, {"model": "MiMo-V2.5-Pro", "score": 68.4}, {"model": "DeepSeek V4 Pro (Max)", "score": 67.9}, {"model": "Moonshot AI (Kimi K2.6)", "score": 66.7}, {"model": "Gemini 3.1 Pro Preview", "score": 67.4}, {"model": "GPT-5.3 Codex", "score": 64.1}, {"model": "Claude Sonnet 4.6", "score": 59.6}]}
```

```json
{"benchmark": "LMSys Chatbot Arena ELO (Overall)", "date": "2026-05-07", "results": [{"model": "Claude Opus 4.7 Thinking", "score": 1505}, {"model": "Claude Opus 4.6 Thinking", "score": 1503}, {"model": "Claude Opus 4.7", "score": 1498}, {"model": "Claude Opus 4.6", "score": 1497}, {"model": "Gemini 3.1 Pro Preview", "score": 1492}, {"model": "Grok 4.20 Beta", "score": 1485}, {"model": "Gemini 3 Pro", "score": 1485}, {"model": "GPT-5.5", "score": 1475}, {"model": "DeepSeek R1", "score": 1450}]}
```

```json
{"benchmark": "ARC-AGI-3 (Interactive Agent Score)", "date": "2026-05-07", "results": [{"model": "Purpose-built system (best)", "score": 12.58}, {"model": "GPT-5.4", "score": 0.37}, {"model": "Claude Opus 4.6", "score": 0.30}, {"model": "Grok 4.2", "score": 0.25}, {"model": "Human baseline", "score": 100.0}]}
```

```json
{"benchmark": "MMLU", "date": "2026-04-28", "results": [{"model": "Claude Opus 4.7", "score": 89.8}, {"model": "Claude Mythos Preview", "score": 92.7}, {"model": "GPT-5.5", "score": 92.4}, {"model": "Gemini 3.1 Flash-Lite", "score": 76.8}, {"model": "Gemma 4 26B A4B (Thinking)", "score": 85.2}]}
```

```json
{"benchmark": "Humanity's Last Exam (HLE)", "date": "2026-04-28", "results": [{"model": "Muse Spark (Contemplating mode)", "score": 50.2}, {"model": "Gemini 3.1 Pro Preview", "score": 48.5}, {"model": "GPT-5.4", "score": 46.3}, {"model": "Muse Spark (standard)", "score": 39.9}, {"model": "Claude Opus 4.6", "score": 38.2}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Mythos Preview | Anthropic | 1M | $25.00 | $125.00 | Text, Image (research preview only) |
| GPT-5.5 | OpenAI | 1.05M | $5.00 | $30.00 | Text, Image, Audio, Video |
| Claude Opus 4.7 | Anthropic | 1M | $5.00 | $25.00 | Text, Image |
| Gemini 3.1 Pro | Google | 1M | $2.00 | $12.00 | Text, Image, Audio, Video, PDF |
| DeepSeek V4 Pro | DeepSeek | 1M | $1.74 | $3.48 | Text, Code |
| Muse Spark | Meta | 262K | Free (API: private preview) | — | Text, Image |
| Claude Opus 4.6 | Anthropic | 1M | $5.00 | $25.00 | Text, Image |
| GPT-5.4 | OpenAI | ~400K | $3.50 | $21.00 | Text, Image, Audio |
| GPT-5.3 Codex | OpenAI | 200K | $2.50 | $15.00 | Text, Code |
| Qwen3.5-397B-A17B | Alibaba | 1M | ~$0.80 | ~$2.40 | Text, Image, Code |
| DeepSeek V4 Flash | DeepSeek | 1M | $0.14 | $0.28 | Text, Code |
| Gemini 3.1 Flash | Google | 1M | $0.50 | $3.50 | Text, Image, Audio, Video |
| Gemini 3.1 Flash-Lite | Google | 1M (64K out) | $0.25 | $1.50 | Text, Image, Audio, Video |
| Qwen3.6-35B-A3B | Alibaba | 128K | ~$0.20 | ~$0.60 | Text, Code |
| Gemma 4 26B A4B | Google | 128K | Open (self-host) | Open | Text, Image |
| Llama 4 Maverick | Meta | 1M | Open (self-host) | Open | Text, Image |

---

## Analysis & Impact

- **For software engineering / coding:** DeepSeek V4-Flash at $0.14/$0.28 per M tokens now delivers ~91.6% LiveCodeBench — making frontier-class automated code generation accessible at commodity pricing. Teams should route day-to-day PR review, completion, and boilerplate tasks to V4-Flash, reserving Claude Opus 4.7 (87.6% SWE-bench Verified) or GPT-5.5 (88.7%) for complex multi-file agentic sessions. Claude Mythos Preview's unreleased 93.9% SWE-bench score signals where the ceiling will be in 6–12 months.

- **For frontier reasoning / math / science:** AIME 2026 is nearly saturated at the top: Kimi K2.6 (96.4%), GLM-5 (95.8%), and multiple models above 92%. The differentiation has shifted to GPQA Diamond (still 4–5pp spread between 94.5% and 90%) and Humanity's Last Exam (meaningful 10pp+ spread). Muse Spark's Contemplating mode achieving 50.2% HLE via multi-agent orchestration suggests that test-time compute scaling — not just larger base models — is the near-term lever for frontier science reasoning.

- **For multimodal / video / audio work:** Gemini 3.1 Pro remains the gold standard for multimodal tasks (82.4% MMMU-Pro, 2M effective context, ~45-min video, 8.4-hr audio per prompt) at $2/$12 per M tokens. GPT-5.5 adds audio and video modalities at higher cost ($5/$30). Muse Spark leads on HealthBench Hard (42.8) and CharXiv Reasoning (86.4%), suggesting specialized strengths in medical and scientific chart understanding. Gemini 3.1 Flash-Lite now GA at $0.25/$1.50 is the right default for high-volume multimodal pipelines where 86.9% GPQA is sufficient.

- **For cost-sensitive or open-source deployments:** DeepSeek V4 (MIT license) and Gemma 4 26B A4B (Apache 2.0) are the two most compelling self-hosted options. V4-Pro's architecture (27% FLOPs, 10% KV cache vs. V3.2) makes it tractable on smaller GPU clusters for long-context tasks. Qwen3.5-397B-A17B (now available via SageMaker JumpStart) covers the 1M-token multimodal use case in the open-weight tier. Llama 4 Maverick holds the leading open-weights position on most general-purpose benchmarks but trails on coding-specific tasks.

- **The test-time compute scaling is now table stakes:** Every major frontier model in 2026 ships with tiered reasoning modes (Gemini 3.1's minimal/low/medium/high, Claude's xhigh effort level, DeepSeek's Max Reasoning Mode). The bare base-model-without-thinking is no longer what gets benchmarked or marketed. This has practical implications: reported benchmark scores increasingly reflect "max compute" settings that may not match production cost budgets, and users must specify reasoning intensity per call to control cost. The 2026 model market is as much about reasoning budget management as it is about raw model selection.

---

## Key Takeaways (TL;DR)

- DeepSeek V4-Pro leads LiveCodeBench at 93.5% with an MIT license, matching Gemini 3.1 Pro on SWE-bench Verified (80.6%) at ~7× lower cost than Claude Opus 4.7.
- Claude Mythos Preview scores 93.9% on SWE-bench Verified — the highest of any model — but Anthropic is withholding it from release after it demonstrated autonomous zero-day exploit development.
- GPT-5.5 leads Terminal-Bench 2.0 (82.7%) and cuts hallucination by 60% vs. GPT-5.4, but at $30/M output tokens it is the most expensive standard-tier model available.
- Gemini 3.1 Flash-Lite reached GA on May 7, delivering 86.9% GPQA Diamond at $0.25/$1.50 per M tokens with 2.5× faster throughput than Gemini 2.5 Flash.
- ARC-AGI-3's interactive agent format has reset the benchmark ceiling: frontier models score below 0.4%, while humans score 100%, exposing a fundamental gap in adaptive real-time reasoning that raw scale alone has not closed.

---

*Sources:*
- https://www.morphllm.com/deepseek-v4
- https://awesomeagents.ai/models/deepseek-v4/
- https://developer.nvidia.com/blog/build-with-deepseek-v4-using-nvidia-blackwell-and-gpu-accelerated-endpoints
- https://deepseekai.guide/news/deepseek-benchmarks-2026/
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- https://lab.feimatrix.com/technical-analysis-report-deepseek-v4-pro/
- https://red.anthropic.com/2026/mythos-preview/
- https://www.rdworldonline.com/claude-mythos-leads-17-of-18-benchmarks-anthropic-measured-muse-spark-put-meta-back-in-the-frontier-club-and-openais-spud-model-is-reportedly-near-launch/
- https://benchlm.ai/models/claude-mythos-preview
- https://openai.com/index/introducing-gpt-5-5/
- https://benchlm.ai/models/gpt-5-5
- https://enter.pro/page/en-US/news/gpt-5-5-benchmarks-swe-bench-hallucination-drop
- https://www.llmreference.com/model/gpt-5.5
- https://openai.com/api/pricing
- https://ai.meta.com/blog/introducing-muse-spark-1-msl/
- https://artificialanalysis.ai/articles/muse-spark-everything-you-need-to-know
- https://the-decoder.com/metas-muse-spark-is-its-first-frontier-model-and-its-first-without-open-weights/
- https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available
- https://deepmind.google/models/model-cards/gemini-3-1-flash-lite
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/
- https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-pro-on-gemini-cli-gemini-enterprise-and-vertex-ai
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/
- https://pricepertoken.com/pricing-page/model/google-gemini-3.1-pro-preview
- https://anthropic.com/claude/opus
- https://www.anthropic.com/news/claude-opus-4-7
- https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- https://llm-stats.com/blog/research/claude-opus-4-7-launch
- https://arcprize.org/leaderboard
- https://medium.com/@AdithyaGiridharan/arc-agi-3-dropped-and-frontier-ai-scored-less-than-1-90cd70e65a61
- https://benchlm.ai/benchmarks/terminalBench2
- https://www.tbench.ai/leaderboard/terminal-bench/2.0
- https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
- https://artificialanalysis.ai/leaderboards/models
- https://benchlm.ai/benchmarks/liveCodeBench
- https://artificialanalysis.ai/evaluations/livecodebench
- https://llm-stats.com/benchmarks/aime-2026
- https://benchlm.ai/benchmarks/aime2026
- https://deepmind.google/blog/gemma-4-byte-for-byte-the-most-capable-open-models
- https://benchlm.ai/benchmarks/sweVerified
- https://www.swebench.com/verified
- https://mwpro.co.uk/blog/2026/05/06/4-new-qwen-models-for-multimodal-reasoning-agentic-coding-and-multilingual-applications-are-now-available-in-amazon-sagemaker-jumpstart/
- https://www.pereiraraphael.com.br/en/blog/compact-ai-models-deepseek-qwen-production/
- https://digitalmindnews.com/companies/openai/deepseek-v4-achieves-near-state-of-art-ai-reasoning-at-16th-cost/
- https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models/
