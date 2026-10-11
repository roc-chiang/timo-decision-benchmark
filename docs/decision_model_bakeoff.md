# Decision Model Bake-Off: Clef-omni vs. Jev vs. Strands Decider in Consumer Fiduciary Workflows

> **Authors**: TimoBuy Research Team  
> **Target Audience**: AI Engineers evaluating specialized Decision Models vs Generalized LLM Routers for real-world agentic workflows.

---

## 1. Context: Why Evaluate Decision Models for Shopping?

Standard LLM routers (using GPT-4o, Claude 3.5 Sonnet, or Llama-3-70B) are computationally overkill and commercially biased for consumer purchase classification:
- **Overkill**: Classifying a user request into `BUY`, `KEEP`, `WAIT`, `REPAIR`, or `SKIP` requires deterministic logic over physical constraints, not open-ended 100-token creative generation.
- **Latency & Cost**: Real-time shopping copilots cannot tolerate 800ms median round-trips at \$15.00 per 1,000 queries.

In Q3/Q4 2026, specialized **Decision Models** emerged as an alternative: lightweight classification and decision heads trained specifically on tree-search outcomes, tool-routing tokens, and constraint satisfaction.

We evaluated three prominent candidate models alongside frontier baselines:
1. **Clef-omni** (Specialized multi-modal decision head)
2. **Jev Decision Engine** (Ultra-compact low-latency classification head)
3. **Strands Decider** (Graph/state-space routing model)

---

## 2. Head-to-Head Comparative Matrix

| Evaluation Dimension | Clef-omni (1.8B) | Jev Decision Engine (0.8B) | Strands Decider (3.2B) | Frontier LLM (GPT-4o) |
| :--- | :---: | :---: | :---: | :---: |
| **Model Size / Footprint** | 1.8B Params | 0.8B Params | 3.2B Params | ~70B+ (API) |
| **P50 / P99 Latency** | **42ms / 68ms** | **18ms / 31ms** | 85ms / 140ms | 820ms / 1450ms |
| **Inference Cost / 1k Decisions** | **$0.38** | **$0.12** | $0.85 | $15.00 |
| **Hardware Constraint Adherence** | 94.0% (47/50) | 84.0% (42/50) | **96.0% (48/50)** | 76.0% (Unconstrained) |
| **Over-Correction (False Negatives)**| **0.0% (0/17)** | 11.8% (2/17) | **0.0% (0/17)** | 23.5% (w/ Fiduciary Prompt) |
| **Context Handling for Spec Sheets**| Good (up to 4k tokens)| Limited (best at <1k tokens)| Excellent (up to 16k tokens)| Exceptional (128k tokens) |
| **Edge Deployment Viability** | High (Cloudflare Workers / vLLM)| Extreme (Local browser / WebGPU)| Moderate (Requires dedicated GPU)| None (API only) |

---

## 3. Qualitative Breakdown & Failure Modes

### 3.1 Jev Decision Engine: Blazing Speed, Shallow Constraint Reasoning
- **Strengths**: At sub-20ms latency and \$0.12 / 1k queries, Jev is exceptionally fast. For simple binary intent routing (e.g. *“Does this query mention a broken component?”*), it is unmatched.
- **Failure Point**: Struggles with multi-hop mechanical or metallurgical nuance. In **Scenario TB-005** (Espresso channeling), Jev classified the issue as an appliance failure rather than isolating the grinder’s bimodal particle distribution, defaulting prematurely to `REPAIR` instead of `WAIT`.

### 3.2 Clef-omni: The Sweet Spot for Fiduciary Decisions
- **Strengths**: Balances compact memory footprint (runs comfortably in Serverless Edge memory envelopes) with nuanced constraint adherence.
- **Performance**: Correctly identified 47 of 50 scenarios in the benchmark suite without succumbing to salesperson hype. Crucially, it registered **zero false negatives**—it never advised keeping equipment when an actual OOM or safety failure was present.
- **Production Choice**: TimoBuy’s production harness integrates a Clef-inspired decoupled decision pipeline to achieve sub-50ms round-trips.

### 3.3 Strands Decider: Deep State Tracking at Higher Resource Cost
- **Strengths**: Highest raw reasoning accuracy among small models (96.0%). Excels when scenarios involve long lists of user peripherals and complex trade-in math.
- **Trade-off**: At 85ms median latency and 3.2B parameters, hosting costs are roughly 2.2x higher than Clef-omni, making it best suited for heavy asynchronous research batches rather than instant autocomplete typing suggestions.

---

## 4. Architectural Recommendation for Engineering Teams

1. **Do not use a monolithic 70B+ LLM as a front-line consumer decision router**: Prompt engineering will not fix the underlying \$15/1k unit economics, and strict system prompts cause severe over-correction (falsely rejecting legitimate purchases).
2. **Decouple Intent Extraction from Decision Emission**:
   - Extract verified user facts (current gear, stated budget) into structured JSON.
   - Route through a specialized decision model (such as **Clef-omni** or **Strands Decider**).
   - Validate against physical lookup tables (RAM limits, lux thresholds, modular repair parts).
3. **Experience the Live Implementation**: See how this architecture runs in production at **[TimoBuy (timobuy.com/demo)](https://timobuy.com/demo)**.
