import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

VISUALS = "/Users/bytedance/Documents/AI_News/2026-05-26/visuals"
plt.style.use('seaborn-v0_8-whitegrid')

# ─────────────────────────────────────────────────
# 1. Intelligence Index (Artificial Analysis v4.0)
# ─────────────────────────────────────────────────
models = ["GPT-5.5", "Claude Opus 4.7", "Qwen 3.7 Max", "DeepSeek V4-Pro"]
scores = [60.2, 57.3, 56.6, 55.5]
colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(models[::-1], scores[::-1], color=colors[::-1], edgecolor='white', linewidth=0.8)
for bar, score in zip(bars, scores[::-1]):
    ax.text(score + 0.2, bar.get_y() + bar.get_height()/2,
            f'{score}', va='center', ha='left', fontsize=12, fontweight='bold')
ax.set_xlabel('Intelligence Index Score', fontsize=13)
ax.set_title('Artificial Analysis Intelligence Index v4.0\nOverall Model Comparison — May 2026', fontsize=14, fontweight='bold')
ax.set_xlim(0, 70)
ax.tick_params(axis='y', labelsize=12)
plt.tight_layout()
plt.savefig(f'{VISUALS}/intelligence-index.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: intelligence-index.png")

# ─────────────────────────────────────────────────
# 2. SWE-Bench Pro (coding agents)
# ─────────────────────────────────────────────────
models2 = ["Claude Opus 4.7", "Kimi K2.6 Thinking", "Qwen 3.7 Max", "GLM-5.1", "GPT-5.5",
           "DeepSeek V4-Pro", "Gemini 3.5 Flash", "Gemini 3.1 Pro", "Mistral Medium 3.5"]
scores2 = [64.3, 59.5, 60.6, 58.4, 58.6, 55.4, 55.1, 54.2, 31.0]
colors2 = ['#DD8452','#8172B3','#55A868','#CCB974','#4C72B0',
           '#C44E52','#64B5CD','#4C72B0','#777777']

sorted_pairs = sorted(zip(scores2, models2, colors2))
s_scores, s_models, s_colors = zip(*sorted_pairs)

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(s_models, s_scores, color=s_colors, edgecolor='white', linewidth=0.8)
for bar, score in zip(bars, s_scores):
    ax.text(score + 0.3, bar.get_y() + bar.get_height()/2,
            f'{score}%', va='center', ha='left', fontsize=10, fontweight='bold')
ax.set_xlabel('% Tasks Resolved', fontsize=13)
ax.set_title('SWE-Bench Pro — Agentic Coding\n(1,865 multi-language tasks, May 2026)', fontsize=14, fontweight='bold')
ax.set_xlim(0, 78)
ax.axvline(x=55, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax.tick_params(axis='y', labelsize=10)
plt.tight_layout()
plt.savefig(f'{VISUALS}/swe-bench-pro.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: swe-bench-pro.png")

# ─────────────────────────────────────────────────
# 3. SWE-Bench Verified vs Pro Gap
# ─────────────────────────────────────────────────
models3 = ["Claude Opus 4.7", "GPT-5.5", "DeepSeek V4-Pro", "Qwen 3.7 Max", "Gemini 3.5 Flash"]
verified = [87.6, 88.7, 83.7, 80.4, 55.1]
pro = [64.3, 58.6, 55.4, 60.6, 55.1]

x = np.arange(len(models3))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, verified, width, label='SWE-Bench Verified', color='#4C72B0', edgecolor='white')
bars2 = ax.bar(x + width/2, pro, width, label='SWE-Bench Pro (harder)', color='#DD8452', edgecolor='white')

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_ylabel('Score (%)', fontsize=13)
ax.set_title('SWE-Bench Verified vs Pro: The Benchmark Inflation Gap\n(Same models, different harnesses)', fontsize=13, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(models3, fontsize=10)
ax.set_ylim(0, 105)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig(f'{VISUALS}/swe-bench-verified-vs-pro.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: swe-bench-verified-vs-pro.png")

# ─────────────────────────────────────────────────
# 4. AI Startup Funding — May 2026
# ─────────────────────────────────────────────────
companies = ["OpenRouter\n(Series B)", "Commure\nHealthcare AI", "Dust\nEnterprise Agents", "Perceptic\nDrug Discovery"]
funding = [113, 70, 40, 12]
colors4 = ['#4C72B0', '#55A868', '#DD8452', '#8172B3']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(companies, funding, color=colors4, edgecolor='white', linewidth=0.8, width=0.5)
for bar, val in zip(bars, funding):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f'${val}M', ha='center', va='bottom', fontsize=13, fontweight='bold')
ax.set_ylabel('Funding ($M)', fontsize=13)
ax.set_title('AI Startup Funding Rounds — Week of May 19–26, 2026', fontsize=14, fontweight='bold')
ax.set_ylim(0, 140)
ax.tick_params(axis='x', labelsize=11)
plt.tight_layout()
plt.savefig(f'{VISUALS}/ai-funding-may2026.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: ai-funding-may2026.png")

# ─────────────────────────────────────────────────
# 5. Anthropic May 2026 Commitments
# ─────────────────────────────────────────────────
labels5 = ["SpaceX Compute\n(3-year total)", "SpaceX Compute\n(annual run rate)", "Gates Foundation\nPartnership", "Project Glasswing\nCredits"]
values5 = [45, 15, 0.2, 0.1]
colors5 = ['#C44E52', '#DD8452', '#55A868', '#4C72B0']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels5[::-1], values5[::-1], color=colors5[::-1], edgecolor='white', linewidth=0.8)
for bar, val in zip(bars, values5[::-1]):
    label = f'${val}B'
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            label, va='center', ha='left', fontsize=12, fontweight='bold')
ax.set_xlabel('Value ($B)', fontsize=13)
ax.set_title('Anthropic May 2026 Commitments & Deals\n(Announced spending obligations and partnership values)', fontsize=13, fontweight='bold')
ax.set_xlim(0, 55)
ax.tick_params(axis='y', labelsize=11)
plt.tight_layout()
plt.savefig(f'{VISUALS}/anthropic-commitments.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: anthropic-commitments.png")

# ─────────────────────────────────────────────────
# 6. Nemotron Inference Throughput (tokens/sec)
# ─────────────────────────────────────────────────
modes = ["AR (baseline)", "FastDiffuser", "LinearSpec", "QuadSpec (est.)"]
tps = [215, 560, 865, 1375]
colors6 = ['#777777', '#55A868', '#4C72B0', '#C44E52']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(modes, tps, color=colors6, edgecolor='white', linewidth=0.8, width=0.5)
for bar, val in zip(bars, tps):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15,
            f'{val} t/s', ha='center', va='bottom', fontsize=12, fontweight='bold')
ax.set_ylabel('Tokens / Second', fontsize=13)
ax.set_title('NVIDIA Nemotron-Labs-Diffusion-8B — Inference Throughput\n(NVIDIA B200, batch=1, SGLang)', fontsize=13, fontweight='bold')
ax.set_ylim(0, 1600)
ax.tick_params(axis='x', labelsize=11)
plt.tight_layout()
plt.savefig(f'{VISUALS}/nemotron-throughput.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: nemotron-throughput.png")

# ─────────────────────────────────────────────────
# 7. HarmBench Jailbreak Success Rate
# ─────────────────────────────────────────────────
models7 = ["Grok 3 Mini", "Gemini 2.5 Pro", "Claude 4 Sonnet", "ChatGPT o4 Mini"]
rates7 = [100, 99, 94, 94]
colors7 = ['#C44E52', '#DD8452', '#8172B3', '#4C72B0']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(models7[::-1], rates7[::-1], color=colors7[::-1], edgecolor='white', linewidth=0.8)
for bar, val in zip(bars, rates7[::-1]):
    ax.text(bar.get_width() - 3, bar.get_y() + bar.get_height()/2,
            f'{val}%', va='center', ha='right', fontsize=13, fontweight='bold', color='white')
ax.set_xlabel('Attack Success Rate (%)', fontsize=13)
ax.set_title('Chain-of-Thought Hijacking: HarmBench Success Rates\n(Black-box "refusal dilution" attack on frontier LRMs — arXiv:2510.26418)', fontsize=13, fontweight='bold')
ax.set_xlim(0, 110)
ax.axvline(x=90, color='red', linestyle='--', alpha=0.4, linewidth=1.5, label='90% threshold')
ax.legend(fontsize=10)
ax.tick_params(axis='y', labelsize=12)
plt.tight_layout()
plt.savefig(f'{VISUALS}/harmbench-jailbreak.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: harmbench-jailbreak.png")

# ─────────────────────────────────────────────────
# 8. LMSys Arena Overall ELO
# ─────────────────────────────────────────────────
models8 = [
    "claude-opus-4-6-thinking", "claude-opus-4-7-thinking", "claude-opus-4-6",
    "claude-opus-4-7", "muse-spark (Meta)", "gemini-3.1-pro-preview",
    "gemini-3-pro", "gpt-5.5-high", "grok-4.20-beta1", "gpt-5.4-high",
    "gpt-5.5", "gemini-3-flash", "ernie-5.1 (Baidu)", "glm-5.1 (Zhipu)", "qwen3.5-max-preview"
]
elos = [1502, 1501, 1498, 1492, 1491, 1490, 1486, 1484, 1479, 1479, 1476, 1474, 1473, 1471, 1465]
colors8 = []
for m in models8:
    if 'claude' in m.lower():
        colors8.append('#DD8452')
    elif 'gpt' in m.lower():
        colors8.append('#4C72B0')
    elif 'gemini' in m.lower():
        colors8.append('#55A868')
    elif 'grok' in m.lower():
        colors8.append('#C44E52')
    else:
        colors8.append('#8172B3')

sorted_pairs8 = sorted(zip(elos, models8, colors8))
s_elos, s_models8, s_colors8 = zip(*sorted_pairs8)

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(s_models8, s_elos, color=s_colors8, edgecolor='white', linewidth=0.5)
for bar, elo in zip(bars, s_elos):
    ax.text(elo + 0.3, bar.get_y() + bar.get_height()/2,
            f'{elo}', va='center', ha='left', fontsize=9, fontweight='bold')
ax.set_xlabel('ELO Score', fontsize=13)
ax.set_title('LMSys Chatbot Arena — Overall ELO\n(May 14, 2026 snapshot)', fontsize=14, fontweight='bold')
ax.set_xlim(1455, 1520)
ax.tick_params(axis='y', labelsize=8.5)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#DD8452', label='Anthropic'),
    Patch(facecolor='#4C72B0', label='OpenAI'),
    Patch(facecolor='#55A868', label='Google'),
    Patch(facecolor='#C44E52', label='xAI'),
    Patch(facecolor='#8172B3', label='Other'),
]
ax.legend(handles=legend_elements, fontsize=9, loc='lower right')
plt.tight_layout()
plt.savefig(f'{VISUALS}/lmsys-arena-elo.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved: lmsys-arena-elo.png")

print("\nAll charts generated successfully.")
