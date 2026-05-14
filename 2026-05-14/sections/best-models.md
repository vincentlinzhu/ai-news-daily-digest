# Best Models & Benchmarks — 2026-05-14

## Top Model News (5)

### 1. NVIDIA Nemotron 3 Nano Omni — First Open Omni Model Unifying Vision, Audio, and Language in a Single 30B MoE
**Source:** [NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) | [Technical Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/) | [ArXiv Paper](https://arxiv.org/html/2604.24954v2)

NVIDIA launched Nemotron 3 Nano Omni on April 28, 2026, the first open-weight model to natively unify video, audio, image, and text reasoning in a single MoE architecture. The 30B-A3B model uses a Mamba2-Transformer hybrid backbone combined with a C-RADIOv4-H vision encoder and Parakeet-TDT speech encoder. It tops six leaderboards including MMlongbench-Doc, OCRBenchV2, WorldSense, DailyOmni, and VoiceBench, while achieving 9× higher throughput than comparable open omni models at equivalent interactivity levels.

The architecture is distinctive: 2× temporal video token compression via Conv3D, dynamic image resolution, and native audio as a first-class input (up to 1-hour WAV/MP3 files). Context window stretches to 256K tokens with support for video up to 2 minutes at 1080p. The model supports NVFP4/FP8/BF16 quantization and runs across Ampere, Hopper, and Blackwell GPU architectures, making it deployable across the full NVIDIA fleet.

For enterprise agentic pipelines, Nemotron 3 Nano Omni is the most compelling open-weight option: it eliminates the need to chain separate vision, audio, and language models, reduces infrastructure complexity, and undercuts closed-model API costs substantially. NVIDIA's paper demonstrates it achieves frontier-class document intelligence and video understanding within a 3B active parameter budget per token—remarkable parameter efficiency.

**Key specs:** 256K tokens context | Text, Image, Video (2 min 1080p), Audio (1 hr) | Open-weight via NVIDIA NIM | Apache 2.0 / NVIDIA Open Model License | Available on NVIDIA API Catalog

---

### 2. ERNIE 5.1 — Baidu Cuts Pre-Training Cost 94% While Competing with Frontier Closed Models
**Source:** [ERNIE Blog](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) | [The Decoder](https://the-decoder.com/baidus-ernie-5-1-cuts-94-percent-of-pre-training-costs-while-competing-with-top-models/) | [LLMReference](https://www.llmreference.com/model/ernie-5.1)

Released May 9, 2026, ERNIE 5.1 is Baidu's most efficiently trained large model: compressed to roughly one-third the total parameters and one-half the active parameters of ERNIE 5.0, at just 6% of the pre-training compute cost of comparable frontier models. Despite this aggressive compression, it ranks 4th globally on the Arena Search leaderboard (score 1,223) and 1st among all Chinese models. On agentic benchmarks τ³-bench and SpreadsheetBench-Verified, it surpasses DeepSeek V4 Pro.

The training efficiency story is the headline. Achieving 94% pre-training cost reduction without catastrophic degradation on knowledge benchmarks (GPQA, MMLU-Pro scores approaching leading closed-source models) suggests Baidu has found significant training-time scaling improvements. The math performance is also notable: 99.6 on AIME26 with tool use, second only to Gemini 3.1 Pro on that benchmark.

For cost-sensitive enterprise applications—particularly in Chinese-language markets or regulated sectors requiring on-premises deployment—ERNIE 5.1 at $0.59/$2.65 per 1M tokens offers a compelling frontier-adjacent option. Its agentic improvements specifically target enterprise workflow automation at a price point that is roughly 4–12× cheaper than Claude Opus 4.7 or GPT-5.5.

**Key specs:** 128K context | Text | $0.59 input / $2.65 output per 1M tokens | Proprietary | Baidu Qianfan API

---

### 3. Grok 4.3 API — xAI Opens Multimodal Access with 83% Price Cut and Native Video Input
**Source:** [Artificial Analysis](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing) | [Awesome Agents](https://awesomeagents.ai/news/xai-grok-4-3-api-launch/) | [xAI Docs](https://docs.x.ai/developers/models)

xAI launched the Grok 4.3 API publicly on May 5–6, 2026 (beta opened April 30 for SuperGrok Heavy subscribers at $300/month), representing a major pricing restructure: input prices cut ~40% and output prices cut ~60% compared to Grok 4.20. The model adds native video input up to 5 minutes at 1080p and native document output (PDF, XLSX, PPTX), making it the first major frontier model to offer native structured document generation. The 1M-token context window opens Grok 4.3 to long-context retrieval use cases that were previously Gemini or Claude territory.

On benchmarks, Grok 4.3 scores 53 on the Artificial Analysis Intelligence Index, ahead of Claude Sonnet 4.6 but trailing the top-tier frontier cluster. Its standout performance is vertical-specific: #1 on Vals Case Law and Corporate Finance benchmarks, 98% on τ²-Bench Telecom (agentic customer support), and 81% on IFBench (instruction following). On GDPval-AA, it gained 321 Elo points over Grok 4.20 to reach 1500—a significant practical capability jump for knowledge work tasks.

The pricing repositioning is strategically significant. At $1.25 input / $2.50 output per 1M tokens, Grok 4.3 undercuts Claude Opus 4.7 ($5/$25) and GPT-5.5 ($5/$30) by roughly 4× on output cost, while remaining well above DeepSeek V4 Pro. For agentic legal, finance, and telecom applications, xAI is clearly targeting enterprise verticals with proven domain performance at a palatable price point.

**Key specs:** 1M token context | Text, Image, Video (5 min 1080p) | $1.25 input / $2.50 output per 1M tokens | Proprietary | xAI API (generally available)

---

### 4. DeepSeek V4 Pro — Open-Weight 1.6T MoE Reaches 80.6% SWE-bench at $1.74/$3.48 per 1M Tokens
**Source:** [Fortune](https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/) | [MorphLLM](https://www.morphllm.com/deepseek-v4) | [Codersera](https://codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/)

DeepSeek V4 Pro launched April 24, 2026, as an MIT-licensed open-weight model with 1.6T total parameters and 49B active per token—operating at just 27% of V3.2's inference FLOPs and 10% of its KV cache requirements at 1M context. The efficiency gains come from two novel attention mechanisms: Compressed Sparse Attention (CSA) with 4× KV compression and Manifold-Constrained Hyper-Connections (mHC) for trillion-parameter stable training. At 80.6% SWE-bench Verified and 93.5 on LiveCodeBench, V4-Pro matches Claude Opus 4.6 on coding and sits within 0.2 points of the frontier closed-model coding cluster.

The open-weight release under MIT license means V4 Pro can be fine-tuned, distilled, or self-hosted. At 32–33 trillion training tokens and Huawei chip co-optimization, it also underscores the continued advancement of Chinese AI labs independent of US export controls. The companion V4-Flash variant (284B total, 13B active) at $0.14/$0.28 per 1M tokens is arguably the most capable sub-$0.30 model ever released, targeting cost-sensitive high-volume inference.

The frontier between open-weight and closed models has effectively collapsed at the coding tier. DeepSeek V4-Pro-Max achieves 80.6% SWE-bench Verified—within the same cluster as Gemini 3.1 Pro (80.6%), MiniMax M2.5 (80.2%), and Mistral Medium 3.5 (77.6%). Only Claude Opus 4.7 (87.6%), GPT-5.5 (88.7%), and gated Claude Mythos Preview (93.9%) maintain meaningful leads at the very top.

**Key specs:** 1M token context | Text, Code | $1.74 input / $3.48 output per 1M tokens (V4-Pro); $0.14/$0.28 (V4-Flash) | MIT license | DeepSeek API + Hugging Face (865 GB download)

---

### 5. Gemini AI Cursor — DeepMind Reimagines Pointer Interaction with Semantic Mouse Understanding
**Source:** [Google DeepMind Blog](https://deepmind.google/blog/ai-pointer/) | [9to5Google](https://9to5google.com/2026/05/12/deepmind-googlebook-magic-pointer/) | [The Register](https://www.theregister.com/software/2026/05/13/googles-ai-enabled-mouse-pointer-understands-this-and-that/5240005)

Announced May 12–13, 2026, Google DeepMind's AI-enabled pointer is the first fundamental redesign of the computer cursor in over 50 years. Powered by Gemini, the system captures visual and semantic context around the cursor position in real time, enabling users to point at UI elements and speak using natural pronouns—"fix this," "move that here"—without writing prompts. The pointer integrates with the computer's microphone and pairs with Gemini's multimodal understanding to determine not just what the cursor is over, but why it matters in context.

Practical demos released in Google AI Studio cover two capabilities: contextual image editing (point at an element, speak an instruction) and location-aware search (hover over a map feature, identify it). The "Magic Pointer" is rolling out in Chrome and will be a flagship feature on Googlebook, Google's new line of Gemini-powered laptops launching fall 2026. This positions Google to own the interaction paradigm for AI-native computing before competitors can respond.

The strategic significance extends beyond a cursor feature. This is Google's answer to the "ambient computing" challenge: if models become powerful enough to understand any UI element semantically, the OS becomes a prompt interface. Combined with Gemini 3.1 Pro's 2M context window and native video/audio modalities, Google is assembling a complete stack—from inference to interaction—that no other lab currently matches end-to-end.

**Key specs:** Deployed via Chrome extension + Googlebook hardware integration | Vision + audio multimodal | No standalone API pricing; part of Gemini Enterprise | Preview available in Google AI Studio

---

## Deep Dive: Most Important Release — GPT-5.5 (April 23, 2026) + GPT-5.5 Instant Default (May 5, 2026)

GPT-5.5 represents the most significant single-model capability leap of the current frontier cycle: it is the first publicly available model to exceed human-average performance on ARC-AGI-2 (85% vs. human average of 66%), leads SWE-bench Verified at 88.7%, tops Terminal-Bench 2.0 at 82.7%, and became the default model for all ChatGPT tiers on May 5, 2026—reaching hundreds of millions of users instantly. No prior model has simultaneously led ARC-AGI-2, a concrete agentic benchmark (Terminal-Bench), a software engineering benchmark (SWE-bench), and a web research benchmark (BrowseComp 84.4%) at the same time.

### What It Can Do

GPT-5.5 is OpenAI's first fully retrained base model since GPT-4.5, with new pretraining and reasoning behavior rather than post-training refinements on an older checkpoint. It excels at multi-step agentic coding tasks in terminal environments, complex reasoning chains requiring extended thinking, and high-accuracy factual recall—with 52.5% fewer hallucinated claims on high-stakes queries (medicine, law, finance) compared to GPT-5.3 Instant. The GPT-5.5 Instant variant adds auto-routing: when users ask complex questions in ChatGPT, the system automatically escalates to GPT-5.5 Thinking mode. Vision capabilities include improved image analysis and STEM diagram interpretation. On OSWorld-Verified it achieves 78.7%, demonstrating genuine computer-use capability across GUIs.

### Benchmark Highlights

| Benchmark | GPT-5.5 | Previous Best |
|---|---|---|
| SWE-bench Verified | 88.7% | Claude Opus 4.7: 87.6% |
| ARC-AGI-2 | 85.0% | GPT-5.4 Pro: 83.3% |
| Terminal-Bench 2.0 | 82.7% | GPT-5.4: 75.1% |
| BrowseComp | 84.4% | Claude Opus 4.6: 84.0% |
| OSWorld-Verified | 78.7% | Prior SOTA: ~72% |
| FrontierMath Tier 4 | 35.4% | Prior best: ~30% |
| GPQA Diamond | 93.6% | GPT-5.4: 92.8% |
| Artificial Analysis Intelligence Index | 60.2 (xhigh) | Claude Opus 4.7: 57.3 |
| CyberGym | 81.8% | Prior best: ~75% |
| FrontierMath Tier 1–3 | 51.7% | GPT-5.4: ~45% |

### Architecture (known)
OpenAI has described GPT-5.5 as a "fully retrained base model" with new pretraining data and novel reasoning behavior—distinct from GPT-5.4 which was a post-training refinement. No architectural specifics (MoE vs. dense, parameter count, training token count) have been disclosed publicly. The reasoning capabilities suggest extended chain-of-thought at inference time, consistent with OpenAI's o-series lineage integrated into the base model. The Instant variant uses a smaller/faster checkpoint of the same base optimized for latency.

### Pricing & Availability
- **GPT-5.5 (full):** $5.00 input / $30.00 output per 1M tokens; cached input $0.50/1M
- **GPT-5.5 Pro (highest accuracy tier):** $30.00 input / $180.00 output per 1M tokens
- **GPT-5.5 Instant (ChatGPT default):** Same API pricing as full GPT-5.5 ($5/$30)
- Context window: 1M tokens; max output: 128K tokens
- Knowledge cutoff: December 2025
- ChatGPT usage limits: Free (10 messages/5 hrs), Plus/Go (160 messages/3 hrs), Pro/Business (unlimited)
- Available via OpenAI API, ChatGPT (all tiers), Azure OpenAI Service

### Strategic Significance

GPT-5.5 crossing 85% on ARC-AGI-2 is not merely a benchmark headline—it marks the first public model exceeding the human baseline on a test that François Chollet designed specifically to resist pattern memorization. This is a meaningful signal that fluid reasoning (adapting to genuinely novel problem structures) has improved beyond what scaling alone was achieving. Combined with 88.7% SWE-bench Verified—resolving real GitHub issues—the gap between AI and senior software engineers on concrete tasks is now narrow enough that the question is no longer "if" but "when and in which workflow."

The ChatGPT default rollout amplifies the impact: GPT-5.5 Instant's 52.5% reduction in hallucinations on high-stakes queries (medicine, law, finance) matters enormously for the 300M+ active ChatGPT users who are not AI researchers tracking benchmarks. This is reliability at mass scale. The auto-switching behavior—where Instant escalates to Thinking mode for complex queries—is also notable as a UX design that hides model complexity from users while maximizing answer quality.

OpenAI's decision to fold GPT-5.5 Instant into the default ChatGPT free tier (with limits) signals aggressive consumer market defense against Gemini's 2M context and Claude's domain leadership. The $5/$30 API pricing holds the premium tier stable while GPT-5.5 Pro at $30/$180 creates a high-margin enterprise ceiling—a tiered strategy that mirrors cloud compute pricing architectures.

### Competitive Context

GPT-5.5 leads on ARC-AGI-2 (85.0% vs. Gemini 3.1 Pro's 77.1% and Claude Opus 4.7 Adaptive's 75.8%), Terminal-Bench 2.0 (82.7% vs. Gemini 3.1 Pro's 68.5% and Claude Opus 4.6's 65.4%), and the Artificial Analysis Intelligence Index (60.2 vs. Claude Opus 4.7's 57.3 and Gemini 3.1 Pro's 57.2). Anthropic's gated Claude Mythos Preview leads on SWE-bench Pro (77.8% vs. GPT-5.5's 58.6%) and HLE, suggesting Anthropic maintains capability leads on proprietary evaluation sets. On GDPval-AA knowledge work, Claude Opus 4.7 leads at 1,753 Elo vs. GPT-5.5's position in a lower cluster—indicating Anthropic holds an edge on economically productive knowledge tasks even as OpenAI dominates abstract reasoning benchmarks.

---

## Benchmark Comparison Data

```json
{"benchmark": "Artificial Analysis Intelligence Index", "results": [{"model": "GPT-5.5 (xhigh)", "score": 60.2}, {"model": "GPT-5.5 (high)", "score": 58.9}, {"model": "Claude Opus 4.7 (Adaptive, Max Effort)", "score": 57.3}, {"model": "Gemini 3.1 Pro Preview", "score": 57.2}, {"model": "GPT-5.5 (medium)", "score": 56.7}, {"model": "Grok 4.3", "score": 53.0}]}
```

```json
{"benchmark": "SWE-bench Verified", "results": [{"model": "Claude Mythos Preview (gated)", "score": 93.9}, {"model": "GPT-5.5", "score": 88.7}, {"model": "Claude Opus 4.7", "score": 87.6}, {"model": "GPT-5.3 Codex", "score": 85.0}, {"model": "Claude Opus 4.5", "score": 80.9}, {"model": "Claude Opus 4.6", "score": 80.8}, {"model": "DeepSeek V4 Pro Max", "score": 80.6}, {"model": "Gemini 3.1 Pro", "score": 80.6}, {"model": "MiniMax M2.5", "score": 80.2}, {"model": "Mistral Medium 3.5", "score": 77.6}]}
```

```json
{"benchmark": "ARC-AGI-2", "results": [{"model": "GPT-5.5", "score": 85.0}, {"model": "GPT-5.4 Pro", "score": 83.3}, {"model": "Gemini 3.1 Pro", "score": 77.1}, {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8}, {"model": "Grok 4", "score": 53.3}, {"model": "Human Average", "score": 66.0}]}
```

```json
{"benchmark": "Terminal-Bench 2.0", "results": [{"model": "GPT-5.5", "score": 82.7}, {"model": "Gemini 3.1 Pro", "score": 68.5}, {"model": "Claude Opus 4.6", "score": 65.4}, {"model": "GPT-5.4", "score": 75.1}]}
```

```json
{"benchmark": "GPQA Diamond", "results": [{"model": "Gemini 3.1 Pro", "score": 94.3}, {"model": "GPT-5.5", "score": 93.6}, {"model": "DeepSeek V4 Pro", "score": 90.1}, {"model": "GPT-5.4", "score": 92.8}]}
```

```json
{"benchmark": "AIME 2026", "results": [{"model": "Kimi K2.6", "score": 96.4}, {"model": "GLM-5 / Kimi K2.5", "score": 95.8}, {"model": "GLM-5.1 / Qwen3.6 Plus", "score": 95.3}, {"model": "ERNIE 5.1 (with tool use)", "score": 99.6}, {"model": "GPT-5.2", "score": 100}, {"model": "Claude Sonnet 4.5", "score": 100}, {"model": "Claude Opus 4.6", "score": 100}]}
```

```json
{"benchmark": "LMSys Chatbot Arena Overall ELO (Apr 2026 snapshot)", "results": [{"model": "Claude Opus 4.6 Thinking", "score": 1504}, {"model": "Gemini 3.1 Pro Preview", "score": 1493}, {"model": "GPT-5.4 High", "score": 1484}, {"model": "Grok 4.20", "score": 1471}, {"model": "DeepSeek V4 Pro", "score": 1462}, {"model": "Claude Sonnet 4.6", "score": 1458}, {"model": "GPT-5.4 Standard", "score": 1455}, {"model": "Gemini 3.0 Pro", "score": 1449}, {"model": "Qwen 3.6-Plus", "score": 1447}, {"model": "Meta Muse Spark", "score": 1441}]}
```

```json
{"benchmark": "GDPval-AA Knowledge Work ELO", "results": [{"model": "Claude Opus 4.7", "score": 1753}, {"model": "GPT-5.4", "score": 1674}, {"model": "Grok 4.3", "score": 1500}, {"model": "Gemini 3.1 Pro", "score": 1314}, {"model": "Claude Opus 4.6", "score": 1606}]}
```

```json
{"benchmark": "BrowseComp", "results": [{"model": "GPT-5.5", "score": 84.4}, {"model": "Claude Opus 4.6", "score": 84.0}]}
```

```json
{"benchmark": "Arena Search Leaderboard ELO", "results": [{"model": "ERNIE 5.1 (Baidu)", "score": 1223, "rank_global": 4, "rank_chinese": 1}]}
```

```json
{"benchmark": "LiveCodeBench", "results": [{"model": "DeepSeek V4 Pro Max", "score": 93.5}]}
```

```json
{"benchmark": "Humanity's Last Exam (with tools)", "results": [{"model": "Claude Opus 4.6", "score": 53.1}, {"model": "Gemini 3.1 Pro", "score": 51.4}]}
```

```json
{"benchmark": "Long-Context Retrieval MRCR v2 @1M tokens", "results": [{"model": "Claude Opus 4.6", "score": 76.0}, {"model": "Gemini 3.0 Pro", "score": 26.3}]}
```

---

## Pricing / Context / Specs Table

| Model | Provider | Context Window | Input $/1M | Output $/1M | Modalities |
|---|---|---|---|---|---|
| GPT-5.5 | OpenAI | 1M tokens | $5.00 | $30.00 | Text, Image |
| GPT-5.5 Pro | OpenAI | 1M tokens | $30.00 | $180.00 | Text, Image |
| Claude Opus 4.7 | Anthropic | 1M tokens (beta) | $5.00 | $25.00 | Text, Image (up to 3.75MP) |
| Gemini 3.1 Pro | Google | 2M tokens | $2.00 | $12.00 | Text, Image, Audio, Video, Code |
| Grok 4.3 | xAI | 1M tokens | $1.25 | $2.50 | Text, Image, Video (5 min) |
| DeepSeek V4 Pro | DeepSeek | 1M tokens | $1.74 | $3.48 | Text, Code |
| DeepSeek V4 Flash | DeepSeek | 1M tokens | $0.14 | $0.28 | Text, Code |
| ERNIE 5.1 | Baidu | 128K tokens | $0.59 | $2.65 | Text |
| Claude Sonnet 4.6 | Anthropic | 200K tokens | $3.00 | $15.00 | Text, Image |
| Mistral Medium 3.5 | Mistral | 128K tokens | ~$2.00 | ~$6.00 | Text, Code |
| Nemotron 3 Nano Omni | NVIDIA | 256K tokens | Open-weight | Open-weight | Text, Image, Audio, Video |
| Qwen 3.5-Plus (397B-A17B) | Alibaba | 128K+ tokens | Open-weight | Open-weight | Text, Image, Video |
| GPT-5.5 Instant (ChatGPT) | OpenAI | 1M tokens | $5.00 | $30.00 | Text, Image |
| Gemini 2.5 Flash | Google | 1M tokens | $0.30 | $2.50 | Text, Image, Audio, Video |

---

## Analysis & Impact

- **For software engineering / coding:** GPT-5.5 now leads public SWE-bench at 88.7%, with Claude Opus 4.7 at 87.6% and the open-weight tier (DeepSeek V4 Pro, Gemini 3.1 Pro, Mistral Medium 3.5) all clustering around 77–80.6%. For teams self-hosting, DeepSeek V4 Pro-Max under MIT license at $1.74/$3.48 delivers ~91% of frontier coding capability at roughly 12× lower API cost than Claude Opus 4.7—making the open-weight vs. closed-API decision primarily an ops and compliance question rather than a capability one.

- **For frontier reasoning / math / science:** ARC-AGI-2 has become the definitive reasoning separator: GPT-5.5 at 85% is now above human average (66%) for the first time ever, with Gemini 3.1 Pro (77.1%) and Claude Opus 4.7 (75.8%) close behind. On AIME 2026, the top cluster (multiple models at 95–100%) means math olympiad problems are effectively saturated—the community should expect FrontierMath Tier 4 (GPT-5.5 at 35.4%) to become the new differentiating reasoning benchmark.

- **For multimodal / video / audio work:** Gemini 3.1 Pro's 2M context window with native video/audio processing remains the strongest production-grade closed option; its long-context retrieval is dramatically ahead of other models (Gemini 3 Pro at 26.3% vs. Claude's 76% on MRCR v2, reversing across model generations). NVIDIA Nemotron 3 Nano Omni is the open-weight answer: a single 30B-A3B model handling video, audio, image, and text at 9× higher throughput than competitors. The Gemini AI Cursor adds a novel interaction paradigm—semantic pointer understanding—that reframes how multimodal AI integrates into OS-level workflows.

- **For cost-sensitive or open-source deployments:** The open-weight frontier has never been stronger. DeepSeek V4-Flash at $0.14/$0.28 per 1M tokens is the cheapest high-capability option. Nemotron 3 Nano Omni provides omni-modal inference at open-weight cost. ERNIE 5.1 at $0.59/$2.65 offers near-frontier Chinese-language performance at a fraction of closed-model prices. Qwen 3.5-Plus (397B-A17B, Apache 2.0) moves open-source to "best-in-class on graduate-level reasoning" per independent evaluations. The cost spread from frontier closed to frontier open is now 10–207× depending on the tier.

- **Extended thinking / test-time compute is now table stakes:** GPT-5.5's auto-escalation from Instant to Thinking mode in ChatGPT, Gemini 3.1 Pro's extended reasoning, and Claude Opus 4.7 Adaptive's flexible compute budget all demonstrate that variable-depth reasoning at inference time is no longer a premium feature—it is expected infrastructure. Models not offering some form of adaptive reasoning are effectively a generation behind the frontier.

---

## Key Takeaways (TL;DR)

- GPT-5.5 becomes the first public model to exceed human average on ARC-AGI-2 at 85%, while simultaneously leading SWE-bench Verified at 88.7% and Terminal-Bench 2.0 at 82.7%.
- NVIDIA Nemotron 3 Nano Omni (30B-A3B, open-weight) is the first open model to natively unify video, audio, image, and text in a single efficient architecture, achieving 9× higher throughput than comparable open omni models.
- ERNIE 5.1 achieves frontier-competitive performance at just 6% of the pre-training compute cost of comparable models and $0.59/$2.65 per 1M tokens—the most efficient frontier training result disclosed publicly.
- DeepSeek V4 Pro (1.6T MoE, MIT license) matches Claude Opus 4.6 on SWE-bench and LiveCodeBench at $1.74/$3.48 per 1M tokens, narrowing the open-vs-closed capability gap to near-zero at the coding tier.
- Gemini 3.1 Pro's 2M token context + Gemini AI Cursor (semantic mouse pointer, May 12) signal Google's strategy to own the full AI-native computing stack from inference to OS interaction.

---

*Sources:*
- https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/
- https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/
- https://arxiv.org/html/2604.24954v2
- https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/
- https://the-decoder.com/baidus-ernie-5-1-cuts-94-percent-of-pre-training-costs-while-competing-with-top-models/
- https://www.llmreference.com/model/ernie-5.1
- https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing
- https://awesomeagents.ai/news/xai-grok-4-3-api-launch/
- https://docs.x.ai/developers/models
- https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/
- https://www.morphllm.com/deepseek-v4
- https://codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/
- https://deepmind.google/blog/ai-pointer/
- https://9to5google.com/2026/05/12/deepmind-googlebook-magic-pointer/
- https://www.theregister.com/software/2026/05/13/googles-ai-enabled-mouse-pointer-understands-this-and-that/5240005
- https://openai.com/index/introducing-gpt-5-5/
- https://openai.com/index/gpt-5-5-instant/
- https://www.anthropic.com/news/claude-opus-4-7
- https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm
- https://deepmind.google/technologies/gemini/pro/
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/
- https://www.swfte.com/blog/lmsys-arena-leaderboard-may-2026
- https://benchlm.ai/benchmarks/sweVerified
- https://benchlm.ai/benchmarks/arcAgi2
- https://benchlm.ai/benchmarks/aime2026
- https://artificialanalysis.ai/leaderboards/models
- https://pricepertoken.com/
- https://www.digitalapplied.com/blog/ai-model-api-pricing-tracker-q2-2026-data-points
- https://devtk.ai/en/models/gemini-3-1-pro/
- https://www.alibabagroup.com/document-1960233590314762240
- https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/
