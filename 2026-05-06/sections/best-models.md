# Best Models — AI News Digest
**Date: 2026-05-06**

---

## Top Stories

### 1. Claude Mythos Preview: Anthropic's "Too Dangerous to Release" Flagship

Announced April 7, 2026, Claude Mythos Preview is Anthropic's most capable model to date — and the first major frontier model in recent memory that the developer has explicitly refused to release publicly. The model sits above the Opus tier and represents a new capability class, particularly in cybersecurity.

**Why it's locked down:** Mythos autonomously discovered thousands of previously unknown zero-day vulnerabilities across every major OS and web browser, including a 27-year-old flaw in OpenBSD and a 16-year-old FFmpeg bug that survived 5 million automated test runs. Anthropic determined this dual-use threat was incompatible with general availability.

**Access via Project Glasswing:** Instead of a public launch, Anthropic deployed Mythos through Project Glasswing — a defensive cybersecurity initiative with 12 named launch partners (AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks) and 40+ additional vetted critical-infrastructure organizations. Anthropic committed up to $100M in usage credits and $4M in donations to open-source security organizations.

**Key benchmarks:**
- SWE-bench Verified: **93.9%** (vs. Opus 4.6's 80.8% — a 13-point jump)
- SWE-bench Pro: **77.8%** (vs. Opus 4.7's 64.3%)
- CyberGym: **83.1%** (vs. Opus 4.6's 66.6%)
- Terminal-Bench 2.0: **82.0%**
- USAMO 2026: **97.6%** (55-point jump over Opus 4.6)
- Humanity's Last Exam: **64.7%**

**Pricing (Project Glasswing only):** $25 input / $125 output per million tokens.

> **Impact:** Sets a precedent for restricted-release frontier models driven by safety assessment rather than commercial readiness. The 93.9% SWE-bench Verified score makes it the clear #1 coding model — but unavailable to most developers.

---

### 2. GPT-5.5: OpenAI's First Full Retraining Since GPT-4.5

Released April 23, 2026, GPT-5.5 is OpenAI's first fully retrained base model since GPT-4.5 — not a fine-tune or variant of GPT-5.4. It targets agentic coding, computer use, and scientific research workflows.

**Specs:**
- Context window: **1,050,000 input / 128,000 output tokens** (API)
- Codex context: 400,000 tokens
- Pricing: **$5.00 input / $30.00 output** per million tokens (2× GPT-5.4)
- Cached input: $0.50/M tokens
- Note: Prompts >272K tokens incur 2× input / 1.5× output surcharge for the full session

**Key benchmarks:**
- Terminal-Bench 2.0: **82.7%** (vs. GPT-5.4's 75.1%)
- GDPval: **84.9%**
- OSWorld-Verified: **78.7%**
- ARC-AGI-2: **85%** (co-leading with Gemini 3.1 Deep Think)
- FrontierMath Tier 1–3: **51.7%** / Tier 4: **35.4%**
- CyberGym: **81.8%**
- GPQA Diamond: **93.6%**
- Artificial Analysis Intelligence Index: **60.2** (xhigh compute tier, #1 overall)

**Availability:** ChatGPT Plus/Pro/Business/Enterprise and Codex, API access rolling out post additional safety review.

> **Impact:** At $30/M output tokens, GPT-5.5 is expensive relative to Claude Opus 4.7 ($25/M). But its ARC-AGI-2 score and agentic computer-use numbers make it the best choice for OSWorld-style workflows. The 2× price premium vs. GPT-5.4 will filter deployment to high-value workflows.

---

### 3. Claude Opus 4.7: Best Generally-Available Model for Software Engineering

Released April 16, 2026, Claude Opus 4.7 is the current best publicly accessible model for software engineering tasks. It introduces an "xhigh" adaptive reasoning effort level and self-verification (the model tests its own outputs before reporting).

**Specs:**
- Pricing: **$5 input / $25 output** per million tokens (unchanged from Opus 4.6)
- Up to 90% cost savings with prompt caching; 50% with batch processing
- Vision: 3.3× higher resolution (up to 2,576px longest edge)
- Multi-session file-system memory for long-running agents

**Key benchmarks:**
- SWE-bench Verified: **87.6%** (up from Opus 4.6's 80.8%)
- SWE-bench Pro: **64.3%** (Anthropic #1 publicly available)
- GPQA Diamond: **94.2%**
- Terminal-Bench 2.0: **69.4%**
- Finance Agent (Vals AI): **64.4%** (state-of-the-art)
- ARC-AGI-2: **75.8%**
- Humanity's Last Exam: **54.7%**

**Availability:** Claude Pro/Max/Team/Enterprise, Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry.

> **Impact:** At the same price as Opus 4.6 but with a 7-point SWE-bench Verified improvement and new xhigh reasoning mode, Opus 4.7 offers a free capability upgrade for existing Anthropic API users. It's the best cost-performance trade-off for coding agents that don't have Mythos access.

---

### 4. DeepSeek V4 Pro: Open-Weights Frontier with 1M Context at Fraction of Cost

Released April 24, 2026, DeepSeek V4 Pro is a 1.6T parameter MoE model (49B active) with open-source weights (MIT license) and the most aggressive pricing of any frontier-quality model.

**Specs:**
- Architecture: MoE, 1.6T total / 49B active parameters
- Context: **1 million tokens**, max output 384K tokens
- Pricing: **$0.435 input / $0.87 output** per million tokens (API)
- Cache hit: $0.0036/M tokens
- License: MIT (open weights on Hugging Face)
- Inference efficiency: Uses only 27% of V3.2's FLOPs and 10% of KV cache at 1M-token context

**Key benchmarks:**
- Codeforces rating: **3,206** (vs. GPT-5.4's 3,168, Gemini 3.1's 3,052)
- LiveCodeBench: **93.5** (vs. Claude Opus 4.6's 88.8)
- IMOAnswerBench: **89.8**
- Putnam-2025 proof: **120/120** (perfect)
- MRCR 1M (long-context retrieval): 83.5 (trails Claude's 92.9)

**Comparison to Kimi K2.6 (also April 2026, 1T params, 256K context):**
- Kimi K2.6 leads on SWE-bench Pro (58.6 vs ~45), AIME, and most coding/reasoning benchmarks
- DeepSeek V4 Pro leads on long-context tasks and AI agent information search
- Kimi K2.6 pricing: $0.95 input/output; DeepSeek V4 Pro: $0.435/$0.87 — DeepSeek wins on price

> **Impact:** DeepSeek V4 Pro's MIT license + 1M context + sub-$1/M pricing creates a new "open frontier" tier. For latency-insensitive workloads that need long context and cost efficiency, it undercuts proprietary alternatives by 30–70×.

---

### 5. Qwen3.6-35B-A3B: Best Open-Weights Model for Local Deployment

Released April 16, 2026, Qwen3.6-35B-A3B is Alibaba's latest sparse MoE coder model — 35B total parameters with only 3B active per token, Apache 2.0 license, available immediately on Hugging Face with no waitlist.

**Architecture:** 256-expert MoE, 3B active parameters per forward pass, native 262K token context extensible to 1,010,000 tokens.

**Hardware requirement:** ~22GB VRAM at 4-bit quantization — fits on a single RTX 4090 or Mac with 24GB unified memory.

**Key benchmarks:**
- SWE-bench Verified: **73.4%**
- Terminal-Bench 2.0: **51.5%**
- AIME 2026: **92.7%**

**Context:** Accompanies Qwen3.6-27B (dense, released May 2026), which reportedly surpasses Qwen3.5-397B-A17B on all major coding benchmarks despite being a fraction of the size.

> **Impact:** 73.4% SWE-bench at 22GB VRAM is a significant threshold — it makes capable agentic coding accessible to a single prosumer GPU. The 3B-active-parameter MoE design also means inference cost is roughly that of a 3B dense model.

---

## Deep Dive: The New Benchmark Landscape — What Actually Differentiates Models in 2026

With SWE-bench Verified now widely considered saturated (see prior digest on contamination), the industry has shifted to three tiers of evaluation:

### Tier 1: General Capability (Intelligence Index)
The Artificial Analysis Intelligence Index v4.0 aggregates 10 evaluations weighted across agents, coding, general reasoning, and science. Current top scores:

| Model | AA Intelligence Index | Compute Tier |
|---|---|---|
| GPT-5.5 | 60.2 | xhigh |
| GPT-5.5 | 58.9 | high |
| Claude Opus 4.7 | 57.3 | xhigh (Adaptive) |
| Gemini 3.1 Pro Preview | 57.2 | — |
| GPT-5.4 | 56.8 | xhigh |

### Tier 2: Reasoning Stress Tests
These benchmarks remain unsaturated and strongly correlate with real-world task performance:

| Benchmark | Description | Top Score | Model |
|---|---|---|---|
| ARC-AGI-2 | Novel abstract reasoning / fluid intelligence | 85% | GPT-5.5 / Gemini 3.1 Deep Think |
| Humanity's Last Exam | 2,500 expert-vetted cross-domain questions | 64.7% | Claude Mythos Preview |
| GPQA Diamond | Expert-level physics/chem/bio (PhD baseline: 65–81%) | 94.3% | Gemini 3.1 Pro |
| AIME 2025 | Competition math, 30 problems | 100% | GPT-5.2 Pro |
| FrontierMath Tier 4 | Research-level math | 35.4% | GPT-5.5 |

### Tier 3: Agentic / Coding (Most Practically Relevant)
| Benchmark | Description | Top Score | Model |
|---|---|---|---|
| SWE-bench Pro | Real GitHub issues, frontier difficulty | 77.8% | Claude Mythos Preview |
| SWE-bench Verified | 500 human-verified GitHub issues | 93.9% | Claude Mythos Preview |
| Terminal-Bench 2.0 | 89 hard agentic terminal tasks (Codex CLI) | 82.7% | GPT-5.5 |
| OSWorld-Verified | Computer use, GUI automation | 78.7% | GPT-5.5 |
| GDPval | Generalist deployment planning | 84.9% | GPT-5.5 |
| CyberGym | Vulnerability discovery and exploitation | 83.1% | Claude Mythos Preview |
| Codeforces Rating | Competitive programming (live contests) | 3,206 | DeepSeek V4 Pro |

**Key observation:** No single model leads across all three tiers. GPT-5.5 leads agentic/computer-use tasks; Claude Mythos leads coding and cybersecurity (but is unavailable); Gemini 3.1 Pro leads scientific reasoning at competitive pricing; DeepSeek V4 Pro leads open-weights cost efficiency at frontier quality.

---

## Benchmark / Data JSON

```json
{
  "date": "2026-05-06",
  "swe_bench_verified": [
    {"model": "Claude Mythos Preview", "score": 93.9, "available": false},
    {"model": "Claude Opus 4.7 (Adaptive)", "score": 87.6, "available": true},
    {"model": "GPT-5.3 Codex", "score": 85.0, "available": true},
    {"model": "Qwen3.6-27B", "score": 73.4, "available": true, "open_weights": true}
  ],
  "swe_bench_pro": [
    {"model": "Claude Mythos Preview", "score": 77.8, "available": false},
    {"model": "Claude Opus 4.7 (Adaptive)", "score": 64.3, "available": true},
    {"model": "GPT-5.5", "score": 58.6, "available": true},
    {"model": "Kimi K2.6", "score": 58.6, "available": true, "open_weights": true},
    {"model": "GPT-5.3 Codex", "score": 56.8, "available": true}
  ],
  "terminal_bench_2": [
    {"model": "GPT-5.5 (Codex CLI)", "score": 82.7, "available": true},
    {"model": "Claude Mythos Preview", "score": 82.0, "available": false},
    {"model": "GPT-5.4 (ForgeCode)", "score": 81.8, "available": true},
    {"model": "Gemini 3.1 Pro (TongAgents)", "score": 80.2, "available": true},
    {"model": "Qwen3.6-35B-A3B", "score": 51.5, "available": true, "open_weights": true}
  ],
  "gpqa_diamond": [
    {"model": "Gemini 3.1 Pro", "score": 94.3},
    {"model": "Claude Opus 4.7 (Adaptive)", "score": 94.2},
    {"model": "GPT-5.5", "score": 93.6},
    {"model": "GPT-5.2 Pro", "score": 93.2}
  ],
  "arc_agi_2": [
    {"model": "GPT-5.5", "score": 85.0},
    {"model": "Gemini 3.1 Deep Think", "score": 85.0},
    {"model": "GPT-5.4 Pro", "score": 83.3},
    {"model": "Gemini 3.1 Pro", "score": 77.1},
    {"model": "Claude Opus 4.7 (Adaptive)", "score": 75.8}
  ],
  "humanity_last_exam": [
    {"model": "Claude Mythos Preview", "score": 64.7},
    {"model": "GPT-5.4 Pro", "score": 58.7},
    {"model": "Claude Opus 4.7", "score": 54.7},
    {"model": "GPT-5.5 Pro", "score": 57.2},
    {"model": "Gemini 3.1 Pro Preview", "score": 44.7}
  ],
  "pricing_per_million_tokens": [
    {"model": "GPT-5.5", "input": 5.00, "output": 30.00, "context_k": 1050},
    {"model": "Claude Opus 4.7", "input": 5.00, "output": 25.00, "context_k": 200},
    {"model": "Claude Mythos Preview", "input": 25.00, "output": 125.00, "context_k": 200},
    {"model": "Gemini 3.1 Pro", "input": null, "output": null, "context_k": null, "note": "pricing not confirmed in sources"},
    {"model": "DeepSeek V4 Pro", "input": 0.435, "output": 0.87, "context_k": 1000, "open_weights": true},
    {"model": "Kimi K2.6", "input": 0.95, "output": 0.95, "context_k": 256, "open_weights": true},
    {"model": "MiniMax M2.7", "input": 0.30, "output": 0.30, "context_k": 200, "open_weights": true},
    {"model": "Qwen3.6 Plus", "input": 0.325, "output": 1.95, "context_k": 1010, "open_weights": true}
  ]
}
```

---

## Architecture & Pattern Notes

### MoE Efficiency Frontier
The April 2026 open-weights wave converged on a single architectural bet: **massive total parameters with small active parameter counts**. All three major releases (DeepSeek V4 Pro at 1.6T/49B, Kimi K2.6 at 1T/~32B, Qwen3.6-35B-A3B at 35B/3B) use MoE. The implication: inference cost is decoupled from model quality in a way that wasn't true 12 months ago. A 1.6T-parameter model now runs at the FLOP cost of a ~50B dense model.

### Hybrid Attention for Long Context
DeepSeek V4 Pro's 10% KV-cache usage at 1M-token context (vs. V3.2's baseline) is the engineering story of the month. The hybrid attention architecture (combining full attention and sliding-window layers at different frequencies) makes 1M context economically viable — not just technically possible. This directly challenges the SubQ/linear-attention narrative from last week, which claimed quadratic attention was the bottleneck.

### Self-Verification in Opus 4.7
Anthropic's addition of a self-verification loop (model tests outputs before reporting) in Opus 4.7 is a notable architectural pattern — not just a capability claim. It implies the model runs multiple inference passes per user request at xhigh effort, effectively trading latency/tokens for accuracy. Combined with file-system memory for multi-session agents, this moves Claude Opus 4.7 toward a "deliberate agent" paradigm rather than a one-shot responder.

### Restricted-Release Precedent
Claude Mythos represents the first case of a Tier-1 lab explicitly withholding a flagship model on safety grounds (not commercial readiness). The Project Glasswing structure — 12 named partners, $100M in usage credits, use-case gating to defensive security — is a template worth watching. If the cybersecurity-vulnerability-discovery capability becomes a standard feature of frontier models, gated release structures may become the norm rather than the exception.

---

## Analysis & Impact

**The SWE-bench Pro gap tells the real story.** Verified is no longer the key number: Pro (77.8% Mythos → 64.3% Opus 4.7 → 58.6% GPT-5.5 → 58.6% Kimi K2.6) shows a clean capability ladder where proprietary models still lead open-weights by ~6 points at the frontier. That gap is closing — Kimi K2.6 at 58.6% on SWE-bench Pro would have been state-of-the-art less than a year ago.

**GPT-5.5 is optimized for agentic/computer-use, not raw intelligence.** Its ARC-AGI-2 and GDPval/OSWorld numbers are the strongest available, but its GPQA Diamond (93.6%) trails Gemini 3.1 Pro (94.3%) and Claude Opus 4.7 (94.2%). For teams building GUI automation or multi-step computer-use pipelines, GPT-5.5 is the clear choice despite the 2× price jump from GPT-5.4.

**The open-weights frontier has reached "good enough for production."** DeepSeek V4 Pro at $0.87/M output tokens with 1M context and MIT license, scoring 3,206 on Codeforces and 93.5 on LiveCodeBench, is a genuine production choice for cost-sensitive coding infrastructure. Teams paying $25–30/M output tokens for GPT-5.5 or Claude Opus 4.7 on high-volume, lower-stakes tasks should reconsider.

**Gemini 3.1 Pro remains the reasoning efficiency leader.** At 94.3% GPQA Diamond, 77.1% ARC-AGI-2, and 44.4% HLE — and accessible across Vertex AI, Gemini API, Gemini CLI, and consumer apps — Google's model punches the highest on pure scientific reasoning per dollar of the major generally available models.

**Qwen3.6-35B-A3B at 22GB VRAM with 73.4% SWE-bench is the local deployment benchmark to beat.** For teams that need on-device or air-gapped deployments, 73.4% SWE-bench Verified at ~3B-active-parameter inference cost is the new floor. This is a 15-point improvement over what was achievable locally in early 2025.

---

## Key Takeaways TL;DR

1. **Claude Mythos Preview** (restricted, Glasswing only) is the world's best coding and cybersecurity model at 93.9% SWE-bench Verified / 77.8% Pro — but effectively unavailable to most builders. Its gated release via Project Glasswing sets a new precedent for safety-motivated access control.

2. **GPT-5.5** (April 23) leads all publicly available models on agentic computer-use tasks (Terminal-Bench 82.7%, OSWorld 78.7%, ARC-AGI-2 85%) at $5/$30 per million tokens — a 2× price increase over GPT-5.4 that narrows its cost-performance edge vs. Claude Opus 4.7.

3. **Claude Opus 4.7** (April 16) is the best publicly available coding model (SWE-bench Pro 64.3%) at the same price as Opus 4.6 — a free upgrade for existing Anthropic API users. Its self-verification and xhigh effort mode introduce a deliberate-agent architecture pattern.

4. **DeepSeek V4 Pro** (April 24, MIT license) delivers near-frontier quality at 97%+ lower cost than GPT-5.5 output ($0.87 vs $30/M tokens) with 1M token context — the strongest open-weights production value proposition as of May 2026.

5. **Qwen3.6-35B-A3B** (April 16, Apache 2.0) achieves 73.4% SWE-bench Verified in 22GB VRAM, setting a new bar for what's deployable locally on a single prosumer GPU.

6. **Benchmark standardization continues shifting**: SWE-bench Pro, Terminal-Bench 2.0, ARC-AGI-2, and HLE are now the differentiating metrics. SWE-bench Verified is increasingly treated as a floor, not a ceiling.

---

## Sources

1. [Introducing GPT-5.5 — OpenAI](https://openai.com/index/introducing-gpt-5-5/)
2. [GPT-5.5 Model Docs — OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.5)
3. [Introducing Claude Opus 4.7 — Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
4. [Claude Opus 4.7 Benchmarks, Pricing, Context — LLM Stats](https://llm-stats.com/blog/research/claude-opus-4-7-launch)
5. [Claude Mythos Preview & Project Glasswing — Anthropic](https://www.anthropic.com/project/glasswing)
6. [Claude Mythos Preview: Benchmarks, Pricing & Project Glasswing — LLM Stats](https://llm-stats.com/blog/research/claude-mythos-preview-launch)
7. [Claude Mythos: Why Anthropic Won't Release Its New AI Model — Built In](https://builtin.com/articles/anthropic-claude-mythos)
8. [Gemini 3.1 Pro Announcement — Google DeepMind](https://deepmind.google/blog/gemini-3-1-pro-a-smarter-model-for-your-most-complex-tasks/)
9. [Gemini 3.1 Pro on Vertex AI — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-pro-on-gemini-cli-gemini-enterprise-and-vertex-ai)
10. [DeepSeek V4 Pro — AI Model Details & Benchmarks — Benchable](https://benchable.ai/models/deepseek/deepseek-v4-pro-20260423)
11. [DeepSeek V4 Launches: 1.6T MoE, 1M Context, 10% KV — Digital Applied](https://www.digitalapplied.com/blog/deepseek-v4-preview-launch-1m-context-efficiency)
12. [DeepSeek V4 Release Date — DeepSeek AI Guide](https://deepseekai.guide/news/deepseek-v4-release-date/)
13. [Kimi K2.6 vs MiniMax M2.7 — DataLearner](https://www.datalearner.com/en/ai-models/compare/kimi-k2-6/vs/minimax-m2-7)
14. [Qwen3.6-35B-A3B: 73.4 SWE-bench, 22GB VRAM — Awesome Agents](https://awesomeagents.ai/news/qwen-3-6-35b-a3b-open-source-coder/)
15. [Qwen3.6 by Alibaba Cloud: Benchmarks — AI Tools Recap](https://aitoolsrecap.com/Blog/meet-qwen36-alibaba-cloud-2026)
16. [SWE-bench Verified Leaderboard — BenchLM](https://benchlm.ai/benchmarks/sweVerified)
17. [SWE-bench Pro Leaderboard — BenchLM](https://benchlm.ai/benchmarks/swePro)
18. [Terminal-Bench 2.0 Leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0)
19. [ARC-AGI-2 Leaderboard — BenchLM](https://benchlm.ai/benchmarks/arcAgi2)
20. [GPQA Diamond Leaderboard — Artificial Analysis](https://artificialanalysis.ai/evaluations/gpqa-diamond)
21. [Humanity's Last Exam Leaderboard — BenchLM](https://benchlm.ai/benchmarks/hle)
22. [AI Model Leaderboard — Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)
23. [Best AI Models April + May 2026 — Build Fast With AI](https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard)
24. [Kimi K2.6, DeepSeek V4, Qwen 3.6: April 2026's Open-Weight Bets — Own Your Mind](https://ownyourmind.ai/journal/open-frontier-catches-up/)
25. [Introducing GPT-5.3-Codex — OpenAI](http://openai.com/index/introducing-gpt-5-3-codex/)
