# Best Models & Benchmarks — 2026-04-24

> **Editor's note:** Today (April 24, 2026) is unusually busy — OpenAI shipped GPT-5.5 yesterday, DeepSeek dropped two massive open-weight models this morning, Claude Opus 4.7 hit general availability a week ago, and Google's Gemini 3.1 Pro still holds the LMSYS Arena crown. Below is a complete briefing on everything that moved.

---

## Top Model News (5 Stories)

### 1. OpenAI GPT-5.5 — First Fully Retrained Agentic Model Since GPT-4.5

**Released:** April 23, 2026 | **Source:** [OpenAI Blog](https://openai.com/index/introducing-gpt-5-5/), [MarkTechPost](https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/)

GPT-5.5 is OpenAI's biggest architectural reset since GPT-4.5. Unlike prior GPT-5.x iterations (which were post-training improvements on the same base), 5.5 involves completely rewritten pretraining corpus, reworked model architecture, and agent-oriented training objectives baked in from the start. OpenAI describes it as "the difference between an assistant who needs a checklist and one who understands the underlying goal." The result is a model that can complete complex multi-step computer tasks — writing and running code, browsing the web, operating GUIs — with minimal human re-prompting at each handoff point.

The gains are concentrated in four domains that OpenAI calls "compounding-return" areas: agentic coding, computer use, knowledge work, and early scientific research. On Terminal-Bench 2.0 — the most demanding public benchmark for CLI-orchestrated multi-step workflows — GPT-5.5 scores 82.7%, a full 13 percentage-point lead over Claude Opus 4.7 (69.4%) and Gemini 3.1 Pro (68.5%). On GDPval, which tests AI agents across 44 occupational knowledge-work categories, it scores 84.9%. SWE-Bench Pro resolution lands at 58.6%, slightly behind Claude Opus 4.7's 64.3% on that metric. An important asterisk: OpenAI has publicly noted that Anthropic's SWE-bench Pro scores may be inflated by memorization on a subset of problems — independent verification is ongoing.

Pricing doubles compared to GPT-5.4: **$5/$30 per million tokens** (input/output) for the standard variant and **$30/$180** for GPT-5.5 Pro. OpenAI argues that GPT-5.5 uses fewer tokens per completed Codex task than 5.4, so the per-task effective cost may remain flat or drop for many workloads. Token efficiency is core to the pitch. The model is rolling out now to Plus, Pro, Business, and Enterprise subscribers; API access is imminent. Batch and Flex pricing run at half the standard rate.

**Key specs:**
| Property | Value |
|---|---|
| Context window | 1M tokens (400K in Codex) |
| Modalities | Text, code, tool use |
| Pricing (standard) | $5/$30 per 1M tokens |
| Pricing (Pro) | $30/$180 per 1M tokens |
| License | Proprietary |
| Availability | ChatGPT Plus/Pro/Business/Enterprise, Codex; API soon |

---

### 2. DeepSeek V4 Preview — Largest Open-Weight Model Yet, Released Today

**Released:** April 24, 2026 (today) | **Sources:** [TechCrunch](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/), [Hugging Face Blog](https://huggingface.co/blog/deepseekv4), [OfficeChai](https://officechai.com/ai/deepseek-v4-pro-deepseek-v4-flash-benchmarks-pricing/)

DeepSeek released two new open-weight MoE models today — V4-Pro (1.6T total / 49B active parameters) and V4-Flash (284B total / 13B active). Both carry 1M-token context windows, represent state-of-the-art open-weight capability, and are available right now on Hugging Face and the DeepSeek API. V4-Pro is the largest open-weight model available to date by total parameter count, eclipsing prior records held by Qwen3.5 (397B MoE).

The technical standout is the hybrid attention architecture. V4 combines Compressed Sparse Attention and Heavily Compressed Attention to make 1M-context inference economically viable at scale — at 1M tokens, V4-Pro requires only 27% of the single-token inference FLOPs and 10% of the KV cache compared to V3.2. That is a meaningful engineering achievement: long-context isn't just bolted on as a marketing number but is actually efficient at runtime. On LiveCodeBench, V4-Pro posts 93.5%, leading all public models. Codeforces rating comes in at 3,206, ahead of GPT-5.4 at 3,168.

The catch: V4 trails frontier proprietary models on knowledge-heavy benchmarks (MMLU-Pro: 87.5 vs. GPT-5.4's 87.5 parity, but behind Gemini 3.1 Pro on reasoning tasks), and the release is flagged as a "Preview" — a signal that DeepSeek wants real-world feedback before a final product launch. Pricing is extremely aggressive: **V4-Flash at $0.14/$0.28 per 1M tokens** and **V4-Pro at ~$0.145 per 1M input tokens** — roughly 35x cheaper than GPT-5.5 on input.

**Key specs:**
| Property | V4-Pro | V4-Flash |
|---|---|---|
| Total parameters | 1.6T | 284B |
| Active parameters | 49B | 13B |
| Context window | 1M tokens | 1M tokens |
| Input price | ~$0.145/1M | $0.14/1M |
| Output price | TBD (very low) | $0.28/1M |
| License | Open weights | Open weights |
| Availability | Hugging Face, DeepSeek API, chat.deepseek.com | Same |

---

### 3. Anthropic Claude Opus 4.7 — Top SWE-bench Verified, New Agentic Architecture

**Released:** April 16, 2026 | **Sources:** [HelpNet Security](https://www.helpnetsecurity.com/2026/04/16/claude-opus-4-7-released/), [DataStudios](https://www.datastudios.org/post/claude-opus-4-7-release-pricing-context-window-and-api-changes), [The Next Web](https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release)

Claude Opus 4.7 launched eight days ago and has already become the benchmark king for software engineering — it posts 87.6% on SWE-bench Verified (vs. Opus 4.6's 80.8%), 64.3% on the harder SWE-bench Pro, and 94.2% on GPQA Diamond (graduate-level biology, chemistry, physics). It also tops the LMSys Arena at approximately 1,503–1,505 Elo in "Thinking" mode, though the lead over Gemini 3.1 Pro and GPT-5.4 is within statistical noise (all three are separated by ~20 Elo points).

Key capability additions: a new `xhigh` effort level between `high` and `max` for fine-grained control over reasoning depth; high-resolution vision up to 2,576 pixels on the long edge (~3.75 megapixels, more than 3x the prior Claude models); self-verification before reporting outputs in agentic pipelines; and improved file-system memory across multi-session agentic work. The model also introduces automated cybersecurity safeguards that block high-risk cyber requests — a notable trust-and-safety architecture change. A restricted research model called Claude Mythos Preview (93.9% SWE-bench Verified, 94.5% GPQA Diamond) exists for security partners but is not publicly available.

Pricing is unchanged from Opus 4.6: **$5/$25 per million tokens**. Context window is 1M input / 128K output. The model is generally available on Claude.ai, the Claude API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry.

**Key specs:**
| Property | Value |
|---|---|
| Context window | 1M input / 128K output |
| Modalities | Text, image (high-res), tool use |
| Pricing | $5/$25 per 1M tokens |
| License | Proprietary |
| Availability | Claude.ai, API, Bedrock, Vertex AI, MS Foundry |

---

### 4. Zhipu AI GLM-5.1 — Open-Weight 754B Agentic Powerhouse for 8-Hour Tasks

**Released:** April 8, 2026 | **Source:** [MarkTechPost](https://www.marktechpost.com/2026/04/08/z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution/)

GLM-5.1 from Zhipu AI (Z.AI) is a 754-billion-parameter open-weight model with MIT license, specifically designed for long-horizon autonomous tasks. Its headline feature is sustained 8-hour autonomous execution — meaning it can work on a problem for a full workday without drifting or losing coherence in its internal state. This directly targets the growing enterprise use case of "AI worker shifts" rather than single-prompt completions. At the time of release, it achieved state-of-the-art on SWE-Bench Pro with 58.4%, matching or exceeding GPT-5.4 and Gemini 3.1 Pro on that metric (it has since been passed by Claude Opus 4.7's 64.3%).

The architecture uses a Mixture of Experts (MoE) approach with a novel Discrete Sparse Attention (DSA) mechanism designed to reduce attention compute at long context lengths. FP8 inference is supported with minimal quality loss, making large-scale deployment more cost-effective on standard hardware. The MIT license is notable — it means commercial use without restriction, making it one of the few large-scale models with true open-source licensing.

The Artificial Analysis Intelligence Index ranks GLM-5.1 at score 51 (top 6 globally), and LMSys Arena places it in the top 8. This is remarkable for an open-weight model from a Chinese AI lab operating outside the GPT/Claude/Gemini trifecta.

**Key specs:**
| Property | Value |
|---|---|
| Total parameters | 754B (MoE) |
| Context window | 256K tokens |
| Architecture | MoE + Discrete Sparse Attention |
| License | MIT (open source) |
| Availability | Hugging Face, Z.AI API |

---

### 5. Alibaba Qwen3.6 Family — Open-Weight Models Competitive with Frontier on Coding

**Released:** April 11–20, 2026 | **Sources:** [BuildFastWithAI](https://www.buildfastwithai.com/blogs/qwen3-6-max-preview-review-2026), [LabellerR](https://www.labellerr.com/blog/qwen3-6-35b-a3b-open-source-ai-model/), [ThePlanetTools](https://theplanettools.ai/blog/qwen-3-6-alibaba-beats-google-gemma-4-coding-benchmarks-2026)

Alibaba released three Qwen3.6 variants across April 11–20: the open-weight Qwen3.6-72B (April 11), the efficient sparse MoE Qwen3.6-35B-A3B (April 15–16), and the proprietary flagship Qwen3.6-Max-Preview (April 20). The 35B-A3B ("35B total, 3B active") is the headline open-weight surprise: it scores 92.7% on AIME 2026 (mathematics competition) and 71.4% on LiveCodeBench, outperforming Google's Gemma 4 on multiple coding benchmarks despite having 3B active parameters during inference — comparable to a 3B dense model on compute cost.

Qwen3.6 Plus (the managed API version) ranks #2 on LiveCodeBench v6 at 87.1%, behind only Gemini 3 Pro Preview at 91.7%. On SWE-bench Verified, Qwen3.6 Plus (listed as Qwen3.6 Plus / 78.8%) sits in the top 10 globally. The 201-language support in the broader Qwen3 family — inherited by Qwen3.6 — remains a differentiator for multilingual enterprise use cases.

For the open-source ecosystem, Qwen3.6 continues Alibaba's strategy of releasing capable, permissively licensed models (Apache 2.0) that pressure proprietary providers on price. The 35B-A3B is expected to become a popular fine-tuning base given its coding performance per active FLOP.

**Key specs (Qwen3.6-35B-A3B):**
| Property | Value |
|---|---|
| Total parameters | 35B (MoE) |
| Active parameters | 3B per token |
| Context window | 256K (native) |
| AIME 2026 | 92.7% |
| License | Apache 2.0 |
| Availability | Hugging Face, Qwen API |

---

## Deep Dive: Most Important Release — GPT-5.5 (April 23, 2026)

### What It Can Do

GPT-5.5 is not simply "smarter at answering questions." It is architecturally oriented toward agentic completion of multi-step computer tasks. The key behavioral difference from prior models: it reduces interruption frequency. Where earlier models (including GPT-5.4) would stall or produce wrong outputs at task handoff points — requiring users to re-prompt, correct, and re-inject context — GPT-5.5 is trained to handle those junctions autonomously.

Concretely, this means: debugging a failing CI pipeline end-to-end, writing and executing data-transformation scripts, navigating a GUI to fill out a form, doing long-horizon coding tasks (feature builds, refactors, deep debugging), and orchestrating sequences of tool calls. OpenAI tested it on a benchmark called Expert-SWE — internal tasks where the median estimated human completion time is 20 hours — and GPT-5.5 significantly outperforms GPT-5.4 there. On OSWorld-Verified (autonomous computer use), it scores 78.7%, meaning it successfully completes 78.7% of tasks that require navigating a real computer environment.

### Benchmark Highlights

| Benchmark | GPT-5.5 | Claude Opus 4.7 | Gemini 3.1 Pro | Notes |
|---|---|---|---|---|
| Terminal-Bench 2.0 | **82.7%** | 69.4% | 68.5% | Complex CLI multi-step workflows |
| GDPval | **84.9%** | — | — | Knowledge work across 44 occupations |
| SWE-bench Pro | 58.6% | **64.3%** | ~54% | Real GitHub issues (4 languages) |
| OSWorld-Verified | **78.7%** | — | — | Autonomous computer use |
| BrowseComp (Pro) | **90.1%** | — | 85.9% | Web research / hard-to-find info |
| Expert-SWE | Best OpenAI | — | — | 20-hour human tasks |
| GPQA Diamond | — | **94.2%** | 94.3% | Graduate reasoning |
| LMSys Arena Elo | ~1,483 | **~1,504** | ~1,492 | Human preference |
| AI Analysis Index | **57** (tied #1) | 57 (tied #1) | 57 (tied #1) | Composite score |

**Note:** GPT-5.5 leads on agentic/computer-use benchmarks; Claude Opus 4.7 leads on software engineering (SWE-bench Pro, SWE-bench Verified) and graduate reasoning; Gemini 3.1 Pro leads on ARC-AGI-2 and LMSYS Arena.

### Architecture

OpenAI has not published an architecture paper for GPT-5.5 but has disclosed:
- **Fully retrained base** — new pretraining corpus and architectural changes (not a post-training iteration of GPT-5.4)
- **Agent-oriented training objectives** built into pretraining, not just RLHF fine-tuning
- **Token efficiency improvement** — completes the same Codex workflows in materially fewer tokens than GPT-5.4
- **Latency parity** with GPT-5.4 despite higher capability, achieved via serving-side optimizations

This is a meaningful claim: prior scaling laws would predict that a ground-up retrain with higher capability would also be slower. Achieving capability improvement with latency parity suggests architectural innovations in the serving stack.

### Pricing & Availability

| Tier | Input | Output | Notes |
|---|---|---|---|
| GPT-5.5 (standard) | $5.00/1M | $30.00/1M | Double GPT-5.4 per-token; offset by token efficiency |
| GPT-5.5 Pro | $30.00/1M | $180.00/1M | High-accuracy, harder tasks |
| Batch/Flex | 50% discount | 50% discount | Applied to both tiers |

Rolling out now to Plus, Pro, Business, Enterprise (ChatGPT and Codex). API access announced as "imminent." ~4 million developers are already active on Codex weekly.

### Strategic Significance

GPT-5.5 is OpenAI's clearest bet on the "agentic computer use" market — the emerging category where AI doesn't just assist with tasks but completes them. The model is optimized for the exact use cases that enterprise SaaS products are being built around: code review, QA automation, data analysis pipelines, customer support escalation, and research synthesis. By leading on Terminal-Bench and GDPval while matching competitors on general reasoning, OpenAI is signaling a deliberate specialization rather than trying to top every leaderboard.

The pricing increase is a risk. At $5/$30, GPT-5.5 is 2x GPT-5.4 per token. OpenAI's "token efficiency offset" argument is credible for teams running Codex-style workloads at scale, but for general Q&A and short-context use cases, the effective cost increases materially. Competitors Claude Opus 4.7 ($5/$25) and Gemini 3.1 Pro ($2/$12) are now meaningfully cheaper per token for non-agentic work.

### Competitive Context

The frontier is genuinely three-way:
- **GPT-5.5** leads on agentic/computer-use tasks and terminal workflows
- **Claude Opus 4.7** leads on software engineering quality (SWE-bench), graduate reasoning, and human preference (Elo)
- **Gemini 3.1 Pro** leads on ARC-AGI-2 (abstract visual reasoning), maintains lowest price point among frontier models, and has the broadest modality support (native audio, video, images)

DeepSeek V4, dropping today, introduces a fourth axis: near-frontier capability at 35x lower input cost with open weights. For any organization willing to host or use the DeepSeek API, V4-Pro's LiveCodeBench score of 93.5% — beating all proprietary models on that metric — is a compelling data point.

---

## Benchmark Comparison Data

```json
{"benchmark": "LMSys Arena (Elo)", "updated": "2026-04-24", "results": [
  {"model": "Claude Opus 4.7 Thinking", "org": "Anthropic", "score": 1505},
  {"model": "Claude Opus 4.7", "org": "Anthropic", "score": 1500},
  {"model": "Gemini 3.1 Pro Preview", "org": "Google", "score": 1493},
  {"model": "Grok 4.20 Beta1", "org": "xAI", "score": 1488},
  {"model": "GPT-5.4 High", "org": "OpenAI", "score": 1483},
  {"model": "Gemini 3 Pro", "org": "Google", "score": 1486}
]}
```

```json
{"benchmark": "SWE-bench Verified (%)", "updated": "2026-04-24", "results": [
  {"model": "Claude Mythos Preview", "org": "Anthropic", "score": 93.9},
  {"model": "Claude Opus 4.7", "org": "Anthropic", "score": 87.6},
  {"model": "GPT-5.3 Codex", "org": "OpenAI", "score": 85.0},
  {"model": "Claude Opus 4.6", "org": "Anthropic", "score": 80.8},
  {"model": "Claude Opus 4.5", "org": "Anthropic", "score": 80.9},
  {"model": "Gemini 3.1 Pro", "org": "Google", "score": 80.6},
  {"model": "Qwen3.6 Plus", "org": "Alibaba", "score": 78.8}
]}
```

```json
{"benchmark": "SWE-bench Pro (%)", "updated": "2026-04-24", "results": [
  {"model": "Claude Opus 4.7", "org": "Anthropic", "score": 64.3},
  {"model": "GPT-5.5", "org": "OpenAI", "score": 58.6},
  {"model": "GLM-5.1", "org": "Zhipu", "score": 58.4},
  {"model": "GPT-5.4", "org": "OpenAI", "score": 57.7},
  {"model": "Gemini 3.1 Pro", "org": "Google", "score": 54.2}
]}
```

```json
{"benchmark": "GPQA Diamond (%)", "updated": "2026-04-24", "results": [
  {"model": "Claude Mythos Preview", "org": "Anthropic", "score": 94.5},
  {"model": "Gemini 3.1 Pro", "org": "Google", "score": 94.3},
  {"model": "Claude Opus 4.7", "org": "Anthropic", "score": 94.2},
  {"model": "GPT-5.4 Pro", "org": "OpenAI", "score": 92.8},
  {"model": "o3", "org": "OpenAI", "score": 91.8},
  {"model": "Claude Opus 4.5", "org": "Anthropic", "score": 91.6}
]}
```

```json
{"benchmark": "ARC-AGI-2 (%)", "updated": "2026-04-24", "human_baseline": 60, "results": [
  {"model": "Gemini 3.1 Pro / Deep Think", "org": "Google", "score": 85},
  {"model": "GPT-5.4", "org": "OpenAI", "score": 83},
  {"model": "Claude Opus 4.6", "org": "Anthropic", "score": 69},
  {"model": "GPT-5.2", "org": "OpenAI", "score": 52.9},
  {"model": "Gemini 3 Pro Deep Think", "org": "Google", "score": 45.1},
  {"model": "Claude Opus 4.5", "org": "Anthropic", "score": 37.6},
  {"model": "Grok 4", "org": "xAI", "score": 16},
  {"model": "DeepSeek V3.2", "org": "DeepSeek", "score": 4},
  {"model": "Qwen 3", "org": "Alibaba", "score": 1},
  {"model": "Llama 4 Maverick", "org": "Meta", "score": 0}
]}
```

```json
{"benchmark": "MMLU (%)", "updated": "2026-04-24", "results": [
  {"model": "o3", "org": "OpenAI", "score": 92.9},
  {"model": "GPT-5", "org": "OpenAI", "score": 92.5},
  {"model": "Gemini 3 Pro", "org": "Google", "score": 91.8},
  {"model": "o1", "org": "OpenAI", "score": 91.8},
  {"model": "Claude Opus 4.5", "org": "Anthropic", "score": 91.6},
  {"model": "DeepSeek V4-Pro", "org": "DeepSeek", "score": 87.5}
]}
```

```json
{"benchmark": "MMLU-Pro (%)", "updated": "2026-04-24", "results": [
  {"model": "Gemini 2.5 Ultra", "org": "Google", "score": 93.4},
  {"model": "o3", "org": "OpenAI", "score": 91.8},
  {"model": "Gemini 2.5 Pro", "org": "Google", "score": 86.2},
  {"model": "DeepSeek V4-Pro", "org": "DeepSeek", "score": 87.5}
]}
```

```json
{"benchmark": "LiveCodeBench v6 (%)", "updated": "2026-04-24", "results": [
  {"model": "Gemini 3 Pro Preview", "org": "Google", "score": 91.7},
  {"model": "Qwen3.6 Plus", "org": "Alibaba", "score": 87.1},
  {"model": "Kimi 2.6", "org": "Moonshot", "score": 89.6},
  {"model": "DeepSeek V4-Pro", "org": "DeepSeek", "score": 93.5},
  {"model": "Qwen3.5 397B", "org": "Alibaba", "score": 83.6},
  {"model": "Kimi K2.5", "org": "Moonshot", "score": 85.0}
]}
```

```json
{"benchmark": "AIME 2026 (%)", "updated": "2026-04-24", "results": [
  {"model": "Qwen3.6-35B-A3B", "org": "Alibaba", "score": 92.7}
]}
```

```json
{"benchmark": "Terminal-Bench 2.0 (%)", "updated": "2026-04-24", "results": [
  {"model": "GPT-5.5", "org": "OpenAI", "score": 82.7},
  {"model": "Claude Opus 4.7", "org": "Anthropic", "score": 69.4},
  {"model": "Gemini 3.1 Pro", "org": "Google", "score": 68.5}
]}
```

```json
{"benchmark": "GDPval (%)", "updated": "2026-04-24", "results": [
  {"model": "GPT-5.5", "org": "OpenAI", "score": 84.9},
  {"model": "GPT-5.5 Pro (BrowseComp)", "org": "OpenAI", "score": 90.1},
  {"model": "Gemini 3.1 Pro (BrowseComp)", "org": "Google", "score": 85.9}
]}
```

```json
{"benchmark": "Artificial Analysis Intelligence Index (composite/100)", "updated": "2026-04-24", "results": [
  {"model": "Gemini 3.1 Pro Preview", "org": "Google", "score": 57},
  {"model": "GPT-5.4", "org": "OpenAI", "score": 57},
  {"model": "Claude Opus 4.7", "org": "Anthropic", "score": 57},
  {"model": "GPT-5.3 Codex", "org": "OpenAI", "score": 54},
  {"model": "Claude Opus 4.6", "org": "Anthropic", "score": 53},
  {"model": "GLM-5.1", "org": "Zhipu", "score": 51},
  {"model": "GLM-5", "org": "Zhipu", "score": 50},
  {"model": "MiniMax-M2.7", "org": "MiniMax", "score": 50}
]}
```

```json
{"benchmark": "FrontierMath (score, Python-assisted)", "updated": "2026-04-24", "note": "Benchmark approaching saturation resistance; most models score very low", "results": [
  {"model": "GPT-5.4", "org": "OpenAI", "score": 0.476},
  {"model": "GPT-4o", "org": "OpenAI", "score": 0.403},
  {"model": "GPT-4 Turbo", "org": "OpenAI", "score": 0.267},
  {"model": "Claude 3.5 Sonnet", "org": "Anthropic", "score": 0.267},
  {"model": "Claude 3 Opus", "org": "Anthropic", "score": 0.263}
]}
```

```json
{"benchmark": "OSWorld-Verified (computer use, %)", "updated": "2026-04-24", "results": [
  {"model": "GPT-5.5", "org": "OpenAI", "score": 78.7}
]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities | License |
|---|---|---|---|---|---|---|
| GPT-5.5 | OpenAI | 1M (400K in Codex) | $5.00 | $30.00 | Text, code, tool use | Proprietary |
| GPT-5.5 Pro | OpenAI | 1M | $30.00 | $180.00 | Text, code, tool use | Proprietary |
| GPT-5.4 | OpenAI | 1M | $2.50 | $15.00 | Text, image, code | Proprietary |
| Claude Opus 4.7 | Anthropic | 1M in / 128K out | $5.00 | $25.00 | Text, image (hi-res), tool use | Proprietary |
| Gemini 3.1 Pro | Google | 1M | $2.00 | $12.00 | Text, image, audio, video, code | Proprietary |
| Gemini 3.1 Pro (200K+) | Google | 1M | $4.00 | $18.00 | Text, image, audio, video, code | Proprietary |
| Gemini 2.5 Pro | Google | 1M | $1.25 | $10.00 | Text, image, audio, video, code | Proprietary |
| Gemini 2.5 Flash | Google | 1M | $0.15 | $0.60 | Text, image, code | Proprietary |
| DeepSeek V4-Pro | DeepSeek | 1M | ~$0.145 | TBD (very low) | Text, code | Open weights |
| DeepSeek V4-Flash | DeepSeek | 1M | $0.14 | $0.28 | Text, code | Open weights |
| DeepSeek V3.2 | DeepSeek | 1M | ~$0.27 | ~$1.10 | Text, code | Open weights |
| Llama 4 Maverick | Meta | 1M | (self-host or API) | — | Text, image | Open weights |
| Llama 4 Scout | Meta | 10M | (self-host) | — | Text, image | Open weights |
| GLM-5.1 | Zhipu AI | 256K | API available | API available | Text, code | MIT |
| Qwen3.6 Plus | Alibaba | 256K | Competitive | Competitive | Text, code | Apache 2.0 (35B-A3B) |
| Mistral Small 4 | Mistral AI | 256K | Low-cost | Low-cost | Text, image | Apache 2.0 |

---

## Analysis & Impact

### Software Engineering Agents: Quality vs. Cost Tradeoff Is Now Real

Claude Opus 4.7's 87.6% SWE-bench Verified and 64.3% SWE-bench Pro performance makes it the obvious choice for autonomous code review, bug-fix agents, and pull-request automation where accuracy is paramount. However, DeepSeek V4-Pro's 93.5% on LiveCodeBench — the contamination-resistant coding benchmark — at 35x lower input cost creates a credible alternative for high-volume, less-sensitive workloads. Engineering teams should now run A/B cost analyses rather than defaulting to a single model.

### Agentic Computer Use Is the New Frontier Battleground

GPT-5.5's Terminal-Bench 2.0 score of 82.7% — 13+ points above the nearest competitor — signals OpenAI's specific bet on the "AI does the computer task" category. This is distinct from code generation (writing code) and moves toward code execution, tool coordination, and GUI operation. Expect Anthropic and Google to respond with comparable specialized benchmarks and model updates targeting this segment by mid-2026.

### Open-Weight Ecosystem Is Now Legitimately Competitive

The trio of DeepSeek V4 (today), GLM-5.1 (April 8), and Qwen3.6 (April 11–20) represents a step change in the open-weight tier. Six months ago, frontier-quality capability was exclusively proprietary. Today, organizations with infrastructure to run large MoE models can access near-frontier performance at a fraction of the API cost, with full data privacy and no vendor lock-in. This has major implications for regulated industries (healthcare, finance, government) where data sovereignty matters.

### The Context War Is Effectively Over: 1M Tokens Is Now Standard

Every major model release this month includes at least 1M-token context: GPT-5.5, Claude Opus 4.7, DeepSeek V4-Pro, DeepSeek V4-Flash, Gemini 3.1 Pro. Llama 4 Scout has a 10M context window. Gemini 2.5 Ultra (announced April 21) targets 2M natively. The "long context" feature has fully commoditized — the differentiator is now whether models can actually use that context well (retrieval quality, faithfulness, instruction following over long spans), not the raw number.

### ARC-AGI-2 Progress: Google Leads; Most Models Still Near-Zero

Gemini 3.1 Pro's 85% on ARC-AGI-2 (the hardest public reasoning benchmark, with a 60% human baseline and 85% prize threshold) is a landmark result — it is effectively at the prize boundary. GPT-5.4 at 83% and Claude Opus 4.6 at 69% follow. The drop-off is sharp: Grok 4 scores 16%, DeepSeek V3.2 scores 4%, and Llama 4 scores 0%. ARC-AGI-2 remains an effective separator of the very top frontier from everything else — it rewards genuine fluid intelligence, not pattern memorization.

---

## Key Takeaways (TL;DR)

- **GPT-5.5 is OpenAI's biggest architectural reset since GPT-4.5**, built from the ground up for agentic workflows — it leads on Terminal-Bench 2.0 (82.7%) and GDPval (84.9%) but trails Claude Opus 4.7 on SWE-bench Pro and general Elo, and costs 2x its predecessor at $5/$30 per million tokens.

- **DeepSeek V4 dropped today as open weights** — V4-Pro (1.6T params / 49B active) and V4-Flash are now on Hugging Face at ~$0.14–$0.145/1M input tokens, roughly 35x cheaper than GPT-5.5, with LiveCodeBench v6 performance of 93.5% that leads all public models on that metric.

- **Claude Opus 4.7 remains the best model for software engineering quality**, posting 87.6% SWE-bench Verified and 64.3% SWE-bench Pro, with the highest LMSys Arena Elo (~1,505 in Thinking mode), 1M context, high-res vision, and the same $5/$25 pricing as its predecessor.

- **The open-weight tier is now legitimately frontier-competitive**: DeepSeek V4, GLM-5.1 (MIT license, 754B, 8-hour agentic execution), and Qwen3.6 (92.7% AIME) give organizations with infrastructure genuine alternatives to proprietary APIs at dramatically lower cost and with full data control.

- **Benchmark saturation is accelerating**: MMLU is essentially done (all top models above 91%), GPQA Diamond has five models above 91%, and SWE-bench Verified is approaching 90%+ at the top — the field is moving to harder benchmarks (ARC-AGI-2, Terminal-Bench, GDPval, Expert-SWE) where meaningful differentiation still exists.

---

## Sources

- [OpenAI: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [MarkTechPost: GPT-5.5 Release — Terminal-Bench 2.0 and GDPval](https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/)
- [Dev.to: GPT-5.5 Pricing and Specs](https://dev.to/owen_fox/gpt-55-released-first-fully-retrained-base-model-since-gpt-45-1m-context-530-pricing-4nj0)
- [TechCrunch: DeepSeek V4 Preview](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/)
- [Hugging Face Blog: DeepSeek V4](https://huggingface.co/blog/deepseekv4)
- [OfficeChai: DeepSeek V4-Pro and V4-Flash Benchmarks](https://officechai.com/ai/deepseek-v4-pro-deepseek-v4-flash-benchmarks-pricing/)
- [HelpNet Security: Claude Opus 4.7](https://www.helpnetsecurity.com/2026/04/16/claude-opus-4-7-released/)
- [The Next Web: Claude Opus 4.7 Benchmarks](https://thenextweb.com/news/anthropic-claude-opus-4-7-coding-agentic-benchmarks-release)
- [DataStudios: Claude Opus 4.7 Pricing/Specs](https://www.datastudios.org/post/claude-opus-4-7-release-pricing-context-window-and-api-changes)
- [MarkTechPost: GLM-5.1 Release](https://www.marktechpost.com/2026/04/08/z-ai-introduces-glm-5-1-an-open-weight-754b-agentic-model-that-achieves-sota-on-swe-bench-pro-and-sustains-8-hour-autonomous-execution/)
- [LMSys Chatbot Arena Leaderboard 2026 — Promptt.dev](https://www.promptt.dev/blog/lmsys-chatbot-arena-leaderboard-2026)
- [AIDEV Day India: Arena Rankings April 2026](https://aidevdayindia.org/blogs/lmsys-chatbot-arena-current-rankings/lmsys-chatbot-arena-leaderboard-current-top-models.html)
- [BenchLM: SWE-bench Verified 2026](https://benchlm.ai/benchmarks/sweVerified)
- [TokenMix: SWE-bench 2026 Rankings](https://tokenmix.ai/blog/swe-bench-2026-claude-opus-4-7-wins)
- [BracAI: ARC-AGI-2 Benchmark Leaderboard](https://www.bracai.eu/post/arc-agi-2-benchmark)
- [BenchLM: ARC-AGI-2 Scores](https://benchlm.ai/benchmarks/arcAgi2)
- [BenchGecko: GPQA Diamond Rankings](https://benchgecko.ai/benchmark/gpqa-diamond)
- [BenchLM: GPQA Diamond](https://benchlm.ai/benchmarks/gpqaDiamond)
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)
- [SmartChunks: AA Intelligence Index April 2026](https://smartchunks.com/artificial-analysis-intelligence-index-april-2026-explained/)
- [FrontierMath Leaderboard — LLM Stats](https://llm-stats.com/benchmarks/frontiermath)
- [Gemini 3.1 Pro Pricing — LLM Stats](https://llm-stats.com/blog/research/gemini-3.1-pro-launch)
- [Google AI for Developers: Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Mistral AI: Mistral Small 4](https://mistral.ai/news/mistral-small-4/)
- [BuildFastWithAI: Best AI Models April 2026](https://www.buildfastwithai.com/blogs/best-ai-models-april-2026)
- [LabellerR: Qwen3.6-35B-A3B](https://www.labellerr.com/blog/qwen3-6-35b-a3b-open-source-ai-model/)
- [CodeSOTA: LLM Benchmarks 2026](https://codesota.com/llm)
- [cciedump: Gemini 2.5 Ultra Announcement](https://cciedump.spoto.net/news/google-unveils-gemini-25-ultra-frontier-reasoning-and-multimodal-leap-reshapes-llm-leaderboards.html)

---
*Compiled: 2026-04-24 | Agent: research-models | Data reflects publicly available benchmark results and pricing as of publication date. Benchmark scores are cited from named sources; none are invented. Pricing in USD per million tokens at standard (non-batch) rates unless noted.*
