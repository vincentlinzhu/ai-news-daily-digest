# ML Research — 2026-05-07

*Daily digest: new papers, model releases, training breakthroughs, and conference highlights*

---

## Top Stories

### 1. ICLR 2026 Outstanding Papers: Transformers Proven Succinct + Multi-Turn LLM Crisis Documented

ICLR 2026 (held April 22–26 in Singapore) awarded two **Outstanding Papers**, both with direct implications for how the field thinks about LLM capabilities and limits.

**"Transformers are Inherently Succinct"** (Bergsträßer, Cotterell, Lin — RPTU Kaiserslautern-Landau / ETH Zürich) presented the first formal proof that transformers encode formal languages *substantially more succinctly* than RNNs, finite automata, or Linear Temporal Logic (LTL) formulas. The paper introduces *succinctness* as a new expressivity metric — measuring the minimum transformer size needed to recognize a language — as a sharper lens than the classic "which languages can transformers recognize?" framing. A key corollary: verifying properties of transformers is provably **EXPSPACE-complete**, establishing that model verification is intractable even in principle. This is the theoretical counterpart to empirical scaling work; it says transformers are efficient *representers* as a fundamental result, not just by observation.

**"LLMs Get Lost in Multi-Turn Conversation"** (Laban, Hayashi, Zhou, Neville — Salesforce AI Research) analyzed 200,000+ simulated multi-turn conversations and documented a **39% average performance drop** versus single-turn baselines across six generation tasks. The mechanism: LLMs make early assumptions, generate premature partial solutions, then anchor on those wrong commitments rather than recovering when given corrective follow-up. Two components: minor aptitude loss + large *unreliability* increase. The paper's scalable evaluation method (no human annotation required) is its methodological contribution. Practical consequence: multi-turn degradation accounts for ~31% of enterprise AI agent pilot failures.

**Honorable Mention — "The Polar Express"** (Amsel, Persson, Musco, Gower — NYU/Waterloo) derives optimal polynomial approximations for the matrix sign function using a minimax strategy, then applies these as a drop-in subroutine to the **Muon optimizer**. On GPT-2 pretraining over FineWeb, Polar Express consistently improves validation loss across all tested learning rates, outperforming prior alternatives. Convergence is proven optimal in worst-case error at every iteration, and the method runs entirely in bfloat16 — no numerical precision compromises.

> **Sources:** [ICLR 2026 Awards](https://iclr.cc/virtual/2026/awards_detail) | [Outstanding Papers Blog](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/) | [Transformers are Inherently Succinct (arXiv:2510.19315)](https://arxiv.org/abs/2510.19315) | [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ) | [Polar Express (arXiv:2505.16932)](https://www.arxiv.org/pdf/2505.16932)

---

### 2. Google Gemma 4 MTP Drafters: 3× Inference Speedup, Zero Quality Loss (Released May 5)

Google DeepMind released **Multi-Token Prediction (MTP) drafter models** for the entire Gemma 4 family on May 5, 2026 — the most significant inference acceleration release since speculative decoding went mainstream. The drafters pair lightweight 4-layer models with the full Gemma 4 target to propose multiple future tokens in parallel, which the target verifies in a single forward pass.

**Measured results on DGX Spark (GB10 Blackwell, FP8-quantized Gemma 4 26B-A4B-it):**
- Single-stream: **108.78 tok/s** (vs. 40.85 baseline — **2.66× speedup**)
- Aggregate at concurrency=8: **674.28 tok/s** (~84 tok/s per request)

The Ars Technica headline figure of "up to 3×" is verified in controlled settings. Architecture details:
- Drafter shares the KV cache with the target model (no redundant computation)
- The 26B MoE variant uses ~E2B-scale drafters (~74M parameters)
- Critical deployment note: drafters must pair with `-it` (instruction-tuned) targets; using base-model targets caused **38% performance degradation** in ablations
- MTP uses the `FROZEN_KV_MTP` scheduling algorithm (implemented in SGLang 2.3+)

All four Gemma 4 sizes (E2B, E4B, 26B-A4B MoE, 31B Dense) have matched drafters. The 31B Dense ranks #3 on Arena AI leaderboard, with MMLU Pro 85.2%, AIME 2026 89.2%, LiveCodeBench v6 80.0%. Apache 2.0 license.

> **Sources:** [Google MTP Blog](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) | [Gemma 4 Overview](https://deepmind.google/models/gemma/gemma-4/) | [Ars Technica](https://arstechnica.com/ai/2026/05/googles-gemma-4-open-ai-models-use-speculative-decoding-to-get-up-to-3x-faster/) | [SGLang PR #24436](https://github.com/sgl-project/sglang/pull/24436) | [DGX Spark benchmark](https://ai-muninn.com/en/blog/dgx-spark-gemma4-mtp-108-toks)

---

### 3. MLPerf Training v6.0: DeepSeek-V3 MoE Becomes Standard Industry Pretraining Benchmark

MLCommons released **MLPerf Training v6.0** in May 2026, adding a first-of-its-kind large-scale MoE pretraining workload based on **DeepSeek-V3** (671B total / 37B active parameters). This is a landmark shift: prior MLPerf training benchmarks used dense models (BERT, ResNet, GPT-3); v6.0 is the first to canonize MoE pretraining, signaling that sparse compute is now production-grade enough to benchmark.

Key benchmark specs:
- **Dataset:** C4 (Llama-3 tokenizer, 128k vocab, 4,096 token sequences)
- **Batch size:** ≥15,360 (production-scale MoE training)
- **Architecture features tested:** Multi-head Latent Attention (MLA), auxiliary-loss-free load balancing, fine-grained expert segmentation (160 routed + shared experts), 2-token MTP objective
- **Warm-start design:** Pre-fine-tuned checkpoint ensures ≥98% of benchmark run occurs in a balanced expert state — measuring steady-state MoE performance, not cold-start token imbalance

The DeepSeek-V3 benchmark reflects the engineering reality: production-scale MoE training with load-imbalance-resistant routing, compressed attention, and multi-token prediction is now the *standard workload* for hardware vendors to target.

> **Source:** [MLCommons v6.0 Announcement](https://mlcommons.org/2026/05/deepseek-v3-training-v6-0/)

---

### 4. SPIRAL (ICLR 2026): Self-Play RL on Zero-Sum Games Transfers to Reasoning — No Supervision Required

**SPIRAL** (Self-Play Incentivizes Reasoning via multi-Agent multi-turn RL) introduces a fully online, self-play framework that trains LLMs to reason by competing against increasingly strong versions of themselves on zero-sum games — **without any human-labeled reasoning data**.

Key contributions:
- **Role-conditioned advantage estimation (RAE):** New stabilization technique for multi-agent RL where agent roles alternate (attacker/defender) — prevents the credit-assignment collapse that plagues symmetric self-play
- **Multi-game curriculum:** TicTacToe → Kuhn Poker → Simple Negotiation in combination yields the best transfer; each game develops distinct cognitive patterns (sequential logic, probabilistic reasoning, strategic deception respectively) that are complementary
- **Performance:** Up to **+10% across 8 reasoning benchmarks** on 4 model families (Qwen-7B, Qwen-14B, Llama-8B, Llama-70B) — outperforming SFT on 25,000 expert game trajectories
- **Generalizes to already-trained reasoners:** DeepSeek-R1-Distill-Qwen-7B (already post-trained with RL) still improves further with SPIRAL — suggesting self-play provides a signal orthogonal to RLHF/RLAIF

The mechanism is interpretable: chain-of-thought traces from multi-game SPIRAL show that models develop distinct cognitive *subroutines* per game that transfer to different reasoning task types.

> **Sources:** [arXiv:2506.24119](https://arxiv.org/pdf/2506.24119) | [ICLR Poster](https://iclr.cc/virtual/2026/poster/10011289) | [GitHub spiral-rl/spiral](https://github.com/spiral-rl/spiral)

---

### 5. Open-Weight Model Wave: Tencent Hy3 (295B MoE), Xiaomi MiMo-V2.5-Pro (1T MoE), SenseNova U1

Three major Chinese lab open-weight releases in the past two weeks are collectively reshaping the open-source frontier:

**Tencent Hy3 Preview** (released Apr 23): 295B total / 21B active (top-8 of 192 experts), 256K context, 80 transformer layers + 1 MTP layer (3.8B params). SWE-bench Verified 74.4%, Terminal-Bench 2.0 54.4%. Notable: built in <3 months from Tencent's February infrastructure rebuild. Available on HuggingFace/ModelScope, BF16, 1.2 yuan/M input.

**Xiaomi MiMo-V2.5-Pro** (released Apr 22): 1.02T total / ~42B active. Hybrid SWA+GA attention (6:1 ratio, 128-token window for ~7× KV-cache reduction). 70 layers, 3 MTP modules (3× output speed). SWE-bench Pro 57.2%, Claw-Eval 63.8%, τ³-Bench 72.9%. Trained in 5 stages through RL/MOPD with progressive context extension to 1M tokens.

**SenseNova U1** (SenseTime, Apr 17 / updated May 4): NEO-Unify architecture eliminates both the Visual Encoder and VAE — the first production multimodal model to model language and vision end-to-end in a native unified token space using Mixture-of-Tokens (MoTs). Available as 8B dense and ~3B-active MoE. Open-source state-of-the-art on combined understanding + generation. Apache 2.0.

---

## Deep Dive: The Muon Optimizer Ecosystem Matures

The Muon optimizer (orthogonalized gradient updates for hidden layers) is rapidly becoming the standard training algorithm for LLM pretraining, with a growing ecosystem of theoretical and practical improvements:

**Newton-Muon (arXiv:2604.01472):** Re-derives Muon as a Newton-type method, incorporating previously ignored right preconditioning from input second moments. Result: 6% fewer iterations, ~4% wall-clock time reduction on GPT-2 pretraining. Theoretical grounding matters because it suggests principled hyperparameter choices rather than grid-search defaults.

**Polar Express (ICLR 2026 Honorable Mention, arXiv:2505.16932):** The matrix sign function computation inside Muon's orthogonalization step is now provably optimal. Prior implementations used heuristic Newton-Schulz iterations; Polar Express solves a minimax optimization to find the optimal polynomial at each step. Practically: better convergence at identical compute cost, stable in bfloat16.

**ARO (arXiv:2602.09006):** Independent work treating gradient rotation as first-class. Consistently outperforms AdamW by 1.3–1.35× and Muon-family methods by 1.1–1.15× in LLM pretraining through 8B parameters, with no diminishing returns observed.

**NorMuon (arXiv:2510.05491):** Combines orthogonalization with adaptive learning rates. +21.74% efficiency versus Adam, +11.31% versus standard Muon.

**FlashOptim (arXiv:2602.23349):** Memory-focused — cuts AdamW per-parameter cost from 16 bytes to 7 bytes (>50% reduction) via improved master weight splitting and 8-bit state quantization. Validates on Llama-3.1-8B fine-tuning with no quality regression.

**DeMo:** Reduces per-step inter-node communication by **up to 85×** vs. AdamW-DDP via top-k sparsification of momentum updates in transformed space — the most significant distributed training communication reduction in years.

The convergence: Muon is theoretically sound (Newton-Muon), computationally optimal in its subroutines (Polar Express), memory efficient (FlashOptim), and distributed-friendly (DeMo). The 2025 AdamW dominance may be ending.

> **Sources:** [Newton-Muon](https://arxiv.org/abs/2604.01472) | [ARO](https://arxiv.org/abs/2602.09006v1) | [NorMuon](https://arxiv.org/abs/2510.05491) | [FlashOptim](https://arxiv.org/abs/2602.23349v1) | [Muon is Scalable (arXiv:2502.16982)](http://arxiv.org/abs/2502.16982v1)

---

## Benchmark / Data

```json
{
  "benchmarks": {
    "gemma_4_mtp_speedup": {
      "model": "Gemma 4 26B-A4B-it (FP8, DGX Spark GB10)",
      "single_stream_baseline_tok_s": 40.85,
      "single_stream_mtp_tok_s": 108.78,
      "speedup_single_stream": "2.66x",
      "aggregate_concurrency8_tok_s": 674.28,
      "max_claimed_speedup": "3x",
      "source": "https://ai-muninn.com/en/blog/dgx-spark-gemma4-mtp-108-toks"
    },
    "gemma_4_31b_dense": {
      "mmlu_pro": 85.2,
      "aime_2026": 89.2,
      "livecodebench_v6": 80.0,
      "arena_rank": 3,
      "source": "https://tpsreport.news/news/google-gemma-4-31b-mtp-assistant-release"
    },
    "deepseek_v4_pro": {
      "total_parameters_T": 1.6,
      "active_parameters_B": 49,
      "context_length_K": 1000,
      "pretrain_tokens_T": 33,
      "swe_bench_verified": 80.6,
      "price_input_per_M": 0.435,
      "price_output_per_M": 0.87,
      "coding_percentile": 94,
      "source": "https://benchable.ai/models/deepseek/deepseek-v4-pro-20260423"
    },
    "tencent_hy3_preview": {
      "total_parameters_B": 295,
      "active_parameters_B": 21,
      "num_experts": 192,
      "top_k": 8,
      "context_length_K": 256,
      "swe_bench_verified": 74.4,
      "terminal_bench_2": 54.4,
      "source": "https://hy3ai.com/"
    },
    "xiaomi_mimo_v2_5_pro": {
      "total_parameters_T": 1.02,
      "active_parameters_B": 42,
      "context_length_K": 1000,
      "swe_bench_pro": 57.2,
      "claw_eval": 63.8,
      "tau3_bench": 72.9,
      "source": "https://mimo.xiaomi.com/mimo-v2-5-pro"
    },
    "spiral_self_play": {
      "reasoning_benchmark_improvement_pct": 10,
      "benchmarks_evaluated": 8,
      "model_families": ["Qwen-7B", "Qwen-14B", "Llama-8B", "Llama-70B"],
      "training_games": ["TicTacToe", "Kuhn Poker", "Simple Negotiation"],
      "vs_sft_25k_expert_trajectories": "outperforms",
      "source": "https://iclr.cc/virtual/2026/poster/10011289"
    },
    "muon_optimizer_gains": {
      "newton_muon_iteration_reduction_pct": 6,
      "newton_muon_wall_clock_reduction_pct": 4,
      "aro_vs_adamw_speedup": "1.30-1.35x",
      "aro_vs_muon_speedup": "1.10-1.15x",
      "normuon_vs_adam_efficiency_pct": 21.74,
      "flashoptim_memory_bytes_per_param": 7,
      "demo_communication_reduction": "85x",
      "source": "https://arxiv.org/abs/2604.01472"
    },
    "multi_turn_llm_degradation": {
      "avg_performance_drop_pct": 39,
      "task_count": 6,
      "conversations_analyzed": 200000,
      "enterprise_pilot_failure_pct": 31,
      "source": "https://iclr.cc/virtual/2026/poster/10009146"
    }
  }
}
```

---

## Architecture / Pattern Notes

### MoE Convergence on 192-Expert, ~20B-Active Designs

The cluster of open-weight releases this week reveals a converging MoE recipe: **~200 routed experts, top-8 selection, ~20-50B active parameters, hybrid sparse/full attention, MTP heads.** Tencent Hy3 (192 experts, 21B active), DeepSeek V4 Pro (160+ experts, 49B active), and Xiaomi MiMo-V2.5-Pro (hybrid SWA+GA) all independently land on similar expert counts. The 6:1 SWA/GA ratio used by MiMo (128-token SWA window) deserves specific attention: it achieves ~7× KV-cache reduction by using full attention only every 7th layer, demonstrating that near-full context recall requires far fewer global attention layers than previously assumed.

### NEO-Unify: The First Production Encoder-Free Multimodal Architecture

SenseNova U1's NEO-Unify removes both the visual encoder (ViT-style) and VAE from multimodal pipelines entirely. Prior work assumed visual encoders were necessary for alignment between vision and language tokens. NEO-Unify's native Mixture-of-Tokens (MoTs) operates in a unified token space from the first layer. At 8B parameters, achieving open-source SOTA on both understanding *and* generation simultaneously is the validation this architecture needed. Expect encoder-free designs to dominate the multimodal research agenda at ICML/NeurIPS 2026.

### MTP as Universal Inference Acceleration

Multi-Token Prediction is now shipping not just as a training objective (DeepSeek V3/V4, MiMo-V2.5-Pro) but as **paired inference-time drafter models** (Gemma 4 MTP, May 5). This represents a paradigm shift: MTP heads trained during pretraining become the speculative decoding drafters at inference, eliminating the cost of training a separate draft model. The deployment constraint (drafters must pair with `-it` fine-tuned targets) is important: base models have diverged enough from instruct fine-tuning that the acceptance rate collapses. This is a new failure mode to watch for in production deployments.

### Horizon Length as Training Bottleneck (ICML 2026)

The ICML 2026 accepted paper "On Training LLMs for Long-Horizon Tasks" (arXiv:2605.02572) provides an empirical characterization: increasing horizon length introduces *exponentially harder* exploration and credit-assignment challenges. The key finding is that **horizon reduction during early training** can stabilize optimization and generalize across horizon lengths — suggesting that curriculum scheduling of horizon length (not just task difficulty) should be standard practice. This complements the SPIRAL result: self-play games provide naturally short-horizon learning signals that transfer to long-horizon reasoning.

---

## Analysis & Impact

**ICLR 2026 sends two signals simultaneously:** The Transformers Succinct result says "these architectures are theoretically efficient representers" while the Multi-Turn paper says "they catastrophically fail in the most common real-world usage pattern." Both are true. The field is simultaneously proving transformers are powerful and documenting their practical brittleness. This tension will define AI systems research for the next year.

**The Muon ecosystem is approaching production readiness.** With Polar Express providing provably optimal orthogonalization, Newton-Muon providing theoretical grounding, FlashOptim halving memory requirements, and DeMo reducing inter-node communication by 85×, the remaining barrier is adoption infrastructure (framework support, hyperparameter defaults, mixed-precision recipes). DeepSeek already used Muon for V4 Pro training. Expect AdamW to be minority usage in new LLM pretraining runs by Q4 2026.

**MLPerf v6.0 canonizing MoE pretraining is consequential for hardware vendors.** Prior benchmarks rewarded fast dense-matrix compute (GEMM throughput). MoE benchmarks reward all-to-all networking bandwidth, dynamic routing efficiency, and KV-cache memory bandwidth. This will directly influence H200 vs. Blackwell vs. Ascend competition narratives for the next 18 months.

**Open-weight Chinese lab releases are reaching frontier capability parity.** MiMo-V2.5-Pro at SWE-bench Pro 57.2, Hy3 at Verified 74.4, DeepSeek V4 Pro at Verified 80.6 — collectively these form an open-source tier that matches or exceeds closed models from 6 months ago. With all three under Apache 2.0 / MIT, the "closed models provide a moat" thesis is weakening in every benchmark dimension.

**SPIRAL demonstrates the viability of pure self-play for LLM reasoning training.** The fact that models *already trained on reasoning data* improve further with SPIRAL suggests self-play provides signal orthogonal to both RLHF and supervised reasoning traces. The critical engineering insight is RAE (role-conditioned advantage estimation) — without it, multi-agent RL for LLMs was unstable. This opens the door to adversarial self-play at scale as a reasoning booster without human annotation cost.

---

## Key Takeaways TL;DR

1. **ICLR 2026 outstanding papers:** Transformers are theoretically the most succinct encoders of formal structure (provably EXPSPACE to verify); LLMs drop 39% in multi-turn conversations due to early-commitment errors — these are complementary "powerful but brittle" findings.

2. **Gemma 4 MTP drafters (May 5):** 2.66–3× inference speedup with zero quality loss; requires `-it` targets; establishes MTP-as-speculative-decoding as production standard.

3. **MLPerf v6.0 adds DeepSeek-V3 MoE pretraining benchmark** — first sparse-compute benchmark, signaling the industry-wide shift to MoE as the default LLM architecture.

4. **SPIRAL:** Self-play on TicTacToe/Poker/Negotiation yields +10% on 8 reasoning benchmarks with *no human supervision* — role-conditioned advantage estimation (RAE) is the key stabilizer.

5. **Muon optimizer ecosystem matures:** Newton-Muon + Polar Express + FlashOptim + DeMo collectively make Muon production-ready across memory, communication, and convergence dimensions.

6. **Open-weight frontier:** Tencent Hy3 (295B MoE), Xiaomi MiMo-V2.5-Pro (1T MoE), SenseNova U1 (encoder-free multimodal) — all Apache 2.0/MIT, collectively matching closed-model benchmarks from late 2025.

7. **Horizon length is a training variable:** ICML 2026 empirically proves that curriculum scheduling of horizon length (not just task difficulty) is necessary for long-horizon LLM training — curriculum RL on composed problems achieves 2–2.65× benchmark improvement.

---

## Sources

| Story | URL |
|---|---|
| ICLR 2026 Awards | https://iclr.cc/virtual/2026/awards_detail |
| ICLR 2026 Outstanding Papers Blog | https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/ |
| "Transformers are Inherently Succinct" (arXiv) | https://arxiv.org/abs/2510.19315 |
| "LLMs Get Lost in Multi-Turn Conversation" (ICLR) | https://iclr.cc/virtual/2026/poster/10009146 |
| "The Polar Express" (ICLR Honorable Mention) | https://arxiv.org/pdf/2505.16932 |
| Gemma 4 MTP Blog | https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/ |
| Gemma 4 DeepMind Page | https://deepmind.google/models/gemma/gemma-4/ |
| Gemma 4 Ars Technica | https://arstechnica.com/ai/2026/05/googles-gemma-4-open-ai-models-use-speculative-decoding-to-get-up-to-3x-faster/ |
| Gemma 4 DGX Spark Benchmark | https://ai-muninn.com/en/blog/dgx-spark-gemma4-mtp-108-toks |
| MLPerf Training v6.0 | https://mlcommons.org/2026/05/deepseek-v3-training-v6-0/ |
| SPIRAL (arXiv:2506.24119) | https://arxiv.org/pdf/2506.24119 |
| SPIRAL ICLR Poster | https://iclr.cc/virtual/2026/poster/10011289 |
| SPIRAL GitHub | https://github.com/spiral-rl/spiral |
| Tencent Hy3 Preview | https://hy3ai.com/ |
| Hy3 HuggingFace Blog | https://huggingface.co/blog/imnotkitty/hy3-preview |
| Xiaomi MiMo-V2.5-Pro | https://mimo.xiaomi.com/mimo-v2-5-pro |
| SenseNova U1 GitHub | https://github.com/OpenSenseNova/SenseNova-U1/ |
| SenseTime Press Release | https://www.sensetime.com/en/news-detail/51170629 |
| DeepSeek V4 Pro (Benchable) | https://benchable.ai/models/deepseek/deepseek-v4-pro-20260423 |
| Newton-Muon | https://arxiv.org/abs/2604.01472 |
| ARO Optimizer | https://arxiv.org/abs/2602.09006v1 |
| NorMuon | https://arxiv.org/abs/2510.05491 |
| Muon is Scalable | https://arxiv.org/abs/2502.16982v1 |
| FlashOptim | https://arxiv.org/abs/2602.23349v1 |
| Value Gradient Flow (VGF) | https://arxiv.org/abs/2604.14265 |
| ICML 2026 Highlights | https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/ |
| Long-Horizon Tasks (arXiv:2605.02572) | https://arxiv.org/abs/2605.02572 |
| Scaling RL with Synthetic Data (arXiv:2603.24202) | https://arxiv.org/abs/2603.24202 |
