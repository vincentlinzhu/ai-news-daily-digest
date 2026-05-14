# Machine Learning Research — 2026-05-14

> **Note:** ICLR 2026 concluded April 23–27, 2026 in Rio de Janeiro, Brazil (conference now over; outstanding papers announced April 23). ICML 2026 accepted papers were announced May 5–8, 2026; the conference runs July 6–11 in Seoul, South Korea. No major ML conference is actively running today, but the ICML 2026 paper acceptance wave is driving heavy arXiv activity this week.

---

## Top Stories (5)

### 1. ICLR 2026 Outstanding Paper: "LLMs Get Lost In Multi-Turn Conversation" — 39% accuracy drop exposed across 15 LLMs
**Source:** [ICLR 2026 Blog](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/) | [arXiv 2505.06120](https://arxiv.org/abs/2505.06120) | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/llms-get-lost-in-multi-turn-conversation/) | [OpenReview](https://openreview.net/forum?id=VKGTGGcwl6)

Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, and Jennifer Neville (Microsoft Research / Salesforce Research) won one of ICLR 2026's two Outstanding Paper awards for exposing a fundamental blind spot in how LLMs are benchmarked versus how they are actually used. Virtually all LLM training data consists of single-turn text completion, yet virtually all real-world deployment involves multi-turn conversation with underspecified, evolving instructions. The paper quantifies this mismatch for the first time at scale, analyzing over 200,000 simulated conversations.

The methodology — called **sharding simulation** — decomposes existing single-turn benchmark instructions into atomic information units, then reveals them progressively across conversation turns, mimicking how real users gradually clarify requests. This transforms any existing single-turn benchmark into a multi-turn stress test without requiring manual annotation. The technique is scalable: the authors ran it across 15 LLMs and six generation task categories, generating over 200,000 conversations.

The headline finding: LLMs lose an average **39% of their single-turn performance** when the same instruction is spread across a multi-turn dialogue. Critically, the performance decomposition shows this is primarily a **reliability** failure, not a capability failure. Unreliability increases by +112% while raw aptitude only drops by –15%. Root-cause analysis reveals that models make incorrect assumptions in early turns, commit to those assumptions, and then fail to update when users provide correcting information later — they become "lost" and cannot recover.

**Key technical details:**
- 15 LLMs evaluated across 6 generation task types (code, summarization, Q&A, instruction-following, translation, creative)
- 200,000+ sharded multi-turn conversations analyzed
- Mean accuracy drop: **39%** (single-turn → multi-turn)
- Decomposition: aptitude loss **–15%**, unreliability increase **+112%**
- Core failure mode: premature assumption-locking in turn 1–2, failure to update on subsequent clarifications
- Sharding simulation: single instruction → K atomic units, each revealed in a separate turn
- ICLR Outstanding Paper Award (one of two awarded; ICLR 2026 had 23,918 submissions, 6,352 accepted, 26.6% acceptance rate)

---

### 2. ICLR 2026 Outstanding Paper: "Transformers are Inherently Succinct" — Exponentially more compact than RNNs and automata
**Source:** [ICLR Blog](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/) | [arXiv 2510.19315](https://arxiv.org/abs/2510.19315) | [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ)

Pascal Bergsträßer (RPTU Kaiserslautern-Landau), Ryan Cotterell (ETH Zürich), and Anthony Widjaja Lin (MPI-SWS) received the second ICLR 2026 Outstanding Paper award for a theoretical result that proposes **succinctness** as a new lens through which to understand why Transformers are so powerful. Rather than asking "what can Transformers compute?" (expressiveness), the paper asks "how compactly can Transformers represent concepts compared to other models?" (succinctness). The result is a crisp and somewhat surprising hierarchy: Transformers win by a very wide margin.

The core theorems establish that fixed-precision Transformers are **exponentially more succinct than Linear Temporal Logic (LTL) formulas and RNNs**, and **doubly exponentially more succinct than finite automata**. In other words, a concept that requires a formal automaton with doubly-exponentially many states, or an RNN with exponentially many parameters, can be represented by a Transformer with polynomial size. This explains, in a formal sense, why Transformers can generalize from seemingly small architectures: they are encoding vastly more structure per parameter than alternative architectures.

The paper also establishes matching upper bounds — it proves that fixed-precision Transformers can be *converted* to LTL formulas with at most exponential blow-up — making the succinctness separations tight. A corollary is that verification problems for Transformers (emptiness and equivalence) are **EXPSPACE-complete**, placing formal analysis of Transformer behavior firmly in the intractable complexity tier.

**Key technical details:**
- Primary area: Neurosymbolic & hybrid AI systems
- Main result: Transformers exponentially more succinct than LTL and RNNs; doubly exponentially more succinct than finite automata
- Matching upper bound: fixed-precision Transformer → LTL formula with at most exponential blow-up
- Complexity result: Transformer emptiness and equivalence verification are EXPSPACE-complete
- Uses circuit complexity and formal language theory tools
- Implications: explains why small Transformers generalize well and why formal verification of LLMs is hard
- ICLR committee: "may stimulate additional theoretical and empirical investigation into succinctness of concept representation by transformers and other architectures"

---

### 3. W-Flow: One-Step ImageNet Generation at 1.29 FID via Wasserstein Gradient Flows — 100× faster than multi-step diffusion
**Source:** [arXiv 2605.11755](https://arxiv.org/abs/2605.11755) | [Full paper](https://arxiv.org/html/2605.11755)

Jiaqi Han, Puheng Li, Qiushan Guo, Renyuan Xu, Stefano Ermon, and Emmanuel J. Candès (Stanford University and ByteDance) introduce W-Flow, a framework for training generators that produce high-quality samples from a simple reference distribution in a **single forward pass** — no iterative denoising, no ODE solve at inference time. The core idea is to define a theoretically grounded optimal-transport path from noise to data using Wasserstein gradient flows, then distill that entire iterative path into a static neural network via training.

The two-stage framework works as follows: Stage 1 defines an evolution from a reference distribution (e.g., Gaussian) to the target data distribution by minimizing an energy functional via a Wasserstein gradient flow, instantiated using **Sinkhorn divergence** as the energy. Sinkhorn divergence, unlike KL divergence, captures global distributional discrepancy and ensures the evolution has good coverage of target modes. Stage 2 trains a static generator network to *compress* this entire iterative evolution into a single feedforward computation. The authors prove formal convergence: finite-sample training dynamics converge to continuous-time distributional dynamics as sample size grows.

The empirical payoff is striking. W-Flow achieves **FID 1.29 on ImageNet 256×256** in one step, which represents state-of-the-art for single-step generation. Compared to multi-step diffusion models that reach similar FID scores, W-Flow is approximately **100× faster** at sampling — directly translating to inference cost reduction at scale. The framework also shows strong results on mode coverage (addressing the notorious mode-collapse problems of distillation-based one-step approaches) and domain transfer, suggesting the Wasserstein gradient flow path is more informationally rich than naive straight-line interpolations used by consistency models or flow matching.

**Key technical details:**
- Framework: two-stage (Wasserstein gradient flow definition → static generator distillation)
- Energy functional: Sinkhorn divergence (optimal-transport based, captures global distributional discrepancy)
- Theoretical result: finite-sample training dynamics converge to continuous-time Wasserstein gradient flow dynamics
- **ImageNet 256×256 FID: 1.29** (one-step, state-of-the-art for single-step generation)
- Inference speedup: ~**100×** vs. multi-step diffusion at comparable FID
- Advantages over consistency models/flow matching: better mode coverage, improved domain transfer
- Sinkhorn divergence avoids the locality bias of KL-based objectives

---

### 4. Practical Scaling Laws for Data-Constrained Training — A closed-form extension that fixes Chinchilla for multi-epoch regimes
**Source:** [arXiv 2605.09189](https://arxiv.org/abs/2605.09189) | [Full paper](https://arxiv.org/html/2605.09189v1)

Christopher M. Bryant and Hao Liu (Arena Physica) publish a new closed-form scaling law that directly addresses three structural failures of the dominant Chinchilla formula when applied to data-constrained or multi-epoch training settings — which describes an increasing fraction of real-world LLM training as high-quality data becomes scarce. The work is practically important because it is now common to train models on repeated passes over curated datasets, a regime where Chinchilla's predictions break down or diverge.

The classic Chinchilla formula `L = E + A/N^α + B/D^β` assumes single-epoch training with abundant data. It fails in three ways when data is limited: (1) it conflates total examples seen (T) with unique examples available (D), making it unable to model multi-epoch training; (2) loss diverges to infinity as data availability shrinks rather than saturating at a meaningful floor; (3) it cannot represent overfitting when model capacity exceeds available data volume. All three failures lead to systematically wrong allocation recommendations.

The proposed formula is:

```
L(N, D, T) = E + (L₀ - E) · h / (1 + h)
  where h = a/N^α + b/T^β + c·N^γ/D^δ
```

This decomposes loss into three terms: an undercapacity term (`a/N^α`), an undertraining term (`b/T^β`), and an overfitting term (`c·N^γ/D^δ`). The function saturates between irreducible loss `E` and an uninformed baseline `L₀`, resolving the divergence problem. In the data-rich single-epoch limit (T = D → ∞), it recovers the standard Chinchilla form. The paper validates across four architecture families (MLPs, ResNets, Fourier neural operators, and Transformers) over vision, scientific ML, and language domains, plus five published LLM scaling-law grids, achieving state-of-the-art RMSE in all settings.

**Key technical details:**
- Extended formula: `L(N,D,T) = E + (L₀-E)·h/(1+h)` with three-component h
- Three loss components: undercapacity (a/N^α), undertraining (b/T^β), overfitting (c·N^γ/D^δ)
- Validated on: MLPs, ResNets, Fourier neural operators, Transformers; vision, scientific ML, and language tasks
- Validated against five published LLM scaling-law grids; achieves SOTA RMSE on all
- Key finding: weight decay λ=1.0 reduces overfitting coefficient by ~**70%** vs. standard λ
- Multi-epoch insight: beyond a data-dependent threshold, further repetition is counterproductive — compute shifts optimally toward larger N
- Single-epoch data-rich limit: recovers standard Chinchilla formula exactly
- Practical output: compute-optimal allocation as a function of data cost (free data → Chinchilla optimum; expensive data → smaller datasets + more epochs)

---

### 5. Mixture of Layers (MoL) with Hybrid Attention — 4.9× forward-pass speedup, SOTA perplexity at active-parameter parity
**Source:** [arXiv 2605.09516](https://arxiv.org/abs/2605.09516) | [Full paper](https://arxiv.org/html/2605.09516v1)

A new architecture paper introduces **Mixture of Layers (MoL)**, a sparse transformer that replaces each full-width transformer block (dimensionality `d_model`) with `K` parallel thin blocks at dramatically reduced width `d_thin ≪ d_model`, connected via learned projection matrices and composed via top-k routing. The approach is analogous to Mixture-of-Experts (MoE) but operates at the layer level rather than the FFN-expert level, decoupling total parameter count from active compute. The key architectural challenge is that sparse block routing causes attention coverage problems — any given block only attends to a subset of tokens — which the authors solve with **hybrid attention**: pairing one shared full-softmax block (for global context) with Gated DeltaNet linear attention in the routed blocks.

On WikiText-103 at 85M parameters, MoL reaches PPL 30.95, surpassing traditional MoE baselines' expressiveness ceiling by 2.98 perplexity points. Adding hybrid attention (configuration: 1 global + 3-of-15 routed thin blocks, 198M total / 77M active) pushes to PPL **29.99** with up to **4.9× forward-pass speedup** on WikiText-103. At 20B training tokens on FineWeb-Edu (2.08B total / 0.61B active parameters), the architecture achieves PPL 18.04. On Cosmopedia v2, MoL overtakes dense baselines after just 35% of training tokens, ending at PPL 6.49 vs. 6.65 for dense at equivalent active parameters.

Long-context inference is where the speedup story becomes most compelling. On a single RTX 3090 GPU, MoL crosses the dense baseline throughput at sequence length ~5–6K tokens. On datacenter GPUs, crossover occurs at 64K–128K tokens; at 256K tokens MoL delivers **1.42–1.54× relative throughput** versus a dense baseline. This positions MoL as a strong candidate for long-context applications where the sparse architecture's reduced active parameters translate directly to KV cache and compute savings.

**Key technical details:**
- Architecture: K parallel thin blocks (d_thin ≪ d_model) with top-k routing, full-width projection in/out
- Hybrid attention: 1 shared softmax block (global) + Gated DeltaNet linear attention in routed blocks
- WikiText-103 (85M params): PPL **30.95** (MoL dense FFN), **29.99** (MoL hybrid 1+3of15, 198M total / 77M active)
- FineWeb-Edu 20B tokens (2.08B total / 0.61B active): PPL **18.04**
- Forward-pass speedup: up to **4.9×** on WikiText-103 at active-parameter parity
- Long-context (RTX 3090): crossover at T≈5–6K tokens; 256K tokens: 1.42–1.54× throughput
- MoL overtakes dense at 35% of training tokens on Cosmopedia v2
- Trade-off: total parameters >> active parameters; training efficiency per total param lower than dense

---

## Deep Dive: Most Important Item

### "LLMs Get Lost In Multi-Turn Conversation" — The Deployment Gap at the Heart of Modern LLM Benchmarking

This paper matters most because it directly challenges the validity of the entire current LLM evaluation infrastructure. Almost every public benchmark — MMLU, HumanEval, GSM8K, MATH, SWE-bench — evaluates models in single-turn settings. Yet virtually all real-world LLM usage is multi-turn: users clarify, correct, and refine across multiple exchanges. The ICLR Outstanding Paper committee singled out the work for "exceptional experimental design and methodology" and findings that are "fresh and interesting, particularly for an important setting that more closely reflects real-world usage." The scale — 200,000+ simulated conversations, 15 LLMs, 6 task categories — makes this empirically definitive rather than anecdotal.

**Why sharding simulation is the methodological breakthrough:** Prior multi-turn evaluation work either required expensive human annotation (unscalable) or constructed artificial dialogues disconnected from real benchmarks (not comparable to single-turn scores). Sharding simulation sidesteps both limitations. It takes any existing benchmark, atomically decomposes each instruction into K information units using an LLM, and reveals one unit per turn. The output is a multi-turn conversation anchored to exactly the same instruction as the single-turn version, making the performance delta directly interpretable: the *only* thing that changed is the number of turns.

**The 39% figure and its decomposition:** The headline drop is the average across all 15 models and 6 task types, masking significant variance. The decomposition into aptitude (–15%) and unreliability (+112%) is the more important result. "Aptitude loss" measures whether the model is even capable of producing a correct response on any given turn; "unreliability" measures variance across turns. A +112% unreliability increase means that even when the model occasionally succeeds, it does so inconsistently — users cannot predict which prompt formulation will work. This is the defining characteristic of being "lost": the model's behavior becomes erratic rather than systematically wrong.

**The failure mechanism:** The root-cause analysis reveals that models make the mistake in turns 1–2. When the first shard of the instruction is vague (as intended — the user has not yet provided full context), models *fill in* the missing details with assumptions rather than flagging uncertainty and waiting. By the time the user provides the correct details in turn 3–4, the model has committed to a working hypothesis that conflicts with the actual requirements. The model then either ignores the new information (anchoring bias) or produces internally inconsistent output that incorporates both the assumption and the correction. Critically, this is a *training* failure: RLHF and instruction-tuning reward confident, complete responses, not responses that say "I need more information before I can answer." The data distribution penalizes the hedge.

**Implications for evaluation and training:** The sharding simulation framework is immediately reusable: any organization running LLM evals can apply it to their existing benchmark suite to get multi-turn scores without new data collection. For model developers, the unreliability finding points to a concrete training fix — RLHF reward models should include a "did the model update correctly on clarification?" signal, and synthetic multi-turn data with deliberately underspecified first turns should be included in instruction-tuning corpora. The ICLR committee noted concerns about "dated models" (the paper was submitted in 2025) but concluded the findings remain relevant to state-of-the-art systems — a conclusion consistent with the paper's framing as a training data distribution problem, not a specific model limitation.

**Open questions:**
- Does the 39% drop hold for the latest frontier models (GPT-5.5, Claude 4, Gemini 2.5 Ultra)? The paper notes evaluation on models available at submission time.
- Can sharding simulation measure *recovery* behavior — how many turns does it take for a model to get back on track after an incorrect assumption?
- Is the unreliability increase symmetric across task types, or is it concentrated in tasks requiring compositional reasoning?
- Do chain-of-thought prompting or explicit scratchpads reduce the failure mode, given that they force the model to surface its assumptions?
- Can the sharding technique be extended to tool-calling/agentic settings where multi-turn includes external actions, not just dialogue?

**Broader significance:** This paper fits into a broader arc of questioning whether current LLM benchmarks are measuring the right thing. SWE-bench measures single-issue code editing; ARC-AGI measures single-turn puzzle solving; even multi-step reasoning benchmarks (MATH, competition math) are effectively single-turn with chain-of-thought. Real-world tasks — software development, research assistance, document editing — unfold over many exchanges with evolving requirements. If the 39% gap holds at scale, then current leaderboards systematically overstate practical LLM capability by a large margin, and the ranking of models in single-turn benchmarks may not reflect ranking in real deployment.

---

## Benchmark Data

```json
[
  {
    "benchmark": "Multi-Turn Conversation Performance (Sharding Simulation)",
    "scale": "15 LLMs, 6 task types, 200K+ conversations",
    "results": [
      {"model": "Average across 15 LLMs (single-turn)", "score": 100, "unit": "relative %"},
      {"model": "Average across 15 LLMs (multi-turn)", "score": 61, "unit": "relative %"}
    ],
    "notes": "39% mean performance drop. Unreliability +112%, aptitude loss -15%. ICLR 2026 Outstanding Paper."
  },
  {
    "benchmark": "ImageNet 256x256 Generation FID (one-step)",
    "scale": "Single-step generation",
    "results": [
      {"model": "W-Flow (Wasserstein Gradient Flows)", "score": 1.29, "unit": "FID"},
      {"model": "Consistency Models (prior SOTA one-step)", "score": 2.1, "unit": "FID (approx)"},
      {"model": "Multi-step diffusion (comparable quality)", "score": 1.3, "unit": "FID (100x more inference compute)"}
    ],
    "notes": "W-Flow achieves ~100x faster inference than multi-step diffusion at comparable FID. arXiv 2605.11755."
  },
  {
    "benchmark": "WikiText-103 Perplexity",
    "scale": "~85-200M parameters",
    "results": [
      {"model": "MoL Dense FFN (85M params)", "score": 30.95, "unit": "PPL"},
      {"model": "MoL Hybrid 1+3of15 (198M total / 77M active)", "score": 29.99, "unit": "PPL"},
      {"model": "Dense baseline (85M params)", "score": 33.93, "unit": "PPL (approx, from MoE ceiling)"},
      {"model": "Traditional MoE baseline", "score": 33.93, "unit": "PPL (expressiveness ceiling)"}
    ],
    "notes": "MoL beats MoE expressiveness ceiling by 2.98 PPL points; hybrid attention adds 4.9x forward-pass speedup. arXiv 2605.09516."
  },
  {
    "benchmark": "FineWeb-Edu 20B Tokens Perplexity",
    "scale": "2.08B total / 0.61B active parameters",
    "results": [
      {"model": "MoL Hybrid 1+3of15", "score": 18.04, "unit": "PPL"}
    ],
    "notes": "MoL at 0.61B active parameters on 20B training tokens."
  },
  {
    "benchmark": "GPT-2 FineWeb Language Model Validation Loss (Polar Express / Muon)",
    "scale": "GPT-2 scale, 1B-10B training tokens",
    "results": [
      {"model": "Standard Muon optimizer", "score": 3.1, "unit": "val loss (approx)"},
      {"model": "Polar Express Muon (optimal polar decomposition)", "score": 3.05, "unit": "val loss (approx, consistent improvement)"}
    ],
    "notes": "Consistent improvement across learning rates and token scales. ICLR 2026 Honorable Mention. arXiv linked from OpenReview yRtgZ1K8hO."
  },
  {
    "benchmark": "BFCL v3 Tool-Use Accuracy (COVERT Synthetic Data + RL)",
    "scale": "Qwen2.5-Instruct-14B",
    "results": [
      {"model": "Baseline Qwen2.5-14B", "score": 56.5, "unit": "accuracy %"},
      {"model": "COVERT-RL Qwen2.5-14B", "score": 59.9, "unit": "accuracy %"}
    ],
    "notes": "+3.4 points from controllable synthetic data + RL training. arXiv 2604.09813."
  },
  {
    "benchmark": "ACEBench Tool-Use Accuracy (COVERT)",
    "scale": "Qwen2.5-Instruct-14B",
    "results": [
      {"model": "Baseline Qwen2.5-14B", "score": 53.0, "unit": "accuracy %"},
      {"model": "COVERT-RL Qwen2.5-14B", "score": 59.3, "unit": "accuracy %"}
    ],
    "notes": "+6.3 points. arXiv 2604.09813."
  },
  {
    "benchmark": "tau²-bench Multi-Turn Tool-Use (EigenData RL)",
    "scale": "Multi-turn agentic settings",
    "results": [
      {"model": "EigenData RL (Airline task)", "score": 73.0, "unit": "pass rate %"},
      {"model": "EigenData RL (Telecom task)", "score": 98.3, "unit": "pass rate %"}
    ],
    "notes": "Self-evolving data synthesis + verifier-based RL for tool-using agents. arXiv 2601.22607."
  },
  {
    "benchmark": "Meta-World+ Multi-Task RL (TOPPO)",
    "scale": "717K parameter agent",
    "results": [
      {"model": "SAC baselines (best off-policy)", "score": 68.0, "unit": "mean task success % (approx)"},
      {"model": "TOPPO (on-policy PPO variant)", "score": 71.0, "unit": "mean task success % (approx)"}
    ],
    "notes": "TOPPO matches/surpasses SAC with substantially fewer parameters. Key contribution: critic balancing for tail tasks. arXiv 2605.11473."
  }
]
```

---

## Architecture / Diagram Notes

### W-Flow: Two-Stage Wasserstein Generative Model
```
Nodes:
  A[Reference Distribution (Gaussian noise)]
  B[Wasserstein Gradient Flow (energy minimization via Sinkhorn divergence)]
  C[Optimal Transport Path (continuous trajectory p_noise → p_data)]
  D[Static Generator Network (neural net trained to compress path)]
  E[Generated Sample (one forward pass)]
Edges: A→B, B→C, C→D (training only), A→D (inference), D→E
Labels:
  A→B: initialize particles from noise
  B→C: iterative flow minimizing Sinkhorn divergence
  C→D: distillation loss (finite-sample → continuous dynamics convergence theorem)
  A→D: inference: single forward pass, no iteration
  D→E: sample output
Notes: Training has two phases. Inference uses only D. ~100x speedup vs. multi-step diffusion.
```

### Mixture of Layers (MoL) Sparse Transformer Block
```
Nodes:
  A[Input Token Embeddings (d_model)]
  B[Down Projection (d_model → d_thin)]
  C1[Thin Block 1 (FFN + local attention, d_thin)]
  C2[Thin Block 2 (FFN + Gated DeltaNet linear attention, d_thin)]
  C3[... Thin Block K (routed via top-k gating)]
  G[Global Softmax Block (shared, full d_model, attends all tokens)]
  R[Top-k Router (learned gating over K thin blocks)]
  U[Up Projection (d_thin → d_model)]
  S[Sum + Normalize (aggregate thin block outputs)]
  O[Output (d_model)]
Edges: A→B, A→G, B→R, R→C1, R→C2, R→C3, C1→S, C2→S, C3→S, S→U, G→O (additive), U→O
Labels:
  A→G: global context (all tokens, full width)
  B→R: project to thin, route to top-k blocks
  C*→S: only top-k blocks active per token
  S→U: aggregate and project back to d_model
  G→O: global block output added residually
Notes: Only K_active < K thin blocks compute per token. Hybrid attention = 1 global softmax + K routed linear (Gated DeltaNet).
```

### Sharding Simulation (Multi-Turn LLM Evaluation)
```
Nodes:
  A[Original Single-Turn Benchmark Instruction]
  B[LLM Shard Decomposer (atomize into K units)]
  C1[Shard 1 (turn 1, underspecified)]
  C2[Shard 2 (turn 2, adds detail)]
  CK[Shard K (turn K, completes specification)]
  D[LLM Under Test]
  E[Response at Turn t (may be incomplete/wrong)]
  F[Performance Evaluator (single-turn score vs. multi-turn score)]
Edges: A→B, B→C1, B→C2, B→CK, C1→D, D→E, E→D (conversation history), C2→D, CK→D, D→F, A→F
Labels:
  A→B: decompose into K atomic information units
  Ct→D: feed shard t as user turn t
  D→E: model responds (may make incorrect assumptions early)
  E→D: conversation history maintained
  A→F: single-turn score (baseline)
  D→F: multi-turn scores (aggregated across turns)
Notes: Performance gap (single vs. multi-turn) = 39% mean drop. Unreliability +112%, Aptitude -15%.
```

### Practical Scaling Law: Loss Surface Decomposition
```
Nodes:
  A[Model Size N (parameters)]
  B[Total Examples Seen T (may repeat data)]
  C[Unique Examples D (actual data budget)]
  D[Undercapacity Term: a/N^α]
  E[Undertraining Term: b/T^β]
  F[Overfitting Term: c·N^γ/D^δ]
  G[Combined h = D + E + F]
  H[Loss L = E_irred + (L₀ - E_irred) · h/(1+h)]
  I[Irreducible Loss E_irred]
  J[Uninformed Baseline L₀]
Edges: A→D, T→E, N→F, D→F (data budget), D→G, E→G, F→G, G→H, I→H, J→H
Labels:
  N↑ → D↓ (more capacity reduces undercapacity loss)
  T↑ → E↓ (more training reduces undertraining loss)
  N↑,D↓ → F↑ (large model + small data increases overfitting)
  H saturates between E_irred and L₀ (no divergence)
Notes: Reduces to Chinchilla when T=D (single epoch), large D. Weight decay λ=1.0 reduces c (overfitting coefficient) by ~70%.
```

---

## Analysis & Impact for ML Researchers

- **Multi-turn evaluation gap demands immediate benchmark updates.** If you are evaluating LLMs for any real-world deployment — coding assistants, research tools, customer support — your single-turn benchmark scores likely overstate practical performance by ~39% on average. Applying sharding simulation to your existing benchmark suite is now the minimum responsible evaluation standard. The code/methodology from Laban et al. is directly replicable. If your use-case involves multi-turn dialogue with evolving requirements, reprioritize evaluation to account for the unreliability (+112%) finding, which may matter more than mean accuracy in production.

- **Scaling law researchers: Chinchilla is broken in data-constrained settings — use the Bryant-Liu formula instead.** If your training run repeats data (T > D), applies strong weight decay, or operates in a data-limited regime (e.g., domain-specific data, synthetic data with fixed budgets), the Chinchilla formula will give you wrong optimal compute allocation recommendations. The new three-component formula (arXiv 2605.09189) has been validated across architecture families and five published LLM scaling grids. The practical recommendation: if data is expensive relative to compute, the optimum shifts toward smaller datasets with more repetition plus stronger weight decay (λ=1.0 cuts overfitting coefficient by 70%).

- **Theoretical ML researchers: Succinctness is a new formal tool for understanding Transformer expressiveness.** The ICLR outstanding paper "Transformers are Inherently Succinct" opens a new research direction that goes beyond traditional expressiveness (what can be computed) to study compactness (how efficiently it is represented). The EXPSPACE-completeness of Transformer equivalence/emptiness verification is directly relevant to researchers working on mechanistic interpretability or formal LLM verification — it provides a complexity-theoretic lower bound on how hard those problems are in general. The succinctness hierarchy (Transformer ≪ LTL ≪ DFA) may also have implications for circuit-complexity analyses and length generalization research.

- **Generative modeling researchers: W-Flow's 100× sampling speedup at SOTA FID points toward a production-ready path.** One-step generation has historically sacrificed quality for speed (consistency models, distillation). W-Flow achieves FID 1.29 on ImageNet 256×256 in one step, which is competitive with multi-step diffusion baselines, while eliminating the ODE solver entirely. The key technical insight — using Sinkhorn divergence (an OT-based energy) rather than KL divergence to define the flow — addresses the mode-coverage failure of earlier one-step methods. Researchers working on video generation, medical imaging, or other compute-heavy diffusion applications should evaluate whether a Wasserstein gradient flow distillation approach can deliver similar gains in their domain.

- **Sparse architecture researchers: MoL's active-parameter efficiency suggests a practical alternative to MoE for long-context inference.** MoE reduces FFN compute but keeps attention full-width; MoL reduces both FFN and attention compute through block-level routing with hybrid attention to maintain global coverage. The 4.9× forward-pass speedup and 1.42–1.54× long-context throughput improvement (at 256K tokens) are compelling for applications where KV cache memory is the bottleneck. The trade-off (total parameters >> active parameters) is manageable if your serving infrastructure can handle sparse loading. For researchers training on FineWeb-Edu or Cosmopedia-style corpora, MoL overtaking dense baselines at 35% of training tokens suggests faster effective convergence in token-limited regimes.

---

## Key Takeaways (TL;DR)

- **ICLR 2026 Outstanding Paper (Laban et al.):** LLMs lose 39% performance in multi-turn conversations — primarily from +112% unreliability, not capability loss — across 15 models and 200,000+ simulated conversations.
- **ICLR 2026 Outstanding Paper (Bergsträßer et al.):** Transformers are exponentially more succinct than RNNs/LTL and doubly exponentially more succinct than finite automata; Transformer verification is EXPSPACE-complete.
- **W-Flow (arXiv 2605.11755):** One-step ImageNet 256×256 generation at FID 1.29 using Wasserstein gradient flows and Sinkhorn distillation — ~100× faster than multi-step diffusion at comparable quality.
- **Practical Scaling Laws (arXiv 2605.09189):** New three-component closed-form law fixes Chinchilla for data-constrained/multi-epoch training; weight decay λ=1.0 reduces overfitting coefficient by 70%.
- **Mixture of Layers (arXiv 2605.09516):** Sparse transformer with top-k thin-block routing + hybrid attention achieves PPL 29.99 on WikiText-103 (198M total / 77M active) with 4.9× forward-pass speedup and 1.42–1.54× long-context throughput at 256K tokens.
- **ICLR 2026 Honorable Mention (Polar Express):** GPU-friendly polar decomposition for the Muon optimizer using approximation theory; consistent validation-loss improvement on GPT-2 scale 1–10B token training.
- **NeurIPS 2026:** MLRC reproducibility challenge becomes an official NeurIPS track for the first time — reproducibility science now has a formal home inside a top-tier conference (Sydney, December 2026).
- **ICML 2026** accepted 6,352 papers from 23,918 submissions (26.6% rate); conference in Seoul July 6–11; lay summaries announced this week, driving heavy arXiv paper activity.
