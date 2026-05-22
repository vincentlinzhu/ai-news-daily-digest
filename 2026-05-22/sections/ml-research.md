# Machine Learning Research — 2026-05-22

> **Note:** ICML 2026 is upcoming (Seoul, July 6–11, 2026); invited speakers announced May 18. No major conference opening or awards today. ICLR 2026 Outstanding Papers were announced April 23. NeurIPS 2026 deadline September 26.

---

## Top Stories (3-5)

### 1. Orthrus: Lossless 7.8× LLM Inference Speedup via Dual-View Diffusion — Frozen backbone + trainable diffusion head shares one KV cache for parallel generation

**Source:** [arXiv:2605.12825](https://arxiv.org/abs/2605.12825) | [GitHub](https://github.com/chiennv2000/orthrus) | [HuggingFace](https://huggingface.co/papers/2605.12825)

Orthrus (Chien Van Nguyen et al., Adobe Research/University of Oregon) introduces a dual-architecture inference framework that augments a frozen autoregressive LLM with a lightweight trainable diffusion attention module at every layer. The key insight is that both the autoregressive head and the diffusion head share the *exact same* KV cache — eliminating the redundant memory overhead that plagues conventional speculative decoding systems, which must maintain separate KV caches for both drafter and verifier models.

The diffusion head projects K=32 candidate tokens in parallel during a single forward pass, while the AR head performs a second verification pass to accept the longest matching prefix. An exact consensus mechanism between the two views mathematically guarantees that the output distribution is *provably identical* to the base model — no accuracy degradation, unlike prior diffusion language model approaches (Fast-dLLM-v2 loses 11 points on MATH-500, Orthrus loses zero). Only 16% of model parameters are trained (the Q, K, V, O projections of the diffusion head), requiring fewer than 1 billion training tokens completed in 24 hours on 8×H200 GPUs.

Benchmarked on Qwen3-8B, Orthrus achieves an acceptance length of 11.7 tokens per forward pass on MATH-500, versus 7.9 for DFlash and 3.5 for EAGLE-3. The KV memory overhead is O(1) — approximately 4.5 MiB flat, independent of context length — versus the O(n) overhead of dual-cache speculative systems. This is a significant practical advantage as context lengths continue to grow.

The method outperforms speculative decoding baselines (EAGLE-3, DFlash) without requiring an external drafter model to initialize or synchronize, resulting in zero time-to-first-token (TTFT) penalty. The authors also find that single-step denoising beats multi-step denoising (6.35 vs. 3.53 tokens per forward pass), and KL distillation outperforms cross-entropy for training the diffusion head's acceptance rate.

**Key technical details:**
- Architecture: Frozen AR backbone (Qwen3-8B) + trainable diffusion attention at every layer; shared KV cache
- Acceptance length: 11.7 tokens/forward pass (vs. 7.9 DFlash, 3.5 EAGLE-3) on MATH-500
- Speedup: up to 7.8× tokens per forward pass (TPF); ~6× wall-clock on MATH-500
- Training cost: 16% of model parameters, <1B tokens, 24h on 8×H200 GPUs
- Memory overhead: O(1), ~4.5 MiB flat vs. separate drafter KV cache in speculative decoding
- Output distribution: provably identical to base model (lossless via exact consensus mechanism)
- Compared to: Dream, Fast-dLLM-v2 (-11 pts MATH-500), SDAR, Mercury, Gemini Diffusion — all of which modify base weights and lose accuracy
- Single-step denoising: 6.35 TPF vs. 3.53 for multi-step; KL distillation > CE loss for acceptance rate

---

### 2. Introspective Training (IXT): 2.8× FLOP Efficiency Gains by Flowing Post-Training Signals Backward Through All LLM Training Stages

**Source:** [arXiv:2605.20285](https://arxiv.org/abs/2605.20285) | NVIDIA Research / University of Washington / CMU / UC San Diego

NVIDIA Research (Brandon Cui, Ximing Lu et al.) proposes Introspective Training (IXT), a unified training algorithm applicable across pretraining, continued pretraining, and supervised fine-tuning stages. The core idea is elegantly simple: use a *thinking reward model* (judge LLM) to annotate every training document with rubric-based natural language critique feedback, then prefix-condition model training on that feedback. This forces quality awareness from the very start of pretraining — not just during post-training as is conventional — bending the standard scaling curve.

IXT is inspired by offline reward-conditioned RL (à la Decision Transformer) but operates at the document level and uses standard next-token prediction as the training objective. The feedback takes two forms: templated quality tokens (lightweight, robust) or free-form natural language critiques (more expressive, +2.6 points better on average). At inference time, the prefix can be tuned to steer generation toward desired quality dimensions, providing a pathway for test-time compute scaling. The annotation cost is computed once offline, meaning the total FLOP overhead is modest and fully accounted for in the reported efficiency numbers.

Experiments on transformer-based dense LLMs (7.5B–12B parameters) trained from scratch through 18 trillion tokens demonstrate consistent gains across all stages. From scratch on Dolmino, IXT raises the average from 43.1 to 48.7 (+5.6 points). Most strikingly, IXT achieves up to 2.8× FLOP efficiency — a model trained with IXT reaches the same performance using only 1/2.8 the compute of standard NTP training. In domain specialization for code, this advantage reaches 3.1× FLOP efficiency. The gains also persist at late-stage checkpoints: applying IXT at the 12T-token checkpoint surpasses the 18T-token general-corpus baseline on HumanEval (65.8% vs. 59.0%).

A key finding is that targeted annotation of only 15% of the data achieves comparable or better results than annotating the full blend, making the approach computationally practical. The method generalizes across rubrics and is domain-agnostic by default, though code-specific rubrics remain an open area for improvement.

**Key technical details:**
- Method: Judge LLM scores documents on rubric dimensions → natural language critique prepended as training prefix
- Total FLOPs accounting: `6·N_train·T_train + 2·N_ann·T_ann` (annotation cost fully included)
- Model scale: 7.5B–12B dense transformers, trained from scratch to 18T tokens
- From scratch (7.5B, Dolmino): GSM8K 35.8→50.2, MATH 42.2→53.9, HumanEval 32.8→37.7, MMLU 40.4→42.7
- FLOP efficiency: up to 2.8× overall; 3.1× on coding; math NTP never reaches IXT asymptote
- Late-stage (12T→IXT): HumanEval 65.8% vs. 59.0% baseline (18T NTP)
- Domain specialization (18T → IXT CPT): HumanEval +10.3 pts, MATH +3.5 pts
- SFT stage: +1.2 points overall average; concentrated in math/coding
- Natural language critiques outperform templated tokens by +2.6 average; +18.3 on GSM8K
- Annotation requires only 15% of data to match full-blend annotation performance

---

### 3. GRAM: Generative Recursive Reasoning Models with 10M Parameters Achieve 97% Sudoku-Extreme and 52% ARC-AGI-1

**Source:** [arXiv:2605.19376](https://arxiv.org/abs/2605.19376) | [Project page](https://ahn-ml.github.io/gram-website) | [OpenReview (ICLR 2026 Workshop RSI)](https://openreview.net/forum?id=Vxu6kcIjwV)

Junyeob Baek, Mingyu Jo, Minsu Kim, Yoshua Bengio, Sungjin Ahn (KAIST + Mila) introduce GRAM (Generative Recursive reAsoning Models), a framework that probabilizes the latent-state recursion used by deterministic recursive reasoning models (HRM, TRM, Looped Transformers). Rather than converging to a single attractor in latent space, GRAM models reasoning as a stochastic latent trajectory — drawing a latent transition from a learned distribution at each recursion step, enabling the model to maintain and explore multiple hypotheses simultaneously.

GRAM is a proper variational latent-variable model: it defines a joint `p_θ(y, z | x)` over outputs y and latent trajectories z given input x, optimized via amortized variational inference with a learned approximate posterior `q_φ(z | x, y)`. This formulation supports both conditional reasoning (`p_θ(y | x)`) and unconditional generation (`p_θ(x)`), providing a unified framework for discriminative and generative tasks in latent space. Inference scales along two axes: depth (more recursion steps) and width (parallel trajectory sampling) — giving practitioners a richer inference-time compute budget allocation strategy than standard chain-of-thought depth scaling.

With only 10 million parameters, GRAM achieves 97.0% accuracy on Sudoku-Extreme (vs. 87.4% for the deterministic TRM baseline), 52.0% on ARC-AGI-1, and 11.1% on ARC-AGI-2. For multi-solution constraint satisfaction tasks like N-Queens, GRAM achieves 90%+ solution coverage, demonstrating the benefit of stochastic trajectory sampling for problems with multiple valid solutions. The results are competitive with LLMs at orders of magnitude larger scale.

**Key technical details:**
- Architecture: Stochastic recursive latent transitions; amortized variational inference (`q_φ(z | x, y)`)
- Latent-variable model: `p_θ(y, z | x)` = conditional; `p_θ(x)` = unconditional generative
- Inference-time scaling: two axes — recursion depth (depth scaling) + parallel trajectory sampling (width scaling)
- Parameter count: 10M parameters
- Sudoku-Extreme: 97.0% (vs. TRM 87.4%, prior HRM 91.4%)
- ARC-AGI-1: 52.0%; ARC-AGI-2: 11.1%
- N-Queens solution coverage: 90%+
- Training: amortized variational inference, latent space computation (no token-level chain-of-thought)

---

### 4. Lance: ByteDance Open-Sources Unified Multimodal Model (3B Params, Apache-2.0) for Image/Video Understanding, Generation, and Editing

**Source:** [arXiv:2605.18678](https://arxiv.org/abs/2605.18678) | [Project page](https://lance-project.github.io/) | ByteDance Research

ByteDance Research releases Lance, a native unified multimodal model trained from scratch that handles image understanding, image generation, image editing, video understanding, and video generation within a single architecture and checkpoint. Unlike prior unified models that bolt together separate specialists or rely on scaling model capacity, Lance pursues task unification through *collaborative multi-task training* on shared interleaved multimodal sequences.

Lance's architecture uses a dual-stream mixture-of-experts design on shared interleaved multimodal sequences, with decoupled pathways for understanding versus generation. A custom modality-aware rotary positional encoding (RoPE variant) mitigates interference between heterogeneous visual tokens (image patches vs. video frames vs. text) while boosting cross-task alignment. Training uses a staged multi-task paradigm with capability-oriented objectives and adaptive data scheduling, completed on a budget of 128 A100 GPUs.

At 3B active parameters under the Apache-2.0 license, Lance represents a self-hostable unified multimodal baseline. The paper reports that Lance substantially outperforms existing open-source unified models on image and video generation benchmarks while retaining strong multimodal understanding. Demos on the project page illustrate text-to-video, multi-turn consistency editing, video question answering, and subject-driven generation.

**Key technical details:**
- Architecture: Dual-stream MoE on shared interleaved multimodal sequences; decoupled understanding/generation pathways
- Novel component: Modality-aware rotary positional encoding (RoPE) for heterogeneous visual tokens
- Training: Staged multi-task paradigm; adaptive data scheduling; 128 A100 GPUs
- Scale: 3B active parameters; Apache-2.0 license
- Capabilities: Image understanding + generation + editing; video understanding + generation
- Benchmarks: Outperforms open-source unified models on image/video generation; strong understanding retained
- Availability: Hugging Face + GitHub checkpoints

---

### 5. ScheduleFree+: Learning-Rate-Free LLM Training Beats Warmup-Stable-Decay by 31% at Long Training Horizons

**Source:** [arXiv:2605.19095](https://arxiv.org/abs/2605.19095) | [GitHub](https://github.com/facebookresearch/schedule_free) | Meta AI / Facebook Research

Meta AI (Aaron Defazio and colleagues) extends the original Schedule-Free Learning framework ("The Road Less Scheduled," 2024) to large language model training at production scale. Prior work had shown promise for Schedule-Free Learning on dozens of standard benchmark problems, but strong LLM training performance had only been demonstrated at small scales. ScheduleFree+ identifies and fixes several failure modes that emerge when scaling to larger batch sizes and larger models, incorporating a novel learning-rate-free Polyak step-size adaptation.

The core advantage of ScheduleFree learning is that it requires no learning rate schedule and no specification of the total training horizon in advance — it operates as an anytime training method. ScheduleFree+ demonstrates this advantage scales: at 1,000 tokens per parameter, ScheduleFree+ outperforms state-of-the-art Warmup-Stable-Decay (WSD) schedules by 31%, and reaches the same final loss value as a linear decay schedule run that is 45% longer (a 31% reduction in required training time). The approach also provides a theoretical foundation for model averaging and checkpoint merging during pretraining.

**Key technical details:**
- Method: Learning-rate-free + schedule-free optimization via adaptive Polyak step-size; no training horizon needed
- Baseline comparison: Warmup-Stable-Decay (WSD) schedules; Linear Decay with grid-searched LR
- Key result: 31% training time reduction to reach same loss at 1,000 tokens/parameter
- Equivalently: ScheduleFree+ reaches the same loss as a training run 45% longer
- Most effective for: Long-duration training (advantage widens with training duration)
- Provides: Theoretical foundation for model averaging and checkpoint merging during pretraining
- Implementation: `adamc_schedulefree_plus_paper.py` in `facebookresearch/schedule_free` repo
- Additional capability: Eliminates need for LR grid search entirely (automated via Polyak step-size)

---

## Deep Dive: Most Important Item

### Orthrus: Lossless Parallel Decoding via Dual-View Diffusion — Reframing the Inference Bottleneck

**Why this matters most:** Every LLM deployment faces the same fundamental bottleneck: autoregressive decoding generates one token per forward pass, making inference throughput linearly coupled to the cost of a full forward pass. Orthrus achieves a 7.8× speedup with *zero accuracy loss* and O(1) memory overhead, using only 24 GPU-hours of training on an existing model. Unlike prior speculative decoding methods that require separate drafter models (adding memory, TTFT latency, and synchronization complexity), or diffusion language models that require retraining from scratch and suffer accuracy degradation, Orthrus is a minimal surgical augmentation to any frozen transformer. The implications for production LLM serving costs are substantial.

**The core architecture.** Standard autoregressive decoding generates tokens sequentially: at step t, the model attends to tokens 1…t to produce token t+1. Each forward pass produces exactly one token. Orthrus adds a parallel "diffusion view" by injecting a lightweight diffusion attention module at every transformer layer. Both the AR head and the diffusion head share the *same* KV cache — the AR head constructs accurate KV representations during a prefill pass, while the diffusion head reads those representations to denoise K=32 candidate tokens *in parallel* in a single forward pass.

**The consensus mechanism.** After the diffusion head generates K parallel candidate tokens, the AR head performs a second verification pass, accepting the longest matching prefix for which the diffusion head's outputs match the AR distribution. This is not a soft approximation — the acceptance criterion is exact, analogous to speculative decoding's rejection sampling guarantee. The output distribution is provably identical to the base autoregressive model. This distinguishes Orthrus from diffusion language models (Dream, Fast-dLLM-v2, Mercury, Gemini Diffusion), which modify base model weights and shift the output distribution, resulting in accuracy degradation.

**Training efficiency.** Orthrus only trains the diffusion head's Q, K, V, O projections — approximately 16% of model parameters. The diffusion head is trained via KL distillation (against the AR head's output logits) rather than cross-entropy, which the authors find improves acceptance rate. The entire training run takes fewer than 1 billion tokens (trivially small by LLM standards) and completes in 24 hours on 8×H200 GPUs. This means Orthrus can be trained on top of any existing frozen LLM checkpoint without retraining or modifying base weights.

**Memory architecture advantage.** Conventional speculative decoding (EAGLE-3, DFlash) requires the drafter and verifier to maintain independent KV caches, resulting in O(n) additional memory proportional to sequence length. Orthrus's shared KV cache design reduces this to O(1) — approximately 4.5 MiB flat regardless of context length. As models operate on longer and longer contexts (1M+ tokens), this memory advantage compounds significantly. In throughput terms, the acceptance length on MATH-500 is 11.7 tokens per forward pass (vs. 7.9 for DFlash and 3.5 for EAGLE-3), and there is zero TTFT penalty since no external drafter needs to be initialized or synchronized before generation begins.

```
Orthrus Inference Algorithm:
1. Prefill pass (AR head): Build KV cache for input tokens 1...n
2. Diffusion forward pass: Diffusion head denoises K=32 candidate tokens in parallel
   using shared KV cache (single forward pass, parallel output)
3. Verification pass (AR head): Accept longest prefix matching AR distribution
4. Append accepted tokens; advance position pointer
5. Repeat from step 2 until EOS

Memory: O(1) overhead (4.5 MiB flat diffusion head params + shared KV cache)
Throughput: 11.7 accepted tokens/forward pass (MATH-500, Qwen3-8B)
```

**Open questions:**
- Evaluation is currently limited to Qwen3-8B; generalization to hybrid architectures (GatedDeltaNet + GatedAttention as in Qwen3.5/3.6) is being explored by the community but not yet validated
- The greedy + rejection sampling decoding has been validated; beam search and other decoding strategies remain untested
- Whether the diffusion head transfer-learns across base model sizes without retraining (scaling properties of the diffusion module) is unknown
- Long-context performance (beyond MATH-500 task lengths) needs evaluation
- The diffusion head's behavior under distribution shift (out-of-distribution inputs relative to its training set) is unexplored

**Broader significance:** Orthrus represents a paradigm shift in how we think about accelerating LLM inference. The key insight — that diffusion and autoregressive generation can coexist in a single model by sharing a KV cache — opens a new axis of model design orthogonal to architecture scaling, quantization, or distillation. If the approach generalizes across model families and hybrid architectures, it could become a standard component of LLM serving stacks. The 16% parameter, 24-hour training cost means any organization with an existing capable LLM can deploy Orthrus-style acceleration without the compute cost of training a separate drafter model.

---

## Benchmark Data

```json
[
  {
    "benchmark": "Tokens Per Forward Pass (Acceptance Length)",
    "scale": "Qwen3-8B on MATH-500",
    "results": [
      {"model": "Orthrus (dual-view diffusion)", "score": 11.7, "unit": "tokens/forward pass"},
      {"model": "DFlash (speculative decoding)", "score": 7.9, "unit": "tokens/forward pass"},
      {"model": "EAGLE-3 (speculative decoding)", "score": 3.5, "unit": "tokens/forward pass"}
    ],
    "notes": "Orthrus uses shared KV cache; no external drafter model; O(1) memory overhead"
  },
  {
    "benchmark": "Wall-clock Speedup (MATH-500)",
    "scale": "Qwen3-8B",
    "results": [
      {"model": "Orthrus", "score": 6.0, "unit": "x wall-clock speedup"},
      {"model": "Orthrus (TPF metric)", "score": 7.8, "unit": "x tokens per forward pass"}
    ],
    "notes": "Fast-dLLM-v2 achieves comparable speed but loses 11 points on MATH-500; Orthrus is lossless"
  },
  {
    "benchmark": "GSM8K",
    "scale": "7.5B from scratch (Dolmino, IXT paper)",
    "results": [
      {"model": "NTP (standard training)", "score": 35.8, "unit": "%"},
      {"model": "IXT (Introspective Training)", "score": 50.2, "unit": "%"}
    ],
    "notes": "IXT: +14.4 points on GSM8K from scratch; same training compute"
  },
  {
    "benchmark": "MATH",
    "scale": "7.5B from scratch (Dolmino, IXT paper)",
    "results": [
      {"model": "NTP (standard training)", "score": 42.2, "unit": "%"},
      {"model": "IXT (Introspective Training)", "score": 53.9, "unit": "%"}
    ],
    "notes": "IXT: +11.7 points on MATH from scratch"
  },
  {
    "benchmark": "HumanEval",
    "scale": "12T token checkpoint, continued pretraining (IXT paper)",
    "results": [
      {"model": "NTP at 18T tokens", "score": 59.0, "unit": "%"},
      {"model": "IXT from 12T checkpoint", "score": 65.8, "unit": "%"}
    ],
    "notes": "IXT at 12T surpasses NTP at 18T — 33% fewer tokens needed"
  },
  {
    "benchmark": "FLOP Efficiency (IXT vs NTP at matched performance)",
    "scale": "7.5B–12B models",
    "results": [
      {"model": "IXT overall", "score": 2.8, "unit": "x FLOP efficiency"},
      {"model": "IXT on coding", "score": 3.1, "unit": "x FLOP efficiency"}
    ],
    "notes": "Annotation cost included in FLOP accounting. On fixed corpus, NTP never reaches IXT asymptote on coding."
  },
  {
    "benchmark": "Sudoku-Extreme",
    "scale": "10M parameters",
    "results": [
      {"model": "GRAM (Generative Recursive Reasoning)", "score": 97.0, "unit": "%"},
      {"model": "TRM (deterministic)", "score": 87.4, "unit": "%"},
      {"model": "HRM-Text 1B (prior digest)", "score": 91.4, "unit": "%"}
    ],
    "notes": "GRAM achieves 97% with 10M params; TRM is deterministic recursive baseline"
  },
  {
    "benchmark": "ARC-AGI-1",
    "scale": "10M parameters (GRAM)",
    "results": [
      {"model": "GRAM", "score": 52.0, "unit": "%"}
    ],
    "notes": "Competitive with frontier LLMs at orders of magnitude fewer parameters"
  },
  {
    "benchmark": "ARC-AGI-2",
    "scale": "10M parameters (GRAM)",
    "results": [
      {"model": "GRAM", "score": 11.1, "unit": "%"}
    ],
    "notes": "ARC-AGI-2 human average ~34%; frontier models 84-85%"
  },
  {
    "benchmark": "Training Time Reduction (ScheduleFree+ vs. Linear Decay)",
    "scale": "120M–1B+ LLM, 1000 tokens/parameter",
    "results": [
      {"model": "ScheduleFree+ vs WSD", "score": 31.0, "unit": "% training time reduction"},
      {"model": "ScheduleFree+ vs Linear Decay (same final loss)", "score": 31.0, "unit": "% shorter training run"}
    ],
    "notes": "ScheduleFree+ advantage widens with training duration; requires no LR schedule or horizon specification"
  },
  {
    "benchmark": "DashAttention vs FlashAttention-3 (inference speedup)",
    "scale": "LLM inference, 75% sparsity",
    "results": [
      {"model": "DashAttention vs FlashAttention-3", "score": 3.36, "unit": "x speedup"},
      {"model": "DashAttention vs InfLLMv2", "score": 1.35, "unit": "x speedup"}
    ],
    "notes": "Achieves full-attention accuracy parity at 75% sparsity; alpha-entmax for adaptive variable-k block selection"
  }
]
```

---

## Architecture / Diagram Notes

### Orthrus Dual-View Diffusion Architecture

```
Nodes:
  INPUT[Input Tokens 1..n]
  PREFILL[Prefill Pass: AR Head builds KV Cache]
  KV[Shared KV Cache (O(1) overhead, ~4.5 MiB)]
  DIFF[Diffusion Head: Parallel denoise K=32 candidate tokens]
  AR[AR Head: Sequential verification pass]
  CONSENSUS[Exact Consensus Mechanism: longest matching prefix]
  OUT[Accepted Tokens (appended to output)]

Edges:
  INPUT → PREFILL
  PREFILL → KV
  KV → DIFF (read shared KV)
  KV → AR (read shared KV)
  DIFF → CONSENSUS (K=32 parallel candidates)
  AR → CONSENSUS (per-token logits for verification)
  CONSENSUS → OUT (longest accepted prefix)
  OUT → KV (loop: new tokens extend KV cache)

Labels:
  INPUT→PREFILL: context tokens
  PREFILL→KV: populate attention keys+values
  KV→DIFF: shared cache, no copy
  KV→AR: shared cache, no copy
  DIFF→CONSENSUS: 32 parallel denoised candidates
  AR→CONSENSUS: exact AR distribution logits
  CONSENSUS→OUT: accepted prefix (avg 11.7 tokens/pass)
  OUT→KV: loop until EOS
```

### Introspective Training (IXT) Pipeline

```
Nodes:
  RAW[Raw Training Data D]
  JUDGE[Judge LLM (thinking reward model, rubric-based)]
  CRITIQUE[Natural Language Critique / Quality Tokens]
  PREFIX[Prefixed Document: [critique] + [document]]
  MODEL[Language Model (7.5B–12B dense transformer)]
  NTP[Next Token Prediction Loss on prefixed sequence]
  WEIGHTS[Updated Model Weights]
  INFERENCE[Inference: prefix with desired quality descriptor]

Edges:
  RAW → JUDGE (one-time offline annotation, 15% of data)
  JUDGE → CRITIQUE (rubric-based quality scoring)
  RAW → PREFIX
  CRITIQUE → PREFIX (prepend critique to document)
  PREFIX → MODEL
  MODEL → NTP
  NTP → WEIGHTS (backprop)
  WEIGHTS → INFERENCE
  INFERENCE → MODEL (test-time quality steering)

Labels:
  RAW→JUDGE: offline pre-annotation (amortized cost)
  JUDGE→CRITIQUE: templated tokens OR free-form NL critique
  CRITIQUE→PREFIX: quality prefix conditioning
  NTP→WEIGHTS: standard LM training (no architectural change)
  INFERENCE→MODEL: user-specified quality prefix at test time
```

### GRAM Stochastic Recursive Reasoning

```
Nodes:
  X[Input x (problem/context)]
  Z0[Initial latent z_0]
  TRANS[Stochastic Transition: q_φ(z_t | z_{t-1}, x, y)]
  ZT[Latent State z_T (after T recursion steps)]
  DECODER[Decoder: p_θ(y | z_T, x)]
  Y[Output y]
  SAMPLE[Parallel Trajectory Sampling (width scaling)]
  AGGR[Trajectory Aggregation / Best-of-N]

Edges:
  X → Z0
  Z0 → TRANS (loop T times)
  TRANS → ZT (loop until T steps, stochastic each step)
  ZT → DECODER
  X → DECODER
  DECODER → Y
  Z0 → SAMPLE (spawn W parallel trajectories)
  SAMPLE → TRANS (each trajectory evolves independently)
  TRANS → AGGR (collect W×T final states)
  AGGR → Y (select best or aggregate)

Labels:
  Z0→TRANS: recursion depth axis (serial compute scaling)
  Z0→SAMPLE: width axis (parallel compute scaling)
  TRANS→ZT: stochastic latent transition (vs. deterministic in TRM/HRM)
  DECODER→Y: conditional p_θ(y|x) or unconditional p_θ(x)
```

---

## Analysis & Impact for ML Researchers

- **If you are doing LLM inference or serving at scale**, the Orthrus result is actionable today. The training cost (24h, 8×H200, 16% of parameters, <1B tokens) is low enough that any organization with an existing LLM can experiment. The O(1) memory overhead and zero TTFT penalty make it architecturally cleaner than speculative decoding in production. The open-source code (github.com/chiennv2000/orthrus) is available for experimentation. Caveat: currently validated only on Qwen3-8B with greedy/rejection sampling; hybrid architectures (Qwen3.5/3.6 with GatedDeltaNet) need separate adaptation work.

- **If you are training LLMs from scratch or continuing pretraining**, IXT (Introspective Training) from NVIDIA is highly relevant. The method requires only a judge LLM (any capable reasoning model) and your existing training pipeline — no architectural changes, just annotate 15% of your data and prepend critiques. The 2.8× FLOP efficiency gain is measured with annotation cost included. For long training runs (12T–18T tokens), the gains persist and accumulate. The key risk is rubric calibration: the reported gains assume a general-purpose quality rubric; domain-specific rubrics (especially for code) require additional engineering.

- **If you study reasoning architectures or work on ARC-AGI-style tasks**, GRAM demonstrates a compelling alternative to token-level chain-of-thought: stochastic latent-space recursion with probabilistic transitions. The 97% Sudoku-Extreme result at 10M parameters (vs. 91.4% for HRM-Text 1B) with parallel trajectory sampling is striking. The connection to variational inference and the dual conditional/unconditional generative formulation suggests this framework could unify reasoning and generation in a principled way. The ICLR 2026 workshop association (Reasoning and System 2 Thinking) signals community interest.

- **If you run long LLM training runs and want to eliminate LR schedule tuning**, ScheduleFree+ eliminates both the schedule and the learning rate grid search (replaced by Polyak step-size adaptation). The 31% training time reduction at 1,000 tokens/parameter and the "anytime" property (checkpoint any time, no horizon commitment) are practically valuable for research teams that iterate frequently. The open-source reference implementation is in the `facebookresearch/schedule_free` repo under `adamc_schedulefree_plus_paper.py`. Adopt cautiously at very large scales where the Polyak step-size behavior under distribution shifts is less well-studied.

- **If you need a unified open-source multimodal baseline** for image+video understanding, generation, and editing tasks, Lance (ByteDance, 3B params, Apache-2.0) represents the current best open-source unified model. The dual-stream MoE architecture with shared interleaved sequences and modality-aware RoPE is a practical design worth studying for anyone building multimodal systems. The staged multi-task training paradigm with adaptive data scheduling is a useful training recipe for multi-capability models, particularly on limited compute (128 A100s).

---

## Key Takeaways (TL;DR)

- **Orthrus (arXiv:2605.12825)** achieves a lossless 7.8× LLM inference speedup by adding a diffusion head that shares the AR model's KV cache, trained in 24h on 8×H200 GPUs at zero accuracy cost.
- **IXT (arXiv:2605.20285)** from NVIDIA bends LLM scaling curves by prefixing training data with LLM-generated quality critiques, delivering up to 2.8× FLOP efficiency across pretraining through SFT stages.
- **GRAM (arXiv:2605.19376)** achieves 97% on Sudoku-Extreme with only 10M parameters by making recursive latent-state reasoning probabilistic via variational inference, enabling inference scaling along both depth and width.
- **Lance (arXiv:2605.18678)** from ByteDance is a 3B-parameter Apache-2.0 unified model for image and video understanding/generation/editing, trained from scratch on 128 A100s with a dual-stream MoE and shared interleaved sequences.
- **ScheduleFree+ (arXiv:2605.19095)** eliminates both LR schedules and grid-search overhead for LLM training, outperforming WSD by 31% at 1,000 tokens/parameter and enabling true anytime training.
- **DashAttention (arXiv:2605.18753)** uses α-entmax for variable-k adaptive block selection in sparse hierarchical attention, achieving full-attention accuracy at 75% sparsity and 3.36× speedup over FlashAttention-3.
- **ICML 2026** (Seoul, July 6–11) announced its six invited speakers (Fung, Athey, Kakade, Regev, Rieser, Narayanan); conference will highlight ML fairness, economics, and AI safety alongside core research.
- The week's theme is **inference efficiency and training efficiency convergence**: Orthrus and DashAttention attack inference cost, IXT and ScheduleFree+ attack training cost, GRAM challenges the assumption that scale is required for reasoning.
