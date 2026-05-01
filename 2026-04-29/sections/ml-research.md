# ML Research — 2026-04-29

> **Coverage window:** New papers, releases, and conference news published April 28–29, 2026. Items reported in the 2026-04-28 digest are excluded unless there is material new information.

---

## Top Stories

### 1. ICLR 2026 Wraps in Rio — Outstanding Papers Announced

ICLR 2026 concluded April 23–27, 2026 in Rio de Janeiro, Brazil, with 5,355 accepted papers from 19,525 submissions (27.4% acceptance). The Outstanding Paper Committee—chaired by Gautam Kamath with 11 co-members from Stanford, McGill, Cornell, Weizmann, and others—recognized two Outstanding Papers and one Honorable Mention after a five-week, three-phase expert-review process.

**Outstanding Paper 1: "Transformers are Inherently Succinct"**
- Authors: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ) | [arXiv:2510.19315](https://arxiv.org/abs/2510.19315)
- **What it proves:** Transformers can represent formal languages *substantially more succinctly* than RNNs, finite automata, and Linear Temporal Logic formulas. "Succinctness" is measured as the smallest denotational size of the transformer needed to recognize a language. The flip side is stark: verifying even simple properties of transformers is EXPSPACE-complete, meaning analysis is provably harder than for equivalent classical models.
- **Why it matters:** Provides the first principled theoretical explanation for *why* transformers outperform alternatives—not just expressiveness but compactness of representation. Expected to catalyze a wave of theoretical follow-up work.

**Outstanding Paper 2: Multi-Turn LLM Evaluation (Salesforce AI Research)**
- Authors: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ)
- **Core finding:** LLMs trained largely on single-turn completions show marked degradation in aptitude and reliability under multi-turn, underspecified-instruction interactions—the exact conditions of real-world deployment. The paper introduces a scalable evaluation methodology and shows the gap is non-trivial even on state-of-the-art models.
- **Significance:** The committee called the experimental design "exceptional," noting the findings directly reveal a systemic optimization blind spot in current RLHF/preference-tuning pipelines.

**Honorable Mention: "The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm"**
- Authors: Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- [OpenReview](https://openreview.net/forum?id=yRtgZ1K8hO)
- **What it does:** Uses approximation theory to design optimal polynomial approximations for the polar decomposition—the key subroutine in the popular Muon optimizer. Unlike classical numerical methods, Polar Express is GPU-native, uses only matrix-matrix multiplications, and runs stably in `bfloat16`. The method solves a minimax optimization at each iteration for worst-case convergence guarantees.
- **Results:** Consistent validation-loss improvements training GPT-2 on 1–10B tokens from FineWeb compared to prior matrix-sign alternatives.
- **Context:** Muon has emerged as a leading optimizer for LLM pre-training; principled theoretical grounding for its core operation is overdue.

**ICLR 2026 Test of Time Awards** (papers from ICLR 2016):
- **DCGAN** (Radford, Metz, Chintala): recognized as the paper that started learned image generation as a subfield.
- **DDPG** (Lillicrap et al.): recognized as the first RL algorithm to translate raw sensor data to continuous physical actions at scale.

---

### 2. IBM Granite 4.1 Family Released — 8B Matches Prior 32B MoE

IBM released the Granite 4.1 family on April 29, 2026 — its most expansive release to date spanning language, vision, speech, embedding, and Guardian (safety) models.

- **Blog:** [research.ibm.com/blog/granite-4-1-ai-foundation-models](https://research.ibm.com/blog/granite-4-1-ai-foundation-models)
- **License:** Apache 2.0

**Architecture & Training:**
- Dense decoder-only language models at 3B, 8B, and 30B parameter sizes
- ~15 trillion training tokens across multi-phase curriculum: broad pre-training → staged refinement toward technical, scientific, and mathematical data
- Context window: **512K tokens**
- Post-training: supervised fine-tuning + multi-stage RL targeting four distinct capability axes: instruction adherence, conversation quality, factual accuracy, and mathematical reasoning

**Benchmark Results:**

| Benchmark | granite-4.1-3b | granite-4.1-8b | granite-4.1-30b |
|---|---|---|---|
| MMLU (5-shot) | 67.02 | 73.84 | 80.16 |
| IFEval Avg | 82.30 | 87.06 | 89.65 |
| GSM8K (8-shot) | 86.88 | 92.49 | 94.16 |
| HumanEval (pass@1) | 79.27 | 87.20 | 89.63 |

**Key headline:** Granite 4.1 8B-Instruct matches or outperforms Granite 4.0 32B MoE across enterprise benchmarks—a significant efficiency win that also simplifies deployment (no routing overhead).

The release also includes multimodal components: Granite 4.1 Speech (industry-leading transcription), Vision (document + image understanding), Guardian (harm detection, compliance), and Embedding models.

---

### 3. NVIDIA Nemotron 3 Nano Omni — Omnimodal MoE at 30B-A3B

Released April 28, 2026, Nemotron 3 Nano Omni is NVIDIA's fully open omnimodal model supporting text, images, video, and audio in a unified architecture.

- **HuggingFace blog:** [huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence)
- **Tech blog:** [developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning...](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/)
- **arXiv:** [2604.24954](https://arxiv.org/html/2604.24954)

**Architecture:**
- 30B total parameters / ~3B active (hybrid Mamba-Transformer MoE backbone)
- Vision encoder: C-RADIOv4-H
- Audio encoder: Parakeet-TDT-0.6B-v2
- Context length: **256K tokens** (extended from 128K in prior version)
- Dynamic image resolution + Conv3D temporal video compression (2× temporal token reduction)
- Quantization support: BF16, FP8, NVFP4 (Ampere, Hopper, Blackwell)
- Inference engines: vLLM and TensorRT-LLM

**Selected Benchmark Results:**

| Domain | Benchmark | Score |
|---|---|---|
| Document Understanding | OCRBenchV2-En | 65.8 |
| Document Understanding | MMlongbench-Doc | 57.5 |
| Chart Reasoning | CharXiv reasoning | 63.6 |
| GUI/Screen | ScreenSpot-Pro | 57.8 |
| GUI/Screen | OSWorld | 47.4 |
| Video efficiency | MediaPerf | #1 throughput, lowest cost |

**Efficiency:** 9× higher throughput and 2.9× faster single-stream reasoning vs. Nemotron Nano V2 VL. Available in BF16, FP8, and NVFP4 checkpoints on HuggingFace.

---

### 4. ScaleRL (Meta / ICLR 2026 Oral): Principled RL Scaling with 400K GPU-Hours

*"The Art of Scaling Reinforcement Learning Compute for LLMs"* was presented as an ICLR 2026 oral, representing the most systematic RL scaling study to date.

- [OpenReview](https://openreview.net/forum?id=FMjeC9Msws)
- **Scale:** >400,000 GPU-hours of experiments

**Core Methodology:**
- Fit sigmoidal compute-performance curves across RL training runs
- Ablate design choices (loss aggregation, normalization, curriculum, off-policy algorithms) to separate their impact on *asymptotic performance* vs. *compute efficiency*

**Three Main Findings:**
1. Different recipes yield different asymptotic performance ceilings — recipe matters as much as compute.
2. Design details like normalization and curriculum primarily shift where on the curve you land per GPU-hour, *not* the ceiling.
3. Stable, scalable recipes follow **predictable scaling trajectories** — curves from small runs extrapolate reliably to large runs.

**ScaleRL Recipe Results:**
- Asymptotic reward: **0.61**, surpassing DeepSeek GRPO, Qwen-2.5 DAPO, Magistral, and MiniMax-M1
- Demonstrated accurate extrapolation up to 100K GPU-hours on an 8B dense model and 50K GPU-hours on a 17Bx16 MoE model
- Provides practitioners a principled playbook: measure the sigmoidal curve at small scale → extrapolate → allocate compute confidently

---

### 5. Nucleus-Image: First Open-Source Sparse MoE Diffusion Model

Released April 14–15, 2026 — included here as the definitive open-weight result in generative image modeling for this week.

- **arXiv:** [2604.12163](https://arxiv.org/abs/2604.12163)
- **HuggingFace:** [huggingface.co/papers/2604.12163](https://huggingface.co/papers/2604.12163)
- **Blog:** [huggingface.co/blog/NucleusAI/nucleus-image](https://huggingface.co/blog/NucleusAI/nucleus-image)
- **License:** Apache 2.0

**Architecture:** 17B-parameter sparse MoE diffusion transformer — 64 routed experts per layer, ~2B parameters active per forward pass. Key innovations:

1. **Decoupled routing:** Separates timestep-aware expert *assignment* from timestep-conditioned expert *computation*, preventing routing collapse across denoising timesteps.
2. **Text KV sharing:** Text tokens bypass the transformer backbone entirely and contribute only as keys/values in joint attention — enables full text KV caching across denoising steps.
3. **Expert-Choice Routing:** Each expert selects its preferred tokens rather than each token choosing experts, improving load balance.
4. **Progressive training curriculum:** Three-stage resolution progression: 256 → 512 → 1024 pixels with progressive sparsification.

**Results (no RL or preference tuning):**

```json
{
  "model": "Nucleus-Image",
  "params_total": "17B",
  "params_active": "~2B",
  "GenEval": 0.87,
  "DPG-Bench": 88.79,
  "OneIG-Bench": 0.522,
  "comparisons": ["Qwen-Image", "GPT Image 1", "Seedream 3.0", "Imagen 4"]
}
```

Nucleus-Image matches or exceeds all four comparators on all three benchmarks — achieved *without* RL or DPO fine-tuning.

---

## Deep Dive: ICLR 2026 Notable Orals

Beyond the award papers, several oral presentations are worth tracking:

### Pre-training Under Infinite Compute
- **Authors:** Konwoo Kim, Suhas Kotha, Percy Liang, Tatsunori Hashimoto (Stanford)
- **arXiv:** [2509.14786](https://arxiv.org/abs/2509.14786)
- **Problem:** What is optimal pre-training when compute grows faster than available web data?
- **Key results:**
  - Optimal weight decay is **30× larger** than standard practice when training multiple epochs
  - Ensemble scaling monotonically decreases loss along a power law in parameter count
  - Distilling ensembles into 8× smaller students retains 83% of ensembling benefit
  - Achieves **5.17× data efficiency** improvement at 200M tokens; **17.5× data efficiency** on math tasks vs. continued pre-training
- **Significance:** As high-quality web text plateaus, this paper provides the roadmap for squeezing maximum capability from fixed data budgets.

### AgentGym-RL: Multi-Turn RL for Long-Horizon Agents
- **arXiv:** [2509.08755](https://arxiv.org/abs/2509.08755)
- **GitHub:** [github.com/WooooDyy/AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL)
- **Core contribution:** An open-source framework for training LLM agents through multi-turn RL across web navigation, deep search, and digital game environments.
- **ScalingInter-RL training strategy:**
  1. Start with short-horizon interactions to establish foundational policies
  2. Progressively expand interaction horizon to encourage deeper exploration
  3. Balance exploration-exploitation by relaxing constraints as training matures
- **Results:** Agents match or surpass OpenAI o3 and Gemini-2.5-Pro across 27 diverse tasks.

### MesaNet: Sequence Modeling via Locally Optimal Test-Time Training
- **arXiv:** [2506.05233](https://arxiv.org/abs/2506.05233)
- **What it is:** A chunkwise parallelizable sequence model where each position minimizes an in-context regression objective to *optimality* using a fast conjugate gradient solver, rather than approximating it with online learning rules (as in DeltaNet, Mamba, xLSTM).
- **Results:** Lower language modeling perplexity and higher downstream benchmark scores vs. prior RNNs, especially on long-context tasks — at the cost of additional inference FLOPs.
- **Theoretical position:** Unifies and strictly generalizes linearized attention approaches; positions the "solve to optimality" principle as the principled limit of the TTT family.

---

## Architecture & Training Notes

### Three-Phase Transformer (3PT)
- **arXiv:** [2604.14430](https://arxiv.org/abs/2604.14430) | April 15, 2026
- **Author:** Mohammad R. Abu Ayyash

A minimal structural prior for decoder-only transformers that partitions the d_model residual stream into N=3 equally-sized cyclic channels:

- **PhaseRotationLayer:** 2D Givens rotation inserted between attention and FFN, rotating each channel by θ + i·(2π/3), forming a balanced AC-like phase structure
- **PhaseAwareRMSNorm:** Per-channel RMSNorm applied independently
- **Phase-aligned GQA:** Attention heads aligned to channel partition
- **Gabriel's Horn DC injection:** Fixed r(p) = 1/(p+1) absolute position signal, orthogonal to RoPE's relative-position component

**Results at 123M params on WikiText-103:**
- 7.20% perplexity reduction (−2.62% bits-per-byte) vs. RoPE-only baseline
- 1.93× step-count convergence speedup (1.64× wall-clock)
- +1,536 trainable parameters (0.00124% of total)

The design is motivated by the unique mathematical property of three-phase AC systems: three sinusoids 120° apart sum to zero with no anti-correlated pair—only three achieves both properties among small integers.

### KV Cache and Inference Efficiency: Three Papers

**SparKV** (arXiv:2604.21231) — overhead-aware KV cache loading for on-device LLM inference. Adaptively decides whether to stream KV chunks from cloud or recompute locally. Reduces Time-to-First-Token by 1.3–5.1× and per-request energy by 1.5–3.3×.

**Flux Attention** (arXiv:2604.07394) — context-aware hybrid attention routing each layer dynamically to Full or Sparse Attention. Achieves 2.8× prefill speedup and 2.0× decode speedup with only 12 GPU-hours of training on 8×A800s.

**HybridKV** (arXiv:2604.05887) — multimodal LLM KV compression via head-type classification (static vs. dynamic). Up to 7.9× KV memory reduction and 1.52× faster decoding on multimodal benchmarks.

---

## RL Training Advances

### IsoCompute Playbook: Optimal Sampling Compute for LLM RL
- **arXiv:** [2603.12151](https://arxiv.org/abs/2603.12151)
- **Authors:** Zhoujun Cheng et al., UC San Diego, CMU, MBZUAI
- **Submitted to ICLR 2026**

Studies how to allocate compute across three axes in on-policy RL: parallel rollouts per problem (n), problems per batch (B_p), and sequential iterations (M) — total compute C = B_p · n · M.

**Key prescriptions:**
1. Optimal n increases predictably with total compute budget, then saturates — don't over-parallelize at small budgets.
2. B_p has marginal effect in a moderate range; prioritize larger B_p at low budgets, shift to larger n at high budgets.
3. Easy and hard problems follow similar scaling curves but through different mechanisms: *solution sharpening* on easy problems, *coverage expansion* on hard problems.

**Batched Contextual Reinforcement / Task-Scaling Law** (arXiv:2604.02322, April 2, 2026): A complementary finding — as concurrent problems N increases during inference, per-problem token usage decreases monotonically while accuracy degrades more gracefully than baselines. Measured 15.8–62.6% token reduction while maintaining or improving accuracy on math benchmarks.

---

## Synthetic Data Research

### FinePhrase: 486B-Token Synthetic Pretraining Dataset
- **Dataset:** [huggingface.co/datasets/HuggingFaceFW/finephrase](https://huggingface.co/datasets/HuggingFaceFW/finephrase)
- **Paper:** [How Can We Synthesize High-Quality Pretraining Data?](https://arxiv.org/abs/2604.13977) (arXiv:2604.13977)

HuggingFace released the largest systematic synthetic pretraining study to date:
- **90 controlled experiments** generating >1 trillion tokens to identify the critical factors
- **12.7 GPU-years** of compute invested
- **Key finding:** Structured output formats consistently outperform curated web baselines. The four best-performing prompt families: **FAQ**, **Math problems**, **Tables**, **Tutorials**. Increasing generator model size *beyond 1B parameters provides no additional benefit*.
- **FinePhrase dataset:** 486B tokens, generated via SmolLM2-1.7B-Instruct rephrasing FineWeb-Edu content. Outperforms all prior synthetic baselines while reducing generation cost by up to **30×**.

```json
{
  "dataset": "FinePhrase",
  "tokens": "486B",
  "generator_model": "SmolLM2-1.7B-Instruct",
  "source": "FineWeb-Edu",
  "formats": ["FAQ", "Math", "Table", "Tutorial"],
  "cost_reduction_vs_baselines": "up to 30x",
  "performance": "outperforms all existing synthetic baselines"
}
```

### Multi-Turn Underspecification: Confirmed Across SOTA Models
The ICLR 2026 Outstanding Paper from Salesforce establishes that the multi-turn degradation is not limited to older models — the methodology is designed to generalize to state-of-the-art systems and the conclusions hold.

---

## Benchmark Data

```json
{
  "date": "2026-04-29",
  "benchmarks": [
    {
      "model": "Granite 4.1 8B Instruct",
      "GSM8K_8shot": 92.49,
      "HumanEval_pass1": 87.20,
      "MMLU_5shot": 73.84,
      "IFEval_avg": 87.06,
      "note": "Matches Granite 4.0 32B MoE"
    },
    {
      "model": "Granite 4.1 30B Instruct",
      "GSM8K_8shot": 94.16,
      "HumanEval_pass1": 89.63,
      "MMLU_5shot": 80.16,
      "IFEval_avg": 89.65
    },
    {
      "model": "Nemotron 3 Nano Omni (30B-A3B)",
      "OCRBenchV2_En": 65.8,
      "MMlongbench_Doc": 57.5,
      "CharXiv_reasoning": 63.6,
      "ScreenSpot_Pro": 57.8,
      "OSWorld": 47.4,
      "note": "9x throughput vs prior version"
    },
    {
      "model": "Nucleus-Image (17B / ~2B active)",
      "GenEval": 0.87,
      "DPG_Bench": 88.79,
      "OneIG_Bench": 0.522,
      "note": "No RL or DPO fine-tuning"
    },
    {
      "model": "ScaleRL Recipe (8B dense)",
      "asymptotic_reward": 0.61,
      "comparators_beaten": ["DeepSeek GRPO", "Qwen-2.5 DAPO", "Magistral", "MiniMax-M1"]
    }
  ]
}
```

---

## Analysis & Impact

**1. ICLR's Two Outstanding Papers Reveal Orthogonal Gaps**
The committee's choices signal what the research community considers genuinely under-addressed. "Transformers are Inherently Succinct" fills a foundational theory gap — after a decade of empirical dominance, there is now a formal argument for *why* transformers win on expressiveness. The multi-turn evaluation paper fills an empirical methodology gap: models are being optimized for single-turn benchmarks while being deployed in multi-turn settings. Both findings have immediate downstream implications for how practitioners think about architecture choice and evaluation design.

**2. The Muon Optimizer Is Becoming Mainstream**
The Polar Express Honorable Mention signals that Muon is no longer a niche research curiosity. Two ICLR 2026 papers engaged with it directly (Polar Express and the broader optimizer landscape), and its polar decomposition step is now receiving the same treatment classically reserved for SGD and Adam's foundational components — formal optimality analysis, hardware-aware implementation, and precision-aware polynomial approximation. Expect Muon to appear in more large-scale training runs in 2026 H2.

**3. Sparse MoE Has Crossed Into Image Generation**
Nucleus-Image is a meaningful inflection point: sparse MoE architecture, long dominant in language (Mixtral, DeepSeek, Nemotron), has now produced a fully open-source, frontier-quality image generation model. The decoupled routing design solving the timestep-collapse problem may become a template for future MoE diffusion work.

**4. RL Scaling Is Now a Principled Engineering Discipline**
Between ScaleRL (400K GPU-hours, sigmoidal curve fitting) and IsoCompute (prescriptive compute-allocation rules), the field has moved from empirical intuition to principled methodology for RL post-training at scale. The key insight that *design choices affect compute efficiency but not asymptotic performance* gives practitioners a clear optimization target: find the stable recipe first, then scale.

**5. Pre-Training Data Efficiency Is the Next Frontier**
Both FinePhrase and "Pre-training under Infinite Compute" address the same constraint from different angles: web text is saturating. FinePhrase shows that synthetic reformatting at 1B-model scale can generate 486B tokens that outperform curated web data at 30× lower cost. "Infinite Compute" shows that ensemble distillation and aggressive regularization can squeeze 17.5× more mathematical capability from the same data. Together, these suggest that the next generation of pre-training will be defined less by raw data volume and more by data curation methodology and multi-epoch training discipline.

**6. IBM Granite 4.1 Resets the Enterprise Efficiency Bar**
An 8B model matching a 32B MoE on enterprise benchmarks — with 512K context, multi-stage RL, and Apache 2.0 licensing — makes Granite 4.1 8B-Instruct a strong default for enterprises constrained by deployment cost. The release of Guardian, Speech, and Vision components in the same family lowers integration complexity for multi-modal enterprise workflows.

---

## Key Takeaways TL;DR

1. **ICLR 2026** crowned two Outstanding Papers: transformers are provably succinct (and verifying them is EXPSPACE-hard), and LLMs degrade markedly in multi-turn underspecified settings — a systematic training gap.
2. **IBM Granite 4.1** (Apache 2.0, 3B–30B, 512K context) ships an 8B model that matches the prior 32B MoE on enterprise benchmarks, with multi-stage RL post-training.
3. **Nemotron 3 Nano Omni** (30B-A3B MoE, open) unifies text/image/video/audio at 9× prior throughput with 256K context — the most capable open omnimodal model yet.
4. **ScaleRL** from Meta (400K GPU-hours, ICLR oral) establishes sigmoidal compute-performance curves as the standard framework for RL scaling; recipe selection determines the asymptote, compute determines where on the curve you land.
5. **Nucleus-Image** (17B MoE / 2B active, Apache 2.0) is the first open-source frontier image generation model with sparse MoE architecture, matching GPT Image 1 and Imagen 4 without RL fine-tuning.
6. **FinePhrase** (486B tokens, HuggingFace) establishes that structured reformatting at 1B-scale generators outperforms curated web data at 30× lower cost — redefining pre-training data strategy.
7. **The Muon optimizer** received formal theoretical treatment at ICLR 2026 (Polar Express Honorable Mention), signaling its transition from research novelty to production optimizer.
8. **Pre-training under Infinite Compute** (Stanford, ICLR oral) shows 17.5× math data efficiency and 30× higher optimal weight decay than standard practice — critical guidance as web text plateaus.

---

## Sources

| # | Source | URL |
|---|---|---|
| 1 | ICLR 2026 Outstanding Papers announcement | https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/ |
| 2 | Transformers are Inherently Succinct (OpenReview) | https://openreview.net/forum?id=Yxz92UuPLQ |
| 3 | Transformers are Inherently Succinct (arXiv) | https://arxiv.org/abs/2510.19315 |
| 4 | The Polar Express (OpenReview) | https://openreview.net/forum?id=yRtgZ1K8hO |
| 5 | ICLR 2026 Test of Time Awards | https://blog.iclr.cc/2026/04/22/announcing-the-test-of-time-awards-from-iclr-2016/ |
| 6 | IBM Granite 4.1 Blog | https://research.ibm.com/blog/granite-4-1-ai-foundation-models |
| 7 | IBM Granite 4.1 (Agent Times) | https://theagenttimes.com/articles/ibm-releases-granite-4-1-8b-under-apache-2-0-for-local-agent-ecc5b5f4 |
| 8 | Nemotron 3 Nano Omni (NVIDIA Tech Blog) | https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/ |
| 9 | Nemotron 3 Nano Omni (HuggingFace) | https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence |
| 10 | Nemotron 3 Nano Omni (arXiv) | https://arxiv.org/html/2604.24954 |
| 11 | ScaleRL (OpenReview) | https://openreview.net/forum?id=FMjeC9Msws |
| 12 | Nucleus-Image (arXiv) | https://arxiv.org/abs/2604.12163 |
| 13 | Nucleus-Image (HuggingFace blog) | https://huggingface.co/blog/NucleusAI/nucleus-image |
| 14 | Pre-training under Infinite Compute (arXiv) | https://arxiv.org/abs/2509.14786 |
| 15 | Pre-training under Infinite Compute (OpenReview) | https://openreview.net/forum?id=ck0aZTAnwK |
| 16 | AgentGym-RL (arXiv) | https://arxiv.org/abs/2509.08755 |
| 17 | AgentGym-RL (GitHub) | https://github.com/WooooDyy/AgentGym-RL |
| 18 | MesaNet (arXiv) | https://arxiv.org/abs/2506.05233 |
| 19 | Three-Phase Transformer (arXiv) | https://arxiv.org/abs/2604.14430 |
| 20 | FinePhrase dataset (HuggingFace) | https://huggingface.co/datasets/HuggingFaceFW/finephrase |
| 21 | FinePhrase paper (arXiv) | https://arxiv.org/abs/2604.13977 |
| 22 | IsoCompute Playbook (arXiv) | https://arxiv.org/abs/2603.12151 |
| 23 | Batched Contextual Reinforcement (arXiv) | https://arxiv.org/abs/2604.02322 |
| 24 | SparKV (arXiv) | https://arxiv.org/abs/2604.21231 |
| 25 | Flux Attention (arXiv) | https://arxiv.org/abs/2604.07394 |
| 26 | HybridKV (arXiv) | https://arxiv.org/abs/2604.05887 |
| 27 | ICLR 2026 Conference Overview (Bohrium) | https://www.bohrium.com/blog/research-notes/iclr-2026-accepted-papers-highlights/ |
