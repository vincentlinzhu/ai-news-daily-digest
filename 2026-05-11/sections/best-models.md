# Best Models & Benchmarks — 2026-05-11

## Top Model News (5)

### 1. Kimi K2.6 — Moonshot AI's Trillion-Parameter Agentic Coding Powerhouse Goes GA

**Source:** [MarkTechPost](https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/) | [Kimi Official](https://kimi-k2.org/blog/24-kimi-k2-6-release) | [BenchLM Benchmarks](https://benchlm.ai/benchmarks/liveCodeBenchPro)

Released April 20–21, 2026 and reaching GA in under eight days, Kimi K2.6 is Moonshot AI's most ambitious model to date — a 1-trillion-parameter MoE architecture with 32B active parameters per token. It is the first production model explicitly engineered for long-horizon autonomous agentic runs: up to 12 continuous hours, 4,000 coordinated steps, and swarms of up to 300 sub-agents operating in parallel. This positions it as a genuine "agent operating system" rather than a chat model with tool calling bolted on.

On benchmarks, K2.6 leads on AIME 2026 at 96.4%, LiveCodeBench v6 at 89.6%, and SWE-Bench Pro at 58.6% — surpassing GPT-5.4 on the latter (57.7%) and Claude Opus 4.6 (53.4%). Its 54.0% on Humanity's Last Exam (HLE-Full with tools) is the highest published score among compared frontier models, underscoring strong general scientific reasoning when paired with tool use.

K2.6 is open-weight under a Modified MIT License, with weights published on Hugging Face. The model includes native vision via its MoonViT encoder (400M parameters) and handles a 262K context window with automatic compression. API access is live via Kimi.com, the Kimi app, and the Kimi Code CLI.

**Key specs:** 262,144 tokens context | Text + Vision (MoonViT) | API pricing TBD | Modified MIT (open weights on HuggingFace) | GA on Kimi.com, API, Kimi Code CLI

---

### 2. GPT-5.5 Instant — OpenAI Makes Hallucination Reduction the New Default

**Source:** [OpenAI Blog](https://openai.com/index/gpt-5-5-instant/) | [System Card](https://openai.com/index/gpt-5-5-instant-system-card/) | [Rolling Out](https://rollingout.com/2026/05/05/openais-gpt-5-5-instant-reduces/)

OpenAI shipped GPT-5.5 Instant on May 5, 2026 as the new default ChatGPT model for all users, replacing GPT-5.3 Instant. The headline number is a 52.5% reduction in hallucinated claims on high-stakes prompts (medicine, law, finance) and a 37.3% reduction in inaccurate claims on conversations flagged for factual errors — the largest factuality jump in the GPT-5 generation. AIME 2025 score leaped from 65.4 to 81.2, and MMMU-Pro multimodal reasoning improved from 69.2 to 76.

The model introduces personalized memory that spans past conversations, uploaded files, and connected Gmail accounts (Plus/Pro users), positioning it as a continuous assistant rather than a stateless chatbot. Image analysis is substantially improved, STEM reasoning sharpened, and the model's self-calibration for web search decisions is more accurate — it knows better when to call external tools rather than hallucinate stale knowledge.

GPT-5.5 Instant is also the leader on Terminal-Bench 2.0 at 82.0–82.7% and tops ARC-AGI-2 at 85%, the first model to approach human average performance (66%) and the grand prize threshold (>85%) on that benchmark. With a 400K context window and full tool-calling support (code interpreter, computer use, file search, image generation), it is the most capable daily-use model currently available to the general public.

**Key specs:** 400,000 tokens context | Text + Image input | $5.00/$30.00 per 1M tokens (input/output) | Proprietary | GA on ChatGPT (all users), OpenAI API

---

### 3. Claude Opus 4.7 — Anthropic's New Flagship Hits 87.6% SWE-bench Verified

**Source:** [Anthropic Blog](https://www.anthropic.com/news/claude-opus-4-7) | [API Docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) | [LLM Stats](https://llm-stats.com/blog/research/claude-opus-4-7-launch)

Released April 16, 2026, Claude Opus 4.7 is Anthropic's most capable publicly available model, posting 87.6% on SWE-bench Verified — a 6.8-point jump from Opus 4.6's 80.8% and cementing Anthropic's lead in real-world software engineering. GPQA Diamond reaches 94.2%, Terminal-Bench 2.0 hits 69.4%, and Finance Agent (SOTA) scores 64.4%. The model also introduces `xhigh` reasoning effort — a new level between `high` and `max` giving developers finer control over compute-accuracy tradeoffs.

The most dramatic single improvement is in vision: a native resolution upgrade to 2,576px on the long edge (3.75MP total, 3.3× more than Opus 4.6) pushes visual acuity from 54.5% to 98.5% on the visual acuity benchmark. The model also gains output self-verification during the planning phase — it checks its own work for logical faults before returning results, reducing error rates on multi-step tasks. A new tokenizer update, however, can generate up to 35% more tokens for equivalent text, effectively increasing per-request costs despite unchanged per-token rates.

Opus 4.7 sits just below the restricted Claude Mythos Preview in Anthropic's capability hierarchy. It is available on the Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry, and Claude.ai (Pro, Max, Team, Enterprise). With 1M input tokens and 128K output, it supports the longest output generation of any Anthropic model to date.

**Key specs:** 1,000,000 input tokens / 128K output | Text + High-res Vision | $5.00/$25.00 per 1M tokens (input/output) | Proprietary | GA on Claude API, Bedrock, Vertex AI, Microsoft Foundry

---

### 4. Qwen3.6-27B — Dense 27B Open-Source Model Beats a 397B MoE on Coding

**Source:** [Alibaba Cloud Blog](https://www.alibabacloud.com/blog/qwen3-6-27b-flagship-level-coding-in-a-27b-dense-model_603063) | [MarkTechPost](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/) | [NYU Shanghai](https://rits.shanghai.nyu.edu/ai/qwen3-6-27b-a-dense-27b-model-that-beats-a-397b-moe-on-coding/)

The Qwen3.6-27B is arguably the most surprising release of the past weeks: a 27-billion-parameter dense model that outperforms Qwen3.5-397B-A17B — a 397B sparse MoE — across all major coding benchmarks, while being roughly 15× smaller in total parameter count. Released April 22, 2026 under Apache 2.0, it scores 77.2% on SWE-bench Verified (vs. 76.2% for the 397B MoE), 53.5% on SWE-bench Pro (vs. 50.9%), and 83.9% on LiveCodeBench v6.

The architectural secret is a hybrid attention design combining Gated DeltaNet linear attention with standard Gated Attention layers, enabling more efficient long-context handling without the quadratic scaling cost of pure attention. Native context is 262K tokens, extensible to 1M via RoPE-based scaling. This puts a self-hostable, single-server model within striking distance of proprietary frontier coding assistants.

A companion release, Qwen3.6-35B-A3B (also April 22), is a sparse MoE variant with 35B total but only 3B active parameters, scoring 73.4% on SWE-bench Verified and 1,397 on QwenWebBench — making it extremely efficient for inference. Both models are on HuggingFace and available via major cloud providers. Four Qwen3.5 models (including Qwen3.5-27B-FP8 with 1M context and 200+ language support) also became available on Amazon SageMaker JumpStart on May 4, extending Alibaba's open-weight lineup further.

**Key specs:** 262K tokens (extensible to 1M) | Text | Apache 2.0 open weights | Available on HuggingFace, AWS SageMaker JumpStart, and self-hosted inference

---

### 5. Mistral Medium 3.5 — One 128B Model to Replace Three, With 256K Context and Self-Hosting on 4 GPUs

**Source:** [The Decoder](https://the-decoder.com/mistrals-new-flagship-medium-3-5-folds-chat-reasoning-and-code-into-one-model/) | [DataNorth](https://datanorth.ai/news/mistral-medium-3-5-release) | [CloudPrice](https://cloudprice.net/models/mistral-medium-3-5)

Mistral released Medium 3.5 on April 29, 2026 — a 128B dense (non-MoE) transformer that collapses Mistral Medium 3.1 (chat), Magistral (reasoning), and Devstral 2 (coding) into a single model with configurable reasoning effort per request. At 77.6% on SWE-bench Verified and 91.4% on Tau-3 Telecom (agentic tool use), it is competitive with frontier models at a dramatically lower infrastructure cost — self-hostable on four GPUs, outputting at 163 tokens/second with 0.53s time-to-first-token.

The vision subsystem features a custom encoder trained on variable image sizes and aspect ratios, giving it stronger document and diagram understanding than most 128B-class models. Reasoning effort is configurable per-request, letting developers pay only for the compute they need — a practical answer to the "always-on thinking" overhead of fixed-effort reasoning models. Batch pricing ($0.75/$3.75 per 1M tokens input/output) makes it highly attractive for offline pipeline workloads.

With a 256K context window and open weights under a Modified MIT license, Mistral Medium 3.5 is the strongest self-hostable frontier alternative to date for organizations that cannot send data to proprietary cloud APIs. Its Intelligence Index of 39.2 and Coding Index of 35.4 place it solidly in the upper tier of frontier open-weight models.

**Key specs:** 256,000 tokens context | Text + Image | $1.50/$7.50 per 1M tokens (API); $0.75/$3.75 batch | Modified MIT (open weights) | GA on Mistral API + self-hosted (4 GPUs)

---

## Deep Dive: Most Important Release — Kimi K2.6 (April 20–21, 2026)

Kimi K2.6 represents the clearest signal yet that the agentic era has arrived not as a roadmap item but as a shipping product. While other labs have added tool-calling to chat models and called them "agentic," Moonshot AI has built K2.6 from first principles for sustained autonomous operation — 12-hour uninterrupted runs, 4,000 coordinated steps, and 300-agent swarms — and backed it up with benchmark results that match or exceed OpenAI and Anthropic's flagship offerings on coding and reasoning tasks, all under an open-weight license.

### What It Can Do

K2.6 executes long-horizon coding tasks autonomously, handling planning, execution, debugging, and verification across thousands of steps without human intervention. Its swarm-coordination capability — orchestrating up to 300 sub-agents in parallel — is a first in production open-weight models. Vision support via MoonViT (400M-parameter dedicated encoder) allows it to analyze screenshots, diagrams, and visual code artifacts natively. BrowseComp scores 83.2% standalone and 86.3% with swarm delegation, making it a strong candidate for complex web research agents. It also leads all compared models on Humanity's Last Exam (HLE-Full, with tools) at 54.0%, indicating broad scientific reasoning depth.

### Benchmark Highlights

| Benchmark | Kimi K2.6 | Previous Best / Closest Rival |
|---|---|---|
| AIME 2026 | 96.4% | GLM-5 / Kimi K2.5: 95.8% |
| LiveCodeBench v6 | 89.6% | DeepSeek V4 Flash (High): 88.4% |
| SWE-Bench Pro | 58.6% | GPT-5.4: 57.7% |
| SWE-Bench Verified | 80.2% | Claude Opus 4.6: 80.8% |
| Terminal-Bench 2.0 | 66.7% | GPT-5.5: 82.0% |
| HLE-Full (w/ tools) | 54.0% | Leads all compared models |
| GPQA Diamond | 90.5% | Claude Opus 4.7: 94.2% |
| BrowseComp (swarm) | 86.3% | BrowseComp solo: 83.2% |
| MathVision (w/ Python) | 93.2% | — |

### Architecture (known)

K2.6 uses a Mixture-of-Experts architecture with 1 trillion total parameters and 32 billion activated per forward pass. The MoE router selects 8 of 384 total experts per token plus 1 shared expert. Vision is handled by the purpose-built MoonViT encoder (400M parameters) rather than adapting a language-model backbone. Context compression is applied automatically at the 262K token boundary to support extended agentic runs without context-window failures. The swarm orchestration layer is implemented at the application level and is not intrinsic to the model weights.

### Pricing & Availability

K2.6 is available now on Kimi.com, the Kimi mobile app, via API, and through the Kimi Code CLI. Open weights are published on Hugging Face under a Modified MIT License, enabling self-hosting. API pricing has not been formally published at time of writing; Moonshot AI has historically offered competitive pricing relative to proprietary alternatives. Context window is 262,144 tokens with automatic compression for longer agentic runs.

### Strategic Significance

K2.6 is the first open-weight model to combine frontier-tier reasoning (AIME 96.4%), leading agentic coding (SWE-Bench Pro 58.6%), and production-grade multi-agent orchestration in a single release. For enterprises evaluating agentic deployments, it removes the forced choice between capability and data sovereignty: organizations can self-host K2.6 and achieve results that rival — and in some cases beat — proprietary locked APIs. This directly pressures OpenAI's Codex/GPT-5 tier and Anthropic's Claude Agent offerings, which require data to leave the customer's infrastructure.

The 300-agent swarm capability also marks a qualitative shift. Previous "multi-agent" frameworks required external orchestration layers; K2.6 makes swarm coordination a first-class model feature. If the benchmark-to-production transfer rate is high (Moonshot reports real-world production deployments from launch), this could reshape how enterprise software teams structure AI-assisted development pipelines in 2026.

For the open-source ecosystem, K2.6's Modified MIT license is the most permissive license attached to a 1T-parameter frontier model to date. Combined with Alibaba's Qwen3.6-27B (Apache 2.0) and Mistral Medium 3.5 (Modified MIT), the open-weight tier is now within measurable distance of the proprietary frontier on every major coding and reasoning benchmark — a structural change that would have been difficult to predict 12 months ago.

### Competitive Context

On SWE-Bench Pro (the harder variant requiring novel approaches), K2.6 (58.6%) edges out GPT-5.4 (57.7%) and substantially exceeds Claude Opus 4.6 (53.4%). Claude Opus 4.7 at 87.6% on SWE-Bench Verified remains the single strongest score on that particular benchmark, but Opus 4.7's SWE-Bench Pro figure has not been published. On pure math (AIME 2026, 96.4%) and live coding (LiveCodeBench v6, 89.6%), K2.6 is the current open-weight leader. GPT-5.5 remains ahead on Terminal-Bench 2.0 (82.0% vs. 66.7%) and leads ARC-AGI-2 at 85% — the one reasoning benchmark where K2.6 has not reported a score.

---

## Benchmark Comparison Data

```json
{"benchmark": "ARC-AGI-2", "results": [{"model": "GPT-5.5", "score": 85.0}, {"model": "GPT-5.4 Pro", "score": 83.3}, {"model": "Gemini 3.1 Pro", "score": 77.1}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8}, {"model": "Grok (xAI)", "score": 53.3}, {"model": "GPT-5.4", "score": 52.9}, {"model": "Gemini 3 Pro Deep Think", "score": 45.1}, {"model": "Llama 4", "score": 42.5}]}
```

```json
{"benchmark": "SWE-bench Verified", "results": [{"model": "Claude Opus 4.7", "score": 87.6}, {"model": "Kimi K2.6", "score": 80.2}, {"model": "Claude Opus 4.6", "score": 80.8}, {"model": "Mistral Medium 3.5", "score": 77.6}, {"model": "Qwen3.6-27B", "score": 77.2}, {"model": "Qwen3.6-35B-A3B", "score": 73.4}, {"model": "DeepSeek V4 Pro", "score": 80.6}]}
```

```json
{"benchmark": "SWE-bench Pro", "results": [{"model": "Kimi K2.6", "score": 58.6}, {"model": "GPT-5.4", "score": 57.7}, {"model": "Claude Opus 4.6", "score": 53.4}, {"model": "Qwen3.6-27B", "score": 53.5}, {"model": "Qwen3.6-35B-A3B", "score": 50.0}]}
```

```json
{"benchmark": "AIME 2026", "results": [{"model": "Kimi K2.6", "score": 96.4}, {"model": "GLM-5", "score": 95.8}, {"model": "Kimi K2.5", "score": 95.8}, {"model": "Qwen3.6 Plus", "score": 95.3}, {"model": "GLM-5.1", "score": 95.3}, {"model": "GPT-5.5 Instant (AIME 2025)", "score": 81.2}]}
```

```json
{"benchmark": "LiveCodeBench v6", "results": [{"model": "DeepSeek V4 Pro (Max)", "score": 93.5}, {"model": "Gemini 3.1 Pro Preview", "score": 91.7}, {"model": "DeepSeek V4 Flash (Max)", "score": 91.6}, {"model": "DeepSeek V4 Pro (High)", "score": 89.8}, {"model": "Kimi K2.6", "score": 89.6}, {"model": "Qwen3.6-27B", "score": 83.9}]}
```

```json
{"benchmark": "GPQA Diamond", "results": [{"model": "Claude Opus 4.7", "score": 94.2}, {"model": "Kimi K2.6", "score": 90.5}, {"model": "DeepSeek V4 Pro", "score": 90.1}, {"model": "GPT-5.4", "score": 88.0}, {"model": "Gemini 3.1 Flash-Lite", "score": 86.9}]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [{"model": "GPT-5.5", "score": 82.0}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 69.4}, {"model": "MiMo-V2.5-Pro", "score": 68.4}, {"model": "DeepSeek V4 Pro (Max)", "score": 67.9}, {"model": "Kimi K2.6", "score": 66.7}, {"model": "Qwen3.6-27B", "score": 59.3}]}
```

```json
{"benchmark": "MMLU (standard)", "results": [{"model": "GPT-5.4", "score": 92.0}, {"model": "Claude Opus 4.6", "score": 91.0}, {"model": "Gemini 3.1 Pro", "score": 90.0}, {"model": "DeepSeek V4", "score": 89.0}]}
```

```json
{"benchmark": "MMLU-Pro", "results": [{"model": "Gemini 3 Pro Preview (high)", "score": 89.8}, {"model": "Gemini 3 Pro Preview (low)", "score": 89.5}, {"model": "Claude Opus 4.5 (Reasoning)", "score": 89.5}, {"model": "GPT-5.4", "score": 78.0}, {"model": "Claude Opus 4.x", "score": 76.0}, {"model": "DeepSeek V4", "score": 74.0}]}
```

```json
{"benchmark": "LMSys Arena ELO (Coding)", "results": [{"model": "Claude Opus 4.7 Thinking", "score": 1573}, {"model": "GPT-5.5", "score": 1560}, {"model": "Claude Opus 4.6 Thinking", "score": 1500}, {"model": "Gemini 3.1 Pro Preview", "score": 1500}, {"model": "Grok 3 Preview", "score": 1493}, {"model": "Gemini 3 Pro", "score": 1485}]}
```

```json
{"benchmark": "HLE-Full (with tools)", "results": [{"model": "Kimi K2.6", "score": 54.0}]}
```

```json
{"benchmark": "BrowseComp", "results": [{"model": "Kimi K2.6 (swarm)", "score": 86.3}, {"model": "Kimi K2.6 (solo)", "score": 83.2}]}
```

```json
{"benchmark": "Tau-3 Telecom (agentic tool use)", "results": [{"model": "Mistral Medium 3.5", "score": 91.4}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| GPT-5.5 Instant | OpenAI | 400K | $5.00 | $30.00 | Text, Image |
| GPT-5.4 Pro | OpenAI | 256K | $3.00 | $15.00 | Text, Image, Audio |
| Claude Opus 4.7 | Anthropic | 1M in / 128K out | $5.00 | $25.00 | Text, High-res Vision |
| Claude Opus 4.6 | Anthropic | 200K | $15.00 | $75.00 | Text, Vision |
| Gemini 3.1 Pro | Google | 2M (≤200K: $2/$12; >200K: $4/$18) | $2.00 | $12.00 | Text, Image, Audio, Video |
| Gemini 3.1 Flash-Lite | Google | 1M | $0.25 | ~$1.00 | Text, Image |
| DeepSeek V4 Pro | DeepSeek | 1M | ~$2.00 | ~$8.00 | Text |
| Mistral Medium 3.5 | Mistral | 256K | $1.50 | $7.50 | Text, Image |
| Mistral Medium 3.5 (Batch) | Mistral | 256K | $0.75 | $3.75 | Text, Image |
| Kimi K2.6 | Moonshot AI | 262K | TBD | TBD | Text, Vision (MoonViT) |
| Qwen3.6-27B | Alibaba | 262K (1M ext.) | Open weights | Open weights | Text |
| Qwen3.6-35B-A3B | Alibaba | 262K | Open weights | Open weights | Text, Vision |
| Qwen3.5-27B-FP8 | Alibaba | 1M | Open weights | Open weights | Text, Vision, 200+ languages |
| Llama 4 Maverick | Meta | 1M | Open weights | Open weights | Text, Vision |
| Gemma 4 | Google | 128K | Open weights | Open weights | Text, Vision |

---

## Analysis & Impact

- **For software engineering / coding:** Claude Opus 4.7 sets a new state of the art at 87.6% SWE-bench Verified with output self-verification — but Kimi K2.6 (80.2% Verified, 58.6% Pro) and Qwen3.6-27B (77.2% Verified) both challenge it, the latter being fully self-hostable at Apache 2.0. Teams with data residency requirements no longer need to accept a significant capability penalty.

- **For frontier reasoning / math / science:** AIME 2026 is now dominated by Kimi K2.6 (96.4%) and a cluster of Chinese models (GLM-5, Kimi K2.5 at 95.8%). ARC-AGI-2 — the hardest public fluid-reasoning benchmark — is led by GPT-5.5 at 85%, the first model to approach the 85%+ grand prize threshold; Claude Opus 4.7's GPQA Diamond at 94.2% leads on graduate-level scientific reasoning. MMLU is saturated (top-4 within 3 points); MMLU-Pro at 89.8% (Gemini 3 Pro Preview) provides better discrimination going forward.

- **For multimodal / video / audio work:** Claude Opus 4.7's vision acuity jumped from 54.5% to 98.5% with its 3.75MP input upgrade — the largest single-generation vision quality leap from Anthropic. Gemini 3.1 Pro remains the leader in long-form multimodal (2M tokens, native audio + video ingestion). Kimi K2.6's MoonViT gives the open-weight tier a production-grade vision encoder for the first time at frontier scale.

- **For cost-sensitive or open-source deployments:** Qwen3.6-27B (Apache 2.0) at 77.2% SWE-bench Verified is the highest-performing Apache-licensed model ever. Mistral Medium 3.5 self-hosts on 4 GPUs at 163 tok/sec with 256K context for $1.50/$7.50 via API or free on-prem. Gemini 3.1 Flash-Lite at $0.25/1M input with 86.9% GPQA Diamond remains the strongest price-performance option for high-volume inference.

- **The agentic autonomy gap is now closing:** Kimi K2.6's 12-hour autonomous runs and 300-agent swarms are no longer a research demo — they are GA product features. OpenAI's GPT-5.5 Instant's dominance on Terminal-Bench 2.0 (82%) reflects strong tool-use in constrained CLI environments. The capability tier for true long-horizon agentic work has officially separated from chat-optimized models, and the open-weight tier (K2.6) is now at parity with — or ahead of — proprietary APIs on the metrics that matter most for agentic pipelines.

---

## Key Takeaways (TL;DR)

- **Kimi K2.6 leads AIME 2026 at 96.4% and SWE-bench Pro at 58.6%**, ships as open weights (Modified MIT), and is the first production model built for 12-hour autonomous agentic runs with 300-agent swarms.
- **GPT-5.5 Instant cuts hallucinations by 52.5%** versus its predecessor, tops ARC-AGI-2 at 85% (approaching the grand prize threshold), and is now the default model for all ChatGPT users as of May 5.
- **Claude Opus 4.7 hits 87.6% SWE-bench Verified** — the highest published score on that benchmark — with a new `xhigh` reasoning effort level and a 3.3× vision resolution upgrade bringing visual acuity to 98.5%.
- **Qwen3.6-27B outperforms a 397B MoE model on coding at Apache 2.0**, scoring 77.2% SWE-bench Verified with a 262K context window, shattering the assumption that frontier coding requires massive parameter counts.
- **Mistral Medium 3.5 consolidates three models into one 128B self-hostable open-weight model** with 256K context, 77.6% SWE-bench Verified, and $0.75/1M input batch pricing — the strongest single offering for on-premises enterprise deployment.

---

*Sources:*
- [Kimi K2.6 official release](https://kimi-k2.org/blog/24-kimi-k2-6-release)
- [MarkTechPost: Kimi K2.6](https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/)
- [OpenAI: GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/)
- [OpenAI: GPT-5.5 Instant System Card](https://openai.com/index/gpt-5-5-instant-system-card/)
- [Rolling Out: GPT-5.5 Instant hallucination reduction](https://rollingout.com/2026/05/05/openais-gpt-5-5-instant-reduces/)
- [LLM Reference: GPT-5.5 Instant specs](https://www.llmreference.com/model/gpt-5.5-instant)
- [Anthropic: Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude API Docs: What's new in Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7)
- [LLM Stats: Claude Opus 4.7 launch](https://llm-stats.com/blog/research/claude-opus-4-7-launch)
- [Alibaba Cloud: Qwen3.6-27B](https://www.alibabacloud.com/blog/qwen3-6-27b-flagship-level-coding-in-a-27b-dense-model_603063)
- [MarkTechPost: Qwen3.6-27B](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)
- [AWS: Qwen3.5 on SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/05/qwen-models-on-sagemaker-jumpstart/)
- [The Decoder: Mistral Medium 3.5](https://the-decoder.com/mistrals-new-flagship-medium-3-5-folds-chat-reasoning-and-code-into-one-model/)
- [CloudPrice: Mistral Medium 3.5 pricing](https://cloudprice.net/models/mistral-medium-3-5)
- [DataNorth: Mistral Medium 3.5 release](https://datanorth.ai/news/mistral-medium-3-5-release)
- [BenchLM: ARC-AGI-2 Benchmark](https://benchlm.ai/benchmarks/arcAgi2)
- [AgentMarketCap: ARC-AGI-2 leaderboard](https://agentmarketcap.ai/blog/2026/04/08/arc-agi-2-leaderboard-2026-gemini-abstract-reasoning-benchmark)
- [BenchLM: LiveCodeBench](https://benchlm.ai/benchmarks/liveCodeBench)
- [BenchLM: Terminal-Bench 2.0](https://benchlm.ai/benchmarks/terminalBench2)
- [BenchLM: AIME 2026](https://benchlm.ai/benchmarks/aime2026)
- [TokenMix: MMLU leaderboard 2026](https://tokenmix.ai/blog/mmlu-benchmark-leaderboard)
- [TokenCost: Claude Opus 4.7 pricing](https://tokencost.app/models/claude-opus-4-7)
- [DevTK: Gemini 3.1 Pro pricing](https://devtk.ai/en/models/gemini-3-1-pro/)
- [Google DeepMind: Gemini 3.1 Pro model card](https://deepmind.google/models/model-cards/gemini-3-1-pro)
- [LMSys Arena ELO April 2026](https://smartchunks.com/lmsys-arena-elo-leaderboard-explained-2026/)
- [BenchLM LLM Leaderboard History](https://benchlm.ai/llm-leaderboard-history)
- [Terminal-Bench official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0)
