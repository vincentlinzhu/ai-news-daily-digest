# Best Models & Benchmarks — 2026-05-15

## Top Model News (3-5)

### 1. Gemma 4 — Google DeepMind's First Apache 2.0 Open-Source Family Hits #3 on Arena AI
**Source:** [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4) | [Google Open Source Blog](https://opensource.googleblog.com/2026/03/gemma-4-expanding-the-gemmaverse-with-apache-20.html) | [Google DeepMind Model Page](https://deepmind.google/models/gemma/gemma-4/)

Released March–April 2026 and actively pushed to developers throughout May, Gemma 4 is Google DeepMind's most capable open-model family to date and the first Gemma release under the OSI-approved Apache 2.0 license — removing restrictions that blocked commercial use under earlier Gemma licenses. The family spans four sizes designed for very different hardware targets: Effective-2B and Effective-4B for mobile and IoT devices, a 26B Mixture-of-Experts (MoE) for constrained servers, and a 31B Dense model for PC and workstation deployment. Google claims all variants outperform competitors up to 20 times their own parameter count on standard evals.

On the Arena AI text leaderboard — the primary human-preference ranking — Gemma 4 31B sits at #3 globally (Arena ELO ~1,452) and the 26B MoE at #6 (~1,441), ahead of many closed models. On math, the 31B Dense model scores 89.2% on AIME 2026 and 80.0% on LiveCodeBench v6, results that were unimaginable from an open-weight model two years ago. Multimodal support covers audio, video, images, and 140 natural languages, with native function calling for agentic workflows. The models are available on Hugging Face, Google AI Studio, Vertex AI, and Ollama.

The strategic significance is the licensing shift: Apache 2.0 means companies can fine-tune, serve, and redistribute Gemma 4 without negotiating terms with Google. Combined with performance that sits inside the top-10 globally, this puts a Google-quality model in the hands of the entire open ecosystem at essentially zero incremental licensing cost.

**Key specs:** Up to 31B Dense / 26B MoE | Text, Audio, Image, Video | Apache 2.0 | Free (self-hosted) / Pay-as-you-go on Vertex AI | Available globally

---

### 2. xAI Grok Build — Terminal-Native Agentic Coding CLI Launches in Beta (May 14)
**Source:** [xAI](https://grokai.build/) | [Dataconomy](https://dataconomy.com/2026/05/15/xai-launches-grok-build-coding-agent-for-developers/) | [Kingy AI](https://kingy.ai/ai/xai-drops-grok-build-an-agentic-cli-that-wants-to-live-in-your-terminal/)

xAI launched Grok Build in early beta on May 14, 2026 — a terminal-native CLI coding agent powered by Grok 4.3, positioned directly against Claude's Kimi Code CLI, OpenAI Codex CLI, and Google Gemini CLI. Currently exclusive to SuperGrok Heavy subscribers ($300/month), Grok Build targets professional software engineers who want a local-first agent that executes entirely on their machine rather than in the cloud. The agent can read full repositories, propose structured plans for review, open code diffs, install dependencies, run shell commands, and check its own work in a plan-review-approve loop.

The distinguishing architecture is its parallel subagent model: Grok Build spawns specialized sub-agents for large tasks and coordinates them across git worktrees simultaneously — a pattern similar to Kimi K2.6's 300-agent swarm and Anthropic's Managed Agents multiagent orchestration. Integration points include GitHub, AGENTS.md convention files, MCP servers, ACP (Agent Control Protocol) for custom bots, and hooks/plugins for security scanning and compliance workflows. A headless mode enables CI/CD integration.

With Grok 4.3 reduced in price to $2.50/M output tokens (announced May 14 Grok retirement schedule), the per-task compute cost for Grok Build sessions is among the lowest of any frontier-model CLI agent. This matters for high-volume dev team deployments where per-token costs accumulate rapidly across long coding sessions.

**Key specs:** Backed by Grok 4.3 | Text, Code | $300/month (SuperGrok Heavy) | Local-first, no cloud execution | Beta access to SuperGrok Heavy subscribers

---

### 3. OpenAI Codex Goes Mobile — iOS & Android Preview Launches May 14
**Source:** [SiliconANGLE](https://siliconangle.com/2026/05/14/openai-brings-codex-mobile-devices-adds-customization-features/) | [Digital Trends](https://www.digitaltrends.com/computing/openai-is-bringing-in-the-mighty-codex-tool-to-the-chatgpt-app-on-your-phone/) | [APIdog Guide](https://apidog.com/blog/openai-codex-from-your-phone/)

OpenAI launched Codex on iOS and Android on May 14, 2026, embedded within the ChatGPT mobile app — making the GPT-5.5-powered agentic coding platform accessible from any device. The mobile experience is designed as a remote control rather than a full editor: users can initiate new tasks or work from GitHub issues, monitor live thread progress, inspect diffs and test results, approve pending commands, interrupt tasks to save tokens, and comment on pull requests that Codex opens — all from their phone. Code and credentials remain on the host machine; only real-time status streams to mobile via an encrypted relay layer.

The launch came with two companion features: **Hooks** (customizable scripts that process Codex prompts/responses for security scanning and compliance logging) and **Remote SSH** (encrypted tunnels letting Codex reach remote dev environments). These are aimed squarely at enterprise security teams worried about agentic code execution in regulated environments. The preview rolled out across all ChatGPT tiers including Free and Go, with macOS support now and Windows coming soon.

This is the first time a top-5 coding agent has shipped a first-party mobile presence for monitoring and control. Combined with GPT-5.5's 88.7% SWE-bench score and the new Hooks compliance infrastructure, OpenAI is building a Codex platform moat — not just a model API.

**Key specs:** GPT-5.5 powered | Text, Code | Included in all ChatGPT tiers (Free through Enterprise) | Preview on iOS/Android | macOS host required currently

---

### 4. Kimi K2.6 — Moonshot AI's Open-Weight 1T MoE Sets AIME 2026 Record at 96.4% (April, New Leaderboard Entries)
**Source:** [MarkTechPost](https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/) | [Microsoft Azure Foundry Blog](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-kimi-k2-6-in-microsoft-foundry/4513125) | [Kimi K2 Org](https://kimi-k2.org/blog/24-kimi-k2-6-release)

Released in late April 2026 (GA April 21), Kimi K2.6 has continued to climb leaderboards through mid-May and now holds the top spot on AIME 2026 (96.4%), Terminal-Bench 2.0 (66.7% among open models), and sits at #4 globally on the Artificial Analysis Intelligence Index. The model is a 1-trillion-parameter MoE with 32B active parameters, 384 experts (8 selected per token + 1 shared), and a 262K-token context window. Under a Modified MIT License, the full weights are on Hugging Face — making K2.6 the most capable openly-licensed MoE currently available.

The standout capability is long-horizon agentic operation: K2.6 sustains autonomous 12-hour sessions with up to 4,000 coordinated steps, and can natively orchestrate up to 300 sub-agents in swarm configurations. This out-of-the-box multi-agent orchestration at open-weight availability is unprecedented. It's also multimodal (text, image, video input) and integrates with Microsoft Azure Foundry, meaning enterprise teams can deploy it with Azure's compliance and data residency guarantees.

Pricing at $0.95/M input and $4.00/M output makes K2.6 significantly cheaper than Claude Opus 4.7 ($5/$25) or GPT-5.5 ($5/$30) while delivering competitive benchmark performance — including 80.2% on SWE-bench Verified, just 7 points below Claude Opus 4.7 (Adaptive).

**Key specs:** 1T total / 32B active params, 384 experts | 262K context | Text, Image, Video | $0.95/$4.00 per 1M tokens | Modified MIT License | Hugging Face + Azure Foundry

---

### 5. GLM-5.1 — Z.AI's Long-Horizon Agentic Model Hits 8-Hour Autonomous Sessions, MIT License
**Source:** [Z.AI Blog](https://z.ai/blog/glm-5) | [Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-everything-you-need-to-know) | [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/04/glm-5-1/)

Z.AI (formerly Zhipu AI) updated GLM-5 to GLM-5.1 in April 2026, adding a key capability: the model evaluates intermediate results and revises its approach hundreds of times before delivering final output, enabling sustained autonomous operation up to 8 hours on a single task. The architecture is a 754B-total/40B-active MoE with DeepSeek Sparse Attention (DSA), released under MIT license with a 200K-token context window and 128K max output. GLM-5.1 reaches #7 on the Artificial Analysis Intelligence Index (score 51.4), ahead of GPT-5.2.

On AIME 2026, GLM-5.1 reaches 95.3%, tied with Qwen 3.6 Plus for second place globally — a remarkable result from a Chinese open-source lab. SWE-bench Verified sits at 77.8%, and Vending Bench 2 (agentic business simulation) shows GLM-5.1 approaching frontier closed-model performance at $4,432 final balance vs. Claude Opus 4.5's $4,967. Pricing at $1.40 input / $4.40 output per 1M tokens is well below Western frontier models.

**Key specs:** 754B total / 40B active | 200K context / 128K output | Text, Code | $1.40/$4.40 per 1M tokens | MIT License | Hugging Face + Z.AI API

---

## Deep Dive: Most Important Release — Gemma 4 (Released April 2026, Active Leaderboard Mover May 15)

The Gemma 4 family is the defining open-model event of mid-May 2026 because it collapses three separate barriers simultaneously: license freedom (Apache 2.0 removes the proprietary restriction that blocked Gemma 1–3 from unrestricted commercial use), scale accessibility (31B Dense and 26B MoE fit on consumer/prosumer hardware while reaching top-10 Arena AI), and multimodal breadth (audio, video, 140 languages, function calling). No previous open-weight model has simultaneously cleared all three bars at Arena ELO above 1,440.

### What It Can Do

Gemma 4's 31B Dense model handles complex multi-step reasoning across text, code, images, audio, and video in a single model, with native function calling for building autonomous agents. It achieves 89.2% on AIME 2026 mathematics and 80.0% on LiveCodeBench v6, outperforming many models with 5–10× its parameter count. The 26B MoE variant provides similar capability with lower inference costs for server deployments. The E2B and E4B variants are designed specifically for on-device inference on mobile hardware. All variants support structured JSON output and multi-step planning primitives required for agentic tool-use loops.

### Benchmark Highlights

| Benchmark | Gemma 4 31B | Gemma 4 26B MoE | Previous Open-Weight Best |
|---|---|---|---|
| Arena AI Text ELO | ~1,452 (#3 overall) | ~1,441 (#6 overall) | ~1,447 (Qwen 3.6 Plus) |
| AIME 2026 | 89.2% | 88.3% | 95.3% (Kimi K2.6) |
| LiveCodeBench v6 | 80.0% | 77.1% | 93.5% (DeepSeek V4 Pro) |
| MMLU Multilingual | 85.2% | 82.6% | ~85.8% (Qwen3.5-32B) |

### Architecture (known)

Gemma 4 uses Google DeepMind's standard Transformer architecture for the Dense variants and a Mixture-of-Experts architecture for the 26B MoE, following the design patterns established in Gemma 3. All models include native multimodal encoders for audio and video, a departure from the text-only Gemma 3 family. The E2B/E4B models use aggressive quantization and knowledge distillation from the larger 31B teacher. Specific layer counts and attention head configurations are not publicly disclosed.

### Pricing & Availability

- **Self-hosted**: Free under Apache 2.0 (Hugging Face, Ollama, any inference stack)
- **Google AI Studio**: Free tier available; paid tier for higher rate limits
- **Vertex AI**: Standard Vertex inference pricing (per-token, varies by region)
- **Context**: Up to 128K tokens (model supports more; API limits may vary by provider)
- **Availability**: Global, released to Hugging Face and Google AI Studio from April 2, 2026

### Strategic Significance

The Apache 2.0 license change is the biggest strategic move. Gemma 1 and 2 used Google's custom Gemma Terms of Use, which prohibited certain commercial uses and competitive applications. Apache 2.0 means any company — including those competing with Google — can deploy, fine-tune, and redistribute Gemma 4 without any Google approval. This matches the model against Llama 4's custom commercial license (which has its own restrictions) and puts Gemma 4 closer to DeepSeek V4 Pro's MIT-adjacent terms.

Google's goal is to make Gemma the default open-model backbone for the Android and Pixel hardware ecosystem. With E2B and E4B models targeting mobile, and the larger models available on all major cloud platforms, Gemma 4 is positioned to become the open-source reference architecture that Google controls the roadmap for — similar to how Meta uses Llama.

The convergence of Apache 2.0 licensing, multimodal capability, top-10 Arena performance, and four hardware-targeted size tiers in a single release makes Gemma 4 the most strategically significant open-model family of Q2 2026. It also puts Google in a position to benefit from the fine-tuning and application ecosystem that will develop around these weights.

### Competitive Context

Gemma 4 31B sits between Llama 4 Maverick (Arena ELO ~1,441, MMLU Pro 80.5%) and Kimi K2.6 (Arena ELO ~1,447, AIME 96.4%) on overall leaderboard position. On math (AIME 89.2%), Gemma 4 trails Kimi K2.6 (96.4%) and Qwen 3.6 Plus (95.3%) but exceeds Llama 4 Maverick (not reported). On coding (LiveCodeBench 80.0%), Gemma 4 trails DeepSeek V4 Pro (93.5%) and Kimi K2.6 (89.6%) but leads Llama 4 Maverick (43.4%). GLM-5 (77.8% SWE-bench) and Gemma 4 are roughly competitive on software engineering, but Gemma 4's multimodal capability and licensing make it the preferred base for most deployment scenarios.

---

## Benchmark Comparison Data

```json
{"benchmark": "Artificial Analysis Intelligence Index", "results": [{"model": "Claude Opus 4.7 (Adaptive)", "score": 57.3}, {"model": "Gemini 3.1 Pro", "score": 57.2}, {"model": "GPT-5.4", "score": 56.8}, {"model": "MiMo-V2.5-Pro", "score": 53.8}, {"model": "GPT-5.3 Codex", "score": 53.6}, {"model": "DeepSeek V4 Pro", "score": 51.5}, {"model": "GLM-5.1", "score": 51.4}, {"model": "GPT-5.2", "score": 51.3}, {"model": "Qwen3.6 Plus", "score": 50.0}, {"model": "GLM-5", "score": 49.8}]}
```

```json
{"benchmark": "LMSys Arena Overall ELO (as of late April 2026)", "results": [{"model": "Claude Opus 4.6 Thinking", "score": 1504}, {"model": "Gemini 3.1 Pro Preview", "score": 1493}, {"model": "GPT-5.4 High", "score": 1484}, {"model": "Grok 4.3", "score": 1471}, {"model": "DeepSeek V4 Pro", "score": 1462}, {"model": "Claude Sonnet 4.6", "score": 1458}, {"model": "GPT-5.4 Standard", "score": 1455}, {"model": "Gemini 3.0 Pro", "score": 1449}, {"model": "Qwen 3.6 Plus", "score": 1447}, {"model": "Meta Muse Spark", "score": 1441}, {"model": "Gemma 4 31B", "score": 1452}, {"model": "Gemma 4 26B MoE", "score": 1441}]}
```

```json
{"benchmark": "SWE-bench Verified", "results": [{"model": "Claude Mythos Preview", "score": 93.9}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 87.6}, {"model": "GPT-5.5", "score": 88.7}, {"model": "GPT-5.3 Codex", "score": 85.0}, {"model": "Claude Opus 4.5", "score": 80.9}, {"model": "DeepSeek V4 Pro (Max)", "score": 80.6}, {"model": "Gemini 3.1 Pro", "score": 80.6}, {"model": "Kimi K2.6", "score": 80.2}, {"model": "MiniMax M2.5", "score": 80.2}, {"model": "GLM-5", "score": 77.8}, {"model": "Qwen 3.6 Plus", "score": 78.8}, {"model": "MiMo-V2.5-Pro", "score": 57.2}]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [{"model": "GPT-5.5", "score": 85.0}, {"model": "Gemini 3.1 Deep Think", "score": 84.6}, {"model": "GPT-5.4 Pro", "score": 83.0}, {"model": "Claude Opus 4.6", "score": 69.0}]}
```

```json
{"benchmark": "AIME 2026", "results": [{"model": "Kimi K2.6", "score": 96.4}, {"model": "Qwen3.6 Plus", "score": 95.3}, {"model": "GLM-5.1", "score": 95.3}, {"model": "GLM-5", "score": 95.8}, {"model": "GPT-5.2", "score": 100.0}, {"model": "Claude Opus 4.6", "score": 100.0}, {"model": "Claude Sonnet 4.5", "score": 100.0}, {"model": "Gemma 4 31B", "score": 89.2}, {"model": "Gemma 4 26B MoE", "score": 88.3}]}
```

```json
{"benchmark": "GPQA Diamond", "results": [{"model": "Gemini 3.1 Pro", "score": 94.3}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 94.2}, {"model": "GPT-5.5", "score": 93.6}, {"model": "GPT-5.4", "score": 92.8}, {"model": "Kimi K2.6", "score": 90.5}, {"model": "DeepSeek V4 Pro", "score": 90.1}, {"model": "Claude Opus 4.6", "score": 89.2}, {"model": "DeepSeek V4 Pro (High)", "score": 89.1}]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [{"model": "Claude Mythos Preview", "score": 92.1}, {"model": "GPT-5.5", "score": 82.7}, {"model": "GPT-5.3 Codex", "score": 77.3}, {"model": "GPT-5.4", "score": 75.1}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 69.4}, {"model": "MiMo-V2.5-Pro", "score": 68.4}, {"model": "Kimi K2.6", "score": 66.7}, {"model": "Qwen 3.6 Max (preview)", "score": 65.4}, {"model": "Qwen 3.6 Plus", "score": 61.6}, {"model": "DeepSeek V4 Pro (Max)", "score": 67.9}]}
```

```json
{"benchmark": "LiveCodeBench v6", "results": [{"model": "DeepSeek V4 Pro (Max)", "score": 93.5}, {"model": "DeepSeek V4 Flash (Max)", "score": 91.6}, {"model": "Gemini 3.0 Pro Preview", "score": 92.0}, {"model": "Gemini 3.1 Pro Preview", "score": 91.7}, {"model": "Kimi K2.6", "score": 89.6}, {"model": "DeepSeek V4 Pro (High)", "score": 89.8}, {"model": "Gemma 4 31B", "score": 80.0}, {"model": "Gemma 4 26B MoE", "score": 77.1}, {"model": "Llama 4 Maverick", "score": 43.4}]}
```

```json
{"benchmark": "SWE-bench Pro (harder variant)", "results": [{"model": "Claude Opus 4.7", "score": 64.3}, {"model": "GLM-5.1", "score": 58.4}, {"model": "MiMo-V2.5-Pro", "score": 57.2}, {"model": "Kimi K2.6", "score": 58.6}, {"model": "MiniMax M2.7", "score": 56.22}, {"model": "Claude Opus 4.6", "score": 53.4}]}
```

```json
{"benchmark": "WorldArena (Robotics)", "results": [{"model": "ShengShu MotuBrain", "score": 63.77}]}
```

```json
{"benchmark": "RoboTwin 2.0 (Robotics, randomized env)", "results": [{"model": "ShengShu MotuBrain", "score": 96.0}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Opus 4.7 | Anthropic | 1M tokens | $5.00 | $25.00 | Text, Image |
| GPT-5.5 | OpenAI | 1.05M tokens | $5.00 | $30.00 | Text, Image, Audio, Code, Computer Use |
| Gemini 3.1 Pro | Google | 2.0M tokens | $2.00 | $12.00 | Text, Audio, Image, Video, Code |
| Kimi K2.6 | Moonshot AI | 262K tokens | $0.95 | $4.00 | Text, Image, Video |
| MiMo-V2.5-Pro | Xiaomi | 1M tokens | $1.00 | $3.00 | Text, Image, Audio, Video |
| GLM-5.1 | Z.AI | 200K tokens | $1.40 | $4.40 | Text, Code |
| DeepSeek V4 Pro | DeepSeek | 1M tokens | $1.74 ($0.44 promo) | $3.48 ($0.87 promo) | Text, Code |
| Qwen 3.6 Plus | Alibaba | 1M tokens | ~$0.40 | ~$2.40 | Text, Code, Image |
| Qwen 3.5 Plus | Alibaba | 1M tokens | $0.40 | $2.40 | Text, Code |
| Gemma 4 31B | Google (self-host) | 128K+ | Free (Apache 2.0) | Free | Text, Audio, Image, Video |
| Gemma 4 26B MoE | Google (self-host) | 128K+ | Free (Apache 2.0) | Free | Text, Audio, Image, Video |
| Llama 4 Maverick | Meta (self-host / API) | 1M tokens | $0.27 | $0.85 | Text, Image |
| Llama 4 Scout | Meta (self-host / API) | 10M tokens | $0.08 | $0.30 | Text, Image |
| GLM-5 | Z.AI | 200K tokens | $1.40 | $4.40 | Text, Code |
| MiniMax M2.5 | MiniMax | — | ~$1.00/hr (100 tok/s) | — | Text, Code |

---

## Analysis & Impact

- **For software engineering / coding:** Claude Opus 4.7 (Adaptive) at 87.6% SWE-bench Verified and Kimi K2.6 at 80.2% are the clearest production-ready choices for autonomous coding agents; Kimi K2.6 at $0.95/$4.00 per 1M tokens now delivers within 8 points of Claude Opus 4.7 at 1/6th the output cost, making it compelling for high-volume automated PR workflows. GPT-5.5 (88.7% SWE-bench) remains the benchmark leader on generally available models, but at $30/M output tokens, cost scales rapidly in long agentic sessions.

- **For frontier reasoning / math / science:** AIME 2026 scores now reach 100% for multiple frontier closed models (GPT-5.2, Claude Opus 4.6) and 96.4% for Kimi K2.6 open-weight — rendering AIME 2026 saturated for top-tier models. GPQA Diamond (94.3% Gemini 3.1 Pro) remains the highest-signal reasoning benchmark, with Gemini 3.1 Pro and Claude Opus 4.7 essentially tied at the frontier. ARC-AGI-2 (85% GPT-5.5, 84.6% Gemini Deep Think) remains the most differentiating held-out test of genuine novel problem-solving.

- **For multimodal / video / audio work:** Gemini 3.1 Pro's 2M-token context and native audio + video processing — at $2/$12 per 1M tokens — sets the price-performance benchmark for multimodal pipelines. Gemma 4's Apache 2.0 license and four-size family (including on-device E2B/E4B) makes it the preferred open-source multimodal backbone for products needing audio/video without vendor lock-in. MiMo-V2.5-Pro (Xiaomi) uniquely supports text + image + audio + video in a single open-weight 1T MoE at $1/$3, previously impossible in a single model at that price point.

- **For cost-sensitive or open-source deployments:** Gemma 4 31B (Apache 2.0, top-10 Arena) is the clearest free option for production deployments needing strong reasoning. DeepSeek V4 Pro at $0.44/$0.87 (promotional until May 31) remains the cheapest capable model for coding; after June 1, rates revert to $1.74/$3.48. Llama 4 Scout at $0.08/$0.30 is the lowest-cost option for long-document and RAG workloads (10M context). Kimi K2.6 and GLM-5.1 (both MIT/Modified MIT) are the recommended open-weight choices for teams needing agentic coding at the frontier without per-token API costs.

- **The "agentic CLI" pattern is now table stakes:** Every major AI lab now ships a terminal-native agentic coding agent: OpenAI Codex CLI (GPT-5.5), Claude Kimi Code CLI, Gemini CLI, Grok Build (xAI, launched May 14), and Kimi Code (Moonshot). The differentiators are now multi-agent orchestration (Kimi K2.6 300-agent swarm vs. Grok Build parallel subagents), compliance infrastructure (Codex Hooks, Remote SSH), and pricing — not the raw model capability which has largely converged across the top-5.

---

## Key Takeaways (TL;DR)

- Gemma 4 31B reaches #3 on the Arena AI leaderboard under Apache 2.0 license — the first Google open model with unrestricted commercial use at top-10 quality.
- Kimi K2.6 tops AIME 2026 at 96.4% and Terminal-Bench 2.0 among open models at 66.7%, while offering native 300-agent swarm orchestration under Modified MIT license at $0.95/$4.00 per 1M tokens.
- xAI launched Grok Build on May 14 — a local-first terminal CLI agent backed by Grok 4.3, completing the set of top-5 lab agentic coding CLIs (alongside OpenAI Codex, Claude CLI, Gemini CLI, Kimi Code).
- OpenAI Codex went mobile on May 14 with iOS/Android preview, Hooks for compliance, and Remote SSH — the first major agentic coding platform to ship cross-device monitoring and control to all subscription tiers including Free.
- GPT-5.5 leads SWE-bench Verified at 88.7% and ARC-AGI-2 at 85% among generally available models, but Claude Opus 4.7 (87.6% SWE-bench, 94.2% GPQA Diamond) has closed the gap to within noise margin on all major benchmarks except ARC-AGI-2.

---

*Sources:*

- https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4
- https://opensource.googleblog.com/2026/03/gemma-4-expanding-the-gemmaverse-with-apache-20.html
- https://deepmind.google/models/gemma/gemma-4/
- https://grokai.build/
- https://dataconomy.com/2026/05/15/xai-launches-grok-build-coding-agent-for-developers/
- https://kingy.ai/ai/xai-drops-grok-build-an-agentic-cli-that-wants-to-live-in-your-terminal/
- https://siliconangle.com/2026/05/14/openai-brings-codex-mobile-devices-adds-customization-features/
- https://www.digitaltrends.com/computing/openai-is-bringing-in-the-mighty-codex-tool-to-the-chatgpt-app-on-your-phone/
- https://apidog.com/blog/openai-codex-from-your-phone/
- https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/
- https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-kimi-k2-6-in-microsoft-foundry/4513125
- https://kimi-k2.org/blog/24-kimi-k2-6-release
- https://z.ai/blog/glm-5
- https://artificialanalysis.ai/articles/glm-5-everything-you-need-to-know
- https://www.analyticsvidhya.com/blog/2026/04/glm-5-1/
- https://www.anthropic.com/news/claude-opus-4-7
- https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- https://openai.com/index/introducing-gpt-5-5/
- https://developers.openai.com/api/docs/pricing
- https://ai.google.dev/gemini-api/docs/pricing
- https://deepmind.google/models/model-cards/gemini-3-1-pro/
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/
- https://www.swfte.com/blog/lmsys-arena-leaderboard-may-2026
- https://benchlm.ai/benchmarks/sweVerified
- https://llm-stats.com/benchmarks/terminal-bench-2
- https://benchlm.ai/benchmarks/terminalBench2
- https://llm-stats.com/benchmarks/aime-2026
- https://benchlm.ai/benchmarks/aime2026
- https://benchlm.ai/benchmarks/gpqaDiamond
- https://artificialanalysis.ai/evaluations/gpqa-diamond
- https://arcprize.org/leaderboard
- https://benchlm.ai/benchmarks/liveCodeBench
- https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
- https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html
- https://roboticsandautomationnews.com/2026/05/15/shengshu-unveils-world-action-model-to-offer-infinite-possibilities-for-robotic-intelligence/101620/
- https://www.marktechpost.com/2026/04/22/xiaomi-releases-mimo-v2-5-pro-and-mimo-v2-5-matching-frontier-model-benchmarks-at-significantly-lower-token-cost/
- https://decrypt.co/365184/xiaomi-mimo-2-5-pro-ai-see-hear-act-one-model
- https://api-docs.deepseek.com/quick_start/pricing
- https://platform.kimi.ai/docs/pricing/chat-k26
- https://tokencost.app/models/kimi-k2-6
- https://pricepertoken.com/pricing-page/provider/qwen
- https://tokencost.app/models/llama-4-maverick
- https://tokencost.app/models/llama-4-scout
- https://ai.meta.com/blog/Llama-4-multimodal-intelligence/
