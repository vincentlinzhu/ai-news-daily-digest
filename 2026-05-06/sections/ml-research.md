# ML Research — 2026-05-06

> Daily digest of significant ML research news. Today's coverage spans ICML 2026 acceptance wave fallout, a flurry of fresh arXiv submissions (2605.xxxxx), and two major open-weight model releases that reset the agentic coding benchmark table.

---

## Top Stories

### 1. Kimi K2.6: First Open-Weight Model to Clear 58% on SWE-Bench Pro

Moonshot AI's **Kimi K2.6**, released April 20, 2026, is now the highest-scoring open-weight model on SWE-Bench Pro at **58.6%**, edging past GPT-5.4 (57.7%) — itself a proprietary model. This is a significant milestone: the open-source frontier has caught up to and in this narrow sense surpassed a closed frontier model on the hardest public software-engineering benchmark.

**Architecture:** 1 trillion total parameters, MoE with **32B active** per token (384 experts, top-8 routing). Vision-language capable via a 400M-parameter MoonViT encoder. Context window: 262,144 tokens. Uses MLA attention + SwiGLU.

**Key execution-layer innovations over K2.5:**
- **Automatic context compression** — summarizes long histories to prevent truncation-induced drift during multi-hour runs
- **Native agent swarm orchestration** — up to 300 sub-agents across 4,000 coordinated steps baked into the base model's training objectives
- **Proactive autonomy** — fine-tuned to recognize when it is stuck and replan rather than confabulate

**Benchmark sweep:**

```json
{
  "model": "Kimi K2.6",
  "release_date": "2026-04-20",
  "type": "open-weight MoE",
  "parameters_total": "1T",
  "parameters_active": "32B",
  "context_window": 262144,
  "benchmarks": {
    "SWE_Bench_Pro": 0.586,
    "SWE_Bench_Verified": 0.802,
    "Terminal_Bench_2.0": 0.667,
    "AIME_2026": 0.964,
    "MathVision_with_Python": 0.932
  },
  "license": "modified MIT",
  "pricing_input_per_M_tokens": 0.95,
  "pricing_output_per_M_tokens": 4.00
}
```

**Sources:** [kimi.com/blog/kimi-k2-6](https://www.kimi.com/blog/kimi-k2-6), [kimi.com/ai-models/kimi-k2-6](https://www.kimi.com/ai-models/kimi-k2-6), [buildfastwithai.com](https://www.buildfastwithai.com/blogs/kimi-k2-6-review-benchmarks)

---

### 2. Mistral Medium 3.5: 128B Dense Model Consolidates Three Prior Releases

Released **April 29, 2026**, Mistral Medium 3.5 is a 128B **dense** (not MoE) model that merges its three predecessor specialist models (Medium 3.1, Magistral for reasoning, Devstral 2 for coding) into a single weight set. This is a significant architectural strategy shift — one model, one deployment, configurable reasoning depth per request.

**Architecture details:**
- 88 decoder layers, 12,288 hidden dim, 96 attention heads, 8 KV heads (GQA)
- Standard LLaMA-style RoPE + RMSNorm + SwiGLU MLP
- Trained-from-scratch vision encoder handling variable image sizes/aspect ratios
- Ships natively in **FP8** — fits on a single H200 node or 2× H100 nodes
- 256K context window; 40+ languages

**Standout design:** Per-request configurable reasoning effort allows the same weights to serve both fast chat responses and deep agentic tasks. This is analogous to OpenAI's effort parameter but applied to an open-weight model.

```json
{
  "model": "Mistral Medium 3.5",
  "release_date": "2026-04-29",
  "type": "dense",
  "parameters_total": "128B",
  "context_window": 262144,
  "native_precision": "FP8",
  "benchmarks": {
    "SWE_Bench_Verified": 0.776,
    "Tau3_Telecom_agentic": 0.914
  },
  "license": "modified MIT",
  "pricing_input_per_M_tokens": 1.50,
  "pricing_output_per_M_tokens": 7.50
}
```

**Sources:** [i-scoop.eu](https://www.i-scoop.eu/mistral-medium-3-5/), [lushbinary.com](https://lushbinary.com/blog/mistral-medium-3-5-developer-guide-api-benchmarks/), [nvidia docs](https://docs.nvidia.com/nemo/automodel/nightly/model-coverage/vlm/mistralai/mistral-medium-3-5.html)

---

### 3. The Condensate Theorem: Transformers Are O(n), Not O(n²)

arXiv:2602.06317 (Feb 6, 2026) — Jorge L. Ruiz Williams

This is one of the most theoretically striking recent claims: that the quadratic complexity of transformer attention is not an inherent property but an artifact of how the computation is implemented. The paper proves that **attention mass concentrates on a topological "Condensate Manifold"** that can be identified dynamically without evaluating all O(n²) pairs.

**The manifold has three components:**
1. An anchor position (globally attended token)
2. A local window (recent tokens)
3. Dynamic top-k elements (content-dependent)

**Key claims:**
- Projecting onto this manifold achieves **bit-exact output equivalence** with full O(n²) attention — not an approximation
- Validated across GPT-2, Pythia, Qwen2, TinyLlama, and Mistral on 1,500+ generated tokens
- Reference kernel achieves **159× measured speedup** at 131K tokens (3.94ms vs 628ms vs FlashAttention-2)
- Projected **>1,200× speedup** at 1M tokens, with 0.07% sparsity at 131K

**Why it matters:** If the theoretical claim holds up under broader scrutiny, it would mean that today's long-context inference costs — a dominant compute expense — are fundamentally unnecessary. The claim of bit-exactness (not approximation) is bold and invites verification. Community review is ongoing.

**Source:** [arxiv.org/abs/2602.06317](https://arxiv.org/abs/2602.06317), [GitHub reference implementation](https://github.com/JorgeLRW/condensate-theorem)

---

### 4. ICML 2026 Acceptance Wave: 6,500+ Papers, Conference July 6–11, Seoul

Author notifications went out **April 30, 2026** for ICML 2026 (43rd International Conference on Machine Learning, Seoul, COEX Convention Center, July 6–11). Over **6,500 papers** were accepted — roughly maintaining the scale from recent prior years.

**Selected accepted paper highlights:**

| Paper | Venue | Key Contribution |
|---|---|---|
| "On Training LLMs for Long-Horizon Tasks" (Kim et al.) | ICML 2026 | Horizon length induces training instability; horizon reduction + generalization |
| "InfoLaw: Information Scaling Laws" | ICML 2026 | 0.15% MAE loss prediction across data mixtures + repetition regimes |
| "Unsupervised Partner Design Enables Robust Ad-hoc Teamwork" (Ruhdorfer et al.) | ICML 2026 Spotlight | Multi-agent coordination without joint training |
| "MEAL: Continual Multi-Agent RL Benchmark" (Tomilin et al.) | ICML 2026 | Benchmark for continual learning in multi-agent settings |
| "Unlearning Isn't Deletion" (Xu et al.) | ICML 2026 | Machine unlearning is reversible via minimal fine-tuning; representational analysis |

**Source:** [icml.cc/Conferences/2026](http://icml.cc/Conferences/2026), [paperdigest.org](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)

---

### 5. ScaleRL: First 400,000 GPU-Hour RL Scaling Study for LLMs (ICLR 2026 Oral)

**"The Art of Scaling Reinforcement Learning Compute for LLMs"** (ICLR 2026 Oral) — the largest-scale empirical study of RL training for LLMs to date, spanning more than 400,000 GPU-hours.

**Core findings:**
1. **Different RL recipes converge to different asymptotic performance ceilings** — the choice of recipe sets an upper bound, not just efficiency
2. **Implementation details (loss aggregation, normalization, curriculum, off-policy) modulate compute efficiency without materially shifting asymptotes**
3. **Stable recipes follow predictable sigmoid-shaped scaling trajectories**, enabling extrapolation from smaller runs

**The ScaleRL recipe** outperforms DeepSeek-GRPO, Qwen2.5-DAPO, Magistral, and MiniMax-M1 at scale, reaching asymptotic reward 0.61. Extrapolated curves from early-stage runs closely predict 100,000 GPU-hour results.

**Practical implication:** Teams can now run small-scale pilot RL experiments (~hundreds of GPU-hours) and reliably predict whether a recipe will scale to production budget — reducing the risk of committing to a suboptimal RL approach at full compute.

**Sources:** [openreview.net](https://openreview.net/forum?id=FMjeC9Msws), [iclr.cc poster](https://iclr.cc/virtual/2026/poster/10010607)

---

## Deep Dive: Training Efficiency Papers from the May 2026 arXiv Batch

Several papers posted the week of May 5–6, 2026 (arXiv batch 2605.xxxxx) address fundamental questions in model training:

### Projection-Free Transformers via Gaussian Kernel Attention (arXiv:2605.02144)

Standard attention requires three learned projection matrices (Q, K, V) per head. GKA replaces these with a single scalar bandwidth parameter σₕ per head and computes token affinities directly via a Gaussian RBF kernel:

```
K^(h)_ij = exp(-||x_i^(h) - x_j^(h)||²_2 / 2σₕ²)
```

followed by row normalization and a single shared output projection Wₒ.

**Results at depth-20:**
- 0.42× parameters of standard attention baseline
- 0.49× total training FLOPs
- Trains stably with near-zero train/validation gap
- Slightly higher bits-per-byte at this compute scale (a natural tradeoff given parameter reduction)

**Interpretation:** GKA provides a new point on the accuracy-efficiency Pareto frontier with an explicit locality scale parameter σₕ that makes the model's spatial inductive bias directly interpretable. This connects transformers to classical kernel smoothing literature.

**Source:** [arxiv.org/abs/2605.02144](https://arxiv.org/abs/2605.02144)

---

### On Training LLMs for Long-Horizon Tasks: Horizon Length Study (arXiv:2605.02572, ICML 2026)

Kim et al. conduct a systematic empirical study of how horizon length H affects RL training of LLMs for multi-step tasks. Key finding: **increasing H creates a compounding triple failure mode:**

1. Higher per-step accuracy requirement (error compounds exponentially with H)
2. Exponential growth in state-action space makes exploration exponentially harder
3. Delayed reward signal creates increasingly ambiguous credit assignment

**Horizon Reduction as a training principle:** Training under reduced horizons, then evaluating at longer horizons, achieves better performance than direct long-horizon training — the paper calls this "horizon generalization." This parallels curriculum learning but applied to the time dimension of RL rollouts.

**Practical takeaway:** Teams training coding or agentic models with RL should not blindly maximize rollout length. Stepwise horizon scheduling may be essential for stability.

**Source:** [arxiv.org/abs/2605.02572](https://arxiv.org/abs/2605.02572)

---

### InfoLaw: Information Scaling Laws (arXiv:2605.02364, ICML 2026)

Standard Chinchilla-style scaling laws break down when pretraining data is quality-weighted (upsampled high-quality sources), because overtraining on limited high-quality data creates scale-dependent diminishing returns that existing formulas cannot model.

InfoLaw treats pretraining as **information accumulation**:
- Quality → information density per token
- Repetition → diminishing marginal information returns (scale-dependent)
- Loss predicted from: {consumed tokens, model size, mixture weights, repetition level}

**Accuracy:** 0.15% mean absolute error, 0.96% max absolute error across unseen training configurations. Validated up to 7B-parameter models with 425B tokens.

**Practical value:** Enables data recipe selection (which sources to weight, how much to oversample) without running a full grid search at target compute scale.

**Source:** [arxiv.org/abs/2605.02364](https://arxiv.org/abs/2605.02364)

---

## Architecture / Pattern Notes

### Tencent Hunyuan 3 (Hy3): Differentiated Expert Size MoE

Released April 23, 2026. Hy3 is notable for its **differentiated expert size design** — routing tokens of varying difficulty to experts of proportionally different capacity, with a P-Penalty Loss that penalizes over-routing to large experts to force utilization of small ones.

```json
{
  "model": "Tencent Hy3 Preview",
  "release_date": "2026-04-23",
  "type": "MoE",
  "parameters_total": "295B",
  "parameters_active": "21B",
  "num_experts": 192,
  "top_k_routing": 8,
  "context_window": 262144,
  "layers": "80 standard + 1 MTP",
  "attention_heads": 64,
  "kv_heads": 8,
  "precision": "BF16",
  "benchmarks": {
    "SWE_Bench_Verified": 0.744,
    "Terminal_Bench_2.0": 0.544,
    "MMMLU_multilingual": 0.8015,
    "GSM8K": 0.9537,
    "MATH": 0.7628
  },
  "deployment": ["vLLM", "SGLang"],
  "min_gpus": 8
}
```

**Source:** [github.com/Tencent-Hunyuan/Hy3-preview](https://github.com/Tencent-Hunyuan/Hy3-preview), [huggingface.co/blog/imnotkitty/hy3-preview](https://huggingface.co/blog/imnotkitty/hy3-preview)

---

### Anon Optimizer: Tunable Adaptivity Across the SGD–Adam Spectrum

arXiv:2605.02317 — accepted at AAAI 2025, now receiving attention as an ICML 2026 community highlight.

The core insight: adaptivity in gradient pre-conditioners is not binary (SGD vs Adam). **Anon introduces a continuous real-valued adaptivity parameter γ** that interpolates — and extrapolates — between SGD-like and Adam-like behavior.

**IDU (Incremental Delay Update):** More flexible than AMSGrad's hard max-tracking strategy. Provides convergence guarantees in both convex and non-convex settings across the full γ spectrum.

**Reported results:** Outperforms SOTA optimizers on image classification, diffusion models, and language modeling.

**Significance:** Provides a unified optimizer framework that makes adaptivity a tunable hyperparameter rather than a discrete architectural choice.

**Source:** [arxiv.org/abs/2605.02317](https://arxiv.org/abs/2605.02317)

---

### SuperNova: RLVR Beyond Math and Code (arXiv:2604.08477)

From UCLA (Suvarna, Phan, Beikzadeh, Bansal, Gabriel). RLVR has been largely confined to math and code because those domains have verifiable ground-truth rewards. SuperNova extends RLVR to **general reasoning** (causal inference, temporal reasoning) by curating 83 candidate tasks from the SuperNI instruction dataset and reformatting them into verifiable formats.

**Key methodological findings from 100+ controlled RL experiments:**
- Task selection by individual target performance > aggregate average performance
- Micro mixing (fine-grained task interleaving) > macro mixing (coarse batching)

**Results:** Up to 52.8% relative improvement on BBEH across model sizes; outperforms Qwen3.5 on BBEH, Zebralogic, and MMLU-Pro.

**Source:** [arxiv.org/abs/2604.08477](https://arxiv.org/abs/2604.08477)

---

## Analysis & Impact

### The Benchmark Landscape Is Rapidly Stratifying

This week's releases clarify a three-tier structure that is crystallizing in the open-weight ecosystem:

| Tier | Models | SWE-Bench Pro Range | Active Params | Price/M out |
|------|--------|---------------------|---------------|-------------|
| Open frontier | Kimi K2.6 | 58.6% | 32B | $4.00 |
| Open strong | Mistral Medium 3.5, Hy3 | 44–58% | 21–128B | $2–7.50 |
| Open efficient | Qwen3.5 32B, DeepSeek-V3.5 | 35–45% | 22–37B | $0.5–1.50 |

Kimi K2.6's SWE-Bench Pro score of 58.6% clearing GPT-5.4 (57.7%) on the same benchmark is a landmark: for the first time an open-weight model *leads* a closed frontier model on the most rigorous public coding benchmark, albeit by a narrow margin. This is partly a product of the SWE-Bench Pro benchmark design (not subject to the contamination issues that plagued SWE-Bench Verified).

### RL Scaling Is Now Predictable (Within a Recipe)

ScaleRL's finding that sigmoid-shaped compute-performance curves are reproducible and extrapolatable is practically transformative. It means RL training for LLMs is transitioning from alchemy (run for 10K GPU-hours and hope) to engineering (run for 500 GPU-hours, fit the sigmoid, predict the 50K-hour ceiling). The caveat: different recipes have different asymptotes. Recipe selection still requires empirical judgment.

### The Condensate Theorem Needs Community Verification

The claim of bit-exact O(n) attention equivalence at 159× speedup is extraordinary. The paper is a single-author work (no peer review yet evident), and 159× speedup on sequence length 131K needs independent replication. The theoretical core (sparsity is a learned topological property, not a design choice) is compelling if true, but the community should pressure-test the "bit-exact" claim on diverse model families and tasks before treating it as settled.

### Long-Horizon RL Training Has a Formal Instability Theory

The long-horizon training instability observed empirically by practitioners now has a principled theoretical account: exponential compounding of step error requirements + exponential state-action expansion + credit assignment ambiguity. This motivates horizon scheduling as a principled engineering practice, analogous to curriculum learning or learning rate schedules.

### Machine Unlearning Is Less Deletion Than Surface Erasure

The ICML 2026 accepted paper "Unlearning Isn't Deletion" is practically important for safety research: it shows that standard unlearning metrics (accuracy, perplexity) are misleading, and that all six standard unlearning methods leave models recoverable via minimal fine-tuning. Only one narrow case of seemingly irreversible targeted forgetting was identified. This should recalibrate confidence in unlearning as a safety mechanism.

---

## Key Takeaways TL;DR

1. **Kimi K2.6** (open MoE, 32B active) reaches 58.6% SWE-Bench Pro, edging GPT-5.4 — the open-weight frontier has caught the closed frontier on the hardest uncontaminated coding benchmark.

2. **Mistral Medium 3.5** (128B dense, FP8, single H200 node) merges three specialist models into one with configurable per-request reasoning depth — a new deployment paradigm for open models.

3. **Condensate Theorem** (arXiv:2602.06317) claims O(n) transformer attention with bit-exact equivalence at 159× measured speedup — extraordinary claim requiring community replication.

4. **ICML 2026** accepted 6,500+ papers (July 6–11, Seoul); highlights include InfoLaw's 0.15% MAE scaling predictions and the long-horizon RL instability study.

5. **ScaleRL** (ICLR 2026 Oral, 400K GPU-hours) proves RL training follows predictable sigmoid curves per recipe — asymptotic ceilings are recipe-determined, not just compute-determined.

6. **SuperNova** extends RLVR to general reasoning via curated verifiable instruction datasets, achieving 52.8% relative BBEH improvement — expanding RL's reach beyond math/code.

7. **Machine unlearning** (ICML 2026) is largely reversible: all six standard methods fail under representational analysis; safety teams should not rely on it as a deletion mechanism.

---

## Sources

| Item | URL |
|------|-----|
| Kimi K2.6 tech blog | https://www.kimi.com/blog/kimi-k2-6 |
| Kimi K2.6 model page | https://www.kimi.com/ai-models/kimi-k2-6 |
| Kimi K2.6 review/benchmarks | https://www.buildfastwithai.com/blogs/kimi-k2-6-review-benchmarks |
| Mistral Medium 3.5 overview | https://www.i-scoop.eu/mistral-medium-3-5/ |
| Mistral Medium 3.5 benchmarks | https://lushbinary.com/blog/mistral-medium-3-5-developer-guide-api-benchmarks/ |
| Mistral Medium 3.5 NVIDIA docs | https://docs.nvidia.com/nemo/automodel/nightly/model-coverage/vlm/mistralai/mistral-medium-3-5.html |
| Condensate Theorem arXiv | https://arxiv.org/abs/2602.06317 |
| Condensate Theorem GitHub | https://github.com/JorgeLRW/condensate-theorem |
| ICML 2026 conference | http://icml.cc/Conferences/2026 |
| ICML 2026 Paper Digest | https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/ |
| ScaleRL OpenReview | https://openreview.net/forum?id=FMjeC9Msws |
| ScaleRL ICLR poster | https://iclr.cc/virtual/2026/poster/10010607 |
| GKA arXiv | https://arxiv.org/abs/2605.02144 |
| Long-horizon training arXiv | https://arxiv.org/abs/2605.02572 |
| InfoLaw arXiv | https://arxiv.org/abs/2605.02364 |
| Hy3 GitHub | https://github.com/Tencent-Hunyuan/Hy3-preview |
| Hy3 HuggingFace blog | https://huggingface.co/blog/imnotkitty/hy3-preview |
| Anon optimizer arXiv | https://arxiv.org/abs/2605.02317 |
| SuperNova arXiv | https://arxiv.org/abs/2604.08477 |
| Unlearning Isn't Deletion arXiv | https://arxiv.org/abs/2505.16831 |
| Machine unlearning ICLR OpenReview | https://openreview.net/forum?id=7cEMkTu7Lf |
