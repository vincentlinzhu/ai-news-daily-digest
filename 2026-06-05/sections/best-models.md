# Best Models & Benchmarks — 2026-06-05

## Top Model News (5)

### 1. Gemini 3.5 Flash — Google ships frontier agentic Flash model at I/O 2026, beats prior Pro on real-work benchmarks
**Source:** [Google Blog](https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/) | [Google AI Dev Docs](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash) | [DeepMind Model Card](https://deepmind.google/models/model-cards/gemini-3-5-flash/) | [LLM Stats](https://llm-stats.com/blog/research/gemini-3.5-flash-launch)

Released on May 19, 2026 at Google I/O, Gemini 3.5 Flash is the first model in Google's new 3.5 family — and the most capable Flash-class model Google has ever shipped. In a striking inversion, it outperforms the previous-generation flagship Gemini 3.1 Pro on 11 of 15 published benchmarks: scoring 76.2% on Terminal-Bench 2.1 (vs. 70.3%), 83.6% on MCP Atlas (vs. 78.2%), 1,656 Elo on GDPval-AA (vs. 1,314), and 57.9% on Finance Agent v2 (vs. 43.0%). The implicit message from Google: "fast" and "capable" are no longer trade-offs.

The model is natively multimodal — text, image, video, audio, and PDF inputs in a single call — and is designed for agentic sub-agent deployment, multi-step workflows, and long-horizon coding loops. It ships with integrated thinking (defaulting to medium effort), built-in search grounding, code execution, and function calling. Notably, Computer Use is not yet supported. Its 1M-token context window and 65K output ceiling make it well-suited for large codebase analysis. Flash outputs tokens roughly 4× faster than other frontier models at its pricing tier. Gemini 3.5 Pro, announced simultaneously, remains in internal testing with GA expected any day in June — Google has confirmed a 2M-token context window, Deep Think reasoning, and a likely ~$15/$60 per 1M pricing tier for Pro.

The broader strategic move is clear: Google is converging Flash-tier speed with Pro-tier capability, while positioning 3.5 Pro as the ceiling for deep-reasoning and long-document tasks. The 342-point swing on GDPval-AA (1,656 vs. 1,314 for the previous Pro) is the sharpest agentic performance delta in Google's model history and puts 3.5 Flash in direct competition with GPT-5.5 and Claude Opus 4.8 for production agent deployments at a fraction of the cost.

**Key specs:** 1M tokens input / 65K output | Text, Image, Video, Audio, PDF | $1.50 input / $9.00 output per 1M tokens ($0.15 cached) | Proprietary | GA via Gemini API, AI Studio, Vertex AI, Android Studio

---

### 2. Qwen3.7-Plus — Alibaba launches multimodal agent model with 1M context at 60% below sibling price
**Source:** [VentureBeat](https://venturebeat.com/technology/alibabas-qwen3-7-plus-supports-text-video-and-imagery-inputs-at-low-cost-of-0-4-1-6-per-1m-token-but-its-proprietary) | [Alibaba Meta AI Labs](https://metaailabs.com/alibabas-qwen-team-launches-qwen3-7-plus-adding-vision-deep-reasoning-tool-invocation-and-autonomous-iteration-on-the-bailian-platform/) | [APIdog](https://apidog.com/blog/qwen-3-7-plus/) | [Qwen Cloud](https://www.qwencloud.com/models/qwen3.7-plus)

Released on June 1–3, 2026, Qwen3.7-Plus is Alibaba's multimodal agent flagship — the visual and agentic expansion of the text-only Qwen3.7-Max launched on May 20. Plus ingests images, videos (up to 2 hours), and text through an early-fusion architecture (vision and language trained jointly from layer one), enabling genuine GUI grounding: it can interpret screenshots and produce precise on-screen coordinates, scoring 79.0 on ScreenSpot Pro — placing it alongside Claude Computer Use and OpenAI Operator in the GUI automation tier. Five agentic capabilities layer on top: deep reasoning, self-programming, tool invocation, verification/testing, and autonomous iteration, with a 35-hour autonomous run ceiling and 1,000+ sequential tool calls supported.

The pricing is the headline for developers: $0.40/M input and $1.60/M output — roughly 6× cheaper than Qwen3.7-Max's $2.50/$7.50 — while maintaining parity on core coding benchmarks (Terminal-Bench: 70.3 for Plus vs. 69.7 for Max; SWE-bench Pro: ~60% each). Alibaba's shift from open-weight (Apache 2.0) to closed API-only models with the 3.7 generation has sparked concern from enterprises that built on open Qwen weights — the 3.7 series is strictly commercial cloud API.

Vision Arena at launch ranked Qwen3.7-Plus-Preview at #16, making Alibaba the #5 lab in vision. On Terminal-Bench 2.0-Terminus (70.3), it outperforms DeepSeek-V4-Pro-Max (67.9) and Gemini 3.1 Pro (63.5). The implication is notable: multimodal capability now comes with less compute cost than pure-text models from other labs, as long as the open-weights requirement is waived.

**Key specs:** 1M tokens (shared with vision) / 64K output | Text, Image, Video | $0.40 input / $1.60 output per 1M tokens ($0.08 cached) | Proprietary (closed API) | Alibaba Cloud Bailian / Model Studio

---

### 3. Update on Claude Opus 4.8 — New benchmark deep-dive confirms #1 Intelligence Index at 61.4, deepens coding/agentic lead
**Source:** [OfficeChai](https://officechai.com/ai/claude-opus-4-8-tops-artificial-analysis-intelligence-index-edges-out-gpt-5-5-with-score-of-61-4/) | [Vellum.ai Benchmarks](https://www.vellum.ai/blog/claude-opus-4-8-benchmarks-explained) | [Lushbinary](https://lushbinary.com/blog/claude-opus-4-8-vs-opus-4-7-whats-new-upgrade-guide/) | [Labellerr](https://www.labellerr.com/blog/claude-opus-4-8-vs-4-7-comparison/) | [BenchLM.ai](https://benchlm.ai/models/claude-opus-4-8)

Released May 28, 2026, Claude Opus 4.8 is now confirmed as the top-ranked model on the Artificial Analysis Intelligence Index v4.0 at 61.4 — a 4.1-point gap over Opus 4.7 (57.3) and 1.2 points clear of GPT-5.5 (60.2). Additional benchmark data published in the days following release reveals the breadth of the gains: SWE-bench Pro up 4.9 points to 69.2%, Terminal-Bench 2.1 up 8.5 points to 74.6%, GDPval-AA up 137 Elo to 1,890, BrowseComp up 5 points to 84.3%, and MCP-Atlas up 4.9 points to 82.2%. Pricing is unchanged at $5/$25 per 1M tokens.

The HLE (Humanity's Last Exam with tools) score of 57.9% is the single most diagnostic number in the new data: it represents real multidisciplinary reasoning headroom not yet saturated by other models, and Opus 4.8 widens the gap over GPT-5.5 (41.4% no-tools) considerably. The OSWorld-Verified score of 83.4% places it first on computer use tasks. GPQA Diamond shows a slight -0.6 regression to 93.6%, but the benchmark is effectively saturated — all top models cluster within statistical noise at the top. The lone critical caveat: Terminal-Bench 2.1 at 74.6% still trails GPT-5.5's 82.7% on that specific shell-intensive benchmark, making GPT-5.5 the better choice for pure CLI-driven autonomous workflows.

Anthropic also shipped Dynamic Workflows with Opus 4.8, enabling a single instance to spawn hundreds of parallel sub-agents — the first production implementation of industrial-scale multi-agent orchestration on the Anthropic platform. This is paired with effort control (configurable reasoning budget) and a reported 35% token-efficiency improvement over Opus 4.7 for equivalent tasks, making the same-price-point upgrade straightforward for most production deployments.

**Key specs:** 1M tokens / up to 32K output | Text, Images | $5.00 input / $25.00 output per 1M tokens | Proprietary | GA via Claude API, Amazon Bedrock, Google Vertex AI

---

### 4. Claude Mythos Preview — Anthropic's unreleased super-Opus achieves 77.8% SWE-bench Pro, restricted to critical-infrastructure partners
**Source:** [llm-stats.com](https://llm-stats.com/blog/research/claude-mythos-preview-launch) | [SmartChunks](https://smartchunks.com/claude-mythos-preview-parameters-benchmarks-explained/) | [KingyAI](https://kingy.ai/ai/claude-mythos-preview-benchmarks-the-ai-that-scored-93-9-on-swe-bench-and-still-wont-be-released/) | [ClaudeFast](https://claudefa.st/blog/models/claude-mythos)

Announced April 7, 2026 alongside Project Glasswing — a gated coalition of ~50 critical-infrastructure organizations — Claude Mythos Preview is the first Anthropic model to sit above Opus class. It is not publicly available, and Anthropic has not committed to a general availability date. New third-party evaluations published this week confirm its position as the highest-scoring model on the SWE-bench Pro leaderboard at 77.8% (vs. 69.2% for Opus 4.8 and 64.3% for Opus 4.7), and #1 on SWE-bench Verified at 93.9% — the highest score ever recorded. On Terminal-Bench 2.0 it scores 82.0%, on USAMO 2026 it scores 97.6%, and it saturates Cybench at 100% pass@1 (35 CTF challenges).

The cybersecurity capability profile is the reason the model is restricted: it autonomously discovered thousands of zero-day vulnerabilities across every major OS and browser during internal evaluation, including a 27-year-old OpenBSD TCP SACK RCE bug and a 17-year-old FreeBSD NFS RCE (now CVE-2026-4747). On the same Firefox 147 JavaScript engine exploit harness, Mythos produced 181 working exploits while Opus 4.6 produced two. The 244-page system card is the first Anthropic has ever published for an unreleased model.

Context: the BenchLM.ai coding leaderboard now lists Claude Mythos Preview at #1 with a weighted coding score of 100 and SWE-bench Pro 77.8% — though it is not accessible to API users. This benchmark data is increasingly relevant as it defines the ceiling for autonomous software engineering AI, shapes expectations for what Opus 4.8 successors will achieve, and motivates the industry's push toward SWE-bench Pro as the primary coding benchmark (SWE-bench Verified is approaching the ceiling and resists contamination less well).

**Key specs:** 1M tokens / 128K output | Text, code | $25.00 input / $125.00 output per 1M tokens (gated, not commercially available) | Proprietary | Project Glasswing partners only (Bedrock, Vertex AI, Microsoft Foundry — gated)

---

### 5. DeepSeek V4 — 1.6T MoE open-weights model matches closed-source frontier on SWE-bench at $1.74/M input
**Source:** [HuggingFace Blog](https://huggingface.co/blog/deepseekv4) | [DeepSeek Guide](https://deepseekai.guide/news/deepseek-v4-release-date/) | [DeepSeek API Docs](https://api-docs.deepseek.com/news/news260424) | [HuggingFace Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

Released April 24, 2026, DeepSeek-V4 is the most capable open-weights model in the field — a 1.6T parameter MoE (49B active) with a 1M-token context window, MIT license, and FP4/FP8 quantization for practical deployment. It matches the then-frontier closed models on SWE-bench Verified (80.6%, essentially tied with Claude Opus 4.6 at 80.8% and Gemini 3.1 Pro at 80.6%), leads all open models on LiveCodeBench (93.5%), and achieves an impressive 95.2% on HMMT 2026. Three reasoning modes (Non-think, Think High, Think Max) allow developers to dial between speed and accuracy. The companion DeepSeek-V4-Flash (284B total / 13B active) provides near-V4-Pro quality at $0.14/M input — cheap enough to make frontier-class inference economically viable for high-volume applications.

The 75% promotional discount that ran through May 31, 2026 has now expired, raising V4-Pro list pricing to $1.74/M input and $3.48/M output — still dramatically cheaper than Claude Opus 4.8 ($5/$25) or GPT-5.5 ($5/$30). The model architecture introduces Token-wise compression and DeepSeek Sparse Attention (DSA), achieving world-leading long-context efficiency; on MRCR at 1M tokens, V4-Pro scores 83.5% vs. Claude Opus 4.6's 92.9% (trailing, but with far lower inference cost). Note: `deepseek-chat` and `deepseek-reasoner` API aliases will retire on July 24, 2026; users should migrate to `deepseek-v4-flash` and `deepseek-v4-pro`.

**Key specs:** 1M tokens / 384K output | Text | $1.74 input / $3.48 output per 1M tokens (list, post-promo) | MIT License | DeepSeek API + self-host (865 GB on-disk for V4-Pro)

---

## Deep Dive: Most Important Release — Gemini 3.5 Flash (May 19, 2026)

Gemini 3.5 Flash is the most strategically important model release this week because it redraws the frontier boundary in a direction previously assumed impossible: a Flash-speed, Flash-price model that materially outperforms the previous full-sized flagship on the benchmarks most relevant to production agent deployments. For developers building multi-step agentic systems on Google Cloud, this means accessing the capabilities of last year's Pro model at $1.50/M input instead of $2.00/M — with 4× the throughput. For the competitive landscape, it means Anthropic and OpenAI's per-token premium is harder to justify for a growing class of workloads.

### What It Can Do

Gemini 3.5 Flash is purpose-built for the agentic era: sub-agent deployment, rapid agentic loops, multi-step coding cycles, and long-horizon tasks at scale. Its native multimodality covers text, image, video, audio, and PDF in a single request — enabling complex document pipelines without multi-model orchestration. The 1M-token input window with 65K output allows reasoning over entire codebases or large document collections. Integrated thinking (adjustable effort level), search grounding with Google Maps, code execution sandboxing, and OpenAPI-compatible function calling make it a complete agentic substrate without add-ons. Thought preservation (automatic maintenance of intermediate reasoning across multi-turn conversations) requires no API changes and reduces token overhead for iterative workflows.

### Benchmark Highlights

| Benchmark | Gemini 3.5 Flash | Previous Best (Gemini 3.1 Pro) |
|---|---|---|
| Terminal-Bench 2.1 | 76.2% | 70.3% |
| MCP Atlas (tool-use) | 83.6% | 78.2% |
| GDPval-AA Elo | 1,656 | 1,314 |
| Finance Agent v2 | 57.9% | 43.0% |
| OSWorld-Verified | 78.4% | 76.2% |
| Toolathlon | 56.5% | 49.4% |
| MMMU-Pro (multimodal) | 83.6% | 80.5% |
| CharXiv Reasoning | 84.2% | 83.3% |
| SWE-bench Pro (Public) | 55.1% | 54.2% |
| Blueprint-Bench 2 | 33.6% | 26.5% |
| ARC-AGI-2 | 72.1% | 77.1% *(regression)* |
| Humanity's Last Exam | 40.2% | 44.4% *(regression)* |
| MRCR v2 (128K) | 77.3% | 84.9% *(regression)* |

### Architecture (known)
Gemini 3.5 Flash is a natively multimodal model with early-fusion vision-language architecture (the same approach as the Gemini 3.x family). It supports configurable thinking effort levels (low, medium default, high) via the Thinking API, and introduces improved "low" effort for code and short agentic tasks. The model ID is `gemini-3.5-flash`; internal version is `3.5-flash-05-2026`. Knowledge cutoff: January 2025. Parameter count: not disclosed. Google's benchmark data shows it runs at roughly 4× the token throughput of other frontier models at comparable serving costs, consistent with a mixture-of-experts efficiency profile — though Google has not confirmed the architecture explicitly.

### Pricing & Availability
- Standard (global): **$1.50/M input, $9.00/M output**, $0.15/M cached input
- Standard (non-global/regional): $1.65/M input, $9.90/M output
- Context: 1,048,576 input tokens / 65,536 output tokens
- Available: Google AI Studio, Gemini API, Vertex AI, Antigravity, Android Studio, Google Workspace, and all consumer Gemini surfaces (app, AI Mode in Search)
- Model ID: `gemini-3.5-flash` (stable GA); `gemini-3-flash-preview` (preview alias)
- Computer Use: **not supported** at launch

### Strategic Significance
The 342-point GDPval-AA swing (1,656 vs. 1,314 for the previous Pro) is the largest agentic performance jump Google has ever published in a single model generation, and it arrives in a Flash model at 25% lower cost than the predecessor Pro. This directly challenges the pricing premium charged by Anthropic and OpenAI for their respective $5/M models: Gemini 3.5 Flash at $1.50/M beats both prior Pro-class competitors on Finance Agent v2, Toolathlon, and GDPval-AA while matching or approaching them on SWE-bench Pro.

The regressions are real and deliberate: ARC-AGI-2 (72.1% vs. 77.1%) and Humanity's Last Exam (40.2% vs. 44.4%) are pure-knowledge and abstract-reasoning benchmarks where a smaller model genuinely trades off against its larger sibling. Google is transparently positioning Gemini 3.5 Pro — still in Vertex AI enterprise preview, GA expected any day in June — to reclaim those regressions with a 2M-token context window and Deep Think reasoning mode. The Flash / Pro split is Google's equivalent of Anthropic's Sonnet / Opus tiering: different capability profiles for different use cases, not a simple upgrade path.

For the open-source ecosystem, Gemini 3.5 Flash's $1.50/M pricing creates direct pressure on DeepSeek V4-Flash ($0.14/M, self-hostable, MIT) — the only remaining significant cost advantage for open-weights deployments is now purely the infrastructure budget, not a 10× quality gap.

### Competitive Context
On the benchmarks that matter for agents — Terminal-Bench, GDPval-AA, MCP Atlas, Finance Agent — Gemini 3.5 Flash now sits above GPT-5.5 on GDPval-AA (1,656 vs. 1,769 for GPT-5.5, a narrowing gap) and above Gemini 3.1 Pro on all agentic metrics. It trails Claude Opus 4.8 substantially on SWE-bench Pro (55.1% vs. 69.2%) and is below GPT-5.5 on Terminal-Bench 2.1 (Google's own card does not report 3.5 Flash vs. GPT-5.5 on this benchmark; independent data places GPT-5.5 at 82.7% vs. Flash at 76.2%). In multimodal tasks (CharXiv: 84.2%, MMMU-Pro: 83.6%), it leads all current models. Gemini 3.5 Pro is expected to close the coding/reasoning gap when it ships.

---

## Benchmark Comparison Data

```json
{"benchmark": "Artificial Analysis Intelligence Index v4.0", "results": [
  {"model": "Claude Opus 4.8", "score": 61.4},
  {"model": "GPT-5.5", "score": 60.2},
  {"model": "Claude Opus 4.7", "score": 57.3},
  {"model": "Muse Spark (Meta)", "score": 52.0},
  {"model": "Qwen3.7-Plus", "score": 53.0}
]}
```

```json
{"benchmark": "SWE-bench Pro (pass rate %)", "results": [
  {"model": "Claude Mythos Preview", "score": 77.8},
  {"model": "Claude Opus 4.8", "score": 69.2},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 64.3},
  {"model": "GPT-5.5", "score": 58.6},
  {"model": "GPT-5.4", "score": 57.7},
  {"model": "Gemini 3.5 Flash", "score": 55.1},
  {"model": "Gemini 3.1 Pro", "score": 54.2},
  {"model": "DeepSeek V4-Pro (Max)", "score": 55.4},
  {"model": "Qwen3.7-Plus / Max", "score": 60.0}
]}
```

```json
{"benchmark": "SWE-bench Verified (pass rate %)", "results": [
  {"model": "Claude Mythos Preview", "score": 93.9},
  {"model": "Claude Opus 4.8", "score": 88.6},
  {"model": "GPT-5.5", "score": 88.7},
  {"model": "Claude Opus 4.7", "score": 87.6},
  {"model": "DeepSeek V4-Pro", "score": 80.6},
  {"model": "Gemini 3.1 Pro", "score": 80.6},
  {"model": "Claude Opus 4.6", "score": 80.8},
  {"model": "Gemini 3.5 Flash", "score": 55.1}
]}
```

```json
{"benchmark": "ARC-AGI-2 (accuracy %)", "results": [
  {"model": "GPT-5.5", "score": 85.0},
  {"model": "GPT-5.4 Pro", "score": 83.3},
  {"model": "Gemini 3.1 Pro", "score": 77.1},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8},
  {"model": "Gemini 3.5 Flash", "score": 72.1},
  {"model": "Grok 4.20", "score": 53.3},
  {"model": "GPT-5.2", "score": 52.9},
  {"model": "Muse Spark", "score": 42.5}
]}
```

```json
{"benchmark": "Terminal-Bench 2.1 (pass rate %)", "results": [
  {"model": "GPT-5.5", "score": 82.7},
  {"model": "Claude Mythos Preview (TB 2.0)", "score": 82.0},
  {"model": "Claude Opus 4.8", "score": 74.6},
  {"model": "Gemini 3.5 Flash", "score": 76.2},
  {"model": "Gemini 3.1 Pro", "score": 70.3},
  {"model": "Qwen3.7-Plus", "score": 70.3},
  {"model": "DeepSeek V4-Pro (Max, TB 2.0)", "score": 67.9},
  {"model": "Claude Opus 4.7", "score": 66.1}
]}
```

```json
{"benchmark": "GDPval-AA Elo (agentic knowledge-work)", "results": [
  {"model": "Claude Opus 4.8", "score": 1890},
  {"model": "GPT-5.5", "score": 1769},
  {"model": "Claude Sonnet 4.6", "score": 1676},
  {"model": "Gemini 3.5 Flash", "score": 1656},
  {"model": "DeepSeek V4-Pro (Max)", "score": 1619},
  {"model": "Claude Opus 4.7", "score": 1753},
  {"model": "Gemini 3.1 Pro", "score": 1314}
]}
```

```json
{"benchmark": "Humanity's Last Exam — No Tools (accuracy %)", "results": [
  {"model": "Claude Opus 4.8", "score": 49.8},
  {"model": "Muse Spark (Contemplating mode)", "score": 58.0},
  {"model": "Claude Opus 4.7", "score": 46.9},
  {"model": "Gemini 3.1 Pro", "score": 44.4},
  {"model": "GPT-5.5", "score": 41.4},
  {"model": "GPT-5.4", "score": 39.8},
  {"model": "DeepSeek V4-Pro", "score": 37.7},
  {"model": "Gemini 3.5 Flash", "score": 40.2}
]}
```

```json
{"benchmark": "Humanity's Last Exam — With Tools (accuracy %)", "results": [
  {"model": "Claude Mythos Preview", "score": 64.7},
  {"model": "Claude Opus 4.8", "score": 57.9},
  {"model": "Claude Opus 4.7", "score": 54.7},
  {"model": "GPT-5.5 (approx)", "score": 54.0},
  {"model": "Gemini 3.1 Pro (est)", "score": 51.6},
  {"model": "DeepSeek V4-Pro", "score": 48.2},
  {"model": "Gemini 3.5 Flash (no tools only)", "score": 40.2}
]}
```

```json
{"benchmark": "GPQA Diamond (accuracy %)", "results": [
  {"model": "Claude Opus 4.7", "score": 94.2},
  {"model": "Gemini 3.1 Pro", "score": 94.3},
  {"model": "Claude Mythos Preview", "score": 94.6},
  {"model": "Claude Opus 4.8", "score": 93.6},
  {"model": "GPT-5.5", "score": 93.6},
  {"model": "DeepSeek V4-Pro", "score": 90.1},
  {"model": "Qwen3.7-Plus", "score": 90.0}
]}
```

```json
{"benchmark": "MCP Atlas (tool-use reliability %)", "results": [
  {"model": "Claude Opus 4.8", "score": 82.2},
  {"model": "Gemini 3.5 Flash", "score": 83.6},
  {"model": "Claude Opus 4.7", "score": 79.1},
  {"model": "Gemini 3.1 Pro", "score": 78.2},
  {"model": "GPT-5.5", "score": 75.3},
  {"model": "Qwen3.7-Plus", "score": 76.4},
  {"model": "DeepSeek V4-Pro", "score": 73.6},
  {"model": "Claude Sonnet 4.6", "score": 69.5}
]}
```

```json
{"benchmark": "LiveCodeBench (pass rate %)", "results": [
  {"model": "DeepSeek V4-Pro (Max)", "score": 93.5},
  {"model": "Qwen3.7-Max", "score": 91.6},
  {"model": "DeepSeek V4-Flash (Max)", "score": 91.6},
  {"model": "DeepSeek V4-Pro (High)", "score": 89.8},
  {"model": "Kimi K2.6", "score": 89.6},
  {"model": "Claude Opus 4.6", "score": 88.8}
]}
```

```json
{"benchmark": "CharXiv Reasoning — multimodal chart understanding (%)", "results": [
  {"model": "Muse Spark", "score": 86.4},
  {"model": "Gemini 3.5 Flash", "score": 84.2},
  {"model": "GPT-5.5", "score": 84.1},
  {"model": "Claude Opus 4.7", "score": 82.1},
  {"model": "Gemini 3.1 Pro", "score": 83.3},
  {"model": "GPT-5.4", "score": 82.8}
]}
```

```json
{"benchmark": "LMArena Text Elo (May–June 2026 snapshot)", "results": [
  {"model": "Claude Opus 4.6 Thinking", "score": 1502},
  {"model": "Claude Opus 4.7 Thinking", "score": 1501},
  {"model": "Claude Opus 4.6", "score": 1498},
  {"model": "Claude Opus 4.7", "score": 1492},
  {"model": "Meta Muse Spark (preliminary)", "score": 1491},
  {"model": "Gemini 3.1 Pro Preview", "score": 1490},
  {"model": "Gemini 3 Pro", "score": 1486},
  {"model": "GPT-5.5 High", "score": 1484},
  {"model": "Grok 4.20 Beta", "score": 1479},
  {"model": "GPT-5.4 High", "score": 1479}
]}
```

```json
{"benchmark": "OSWorld-Verified — computer use (%)", "results": [
  {"model": "Claude Opus 4.8", "score": 83.4},
  {"model": "Claude Opus 4.7", "score": 82.8},
  {"model": "GPT-5.5", "score": 78.7},
  {"model": "Gemini 3.5 Flash", "score": 78.4},
  {"model": "Gemini 3.1 Pro", "score": 76.2},
  {"model": "Claude Mythos Preview", "score": 79.6},
  {"model": "Claude Sonnet 4.6", "score": 72.5}
]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Opus 4.8 | Anthropic | 1M | $5.00 | $25.00 | Text, Image |
| Claude Opus 4.7 | Anthropic | 1M | $5.00 | $25.00 | Text, Image |
| GPT-5.5 | OpenAI | 1M | $5.00 | $30.00 | Text, Image, Audio, Video |
| GPT-5.5 Pro | OpenAI | 1M | $30.00 | $180.00 | Text, Image, Audio, Video |
| Gemini 3.5 Flash | Google | 1M | $1.50 | $9.00 | Text, Image, Video, Audio, PDF |
| Gemini 3.1 Pro | Google | 1M | $2.00 | $12.00 | Text, Image, Video, Audio |
| Grok 4.3 | xAI | 1M (est.) | ~$3.00 | ~$15.00 | Text, Image |
| DeepSeek V4-Pro | DeepSeek | 1M | $1.74 | $3.48 | Text |
| DeepSeek V4-Flash | DeepSeek | 1M | $0.14 | $0.28 | Text |
| Qwen3.7-Plus | Alibaba | 1M | $0.40 | $1.60 | Text, Image, Video |
| Qwen3.7-Max | Alibaba | 1M | $2.50 | $7.50 | Text only |
| Meta Muse Spark | Meta | N/A (API preview) | Not disclosed | Not disclosed | Text, Image (multimodal) |
| Claude Mythos Preview | Anthropic | 1M | $25.00 | $125.00 | Text, Code (gated) |
| Gemini 3.5 Pro (pending) | Google | 2M (projected) | ~$15.00 (est.) | ~$60.00 (est.) | Text, Image, Video, Audio |
| Mistral Medium 3.5 | Mistral | 256K (est.) | ~$2.00 | ~$6.00 | Text |

---

## Analysis & Impact

- **For software engineering / coding:** Claude Opus 4.8 at 69.2% SWE-bench Pro is the clear production choice for complex multi-file coding and agentic SE tasks. Claude Mythos Preview at 77.8% sets the ceiling but is inaccessible. DeepSeek V4-Pro at $1.74/M and ~80.6% SWE-bench Verified is the cost-effective open-weights option — still unmatched on LiveCodeBench (93.5%). For CI-loop, rapid iteration, and sub-agent coding, Gemini 3.5 Flash at $1.50/M now competes directly with models that cost 3× more.

- **For frontier reasoning / math / science:** GPT-5.5 leads ARC-AGI-2 at 85% — the abstract reasoning benchmark where Gemini and Claude show meaningful gaps. Claude Opus 4.8 leads on HLE with tools (57.9%) and GDPval-AA (1,890 Elo), making it the best choice for economics, science synthesis, and multi-domain professional work. Meta's Muse Spark leads Contemplating-mode HLE at 58% (no-tools baseline) and HealthBench Hard at 42.8 — carving out a niche in health and scientific reasoning that the other frontier labs have not prioritized.

- **For multimodal / video / audio work:** Gemini 3.5 Flash leads on MMMU-Pro (83.6%) and CharXiv Reasoning (84.2%), with native video and audio understanding in a single API call. Qwen3.7-Plus at $0.40/M adds image and video input with 79.0 ScreenSpot Pro GUI grounding — the cheapest multimodal option with agentic capabilities. Muse Spark leads CharXiv Reasoning (86.4%) and MMMU-Pro multimodal (80.5%) in its category, though pricing and availability remain limited.

- **For cost-sensitive or open-source deployments:** DeepSeek V4-Flash at $0.14/M input (MIT license, self-hostable) remains the strongest open-weights model for bulk inference — near-V4-Pro quality on simple agentic tasks at 1/12 the cost of GPT-5.5. Qwen3.7-Plus at $0.40/M adds vision on top at a fraction of any frontier API cost. The 3.7-Plus/Max transition to closed API is the most significant open-source regression this cycle; the last open Qwen checkpoints are the Qwen3.6 series (Apache 2.0, up to 35B-A3B).

- **The agentic-first benchmark suite is now table stakes:** Terminal-Bench, MCP Atlas, GDPval-AA, and OSWorld-Verified are the benchmarks every major lab is now reporting — not MMLU or HumanEval. The era of general-knowledge benchmarks as the primary differentiation signal is effectively over for frontier labs; the new arms race is measured in real-world task completion rates on agents running in actual compute environments. Gemini 3.5 Flash's architecture — 4× throughput, tuned for "rapid agentic loops" — signals that low-latency sub-agent execution will be the next major optimization frontier after raw capability.

---

## Key Takeaways (TL;DR)

- **Gemini 3.5 Flash is GA at $1.50/M input and beats the previous Pro flagship on 11 of 15 benchmarks**, including a 342-point GDPval-AA swing — the biggest agentic-performance jump in Google's model history.
- **Claude Opus 4.8 holds the #1 spot on the Artificial Analysis Intelligence Index at 61.4** with 69.2% SWE-bench Pro, 1,890 GDPval-AA Elo, and 57.9% HLE (with tools), at an unchanged $5/$25 price.
- **Qwen3.7-Plus launched June 1–3 at $0.40/M with multimodal vision, 1M context, and GUI grounding (79.0 ScreenSpot Pro)** — the most capable low-cost multimodal model available today.
- **Claude Mythos Preview (not publicly available) holds SWE-bench Pro at 77.8% and SWE-bench Verified at 93.9%**, setting the coding benchmark ceiling that will shape expectations for the next Opus generation.
- **DeepSeek V4-Pro's 75% promo ended May 31**; list price is now $1.74/M input, but it remains the only open-weights model to match closed-source frontiers on SWE-bench Verified (80.6%) with full MIT license self-hosting at 1M context.

---

*Sources:*
- https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/
- https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash
- https://deepmind.google/models/model-cards/gemini-3-5-flash/
- https://llm-stats.com/blog/research/gemini-3.5-flash-launch
- https://www.nxcode.io/nl/resources/news/gemini-3-5-flash-complete-guide-benchmarks-pricing-api-2026
- https://byteiota.com/gemini-35-pro-api-access-pricing-developer-guide/
- https://wavespeed.ai/blog/posts/gemini-3-5-pro-flash/
- https://codersera.com/blog/gemini-3-5-complete-guide-2026/
- https://www.creeta.com/en/gemini-3-5-flash-vs-pro-guide-2026/
- https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5
- https://officechai.com/ai/claude-opus-4-8-tops-artificial-analysis-intelligence-index-edges-out-gpt-5-5-with-score-of-61-4/
- https://www.vellum.ai/blog/claude-opus-4-8-benchmarks-explained
- https://lushbinary.com/blog/claude-opus-4-8-vs-opus-4-7-whats-new-upgrade-guide/
- https://www.labellerr.com/blog/claude-opus-4-8-vs-4-7-comparison/
- https://benchlm.ai/models/claude-opus-4-8
- https://llm-stats.com/blog/research/claude-mythos-preview-launch
- https://smartchunks.com/claude-mythos-preview-parameters-benchmarks-explained/
- https://kingy.ai/ai/claude-mythos-preview-benchmarks-the-ai-that-scored-93-9-on-swe-bench-and-still-wont-be-released/
- https://claudefa.st/blog/models/claude-mythos
- https://ai-stats.phaseo.app/models/anthropic/claude-mythos-preview
- https://venturebeat.com/technology/alibabas-qwen3-7-plus-supports-text-video-and-imagery-inputs-at-low-cost-of-0-4-1-6-per-1m-token-but-its-proprietary
- https://metaailabs.com/alibabas-qwen-team-launches-qwen3-7-plus-adding-vision-deep-reasoning-tool-invocation-and-autonomous-iteration-on-the-bailian-platform/
- https://apidog.com/blog/qwen-3-7-plus/
- https://www.qwencloud.com/models/qwen3.7-plus
- https://ofox.ai/blog/qwen-3-7-plus-vs-qwen-3-7-max-real-benchmark-2026/
- https://developer.puter.com/ai/qwen/qwen3.7-plus/
- https://huggingface.co/blog/deepseekv4
- https://deepseekai.guide/news/deepseek-v4-release-date/
- https://deepseekai.guide/models/deepseek-v4-pro/
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- https://api-docs.deepseek.com/news/news260424
- https://ai.meta.com/blog/introducing-muse-spark-msl/?hl=en-GB
- https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/
- https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since
- https://www.yottalabs.ai/post/meta-muse-spark-architecture-explained-multi-agent-inference-guide
- https://tokenmix.ai/blog/gpt-5-5-spud-review-88-swe-bench-2026
- https://appwrite.io/blog/post/gpt-5-5-launch
- https://www.ai.cc/blogs/gpt-5-5-everything-you-need-to-know/
- https://developers.openai.com/api/docs/models/gpt-5.5
- https://llm-stats.com/blog/research/gpt-5-5-vs-gpt-5-4
- https://presenc.ai/research/lmsys-chatbot-arena-elo-rankings-may-2026
- https://www.swfte.com/ai/llm/leaderboard
- https://benchlm.ai/benchmarks/arcAgi2
- https://benchlm.ai/coding
- https://github.com/leoncuhk/awesome-llm-bench
- https://mungomash.com/ai/models/
- https://www.deeplearning.ai/the-batch/issue-356
- https://www.datalearner.com/en/leaderboards/category/code?benchmark=SWE-bench+Multilingual&modelType=chatLLM
- https://research.mental-momentum.ai/r/how-gpt-5-6-claude-sonnet-4-8-gemini-3-5-q08wat
- https://gudz.ai/posts/june-2026-ai-model-showdown
- https://tokenmix.ai/blog/gpt-5-6-release-date-leaks-2026
