# Machine Learning Research — 2026-06-02

> **Note:** No major conference today. ICML 2026 is scheduled for Seoul, South Korea, July 6–11, 2026. Accepted papers are now publicly listed on the ICML virtual site; awards will be announced at the conference.

---

## Top Stories (5)

### 1. MaxRL: Maximum Likelihood Reinforcement Learning — Fixes RL's Fundamental Approximation Flaw, Earns ICML 2026 Oral
**Source:** [ICML 2026 Oral](https://icml.cc/virtual/2026/oral/71072) | [arXiv:2602.02710](https://arxiv.org/abs/2602.02710) | [Project Page](https://zanette-labs.github.io/MaxRL/)

Standard reinforcement learning for binary correctness tasks (math, code, navigation) is mathematically provably only a *first-order approximation* of the maximum likelihood objective. For low-success prompts, the RL gradient signal vanishes — a fundamental flaw, not a tuning problem. MaxRL (Maximum Likelihood Reinforcement Learning), authored by Fahim Tajwar, Ruslan Salakhutdinov, Andrea Zanette et al., derives a principled fix by showing that the pass@k objective's Maclaurin expansion provides a family of objectives that interpolate between standard RL (at T=1) and full maximum likelihood (T→∞) as compute budget grows.

The key insight is that the log-likelihood of producing at least one correct answer — `log(1 - (1-p)^T)` — can be expanded as a truncated sum that gives increasingly accurate gradient signals at the cost of more sampling. MaxRL defines a compute-indexed family `J^(T)(x) = -∑_{k=1}^{T} (1-p)^k / k`, and derives a simple, unbiased policy-gradient estimator. At T=1, this collapses to GRPO/REINFORCE; at T→∞, it converges to exact MLE. The framework has been validated on maze navigation, GSM8K, and large-scale Qwen3 training (1.7B and 4B base models on the POLARIS-53K math reasoning dataset).

Results are striking: on Qwen3-4B, MaxRL **Pareto-dominates GRPO across all benchmarks**, achieving similar or better pass@1 while dramatically improving pass@k, translating to **7.9×–19.2× gains in test-time scaling efficiency**. MaxRL also exhibits less diversity degradation relative to the base model than GRPO, making it a better foundation for test-time search methods. The paper was awarded an oral presentation slot at ICML 2026 (July 7), confirming its theoretical and empirical significance.

**Key technical details:**
- Objective: `J^(T)_MaxRL(x) = -∑_{k=1}^{T} (1-p)^k / k` where p = pass@1 probability
- Gradient: `∇_θ J^(T) = ∑_{k=1}^{T} (1/k) ∇_θ pass@k(x)` — a weighted sum over pass@k gradients
- T=1 recovers standard RL/GRPO; T→∞ → exact MLE
- Pareto-dominates GRPO on Qwen3-4B across math benchmarks
- 7.9×–19.2× test-time scaling efficiency improvement vs. GRPO counterpart
- Admits simple on-policy estimator; no architecture changes required
- Validated: maze navigation, GSM8K, POLARIS-53K (~50K math prompts), and large-scale MoE pretraining

---

### 2. Mellum2 (JetBrains): 12B MoE Open-Source Model Matches 7B Dense Inference Throughput — Released June 1
**Source:** [JetBrains Blog](https://blog.jetbrains.com/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/) | [arXiv:2605.31268](https://arxiv.org/abs/2605.31268) | [HuggingFace](https://huggingface.co/collections/JetBrains/mellum-2)

JetBrains open-sourced Mellum2 on June 1, 2026 — a 12B-parameter Mixture-of-Experts model that activates only 2.5B parameters per token, purpose-built for software engineering workflows and multi-model agentic pipelines. Released under Apache 2.0, Mellum2 is positioned as an efficient inference-tier model for routing, RAG, summarization, sub-agents, code completion, and private deployments where latency matters more than peak capability.

The architecture makes several deliberate efficiency choices: 64 total experts with 8 activated per token, Sliding Window Attention (SWA) on 3 of every 4 layers (window size 1,024), full attention on the remaining layer to preserve long-range capability, Grouped-Query Attention (GQA) with 32 query heads and only 4 KV heads, and a Multi-Token Prediction (MTP) auxiliary head that doubles as a built-in draft model for speculative decoding. The net result: Mellum2 matches or exceeds the inference throughput of Qwen2.5-7B on a single H100, even at double the context length, because the SWA layers dominate compute.

Despite running at 2.5B active parameters, Mellum2 is competitive with full 7B dense models on several benchmarks, and notably outperforms them on EvalPlus (78.4% vs 69.4% for Qwen3.5-4B), demonstrating that careful architectural specialization can compensate for lower active parameter count. The context window is 131,072 tokens, achieved via a dedicated long-context extension phase in training.

**Key technical details:**
- 12B total params, 2.5B active per token (64 experts, top-8 routing)
- 28 layers, hidden size 2,304, bfloat16
- GQA: 32 query heads, 4 KV heads
- SWA: 3/4 layers with 1,024-token window; 1/4 full attention
- MTP head: auxiliary pretraining + speculative decoding draft
- Context length: 131,072 tokens
- EvalPlus: 78.4% | GSM8K: 81.7% | MMLU-Pro: 59.3% | BBH: 74.9% | LiveCodeBench v6: 37.2%
- Inference: matches/exceeds Qwen2.5-7B throughput on single H100
- License: Apache 2.0

---

### 3. JAMEL: Joint Agent Memory and Exploration Learning via Novelty Signals — Solves the Annotation-Free Memory Training Problem
**Source:** [arXiv:2606.01528](https://arxiv.org/abs/2606.01528) | [GitHub: MobileLLM/JAMEL](https://github.com/MobileLLM/JAMEL)

Training an agent's memory module is notoriously hard: latent memory representations cannot learn from task reward alone because they are compositional with the exploration policy and receive no direct supervision. JAMEL, a new paper from MobileLLM, solves this by observing a mutually reinforcing loop — good memory enables deeper exploration (avoiding revisiting exhausted states), and deeper exploration generates diverse trajectories that provide supervisory signal to train better memory. The key breakthrough is using deterministic, persistent novelty signals such as **code coverage** in GUI environments as annotation-free memory supervision.

Concretely, JAMEL's latent memory architecture compresses long interaction histories into memory tokens, cutting computational overhead for processing long trajectories. Training data is collected via rejection fine-tuning across 86 web applications in GUI domains (24K training samples). The memory module learns to encode information that enables the exploration policy to navigate to uncovered code paths — a signal that is deterministic (no human labeling), persistent (coverage is monotone), and rich (code coverage encodes semantic application structure).

JAMEL generalizes to 10 held-out unseen applications, outperforming all open-weight agent baselines on exploration depth, and rivals the exploration depth of a closed-source model while reducing token consumption. This positions JAMEL as a significant step toward agents that can bootstrap knowledge acquisition in novel environments without expensive human annotation.

**Key technical details:**
- Latent memory: compresses interaction history → memory tokens (reduces long-trajectory cost)
- Novelty signal: code coverage in GUI domain (deterministic, persistent, annotation-free)
- Training: rejection fine-tuning, 24K samples, 86 web applications
- Eval: 10 held-out unseen GUI applications
- Outperforms open-weight baselines on exploration depth; rivals closed-source
- Reduces token consumption vs. raw-history approaches
- Open-source: weights + code at github.com/MobileLLM/JAMEL

---

### 4. GAGPO: Critic-Free Temporal Credit Assignment for Multi-Turn Agentic RL
**Source:** [arXiv:2605.13217](https://arxiv.org/abs/2605.13217)

Multi-turn agentic RL has a fundamental credit assignment problem: trajectory-level rewards given only at episode end provide uniform, undifferentiated supervision to every intermediate step. GRPO broadcasts a shared advantage to all tokens, making it impossible for the policy to identify which specific steps were responsible for success or failure. GAGPO (Generalized Advantage Grouped Policy Optimization) addresses this with a critic-free approach that computes TD/GAE-style temporal advantages without a learned value function.

GAGPO treats each environment step (rather than each token) as the unit of credit. It constructs a non-parametric grouped value proxy from sampled rollout groups, computes step-aligned advantages via temporal recursion, and applies group-wise advantage normalization for stability. An action-level importance ratio replaces the standard token-level ratio, aligning optimization with the agent's decision boundaries rather than individual generated tokens.

On ALFWorld and WebShop with Qwen2.5-1.5B and 7B-Instruct, GAGPO outperforms strong RL baselines (GRPO, GiGPO) with faster early-stage learning, improved interaction efficiency, and smoother training dynamics. The critic-free design means no additional model to train or maintain, making it simple to drop into existing GRPO-style pipelines.

**Key technical details:**
- Unit of credit: environment step (not token)
- Grouped value proxy: non-parametric estimate from rollout groups
- Temporal propagation: TD/GAE-style recursion without a learned critic
- Group-wise advantage normalization for stable optimization
- Action-level importance ratio (not per-token)
- Benchmarks: ALFWorld, WebShop; models: Qwen2.5-1.5B, Qwen2.5-7B-Instruct
- Outperforms GRPO and GiGPO baseline on both benchmarks
- Simple integration: compatible with existing grouped policy optimization frameworks

---

### 5. MONA: Muon + Nesterov Acceleration Optimizer Achieves SOTA on 68B MoE Training at 1T Tokens
**Source:** [arXiv:2605.26842](https://arxiv.org/html/2605.26842)

Muon (Matrix Orthogonalization) has emerged as a strong alternative to AdamW for LLM pretraining, but like all first-order methods it can stagnate near sharp local minima. MONA (Muon Optimizer with Nesterov Acceleration) adds a curvature-aware acceleration term — an exponential moving average of gradient differences — directly into Muon's orthogonalization pipeline. This provides escape dynamics from sharp minima while preserving Muon's spectral-norm regularization.

MONA was validated at unprecedented scale: 1B, 15B, and 68B MoE architectures, with the largest trained on 1 trillion tokens. Across all three scales, MONA consistently outperforms both AdamW and vanilla Muon on validation loss. After code-specific SFT on the 68B model, MONA achieves new SOTA on BigCode benchmarks. For memory-constrained settings, MONA-Lite combines BF16 quantization with streaming gradient computation to cut the acceleration term's memory overhead by approximately 75% without training quality regression.

**Key technical details:**
- Acceleration term: EMA of gradient differences, plugged into Muon's pipeline
- Proven convergence: acceleration enables escape from sharp minima, retains spectral-norm regularization
- Scales: 1B, 15B, 68B MoE (largest trained on 1T tokens)
- Outperforms AdamW and Muon at all three scales on validation perplexity
- Post-SFT: SOTA on BigCode evaluations
- MONA-Lite: BF16 quant + streaming computation → ~75% memory reduction for acceleration term

---

## Deep Dive: Most Important Item

### Maximum Likelihood Reinforcement Learning (MaxRL) — A Theoretically Principled Fix to GRPO's Core Limitation

MaxRL is the most important research story today because it identifies and resolves a fundamental mathematical flaw in the dominant post-training paradigm for LLMs. GRPO and REINFORCE-style RL methods are used in nearly every state-of-the-art LLM training pipeline (DeepSeek-R1, Qwen3, o1/o3), yet MaxRL proves they are merely first-order approximations of the true maximum likelihood objective — and this approximation *systematically fails* on the hardest problems, precisely where we want LLMs to improve most.

The key theoretical result is as follows. For binary correctness tasks with pass rate p, the standard RL objective maximizes `E[R] = p`. The maximum likelihood objective for generating correct answers is instead `log(1 - (1-p)^∞)` = `log p` in the limit. The Taylor expansion of `-log(1-q)` around q=0 gives `-log(1-q) = q + q²/2 + q³/3 + ...`. Standard RL optimizes only the first term (q = 1-p), which provides vanishing gradient when p is near 0 — exactly the low-success regime where more learning signal is most needed.

MaxRL truncates this expansion at level T:

```
J^(T)_MaxRL(x) = -∑_{k=1}^{T} (1-p)^k / k
```

The corresponding gradient is:

```
∇_θ J^(T)_MaxRL(x) = ∑_{k=1}^{T} (1/k) ∇_θ pass@k(x)
```

This is a weighted sum over pass@k gradients, where higher-order terms provide learning signal even when p is near zero. The gradient estimator is unbiased and computable from sampled rollouts — it requires no new architecture, no critic, and no additional model. T is the only hyperparameter, controlling the trade-off between compute and fidelity to MLE.

The practical impact is substantial. On Qwen3-4B trained on POLARIS-53K math reasoning prompts, MaxRL achieves similar or better pass@1 vs. GRPO while providing 7.9×–19.2× improvements in pass@k — meaning models trained with MaxRL are dramatically more useful when combined with test-time search (best-of-N, beam search, MCTS). This is not a marginal improvement; it suggests GRPO-trained models have been systematically undertrained on hard examples.

The ICML 2026 oral award validates the community's recognition: this is both theoretically clean and empirically impactful. The method is immediately applicable to any pipeline currently using GRPO, REINFORCE, or RLOO — which is essentially the entire frontier of LLM post-training. If MaxRL scales to the sizes at which frontier models are trained (70B–671B parameters), it could unlock substantially more capable models from the same compute budget by better utilizing hard training examples.

**Open questions:**
- Does the scaling benefit of higher T (more sampling compute) hit diminishing returns at very high pass@1 regimes?
- How does MaxRL interact with process reward models vs. outcome reward models?
- Is there a computationally efficient online variant that avoids storing k rollouts per example?
- Does the MLE interpretation extend to multi-turn agentic settings with partial correctness signals?
- Can MaxRL's higher-order gradient terms be approximated with importance sampling rather than exact pass@k estimation?

**Broader significance:** MaxRL reveals that the dominant RL post-training paradigm for LLMs has been inadvertently sub-optimal since the introduction of RLHF. The theoretical connection to MLE creates a unified framework that bridges supervised learning and RL for discrete sampling. As test-time compute scaling becomes increasingly important (inference-time search, OpenAI o-series, Anthropic Extended Thinking), MaxRL's improvement in pass@k makes it a natural complement to those scaling strategies.

---

## Benchmark Data

```json
[
  {
    "benchmark": "pass@k test-time scaling efficiency",
    "scale": "Qwen3-4B",
    "results": [
      {"model": "MaxRL (Qwen3-4B)", "score": 19.2, "unit": "× efficiency gain over GRPO"},
      {"model": "MaxRL (Qwen3-1.7B)", "score": 7.9, "unit": "× efficiency gain over GRPO"},
      {"model": "GRPO (baseline)", "score": 1.0, "unit": "× (reference)"}
    ],
    "notes": "Efficiency measured as test-time scaling improvement in pass@k; MaxRL also matches or exceeds GRPO on pass@1"
  },
  {
    "benchmark": "EvalPlus (code generation)",
    "scale": "~10B parameter range",
    "results": [
      {"model": "Mellum2 Instruct (12B MoE, 2.5B active)", "score": 78.4, "unit": "%"},
      {"model": "Qwen3.5 (9B)", "score": 71.8, "unit": "%"},
      {"model": "Ministral 3 (14B)", "score": 74.1, "unit": "%"},
      {"model": "Qwen3.5 (4B)", "score": 69.4, "unit": "%"},
      {"model": "Seed-Coder (8B)", "score": 73.8, "unit": "%"},
      {"model": "OLMo-3 (7B)", "score": 67.3, "unit": "%"}
    ],
    "notes": "Mellum2 leads despite equivalent compute to a 2.5B dense model"
  },
  {
    "benchmark": "LiveCodeBench v6",
    "scale": "~10B parameter range",
    "results": [
      {"model": "Qwen3.5 (9B)", "score": 63.7, "unit": "%"},
      {"model": "Qwen3.5 (4B)", "score": 51.0, "unit": "%"},
      {"model": "Ministral 3 (14B)", "score": 42.4, "unit": "%"},
      {"model": "Mellum2 Instruct", "score": 37.2, "unit": "%"},
      {"model": "OLMo-3 (7B)", "score": 28.2, "unit": "%"},
      {"model": "Seed-Coder (8B)", "score": 28.1, "unit": "%"}
    ],
    "notes": "LCB v6 is a harder, contamination-resistant coding benchmark; Qwen3.5-9B leads"
  },
  {
    "benchmark": "GPQA Diamond",
    "scale": "~10B parameter range",
    "results": [
      {"model": "Qwen3.5 (9B)", "score": 79.8, "unit": "%"},
      {"model": "Qwen3.5 (4B)", "score": 76.8, "unit": "%"},
      {"model": "Ministral 3 (14B)", "score": 58.6, "unit": "%"},
      {"model": "Mellum2 Instruct", "score": 40.9, "unit": "%"},
      {"model": "OLMo-3 (7B)", "score": 40.9, "unit": "%"}
    ],
    "notes": "GPQA Diamond measures graduate-level scientific reasoning"
  },
  {
    "benchmark": "GSM8K",
    "scale": "~7B range",
    "results": [
      {"model": "Mellum2 (12B MoE)", "score": 81.7, "unit": "%"},
      {"model": "Qwen3.5 (9B, approx)", "score": 82.0, "unit": "%"},
      {"model": "Qwen2.5-7B (reference)", "score": 81.9, "unit": "%"}
    ],
    "notes": "Mellum2 competitive with 7B dense despite 2.5B active params"
  },
  {
    "benchmark": "MMLU-Pro",
    "scale": "~7-12B range",
    "results": [
      {"model": "Mellum2 (12B MoE)", "score": 59.3, "unit": "%"},
      {"model": "Qwen2.5-7B (reference)", "score": 54.9, "unit": "%"}
    ],
    "notes": "Mellum2 exceeds Qwen2.5-7B on MMLU-Pro"
  },
  {
    "benchmark": "BBH (Big Bench Hard)",
    "scale": "~7B range",
    "results": [
      {"model": "Mellum2 (12B MoE)", "score": 74.9, "unit": "%"},
      {"model": "Qwen2.5-7B (reference)", "score": 74.2, "unit": "%"}
    ],
    "notes": "Comparable performance; Mellum2 slightly above Qwen2.5-7B"
  },
  {
    "benchmark": "Spectra vs AdamW convergence speed",
    "scale": "LLaMA3-8B, 50B tokens",
    "results": [
      {"model": "Spectra", "score": 30.0, "unit": "% faster to same loss vs AdamW"},
      {"model": "Spectra optimizer state memory", "score": -49.25, "unit": "% vs AdamW"},
      {"model": "Spectra downstream accuracy gain", "score": 1.62, "unit": "pp over AdamW"},
      {"model": "Spectra vs Muon optimizer speed", "score": 5.1, "unit": "× faster than Muon"}
    ],
    "notes": "Spectra spike-aware optimizer for LLM training"
  },
  {
    "benchmark": "Soul benchmark (human behavior simulation)",
    "scale": "LLM-scale",
    "results": [
      {"model": "Ditto (RL with verbal feedback)", "score": 36.0, "unit": "% avg improvement over base model"},
      {"model": "Ditto vs GPT-5.4 (tasks won)", "score": 6.0, "unit": "out of 10 tasks"}
    ],
    "notes": "Soul spans 10 tasks: Theory of Mind, role play, social skill, learner/user/persona simulation"
  }
]
```

---

## Architecture / Diagram Notes

### Mellum2 MoE Architecture
```
Nodes:
  A[Token Input]
  B[Token Embedding (vocab: 98,304)]
  C[MoE Layer ×21 (SWA)]
  D[Full Attention Layer ×7]
  E[Router: Top-8 of 64 experts]
  F[Expert FFN ×8 (active)]
  G[GQA Attention (32Q / 4KV, window=1024)]
  H[MTP Head (speculative decoding draft)]
  I[Output Logits]
Edges:
  A→B: embed
  B→C: 3 of 4 layers are SWA MoE
  B→D: 1 of 4 layers is full-attention MoE
  C→E: route tokens
  E→F: activate top-8 experts
  F→G: aggregate expert outputs → attention
  D→G: full attention path
  G→C: layer stack repeats (28 total layers)
  G→H: auxiliary MTP objective during training
  G→I: final projection
Labels:
  C→E: [MoE routing, sparsely activated]
  H: [also serves as draft model at inference]
```

### MaxRL Training Loop
```
Nodes:
  A[Prompt x]
  B[Policy π_θ: sample k rollouts]
  C[Correctness Oracle: binary reward per rollout]
  D[pass@k estimator: estimate p = pass@1]
  E[MaxRL Objective: J^(T) = -∑_{k=1}^{T} (1-p)^k / k]
  F[Gradient: ∇_θ J^(T) = ∑_{k=1}^{T} (1/k) ∇_θ pass@k]
  G[Policy Update via gradient ascent]
Edges:
  A→B: condition policy on prompt
  B→C: evaluate k rollouts for correctness
  C→D: compute pass@k for k=1..T
  D→E: plug estimated p into truncated MLE objective
  E→F: derive unbiased policy gradient estimator
  F→G: update θ
  G→B: repeat with updated policy
Labels:
  B→C: [T rollouts sampled per prompt]
  E: [T=1 recovers standard RL; T→∞ recovers exact MLE]
```

### GAGPO Credit Assignment
```
Nodes:
  A[Multi-turn episode rollout (N trajectories)]
  B[Group rollouts sharing same prefix/state]
  C[Non-parametric grouped value proxy V̂(s)]
  D[TD/GAE temporal advantage A(s,a)]
  E[Group-wise advantage normalization]
  F[Action-level importance ratio clip]
  G[Policy update]
Edges:
  A→B: group by shared environment state
  B→C: estimate V̂(s) from group outcomes (no critic model)
  C→D: propagate rewards backward via TD recursion
  D→E: normalize advantages within group
  E→F: compute importance ratio at action boundary
  F→G: PPO-style clipped policy gradient update
Labels:
  B→C: [critic-free; non-parametric bootstrapping]
  D: [temporal recursion propagates outcome back to each step]
```

### JAMEL Memory-Exploration Loop
```
Nodes:
  A[Open-ended GUI environment]
  B[Exploration Policy π_explore]
  C[Latent Memory Module M (compresses history → tokens)]
  D[Novelty Signal: code coverage Δcov(a)]
  E[Rejection Fine-tuning on exploratory trajectories]
  F[Memory Supervision: trajectories using memory that discover new coverage]
Edges:
  A→B: agent acts in environment
  B→C: compress interaction history
  C→B: memory tokens condition next action
  B→D: execute action, measure Δ code coverage
  D→E: collect high-coverage-gain trajectories
  E→F: train memory module on trajectories where memory predicted correct novelty
  F→C: updated memory parameters
  F→B: updated exploration policy
Labels:
  C→B: [memory tokens replace raw history; reduces token cost]
  D: [deterministic, persistent, annotation-free signal]
  B↔C: [mutually reinforcing loop: better memory → deeper explore → better memory supervision]
```

---

## Analysis & Impact for ML Researchers

- **If you are currently using GRPO, RLOO, or REINFORCE for LLM post-training**, MaxRL is a near-drop-in replacement that you should evaluate immediately. The theoretical argument that RL for binary tasks is only a first-order MLE approximation is rigorous, and the 7.9×–19.2× test-time scaling efficiency improvement on Qwen3-4B is not marginal. Start by reproducing Figure 1 from the MaxRL website on your own task — if you see pass@k improvements over GRPO at the same compute, switch your pipeline. The ICML oral award indicates community consensus on impact.

- **If you need a fast routing, RAG, or sub-agent model in a multi-model pipeline**, Mellum2 offers an interesting trade-off: 7B-dense equivalent quality at 2.5B active parameter cost, with 2×+ throughput gains on H100. The MTP head also enables speculative decoding without a separate draft model. Before defaulting to a full 7B dense model for latency-sensitive roles, benchmark Mellum2 on your specific task — the EvalPlus and MMLU-Pro numbers suggest it may be competitive for most code-adjacent subtasks.

- **If your workload involves agentic RL in multi-turn settings** (web navigation, coding agents, tool-use agents), both GAGPO and JAMEL offer complementary improvements. GAGPO improves training credit assignment (better gradient signal per episode) while JAMEL improves exploration behavior (broader state coverage). Running GAGPO during training and deploying JAMEL-style memory at inference would be a natural combination for GUI or software automation agents.

- **For optimizer research and large-scale pretraining teams**: MONA and Spectra both challenge AdamW's default status for LLM training. Spectra's 30% wall-clock improvement and 49% memory reduction on LLaMA3-8B are validated on 50B tokens — a sufficient token count to be credible for pretraining workloads. MONA has been validated at 68B parameters on 1T tokens, which is production-scale. The Muon optimizer family appears to be maturing rapidly; it is worth running comparative ablations on your next training run.

- **Theoretical foundations of RL-from-feedback are being actively revisited**. MaxRL, GAGPO, and Ditto (verbal feedback RL) all challenge implicit assumptions in the dominant GRPO paradigm: MaxRL challenges the reward = RL objective equivalence; GAGPO challenges token-level credit assignment; Ditto challenges the need for scalar reward signals. The convergence of these critiques suggests that the post-DeepSeek-R1 training paradigm is about to undergo significant architectural evolution. Papers accepted at ICML 2026 (July 6–11) are now publicly listed — worth scanning the full accepted papers list for emerging themes.

---

## Key Takeaways (TL;DR)

- **MaxRL (ICML 2026 Oral)**: Standard RL for binary tasks is only a first-order MLE approximation; MaxRL fixes this with a compute-indexed Maclaurin expansion, achieving **7.9–19.2× test-time scaling efficiency** over GRPO on Qwen3-4B.
- **Mellum2 (JetBrains, June 1)**: Apache 2.0 12B MoE with 2.5B active params, 128K context, matches Qwen2.5-7B inference throughput on a single H100, leads EvalPlus at **78.4%** among the ~10B class.
- **JAMEL (arXiv:2606.01528, June 2)**: First open-source framework to train agentic latent memory using code-coverage novelty signals; rivals closed-source exploration depth while reducing token consumption.
- **GAGPO**: Critic-free step-aligned temporal credit assignment for multi-turn RL via non-parametric grouped value proxies; outperforms GRPO and GiGPO on ALFWorld and WebShop.
- **MONA optimizer**: Muon + Nesterov acceleration achieves SOTA on 68B MoE trained on **1 trillion tokens**; MONA-Lite cuts acceleration memory by ~75% with no quality loss.
- **Spectra optimizer**: Spike-aware optimizer reaches the same LLaMA3-8B loss **30% faster** than AdamW, cuts optimizer-state memory by 49.25%, and is 5.1× faster than Muon in per-step optimizer compute.
- **ICML 2026 (Seoul, July 6–11)**: Conference not yet held, but accepted papers now visible; oral slots and awards will be announced on-site — track the virtual site for breakthrough papers in the coming weeks.
- **RL training theory is in flux**: MaxRL, GAGPO, DGPO, and GraphGPO collectively challenge GRPO's token-level credit attribution — the post-training paradigm inherited from DeepSeek-R1 will likely look different by late 2026.
