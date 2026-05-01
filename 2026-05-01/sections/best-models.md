# Best Models & Benchmarks — 2026-05-01

> **Coverage window:** Late April – May 1, 2026. Items already covered in the 2026-04-30 digest (GPT-5.5 ARC-AGI-2 threshold, DeepSeek V4 Pro, Claude Mythos, Kimi K2.6, SWE-bench credibility crisis) are referenced only where there is genuinely new data.

---

## Top Stories

### 1. Claude Opus 4.7 Consolidates Anthropic's Coding Lead (Released April 16)

Anthropic's Claude Opus 4.7 is now the top publicly-available (non-restricted) model on SWE-bench Verified and SWE-bench Pro, edging out GPT-5.5 on code-quality benchmarks while maintaining the same pricing as Opus 4.6.

**Key benchmark jumps vs. Opus 4.6:**

| Benchmark | Opus 4.6 | Opus 4.7 | Delta |
|---|---|---|---|
| SWE-bench Verified | 80.8% | **87.6%** | +6.8 pp |
| SWE-bench Pro | 53.4% | **64.3%** | +10.9 pp |
| Terminal-Bench 2.0 | ~65% | **69.4%** | +~4 pp |
| GPQA Diamond | ~91% | **94.2%** | +~3 pp |
| OSWorld-Verified | 72.7% | **78.0%** | +5.3 pp |
| MCP-Atlas (tool use) | — | **77.3%** | new |

**Architecture / capability notes:**
- Vision resolution increased **3.3×** — up to 2,576px (~3.75 MP), enabling richer diagram/screenshot understanding in agentic loops.
- New `xhigh` effort level for granular reasoning control (join `low` / `medium` / `high`).
- **Self-verification** added: model verifies its own output before reporting, reducing silent failures on multi-step coding tasks.
- **File-system memory** persists context across multi-session agentic jobs — directly relevant to autonomous coding workflows.
- Pricing **unchanged** at $5 / $25 per million input / output tokens.
- Context window: **1M tokens** (same as Opus 4.6).
- Safety tier: **ASL-3** (same tier as Opus 4.6).

**LMSys Arena standing:** Opus 4.7 Thinking reaches ~1505 Elo, slightly ahead of Opus 4.6 Thinking (~1503), with only ~8 Elo separating the top five models — statistically within noise.

**Sources:** [Anthropic Research](https://www.anthropic.com/research/claude-opus-4-7) | [llm-stats.com](https://llm-stats.com/blog/research/claude-opus-4-7-launch) | [Vellum AI benchmarks](https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained)

---

### 2. Qwen3.6-Max-Preview: Alibaba Goes Closed-Weight for Its Flagship

Released April 20, Qwen3.6-Max-Preview is the **first Qwen flagship model shipped as closed-weights only** — a deliberate pivot away from Alibaba's historical open-source posture. It claims the #1 slot on **six** coding and agentic benchmarks simultaneously.

**Key specs:**
- 1 trillion total parameters, MoE architecture
- 256K–262K context window
- Available only via Alibaba Cloud Model Studio / Qwen Studio API
- OpenAI- and Anthropic-compatible endpoints

**Benchmark leadership claims:**

| Benchmark | Score | Rank |
|---|---|---|
| SWE-bench Pro | 57.30 | **#1** |
| Terminal-Bench 2.0 | 65.40 | **#1** |
| SkillsBench | — | **#1** |
| SciCode | — | **#1** |
| QwenClawBench | — | **#1** |
| QwenWebBench | — | **#1** |

**Simultaneous open release:** Qwen3.6-35B-A3B (Apache 2.0, 35B total / 3B active MoE) was released April 16, scoring 73.4% SWE-bench Verified and 92.7% AIME 2026 — competitive with much larger models. Qwen3.6-27B dense (April 22, Apache 2.0) achieves 77.2% SWE-bench Verified and outperforms the older Qwen3.5-397B on agentic coding tasks.

**Significance:** Alibaba is following Meta/OpenAI's playbook — maintain open-source community goodwill with smaller models while locking frontier capability behind an API. The closed-weights shift signals monetization pressure even among historically open labs.

**Sources:** [TokenMix Blog](https://tokenmix.ai/blog/qwen3-6-max-preview-benchmark-review-2026) | [MarkTechPost Qwen3.6-27B](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/) | [DataLearner](https://www.datalearner.com/en/ai-models/pretrained-models/qwen3-6-max-preview)

---

### 3. Mistral Medium 3.5 (128B): One-Model Unification Strategy

Released April 29 — just two days ago — Mistral's flagship Mistral Medium 3.5 is a **128B dense model** replacing three separate prior products (Medium 3.1, Magistral, and Devstral 2) with a single unified checkpoint. It achieves **77.6% on SWE-bench Verified**, ranking it among the top open-accessible coding models.

**Key specs:**
- 128B parameters, dense architecture (not MoE)
- 256K context window
- Configurable reasoning effort per request
- Multimodal: text + image input
- Native function calling and JSON output
- Modified MIT license for commercial use
- API pricing: **$1.50 / $7.50** per million input / output tokens

**Benchmark snapshot:**

| Benchmark | Score |
|---|---|
| SWE-bench Verified | **77.6%** |
| T3-Telecom | 91.4% |
| vs. Qwen3.6-35B-A3B on BenchLM | 77.6 vs. 66.9 (Mistral leads) |

**Strategic note:** By collapsing three models into one, Mistral simplifies the developer integration story. This mirrors Anthropic's move of merging "thinking" and "non-thinking" modes into a single model. The move is partly defensive — with Qwen and MiniMax pushing competitive open-weight options, Mistral needs a clean flagship story.

**Sources:** [The Decoder](https://the-decoder.com/mistrals-new-flagship-medium-3-5-folds-chat-reasoning-and-code-into-one-model/) | [BenchLM comparison](https://benchlm.ai/compare/mistral-medium-3-5-128b-vs-qwen3-6-35b-a3b) | [Artificial Analysis](https://artificialanalysis.ai/models/mistral-medium-3-5/providers)

---

### 4. ARC-AGI-3 Resets the Goalposts: Best AI Scores 0.37%, Humans Score 100%

ARC Prize released ARC-AGI-3 on March 25 — and the results are a dramatic reset after GPT-5.5 cleared ARC-AGI-2's 85% grand prize threshold (reported yesterday). ARC-AGI-3 shifts from static grid pattern-matching to **interactive, turn-based exploration environments**.

**Top AI scores (as of benchmark launch):**
- Gemini 3.1 Pro: **0.37%**
- GPT-5.4: 0.26%
- Claude Opus 4.6: 0.20%
- Grok 4.20: 0.00%
- **Human baseline: 100%**

**What changed:**
- 135 abstract environments with 150+ handcrafted scenarios and 1,000+ levels
- Agents must infer rules without instructions, determine win conditions, and plan multi-step strategies
- Scoring uses **RHAE (Relative Human Action Efficiency)** — taking 10× more actions than humans yields only 1% score, not 10%, creating an efficiency penalty
- $700K grand prize (of $850K total pool) for matching human performance — deadline November 2, 2026

**Significance:** ARC-AGI-3 suggests that pattern recognition (ARC-AGI-2's core demand) is a solved problem, but open-ended exploration and rule-induction in novel interactive environments remains nearly impossible for current frontier models. The benchmark reframes the "AGI gap" from knowledge recall to **adaptive exploration under uncertainty**.

**Sources:** [ARC Prize](https://arcprize.org/blog/arc-agi-3-human-dataset) | [Revolution in AI](https://www.revolutioninai.com/2026/03/arc-agi-3-benchmark-ai-scores-openai-spud-anthropic-2026.html) | [TokenCost](https://tokencost.app/blog/arc-agi-3-benchmark-cost)

---

### 5. MiniMax M2.7: Self-Evolving Open-Source Agent at One-Third the Cost

MiniMax open-sourced M2.7 in April — a 230B MoE model (10B active) built specifically for agentic professional workflows. At **$0.30 / $1.20** per million input/output tokens, it costs approximately one-third of comparable models (GLM-5 prices at $0.90 / $3.60).

**Key benchmark results:**

| Benchmark | Score |
|---|---|
| SWE-bench Pro | 56.22% |
| Terminal-Bench 2.0 | 57.0% |
| VIBE-Pro (agentic eval) | 55.6% |
| SWE Multilingual | 76.5% |
| Multi-SWE-Bench | 52.7% |
| GDPval-AA Elo | 1494 |
| Hallucination rate | 34% (lowest recorded) |

**Self-evolution:** M2.7 can autonomously improve through iterative optimization cycles — a form of online RLHF without human feedback — and debug production systems in under three minutes via root-cause reasoning.

**Architecture:** 256 local experts, 8 activated per token (4.3% activation rate), 200K context.

**Sources:** [MarkTechPost](https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56-22-on-swe-pro-and-57-0-on-terminal-bench-2/) | [Artificial Analysis](https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know)

---

## Deep Dive: The Two-Tier Open-Weight Landscape

The open-weight model space has bifurcated in April 2026:

**Tier 1 — Competitive Flagship (MoE, >200B total params):**
- DeepSeek V4 Pro (1.6T / 49B active) — #1 LiveCodeBench at 93.5%
- GLM-5 (744B / 40B active) — 77.8% SWE-bench Verified, MIT
- MiniMax M2.7 (230B / 10B active) — $0.30/M input, lowest hallucination

**Tier 2 — Efficient Mid-Size (MoE or dense, 27–128B):**
- Qwen3.6-35B-A3B (35B / 3B active) — 73.4% SWE-bench Verified, Apache 2.0
- Qwen3.6-27B (27B dense) — 77.2% SWE-bench Verified, Apache 2.0
- Mistral Medium 3.5 (128B dense) — 77.6% SWE-bench Verified, Modified MIT

**Key trend:** The T2 tier is closing on T1 on SWE-bench Verified (all scoring 73–78%), suggesting the benchmark may be approaching saturation for this class of models — reinforcing yesterday's SWE-bench Verified contamination findings. SWE-bench Pro (where T1 models score 56–64% and T2 models score ~40–50%) remains the meaningful differentiator.

---

## Benchmark Data Blocks

### SWE-bench Verified — Top 10 as of May 1, 2026

```json
{
  "benchmark": "SWE-bench Verified",
  "date": "2026-05-01",
  "source": "https://benchlm.ai/benchmarks/sweVerified",
  "top_models": [
    {"rank": 1, "model": "Claude Mythos Preview", "org": "Anthropic", "score": 93.9, "access": "restricted"},
    {"rank": 2, "model": "Claude Opus 4.7 (Adaptive)", "org": "Anthropic", "score": 87.6, "access": "API"},
    {"rank": 3, "model": "GPT-5.3 Codex", "org": "OpenAI", "score": 85.0, "access": "API"},
    {"rank": 4, "model": "GPT-5.5", "org": "OpenAI", "score": 83.2, "access": "API"},
    {"rank": 5, "model": "Mistral Medium 3.5", "org": "Mistral AI", "score": 77.6, "access": "API/open"},
    {"rank": 6, "model": "Qwen3.6-27B", "org": "Alibaba", "score": 77.2, "access": "open-weight"},
    {"rank": 7, "model": "GLM-5", "org": "Zhipu AI", "score": 77.8, "access": "open-weight"},
    {"rank": 8, "model": "Qwen3.6-35B-A3B", "org": "Alibaba", "score": 73.4, "access": "open-weight"},
    {"rank": 9, "model": "MiniMax M2.7", "org": "MiniMax", "score": 71.0, "access": "open-weight"},
    {"rank": 10, "model": "Gemini 3.1 Pro", "org": "Google", "score": 68.5, "access": "API"}
  ],
  "note": "Scores for non-top-3 positions are approximate from multiple sources; benchmark showing contamination per 2026-04-30 report."
}
```

### SWE-bench Pro — Top 6 as of May 1, 2026

```json
{
  "benchmark": "SWE-bench Pro",
  "date": "2026-05-01",
  "source": "https://benchlm.ai/benchmarks/swePro",
  "top_models": [
    {"rank": 1, "model": "Claude Mythos Preview", "org": "Anthropic", "score": 77.8, "access": "restricted"},
    {"rank": 2, "model": "Claude Opus 4.7 (Adaptive)", "org": "Anthropic", "score": 64.3, "access": "API"},
    {"rank": 3, "model": "GPT-5.5", "org": "OpenAI", "score": 58.6, "access": "API"},
    {"rank": 4, "model": "Qwen3.6-Max-Preview", "org": "Alibaba", "score": 57.3, "access": "API-only"},
    {"rank": 5, "model": "MiniMax M2.7", "org": "MiniMax", "score": 56.22, "access": "open-weight"},
    {"rank": 6, "model": "Gemini 3.1 Pro", "org": "Google", "score": 54.2, "access": "API"}
  ]
}
```

### Terminal-Bench 2.0 — Top 5 as of May 1, 2026

```json
{
  "benchmark": "Terminal-Bench 2.0",
  "date": "2026-05-01",
  "source": "https://www.tbench.ai/leaderboard/terminal-bench/2.0",
  "top_models": [
    {"rank": 1, "model": "Codex + GPT-5.5", "org": "OpenAI", "score": 82.0, "submitted": "2026-04-23"},
    {"rank": 2, "model": "ForgeCode + GPT-5.4", "org": "OpenAI", "score": 81.8, "submitted": "2026-03-12"},
    {"rank": 3, "model": "TongAgents + Gemini 3.1 Pro", "org": "Google", "score": 80.2, "submitted": "2026-03-13"},
    {"rank": 4, "model": "ForgeCode + Claude Opus 4.6", "org": "Anthropic", "score": 79.8, "submitted": "2026-03-12"},
    {"rank": 5, "model": "SageAgent + GPT-5.3-Codex", "org": "OpenAI", "score": 78.4, "submitted": "2026-03-13"}
  ],
  "note": "Standalone model scores: Claude Opus 4.7 69.4%, Qwen3.6-Max-Preview 65.40%, MiniMax M2.7 57.0%"
}
```

### GPQA Diamond — Top 7 as of May 1, 2026

```json
{
  "benchmark": "GPQA Diamond",
  "date": "2026-05-01",
  "source": "https://benchlm.ai/benchmarks/gpqaDiamond",
  "human_expert_baseline": "~65%",
  "top_models": [
    {"rank": 1, "model": "Claude Mythos Preview", "org": "Anthropic", "score": 94.5},
    {"rank": 2, "model": "Gemini 3.1 Pro", "org": "Google", "score": 94.3},
    {"rank": 3, "model": "Claude Opus 4.7", "org": "Anthropic", "score": 94.2},
    {"rank": 4, "model": "GPT-5.4 Pro", "org": "OpenAI", "score": 92.8},
    {"rank": 5, "model": "Gemini 3.1 Pro Preview", "org": "Google", "score": 92.1},
    {"rank": 6, "model": "GPT-5.4", "org": "OpenAI", "score": 91.1},
    {"rank": 7, "model": "Gemini 3 Pro", "org": "Google", "score": 90.2}
  ],
  "note": "Benchmark approaching saturation — 5 models now above 91%"
}
```

### LiveCodeBench — Top 5 as of April 29, 2026

```json
{
  "benchmark": "LiveCodeBench",
  "date": "2026-04-29",
  "source": "https://benchlm.ai/benchmarks/liveCodeBench",
  "top_models": [
    {"rank": 1, "model": "DeepSeek V4 Pro (Max)", "org": "DeepSeek", "score": 93.5},
    {"rank": 2, "model": "DeepSeek V4 Flash (Max)", "org": "DeepSeek", "score": 91.6},
    {"rank": 3, "model": "DeepSeek V4 Pro (High)", "org": "DeepSeek", "score": 89.8},
    {"rank": 4, "model": "Moonshot AI (Kimi)", "org": "Moonshot AI", "score": 89.6},
    {"rank": 5, "model": "DeepSeek V4 Flash (High)", "org": "DeepSeek", "score": 88.4}
  ],
  "note": "DeepSeek V4 dominates top 5. DeepSeek V4 Pro reported in 2026-04-30 digest; scores unchanged."
}
```

### AIME 2026 — Top 6

```json
{
  "benchmark": "AIME 2026",
  "date": "2026-05",
  "source": "https://benchlm.ai/benchmarks/aime2026",
  "top_models": [
    {"rank": 1, "model": "Kimi 2.6", "org": "Moonshot AI", "score": 96.4},
    {"rank": 2, "model": "GLM-5", "org": "Zhipu AI", "score": 95.8},
    {"rank": 3, "model": "Kimi K2.5", "org": "Moonshot AI", "score": 95.8},
    {"rank": 4, "model": "GLM-5.1", "org": "Zhipu AI", "score": 95.3},
    {"rank": 5, "model": "Qwen3.6 Plus Preview", "org": "Alibaba", "score": 95.3},
    {"rank": 6, "model": "Claude Opus 4.5", "org": "Anthropic", "score": 93.3}
  ],
  "note": "Multiple open and closed models now exceed 90% on this olympiad-math benchmark"
}
```

### ARC-AGI-3 Launch Scores

```json
{
  "benchmark": "ARC-AGI-3",
  "date": "2026-03-25",
  "source": "https://arcprize.org/blog/arc-agi-3-human-dataset",
  "human_baseline": "100%",
  "scoring_metric": "RHAE (Relative Human Action Efficiency)",
  "top_models": [
    {"model": "Gemini 3.1 Pro", "org": "Google", "score": 0.37},
    {"model": "GPT-5.4", "org": "OpenAI", "score": 0.26},
    {"model": "Claude Opus 4.6", "org": "Anthropic", "score": 0.20},
    {"model": "Grok 4.20", "org": "xAI", "score": 0.00}
  ],
  "prize_pool": "$850K",
  "grand_prize": "$700K",
  "deadline": "2026-11-02"
}
```

### GAIA Benchmark — Top 6 as of April 27, 2026

```json
{
  "benchmark": "GAIA",
  "date": "2026-04-27",
  "source": "https://benchlm.ai/benchmarks/gaia",
  "human_baseline": "92%",
  "top_models": [
    {"rank": 1, "model": "Claude Mythos Preview", "org": "Anthropic", "score": 52.3, "access": "restricted"},
    {"rank": 2, "model": "GPT-5.4 Pro", "org": "OpenAI", "score": 50.5},
    {"rank": 3, "model": "GPT-5.4", "org": "OpenAI", "score": 48.2},
    {"rank": 4, "model": "Claude Opus 4.6", "org": "Anthropic", "score": 47.8},
    {"rank": 5, "model": "Gemini 3.1 Pro", "org": "Google", "score": 46.1},
    {"rank": 6, "model": "Claude Sonnet 4.6", "org": "Anthropic", "score": 45.5}
  ]
}
```

### API Pricing Comparison — Frontier Models (May 1, 2026)

```json
{
  "date": "2026-05-01",
  "models": [
    {"model": "GPT-5.5", "org": "OpenAI", "input_per_M": 5.00, "output_per_M": 30.00, "context_k": 1050},
    {"model": "Claude Opus 4.7", "org": "Anthropic", "input_per_M": 5.00, "output_per_M": 25.00, "context_k": 1000},
    {"model": "Gemini 3.1 Pro", "org": "Google", "input_per_M": null, "output_per_M": null, "context_k": null, "note": "pricing not verified in search"},
    {"model": "Grok 4.20", "org": "xAI", "input_per_M": 2.00, "output_per_M": 6.00, "context_k": 2000},
    {"model": "DeepSeek V4 Pro", "org": "DeepSeek", "input_per_M": 1.74, "output_per_M": 3.48, "context_k": 1000},
    {"model": "Qwen3.6-Max-Preview", "org": "Alibaba", "input_per_M": null, "output_per_M": null, "note": "pricing not published in search results"},
    {"model": "Mistral Medium 3.5", "org": "Mistral AI", "input_per_M": 1.50, "output_per_M": 7.50, "context_k": 256},
    {"model": "MiniMax M2.7", "org": "MiniMax", "input_per_M": 0.30, "output_per_M": 1.20, "context_k": 200},
    {"model": "GLM-5", "org": "Zhipu AI", "input_per_M": 0.90, "output_per_M": 3.60, "context_k": 200}
  ]
}
```

---

## Architecture & Pattern Notes

### MoE Dominance at Frontier Scale
Every non-Anthropic frontier model disclosed this cycle uses Mixture-of-Experts:
- **DeepSeek V4 Pro:** 1.6T total / 49B active (3.1% activation rate)
- **Qwen3.6-Max-Preview:** ~1T total, MoE
- **GLM-5:** 744B total / 40B active (5.4% activation rate)
- **MiniMax M2.7:** 230B total / 10B active (4.3% activation rate)
- **Qwen3.6-35B-A3B:** 35B total / 3B active (8.6% activation rate)

Dense exceptions: Mistral Medium 3.5 (128B) and Qwen3.6-27B remain dense. This is deliberate — dense models offer simpler deployment (no expert routing), predictable latency, and better throughput on single-node inference.

### Unified "Think/No-Think" Models Replace Model Families
The week's releases confirm a strong trend: labs are collapsing separate "reasoning" and "non-reasoning" checkpoints into single models with configurable effort levels:
- **Mistral Medium 3.5** replaces Medium 3.1 + Magistral + Devstral 2
- **GLM-5** ships with unified "think" / "non-think" modes via post-training
- **Claude Opus 4.7** adds `xhigh` effort level to the existing effort scale
- **Grok 4.20** exposes reasoning depth through Heavy variant (16 sub-agents)

This simplifies the developer stack — one model, one API endpoint, dial up or down inference compute per request. The tradeoff is higher baseline model weight; these unified models tend to be larger than their specialized predecessors.

### Adaptive Test-Time Compute: From Static to Dynamic Allocation
Recent arxiv research (April 2026, [arXiv:2604.14853](https://arxiv.org/abs/2604.14853)) demonstrates **Constrained Policy Optimization for adaptive test-time compute allocation** — dynamically assigning inference budget per problem rather than uniformly. Results show 12.8% relative accuracy improvement at matched compute budgets. This is the methodological path that will improve benchmark scores on AIME and GPQA without increasing model size.

---

## Analysis & Impact

### GPQA Diamond Is Saturating
Five models now exceed 91% on GPQA Diamond (human experts average 65%). The benchmark has advanced **62.6 percentage points in 23 months**. Within 1–2 major model cycles, GPQA Diamond will likely be retired as a primary differentiator — its questions are becoming part of training data curricula. Labs will need to move to GPQA+ or equivalent expert-validated sets with contamination controls.

### SWE-bench Verified vs. Pro: The Contamination Wedge Grows
The 2026-04-30 digest noted a 35-point gap between SWE-bench Verified and SWE-bench Pro. Today's data reinforces this: top models cluster at 77–88% on Verified but only 54–64% on Pro. Claude Opus 4.7's +6.8pp Verified gain translates to a +10.9pp Pro gain — suggesting that real capability improvement is *magnified* on Pro relative to the saturated Verified subset.

### Alibaba's Closed-Weights Pivot Has Strategic Implications for Open-Source
Qwen3.6-Max-Preview represents the first Chinese frontier model to go explicitly API-only at the flagship tier. This follows Meta's Llama pivot (covered yesterday) and suggests a broader industry shift: **open-weights are being retained at the 27–128B efficient-serving tier, while trillion-parameter MoE flagships are going proprietary**. The developer community receives capable open models; the infrastructure/API margin is protected at the frontier.

### ARC-AGI-3 Is Not "GPT-5.5 Level": The Gap is ~225×
GPT-5.5 cleared ARC-AGI-2 at 85% (reported yesterday). ARC-AGI-3's best result is 0.37%. This is not a regression — it is a fundamentally different capability being measured: exploration under novel rules vs. pattern completion. The benchmark designers are deliberately targeting the next hard wall. Given the ARC-AGI-2 trajectory (from ~10% to 85% in ~12 months), the question is whether the same inference-time scaling that cracked ARC-AGI-2 transfers to ARC-AGI-3's turn-based environments.

### Cost Pressure Is Real: MiniMax M2.7 at $0.30/M
The pricing gradient from frontier ($5–30/M input) to efficient open-weight ($0.30–1.74/M) has widened. MiniMax M2.7 delivers SWE-bench Pro scores (56.2%) competitive with GPT-5.5 (58.6%) at 1/17th the input cost. For production agentic deployments making millions of LLM calls, this is the primary adoption driver — not benchmark rankings.

---

## Key Takeaways (TL;DR)

1. **Claude Opus 4.7** (April 16) is the leading publicly-accessible coding model: 87.6% SWE-bench Verified, 64.3% SWE-bench Pro, 94.2% GPQA Diamond — same price as Opus 4.6.

2. **Alibaba closed the weights** on its flagship Qwen3.6-Max-Preview (1T MoE), claiming 6 benchmark #1s including SWE-bench Pro and Terminal-Bench 2.0 — a strategic pivot mirroring Meta's Llama shift.

3. **Mistral consolidated** three separate models (reasoning + coding + chat) into Mistral Medium 3.5 (128B, $1.50/M input, 77.6% SWE-bench Verified) — simplifying developer adoption.

4. **ARC-AGI-3 resets the bar**: interactive turn-based environments show a 225× gap between the best AI (0.37%) and humans (100%) — open-ended exploration is the next hard wall, not knowledge recall.

5. **MiniMax M2.7** delivers ~56% SWE-bench Pro at $0.30/M input — forcing a cost-capability rethink for production agentic deployments.

6. **GPQA Diamond** is near saturation (5 models above 91%); expect it to lose benchmark prominence within 1–2 model cycles.

7. **MoE + unified think/no-think** is the dominant architecture pattern: every major new release is either MoE with adjustable reasoning effort, or a dense model replacing a multi-variant family.

---

## Sources

| Source | URL |
|---|---|
| Anthropic — Claude Opus 4.7 | https://www.anthropic.com/research/claude-opus-4-7 |
| llm-stats.com — Opus 4.7 benchmarks | https://llm-stats.com/blog/research/claude-opus-4-7-launch |
| Vellum AI — Opus 4.7 benchmarks explained | https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained |
| Anthropic — Claude Opus 4.7 system card | https://allthings.how/claude-opus-4-7-system-card-key-findings-and-benchmarks/ |
| TokenMix — Qwen3.6-Max-Preview review | https://tokenmix.ai/blog/qwen3-6-max-preview-benchmark-review-2026 |
| MarkTechPost — Qwen3.6-27B | https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/ |
| DataLearner — Qwen3.6-Max-Preview | https://www.datalearner.com/en/ai-models/pretrained-models/qwen3-6-max-preview |
| Idlen — Qwen3.6-35B-A3B | https://www.idlen.io/news/alibaba-qwen-36-35b-a3b-moe-open-source-apache-swe-bench-april-2026 |
| The Decoder — Mistral Medium 3.5 | https://the-decoder.com/mistrals-new-flagship-medium-3-5-folds-chat-reasoning-and-code-into-one-model/ |
| BenchLM — Mistral vs. Qwen comparison | https://benchlm.ai/compare/mistral-medium-3-5-128b-vs-qwen3-6-35b-a3b |
| ARC Prize — ARC-AGI-3 human dataset | https://arcprize.org/blog/arc-agi-3-human-dataset |
| ARC Prize — ARC-AGI-3 competition | https://three.arcprize.org/competitions/2026 |
| TokenCost — ARC-AGI-3 benchmark cost | https://tokencost.app/blog/arc-agi-3-benchmark-cost |
| MarkTechPost — MiniMax M2.7 | https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56-22-on-swe-pro-and-57-0-on-terminal-bench-2/ |
| Artificial Analysis — MiniMax M2.7 | https://artificialanalysis.ai/articles/minimax-m2-7-everything-you-need-to-know |
| BenchLM — SWE-bench Verified | https://benchlm.ai/benchmarks/sweVerified |
| BenchLM — SWE-bench Pro | https://benchlm.ai/benchmarks/swePro |
| tbench.ai — Terminal-Bench 2.0 leaderboard | https://www.tbench.ai/leaderboard/terminal-bench/2.0 |
| BenchLM — GPQA Diamond | https://benchlm.ai/benchmarks/gpqaDiamond |
| BenchLM — LiveCodeBench | https://benchlm.ai/benchmarks/liveCodeBench |
| BenchLM — AIME 2026 | https://benchlm.ai/benchmarks/aime2026 |
| BenchLM — GAIA | https://benchlm.ai/benchmarks/gaia |
| LMSys Chatbot Arena — top models | https://smartchunks.com/lmsys-arena-elo-leaderboard-explained-2026/ |
| OpenAI — GPT-5.5 intro | https://openai.com/index/introducing-gpt-5-5/ |
| OpenAI — GPT-5.5 model card | https://developers.openai.com/api/docs/models/gpt-5.5 |
| xAI — Grok 4.20 | https://awesomeagents.ai/models/grok-4-20/ |
| buildfastwithai — GLM-5 | https://www.buildfastwithai.com/blogs/glm-5-released-open-source-model-2026 |
| AgentVsAI — test-time compute scaling | https://www.agentvsai.com/test-time-compute-new-scaling-reasoning-budgets-adaptive-inference/ |
| arXiv:2604.14853 — adaptive TTC allocation | https://arxiv.org/abs/2604.14853 |
| AgentMarketCap — ARC-AGI-3 analysis | https://agentmarketcap.ai/blog/2026/04/06/gaia-benchmark-2026-general-agent-leaderboard-swe-bench-alternative |
