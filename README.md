# Timo Decision Benchmark (TDB)

[![Live Demo](https://img.shields.io/badge/Production%20Live%20Demo-TimoBuy.com-0f172a?style=for-the-badge&logo=safari&logoColor=white)](https://timobuy.com)
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

## 📊 Benchmark Results

We tested **50 high-stakes consumer scenarios** across computing, outdoor gear, kitchen appliances, ergonomic furniture, cameras, home audio, and mobile devices:

| Architecture / Model | Overall Accuracy | Fiduciary Restraint Rate* | Median Latency | Cost / 1k Decisions |
| :--- | :---: | :---: | :---: | :---: |
| **Rule-Based Router (Retail Baseline)** | 38.0% | 6.1% | **4.2 ms** | **$0.01** |
| **Heavy General LLM (Frontier 70B+)** | 76.0% | 63.6% | 820.0 ms | $15.00 |
| **Timo Fiduciary Decision Architecture** | **96.0%** | **93.9%** | **48.0 ms** | **$0.45** |

*\* **Fiduciary Restraint Rate**: Percentage of non-essential purchase cases where the system correctly advised `KEEP`, `WAIT`, `REPAIR`, or `SKIP` instead of pushing an unnecessary purchase.*

### Key Takeaway
Specialized decision architectures trained and constrained for buyer-side fiduciary duty achieve **higher decision accuracy than frontier models** while slashing inference costs by **33x** and latency by **17x**.

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
│   └── scenarios_50.json     # 50 verified consumer decision scenarios with ground truth
├── evaluator/
│   └── run_benchmark.py      # Independent evaluator script (zero heavy dependencies)
├── results/
│   ├── benchmark_report.md   # In-depth technical breakdown and case studies
│   └── latest_run.json       # Machine-readable output from latest evaluation
├── LICENSE                   # MIT License
└── README.md                 # Project documentation & findings
```

---

## ⚡ Quick Start (Reproduce in 60 Seconds)

The benchmark harness is lightweight and runs out of the box using Python standard library:

```bash
# Clone the repository
git clone https://github.com/TimoBuy/timo-decision-benchmark.git
cd timo-decision-benchmark/evaluator

# Run the benchmark
python run_benchmark.py
```

Sample output:
```text
================================================================================
  TIMO DECISION BENCHMARK (TDB) - PRODUCTION SUITE
  Dataset: ../datasets/scenarios_50.json (50 Scenarios)
  Live Demo: https://timobuy.com
================================================================================

Architecture / Model                     | Accuracy   | Fiduciary %  | Latency    | Cost / 1k 
------------------------------------------------------------------------------------------
Rule-Based Router (Retail Baseline)      |     38.0% |        6.1% |     4.2ms | $    0.01
Heavy General LLM (Frontier 70B+)        |     76.0% |       63.6% |   820.0ms | $   15.00
Timo Fiduciary Decision Architecture     |     96.0% |       93.9% |    48.0ms | $    0.45
==========================================================================================
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

## 🌐 Try the Live Experience

Experience how this decision philosophy works in a real consumer product:

👉 **[Launch TimoBuy (timobuy.com)](https://timobuy.com)**  
*Ask any purchase question: "Should I buy X?", "Is Y worth upgrading?", "How do I fix Z?"*

---

## 🤝 Contributing

We welcome community contributions! You can:
1. Submit real-world edge cases to `datasets/scenarios_50.json`.
2. Add new model adapters to `evaluator/run_benchmark.py` (e.g., custom local quantized models, specialized small language models).

Please open an issue or pull request.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.  
Maintained by the **TimoBuy Research Team** ([https://timobuy.com](https://timobuy.com)).
