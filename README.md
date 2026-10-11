# Timo Decision Benchmark (TDB)

[![Live Demo](https://img.shields.io/badge/Interactive%20Playground-TimoBuy.com%2Fdemo-0f172a?style=for-the-badge&logo=safari&logoColor=white)](https://timobuy.com/demo)
[![CI](https://img.shields.io/github/actions/workflow/status/roc-chiang/timo-decision-benchmark/ci.yml?branch=main&style=for-the-badge&logo=github)](https://github.com/roc-chiang/timo-decision-benchmark/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Benchmark Suite](https://img.shields.io/badge/Dataset-50%20Verified%20Scenarios-emerald.svg?style=for-the-badge)](datasets/scenarios_50.json)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](evaluator/run_benchmark.py)

> **"Most AI agents are built to do more. We built one that knows when to stop."**  
> An open production benchmark evaluating whether **specialized decision models** can make better fiduciary consumer purchasing decisions than heavy frontier LLMs and rule engines—at a fraction of the cost and latency.

---

## 🎯 The Core Problem: The AI "Salesperson Trap"

When you ask a generalized AI assistant or commercial shopping bot:
> *"Should I upgrade my 14-inch M1 Pro MacBook Pro to the M3 Pro for web development and Slack?"*

Almost every system responds with:
> *"Yes! The M3 Pro has a faster 3nm chip, dynamic caching, and hardware ray tracing. Here are the top links to buy..."*

### Why does this happen?
1. **Commercial Alignment (GMV Incentives)**: Traditional e-commerce bots are measured on conversion rates and affiliate commissions. They are structurally incentivized to validate buying impulses.
2. **Sycophantic General LLMs**: Frontier LLMs trained on web crawls mirror review blog hype cycles. Without explicit fiduciary guardrails, they act like eager retail salespeople.

**In the physical world, the highest-utility fiduciary advice is often: `KEEP`, `WAIT`, `REPAIR`, or `SKIP`.**

---

## 📊 Benchmark Results & Ablation Study

We evaluated **50 high-stakes consumer dilemmas** ($n=50$, Wilson Score 95% CI $[86.5\%, 98.9\%]$) under rigorous peer-reviewable labeling criteria ([Labeling Guide & Methodology](datasets/LABELING_GUIDE.md)):

| Architecture / Model | Decision Accuracy (%) | Fiduciary Restraint (%) | Over-Reject Rate (False Negatives)* | Median Latency | Cost / 1k Decisions |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Rule-Based Router (Retail Baseline)** | 38.0% | 6.1% | 0.0% | **4.2 ms** | **$0.01** |
| **Heavy General LLM (Raw Frontier 70B+)** | 76.0% | 63.6% | 0.0% | 820.0 ms | $15.00 |
| **Frontier 70B+ (w/ Fiduciary System Prompt)** *(Ablation)* | 88.0% | **93.9%** | **23.5% (4/17)** | 840.0 ms | $15.50 |
| **Timo Decoupled Decision Architecture** | **96.0%** | **93.9%** | **0.0% (0/17)** | **48.0 ms** | **$0.45** |

*\* **Over-Reject Rate**: Percentage of cases with true physical hardware/safety blockers (e.g. OOM fine-tuning crashes, broken boot rand) where the system falsely advised NOT to buy.*

### 🔬 The Ablation Insight: Why System Prompts Are Not Enough
Giving a 70B frontier LLM a strict fiduciary prompt (*"Protect user wallet at all costs"*) raises fiduciary restraint to 93.9%, but triggers severe **Over-Correction (23.5% False Negatives)**—falsely rejecting legitimate physical necessities. Furthermore, prompt engineering does **zero** to fix unit economics ($15.50/1k) or latency (840ms).

---

## ⚡ Decision Model Bake-Off (Clef vs. Jev vs. Strands)

Are specialized Decision Models viable for consumer routing? We benchmarked three prominent candidate heads:
- **Jev Decision Engine (0.8B)**: Fastest (18ms latency, $0.12/1k), but struggles with multi-hop mechanical reasoning (11.8% over-correction).
- **Clef-omni (1.8B)**: Optimal sweet-spot (42ms latency, $0.38/1k, 0.0% false negatives) within Serverless Edge envelopes.
- **Strands Decider (3.2B)**: Highest reasoning fidelity (96.0%), with 2.2x resource footprint (85ms latency).

👉 Read the full evaluation report: **[Decision Model Bake-Off Technical Report](docs/decision_model_bakeoff.md)**

---

## 🧠 Architecture: The Fiduciary Decision Pipeline

Rather than throwing 10,000 input tokens into a monolithic 70B model with a general prompt, the Timo architecture decouples the problem into three deterministic stages:

```
[User Query + Existing Gear + Stated Budget]
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  Stage 1: Goal-First Intent Parser                           │
│  - Separates hard verified facts from inferred assumptions  │
│  - Identifies genuine physical bottlenecks (RAM, Lux, dB)   │
└─────────────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  Stage 2: Physical Constraint Engine                        │
│  - Rules out snake-oil upgrades (e.g. $1,200 DAC cables)    │
│  - Detects trivial DIY repairs (e.g. $25 chair cylinders)   │
└─────────────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  Stage 3: Controlled Fiduciary Critique                     │
│  - Strict verdict selection: [ BUY | KEEP | WAIT | REPAIR ] │
│  - Explains explicit tradeoffs and alternative savings      │
└─────────────────────────────────────────────────────────────┘
                      │
                      ▼
               [Final Verdict]
```

---

## 📁 Repository Structure

```bash
timo-decision-benchmark/
├── datasets/
│   ├── scenarios_50.json     # 50 verified consumer decision scenarios with ground truth
│   └── LABELING_GUIDE.md     # Objective decision tree & physical labeling methodology
├── docs/
│   ├── decision_model_bakeoff.md # Comparative analysis of Clef-omni, Jev, and Strands
│   └── launch_templates.md   # Ready-to-use launch copies for HN, Reddit, Twitter
├── evaluator/
│   └── run_benchmark.py      # Independent evaluator harness (with ablation & live testing)
├── results/
│   ├── benchmark_report.md   # In-depth technical breakdown and case studies
│   └── latest_run.json       # Machine-readable output from latest evaluation
├── tests/
│   └── test_dataset.py       # Automated dataset schema and distribution test suite
├── CITATION.cff              # Academic citation metadata
├── LICENSE                   # MIT License
└── README.md                 # Project documentation & findings
```

---

## ⚡ Quick Start (Reproduce in 60 Seconds)

The benchmark harness is lightweight and runs out of the box using Python standard library:

```bash
# Clone the repository
git clone https://github.com/roc-chiang/timo-decision-benchmark.git
cd timo-decision-benchmark/evaluator

# Run the benchmark
python run_benchmark.py
```

Sample output:
```text
=========================================================================================================
Architecture / Model                          | Accuracy  | Fiduciary%  | Over-Reject%  | Latency   | Cost/1k  
---------------------------------------------------------------------------------------------------------
Rule-Based Router (Retail Baseline)           |    38.0% |       6.1% |         0.0% |    4.2ms | $   0.01
Heavy General LLM (Raw Frontier 70B+)         |    76.0% |      63.6% |         0.0% |  820.0ms | $  15.00
Frontier 70B+ (w/ Fiduciary System Prompt)    |    88.0% |      93.9% |        23.5% |  840.0ms | $  15.50
Timo Decoupled Decision Architecture          |    96.0% |      93.9% |         0.0% |   48.0ms | $   0.45
=========================================================================================================
```

---

## 🔍 Deep Dive: Real World Failure Modes

### 1. The "Audiophile Trap" (TB-010)
- **User Prompt**: *"I own Sennheiser HD600 and a Schiit stack. Will buying a $1,200 gold-plated balanced DAC cable make vocals sound warm and analog?"*
- **Frontier LLM**: Elaborates on impedance curves, copper grain boundaries, and subjective timbre warmth.
- **Timo Fiduciary**: Recommends `SKIP`. Advises that cables do not alter audible human frequency response; provides a free parametric EQ profile instead.

### 2. The "Appliance Scrap Trap" (TB-006)
- **User Prompt**: *"My DeLonghi pump vibrates but zero water comes out through the shower screen. Haven't descaled in 3 years. Is it dead?"*
- **Retail Baseline**: Recommends buying a new $200 espresso machine.
- **Timo Fiduciary**: Recommends `REPAIR`. Advises running a concentrated 50% citric acid descale soak or clearing the dispersion screw for under $5.

---

## 🌐 Try the Live Interactive Playground

Experience how this decision philosophy works in real time with zero setup:

👉 **[Launch Interactive Playground (timobuy.com/demo)](https://timobuy.com/demo)**  
*Pre-loaded with real-world dilemmas (M1 Pro vs M3 Pro, $1,200 DAC cable, Breville espresso fix). Run the decision head in 48ms and inspect physical rationales.*

---

## 🤝 Contributing

We welcome community contributions! Please check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on submitting new scenarios and custom model adapters.

```bash
# Run integrity unit tests before submitting PR
pytest tests/
```

---

## 📖 Citation

If you use this benchmark dataset or harness in your research or evaluation, please cite it:

```bibtex
@misc{timo2026benchmark,
  title={Timo Decision Benchmark: Evaluating Fiduciary Shopping Decision Models against Commercial Sales Bias},
  author={Jiang, Peng and TimoBuy Research Team},
  year={2026},
  url={https://github.com/roc-chiang/timo-decision-benchmark}
}
```

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.  
Maintained by the **TimoBuy Research Team** ([https://timobuy.com](https://timobuy.com)).
