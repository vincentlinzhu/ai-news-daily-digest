import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = "/Users/bytedance/Documents/AI_News/2026-05-14/visuals"
plt.style.use('seaborn-v0_8-whitegrid')

# ── Chart 1: Artificial Analysis Intelligence Index ──────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
models = [
    "GPT-5.5 (xhigh)", "GPT-5.5 (high)", "Claude Opus 4.7\n(Adaptive, Max Effort)",
    "Gemini 3.1 Pro Preview", "GPT-5.5 (medium)", "Grok 4.3"
]
scores = [60.2, 58.9, 57.3, 57.2, 56.7, 53.0]
colors = ['#1f77b4', '#4a90d9', '#e07b3e', '#e34234', '#7ab3e0', '#8b1a1a']
bars = ax.barh(models, scores, color=colors, height=0.6, edgecolor='white', linewidth=0.5)
for bar, score in zip(bars, scores):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{score}', va='center', ha='left', fontsize=11, fontweight='bold')
ax.set_xlabel("Intelligence Index Score", fontsize=12)
ax.set_title("Artificial Analysis Intelligence Index — May 2026", fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(45, 65)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(f"{OUT}/intelligence-index.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 done: intelligence-index.png")

# ── Chart 2: SWE-bench Verified ───────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 7))
models = [
    "Claude Mythos Preview\n(gated)", "GPT-5.5", "Claude Opus 4.7",
    "GPT-5.3 Codex", "Claude Opus 4.5", "Claude Opus 4.6",
    "DeepSeek V4 Pro Max", "Gemini 3.1 Pro", "MiniMax M2.5", "Mistral Medium 3.5"
]
scores = [93.9, 88.7, 87.6, 85.0, 80.9, 80.8, 80.6, 80.6, 80.2, 77.6]
colors = ['#9b59b6', '#1f77b4', '#e07b3e', '#1f77b4', '#e07b3e', '#e07b3e',
          '#2ecc71', '#e34234', '#3498db', '#95a5a6']
bars = ax.barh(models, scores, color=colors, height=0.65, edgecolor='white', linewidth=0.5)
for bar, score in zip(bars, scores):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'{score}%', va='center', ha='left', fontsize=10, fontweight='bold')
ax.set_xlabel("% Issues Resolved", fontsize=12)
ax.set_title("SWE-bench Verified — Coding Agent Leaderboard (May 2026)", fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(70, 100)
ax.invert_yaxis()
legend_handles = [
    mpatches.Patch(color='#9b59b6', label='Anthropic (gated)'),
    mpatches.Patch(color='#1f77b4', label='OpenAI'),
    mpatches.Patch(color='#e07b3e', label='Anthropic'),
    mpatches.Patch(color='#2ecc71', label='DeepSeek (open-weight)'),
    mpatches.Patch(color='#e34234', label='Google'),
    mpatches.Patch(color='#3498db', label='MiniMax'),
    mpatches.Patch(color='#95a5a6', label='Mistral'),
]
ax.legend(handles=legend_handles, loc='lower right', fontsize=9)
plt.tight_layout()
plt.savefig(f"{OUT}/swe-bench-verified.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 done: swe-bench-verified.png")

# ── Chart 3: ARC-AGI-2 ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
models = ["GPT-5.5", "GPT-5.4 Pro", "Human Average", "Gemini 3.1 Pro", "Claude Opus 4.7\n(Adaptive)", "Grok 4"]
scores = [85.0, 83.3, 66.0, 77.1, 75.8, 53.3]
colors = ['#1f77b4', '#4a90d9', '#2ca02c', '#e34234', '#e07b3e', '#8b1a1a']
bars = ax.bar(models, scores, color=colors, width=0.6, edgecolor='white', linewidth=0.5)
# Human average reference line
ax.axhline(y=66.0, color='#2ca02c', linestyle='--', linewidth=1.5, alpha=0.7, label='Human Average (66%)')
for bar, score in zip(bars, scores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{score}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
ax.set_ylabel("Score (%)", fontsize=12)
ax.set_title("ARC-AGI-2 — Abstract Reasoning Benchmark (May 2026)\nGPT-5.5 First to Exceed Human Average", fontsize=13, fontweight='bold', pad=12)
ax.set_ylim(40, 95)
ax.legend(fontsize=10)
plt.xticks(rotation=0, ha='center', fontsize=9)
plt.tight_layout()
plt.savefig(f"{OUT}/arc-agi-2.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3 done: arc-agi-2.png")

# ── Chart 4: Mind Robotics Funding Trajectory ─────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
rounds = ["Seed\n(Late 2025)", "Series A\n(Mar 2026)", "Series B\n(May 2026)"]
amounts = [115, 500, 400]
cumulative = [115, 615, 1015]
x = np.arange(len(rounds))
bars = ax.bar(x, amounts, color=['#3498db', '#2980b9', '#1a5276'], width=0.5, edgecolor='white', linewidth=0.8, label='Round Size ($M)')
ax2 = ax.twinx()
ax2.plot(x, cumulative, 'o-', color='#e74c3c', linewidth=2.5, markersize=10, label='Cumulative Total ($M)')
for i, (bar, amt, cum) in enumerate(zip(bars, amounts, cumulative)):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 8,
            f'${amt}M', ha='center', va='bottom', fontsize=12, fontweight='bold', color='#1a5276')
    ax2.annotate(f'${cum}M total', xy=(i, cum), xytext=(0, 12),
                 textcoords='offset points', ha='center', fontsize=10, color='#e74c3c', fontweight='bold')
ax.set_ylabel("Round Size ($M)", fontsize=12, color='#1a5276')
ax2.set_ylabel("Cumulative Raised ($M)", fontsize=12, color='#e74c3c')
ax.set_title("Mind Robotics Funding Trajectory 2025–2026\n$1B+ in Under 6 Months (Kleiner Perkins Lead, $3.4B Valuation)", fontsize=13, fontweight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(rounds, fontsize=11)
ax.set_ylim(0, 620)
ax2.set_ylim(0, 1200)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig(f"{OUT}/mind-robotics-funding.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4 done: mind-robotics-funding.png")

# ── Chart 5: LLM API Output Pricing Comparison ───────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
models = ["Claude Mythos\n(Anthropic)", "GPT-5.5 Pro\n(OpenAI)", "Claude Opus 4.7\n(Anthropic)",
          "GPT-5.5\n(OpenAI)", "Gemini 3.1 Pro\n(Google)", "Grok 4.3\n(xAI)",
          "DeepSeek V4 Pro\n(DeepSeek)", "ERNIE 5.1\n(Baidu)", "DeepSeek V4 Flash\n(DeepSeek)"]
prices = [125, 180, 25, 30, 12, 2.50, 3.48, 2.65, 0.28]
colors = ['#9b59b6', '#1f77b4', '#e07b3e', '#4a90d9', '#e34234', '#8b1a1a', '#2ecc71', '#f39c12', '#27ae60']
bars = ax.barh(models, prices, color=colors, height=0.65, edgecolor='white', linewidth=0.5)
for bar, price in zip(bars, prices):
    label = f'${price:.2f}' if price < 10 else f'${price:.0f}'
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            label, va='center', ha='left', fontsize=10, fontweight='bold')
ax.set_xlabel("Output Price per 1M Tokens (USD)", fontsize=12)
ax.set_title("Frontier LLM API Output Pricing — May 2026\n(Higher = More Expensive)", fontsize=13, fontweight='bold', pad=12)
ax.set_xscale('log')
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(f"{OUT}/llm-api-pricing.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5 done: llm-api-pricing.png")

# ── Chart 6: Multi-Turn Performance Drop ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
categories = ['Single-Turn\nBaseline', 'Multi-Turn\n(Sharding Simulation)']
values = [100, 61]
colors_bar = ['#2ecc71', '#e74c3c']
bars = ax.bar(categories, values, color=colors_bar, width=0.45, edgecolor='white', linewidth=0.8)
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{val}%', ha='center', va='bottom', fontsize=18, fontweight='bold')
ax.annotate('', xy=(1, 61), xytext=(0, 100),
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=2.5))
ax.text(0.5, 80, '−39%\nperformance\ndrop', ha='center', va='center', fontsize=14,
        color='#c0392b', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#fadbd8', edgecolor='#e74c3c', alpha=0.9))
ax.set_ylim(0, 115)
ax.set_ylabel("Relative Performance (%)", fontsize=12)
ax.set_title("LLMs Get Lost in Multi-Turn Conversation\n(ICLR 2026 Outstanding Paper — 15 LLMs, 200K+ Conversations)", fontsize=13, fontweight='bold', pad=12)
props_text = "Unreliability: +112% | Aptitude loss: −15%"
ax.text(0.5, -0.12, props_text, transform=ax.transAxes, ha='center', fontsize=11,
        color='#555', style='italic')
plt.tight_layout()
plt.savefig(f"{OUT}/multi-turn-performance-drop.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 6 done: multi-turn-performance-drop.png")

# ── Chart 7: Terminal-Bench 2.0 & OSWorld ─────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
benchmarks = ["Terminal-Bench 2.0", "OSWorld-Verified", "BrowseComp", "GPQA Diamond"]
gpt55 = [82.7, 78.7, 84.4, 93.6]
gemini = [68.5, None, None, 94.3]
claude = [65.4, None, 84.0, None]
gpt54 = [75.1, None, None, 92.8]

x = np.arange(len(benchmarks))
width = 0.2

b1 = ax.bar(x - 1.5*width, gpt55, width, label='GPT-5.5', color='#1f77b4', edgecolor='white')
b2 = ax.bar(x - 0.5*width, [v if v else 0 for v in gemini], width, label='Gemini 3.1 Pro', color='#e34234', edgecolor='white')
b3 = ax.bar(x + 0.5*width, [v if v else 0 for v in claude], width, label='Claude Opus 4.6', color='#e07b3e', edgecolor='white')
b4 = ax.bar(x + 1.5*width, [v if v else 0 for v in gpt54], width, label='GPT-5.4', color='#4a90d9', edgecolor='white')

def add_labels(bars, values):
    for bar, val in zip(bars, values):
        if val:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                    f'{val}', ha='center', va='bottom', fontsize=8, fontweight='bold')

add_labels(b1, gpt55)
add_labels(b2, gemini)
add_labels(b3, claude)
add_labels(b4, gpt54)

ax.set_ylabel("Score (%)", fontsize=12)
ax.set_title("Agentic & Capability Benchmarks Comparison — May 2026", fontsize=13, fontweight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(benchmarks, fontsize=10)
ax.set_ylim(50, 105)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(f"{OUT}/agentic-benchmarks.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 7 done: agentic-benchmarks.png")

# ── Chart 8: GDPval-AA Knowledge Work ELO ────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
models = ["Claude Opus 4.7", "Claude Opus 4.6", "GPT-5.4", "Grok 4.3", "Gemini 3.1 Pro"]
elos = [1753, 1606, 1674, 1500, 1314]
colors_elo = ['#e07b3e', '#e07b3e', '#1f77b4', '#8b1a1a', '#e34234']
sorted_pairs = sorted(zip(elos, models, colors_elo), reverse=True)
elos_s, models_s, colors_s = zip(*sorted_pairs)
bars = ax.barh(list(models_s), list(elos_s), color=list(colors_s), height=0.6, edgecolor='white', linewidth=0.5)
for bar, elo in zip(bars, elos_s):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'{elo}', va='center', ha='left', fontsize=12, fontweight='bold')
ax.set_xlabel("Elo Rating", fontsize=12)
ax.set_title("GDPval-AA Knowledge Work Elo — May 2026\n(Economic productivity tasks: legal, finance, research)", fontsize=13, fontweight='bold', pad=12)
ax.set_xlim(1250, 1820)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(f"{OUT}/gdpval-knowledge-work.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 8 done: gdpval-knowledge-work.png")

print("\nAll 8 charts generated successfully.")
