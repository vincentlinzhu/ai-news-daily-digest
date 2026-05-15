# Machine Learning Research — 2026-05-15

> **Note:** ICML 2026 acceptance notifications were released in early May 2026 (conference scheduled July 6-11, 2026 in Seoul, South Korea). No outstanding paper awards announced yet — those typically land at the conference itself. CVPR 2026 and prior ICML 2026 accepted papers are now appearing on arXiv. No major conference happening today; arXiv cross-listing day brings the week's batch.

---

## Top Stories (5)

### 1. G-Zero: Verifier-Free Self-Play Enables LLM Self-Improvement on Open-Ended Tasks — First provably-grounded framework for autonomous LLM improvement without external judges

**Source:** [arXiv 2605.09959](https://arxiv.org/abs/2605.09959) | [GitHub](https://github.com/Chengsong-Huang/G-Zero)

G-Zero introduces a co-evolutionary framework where a large language model autonomously improves itself on open-ended generation tasks without requiring any external verifier, ground-truth labels, or LLM-as-judge. Prior self-improvement methods (RLVR, STaR, etc.) work well on verifiable domains like mathematics or code—where correctness can be checked mechanically—but collapse on creative writing, summarization, and open-ended QA where no ground truth exists. G-Zero breaks this barrier with a novel intrinsic reward signal called **Hint-δ**.

The framework operates through a three-phase cycle. A **Proposer** model (trained via GRPO) generates challenging queries paired with informative hints that target the Generator's demonstrated blind spots. For each query-hint pair, an unassisted response is sampled and compared to a hint-conditioned response; the predictive shift δ between the two serves as the reward signal—no judge needed. The **Generator** is then trained via DPO to internalize these hint-induced improvements so that at test time it can produce better responses without any hint. The Proposer and Generator co-evolve, with the Proposer dynamically targeting harder and harder gaps.

The key theoretical result is a best-iterate suboptimality guarantee for an idealized DPO variant of G-Zero, provided the Proposer achieves sufficient exploration coverage and data filtration keeps pseudo-label noise low. This is the first provable guarantee for open-domain LLM self-improvement that does not rely on an external oracle. Empirically, G-Zero avoids the reward hacking and capability ceiling that plague LLM-as-judge setups—since the Proposer cannot "fool" a static external judge, it must find genuinely exploitable gaps.

**Key technical details:**
- Training signal: Hint-δ = KL divergence between p(response | query) and p(response | query, hint)
- Challenger phase uses GRPO for Proposer; Generator optimized via DPO
- No external verifiers, LLM judges, or majority-vote pseudo-labels required
- Theoretical guarantee: best-iterate suboptimality under coverage + noise assumptions
- Addresses "open-ended generation" domain where SFT and RLVR both fail
- Related: R-Zero (self-evolving reasoning), Trans-Zero (multilingual self-play without parallel data)

---

### 2. Parcae: Looped Language Models Match 1.3B Transformers with 770M Parameters — Stable architecture + first scaling laws for looped LMs enable a new compute-optimal training paradigm

**Source:** [arXiv 2604.12946](https://arxiv.org/abs/2604.12946) | [Sandy Research Lab](https://sandyresearch.github.io/parcae/) | [Together AI Blog](https://www.together.ai/blog/parcae)

Looped language models—where the same transformer block is applied multiple times before producing output—have long been theoretically appealing: they decouple parameter count from compute, allowing models to think harder without growing bigger. The problem has always been training instability (residual explosion, loss spikes). Parcae (named after the Roman Fates) solves this by mathematically analyzing looping as a nonlinear time-variant dynamical system over the residual stream and pinpointing instability to large spectral norms in the "injection parameters" that re-enter activations each loop.

The fix is elegant: constrain the spectral norm of injection parameters by discretizing a negative diagonal parameterization. This keeps the residual stream bounded across an arbitrary number of loops. With stability solved, the authors then derive the first scaling laws for looped models, finding that compute-optimal training requires increasing loop count and data in tandem for a fixed FLOP budget. At test time, looped models scale predictably following a saturating exponential decay—meaning practitioners can buy more quality simply by running more loops without retraining.

The empirical results are striking: a 770M-parameter Parcae matches a 1.3B-parameter standard Transformer trained on the same data. At the 1.3B scale, Parcae outperforms the Transformer baseline by 2.99 points on CORE and 1.18 points on Core-Extended benchmarks, while achieving 6.3% lower validation perplexity than prior large-scale looped models. This is a fundamentally different approach to the compute-quality frontier: instead of scaling model size, scale loops.

**Key technical details:**
- Architecture: single shared transformer block looped N times; token injection at each loop entry
- Instability root cause: large spectral norms in injection parameters → residual explosion
- Fix: discretize negative diagonal parameterization to constrain spectral norm
- Scaling law: optimal FLOP budget allocation requires joint scaling of loops + data
- 770M Parcae ≈ 1.3B Transformer on identical data/compute
- Test-time compute scaling follows saturating exponential decay, predictably
- CORE benchmark: +2.99 pts over Transformer baseline at 1.3B params
- Validation perplexity: 6.3% improvement over prior looped model SOTA

---

### 3. D-VLA: Linear Speedup for Trillion-Parameter Vision-Language-Action RL Training — Distributed asynchronous RL framework breaks the simulation-optimization bottleneck for embodied AI

**Source:** [arXiv 2605.13276](https://arxiv.org/abs/2605.13276)

Training large Vision-Language-Action (VLA) models with reinforcement learning faces a critical resource conflict: high-fidelity physics simulation is CPU-memory intensive and runs at its own frequency, while deep learning optimization requires GPU-VRAM at a different cadence. Current frameworks serialize these two workloads, creating massive idle time and making trillion-parameter VLA training effectively impractical. D-VLA (Distributed Vision-Language-Action) eliminates this bottleneck through three coordinated innovations.

**Plane Decoupling** physically isolates the simulation plane from the optimization plane: high-frequency environment sampling runs on separate nodes from gradient computation, with a shared parameter server handling weight distribution. A **Swimlane Pipeline** introduces a four-thread asynchronous architecture that fully overlaps sampling, inference, gradient accumulation, and parameter broadcast—meaning no thread waits for another. Finally, **VRAM Management** via a dual-pool model and topology-aware replication prevents memory fragmentation that typically plagues large-scale distributed training.

The result is linear speedup with respect to the number of nodes, demonstrated empirically up to trillion-parameter scale. On the LIBERO benchmark for robotic manipulation, D-VLA significantly outperforms mainstream RL frameworks in throughput and sampling efficiency for billion-parameter VLAs. This is especially consequential because VLA models are increasingly the path to generalizable dexterous robotics—training them via RL (which requires environment interaction) has been the bottleneck separating current demos from real capabilities.

**Key technical details:**
- Architecture: Plane Decoupling (sim-plane / opt-plane) + Swimlane Pipeline (4-thread async) + VRAM dual-pool
- Speedup: linear with node count; demonstrated at trillion-parameter scale
- Benchmark: LIBERO (robotic manipulation); outperforms mainstream RL frameworks in throughput
- Related work: RLinf-VLA achieves 20-85% performance improvement across benchmarks; SimpleVLA-RL outperforms SFT baselines
- Application domain: embodied AI / dexterous robotics foundation models
- Key constraint solved: eliminates idle time from serialized simulation + gradient computation

---

### 4. InfoLaw: Principled Scaling Laws for Quality-Weighted Data Mixtures Under Repetition — Framework predicts pretraining loss with 0.15% mean error across unseen data recipes

**Source:** [arXiv 2605.02364](https://arxiv.org/abs/2605.02364) | [Cool Papers](https://papers.cool/arxiv/2605.02364)

The standard Chinchilla scaling law tells practitioners how many tokens to train on for a given compute budget, but it silently assumes homogeneous data quality and no repetition. Real pretraining uses curated mixtures of web text, code, books, and scientific papers—each with different quality levels—and many practitioners upsample scarce high-quality data until it repeats. InfoLaw is the first scaling framework that explicitly models all three variables: quality weights, mixture proportions, and repetition levels, unified under an information accumulation view of pretraining.

The core insight is to model pretraining as accumulating information from a mixture of sources, where quality modulates information density and repetition introduces scale-dependent diminishing returns. InfoLaw derives a closed-form loss predictor as a function of: consumed tokens, model size, per-source quality weights, and repetition levels. The framework was validated across 7B-parameter models trained on up to 425 billion tokens, predicting performance on held-out data recipes and extrapolating to new compute scales.

Prediction accuracy is exceptional: 0.15% mean absolute error and 0.96% maximum absolute error in loss across all held-out configurations. This is practically useful: instead of running expensive ablations to find optimal data mixtures, teams can query the InfoLaw predictor to identify the best recipe for their compute budget in minutes. The framework also explains the empirical observation that upweighting quality helps up to a point—beyond a certain repetition level, the marginal information gain from repeating a high-quality document falls below that of adding a generic document.

**Key technical details:**
- Model: loss = f(tokens, params, quality_weights, repetition_levels) via information accumulation
- Validation: up to 7B parameters, 425B tokens
- Mean absolute error in loss prediction: 0.15%; max error: 0.96%
- Reliable extrapolation across overtraining levels (key gap vs. prior scaling laws)
- Submitted to ICML 2026
- Related: LayerMix Law (OpenReview), Scaling Laws for Mixture Pretraining Under Data Constraints (arXiv 2605.12715)

---

### 5. PFlowNet (ICML 2026): Variational RL Fixes Vision-Language Model Hallucinations — Decoupling perception from reasoning via geometric reward shaping sets new SOTA on visual grounding benchmarks

**Source:** [arXiv 2605.02730](https://arxiv.org/abs/2605.02730) | [HuggingFace Papers](https://huggingface.co/papers/2605.02730) | ICML 2026 Accepted

PFlowNet (Perceptual Flow Network) tackles one of the most persistent failure modes in deployed multimodal systems: Large Vision-Language Models (LVLMs) hallucinate visual details because standard MLE training doesn't adequately constrain visual trajectories. Existing fixes try to inject geometric priors from visual expert models (detectors, segmenters), but the paper's preliminary study reveals a counterintuitive finding: the most geometrically precise expert annotations are *not* the most helpful for visual reasoning. Optimizing for geometric precision creates a "tunnel vision effect"—the model becomes overly focused on detected objects and loses broader scene reasoning capability.

PFlowNet solves this through a self-conditioned generation process that uses variational reinforcement learning to integrate multi-dimensional rewards with vicinal geometric shaping. Rather than rigidly aligning to expert priors, it learns to identify which geometric signals are reasoning-relevant vs. reasoning-harmful for each specific query. The decoupling of perception (where to look) from reasoning (what to conclude) is the key architectural innovation. The framework comes with provable performance guarantees derived from the VRL objective.

**Key technical details:**
- Problem: LVLM hallucination from MLE + expert geometric prior misalignment
- Innovation: Self-conditioned generation + variational RL with multi-dim rewards
- Finding: Geometrically precise expert annotations hurt reasoning (tunnel vision effect)
- V* Bench: 90.6% (new SOTA)
- MME-RealWorld-lite: 67.0% (new SOTA)
- Accepted ICML 2026 (23,918 submissions → 6,352 accepted; 26.6% acceptance rate)

---

## Deep Dive: Most Important Item

### G-Zero: The First Verifier-Free Self-Play Framework with Provable Self-Improvement Guarantees

**Why this matters most:** Every prior LLM self-improvement method requires either (a) external verifiers (code execution, math checkers), (b) human labels, or (c) LLM-as-judge—each with fundamental ceiling problems. G-Zero breaks this with a framework that works on *any* generation task, has provable convergence properties, and is fully self-contained. If it scales, it represents a path to LLM self-improvement that doesn't bottleneck on humans or task-specific verifiers.

**The core problem in depth:** RLVR (RL from Verifiable Rewards) has driven much of the recent reasoning improvement in models like o1, DeepSeek-R1, and QwQ. But RLVR requires a reward function that can judge correctness—possible for math, code, and formal logic, but not for the majority of natural language tasks. LLM-as-judge methods introduce a new ceiling: the judge's quality bounds the model's quality, reward hacking is rampant, and stronger judges cost more at inference time. G-Zero sidesteps both.

**Hint-δ as intrinsic reward:** The key insight is that *how much an LLM's response changes when given a hint* directly measures the magnitude of its blind spot. Formally:

```
δ(q, h) = D_KL[ p(y | q, h) || p(y | q) ]
```

where q is the query, h is the hint, and y is the response. A large δ means the hint revealed something the model didn't know—that's a genuine gap, and the reward signal is proportional to it. No external judge needed; the model's own distribution shift *is* the signal.

**Challenger-Generator co-evolution:** The Proposer is trained with GRPO to maximize E[δ(q, h)] over the Generator's current distribution—it learns to find the queries where the Generator is most ignorant. For each (q, h, δ) tuple above a threshold, a DPO pair is constructed: the unassisted response y⁻ and the hint-conditioned response y⁺. The Generator is then trained via DPO to make y⁻ as good as y⁺—i.e., to internalize the hint. This alternates: a better Generator forces the Proposer to find harder blind spots, driving continuous improvement.

**Theoretical guarantee:** The paper proves that for an idealized standard-DPO variant, the best-iterate solution achieves suboptimality bounded by:

```
ε_best ≤ O(σ_noise / √T_DPO + 1/√|D_challenge|)
```

where σ_noise is pseudo-label score noise (controlled by filtration), T_DPO is DPO training steps, and |D_challenge| is the challenge dataset size. As long as the Proposer achieves ε-coverage of the Generator's gap distribution (i.e., explores broadly enough), and filtration keeps σ_noise small, the Generator is guaranteed to improve.

**Open questions:**
- Does Hint-δ as reward remain well-calibrated as the Generator approaches the Proposer's capability level? (Chicken-and-egg collapse risk)
- How does this scale empirically to 70B+ parameter models and long-context tasks?
- Can the same framework apply to multimodal generation (image + text) where hints could be visual patches?
- What is the empirical verification that the Proposer achieves sufficient coverage in practice?
- The guarantee is for the "idealized" DPO variant—does it hold for the practical GRPO-DPO mixed implementation?

**Broader significance:** This sits at the intersection of two major arcs in ML research: (1) the push toward self-improving AI systems that don't require constant human feedback, and (2) the recognition that most real-world tasks are not verifiable. G-Zero is the first framework to make progress on both simultaneously with theoretical backing. Combined with growing compute budgets for inference-time scaling, this could enable LLMs to improve continuously on deployed tasks without any labeling infrastructure—with implications across customer service, creative writing, education, and scientific reasoning.

---

## Benchmark Data

```json
[
  {
    "benchmark": "V* Bench (Visual Grounding)",
    "scale": "Large Vision-Language Model",
    "results": [
      {"model": "PFlowNet (ICML 2026)", "score": 90.6, "unit": "%"},
      {"model": "Prior SOTA (LVLM with expert priors)", "score": null, "unit": "% (not disclosed; PFlowNet claims new SOTA)"}
    ],
    "notes": "PFlowNet accepted to ICML 2026; variational RL with multi-dim rewards + geometric shaping"
  },
  {
    "benchmark": "MME-RealWorld-lite",
    "scale": "Large Vision-Language Model",
    "results": [
      {"model": "PFlowNet (ICML 2026)", "score": 67.0, "unit": "%"}
    ],
    "notes": "New SOTA; decouples perception from reasoning"
  },
  {
    "benchmark": "CORE benchmark (language model quality)",
    "scale": "1.3B parameters",
    "results": [
      {"model": "Parcae (looped LM)", "score": 2.99, "unit": "points over Transformer baseline"},
      {"model": "Standard Transformer", "score": 0.0, "unit": "points (baseline)"}
    ],
    "notes": "Parcae 770M also matches 1.3B Transformer; looping increases effective compute without adding parameters"
  },
  {
    "benchmark": "Core-Extended benchmark",
    "scale": "1.3B parameters",
    "results": [
      {"model": "Parcae (looped LM)", "score": 1.18, "unit": "points over Transformer baseline"}
    ],
    "notes": "arXiv 2604.12946; Sandy Research + Together AI"
  },
  {
    "benchmark": "Validation Perplexity",
    "scale": "Large-scale looped models",
    "results": [
      {"model": "Parcae", "score": -6.3, "unit": "% vs. prior SOTA looped models (lower is better)"}
    ],
    "notes": "Spectral norm constraint on injection params eliminates residual explosion"
  },
  {
    "benchmark": "InfoLaw Loss Prediction Accuracy",
    "scale": "Up to 7B params, 425B tokens",
    "results": [
      {"model": "InfoLaw", "score": 0.15, "unit": "% mean absolute error in loss"},
      {"model": "InfoLaw", "score": 0.96, "unit": "% maximum absolute error in loss"}
    ],
    "notes": "arXiv 2605.02364; across unseen data recipes and overtraining levels"
  },
  {
    "benchmark": "LIBERO (robotic manipulation throughput)",
    "scale": "Billion-parameter VLA models",
    "results": [
      {"model": "D-VLA", "score": null, "unit": "linear speedup with nodes (vs. sublinear for baselines)"}
    ],
    "notes": "arXiv 2605.13276; D-VLA maintains linear node-scaling at trillion-parameter scale"
  },
  {
    "benchmark": "LongMemEval-S",
    "scale": "MCP agent memory layer",
    "results": [
      {"model": "Lumetra Engram (GA, May 14 2026)", "score": 91.6, "unit": "% (458/500)"}
    ],
    "notes": "MCP-native memory with BM25 + semantic + knowledge-graph fusion; not an ML research paper but directly relevant to deployed agent systems"
  },
  {
    "benchmark": "ICML 2026 Acceptance Statistics",
    "scale": "Conference-wide",
    "results": [
      {"model": "Acceptance rate", "score": 26.6, "unit": "%"},
      {"model": "Spotlight rate", "score": 2.2, "unit": "%"},
      {"model": "Total submissions", "score": 23918, "unit": "papers"},
      {"model": "Total accepted", "score": 6352, "unit": "papers"}
    ],
    "notes": "ICML 2026, Seoul, July 6-11 2026"
  },
  {
    "benchmark": "BFCL v3 (tool-use accuracy)",
    "scale": "Qwen2.5-Instruct-14B",
    "results": [
      {"model": "Base Qwen2.5-Instruct-14B", "score": 56.5, "unit": "%"},
      {"model": "COVERT-RL (synthetic tool-use data)", "score": 59.9, "unit": "%"}
    ],
    "notes": "arXiv 2604.09813; oracle-preserving synthetic data pipeline for tool-use RL"
  },
  {
    "benchmark": "Mixture Pretraining Repetition Tolerance",
    "scale": "Scarce target data corpora",
    "results": [
      {"model": "Prior accepted ceiling (single-source)", "score": 4, "unit": "repetitions"},
      {"model": "Mixture training (arXiv 2605.12715)", "score": 17.5, "unit": "repetitions (15-20 range)"}
    ],
    "notes": "Mixture training with abundant generic data tolerates 15-20x repetition of scarce target data"
  }
]
```

---

## Architecture / Diagram Notes

### G-Zero: Challenger-Generator Co-Evolution

```
Nodes:
  P[Proposer (GRPO-trained)]
  G[Generator (DPO-trained)]
  QH[Query-Hint Pairs (q, h)]
  D[Hint-δ Signal = KL(p(y|q,h) || p(y|q))]
  F[Filtration: keep δ > threshold]
  DPO[DPO Pairs: (q, y⁻_unassisted, y⁺_hint-conditioned)]
  
Edges:
  G→P (Proposer targets Generator's current blind spots)
  P→QH (generates challenging query + hint pairs)
  QH→D (compute δ by sampling both conditional distributions from G)
  D→F (filter: only high-δ pairs are informative)
  F→DPO (construct preference pairs)
  DPO→G (DPO training: Generator learns to match hint-conditioned quality without hint)
  G→P (loop: improved Generator forces Proposer to find new gaps)

Labels:
  G→P: [evaluate current gap distribution]
  P→QH: [GRPO: maximize E[δ]]
  QH→D: [intrinsic reward signal, no external judge]
  DPO→G: [internalize hint knowledge; test-time hint-free]
```

### Parcae: Looped Language Model Architecture

```
Nodes:
  T[Token Embeddings]
  INJ[Injection Parameters (spectral-norm constrained)]
  LOOP[Shared Transformer Block (looped N times)]
  RS[Residual Stream]
  OUT[Output Layer / LM Head]
  
Edges:
  T→INJ (token embeddings enter injection params)
  INJ→RS (inject into residual stream at each loop entry)
  RS→LOOP (pass through shared transformer block)
  LOOP→RS (output back to residual stream)
  RS→INJ (loop back: inject again for next loop iteration, N times)
  RS→OUT (final residual stream → output after N loops)

Labels:
  INJ→RS: [negative diagonal parameterization; spectral norm ≤ ρ]
  LOOP→RS: [same weights every loop; no per-loop parameters]
  RS→INJ: [loop 1..N; test-time: increase N for more compute]
```

### D-VLA: Distributed Async VLA Training

```
Nodes:
  SIM[Simulation Plane (physics envs, high-frequency)]
  ENV[Environment Workers (CPU nodes)]
  SAMP[Sampling Threads (inference)]
  GRAD[Gradient Computation (GPU nodes)]
  PARAM[Parameter Server (topology-aware replication)]
  VRAM[Dual-Pool VRAM Manager]

Edges:
  SIM→ENV (run environment steps asynchronously)
  ENV→SAMP (send observations for inference)
  SAMP→GRAD (send trajectories for gradient computation)
  GRAD→PARAM (push gradients; pull updated weights)
  PARAM→VRAM (distribute weights; dual-pool prevents fragmentation)
  PARAM→SAMP (broadcast updated weights asynchronously)
  SAMP→ENV (send actions back to environment)

Labels:
  SIM→ENV: [Plane Decoupling: sim never blocks opt]
  SAMP/GRAD/PARAM/ENV: [Swimlane Pipeline: 4 threads fully overlapped]
  PARAM→VRAM: [topology-aware: NVLink within node, InfiniBand across]
```

### TIDE: Token Injection at Every Transformer Layer

```
Nodes:
  TOK[Token Index (discrete)]
  EMB[Standard Input Embedding]
  EMEM[EmbeddingMemory (K MemoryBlocks)]
  ROUTER[Depth-Conditioned Softmax Router]
  NULL[Learnable Null Bank]
  L1[Layer 1 (Attn + FFN)]
  L2[Layer 2 (Attn + FFN)]
  LN[Layer N (Attn + FFN)]
  OUT[Output]

Edges:
  TOK→EMB (standard single-shot embedding at input)
  TOK→EMEM (TIDE: also map to EmbeddingMemory; computed once)
  EMEM→ROUTER (K context-free semantic vectors)
  NULL→ROUTER (null bank for opt-out routing)
  ROUTER→L1 (inject token-identity vector at Layer 1)
  ROUTER→L2 (inject at Layer 2)
  ROUTER→LN (inject at Layer N; depth-conditioned routing weight)
  EMB→L1 (standard path)
  L1→L2 (standard residual stream)
  LN→OUT

Labels:
  TOK→EMEM: [computed once, reused at every layer; solves rare token under-training]
  ROUTER→Lx: [depth-conditioned softmax; different injection weight per layer]
  NULL→ROUTER: [opt-out: layer can ignore token identity if contextually redundant]
```

---

## Analysis & Impact for ML Researchers

- **If you are training LLMs on domain-specific or low-resource data:** The Scaling Laws for Mixture Pretraining Under Data Constraints (arXiv 2605.12715) and InfoLaw (arXiv 2605.02364) should be required reading before your next pretraining run. The finding that scarce target corpora can be safely repeated 15-20× in a mixture (vs. the prior 4× ceiling) means you may have much more flexibility in your data recipe than you assumed. InfoLaw's 0.15% loss prediction accuracy means you can now select optimal data mixtures via the predictor rather than running expensive ablations—read the InfoLaw paper and check if their code is available before your next recipe sweep.

- **If you are building or fine-tuning embodied / robotics models:** D-VLA (arXiv 2605.13276) directly solves the infrastructure bottleneck for VLA reinforcement learning. If your current pipeline serializes environment simulation and gradient computation, you are leaving throughput on the table. The four-thread Swimlane Pipeline and Plane Decoupling architecture are implementable on existing hardware—review the paper's system design section before your next large-scale VLA run. The concurrent RLinf-VLA (arXiv 2510.06710) also reports 20-85% performance improvements across benchmarks with unified RL training.

- **If you work on self-supervised or self-improving systems:** G-Zero (arXiv 2605.09959) is the most important theoretical advance this week. The Hint-δ intrinsic reward opens up RL-based self-improvement to arbitrary generation tasks beyond math/code. Read the theoretical section carefully—the coverage + noise conditions on the guarantee are non-trivial and understanding them will help you assess whether your domain satisfies them. If you are working on RLVR for a verifiable domain, this is still a directional pointer toward where self-improvement research is heading.

- **If you are interested in efficient architectures:** Parcae (arXiv 2604.12946) demonstrates that looped models can achieve the quality of models nearly 2× their parameter count. The spectral norm constraint is a simple fix (negative diagonal reparameterization), and the scaling laws give you a principled compute budget allocation. The Together AI blog post has practical details on training setup. If you have a compute-constrained deployment environment (edge, mobile), looped models are now a serious alternative to distillation.

- **If you work on multimodal or vision-language systems:** PFlowNet's key finding—that the most geometrically precise expert annotations hurt reasoning via "tunnel vision effect"—has immediate implications for how you should use object detection and segmentation models as teaching signal for LVLMs. Before blindly upcycling DINO/SAM annotations as VRL supervision, read PFlowNet (arXiv 2605.02730) and consider whether vicinal shaping + reward mixing might be a better route than strict geometric alignment.

---

## Key Takeaways (TL;DR)

- **G-Zero (arXiv 2605.09959) enables verifier-free LLM self-improvement on open-ended tasks** using Hint-δ, a provably grounded intrinsic reward with no external judge required.
- **Parcae (arXiv 2604.12946) achieves 1.3B Transformer quality with a 770M looped model**, with the first stable looped-LM scaling laws enabling principled test-time compute scaling.
- **D-VLA (arXiv 2605.13276) achieves linear node-scaling for trillion-parameter VLA reinforcement learning**, eliminating the simulation-optimization bottleneck in embodied AI training.
- **InfoLaw (arXiv 2605.02364) predicts pretraining loss with 0.15% mean error across unseen data recipes**, making data mixture selection practical without costly ablations.
- **Scarce target data can be safely repeated 15-20× in mixture pretraining (vs. the 4× prior ceiling)**, per Scaling Laws for Mixture Pretraining Under Data Constraints (arXiv 2605.12715).
- **ICML 2026 accepted 6,352 papers from 23,918 submissions** (26.6% acceptance rate); conference runs July 6-11 in Seoul—no outstanding paper awards yet.
- **PFlowNet sets new SOTA at 90.6% on V* Bench and 67.0% on MME-RealWorld-lite** (ICML 2026), proving that decoupling perception from reasoning via variational RL beats rigid geometric alignment.
- **Lumetra Engram (GA May 14)** scores 91.6% on LongMemEval-S out-of-the-box as an MCP-native memory layer, fusing BM25 + semantic + knowledge-graph retrieval for deployed agents.
