# Best Models & Benchmarks — 2026-06-02

## Top Model News (3-5)

### 1. NVIDIA Cosmos 3 — First Open Omnimodal Foundation Model for Physical AI

**Source:** [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai) | [Technical Blog](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/) | [Hugging Face Blog](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)

NVIDIA launched Cosmos 3 on May 31, 2026, at GTC Taipei — the first fully open omnimodal world foundation model designed to unify physical AI reasoning, world simulation, and action generation within a single framework. Built on a Mixture-of-Transformers (MoT) architecture, it natively processes and generates text, images, video, ambient sound, and action sequences in a single model, subsuming what previously required a stack of specialized vision-language models, video generators, and world simulators. NVIDIA simultaneously launched the Cosmos Coalition with robotics and AI lab partners to drive physical AI adoption.

Two model sizes ship today: **Cosmos 3 Nano** (16B parameters, 8B reasoner + 8B generator) optimized for workstation-grade inference on NVIDIA RTX PRO 6000, and **Cosmos 3 Super** (64B parameters, 32B reasoner + 32B generator) designed for large-scale synthetic data generation on Hopper and Blackwell GPUs. A **Cosmos 3 Edge** variant for real-time inference is announced but not yet available. Open post-training scripts, synthetic data generation datasets, and a Cosmos Framework on GitHub make this not just a model release but a complete physical AI development platform.

This launch directly addresses the robotics and autonomous vehicle industries' need for a unified foundation model. Rather than assembling multiple model pipelines, developers can fine-tune Cosmos 3 on their domain data to build robot policies (e.g., a DROID manipulation policy is included) and AV world models. The open release under a permissive NVIDIA license — with weights on Hugging Face and NIM microservices for production deployment — positions NVIDIA as the infrastructure layer for the physical AI wave, complementing its GPU hardware dominance.

**Key specs:** Variable context | Text, image, video, audio, action (omnimodal) | Free (open weights) | NVIDIA Open Model License | Available now on Hugging Face, build.nvidia.com, NVIDIA NIM

---

### 2. Claude Opus 4.8 — Reclaims #1 on Intelligence Index with Agentic Coding Leap

**Source:** [Anthropic Blog](https://www.anthropic.com/news/claude-opus-4-8) | [SWE-bench Leaderboard](https://benchlm.ai/benchmarks/swePro) | [Benchmark Analysis](https://allthings.how/claude-opus-4-8-benchmarks-scores-rankings-and-pricing-may-2026/)

Released May 28, 2026, Claude Opus 4.8 is Anthropic's fifth Opus iteration in seven months and the current benchmark leader on agentic and knowledge-work evaluations. The most concrete gains come in coding reliability (4× less likely than Opus 4.7 to let its own code flaws pass without flagging), SWE-bench Pro (69.2%, up from 64.3%), and GDPval-AA real-world agentic performance (1,890 Elo, +137 over Opus 4.7, +121 over GPT-5.5). It achieves all this while using ~35% fewer output tokens than its predecessor — meaning it's simultaneously more capable and cheaper to run in practice. The Artificial Analysis Intelligence Index places it at **61.4** — new #1, ahead of GPT-5.5 (60.2) and Opus 4.7 (57.3).

Two major capability additions ship with Opus 4.8: **Effort Control** (five tiers: Low/Medium/High/Max, defaulting to High) lets developers trade compute for speed, and **Dynamic Workflows** in Claude Code (research preview) allows a single Opus 4.8 instance to spawn hundreds of parallel subagents for large-scale codebase tasks — the same mechanism that underpins Anthropic's claim of migrating a 750K-line codebase in 11 days. The new **Fast Mode** runs at 2.5× speed for $10/$50 per million tokens — three times cheaper than Opus 4.7 fast mode. Pricing for standard mode is unchanged at $5/$25 per million tokens.

Anthropic also disclosed benchmark updates alongside the release: Terminal-Bench 2.1 scores are now reported with the public Terminus-2 harness for all models (GPT-5.5 Codex CLI-harness score is 83.4%, correcting an earlier overcount). OSWorld-Verified methodology was also updated, revising Opus 4.7's score to 82.3%. These meta-disclosures signal Anthropic moving toward more harness-standardized reporting — a meaningful transparency gesture in a space where benchmark definitions differ by lab.

**Key specs:** 1M token context | Text + vision | $5/$25 per 1M tokens (standard), $10/$50 (fast mode) | Proprietary | Generally available via Claude API (`claude-opus-4-8`)

---

### 3. JetBrains Mellum2 — 12B MoE Model for High-Throughput Coding Infrastructure

**Source:** [Hugging Face Blog](https://huggingface.co/blog/JetBrains/mellum2-launch) | [JetBrains AI Blog](https://blog.jetbrains.com/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/) | [Technical Report](https://arxiv.org/pdf/2605.31268) | [MarkTechPost](https://www.marktechpost.com/2026/06/02/jetbrains-releases-mellum2-a-12b-moe-model-for-fast-specialized-tasks-in-multi-model-ai-pipelines/)

JetBrains released Mellum2 on June 1, 2026, open-sourcing the weights under Apache 2.0. It is a 12B-parameter Mixture-of-Experts model trained from scratch on ~10.6 trillion tokens of natural language and code, with only 2.5B parameters active per token — enabling inference throughput that matches or exceeds Qwen2.5-7B on a single H100 at under half the compute. The model was built specifically for the latency-sensitive sub-tasks in multi-model AI pipelines: routing, RAG retrieval, summarization, sub-agent calls, and high-throughput coding completions where the largest frontier model is unnecessary and prohibitively slow.

Mellum2's benchmark profile reflects its design intent: it excels on EvalPlus (78.4%, beating Qwen3.5-9B's 71.8%) and MultiPL-E (67.1%, matching Qwen3.5-9B), while trailing on LiveCodeBench v6 (37.2% vs. Qwen3.5-9B's 63.7%), which favors complex multi-step reasoning over syntactic correctness. On AIME 2025+2026, Mellum2 scores 41.7% — competitive with Qwen3.5 (4B) at 38.3% despite running at 2.5B active parameter compute. The 128K extended context window (full technical recipe in the report) and tool-use parity with Ministral 3 14B on BFCL v3 (66.3% vs. 52.7%) make it the strongest open Apache-2.0 sub-agent routing model available today.

The strategic angle here is JetBrains repositioning from IDE plugin provider to AI infrastructure contributor. Mellum2 is the open-weight backbone for JetBrains AI features across the IDE suite, but releasing it under Apache 2.0 invites the broader open-source ecosystem to build on it — a bet that model-level openness drives IDE adoption upstream. For teams building compound AI systems, Mellum2 is the first truly production-grade open model explicitly designed for the "specialist worker node" role rather than the "flagship general agent" role.

**Key specs:** 128K token context | Text + code | Free (Apache 2.0 open weights) | Open weights on Hugging Face | Available now

---

### 4. Gemini 3.5 Flash — GA Since May 19; Fastest Frontier Model, Leads Agentic Tool-Use

**Source:** [Google Blog](https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/) | [Dev.to Developer Guide](https://dev.to/akaranjkar08/gemini-35-flash-complete-developer-guide-api-benchmarks-pricing-migration-2026-3c8e) | [Benchmark Comparison](https://www.creeta.com/en/gemini-3-5-flash-vs-pro-guide-2026/)

While Gemini 3.5 Flash launched May 19, it is the most consequential newly-accessible model for builders as of June 2: it has now fully replaced Gemini 3.1 Pro as the default model across Gemini app, AI Mode in Google Search (1 billion monthly users), and Gemini Enterprise Agent Platform. At 284 tokens/second — 4× faster than competing frontier models at comparable quality — it enables streaming applications that previously required latency tradeoffs. On agentic benchmarks it surpasses 3.1 Pro on 11 of 15 published evaluations: Terminal-Bench 2.1 (76.2% vs. 70.3%), MCP Atlas tool-use reliability (83.6% vs. 78.2%), GDPval-AA (1,656 Elo vs. 1,314), and Finance Agent v2 (57.9% vs. 43.0%).

Pricing is $1.50/$9.00 per million tokens — 40% cheaper than Gemini 3.1 Pro and less than one-third the cost of Claude Opus 4.8 at standard mode. The model supports text, image, audio, and video input with four thinking levels (Minimal/Low/Medium/High) and a 1M-token context window (65,536 max output). It regresses vs. 3.1 Pro on Humanity's Last Exam (40.2% vs. 44.4%), ARC-AGI-2 (72.1% vs. 77.1%), and long-context retrieval at 128K (77.3% vs. 84.9%), so it is optimized for agentic tool-use speed, not frontier reasoning depth.

Gemini 3.5 Pro remains in limited preview for select Vertex customers with no public model ID, pricing, or benchmark data as of June 2. It is expected in June 2026 with a 2M-token context window and Deep Think reasoning mode. The Flash→Pro split in the 3.5 generation mirrors Google's strategic bet: Flash for production agent pipelines at scale, Pro for deep reasoning tasks where latency and cost are secondary.

**Key specs:** 1M token context, 65K max output | Text, image, audio, video input | $1.50/$9.00 per 1M tokens | Proprietary | GA via `gemini-3.5-flash` in Gemini API, AI Studio, Vertex AI

---

### 5. Qwen3.7-Max — Alibaba's 1M-Context Agent Flagship Enters Preview

**Source:** [MarkTechPost](https://www.marktechpost.com/2026/05/21/qwen-introduces-qwen3-7-max-a-reasoning-agent-model-with-a-1m-token-context-window/) | [Yotta Labs](https://www.yottalabs.ai/post/qwen-3-7-max-release-date-features-open-source-status-and-how-to-access-2026) | [OpenRouter](https://openrouter.ai/qwen/qwen3.7-max/api)

Alibaba's Qwen team formally launched Qwen3.7-Max at the 2026 Alibaba Cloud Summit on May 19–20, 2026, positioning it as "The Agent Frontier." The model hits **56.6 on the Artificial Analysis Intelligence Index** — ranking #5 overall, a +4.8-point jump from Qwen3.6 Max Preview — and doubles the context window to 1M tokens (up from 256K), enough to ingest a full mid-sized code repository in a single request. Alibaba's internal testing claims sustained 1,000+ tool calls and 35-hour autonomous execution, though no independent verification exists yet. The model is text-input/output only (no multimodal), proprietary (no open weights), and available exclusively through Alibaba Cloud Model Studio API.

Pricing is listed at approximately $1.25/$3.75 per million tokens on OpenRouter (routing through Alibaba Cloud), making it competitive with DeepSeek V4 Pro on cost while offering stronger reasoning-mode polish. The key differentiator vs. Qwen3.6 Max Preview is the 1M context window and improved agentic task completion, particularly for long-horizon coding agents and office productivity workflows. However, benchmark coverage is still thin: Alibaba self-reports show gains on coding and agent benchmarks vs. Qwen3.6 Max Preview, but independent audits on SWE-bench Pro and ARC-AGI-2 are not yet available.

The open-weight complement to Qwen3.7-Max is the **Qwen3.6-35B-A3B** (35B total / 3B active MoE, Apache 2.0, 262K context), which sits in the 49–53% SWE-bench Verified range and is the most capable self-hostable Qwen model available today.

**Key specs:** 1M token context, 65K max output | Text only | ~$1.25/$3.75 per 1M tokens (OpenRouter) | Proprietary, closed weights | Preview via Alibaba Cloud Model Studio

---

## Deep Dive: Most Important Release — NVIDIA Cosmos 3 (May 31, 2026)

The launch of Cosmos 3 is the defining model event of this period because it is the first credible open-weight foundation model to unify the modality stack required for physical AI — not as a bolted-together pipeline but as a single trained architecture. Every prior attempt at this unification was either closed-source (OpenAI's internal robotics work), narrow (video-only or action-only), or required multiple specialist models in sequence. Cosmos 3 ships a single Mixture-of-Transformers checkpoint that jointly handles visual reasoning, world simulation, and action generation, directly in the training regime — a structural breakthrough that open-sources what has been frontier lab secret sauce.

### What It Can Do

Cosmos 3 Nano (16B) and Super (64B) process sequences of text, image, video, ambient audio, and action tokens natively, enabling end-to-end robot policy training without separate tokenization pipelines for each modality. The architecture supports Text2Image, Image2Video, and direct action prediction from visual observations, with an included DROID manipulation policy fine-tune demonstrating real-world robot control. The model can generate physically plausible synthetic data at scale for training downstream robot policies — a capability that addresses the chronic data bottleneck in robotics. Cosmos 3 Nano is specifically designed to run in real time on workstation-class GPUs (RTX PRO 6000), enabling on-device robot inference without datacenter connectivity.

### Benchmark Highlights

NVIDIA has not published standard LLM benchmark scores (GPQA, SWE-bench, etc.) for Cosmos 3, as it is a physical AI foundation model rather than a general-purpose language model. Performance is measured on domain-specific robotics and video generation benchmarks:

| Benchmark | Cosmos 3 | Notes |
|---|---|---|
| Physical AI Reasoning | Leaderboard-topping (self-reported) | NVIDIA claims top position; third-party audit pending |
| Synthetic Data Generation Quality | State-of-the-art (Super) | Measured by downstream policy success rate |
| Real-time Inference Latency | Sub-second (Nano on RTX PRO 6000) | Suitable for real-time robot control loops |
| Architecture Parameters | Nano: 16B (8B+8B) / Super: 64B (32B+32B) | Reasoner + Generator split |

### Architecture (known)

Cosmos 3 is built on a **Mixture-of-Transformers (MoT)** architecture, which routes different token types (text, image patches, video frames, audio spectrograms, action embeddings) through specialized transformer sub-networks within a single unified model. The "reasoner + generator" split within each size tier reflects the dual function: a reasoning module for understanding/predicting physical states, and a generation module for producing synthetic video and action outputs. Training data includes real-world robotics datasets (DROID manipulation), autonomous driving footage, and physics simulation outputs. The Cosmos Framework (GitHub) provides full post-training scripts, enabling domain-specific fine-tuning. NVIDIA's full technical report is available at research.nvidia.com/labs/cosmos-lab/cosmos3.

### Pricing & Availability

- **Cosmos 3 Nano** (16B): Free open weights on Hugging Face (`nvidia/Cosmos3-Nano`); also available as NVIDIA NIM microservice (Reasoner NIM GA now; Generator NIM coming soon)
- **Cosmos 3 Super** (64B): Free open weights on Hugging Face (`nvidia/Cosmos3-Super`); NIM microservice for datacenter deployment
- **Cosmos 3 Edge**: Announced, not yet available
- **Try without downloading**: `build.nvidia.com`
- **License**: NVIDIA Open Model License (permissive for commercial use with attribution)
- **Context**: Omnimodal sequences; variable length depending on modality mix

### Strategic Significance

NVIDIA's move here is not primarily a model launch — it is an infrastructure land-grab for the physical AI era. By open-sourcing Cosmos 3 under a permissive license, NVIDIA ensures that every robotics company, AV team, and industrial AI lab building on it will need NVIDIA GPUs for training and inference. The Cosmos Coalition (Agile Robots, Black Forest Labs, and others) locks in integration partners at the foundation model layer before competing hardware platforms can offer equivalent open alternatives. This is the same playbook CUDA ran against OpenCL: make the open-source tooling so good that the ecosystem standardizes on NVIDIA's compute substrate.

The second strategic angle is synthetic data generation. The chronic bottleneck in physical AI is real-world data collection — robots need millions of hours of demonstrated behaviors, which are expensive and slow to gather. Cosmos 3 Super's physics-accurate world simulation enables generating unlimited synthetic training data for downstream robot policies. If this holds up under independent evaluation, it could compress years of physical robot training timelines — a capability that has no equivalent in the open-source ecosystem.

The third angle is timing: Cosmos 3 arrives just as humanoid robotics funding is at a historic peak (Figure AI, 1X, Physical Intelligence, Apptronik all raised 2025–2026), and as autonomous vehicle programs are restarting after the 2024 consolidation. NVIDIA is positioning Cosmos 3 as the foundation layer for both waves simultaneously.

### Competitive Context

No directly comparable open model exists at this capability level. Google's RT-2 and Physical Intelligence's π0 are proprietary. OpenAI's robotics work is entirely closed. DeepMind has published physical AI research (SayCan, RT-X) but not released unified open foundation models at this scale. The closest open competition is from Meta's V-JEPA for video understanding and Hugging Face's LeRobot ecosystem — both of which are narrower in scope and modality coverage. On the language model side, Cosmos 3 is not competing with Claude, GPT-5.5, or Gemini; it occupies a separate niche where the benchmark that matters is whether a robot arm picks up the correct object, not whether the model scores well on GPQA Diamond.

---

## Benchmark Comparison Data

```json
{"benchmark": "SWE-bench Verified", "results": [{"model": "Claude Mythos Preview", "score": 93.9}, {"model": "Claude Opus 4.8", "score": 88.6}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 87.6}, {"model": "GPT-5.5", "score": 85.0}, {"model": "Claude Opus 4.6", "score": 80.9}, {"model": "Claude Opus 4.5", "score": 80.8}, {"model": "DeepSeek V4 Pro (Max)", "score": 80.6}, {"model": "Gemini 3.1 Pro", "score": 80.6}, {"model": "MiniMax M2.5", "score": 80.5}, {"model": "Qwen3.7-Max", "score": 80.4}, {"model": "Moonshot Kimi K2.6", "score": 80.2}, {"model": "GPT-5.4", "score": 80.0}, {"model": "DeepSeek V4 Flash (Max)", "score": 79.0}, {"model": "Mistral Medium 3.5 128B", "score": 77.6}, {"model": "Qwen3.6-35B-A3B", "score": 77.2}]}
```

```json
{"benchmark": "SWE-bench Pro", "results": [{"model": "Claude Mythos Preview", "score": 77.8}, {"model": "Claude Opus 4.8", "score": 69.2}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 64.3}, {"model": "Qwen3.7-Max", "score": 60.6}, {"model": "MiniMax M2.5", "score": 59.0}, {"model": "GPT-5.5", "score": 58.6}, {"model": "Moonshot Kimi K2.6", "score": 58.6}, {"model": "Z.AI GLM-5.1", "score": 58.4}, {"model": "GPT-5.4", "score": 57.7}, {"model": "Qwen3.6 Max (preview)", "score": 57.3}, {"model": "DeepSeek V4 Pro", "score": 55.4}, {"model": "Gemini 3.1 Pro", "score": 54.2}]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [{"model": "GPT-5.5", "score": 85.0}, {"model": "GPT-5.4 Pro", "score": 83.3}, {"model": "Gemini 3.1 Pro", "score": 77.1}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8}, {"model": "GPT-5.4", "score": 73.3}, {"model": "Gemini 3.5 Flash", "score": 72.1}, {"model": "Claude Opus 4.6", "score": 68.8}, {"model": "Claude Sonnet 4.6", "score": 59.0}, {"model": "Grok 4.20", "score": 53.3}, {"model": "GPT-5.2", "score": 52.9}, {"model": "Claude Opus 4.5", "score": 13.6}]}
```

```json
{"benchmark": "GPQA Diamond (%)", "results": [{"model": "Gemini 3.1 Pro", "score": 94.3}, {"model": "GPT-5.4 Pro", "score": 94.4}, {"model": "GPT-5.4", "score": 92.8}, {"model": "Claude Opus 4.6", "score": 91.3}, {"model": "DeepSeek V4 Pro", "score": 88.8}, {"model": "Qwen3.6 Max Preview", "score": 88.8}, {"model": "Mellum2 (12B)", "score": 40.9}]}
```

```json
{"benchmark": "Terminal-Bench 2.1 (%)", "results": [{"model": "GPT-5.5 (Codex CLI harness)", "score": 83.4}, {"model": "GPT-5.5 (Terminus-2 harness)", "score": 78.2}, {"model": "Gemini 3.5 Flash", "score": 76.2}, {"model": "Claude Opus 4.8", "score": 74.6}, {"model": "Gemini 3.1 Pro", "score": 70.3}, {"model": "GPT-5.4", "score": 75.1}, {"model": "Claude Opus 4.7", "score": 66.1}]}
```

```json
{"benchmark": "GDPval-AA (Elo)", "results": [{"model": "Claude Opus 4.8", "score": 1890}, {"model": "GPT-5.5", "score": 1769}, {"model": "Claude Opus 4.7", "score": 1753}, {"model": "Gemini 3.5 Flash", "score": 1656}, {"model": "Gemini 3.1 Pro", "score": 1314}]}
```

```json
{"benchmark": "OSWorld-Verified (computer use %)", "results": [{"model": "Claude Opus 4.8", "score": 83.4}, {"model": "Claude Opus 4.7", "score": 82.3}, {"model": "GPT-5.5", "score": 78.7}, {"model": "Gemini 3.5 Flash", "score": 76.2}, {"model": "Gemini 3.1 Pro", "score": 76.2}]}
```

```json
{"benchmark": "LMArena Elo (Overall Text, May 2026)", "results": [{"model": "Claude Opus 4.6 Thinking", "score": 1502}, {"model": "Claude Opus 4.7 Thinking", "score": 1501}, {"model": "Claude Opus 4.6", "score": 1498}, {"model": "Claude Opus 4.7", "score": 1492}, {"model": "Meta Muse Spark (preview)", "score": 1491}, {"model": "Gemini 3.1 Pro Preview", "score": 1490}, {"model": "Gemini 3 Pro", "score": 1486}, {"model": "GPT-5.5 High", "score": 1484}, {"model": "Grok 4.20 Beta", "score": 1479}, {"model": "GPT-5.4 High", "score": 1479}, {"model": "Qwen3.5-Max-Preview", "score": 1465}]}
```

```json
{"benchmark": "Humanity's Last Exam (with tools, %)", "results": [{"model": "Claude Opus 4.8", "score": 57.9}, {"model": "GPT-5.5", "score": 52.2}, {"model": "Claude Opus 4.6", "score": 53.0}, {"model": "Gemini 3.5 Flash", "score": 40.2}]}
```

```json
{"benchmark": "MCP Atlas Tool-Use Reliability (%)", "results": [{"model": "Gemini 3.5 Flash", "score": 83.6}, {"model": "Gemini 3.1 Pro", "score": 78.2}, {"model": "GPT-5.4", "score": 67.2}, {"model": "Gemini 3.1 Pro (prior)", "score": 69.2}]}
```

```json
{"benchmark": "Artificial Analysis Intelligence Index", "results": [{"model": "Claude Opus 4.8", "score": 61.4}, {"model": "GPT-5.5", "score": 60.2}, {"model": "Claude Opus 4.7", "score": 57.3}, {"model": "Qwen3.7-Max", "score": 56.6}, {"model": "Gemini 3.5 Flash (high)", "score": 55.0}, {"model": "Grok 4.3", "score": 53.0}, {"model": "Claude Sonnet 4.6", "score": 52.0}, {"model": "DeepSeek V4 Pro", "score": 51.5}, {"model": "Qwen3.6 Max Preview", "score": 51.8}]}
```

```json
{"benchmark": "LiveCodeBench v6 (%)", "results": [{"model": "Qwen3.5 (9B)", "score": 63.7}, {"model": "Ministral 3 (14B)", "score": 42.4}, {"model": "Mellum2 Instruct (12B MoE)", "score": 37.2}, {"model": "OLMo-3 (7B)", "score": 28.2}, {"model": "Seed-Coder (8B)", "score": 28.1}]}
```

```json
{"benchmark": "Finance Agent v2 (%)", "results": [{"model": "Claude Opus 4.8", "score": 53.9}, {"model": "GPT-5.5", "score": 51.8}, {"model": "Gemini 3.5 Flash", "score": 57.9}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Opus 4.8 | Anthropic | 1M | $5.00 | $25.00 | Text, vision |
| Claude Opus 4.8 (Fast Mode) | Anthropic | 1M | $10.00 | $50.00 | Text, vision |
| GPT-5.5 | OpenAI | ~1.1M | $5.00 | $30.00 | Text, image, audio |
| GPT-5.4 Pro | OpenAI | 1.05M | $30.00 | $180.00 | Text, image |
| Gemini 3.1 Pro | Google | 2M | $2.00–4.00 | $12.00–20.00 | Text, image, video, audio |
| Gemini 3.5 Flash | Google | 1M | $1.50 | $9.00 | Text, image, video, audio |
| Gemini 3.5 Pro (preview) | Google | 2M (est.) | TBD | TBD | Text, image, video, audio |
| Qwen3.7-Max | Alibaba | 1M | ~$1.25 | ~$3.75 | Text |
| Qwen3.6 Max Preview | Alibaba | 262K | $1.30 | $7.80 | Text |
| DeepSeek V4 Pro | DeepSeek | 1.05M | $1.74 | $3.48 | Text |
| DeepSeek V4 Flash | DeepSeek | 1M | $0.14 | $0.28 | Text |
| Grok 4.20 | xAI | 256K | $5.00 | $15.00 | Text |
| Claude Sonnet 4.6 | Anthropic | 500K | $3.00 | $15.00 | Text, vision |
| Mistral Medium 3.5 128B | Mistral | 256K | $1.50 | $7.50 | Text |
| Meta Muse Spark | Meta | 200K | $0.95 | $3.80 | Text |
| NVIDIA Cosmos 3 Nano (16B) | NVIDIA | Variable | Free (open) | Free (open) | Text, image, video, audio, action |
| NVIDIA Cosmos 3 Super (64B) | NVIDIA | Variable | Free (open) | Free (open) | Text, image, video, audio, action |
| JetBrains Mellum2 (12B MoE) | JetBrains | 128K | Free (open) | Free (open) | Text, code |
| Qwen3.6-35B-A3B | Alibaba | 262K | Free (open) | Free (open) | Text, image, video |
| GLM-5 Air | Zhipu | 200K | $0.30 | $0.90 | Text |

---

## Analysis & Impact

- **For software engineering / coding:** Claude Opus 4.8 is now the unambiguous leader for multi-file autonomous coding at 69.2% SWE-bench Pro — a 10.6-point gap over GPT-5.5 (58.6%). The exception is pure terminal-command workflows, where GPT-5.5 still leads at 78.2% Terminal-Bench 2.1. For open-source CI/CD integrations and sub-agent routing within coding pipelines, JetBrains Mellum2 (Apache 2.0, 2×+ inference speed, competitive EvalPlus) is the first production-grade open alternative to embedding a frontier model for every call.

- **For frontier reasoning / math / science:** GPT-5.5 holds the ARC-AGI-2 top spot at 85% (matching the published grand prize threshold), but Gemini 3.1 Pro leads GPQA Diamond at 94.3% and Claude Mythos Preview holds SWE-bench Verified at 93.9%. These three models occupy different reasoning niches: GPT-5.5 for abstract novel-pattern reasoning, Gemini 3.1 Pro for graduate-level scientific reasoning, and Claude Mythos for applied software engineering reasoning. MMLU is now effectively saturated (all frontier models above 88%), confirming Humanity's Last Exam and domain-specific agentic benchmarks as the new differentiators.

- **For multimodal / video / audio work:** Gemini 3.5 Flash is the leading production choice for mixed-modality pipelines: it accepts text, image, video, and audio in a single request at 284 tok/sec — 4× faster than comparable frontier models — and leads on CharXiv Reasoning (multimodal: 84.2%) and MCP Atlas (83.6%). For physical AI, robotics, and AV applications, NVIDIA Cosmos 3 represents a categorical leap: the first open omnimodal model that natively generates video and action outputs alongside language, enabling end-to-end synthetic data pipelines for physical systems.

- **For cost-sensitive or open-source deployments:** DeepSeek V4 Flash at $0.14/$0.28 per million tokens reaches 79% SWE-bench Verified — within 10 points of Claude Opus 4.8 at 35× lower cost. JetBrains Mellum2 (Apache 2.0) is the best new open model for high-throughput sub-agent and routing workloads, running at 2.5B active parameters while matching 9–14B dense models on most code benchmarks. Qwen3.6-35B-A3B (Apache 2.0, 3B active params, 77% SWE-bench Verified) is the strongest self-hostable model for production coding pipelines that need frontier-adjacent coding quality without API costs.

- **Agentic orchestration is now table stakes:** Every major frontier model released in May–June 2026 — Opus 4.8 (Dynamic Workflows + Effort Control), Gemini 3.5 Flash (MCP Atlas, Gemini Spark), Qwen3.7-Max ("Agent Frontier"), Cosmos 3 (action generation) — ships with explicit agentic architecture as a primary feature, not an afterthought. The benchmark landscape has shifted accordingly: GDPval-AA (real-world knowledge work), MCP Atlas (tool-use reliability), Terminal-Bench 2.1 (autonomous terminal execution), and Finance Agent v2 (domain-specific long-horizon agents) are now the primary tier-1 differentiators, with academic benchmarks like MMLU serving mainly as sanity checks.

---

## Key Takeaways (TL;DR)

- Claude Opus 4.8 reclaimed the #1 spot on the Artificial Analysis Intelligence Index at 61.4, leading GDPval-AA (1,890 Elo) and SWE-bench Pro (69.2%) while holding the $5/$25 price — the best coding+agentic value in the closed frontier tier.
- NVIDIA Cosmos 3 (May 31) is the first open-weight omnimodal foundation model for physical AI, unifying text, image, video, audio, and action in a single Mixture-of-Transformers architecture across 16B and 64B sizes under a permissive license.
- GPT-5.5 is the only model to hit the ARC-AGI-2 grand prize threshold of 85%, while Claude Mythos Preview (still gated) holds the SWE-bench Verified record at 93.9%.
- Gemini 3.5 Flash (GA since May 19) delivers frontier-class agentic performance at $1.50/$9.00 per million tokens and 284 tok/sec — 4× faster than competing models, now default across Google Search AI Mode (1B monthly users).
- JetBrains Mellum2 (Apache 2.0, 12B MoE, 2.5B active params) sets a new standard for open-source high-throughput sub-agent and routing models, matching or beating 9–14B dense models on most code benchmarks at under half the inference latency.

---

*Sources:*
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai
- https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/
- https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai
- https://github.com/nvidia/Cosmos
- https://www.anthropic.com/news/claude-opus-4-8
- https://benchlm.ai/benchmarks/sweVerified
- https://benchlm.ai/benchmarks/swePro
- https://llm-stats.com/benchmarks/swe-bench-verified
- https://llm-stats.com/benchmarks/swe-bench-pro
- https://leaderboard.steel.dev/leaderboards/swe-bench-verified/
- https://huggingface.co/blog/JetBrains/mellum2-launch
- https://blog.jetbrains.com/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/
- https://arxiv.org/pdf/2605.31268
- https://www.marktechpost.com/2026/06/02/jetbrains-releases-mellum2-a-12b-moe-model-for-fast-specialized-tasks-in-multi-model-ai-pipelines/
- https://blog.google/intl/en-africa/products/explore-get-answers/gemini-3-5/
- https://dev.to/akaranjkar08/gemini-35-flash-complete-developer-guide-api-benchmarks-pricing-migration-2026-3c8e
- https://memeburn.com/gemini-3-5-flash-vs-claude-gpt-pricing/
- https://www.creeta.com/en/gemini-3-5-flash-vs-pro-guide-2026/
- https://www.marktechpost.com/2026/05/21/qwen-introduces-qwen3-7-max-a-reasoning-agent-model-with-a-1m-token-context-window/
- https://www.yottalabs.ai/post/qwen-3-7-max-release-date-features-open-source-status-and-how-to-access-2026
- https://openrouter.ai/qwen/qwen3.7-max/api
- https://presenc.ai/research/lmsys-chatbot-arena-elo-rankings-may-2026
- https://www.swfte.com/lmarena
- https://benchlm.ai/benchmarks/arcAgi2
- https://benchlm.ai/blog/posts/arc-agi-2-explained
- https://allthings.how/claude-opus-4-8-benchmarks-scores-rankings-and-pricing-may-2026/
- https://ofox.ai/blog/claude-opus-4-8-release-review-2026/
- https://contracollective.com/blog/gpt-5-5-vs-claude-opus-4-8-2026
- https://wandb.ai/byyoung3/ml-news/reports/Claude-Opus-4-8-Benchmark-Scores--VmlldzoxNzA0NTk3MQ
- https://aitoolbolt.com/claude-opus-4-8-vs-gemini-3-5-pro/
- https://ominigate.ai/en/vs/deepseek-v4-pro-vs-qwen3-6-max-preview
- https://deepseekai.guide/comparisons/deepseek-vs-qwen/
- https://yingtu.ai/en/blog/gpt-5-4-vs-gpt-5-3-vs-gemini-3-1
- https://intuitionlabs.ai/articles/gpqa-diamond-ai-benchmark
- https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough
- https://thewincentral.com/gpt-5-6-leaks-suggest-openais-next-big-ai-upgrade-could-arrive-in-june/
- https://chatforest.com/
