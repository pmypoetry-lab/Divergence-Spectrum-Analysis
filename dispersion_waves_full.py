# -*- coding: utf-8 -*-
"""
Unified Poetic Divergence Analysis Script (4 poems)
---------------------------------------------------
Generates:
1. Dispersion Trajectory σ_model(t)
2. Normalized Poetic Margin Energy (E′)
3. Centered Poetic Phase Diagram (E′ vs ρ′)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Ⅰ. Load & compute σ_model(t)
# ===============================

MODEL_COLS = [
    "OpenAI:text-embedding-3-small",
    "Ruri:cl-nagoya/ruri-v3-30m",
    "SBERT-en:all-MiniLM-L6-v2",
    "SBERT-multi:paraphrase-multilingual-MiniLM-L12-v2"
]

def load_models_only(path):
    """Load only the 4 embedding columns and compute σ per line"""
    df_raw = pd.read_csv(path)
    df = df_raw[MODEL_COLS].apply(lambda col: pd.to_numeric(col, errors="coerce"))
    sigma = df.std(axis=1, ddof=1)
    return sigma

# Load four poems’ divergence data
mugen_sigma = load_models_only("MugenEn_4wavesData.csv")
poem2_sigma  = load_models_only("poem2_4wavesData.csv")
poem3_sigma   = load_models_only("poem3_4wavesData.csv")
poem4_sigma = load_models_only("poem4_4wavesData.csv")

# --- Dispersion Trajectory Plot ---
plt.figure(figsize=(10,5))
plt.plot(range(1, len(mugen_sigma)+1), mugen_sigma,
         label="MugenEn (Infinite Contact)", color="#1f77b4", alpha=0.9)
plt.plot(range(1, len(poem2_sigma)+1), poem2_sigma,
         label="poem2 (Alien/You/Experience)", color="#ff7f0e", alpha=0.9)
plt.plot(range(1, len(poem3_sigma)+1), poem3_sigma,
         label="poem3", color="#2ca02c", alpha=0.9)
plt.plot(range(1, len(poem4_sigma)+1), poem4_sigma,
         label="poem4 (Proof of Infinity)", color="#9467bd", alpha=0.9)

plt.title("Dispersion Trajectory — True Instantaneous σ_model(t)")
plt.xlabel("Line Number (Poetic Progression)")
plt.ylabel("σ_model(t) — Instantaneous Semantic Dispersion")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("dispersion_trajectory_TRUE_4poems.png")
plt.close()

# ===============================
# Ⅱ. Compute E′ and ρ′
# ===============================

E_norm = {
    "MugenEn": mugen_sigma.sum() / len(mugen_sigma),
    "poem2": poem2_sigma.sum() / len(poem2_sigma),
    "poem3": poem3_sigma.sum() / len(poem3_sigma),
    "poem4": poem4_sigma.sum() / len(poem4_sigma)
}
rho_norm = {name: 1 / E for name, E in E_norm.items()}

# --- Bar chart for E′ ---
plt.figure(figsize=(7,4))
bars=plt.bar(E_norm.keys(), E_norm.values(),
        color=["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"], alpha=0.8)
plt.ylabel("E′ (Normalized Poetic Margin Energy)\nMean Semantic Dispersion per Line")
plt.title("Normalized Poetic Margin Energy — Four Poems")

# --- ★ 各棒の上に E′値を表示 ---
for bar, value in zip(bars, E_norm.values()):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,   # 棒の中央
        height + 0.002,                      # 少し上
        f"{value:.3f}",                      # 小数3桁表示
        ha='center', va='bottom', fontsize=9, color='black'
    )

plt.tight_layout()
plt.savefig("poetic_margin_energy_TRUE_4poems.png")
plt.close()





# ===============================
# Ⅲ. Centered Poetic Phase Diagram
# ===============================

plt.figure(figsize=(7,6))
xs = list(E_norm.values())
ys = list(rho_norm.values())
labels = list(E_norm.keys())
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"]

for x, y, lab, c in zip(xs, ys, labels, colors):
    plt.scatter(x, y, color=c, s=140, alpha=0.85)
    plt.text(x * 1.01, y * 0.99, lab, fontsize=10)

plt.axhline(0, color="black", linewidth=1, alpha=0.7)
plt.axvline(0, color="black", linewidth=1, alpha=0.7)
plt.xlabel("E′ (Normalized Poetic Margin Energy)\nSemantic Dispersion per Line")
plt.ylabel("ρ′ = 1 / E′ (Normalized Poetic Condensation Density)")
plt.title("Centered Poetic Phase Diagram — Poetic Polarity Space (4 Poems)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("poetic_phase_diagram_centered_TRUE_4poems.png")
plt.close()

# ===============================
# Ⅳ. Print results
# ===============================

print("E′ values:", E_norm)
print("ρ′ values:", rho_norm)
print("\nOutput Files:")
print(" - dispersion_trajectory_TRUE_4poems.png")
print(" - poetic_margin_energy_TRUE_4poems.png")
print(" - poetic_phase_diagram_centered_TRUE_4poems.png")

