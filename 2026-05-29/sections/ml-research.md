# Machine Learning Research — 2026-05-29

> **Note:** No major conference today. ICML 2026 is upcoming (July 6–11, Seoul, South Korea). ICLR 2026 concluded April 23–27 in Brazil; outstanding papers were announced April 23. NeurIPS 2026 paper notifications are scheduled for September 24, 2026.

---

## Top Stories (3-5)

### 1. GRAM: Generative Recursive Reasoning Models — Stochastic latent-space recursion beats frontier LRMs on ARC-AGI with 10M parameters

**Source:** [arXiv:2605.19376](https://arxiv.org/abs/2605.19376) | [Project page](https://ahn-ml.github.io/gram-website) | [OpenReview (ICLR 2026 Workshop RSI)](https://openreview.net/forum?id=Vxu6kcIjwV)

GRAM (Generative Recursive reAsoning Models) from KAIST, Mila, NYU, and Université de Montréal — co-authored by Yoshua Bengio and Sungjin Ahn — proposes a fundamentally new framing of recursive reasoning: instead of deterministic latent-state updates (as in Looped Transformers, HRM, and TRM), GRAM treats each reasoning step as a stochastic latent transition drawn from a learned distribution. This turns the entire reasoning process into a variational generative model over latent trajectories, enabling the model to maintain and explore multiple hypothesis paths simultaneously.

The core technical contribution is replacing deterministic recurrence \(h_{t+1} = f(h_t, x)\) with a stochastic latent transition \(z_{t+1} \sim q_\phi(z_{t+1} \mid z_t, x)\) parameterized as a Gaussian residual perturbation on the hidden state. The model is trained end-to-end via amortized variational inference (ELBO objective), jointly learning the prior \(p_\theta\) and posterior \(q_\phi\) networks. A single GRAM checkpoint can perform conditional reasoning \(p_\theta(y \mid x)\) or unconditional generation \(p_\theta(x)\), making it a unified generative model and reasoner.

At inference time, GRAM scales in two orthogonal dimensions that prior recursive models could not: depth (more recurrence steps) and width (parallel trajectory sampling over multiple stochastic paths). This is analogous to both extended chain-of-thought and beam search, but entirely in continuous latent space with no token overhead. The result is a 10M parameter model that achieves 97.0% on Sudoku-Extreme (vs. 87.4% for TRM-7M, 55.0% for HRM-27M) and 52.0% on ARC-AGI-1 — surpassing DeepSeek-R1 (671B), Claude 3.7, and o3-mini-high on that benchmark, and approaching GPT-5.2's 55.7% at a fraction of the parameter count.

What makes this result particularly striking is that GRAM does it without any language model pretraining, external tool use, or chain-of-thought token generation. The model's reasoning is entirely latent, more akin to biological intuition than token-by-token verbalization. This opens a line of research where recursive latent models and large language models could be combined — using GRAM as a structured reasoning component inside a larger system.

**Key technical details:**
- Architecture: shared-weight recursive transformer blocks with Gaussian residual latent transitions; trained via ELBO with amortized inference network \(q_\phi\)
- Parameters: 10M (GRAM) vs. 27M (HRM), 7M (TRM/Looped TF)
- Sudoku-Extreme accuracy: GRAM 97.0% > TRM 87.4% > HRM 55.0% > Looped TF 61.3%
- ARC-AGI-1: GRAM 52.0% > TRM 44.6% > HRM 40.3%; beats o3-mini-high (34.5%), Claude 3.7 (28.6%), DeepSeek-R1 (15.8%)
- ARC-AGI-2: GRAM 11.1% > HRM 5.0%; Gemini 3 Pro leads at 31.1%
- N-Queens multi-solution coverage: >90%
- Inference-time scaling: both depth (more recursion steps) and width (parallel latent trajectory sampling)
- Training: amortized variational inference; Gaussian residuals on latent state, no token generation

---

### 2. "Transformers Are Inherently Succinct" — ICLR 2026 Outstanding Paper proves transformers exponentially more compact than RNNs and SSMs

**Source:** [arXiv:2510.19315](https://arxiv.org/html/2510.19315v2) | [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ) | [ICLR 2026 Outstanding Paper Announcement](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)

This purely theoretical paper — awarded one of ICLR 2026's two Outstanding Paper awards — introduces succinctness as a new lens for measuring transformer expressivity. While previous work asked "what can transformers compute?" (expressiveness), Bergsträßer, Cotterell, and Lin ask "how compactly can they describe it?" (succinctness). The distinction is crucial: a formalism can be equally expressive but require dramatically more parameters to represent the same concept.

The key result is a set of tight separation theorems. Fixed-precision transformers are **exponentially more succinct** than Linear Temporal Logic (LTL) and recurrent neural networks (including, by extension, all state-space models like Mamba and RWKV). They are **doubly exponentially more succinct** than finite automata. In other words, there exist families of formal languages that polynomial-size transformers can describe, but whose smallest equivalent RNN/SSM is exponentially larger, and whose smallest equivalent automaton is doubly exponentially larger. The paper also establishes matching upper bounds: any fixed-precision transformer can be converted to an LTL formula with at most exponential blowup (improving a prior doubly exponential bound).

A direct corollary of this extreme succinctness is that transformer verification is provably intractable. Checking even whether a transformer accepts at least one string (emptiness) or whether two transformers recognize the same language (equivalence) is EXPSPACE-complete — meaning the memory required to solve these problems grows exponentially with the model's size. This has immediate implications for safety research: formal verification of transformer behavior is computationally harder than previously appreciated.

The practical interpretation is nuanced. The result explains why relatively small transformers can generalize to complex patterns that would require enormous RNNs to represent. It does not mean transformers are always better than SSMs on all tasks — it means the parameter budget is more efficiently used by the attention mechanism for certain structured language tasks. The review committee cited the paper as "offering a new perspective for explaining the power of the Transformer architecture."

**Key technical details:**
- Succinctness gaps: transformers vs. LTL/RNN: exponential; transformers vs. finite automata: doubly exponential
- Construction: encodes a 2^n-tiling problem in a polynomial-size transformer using attention to check horizontal (adjacency) and vertical (counter-match) constraints
- Complexity of transformer emptiness/equivalence: EXPSPACE-complete (previously known only for weaker models)
- Upper bound: any fixed-precision transformer → LTL formula with ≤ exponential blowup (prior best: doubly exponential)
- No experiments; entirely proof-based; 2024 preprint, awarded ICLR 2026 Outstanding Paper
- Companion honorable mention: "The Polar Express" (Amsel, Persson, Musco, Gower) on minimax-optimal polar decomposition for the Muon optimizer

---

### 3. AutoTTS — AI agent discovers test-time scaling strategies that cut token usage 69.5% at equal accuracy

**Source:** [arXiv:2605.08083](https://arxiv.org/abs/2605.08083) | [GitHub: zhengkid/AutoTTS](https://github.com/zhengkid/AutoTTS) | [VentureBeat coverage](https://venturebeat.com/orchestration/researchers-automated-llm-reasoning-strategy-design-and-cut-token-usage-by-69-5)

AutoTTS (from UMD, UVA, WUSTL, UNC, Google, and Meta) reframes the test-time scaling (TTS) problem: instead of humans manually designing heuristics like Self-Consistency or Early-Stopping Self-Consistency, they build an environment where an AI agent (Claude Code) automatically discovers optimal compute-allocation controllers. The key insight is that TTS strategies can be expressed as code-defined controllers operating over pre-collected reasoning trajectories — making evaluation cheap (no repeated LLM calls) and deterministic (offline replay).

The discovery process works as follows: a coding agent iteratively proposes and refines Python controllers that specify when to branch, continue, probe, prune, or stop a reasoning trajectory. Beta parameterization constrains controllers to expose a single scalar trade-off knob (β), preventing the search from degenerating into excessive hyperparameter tuning. Fine-grained execution trace feedback tells the agent not just accuracy/cost scalars but *why* a particular controller failed, enabling directed refinement.

The discovered controller — named Confidence Momentum Controller (CMC) — uses trend-based stopping (stop when confidence level trend is non-negative), coupled width-depth control (spawn new branches only when existing paths show stagnation or regression), and alignment-aware depth allocation (give more compute to branches aligned with emerging consensus). This was discovered in $39.9 and 160 minutes of compute, then evaluated on held-out benchmarks the agent never saw.

Results: at the balanced β=0.5 operating point, AutoTTS-CMC cuts aggregate token usage by 69.5% vs. SC@64 while maintaining equivalent average accuracy across four Qwen3 model scales (0.6B–8B) and a DeepSeek-R1 8B distillation. On GPQA-Diamond, token cost drops from 510K to 151K tokens with a slight accuracy improvement. On HMMT25, the DeepSeek-R1 backbone with AutoTTS achieves the highest overall accuracy while cutting token spend nearly in half. Strategies generalize across held-out benchmarks and model scales with no retuning.

**Key technical details:**
- Framework: offline replay environment, zero LLM calls during controller evaluation
- Beta parameterization: single scalar β controls accuracy-cost trade-off
- Discovered controller (CMC): trend-based stopping, coupled width-depth, alignment-aware depth allocation, conservative branch abandonment
- Token reduction vs. SC@64: 69.5% at equal accuracy (β=0.5 operating point)
- GPQA-Diamond: 510K → 151K tokens, slight accuracy gain
- HMMT25 with DeepSeek-R1 8B: highest accuracy among all methods, ~50% token reduction
- Discovery cost: $39.9, 160 minutes; agent: Claude Code, 5 discovery rounds
- Generalizes across 0.6B–8B Qwen3 scales and DeepSeek-R1 8B without retuning

---

### 4. Muown — Drop-in Muon replacement with row-norm control beats AdamW, SOAP, and Muon at 2.7B scale

**Source:** [arXiv:2605.10797](https://arxiv.org/abs/2605.10797) | [GitHub: kcc-lion/muown](https://github.com/kcc-lion/muown)

Muown addresses a known instability in the Muon optimizer: without decoupled weight decay, the spectral norm of weight matrices drifts upward during training. The authors identify the root cause via a decomposition of the spectral norm into two factors — row magnitude and row coherence — and show empirically and theoretically that the row-magnitude component is the driver of spectral drift, while the row-coherence component stays well-behaved.

The fix is elegant: Muown reparameterizes each weight matrix as \(W = \text{diag}(r) \cdot \hat{W}\), where \(r\) is the row-magnitude vector and \(\hat{W}\) is the normalized directional component. Muon is applied unchanged to the directional component. The magnitude vector \(r\) is treated as an explicit optimizer variable updated under \(\ell_\infty\) geometry, which is the natural geometry induced by the decomposition. This adds negligible computational overhead when weight matrices are sharded appropriately across devices.

The paper proves that Muown achieves optimal non-convex convergence rates under the dual norm aligned with both geometries (Schatten-p for the directional component, \(\ell_\infty\) for magnitudes), with a stochastic noise coefficient empirically below Muon throughout training. Across GPT-style pretraining on FineWeb-Edu from 124M to 2.7B parameters, Muown consistently improves perplexity over Muon, SOAP, AdamW, and Lion, with the improvement persisting and not attenuating as model scale increases (0.30 PPL improvement at 1B, maintained at 2.7B). It also widens the plateau of near-optimal learning rates — a practical advantage for practitioners who don't want to run extensive hyperparameter sweeps.

**Key technical details:**
- Decomposition: \(\|W\|_{\text{spec}} = \|r\|_\infty \cdot \|\hat{W}\|_{\text{spec}}\); row magnitude \(r\) drives spectral drift under Muon
- Row magnitude update: \(\ell_\infty\) geometry; directional component: Muon update unchanged
- Proof: optimal non-convex rates in deterministic and stochastic regimes
- 1B param: Muown PPL 11.90 vs. Muon best 12.20 (Δ0.30 improvement)
- 2.7B param: improvement maintained, does not attenuate with scale
- Outperforms Muon, SOAP, AdamW, Lion across all tested scales (124M–2.7B)
- Training dataset: FineWeb-Edu; architecture: GPT-style with GLU-MLP, RMSNorm
- Code: open-source, supports torchrun multi-GPU with WSD scheduling

---

### 5. "Language Models Need Sleep" — CMU/UMD proposes offline memory consolidation to handle long-horizon reasoning

**Source:** [arXiv:2605.26099](https://arxiv.org/abs/2605.26099) | [EmergentMind summary](https://www.emergentmind.com/papers/2605.26099)

Researchers from CMU and the University of Maryland (Sangyun Lee, Sean McLeish, Tom Goldstein, Giulia Fanti) propose a biologically-inspired sleep mechanism for hybrid attention-SSM language models. The key observation: the bottleneck for long-horizon reasoning is not memory *capacity* (which SSMs have) but the *compute budget available to transform evicted context into useful internal state*. Standard SSM-attention hybrids perform a single forward pass per token; when context is evicted from the KV cache, that information is gone — there is no opportunity for deep processing.

The sleep mechanism: when the model's context window is nearly full, instead of continuing, the model enters a sleep phase of N offline recurrent passes over all accumulated context. During each pass, fast weights in the SSM blocks are updated via a learned local rule (trained end-to-end with gradients flowing through sleep). After N passes, the KV cache is cleared and the model resumes wake-time inference with the consolidated fast weights. From the user's perspective, wake-time latency is unchanged — the extra compute is amortized over the sleep period.

Evaluations on cellular automata, multi-hop graph retrieval, and GSM-Infinite math show that standard transformers and vanilla SSM-attention hybrids fail on tasks requiring deep sequential reasoning over evicted context, while sleep models succeed. Crucially, increasing sleep depth N monotonically improves performance, with the largest gains on examples requiring deeper reasoning. The paper uses Muon optimizer alongside fixed AdamW for training, and implements the mechanism as a modification to existing hybrid architectures (compatible with Mamba, RWKV).

This work directly challenges the dominant paradigm of expanding context windows. Quadratic attention over 1M+ token windows is expensive; the sleep approach suggests an alternative: finite attention windows with periodic compression. The compute spike during sleep is amortized — e.g., if sleep fires every 10K tokens, the cost is lower than quadratic attention over a 1M-token sequence. The mechanism is also architecture-agnostic for the SSM component.

**Key technical details:**
- Architecture: hybrid attention-SSM with added sleep phase; SSM fast weights updated via learned local rule
- Sleep phase: N offline recurrent passes over accumulated context before KV cache eviction
- Training: end-to-end with gradients through sleep; Muon + AdamW
- Tasks: cellular automata (structured memory), multi-hop graph retrieval (relational), GSM-Infinite (math)
- Result: performance improves monotonically with sleep depth N; vanilla transformer/SSM hybrids fail on same tasks
- Wake-time latency: unchanged (extra compute in sleep phase only)
- Compatible with existing Mamba/RWKV SSM blocks as drop-in modification
- Published: arXiv May 25, 2026

---

## Deep Dive: Most Important Item

### GRAM: Generative Recursive Reasoning — Why Latent-Space Stochastic Recursion May Be the Next Reasoning Paradigm

GRAM is the most consequential paper published this week because it demonstrates — at a scale of only 10M parameters — a reasoning approach that is fundamentally orthogonal to all mainstream methods: it reasons entirely in continuous latent space, scales at inference time in two independent dimensions (depth and width), and outperforms frontier 100B+ models on structured benchmarks. If the approach scales, it represents a potentially cheaper and faster path to System-2 reasoning than extending chain-of-thought token sequences.

**Why this matters most.** Current large reasoning models (LRMs) like o3, Gemini 3 Pro, and GPT-5.2 extend computation by generating more tokens — often thousands of chain-of-thought steps. This is expensive: more tokens means more memory bandwidth, more KV cache, and longer latency. Recursive latent models like GRAM decouple reasoning depth from parameter count and token count. The recursion happens inside the weight-shared blocks, not across new token positions. Combined with GRAM's stochastic trajectories, inference-time scaling is done by sampling multiple latent paths in parallel — a width operation analogous to beam search but without discrete token commitments at each step.

**Technical depth.** GRAM's generative formulation starts from the variational lower bound on log p(y|x): ELBO = E_{q_φ}[log p_θ(y|z)] − KL(q_φ(z|x,y) || p_θ(z|x)). The prior p_θ encodes what the model expects a reasoning trajectory to look like given input x; the posterior q_φ encodes what trajectory actually produced output y during training. At test time, the model samples from p_θ, executing multiple stochastic reasoning paths in parallel. The shared-weight transition blocks mean parameter count doesn't grow with recursion depth — a 10M parameter model can run 16, 32, or 64 recursion steps without additional parameters. The deterministic failure modes of prior RRMs (mode collapse, single attractor) are broken by the Gaussian residual perturbations injected at each recursive step.

**Why GRAM beats frontier LRMs on Sudoku while they score 0%.** Sudoku-Extreme requires backtracking over constraint-propagation states — a search problem with a deep combinatorial structure. Autoregressive LRMs generate tokens sequentially, which means once they commit to a digit placement at position k, recovering from a contradicted constraint requires the model to generate many more tokens to undo it. GRAM's latent-space search doesn't commit to discrete decisions at each step; instead, it maintains a distribution over possible states that can be refined iteratively. This is structurally more compatible with constraint satisfaction than token generation.

**Open questions:**
- Does GRAM's advantage hold at larger parameter scales (100M–1B), and can it be combined with a language backbone for open-domain reasoning?
- The current evaluation compares against recursive baselines, not against chain-of-thought prompting on frontier models with search scaffolding (e.g., tree-of-thought on GPT-5.2)
- ARC-AGI-2 score of 11.1% is far below Gemini 3 Pro (31.1%) and Grok-4-thinking (16.0%) — ARC-AGI-2's more abstract transformations may require visual/symbolic grounding that GRAM lacks
- The training procedure (amortized VI with ELBO) is significantly more complex than cross-entropy; scaling this stably to larger models is an open engineering challenge
- N-Queens and graph coloring results are promising for multi-solution problems, but coverage metrics (>90%) don't yet have rigorous evaluation protocols across difficulty levels

**Broader significance.** GRAM joins a growing literature on latent-space reasoning (HRM, TRM, Looped Transformers) and positions this line of work as a credible competitor to token-extended reasoning. The Bengio lab's involvement signals this is being taken seriously at the research frontier. If GRAM's stochastic approach scales — and if it can be hybridized with language model decoders — it could enable models that reason efficiently in latent space and only "surface" to token generation when producing final outputs, dramatically reducing inference costs for hard reasoning tasks.

---

## Benchmark Data

```json
[
  {
    "benchmark": "Sudoku-Extreme",
    "scale": "10M–27M parameters (recursive models)",
    "results": [
      {"model": "GRAM (Ours)", "score": 97.0, "unit": "% accuracy"},
      {"model": "TRM (7M)", "score": 87.4, "unit": "% accuracy"},
      {"model": "Looped TF (7M)", "score": 61.3, "unit": "% accuracy"},
      {"model": "HRM (27M)", "score": 55.0, "unit": "% accuracy"},
      {"model": "Direct Pred (27M)", "score": 0.0, "unit": "% accuracy"},
      {"model": "DeepSeek-R1 (671B)", "score": 0.0, "unit": "% accuracy"},
      {"model": "Claude 3.7 (16k CoT)", "score": 0.0, "unit": "% accuracy"},
      {"model": "o3-mini-high", "score": 0.0, "unit": "% accuracy"}
    ],
    "notes": "Recursive models dominate; all frontier LRMs score 0% — structured constraint satisfaction not solved by token generation"
  },
  {
    "benchmark": "ARC-AGI-1",
    "scale": "Various",
    "results": [
      {"model": "Gemini 3 Pro", "score": 75.0, "unit": "% accuracy"},
      {"model": "Grok-4-thinking (1.7T)", "score": 66.7, "unit": "% accuracy"},
      {"model": "GPT-5.2 (low)", "score": 55.7, "unit": "% accuracy"},
      {"model": "GRAM (10M)", "score": 52.0, "unit": "% accuracy"},
      {"model": "TRM (7M)", "score": 44.6, "unit": "% accuracy"},
      {"model": "o3-mini-high", "score": 34.5, "unit": "% accuracy"},
      {"model": "HRM (27M)", "score": 40.3, "unit": "% accuracy"},
      {"model": "Claude 3.7", "score": 28.6, "unit": "% accuracy"},
      {"model": "DeepSeek-R1 (671B)", "score": 15.8, "unit": "% accuracy"},
      {"model": "Direct Pred (27M)", "score": 21.0, "unit": "% accuracy"}
    ],
    "notes": "GRAM (10M) beats o3-mini-high, Claude 3.7, and DeepSeek-R1 despite 67× fewer parameters than R1"
  },
  {
    "benchmark": "ARC-AGI-2",
    "scale": "Various",
    "results": [
      {"model": "Gemini 3 Pro", "score": 31.1, "unit": "% accuracy"},
      {"model": "Grok-4-thinking (1.7T)", "score": 16.0, "unit": "% accuracy"},
      {"model": "GRAM (10M)", "score": 11.1, "unit": "% accuracy"},
      {"model": "GPT-5.2 (low)", "score": 9.7, "unit": "% accuracy"},
      {"model": "HRM (27M)", "score": 5.0, "unit": "% accuracy"},
      {"model": "TRM (7M)", "score": 7.8, "unit": "% accuracy"},
      {"model": "o3-mini-high", "score": 3.0, "unit": "% accuracy"},
      {"model": "Claude 3.7", "score": 0.7, "unit": "% accuracy"},
      {"model": "DeepSeek-R1", "score": 1.3, "unit": "% accuracy"}
    ],
    "notes": "ARC-AGI-2 favors visual/symbolic grounding; Gemini 3 Pro leads substantially"
  },
  {
    "benchmark": "Muon Optimizer — GPT pretraining perplexity (FineWeb-Edu)",
    "scale": "1B–2.7B parameters",
    "results": [
      {"model": "Muown (1B)", "score": 11.90, "unit": "perplexity"},
      {"model": "Muon (1B, best run)", "score": 12.20, "unit": "perplexity"},
      {"model": "SOAP (1B)", "score": null, "unit": "perplexity (Muown beats)"},
      {"model": "AdamW (1B)", "score": null, "unit": "perplexity (Muown beats)"},
      {"model": "Lion (1B)", "score": null, "unit": "perplexity (Muown beats)"}
    ],
    "notes": "Muown consistently beats all baselines 124M–2.7B; 0.30 PPL improvement at 1B scale"
  },
  {
    "benchmark": "OpenWebText — Continuous Diffusion LM Perplexity (RePlaid)",
    "scale": "0.1B parameters",
    "results": [
      {"model": "RePlaid (s.c.)", "score": 22.1, "unit": "PPL bound"},
      {"model": "MDLM (low var.)", "score": 23.1, "unit": "PPL bound"},
      {"model": "Duo", "score": 25.2, "unit": "PPL bound"},
      {"model": "Plaid", "score": 24.4, "unit": "PPL bound"},
      {"model": "LangFlow", "score": 32.2, "unit": "PPL bound"},
      {"model": "Diffusion-LM", "score": 118.6, "unit": "PPL bound"}
    ],
    "notes": "RePlaid closes the continuous vs. discrete DLM compute gap to 20× vs. AR baseline; best continuous DLM result on OpenWebText"
  },
  {
    "benchmark": "AutoTTS — Token efficiency vs. Self-Consistency SC@64",
    "scale": "Qwen3 0.6B–8B, DeepSeek-R1 8B distill",
    "results": [
      {"model": "AutoTTS-CMC (β=0.5)", "score": 69.5, "unit": "% token reduction vs. SC@64"},
      {"model": "AutoTTS-CMC (max accuracy)", "score": 5, "unit": "of 8 test cases beat all baselines"}
    ],
    "notes": "GPQA-Diamond: 510K → 151K tokens with accuracy improvement. Discovery cost: $39.9, 160 min"
  },
  {
    "benchmark": "Step 3.5 Flash — Coding and reasoning",
    "scale": "196B MoE (11B active)",
    "results": [
      {"model": "Step 3.5 Flash", "score": 97.3, "unit": "% AIME 2025"},
      {"model": "Step 3.5 Flash", "score": 74.4, "unit": "% SWE-bench Verified"},
      {"model": "Step 3.5 Flash", "score": 86.4, "unit": "% LiveCodeBench-V6"},
      {"model": "Step 3.5 Flash", "score": 51.0, "unit": "% Terminal-Bench 2.0"},
      {"model": "Step 3.5 Flash", "score": 350, "unit": "tok/s peak (coding)"}
    ],
    "notes": "Apache 2.0, 196B MoE (11B active); MTP-3 generates 4 tokens simultaneously; 256K context window"
  },
  {
    "benchmark": "Open Weights Intelligence Index (Artificial Analysis v4.0)",
    "scale": "Various open-weight models",
    "results": [
      {"model": "Kimi K2.6", "score": 54, "unit": "Intelligence Index"},
      {"model": "MiMo-V2.5-Pro", "score": 54, "unit": "Intelligence Index"},
      {"model": "DeepSeek V4 Pro (Reasoning, Max Effort)", "score": 52, "unit": "Intelligence Index"}
    ],
    "notes": "241 open-weights models evaluated out of 377 total; index incorporates 10 evaluations including HLE, GPQA Diamond"
  }
]
```

---

## Architecture / Diagram Notes

### GRAM (Generative Recursive Reasoning Model)

```
Nodes:
  X[Input x]
  ENC[Encoder / Input Embedding]
  H0[Initial Hidden State h_0]
  PRIOR[Prior Network p_θ(z_{t+1}|h_t)]
  POST[Posterior Network q_φ(z_{t+1}|h_t, y)]
  TRANS[Shared-Weight Transition Block f(h_t, z_t)]
  HT[Hidden State h_T after T steps]
  DEC[Decoder / Output Head]
  Y[Output y]
  SAMPLE[Parallel Trajectory Sampler (width K)]

Edges:
  X→ENC, ENC→H0
  H0→PRIOR, H0→POST
  PRIOR→TRANS, POST→TRANS
  TRANS→HT [loop T times, shared weights]
  HT→DEC, DEC→Y
  H0→SAMPLE [K parallel stochastic paths]
  SAMPLE→TRANS

Labels:
  PRIOR→TRANS: sample z_{t+1} ~ N(μ_θ(h_t), σ²_θ(h_t))
  TRANS→HT: h_{t+1} = f(h_t) + z_{t+1}  [stochastic residual]
  SAMPLE→TRANS: width scaling (parallel trajectories)
  HT→TRANS: depth scaling (more recursive steps)
```

### Muown Weight Decomposition

```
Nodes:
  W[Weight Matrix W ∈ R^{m×n}]
  DECOMP[Decompose: W = diag(r) · Ŵ]
  R[Row Magnitude Vector r ∈ R^m]
  WHAT[Normalized Directional Component Ŵ]
  MUON[Muon Update on Ŵ (orthogonalized gradient)]
  LINF[ℓ∞ Update on r (explicit optimizer variable)]
  RECON[Reconstruct: W_new = diag(r_new) · Ŵ_new]

Edges:
  W→DECOMP, DECOMP→R, DECOMP→WHAT
  WHAT→MUON, R→LINF
  MUON→RECON, LINF→RECON
  RECON→W [next step]

Labels:
  DECOMP→R: ‖W‖_spec ≈ ‖r‖_∞ · ‖Ŵ‖_spec
  LINF→R: r updated under ℓ_∞ geometry (prevents spectral drift)
  MUON→WHAT: standard Newton-Schulz orthogonalization
```

### Language Models Need Sleep — Hybrid SSM-Attention with Sleep Phase

```
Nodes:
  TOK[Input Tokens (streaming)]
  ATT[Attention Layers (KV Cache)]
  SSM[SSM Blocks (Fast Weights)]
  SLEEP_GATE[Sleep Trigger: KV Cache Full?]
  SLEEP[Sleep Phase: N offline recurrent passes]
  RULE[Learned Local Update Rule for Fast Weights]
  CLEAR[Clear KV Cache]
  WAKE[Wake-time Inference (single forward pass)]
  OUT[Output Tokens]

Edges:
  TOK→ATT, ATT→SSM
  ATT→SLEEP_GATE
  SLEEP_GATE→SLEEP [if cache full]
  SLEEP→RULE, RULE→SSM [update fast weights]
  SLEEP→CLEAR [after N passes]
  CLEAR→WAKE
  SSM→WAKE [consolidated fast weights available]
  WAKE→OUT
  TOK→WAKE [continued token intake after wake]

Labels:
  SLEEP_GATE→SLEEP: trigger every ~10K tokens
  SLEEP→RULE: N recurrent passes; N controls reasoning depth
  RULE→SSM: fast weight update; no new tokens consumed during sleep
  WAKE→OUT: latency unchanged from baseline
```

---

## Analysis & Impact for ML Researchers

- **GRAM signals that latent-space recursive reasoning is now competitive with frontier LRMs on structured tasks.** If you work on planning, constraint satisfaction, or combinatorial reasoning, GRAM (arXiv:2605.19376) is required reading. The stochastic variational formulation enables width scaling that is architecturally infeasible in token-autoregressive models. Immediate practical action: evaluate GRAM on your domain's structured reasoning benchmarks; the 10M parameter model is small enough to run in any lab.

- **The ICLR 2026 Outstanding Paper result ("Transformers Are Inherently Succinct") reframes the expressivity vs. SSM debate.** The practical implication: for workloads where the concept space is complex and structured (code, formal logic, hierarchical language), transformers are likely more parameter-efficient than RNNs/SSMs of equal size. If your architecture search is comparing attention vs. state-space models on expressivity grounds, you now have a formal result showing attention dominates on succinctness. For safety researchers: EXPSPACE-completeness of transformer verification means any formal safety guarantee proof must find tractable special cases — track the verification literature carefully.

- **AutoTTS demonstrates that test-time scaling strategies should be discovered, not hand-crafted.** If you are deploying reasoning models in production and paying per-token costs, AutoTTS (arXiv:2605.08083) at 69.5% token reduction with no accuracy loss is directly applicable. The $39.9 discovery cost and 160-minute runtime make this accessible: you can run AutoTTS discovery on your specific domain (e.g., code generation, medical reasoning) and get a custom-tuned controller without modifying the base model. The CMC controller code is open-source.

- **Muown and the Polar Express together suggest the Muon ecosystem is now mature enough to replace AdamW for serious pretraining runs.** Muown (arXiv:2605.10797) fixes Muon's spectral norm drift and consistently outperforms AdamW, SOAP, and Lion from 124M to 2.7B. The Polar Express (ICLR 2026 Honorable Mention, arXiv:2505.16932) provides a theoretically optimal polar decomposition kernel for Muon that is numerically stable in bfloat16. If you are planning a pretraining run at any scale, you should benchmark Muown over AdamW; the code is available and the overhead is negligible when sharded.

- **"Language Models Need Sleep" opens a new direction in long-context architectures that is directly complementary to sliding window attention and SSMs.** For researchers working on long-horizon agents (e.g., coding agents that must reason over large codebases), the sleep-and-consolidate paradigm offers a third option alongside: (a) infinite attention windows (quadratic cost), (b) fixed SSM states (limited reasoning depth per eviction). Sleep phases shift compute to offline periods, enabling deeper reasoning over evicted context at bounded wake-time latency. The CMU/UMD implementation is compatible with existing Mamba/RWKV SSM blocks.

---

## Key Takeaways (TL;DR)

- **GRAM (10M params) achieves 97.0% on Sudoku-Extreme and 52.0% on ARC-AGI-1 by treating recursive latent reasoning as a stochastic variational process**, outperforming DeepSeek-R1, Claude 3.7, and o3-mini-high at a tiny fraction of their parameter count.
- **ICLR 2026 Outstanding Paper proves transformers are exponentially more succinct than RNNs/SSMs and doubly exponentially more succinct than finite automata**, with the corollary that basic transformer verification is EXPSPACE-complete.
- **AutoTTS (Meta/Google/universities) uses an AI agent to auto-discover test-time scaling controllers**, cutting inference token cost by 69.5% vs. Self-Consistency at equal accuracy for $39.9 in compute.
- **Muown fixes Muon's spectral norm drift** by treating row magnitudes as explicit optimizer variables under ℓ∞ geometry, consistently beating AdamW, SOAP, and Muon across 124M–2.7B parameter GPT-style models.
- **"Language Models Need Sleep" proposes periodic offline memory consolidation** in hybrid SSM-attention models: N recurrent passes over context before KV eviction enable deep reasoning over long horizons without increasing wake-time latency.
- **ICML 2026 (Seoul, July 6–11) is the next major venue** — paper acceptance notifications have been sent; watch for outstanding paper announcements around the conference start date.
- **The open-source LLM landscape is dominated by hybrid attention-SSM architectures and MoE designs** — Step 3.5 Flash (196B MoE, 11B active, Apache 2.0) leads on AIME 2025 (97.3%) and SWE-bench Verified (74.4%) among open-weight models.
- **System-level "harness scaling" is now recognized as a distinct research problem from model scaling** (arXiv:2605.26112, UC Berkeley): once a model crosses a capability threshold, performance on long-horizon tasks depends more on memory, context, tool routing, and verification design than on further model scaling.
