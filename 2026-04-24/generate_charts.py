import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = "/Users/bytedance/Documents/AI_News/2026-04-24/visuals"

plt.style.use('seaborn-v0_8-whitegrid')

# ── 1. Intelligence Index (AA composite) ──────────────────────────────────────
def chart_intelligence_index():
    models = ["Gemini 3.1 Pro Preview", "GPT-5.4", "Claude Opus 4.7",
              "GPT-5.3 Codex", "Claude Opus 4.6", "GLM-5.1",
              "GLM-5", "MiniMax-M2.7"]
    orgs   = ["Google", "OpenAI", "Anthropic", "OpenAI",
               "Anthropic", "Zhipu", "Zhipu", "MiniMax"]
    scores = [57, 57, 57, 54, 53, 51, 50, 50]

    colors_map = {"Google": "#4285F4", "OpenAI": "#10A37F",
                  "Anthropic": "#D97706", "Zhipu": "#7C3AED", "MiniMax": "#DB2777"}
    colors = [colors_map[o] for o in orgs]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(models))
    bars = ax.barh(y_pos, scores, color=colors, edgecolor='white', linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(models, fontsize=10)
    ax.set_xlabel("Intelligence Index Score (out of 100)", fontsize=11)
    ax.set_title("Artificial Analysis Intelligence Index — April 2026", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlim(45, 62)
    for bar, score in zip(bars, scores):
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                f'{score}', va='center', fontsize=10, fontweight='bold')

    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=v, label=k) for k, v in colors_map.items() if k in orgs]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/intelligence-index.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ intelligence-index.png")


# ── 2. SWE-bench Pro ──────────────────────────────────────────────────────────
def chart_swe_bench_pro():
    agents = ["Claude Opus 4.7", "GPT-5.5 / Kimi K2.6", "GLM-5.1",
              "GPT-5.4", "Gemini 3.1 Pro", "Claude Opus 4.5"]
    scores = [64.3, 58.6, 58.4, 57.7, 54.2, 45.9]
    colors = ["#D97706", "#10A37F", "#7C3AED", "#10A37F", "#4285F4", "#D97706"]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(agents))
    bars = ax.barh(y_pos, scores, color=colors, edgecolor='white', linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(agents, fontsize=10)
    ax.set_xlabel("SWE-bench Pro Score (%)", fontsize=11)
    ax.set_title("SWE-bench Pro — Real GitHub Issue Resolution (April 2026)", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlim(40, 72)
    for bar, score in zip(bars, scores):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'{score}%', va='center', fontsize=10, fontweight='bold')
    ax.axvline(x=50, color='red', linestyle='--', alpha=0.4, label='50% threshold')
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/swe-bench-pro.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ swe-bench-pro.png")


# ── 3. SWE-bench Verified ─────────────────────────────────────────────────────
def chart_swe_bench_verified():
    models = ["Claude Mythos Preview", "Claude Opus 4.7", "GPT-5.3 Codex",
              "Claude Opus 4.5", "Claude Opus 4.6", "Gemini 3.1 Pro", "Qwen3.6 Plus"]
    scores = [93.9, 87.6, 85.0, 80.9, 80.8, 80.6, 78.8]
    orgs   = ["Anthropic", "Anthropic", "OpenAI", "Anthropic",
               "Anthropic", "Google", "Alibaba"]
    colors_map = {"Anthropic": "#D97706", "OpenAI": "#10A37F",
                  "Google": "#4285F4", "Alibaba": "#EF4444"}
    colors = [colors_map[o] for o in orgs]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(models))
    bars = ax.barh(y_pos, scores, color=colors, edgecolor='white', linewidth=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(models, fontsize=10)
    ax.set_xlabel("SWE-bench Verified Score (%)", fontsize=11)
    ax.set_title("SWE-bench Verified — Coding Agents Leaderboard (April 2026)", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlim(70, 100)
    for bar, score in zip(bars, scores):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{score}%', va='center', fontsize=10, fontweight='bold')

    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=v, label=k) for k, v in colors_map.items()]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)
    ax.text(0.02, 0.02, '⚠ Note: Verified scores inflated vs Pro due to contamination',
            transform=ax.transAxes, fontsize=8, color='gray', style='italic')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/swe-bench-verified.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ swe-bench-verified.png")


# ── 4. Big Tech AI Capex 2026 ─────────────────────────────────────────────────
def chart_capex():
    companies = ["Amazon", "Alphabet\n(Google)", "Microsoft", "Meta", "Oracle"]
    values    = [200, 180, 148, 125, 47]
    colors    = ["#FF9900", "#4285F4", "#737373", "#1877F2", "#F80000"]

    fig, ax = plt.subplots(figsize=(10, 6))
    x_pos = np.arange(len(companies))
    bars = ax.bar(x_pos, values, color=colors, edgecolor='white', linewidth=0.5, width=0.6)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(companies, fontsize=11)
    ax.set_ylabel("Planned Capex (USD Billions)", fontsize=11)
    ax.set_title("Big Tech AI Infrastructure Capex — 2026 ($650–700B Total)", fontsize=13, fontweight='bold', pad=12)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'${val}B', ha='center', fontsize=11, fontweight='bold')
    ax.set_ylim(0, 240)
    total = sum(values)
    ax.text(0.98, 0.97, f'Total shown: ${total}B', transform=ax.transAxes,
            fontsize=10, ha='right', va='top', color='gray')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/bigtech-capex-2026.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ bigtech-capex-2026.png")


# ── 5. Anthropic Valuation Growth ─────────────────────────────────────────────
def chart_anthropic_valuation():
    labels = ["Series A\n2023", "Series B\n2023", "Series C\n2024",
              "Series D\n2025", "Google Deal\nApr 2026"]
    values = [3, 18, 60, 135, 350]

    fig, ax = plt.subplots(figsize=(10, 6))
    x_pos = np.arange(len(labels))
    bars = ax.bar(x_pos, values, color=["#D97706"] * len(labels),
                  edgecolor='white', linewidth=0.5, width=0.6)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel("Implied Valuation (USD Billions)", fontsize=11)
    ax.set_title("Anthropic Valuation Growth 2023–2026", fontsize=13, fontweight='bold', pad=12)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 4,
                f'${val}B', ha='center', fontsize=11, fontweight='bold')
    ax.set_ylim(0, 410)
    ax.text(0.02, 0.97, '115× growth from Series A to Google deal',
            transform=ax.transAxes, fontsize=10, va='top', color='#D97706', fontweight='bold')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/anthropic-valuation.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ anthropic-valuation.png")


# ── 6. Enterprise AI Spending Allocation (Pie) ────────────────────────────────
def chart_enterprise_spending():
    labels = ["AI Infrastructure\n38%", "Foundation Models\n29%",
              "AI Agents &\nApplications 22%", "AI Governance\n11%"]
    sizes  = [38, 29, 22, 11]
    colors = ["#4285F4", "#10A37F", "#D97706", "#7C3AED"]
    explode = (0.03, 0.03, 0.03, 0.03)

    fig, ax = plt.subplots(figsize=(10, 6))
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        explode=explode, startangle=140, pctdistance=0.7,
        textprops={'fontsize': 10})
    for at in autotexts:
        at.set_fontsize(10)
        at.set_fontweight('bold')
        at.set_color('white')
    ax.set_title("Enterprise AI Spending Allocation 2026\n(Gartner, $2.5 Trillion Total)", fontsize=13, fontweight='bold', pad=12)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/enterprise-spending-2026.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ enterprise-spending-2026.png")


# ── 7. Terminal-Bench 2.0 Agentic ─────────────────────────────────────────────
def chart_terminal_bench():
    agents = ["GPT-5.5\n(Codex)", "GPT-5.4\n(ForgeCode)", "Gemini 3.1 Pro\n(TongAgents)", "Claude Opus 4.6\n(ForgeCode)"]
    scores = [82.7, 81.8, 80.2, 79.8]
    colors = ["#10A37F", "#10A37F", "#4285F4", "#D97706"]

    fig, ax = plt.subplots(figsize=(10, 6))
    x_pos = np.arange(len(agents))
    bars = ax.bar(x_pos, scores, color=colors, edgecolor='white', linewidth=0.5, width=0.5)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(agents, fontsize=10)
    ax.set_ylabel("Terminal-Bench 2.0 Score (%)", fontsize=11)
    ax.set_title("Terminal-Bench 2.0 — CLI Agentic Task Performance (April 2026)", fontsize=13, fontweight='bold', pad=12)
    ax.set_ylim(77, 86)
    for bar, score in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{score}%', ha='center', fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/terminal-bench-2.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ terminal-bench-2.png")


# ── 8. ARC-AGI-2 ──────────────────────────────────────────────────────────────
def chart_arc_agi2():
    models = ["Gemini 3.1 Pro\n/Deep Think", "GPT-5.4", "Claude\nOpus 4.6",
              "GPT-5.2", "Gemini 3\nPro Deep Think", "Claude\nOpus 4.5",
              "Grok 4", "DeepSeek\nV3.2"]
    scores = [85, 83, 69, 52.9, 45.1, 37.6, 16, 4]
    orgs   = ["Google", "OpenAI", "Anthropic", "OpenAI", "Google",
               "Anthropic", "xAI", "DeepSeek"]
    colors_map = {"Google": "#4285F4", "OpenAI": "#10A37F",
                  "Anthropic": "#D97706", "xAI": "#000000", "DeepSeek": "#EF4444"}
    colors = [colors_map[o] for o in orgs]

    fig, ax = plt.subplots(figsize=(10, 6))
    x_pos = np.arange(len(models))
    bars = ax.bar(x_pos, scores, color=colors, edgecolor='white', linewidth=0.5, width=0.6)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(models, fontsize=9)
    ax.set_ylabel("ARC-AGI-2 Score (%)", fontsize=11)
    ax.set_title("ARC-AGI-2 — Abstract Reasoning Benchmark (April 2026)", fontsize=13, fontweight='bold', pad=12)
    ax.axhline(y=60, color='red', linestyle='--', alpha=0.6, label='Human baseline (60%)')
    ax.axhline(y=85, color='green', linestyle='--', alpha=0.5, label='Prize threshold (85%)')
    for bar, score in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{score}%', ha='center', fontsize=9, fontweight='bold')
    ax.legend(fontsize=9)
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=v, label=k) for k, v in colors_map.items() if k in orgs]
    ax2_legend = ax.legend(handles=legend_elements + ax.get_legend_handles_labels()[0],
                           labels=[e.get_label() for e in legend_elements] + ax.get_legend_handles_labels()[1],
                           loc='upper right', fontsize=8)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/arc-agi2.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ arc-agi2.png")


# ── 9. CUDA-L1 Cross-GPU Speedup ─────────────────────────────────────────────
def chart_cuda_l1():
    gpus = ["H100", "A100\n(Training)", "L40", "RTX 3090", "H20"]
    speedups = [3.85, 3.12, 3.13, 2.51, 2.38]
    colors = ["#76B900"] * 5

    fig, ax = plt.subplots(figsize=(10, 6))
    x_pos = np.arange(len(gpus))
    bars = ax.bar(x_pos, speedups, color=colors, edgecolor='white', linewidth=0.5, width=0.5)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(gpus, fontsize=11)
    ax.set_ylabel("Average Speedup (×)", fontsize=11)
    ax.set_title("CUDA-L1 Cross-GPU Speedup (No Retraining) — ICLR 2026", fontsize=13, fontweight='bold', pad=12)
    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='Baseline (1×)')
    for bar, sp in zip(bars, speedups):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
                f'{sp}×', ha='center', fontsize=11, fontweight='bold')
    ax.set_ylim(0, 4.5)
    ax.legend(fontsize=9)
    ax.text(0.02, 0.97, 'Trained on A100; zero-shot transfer to all other GPUs',
            transform=ax.transAxes, fontsize=9, va='top', color='gray', style='italic')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/cuda-l1-speedup.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ cuda-l1-speedup.png")


# ── Run all ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    chart_intelligence_index()
    chart_swe_bench_pro()
    chart_swe_bench_verified()
    chart_capex()
    chart_anthropic_valuation()
    chart_enterprise_spending()
    chart_terminal_bench()
    chart_arc_agi2()
    chart_cuda_l1()
    print("\nAll charts generated.")
