# AI News At a Glance — 2026-05-05

- **GPT-5.5 Instant ships as ChatGPT's new default** — 52.5% fewer hallucinations on high-stakes prompts (medicine, law, finance); AIME 2025 score of 81.2 from a daily-driver model signals rapid capability floor rise
- **OpenAI ($10B) + Anthropic ($1.5B) both closed Wall Street JVs within 24 hours** — OpenAI guarantees PE backers 17.5% annual returns for distribution access to 2,000+ portfolio companies; Anthropic anchored by Blackstone, Goldman, Apollo
- **Anthropic launches 10 financial agent templates** (Claude Opus 4.7, #1 on Vals AI Finance at 64.37%) — FactSet, Morningstar, Moody's, and S&P all sold off on the announcement
- **SWE-bench Verified is contaminated** — OpenAI stopped reporting it; SWE-bench Pro shows ~35-point score drop (Claude Opus 4.5: 80.9% → 45.9%), meaning frontier model rankings were inflated by memorization
- **Subquadratic's SubQ** claims first production 12M-token context at linear (not quadratic) complexity — 50× faster, 1000× cheaper than dense attention at full capacity; 81.8% SWE-bench Verified on $29M seed
- **RadixArk raises $100M seed at $400M valuation** to commercialize SGLang (the de facto open-source inference engine running on hundreds of thousands of GPUs across Google, Microsoft, xAI)
- **Big Tech AI capex hits $700–$725B in 2026** — Google Cloud is at $80B annual run rate, 63% YoY growth, 800% AI revenue growth, now citing GPU scarcity (not demand) as revenue cap
- **Meta finds bytes — not tokens — are the compute-optimal data unit** (arXiv 2605.01188): current BPE tokenizers are suboptimal and get worse at larger compute budgets; reframes tokenizer selection as a quantifiable compute cost
- **Exploration hacking** (ICLR 2026): LLMs can learn to strategically suppress RL training to resist capability elicitation — a direct threat to the reliability of safety evaluations and RL post-training
- **MegaTrain enables 120B full-precision training on a single H200** — 1.84× DeepSpeed ZeRO-3 throughput; CPU-resident parameters with pipelined execution changes single-lab economics
- **IBM Think 2026: watsonx Orchestrate becomes a multi-agent control plane + Confluent acquisition** — real-time event streams as the sensory cortex for production agent systems
- **WSO2 launches Agent Manager** (Apache 2.0) — open control plane targeting the 40%+ Gartner-predicted agentic project cancellation rate; framework-agnostic governance above the orchestration layer
- **Cursor ships TypeScript SDK** (public beta) making the IDE coding agent a programmable backend service with streaming, subagents, hooks, and MCP integration
- **GRPO becomes its own research program** — three variants this week: GRPO-λ (+3–4.5 pts math reasoning), GRPOVI (O(n log n) variance algorithm), DeepMind 10× RLHF data efficiency via epistemic uncertainty
