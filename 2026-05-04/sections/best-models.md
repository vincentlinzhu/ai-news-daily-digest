# Best Models — AI News Digest 2026-05-04

> Coverage window: ~April 23 – May 4, 2026. Stories from the 2026-05-01 digest are not repeated unless materially updated.

---

## Top Stories

### 1. GPT-5.5 Tops the Intelligence Index — Breaks Three-Way Tie at the Frontier

OpenAI released GPT-5.5 on **April 23, 2026**, the first fully retrained base model since GPT-4.5. It breaks a three-way tie between OpenAI, Anthropic, and Google on the Artificial Analysis Intelligence Index, claiming the #1 spot with a score of **60** — a 3-point lead over Claude Opus 4.7 and Gemini 3.1 Pro Preview (both at 57).

GPT-5.5 leads five headline evaluations: Terminal-Bench Hard, GDPval-AA (economic task performance, Elo 1785), APEX-Agents-AA (new agentic benchmark), AA-Omniscience accuracy (57%, highest ever recorded), and τ²-Bench Telecom. It places second to Gemini 3.1 Pro Preview on three benchmarks.

**The effort-scaling story is genuinely useful for practitioners:** GPT-5.5 (medium) matches Claude Opus 4.7 (max) on the Intelligence Index at roughly one-quarter the cost (~$1,200 vs $4,800 to run the full AA benchmark suite), while Gemini 3.1 Pro Preview achieves similar parity at ~$900. GPT-5.5 (low) approximates Claude Opus 4.7 (non-reasoning, high) at ~$500 vs ~$1,000.

**Caveat — hallucination:** GPT-5.5's 86% hallucination rate on AA-Omniscience is well above Claude Opus 4.7 (36%) and Gemini 3.1 Pro Preview (50%). It's more likely to "answer confidently when it doesn't know," which matters in production RAG pipelines and fact-sensitive applications.

Pricing doubled from GPT-5.4: **$5.00 / $30.00 per 1M input/output tokens** (cached input: $0.50). The ~40% token efficiency gain partially offsets the hike — net ~20% cost increase to run the same workload.

**Source:** [Artificial Analysis, April 23, 2026](https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model)

---

### 2. Open Weights Surge: Kimi K2.6, DeepSeek V4, and MiMo V2.5 Pro Cluster Within 6 Points of Proprietary Frontier

In the final week of April 2026, three major open-weights MoE models arrived in rapid succession — all from China-based labs, all permissively licensed, and all now within 3–6 points of GPT-5.5 on the Intelligence Index. One year ago, the best open-weights model (DeepSeek V3 0324) trailed the leader by 13 points; today that gap has roughly halved.

| Model | Lab | Total Params | Active Params | Context | AA Index | License | Pricing (input/output /1M) |
|---|---|---|---|---|---|---|---|
| **Kimi K2.6** | Moonshot AI | 1T | 32B | 256K | 54 | Modified MIT | API variable |
| **MiMo V2.5 Pro** | Xiaomi | 1.02T | 42B | 1M | 54 | Apache 2.0 | $1.00 / $3.00 |
| **DeepSeek V4 Pro** | DeepSeek | 1.6T | 49B | 1M | 52 | MIT | $1.74 / $3.48 |

**Key divergence:** While these models approach proprietary parity on general intelligence, the gap to closed models is still large on the hardest reasoning and agentic coding tasks:
- HLE (Humanity's Last Exam): open weights 34–36% vs GPT-5.5 44%, Gemini 3.1 Pro 45%
- CritPt (research-level physics): open weights 4–12% vs GPT-5.5 27%
- TerminalBench Hard: open weights 43–46% vs GPT-5.5 61%, Gemini 3.1 Pro 54%

Open-weights models now dominate the **Pareto frontier for Intelligence vs. Price**: 9 of 13 Pareto-optimal models are open weights. Kimi K2.6 and MiMo V2.5 Pro are explicitly on the frontier; DeepSeek V4 Pro sits just below.

**Sources:** [Artificial Analysis open-weights roundup, April 30](https://artificialanalysis.ai/articles/recent-open-weights-model-launches); [DeepSeek V4 analysis, April 24](https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash); [MarkTechPost Kimi K2.6, April 20](https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/)

---

### 3. Mistral Medium 3.5 — Open-Weights Coding Record at Mid-Tier Price

Mistral AI shipped **Mistral Medium 3.5** on April 29, 2026, a 128B dense (not MoE) model with a **77.6% SWE-bench Verified** score — the highest open-weights result on that benchmark, edging past Claude Sonnet 4 (77.2%) and sitting above Gemini 3.1 Pro Preview (78.8%) as its nearest peer.

Architecture: 256K context window, native vision (text + images), configurable reasoning effort, JSON output, and native function calling. Self-hostable on **four H100/H200 GPUs** — a lower hardware requirement than 1T-parameter MoE models. Available under **Modified MIT license**.

Pricing via Mistral AI API: **$1.50 / $7.50 per 1M input/output tokens** (image input: $1.00/M). This slots it between budget and frontier price tiers, making it a strong choice for teams that want open-weights auditability with near-Claude-Sonnet coding performance.

Mistral simultaneously launched Medium 3.5 as the backend for their **remote coding agents** in Vibe and Le Chat — similar to how Anthropic uses Opus for Claude Code.

**Source:** [LLM Reference](https://www.llmreference.com/model/mistral-medium-3.5); [Awesome Agents](https://awesomeagents.ai/news/mistral-medium-3-5-vibe-remote-agents/)

---

### 4. Grok 4.3 — Better Agentic Performance, ~40–60% Price Cut

xAI released **Grok 4.3** on April 30, 2026. It scores **53 on the AA Intelligence Index**, 4 points above Grok 4.20, while cutting prices by ~37.5% on input and ~58% on output tokens versus Grok 4.20 0309 v2.

The single largest improvement: **GDPval-AA Elo jumped 321 points** (1179 → 1500) — a major gain on real-world economic task performance, surpassing Gemini 3.1 Pro Preview and GPT-5.4-mini on that benchmark while still trailing GPT-5.5 by 276 Elo points (~17% win rate under standard Elo).

Grok 4.3 costs ~$395 to run the full Artificial Analysis Intelligence Index — among the lowest at its intelligence tier. However, it uses ~44% more output tokens than Grok 4.20, which partially offsets the per-token price reduction.

Strong instruction-following: 98% on τ²-Bench Telecom (customer service agents), matching GLM-5.1. IFBench maintained at 81%.

**Source:** [Artificial Analysis, April 30, 2026](https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing)

---

### 5. Claude Mythos Preview — Anthropic's Restricted Release for Critical Infrastructure

*New details since the 2026-05-01 digest: broader access scope and pricing confirmed.*

Claude Mythos Preview, released April 7, 2026, is available to approximately **52 organizations total** — 12 founding Project Glasswing partners (Amazon, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks + one unannounced) plus ~40 additional vetted critical infrastructure organizations. No public waitlist exists.

Pricing is **$25 / $125 per 1M input/output tokens** — 5× Claude Opus 4.7 pricing, reflecting both exclusivity and the model's exceptional capability for zero-day vulnerability detection. On BenchLM's coding leaderboard, Mythos Preview achieves **93.9% on SWE-bench Verified**, roughly 6 points above Claude Opus 4.7 (87.6%).

A signal in the [idlen.io tracking data](https://www.idlen.io/news/claude-mythos-imminent-release-before-may-6-code-with-claude-anthropic/) suggests a possible broader "Code with Claude" launch before May 6, though Anthropic has not confirmed public availability timelines.

**Sources:** [WaveSpeedAI](https://wavespeed.ai/blog/posts/claude-mythos-preview-access-2026/); [Awesome Agents](https://awesomeagents.ai/models/claude-mythos-preview/); [gentic.news](https://gentic.news/article/claude-mythos-preview-priced-at-25)

---

## Deep Dive: Kimi K2.6 Architecture and Agentic Engineering

Kimi K2.6 deserves extended treatment because it demonstrates what trillion-parameter open-weights MoE can do when the training objective is explicitly agentic.

### Architecture

- **MoE:** 1T total / 32B active parameters, 384 experts (8 selected per token + 1 shared expert always active), 61 layers (1 dense), MLA attention
- **Vision:** MoonViT encoder (400M params), native image + video, no adapter bolt-on
- **Context:** 256K tokens
- **Deployment:** vLLM, SGLang, or KTransformers; compatible with K2.5 deployment configs (`transformers >= 4.57.1, < 5.0.0`)
- **Two inference modes:** Thinking (chain-of-thought, temp 1.0, preserve_thinking for multi-turn agents) and Instant (temp 0.6, top-p 0.95)

### Long-Horizon Real-World Demos

**Demo 1 — Zig inference optimization:**
- Task: deploy Qwen3.5-0.8B on macOS, optimize inference in Zig
- Execution: 4,000+ tool calls, 12+ hours, 14 iterations
- Result: throughput 15 → 193 tokens/sec (~20% faster than LM Studio)

**Demo 2 — 8-year-old financial matching engine:**
- Task: overhaul exchange-core (Java, open source, financial grade)
- Execution: 13 hours, 1,000+ tool calls, 4,000+ lines modified
- Actions: profiled CPU/memory flame graphs, reconfigured thread topology (4ME+2RE → 2ME+1RE)
- Result: +185% medium throughput (0.43 → 1.24 MT/s), +133% peak throughput (1.23 → 2.86 MT/s)

### Agent Swarm Architecture: Claw Groups

The Claw Groups system (research preview) enables a heterogeneous multi-agent ecosystem where K2.6 serves as the **adaptive coordinator**:
- External agents from any device, any model, with own tools/memory
- K2.6 dynamically assigns tasks based on agent skill profiles
- Detects failures, reassigns or regenerates subtasks
- Scales to 300 sub-agents, 4,000 coordinated steps (3× K2.5 capacity)

The **Skills** capability — converting any PDF/spreadsheet/slide into a reusable task template — is a notable productization move: it makes knowledge from documents executable by the swarm rather than just retrievable.

---

## Benchmark Data

### Artificial Analysis Intelligence Index (May 2026 snapshot)

```json
{
  "leaderboard": [
    {"model": "GPT-5.5 (xhigh)", "lab": "OpenAI", "score": 60, "type": "proprietary", "cost_to_run_index_usd": "~1500"},
    {"model": "GPT-5.5 (high)", "lab": "OpenAI", "score": 58.9, "type": "proprietary"},
    {"model": "Claude Opus 4.7 (Adaptive, Max)", "lab": "Anthropic", "score": 57, "type": "proprietary", "cost_to_run_index_usd": 4811},
    {"model": "Gemini 3.1 Pro Preview", "lab": "Google", "score": 57, "type": "proprietary", "cost_to_run_index_usd": "~900"},
    {"model": "GPT-5.4 (xhigh)", "lab": "OpenAI", "score": 56.8, "type": "proprietary"},
    {"model": "Kimi K2.6 (Reasoning)", "lab": "Moonshot AI", "score": 54, "type": "open-weights", "cost_to_run_index_usd": 948},
    {"model": "MiMo V2.5 Pro (Reasoning)", "lab": "Xiaomi", "score": 54, "type": "open-weights"},
    {"model": "DeepSeek V4 Pro (Reasoning, Max)", "lab": "DeepSeek", "score": 52, "type": "open-weights", "cost_to_run_index_usd": 1071},
    {"model": "Grok 4.3", "lab": "xAI", "score": 53, "type": "proprietary", "cost_to_run_index_usd": 395},
    {"model": "Muse Spark", "lab": "unknown", "score": "~53", "type": "proprietary"},
    {"model": "DeepSeek V4 Flash (Reasoning, Max)", "lab": "DeepSeek", "score": 47, "type": "open-weights", "cost_to_run_index_usd": 113}
  ],
  "note": "AA Intelligence Index aggregates multiple benchmarks. Costs are to run the full Artificial Analysis benchmark suite.",
  "source": "https://artificialanalysis.ai (multiple articles, April 23-30 2026)"
}
```

### SWE-bench Verified (Coding — Real GitHub Issues)

```json
{
  "benchmark": "SWE-bench Verified",
  "top_results": [
    {"model": "Claude Mythos Preview", "score_pct": 93.9, "type": "proprietary-restricted"},
    {"model": "Claude Opus 4.7 (Adaptive)", "score_pct": 87.6, "type": "proprietary"},
    {"model": "GPT-5.5", "score_pct": 82.6, "type": "proprietary"},
    {"model": "Claude Opus 4.7 (standard)", "score_pct": 82.0, "type": "proprietary"},
    {"model": "Kimi K2.6", "score_pct": 80.2, "type": "open-weights"},
    {"model": "Gemini 3.1 Pro Preview", "score_pct": 78.8, "type": "proprietary"},
    {"model": "Mistral Medium 3.5", "score_pct": 77.6, "type": "open-weights"},
    {"model": "Claude Sonnet 4", "score_pct": 77.2, "type": "proprietary"}
  ],
  "note": "500 human-verified real GitHub issues from Python OSS repos",
  "sources": ["benchlm.ai", "awesomeagents.ai", "llmreference.com"]
}
```

### SWE-bench Pro (Harder, Professional Repos)

```json
{
  "benchmark": "SWE-bench Pro",
  "top_results": [
    {"model": "Kimi K2.6", "score_pct": 58.6, "type": "open-weights"},
    {"model": "GPT-5.4 (xhigh)", "score_pct": 57.7, "type": "proprietary"},
    {"model": "MiMo V2.5 Pro", "score_pct": 57.2, "type": "open-weights"},
    {"model": "Gemini 3.1 Pro (thinking high)", "score_pct": 54.2, "type": "proprietary"},
    {"model": "Claude Opus 4.6 (max effort)", "score_pct": 53.4, "type": "proprietary"},
    {"model": "Kimi K2.5", "score_pct": 50.7, "type": "open-weights"}
  ],
  "note": "Professional-grade repositories, harder than SWE-bench Verified",
  "source": "MarkTechPost / Moonshot AI release (April 20 2026)"
}
```

### Key Agentic & Reasoning Benchmarks (Multi-Model Comparison)

```json
{
  "benchmarks": {
    "HLE_full_with_tools": {
      "description": "Humanity's Last Exam — one of the hardest knowledge benchmarks, tool-use variant",
      "results": [
        {"model": "Kimi K2.6", "score": 54.0},
        {"model": "Claude Opus 4.6", "score": 53.0},
        {"model": "GPT-5.4 (xhigh)", "score": 52.1},
        {"model": "Gemini 3.1 Pro", "score": 51.4},
        {"model": "Kimi K2.6 (open-weights, no tools)", "score": "34-36%"},
        {"model": "GPT-5.5 (xhigh, no tools)", "score": 44},
        {"model": "Gemini 3.1 Pro Preview (no tools)", "score": 45}
      ]
    },
    "terminal_bench_2_hard": {
      "description": "Agentic coding and terminal use",
      "results": [
        {"model": "GPT-5.5 (xhigh)", "score": 61},
        {"model": "Gemini 3.1 Pro Preview", "score": 54},
        {"model": "MiMo V2.5 Pro", "score": "43-46"},
        {"model": "Kimi K2.6", "score": "43-46"},
        {"model": "DeepSeek V4 Pro", "score": "43-46"}
      ]
    },
    "AIME_2026": {
      "description": "Math olympiad — replaces AIME 2025 which was saturated",
      "results": [
        {"model": "Kimi K2.6", "score_pct": 96.4},
        {"model": "GLM-5", "score_pct": 95.8},
        {"model": "Kimi K2.5", "score_pct": 95.8}
      ]
    },
    "GDPval_AA_Elo": {
      "description": "Real-world economically valuable task performance (Artificial Analysis)",
      "results": [
        {"model": "GPT-5.5 (xhigh)", "elo": 1785},
        {"model": "DeepSeek V4 Pro (Max)", "elo": 1554},
        {"model": "GLM-5.1", "elo": 1535},
        {"model": "MiniMax-M2.7", "elo": 1514},
        {"model": "Kimi K2.6", "elo": 1484},
        {"model": "Grok 4.3", "elo": 1500},
        {"model": "Claude Opus 4.7 (max)", "elo": "~1755"}
      ]
    }
  }
}
```

### Pricing Comparison Table (May 2026)

```json
{
  "models": [
    {"model": "Claude Mythos Preview", "input_per_1m": 25.00, "output_per_1m": 125.00, "type": "proprietary-restricted", "context_k": 200},
    {"model": "Claude Opus 4.7", "input_per_1m": 5.00, "output_per_1m": 25.00, "type": "proprietary", "context_k": 200},
    {"model": "GPT-5.5", "input_per_1m": 5.00, "output_per_1m": 30.00, "type": "proprietary", "context_k": 128},
    {"model": "Gemini 3.1 Pro", "input_per_1m": "~3.50", "output_per_1m": "~10.50", "type": "proprietary", "context_k": 1000},
    {"model": "Mistral Medium 3.5", "input_per_1m": 1.50, "output_per_1m": 7.50, "type": "open-weights-API", "context_k": 256},
    {"model": "MiMo V2.5 Pro", "input_per_1m": 1.00, "output_per_1m": 3.00, "type": "open-weights", "context_k": 1000},
    {"model": "DeepSeek V4 Pro", "input_per_1m": 1.74, "output_per_1m": 3.48, "type": "open-weights", "context_k": 1000},
    {"model": "DeepSeek V4 Flash", "input_per_1m": 0.14, "output_per_1m": 0.28, "type": "open-weights", "context_k": 1000},
    {"model": "MiniMax M2.7", "input_per_1m": 0.30, "output_per_1m": "~1.20", "type": "open-weights", "context_k": 1000}
  ],
  "note": "V4 Flash and M2.7 represent extreme value tiers. Cached input pricing often 10-20% of base input."
}
```

---

## Architecture & Pattern Notes

### The 1T MoE MoE Architecture Convergence

Three of the four leading open-weights models now share near-identical top-level specs: ~1T total params, 32–49B active, MLA-style attention, MoE routing with sparse expert selection, permissive licenses. This is now the de facto architecture for frontier-class open-weights:

- **Kimi K2.6:** 1T / 32B active, 384 experts (8+1), 256K context
- **MiMo V2.5 Pro:** 1.02T / 42B active, 1M context, native omnimodal
- **DeepSeek V4 Pro:** 1.6T / 49B active (outlier — bigger active slice), 1M context
- **MiniMax M2.7** (from prior digest): 56B active, 1M context, $0.30/M input

The tradeoff between active parameter count (compute cost per token) and total param count (model capacity) is the key architectural lever. DeepSeek V4 Pro's 49B active params make it the most expensive of the group to serve; Kimi K2.6's 32B is the lowest inference cost per token at this intelligence tier.

### Reasoning Effort as a First-Class API Parameter

GPT-5.5's five-tier effort system (xhigh / high / medium / low / non-reasoning) formalized what Claude has offered with "Adaptive Reasoning" and Kimi offers with Thinking/Instant modes. The pattern is now universal: a single model checkpoint, multiple latency/cost/quality operating points configured at request time. This shifts optimization from model selection to effort routing, and makes per-query cost modeling a first-class engineering concern.

### Hallucination Rate Divergence at the Frontier

GPT-5.5's 86% hallucination rate on AA-Omniscience vs. Anthropic's 36% is a meaningful signal. The "accuracy-first" training objective (maximizing correct answers) without a commensurate "abstain-when-uncertain" signal appears to be trading factual recall for confabulation risk. Claude's Constitutional AI training and Google's RLHF/RLAIF approach both show more conservative hallucination profiles. For applications where false confidence is costly (legal, medical, financial), this gap matters more than the 3-point Intelligence Index advantage.

---

## Analysis & Impact

**The 6-point gap is the headline, but the shape of the gap matters more.** Open-weights models are now within 6 points of proprietary leaders on general intelligence aggregates, but the gap is concentrated in the hardest 5–10% of tasks: CritPt physics (12% vs 27%), TerminalBench Hard (46% vs 61%), HLE without tools (36% vs 44%). For the 90%+ of production use cases that don't require research-level physics or sustained long-horizon coding, open-weights at $1–3.50/M is effectively "good enough."

**GPT-5.5's position is real but fragile.** A 3-point Intelligence Index lead with 86% hallucination is a lead that Anthropic and Google will contest directly. Claude Opus 4.7 (max) costs ~3× more than GPT-5.5 (xhigh) to run the same index suite — but scores within 3 points with far lower hallucination. The practical premium for Claude is justified in accuracy-sensitive pipelines; the practical premium for GPT-5.5 is justified in raw-capability agentic pipelines.

**Mistral Medium 3.5 is the value story of the week.** At $1.50/M input and 77.6% SWE-bench Verified — above Claude Sonnet 4 — it undercuts the mid-tier proprietary bracket significantly. Its 128B dense architecture (vs MoE) means more predictable inference latency, and four-GPU self-hosting is accessible to mid-size engineering teams. For organizations running high-volume coding agents who can't afford Claude Opus pricing, this is the clearest new option.

**DeepSeek V4 Pro's hallucination rate (94%) is a deployment risk.** Despite scoring 52 on the Intelligence Index and leading open-weights on real-world economic tasks (GDPval-AA Elo 1554), the model essentially always responds even when wrong. For RAG/retrieval pipelines or knowledge-intensive agents, this is a reliability hazard that likely outweighs its benchmark advantages over Kimi K2.6 and MiMo V2.5 Pro.

**Claude Mythos Preview's pricing signals its positioning.** At $25/$125 per 1M tokens — 5× Opus — it's not designed for production API scale; it's priced as a consulting-grade security research tool. The 93.9% SWE-bench Verified score (vs 87.6% for Opus 4.7) is significant, but the ~6pp improvement comes at a 5× price multiplier. Broad availability would require at minimum a cost-reduction path — perhaps a Sonnet-tier distillation.

---

## Key Takeaways (TL;DR)

1. **GPT-5.5 leads the Intelligence Index** (score: 60) but at doubled per-token pricing ($5/$30) and the highest hallucination rate at the frontier (86%). Effort-scaling makes it cost-competitive at medium tier vs. Claude Opus.

2. **Three leading open-weights models cluster at 52–54 on the Intelligence Index** — Kimi K2.6, MiMo V2.5 Pro, and DeepSeek V4 Pro. The gap to proprietary has halved in one year. All are trillion-parameter MoE, permissively licensed, from China-based labs.

3. **Mistral Medium 3.5 sets the open-weights SWE-bench Verified record** (77.6%), beats Claude Sonnet 4, and is self-hostable on 4× H100s at $1.50/M. The clearest new production option for mid-tier coding agents.

4. **Grok 4.3 offers the best $/intelligence trade at 53** — $395 to run the full AA index, with a 321-point GDPval-AA Elo jump over Grok 4.20.

5. **Claude Mythos Preview (93.9% SWE-bench Verified) is the most capable coding model** but restricted to ~52 vetted critical infrastructure organizations at $25/$125 per 1M. A broader release signal is emerging but unconfirmed.

6. **Hallucination rates diverge sharply at the frontier**: GPT-5.5 (86%) vs. Claude Opus 4.7 (36%) vs. Gemini 3.1 Pro (50%). For factual-accuracy-sensitive applications, the Intelligence Index ranking does not translate directly to deployment trust.

7. **Effort-level API parameters are now universal** — GPT-5.5 (5 tiers), Claude Adaptive Reasoning, Kimi Thinking/Instant. The engineering problem has shifted from "which model" to "which effort level for this query class."

---

## Sources

| Source | URL | Date |
|---|---|---|
| Artificial Analysis — GPT-5.5 Analysis | https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model | April 23, 2026 |
| Artificial Analysis — Open Weights Roundup | https://artificialanalysis.ai/articles/recent-open-weights-model-launches | April 30, 2026 |
| Artificial Analysis — DeepSeek V4 | https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash | April 24, 2026 |
| Artificial Analysis — Grok 4.3 | https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing | April 30, 2026 |
| MarkTechPost — Kimi K2.6 | https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/ | April 20, 2026 |
| Moonshot AI — Kimi K2.6 Blog | https://www.kimi.com/blog/kimi-k2-6 | April 2026 |
| LLM Reference — Mistral Medium 3.5 | https://www.llmreference.com/model/mistral-medium-3.5 | April 29, 2026 |
| Awesome Agents — Mistral Medium 3.5 | https://awesomeagents.ai/models/mistral-medium-3.5/ | April 2026 |
| SiliconANGLE — Claude Mythos | https://siliconangle.com/2026/03/27/anthropic-launch-new-claude-mythos-model-advanced-reasoning-features/ | March 2026 |
| WaveSpeedAI — Mythos Access | https://wavespeed.ai/blog/posts/claude-mythos-preview-access-2026/ | 2026 |
| gentic.news — Mythos Pricing | https://gentic.news/article/claude-mythos-preview-priced-at-25 | 2026 |
| BenchLM — SWE-bench Verified | https://benchlm.ai/benchmarks/sweVerified | May 2026 |
| Decrypt — MiMo V2.5 Pro | https://decrypt.co/365184/xiaomi-mimo-2-5-pro-ai-see-hear-act-one-model | April 2026 |
| Plain AI — MiMo V2.5 Pro | https://plainai.tech/articles/xiaomi-mimo-v25-pro-open-source-ai-model-review-benchmarks | April 2026 |
| OpenAI — GPT-5.5 Announcement | https://openai.com/index/introducing-gpt-5-5/ | April 23, 2026 |
| Deep Learning AI — GPT-5.5 | https://www.deeplearning.ai/the-batch/openais-latest-model-gpt-5-5-tops-leaderboards-for-coding-visual-puzzles-and-overall-intelligence/ | April 2026 |
