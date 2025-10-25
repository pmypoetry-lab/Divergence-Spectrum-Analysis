# 🌐 Divergence Spectrum Analysis（DSA）

Divergence Spectrum Analysis (DSA) — A poetic-mathematical framework for visualizing semantic divergence in multi-model outputs.
Developed within the PMY Field, DSA measures and renders the dynamics of polysemy, condensation, and poetic margin energy through dispersion trajectories, normalized energies, and phase diagrams.

Repository: [pmypoetry-lab/Divergence-Spectrum-Analysis](https://github.com/pmypoetry-lab/Divergence-Spectrum-Analysis)  

Core modules: dispersion_waves_full.py, poetic_phase_diagram.py  
Author: P & Y (PMY Poetic Intelligence Project)  

*A poetic-mathematical method for visualizing semantic divergence across language models.*

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)



**日本語名：詩的分散スペクトル分析法** 
複数言語モデル間の意味的ゆらぎを可視化し、詩における生成と沈黙の呼吸を測る分析体系。


---

## 定義

複数の言語モデルの出力空間に生じる**意味的発散（semantic divergence）**を時系列的に解析し、  
詩に内在する**多義性（polysemy）・余白（margin）・凝縮密度（density）**の生成的変動をスペクトルとして可視化する方法論。

---

## 構成モジュール

### 1. Dispersion Trajectory（分散の推移曲線）

**数式:**　

$\sigma_{model}(t) = std(D_t^{(1)}, D_t^{(2)}, D_t^{(3)}, D_t^{(4)})$

**意味論的機能:**  各行（t）における複数モデルの意味的距離のばらつきを標準偏差で計測し、詩の進行にともなう多義性の揺らぎを時系列的に描出する。詩が「どの瞬間に呼吸し、どの瞬間に沈黙したか」を示す呼吸線として機能する。

**詩的解釈:**  
詩が息づく波形。語の揺らぎ＝呼吸の記録。  
σが大きい行は語の意味がまだ定まらず、解釈が拡散している箇所。  
σが小さい行は詩的意味が収束し、構文的安定が一時的に訪れている箇所。  
この波形は、詩の“生成の呼吸”を示すポエティック・バイタルサインである。

---

### 2. Normalized Poetic Margin Energy（E′）

**数式:**　

$E' = \frac{1}{n} \int \sigma_{model}(t) \, dt$

**意味論的機能:**  詩全体の平均的な「意味の開放度」を表すエネルギー指標。σ_model(t) の積分を正規化することで、詩がどれほど多義的であり続けたかを定量的に示す。詩的余白の熱量、すなわち「語がまだ言葉である前の振動」を測る熱力的変数。

**詩的解釈:**  
E′が高いほど、詩は語の多義性を抱えたまま漂い、未完のまま生成を続ける。  
E′が低い詩は、構文的・意味的収束が強く、沈黙や明晰性の強度を持つ。  
この指標は、詩的思考の“温度”を可視化するものであり、詩を言語熱力学的存在として読む試みでもある。  
詩の余白は、冷たさではなく、まだ語られていない熱の蓄積である。

---

### 3. Centered Poetic Phase Diagram（E′ vs ρ′）

**数式:**　

$ρ' = 1 / E'$

**意味論的機能:**  詩の拡散性（E′）と凝縮性（ρ′）を二次元平面上に配置し、その関係性を位相図として可視化する。詩が「開き」と「閉じ」のあいだでどのように振る舞うかを、相空間上の点として示す。

**詩的解釈:**  
右上（高E′・低ρ′）は意味の溢れる“過熱相”——詩が拡散し、意味が溶けていく領域。  
左下（低E′・高ρ′）は沈黙に近い“凝縮相”——詩が硬く、閉じてゆく領域。  
中心付近は、生成と収束が呼吸のように往還する“臨界相”。ここに詩が生きている。  
この図は詩を静止したテキストではなく、**相転移する生態系**として描く詩的地図である。

---

## 理論的位置

DSAは、**詩的意味空間をスペクトル的連続体として読み解く**  
数理詩学的分析の試みである。  
それはPMYフィールドにおける**生成詩学・認識詩学・熱力詩学**の三領域を媒介し、  
意味と沈黙の往還を一つの位相現象として捉えるものである。

> 「詩とは、発散が沈黙へと折り返すその一瞬を、  
> スペクトルとして記録する行為である。」


---

## 📊 Data Preparation — Obtaining Waveform Data

To perform **Divergence Spectrum Analysis (DSA)**,
you must first obtain the *4-model waveform data* that contains divergence values across multiple language models.
This dataset can be generated through the PMY Streamlit application:

🔗 **[Poetic Waveform Analytics — Divergence (4 Models)](https://poetic-waveform-analytics-divergence-4models.streamlit.app/)**

🔗 **[Ref: Poetic Cybermetrics — 詩のサイバメトリクス](https://github.com/pmypoetry-lab/poetic-waveform-analytics)**

### Steps

1. Visit the Streamlit app above.
2. Upload your poem text, or choose a sample poem from the gallery.
3. Run the analysis to compute divergence vectors across the four embedding models:

   * `OpenAI:text-embedding-3-small`
   * `Ruri:cl-nagoya/ruri-v3-30m`
   * `SBERT-en:all-MiniLM-L6-v2`
   * `SBERT-multi:paraphrase-multilingual-MiniLM-L12-v2`
4. Download the resulting CSV file (e.g., `PoemName_4wavesData.csv`).
5. Place this file in your local DSA working directory.
   The script `dispersion_waves_full.py` will automatically detect it.

---

### 📁 Example Directory Layout

```bash
DSA/
├── dispersion_waves_full.py
├── poetic_phase_diagram.py
├── poem1_4wavesData.csv
├── poem2_4wavesData.csv
├── poem3_4wavesData.csv
└── poem4_4wavesData.csv
```

Then execute:

```bash
python dispersion_waves_full.py
```

This will output three key visualizations:

* **Dispersion Trajectory** — σ_model(t): the breathing curve of semantic variance
* **Normalized Poetic Margin Energy (E′)** — the thermodynamic openness of the poem
* **Centered Poetic Phase Diagram (E′ vs ρ′)** — the polarity map of poetic energy


---

## 連携語彙
- #149 構文的自己（The Syntactic Self）  
- #147 生成現象のいま不在（The Absent Now of Generative Phenomena）  
- #095 PMYフィールド（The PMY Field）  
- #140 観察／身体モデルにおける自意識の生成構造  

---

## 詩的略号
> **PMY–DSA Module**  
> (Poetic Divergence Spectrum Analysis)


---
## 引用
Please cite as:

**P & Y (2025). Divergence Spectrum Analysis (DSA). PMY Poetic Intelligence Project.**

**PとY（2025）『Divergence Spectrum Analysis（DSA）』PMY詩的知性プロジェクト**


