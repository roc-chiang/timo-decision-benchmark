# Timo Decision Benchmark (TDB) - Launch & Outreach Templates

This document provides ready-to-use launch copy tailored for Hacker News, Reddit, Twitter/X, and LinkedIn.
The narrative positions TimoBuy as a **practical, production case study** of decision models solving the "salesperson trap" in consumer AI.

---

## 1. Hacker News (Show HN)

**Suggested Title:**
> `Show HN: Can a Small Decision Model Make a Better AI Buyer? (50-Scenario Benchmark)`

**Body:**
```markdown
Hi HN,

Most AI shopping agents are built with an implicit bias: they want you to buy things. E-commerce platforms optimize for GMV, and frontier LLMs trained on web review hype naturally mirror that enthusiasm. When a user asks "Should I upgrade my M1 Pro to M3 Pro for web dev?", the average LLM enthusiastically recites new GPU specs and validates the purchase.

In the real world, the fiduciary answer is often: KEEP, WAIT, REPAIR, or SKIP.

We wanted to know: Can a specialized decision model outperform generalized 70B+ LLMs on fiduciary consumer purchasing decisions, while reducing latency and cost?

To test this, we built a 50-scenario benchmark across laptops, coffee gear, trail footwear, ergonomics, and home appliances:
https://github.com/roc-chiang/timo-decision-benchmark

Results across the 50 scenarios:
- Traditional E-Commerce Rule Routers: 38% accuracy | 6.1% fiduciary restraint | 4.2ms | $0.01 / 1k queries
- Generalized Frontier LLMs (70B+ class): 76% accuracy | 63.6% fiduciary restraint | 820ms | $15.00 / 1k queries
- Fiduciary Decision Architecture: 96% accuracy | 93.9% fiduciary restraint | 48ms | $0.45 / 1k queries

Key learnings:
1. "The Salesperson Trap": Frontier LLMs without rigid physical constraints suffer from sycophancy. If the user mentions upgrading, the model rationalizes the purchase 36% of the time, ignoring un-saturable memory bandwidth or existing equipment.
2. The unit economics of full LLMs for shopping routers are broken ($15/1k queries). A decoupled Goal-First parser + decision head costs 33x less and runs in under 50ms.

The repo includes the 50 scenarios, ground truth reasoning, and a zero-dependency Python evaluator (supports live testing via any OpenAI-compatible endpoint).

We also deployed an interactive playground in our production copilot, TimoBuy: https://timobuy.com/demo

We'd love to hear your feedback on edge cases, ground truth classifications, and how you approach fiduciary alignment in agentic workflows.
```

---

## 2. Reddit (r/LocalLLaMA & r/MachineLearning)

**Suggested Title:**
> `Why General LLMs Make Terrible Buyers: Open Benchmark & 33x Cost Reduction with Specialized Decision Models`

**Body:**
```markdown
Hey everyone,

We just open-sourced a 50-scenario production benchmark evaluating whether specialized decision models can outperform generalized frontier LLMs on consumer purchasing decisions:
https://github.com/roc-chiang/timo-decision-benchmark

The problem:
When you prompt a 70B model with a shopping dilemma, it almost always defaults to "helpful salesperson mode". In our dataset:
- Breville espresso tasting sour? LLMs recommend a $2,500 dual boiler (ignoring the built-in conical grinder bottleneck).
- Ergonomic chair sinking 1 inch? LLMs recommend buying a new $1,400 chair (ignoring a $25 gas cylinder swap).
- M1 Pro for React/Slack? LLMs validate an M3 Pro upgrade citing 3nm benchmarks.

By decoupling the pipeline into a Goal-First Intent Parser + Constraint Engine, a specialized sub-3B decision architecture achieved:
- 96% decision accuracy (vs 76% for general LLMs)
- 93.9% fiduciary restraint on unnecessary upgrades (vs 63.6%)
- 48ms latency (vs 820ms)
- $0.45 per 1,000 decisions (vs $15.00)

Harness and dataset are MIT licensed and run with pure Python standard library:
```bash
git clone https://github.com/roc-chiang/timo-decision-benchmark.git
cd timo-decision-benchmark/evaluator && python run_benchmark.py
```
You can also hook up Ollama or local vLLM instances using `--live --base-url http://localhost:11434/v1`.

Curious to hear how others handle sycophancy in shopping agents!
```

---

## 3. Twitter / X (Thread)

**Tweet 1:**
> Most AI agents are built to do more. We built one that knows when to stop.  
> 
> Can a small decision model make a better AI buyer than GPT-4?  
> We open-sourced a 50-scenario benchmark comparing Rule Routers vs Frontier LLMs vs Decision Models.  
> 
> Results, dataset & findings 👇 🧵  
> https://github.com/roc-chiang/timo-decision-benchmark

**Tweet 2:**
> Frontier LLMs have an implicit "salesperson trap":  
> If you ask about upgrading your M1 Pro to M3 Pro for web dev, they recite 3nm benchmarks and tell you to buy.  
> 
> In reality, web dev doesn't saturate M1 Pro memory bandwidth. The fiduciary answer is KEEP.

**Tweet 3:**
> Across 50 real-world consumer dilemmas:  
> ❌ Rules Baseline: 38% accuracy ($0.01 / 1k)  
> ⚠️ Frontier 70B+: 76% accuracy, 63% restraint ($15.00 / 1k)  
> ✅ Decision Architecture: 96% accuracy, 94% restraint ($0.45 / 1k)  
> 
> 33x cheaper. 17x faster.

**Tweet 4:**
> We put this decision philosophy into production at @TimoBuy:  
> https://timobuy.com/demo  
> 
> An AI buyer that doesn't always tell you to buy.  
> Try asking it if you should upgrade your setup today.
