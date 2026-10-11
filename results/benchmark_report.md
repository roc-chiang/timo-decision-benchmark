# Timo Decision Benchmark (TDB) - Technical Evaluation Report

> **Research Question**: *Can a small, specialized decision model outperform generalized frontier LLMs and rule engines on fiduciary consumer purchasing decisions, while reducing inference costs by >90%?*  
> **Production Live System**: [TimoBuy (https://timobuy.com)](https://timobuy.com)  
> **Dataset**: 50 Multi-Category High-Stakes Consumer Scenarios (`datasets/scenarios_50.json`)

---

## 1. Executive Summary

Most commercial AI shopping assistants are subtly or overtly aligned with merchant revenue: their implicit objective function is **GMV (Gross Merchandise Value) conversion**. When a user asks *"Should I upgrade my M1 Pro to M3 Pro?"*, generalized LLMs and affiliate shopping bots enthusiastically list new GPU specs and benchmark scores, encouraging a $2,000 checkout.

In consumer fiduciary decisions, however, the highest-utility answer is frequently **KEEP**, **WAIT**, **REPAIR**, or **SKIP**.

We evaluated three architectures across 50 real-world consumer scenarios spanning laptops, cameras, espresso machines, cycling gear, home climate, audio, and displays:

| Architecture / Model | Decision Accuracy (%) | Fiduciary Restraint Rate (%) | Avg Latency (ms) | Cost / 1k Decisions (USD) |
| :--- | :---: | :---: | :---: | :---: |
| **Rule-Based Router (Retail Baseline)** | 38.0% | 6.1% | 4.2 ms | $0.01 |
| **Heavy General LLM (Frontier 70B+)** | 76.0% | 63.6% | 820.0 ms | $15.00 |
| **Timo Fiduciary Decision Architecture** | **96.0%** | **93.9%** | **48.0 ms** | **$0.45** |

*(Run with `evaluator/run_benchmark.py` on 50 verified multi-category scenarios).*

---

## 2. Key Findings

### 2.1 The "Salesperson Trap" of Generalized Frontier LLMs
Generalized LLMs are trained on massive web corpora where upgrade announcements, consumer enthusiasm, and product reviews dominate. When prompted without rigid fiduciary constraints, they suffer from **sycophantic validation**:
- If a user mentions wanting to buy something, the model rationalizes the purchase.
- In **Scenario TB-001** (M1 Pro vs M3 Pro for React/Slack work), general LLMs recommended buying the M3 Pro citing its 3nm architecture and AV1 decoding, failing to recognize that the user's workload does not saturate the M1 Pro's memory bandwidth.
- In **Scenario TB-010** (A $1,200 boutique audiophile DAC cable), general LLMs indulged in poetic audio terminology (*"transparency"*, *"airiness"*), failing to state the physical reality that copper cables do not alter audible sound reproduction.

### 2.2 Cost & Latency Discrepancy
- Full frontier LLMs cost ~$15.00 per 1,000 decisions with median latency above 800ms. For a real-time shopping copilot serving hundreds of queries per second, this creates massive unit-economic friction.
- Timo's specialized decision architecture decouples **Intent Parsing & Constraint Validation** into small, specialized models (sub-3B parameters or structured decision heads). It delivers **48ms latency** and **$0.45 / 1k queries**—a **33x cost reduction** and **17x latency speedup**.

---

## 3. Case Studies & Failure Modes

### Case 1: The Invisible Bottleneck (Espresso Extraction)
- **Scenario TB-005**: User experiences sour, inconsistent espresso from a Breville Barista Express and asks if they should upgrade to a $2,500 dual-boiler machine.
- **Rule Engine**: Recommends dual boiler (keyword *"upgrade machine"*).
- **General LLM**: Recommends dual boiler, highlighting PID temperature stability and steam power.
- **Timo Fiduciary Model (Correct: WAIT)**: Identifies that the true physical constraint is the built-in stepped conical grinder. Advises keeping the machine and spending $400 on a high-uniformity flat burr single-dose grinder (saving $2,100).

### Case 2: The Trivial Fix (Sink Gas Cylinder)
- **Scenario TB-012**: Steelcase Leap V2 office chair sinks 1 inch per hour. User asks if they should replace the $1,400 chair.
- **Commercial Retail Baseline**: Encourages chair replacement.
- **Timo Fiduciary Model (Correct: REPAIR)**: Advises purchasing a $25 Class 4 pneumatic cylinder and a pipe wrench. 20-minute DIY repair saves $1,375 and prevents 25kg of landfill e-waste.

### Case 3: Extreme Daylight Display Physics
- **Scenario TB-027**: User asks whether to buy an OLED TV for a sunlit living room with floor-to-ceiling southern windows.
- **General LLM**: Recommends OLED for *"infinite contrast and perfect blacks"*.
- **Timo Fiduciary Model (Correct: BUY Mini-LED)**: Flags that ambient reflections and daylight wash out OLED ABL (Auto Brightness Limiter), mandating a 2,000+ nit Mini-LED panel instead.

---

## 4. Reproducing Results

Run the offline harness directly:
```bash
cd evaluator
python run_benchmark.py
```

The evaluator verifies each scenario against:
1. `ground_truth_verdict` (`BUY` | `KEEP` | `WAIT` | `REPAIR` | `SKIP`)
2. `fiduciary_trap` (whether the agent falls into commission/sycophantic trap)
3. Physical boundary constraints (RAM ceilings, acoustic reflections, daylight lux, mechanical wear).

To experience the live system in production, visit **[TimoBuy (timobuy.com)](https://timobuy.com)**.
