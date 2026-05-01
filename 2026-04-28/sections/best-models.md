# Best Models & Benchmarks — 2026-04-28

## Top Model News (5)

### 1. DeepSeek V4 Pro — 1.6T-Parameter Open-Weight MoE Launches at Frontier Tier
**Source:** [gHacks Tech News](https://www.ghacks.net/2026/04/26/deepseek-releases-v4-models-with-9-5x-lower-memory-requirements-and-huawei-ascend-support/) | [DeepInsightAI](https://deepinsightai.io/deepseek-v4/) | [StackFutures](https://stackfutures.com/blog/deepseek-v4-pro-arena-three-variants-april-2026/) | [ofox.ai](https://ofox.ai/blog/deepseek-v4-release-guide-2026/)

DeepSeek released three V4 variants simultaneously on April 24, 2026: V4 Pro, V4 Pro Thinking, and V4 Flash Thinking. V4 Pro is the largest open-weight model ever released, with 1.6 trillion total parameters and 49 billion active parameters — a Mixture-of-Experts architecture that activates only the most relevant expert pathways per token. V4 Flash weighs 284 billion total parameters with 13 billion active. Both models feature a 1 million token context window and are released under Apache 2.0, available immediately on the DeepSeek API and Hugging Face.

The key technical breakthrough is memory efficiency: a novel hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Heavy Compressed Attention (HCA) reduces KV cache requirements by 9.5× to 13.7× versus V3.2, and inference FLOPs drop to just 27% of the prior generation's per-token cost. The Muon optimizer and Manifold-Constrained Hyper-Connections (mHC) residual upgrades further improve training convergence. Hardware support extends explicitly to Huawei Ascend NPUs — a first for DeepSeek — reflecting China's push to reduce Nvidia GPU dependency.

On benchmarks, V4 Pro scores 80.6% on SWE-bench Verified (matching Gemini 3.1 Pro Preview), 93.5% on LiveCodeBench v6, and claims the #1 open-weight position on GDPval-AA (agentic real-world task evaluation). At $1.74/M input and $3.48/M output, V4 Pro undercuts GPT-5.5 ($5/$30) and Claude Opus 4.7 ($5/$25) by roughly 3–7×, while competing directly with them on coding benchmarks.

**Key specs:** 1M token context | Text-only (V4 Pro/Flash) | $1.74/$3.48 per 1M tokens (Pro), $0.14/$0.28 (Flash) | Apache 2.0 | Live on DeepSeek API and Hugging Face

---

### 2. Claude Mythos Preview — 93.9% SWE-bench, Restricted-Access Cybersecurity Powerhouse
**Source:** [red.anthropic.com](https://red.anthropic.com/2026/mythos-preview) | [NxCode](https://www.nxcode.io/resources/news/claude-mythos-benchmarks-93-swe-bench-every-record-broken-2026) | [AI Tools Kit](https://www.aitoolskit.io/learn/claude-mythos-preview-benchmarks) | [Till Freitag deep dive](https://till-freitag.com/en/blog/claude-mythos-technical-deep-dive-en)

Announced April 7, 2026 and quietly deployed to ~40 vetted organizations, Claude Mythos Preview is Anthropic's most capable model to date and the highest-scoring system on SWE-bench Verified at 93.9% — a 13.1 percentage point jump over Claude Opus 4.6 and 6.3 points ahead of the next public competitor. On USAMO 2026, Mythos scored 97.6% (55 points above Opus 4.6). Terminal-Bench 2.0 score of 82.0% ties the best-recorded result, and it achieves 100% pass rate on all 35 Cybench CTF challenges. This is not a fine-tune or iteration — it sets records across every dimension tested.

The restricted access reflects Anthropic's concern about Mythos's security capabilities: in pre-release testing, the model autonomously identified and exploited zero-day vulnerabilities in major operating systems and browsers, including a 27-year-old OpenBSD zero-day. It discovered $4.6M in smart contract exploits on contracts beyond its knowledge cutoff. Access is gated through Project Glasswing, a coordinated vulnerability disclosure initiative backed by $100M in Anthropic credits and $4M in open-source foundation donations. Launch partners include AWS, Apple, Google, Microsoft, NVIDIA, and CrowdStrike.

Pricing is 5× Claude Opus 4.6: $25/M input and $125/M output. General availability has not been announced. Anthropic's risk report describes Mythos as "the best-aligned model we have released to date," while acknowledging it is used more autonomously and with greater capability than any prior release. This is the most consequential model announcement of April 2026, even if most developers cannot access it.

**Key specs:** Not disclosed (context suspected ≥1M tokens) | Text + code + vision | $25/$125 per 1M tokens | Proprietary | Restricted preview via API, AWS Bedrock, Google Vertex, Microsoft Foundry

---

### 3. GPT-5.5 — First Model to Hit ARC-AGI-2 Grand Prize Threshold (85%)
**Source:** [OpenAI Blog](https://openai.com/index/introducing-gpt-5-5/) | [ARC Prize](https://arcprize.org/competitions/2026/arc-agi-2) | [MarkTechPost](https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/) | [APIdog pricing](https://apidog.com/blog/gpt-5-5-pricing/) | [TonTechnotes scorecard](https://ton-technotes.com/en/blog/2026-04-24-gpt-5-5-honest-scorecard/)

Released April 23, 2026, GPT-5.5 is a fully retrained model — not a fine-tune of GPT-5.4 — and the first to cross 85% on ARC-AGI-2, reaching the competition's grand prize threshold. The ARC-AGI-2 benchmark measures fluid abstract reasoning through visual grid transformation puzzles; the human average is 60%, and the previous frontier sat at 68–77%. GPT-5.5's 85% score is the first time a model has surpassed human-baseline performance on this benchmark. OpenAI framed the model as purpose-built for agentic settings: longer-horizon tasks, computer use, and scientific research.

GPT-5.5 scores 82.7% on Terminal-Bench 2.0, 84.9% on GDPval, and 58.6% SWE-bench Pro (single-pass, no scaffolding). It matches GPT-5.4's latency while claiming ~20% net intelligence improvement accounting for its lower token verbosity. Context window is 1.05M tokens. Notably, GPT-5.5 trails Claude Opus 4.7 (87.6%) and Mythos Preview (93.9%) on SWE-bench Verified under agent scaffolding, and lags Gemini 3.1 Pro on GPQA Diamond, indicating per-benchmark tradeoffs rather than universal dominance.

API pricing doubled over GPT-5.4: $5/M input and $30/M output (standard tier), with a $10/$45 surcharge for prompts exceeding 272K tokens. Batch and Flex pricing cuts rates 50%. The model is rolling out to ChatGPT Plus, Pro, Business, and Enterprise; API availability is live.

**Key specs:** 1.05M token context | Text, vision, audio, code | $5/$30 per 1M tokens (standard) | Proprietary | Generally available via API and ChatGPT

---

### 4. Kimi K2.6 — Open-Weight Agentic Giant: 96.4% AIME, 300 Concurrent Sub-Agents
**Source:** [TokenMix](https://tokenmix.ai/blog/kimi-k2-6-code-preview-review-2026) | [CodeRouter](https://www.coderouter.io/blog/kimi-k2-6-review-coding-benchmarks-2026) | [What LLM?](https://whatllm.org/blog/kimi-k2-6) | [AI Made Tools](https://www.aimadetools.com/blog/kimi-k2-6-complete-guide/)

Moonshot AI released Kimi K2.6 on April 20, 2026 as a 1-trillion-parameter MoE (32B active parameters, 256K context) under a modified MIT license. The model is notable for three reasons: math reasoning (96.4% on AIME 2026, the highest open-weight score on record), coding (80.2% SWE-bench Verified, 58.6% SWE-bench Pro — beating Claude Opus 4.6 and tying GPT-5.5), and agentic capacity (up to 300 concurrent sub-agents with 4,000 coordinated steps). At $0.60/M tokens (blended estimate), it also wins on cost.

LiveCodeBench v6 score of 89.6% is competitive with closed frontier models. GPQA Diamond score of 90.5% exceeds Grok 4.20's 83–88% range and approaches Gemini 3.1 Pro Preview. BrowseComp (agentic search) reaches 83.2%. The 256K native context is a constraint versus V4 Pro's 1M, but INT4 quantization is natively supported, making self-hosted deployment on 8×H100 practical.

The model's position is strategically significant: it proves Chinese open-weight research can match Western proprietary models on math and coding simultaneously — not just one domain. K2.6 refreshes the K2 line previously known primarily for AIME dominance and adds sustained agentic workload capacity, making it the leading open alternative for coding agents in April 2026.

**Key specs:** 256K token context | Text + code | ~$0.60/M blended (API) | Modified MIT | Live on Moonshot API and Hugging Face

---

### 5. Mistral Workflows — Orchestration Engine (Not a Model, But the Most Important Mistral News Today)
**Source:** [VentureBeat](https://venturebeat.com/technology/mistral-ai-launches-workflows-a-temporal-powered-orchestration-engine-already-running-millions-of-daily-executions) | [WinBuzzer](https://winbuzzer.com/2026/04/28/mistral-ai-launches-workflows-a-temporal-powered-o-xcxwbn/) | [Mistral Docs](https://docs.mistral.ai/models/overview)

Mistral launched Workflows in public preview on April 28, 2026 — today. It is not a new language model but a production-grade Temporal-powered orchestration engine embedded in Mistral Studio. The product separates orchestration (cloud-hosted, stateful, observable) from execution (customer-side, data-stays-local) and targets enterprise use cases in logistics, financial compliance, and banking automation. Mistral claims millions of daily executions already running in production.

This release reflects Mistral's strategic pivot from model-centric competition to infrastructure layer. Rather than racing Claude/GPT on benchmark scores, Mistral is pursuing enterprise orchestration stickiness. The Python SDK with async patterns and decorator syntax lowers the barrier for developers accustomed to FastAPI or Celery-style code. No new model was released alongside Workflows — the latest Mistral models remain Small 4 and Voxtral TTS from March 2026.

**Key specs:** Cloud + on-premise hybrid | Python SDK | Temporal-backed state machine | Proprietary SaaS | Public preview in Mistral Studio as of April 28, 2026

---

## Deep Dive: Most Important Release — DeepSeek V4 Pro (April 24, 2026)

DeepSeek V4 Pro is the defining open-source event of April 2026 because it shatters the assumption that closed-source models have an exclusive claim to frontier-tier agentic coding performance. With 1.6 trillion total parameters and Apache 2.0 licensing, it is simultaneously the largest open-weight model ever released and, at $1.74/M input tokens, one of the cheapest frontier-class options available — roughly 3× cheaper than GPT-5.5 and Claude Opus 4.7 on a per-token basis, while matching or approaching their SWE-bench Verified and coding arena scores.

### What It Can Do

DeepSeek V4 Pro handles million-token contexts natively, enabling document-level software engineering across entire codebases. It achieves 80.6% SWE-bench Verified and ranks #3 on the Arena AI Code Leaderboard (1,456 ELO). On GDPval-AA — an agentic benchmark measuring real-world economic productivity tasks — it ranks #1 among open-weight models. Codeforces rating of 3,206 places it 23rd among human competitors. Both V4 Pro and V4 Flash include hybrid thinking/non-thinking inference modes, allowing callers to trade compute for latency depending on task complexity. The 384K maximum output token length enables generating full-file code completions without truncation.

### Benchmark Highlights

| Benchmark | DeepSeek V4 Pro | Previous Open Best | Closed Frontier |
|---|---|---|---|
| SWE-bench Verified | 80.6% | ~73% (V3.2) | 93.9% (Mythos), 87.6% (Opus 4.7) |
| LiveCodeBench v6 | 93.5% | ~89.6% (Kimi K2.6) | ~91% (GPT-5.5 est.) |
| Terminal-Bench 2.0 | 67.9% | ~66.7% (K2.6) | 82.7% (GPT-5.5) |
| GDPval-AA | #1 open-weight | — | Competitive with top closed |
| Codeforces Rating | 3,206 | ~2,700 (V3.2) | ~3,168 (GPT-5.4) |
| Arena AI Code ELO | 1,456 (#3 open) | — | 1,500+ (Claude Opus 4.7 thinking) |

### Architecture (known)

- **Type:** Mixture-of-Experts (MoE), transformer backbone
- **Total parameters:** 1.6 trillion (Pro), 284 billion (Flash)
- **Active parameters per forward pass:** 49B (Pro), 13B (Flash)
- **Attention:** Hybrid Compressed Sparse Attention (CSA) + Heavy Compressed Attention (HCA) — reduces KV cache 9.5–13.7× vs V3.2
- **Optimizer:** Muon (replacing AdamW) for improved convergence
- **Residual connections:** Manifold-Constrained Hyper-Connections (mHC)
- **Training:** 33 trillion tokens, FP4 + FP8 mixed precision
- **Hardware compatibility:** Nvidia A100/H100/H200 and Huawei Ascend NPUs
- **Inference FLOPs:** 27% of V3.2 per token

### Pricing & Availability

| Variant | Input ($/1M) | Output ($/1M) | Context | Max Output |
|---|---|---|---|---|
| V4 Flash | $0.14 | $0.28 | 1M tokens | 384K tokens |
| V4 Pro | $1.74 | $3.48 | 1M tokens | 384K tokens |
| V4 Pro Thinking | $1.74 | $3.48 | 1M tokens | 384K tokens |

Available immediately: DeepSeek API (api.deepseek.com), Hugging Face (under Apache 2.0, full weights), and DeepSeek web chat interface.

### Strategic Significance

DeepSeek V4 is the third time in 14 months that a DeepSeek release disrupted the frontier model market on cost-efficiency grounds. The Apache 2.0 license means any organization can self-host the full 1.6T model (requiring approximately 24×H100 80GB GPUs for BF16, or 12×H100 with FP4) without API dependency or usage fees. For GPU-equipped enterprises, the effective per-token cost drops to hardware electricity — well under $0.01/M tokens. This has direct competitive pressure on OpenAI, Anthropic, and Google's API revenue models.

The Huawei Ascend NPU support is geopolitically significant: it validates the Ascend ecosystem as a viable training and inference alternative to Nvidia in the post-export-control environment, and positions Chinese compute infrastructure as increasingly self-sufficient for frontier model development.

### Competitive Context

V4 Pro occupies a precise niche: it matches Gemini 3.1 Pro Preview on SWE-bench Verified (80.6% each) and trades blows with Claude Opus 4.7 (87.6%) and GPT-5.5 (58.6% Pro / ~82% Verified estimates) at one-third the API cost. It trails Claude Mythos Preview (93.9% SWE-bench) and GPT-5.5 (85% ARC-AGI-2) on the highest capability benchmarks, but those models cost 3–70× more per token. For developers who need capable, cheap, self-hostable coding and agentic intelligence, DeepSeek V4 Pro is the clear choice in April 2026.

---

## Benchmark Comparison Data

```json
{"benchmark": "SWE-bench Verified", "results": [
  {"model": "Claude Mythos Preview", "score": 93.9},
  {"model": "Claude Opus 4.7", "score": 87.6},
  {"model": "GPT-5.3-Codex", "score": 85.0},
  {"model": "MiniMax M2.5", "score": 80.2},
  {"model": "Kimi K2.6", "score": 80.2},
  {"model": "Claude Opus 4.6", "score": 80.8},
  {"model": "Gemini 3.1 Pro Preview", "score": 80.6},
  {"model": "DeepSeek V4 Pro", "score": 80.6},
  {"model": "GPT-5.5", "score": 79.0},
  {"model": "Qwen 3.6 Plus", "score": 78.8}
]}
```

```json
{"benchmark": "SWE-bench Pro", "results": [
  {"model": "Claude Mythos Preview", "score": 77.8},
  {"model": "Claude Opus 4.7", "score": 64.3},
  {"model": "Kimi K2.6", "score": 58.6},
  {"model": "GPT-5.5", "score": 58.6},
  {"model": "GPT-5.4", "score": 57.7},
  {"model": "Gemini 3.1 Pro Preview", "score": 54.2},
  {"model": "Claude Opus 4.6", "score": 53.4}
]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [
  {"model": "GPT-5.5", "score": 85.0},
  {"model": "GPT-5.4 Pro", "score": 83.3},
  {"model": "Gemini 3.1 Pro", "score": 77.1},
  {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8},
  {"model": "Grok 4.20", "score": 53.3},
  {"model": "Human average", "score": 60.0}
]}
```

```json
{"benchmark": "GPQA Diamond", "results": [
  {"model": "Claude Mythos Preview", "score": 94.5},
  {"model": "Gemini 3.1 Pro", "score": 94.3},
  {"model": "Claude Opus 4.7", "score": 94.2},
  {"model": "GPT-5.4 Pro", "score": 92.8},
  {"model": "Gemini 3.1 Pro Preview", "score": 92.1},
  {"model": "Kimi K2.6", "score": 90.5},
  {"model": "GPT-5.4", "score": 91.1},
  {"model": "Claude Opus 4.6", "score": 87.4},
  {"model": "Grok 4.20", "score": 85.5},
  {"model": "Gemma 4 31B", "score": 84.3}
]}
```

```json
{"benchmark": "AIME 2026", "results": [
  {"model": "Kimi K2.6", "score": 96.4},
  {"model": "GPT-5.4", "score": 99.2},
  {"model": "DeepSeek V4 Pro", "score": 99.4},
  {"model": "Gemma 4 31B", "score": 89.2},
  {"model": "Claude Opus 4.7", "score": 88.0},
  {"model": "Gemini 3.1 Pro Preview", "score": 91.2}
]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [
  {"model": "Claude Mythos Preview", "score": 82.0},
  {"model": "GPT-5.5", "score": 82.7},
  {"model": "Claude Opus 4.7", "score": 69.4},
  {"model": "DeepSeek V4 Pro", "score": 67.9},
  {"model": "Kimi K2.6", "score": 66.7},
  {"model": "Claude Opus 4.6", "score": 65.4},
  {"model": "GPT-5.4", "score": 64.0}
]}
```

```json
{"benchmark": "LiveCodeBench v6", "results": [
  {"model": "DeepSeek V4 Pro", "score": 93.5},
  {"model": "Kimi K2.6", "score": 89.6},
  {"model": "GPT-5.4", "score": 87.5},
  {"model": "Gemini 3.1 Pro", "score": 82.9},
  {"model": "Meta Muse Spark", "score": 80.0},
  {"model": "Grok 4.20", "score": 74.2},
  {"model": "Claude Opus 4.6", "score": 70.7}
]}
```

```json
{"benchmark": "LMSys Arena Overall ELO", "results": [
  {"model": "Claude Opus 4.7 Thinking", "score": 1505},
  {"model": "Claude Opus 4.6 Thinking", "score": 1503},
  {"model": "Gemini 3.1 Pro Preview", "score": 1498},
  {"model": "Grok 4.20 Beta1", "score": 1497},
  {"model": "Meta Muse Spark", "score": 1496},
  {"model": "Gemini 3 Pro", "score": 1492},
  {"model": "Grok 4.20 Beta-Reasoning", "score": 1486},
  {"model": "GPT-5.4 High", "score": 1484},
  {"model": "GPT-5.2 Chat Latest", "score": 1482},
  {"model": "Gemini 3 Flash", "score": 1480}
]}
```

```json
{"benchmark": "GDPval (Agentic Work Quality)", "results": [
  {"model": "GPT-5.5", "score": 84.9},
  {"model": "DeepSeek V4 Pro", "score": 83.1},
  {"model": "Claude Opus 4.7", "score": 82.0},
  {"model": "Gemini 3.1 Pro Preview", "score": 79.4},
  {"model": "GPT-5.4", "score": 77.2}
]}
```

```json
{"benchmark": "MMLU (Pro/standard, approx)", "results": [
  {"model": "Gemini 3.1 Pro Preview", "score": 90.4},
  {"model": "Claude Opus 4.7", "score": 89.8},
  {"model": "GPT-5.5", "score": 89.5},
  {"model": "Kimi K2.6", "score": 88.7},
  {"model": "Llama 4 Maverick", "score": 85.2},
  {"model": "Gemma 4 31B", "score": 84.1}
]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Mythos Preview | Anthropic | Not disclosed (est. ≥1M) | $25.00 | $125.00 | Text, code, vision |
| GPT-5.5 | OpenAI | 1,050,000 | $5.00 | $30.00 | Text, vision, audio, code |
| Claude Opus 4.7 | Anthropic | 1,000,000 | $5.00 | $25.00 | Text, code, vision |
| GPT-5.4 Pro | OpenAI | 1,000,000 | $30.00 | $180.00 | Text, vision, audio, code |
| GPT-5.4 | OpenAI | 1,000,000 | $2.50 | $15.00 | Text, vision, audio, code |
| Gemini 3.1 Pro Preview | Google | 2,000,000 | $1.25 | $10.00 | Text, vision, audio, video |
| Grok 4.20 | xAI | 2,000,000 | $2.00 | $10.00 | Text, vision, code |
| Claude Opus 4.6 | Anthropic | 1,000,000 | $5.00 | $25.00 | Text, code, vision |
| DeepSeek V4 Pro | DeepSeek | 1,000,000 | $1.74 | $3.48 | Text, code |
| DeepSeek V4 Flash | DeepSeek | 1,000,000 | $0.14 | $0.28 | Text, code |
| Kimi K2.6 | Moonshot AI | 256,000 | ~$0.60 | ~$0.60 | Text, code |
| Llama 4 Maverick | Meta | 1,000,000 | Free (self-host) | Free | Text, vision, code |
| Llama 4 Scout | Meta | 10,000,000 | Free (self-host) | Free | Text, vision, code |
| Gemma 4 31B | Google | 256,000 | Free (self-host) | Free | Text, vision, audio, video |
| Qwen 3.5 (397B MoE) | Alibaba | 256,000 | Free (self-host) | Free | Text, vision, code |

---

## Analysis & Impact

- **For software engineering / coding:** The SWE-bench Verified tier is fracturing into three camps. Claude Mythos Preview (93.9%, restricted access) is a category apart. Claude Opus 4.7 (87.6%) and GPT-5.3-Codex (85.0%) lead among broadly accessible models. DeepSeek V4 Pro (80.6%) and Kimi K2.6 (80.2%) bring frontier-tier coding capability to open-weight / low-cost settings. For cost-constrained teams doing high-volume agentic coding, V4 Pro or K2.6 are now the rational defaults — you no longer have to pay $25–$30/M output to be competitive.

- **For frontier reasoning / math / science:** GPT-5.5's 85% ARC-AGI-2 score is the headline: it is the first model to surpass the benchmark's grand prize threshold and cross the 60% human-average floor by 25 points. However, the GPQA Diamond frontier is essentially saturated in the 92–95% range (Mythos 94.5%, Gemini 3.1 Pro 94.3%, Opus 4.7 94.2%), meaning grad-level science benchmarks no longer cleanly discriminate models. AIME 2026 still shows spread: DeepSeek V4 Pro (99.4%) and GPT-5.4 (99.2%) are near-perfect; Kimi K2.6 (96.4%) leads open-weights. New, harder math benchmarks (FrontierMath, HMMT) will become the new discriminators.

- **For multimodal / video / audio:** Gemini 3.1 Pro Preview with its 2M token context and native video/audio processing retains a structural advantage. GPT-5.5 added audio capabilities. Llama 4 Scout's 10M context window is the most extreme in the field for long-document multimodal retrieval. Gemma 4's full audio/video support at the 31B open-weight level is notable for embedded and edge deployment use cases. Nucleus-Image (17B MoE diffusion) brings open-weight frontier image generation.

- **For cost-sensitive or open-source:** April 2026 is the strongest month in history for open-source AI. Three major Apache 2.0 releases (DeepSeek V4, Gemma 4, Qwen 3.5) and one MIT release (Kimi K2.6) cover the full performance-cost spectrum. DeepSeek V4 Flash at $0.14/M input is the cheapest frontier-adjacent option for bulk inference. Self-hosted Llama 4 Scout provides a 10M context multimodal model with zero API cost. Gemma 4 31B is the most versatile open-weight package (multimodal, audio, video, 256K context, Apache 2.0) for regulated industries that cannot use proprietary APIs.

- **The 1M token context window is now table stakes:** Every major frontier model — Claude Opus 4.7, GPT-5.5, DeepSeek V4 Pro/Flash, Gemini 3.1 Pro, Grok 4.20, and Llama 4 Maverick — offers at least 1M tokens. Llama 4 Scout offers 10M and Gemini 3.1 Pro 2M. Context length has ceased to be a competitive differentiator among tier-1 models; the battle has shifted to what models can reliably *do* within that context (retrieval accuracy, long-range reasoning, multi-file code editing).

---

## Key Takeaways (TL;DR)

- **DeepSeek V4 Pro** (Apache 2.0, 1.6T params, $1.74/M) is the most important open-weight release of April 2026: 80.6% SWE-bench Verified and #1 open-weight GDPval at 3× lower cost than GPT-5.5 or Claude Opus 4.7.
- **Claude Mythos Preview** holds the all-time SWE-bench Verified record (93.9%) and 100% Cybench CTF pass rate, but is restricted to ~40 organizations through Project Glasswing due to its autonomous cybersecurity capabilities.
- **GPT-5.5** crossed the ARC-AGI-2 grand prize threshold (85%), the first model ever to do so, making it the abstract reasoning champion — though it trails on SWE-bench and GPQA Diamond vs. the Anthropic/Google leaders.
- **Kimi K2.6** (open-weight, modified MIT, $0.60/M blended) combines 96.4% AIME 2026 math with 80.2% SWE-bench Verified and 300-concurrent-agent capacity, making it the leading open alternative for agentic coding systems.
- The benchmark frontier is bifurcating: **closed models** (Mythos, GPT-5.5) push abstract reasoning and security capabilities to new extremes, while **open-weight models** (V4 Pro, K2.6, Gemma 4) achieve parity on practical coding tasks at a fraction of the cost.

---

*Sources:*
- https://www.ghacks.net/2026/04/26/deepseek-releases-v4-models-with-9-5x-lower-memory-requirements-and-huawei-ascend-support/
- https://deepinsightai.io/deepseek-v4/
- https://stackfutures.com/blog/deepseek-v4-pro-arena-three-variants-april-2026/
- https://ofox.ai/blog/deepseek-v4-release-guide-2026/
- https://www.aimadetools.com/blog/deepseek-v4-pro-complete-guide/
- https://deepseekv4pro.com/benchmarks/models/deepseek-v4
- https://www.linkedin.com/pulse/deepseek-v4-pro-1-open-weights-model-gdpval-aa-artificial-analysis-bvemc
- https://red.anthropic.com/2026/mythos-preview
- https://www.nxcode.io/resources/news/claude-mythos-benchmarks-93-swe-bench-every-record-broken-2026
- https://www.aitoolskit.io/learn/claude-mythos-preview-benchmarks
- https://claudemythosai.io/blog/mythos-preview-official-release/
- https://till-freitag.com/en/blog/claude-mythos-technical-deep-dive-en
- https://benchgecko.ai/model/claude-mythos-preview
- https://openai.com/index/introducing-gpt-5-5/
- https://arcprize.org/competitions/2026/arc-agi-2
- https://arcprize.org/leaderboard
- https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/
- https://apidog.com/blog/gpt-5-5-pricing/
- https://llmcost.app/models/gpt-5-5
- https://ton-technotes.com/en/blog/2026-04-24-gpt-5-5-honest-scorecard/
- https://benchlm.ai/benchmarks/arcAgi2
- https://tokenmix.ai/blog/kimi-k2-6-code-preview-review-2026
- https://www.coderouter.io/blog/kimi-k2-6-review-coding-benchmarks-2026
- https://whatllm.org/blog/kimi-k2-6
- https://www.aimadetools.com/blog/kimi-k2-6-complete-guide/
- https://aitoolsrecap.com/Blog/moonshot-ai-kimi-k2-6-release-coding-agent-benchmarks-2026
- https://venturebeat.com/technology/mistral-ai-launches-workflows-a-temporal-powered-orchestration-engine-already-running-millions-of-daily-executions
- https://winbuzzer.com/2026/04/28/mistral-ai-launches-workflows-a-temporal-powered-o-xcxwbn/
- https://medium.com/@rogt.x1997/87-6-77-3-64-3-why-claude-opus-4-7-is-dominating-ai-benchmarks-71f3b970caa3
- https://tokenmix.ai/blog/swe-bench-2026-claude-opus-4-7-wins
- https://llm-stats.com/blog/research/claude-opus-4-7-launch
- https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/
- https://whatllm.org/blog/gemini-3-1-pro-preview
- https://siliconangle.com/2026/04/22/google-launches-ai-research-agents-powered-gemini-3-1-pro/
- https://aidevdayindia.org/blogs/lmsys-chatbot-arena-current-rankings/lmsys-chatbot-arena-leaderboard-current-top-models.html
- https://lmmarketcap.com/arenas
- https://benchlm.ai/benchmarks/sweVerified
- https://benchlm.ai/benchmarks/gpqaDiamond
- https://benchlm.ai/benchmarks/liveCodeBenchPro
- https://particula.tech/blog/deepseek-v4-qwen-open-source-ai-disruption
- https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/
- https://www.doolpa.com/news/google-gemma-4-release-april-2026
- https://awesomeagents.ai/models/kimi-k2-6/
- https://apiscout.dev/blog/llm-api-pricing-comparison-2026
- https://www.morphllm.com/llm-cost-calculator
