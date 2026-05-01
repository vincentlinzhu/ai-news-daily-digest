# ML Research — 2026-04-30

---

## Top Stories

### 1. DeepSeek V4 Pro: 1.6T Parameters, 1M Context, Open Source — and Trained on Huawei Chips
**Released April 24, 2026** | [HuggingFace Blog](https://huggingface.co/blog/deepseekv4) | [Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

DeepSeek's V4 Pro is the week's most architecturally significant open-source release. At 1.6 trillion total parameters with 49 billion active per token, it introduces two novel attention mechanisms that fundamentally change the efficiency calculus for long-context inference:

- **Compressed Sparse Attention (CSA):** Compresses KV entries by 4× via softmax-gated pooling.
- **Heavily Compressed Attention (HCA):** Compresses KV entries by 128× using dense attention over the compressed stream.

These alternate across the 61-layer stack with sliding-window attention for recent tokens. The result: at 1M token context, V4 Pro uses only **27% of single-token inference FLOPs** and **10% of KV cache** compared to DeepSeek-V3.2 — roughly 2% of the KV cache of standard GQA architectures.

Additional architecture choices:
- **Manifold-Constrained Hyper-Connections (mHC):** Replaces standard residual skip connections with learned manifold projections, improving gradient flow through the very deep stack.
- **Muon Optimizer** (not AdamW): Orthogonalizes gradient updates to remove inter-direction correlations, enabling more stable training at this parameter scale.
- **384 routed experts + 1 shared**, with 6 active per token; trained on 32–33 trillion tokens, largely on Huawei Ascend 950PR chips (not NVIDIA).

**Benchmark highlights:**
| Benchmark | V4 Pro | Notes |
|---|---|---|
| SWE-bench Verified | 80.6% | Matches Gemini; just behind Claude Opus 4.6 (80.8%) |
| SWE-bench Pro | 55.4% | Harder contamination-resistant benchmark |
| LiveCodeBench | 93.5% Pass@1 | #1 across all evaluated models |
| Codeforces Rating | 3206 | 23rd among all human competitors |
| IMOAnswerBench | 89.8% | Top math reasoning |
| GPQA | 90.1 | |
| MMLU-Pro | 87.5 | |

The MIT license and weights availability on HuggingFace make this the most capable open-weight model for long-context agentic coding as of this date.

---

### 2. Kimi K2.6: Open-Source Trillion-Parameter Model Ties GPT-5.5 on SWE-Bench Pro
**Released April 20, 2026** | [Kimi Tech Blog](https://www.kimi.com/blog/kimi-k2-6) | [HuggingFace: moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)

Moonshot AI's Kimi K2.6 is the other major open-weight release of the week, targeting ultra-long agentic coding runs as its primary capability.

**Architecture:**
- ~1 trillion total parameters, 32 billion active per token
- MoE: 384 routed experts + 1 shared, 8 active per token
- **Multi-head Latent Attention (MLA)** + SwiGLU activation
- 262,144-token context with automatic compression to prevent truncation-induced drift
- **MoonViT** (400M params) vision encoder for image and video input

**Key capability differentiation:** K2.6 is engineered explicitly for *extended autonomous operation*, not just high single-turn accuracy:
- **12-hour autonomous runs** with 4,000+ coordinated steps demonstrated
- **300-agent swarm orchestration** with native coordination primitives
- Proactive autonomy: model recognizes when stuck and replans or escalates without human prompting

**Benchmarks:**
| Benchmark | K2.6 Score |
|---|---|
| SWE-Bench Pro | 58.6% (tied with GPT-5.5, ahead of DeepSeek V4 Pro 55.4%) |
| SWE-Bench Verified | 80.2% |
| Terminal-Bench 2.0 | 66.7% |
| MathVision (w/ Python tools) | 93.2% |

Available under Modified MIT on HuggingFace with deployment guides for vLLM, SGLang, and KTransformers. Real-world demonstrations include a 12-hour run optimizing a Zig inference runtime and overhauling a financial matching engine with 1,000+ tool calls.

---

### 3. Train-to-Test (T²) Scaling Laws: Chinchilla Is Wrong When You Factor In Inference
**arXiv 2604.01411** | [Paper](https://arxiv.org/abs/2604.01411v1) | University of Wisconsin-Madison & Stanford

This paper from Roberts et al. closes a fundamental gap in the pretraining scaling laws literature: Chinchilla and its successors optimize for pretraining compute, but modern LLMs are deployed with test-time scaling (repeated sampling, best-of-N). When you account for that inference cost, the optimal training decisions shift dramatically.

**The T² framework** jointly optimizes three variables — model size N, training tokens D, and inference samples k — under a fixed *end-to-end* compute budget (not just pretraining budget).

**Key findings:**
- Optimal pretraining now lies **well into the overtraining regime** relative to Chinchilla's prescription. Smaller models trained on substantially more tokens outperform larger Chinchilla-optimal models under equalized end-to-end compute.
- Results validated empirically: the authors pretrained heavily overtrained models in the T²-optimal region and confirmed superior downstream performance.
- Two variants: **T²-NLL** (loss-based forecasting) and **T²-Acc** (accuracy-based), validated across 8 downstream tasks.
- Post-training (RLHF, SFT) does not invalidate T² predictions — remains applicable to production deployment pipelines.

**Significance:** This reframes the canonical question "how big a model, how many tokens?" to "how big a model, how many tokens, and how many inference samples?" — a necessary modernization given that test-time scaling is now standard practice.

---

### 4. Latent Phase-Shift Rollback (LPSR): Inference-Time Error Correction Without Fine-Tuning
**arXiv 2604.18567** | [Paper](https://arxiv.org/abs/2604.18567v1)

LPSR is a notable inference-time intervention: it detects and corrects reasoning errors *during generation* by monitoring residual streams and rolling back the KV cache with steering vectors — no gradient computation, no additional forward passes, no fine-tuning.

**Mechanism:**
1. Monitor the residual stream at a target layer during generation.
2. Detect abrupt directional reversals ("phase shifts") using a dual gate: cosine-similarity drop + entropy spike.
3. On detection, roll back the KV cache to the pre-error state and inject a pre-computed steering vector to redirect generation.

**Performance on MATH-500 (8B model):**
| Method | Accuracy |
|---|---|
| Standard autoregressive | 28.8% |
| Prompted self-correction | 19.8% |
| Best-of-16 sampling | 36.2% |
| **LPSR (proposed)** | **44.0%** |
| Standard 70B model | 35.2% |

LPSR on an 8B model beats a standard 70B model (+8.8 pp) with **8.75× fewer parameters**, and beats Best-of-16 sampling by 7.8 pp at **5.4× lower token cost**.

**Key finding — detection-correction dissociation:** A 32-layer analysis shows that optimal error *detection* peaks at layer 14 (AUC 0.718), while optimal task *correction* peaks at layer 16 (44.0% vs. 29.2%). This layer-level mismatch suggests different mechanisms are responsible for identifying versus recovering from errors.

---

### 5. GenericAgent: 89.6% Fewer Tokens, 100% Task Completion via Context Density Maximization
**arXiv 2604.17091** | [Paper](https://arxiv.org/abs/2604.17091) | [GitHub](https://github.com/lsdefine/GenericAgent)

GenericAgent reframes the core challenge of long-horizon LLM agents: the bottleneck is not context *length* but context *density* — the fraction of context budget occupied by decision-relevant information.

**Four mechanisms to maximize information density:**
1. **Minimal atomic tool set:** Only 9 atomic tools (file ops, code execution, web interaction, memory management, human-in-the-loop).
2. **Hierarchical on-demand memory:** A small high-level index is shown by default; detailed knowledge is retrieved via tool calls only when needed.
3. **Self-evolution:** Verified execution paths are converted into reusable SOPs and executable code, progressively compressing experience.
4. **Context truncation and compression:** Maintains density during long executions.

**Results vs. leading agent frameworks:**
- Works within ~30K tokens (6× smaller than comparable frameworks).
- **100% task completion** on Lifelong AgentBench using only 222K input tokens — 15.5% of OpenClaw.
- **89.6% reduction** in token consumption across 9 repeated tasks through self-evolution.
- ~3,000 lines of core code; ~100-line agent loop.

---

## Deep Dive: AC/DC — Open-Ended LLM Expert Discovery via Task-Capability Coevolution

**ICLR 2026 Poster** | [OpenReview](https://openreview.net/forum?id=efNINVs2So) | [arXiv 2604.14969](https://arxiv.org/abs/2604.14969v1) | Sakana AI

AC/DC (Assessment Coevolving with Diverse Capabilities) takes a qualitatively different approach to capability expansion: instead of training a single model, it evolves an *archive* of diverse LLM experts alongside an evolving archive of tasks.

**Coevolution loop:**
- **LLM Population Evolution:** Model merging (weight or activation combination) from high-performing models generates new variants.
- **Task Archive Growth:** Synthetic data generation creates novel natural language tasks that challenge the current model population. As the model archive grows more capable, harder tasks are required to drive further differentiation.

The two archives co-drive each other: better models demand harder tasks; harder tasks surface capability gaps that drive model evolution.

**Results:**
- Discovered LLM populations surpass **larger** models in capability breadth while consuming less GPU memory.
- Coverage metric (diversity of expertise) improves continuously over time.
- Performance in multi-agent best-of-N selection improves as population diversifies.
- Entire pipeline runs in a single automated run with no manual benchmark selection.

**Why it matters:** The standard paradigm trains toward fixed benchmarks. AC/DC's open-ended coevolution discovers capabilities that no predefined benchmark would have targeted — a closer analog to how biological systems develop broad competence.

---

## Architecture & Pattern Notes

### Parcae: Looped Transformers Get Their First Stable Scaling Laws
**arXiv 2604.12946** | [Paper](https://arxiv.org/abs/2604.12946) | UCSD + Together AI

Looped architectures route activations through the same block of layers multiple times, increasing effective FLOPs without increasing parameters. Prior looped models have been unstable. Parcae fixes this by analyzing the residual stream as a **nonlinear time-variant dynamical system** and constraining the spectral norm of injection parameters — borrowed from state space model theory.

- A 770M-parameter Parcae matches a 1.3B-parameter standard Transformer on validation quality.
- At 1.3B parameters, improves CORE and Core-Extended quality by 2.99 and 1.18 points vs. Transformer baselines.
- First derivation of predictable scaling laws for looping: compute-optimal training requires increasing looping and data in tandem.

**Practical implication:** Compute scaling without parameter scaling — relevant for inference-constrained deployment where parameter count (model load time, KV cache) matters more than raw FLOPs.

---

### Audio Flamingo Next (NVIDIA + UMD): Temporal Chain-of-Thought for 30-Minute Audio
**arXiv 2604.10905** | [Paper](https://arxiv.org/abs/2604.10905) | [HuggingFace: nvidia/audio-flamingo-next-hf](https://huggingface.co/nvidia/audio-flamingo-next-hf)

AF-Next is NVIDIA's next-generation open audio-language model, extending to 30-minute audio inputs and introducing **Temporal Audio Chain-of-Thought (TACoT)** reasoning: intermediate reasoning steps grounded to timestamps in long audio. Three released variants:

- **AF-Next-Instruct:** QA, chat, general understanding.
- **AF-Next-Think:** Explicit multi-step reasoning with timestamp-grounded evidence.
- **AF-Next-Captioner:** Dense long-form captions.

Trained on 1M+ hours across AudioSkills-XL, LongAudio-XL, AF-Think, and AF-Chat datasets. Outperforms similarly-sized open models across 20 audio understanding/reasoning benchmarks; competitive with much larger models.

---

### Dataset Policy Gradient (DPG): Differentiable Control Over Synthetic Training Data
**arXiv 2604.08423** | [Paper](https://arxiv.org/abs/2604.08423) | Stanford

DPG is a reinforcement learning primitive from Thrush et al. at Stanford that frames synthetic data generation as a policy optimization problem. It uses **exact data attribution via higher-order gradients** to assign per-example rewards to synthetic training examples, then applies policy gradient to optimize the data generator.

Demonstrated capabilities:
- Cause LM head weights to embed a QR code, embed the pattern "67", or have lower ℓ² norm.
- Cause generators to rephrase inputs in a new language or produce a specific UUID — *without these objectives being explicitly stated in prompts*.

**Significance:** Prior synthetic data methods optimize heuristics (format, style, difficulty). DPG makes the data generator directly optimize whatever differentiable metric the practitioner cares about — a potentially more principled path to targeted capability elicitation.

---

## RL Training Advances

### Freshness-Aware Prioritized Experience Replay for LLMs (arXiv 2604.16918)

Standard Prioritized Experience Replay (PER) was designed for dense-reward RL; applying it to LLM post-training causes *priority staleness*: old high-priority trajectories dominate sampling even after the policy has moved on. This paper introduces **exponential age decay** on priorities, balancing freshness vs. historical signal.

Results on 0.5B–7B models:
- +46% on NQ Search
- +367% on Sokoban
- +133% on VLM FrozenLake

### KnowRL: Minimal-Sufficient Knowledge Guidance for RL Reasoning (arXiv 2604.12627)

Treats hint design as a *minimal-sufficient guidance* problem: decompose hints into atomic knowledge points and provide only what is strictly necessary. KnowRL-Nemotron-1.5B achieves **70.08% average accuracy without hints** and **74.16% with selected hints** across 8 reasoning benchmarks — competitive with much larger models.

### Efficient RL Training via Experience Replay (arXiv 2604.08706)

Challenges the assumption that on-policy data is essential for LLM post-training. Formalizes replay buffer design as a trade-off between staleness-induced variance, sample diversity, and generation cost. Well-designed replay buffers can reduce inference compute without degrading performance.

---

## Benchmarks & Datasets

```json
{
  "benchmarks": [
    {
      "name": "SWE-bench Pro",
      "type": "coding / software engineering",
      "top_score": "58.6% (Kimi K2.6)",
      "notes": "New harder contamination-resistant SE benchmark from Scale AI; sources diverse codebases. Top models score ~23% on public set vs 70%+ on SWE-bench Verified",
      "url": "https://scale.com/leaderboard/swe_bench_pro_public"
    },
    {
      "name": "ARC-AGI-3",
      "type": "abstract reasoning / general intelligence",
      "human_performance": "High (100% of 135 envs solved by ≥2 participants)",
      "frontier_ai_performance": "<1% as of March 2026",
      "notes": "135 novel abstract reasoning environments; 458-participant human study April 14 2026; task completion times peaked at 345–375s",
      "url": "https://arcprize.org/blog/arc-agi-3-human-dataset"
    },
    {
      "name": "LongBench v2",
      "type": "long-context multi-task QA",
      "top_score": "64.4% (Claude Opus 4.5, as of April 22 2026)",
      "runner_up": "63.2% (Qwen3.5 397B)",
      "notes": "503 MC questions, contexts 8K–2M words, 6 task categories",
      "url": "https://longbench2.github.io"
    },
    {
      "name": "Terminal-Bench 2.0",
      "type": "agentic terminal task completion",
      "top_score": "66.7% (Kimi K2.6)",
      "notes": "Evaluates long-horizon terminal use; Kimi K2.6 leads open-source models"
    },
    {
      "name": "LiveCodeBench",
      "type": "coding",
      "top_score": "93.5% Pass@1 (DeepSeek V4 Pro)",
      "notes": "Codeforces rating 3206 for DeepSeek V4 Pro — 23rd among all human competitors"
    }
  ]
}
```

---

## ICLR 2026 Outstanding Papers (Update)

The ICLR 2026 Outstanding Paper awards announced April 23 — covered briefly in yesterday's digest — have an important follow-up: the **Polar Express** honorable mention directly connects to this week's model releases. The paper optimizes polynomial approximations for **polar decomposition** in the Muon optimizer, with focus on GPU computation and low-precision arithmetic. Given that DeepSeek V4 Pro chose Muon over AdamW as its production optimizer for a 1.6T-parameter model, theoretical work on Muon's mathematical foundations is suddenly more than academic.

| Award | Paper | Authors |
|---|---|---|
| Outstanding Paper | "Transformers are Inherently Succinct" | Bergsträßer, Cotterell, Lin |
| Outstanding Paper | Multi-turn LLM capabilities paper | Laban, Hayashi, Zhou, Neville (Salesforce AI) |
| Honorable Mention | "The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm" | Amsel, Persson, Musco, Gower |

---

## Analysis & Impact

**The open-weight frontier keeps moving.** Two trillion-parameter models released within days of each other (DeepSeek V4 Pro, Kimi K2.6) both reach or exceed 80% SWE-bench Verified — a score that would have been frontier-only six months ago. The bar is rising so fast that "open-source" and "frontier" are converging on coding benchmarks.

**Architecture diversity is resurging.** This week saw Parcae (looped transformers), LPSR (residual stream interventions), and DeepSeek's hybrid CSA/HCA attention — all addressing the same problem (compute efficiency at inference) from different angles. The field is no longer converging on "bigger Transformer"; specialized architectural choices are back.

**Training methodology is bifurcating.** T² scaling laws reveal that Chinchilla prescriptions are wrong for any model that will be deployed with test-time scaling. At the same time, DeepSeek V4 Pro's adoption of Muon in production (confirmed by ICLR's Polar Express honorable mention gaining new relevance) suggests the optimizer question is reopening at scale. These two shifts — overtrain more, use different optimizers — both push against 2023-era conventional wisdom.

**The RL training paper cluster this week** (experience replay, KnowRL, DPG) collectively argues for more principled sample selection and synthetic data generation. The shift from "collect and filter" to "generate and optimize" appears to be the dominant post-training paradigm entering 2026.

**ARC-AGI-3's <1% AI score vs. near-100% human score** is the starkest current benchmark gap. With GPT-5.5 having just crossed ARC-AGI-2's threshold, this represents the immediately next hard wall for reasoning research.

---

## Key Takeaways TL;DR

1. **DeepSeek V4 Pro** (1.6T params, MIT license) introduced hybrid CSA/HCA attention cutting inference FLOPs to 27% at 1M context; trained with Muon optimizer on Huawei chips — architecturally the most interesting open release of the month.

2. **Kimi K2.6** (1T params, 58.6% SWE-bench Pro) targets 12-hour autonomous runs and 300-agent orchestration — open source's best extended-run coding agent.

3. **T² scaling laws** prove Chinchilla is wrong for deployed models: when inference (test-time sampling) costs are included, optimal training shifts deep into the overtraining regime.

4. **LPSR** achieves 44% MATH-500 on an 8B model (beating a 70B baseline) by correcting reasoning errors during generation via KV-cache rollback — no fine-tuning required.

5. **GenericAgent** reduces agent token consumption by 89.6% through context information density maximization — a paradigm for building long-horizon agents within fixed context budgets.

6. **ARC-AGI-3** formally establishes a new hard wall: humans solve all 135 environments; frontier AI is below 1% as of March 2026.

---

## Sources

| # | Source | URL |
|---|---|---|
| 1 | DeepSeek V4 Pro HuggingFace Blog | https://huggingface.co/blog/deepseekv4 |
| 2 | DeepSeek V4 Pro Model Card | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro |
| 3 | DeepSeek V4 Pro Complete Guide | https://www.aimadetools.com/blog/deepseek-v4-pro-complete-guide/ |
| 4 | Kimi K2.6 Tech Blog | https://www.kimi.com/blog/kimi-k2-6 |
| 5 | Kimi K2.6 HuggingFace Guide | https://avenchat.com/blog/kimi-k2-6-huggingface-guide |
| 6 | Kimi K2.6 Benchmark Review | https://tokenmix.ai/blog/kimi-k2-6-code-preview-review-2026 |
| 7 | T² Scaling Laws (arXiv 2604.01411) | https://arxiv.org/abs/2604.01411v1 |
| 8 | LPSR (arXiv 2604.18567) | https://arxiv.org/abs/2604.18567v1 |
| 9 | GenericAgent (arXiv 2604.17091) | https://arxiv.org/abs/2604.17091 |
| 10 | AC/DC ICLR 2026 (arXiv 2604.14969) | https://arxiv.org/abs/2604.14969v1 |
| 11 | Parcae (arXiv 2604.12946) | https://arxiv.org/abs/2604.12946 |
| 12 | Audio Flamingo Next (arXiv 2604.10905) | https://arxiv.org/abs/2604.10905 |
| 13 | Dataset Policy Gradient (arXiv 2604.08423) | https://arxiv.org/abs/2604.08423 |
| 14 | Freshness-Aware PER (arXiv 2604.16918) | https://arxiv.org/abs/2604.16918 |
| 15 | KnowRL (arXiv 2604.12627) | https://arxiv.org/abs/2604.12627 |
| 16 | Efficient RL via Experience Replay (arXiv 2604.08706) | https://arxiv.org/abs/2604.08706 |
| 17 | ARC-AGI-3 Human Performance | https://arcprize.org/blog/arc-agi-3-human-dataset |
| 18 | SWE-bench Pro Leaderboard | https://scale.com/leaderboard/swe_bench_pro_public |
| 19 | LongBench v2 | https://longbench2.github.io |
| 20 | ICLR 2026 Outstanding Papers | https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/ |
| 21 | Parcae - Sandy Research Lab | https://sandyresearch.github.io/parcae/ |
