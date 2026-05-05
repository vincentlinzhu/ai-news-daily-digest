# Best Models — 2026-05-05

> **Scope:** Frontier model releases, benchmark leaderboards, and cost-capability tradeoffs current as of May 5, 2026. All items are new since the 2026-05-04 digest.

---

## Top Stories

### 1. GPT-5.5 Instant Releases Today — 52.5% Fewer Hallucinations, New Default for ChatGPT

OpenAI shipped **GPT-5.5 Instant** on May 5, 2026, making it the new default model for all ChatGPT users (rolling out today). The "Instant" variant is the daily-driver model—distinct from the full GPT-5.5 frontier released April 23—optimized for low latency at high volume.

**Key upgrades:**
- **52.5% fewer hallucinated claims** than GPT-5.3 Instant on high-stakes prompts (medicine, law, finance)
- **37.3% reduction** in inaccurate claims on user-flagged challenging conversations
- AIME 2025 math: **81.2** (vs. 65.4 for GPT-5.3 Instant — a 24% improvement)
- MMMU-Pro multimodal reasoning: **76** vs. 69.2 prior
- Stronger image analysis, STEM, and search-use judgment
- **Memory sources feature** across all models: shows users what context (saved memories, past chats, Gmail) shaped each response; users can delete/correct cited sources
- Enhanced personalization using past conversations and connected Gmail; rolling to Plus/Pro web first

**API availability:** `chat-latest` in the API, GPT-5.3 Instant accessible to paid users for 3 more months before retirement.

**Caveat:** Despite the hallucination reduction *within the Instant tier*, the full GPT-5.5 model still carries an **86% hallucination rate** on the AA-Omniscience accuracy benchmark — highest at the frontier, vs. Claude Opus 4.7 at 36% and Gemini 3.1 Pro at ~50%. Reducing within-tier hallucinations does not close that structural accuracy gap.

> **Sources:** [OpenAI official launch](https://openai.com/index/gpt-5-5-instant/) · [TechCrunch, May 5 2026](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/) · [The Verge, May 5 2026](https://www.theverge.com/ai-artificial-intelligence/924225/openai-chatgpt-default-model-gpt-5-5-instant)

---

### 2. SWE-bench Verified Leaderboard Refreshes (May 5, 2026) — Claude Mythos Extends Lead at 93.9%

As of today, BenchLM confirms the live SWE-bench Verified leaderboard with **44 evaluated models**. Claude Mythos Preview remains the top coding benchmark score by a wide margin.

**Top 10 — SWE-bench Verified (May 5, 2026):**

| Rank | Model | Provider | Score | Type |
|------|-------|----------|-------|------|
| 1 | Claude Mythos Preview | Anthropic | **93.9%** | Closed |
| 2 | Claude Opus 4.7 (Adaptive) | Anthropic | 87.6% | Closed |
| 3 | GPT-5.3 Codex | OpenAI | 85.0% | Closed |
| 4 | Claude Opus 4.5 | Anthropic | 80.9% | Closed |
| 5 | Claude Opus 4.6 | Anthropic | 80.8% | Closed |
| 6 | **DeepSeek V4 Pro (Max)** | DeepSeek | **80.6%** | **Open** |
| 7 | **Kimi K2.6** | Moonshot AI | **80.2%** | **Open** |
| 8 | GPT-5.5 | OpenAI | 80.0% | Closed |
| 9 | Claude Opus 4.4 | Anthropic | 79.6% | Closed |
| 10 | DeepSeek V4 Pro (High) | DeepSeek | 79.4% | Open |

Notable mid-table: **Mistral Medium 3.5** at 77.6% (open, self-hostable). **GLM-5.1** at 77.8% (open). **MiMo V2.5 Pro** (Xiaomi) at 78.0%.

This is the **first time open-weights models have clustered at 77–80%** on SWE-bench Verified, within 8 percentage points of proprietary mid-tier models. The closed/open gap at the top is now ~7 points (87.6% Claude Opus 4.7 vs. 80.6% DeepSeek V4 Pro).

> **Sources:** [BenchLM SWE-bench Verified, May 5 2026](https://benchlm.ai/benchmarks/sweVerified) · [LLM Stats](https://llm-stats.com/benchmarks/swe-bench-verified)

---

### 3. GPT-5.5 Instant vs. Claude Opus 4.7 — The Factuality Tradeoff in Full

Today's GPT-5.5 Instant launch crystallizes a tradeoff that matters for production deployments. The two top frontier models have complementary failure modes:

| Metric | GPT-5.5 | Claude Opus 4.7 |
|--------|---------|-----------------|
| Intelligence Index (AA) | **60.2** | 57.3 |
| Terminal-Bench 2.0 | **82.7%** | 69.4% |
| SWE-bench Verified | 80.0% | **87.6%** |
| SWE-bench Pro | 58.6% | **64.3%** |
| GPQA Diamond | 93.6% | **94.2%** |
| Hallucination Rate (AA-Omniscience) | **86%** | **36%** |
| API pricing (input/output per 1M) | $5 / $30 | $15 / $75 |
| Context window | 256K | 200K (1M beta) |

GPT-5.5 leads on agentic / terminal workflows and raw intelligence index. Claude Opus 4.7 leads on real-world coding accuracy, hallucination reliability, and GPQA scientific reasoning. For applications where factual correctness matters (legal, medical, research), the 2.4× hallucination rate difference is the operative signal, not the 2.9-point Intelligence Index gap.

---

### 4. DeepSeek V4 Dominates LiveCodeBench at 93.5% — Open-Weights #1 on Code Execution

**DeepSeek V4 Pro**, released April 24 and now running in production, has claimed **#1 on LiveCodeBench at 93.5% Pass@1** — ahead of all closed models. On SWE-bench Verified it scores 80.6%, matching Claude Opus 4.6. The architecture breakthrough enabling this:

**Hybrid Attention:**
- **CSA (Compressed Sparse Attention):** 4× KV compression, top-1,024 entry selection per query, 128-token sliding window
- **HCA (Heavily Compressed Attention):** 128× compression for global context
- Result: 1M-token context at **27% of V3.2's single-token inference FLOPs** and **10% of KV cache cost**

Built on 100,000+ Huawei Ascend 910B chips — zero Nvidia hardware. The US export controls on AI chips did not prevent this result; they appear to have accelerated Huawei's domestic chip program instead.

**Two-variant pricing:**

| Model | Params (Total/Active) | Context | Input $/M | Output $/M | License |
|-------|----------------------|---------|-----------|------------|---------|
| V4-Pro | 1.6T / 49B | 1M | $0.55 | $2.19 | MIT |
| V4-Flash | 284B / 13B | 1M | **$0.14** | **$0.55** | MIT |

V4-Flash at $0.14/M input is the cheapest capable frontier-adjacent model available, enabling routing architectures where 70%+ of traffic can be handled at near-zero marginal cost.

> **Sources:** [Novita AI blog](https://blogs.novita.ai/deepseek-v4-pro-novita-ai-livecodebench-1m-context/) · [Morph LLM deepseek-v4](https://www.morphllm.com/deepseek-v4) · [Build Fast with AI leaderboard](https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard)

---

### 5. Claude Mythos Preview — Restricted-Access Model at 93.9% SWE-bench, $25/$125 per 1M

**Claude Mythos Preview** (announced April 7) remains the highest-scoring model on both SWE-bench Verified (93.9%) and GPQA Diamond (94.6%), but access is restricted to ~52 organizations via Project Glasswing (12 founding partners + 40 critical-infrastructure operators). This is not commercially available at scale.

The restriction stems from its cybersecurity capabilities: Mythos autonomously passed **100% of 35 CTF challenges** on Cybench at pass@1, scored 83.1% on CyberGym, and found thousands of zero-day vulnerabilities including a 27-year-old OpenBSD bug and a 17-year-old FreeBSD NFS vulnerability. Anthropic published a **244-page System Card** before general release — a new precedent for frontier model safety documentation.

**Benchmark profile vs. Opus 4.6:**

| Benchmark | Mythos Preview | Opus 4.6 |
|-----------|---------------|----------|
| SWE-bench Verified | **93.9%** | 80.8% |
| SWE-bench Pro | **77.8%** | 53.4% |
| Terminal-Bench 2.0 | **82.0%** | 65.4% |
| SWE-bench Multimodal | **59.0%** | 27.1% |
| USAMO 2026 | **97.6%** | 42.3% |
| GPQA Diamond | **94.6%** | ~89% |
| Long-context (GraphWalks 256K–1M) | **80.0%** | 38.7% |

Pricing: **$25/$125 per 1M tokens** — 5× Opus 4.6 rates. Available via Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry (for approved orgs only).

> **Sources:** [Claude Mythos Preview benchmarks](https://claudemythosai.io/blog/mythos-preview-official-release/) · [SiliconAngle, Mar 27 2026](https://siliconangle.com/2026/03/27/anthropic-launch-new-claude-mythos-model-advanced-reasoning-features/) · [Anthropic Risk Report](https://www.anthropic.com/claude-mythos-preview-risk-report)

---

## Deep Dive: The Open-Weights Cluster at 77–80% SWE-bench Verified

Six months ago, the standard claim was "open-source is 2 years behind." As of today's leaderboard refresh, that claim is empirically wrong. Four open-weights models cluster between 77.6% and 80.6% on SWE-bench Verified — within 7 percentage points of the best publicly available closed model (Claude Opus 4.7 at 87.6%) and **ahead of GPT-5.5's 80.0%** in the standard (non-Codex) configuration.

**The open-weights cluster (SWE-bench Verified, May 5 2026):**

| Model | Score | Params | Context | License | Training Infra |
|-------|-------|--------|---------|---------|---------------|
| DeepSeek V4 Pro (Max) | 80.6% | 1.6T/49B active | 1M | MIT | Huawei Ascend |
| Kimi K2.6 | 80.2% | 1T/32B active | 256K | Apache 2.0 | Huawei Ascend |
| GLM-5.1 | 77.8% | 744B/40B active | 128K | MIT | Huawei Ascend |
| MiMo V2.5 Pro | 78.0% | 1T/42B active | 1M | Apache 2.0 | Unknown |
| Mistral Medium 3.5 | 77.6% | ~128B dense | 128K | Apache 2.0 | Nvidia |
| Qwen 3.6-35B-A3B | 73.4% | 35B/3B active | 128K | Apache 2.0 | Nvidia |

**Qwen 3.6-35B-A3B deserves special mention for local deployment:** Only 3B active parameters per token, runs on a single RTX 4090 with quantization, achieves 73.4% SWE-bench Verified and 86.0% GPQA Diamond — single-GPU frontier-adjacent performance is now real.

### Kimi K2.6 vs. DeepSeek V4 Pro Head-to-Head

| Benchmark | Kimi K2.6 | DeepSeek V4 Pro |
|-----------|-----------|-----------------|
| MMLU PRO | 84.6 | **87.5** |
| SWE-bench Verified | 80.2% | **80.6%** |
| LiveCodeBench | 89.6% | **93.5%** |
| GPQA Diamond | **90.5** | 90.1 |
| IMO-AnswerBench | **86.0** | 35.3 |
| AIME 2026 | **96.4%** | ~90% |
| SWE-bench Pro | **58.6%** | ~50% |
| Input price (per 1M) | $0.74–0.95 | **$0.55** |

Key insight: Kimi K2.6 leads on math reasoning by a massive margin (IMO-AnswerBench: 86 vs. 35.3). DeepSeek V4 Pro leads on pure coding execution (LiveCodeBench). Both trail GPT-5.5 and Claude Opus 4.7 on SWE-bench Pro — but at a fraction of the cost.

---

## Benchmark / Data JSON Blocks

### SWE-bench Verified — Top 16 (May 5, 2026)

```json
{
  "benchmark": "SWE-bench Verified",
  "date": "2026-05-05",
  "source": "benchlm.ai",
  "models": [
    {"rank": 1, "model": "Claude Mythos Preview", "provider": "Anthropic", "score": 93.9, "type": "closed"},
    {"rank": 2, "model": "Claude Opus 4.7 (Adaptive)", "provider": "Anthropic", "score": 87.6, "type": "closed"},
    {"rank": 3, "model": "GPT-5.3 Codex", "provider": "OpenAI", "score": 85.0, "type": "closed"},
    {"rank": 4, "model": "Claude Opus 4.5", "provider": "Anthropic", "score": 80.9, "type": "closed"},
    {"rank": 5, "model": "Claude Opus 4.6", "provider": "Anthropic", "score": 80.8, "type": "closed"},
    {"rank": 6, "model": "DeepSeek V4 Pro (Max)", "provider": "DeepSeek", "score": 80.6, "type": "open"},
    {"rank": 7, "model": "Kimi K2.6", "provider": "Moonshot AI", "score": 80.2, "type": "open"},
    {"rank": 8, "model": "GPT-5.5", "provider": "OpenAI", "score": 80.0, "type": "closed"},
    {"rank": 9, "model": "DeepSeek V4 Pro (High)", "provider": "DeepSeek", "score": 79.4, "type": "open"},
    {"rank": 10, "model": "DeepSeek V4 Flash (Max)", "provider": "DeepSeek", "score": 79.0, "type": "open"},
    {"rank": 11, "model": "MiMo V2.5 Pro", "provider": "Xiaomi", "score": 78.0, "type": "closed"},
    {"rank": 12, "model": "GLM-5.1", "provider": "Z.AI", "score": 77.8, "type": "open"},
    {"rank": 13, "model": "Mistral Medium 3.5", "provider": "Mistral", "score": 77.6, "type": "open"},
    {"rank": 14, "model": "Kimi K2.6 (Reasoning)", "provider": "Moonshot AI", "score": 76.8, "type": "open"},
    {"rank": 15, "model": "Qwen 3.7-235B-A22B", "provider": "Alibaba", "score": 76.2, "type": "open"},
    {"rank": 16, "model": "Grok Code Fast 1", "provider": "xAI", "score": 70.8, "type": "closed"}
  ]
}
```

### Terminal-Bench 2.0 — Top Scores

```json
{
  "benchmark": "Terminal-Bench 2.0",
  "date": "2026-05-05",
  "source": "tbench.ai / benchlm.ai",
  "description": "89 realistic CLI/shell/container/sysadmin tasks",
  "models": [
    {"rank": 1, "model": "GPT-5.5", "provider": "OpenAI", "score": 82.7},
    {"rank": 2, "model": "Claude Mythos Preview", "provider": "Anthropic", "score": 82.0},
    {"rank": 3, "model": "GPT-5.3 Codex", "provider": "OpenAI", "score": 77.3},
    {"rank": 4, "model": "Claude Opus 4.7 (Adaptive)", "provider": "Anthropic", "score": 69.4},
    {"rank": 5, "model": "DeepSeek V4 Pro (Max)", "provider": "DeepSeek", "score": 67.9}
  ]
}
```

### GPQA Diamond — Top Scores (May 2026)

```json
{
  "benchmark": "GPQA Diamond",
  "date": "2026-05",
  "source": "benchlm.ai / awesomeagents.ai",
  "models": [
    {"model": "Claude Mythos Preview", "score": 94.6},
    {"model": "Claude Opus 4.7 (Adaptive)", "score": 94.2},
    {"model": "Gemini 3.1 Pro Preview", "score": 94.3},
    {"model": "GPT-5.5", "score": 93.6},
    {"model": "Kimi K2.6", "score": 90.5},
    {"model": "DeepSeek V4 Pro (Max)", "score": 90.1},
    {"model": "Qwen 3.6-35B-A3B", "score": 86.0}
  ]
}
```

### AIME 2026 — Reasoning Benchmark

```json
{
  "benchmark": "AIME 2026",
  "date": "2026-05",
  "source": "ai-stats.phaseo.app / awesomeagents.ai",
  "models": [
    {"model": "GPT-5.4", "score": "~99%", "type": "closed"},
    {"model": "Gemini 3.1 Pro Preview", "score": "98.1%", "type": "closed"},
    {"model": "Claude Opus 4.6", "score": "98.2%", "type": "closed"},
    {"model": "Kimi K2.6", "score": "96.4%", "type": "open"},
    {"model": "GLM-5.1", "score": "95.3%", "type": "open"},
    {"model": "Qwen 3.6 Plus", "score": "95.3%", "type": "open"},
    {"model": "GPT-5.5 Instant", "score": "81.2 (AIME 2025 scaled)", "note": "AIME 2025 score used in OpenAI launch materials"}
  ]
}
```

### Frontier Pricing Comparison (May 5, 2026)

```json
{
  "date": "2026-05-05",
  "pricing_per_million_tokens": [
    {"model": "Claude Mythos Preview", "input": 25.00, "output": 125.00, "access": "restricted"},
    {"model": "GPT-5.5 Pro", "input": 30.00, "output": 180.00},
    {"model": "GPT-5.5", "input": 5.00, "output": 30.00},
    {"model": "Claude Opus 4.7", "input": 15.00, "output": 75.00},
    {"model": "Gemini 3.1 Pro", "input": 2.00, "output": 12.00},
    {"model": "DeepSeek V4 Pro", "input": 0.55, "output": 2.19, "license": "MIT"},
    {"model": "Kimi K2.6", "input": 0.74, "output": 4.00, "license": "Apache 2.0"},
    {"model": "DeepSeek V4 Flash", "input": 0.14, "output": 0.55, "license": "MIT"},
    {"model": "GLM-5.1 (API plan)", "monthly_flat": 3.00, "license": "MIT"}
  ]
}
```

---

## Architecture / Pattern Notes

### DeepSeek V4 Hybrid Attention — Why It Matters for Long Context

The V4 Hybrid Attention system is the most significant architectural innovation in the open-weights tier this cycle. Two attention modes interleaved:

- **CSA (Compressed Sparse Attention):** 4× KV compression, selects top-1,024 entries per query with a 128-token sliding window. Handles "needle in haystack" precise retrieval.
- **HCA (Heavily Compressed Attention):** 128× compression, dense attention over all tokens. Maintains global semantic coherence.

Combined result: **27% of V3.2's FLOPs and 10% of KV cache** at 1M token context. This is why $0.14/M tokens at 1M context is economically viable — the memory and compute cost curve is fundamentally different from standard transformer attention.

The Muon optimizer (used for all non-embedding weights, AdamW for embeddings) provides numerical stability at the 1.6T parameter scale without resorting to FP8 training instabilities that plagued earlier models.

### Multi-Model Routing Is Now the Standard Architecture

Data from production deployments confirms a canonical three-tier routing pattern:

```
70% traffic → DeepSeek V4-Flash ($0.14/M) — intent classification, simple Q&A
25% traffic → Claude Sonnet 4.6 (~$3/M) — standard generation
 5% traffic → Claude Opus 4.7 ($15/M) — complex coding, long-context analysis
```

Net result: **~15% of all-frontier cost, indistinguishable overall performance.** Any application hardcoded to a single model is accumulating technical debt at 255+ releases/quarter pace.

### Context Window Landscape (May 2026)

| Window Size | Models |
|-------------|--------|
| 10M tokens | Llama 4 Scout (Meta) |
| 1M tokens | Gemini 3.1 Pro, DeepSeek V4 Pro/Flash, MiMo V2.5 Pro, Claude Mythos Preview |
| 1M (beta) | Claude Opus 4.7 |
| 400K tokens | GPT-5.3 Codex |
| 256K tokens | GPT-5.5, Kimi K2.6 |
| 200K tokens | Claude Opus 4.7 (standard) |
| 128K tokens | GLM-5.1, Mistral Medium 3.5, Qwen 3.6 series |

Gemini 3.1 Pro's 1M standard context + $2/$12 pricing is still the strongest cost-context combination for document-heavy enterprise workloads.

---

## Analysis & Impact

### The Factuality Paradox at the Frontier

GPT-5.5 Instant's launch today surfaces a paradox: OpenAI's fastest-improving area (52.5% hallucination reduction in the Instant variant) addresses the *wrong* baseline. The full GPT-5.5 still hallucinates at 86% on AA-Omniscience — more than twice Claude Opus 4.7's 36% rate. The Instant improvements are relative to a worse starting point. For high-stakes deployments in regulated industries, Claude's accuracy advantage is not narrowing despite OpenAI's raw capability leads on the Intelligence Index.

### Open-Weights Models Have Crossed the Cost-Quality Inflection Point

Three months ago, the pragmatic argument for open-weights was "good enough for non-critical tasks." That framing is obsolete. DeepSeek V4 Pro at 80.6% SWE-bench Verified is within 7 points of the best publicly available closed model, MIT licensed, self-hostable. For any team running >1B tokens/month, the economics are compelling: DeepSeek V4 Pro at $0.55/M vs. Claude Opus 4.7 at $15/M is a 27× output cost difference. Even a 5-point coding accuracy penalty may be worth $270,000 per billion output tokens saved.

### Claude Mythos Is the "Known Unknown" of the Frontier

With 93.9% SWE-bench Verified, Mythos Preview is ~6 points above the next publicly available model (Claude Opus 4.7 at 87.6%). But access is restricted to ~52 organizations. This means the published frontier leaderboard understates Anthropic's actual capability lead. The question for the next 60–90 days is whether Anthropic makes Mythos generally available — or waits for Claude 5 "Fennec" — and whether either move comes before GPT-6.

### What the GPT-5.5 Instant Benchmarks Actually Signal

AIME 2025 score of 81.2 for the Instant model is notable. The Instant tier is a low-latency, lower-cost model — not the flagship GPT-5.5. An 81.2 AIME 2025 score from a *commodity* daily-driver model indicates significant progress on reasoning capability diffusion down the model tier. When the throwaway default model scores higher on math than last year's frontier models, capability floor is rising rapidly across the entire tier stack.

### Upcoming Catalysts (Next 60–90 Days)

- **GPT-6:** Expected May–July 2026. Polymarket estimates ~45–72% probability before June 30. Positioned as long-term memory + major agentic leap. Sam Altman has described it as "GPT-4 to GPT-3.5" magnitude jump.
- **Claude 5 "Fennec":** Q2–Q3 2026. Full architecture rebuild (not post-training refinement). Developer expectations: >90% SWE-bench Verified, native multi-step tool calling, better state management for long-horizon agents. Codename leaked via `claude-sonnet-5@20260203` in Google Vertex AI logs.
- **Chinese lab responses:** GLM-5.2, Kimi K2.7, MiMo V3, and DeepSeek V4.5 are all expected before Q3. Each prior cycle took 6–8 weeks between major Chinese lab releases.

---

## Key Takeaways TL;DR

1. **GPT-5.5 Instant ships today** — 52.5% fewer hallucinations vs. prior Instant, AIME 81.2, replaces GPT-5.3 Instant as ChatGPT default. Memory sources now show what context shaped each answer.

2. **SWE-bench Verified leaderboard (May 5):** Claude Mythos 93.9% → Claude Opus 4.7 87.6% → GPT-5.3 Codex 85%. First time four open-weights models cluster at 77–80% (DeepSeek V4, Kimi K2.6, GLM-5.1, MiMo V2.5).

3. **DeepSeek V4 is #1 on LiveCodeBench at 93.5%** — open, MIT licensed, $0.14/M on Flash variant, 1M context at 10% of V3.2's KV cache cost. The no-Nvidia-hardware milestone is geopolitically significant.

4. **Claude Mythos Preview is the real frontier ceiling** (93.9% SWE-bench, 94.6% GPQA, 100% Cybench CTF) — but it's invitation-only at $25/$125 per 1M. The publicly accessible leaderboard understates Anthropic's capability lead.

5. **GPT-5.5's 86% hallucination rate** (AA-Omniscience) vs. Claude Opus 4.7's 36% is the operative differentiation for regulated-industry deployments — more impactful than the 3-point Intelligence Index gap.

6. **Multi-model routing is now standard production architecture** — 70/25/5 split across DeepSeek Flash / Sonnet-tier / Opus-tier delivers frontier-equivalent performance at ~15% of all-frontier cost.

7. **GPT-6 and Claude 5 "Fennec" are the next leaderboard resets** — both expected Q2–Q3 2026. Current rankings will be materially different by August.

---

## Sources

| Publication | URL | Date |
|-------------|-----|------|
| OpenAI — GPT-5.5 Instant official launch | https://openai.com/index/gpt-5-5-instant/ | May 5, 2026 |
| TechCrunch — GPT-5.5 Instant coverage | https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/ | May 5, 2026 |
| The Verge — ChatGPT default model | https://www.theverge.com/ai-artificial-intelligence/924225/openai-chatgpt-default-model-gpt-5-5-instant | May 5, 2026 |
| BenchLM — SWE-bench Verified (live) | https://benchlm.ai/benchmarks/sweVerified | May 5, 2026 |
| Terminal-Bench 2.0 leaderboard | https://www.tbench.ai/leaderboard/terminal-bench/2.0 | May 2026 |
| GPQA Benchmark — BenchLM | https://benchlm.ai/benchmarks/gpqa | May 2026 |
| AIME 2026 leaderboard | https://ai-stats.phaseo.app/benchmarks/aime-2026 | May 2026 |
| Claude Mythos Preview benchmarks | https://claudemythosai.io/blog/mythos-preview-official-release/ | April 2026 |
| Anthropic Claude Mythos Risk Report | https://www.anthropic.com/claude-mythos-preview-risk-report | April 7, 2026 |
| SiliconAngle — Mythos announcement | https://siliconangle.com/2026/03/27/anthropic-launch-new-claude-mythos-model-advanced-reasoning-features/ | March 27, 2026 |
| Build Fast with AI — April/May leaderboard | https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard | April 30, 2026 |
| Morph LLM — DeepSeek V4 spec | https://www.morphllm.com/deepseek-v4 | April 2026 |
| Novita AI — DeepSeek V4 Pro LiveCodeBench | https://blogs.novita.ai/deepseek-v4-pro-novita-ai-livecodebench-1m-context/ | April 2026 |
| DataLearner — DeepSeek V4 vs Kimi K2.6 | https://www.datalearner.com/en/ai-models/compare/deepseek-v4-pro/vs/kimi-k2-6 | April 2026 |
| GPT-5.5 pricing breakdown — APIdog | https://apidog.com/blog/gpt-5-5-pricing/ | April 2026 |
| Artificial Analysis Intelligence Index | https://www.datalearner.com/en/leaderboards/external/aa-quality-index | May 2026 |
| Claude 5 "Fennec" release tracker | https://claude5.com/claude-5-release-date | May 2026 |
| GPT-6 / upcoming models overview | https://www.abhs.in/blog/ai-models-april-june-2026-gpt6-claude5-llama4-what-developers-should-prepare | April 2026 |
