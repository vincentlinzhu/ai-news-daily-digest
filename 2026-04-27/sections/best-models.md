# Best Models & Benchmarks — 2026-04-27

---

## Top Model News (3-5)

### 1. Claude Opus 4.7 — Anthropic's New Flagship Reclaims Top Spot

**Source:** [VentureBeat](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm) | [Anthropic Blog](https://www.anthropic.com/news/claude-opus-4-7) | [Claude Docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7)

Released April 16, 2026, Claude Opus 4.7 is Anthropic's latest and most capable publicly available model, and it narrowly retakes the top position on the LMSys Chatbot Arena with an ELO of 1498 (and 1505 in Thinking mode). The release is focused on capability refinement in agentic workflows rather than architectural novelty: Opus 4.7 introduces "adaptive thinking," which dynamically allocates reasoning tokens per request based on prompt complexity, replacing the fixed-budget extended thinking system from Opus 4.6. This means the model can silently scale up compute for hard problems and scale down for simple ones, avoiding wasted inference budget. Effort tuning is now exposed via five explicit levels — `low`, `medium`, `high`, `xhigh`, and `max` — giving developers fine-grained control over latency vs. capability tradeoffs.

In terms of concrete capability jumps, the standout number is SWE-bench Verified: 87.6%, up from 80.8% on Opus 4.6 — a 6.8-point gain on the hardest widely-cited coding benchmark. Anthropic's internal data shows that Opus 4.7 beats GPT-5.4 and Gemini 3.1 Pro on a combined 7-4 benchmark comparison spanning agentic coding, scaled tool-use, computer-use, and financial analysis. Vision quality has also improved, with image processing now supporting up to 2,576 pixels on the long edge — more than 3.3× higher resolution than previous Claude versions. Self-verification is a new default behavior: the model writes tests and sanity checks before reporting results, reducing silent failures in long agentic runs.

On the GPQA Diamond benchmark (graduate-level science), Opus 4.7 scores 94.2%, near the ceiling of what the benchmark can differentiate. Compared to Opus 4.6, the model shows dramatically better retention of instructions across its full 1-million token context — earlier versions would "wash out" instructions buried in long sequences. Multi-session memory via file-system tooling makes 10-minute-plus autonomous task horizons now routine rather than experimental. Pricing is unchanged from Opus 4.6: $5.00/1M input and $25.00/1M output.

**Key specs:** 1M token context window | Text + Image (2,576px max) | $5.00/$25.00 per 1M tokens | Proprietary | Generally available on Claude.ai, API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry

---

### 2. Meta Muse Spark — Meta's Closed-Weights Pivot and Multimodal Reasoning Debut

**Source:** [MarkTechPost](https://www.marktechpost.com/2026/04/09/meta-superintelligence-lab-releases-muse-spark-a-multimodal-reasoning-model-with-thought-compression-and-parallel-agents/) | [DeepLearning.AI The Batch](https://www.deeplearning.ai/the-batch/with-muse-spark-meta-pivots-away-from-its-open-weights-llama-strategy/) | [NeuralCoreTech](https://neuralcoretech.com/meta-muse-spark-review-benchmarks-2026/)

Meta launched Muse Spark on April 8, 2026, as the first model from Meta Superintelligence Labs (MSL), the new unit led by Scale AI founder Alexandr Wang. Muse Spark represents a complete ground-up rebuild of Meta's AI stack, and — most controversially — it is a closed-weights proprietary model. This marks a major strategic reversal from Meta's historically open Llama series; The Batch called it "Meta pivoting away from its open-weights Llama strategy." The model is currently available free via meta.ai and the Meta AI app, with planned integration across Facebook, Instagram, WhatsApp, and Messenger.

Architecturally, Muse Spark is natively multimodal — it processes text and visual inputs simultaneously in a unified architecture rather than attaching vision adapters to a language backbone. Three reasoning modes are exposed: Instant (low latency), Thinking (chain-of-thought), and Contemplating (multi-agent parallel processing). The flagship innovation is "thought compression": reinforcement learning training penalizes excessive reasoning tokens, forcing the model to compress and optimize chains-of-thought. The result is dramatically lower output token counts — approximately 58M output tokens on benchmark suites vs. 157M for Claude Opus 4.6 and 120M for GPT-5.4 — translating directly to lower latency and API cost.

Benchmark performance shows Muse Spark excelling in multimodal tasks: CharXiv Reasoning at 86.4% (leading competitors), MMMU-Pro at 80.5% (second only to Gemini), and HealthBench Hard at 42.8% (industry-leading for medical/clinical reasoning). On screenshot localization (ScreenSpot Pro), it achieves 72.2% standalone, rising to 84.1% with computer-use tools. The model lags frontier peers on pure coding (SWE-Bench Pro: 52.4%) and sits #4-5 overall on the AI Intelligence Index (score: 52). Its 262K input context window is also smaller than the 1M+ windows offered by Claude, GPT-5.4, and Grok 4.20.

**Key specs:** 262K token context window | Text + Image + Voice input, Text output | Free on meta.ai | Proprietary (closed weights) | Available on meta.ai, Meta AI app

---

### 3. GPT-Rosalind — OpenAI's Vertical Frontier Model for Life Sciences

**Source:** [OpenAI Blog](https://openai.com/index/introducing-gpt-rosalind/) | [MarkTechPost](https://www.marktechpost.com/2026/04/16/openai-launches-gpt-rosalind-life-sciences-ai/) | [Technology.org](https://www.technology.org/2026/04/17/openais-gpt-rosalind-wants-to-shave-years-off-drug-discovery/)

Also released on April 16, 2026 — the same day as Claude Opus 4.7 — OpenAI launched GPT-Rosalind, its first domain-specific vertical model purpose-built for life sciences, drug discovery, and translational medicine. Named after Rosalind Franklin (whose X-ray crystallography work underpinned the discovery of DNA's double helix), the model is optimized for molecular reasoning, protein engineering, genomics, pathway analysis, and experimental planning. It connects natively to over 50 specialized scientific tools and databases through a Life Sciences research plugin for Codex, making it a reasoning-plus-tooling stack rather than a pure language model.

GPT-Rosalind is OpenAI's clearest signal yet that frontier labs are now building vertical specialist models alongside their horizontal flagships. On the BixBench bioinformatics benchmark, GPT-Rosalind achieves a Pass@1 rate of 0.751 — beating GPT-5.4 (0.732), Grok 4.2 (0.698), and Gemini 3.1 Pro (0.550) on the same tasks. The model supports multi-step research workflows spanning literature synthesis, database querying, sequence-to-function interpretation, and hypothesis generation in a single, coherent pipeline.

Availability is currently narrow: research preview through a trusted access program for qualified U.S. enterprise customers with legitimate biology research workflows. Partners include Amgen, Moderna, Novo Nordisk, Thermo Fisher Scientific, the Allen Institute, and NVIDIA. Individual researchers and non-enterprise customers are not supported in the current preview. No public pricing or API generally-available date has been announced.

**Key specs:** Not publicly disclosed | Text + scientific tools | Research preview pricing unknown | Proprietary | Restricted access (U.S. enterprise partners only)

---

### 4. Gemma 4 — Google's Most Capable Open Model, Apache 2.0 Licensed

**Source:** [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4) | [ZBuild](https://www.zbuild.io/resources/news/gemma-4-release-specs-benchmarks-complete-guide-2026) | [Towards AI](https://pub.towardsai.net/googles-gemma-4-is-the-most-architecturally-interesting-open-model-released-this-year-b245a406cd6a)

Google released Gemma 4 on April 2, 2026, under an Apache 2.0 license — the first truly permissive Gemma release, enabling full commercial use without custom restrictions. Four variants ship: E2B (2.3B, dense, 128K context), E4B (4.5B, dense, 128K), 26B MoE (26B total / 3.8B active per token, 256K context), and 31B Dense (256K context). The edge variants (E2B, E4B) are designed for on-device deployment on smartphones, tablets, and Raspberry Pi-class hardware, extending capable AI to fully offline endpoints.

Performance of the 31B Dense variant is the architectural highlight of 2026 in the open-source ecosystem. On AIME 2026 math, it achieves 89.2% — an astonishing 68-point gain over Gemma 3 (which scored 20.8%). On GPQA Diamond, it reaches 84.3%, competitive with proprietary frontier models from late 2025. LiveCodeBench v6 scores 80.0%, and MMLU Pro reaches 85.2%. The 26B MoE achieves 97% of the 31B model's quality while activating only 3.8B parameters per token — making it extremely compute-efficient. The model ranks #3 globally among open models on Arena AI's leaderboard, with the 26B variant at #6, outcompeting models 20× its parameter count.

Native multimodal capability (text, images, video, audio), 140+ supported language support, and a configurable thinking mode with 4,000+ token reasoning chains make this the most architecturally complete open-weight model of the year. Built on the same technology foundation as Gemini 3, Gemma 4 is the closest open-source proxy to a frontier proprietary model available for self-hosting or fine-tuning.

**Key specs:** 256K context (large variants) / 128K (edge) | Text + Image + Video + Audio | Free / Apache 2.0 | Open weights | Hugging Face, Google AI Studio, Vertex AI

---

### 5. Grok 4.20 — xAI's 2M-Context Ultra-Long Reasoning Model

**Source:** [TokenCost](https://tokencost.app/blog/grok-4-20-beta-pricing-benchmarks) | [IBTimes AU](https://www.ibtimes.com.au/grok-420-beta-2-powers-xai-advances-model-tops-benchmarks-saves-lives-april-2026-1866556) | [CloudPrice](https://cloudprice.net/models/xai-grok-4-20)

Released March 31, 2026, Grok 4.20 Beta is xAI's flagship model with the largest context window of any publicly available frontier model: 2.0 million tokens — 8× the context of the original Grok 4. This positions it uniquely for full-codebase analysis, book-length document synthesis, and ultra-long agent memory. The model is available on OpenRouter and the xAI API, with aggressive pricing: $2.00/1M input ($0.20 cached) and $6.00/1M output, underpricing GPT-5.4 by 20% on input and 60% on output.

On instruction-following benchmarks, Grok 4.20 Beta 2 leads all models with 83% on IFBench — its primary differentiator vs. frontier peers. It ranks #1 on BridgeBench (reasoning) and achieves 78% on AA-Omniscience (non-hallucination), setting a record high. The model processes text and images, with reasoning mode available as a switchable variant through the API. Batch API provides a 50% discount at $1.00/1M input and $3.00/1M output.

The "4.20" naming and March 31 release date appear to carry deliberate Musk-associated cultural signaling, but beneath the branding sits a technically serious model. Its 2M context window and aggressive pricing make it particularly appealing for enterprise workloads requiring large-context retrieval or full-repository agentic coding. On the LMSys Arena leaderboard, Grok 4.20 Beta1 holds positions 8th overall (ELO: 1485–1491), trailing Claude Opus 4.7 and Gemini 3.1 Pro but competitive with GPT-5.4.

**Key specs:** 2.0M token context window | Text + Image | $2.00/$6.00 per 1M tokens | Proprietary | xAI API, OpenRouter, Grok.com

---

## Deep Dive: Most Important Release — Claude Opus 4.7 (April 16, 2026)

Claude Opus 4.7 is the defining model event of this period because it represents the convergence of three previously distinct capability vectors — long-context agentic reliability, reasoning-time compute scaling, and vision quality — into a single generally available model that beats all public alternatives on the most practically significant coding benchmark (SWE-bench Verified at 87.6%). It is not the most dramatic leap in any single dimension, but it is the most complete and production-ready model available to developers as of April 27, 2026, and its arrival simultaneously dethroned GPT-5.4 on Arena ELO and extended Anthropic's lead in agentic software engineering.

### What It Can Do

Opus 4.7 reliably executes software engineering workflows spanning hours, not minutes: it maintains coherent multi-step plans over 10+ minute autonomous runs, parallelizes tool calls efficiently, and self-verifies outputs before reporting. In multimodal tasks, the 3.3× vision resolution upgrade enables analysis of dense diagrams, circuit schematics, and scientific charts that previous Claude versions could not resolve. The adaptive thinking system means prompts that require graduate-level reasoning silently receive more compute budget, while simple queries remain fast and cheap. Five effort levels give developers precise control over the latency-vs-capability tradeoff at the API level. Long-context instruction following no longer "washes out" — the model retains and applies instructions embedded anywhere across the full 1M token window.

### Benchmark Highlights

| Benchmark | Claude Opus 4.7 | Previous Best (Publicly Available) |
|---|---|---|
| SWE-bench Verified | **87.6%** | 80.9% (Claude Opus 4.5) |
| GPQA Diamond | **94.2%** | 94.3% (Gemini 3.1 Pro) |
| Terminal-Bench 2.0 | **69.4%** | ~79.8% (ForgeCode + Opus 4.6 agent) |
| Finance Agent | **64.4%** | ~62% (prior SOTA) |
| LMSys Arena Overall ELO (Thinking) | **1505** | 1503–1504 (Opus 4.6 Thinking) |
| LMSys Arena Overall ELO (Standard) | **1498** | 1497–1500 (Opus 4.6) |
| CursorBench | **70%** | 58% (Opus 4.6) |
| BixBench (bioinformatics) | ~0.73 | 0.751 (GPT-Rosalind, same release day) |

### Architecture (Known)

Anthropic has not disclosed the internal architecture of Opus 4.7. No MoE, SSM, or hybrid architecture details have been publicly confirmed. The primary architectural change surfaced in the API is the adaptive thinking system — a dynamic compute budget allocator replacing the fixed `budget_tokens` parameter from Opus 4.6. The `xhigh` effort level is a new tier inserted between `high` and `max`. Structured outputs, function calling, and the full 128K max output token ceiling are unchanged. The model ID is `claude-opus-4-7`.

### Pricing & Availability

- **Input:** $5.00 per 1M tokens
- **Output:** $25.00 per 1M tokens
- **Prompt caching:** Up to 90% savings
- **Batch API:** 50% savings
- **Context window:** 1,000,000 input tokens
- **Max output:** 128,000 tokens
- **Available on:** Claude.ai, Anthropic API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry

### Strategic Significance

Opus 4.7 matters beyond its benchmark numbers because it cements Anthropic's lead in the agentic software engineering market, which is the fastest-growing AI deployment category of 2026. With SWE-bench Verified at 87.6%, Claude Mythos Preview (restricted to enterprise partners) at 93.9%, and the open-access Opus 4.7 at 87.6%, Anthropic controls the top two public and restricted positions in the benchmark that matters most to the enterprise buyer. The adaptive thinking system is the first major step toward dynamic inference pricing — a model that costs more only when the problem warrants it, rather than charging a fixed premium for reasoning capability.

### Competitive Context

GPT-5.4 (released March 5, 2026) priced at $2.50/$15.00 per 1M tokens undercuts Opus 4.7 by half on input and 40% on output, and leads on ARC-AGI-2 (83.3% vs. 75.8%). Gemini 3.1 Pro (released February 2026) at $2.00/$12.00 leads on GPQA Diamond (94.3% vs. 94.2%) and multimodal breadth. Opus 4.7's premium pricing ($5/$25) is therefore justified primarily by its agentic coding advantage (SWE-bench lead of ~7 points over Gemini) and its Thinking-mode Arena ELO lead. For cost-sensitive workloads, GPT-5.4 or Gemini 3.1 Pro at 40-60% lower cost are rational alternatives. The Grok 4.20 2M context window is a distinct competitive advantage Anthropic cannot match in the 1M-context tier.

---

## Benchmark Comparison Data

```json
{"benchmark": "LMSys Chatbot Arena — Overall ELO", "results": [{"model": "Claude Opus 4.7 Thinking", "score": 1505}, {"model": "Claude Opus 4.6 Thinking", "score": 1503}, {"model": "Claude Opus 4.7", "score": 1498}, {"model": "Claude Opus 4.6", "score": 1498}, {"model": "Meta Muse-Spark", "score": 1496}, {"model": "Gemini 3.1 Pro Preview", "score": 1492}, {"model": "Gemini 3 Pro", "score": 1486}, {"model": "Grok 4.20 Beta1", "score": 1488}, {"model": "GPT-5.4 High", "score": 1483}, {"model": "Claude Sonnet 4.6 Thinking", "score": 1470}]}
```

```json
{"benchmark": "SWE-bench Verified (%)", "results": [{"model": "Claude Mythos Preview (Anthropic, restricted)", "score": 93.9}, {"model": "Claude Opus 4.7 Adaptive (Anthropic)", "score": 87.6}, {"model": "GPT-5.3 Codex (OpenAI)", "score": 85.0}, {"model": "Claude Opus 4.5 (Anthropic)", "score": 80.9}, {"model": "Claude Opus 4.6 (Anthropic)", "score": 80.8}, {"model": "Gemini 3.1 Pro (Google)", "score": 80.6}, {"model": "Minimax M 2.5", "score": 80.2}]}
```

```json
{"benchmark": "GPQA Diamond (%)", "results": [{"model": "Claude Mythos Preview (Anthropic)", "score": 94.6}, {"model": "Gemini 3.1 Pro (Google)", "score": 94.3}, {"model": "Claude Opus 4.7 (Anthropic)", "score": 94.2}, {"model": "GPT-5.4 Pro (OpenAI)", "score": 92.8}, {"model": "Gemini 3.1 Pro Preview (Google)", "score": 92.1}, {"model": "GPT-5.4 (OpenAI)", "score": 91.1}, {"model": "Gemma 4 31B Dense (Google)", "score": 84.3}, {"model": "Human PhD expert baseline", "score": 67.0}]}
```

```json
{"benchmark": "ARC-AGI-2 (%)", "results": [{"model": "GPT-5.5 (OpenAI)", "score": 85.0}, {"model": "GPT-5.4 Pro (OpenAI)", "score": 83.3}, {"model": "Gemini 3.1 Pro (Google)", "score": 77.1}, {"model": "Claude Opus 4.7 Adaptive (Anthropic)", "score": 75.8}, {"model": "Grok 4.20 (xAI)", "score": 53.3}, {"model": "Human baseline", "score": 60.0}]}
```

```json
{"benchmark": "AIME 2026 (%)", "results": [{"model": "Kimi K2.6 (Moonshot AI)", "score": 96.4}, {"model": "GLM-5 (Z.AI / Zhipu)", "score": 95.8}, {"model": "Kimi K2.5 (Moonshot AI)", "score": 95.8}, {"model": "GLM-5.1 (Z.AI)", "score": 95.3}, {"model": "Gemini 3 Flash High (Google)", "score": 93.3}, {"model": "Gemma 4 31B Dense (Google)", "score": 89.2}]}
```

```json
{"benchmark": "LiveCodeBench v6 (%)", "results": [{"model": "GLM-4.7 (Z.AI / Zhipu)", "score": 84.9}, {"model": "Claude Opus 4.7 Adaptive (weighted)", "score": 95.2}, {"model": "Gemma 4 31B Dense (Google)", "score": 80.0}, {"model": "DeepSeek V3 (DeepSeek)", "score": 37.6}]}
```

```json
{"benchmark": "Terminal-Bench 2.0 (%)", "results": [{"model": "Codex + GPT-5.5 (OpenAI)", "score": 82.0}, {"model": "ForgeCode + GPT-5.4 (OpenAI)", "score": 81.8}, {"model": "TongAgents + Gemini 3.1 Pro (Google)", "score": 80.2}, {"model": "ForgeCode + Claude Opus 4.6 (Anthropic)", "score": 79.8}, {"model": "SageAgent + GPT-5.3 Codex (OpenAI)", "score": 78.4}]}
```

```json
{"benchmark": "MMLU (%)", "results": [{"model": "GPT-5.4 (OpenAI)", "score": 92.0}, {"model": "Claude Opus 4.6 (Anthropic)", "score": 91.0}, {"model": "Gemini 3.1 Pro (Google)", "score": 90.0}, {"model": "DeepSeek V4 (DeepSeek)", "score": 89.4}, {"model": "Gemma 4 31B Dense (Google)", "score": 85.2}]}
```

```json
{"benchmark": "Artificial Analysis Intelligence Index v4.0 (max 57)", "results": [{"model": "Gemini 3.1 Pro Preview (Google)", "score": 57}, {"model": "GPT-5.4 xhigh (OpenAI)", "score": 57}, {"model": "GPT-5.3 Codex xhigh (OpenAI)", "score": 54}, {"model": "Claude Opus 4.6 (Anthropic)", "score": 53}, {"model": "Claude Sonnet 4.6 (Anthropic)", "score": 52}, {"model": "Meta Muse-Spark", "score": 52}]}
```

```json
{"benchmark": "BixBench Bioinformatics Pass@1 (GPT-Rosalind specialty)", "results": [{"model": "GPT-Rosalind (OpenAI)", "score": 0.751}, {"model": "GPT-5.4 (OpenAI)", "score": 0.732}, {"model": "Grok 4.2 (xAI)", "score": 0.698}, {"model": "Gemini 3.1 Pro (Google)", "score": 0.550}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Opus 4.7 | Anthropic | 1,000,000 | $5.00 | $25.00 | Text, Image |
| Claude Opus 4.6 | Anthropic | 1,000,000 | $5.00 | $25.00 | Text, Image |
| GPT-5.4 | OpenAI | 1,050,000 | $2.50 | $15.00 | Text, Image |
| GPT-5.4 Pro | OpenAI | 1,050,000 | $30.00 | $180.00 | Text, Image |
| Gemini 3.1 Pro | Google | 1,000,000 | $2.00 | $12.00 | Text, Image, Audio, Video, Code |
| Grok 4.20 | xAI | 2,000,000 | $2.00 | $6.00 | Text, Image |
| Meta Muse-Spark | Meta | 262,000 | Free (consumer) | Free (consumer) | Text, Image, Voice |
| DeepSeek V4-Pro | DeepSeek | 1,000,000 | $0.14 | ~$0.56 | Text, Code |
| Qwen 3.5 (397B MoE) | Alibaba | 256,000 | Open-weight | Open-weight | Text, Image |
| Gemma 4 31B Dense | Google | 256,000 | Open-weight (Apache 2.0) | Open-weight | Text, Image, Video, Audio |
| Gemma 4 26B MoE | Google | 256,000 | Open-weight (Apache 2.0) | Open-weight | Text, Image, Video, Audio |
| GPT-5 nano | OpenAI | ~128,000 | $0.05 | $0.40 | Text |
| Mistral Small 3.2 | Mistral | ~128,000 | $0.06 | $0.18 | Text, Code |
| Claude Sonnet 4.6 | Anthropic | 200,000 | $3.00 | $15.00 | Text, Image |
| Gemini 3.1 Flash | Google | 1,000,000 | $0.10 | $0.40 | Text, Image, Audio, Video |

---

## Analysis & Impact

- **For software engineering / coding:** Claude Opus 4.7 is the clear leader for agentic workflows with SWE-bench Verified at 87.6%, though it comes at the highest price point ($5/$25). GPT-5.3 Codex (85%) and Gemini 3.1 Pro (80.6%) are competitive at lower cost. Terminal-Bench 2.0 shows that OpenAI's agents (Codex + GPT-5.5 at 82%) lead in pure terminal-task completion. For cost-sensitive coding, DeepSeek V4-Pro at $0.14/1M input with 89.4% MMLU and strong HumanEval scores is the value leader.

- **For frontier reasoning / math / science:** ARC-AGI-2 remains the hardest broadly-used benchmark, and GPT-5.5 (85%) plus GPT-5.4 Pro (83.3%) lead, with Gemini 3.1 Pro (77.1%) and Claude Opus 4.7 (75.8%) following. On competition math (AIME 2026), Chinese models now dominate: Kimi K2.6 (96.4%) and GLM-5 (95.8%) exceed all Western frontier models reported publicly. GPQA Diamond is saturated at the top — four models now exceed 92%, and the benchmark's discriminative power for ranking top models is nearly exhausted.

- **For multimodal / video / audio:** Gemini 3.1 Pro is the clear leader for true native multimodal (text + image + audio + video + code in a single pipeline). Meta Muse-Spark leads on CharXiv reasoning charts (86.4%) and HealthBench Hard (42.8%). Gemma 4's open-weight four-modality support brings comparable capability to self-hosted deployments. GPT-Rosalind shows the frontier is now moving toward specialized vertical multimodal models in high-value domains like life sciences.

- **For cost-sensitive or open-source:** Gemma 4 under Apache 2.0 is the headline open-weight story — 31B Dense scores 89.2% on AIME 2026 and 84.3% on GPQA Diamond, beating proprietary models from 6 months ago. DeepSeek V4-Pro ($0.14/1M input) and Qwen 3.5 (open-weight, 397B MoE) offer near-frontier performance at a fraction of proprietary API cost. Mistral Small 3.2 ($0.06/$0.18) serves as the practical frontier for budget-constrained high-throughput use cases. The Chinese open-weight ecosystem (Qwen, DeepSeek, Kimi, GLM) now collectively captures ~15% of global AI market share, up from ~1% in January 2025.

- **The "thinking mode" reasoning toggle is now table stakes:** Every major frontier model — Claude (adaptive thinking), GPT-5.4 (reasoning mode), Gemini 3.1 (low/medium/high thinking levels), Grok 4.20 (reasoning variant), Gemma 4 (configurable thinking), and Muse-Spark (Thinking + Contemplating modes) — now ships with switchable extended reasoning. The differentiation is shifting from whether a model can reason to how efficiently it can reason (thought compression, adaptive budgets, effort tuning) and how well it integrates reasoning with tool use in agentic loops.

---

## Key Takeaways (TL;DR)

- **Claude Opus 4.7 reclaims #1** on LMSys Arena (ELO 1505 Thinking, 1498 Standard) and extends Anthropic's SWE-bench lead to 87.6% — the best publicly available agentic coding result in the industry.
- **Meta's closed-weights pivot with Muse Spark** is the biggest strategic news: the company that built the open-source AI ecosystem is now competing proprietary, with thought compression delivering 2.7× token efficiency over Claude Opus 4.6.
- **OpenAI launches its first vertical specialist** in GPT-Rosalind (life sciences), signaling the frontier lab era of domain-specific proprietary models targeting high-value verticals like drug discovery, genomics, and translational medicine.
- **Gemma 4 under Apache 2.0** is the best open-weight release of 2026 to date — AIME 2026 at 89.2%, full multimodal support, 256K context, and four model sizes from on-device edge to 31B Dense.
- **The ARC-AGI-2 barrier is effectively broken** by frontier models (GPT-5.5 at 85%, matching the grand prize threshold), while Chinese models (Kimi K2.6, GLM-5) dominate competition math (AIME 2026 at 96%+), marking a clear bifurcation in where frontier capability is advancing fastest.

---

*Sources:*

- https://www.anthropic.com/news/claude-opus-4-7
- https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm
- https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- https://www.claudedirectory.org/blog/claude-opus-4-7-deep-reasoning
- https://allthings.how/claude-opus-4-7-adaptive-thinking-explained/
- https://www.ibuildwith.ai/blog/effort-thinking-opus-4-7-changed-the-rules/
- https://openai.com/index/introducing-gpt-rosalind/
- https://www.marktechpost.com/2026/04/16/openai-launches-gpt-rosalind-life-sciences-ai/
- https://www.technology.org/2026/04/17/openais-gpt-rosalind-wants-to-shave-years-off-drug-discovery/
- https://help.openai.com/en/articles/20001193-introducing-gpt-rosalind-for-life-sciences-research
- https://www.euronews.com/health/2026/04/17/what-to-know-about-openais-new-model-for-life-sciences-research-gpt-rosalind
- https://openai.com/index/introducing-gpt-5-4/
- https://platform.openai.com/docs/models/gpt-5.4
- https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4
- https://www.zbuild.io/resources/news/gemma-4-release-specs-benchmarks-complete-guide-2026
- https://pub.towardsai.net/googles-gemma-4-is-the-most-architecturally-interesting-open-model-released-this-year-b245a406cd6a
- https://deepmind.google/models/model-cards/gemini-3-1-pro/
- https://llm-stats.com/blog/research/gemini-3.1-pro-launch
- https://www.nxcode.io/resources/news/gemini-3-1-pro-complete-guide-benchmarks-pricing-api-2026
- https://www.marktechpost.com/2026/04/09/meta-superintelligence-lab-releases-muse-spark-a-multimodal-reasoning-model-with-thought-compression-and-parallel-agents/
- https://www.deeplearning.ai/the-batch/with-muse-spark-meta-pivots-away-from-its-open-weights-llama-strategy/
- https://neuralcoretech.com/meta-muse-spark-review-benchmarks-2026/
- https://medium.com/predict/muse-spark-architectural-efficiency-and-the-transition-to-personal-superintelligence-7aa163bca2ec
- https://tokencost.app/blog/grok-4-20-beta-pricing-benchmarks
- https://cloudprice.net/models/xai-grok-4-20
- https://www.ibtimes.com.au/grok-420-beta-2-powers-xai-advances-model-tops-benchmarks-saves-lives-april-2026-1866556
- https://docs.x.ai/developers/models.md
- https://aidevdayindia.org/blogs/lmsys-chatbot-arena-current-rankings/lmsys-chatbot-arena-leaderboard-current-top-models.html
- https://www.promptt.dev/blog/lmsys-chatbot-arena-leaderboard-2026
- https://www.swebench.com/verified
- https://benchlm.ai/benchmarks/sweVerified
- https://benchlm.ai/benchmarks/arcAgi2
- https://arcprize.org/leaderboard
- https://arcprize.org/blog/arc-agi-2-technical-report
- https://benchlm.ai/benchmarks/gpqaDiamond
- https://benchgecko.ai/benchmark/gpqa-diamond
- https://llm-stats.com/benchmarks/aime-2026
- https://benchlm.ai/benchmarks/aime2026
- https://benchlm.ai/benchmarks/liveCodeBench
- https://livecodebench.github.io/
- https://www.tbench.ai/leaderboard/terminal-bench/2.0
- https://airank.dev/benchmarks/terminal-bench-2
- https://www.artificialanalysis.ai/methodology/intelligence-benchmarking
- https://www.promptt.dev/blog/artificial-analysis-intelligence-index-rankings-march-2026
- https://particula.tech/blog/deepseek-v4-qwen-open-source-ai-disruption
- https://openlm.ai/deepseek-v4/
- https://tokenmix.ai/blog/mmlu-benchmark-leaderboard
- https://aicostcheck.com/blog/ai-cost-per-million-tokens-2026
- https://llm-stats.com/blog/research/claude-opus-4-7-launch
- https://www.buildfastwithai.com/blogs/claude-opus-4-7-review-benchmarks-2026
- https://epoch.ai/benchmarks/terminal-bench/
- https://epoch.ai/benchmarks/gpqa-diamond/
