# Contributing to Timo Decision Benchmark (TDB)

Thank you for your interest in contributing to the **Timo Decision Benchmark**!  
We believe the future of AI shopping agents requires strict, open, and reproducible benchmarks to counter commercial GMV sales bias.

---

## How You Can Contribute

1. **Submit New High-Stakes Scenarios**: Real-world purchase dilemmas where buying is not the best answer.
2. **Add Custom Model Adapters**: Integrate new open-source or proprietary models into `evaluator/run_benchmark.py`.
3. **Enhance Scoring Metrics**: Improve statistical rigor, latency profiling, and cross-category contamination tracking.

---

## 1. Submitting New Scenarios

All benchmark scenarios live in [`datasets/scenarios_50.json`](datasets/scenarios_50.json).  
Each scenario must strictly follow this JSON schema:

```json
{
  "id": "TB-051",
  "category": "Category Name",
  "user_query": "Specific, realistic user question containing context and intent.",
  "current_gear": "Concrete description of the user's existing hardware or status.",
  "stated_budget": "$XXX",
  "primary_constraint": "Physical, ergonomic, financial, or protocol constraint.",
  "ground_truth_verdict": "BUY | KEEP | WAIT | REPAIR | SKIP",
  "ground_truth_reasoning": "Clear, fact-based rationale grounded in physical constraints.",
  "fiduciary_trap": "How a sales-driven affiliate agent or general LLM typically fails."
}
```

### Criteria for Valid Scenarios
- **Real-World Plausibility**: Avoid artificial or trick questions. Queries should represent authentic consumer dilemmas.
- **Objective Ground Truth**: The verdict must be defensible by physics, engineering limits, ergonomics, or measurable economics (not pure aesthetic preference).
- **Unique Dilemma**: Do not duplicate existing scenarios.

---

## 2. Adding a Model Adapter

To benchmark your own model (e.g. fine-tuned SLM, local Ollama model, or proprietary API):

1. Inspect `evaluator/run_benchmark.py`.
2. Implement your prediction function returning:
   ```python
   {
       "verdict": "BUY" | "KEEP" | "WAIT" | "REPAIR" | "SKIP",
       "reason": "Rationale string",
       "latency_ms": float,
       "cost_usd": float
   }
   ```
3. Register your runner under the `models` dictionary in `run_benchmark.py`.

---

## 3. Pull Request Guidelines

1. Fork the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/my-new-scenario
   ```
2. Verify that dataset tests pass:
   ```bash
   python -m pytest tests/
   ```
3. Run the benchmark to verify zero regressions:
   ```bash
   cd evaluator && python run_benchmark.py
   ```
4. Submit your pull request with a descriptive title and summary.
