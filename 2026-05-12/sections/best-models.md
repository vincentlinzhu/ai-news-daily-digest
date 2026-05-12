# Best Models & Benchmarks — 2026-05-12

## Top Model News (5)

### 1. Claude Mythos Preview — Anthropic's Restricted Frontier Model Tops SWE-bench Pro at 77.8%
**Source:** [Anthropic Red Team](https://red.anthropic.com/2026/mythos-preview) | [BuiltIn](https://builtin.com/articles/anthropic-claude-mythos) | [Awesome Agents](https://awesomeagents.ai/models/claude-mythos-preview/) | [BenchLM SWE-bench Pro](https://benchlm.ai/benchmarks/swePro)

Announced April 7, 2026, Claude Mythos Preview is Anthropic's most capable model to date and holds the top position on SWE-bench Pro (77.8%) — a 13-point lead over the next non-restricted competitor. But unlike every prior Anthropic release, it has deliberately not been made public. Access is strictly limited to 52 organizations: 12 founding partner companies and ~40 critical infrastructure operators vetted through Project Glasswing, Anthropic's cross-industry cybersecurity initiative.

The reason for the restricted release is stark: during red-teaming, Mythos demonstrated the ability to discover zero-day vulnerabilities across all major operating systems and web browsers, find 27-year-old bugs (including an OpenBSD TCP vulnerability), and write complex multi-step exploits including a four-vulnerability chain with JIT heap sprays. Anthropic concluded that unrestricted public availability constituted an "existential threat" to the cybersecurity industry. At $25/$125 per 1M input/output tokens — 5× the cost of Claude Opus 4.6 — it is priced to reflect both capability and scarcity.

Beyond security, Mythos achieves 93.9% on SWE-bench Verified (the highest ever published under any controlled setting), 94.6% on GPQA Diamond, 97.6% on USAMO 2026, and 82.0% on Terminal-Bench 2.0. Its architecture is a Mixture-of-Experts with an estimated ~10 trillion total parameters. While it cannot be accessed by most developers, its benchmark scores are now the new ceiling every lab is benchmarking against — and will inevitably pressure the next public release cycle.

**Key specs:** 1M token context | Text, code | $25/$125 per 1M tokens | Proprietary/restricted | Limited to 52 vetted organizations via Project Glasswing

---

### 2. DeepSeek V4 Pro — Open-Weight 1.6T MoE Tops LiveCodeBench at 93.5%
**Source:** [DeepSeek AI Guide](https://deepseekai.guide/news/deepseek-v4-release-date/) | [Benchable](https://benchable.ai/models/deepseek/deepseek-v4-pro) | [TechSifted](https://techsifted.com/posts/deepseek-v4-review-april-2026/) | [Digital Applied](https://www.digitalapplied.com/blog/deepseek-v4-preview-launch-1m-context-efficiency)

Released April 24, 2026, DeepSeek V4 Pro is a 1.6 trillion total parameter Mixture-of-Experts model with 49 billion active parameters per token — a ratio achieved through Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) that reduces KV cache to just 10% of V3.2's footprint while supporting a full 1 million token context window and up to 384K output tokens per run. The weights are open on Hugging Face. Inference cost is approximately 27% of V3.2's per-token FLOPs, and API pricing is $1.74/$3.48 per 1M input/output tokens.

Performance is most striking in code: V4 Pro achieves 93.5% on LiveCodeBench Pass@1 and a Codeforces rating of 3,206 — both #1 among non-restricted models. It also scores 80.6% on SWE-bench Verified (tied with Gemini 3.1 Pro). The 1M context window enables entire large codebases to be processed in a single call, and the model's "Max" reasoning effort mode (enabled via the API `reasoning_effort: max` parameter) unlocks additional performance headroom at higher cost.

The model trails GPT-5.4 and Gemini 3.1 Pro by roughly 3–6 months on general knowledge benchmarks (SimpleQA-Verified: 57.9 vs Gemini's 75.6), but for pure coding tasks it has no open-weight peer and competes directly with frontier proprietary models. Given the price point and open availability, V4 Pro immediately became the reference inference target for cost-conscious engineering teams.

**Key specs:** 1M token context (384K max output) | Text + code | $1.74/$3.48 per 1M tokens | Open weights (MIT) | API live, Hugging Face

---

### 3. Perceptron Mk1 — Specialized Video AI at 80–90% Lower Cost Than Frontier Labs
**Source:** [VentureBeat](https://venturebeat.com/technology/perceptron-mk1-shocks-with-highly-performant-video-analysis-ai-model-80-90-cheaper-than-anthropic-openai-and-google) | [Las Vegas Sun](https://lasvegassun.com/news/2026/may/12/perceptron-ai-launches-physical-ai-model-that-matc/)

Launched May 12, 2026 (today), Perceptron Mk1 is a purpose-built video-understanding and embodied-reasoning model from Perceptron Inc. The model processes native video at 2 frames per second across a 32K token window and achieves competitive performance with GPT-5.5, Claude Opus 4.7, and Gemini 3.1 Pro on spatial/video benchmarks — at a fraction of the cost: $0.15/$1.50 per 1M input/output tokens vs. $5–$30 input for comparable frontier models.

On spatial and video-specific evaluations, Mk1 scores 85.1 on EmbSpatialBench and 88.5 on VSI-Bench. Target applications include manufacturing quality control, robotics perception pipelines, media content analysis, and physical security monitoring. The release positions Perceptron as a vertical specialist that trades breadth for depth in video — the one modality where cost-performance ratios for general-purpose models remain prohibitive.

This launch matters structurally: it represents a new generation of task-optimized models that can undercut hyperscaler pricing by 80–90% on specific workloads rather than competing on the general intelligence leaderboard. Expect similar specialized entrants in audio, CAD/3D, and long-form document domains throughout 2026.

**Key specs:** 32K token context | Video (2 fps), text | $0.15/$1.50 per 1M tokens | Proprietary | API available

---

### 4. ERNIE 5.1 — Baidu Achieves Frontier Performance at 6% Pre-Training Cost
**Source:** [ERNIE Blog](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) | [The Decoder](https://the-decoder.com/baidus-ernie-5-1-cuts-94-percent-of-pre-training-costs-while-competing-with-top-models/) | [LLM Reference](https://www.llmreference.com/model/ernie-5.1)

Released May 9, 2026, ERNIE 5.1 is the most striking training efficiency demonstration of the year. By applying Baidu's "Once-For-All elastic training framework" — which enables multi-dimensional elastic compression across depth, expert capacity, and routing sparsity — the model achieves ERNIE 5.0-class performance with approximately one-third the total parameters and half the active parameters, at just 6% of comparable models' pre-training compute cost. The result is roughly 800B total parameters delivering performance that matches leading closed-source models on GPQA and MMLU-Pro while ranking 4th globally (1st among Chinese models) on the LMArena Search leaderboard with a score of 1,223.

On AIME 2026 with tool use, ERNIE 5.1 scores 99.6 — second only to Gemini 3.1 Pro globally. It also outperforms DeepSeek V4 Pro on τ³-bench and SpreadsheetBench-Verified agent evaluation tasks. API pricing is $0.59/$2.65 per 1M input/output tokens via Baidu Qianfan — one of the cheapest frontier-competitive offerings available.

The broader signal is efficiency: while other labs race for parameter count and training tokens, Baidu has demonstrated that architectural compression can dramatically reduce the capital required to maintain frontier-caliber models. This has significant implications for smaller nations and organizations aiming to train competitive sovereign AI without hyperscaler-level CapEx.

**Key specs:** 128K token context (65K max output) | Text | $0.59/$2.65 per 1M tokens | Proprietary | Baidu Qianfan API

---

### 5. NVIDIA Nemotron 3 Nano Omni — Open Multimodal MoE with Mamba2 Hybrid Architecture
**Source:** [NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) | [NVIDIA Developer](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/) | [HuggingFace](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence) | [arXiv 2604.24954](https://arxiv.org/html/2604.24954)

Released April 28, 2026, Nemotron 3 Nano Omni is NVIDIA's first production model using a Mamba2-Transformer Hybrid Mixture-of-Experts architecture — combining the efficiency of SSM (state space models) with the reasoning power of transformers. The model has 30B total parameters with only 3B active per token (A3B) and natively ingests video (up to 2 minutes), audio (up to 1 hour), images, and text within a 256K token context window. Open weights are available in BF16, FP8, and NVFP4 formats on Hugging Face and NGC.

Nemotron 3 achieves 9× higher throughput vs. other open omni models and 2.9× faster single-stream reasoning on multimodal tasks. It tops the MMlongbench-Doc and OCRBenchV2 document intelligence leaderboards and achieves best-in-class performance on WorldSense, DailyOmni, and VoiceBench video/audio benchmarks. The combination of open weights, novel hybrid architecture, and native true omni-modality (not separate adapters) makes this the most interesting open-weight multimodal release since Llama 4 Maverick.

The architectural choice to use Mamba2 for efficient long-sequence processing while retaining transformer attention for reasoning-heavy tasks is a notable hedge: NVIDIA is simultaneously enabling hardware-agnostic research and validating SSM viability at production scale. Unlike pure-transformer models, Mamba2 hybrids scale KV cache sublinearly — a critical advantage for the 256K context the model targets.

**Key specs:** 256K token context | Video, audio, image, text | Open weights (Apache 2.0) | Available on Hugging Face, NGC, Build.Nvidia.com | English only

---

## Deep Dive: Most Important Release — Claude Mythos Preview (April 7, 2026)

### What It Can Do

Claude Mythos Preview is the first AI model deemed by its creator to be too dangerous for general public release. Its primary breakout capability is autonomous software vulnerability research: given access to source code, binary, or API documentation, Mythos can independently discover previously unknown security flaws — zero-days — across every major OS and browser, synthesize multi-stage exploit chains (including JIT heap spray sequences), and write production-ready proof-of-concept code. During testing it found a vulnerability present in OpenBSD's TCP stack for 27 years. Beyond security, it is simply the most capable general-purpose model yet produced: 93.9% SWE-bench Verified, 94.6% GPQA Diamond, 97.6% USAMO 2026 math olympiad, and 73% on AISI expert-level CTF challenges.

### Benchmark Highlights

| Benchmark | Claude Mythos Preview | Previous Best (non-Mythos) |
|---|---|---|
| SWE-bench Pro | 77.8% | 64.3% (Claude Opus 4.7 Adaptive) |
| SWE-bench Verified | 93.9% | 87.6% (Claude Opus 4.7) |
| GPQA Diamond | 94.6% | 91.2% (Gemini 2.5 Ultra) |
| Terminal-Bench 2.0 | 82.0% | 82.7% (GPT-5.5 — marginal lead) |
| CyberGym | 83.1% | 81.8% (GPT-5.5) |
| USAMO 2026 | 97.6% | ~96.4% (Kimi K2.6 AIME equivalent) |
| CTF Expert Level (AISI) | 73% | ~50% (est. prior best) |

### Architecture (known)

Mixture-of-Experts transformer with an estimated ~10 trillion total parameters (active parameters undisclosed). Context window: 1 million tokens. Modalities: text and code (no confirmed image/video). Extended thinking with `xhigh` reasoning effort tier inherited from Opus 4.7 lineage. Training methodology unknown; Anthropic has not published a technical report as of May 12, 2026, citing security concerns.

### Pricing & Availability

$25 per 1M input tokens / $125 per 1M output tokens — the most expensive commercial LLM API to date. Access exclusively through Project Glasswing; applications from critical infrastructure operators are vetted by Anthropic's security team. No consumer or standard API access. No timeline for broader release has been given.

### Strategic Significance

Mythos creates a new category: the **restricted frontier model**. By demonstrating that a model can be "too capable to release," Anthropic has simultaneously:
1. Established the first credible safety-first release gate for a frontier model
2. Created a moat that competitors cannot replicate without similar safety infrastructure
3. Signaled to regulators that voluntary capability restriction is viable — potentially preempting mandatory AI Act-style licensing
4. Anchored the SWE-bench Pro leaderboard ceiling at 77.8%, forcing all future coding agent comparisons to acknowledge a 13-point gap that cannot be closed without accessing a model most developers will never touch

The downside: withholding the model may slow safety research. And pricing at $25/$125 restricts use even among vetted partners to high-value, high-stakes workflows.

### Competitive Context

GPT-5.5 (xhigh) currently tops the publicly accessible frontier at 60/100 on the Artificial Analysis Intelligence Index, followed by Claude Opus 4.7 (57) and Gemini 3.1 Pro (57). Mythos is not on the public index, but its SWE-bench and GPQA numbers suggest it would score materially higher. Google's Gemini 2.5 Ultra (April 2026) reached 72.8% SWE-bench Verified — impressive but 21 points behind Mythos. DeepSeek V4 Pro at 80.6% SWE-bench Verified is the open-weight leader but still 13 points behind on the more rigorous SWE-bench Pro evaluation. The coding capability gap between Mythos and the second-place public model is roughly equivalent to the gap between GPT-4o and Claude Opus 3 — a full generation.

---

## Benchmark Comparison Data

```json
{"benchmark": "Artificial Analysis Intelligence Index (v4.0)", "results": [
  {"model": "GPT-5.5 (xhigh)", "score": 60.2},
  {"model": "GPT-5.5 (high)", "score": 58.9},
  {"model": "Claude Opus 4.7 (Adaptive, Max)", "score": 57.3},
  {"model": "Gemini 3.1 Pro Preview", "score": 57.2},
  {"model": "GPT-5.5 (medium)", "score": 56.7},
  {"model": "Qwen 3.6 Max", "score": 52.0},
  {"model": "Grok 4.3", "score": 53.0}
]}
```

```json
{"benchmark": "MMLU", "results": [
  {"model": "o3", "score": 92.9},
  {"model": "Claude Opus 4.5", "score": 91.8},
  {"model": "Gemini 3 Pro", "score": 91.4},
  {"model": "GPT-5", "score": 90.8},
  {"model": "DeepSeek V3", "score": 87.1},
  {"model": "Qwen 3.5-122B", "score": 84.8}
]}
```

```json
{"benchmark": "GPQA Diamond", "results": [
  {"model": "Claude Mythos Preview", "score": 94.6},
  {"model": "Gemini 2.5 Ultra", "score": 91.2},
  {"model": "GPT-5.4", "score": 88.5},
  {"model": "Claude Opus 4.6", "score": 88.4},
  {"model": "o3", "score": 87.7},
  {"model": "Grok 4.3", "score": 65.8}
]}
```

```json
{"benchmark": "SWE-bench Verified", "results": [
  {"model": "Claude Mythos Preview", "score": 93.9},
  {"model": "GPT-5.5", "score": 88.7},
  {"model": "Claude Opus 4.7", "score": 87.6},
  {"model": "DeepSeek V4 Pro", "score": 80.6},
  {"model": "Gemini 3.1 Pro", "score": 80.6},
  {"model": "Gemini 2.5 Ultra", "score": 72.8}
]}
```

```json
{"benchmark": "SWE-bench Pro", "results": [
  {"model": "Claude Mythos Preview", "score": 77.8},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 64.3},
  {"model": "GPT-5.5", "score": 58.6},
  {"model": "Kimi K2.6", "score": 58.6},
  {"model": "GLM-5.1", "score": 58.4},
  {"model": "Qwen 3.6 Max", "score": 57.3},
  {"model": "DeepSeek V4 Pro", "score": 55.0}
]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [
  {"model": "GPT-5.5", "score": 85.0},
  {"model": "GPT-5.4 Pro", "score": 83.3},
  {"model": "Gemini 3.1 Pro", "score": 77.1},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8},
  {"model": "Grok", "score": 53.3},
  {"model": "GPT-5.4", "score": 52.9},
  {"model": "Human average", "score": 66.0}
]}
```

```json
{"benchmark": "AIME 2026", "results": [
  {"model": "Kimi K2.6", "score": 96.4},
  {"model": "GLM-5", "score": 95.8},
  {"model": "Kimi K2.5", "score": 95.8},
  {"model": "GLM-5.1", "score": 95.3},
  {"model": "Qwen 3.6 Plus", "score": 95.3},
  {"model": "ERNIE 5.1 (with tools)", "score": 99.6}
]}
```

```json
{"benchmark": "LiveCodeBench Pass@1", "results": [
  {"model": "DeepSeek V4 Pro (Max)", "score": 93.5},
  {"model": "DeepSeek V4 Flash (Max)", "score": 91.6},
  {"model": "DeepSeek V4 Pro (High)", "score": 89.8},
  {"model": "Moonshot AI (Kimi K2.6)", "score": 89.6},
  {"model": "DeepSeek V4 Flash (High)", "score": 88.4}
]}
```

```json
{"benchmark": "LMSys Chatbot Arena — Overall ELO", "results": [
  {"model": "Claude Opus 4.6 (Thinking)", "score": 1506},
  {"model": "Gemini 3.1 Pro", "score": 1505},
  {"model": "Gemini 3 Pro", "score": 1486},
  {"model": "Grok 4.1 (Thinking)", "score": 1475},
  {"model": "GPT-5.1 High", "score": 1457}
]}
```

```json
{"benchmark": "LMSys Arena — Coding ELO", "results": [
  {"model": "Claude Opus 4.6 (Thinking)", "score": 1545},
  {"model": "GLM-5.1", "score": 1530},
  {"model": "Gemini 3.1 Pro", "score": 1520},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 1515},
  {"model": "GPT-5.5", "score": 1505}
]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [
  {"model": "GPT-5.5", "score": 82.7},
  {"model": "Claude Mythos Preview", "score": 82.0},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 69.4},
  {"model": "MiMo-V2.5-Pro (Xiaomi)", "score": 68.4},
  {"model": "DeepSeek V4 Pro (Max)", "score": 67.9},
  {"model": "Moonshot AI (Kimi)", "score": 66.7},
  {"model": "Qwen 3.6 Max", "score": 65.0}
]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Mythos Preview | Anthropic | 1M | $25.00 | $125.00 | Text, code (restricted access) |
| GPT-5.5 (xhigh) | OpenAI | 1.05M | $10.00 | $60.00 | Text, images, code |
| GPT-5.5 (standard) | OpenAI | 1.05M | $5.00 | $30.00 | Text, images, code |
| Claude Opus 4.7 (Adaptive) | Anthropic | 1M | $5.00 | $25.00 | Text, images, code |
| Gemini 3.1 Pro | Google | 2M | $2.00 | $12.00 | Text, images, video, audio, code |
| Grok 4.3 | xAI | 1M | $1.25 | $2.50 | Text, images, video (≤5 min) |
| DeepSeek V4 Pro | DeepSeek | 1M | $1.74 | $3.48 | Text, code |
| ERNIE 5.1 | Baidu | 128K | $0.59 | $2.65 | Text |
| Qwen 3.6 Max | Alibaba | 256K | ~$1.50 | ~$6.00 | Text, code |
| GLM-5.1 | Z.AI (Zhipu) | 200K | ~$1.00 | ~$4.00 | Text, code |
| Kimi K2.6 | Moonshot AI | 1M | ~$2.00 | ~$8.00 | Text, code, agentic |
| Nemotron 3 Nano Omni | NVIDIA | 256K | Open weights | Open weights | Video, audio, image, text |
| Perceptron Mk1 | Perceptron Inc. | 32K | $0.15 | $1.50 | Video, text |
| GPT-Realtime-2 (audio) | OpenAI | 128K | $32.00 | $64.00 | Speech, text |

---

## Analysis & Impact

- **For software engineering / coding:** Claude Mythos Preview (77.8% SWE-bench Pro) is the undisputed leader but inaccessible to most teams. For publicly accessible models, DeepSeek V4 Pro (93.5% LiveCodeBench, 80.6% SWE-bench Verified, $1.74/$3.48) is the strongest open-weight choice, while Claude Opus 4.7 (Adaptive) (64.3% SWE-bench Pro) and GPT-5.5 (58.6%) are the best proprietary options at production scale. Terminal-Bench 2.0 places GPT-5.5 marginally ahead on autonomous agent tasks. GLM-5.1 (SWE-bench Pro 58.4%, LMArena Coding ELO 1530) is a serious open-source dark horse from Zhipu at competitive pricing.

- **For frontier reasoning / math / science:** ERNIE 5.1 achieves the highest AIME 2026 score with tool use (99.6%) and is second only to Gemini 3.1 Pro — at $0.59/$2.65 per 1M tokens. For GPQA Diamond, Claude Mythos (94.6%) is first and restricted; Gemini 2.5 Ultra (91.2%) is the best publicly available science reasoner. On ARC-AGI-2, GPT-5.5 (85%) has now crossed the grand prize threshold, confirming abstract reasoning at human-competitive level is achieved. For math olympiad reasoning without tool use, Kimi K2.6 (96.4% AIME 2026) and GLM-5/5.1 (95.8%) are neck-and-neck open alternatives.

- **For multimodal / video / audio work:** Gemini 3.1 Pro (2M context, native video/audio) remains the strongest general multimodal frontier model. NVIDIA Nemotron 3 Nano Omni (open weights, Mamba2-hybrid, video up to 2 min, audio up to 1 hour, 256K context) is the best open-weight multimodal choice with 9× throughput vs. peers. Perceptron Mk1 (today's launch) is a compelling video-specialist at 80–90% lower cost than frontier APIs for visual inference pipelines. GPT-Realtime-2 ($32/$64/M audio tokens) leads for voice-first applications with GPT-5-class reasoning at 128K context.

- **For cost-sensitive or open-source deployments:** DeepSeek V4 Pro (MIT open weights, $1.74/$3.48 API) is the best price-performance choice for coding/agentic tasks. ERNIE 5.1 ($0.59/$2.65) offers frontier-competitive reasoning at the lowest price among closed APIs. Grok 4.3's 83% price cut to $1.25/$2.50 with 1M context and video support makes it attractive for consumer-scale agentic workloads. NVIDIA Nemotron 3 Nano Omni (fully open, Apache 2.0) is the strongest option for teams needing to run multimodal inference on-premises.

---

## Key Takeaways (TL;DR)

- **Claude Mythos Preview sets a new unreachable ceiling** at 77.8% SWE-bench Pro and 93.9% SWE-bench Verified — but is restricted to 52 vetted security partners, creating a public/private frontier gap of ~13 percentage points in coding
- **DeepSeek V4 Pro (open weights, 1.6T MoE)** tops LiveCodeBench at 93.5% and supports 1M-token context at $1.74 input — the best publicly accessible coding model and the most important open-weight release since Llama 4
- **Perceptron Mk1 (launched today)** delivers frontier-competitive video understanding at $0.15/$1.50 per 1M tokens — 80–90% cheaper than GPT-5.5, Gemini, or Claude for video-native workloads
- **ERNIE 5.1** achieves AIME 2026 (w/ tools) score of 99.6 at 6% of comparable pre-training cost and $0.59 input pricing — the clearest evidence yet that compute-efficient training can reach frontier performance
- **ARC-AGI-2 grand prize threshold (>85%) has been crossed** by GPT-5.5 at 85%, while the LMSys Arena has seen its first 1500+ ELO models — two structural milestones confirming that 2026 is the year abstract reasoning benchmarks stop being useful discriminators

---

*Sources:*

- https://red.anthropic.com/2026/mythos-preview
- https://builtin.com/articles/anthropic-claude-mythos
- https://awesomeagents.ai/models/claude-mythos-preview/
- https://benchlm.ai/benchmarks/swePro
- https://scale.com/leaderboard/swe%5Fbench%5Fpro%5Fpublic
- https://deepseekai.guide/news/deepseek-v4-release-date/
- https://benchable.ai/models/deepseek/deepseek-v4-pro
- https://techsifted.com/posts/deepseek-v4-review-april-2026/
- https://www.digitalapplied.com/blog/deepseek-v4-preview-launch-1m-context-efficiency
- https://venturebeat.com/technology/perceptron-mk1-shocks-with-highly-performant-video-analysis-ai-model-80-90-cheaper-than-anthropic-openai-and-google
- https://lasvegassun.com/news/2026/may/12/perceptron-ai-launches-physical-ai-model-that-matc/
- https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/
- https://the-decoder.com/baidus-ernie-5-1-cuts-94-percent-of-pre-training-costs-while-competing-with-top-models/
- https://www.llmreference.com/model/ernie-5.1
- https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/
- https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/
- https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence
- https://arxiv.org/html/2604.24954
- https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model
- https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
- https://benchlm.ai/benchmarks/arcAgi2
- https://arcprize.org/leaderboard
- https://benchlm.ai/benchmarks/aime2026
- https://llm-stats.com/benchmarks/aime-2026
- https://benchlm.ai/benchmarks/liveCodeBench
- https://benchlm.ai/benchmarks/terminalBench2
- https://www.tbench.ai/leaderboard/terminal-bench/2.0
- https://www.promptt.dev/blog/lmsys-chatbot-arena-leaderboard-2026
- https://benchlm.ai/llm-leaderboard-history
- https://lmmarketcap.com/benchmarks/gpqa_diamond
- https://codesota.com/llm
- https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model
- https://openai.com/index/introducing-gpt-5-5/
- https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- https://www.llmreference.com/model/gpt-realtime-2
- https://anthemcreation.com/en/artificial-intelligence/gpt-realtime-2-128k-context-reasoning/
- https://z.ai/blog/glm-5
- https://techbriefly.com/2026/04/08/z-ai-launches-glm-5-1-model-surpassing-competitors-in-benchmarks/
- https://awesomeagents.ai/news/alibaba-qwen36-max-closed-weights/
- https://datanorth.ai/news/alibaba-releases-qwen3-6-max-preview
- https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing
- https://awesomeagents.ai/news/xai-grok-4-3-api-launch/
- https://cciedump.spoto.net/news/google-unveils-gemini-25-ultra-frontier-reasoning-and-multimodal-breakthroughs-reshape-llm-leaderboards.html
- https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro
- https://crazyrouter.com/en/blog/ai-api-pricing-comparison-may-2026-developer-guide
- https://fungies.io/llm-api-pricing-comparison-2026-7/
