# Best Models & Benchmarks — 2026-05-22

## Top Model News (3-5)

### 1. Gemini 3.5 Flash — Google's Fastest Frontier Model Launches at Google I/O 2026
**Source:** [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) | [Google DeepMind Model Card](https://deepmind.google/models/model-cards/gemini-3-5-flash/) | [CIO Dive](https://www.ciodive.com/news/google-unveils-Gemini-agentic-models/820783/)

Gemini 3.5 Flash launched at Google I/O 2026 on May 19 as the first model in Google's new 3.5 generation, replacing Gemini 3.1 Pro as the default model for the Gemini app, AI Mode in Google Search, and the Google Antigravity platform. Google claims it is the strongest Flash-tier model ever shipped, outperforming the previous premium Gemini 3.1 Pro on most of the agentic benchmarks the Flash line was built for — notably posting 76.2% on Terminal-Bench 2.1 against Gemini 3.1 Pro's 68.5% (same harness), and 83.6% on the multi-step MCP Atlas benchmark, beating every model in Google's comparison table. The model delivers 289 tokens/second sustained output at $1.50 input / $9.00 output per million tokens — approximately four times the throughput of comparable flagship models at roughly half their cost.

Beyond raw speed, Gemini 3.5 Flash ships with a full 1M-token context window, multimodal capabilities spanning text, image, and video understanding, and configurable reasoning depth. Its ARC-AGI-2 score of 72.1% clears the 66% human average threshold, though it lags GPT-5.5's 84.6% on that specific test. Google announced at the same event that Gemini 3.5 Pro — currently in internal testing — will ship "next month" (June 2026), drawing audible groans from the live I/O audience.

The strategic significance is large: Gemini 3.5 Flash is deployed to over one billion monthly users as the Gemini app default from day one, making it the highest-distribution frontier-level model in history. The pricing undercuts GPT-5.5 ($5/$30 per M tokens) by more than 3× on input and makes heavy agentic workloads dramatically cheaper. Google Antigravity (the Google Cloud AI compute infrastructure) processes this model at scale for enterprise customers.

**Key specs:** 1M token context | Text, image, video input | $1.50/$9.00 per 1M tokens | Proprietary | GA — Gemini app, Gemini API (AI Studio, Android Studio), Antigravity, Gemini Enterprise

---

### 2. GPT-5.5 Instant — OpenAI's New Daily Driver for 500M+ ChatGPT Users
**Source:** [OpenAI Blog](https://openai.com/index/gpt-5-5-instant/) | [OpenAI API Docs](https://developers.openai.com/api/docs/models/gpt-5.5) | [DataNorth Coverage](https://datanorth.ai/news/openai-releases-gpt-5-5-instant)

OpenAI deployed GPT-5.5 Instant as the new ChatGPT default model on May 5, 2026, replacing GPT-5.3 Instant for all tiers including free users. The model claims a 52.5% reduction in hallucinated claims on high-stakes medical, legal, and financial prompts — a headline safety improvement that doubles as a quality signal. GPT-5.5 Instant is the "daily driver" sibling of GPT-5.5 Thinking (which launched April 23 for Pro/Plus users) and GPT-5.5 Pro, sharing the same generation but tuned for conversational flow and latency rather than maximal reasoning depth.

GPT-5.5 Instant introduces deeply expanded personalization: the model now draws on past conversations, uploaded files, and optionally connected Gmail to produce contextually relevant responses without manual context re-injection. Memory sources are surfaced with attribution so users can audit or delete what context was used, and a "temporary chat" mode disables all personalization. For developers, the `chat-latest` API alias now resolves to GPT-5.5 Instant (snapshot `gpt-5.5-2026-04-23`), and the model supports 1,050,000 token context with configurable `reasoning_effort` (`none`, `low`, `medium`, `high`, `xhigh`).

This is the first OpenAI Instant-tier model classified as "High capability" under AISI's Cybersecurity and Biological & Chemical Preparedness categories, triggering additional safety protocols even for the lightweight product tier. GPT-5.3 Instant remains accessible under its explicit model ID for paid API users through approximately August 2026.

**Key specs:** 1,050,000 token context | Text, image input | $5.00/$30.00 per 1M tokens (128K max output) | Proprietary | GA — all ChatGPT tiers, API (`chat-latest`)

---

### 3. Kimi K2.6 — Moonshot AI's Trillion-Parameter Open-Weight Agent Model
**Source:** [Replicate Model Page](https://replicate.com/moonshotai/kimi-k2.6) | [NVIDIA NIM Reference](https://docs.api.nvidia.com/nim/reference/moonshotai-kimi-k2-6) | [Miraflow Analysis](https://miraflow.ai/blog/kimi-k2-6-explained-moonshot-ai-open-source-model-ties-gpt-5-5-coding)

Moonshot AI released Kimi K2.6 on April 20–29, 2026 (preview April 20, GA/NVIDIA April 29), marking the most capable open-weight agentic coding model available as of late May 2026. Built on a trillion-parameter MoE backbone with 32B active parameters per token, K2.6 is natively multimodal (text, images, video via MoonViT 400M encoder), runs on 262K-token context with automatic session compression for multi-hour tasks, and is purpose-built to orchestrate up to 300 sub-agents executing 4,000+ coordinated steps in a single autonomous run. Key validated benchmark results include: AIME 2026 96.4% (#1 among open-weight models on llm-stats.com), GPQA Diamond 90.5%, HLE-Full with tools 54.0% (open-source leader), SWE-Bench Verified 80.2%, SWE-Bench Pro 58.6% (matching GPT-5.5's published SWE-Bench Pro score).

In published Moonshot showcases, K2.6 spent 13 hours overhauling a legacy financial matching engine (4,000+ lines of code, 1,000+ tool calls), achieving 185% throughput improvement. A second showcase saw the model deploy Qwen3.5-0.8B, implement inference in Zig, and optimize from ~15 to ~193 tokens/second across 14 autonomous iterations — without human intervention. These are not benchmark simulations; they are agentic execution logs with verifiable outputs.

At $0.95 input / $4.00 output per million tokens, K2.6 undercuts GPT-5.5 by more than 5× on input and roughly 7.5× on output, while posting broadly competitive or superior scores on agentic benchmarks. The Modified MIT license permits commercial use below a revenue threshold, making it the highest-performing commercially-viable open-weight coding model currently available. Validated by Vercel and Factory.ai as a production coding agent.

**Key specs:** 262K token context (auto-compression for longer runs) | Text, image, video input | $0.95/$4.00 per 1M tokens | Modified MIT open-weight | Kimi API, Kimi Code CLI, NVIDIA NIM, Hugging Face (`moonshotai/Kimi-K2.6`)

---

### 4. Claude Opus 4.7 — Anthropic's Most Capable GA Model with xhigh Effort and Hi-Res Vision
**Source:** [Anthropic Blog](https://www.anthropic.com/news/claude-opus-4-7?5=) | [Claude API Docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7) | [BenchLM Coding Leaderboard](https://benchlm.ai/coding)

Anthropic released Claude Opus 4.7 on April 16, 2026 as its most capable generally-available model. Benchmarked as #2 overall on SWE-bench Verified (87.6%) behind the restricted Claude Mythos Preview, and #2 on SWE-bench Pro (64.3%), Opus 4.7 is the strongest coding model freely available to API customers. On the LMSys Arena as of mid-April, Claude Opus 4.7 Thinking posted ~1505 Elo — holding the #1 overall text leaderboard slot. Three significant upgrades shipped with this release: (1) a new `xhigh` effort level between `high` and `max`, giving developers finer reasoning-vs-latency control on hard tasks; (2) high-resolution image support expanded to 2,576px / 3.75MP (up from 1,568px / 1.15MP), directly improving computer use, screenshot analysis, and document understanding; (3) task budgets in public beta, letting developers give Claude a running token countdown so it can prioritize work and finish gracefully on long agentic runs.

Claude Code integration ships new capabilities simultaneously: the `/ultrareview` slash command produces a detailed code review flagging bugs and design issues that a careful senior engineer would catch; Auto Mode in Claude Code (now extended to Max users) allows the model to make approval decisions autonomously for extended runs. These are consequential for production agentic engineering pipelines. On GPQA Diamond, Opus 4.7 posts 94.2% (within 0.1% of Gemini 3.1 Pro's 94.3% lead), and its ARC-AGI-2 score of 75.8% puts it in the second tier behind GPT-5.5's 84.6%.

Pricing for Opus 4.7 is unchanged from Opus 4.6 at $5 input / $25 output per million tokens — a meaningful contrast to GPT-5.5's $5/$30 and a sharp undercut of GPT-5.5 Pro's $30 output rate. It is available across all major cloud platforms: Anthropic API, Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry.

**Key specs:** 1M token context | 128K max output | Text, image (up to 3.75MP) input | $5.00/$25.00 per 1M tokens | Proprietary | GA — Anthropic API (`claude-opus-4-7`), Bedrock, Vertex AI, Foundry

---

### 5. DeepSeek V4 — First Open-Weight Frontier MoE of 2026 Closes the Gap on Proprietary Leaders
**Source:** [DeepSeek V4 Guide](https://deepseekai.guide/news/deepseek-v4-release-date/) | [DeepSeek V4 Model Card](https://deepseekai.guide/models/deepseek-v4/) | [Handy AI Analysis](https://handyai.substack.com/p/model-drop-deepseek-v4)

DeepSeek V4 launched April 22–24, 2026 in two MIT-licensed tiers: V4-Pro (1.6T total / 49B active per token, 1M context) and V4-Flash (284B total / 13B active, 1M context). Trained on Huawei Ascend 950 + Cambricon hardware — a notable geopolitical signal — V4-Pro posts Codeforces rating 3,206 (highest ever reported by any model at release), LiveCodeBench 93.5% (open-weight state of the art), and Terminal-Bench 2.0 67.9% (above Claude Opus 4.6's 65.4%). V4-Pro carries SWE-Bench Verified 80.6%, matching Gemini 3.1 Pro and within 0.2 points of Claude Opus 4.6's 80.8% at the time of release.

The honest limitation: DeepSeek's own technical report acknowledges that V4-Pro trails the frontier closed-source leaders by "roughly 3 to 6 months" on reasoning benchmarks. Against the models current at publication (April 23–24, 2026), V4-Pro lags Opus 4.7 (released April 16) and GPT-5.5 (released April 23) by 3–15 points on agentic benchmarks. DeepSeek chose not to update its benchmark comparison table to include Opus 4.7, drawing criticism from independent analysts. Nonetheless, on price/performance for open-source deployments V4 Pro is extraordinary: $1.74 input / $3.48 output per million tokens via the API, with MIT-licensed weights deployable on 8×H100 hardware.

V4-Flash (284B, 13B active) fits on a single 80GB GPU in 4-bit quantization or a 2×48GB box with Unsloth GGUF builds, making it practical for teams that require self-hosted inference. Combined, the V4 tier provides the first credible open-weight alternative to frontier proprietary models for full-stack software engineering tasks in 2026.

**Key specs (V4-Pro):** 1M token context (384K output) | Text input | $1.74/$3.48 per 1M tokens | MIT license | GA — DeepSeek API, Hugging Face (`deepseek-ai/DeepSeek-V4-Pro`), vLLM/SGLang day-0

---

## Deep Dive: Most Important Release — Gemini 3.5 Flash (May 19, 2026)

Gemini 3.5 Flash is the defining model event of this week because it is the first time a sub-premium-tier model has landed in a billion-user consumer product, a developer API, and an enterprise compute platform simultaneously from day one. While prior Flash-tier models were secondary offerings, Gemini 3.5 Flash *is* the Gemini app — it is the model all Search AI Mode users interact with, making its real-world deployment footprint larger than any previous frontier release. Its pricing undercut of proprietary competitors also signals that the inference economics war is shifting from throughput races to cost-per-quality-point competition.

### What It Can Do

Gemini 3.5 Flash scores 76.2% on Terminal-Bench 2.1 — the benchmark measuring autonomous terminal-based coding tasks — beating Gemini 3.1 Pro (68.5%) and Claude Opus 4.7's disclosed score (66.1%) while approaching GPT-5.5's 78.2%. On MCP Atlas (multi-step workflows via Model Context Protocol), it posts 83.6%, beating every model in the official comparison table including GPT-5.5 (75.3%) and Gemini 3.1 Pro (78.2%). The model processes 1M-token context at 289 tokens/second, and achieved generating a functioning operating system in 12 hours in Google's internal showcase. On multimodal reasoning benchmarks (CharXiv 84.2%, MMMU-Pro 83.6%), it matches or exceeds GPT-5.5. Its GDPval-AA Elo of 1,656 positions it between Gemini 3 Flash (1,204) and Gemini 3.1 Pro (1,314) on economically-valued knowledge work — a gap GPT-5.5 closes at 1,769 and Claude Opus 4.7 at 1,753.

### Benchmark Highlights

| Benchmark | Gemini 3.5 Flash | Previous Best (Model) |
|---|---|---|
| Terminal-Bench 2.1 | 76.2% | 78.2% (GPT-5.5) |
| MCP Atlas | 83.6% | 79.1% (Claude Opus 4.7) — Flash leads |
| SWE-Bench Pro (single attempt) | 55.1% | 64.3% (Claude Opus 4.7) |
| OSWorld-Verified | 78.4% | 78.7% (GPT-5.5) |
| ARC-AGI-2 | 72.1% | 84.6% (GPT-5.5) |
| Humanity's Last Exam | 40.2% | 46.9% (Claude Opus 4.7) |
| CharXiv Reasoning | 84.2% | 84.1% (GPT-5.5) — Flash leads |
| MMMU-Pro | 83.6% | 81.2% (GPT-5.5) — Flash leads |
| Finance Agent v2 | 57.9% | 51.8% (GPT-5.5) — Flash leads |
| GDPval-AA (Elo) | 1,656 | 1,769 (GPT-5.5) |
| MRCR v2 @ 1M tokens | 26.6% | 94.8% (GPT-5.5, 128K only disclosed) |

### Architecture (known)

Google has not publicly disclosed the parameter count or training methodology for Gemini 3.5 Flash. The model-card methodology page at `deepmind.com/models/evals-methodology/gemini-3-5-flash` references a multimodal architecture evaluated across "tool use, multimodal capabilities, and multi-turn context." Based on the MCP Atlas and Toolathlon results, the model is natively tool-calling with strong multi-step orchestration. Output speed of 289 tok/s at full context suggests an efficient speculative decoding or distillation approach relative to Gemini 3.1 Pro. Gemini Omni (announced at the same I/O event) is a separate model for cinematic video generation; Gemini 3.5 Flash is the text/multimodal reasoning tier.

### Pricing & Availability

- **Paid API:** $1.50 input / $9.00 output per 1M tokens; cached input $0.15 / 1M; context caching storage $1.00 / 1M tokens per hour
- **Free tier:** Available in Google AI Studio with usage limits
- **Context window:** 1,000,000 tokens
- **Max output:** Not separately disclosed (inherits Gemini API standard)
- **Available on:** Gemini app (default), AI Mode in Google Search (default), Google AI Studio, Android Studio, Gemini API, Gemini Enterprise Agent Platform, Google Antigravity
- **Grounding:** Google Search and Google Maps grounding available at 5,000 prompts/month free, then $14/1,000 queries

### Strategic Significance

Gemini 3.5 Flash is Google's clearest assertion yet that the AI wars will be decided on inference economics and distribution, not solely benchmark supremacy. By making a model that beats Gemini 3.1 Pro on most agentic tasks the default for *every* Gemini app and Google Search user — at half the API cost — Google simultaneously undercuts OpenAI's monetization of frontier-tier pricing and creates a moat through search integration that no competitor can replicate. The $1.50/M input price point puts it closer to commodity pricing than to frontier pricing, yet it outperforms models that cost 2–3× more on the specific benchmarks enterprise and developer customers care about most.

The delay of Gemini 3.5 Pro — confirmed publicly with an audible audience reaction at I/O — is significant context. Pro is the model Google itself internally ranks as the actual capability leap; Flash is the deployment vehicle. This mirrors OpenAI's strategy with the GPT-5.5 Instant / Thinking split: ship the daily-driver broadly first, hold the reasoning heavyweight for a separate launch that can command premium pricing. It also means the competitive picture will shift meaningfully again in approximately 4–6 weeks when 3.5 Pro reaches GA.

The MCP Atlas score (83.6%) is the most consequential individual benchmark result in this release. As the AI industry converges on MCP as the standard for agentic tool orchestration — following AWS MCP Server GA and Docker MCP Gateway — a model that outperforms every competitor on multi-step MCP workflows is positioned to capture the enterprise agentic workload that represents the fastest-growing segment of AI compute spend.

### Competitive Context

On the benchmarks where direct comparison is possible, Gemini 3.5 Flash trails GPT-5.5 on SWE-Bench Pro (55.1% vs 58.6%), Terminal-Bench 2.1 (76.2% vs 78.2%), ARC-AGI-2 (72.1% vs 84.6%), and HLE (40.2% vs 41.4%). It leads GPT-5.5 on MCP Atlas (83.6% vs 75.3%), MMMU-Pro (83.6% vs 81.2%), CharXiv (84.2% vs 84.1%), Finance Agent v2 (57.9% vs 51.8%), and OSWorld-Verified (78.4% vs 78.7%). Against Claude Opus 4.7, Flash leads on Terminal-Bench 2.1 (76.2% vs 66.1%), MCP Atlas (83.6% vs 79.1%), and MMMU-Pro (83.6% vs 75.2%), but trails significantly on SWE-Bench Pro (55.1% vs 64.3%) and Humanity's Last Exam (40.2% vs 46.9%). The closest rival at comparable price is Kimi K2.6 ($0.95/$4.00), which leads on HLE-Full with tools (54.0%) and AIME 2026 (96.4%), but has lower documented MCP-native benchmark coverage.

---

## Benchmark Comparison Data

```json
{"benchmark": "SWE-bench Verified", "results": [{"model": "Claude Mythos Preview", "score": 93.9}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 87.6}, {"model": "GPT-5.5", "score": 88.7}, {"model": "GPT-5.3 Codex", "score": 85.0}, {"model": "DeepSeek V4-Pro (Max)", "score": 80.6}, {"model": "Claude Sonnet 4.6", "score": 79.6}, {"model": "Gemini 3.1 Pro", "score": 80.6}, {"model": "Mistral Medium 3.5", "score": 77.6}, {"model": "Kimi K2.6", "score": 80.2}]}
```

```json
{"benchmark": "SWE-bench Pro", "results": [{"model": "Claude Mythos Preview", "score": 77.8}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 64.3}, {"model": "Qwen3.7 Max", "score": 60.6}, {"model": "GPT-5.5", "score": 58.6}, {"model": "Kimi K2.6", "score": 58.6}, {"model": "Gemini 3.5 Flash", "score": 55.1}, {"model": "Gemini 3.1 Pro", "score": 54.2}, {"model": "DeepSeek V4-Pro (Max)", "score": 55.4}]}
```

```json
{"benchmark": "Terminal-Bench 2.1", "results": [{"model": "GPT-5.5", "score": 78.2}, {"model": "Gemini 3.5 Flash", "score": 76.2}, {"model": "Gemini 3.1 Pro (T-Bench 2.1)", "score": 70.3}, {"model": "Claude Opus 4.7", "score": 66.1}, {"model": "Claude Sonnet 4.6", "score": 58.0}]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [{"model": "GPT-5.5 (Codex CLI)", "score": 82.7}, {"model": "DeepSeek V4-Pro (Max)", "score": 67.9}, {"model": "Kimi K2.6", "score": 66.7}, {"model": "Claude Opus 4.6", "score": 65.4}]}
```

```json
{"benchmark": "GPQA Diamond", "results": [{"model": "Claude Mythos Preview", "score": 94.5}, {"model": "Gemini 3.1 Pro", "score": 94.3}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 94.2}, {"model": "GPT-5.5 Pro", "score": 94.2}, {"model": "GPT-5.5", "score": 93.6}, {"model": "GPT-5.4", "score": 92.8}, {"model": "Kimi K2.6", "score": 90.5}, {"model": "DeepSeek V4-Pro (Max)", "score": 90.1}, {"model": "Mistral Medium 3.5", "score": 74.8}]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [{"model": "GPT-5.5", "score": 84.6}, {"model": "Gemini 3.1 Pro Preview", "score": 77.1}, {"model": "Claude Opus 4.7", "score": 75.8}, {"model": "Gemini 3.5 Flash", "score": 72.1}, {"model": "Claude Sonnet 4.6", "score": 58.3}, {"model": "Gemini 3 Flash", "score": 33.6}]}
```

```json
{"benchmark": "AIME 2026", "results": [{"model": "Kimi K2.6", "score": 96.4}, {"model": "Qwen3.6 Plus", "score": 95.3}, {"model": "GLM-5.1 (Z.AI)", "score": 95.3}, {"model": "Qwen3.6 35B-A3B", "score": 94.1}, {"model": "DeepSeek V4-Pro (Max) (HMMT 2026 proxy)", "score": 95.2}, {"model": "Claude Opus 4.6", "score": 100.0}, {"model": "GPT-5.2", "score": 100.0}, {"model": "Claude Sonnet 4.5", "score": 100.0}]}
```

```json
{"benchmark": "LiveCodeBench", "results": [{"model": "DeepSeek V4-Pro (Max)", "score": 93.5}, {"model": "Gemini 3.1 Pro", "score": 91.7}, {"model": "Kimi K2.6", "score": 89.6}, {"model": "Claude Opus 4.6", "score": 88.8}]}
```

```json
{"benchmark": "LMSys Arena Overall ELO (April 17-19, 2026)", "results": [{"model": "Claude Opus 4.7 Thinking", "score": 1505}, {"model": "Claude Opus 4.6 Thinking", "score": 1503}, {"model": "Claude Opus 4.7", "score": 1498}, {"model": "Claude Opus 4.6", "score": 1497}, {"model": "Meta Muse Spark", "score": 1496}, {"model": "Gemini 3.1 Pro Preview", "score": 1492}, {"model": "Gemini 3 Pro", "score": 1486}, {"model": "Grok 4.20 Beta1", "score": 1485}, {"model": "GPT-5.4 High", "score": 1482}, {"model": "Claude Sonnet 4.6 Thinking", "score": 1467}]}
```

```json
{"benchmark": "MCP Atlas (multi-step tool workflows)", "results": [{"model": "Gemini 3.5 Flash", "score": 83.6}, {"model": "Gemini 3.1 Pro", "score": 78.2}, {"model": "Claude Opus 4.7", "score": 79.1}, {"model": "GPT-5.5", "score": 75.3}, {"model": "Claude Sonnet 4.6", "score": 69.5}, {"model": "Gemini 3 Flash", "score": 62.0}]}
```

```json
{"benchmark": "OSWorld-Verified (computer use)", "results": [{"model": "GPT-5.5", "score": 78.7}, {"model": "Gemini 3.5 Flash", "score": 78.4}, {"model": "Gemini 3.1 Pro", "score": 76.2}, {"model": "Claude Sonnet 4.6", "score": 72.5}, {"model": "Kimi K2.6", "score": 73.1}, {"model": "Gemini 3 Flash", "score": 65.1}]}
```

```json
{"benchmark": "Humanity's Last Exam (HLE, no tools)", "results": [{"model": "Claude Opus 4.7", "score": 46.9}, {"model": "Gemini 3.1 Pro", "score": 44.4}, {"model": "GPT-5.5", "score": 41.4}, {"model": "Gemini 3.5 Flash", "score": 40.2}, {"model": "DeepSeek V4-Pro (Max)", "score": 37.7}]}
```

```json
{"benchmark": "HLE with tools", "results": [{"model": "Kimi K2.6", "score": 54.0}, {"model": "GPT-5.4", "score": 52.1}, {"model": "Claude Opus 4.6", "score": 53.0}, {"model": "Gemini 3.1 Pro", "score": 51.4}]}
```

```json
{"benchmark": "GDPval-AA (Elo, economically-valued knowledge work)", "results": [{"model": "GPT-5.5", "score": 1769}, {"model": "Claude Opus 4.7", "score": 1753}, {"model": "Claude Sonnet 4.6", "score": 1676}, {"model": "Gemini 3.5 Flash", "score": 1656}, {"model": "Gemini 3.1 Pro", "score": 1314}, {"model": "Gemini 3 Flash", "score": 1204}]}
```

```json
{"benchmark": "MMMU-Pro (multimodal reasoning)", "results": [{"model": "Gemini 3.5 Flash", "score": 83.6}, {"model": "Gemini 3 Flash", "score": 81.2}, {"model": "GPT-5.5", "score": 81.2}, {"model": "Gemini 3.1 Pro", "score": 80.5}, {"model": "Claude Opus 4.7", "score": 75.2}, {"model": "Kimi K2.6", "score": 79.4}]}
```

```json
{"benchmark": "CharXiv Reasoning (charts)", "results": [{"model": "Gemini 3.5 Flash", "score": 84.2}, {"model": "GPT-5.5", "score": 84.1}, {"model": "Gemini 3.1 Pro", "score": 83.3}, {"model": "Claude Opus 4.7", "score": 82.1}, {"model": "Gemini 3 Flash", "score": 80.3}, {"model": "Kimi K2.6", "score": 80.4}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| Claude Mythos Preview | Anthropic | 1M | ~$125 (restricted) | N/A | Text, Image |
| GPT-5.5 (Thinking) | OpenAI | 1,050,000 | $5.00 | $30.00 | Text, Image, Audio |
| GPT-5.5 Instant | OpenAI | 1,050,000 | $5.00 | $30.00 | Text, Image |
| Claude Opus 4.7 | Anthropic | 1M | $5.00 | $25.00 | Text, Image (3.75MP) |
| Gemini 3.5 Flash | Google | 1M | $1.50 | $9.00 | Text, Image, Video |
| Gemini 3.1 Pro | Google | 2M | $2.70 | $16.20 | Text, Image, Video, Audio |
| Kimi K2.6 | Moonshot AI | 262K | $0.95 | $4.00 | Text, Image, Video |
| Claude Sonnet 4.6 | Anthropic | 1M | $3.00 | $15.00 | Text, Image |
| DeepSeek V4-Pro | DeepSeek | 1M | $1.74 | $3.48 | Text |
| DeepSeek V4-Flash | DeepSeek | 1M | $0.14 | $0.28 | Text |
| Mistral Medium 3.5 | Mistral AI | 256K | $1.50 | $7.50 | Text, Image |
| Qwen3.7 Max | Alibaba | 1M | $0.50 | $3.00 | Text |
| Qwen3.6-27B (open) | Alibaba | 262K | $0.60 | $3.60 | Text |
| Grok 4.3 | xAI | 1M | $1.25 | ~$5.00 | Text |
| Gemini 3.5 Flash Lite | Google | 1M | $0.75 | $4.50 | Text, Image |

---

## Analysis & Impact

- **For software engineering / coding:** The SWE-bench Verified leaderboard is now effectively a two-tier market: Claude Mythos Preview (93.9%, restricted) defines the ceiling, while Claude Opus 4.7 (87.6%), GPT-5.5 (88.7%), and Kimi K2.6 (80.2%) define the accessible frontier. SWE-bench Pro (not Verified) remains the recommended signal for real-world agent quality per UC Berkeley's May 2026 benchmark hacking study; on that benchmark, the gap between Opus 4.7 (64.3%) and the next tier is 6+ points. For cost-sensitive coding CI pipelines, DeepSeek V4-Pro at $1.74/$3.48 posts 80.6% SWE-Bench Verified and is MIT-licensed — the strongest open-weight option by a significant margin.

- **For frontier reasoning / math / science:** GPQA Diamond has saturated the top tier (Gemini 3.1 Pro 94.3%, Opus 4.7 94.2%, GPT-5.5 93.6% — all within 0.7 points); the discrimination signal has shifted to HLE and AIME 2026. On HLE *without* tools, Claude Opus 4.7 (46.9%) leads. On HLE *with* tools, Kimi K2.6 (54.0%) leads all tested models — the best evidence that open-weight models can exceed proprietary ones when agentic tool use is included in evaluation. AIME 2026 has essentially saturated for the top closed-source tier (GPT-5.2, Claude Sonnet 4.5, Claude Opus 4.6 all at 100%), making Kimi K2.6's open-weight 96.4% the most relevant open-source math figure.

- **For multimodal / video / audio work:** Gemini 3.5 Flash leads the multimodal tier on MMMU-Pro (83.6%), CharXiv (84.2%), and Finance Agent v2 (57.9%) at $1.50/M input — better scores than GPT-5.5 or Claude Opus 4.7 on those specific benchmarks. Claude Opus 4.7's hi-res image upgrade (2,576px / 3.75MP) is a meaningful improvement for computer use and document workflows. Kimi K2.6's native video understanding via MoonViT (87.4% MathVision with tools) is the strongest open-weight multimodal vision result available. Gemini Omni (separate from 3.5 Flash, announced at I/O) handles text-to-cinematic-video but is not yet publicly available.

- **For cost-sensitive or open-source deployments:** DeepSeek V4-Flash ($0.14/$0.28 per 1M, MIT, 1M context, 13B active) is the new price/performance reference for teams that cannot afford frontier pricing. Kimi K2.6 ($0.95/$4.00, Modified MIT, 262K context, 1T/32B) leads open-weight models on most agentic benchmarks and is deployable via NVIDIA NIM, Hugging Face, or the Kimi API. Qwen3.6-27B (Apache 2.0, 77.2% SWE-bench Verified, single 8×H100 node) remains the most accessible self-hostable frontier-grade coding model. Mistral Medium 3.5 (Modified MIT, 128B dense, 256K context, 77.6% SWE-bench) closes the Sonnet-tier gap for teams that require EU-origin open weights.

- **The MCP Atlas benchmark is now table stakes:** Every major model release in May 2026 includes MCP Atlas scores in its official comparison table, signaling that multi-step Model Context Protocol workflow performance has become a required specification for enterprise AI procurement. Gemini 3.5 Flash's 83.6% MCP Atlas lead — above Claude Opus 4.7's 79.1% and GPT-5.5's 75.3% — is strategically significant as the industry standardizes on MCP as the agentic API layer.

---

## Key Takeaways (TL;DR)

- **Gemini 3.5 Flash** (released May 19) reaches 1B+ users as the new Gemini app default at $1.50/$9.00/1M, posting 76.2% Terminal-Bench 2.1 and 83.6% MCP Atlas — both ahead of Gemini 3.1 Pro and competitive with GPT-5.5.
- **GPT-5.5 Instant** (released May 5) replaced GPT-5.3 as ChatGPT's default with 52.5% fewer hallucinations; the `chat-latest` API alias changed on the same date, impacting production developer integrations silently.
- **Kimi K2.6** (released April 20-29) is the strongest open-weight agentic coding model available: 1T MoE / 32B active, 96.4% AIME 2026 (#1 open-weight), 54.0% HLE-with-tools (#1 all models), at $0.95/$4.00/1M under Modified MIT.
- **Claude Mythos Preview** holds the SWE-bench Verified record (93.9%) and SWE-bench Pro record (77.8%) as of May 21, 2026 — but remains restricted to approved users after autonomous zero-day vulnerability discovery.
- **GPQA Diamond has saturated** at the frontier tier (three models within 0.7% of each other); the benchmarks that now meaningfully differentiate frontier models are SWE-bench Pro, HLE-with-tools, and MCP Atlas.

---

*Sources:*
- [Google Blog: Gemini 3.5 launch](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
- [Google DeepMind: Gemini 3.5 Flash Model Card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)
- [CIO Dive: Google unveils Gemini agentic models](https://www.ciodive.com/news/google-unveils-Gemini-agentic-models/820783/)
- [Let's Data Science: Google delays Gemini 3.5 Pro](https://letsdatascience.com/news/google-delays-gemini-35-pro-releases-35-flash-at-io-0dcab6cd)
- [Appwrite: Gemini 3.5 Flash deep dive](https://appwrite.io/blog/post/gemini-3-5-flash-deep-dive)
- [Awesome Agents: Gemini 3.5 Flash](https://awesomeagents.ai/models/gemini-3-5-flash/)
- [Google AI Developer Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [WaveSpeed Blog: Gemini 3.5 Pro incoming](https://wavespeed.ai/blog/posts/gemini-3-5-pro-coming-next-month/)
- [OpenAI: Introducing GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/)
- [OpenAI: GPT-5.5 Instant System Card](https://openai.com/index/gpt-5-5-instant-system-card/)
- [OpenAI API Docs: GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5)
- [DataNorth: GPT-5.5 Instant](https://datanorth.ai/news/openai-releases-gpt-5-5-instant)
- [OpenAI: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [Anthropic: Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7?5=)
- [Anthropic Claude API Docs: Opus 4.7 What's New](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7)
- [Replicate: Kimi K2.6](https://replicate.com/moonshotai/kimi-k2.6)
- [NVIDIA NIM: Kimi K2.6](https://docs.api.nvidia.com/nim/reference/moonshotai-kimi-k2-6)
- [Miraflow: Kimi K2.6 Explained](https://miraflow.ai/blog/kimi-k2-6-explained-moonshot-ai-open-source-model-ties-gpt-5-5-coding)
- [Vercel AI Gateway: Kimi K2.6](https://vercel.com/ai-gateway/models/kimi-k2.6)
- [DeepSeek V4 Guide: Release Date](https://deepseekai.guide/news/deepseek-v4-release-date/)
- [DeepSeek V4 Model Review](https://deepseekai.guide/models/deepseek-v4/)
- [Handy AI: DeepSeek V4 Model Drop](https://handyai.substack.com/p/model-drop-deepseek-v4)
- [CoderSera: DeepSeek V4 Pro Review](https://ghost.codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/)
- [BenchLM: SWE-bench Verified Leaderboard](https://benchlm.ai/benchmarks/sweVerified)
- [BenchLM: SWE-bench Pro Leaderboard](https://benchlm.ai/benchmarks/swePro)
- [BenchLM: Coding Leaderboard](https://benchlm.ai/coding)
- [BenchLM: GPQA-D Leaderboard](https://benchlm.ai/benchmarks/gpqaDiamond)
- [BenchGecko: GPQA Diamond Leaderboard](https://benchgecko.ai/benchmark/gpqa-diamond)
- [Swfte: LMSys Arena May 2026](https://www.swfte.com/blog/lmsys-arena-leaderboard-may-2026)
- [SmartChunks: LMSys Arena April 2026](https://smartchunks.com/lmsys-arena-elo-leaderboard-explained-2026/)
- [LLM-Stats: AIME 2026 Leaderboard](https://llm-stats.com/benchmarks/aime-2026)
- [MadeByAgents: AIME 2026](https://www.madebyagents.com/benchmarks/aime-2026)
- [LLM-Stats: AI Updates May 2026](https://llm-stats.com/llm-updates)
- [Marc0.dev: SWE-bench Leaderboard May 2026](https://www.marc0.dev/en/leaderboard)
- [Awesome Agents: SWE-bench Coding Agent Leaderboard](https://awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/)
- [Mistral Medium 3.5 Review — Design for Online](https://designforonline.com/ai-models/mistral-mistral-medium-3-5/)
- [Mistral Medium 3.5 — Awesome Agents](https://awesomeagents.ai/models/mistral-medium-3-5/)
- [Mistral Medium 3.5 — ChatForest Review](https://chatforest.com/reviews/mistral-medium-3-5-dense-128b-agentic-llm-review/)
- [Nerd Level Tech: Mistral Medium 3.5](https://nerdleveltech.com/mistral-medium-3-5-open-weight-128b-frontier-coder)
- [Winbuzzer: Claude Mythos AISI Cyber Range](https://winbuzzer.com/2026/05/14/openais-gpt-55-matches-claude-mythos-in-security-tests-xcxwbn/)
- [Bind AI: Gemini 3.5 Flash vs GPT-5.5 Coding](https://blog.getbind.co/gemini-3-5-flash-vs-gpt-5-5-which-is-better-for-coding/)
- [Neowin: Gemini 3.5 Flash strongest coding model](https://www.neowin.net/news/google-announces-gemini-35-flash-its-strongest-coding-model-yet/)
