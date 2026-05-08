# Machine Learning Research — 2026-05-08

> **Note:** ICML 2026 is upcoming (Seoul, July 7–11, 2026); workshop list announced April 6 with 44 workshops (247 proposals submitted, most competitive in conference history). No major conference opening or awards today. CVPR 2026 (Denver) papers list published but best paper awards not yet announced as of today.

---

## Top Stories (3-5)

### 1. Odysseus — Princeton's Open Framework Trains VLMs to Play Super Mario Land via RL for 100+ Turns

**Source:** [arXiv:2605.00347](https://arxiv.org/abs/2605.00347) | [Project page](https://odysseus-project.github.io/) | [Hugging Face](https://huggingface.co/papers/2605.00347)

Researchers from Princeton Language and Intelligence (with collaborators at Fudan and Tsinghua) released Odysseus, an open training framework that extends vision-language models to long-horizon embodied decision-making via reinforcement learning. The work tackles a critical gap: existing RL for VLMs typically operates at 20–30 turn horizons, but meaningful real-world embodied tasks — robotics, GUI agents, game control — require hundreds of sequential decisions. Using Super Mario Land as a testbed, the team pushed a Qwen3-VL-8B-Instruct-based agent to achieve at least **3× higher average game progress** than frontier models including GPT-5.4 and GLM-4.6V, and **6×** over the base model.

The key algorithmic discovery is that **critic-free RL methods (GRPO, Reinforce++) fail** in long-horizon dense-reward settings, regardless of reward design. Only PPO with a learned critic succeeds — but the team's innovation is that this critic can be a **tiny CNN** (the same architecture used in classical deep RL), not a second full VLM as prior work assumed. This turn-level CNN critic decouples temporal credit assignment from token generation, roughly halving memory and compute compared to VLM-as-critic approaches. They further add **positive-advantage filtering** (discarding negative-advantage samples), which stabilizes optimization.

A key finding with broader implications: VLM-based RL achieves **~2× higher sample efficiency** than classical deep RL trained from scratch, even without action-space engineering. This confirms that the world knowledge encoded in pretrained VLMs functions as a genuine inductive prior for embodied control — not just a warm start. The framework includes a lightweight SFT initialization stage using ~5,000 walkthrough frames annotated by GPT-o3, emphasizing domain perception rather than action control.

**Key technical details:**
- Base model: Qwen3-VL-8B-Instruct; framework is model-agnostic
- PPO variant with turn-level CNN critic + positive-advantage filtering
- Auto-curriculum mechanism: sample level by inverse difficulty (harder levels sampled more frequently)
- Action space: 7 discrete buttons, up to 2 simultaneous; structured CoT via `<observation>`, `<analysis>`, `<action>` XML tags
- Reward: dense, forward x-position delta at each turn (`r_t = x_{t+1} - x_t`)
- Evaluation: 10 of 12 Super Mario Land levels; cross-game transfer maintained general-domain capabilities
- Code and checkpoints released open-source

---

### 2. Compute Optimal Tokenization (Meta / UW) — Bytes, Not Tokens, Are the Right Unit for Scaling Laws

**Source:** [arXiv:2605.01188](https://arxiv.org/abs/2605.01188) | [Project page](https://co-tok.github.io/) | [Meta AI Research](https://ai.meta.com/research/publications/compute-optimal-tokenization/)

Meta FAIR and the University of Washington published a landmark study that challenges a foundational assumption in neural scaling laws: that data volume should be measured in tokens. By training **988 Byte Latent Transformer (BLT) models** ranging from 50M to 7B parameters across a wide range of compression rates (T = 1 to 12 bytes/token), they discover that the optimal bytes-per-parameter ratio stays nearly constant regardless of compression rate or compute budget. This means the Chinchilla rule of ~20 tokens per parameter should be restated as ~60 bytes per parameter — a compression-rate-invariant formulation.

The second key result is that there exists an **optimal compression rate** for each training compute budget, and this optimal T* decreases slowly as compute grows. At 10^20 FLOPs, the optimal is T* ≈ 3.69 bytes/token, and at 2×10^21 FLOPs it's T* ≈ 3.33 — notably *below* the current standard BPE tokenizer rate of ~4.57 bytes/token. This means current BPE tokenizers at standard vocabulary sizes may be slightly over-compressed for large compute budgets, and future models may benefit from coarser tokenization. The result holds for both latent and subword tokenization and generalizes across six languages (French, Vietnamese, Arabic, Russian, Hindi, English).

This work provides practical guidance for any team selecting tokenizers: if training a very large model, consider slightly lowering compression versus standard BPE. The team also finds that at very large compute budgets, BPE with 90% of vocabulary masked (effectively lower compression) *outperforms* full-vocabulary BPE — a counterintuitive result that directly validates the decreasing-optimal-T* finding.

**Key technical details:**
- 988 BLT latent models + 320 subword models, 50M–7B params, 5×10^18 to 2×10^21 FLOPs
- Scaling Law I: `B*(C,T) ≈ B₀ · C^α · T^β`; fitted α=0.465, β=0.471 (both ≈0.5 confirms byte-constant scaling)
- Scaling Law II: `L*(C,T) ≈ L₀ · C^γ + F·log²(C^δ·T / T₀) + E`; fitted γ=−0.206
- Optimal bytes/parameter ratio ρ* ≈ 60 (vs Chinchilla's ~20 tokens/parameter with BPE)
- Current BPE: T=4.57; optimal at 10^20 FLOPs: T*≈3.69 (BPE is slightly over-compressed)
- HellaSwag 0-shot: 3.3B at T=4 scores 74.1% vs 3.3B at T=8 scores 68.2% at equal inference cost
- English results replicated for French, Vietnamese, Arabic, Russian, Hindi

---

### 3. CRISP / OPSDC — On-Policy Self-Distillation Achieves 57–59% Reasoning Token Compression While *Improving* Accuracy

**Source:** [arXiv:2603.05433](https://arxiv.org/abs/2603.05433) | [GitHub: HJSang/OPSD_Reasoning_Compression](https://github.com/HJSang/OPSD_Reasoning_Compression)

CRISP (Compressed Reasoning via Iterative Self-Policy Distillation), also known as OPSDC, presents a strikingly simple method to simultaneously reduce reasoning token counts and improve accuracy in thinking models. The insight: most tokens emitted by chain-of-thought models are not merely redundant but **actively harmful** — they compound errors and fill context with low-value deliberation. The method requires no extra annotations, no external critic, and no difficulty estimator: it simply adds a "be concise" instruction to generate teacher logits, then trains the student via per-token reverse KL divergence on its own rollouts.

On Qwen3-8B, the method achieves **59% token reduction** on MATH-500 with a **+9-point accuracy improvement** (77% → 86%). On Qwen3-14B, **57% compression** with **+16 points** (70% → 86%). On AIME 2024, the 14B model gains **+10 points with 41% fewer tokens**. Crucially, the compression is adaptive: easy problems are compressed ~1.6× more aggressively than hard ones, meaning the model learns to calibrate deliberation depth to problem difficulty automatically — without explicit difficulty supervision.

The method generalizes across model families (not just Qwen3) and transfers from math to multi-step planning tasks. This is significant because it suggests a training-time recipe applicable to any current thinking model without access to its training data or reward model. The result calls into question whether current thinking models are being trained with appropriate length penalties — CRISP implies that naive RLHF maximizing task reward with no token cost signal systematically over-produces reasoning tokens.

**Key technical details:**
- Method: "be concise" instruction → teacher logits → per-token reverse KL divergence on student's own on-policy rollouts
- No ground-truth answers, token budgets, or difficulty estimators required
- Qwen3-8B, MATH-500: 59% token reduction, 77% → 86% accuracy (+9pp)
- Qwen3-14B, MATH-500: 57% token reduction, 70% → 86% accuracy (+16pp)
- Qwen3-14B, AIME 2024: 41% token compression, +10 absolute accuracy points
- Easy vs. hard problem compression ratio: ~1.6× (adaptive, emergent — not supervised)
- Generalizes to multi-step planning beyond mathematical reasoning

---

### 4. NVIDIA Nemotron 3 Super — 120B Hybrid Mamba-Transformer MoE With 7.5× Throughput Gain Over Qwen3.5-122B

**Source:** [arXiv:2604.12374](https://arxiv.org/abs/2604.12374) | [NVIDIA Research](https://research.nvidia.com/labs/nemotron/Nemotron-3-Super/) | [NVIDIA Blog](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/)

NVIDIA released Nemotron 3 Super, a fully open-source 120B-parameter (12B active) hybrid Mamba-2/Transformer mixture-of-experts model targeting agentic reasoning workloads. The architecture integrates three key innovations: (1) **LatentMoE**, which routes tokens through a 1,024-dimensional latent space before expert selection, enabling 512 total experts with top-22 activation while reducing memory bandwidth; (2) a **hybrid Mamba-2 / self-attention backbone** that uses state-space layers for sequence processing but places full attention at strategic layers for precision reasoning; and (3) **Multi-Token Prediction (MTP)** for native speculative decoding support.

On benchmarks, Nemotron 3 Super matches or exceeds GPT-OSS-120B across most tasks while delivering **2.2× higher throughput** on 8K input / 64K output settings, and **7.5× higher throughput** than Qwen3.5-122B on those same settings. On coding, it scores 60.47% on SWE-Bench Verified (OpenHands), far ahead of GPT-OSS-120B's 41.90%, though trailing Qwen3.5-122B's 66.40%. On math competition tasks, it scores 93.67% on HMMT Feb 2025, outpacing both GPT-OSS-120B (90%) and Qwen3.5-122B (91.40%). The model was pretrained on 25 trillion tokens across two phases (20T diversity, 5T high-quality), followed by SFT and RL post-training, supporting 1M-token context.

**Key technical details:**
- Total parameters: 120B; active parameters per token: 12B (10:1 sparsity ratio)
- LatentMoE: 1,024-dim latent routing; 512 experts; top-22 activated per token
- Hybrid layers: Mamba-2 SSM backbone + strategic self-attention layers
- MTP: predicts multiple future tokens; enables native speculative decoding
- Training: 25T tokens (20T diversity phase + 5T quality phase) + SFT + RL post-training
- Context length: 1,000,000 tokens
- AIME 2025: 90.21%; HMMT Feb 2025: 93.67% (with tools: 94.73%)
- SWE-Bench Verified (OpenHands): 60.47%; LiveCodeBench: 81.19%
- Throughput: 2.2× vs GPT-OSS-120B; 7.5× vs Qwen3.5-122B (8K in / 64K out)
- Open-source: NVFP4, FP8, BF16 checkpoints + training recipes + datasets on HuggingFace

---

### 5. Lyapunov-Guided Cooperative Games for Stable Constraint Fusion in LLM Multi-Agent Systems

**Source:** [npj Artificial Intelligence (2026)](https://www.nature.com/articles/s44387-026-00110-5)

Published in Nature's npj Artificial Intelligence, this work addresses a fundamental stability problem in multi-agent LLM systems: when multiple agents share coupled constraints (e.g., collision avoidance, lane-keeping, speed limits in autonomous driving), naive constraint fusion causes the system to oscillate among local feasible solutions rather than converging. The paper formulates constraint fusion as a Lyapunov stability convergence problem, using cooperative differential game theory to find Pareto-improving constraint directions within a model predictive control (MPC) formulation.

The practical mechanism is elegant: constraint deviations across all agents are integrated into a unified system state metric via a Lyapunov function, and corrections are applied in real-time as **exponential penalty modifications to token probability distributions** during LLM inference. Evaluated on the nuScenes autonomous driving dataset using Llama3:8B as the base LLM, the framework achieves a **7.0% improvement** in overall constraint satisfaction rate over baseline methods, with gains across collision rate, trajectory accuracy, and individual constraint satisfaction metrics.

**Key technical details:**
- Framework: Lyapunov-guided cooperative differential game for multi-agent LLM constraint fusion
- MPC formulation for finding Pareto-improving constraint directions
- Intervention: exponential penalty on token probabilities at inference time (no retraining)
- Evaluation: nuScenes dataset; base LLM: Llama3:8B
- Overall constraint satisfaction improvement: +7.0% over baseline
- Metrics improved: collision rate, trajectory accuracy, constraint satisfaction rate

---

## Deep Dive: Most Important Item

### Compute Optimal Tokenization: Rewriting the Foundation of Neural Scaling Laws

This is the most significant theoretical result this week because it corrects a foundational assumption that every major LLM training run has silently relied on: that the "right" unit for scaling laws is the token. Kaplan et al. (2020) and Hoffmann et al. (2022, "Chinchilla") established that compute-optimal training requires roughly 20 tokens per parameter. But this ratio was derived using a fixed BPE tokenizer — and turns out to be tokenizer-specific, not fundamental.

The core finding is simple but profound: if you change the compression rate of your tokenizer (bytes per token), the optimal token-to-parameter ratio changes proportionally, but the optimal **byte**-to-parameter ratio stays roughly constant at ~60. This means the Chinchilla law should be stated as: train on ~60 bytes per parameter, not ~20 tokens per parameter. For a 70B model, that's 4.2 trillion bytes ≈ ~920 billion BPE tokens — close to what the community has empirically discovered through costly trial and error, but now derived from first principles.

```
Scaling Law I (optimal data): 
  B*(C, T) ≈ B₀ · C^α · T^β
  Fitted: α ≈ 0.465, β ≈ 0.471 (both ≈ 0.5)
  → ρ* = B*/N* ≈ constant ≈ 60 bytes/param

Scaling Law II (optimal loss):
  L*(C, T) ≈ L₀ · C^γ + F · log²(C^δ · T / T₀) + E
  Fitted: γ = −0.206, T₀ = 18.2, δ = 0.035
  → T*(C) = T₀ / C^δ (optimal compression decreases with compute)
  → T* = 3.69 at C = 10^20 FLOPs
  → T* = 3.33 at C = 2×10^21 FLOPs
  
Current BPE tokenizers: T ≈ 4.57 bytes/token
→ Slightly over-compressed at large compute scales
```

The practical implication for model builders: popular BPE tokenizers with ~4.57 bytes/token are near-optimal for mid-scale training but become slightly suboptimal at frontier scales. Teams training at 10^22+ FLOPs should consider tokenizers with compression rates of T ≈ 3–3.5. SuperBPE (T ≈ 6.16) and very aggressive compression are clearly suboptimal. The sweet spot is closer to standard BPE than to byte-level approaches.

The study also resolves a cross-tokenizer comparability problem: results from models with different tokenizers (e.g., Llama 3 BPE vs. Qwen3 BPE vs. a byte-level model) couldn't previously be compared on equal compute footing because tokens have different information densities. By anchoring to bytes, researchers now have a tokenizer-agnostic compute-optimal framework. This matters enormously for evaluating architectural innovations: a new architecture that achieves better loss at 10^20 FLOPs with a BPE tokenizer vs. a competitor using character-level tokenization can now be properly adjusted for compression rate before claiming a win.

The result generalizes to five non-English languages with diverse scripts (French, Vietnamese, Arabic, Russian, Hindi), with one finding specific to multilingual settings: optimal compression rate varies by language, roughly proportional to the "parity" (bytes of text in that language per byte of equivalent English text). Languages that encode more bytes per character at the UTF-8 level (e.g., Hindi in Devanagari, Arabic) benefit from different optimal compression rates than English.

**Open questions:**
- The study trains models up to 7B — do the findings extrapolate to 70B+ parameter regimes without re-validation?
- BLT (Byte Latent Transformer) was used to control compression; do results fully transfer to standard BPE architectures at the same scale?
- What is the optimal compression rate for code-heavy training corpora vs. natural language?
- Does the constant bytes/parameter ratio hold when data is multimodal (images, audio)?
- The study uses DCLM (English filtered web text) as primary corpus — how robust are findings to diverse multi-domain datasets?

**Broader significance:** This work reframes every scaling law discussion that has occurred since 2020. If the community adopts the bytes-per-parameter framing, it will enable apple-to-apple comparisons across models with different tokenizers, improve prescriptions for multilingual models, and provide a cleaner theoretical foundation for future tokenization research. It also implicitly validates the bet on byte-level and latent tokenization approaches — they sit closer to the natural unit of the scaling law than character-level or heavy BPE approaches.

---

## Benchmark Data

```json
[
  {
    "benchmark": "MATH-500 (Accuracy)",
    "scale": "8B",
    "results": [
      {"model": "Qwen3-8B baseline", "score": 77, "unit": "%"},
      {"model": "Qwen3-8B + CRISP", "score": 86, "unit": "%"}
    ],
    "notes": "CRISP achieves 59% token reduction alongside +9pp accuracy gain"
  },
  {
    "benchmark": "MATH-500 (Accuracy)",
    "scale": "14B",
    "results": [
      {"model": "Qwen3-14B baseline", "score": 70, "unit": "%"},
      {"model": "Qwen3-14B + CRISP", "score": 86, "unit": "%"}
    ],
    "notes": "57% token reduction with +16pp accuracy gain"
  },
  {
    "benchmark": "AIME 2024 (Accuracy)",
    "scale": "14B",
    "results": [
      {"model": "Qwen3-14B baseline", "score": null, "unit": "%"},
      {"model": "Qwen3-14B + CRISP", "score": null, "unit": "% (relative: +10pp, 41% token compression)"}
    ],
    "notes": "Absolute AIME baseline not reported; CRISP yields +10pp with 41% fewer tokens"
  },
  {
    "benchmark": "CRISP Token Compression Rate",
    "scale": "8B/14B",
    "results": [
      {"model": "Qwen3-8B MATH-500", "score": 59, "unit": "% tokens saved"},
      {"model": "Qwen3-14B MATH-500", "score": 57, "unit": "% tokens saved"},
      {"model": "Qwen3-14B AIME 2024", "score": 41, "unit": "% tokens saved"}
    ],
    "notes": "Easy problems compressed ~1.6x more aggressively than hard problems (emergent, not supervised)"
  },
  {
    "benchmark": "Super Mario Land Game Progress (vs frontier models)",
    "scale": "8B VLM",
    "results": [
      {"model": "GPT-5.4 (frontier)", "score": 1.0, "unit": "relative progress (baseline)"},
      {"model": "GLM-4.6V (frontier)", "score": 1.0, "unit": "relative progress (baseline)"},
      {"model": "Qwen3-VL-8B-Instruct (base)", "score": 1.0, "unit": "relative progress (baseline)"},
      {"model": "Odysseus (RL-trained)", "score": 5.0, "unit": "relative progress vs GPT-5.4 (5×)"}
    ],
    "notes": "Odysseus achieves 5x vs GPT-5.4, 3x vs GLM-4.6V, 6x vs base Qwen3-VL-8B"
  },
  {
    "benchmark": "SWE-Bench Verified (OpenHands)",
    "scale": "120B",
    "results": [
      {"model": "GPT-OSS-120B", "score": 41.90, "unit": "%"},
      {"model": "Nemotron 3 Super 120B-A12B", "score": 60.47, "unit": "%"},
      {"model": "Qwen3.5-122B", "score": 66.40, "unit": "%"}
    ],
    "notes": "Nemotron 3 Super far exceeds GPT-OSS but trails Qwen3.5-122B on this specific benchmark"
  },
  {
    "benchmark": "AIME 2025",
    "scale": "120B",
    "results": [
      {"model": "GPT-OSS-120B", "score": 92.50, "unit": "%"},
      {"model": "Nemotron 3 Super 120B-A12B", "score": 90.21, "unit": "%"},
      {"model": "Qwen3.5-122B", "score": 90.36, "unit": "%"}
    ],
    "notes": "Very close 3-way match on AIME 2025; all within 2.3pp"
  },
  {
    "benchmark": "HMMT Feb 2025",
    "scale": "120B",
    "results": [
      {"model": "GPT-OSS-120B", "score": 90.0, "unit": "%"},
      {"model": "Nemotron 3 Super 120B-A12B (no tools)", "score": 93.67, "unit": "%"},
      {"model": "Nemotron 3 Super 120B-A12B (with tools)", "score": 94.73, "unit": "%"},
      {"model": "Qwen3.5-122B", "score": 91.40, "unit": "%"}
    ],
    "notes": "Nemotron 3 Super leads on math competition despite being hybrid SSM architecture"
  },
  {
    "benchmark": "LiveCodeBench",
    "scale": "120B",
    "results": [
      {"model": "Nemotron 3 Super 120B-A12B", "score": 81.19, "unit": "%"},
      {"model": "Qwen3.5-122B", "score": 78.93, "unit": "%"}
    ],
    "notes": "Nemotron 3 Super leads Qwen3.5-122B by 2.26pp on live coding"
  },
  {
    "benchmark": "Inference Throughput (8K input / 64K output)",
    "scale": "120B",
    "results": [
      {"model": "GPT-OSS-120B", "score": 1.0, "unit": "relative (baseline)"},
      {"model": "Nemotron 3 Super 120B-A12B", "score": 2.2, "unit": "relative (2.2x over GPT-OSS)"},
      {"model": "Qwen3.5-122B", "score": 0.133, "unit": "relative (7.5x below Nemotron)"}
    ],
    "notes": "7.5x throughput advantage over Qwen3.5-122B is the headline efficiency claim"
  },
  {
    "benchmark": "Compute Optimal Bytes/Parameter Ratio",
    "scale": "50M–7B",
    "results": [
      {"model": "BLT latent (T=1)", "score": 60, "unit": "approx bytes/param (ρ*)"},
      {"model": "BLT latent (T=4)", "score": 60, "unit": "approx bytes/param (ρ*)"},
      {"model": "BLT latent (T=8)", "score": 60, "unit": "approx bytes/param (ρ*)"},
      {"model": "BPE subword (T=4.57)", "score": 60, "unit": "approx bytes/param (ρ*)"}
    ],
    "notes": "Constant ρ* ≈ 60 bytes/param holds across all compression rates and tokenizer types — this is the Chinchilla law restated in bytes"
  },
  {
    "benchmark": "Optimal Tokenizer Compression Rate vs Compute Budget",
    "scale": "50M–7B",
    "results": [
      {"model": "C=10^20 FLOPs", "score": 3.69, "unit": "optimal bytes/token (T*)"},
      {"model": "C=2×10^21 FLOPs", "score": 3.33, "unit": "optimal bytes/token (T*)"},
      {"model": "Current BPE (standard)", "score": 4.57, "unit": "bytes/token (T, not optimal at large scale)"}
    ],
    "notes": "Optimal compression decreases with larger compute; current BPE over-compressed at large scale"
  },
  {
    "benchmark": "LLM Multi-Agent Constraint Satisfaction (nuScenes)",
    "scale": "8B",
    "results": [
      {"model": "Llama3:8B baseline", "score": null, "unit": "% (relative: +7.0% improvement with Lyapunov framework)"},
      {"model": "Llama3:8B + Lyapunov cooperative games", "score": null, "unit": "+7.0% overall satisfaction rate"}
    ],
    "notes": "Evaluated on nuScenes autonomous driving; metrics include collision rate, trajectory accuracy, constraint satisfaction"
  },
  {
    "benchmark": "Qwen3-235B-A22B Benchmarks",
    "scale": "235B (22B active)",
    "results": [
      {"model": "Qwen3-235B-A22B (non-thinking)", "score": 89.2, "unit": "% MMLU-Redux"},
      {"model": "Qwen3-235B-A22B (non-thinking)", "score": 62.9, "unit": "% GPQA"},
      {"model": "Qwen3-235B-A22B (non-thinking)", "score": 24.7, "unit": "% AIME 2025"},
      {"model": "Qwen3-235B-A22B-Instruct-2507", "score": 93.1, "unit": "% MMLU-Redux"},
      {"model": "Qwen3-235B-A22B-Instruct-2507", "score": 77.5, "unit": "% GPQA"},
      {"model": "Qwen3-235B-A22B-Instruct-2507", "score": 70.3, "unit": "% AIME 2025"}
    ],
    "notes": "Instruct-2507 version shows dramatic gains; Apache 2.0, available on HuggingFace"
  }
]
```

---

## Architecture / Diagram Notes

### Odysseus: VLM + RL Pipeline for Long-Horizon Decision-Making

```
Nodes:
  A[Environment: Super Mario Land (POMDP)]
  B[Observation: Screen Frame + Prompt]
  C[VLM Agent: Qwen3-VL-8B]
  D[Structured CoT: <observation>, <analysis>, <action>]
  E[Action Parser]
  F[Frame-Skip Executor (N consecutive frames)]
  G[Reward Signal: Δx (forward position delta)]
  H[Turn-Level CNN Critic]
  I[PPO Update with Positive-Advantage Filtering]
  J[Auto-Curriculum Level Selector]
  K[SFT Initialization (5K frames, GPT-o3 annotations)]

Edges:
  A→B (observation at turn t)
  B→C (frame + prompt input)
  C→D (generate CoT)
  D→E (parse action tokens)
  E→F (execute action)
  F→A (environment step, loop until terminal)
  F→G (compute reward from game RAM x-coordinate)
  G→H (turn-level value estimation via CNN)
  H→I (advantage = r_t + γ·V_{t+1} - V_t; filter negative advantages)
  I→C (policy gradient update)
  J→A (select next level for training batch)
  K→C (SFT warmup before RL phase, one-time)

Labels:
  A→B: pixel frames + game state
  C→D: beam/greedy decode with CoT structure
  H: lightweight CNN, not full VLM critic
  I→C: PPO clipping objective, positive-advantage only
```

### Compute Optimal Tokenization: BLT Hierarchy

```
Nodes:
  A[Raw Text (bytes)]
  B[Local Encoder: CNN on byte n-grams]
  C[Latent Tokenizer: entropy-threshold segmentation]
  D[Latent Token Sequence (T bytes/token average)]
  E[Global Transformer Module: operates on latent tokens]
  F[Latent Representation per token]
  G[Local Decoder: cross-attention byte ← latent]
  H[Next-Byte Prediction Output]

Edges:
  A→B (byte-level feature extraction)
  B→C (entropy spikes define token boundaries)
  C→D (segments at average T bytes per latent token)
  D→E (standard Transformer forward pass)
  E→F (contextual latent embeddings)
  F→G (cross-attention: byte positions attend to latent)
  G→H (predict next byte)

Labels:
  C→D: compression rate T controllable by threshold
  D→E: bulk of compute here; reduce T → fewer tokens → fewer FLOPs
  Optimal T*: decreases with larger compute budget
```

### CRISP / OPSDC: On-Policy Self-Distillation Loop

```
Nodes:
  A[Reasoning Problem Input]
  B[Teacher: Same Model + "be concise" instruction]
  C[Teacher Logit Distribution P_teacher]
  D[Student: Same Model (no special instruction)]
  E[Student Rollout (on-policy sampling)]
  F[Per-Token Reverse KL Divergence Loss]
  G[Gradient Update (policy gradient + KL loss)]
  H[Updated Student: Shorter, More Accurate Reasoning]

Edges:
  A→B (input + "be concise" prompt)
  B→C (forward pass → teacher logits)
  A→D (same input, no conciseness instruction)
  D→E (on-policy sample reasoning trace)
  E→F (compare student tokens to teacher logits)
  C→F (KL target)
  F→G (backprop)
  G→D (update model parameters; loop until converged)
  G→H (final converged student)

Labels:
  B→C: no gradient through teacher
  F: reverse KL = Σ P_student · log(P_student / P_teacher)
  D→E: on-policy (student generates its own rollouts)
  H: adaptive compression — easy problems 1.6x more compressed than hard
```

---

## Analysis & Impact for ML Researchers

- **If you are training a large language model and selecting a tokenizer:** The compute-optimal tokenization paper (arXiv:2605.01188) directly affects your decision. Standard BPE at ~4.57 bytes/token is slightly over-compressed at frontier scales (10^21+ FLOPs). Plan to use compression rates closer to T≈3.3–3.7 bytes/token for largest runs. For multilingual models, measure the parity ratio of your target languages — Arabic and Hindi may need different optimal compression than English. Recommended action: read the paper and recompute your planned tokens/param ratios in bytes/param using ρ* ≈ 60.

- **If you are working on efficient inference for reasoning models:** CRISP (arXiv:2603.05433) provides an immediately deployable training recipe requiring no labeled data beyond a "be concise" system prompt and on-policy rollouts. Achieving 57–59% token reduction while *improving* accuracy (+9 to +16pp on MATH-500) is a qualitative regime shift — not a quality-latency tradeoff but a Pareto improvement. This should become a standard post-training step for any thinking model. Recommended action: replicate CRISP on your model family using the open-source code; likely to generalize beyond Qwen3.

- **If you are developing embodied agents or VLM-based decision-making systems:** Odysseus (arXiv:2605.00347) definitively establishes that (a) critic-free RL methods (GRPO/Reinforce++) fail at horizons >30 turns, (b) a tiny CNN critic is sufficient to stabilize PPO for VLMs — you do not need a second large model, and (c) pretrained VLMs provide ~2× sample efficiency over scratch-trained CNN agents even in novel visual environments. The auto-curriculum and positive-advantage filtering are simple additions worth including in any long-horizon VLM RL pipeline.

- **If you are evaluating open-source models for production agentic workloads:** Nemotron 3 Super (arXiv:2604.12374) changes the inference economics calculus. Its 7.5× throughput advantage over Qwen3.5-122B on long-output tasks (8K in / 64K out) is dramatic — at scale, this translates directly to cost and latency. For agentic tasks generating long reasoning traces or code completions, the effective cost per useful output token may be lower with Nemotron 3 Super despite comparable quality. The 1M context window and MTP-based speculative decoding make it particularly suited for retrieval-augmented generation at scale.

- **If you are building multi-agent LLM systems with safety or operational constraints:** The Lyapunov cooperative games paper (npj AI) offers the first formal framework with convergence guarantees for constraint fusion in multi-agent LLM systems. The key design choice — intervening via token probability penalties at inference time without retraining — means it can be wrapped around any existing LLM agent deployment. The 7% improvement on nuScenes is modest but the theoretical guarantees (Lyapunov stability → convergence proof) are more valuable than the number for safety-critical applications. The framework is immediately applicable to autonomous driving, robotics, and multi-agent code execution pipelines.

---

## Key Takeaways (TL;DR)

- **Odysseus (Princeton)** proves that PPO with a lightweight CNN critic enables VLMs to play 100+ turn games with 5× better performance than GPT-5.4, resolving the long-horizon RL training problem for VLMs.
- **Compute Optimal Tokenization (Meta/UW)** rewrites Chinchilla: the correct scaling unit is ~60 bytes/parameter (not ~20 tokens/param), and current BPE tokenizers are slightly over-compressed at frontier compute scales.
- **CRISP/OPSDC** simultaneously compresses reasoning traces 57–59% and *improves* accuracy by 9–16 points on MATH-500 using only a "be concise" self-distillation signal — no external annotations needed.
- **Nemotron 3 Super** (NVIDIA, 120B/12B active) delivers 7.5× inference throughput over Qwen3.5-122B and 2.2× over GPT-OSS-120B while matching quality on most benchmarks, fully open-source.
- **ICML 2026** received 247 workshop proposals (up from ~150 in 2025), accepted 44; conference runs Seoul, July 7–11 — the most contested ICML workshop selection in history signals accelerating field breadth.
- **Lyapunov cooperative games** provide the first stability-guaranteed constraint fusion for multi-agent LLM systems, achieving +7% constraint satisfaction on nuScenes via inference-time token probability modification.
- **Qwen3-235B-A22B** (Apache 2.0) remains a key open-weight frontier reference: 93.1% MMLU-Redux, 77.5% GPQA, 70.3% AIME 2025 in the Instruct-2507 configuration.
- The week's theme: **efficiency at every layer** — optimal tokenization reduces training waste, CRISP removes reasoning waste, Nemotron 3 Super reduces inference waste, and Odysseus reduces RL sample waste.
