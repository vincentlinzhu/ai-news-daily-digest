# Best Models & Benchmarks — 2026-04-29

> **Section:** Best Models & Benchmarks | **Date:** April 29, 2026 | **Agent:** research-models

---

## Top Stories

### 1. Claude Opus 4.7 Launches: 87.6% SWE-bench Verified, xhigh Thinking, Constrained Cyber Capabilities

Anthropic released **Claude Opus 4.7** on April 16, 2026 — its most capable publicly available model — with a notable deliberate tradeoff: significantly boosted software engineering performance paired with intentionally constrained cybersecurity capabilities.

**Benchmark highlights:**
- **SWE-bench Verified: 87.6%** (up from 80.8% in Opus 4.6; +6.8 pp)
- **SWE-bench Pro: 64.3%** (up from 53.4%; +10.9 pp) — leads GPT-5.4 (57.7%) and Gemini 3.1 Pro (54.2%) on this harder evaluation
- **GPQA Diamond: 94.2%** — graduate-level scientific knowledge
- **Terminal-Bench 2.0: 69.4%**
- **OSWorld-Verified (computer use): 78.0%**
- **MCP-Atlas (tool use): 77.3%**
- **ARC-AGI-2: 75.8%** (Adaptive variant)
- **BrowseComp (agentic search): 79.3%** — notable regression from 83.7% in predecessor
- **CursorBench: 70%** (up from 58%)
- **LMArena Elo: ~1497–1498** (non-thinking), **~1504–1505** (thinking variant) — top-2 globally

**New capabilities:**
- `xhigh` effort level between `high` and `max` for finer reasoning control granularity
- Self-verification: model checks outputs before reporting, reducing errors on long-running agentic tasks
- 3.3× higher-resolution vision analysis (up to 3.75 megapixels per image)
- Improved file-system memory across multi-session agent workflows
- 1M token context window, 128K max output tokens

**Cybersecurity stance:** The 232-page system card reveals Anthropic deliberately reduced Opus 4.7's cyber capabilities during training. UK AI Security Institute testing confirmed the model cannot fully compromise a cyber range but can execute reconnaissance, lateral movement, credential extraction, and browser credential theft. A new **Cyber Verification Program** grants authorized security researchers (pen-testers, red teams, vuln researchers) access to a higher-capability tier.

**Pricing:** Unchanged at $5/M input, $25/M output. Available on Claude API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry.

**Sources:**
- [Anthropic Blog](https://www.anthropic.com/news/claude-opus-4-7)
- [System Card deep-dive (allthings.how)](https://allthings.how/claude-opus-4-7-system-card-key-findings-and-benchmarks/)
- [Vellum benchmarks breakdown](https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained)

---

### 2. Poolside Laguna M.1 and XS.2: New Agentic Coding Models (72.5% / 68.2% SWE-bench Verified)

**Poolside AI** released two new models from its Laguna family on April 28, 2026, targeting professional agentic software engineering with a focus on long-horizon task completion.

**Laguna M.1** (proprietary, API-only):
- 225B total parameters, 23B active (MoE)
- Trained on 30T tokens across 6,144 NVIDIA Hopper GPUs
- SWE-bench Verified: **72.5%** | Multilingual: 67.3% | Pro: 46.9%
- Terminal-Bench 2.0: 40.7%
- Available via Poolside API (limited preview)

**Laguna XS.2** (open-weight, Apache 2.0):
- 33B total parameters, 3B active (2nd-gen MoE)
- Trained on 30T tokens; built on lessons from M.1's training run
- SWE-bench Verified: **68.2%** | Multilingual: 62.4% | Pro: 44.5%
- Terminal-Bench 2.0: 30.1%
- 128K token context window; native reasoning support; FP8 KV cache quantization
- Runs locally on Mac with 36GB RAM via Ollama
- vLLM support merged April 28, 2026
- Also available on OpenRouter

**Significance:** Laguna XS.2 is a rare case of an open-weight model at the 3B-active parameter tier scoring above 68% on SWE-bench Verified — competitive with models many times its active compute. Poolside also released an open-source agent harness ("pool") for orchestrating the model.

**Sources:**
- [MarkTechPost announcement](https://www.marktechpost.com/2026/04/28/poolside-ai-introduces-laguna-xs-2-and-m-1-agentic-coding-models-reaching-68-2-and-72-5-on-swe-bench-verified/)
- [Poolside blog deep dive](https://poolside.ai/blog/laguna-a-deeper-dive)
- [HuggingFace model card](https://huggingface.co/poolside/Laguna-XS.2)
- [OpenRouter pricing page](https://openrouter.ai/poolside/laguna-xs.2)

---

### 3. IBM Granite 4.1 Family: 512K Context, 15T Tokens, Enterprise-Grade Apache 2.0

IBM released its **Granite 4.1 family** on April 29, 2026 — today — in the most expansive model release in the Granite line's history. The family spans language, vision, speech, embedding, and guardian safety models.

**Language model lineup (3B / 8B / 30B):**

| Model | MMLU (5-shot) | GSM8K (8-shot) | HumanEval (pass@1) | ArenaHard |
|-------|:---:|:---:|:---:|:---:|
| granite-4.1-3b-instruct | 67.0% | 86.9% | 79.3% | 37.8 |
| granite-4.1-8b-instruct | 73.8% | 92.5% | 87.2% | 69.0 |
| granite-4.1-30b-instruct | 80.2% | 94.2% | 89.6% | 71.0 |

**Architecture notes:**
- Trained on ~15 trillion tokens across multi-phase runs
- Extended context to 512K tokens — notable for enterprise document workflows
- 8B instruct variant matches or outperforms the previous 32B MoE model, suggesting improved training efficiency over architecture bloat
- Additional modality models: state-of-the-art ASR accuracy (speech), table/chart extraction (vision), harm detection (Granite Guardian)

**Licensing:** Apache 2.0 across the full family. Available on Hugging Face, Ollama, and watsonx.ai.

**Sources:**
- [IBM Research blog](https://research.ibm.com/blog/granite-4-1-ai-foundation-models)
- [Agent Times coverage](https://theagenttimes.com/articles/ibm-releases-granite-4-1-8b-under-apache-2-0-for-local-agent-ecc5b5f4)

---

### 4. Nvidia Nemotron 3 Nano Omni: 30B-A3B Mamba-MoE Multimodal at 9× Throughput

Nvidia released **Nemotron 3 Nano Omni** on April 28, 2026 — a uniquely efficient open multimodal model that collapses text, image, video, and audio processing into a single model using a Mamba-Transformer hybrid MoE architecture.

**Architecture:**
- 30B total parameters, 3B active per inference (Mamba-Transformer hybrid + MoE)
- 256K token context window
- Trained on 717B tokens, with synthetic data from Qwen, GPT-OSS, and DeepSeek-OCR

**Benchmark highlights:**

| Benchmark | Nemotron 3 Nano Omni | Previous Nemotron |
|-----------|:---:|:---:|
| OCRBenchV2-En | 65.8 | 61.2 |
| MMLongBench-Doc | 57.5 | 38.0 |
| CharXiv reasoning | 63.6 | 41.3 |
| ScreenSpot-Pro (GUI) | 57.8 | — |
| OSWorld (computer use) | **47.4** | 11.0 |

- Leads WorldSense, DailyOmni, and VoiceBench in audio/video understanding
- MediaPerf: highest throughput and lowest inference cost for video-level tagging

**Efficiency claims:**
- **9× higher throughput** vs. Qwen3-Omni at comparable interactivity
- **2.9× faster** single-stream multimodal reasoning
- 7.4× higher system efficiency for multi-document tasks
- 9.2× higher for video tasks vs. comparable open models

**Sources:**
- [NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/)
- [HuggingFace blog](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence)
- [arXiv technical report: 2604.24954](https://arxiv.org/html/2604.24954)
- [The Decoder analysis](https://the-decoder.com/with-nemotron-3-nano-omni-nvidia-reveals-what-really-goes-into-a-modern-multimodal-model/)

---

### 5. Qwen3.6-27B Dense: 27B Model Outperforms Alibaba's Own 397B MoE on Coding

Alibaba's Qwen team released **Qwen3.6-27B** on April 22, 2026 — a fully dense (non-MoE) open-weight model that beats the much larger Qwen3.5-397B-A17B on agentic coding benchmarks despite being 14.7× smaller in active compute.

**Architecture:**
- 27B parameters, all active (fully dense)
- Hybrid Gated DeltaNet + gated multi-head attention (64 layers; 3:1 linear:full-attention ratio)
- Native 262K token context; YaRN-extended to 1,010,000 tokens
- Apache 2.0 license on HuggingFace

**Benchmarks:**
- SWE-bench Verified: **77.2%** (vs. 75.0% predecessor)
- Terminal-Bench 2.0: **59.3%**
- GPQA Diamond: **87.8%**
- NL2Repo: 36.2% (repo-level generation)
- QwenWebBench: 1487 Elo (frontend code)

**Novel feature — Thinking Preservation:** A template flag that retains earlier chain-of-thought reasoning blocks in visible conversation history across multi-turn tool calls. This avoids the model redundantly re-deriving the same intermediate steps each round — a meaningful efficiency gain for long-horizon agentic workflows.

**Earlier in the Qwen3.6 cycle (April 16):** Alibaba released **Qwen3.6-35B-A3B** (MoE, 35B total / 3B active), which scores 73.4% on SWE-bench Verified and 92.7% on AIME 2026, making it the most efficient model per active parameter on coding benchmarks at time of release.

**Sources:**
- [MarkTechPost](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)
- [Mervin Praison architecture deep-dive](https://mer.vin/2026/04/qwen3-6-27b-dense-hybrid-attention-and-thinking-preservation/)
- [GitHub: QwenLM/Qwen3.6](https://github.com/QwenLM/Qwen3.6)

---

## Deep Dive: The SWE-bench Verified Leaderboard as of April 29, 2026

SWE-bench Verified (500 human-validated GitHub issues from real Python repos) has become the primary signal for real-world software engineering capability. The leaderboard has shifted dramatically in 2026:

```json
{
  "benchmark": "SWE-bench Verified",
  "as_of": "2026-04-29",
  "leaderboard": [
    {"rank": 1, "model": "Claude Mythos Preview", "org": "Anthropic", "score": 93.9, "notes": "Restricted release, ~40 orgs"},
    {"rank": 2, "model": "Claude Opus 4.7 (Adaptive)", "org": "Anthropic", "score": 87.6, "notes": "GA since April 16"},
    {"rank": 3, "model": "GPT-5.3 Codex", "org": "OpenAI", "score": 85.0, "notes": ""},
    {"rank": 4, "model": "MiniMax M2.5", "org": "MiniMax", "score": 80.2, "notes": "Open-weight, 229B-A10B"},
    {"rank": 5, "model": "Gemini 3.1 Pro", "org": "Google DeepMind", "score": 80.6, "notes": "Released Feb 19"},
    {"rank": 6, "model": "MiMo-V2.5-Pro", "org": "Xiaomi", "score": 78.9, "notes": "1.02T-A42B, released Apr 27"},
    {"rank": 7, "model": "GLM-5", "org": "Z.ai (Zhipu AI)", "score": 77.8, "notes": "744B-A44B MoE"},
    {"rank": 8, "model": "Qwen3.6-27B", "org": "Alibaba", "score": 77.2, "notes": "Dense 27B, Apache 2.0"},
    {"rank": 9, "model": "Qwen3.6-35B-A3B", "org": "Alibaba", "score": 73.4, "notes": "MoE, 3B active"},
    {"rank": 10, "model": "Laguna M.1", "org": "Poolside AI", "score": 72.5, "notes": "225B-A23B MoE"},
    {"rank": 11, "model": "Grok 4.20", "org": "xAI", "score": 72.0, "notes": "~3T MoE, released Mar 31"},
    {"rank": 12, "model": "Laguna XS.2", "org": "Poolside AI", "score": 68.2, "notes": "Open-weight, 33B-A3B, Apache 2.0"}
  ]
}
```

**Key observations:**
- The gap between the top proprietary model (Mythos at 93.9%) and the best open-weight model (MiniMax M2.5 at 80.2%) has narrowed to 13.7 pp — its smallest ever
- Claude Opus 4.7's SWE-bench Pro score of 64.3% (harder variant, real-world non-curated issues) already exceeds where Verified was 12 months ago — the whole distribution is shifting up
- Poolside's Laguna XS.2 achieves 68.2% with only 3B active parameters — the most efficient active-compute model on the board

---

## LMArena (Chatbot Arena) Leaderboard Snapshot — April 2026

```json
{
  "benchmark": "LMArena (Chatbot Arena)",
  "methodology": "Bradley-Terry model, bootstrap CI ±5–11 Elo points",
  "total_votes": "5.8M+",
  "models_tracked": "339–635",
  "as_of": "2026-04-29",
  "top_10": [
    {"rank": 1, "model": "Claude Opus 4.7 Thinking", "elo": 1505},
    {"rank": 2, "model": "Claude Opus 4.6 Thinking", "elo": 1502},
    {"rank": 3, "model": "Claude Opus 4.7", "elo": 1497},
    {"rank": 4, "model": "Claude Opus 4.6", "elo": 1496},
    {"rank": 5, "model": "Meta Muse Spark", "elo": 1494},
    {"rank": 6, "model": "Gemini 3.1 Pro Preview", "elo": 1492},
    {"rank": 7, "model": "Gemini 3 Pro", "elo": 1486},
    {"rank": 8, "model": "Grok 4.20 Beta1", "elo": 1484},
    {"rank": 9, "model": "GPT-5.4 High", "elo": 1482},
    {"rank": 10, "model": "Claude Sonnet 4.6 Thinking", "elo": 1467}
  ],
  "note": "Anthropic holds 4 of top 5 slots within a ~20-point cluster; #1 coding: Claude Opus 4.7 (82.0% SWE-bench Verified per internal coding leaderboard)"
}
```

**Sources:** [LMArena 2026 overview (promptt.dev)](https://www.promptt.dev/blog/lmsys-chatbot-arena-leaderboard-2026) | [SmartChunks Elo deep-dive](https://smartchunks.com/lmsys-arena-elo-leaderboard-explained-2026/)

---

## ARC-AGI-2 Leaderboard — April 27, 2026

```json
{
  "benchmark": "ARC-AGI-2",
  "human_average": 66,
  "grand_prize_threshold": 85,
  "prize_pool": "$700,000",
  "as_of": "2026-04-27",
  "leaderboard": [
    {"rank": 1, "model": "GPT-5.5", "org": "OpenAI", "score": 85.0, "notes": "First to hit Grand Prize threshold"},
    {"rank": 2, "model": "GPT-5.4 Pro", "org": "OpenAI", "score": 83.3},
    {"rank": 3, "model": "Gemini 3.1 Pro", "org": "Google DeepMind", "score": 77.1, "notes": "2× Gemini 3 Pro's 31.1%"},
    {"rank": 4, "model": "Claude Opus 4.7 (Adaptive)", "org": "Anthropic", "score": 75.8},
    {"rank": 5, "model": "Grok 4.20", "org": "xAI", "score": 53.3}
  ],
  "total_evaluated": 10
}
```

GPT-5.5 hitting exactly 85% — the Grand Prize threshold — is significant: it's the first model to surpass average human performance (66%) on a benchmark specifically designed to resist pattern-matching and require genuine fluid intelligence. The 10-model evaluation count reflects how few models are competitively submitted at this level.

**Sources:** [BenchLM ARC-AGI-2 tracker](https://benchlm.ai/benchmarks/arcAgi2) | [ARC Prize 2026 competition page](https://arcprize.org/competitions/2026/arc-agi-2)

---

## Notable Models Not in Top Stories (Additional Releases)

### Xiaomi MiMo-V2.5-Pro (April 27, 2026)
Xiaomi released MiMo-V2.5-Pro (1.02T total, 42B active, 1M context) with improved agentic capabilities over the March V2 release. It matches Claude Opus 4.6 on SWE-bench Pro (57.2% vs 57.3%) and leads on Terminal-Bench 2.0 (68.4% vs 65.4%). Priced at $1/M input, $3/M output — roughly 5× cheaper than Opus 4.6 at equivalent task difficulty. Open-source via Xiaomi's GitHub.

**Source:** [BuildFastWithAI review](https://www.buildfastwithai.com/blogs/xiaomi-mimo-v2-5-pro-review-2026)

### GLM-5.1 from Z.ai (April 7, 2026)
Z.ai (formerly Zhipu AI) updated GLM-5 to GLM-5.1, which now leads SWE-bench Pro globally at **58.4%** — above GPT-5.4 (57.7%) and Claude Opus 4.6 (57.3%). Architecture: 744B-A44B MoE, DeepSeek sparse attention, 200K context, MIT license. AIME 2026: 95.3%. BrowseComp: 68.0% (best). CyberGym: 68.7% (top). Autonomous coding runs up to 8 hours sustained.

**Source:** [GLM-5.1 review](https://buildfastwithai.com/blogs/glm-5-1-open-source-review-2026) | [NYU Shanghai RITS analysis](https://rits.shanghai.nyu.edu/ai/glm-5-1-z-ais-open-weight-model-takes-1-on-swe-bench-pro/)

### Meta Muse Spark (April 8, 2026)
Meta launched Muse Spark from its Meta Superintelligence Labs — a natively multimodal reasoning model and a strategic pivot away from its open-weights Llama strategy. Supports 262K context; "Contemplating mode" orchestrates parallel sub-agents, achieving 58% on Humanity's Last Exam and 38% on FrontierScience Research. LMArena Elo ~1494 (#5). Available on meta.ai, WhatsApp, Instagram, Facebook, Messenger, and Ray-Ban glasses.

**Source:** [Meta AI Blog](https://ai.meta.com/blog/introducing-muse-spark-1-msl/) | [TechCrunch](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai)

### Grok 4.20 from xAI (March 31, 2026)
xAI's Grok 4.20 uses a ~3T parameter MoE backbone with native multi-agent capabilities (up to 16 coordinating sub-agents). Context: 2M tokens. Pricing: $2/M input, $6/M output. GPQA Diamond: 91.1%. Output throughput: 234.9 tokens/sec (leading among flagships). Claims 78% non-hallucination rate (omniscience) and 65% reduction in hallucinations vs. Grok 4.1. LMArena Elo ~1484 (#8 overall).

**Source:** [Benchable.ai model card](https://benchable.ai/models/x-ai/grok-4.20) | [Awesome Agents overview](https://awesomeagents.ai/models/grok-4-20/)

### OpenAI Privacy Filter (April 28, 2026)
OpenAI open-sourced Privacy Filter — a 1.5B-parameter PII detection and redaction model (50M active parameters, sparse MoE) under Apache 2.0. Detects 8 categories of sensitive information; designed for on-premises data sanitization pipelines.

**Source:** [MarkTechPost](https://www.marktechpost.com/2026/04/28/openai-releases-privacy-filter-a-1-5b-parameter-open-source-pii-redaction-model-with-50m-active-parameters/)

---

## Architecture & Pattern Notes

### The Convergence on MoE-Hybrid Designs

By April 2026, every major frontier model and most serious open-weight releases use Mixture-of-Experts — but the architectural differentiation has shifted to *what the experts are combined with*:

| Hybrid Type | Example Models | Active Param Efficiency |
|---|---|---|
| MoE + Mamba/SSM | Nemotron 3 Nano Omni, Jamba-1.5 | Very high (linear-complexity sequences) |
| MoE + Hybrid Attention (linear + full) | Qwen3.6-27B (Gated DeltaNet), MiMo-V2.5-Pro | High |
| MoE + Multi-Head Latent Attention (MLA) | DeepSeek V4 Pro | High (KV cache compression) |
| Dense (no MoE) | Qwen3.6-27B | Standard |

**Why this matters:** The efficiency frontier has diverged from raw parameter counts. Laguna XS.2 (3B active) achieves 68.2% SWE-bench; Qwen3.6-27B (27B, dense) hits 77.2%. Active parameter count is now a better predictor of inference cost than total parameters, and the ratio of total:active continues to grow (Grok 4.20's ~3T total with ~40-100B estimated active is an extreme example).

### Thinking Preservation — A New Architecture Pattern for Agentic Systems

Qwen3.6-27B's "Thinking Preservation" flag is a practical solution to a specific agentic efficiency problem: LLMs re-derive reasoning across multi-turn tool calls because chain-of-thought isn't carried in visible history. By retaining earlier reasoning blocks, the model avoids redundant intermediate computation across agent steps. Expect this pattern to spread to other frontier models in H2 2026.

### Test-Time Compute Maturation

As of April 2026, adaptive test-time compute allocation is a key differentiator — not just whether a model *can* think, but how efficiently it allocates thinking compute to problem difficulty. Recent research (arXiv:2604.14853) shows adaptive allocation achieves up to **12.8% relative accuracy improvement** over uniform extended thinking with the same compute budget. Claude Opus 4.7's new `xhigh` effort level is a product manifestation of this: finer-grained control over where compute is spent without always running at `max`.

---

## Pricing Snapshot — Current Flagship Models (April 29, 2026)

```json
{
  "as_of": "2026-04-29",
  "pricing_per_million_tokens": [
    {"model": "Claude Opus 4.7", "org": "Anthropic", "input": 5.00, "output": 25.00},
    {"model": "Claude Sonnet 4.6", "org": "Anthropic", "input": 3.00, "output": 15.00},
    {"model": "Gemini 3.1 Pro", "org": "Google", "input": 2.00, "output": "n/a (comparable to predecessor)"},
    {"model": "Grok 4.20", "org": "xAI", "input": 2.00, "output": 6.00},
    {"model": "MiMo-V2.5-Pro", "org": "Xiaomi", "input": 1.00, "output": 3.00},
    {"model": "MiniMax M2.5 Standard", "org": "MiniMax", "input": 0.15, "output": 1.20},
    {"model": "MiniMax M2.5 Lightning", "org": "MiniMax", "input": 0.30, "output": 2.40},
    {"model": "DeepSeek V4 Pro", "org": "DeepSeek", "input": 1.74, "output": "~7.00 (estimated)"},
    {"model": "Laguna XS.2", "org": "Poolside", "input": "Open-weight / free API preview", "output": "—"},
    {"model": "Qwen3.6-27B", "org": "Alibaba", "input": "Open-weight (Apache 2.0)", "output": "—"}
  ],
  "note": "MiniMax M2.5 Standard represents ~$1/hour of continuous operation at 50 tokens/sec — approximately 13× cheaper than Claude Opus for equivalent task complexity where it competes"
}
```

---

## Analysis & Impact

### 1. The Open-Weight Frontier Is Closing the Proprietary Gap Faster Than Expected

The gap between the best open-weight model and the best proprietary model on SWE-bench Verified is now **~6.3 pp** (MiniMax M2.5 at 80.2% vs. Claude Opus 4.7 at 87.6% — or **13.7 pp** vs. Mythos Preview at 93.9% in restricted access). A year ago, this gap was 20–30 pp. The releases of Laguna XS.2, Qwen3.6-27B, and GLM-5.1 this month alone demonstrate that open-weight models in the 27–230B parameter range are now credible alternatives for production agentic coding deployments.

### 2. Anthropic's Strategic Safety-Capability Tradeoff Is a First

Deliberately reducing a model's cybersecurity capabilities — and publishing a 232-page system card explaining why — is unprecedented from a major lab. Anthropic's Cyber Verification Program (giving security researchers access to higher-capability tiers) attempts to preserve legitimate professional use while restricting general availability of cyber-offensive capabilities. This will likely influence how other labs structure capability releases for dual-use domains.

### 3. Architecture Efficiency Is the New Benchmark Race

The most interesting competition in April 2026 isn't top-line Elo score — it's the active-parameter efficiency race. Laguna XS.2 (3B active) at 68.2% SWE-bench, Qwen3.6-35B-A3B (3B active) at 73.4%, and Nemotron 3 Nano Omni (3B active) across multimodal tasks all demonstrate that careful MoE design + high-quality training data can stretch 3B active parameters very far. The implication: inference costs for frontier-quality coding tasks are about to drop significantly.

### 4. Meta's Closed-Weights Pivot Is the Year's Biggest Strategic Surprise

Meta launching Muse Spark as a closed model (with only a private API preview for partners) and as a product of "Meta Superintelligence Labs" marks a significant departure from the Llama open-weights strategy. Whether Muse Spark's performance (LMArena #5 at ~1494 Elo) justifies the strategy vs. open-weight goodwill is an open debate — but it signals Meta believes top-tier reasoning models require closed development.

### 5. ARC-AGI-2's Grand Prize Threshold Has Been Crossed

GPT-5.5 reaching 85% on ARC-AGI-2 (first to surpass the Grand Prize threshold) means abstract reasoning at human-average level is now within reach for top frontier models. However, only 10 models have been evaluated — the benchmark remains an elite differentiator, not a commodity. ARC Prize 2026's competition pool ($700K, $150K bonus for first eligible solution) will likely draw many more submissions in Q2.

---

## Key Takeaways TL;DR

- **Claude Opus 4.7** (April 16): 87.6% SWE-bench Verified, new `xhigh` thinking mode, intentionally reduced cyber capabilities with new Cyber Verification Program; pricing unchanged ($5/$25 per M)
- **Poolside Laguna XS.2** (April 28): Open-weight, Apache 2.0, 3B active parameters, 68.2% SWE-bench Verified; most efficient open model per active compute on coding
- **IBM Granite 4.1** (April 29 — today): 3B/8B/30B family, 512K context, 15T token training, Apache 2.0; 8B model matches prior 32B MoE
- **Nvidia Nemotron 3 Nano Omni** (April 28): 30B-A3B Mamba-MoE, processes text/image/video/audio, 9× throughput vs. Qwen3-Omni, 47.4% OSWorld
- **Qwen3.6-27B** (April 22): Dense 27B beats Alibaba's own 397B MoE on coding (77.2% SWE-bench Verified); introduces "Thinking Preservation" for multi-turn agentic efficiency
- **MiMo-V2.5-Pro** (April 27): 1.02T-A42B Xiaomi model at $1/M input, matches Opus 4.6 on SWE-bench Pro at 5× lower price
- **LMArena top 4** remain Anthropic models (Opus 4.7/4.6 × Thinking/Standard); Meta Muse Spark and Gemini 3.1 Pro round out top 6
- **ARC-AGI-2**: GPT-5.5 first to hit the 85% Grand Prize threshold; Gemini 3.1 Pro at 77.1% (2× its predecessor)
- **Architecture trend**: Mamba-MoE, hybrid linear/full-attention MoE, and Thinking Preservation are the structural patterns of the month
- **Open-weight gap**: ~6 pp to best proprietary GA model; 14 pp to best restricted model (Mythos) — fastest closing rate in benchmark history

---

## Sources

| Source | URL |
|--------|-----|
| Anthropic Claude Opus 4.7 announcement | https://www.anthropic.com/news/claude-opus-4-7 |
| Claude Opus 4.7 system card (allthings.how) | https://allthings.how/claude-opus-4-7-system-card-key-findings-and-benchmarks/ |
| Vellum Opus 4.7 benchmarks | https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained |
| LLM Stats launch analysis | https://llm-stats.com/blog/research/claude-opus-4-7-launch |
| Poolside Laguna announcement (MarkTechPost) | https://www.marktechpost.com/2026/04/28/poolside-ai-introduces-laguna-xs-2-and-m-1-agentic-coding-models-reaching-68-2-and-72-5-on-swe-bench-verified/ |
| Poolside blog deep dive | https://poolside.ai/blog/laguna-a-deeper-dive |
| HuggingFace Laguna XS.2 | https://huggingface.co/poolside/Laguna-XS.2 |
| IBM Granite 4.1 Research Blog | https://research.ibm.com/blog/granite-4-1-ai-foundation-models |
| NVIDIA Nemotron 3 Nano Omni Tech Blog | https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/ |
| arXiv Nemotron paper 2604.24954 | https://arxiv.org/html/2604.24954 |
| Qwen3.6-27B MarkTechPost | https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/ |
| Qwen3.6 GitHub | https://github.com/QwenLM/Qwen3.6 |
| LMArena 2026 overview | https://www.promptt.dev/blog/lmsys-chatbot-arena-leaderboard-2026 |
| BenchLM SWE-bench tracker | https://benchlm.ai/benchmarks/sweVerified |
| BenchLM ARC-AGI-2 tracker | https://benchlm.ai/benchmarks/arcAgi2 |
| ARC Prize 2026 competition | https://arcprize.org/competitions/2026/arc-agi-2 |
| Meta Muse Spark blog | https://ai.meta.com/blog/introducing-muse-spark-1-msl/ |
| GLM-5.1 review (BuildFastWithAI) | https://buildfastwithai.com/blogs/glm-5-1-open-source-review-2026 |
| GLM-5.1 SWE-bench Pro #1 (NYU Shanghai) | https://rits.shanghai.nyu.edu/ai/glm-5-1-z-ais-open-weight-model-takes-1-on-swe-bench-pro/ |
| Xiaomi MiMo-V2.5-Pro (BuildFastWithAI) | https://www.buildfastwithai.com/blogs/xiaomi-mimo-v2-5-pro-review-2026 |
| Grok 4.20 model card (benchable.ai) | https://benchable.ai/models/x-ai/grok-4.20 |
| Gemini 3.1 Pro (Google DeepMind) | https://deepmind.google/models/gemini/pro/ |
| Adaptive TTC arXiv 2604.14853 | https://arxiv.org/abs/2604.14853 |
| Frontier model architectures 2026 (largo.dev) | https://largo.dev/articles/frontier-llm-architectures-2026/ |
| OpenAI Privacy Filter (MarkTechPost) | https://www.marktechpost.com/2026/04/28/openai-releases-privacy-filter-a-1-5b-parameter-open-source-pii-redaction-model-with-50m-active-parameters/ |
