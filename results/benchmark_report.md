# Timo Decision Benchmark (TDB) - Technical Evaluation Report

> **Research Question**: *Can a small, specialized decision model outperform generalized frontier LLMs on fiduciary consumer purchasing decisions, while reducing inference costs by >90% without over-correcting?*  
> **Production Live System**: [TimoBuy (https://timobuy.com/demo)](https://timobuy.com/demo)  
> **Dataset**: 50 Multi-Category High-Stakes Consumer Scenarios (`datasets/scenarios_50.json`)  
> **Methodology Guide**: [`datasets/LABELING_GUIDE.md`](../datasets/LABELING_GUIDE.md)

---

## 1. Executive Summary & Benchmark Results

Most commercial AI shopping assistants optimize for **GMV (Gross Merchandise Value)** and affiliate conversion. When a user asks *"Should I upgrade my M1 Pro to M3 Pro?"*, unconstrained LLMs enthusiastically recite new GPU specs, encouraging a \$2,000 checkout.

In consumer fiduciary decisions, however, the highest-utility answer is frequently **KEEP**, **WAIT**, **REPAIR**, or **SKIP**.

We evaluated four architectures across 50 verified consumer dilemmas ($n=50$, Wilson Score 95% CI $[86.5\%, 98.9\%]$):

| Architecture / Model | Decision Accuracy (%) | Fiduciary Restraint Rate (%) | Over-Reject Rate (False Negatives)* | Median Latency (ms) | Cost / 1k Decisions (USD) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Rule-Based Router (Retail Baseline)** | 38.0% | 6.1% | 0.0% | **4.2 ms** | **$0.01** |
| **Heavy General LLM (Raw Frontier 70B+)** | 76.0% | 63.6% | 0.0% | 820.0 ms | $15.00 |
| **Frontier 70B+ (w/ Fiduciary System Prompt)** *(Ablation)* | 88.0% | **93.9%** | **23.5% (4/17)** | 840.0 ms | $15.50 |
| **Timo Decoupled Decision Architecture** | **96.0%** | **93.9%** | **0.0% (0/17)** | **48.0 ms** | **$0.45** |

*\* **Over-Reject Rate (False Negatives)**: The percentage of cases with genuine physical failure/OOM blockers where the system incorrectly advised the user NOT to purchase.*

---

## 2. The Ablation Study: Why Prompt Engineering Alone Fails

A common and reasonable criticism from AI engineers is:
> *"What if you simply give the 70B frontier model a strict fiduciary system prompt: 'You are a fiduciary advisor. Protect the user's money at all costs'?"*

We ran this exact ablation experiment:
1. **The Positive**: Fiduciary restraint jumped from 63.6% to 93.9%. The model successfully stopped hyping \$1,200 audiophile cables (TB-010) and incremental luxury watches (TB-038).
2. **The "Austerity Trap" (23.5% False Negatives)**:
   - When told to be ultra-conservative, the frontier LLM began rejecting legitimate physical upgrade necessities.
   - In **Scenario TB-002** (fine-tuning 70B LLMs locally on an Intel laptop with 16GB RAM), it incorrectly advised the user to `KEEP` their existing laptop and "use Google Colab free tier", ignoring the user's explicit local offline constraint.
   - In **Scenario TB-026** (an Ironman 70.3 athlete whose Apple Watch dies after 4.5 hours), it advised `KEEP` and suggested "pausing the watch at water stations".
3. **The Economic Barrier**: System prompt engineering did not reduce token consumption or inference round-trips. Latency remained above 800ms, and cost was still **\$15.50 / 1,000 decisions**—34x more expensive than specialized models.

---

## 3. Decision Model Bake-Off: Clef-omni vs. Jev vs. Strands

Rather than treating the decision model as a black box, we conducted a bake-off among specialized small decision models (detailed in [`docs/decision_model_bakeoff.md`](../docs/decision_model_bakeoff.md)):

| Dimension | Clef-omni (1.8B) | Jev Decision Engine (0.8B) | Strands Decider (3.2B) | Frontier LLM (70B+) |
| :--- | :---: | :---: | :---: | :---: |
| **Model Size** | 1.8B Params | 0.8B Params | 3.2B Params | ~70B+ (API) |
| **P50 / P99 Latency** | **42ms / 68ms** | **18ms / 31ms** | 85ms / 140ms | 820ms / 1450ms |
| **Cost / 1k Queries** | **$0.38** | **$0.12** | $0.85 | $15.00 |
| **Hardware Constraint Adherence** | 94.0% (47/50) | 84.0% (42/50) | **96.0% (48/50)** | 76.0% (Raw) |
| **Over-Correction Rate** | **0.0%** | 11.8% | **0.0%** | 23.5% (Prompted) |

### Key Insight
- **Jev (0.8B)** is blistering fast (18ms) but struggles with mechanical multi-hop reasoning (e.g. confusing espresso extraction channels with pump failure).
- **Clef-omni (1.8B)** strikes the optimal balance between serverless edge deployment envelopes and nuanced constraint fidelity without false negatives.
- **Strands Decider (3.2B)** provides the highest raw reasoning fidelity among SLMs, but with 2.2x higher hosting resource requirements.

---

## 4. Reproducing Results

Run the full evaluation harness directly:
```bash
# Run simulated benchmark with ablation suite
python evaluator/run_benchmark.py

# Or test live against your own OpenAI/Ollama/vLLM endpoint
python evaluator/run_benchmark.py --live --model gpt-4o-mini --api-key $OPENAI_API_KEY
```

For interactive testing in production, visit the live playground at **[TimoBuy Demo (timobuy.com/demo)](https://timobuy.com/demo)**.
