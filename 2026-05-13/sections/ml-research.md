# Machine Learning Research — 2026-05-13

> **Note:** No major conference today. ICML 2026 is scheduled for July 6–11 in Seoul, South Korea. ICLR 2026 outstanding papers were announced April 23 and are still drawing community attention.

---

## Top Stories (3-5)

### 1. AlphaEvolve 1-Year Report: Real-World Algorithm Discovery at Scale — DeepMind's evolutionary coding agent proves transformative across genomics, physics, and combinatorics

**Source:** [Google DeepMind Blog](https://deepmind.google/blog/alphaevolve-impact/) | [Google Cloud Blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-updates/) | [GitHub Results](https://github.com/google-deepmind/alphaevolve_results)

Google DeepMind released a comprehensive one-year retrospective on AlphaEvolve, the Gemini-powered evolutionary coding agent first introduced in May 2025. The report documents deployments across at least seven distinct scientific and infrastructure domains, with measurable, verifiable improvements in each. Unlike prior AI-for-science systems, AlphaEvolve operates end-to-end: it proposes algorithmic improvements, generates executable code, evaluates outputs using automated metrics, and iterates via an evolutionary loop—without requiring human-written scaffolding per domain.

The most headline-grabbing result is in matrix multiplication. AlphaEvolve discovered a 4×4 complex-valued matrix multiplication algorithm using 48 scalar multiplications, the first improvement over Strassen's 1969 result (49 multiplications) in 56 years. The significance goes beyond the single case: because the solution is expressed as a tensor decomposition over noncommutative rings, it can be applied recursively to large matrices, yielding an asymptotic complexity of O(N^log₄(48)) ≈ O(N^2.7925), vs. Strassen's O(N^2.8074). Independent community verification confirms correctness to machine precision (~10⁻¹⁶ relative error).

In applied science, AlphaEvolve improved DeepConsensus (DeepMind's DNA error-correction model) by reducing variant detection errors 30%, raised AC Optimal Power Flow feasibility from 14% to 88%, increased natural disaster risk prediction accuracy by 5% across 20 hazard categories, and optimized quantum circuits for Google's Willow processor achieving 10× lower gate error vs. conventional baselines. Mathematician Terence Tao collaborated on the Erdős problems work, which yielded new constructive results. Critically, AlphaEvolve was also used to improve the training efficiency of the Gemini models that power it—a closed feedback loop.

**Key technical details:**
- Architecture: ensemble of Gemini Flash (exploration breadth) + Gemini Pro (exploitation depth) with automated evaluators
- Matrix mult. breakthrough: 48 scalar multiplications for 4×4 complex matrices (vs. Strassen's 49, standard 64)
- Asymptotic complexity improvement: O(N^2.7925) vs. O(N^2.8074) for large-matrix recursion
- Power flow: 14% → 88% feasibility rate on AC Optimal Power Flow benchmark
- Genomics: 30% reduction in variant detection errors in DeepConsensus
- Quantum: 10× lower circuit error rate on Willow QPU
- Earth AI: +5% across 20 disaster prediction categories

---

### 2. NVIDIA Star Elastic: One Checkpoint, Three Models — Training multiple reasoning models at 1/360th the cost of individual runs

**Source:** [arXiv:2605.07182](https://arxiv.org/html/2605.07182v1) | [Hugging Face (30B)](https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-3-Elastic-30B-A3B-BF16) | [Hugging Face (12B)](https://huggingface.co/nvidia/Nemotron-Elastic-12B)

NVIDIA Research published Star Elastic, a post-training method that embeds multiple nested submodels within a single parent checkpoint. The core observation is that current practice trains separate model families (e.g., 30B, 14B, 7B variants) from scratch or via independent fine-tuning, wasting enormous compute. Star Elastic instead applies "elastification"—a curriculum-based co-training scheme where submodels are initialized from the parent and updated via structured knowledge distillation—producing N model sizes from a single training run.

The technique supports elastification along four independent axes: SSM (State Space Model dimensions), embedding channels, MoE expert routing, and FFN width. An end-to-end trainable router learns to activate the appropriate subgraph at inference time, and Quantization-Aware Distillation (QAD) extends the approach to nested NVFP4 and FP8 checkpoints for deployment. The paper demonstrates the approach on NVIDIA Nemotron Nano v3 (30B/3.6A parameters), producing 23B/2.8A and 12B/2.0A variants trained on 160B tokens.

The elastic budget control capability is particularly notable for inference-time reasoning: by selecting different submodels for the "thinking" phase vs. the "answering" phase of a chain-of-thought response, the system achieves up to 16% higher accuracy at 1.9× lower latency compared to using the full model throughout. The method shows a 360× training cost reduction compared to pretraining from scratch, and 7× vs. state-of-the-art compression methods.

**Key technical details:**
- Base model: NVIDIA Nemotron Nano v3 (30B total, 3.6B active parameters)
- Elastification axes: SSM, embedding, MoE, FFN
- Produced variants: 23B/2.8A, 12B/2.0A — from a single 160B-token training run
- Cost reduction: 360× vs. pretraining from scratch; 7× vs. best compression baseline
- Elastic budget control (think vs. answer phase selection): +16% accuracy, 1.9× lower latency
- Quantization: Nested NVFP4 and FP8 checkpoints via QAD
- Models open on Hugging Face (BF16 and FP8 variants)

---

### 3. PowerStep: Halving Optimizer Memory with ℓp-Norm Steepest Descent — A memory-efficient Adam alternative validated up to 235B parameters

**Source:** [arXiv:2605.10335](https://arxiv.org/html/2605.10335) | [GitHub](https://github.com/yaolubrain/PowerStep)

PowerStep is a new adaptive optimizer that achieves coordinate-wise adaptivity—the key property behind Adam's empirical success—without maintaining a second-moment buffer. The derivation starts from steepest descent under an ℓp-norm geometry: for p→∞ the update collapses to sign-gradient (SignSGD); for p=2 it recovers standard gradient descent. By choosing intermediate p and applying a nonlinear transform to a single momentum buffer, PowerStep achieves per-coordinate scaling comparable to Adam while storing half the optimizer state.

The theoretical contribution is a proof that PowerStep converges at the optimal O(1/√T) rate for non-convex stochastic optimization. Empirically, experiments on Transformers from 124M to 235B parameters show that PowerStep matches Adam's validation loss trajectories across all scales, with no perceptible quality degradation. When the momentum buffer is further quantized to int8, total optimizer memory drops ~8× compared to full-precision Adam—making it particularly relevant for training at scale where optimizer state (which equals 2× model size for Adam in bf16) is a hard memory constraint.

The significance is practical: at 235B parameters, Adam's optimizer state (first + second moments in bf16) consumes ~940GB of GPU memory. PowerStep reduces this to ~470GB (half-precision single moment), or ~118GB with int8 quantization. For researchers without access to large GPU clusters, this directly expands the model scale that is trainable on a fixed budget.

**Key technical details:**
- Algorithm: ℓp-norm steepest descent with nonlinear momentum transform
- Memory: 50% of Adam (single momentum buffer vs. two); ~12.5% with int8 quantization
- Convergence guarantee: O(1/√T) for non-convex stochastic optimization
- Tested on Transformers: 124M → 235B parameters, no quality degradation
- With int8 quantization: ~8× memory reduction vs. full-precision Adam
- Code: https://github.com/yaolubrain/PowerStep (Apache 2.0)

---

### 4. AntAngelMed: State-of-the-Art Open-Source Medical LLM with 103B MoE — Leads HealthBench with only 6.1B active parameters

**Source:** [MarkTechPost](https://www.marktechpost.com/2026/05/12/meet-antangelmed-a-103b-parameter-open-source-medical-language-model-built-on-a-1-32-activation-ratio-moe-architecture/) | [GitHub](https://github.com/MedAIBase/AntAngelMed) | [Hugging Face](https://hf.co/MedAIBase/AntAngelMed)

AntAngelMed, a joint project from Zhejiang Province Health Information Center, Ant Healthcare, and Zhejiang Anzhen'er Medical AI Technology, is a 103B-parameter Mixture-of-Experts medical language model released under Apache 2.0. The 1/32 activation ratio means only 6.1B parameters are active per token—providing the quality of a ~40B dense model at the inference cost of a 6B model. On H20 hardware, the model exceeds 200 tokens/second, approximately 3× the throughput of 36B dense models.

Training followed a three-stage pipeline: (1) continual pre-training on medical encyclopedias, web text, and academic publications; (2) supervised fine-tuning on multi-source instruction datasets mixing general reasoning with medical scenarios; (3) reinforcement learning via GRPO with task-specific reward models covering diagnostic reasoning, evidence-based recommendations, and clinical risk stratification. The RL stage is responsible for the model's particularly strong performance on hard reasoning cases.

On benchmarks, AntAngelMed ranks first among all open-source models on OpenAI's HealthBench (63.4, vs. 58.9 for the next best open model), with a particularly large lead on the Hard subset (61.2 vs. 53.1). Chinese clinical benchmarks MedAIBench (87.2) and MedBench (84.7) also show substantial margins over prior open models. The model is available on both Hugging Face and ModelScope.

**Key technical details:**
- Architecture: 103B total / 6.1B active, MoE with 1/32 activation ratio
- Hardware throughput: >200 tokens/sec on H20; ~3× faster than 36B dense models
- HealthBench: 63.4 (open-source SOTA); HealthBench-Hard: 61.2
- MedAIBench: 87.2; MedBench: 84.7
- Training: 3-stage (continual pre-train → SFT → GRPO RL)
- License: Apache 2.0
- Available: Hugging Face (MedAIBase/AntAngelMed), ModelScope

---

### 5. G-Zero: Verifier-Free Self-Play for Open-Ended LLM Improvement — Intrinsic reward enables co-evolution without LLM-as-judge

**Source:** [arXiv:2605.09959](https://arxiv.org/html/2605.09959v1)

G-Zero attacks one of the core limitations of self-evolving LLMs: existing self-improvement frameworks work well in verifiable domains (math, code) where ground-truth signals are cheap, but fail in open-ended tasks (instruction following, dialogue, creative writing) where they must rely on LLM-as-judge. The judge introduces a capability ceiling (the model cannot exceed the judge's ability to distinguish quality) and reward hacking (models learn to exploit the judge's stylistic biases).

The key innovation is **Hint-δ**, an intrinsic reward that measures how much a self-generated hint shifts the model's output distribution. Formally, if G(q) is the generator's response to query q and G(q, h) is the response conditioned on hint h produced by the proposer, Hint-δ captures the KL-divergence-like shift between these distributions. Large shift implies the hint contained genuinely new information the model couldn't derive unaided—a proxy for task difficulty and learning signal quality.

The system co-evolves two models: a Proposer (trained via GRPO to find queries/hints that maximally challenge the Generator) and a Generator (optimized via DPO to internalize hint-guided improvements). The paper proves a best-iterate suboptimality guarantee for the idealized DPO variant under conditions on Proposer coverage and data filtration noise bounds. Importantly, this framework requires zero external labeled data—the initial seed is just the base model itself.

**Key technical details:**
- Problem: Self-improvement for open-ended (non-verifiable) tasks
- Reward: Hint-δ = distributional shift between G(q) and G(q, hint), intrinsic and judge-free
- Architecture: Proposer (GRPO) + Generator (DPO), co-evolving with no external data
- Theoretical guarantee: best-iterate suboptimality bound under Proposer coverage + noise conditions
- Eliminates: LLM-as-judge capability ceiling and reward hacking

---

## Deep Dive: Most Important Item

### AlphaEvolve's One-Year Impact Report: Closed-Loop AI-Driven Algorithm Discovery Now a Production Reality

AlphaEvolve earns the "most important" designation not because of any single result but because it represents the clearest evidence yet that AI systems can reliably discover novel algorithms—not just rediscover known ones—across a wide range of rigorous, human-verified domains. One year in, the system has produced results that passed peer scrutiny in genomics, power systems, quantum hardware, and 56-year-old open problems in combinatorics. The closed-loop aspect—where AlphaEvolve also optimized its own training pipeline—marks a qualitative shift from AI as tool to AI as co-developer of AI.

**Architectural foundation.** AlphaEvolve is built on two Gemini models in an asymmetric ensemble: Gemini Flash for high-throughput generation of candidate code variants (breadth of evolutionary search), and Gemini Pro for deep refinement of the most promising candidates (depth). Candidates are evaluated by domain-specific automated verifiers—objective metrics like solver feasibility rates, benchmark accuracy deltas, or numerical error norms. There is no human-in-the-loop evaluation; the evolutionary loop runs autonomously at scale.

**The matrix multiplication result in depth.** The 4×4 complex matrix multiplication case is technically the most significant. A naïve algorithm requires 64 multiplications; Strassen's recursive decomposition uses 49; AlphaEvolve found 48. While Winograd in 1968 also achieved 48 multiplications for real matrices, AlphaEvolve's solution is a rank-48 tensor decomposition over ℂ, which is the noncommutative setting. This matters because tensor decompositions compose recursively: using the decomposition to multiply 4×4 blocks within larger matrices yields an algorithm for N×N matrices with asymptotic cost:

```
T(N) = O(N^(log_4(48))) ≈ O(N^2.7925)
```

vs. Strassen's O(N^2.8074). The improvement compounds: for N=10,000 matrices, this is a ~25% reduction in scalar multiplications. Whether this translates to wall-clock speedups on current hardware depends on cache/memory bandwidth, but the theoretical bound improvement is rigorous.

**The AC Optimal Power Flow result.** The improvement from 14% to 88% feasibility rate on the AC Optimal Power Flow (ACOPF) problem is arguably the most practically consequential. ACOPF governs how electricity grids balance generation and load while respecting physical constraints (voltage limits, line ratings). Current practice uses convex relaxations that often produce infeasible solutions requiring expensive heuristic repair. AlphaEvolve found problem-specific preprocessing transformations that condition the optimization landscape, raising the fraction of cases where modern solvers find globally feasible solutions from 14% to 88%—without changing the solver itself.

**Self-referential improvement.** AlphaEvolve was used to discover more efficient data center scheduling algorithms at Google, reducing compute waste, and to find improvements to its own LLM training pipeline. This is the first publicly documented case of a production AI system materially accelerating its own training through algorithmic discovery. The exact speedup is not disclosed, but DeepMind describes it as "meaningful" relative to prior training runs for Gemini models.

**Open questions:**
- What is the wall-clock speedup of the 4×4 matrix multiplication improvement on current GPU/TPU hardware (as distinct from scalar operation count)?
- Can AlphaEvolve generalize across domains without domain-specific evaluator engineering, or is each deployment still significant manual effort?
- What is the sample efficiency of the evolutionary loop—how many candidate programs are evaluated per successful discovery?
- Does the self-referential training improvement compound over multiple iterations (bootstrapping), and is there a stability ceiling?
- Are there classes of mathematical or algorithmic problems where AlphaEvolve reliably fails?

**Broader significance:** AlphaEvolve represents a proof-of-concept for recursive self-improvement in a narrow but rigorous sense—the system improved the training of the models that power it. Combined with the ACOPF result (with direct energy infrastructure implications), the genomics result (healthcare), and the combinatorics result (pure mathematics), it demonstrates that evolutionary LLM-based program synthesis is now a broadly applicable discovery engine, not a narrow demonstration. The key remaining question is whether the approach scales to problems where automated verification is harder (e.g., novel proofs requiring formal verification), and how much human domain expertise is required to construct the evaluators.

---

## Benchmark Data

```json
[
  {
    "benchmark": "HealthBench (OpenAI Medical)",
    "scale": "full model",
    "results": [
      {"model": "AntAngelMed-103B-MoE", "score": 63.4, "unit": "score"},
      {"model": "Best prior open-source", "score": 58.9, "unit": "score"},
      {"model": "GPT-5.5 (closed)", "score": 72.1, "unit": "score"}
    ],
    "notes": "AntAngelMed is open-source SOTA; 6.1B active params at inference"
  },
  {
    "benchmark": "HealthBench-Hard",
    "scale": "full model",
    "results": [
      {"model": "AntAngelMed-103B-MoE", "score": 61.2, "unit": "score"},
      {"model": "Best prior open-source", "score": 53.1, "unit": "score"}
    ],
    "notes": "8.1-point lead on the hard subset — largest margin on this benchmark"
  },
  {
    "benchmark": "MedAIBench",
    "scale": "full model",
    "results": [
      {"model": "AntAngelMed-103B-MoE", "score": 87.2, "unit": "score"},
      {"model": "Best prior open-source", "score": 79.5, "unit": "score"}
    ],
    "notes": "Chinese clinical benchmark"
  },
  {
    "benchmark": "CyberGym (1,507 real CVEs, 188 projects)",
    "scale": "agentic system",
    "results": [
      {"model": "Microsoft MDASH", "score": 88.45, "unit": "percent"},
      {"model": "Next best (undisclosed)", "score": 83.5, "unit": "percent"}
    ],
    "notes": "MDASH orchestrates 100+ specialized AI agents; 21/21 planted vulns found with 0 false positives"
  },
  {
    "benchmark": "SWE-Bench Pro (agentic coding)",
    "scale": "full model",
    "results": [
      {"model": "Kimi K2.6", "score": 58.6, "unit": "percent"},
      {"model": "Claude Mythos (restricted)", "score": 77.8, "unit": "percent"},
      {"model": "DeepSeek V4 Pro (open)", "score": 62.1, "unit": "percent"}
    ],
    "notes": "Kimi K2.6 released April 21, 2026 with 1T total / 32B active MoE params"
  },
  {
    "benchmark": "AIME 2026",
    "scale": "full model",
    "results": [
      {"model": "Kimi K2.6", "score": 96.4, "unit": "percent"},
      {"model": "GPQA-Diamond (Kimi K2.6)", "score": 90.5, "unit": "percent"}
    ],
    "notes": "Kimi K2.6 open-weight, MIT license; $0.95/M input tokens"
  },
  {
    "benchmark": "Overall Open-Weight LLM Ranking (BenchLM.ai, April 2026)",
    "scale": "composite",
    "results": [
      {"model": "DeepSeek V4 Pro (Max)", "score": 87, "unit": "composite"},
      {"model": "Kimi K2.6", "score": 84, "unit": "composite"},
      {"model": "GLM-5 Reasoning", "score": 83, "unit": "composite"},
      {"model": "Qwen3.5 397B Reasoning", "score": 79, "unit": "composite"}
    ],
    "notes": "Open/closed gap: best open (87) vs. proprietary ceiling (~93) = 6 points"
  },
  {
    "benchmark": "AC Optimal Power Flow feasibility (AlphaEvolve)",
    "scale": "grid optimization",
    "results": [
      {"model": "AlphaEvolve-optimized solver", "score": 88, "unit": "percent feasible"},
      {"model": "Prior state-of-the-art", "score": 14, "unit": "percent feasible"}
    ],
    "notes": "6.3× improvement in solver feasibility rate without changing the solver"
  },
  {
    "benchmark": "Matrix Multiplication (4×4 complex, scalar multiplications)",
    "scale": "algorithmic",
    "results": [
      {"model": "AlphaEvolve", "score": 48, "unit": "scalar multiplications"},
      {"model": "Strassen (1969)", "score": 49, "unit": "scalar multiplications"},
      {"model": "Naïve", "score": 64, "unit": "scalar multiplications"}
    ],
    "notes": "First improvement in 56 years; yields O(N^2.7925) asymptotic vs. Strassen's O(N^2.8074)"
  },
  {
    "benchmark": "Optimizer Memory (Adam relative, 235B Transformer)",
    "scale": "235B parameters",
    "results": [
      {"model": "PowerStep (bf16)", "score": 50, "unit": "% of Adam memory"},
      {"model": "PowerStep (int8)", "score": 12.5, "unit": "% of Adam memory"},
      {"model": "Adam (bf16 baseline)", "score": 100, "unit": "% baseline"}
    ],
    "notes": "No measurable quality degradation; convergence at O(1/sqrt(T)) proven"
  },
  {
    "benchmark": "Star Elastic cost vs. pretraining from scratch",
    "scale": "30B→23B+12B",
    "results": [
      {"model": "Star Elastic (NVIDIA)", "score": 0.28, "unit": "% of scratch cost"},
      {"model": "State-of-the-art compression", "score": 14, "unit": "% of scratch cost"}
    ],
    "notes": "360× reduction over scratch; 7× over best prior compression"
  }
]
```

---

## Architecture / Diagram Notes

### AlphaEvolve Evolutionary Loop
```
Nodes:
  A[Gemini Flash - Breadth Explorer]
  B[Gemini Pro - Depth Refiner]
  C[Candidate Code Population]
  D[Domain-Specific Automated Evaluator]
  E[Fitness Score / Objective Metric]
  F[Evolutionary Selection]
  G[Deployed Algorithm]
Edges: A->C, B->C, C->D, D->E, E->F, F->C, F->G
Labels:
  A->C: [generate N variants]
  B->C: [refine top-k candidates]
  C->D: [execute candidate code]
  D->E: [feasibility rate / error delta / speedup]
  E->F: [selection pressure]
  F->C: [mutation + crossover]
  F->G: [export best solution]
```

### NVIDIA Star Elastic Training Architecture
```
Nodes:
  A[Parent Model - 30B/3.6A Nemotron Nano v3]
  B[Elastification Layer - SSM / Embed / MoE / FFN]
  C[Curriculum-Based Co-Training]
  D[Structured Knowledge Distillation]
  E[Elastic Router - Trainable]
  F[23B/2.8A Submodel]
  G[12B/2.0A Submodel]
  H[QAD - Quantization-Aware Distillation]
  I[NVFP4 / FP8 Nested Checkpoints]
Edges: A->B, B->C, C->D, D->E, E->F, E->G, E->H, H->I
Labels:
  A->B: [slice along 4 axes]
  C->D: [teacher=parent, student=submodel]
  E->F: [route to 23B at inference]
  E->G: [route to 12B at inference]
  E->H: [quantize while preserving nested structure]
```

### PowerStep Optimizer Computation Graph
```
Nodes:
  A[Gradient g_t]
  B[Momentum Buffer m_t - single buffer]
  C[Nonlinear Transform - f_p(m_t)]
  D[Coordinate-Wise Update Signal]
  E[Parameter Update theta_t+1]
  F[int8 Quantizer - optional]
Edges: A->B, B->C, B->F, C->D, D->E, F->D
Labels:
  A->B: [EMA update: m_t = beta*m_{t-1} + (1-beta)*g_t]
  B->C: [p-norm steepest descent transform]
  C->D: [coordinate-wise scale, no 2nd moment stored]
  B->F: [quantize to int8 for 8x memory reduction]
  D->E: [theta_{t+1} = theta_t - lr * D]
```

### G-Zero Co-Evolution Framework
```
Nodes:
  A[Base LLM]
  B[Proposer Model]
  C[Generator Model]
  D[Query Synthesizer]
  E[Hint Generator]
  F[Hint-delta Reward - KL shift measure]
  G[GRPO Training Signal - Proposer]
  H[DPO Training Signal - Generator]
Edges: A->B, A->C, B->D, B->E, C->F, E->F, F->G, F->H, G->B, H->C
Labels:
  B->D: [synthesize challenging queries]
  B->E: [generate informative hints]
  C->F: [compare G(q) vs G(q,hint) distributions]
  E->F: [hint that maximizes distributional shift]
  F->G: [reward proposer for large Hint-delta]
  F->H: [reward generator for internalizing hints]
```

---

## Analysis & Impact for ML Researchers

- **AlphaEvolve signals that program synthesis with LLMs has crossed a threshold.** The combination of verifiable domains + evolutionary search + automated evaluation is now a reproducible template. If your research involves algorithm optimization over discrete or continuous structured spaces (e.g., compiler passes, numerical methods, architecture search), the AlphaEvolve paradigm—Gemini Flash for breadth + Gemini Pro for depth + automated evaluator—is worth adopting or studying closely. The barrier to entry is now primarily the quality of the domain evaluator, not the search methodology.

- **PowerStep is the first memory-efficient Adam substitute with both theory and 235B-scale empirical validation.** If you are training models where optimizer state is a memory bottleneck (anything >70B parameters), PowerStep with int8 quantization is a direct drop-in candidate. The 8× memory reduction means you can train a model 2.8× larger on the same hardware budget while maintaining Adam-equivalent convergence. The open-source code (yaolubrain/PowerStep) is ready to use. Caveat: results are from NVIDIA-affiliated researchers; independent replication at full scale is still needed.

- **NVIDIA Star Elastic changes the economics of multi-size model deployment.** If you need to serve a model family across different hardware tiers (data center GPU vs. edge accelerator vs. mobile NPU), training one Star Elastic checkpoint replaces N separate training runs at 1/360th the compute cost. The elastic budget control result (+16% accuracy, 1.9× lower latency by switching submodels between thinking and answering phases) is directly applicable to any chain-of-thought inference stack. Expect this technique to become standard practice for production LLM deployment in 2026.

- **AntAngelMed establishes a new ceiling for open-source domain-specialized LLMs.** The 103B/6.1A architecture with GRPO RL training is a replicable blueprint for high-quality medical (and likely legal, financial, scientific) domain models that can be self-hosted. For researchers building domain-specific applications: the combination of (a) sparse MoE for inference efficiency, (b) GRPO RL with task-specific reward models, and (c) multi-stage training (continual pre-train → SFT → RL) is currently the strongest known recipe for open-weight domain specialization.

- **The open/closed model gap in general capability has narrowed to ~6 points.** DeepSeek V4 Pro scores 87 vs. the proprietary ceiling of ~93 on BenchLM's composite, and Kimi K2.6 (96.4% on AIME 2026, 90.5% on GPQA-Diamond) is competitive with top closed models on reasoning benchmarks. For researchers choosing a base model: in reasoning-heavy domains, open-weight models are now viable alternatives to closed APIs, with the added benefit of full weight access for fine-tuning, distillation, and mechanistic interpretability.

---

## Key Takeaways (TL;DR)

- **AlphaEvolve improved a 56-year-old matrix multiplication bound** (48 vs. Strassen's 49 for 4×4 complex) and raised AC Optimal Power Flow feasibility from 14% to 88%—one year in, the evolutionary algorithm discovery framework is producing verified, cross-domain breakthroughs.
- **NVIDIA Star Elastic generates 3 model sizes from 1 training run at 360× lower cost** than pretraining from scratch, with +16% accuracy and 1.9× lower latency via elastic budget control at inference time.
- **PowerStep halves Adam optimizer memory and achieves 8× reduction with int8 quantization**, validated up to 235B parameters with O(1/√T) convergence proof—the strongest memory-efficient optimizer result to date.
- **AntAngelMed (103B MoE, 6.1B active, Apache 2.0) leads all open-source models on HealthBench at 63.4**, with a 7-point lead on the Hard subset—the blueprint for domain-specialized open LLMs is now clear.
- **G-Zero eliminates the LLM-as-judge bottleneck** by using an intrinsic Hint-δ reward to enable verifier-free self-play in open-ended tasks—a potential path to self-improvement without human-labeled data.
- **Microsoft MDASH achieved 88.45% on CyberGym** (100+ specialized agents) and found 4 critical Windows RCEs including kernel TCP/IP and IKEv2 vulnerabilities—agentic AI for security has crossed the production-readiness threshold.
- **ICLR 2026 outstanding paper "Transformers are Inherently Succinct"** proves transformers represent formal languages exponentially more compactly than finite automata—and that verifying transformer properties is EXPSPACE-complete.
- **Open-weight models close to within 6 composite points of proprietary leaders**: DeepSeek V4 Pro (87), Kimi K2.6 (84 composite; 96.4% AIME 2026, 58.6% SWE-Bench Pro) are now viable in most research use cases.
