# Machine Learning Research — 2026-04-27

> **Note:** ICLR 2026 Workshops are running today (April 27) in Rio de Janeiro, Brazil — the final day of the full ICLR 2026 program (main conference April 23–25, workshops April 26–27). Outstanding paper awards were announced April 23.

---

## Top Stories (5)

### 1. ICLR 2026 Outstanding Papers: Transformers Are Formally Succinct + Muon Optimizer Theory — Conference highlights expressivity theory and optimizer math

**Source:** [ICLR 2026 Awards Page](https://iclr.cc/virtual/2026/awards_detail) | [arXiv:2510.19315](https://arxiv.org/abs/2510.19315) | [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ) | [Polar Express OpenReview](https://openreview.net/forum?id=yRtgZ1K8hO)

ICLR 2026's Outstanding Paper Award went to "Transformers are Inherently Succinct" by Pascal Bergsträßer, Ryan Cotterell, and Anthony Widjaja Lin. The paper rigorously characterizes the expressive power of transformer architectures using the lens of succinctness — how compactly a model can represent formal concepts. The authors prove that fixed-precision transformers can describe formal languages (specifically star-free regular languages) exponentially more succinctly than equivalent finite automata or Linear Temporal Logic (LTL) formulas, revealing a previously underappreciated dimension of transformer capability.

A striking consequence of this succinctness result is intractability: the very property that makes transformers powerful also makes verifying their behavior EXPSPACE-complete. This has immediate implications for AI safety and interpretability research, as formal verification of transformer properties is provably as hard as problems believed to be outside even PSPACE. The work bridges automata theory, complexity theory, and deep learning in a way that is rare and rigorous.

The Honorable Mention went to "The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm" by Noah Amsel, David Persson, Christopher Musco, and Robert M. Gower. This work uses approximation theory to design GPU-friendly algorithms for the polar decomposition via polynomial approximations of the matrix sign function — directly improving the Muon optimizer used in competitive LLM training. In validation experiments training GPT-2 on 1–10 billion tokens from FineWeb, Polar Express consistently improved validation loss over competing optimizers across a wide range of learning rates.

**Key technical details:**
- "Transformers are Inherently Succinct": Fixed-precision transformers recognize exactly the star-free languages (a subclass of regular languages)
- Succinctness separation: transformers represent certain languages with exponentially fewer parameters than equivalent automata or LTL formulas
- Verification hardness: checking properties of transformers is EXPSPACE-complete
- Polar Express: uses only matrix-matrix multiplications (no custom CUDA kernels) for GPU efficiency
- Adapts update rule each iteration by solving a minimax optimization to minimize worst-case polar decomposition error
- GPT-2 validation: consistent loss improvements training on 1B–10B FineWeb tokens vs. Nesterov, Adam, Shampoo baselines
- arXiv identifier for "Succinct" paper: 2510.19315

---

### 2. Reinforcement Learning via Value Gradient Flow (VGF) — Reframing offline RL and RLHF as optimal transport

**Source:** [arXiv:2604.14265](https://arxiv.org/abs/2604.14265) | [GitHub: ryanxhr/vgf](https://github.com/ryanxhr/vgf) | [ICLR 2026 OpenReview](https://openreview.net/pdf?id=JLL4VNVhM9)

Value Gradient Flow (VGF), by Haoran Xu, Kaiwen Hu, Somayeh Sojoudi, and Amy Zhang (ICLR 2026), proposes a fundamentally different formulation for behavior-regularized reinforcement learning. Rather than specifying a policy as a parameterized distribution and optimizing it with policy gradients, VGF treats the problem as an optimal transport problem: find the distribution that maps a reference (the dataset distribution in offline RL, or the base model in RLHF) to a value-induced optimal distribution.

The core mechanics use discrete gradient flow. Starting from particles sampled from the reference distribution, VGF iteratively nudges each particle in the direction of the value gradient, transporting probability mass toward high-value regions of policy space. Regularization is implicit: the total transport budget controls how far particles move from the reference, replacing explicit KL penalties or behavior cloning terms. This design elegantly unifies offline RL and RLHF fine-tuning under a single mathematical framework.

A compelling feature is adaptive test-time scaling: at inference time, users can increase the transport budget (more gradient-flow steps) to further optimize outputs, functioning like a test-time compute knob. This is analogous to how sampling temperature or chain-of-thought steps are tuned in LLMs, but grounded in the RL objective rather than heuristics. The method achieves state-of-the-art on both D4RL (locomotion and manipulation tasks) and OGBench (offline goal-conditioned RL suite), as well as LLM alignment tasks.

**Key technical details:**
- VGF objective: minimize `E_{x~π}[V(x)] + (1/β) * W₂(π, π_ref)` where W₂ is Wasserstein-2 distance
- Implementation: discrete particle transport — sample `{x_i}` from π_ref, update `x_i ← x_i + α * ∇_x V(x_i)`
- No explicit policy parameterization required — policy is implicit in particle set
- Regularization strength controlled by transport budget τ (number of steps × step size)
- D4RL benchmark: SOTA on standard locomotion suite (HalfCheetah-medium-v2, Hopper-medium-expert-v2, etc.)
- OGBench: SOTA on several goal-conditioned offline RL tasks
- Test-time scaling: 2–5× more transport steps consistently improves final policy quality
- Eliminates need for policy networks that are incompatible with large generative model architectures

---

### 3. Train-to-Test (T²) Scaling Laws: Overtraining Is Compute-Optimal When Inference Counts — Rethinking the Chinchilla paradigm

**Source:** [arXiv:2604.01411](https://arxiv.org/abs/2604.01411) | [HuggingFace Paper Page](https://huggingface.co/papers/2604.01411) | [Emergent Mind Summary](https://www.emergentmind.com/papers/2604.01411)

The paper "Test-Time Scaling Makes Overtraining Compute-Optimal" introduces Train-to-Test (T²) scaling laws, which jointly optimize model size N, training tokens D, and number of inference samples k under a fixed total compute budget C_total = C_train + k × C_infer. The central finding: when inference cost is included in the compute budget, the optimal pretraining point shifts dramatically into the "overtraining" regime — training substantially smaller models on far more tokens than Chinchilla prescribes.

The intuition is as follows. A Chinchilla-optimal model of size N is trained for D ∝ N tokens, giving a single strong sample at inference. But a model trained at 10× Chinchilla tokens (heavily overtrained) costs the same to train, produces a weaker individual sample, but if test-time compute (best-of-k, chain-of-thought, beam search, etc.) is applied, the aggregate of k samples from the overtrained model often dominates. The cross-over point depends on the relative cost of training vs. inference and the specific test-time scaling method used.

T² formalizes this through two complementary estimators: T²-NLL (which models per-token loss as a function of N, D, k) and T²-Acc (which directly fits task accuracy). Both are validated by actually training heavily overtrained models in the optimal compute region T² forecasts, then applying pass@k and majority-vote decoding. Across eight downstream tasks, T² predictions are confirmed: heavily overtrained small models with moderate test-time scaling outperform Chinchilla-optimal large models under equal total compute.

**Key technical details:**
- Total budget: C_total = 6ND + k × C_infer (where C_infer ≈ 2N per token for autoregressive decoding)
- Optimal N* under T² is significantly smaller than Chinchilla-optimal N* = sqrt(C_train / 6)
- Optimal D* under T² is substantially larger: D* ∝ C_train / (6N*) ≫ N*
- Two methods: T²-NLL fits loss surface; T²-Acc fits task-specific accuracy surface
- Validated on 8 downstream tasks; results robust through post-training (SFT, RLHF) stages
- Practical implication: at 10²³ total FLOPs with k=64 samples, optimal model is ~3× smaller but trained ~3× longer than Chinchilla-optimal
- Effect is stronger for reasoning-heavy tasks where test-time scaling has higher returns

---

### 4. Decoupled DiLoCo: Google DeepMind's Resilient Distributed Training at 0.84 Gbps — Internet-speed inter-datacenter LLM training

**Source:** [Google DeepMind Blog](https://deepmind.google/blog/decoupled-diloco/) | [GitHub: google-deepmind/asyncdiloco](https://github.com/google-deepmind/asyncdiloco) | [MarkTechPost Coverage](https://www.marktechpost.com/2026/04/23/google-deepmind-introduces-decoupled-diloco-an-asynchronous-training-architecture-achieving-88-goodput-under-high-hardware-failure-rates/)

Google DeepMind released Decoupled DiLoCo in April 2026, a distributed training architecture enabling LLM training across geographically distributed data centers over internet-scale bandwidth. The key insight is decoupling the inner loop (standard gradient descent within each "island" of compute) from the outer loop (periodic synchronization between islands), allowing islands to run fully asynchronously without waiting for slower or failed peers.

Classical data-parallel training requires tight all-reduce synchronization across all chips — any hardware failure stalls the entire run. DiLoCo (2023) reduced inter-datacenter bandwidth by allowing many local gradient steps before communicating, but still required synchronous outer updates. Decoupled DiLoCo removes even this synchrony: islands process their own data streams, periodically push their local model updates to a parameter server, and immediately continue without waiting. The parameter server merges updates asynchronously using an outer optimizer (e.g., Nesterov momentum).

The bandwidth numbers are striking: standard data-parallel training across 8 data centers requires ~198 Gbps of inter-datacenter bandwidth. Decoupled DiLoCo requires only 0.84 Gbps — a 236× reduction — enabling training across data centers connected by standard internet links rather than bespoke high-speed interconnects. The system achieves 88% goodput (fraction of time doing productive computation) even under high hardware failure rates, validated using chaos engineering: artificial failures were introduced during Gemma 4 training runs.

**Key technical details:**
- Architecture: learner islands (inner workers) + async parameter server (outer coordinator)
- Inner optimizer: standard AdamW within each island; outer optimizer: Nesterov momentum on pseudo-gradients
- Pseudo-gradient: difference between island start-of-round parameters and end-of-round parameters
- Inter-datacenter bandwidth: 0.84 Gbps vs 198 Gbps for synchronous data-parallel (236× reduction)
- Goodput: 88% under high hardware failure rates (full learner unit failures tolerated)
- Tested on Gemma 4 training runs with chaos engineering (injected hardware failures)
- Island count: validated at up to 8 geographically distributed data centers
- Built on Pathways (async data flow) + original DiLoCo (low-communication federated training)
- Open-sourced at github.com/google-deepmind/asyncdiloco

---

### 5. Batched Contextual Reinforcement (BCR): Task-Scaling Law for Efficient Reasoning — 62.6% fewer tokens, same accuracy

**Source:** [arXiv:2604.02322](https://arxiv.org/abs/2604.02322) | [AlphaXiv Overview](https://www.alphaxiv.org/overview/2604.02322v1)

Batched Contextual Reinforcement (BCR), by Bangji Yang, Hongbo Ma, Jiajun Fan, and Ge Liu, addresses the runaway token cost of chain-of-thought (CoT) reasoning in LLMs by training models to solve N problems simultaneously within a single shared context window. Instead of generating a complete solution for one problem before starting the next, BCR presents all N problems together and trains the model to interleave solutions, cross-reference shared reasoning, and eliminate redundant metacognitive loops.

The training signal is per-instance accuracy: each of the N problems is evaluated independently, and correct solutions are reinforced regardless of the token budget used. Crucially, no explicit length penalty is applied — models learn token efficiency as an emergent behavior from the implicit competition for context space among concurrent problems. This avoids the adversarial gradients and training instability that plague explicit length penalty approaches.

The result is a task-scaling law: as N (the batch size of concurrent problems) increases, per-problem token usage decreases monotonically in a power-law fashion, while accuracy degrades much more slowly. At N=8, token reduction of 62.6% was measured on 4B-parameter models with maintained or improved accuracy across five major mathematical benchmarks (MATH, AMC, AIME, GSM8K, Olympiad-level). The authors term this a "free lunch" — throughput scales with N (more problems processed per forward pass) while per-problem quality holds.

**Key technical details:**
- Training paradigm: N problems concatenated in context, each solved with per-instance RL reward
- No explicit length supervision; efficiency emerges from context competition
- Task-scaling law: token_per_problem ∝ N^{-α} for some α > 0 (power-law decay)
- Token reduction: 15.8% (N=2) to 62.6% (N=8) on 4B models
- Accuracy: maintained or improved on MATH, AMC, AIME, GSM8K, Olympiad benchmarks
- Models tested: 1.5B and 4B parameter families
- Emergent behavior: models eliminate redundant metacognitive preamble ("Let me think step by step...")
- Throughput benefit: 8× concurrent problems processed with ~2.7× total tokens (3× amortized efficiency)
- Circumvents adversarial gradient problem of explicit length penalties (no mode collapse observed)

---

## Deep Dive: Most Important Item

### Train-to-Test (T²) Scaling Laws: Why Overtraining Is Now the Right Answer

This paper matters most because it directly challenges and supersedes the Chinchilla scaling law, which has been the dominant guide for LLM pretraining compute allocation since 2022. Chinchilla argued that for a fixed training compute budget C, the optimal model size is N* ∝ sqrt(C) and optimal tokens are D* ∝ sqrt(C), giving a 1:1 ratio of model-size FLOPs to data FLOPs. T² shows that this is correct only if you ignore the inference phase — and in the era of test-time scaling (chain-of-thought, majority vote, MCTS, beam search), you cannot ignore inference.

**The Math of T² Scaling**

Standard Chinchilla formulation minimizes training loss L(N, D) subject to C_train = 6ND:

```
L(N, D) = E + A/N^α + B/D^β
```

where E is irreducible entropy, A, B, α, β are fitted constants (Hoffmann et al. 2022 found α ≈ 0.34, β ≈ 0.28 for large LLMs). Minimizing under C_train = 6ND gives:

```
N* = (A·α / (B·β))^(1/(α+β)) · (C/6)^(β/(α+β))
D* = C / (6·N*)
```

T² instead minimizes total compute C_total = C_train + k·C_infer where C_infer ≈ 2N (cost of one generation at length L_gen). The quantity to optimize is not L(N,D) but the accuracy under k inference samples:

```
Acc(N, D, k) = f(L(N, D), k)   [T²-Acc model]
or
Acc ≈ g(pass@k, L(N,D))       [via pass@k = 1 - (1 - p(L))^k where p ~ e^{-L}]
```

The joint optimization over (N, D, k) subject to 6ND + 2Nk·L_gen ≤ C_total shifts the optimal N* downward and D* upward:

```
N*_T2 < N*_Chinchilla
D*_T2 > D*_Chinchilla
k* > 1 (use multiple inference samples)
```

**Empirical Validation**

The authors actually trained models in the T²-optimal compute region — something previous scaling law papers sometimes skipped. They trained models at 3–10× Chinchilla token counts (heavy overtraining) then evaluated with k=1, 4, 16, 64 samples using both greedy decoding and majority voting. The T²-Acc predictions were accurate to within ~2% across 8 downstream tasks.

**Implications for the Field**

The result has immediate practical consequences. At a fixed inference budget of, say, $1M/month serving a production model, a company should train a smaller, overtrained model and use test-time compute to compensate, rather than a large Chinchilla-optimal model used once per query. This shifts the optimal point toward what some practitioners (e.g., TinyLlama, MiniCPM teams) had intuited but not formally justified.

The result also applies post-training: T² scaling holds through SFT and RLHF fine-tuning stages, meaning the inference-budget-adjusted pretraining optimum transfers to the final deployed model. This is non-trivial because post-training can shift the loss landscape significantly.

**Open questions:**
- How do T² optimal points change when using speculative decoding, where inference cost is no longer linear in N?
- Does the T²-NLL model remain accurate for very long inference chains (multi-step reasoning with 1000+ tokens)?
- How does test-time scaling quality (the function f(L, k)) vary across task domains — is the math valid for coding, factual QA, and multi-step reasoning equally?
- What happens at the extreme overtraining limit (100× Chinchilla)? Does the loss surface violate the smooth parameterization assumed?
- Does joint (N, D, k) optimization interact with model architecture choices (depth vs. width, MoE vs. dense)?

**Broader significance:** T² represents the formal unification of pretraining scaling laws with test-time scaling — two threads that have developed in parallel since 2020. It implies that the entire industry's compute allocation strategy should be reconsidered under any deployment scenario involving repeated or multi-sample inference, which includes virtually all production LLM deployments in 2026. The paper sets up a new optimization problem that will drive future scaling law research and hardware planning.

---

## Benchmark Data

```json
[
  {
    "benchmark": "Long Range Arena — ListOps",
    "scale": "sequence length T=512",
    "results": [
      {"model": "Hierarchical Kernel Transformer (HKT)", "score": 55.10, "unit": "accuracy %"},
      {"model": "Standard Attention (baseline)", "score": 50.33, "unit": "accuracy %"}
    ],
    "notes": "HKT at 1.31x compute overhead; improvement of +4.77pp"
  },
  {
    "benchmark": "Sequential CIFAR-10",
    "scale": "sequence length T=1024",
    "results": [
      {"model": "Hierarchical Kernel Transformer (HKT)", "score": 35.45, "unit": "accuracy %"},
      {"model": "Standard Attention (baseline)", "score": 34.01, "unit": "accuracy %"}
    ],
    "notes": "+1.44pp over baseline"
  },
  {
    "benchmark": "IMDB Sentiment (character-level)",
    "scale": "sequence length T=1024",
    "results": [
      {"model": "Hierarchical Kernel Transformer (HKT)", "score": 70.19, "unit": "accuracy %"},
      {"model": "Standard Attention (baseline)", "score": 62.72, "unit": "accuracy %"}
    ],
    "notes": "+7.47pp improvement — largest gain among LRA tasks"
  },
  {
    "benchmark": "SWE-Bench Pro",
    "scale": "coding agent",
    "results": [
      {"model": "Kimi K2.6", "score": 58.6, "unit": "solve rate %"},
      {"model": "GPT-5.4", "score": 57.7, "unit": "solve rate %"}
    ],
    "notes": "Kimi K2.6 is 1T-param MoE with 32B active; released April 20, 2026"
  },
  {
    "benchmark": "Humanity's Last Exam (with tools)",
    "scale": "frontier reasoning",
    "results": [
      {"model": "Kimi K2.6", "score": 54.0, "unit": "accuracy %"}
    ],
    "notes": "Leading score among compared models as of release date"
  },
  {
    "benchmark": "AIME 2026",
    "scale": "math competition",
    "results": [
      {"model": "Kimi K2.6", "score": 96.4, "unit": "accuracy %"},
      {"model": "Gemma 4 31B", "score": 89.2, "unit": "accuracy %"}
    ],
    "notes": "Gemma 4 released April 2, 2026; Kimi K2.6 released April 20, 2026"
  },
  {
    "benchmark": "GPQA-Diamond",
    "scale": "graduate-level science",
    "results": [
      {"model": "Kimi K2.6", "score": 90.5, "unit": "accuracy %"},
      {"model": "Gemma 4 31B", "score": 84.3, "unit": "accuracy %"}
    ],
    "notes": "Both models open-weight"
  },
  {
    "benchmark": "LiveCodeBench v6",
    "scale": "coding",
    "results": [
      {"model": "Kimi K2.6", "score": 89.6, "unit": "accuracy %"},
      {"model": "Gemma 4 31B", "score": 80.0, "unit": "accuracy %"}
    ],
    "notes": ""
  },
  {
    "benchmark": "Tau2 Agentic Tool Use",
    "scale": "tool-use / agents",
    "results": [
      {"model": "Gemma 4 31B", "score": 76.9, "unit": "accuracy %"}
    ],
    "notes": "Released Apache 2.0"
  },
  {
    "benchmark": "BCR Mathematical Reasoning (token efficiency)",
    "scale": "N=8 concurrent problems, 4B model",
    "results": [
      {"model": "BCR (Batched Contextual RL)", "score": 62.6, "unit": "token reduction %"},
      {"model": "BCR (Batched Contextual RL)", "score": 15.8, "unit": "token reduction % (N=2)"}
    ],
    "notes": "Accuracy maintained or improved on MATH, AMC, AIME, GSM8K; tested on 1.5B and 4B models"
  },
  {
    "benchmark": "Decoupled DiLoCo — Inter-datacenter bandwidth",
    "scale": "8 data centers",
    "results": [
      {"model": "Decoupled DiLoCo", "score": 0.84, "unit": "Gbps required"},
      {"model": "Synchronous Data-Parallel", "score": 198, "unit": "Gbps required"}
    ],
    "notes": "236x bandwidth reduction; 88% goodput under high hardware failure rates"
  },
  {
    "benchmark": "Dataset Scaling Efficiency",
    "scale": "tiny attention-only decoder, arXiv:2604.09389",
    "results": [
      {"model": "Attention-Only Decoder (30% data)", "score": 90.0, "unit": "% of full-data validation accuracy"}
    ],
    "notes": "~30% of training data sufficient to reach 90% of full-data performance"
  },
  {
    "benchmark": "Graph Transformer Distributed Training Speedup",
    "scale": "8 GPUs, arXiv:2604.16715",
    "results": [
      {"model": "Adaptive Parallel Graph Transformer", "score": 6.0, "unit": "x speedup vs single GPU"},
      {"model": "Adaptive Parallel Graph Transformer", "score": 78.0, "unit": "% memory reduction vs baseline"}
    ],
    "notes": "Automatically selects parallelization strategy based on graph structure"
  }
]
```

---

## Architecture / Diagram Notes

### Hierarchical Kernel Transformer (HKT)

```
Nodes: IN[Input Sequence], DS1[Causal Downsample L=1], DS2[Causal Downsample L=2], DS3[Causal Downsample L=3], SA1[Scale-1 Attention], SA2[Scale-2 Attention], SA3[Scale-3 Attention], CW[Learned Convex Weights], AGG[Weighted Aggregate Score Matrix], OUT[Output]
Edges: IN->DS1, IN->DS2, IN->DS3, DS1->SA1, DS2->SA2, DS3->SA3, SA1->CW, SA2->CW, SA3->CW, CW->AGG, AGG->OUT
Labels: IN->DS1: [scale 1 (full res)], IN->DS2: [scale 2 (half res)], IN->DS3: [scale 3 (quarter res)], CW->AGG: [λ₁S₁ + λ₂S₂ + λ₃S₃, Σλᵢ=1], AGG->OUT: [cost ≤ 1.31× standard attn]
Notes: PSD kernel property guaranteed; score matrix decomposes into symmetric (reciprocal) + antisymmetric (directional) components; L=3 levels is default configuration
```

### Value Gradient Flow (VGF) — Optimal Transport RL

```
Nodes: REF[Reference Distribution π_ref], PART[Particle Set {xᵢ}], VNET[Value Network V(x)], GRAD[Value Gradient ∇ₓV(xᵢ)], TRANS[Transport Step xᵢ ← xᵢ + α·∇ₓV(xᵢ)], BUDGET[Transport Budget τ], POLICY[Implicit Policy π*]
Edges: REF->PART, PART->VNET, VNET->GRAD, GRAD->TRANS, BUDGET->TRANS, TRANS->PART (loop until budget exhausted), PART->POLICY
Labels: REF->PART: [sample N particles], TRANS->PART: [repeat τ steps], PART->POLICY: [empirical distribution of transported particles]
Notes: No explicit policy network; regularization implicit via τ; test-time scaling = increase τ; unifies offline RL (π_ref = dataset) and RLHF (π_ref = base LLM)
```

### Decoupled DiLoCo — Distributed Training Architecture

```
Nodes: DC1[Data Center 1 (Island 1)], DC2[Data Center 2 (Island 2)], DC3[Data Center N (Island N)], PS[Async Parameter Server], INNER[Inner Optimizer: AdamW], OUTER[Outer Optimizer: Nesterov Momentum], CKPT[Checkpoint Store]
Edges: DC1->INNER, DC2->INNER, DC3->INNER, INNER->DC1 (loop: local steps H), INNER->DC2 (loop: local steps H), INNER->DC3 (loop: local steps H), DC1->PS, DC2->PS, DC3->PS, PS->OUTER, OUTER->PS, PS->CKPT
Labels: DC1->PS: [push Δθ = θ_start - θ_end (pseudo-gradient), async], PS->OUTER: [merge pseudo-gradients from all islands], OUTER->PS: [update global model θ_global], PS->DC1: [pull updated θ_global before next round], DC1->INNER: [run H local steps]
Notes: Bandwidth = 0.84 Gbps inter-DC (vs 198 Gbps for sync data-parallel); goodput 88% under failures; built on Pathways async runtime
```

### Train-to-Test (T²) Scaling — Joint Optimization

```
Nodes: BUDGET[Fixed Total Budget C_total], TRAIN[Training Compute C_train = 6ND], INFER[Inference Compute k·2N·L_gen], MODEL[Model Size N], DATA[Training Tokens D], SAMPLES[Inference Samples k], LOSS[Pretraining Loss L(N,D)], ACC[Task Accuracy Acc(N,D,k)], OPT[Joint Optimum (N*,D*,k*)]
Edges: BUDGET->TRAIN, BUDGET->INFER, TRAIN->MODEL, TRAIN->DATA, INFER->SAMPLES, MODEL->LOSS, DATA->LOSS, LOSS->ACC, SAMPLES->ACC, ACC->OPT
Labels: TRAIN->MODEL: [N* ≪ N*_Chinchilla], TRAIN->DATA: [D* ≫ D*_Chinchilla], ACC->OPT: [minimize C_total s.t. Acc ≥ target]
Notes: T²-NLL fits L(N,D); T²-Acc fits Acc(N,D,k) directly; both validated on 8 downstream tasks; result holds through SFT/RLHF post-training
```

### Batched Contextual Reinforcement (BCR)

```
Nodes: PROBS[N Problems {P₁,...,Pₙ}], CTX[Shared Context Window], LLM[Language Model], SOLS[Interleaved Solutions {S₁,...,Sₙ}], REWARD[Per-Instance Accuracy Reward], RL[RL Update (GRPO/PPO)], EMERGE[Emergent: Eliminate Redundant CoT]
Edges: PROBS->CTX, CTX->LLM, LLM->SOLS, SOLS->REWARD, REWARD->RL, RL->LLM (training loop), LLM->EMERGE
Labels: CTX->LLM: [all N problems in one forward pass], SOLS->REWARD: [score each Sᵢ independently], RL->LLM: [reinforce token-efficient correct solutions], EMERGE: [power-law: tokens/problem ∝ N^{-α}]
Notes: No explicit length penalty; 62.6% token reduction at N=8; 1.5B and 4B models tested; circumvents adversarial gradients of explicit penalties
```

---

## Analysis & Impact for ML Researchers

- **Revisit your pretraining compute allocation immediately.** The T² scaling laws (arXiv:2604.01411) show that Chinchilla-optimal training is suboptimal whenever you use multi-sample inference (best-of-k, chain-of-thought, beam search). The formal framework gives you a recipe: estimate your production k (number of inference samples per query), your inference budget fraction, and use T²-Acc to find the jointly optimal (N, D) pair. For most production settings with k≥4, the optimal model is 2–4× smaller but trained 2–4× longer than Chinchilla prescribes.

- **Consider VGF as a drop-in alternative to PPO/DPO for fine-tuning large generative models.** Value Gradient Flow (arXiv:2604.14265) eliminates the need for an explicit policy parameterization that is distinct from the base model, which is the core engineering pain point when applying RLHF to 70B+ models. The optimal transport framing also provides cleaner theoretical guarantees than policy gradient methods. The test-time scaling knob (adjustable transport budget) is especially valuable for inference-time alignment.

- **Monitor the Polar Express / Muon optimizer results carefully.** The ICLR 2026 Honorable Mention (OpenReview:yRtgZ1K8hO) shows consistent GPT-2 training loss improvements over Adam/Nesterov/Shampoo with a theoretically grounded, GPU-native optimizer. Muon-family optimizers are gaining empirical momentum alongside Shampoo for large-scale training; the Polar Express paper provides the missing theoretical foundation (optimal polynomial approximation of polar decomposition) that may make these optimizers more trustworthy for production use.

- **BCR's task-scaling law suggests a practical route to 2–5× inference throughput without accuracy loss.** For teams deploying reasoning models (math, coding, science QA), training with BCR (arXiv:2604.02322) and then batching N=4–8 problems per forward pass at inference time can yield substantial cost savings. The key engineering requirement is a context window large enough to fit N complete problem+solution pairs — a constraint that 128K+ context models easily satisfy. The "free lunch" window appears widest for mathematical reasoning tasks.

- **Decoupled DiLoCo (github.com/google-deepmind/asyncdiloco) makes inter-datacenter training viable without bespoke networking.** For organizations with compute spread across multiple cloud regions or co-lo facilities, the 236× bandwidth reduction means you can train large models across geographically distributed fleets using standard 1–10 Gbps internet connections. The 88% goodput under high failure rates is the more practically important number — it means training runs are no longer brittle to individual hardware failures in any island.

---

## Key Takeaways (TL;DR)

- **T² scaling laws prove Chinchilla is wrong whenever inference sampling is used** — the jointly optimal pretraining point is 2–4× smaller models trained on 2–4× more tokens, with k>1 inference samples compensating.
- **ICLR 2026's top paper formalizes that transformers are exponentially more succinct than automata**, but this very expressivity makes transformer property verification EXPSPACE-complete — a new formal barrier for AI safety.
- **Value Gradient Flow (VGF) unifies offline RL and RLHF as optimal transport**, eliminating explicit policy parameterization and enabling adaptive test-time scaling via transport budget control.
- **Decoupled DiLoCo reduces inter-datacenter training bandwidth 236× (198 Gbps → 0.84 Gbps)**, achieving 88% goodput under high hardware failure rates — internet-connected multi-datacenter LLM training is now practical.
- **Batched Contextual Reinforcement achieves 62.6% token reduction on 4B reasoning models** (N=8 concurrent problems) with maintained accuracy — a throughput multiplier requiring no inference-time changes beyond batching.
- **The Polar Express algorithm provides theoretically optimal GPU-native matrix polar decomposition**, improving Muon optimizer validation loss on GPT-2 training runs of 1–10B tokens across all tested learning rates.
- **ICLR 2026 Workshops conclude today (April 27)** in Rio de Janeiro, with outstanding papers spanning expressivity theory, optimizer math, and multi-turn LLM evaluation — the field is increasingly formalizing intuitions about transformer capabilities.
- **Kimi K2.6 (1T-param MoE, 32B active) leads SWE-Bench Pro at 58.6%** and scores 96.4% on AIME 2026, demonstrating that open-weight models now match or exceed closed frontier models on competitive benchmarks.
