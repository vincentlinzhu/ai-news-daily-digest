# Machine Learning Research — 2026-06-05

> **Note:** CVPR 2026 is in session today (June 5–7, Nashville) — oral presentations and poster sessions are live, with award candidates presenting today. D4RT (4D reconstruction) and SAM 3D (3D object reconstruction, Best Paper Honorable Mention) are both presenting oral sessions and poster sessions today.

---

## Top Stories (5)

### 1. NVIDIA Nemotron 3 Ultra — 550B Open MoE Sets New US Open-Weights Intelligence Record
**Source:** [NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/) | [Artificial Analysis](https://artificialanalysis.ai/articles/nvidia-nemotron-3-ultra-launch-announced) | [MarkTechPost](https://www.marktechpost.com/2026/06/04/nvidia-ai-releases-nemotron-3-ultra-an-open-550b-mixture-of-experts-hybrid-mamba-transformer-for-long-running-agents/)

Released June 4, 2026, NVIDIA Nemotron 3 Ultra is a 550B-parameter Mixture-of-Experts model with 55B active parameters — the largest and most capable US-origin open-weights model available today, scoring 48 on the Artificial Analysis Intelligence Index (next best US open model: Gemma 4 31B at 39). It achieves this while maintaining approximately 5–6× higher inference throughput than comparable open MoE models in its class, a result of three compounding architectural choices: hybrid Mamba-Transformer layers for long-context efficiency, LatentMoE for dense expert routing at lower per-parameter cost, and native NVFP4 quantization enabling a single checkpoint to run on Hopper, Blackwell, and Ampere architectures.

The model's training methodology centers on Multi-Teacher On-Policy Distillation (MOPD) and multi-environment RL — distilling from ten specialized domain-teacher models to produce a generalist that maintains frontier accuracy across coding, reasoning, knowledge, and long-context tasks. Multi-Token Prediction (MTP) heads (2 heads with shared parameters) enable native speculative decoding for low-latency generation and improve model quality modestly during training. The NVFP4 pre-training (E2M1 format with 2D block quantization on weights) is the largest-scale demonstration of stable NVFP4 training to date.

For agentic workloads specifically, Nemotron 3 Ultra reduces per-turn cost by up to 30% compared to models at comparable accuracy — completing long-running agentic tasks faster and cheaper. Its 1M-token context window with a Ruler@1M score of 95% outpaces competitors like Kimi K2.6 (limited to 256K context). The model also achieves the highest non-hallucination score in its comparison set at 78.7 on AA-Omniscience, suggesting materially lower confabulation rates on knowledge tasks.

**Key technical details:**
- Total/active parameters: 550B total / 55B active (~90% sparsity)
- Architecture: Hybrid Mamba-Transformer MoE with LatentMoE routing + 2 MTP heads
- Quantization: NVFP4 (E2M1, 2D block quantization); supports BF16 for full quality
- Context: 1M tokens; Ruler@1M = 95%
- Throughput: 5.9× vs GLM-5.1 on GB200 (8K input / 64K output, TRT-LLM); >300 tokens/sec on pre-release DeepInfra endpoint
- Benchmarks: PinchBench 90.0 | SWE-Bench Verified 71.9 | Terminal Bench 2.1 56.4 | IOI 2025 570.0 (top-3 human competitive programming level) | AA-Omniscience 78.7 | IFBench 82 | Ruler@1M 95%
- AA Intelligence Index: 48 (best US open weights; behind Kimi K2.6 at 54)
- Cost reduction: 30% lower per-turn cost for agentic tasks vs. comparable models
- License: OpenMDW-1.1 (Linux Foundation permissive, full model materials)
- Additional models: Nemotron 3.5 Content Safety 4B guardrail model for multimodal safety classification

---

### 2. MiniMax M3 — First Open-Weight Model with Frontier Coding + 1M Context + Native Multimodality
**Source:** [MiniMax Blog](https://www.minimax.io/blog/minimax-m3) | [Developer Guide](https://lushbinary.com/blog/minimax-m3-developer-guide-benchmarks-pricing-msa-architecture/) | [MSA Architecture Deep Dive](https://huggingface.co/blog/AtlasCloud-AI/minimax-goes-sparse)

Released June 1, 2026 (API live May 31), MiniMax M3 is the first open-weight model to simultaneously deliver: frontier-level coding performance (59.0% SWE-Bench Pro), a 1M-token context window (512K guaranteed minimum), and native multimodal inputs (text, image, video). The key enabling technology is MiniMax Sparse Attention (MSA), an attention architecture that cuts per-token compute at 1M context to 1/20th of the prior generation while retaining quality across the vast majority of capabilities.

MSA's core mechanism is block-level KV-cache selection: instead of quadratic full attention, a lightweight index branch scans incoming tokens, partitions the KV cache into blocks, and selects only the relevant blocks for each query. Critically, MSA operates on uncompressed GQA key-value pairs (unlike latent-compression approaches like MLA), preserving precision and prefix-caching compatibility. The kernel engineering uses a "KV outer gather Q" pattern where KV blocks form the outer loop and all queries hitting a given block are batched together — each block is read from memory exactly once in contiguous access, achieving >4× speedup over open-source alternatives like Flash-Sparse-Attention and flash-moba.

At 1M context, MSA achieves 9.7× faster prefill and 15.6× faster decoding than the prior M2 generation. The decode speedup exceeding prefill speedup is principled: during decode, each query touches only the selected KV blocks, and the effective receptive field is approximately 60K–70K tokens (~6–7% of 1M), consistent with the sparsity rates reported in DeepSeek NSA. On output speed, M3 runs at ~100 tokens/sec, approximately 3× faster than Claude Opus. Weights and technical report are due within 10 days of the June 1 launch; the API is live now at promotional pricing of ~$0.30/M input tokens.

**Key technical details:**
- Architecture: Sparse MoE with MiniMax Sparse Attention (MSA); GQA + single-branch block selection
- Context window: Up to 1M tokens (512K guaranteed minimum)
- MSA speedup at 1M: 9.7× prefill, 15.6× decode vs. prior generation; per-token compute = 1/20 of M2
- MSA effective receptive field: ~60K–70K tokens at 1M context (~6–7% sparsity rate)
- Output speed: ~100 tokens/sec (~3× faster than Claude Opus)
- Benchmarks: SWE-Bench Pro 59.0% | Terminal-Bench 2.1 66.0% | OSWorld-Verified 70.06% | BrowseComp 83.5 | MCP Atlas 74.2% | SWE-fficiency 34.8% | KernelBench Hard 28.8%
- Modalities: Text, image, video input; desktop computer control
- Pricing: ~$0.30/M input tokens (promotional); $1.20/M output tokens (estimated)
- Open weights release: Within 10 days of June 1 launch

---

### 3. CVPR 2026 Best Paper Honorable Mention: SAM 3D — Single-Image 3D Reconstruction at Scale
**Source:** [CVF CVPR 2026](https://cvpr.thecvf.com/virtual/2026/oral/40370) | [Meta AI Research](https://ai.meta.com/research/publications/sam-3d-3dfy-anything-in-images/) | [arXiv:2511.16624](https://huggingface.co/papers/2511.16624)

From Meta AI (Piotr Dollár, Georgia Gkioxari, Jitendra Malik, and 19 co-authors), SAM 3D received a CVPR 2026 Best Paper Honorable Mention — presenting in an oral session today (June 5). SAM 3D is a generative model for visually grounded 3D object reconstruction that predicts geometry, texture, and layout from a single image, extending the Segment Anything Model philosophy to 3D. The key bottleneck it addresses is the 3D data barrier: high-quality labeled 3D geometry data for real-world images has historically been scarce, limiting generalization to in-the-wild scenes with occlusion and clutter.

SAM 3D breaks this barrier with a human- and model-in-the-loop annotation pipeline that generates 3D shape, texture, and pose annotations at unprecedented scale. This data then trains the model through a multi-stage framework combining synthetic pre-training (on clean 3D assets) with real-world alignment fine-tuning. The result is a model that explicitly leverages visual recognition context — understanding what an object is to better infer its unseen geometry — unlike pure geometric-reconstruction approaches.

The gains are substantial: SAM 3D achieves at least a 5:1 win rate over prior state-of-the-art in human preference tests on real-world objects and scenes. It outperforms all baselines on the SA-3DAO benchmark (challenging real-world inputs) and matches or exceeds prior SOTA on ISO3D (isolated object images). Meta plans to release code, model weights, an online demo, and a new in-the-wild 3D reconstruction benchmark.

**Key technical details:**
- Task: Single-image 3D object reconstruction (geometry, texture, layout)
- Architecture: Generative model with unified reconstruction across shape and texture
- Training pipeline: Human + model-in-the-loop annotation → multi-stage (synthetic pretraining + real-world alignment)
- Key insight: Leverages visual recognition context cues (object identity/class) to resolve ambiguous geometry in occluded scenes
- Human preference win rate: ≥5:1 over prior SOTA on real-world images
- Evaluated on: ISO3D (isolated objects), SA-3DAO (challenging real-world)
- Award: CVPR 2026 Best Paper Honorable Mention
- Oral session: June 5, 12:50–1:02 PM PDT; Poster Session 2: 3:00–5:00 PM PDT

---

### 4. CVPR 2026 Award Candidate: D4RT — Unified Feedforward 4D Reconstruction in Real Time
**Source:** [CVF CVPR 2026](https://cvpr.thecvf.com/virtual/2026/events/AwardCandidates2026) | [Project Page](https://d4rt-paper.github.io/) | [arXiv:2512.08924](https://arxiv.org/html/2512.08924)

D4RT (from a Google DeepMind team including Andrew Zisserman, Raia Hadsell, Zoubin Ghahramani, and collaborators) is a feedforward model for 4D dynamic scene reconstruction from a single video, presented as an award candidate at CVPR 2026 in an oral session today (June 5). Its core innovation is a unified transformer architecture that jointly infers depth, spatio-temporal correspondence, and full camera parameters from video — in a single forward pass, without separate task-specific decoders.

The key architectural novelty is a query-based decoder that independently probes 3D position of any point in space and time without dense per-frame decoding. Instead of computing dense feature grids per frame (computationally expensive and memory-intensive), D4RT decouples point queries from the frame grid entirely: any 3D+time coordinate can be queried independently, and inference scales linearly with the number of queried points rather than quadratically with sequence length. This allows the same model to handle depth estimation, 3D point cloud reconstruction, and 3D point tracking in a single unified system.

D4RT achieves state-of-the-art results across a wide spectrum of 4D tasks and shows clear scaling behavior: enlarging both the model and training data yields consistent gains. The flexible query interface also enables selective evaluation — running at high resolution for key frames while sampling sparsely elsewhere — a capability no previous 4D reconstruction model supported cleanly.

**Key technical details:**
- Task: Dynamic 4D reconstruction — depth + spatio-temporal correspondence + camera parameters from video
- Architecture: Unified Transformer with query-based decoder (any (x, y, z, t) point queried independently)
- Key innovation: No dense per-frame decoders; inference scales linearly with number of queried points
- Covers: Depth estimation, 3D point cloud estimation, 3D point tracking — unified in one model
- Scaling behavior: Clear scaling laws with data and model size on tracking accuracy and generalization
- Award: CVPR 2026 Award Candidate (Oral + Highlight designation)
- From: Google DeepMind (Chuhan Zhang, Andrew Zisserman, Raia Hadsell, Zoubin Ghahramani, et al.)

---

### 5. OmniOPD — Logit-Free On-Policy Distillation Enables Black-Box Teacher Transfer
**Source:** [arXiv:2606.01476](https://arxiv.org/html/2606.01476v1) | [Newsference](https://newsference.com/c/arxiv-omniopd-logit-free-on-policy-distillation-via-speculative-v-5711776)

Published May 31/June 2026, OmniOPD proposes a new on-policy distillation (OPD) framework that breaks a fundamental constraint of the standard approach: the requirement for white-box (logit-level) access to the teacher model. Standard OPD supervises students with token-level logit matching — which requires the teacher to expose probability distributions over its entire vocabulary, something no proprietary API provides. OmniOPD replaces this with a logit-free, chunk-level semantic verification signal derived from Monte Carlo rollouts, enabling any black-box model (Claude, Gemini, GPT) to serve as a teacher.

The framework has three technical pillars: (1) Peak-entropy chunk scheduling — instead of querying the teacher at every token, OmniOPD audits only at high-uncertainty decision boundaries in the student's reasoning trajectory, reducing API calls dramatically; (2) Dirichlet-Multinomial Bayesian smoothing — anchors noisy discrete Monte Carlo estimates with the student's base-model prior to reduce variance; (3) Base-model KL anchor — applies a KL divergence constraint on unaudited tokens to prevent policy collapse (ablations show removing this causes catastrophic performance collapse from 69.08% to 8.28%). Together, these yield a gradient signal that is empirically more reliable than token-level logit matching, since logits have high information density but also high noise from token-vocabulary misalignment between teacher and student.

OmniOPD outperforms standard white-box OPD by up to +45.31% relative on mathematical reasoning and +28.64% absolute on math benchmarks, and exceeds self-exploratory RL by up to +18.52% on competitive programming. When paired with stronger proprietary teachers (Claude 4.5-Haiku, Gemini 2.5-Flash), it advances the student model beyond the performance ceiling achievable with open-weight teachers. This positions OmniOPD as a key enabler for the growing trend of capability distillation from frontier API models into open-weight deployable students.

**Key technical details:**
- Problem: Standard OPD requires teacher logits → excludes all proprietary model APIs as teachers
- Solution: Monte Carlo rollout-based semantic similarity estimated over multi-token chunks
- Peak-entropy scheduler: Audits student only at high-uncertainty decision forks (reduces API query budget)
- Bayesian smoothing: Dirichlet-Multinomial prior over discrete MC samples; KL anchor on unaudited tokens
- Ablation: Removing KL anchor collapses performance from 69.08% → 8.28% (policy degeneracy on unsupervised gaps)
- Math gains: +45.31% relative over standard white-box OPD; +28.64% absolute vs. prior SOTA
- Coding gains: +18.52% relative on competitive programming
- Black-box teacher advantage: +9.54% additional relative when using Claude-4.5-Haiku vs. open-weight teacher

---

## Deep Dive: Most Important Item

### NVIDIA Nemotron 3 Ultra — Why This Is the Watershed Moment for US Open-Weights AI

This model matters most because it demonstrates, for the first time, that the US open-weights frontier can achieve near-parity with Chinese-led open-weight models (Kimi K2.6 at 54 vs. 48 on the AA Intelligence Index) while simultaneously delivering inference efficiency that makes it economically practical for production agentic systems. Previous US open-weight releases (GPT-oss-120B, Gemma 4 31B) scored 33 and 39 respectively — there was a significant capability gap. Nemotron 3 Ultra closes the gap substantially and does so while being fully open: weights, data (where redistribution rights exist), training recipes, and software are all released.

**Architecture: Why Hybrid Mamba-Transformer MoE Was the Right Bet**

Standard Transformer attention is quadratic in sequence length, making 1M-token context prohibitively expensive without sparse attention or architectural modifications. Nemotron 3 Ultra addresses this with hybrid Mamba layers — state-space model layers interleaved with standard Transformer attention blocks. Mamba layers have linear complexity in sequence length for the SSM scan, making long-context token processing dramatically cheaper. The MoE structure (550B total / 55B active) provides the parameter capacity of a very large dense model at the inference cost of a 55B model. The combination means the model can handle multi-turn agentic conversations over 1M token contexts without the inference cost explosion that would otherwise make it impractical.

**LatentMoE: Dense Experts at Lower Cost**

Standard granular MoE designs trade hidden-dimension width for number of experts. LatentMoE improves on this by performing expert routing in a compressed latent space, enabling more fine-grained expert specialization at fixed inference cost. NVIDIA reports better accuracy-per-parameter than standard granular MoE designs. The effect: the model can develop more specialized internal circuits for routing across reasoning, code generation, tool calls, and domain-specific logic without paying a linear inference cost premium per expert.

**Multi-Token Prediction (MTP) for Speculative Decoding**

Two MTP heads (with shared parameters during training) allow the model to draft multiple tokens per forward pass. In the inference pipeline, these function as built-in speculation heads — the main model's probability distribution over next tokens can be verified against the MTP draft in a single forward pass. This is architecturally cleaner than external speculative decoding (which requires a separate small draft model) and enables the 5.9× throughput advantage at the 8K-input/64K-output agentic workload profile. The 2-head parameter sharing during training also provides a mild but consistent quality improvement, consistent with prior work (DeepSeek V3's MTP analysis).

**NVFP4 Pre-Training: The Largest Demonstration to Date**

NVFP4 (E2M1 format with 2D block quantization on weights) pre-training at the 550B scale is the largest stable NVFP4 training run yet published. The significance extends beyond this model: it establishes that frontier-scale training can be conducted natively in FP4, enabling Blackwell GPU architectures (GB200) to run training and inference in the same quantization format. This eliminates the calibration and quality degradation risk associated with post-hoc quantization of BF16 models. A single NVFP4 checkpoint runs across Hopper (H100), Blackwell (GB200), and Ampere (A100) without recompilation.

```
Throughput comparison (8K in / 64K out, GB200, TRT-LLM vs vLLM):
Nemotron 3 Ultra (NVFP4): 5.9× GLM-5.1 | 4.8× Kimi K2.6 | 1.6× Qwen-3.5
Note: Nemotron uses TRT-LLM; competitors use vLLM — methodology differs.
```

**Open questions:**
- How does MOPD scale — do more teacher models consistently improve quality, and at what diminishing returns?
- What is the actual quality delta between NVFP4 and BF16 weights across tasks? (Not reported quantitatively)
- How does Nemotron 3 Ultra perform on new safety/alignment benchmarks vs. proprietary frontier models?
- Does LatentMoE routing generalize to new domains not in pre-training, or does it overspecialize?
- Ruler@1M = 95% on synthetic long-context tasks, but real-world long-context agentic performance may differ substantially

**Broader significance:** Nemotron 3 Ultra represents the convergence of four trends that have been developing independently: MoE sparsity for practical large models, linear-complexity SSM layers for long context, native low-precision training for hardware efficiency, and on-policy distillation for quality. The fact that all four can be combined stably at 550B scale, with full openness, changes the equation for enterprise AI: organizations that were previously forced to use proprietary APIs for frontier performance now have a credible open alternative for agentic workloads. The 30% cost-per-task reduction and 5–6× throughput advantage over comparable open models are large enough to change build-vs-buy decisions for production systems.

---

## Benchmark Data

```json
[
  {
    "benchmark": "Artificial Analysis Intelligence Index v4.0",
    "scale": "varies",
    "results": [
      {"model": "Kimi K2.6 (1T params)", "score": 54, "unit": "index points"},
      {"model": "Nemotron 3 Ultra 550B A55B", "score": 48, "unit": "index points"},
      {"model": "Gemma 4 31B", "score": 39, "unit": "index points"},
      {"model": "Nemotron 3 Super", "score": 36, "unit": "index points"},
      {"model": "gpt-oss-120b", "score": 33, "unit": "index points"}
    ],
    "notes": "Composite benchmark: GDPval-AA, tau2-Bench Telecom, Terminal-Bench Hard, SciCode, AA-LCR, AA-Omniscience, IFBench, HLE, GPQA Diamond, CritPt. Nemotron 3 Ultra = best US open-weights model."
  },
  {
    "benchmark": "PinchBench (Agent Productivity)",
    "scale": "frontier models",
    "results": [
      {"model": "Nemotron 3 Ultra 550B", "score": 90.0, "unit": "%"},
      {"model": "Kimi K2.6 (1T)", "score": 91.0, "unit": "%"},
      {"model": "Qwen3.5 (397B)", "score": 89.0, "unit": "%"},
      {"model": "GLM 5.1 (744B)", "score": 84.0, "unit": "%"}
    ],
    "notes": "NVIDIA held-out generalization gate benchmark for agentic productivity; scored once on final model."
  },
  {
    "benchmark": "SWE-Bench Verified",
    "scale": "frontier models",
    "results": [
      {"model": "Nemotron 3 Ultra 550B", "score": 71.9, "unit": "%"},
      {"model": "MiniMax M3", "score": 59.0, "unit": "% (SWE-Bench Pro variant)"}
    ],
    "notes": "Note: SWE-Bench Verified and SWE-Bench Pro are distinct benchmarks; MiniMax reports Pro variant."
  },
  {
    "benchmark": "Terminal-Bench 2.1",
    "scale": "frontier models",
    "results": [
      {"model": "MiniMax M3", "score": 66.0, "unit": "%"},
      {"model": "Kimi K2.6 (1T)", "score": 67.2, "unit": "% (Terminal Bench 2.0)"},
      {"model": "Nemotron 3 Ultra 550B", "score": 56.4, "unit": "%"}
    ],
    "notes": "MiniMax M3 and Kimi K2.6 lead on command-line agentic tasks. Nemotron 3 Ultra score is for Terminal Bench 2.1; NVIDIA table shows 2.0 variant at 54."
  },
  {
    "benchmark": "BrowseComp (Web Browsing & Search)",
    "scale": "frontier models",
    "results": [
      {"model": "MiniMax M3", "score": 83.5, "unit": "points"}
    ],
    "notes": "MiniMax reports BrowseComp score surpasses GPT-5.5 and Gemini 3.1 Pro; no independent validation at launch."
  },
  {
    "benchmark": "OSWorld-Verified (Computer Use)",
    "scale": "frontier models",
    "results": [
      {"model": "MiniMax M3", "score": 70.06, "unit": "%"}
    ],
    "notes": "Vendor-reported; no independent validation at launch."
  },
  {
    "benchmark": "MCP Atlas (Tool Use)",
    "scale": "frontier models",
    "results": [
      {"model": "MiniMax M3", "score": 74.2, "unit": "%"}
    ],
    "notes": "Tool use via Model Context Protocol; vendor-reported."
  },
  {
    "benchmark": "MSA Attention Speedup at 1M context (MiniMax M3)",
    "scale": "1M token context",
    "results": [
      {"model": "MSA vs. prior generation (prefill)", "score": 9.7, "unit": "× speedup"},
      {"model": "MSA vs. prior generation (decode)", "score": 15.6, "unit": "× speedup"},
      {"model": "MSA vs. Flash-Sparse-Attention / flash-moba", "score": 4.0, "unit": "× faster kernel"}
    ],
    "notes": "Per-token compute at 1M context = 1/20 of prior M2 generation. Effective receptive field: ~60K-70K tokens (~6-7% of 1M blocks selected)."
  },
  {
    "benchmark": "Nemotron 3 Ultra Inference Throughput",
    "scale": "GB200 (8K in / 64K out, TRT-LLM)",
    "results": [
      {"model": "vs. GLM-5.1 (vLLM)", "score": 5.9, "unit": "× faster"},
      {"model": "vs. Kimi K2.6 (vLLM)", "score": 4.8, "unit": "× faster"},
      {"model": "vs. Qwen-3.5 (vLLM)", "score": 1.6, "unit": "× faster"},
      {"model": "DeepInfra endpoint (pre-release)", "score": 300, "unit": "tokens/sec"}
    ],
    "notes": "Methodology caveat: Nemotron uses TRT-LLM, competitors use vLLM — not an apples-to-apples comparison."
  },
  {
    "benchmark": "AA-Omniscience (Non-Hallucination)",
    "scale": "frontier models",
    "results": [
      {"model": "Nemotron 3 Ultra 550B", "score": 78.7, "unit": "score (highest in comparison set)"}
    ],
    "notes": "Measures tendency to refuse uncertain knowledge rather than confabulate."
  },
  {
    "benchmark": "OmniOPD Math Reasoning (vs. White-Box OPD Baseline)",
    "scale": "student LLMs",
    "results": [
      {"model": "OmniOPD (open-weight teacher)", "score": 69.08, "unit": "% (average)"},
      {"model": "OmniOPD (Claude-4.5-Haiku teacher) relative gain", "score": 9.54, "unit": "% additional relative gain"},
      {"model": "vs. standard white-box OPD (max gain)", "score": 45.31, "unit": "% relative improvement"},
      {"model": "vs. standard white-box OPD (math, absolute)", "score": 28.64, "unit": "% absolute improvement"},
      {"model": "vs. self-exploratory RL (coding)", "score": 18.52, "unit": "% relative improvement"}
    ],
    "notes": "Ablation: removing base-model KL anchor causes catastrophic collapse from 69.08% to 8.28%."
  },
  {
    "benchmark": "CVPR 2026 SAM 3D Human Preference",
    "scale": "real-world 3D reconstruction",
    "results": [
      {"model": "SAM 3D vs. prior SOTA (win rate)", "score": 5.0, "unit": ":1 win rate"}
    ],
    "notes": "Tested on real-world objects and scenes with occlusion. SA-3DAO (challenging real-world) shows largest gains."
  },
  {
    "benchmark": "Ruler @ 1M (Long-Context Retrieval)",
    "scale": "1M token context",
    "results": [
      {"model": "Nemotron 3 Ultra 550B", "score": 95, "unit": "%"},
      {"model": "Qwen3.5 (397B)", "score": 90, "unit": "%"},
      {"model": "Kimi K2.6", "score": null, "unit": "N/A (max 256K context)"},
      {"model": "GLM 5.1", "score": null, "unit": "N/A (max 256K context)"}
    ],
    "notes": "Nemotron 3 Ultra is one of the few frontier-class models supporting true 1M context."
  }
]
```

---

## Architecture / Diagram Notes

### Nemotron 3 Ultra: Hybrid Mamba-Transformer MoE
```
Nodes:
  IN[Input Tokens]
  EMB[Token Embedding]
  MAMBA[Mamba SSM Layers (linear complexity)]
  ATTN[Transformer Attention Layers]
  GATE[LatentMoE Router (latent-space routing)]
  E1[Expert 1] E2[Expert 2] EN[Expert N (up to K active)]
  MTP[MTP Heads x2 (shared params)]
  OUT[Output Logits + Speculative Draft]

Edges:
  IN→EMB→MAMBA (interleaved) →ATTN (interleaved) →GATE
  GATE→E1, GATE→E2, GATE→EN (select top-K active experts)
  E1→OUT, E2→OUT, EN→OUT
  ATTN→MTP→OUT (parallel draft tokens)

Labels:
  EMB→MAMBA: NVFP4 weights (E2M1, 2D block quant)
  GATE→E1..EN: LatentMoE selects 55B active of 550B total
  MTP→OUT: Native speculative decoding (2 heads)
  MAMBA→ATTN: Interleaved for long-context efficiency (1M tokens)
```

### MiniMax Sparse Attention (MSA) Mechanism
```
Nodes:
  Q[Query Tokens]
  IDX[Index Branch (lightweight scanner)]
  BLOCKS[KV Cache partitioned into blocks B1..Bk]
  SEL[Block Selection (top-k blocks per query group)]
  ATTN_SPARSE[Sparse Attention (selected blocks only)]
  OUT[Output Hidden States]

Edges:
  Q→IDX (scan all tokens)
  IDX→SEL (select relevant block indices)
  BLOCKS→SEL (indexed access)
  SEL→ATTN_SPARSE
  Q→ATTN_SPARSE (GQA groups share selection I)
  ATTN_SPARSE→OUT

Labels:
  Q→IDX: Full-length scan (unavoidable)
  IDX→SEL: ~6-7% of blocks selected at 1M context
  SEL→ATTN_SPARSE: "KV outer gather Q" — each block read once, contiguous
  BLOCKS: Uncompressed GQA KV (not latent-compressed)
  ATTN_SPARSE: Flash-attention kernels reused unchanged
```

### OmniOPD: Logit-Free Distillation Pipeline
```
Nodes:
  STUDENT[Student Model Policy]
  CHUNK_SCHED[Peak-Entropy Chunk Scheduler]
  MC_ROLLOUT[Monte Carlo Rollouts (teacher API)]
  TEACHER[Black-Box Teacher (Claude / Gemini / GPT)]
  BAYES[Dirichlet-Multinomial Bayesian Smoother]
  KL_ANC[Base-Model KL Anchor]
  GRAD[Gradient Update]

Edges:
  STUDENT→CHUNK_SCHED (generate trajectory, track entropy)
  CHUNK_SCHED→MC_ROLLOUT (audit at high-uncertainty decision forks only)
  MC_ROLLOUT→TEACHER (sample multiple rollouts via API)
  TEACHER→BAYES (raw MC estimates of teacher preference)
  BAYES→GRAD (variance-reduced chunk-level signal)
  KL_ANC→GRAD (regularize unaudited tokens to base-model prior)
  GRAD→STUDENT (update policy)

Labels:
  CHUNK_SCHED→MC_ROLLOUT: High-entropy boundary detection (reduces API calls)
  TEACHER→BAYES: Semantic similarity score over multi-token chunks (not logits)
  KL_ANC: β·KL(student || base-model); ablation shows β=0 → collapse
  BAYES: Anchors MC estimates; bounds variance of discrete sampling
```

### SAM 3D: Multi-Stage 3D Reconstruction Training
```
Nodes:
  IMG[Single Input Image]
  VIS_CTX[Visual Recognition Context (object identity)]
  ANNOT[Human+Model-in-Loop Annotation Pipeline]
  SYNTH_DATA[Synthetic 3D Assets]
  SYNTH_PT[Synthetic Pre-training]
  REAL_ALIGN[Real-World Alignment Fine-tuning]
  GEN_MODEL[SAM 3D Generative Model]
  OUT_GEOM[3D Geometry (mesh)]
  OUT_TEX[Texture Map]
  OUT_POSE[Object Pose / Layout]

Edges:
  IMG→VIS_CTX
  VIS_CTX→GEN_MODEL (recognition cues for occluded geometry inference)
  SYNTH_DATA→SYNTH_PT→GEN_MODEL
  ANNOT→REAL_ALIGN→GEN_MODEL
  GEN_MODEL→OUT_GEOM, GEN_MODEL→OUT_TEX, GEN_MODEL→OUT_POSE

Labels:
  ANNOT: Annotates shape+texture+pose at unprecedented scale
  SYNTH_PT→REAL_ALIGN: Two-stage training breaks the 3D data barrier
  VIS_CTX→GEN_MODEL: Key differentiator — uses what object IS to infer unseen geometry
```

---

## Analysis & Impact for ML Researchers

- **If you work on long-context inference or RAG systems:** Nemotron 3 Ultra's Ruler@1M = 95% and 5–6× throughput advantage makes it the first open-weight model practically deployable at 1M context. MSA in MiniMax M3 also demonstrates that GQA block-selection with "KV outer gather Q" is the current hardware-optimal sparse attention design — if you are implementing custom attention kernels, this is the pattern to replicate. The decode speedup exceeding prefill speedup (15.6× vs 9.7×) is a principled result from the different compute profiles during each phase.

- **If you work on knowledge distillation or post-training of smaller models:** OmniOPD removes the last major barrier to using proprietary API models as teachers — the logit access requirement. The 5:1 importance ratio of the base-model KL anchor (its removal causes catastrophic collapse from 69% → 8%) is a critical engineering insight: sparse supervision signals over long trajectories require explicit regularization on unaudited tokens or the policy degenerates. Read arXiv:2606.01476 and the associated survey at arXiv:2604.00626 for the full taxonomy.

- **If you work on 3D computer vision or reconstruction:** SAM 3D (CVPR 2026 Honorable Mention) and D4RT (Award Candidate) together represent the new frontier of 3D/4D reconstruction: both use a unified Transformer architecture, both break away from task-specific decoders, and both demonstrate that scale (data and model size) drives consistent gains. The key takeaway from D4RT is that query-based decoders with linear scaling are strictly preferable to dense per-frame decoders for 4D tasks — this architectural principle will likely transfer broadly.

- **If you work on agentic benchmarking or evaluation methodology:** Nemotron 3 Ultra scored 90.0 on PinchBench and 56.0 on ProfBench (Search), both held-out benchmarks that NVIDIA says were scored only once on the final model. This is the right evaluation methodology given the Berkeley RDI audit findings on benchmark exploitability published last week. Researchers should now treat any model score on SWE-Bench Verified, GAIA, or Terminal-Bench as potentially inflated; prefer FeatureBench, SWE-Bench Pro, or held-out proprietary evaluations like PinchBench where available.

- **If you work on training efficiency or optimizer research:** The NVFP4 pre-training at 550B scale is a landmark result — it establishes that E2M1 format with 2D block quantization is stable at frontier scale. Combined with last week's MaxRL (ICML 2026 Oral) showing 7.9–19.2× test-time scaling efficiency gains over GRPO/REINFORCE, and the MONA optimizer achieving SOTA at 68B MoE + 1T tokens, the training stack is changing rapidly. The convergence of native FP4 training, LatentMoE routing, and on-policy distillation suggests the next generation of open models will need all three to be competitive.

---

## Key Takeaways (TL;DR)

- **NVIDIA Nemotron 3 Ultra (550B/55B active)** sets a new US open-weights intelligence record at 48 on the AA Intelligence Index, 5–6× faster throughput than comparable open models, and 30% lower per-agentic-task cost — fully open including weights, data, and recipes under OpenMDW-1.1.
- **MiniMax M3's MSA architecture** achieves 9.7× faster prefill and 15.6× faster decode at 1M context by selecting only ~6–7% of KV blocks per query, with per-token compute = 1/20 of the prior generation — the most efficient true-1M-context architecture published to date.
- **CVPR 2026 is live today** (June 5–7, Nashville) with oral sessions presenting SAM 3D (CVPR Best Paper Honorable Mention, Meta AI) and D4RT (Award Candidate, Google DeepMind) — both redefining 3D/4D reconstruction with unified Transformer architectures.
- **OmniOPD** enables black-box proprietary models (Claude, Gemini) to serve as on-policy distillation teachers without logit access, yielding +45% relative gains over white-box OPD on math — the KL anchor on unaudited tokens is essential (removal causes 69% → 8% collapse).
- **Humanoid-GPT** (CVPR 2026, arXiv:2606.03985) scales humanoid motion tracking to 2B training frames and shows clear scaling laws — the first GPT-style causal Transformer for whole-body humanoid control with zero-shot generalization to unseen motions on the Unitree G1.
- **MiniMax M3** is the first open-weight model unifying frontier coding (SWE-Bench Pro 59.0%), 1M context, and native multimodality (text/image/video + computer use); weights and technical report due within 10 days.
- **OmniVGGT, MoRe, Scal3R, and D4RT** at CVPR 2026 signal that feedforward, feed-everything 4D reconstruction is now the dominant paradigm in 3D vision — encoder-decoder separation and task-specific decoders are being retired in favor of unified query-based models.
- **The US open-weights ecosystem is converging rapidly** with Nemotron 3 Ultra, MiniMax M3, Mellum2, and Holo3.1 all landing this week — each targeting a distinct deployment profile (agentic orchestration, long-context, code-specialized, and computer-use respectively).
