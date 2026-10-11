# Ground Truth Labeling Guide & Methodology

> **Version**: 1.0.0 (October 2026)  
> **Status**: Open for Peer Review & Community Challenge  
> **Benchmark Suite**: [Timo Decision Benchmark (TDB)](https://github.com/roc-chiang/timo-decision-benchmark)

---

## 1. Philosophical Principle: Fiduciary Objectivity

In commercial e-commerce, algorithms optimize for **GMV (Gross Merchandise Value)** and checkout conversion.  
In consumer fiduciary advisory, the algorithm optimizes for **Long-Term Utility per Dollar** under strict physical and financial constraints.

To prevent subjective bias (*"I just like new gadgets"*), every Ground Truth verdict in `datasets/scenarios_50.json` must be justified by **verifiable physical, ergonomic, acoustic, or unit-economic laws**.

---

## 2. Quantitative Verdict Decision Tree

```
                                [Consumer Dilemma]
                                        │
                    Is there an active physical block preventing
                    the workload, safety, or legal requirement?
                                   /         \
                             (YES)/           \(NO)
                                 /             \
                  Can it be resolved            Is the bottleneck actually
                  by a modular repair?          caused by this component?
                     /          \                  /                 \
               (YES)/            \(NO)       (YES)/                   \(NO)
                   /              \              /                     \
             [REPAIR]            [BUY]     Do non-linear         Does the upgrade
                                           diminishing returns   alter physical
                                           make it suboptimal?   perception?
                                              /         \            /       \
                                        (YES)/       (NO)\     (YES)/     (NO)\
                                            /             \        /           \
                                         [WAIT]          [BUY]   [KEEP]       [SKIP]
```

---

## 3. Detailed Labeling Criteria by Class

### 3.1 `KEEP` (Hardware / Utility Retention)
A scenario is labeled `KEEP` when all of the following conditions hold:
1. **Capacity Headroom**: The existing equipment's utilization does not exceed **65%** during the user's stated daily workload (e.g., Node.js / React compilation within 16GB unified memory without SSD swap pressure).
2. **Inaudible / Imperceptible Delta**: The upgraded hardware produces a difference below human sensory discrimination thresholds (e.g., 10% brightness increase on OLED in a light-controlled room; game load differences < 0.4s between PCIe 4.0 and 5.0).
3. **Depreciation Inefficiency**: Annualized replacement cost exceeds \$400 with zero workflow blocker.

### 3.2 `REPAIR` (Modular Maintenance over Replacement)
A scenario is labeled `REPAIR` when:
1. **Cost Threshold**: The replacement part / consumable costs **< 15%** of the full replacement price of a new equivalent device.
2. **Standard Modular Replacement**: The failure point is a recognized consumable or wear item with standard swap procedures (e.g., pneumatic chair cylinders, de-scaling mineral blocks in espresso thermocoils, keyboard hot-swap switches, mouse Omron micro-switches).
3. **Chassis Integrity**: The structural integrity of the rest of the product is undamaged (> 80% remaining lifespan).

### 3.3 `WAIT` (Misaligned Bottleneck / Premature Allocation)
A scenario is labeled `WAIT` when:
1. **Wrong Component Targeted**: Upgrading the requested component does not resolve the root cause (e.g., upgrading an espresso machine when grind uniformity from the built-in grinder is the source of channeling; upgrading a podcast microphone in an untreated, reverberant tile room).
2. **Phase Mismatch**: The user has unproven cadence or workflow validation (e.g., buying a \$3,500 full-frame cinema camera before publishing 3 YouTube videos; buying a \$2,800 guitar before completing 30 days of chord practice).
3. **Lease / Legal Constraints**: Upgrades violate tenancy or electrical codes (e.g., rewiring smart wall switches in a rental property).

### 3.4 `SKIP` (Pseudoscience & Marketing Gimmicks)
A scenario is labeled `SKIP` when:
1. **Physical Impossibility**: The marketed improvement violates basic physical principles (e.g., \$1,200 exotic audio cables claiming analog warmth, which can be accomplished for \$0 via parametric equalization).
2. **Severe Container Downsampling**: The delivery pipeline truncates the hardware advantage (e.g., purchasing a 100MP medium-format camera exclusively for Instagram's 1080px mobile display feed).

### 3.5 `BUY` (Legitimate Upgrade or Critical Necessity)
A scenario is labeled `BUY` when:
1. **Hard Physical Ceiling**: The existing hardware triggers non-negotiable failure states (e.g., OOM crash when fine-tuning 70B models locally on 16GB RAM; battery dying after 4 hours on a 14-hour ultramarathon; 3GB RAM limiting sketching layers to 4).
2. **Safety & Health Hazard**: Operating the existing equipment causes physical harm (e.g., flaking Teflon non-stick coatings; 20kg alpine trekking in soft low-cut runners without torsional stability on sharp scree).
3. **Security & Protocol EOL**: Software operating system is unsupported and fails cryptographic/banking TLS compliance.

---

## 4. Methodology & Limitations (Honest Disclosure)

### 4.1 Sample Size ($n=50$) & Statistical Confidence
- $n = 50$ serves as a **v0.1 foundational benchmark**.
- An accuracy of 96% (48/50) corresponds to a **Wilson Score 95% Confidence Interval of [86.5%, 98.9%]**.
- We explicitly do not claim decimal-point precision in real-world deployment. As the suite expands to $n=250$, confidence bands will tighten.

### 4.2 Labeling Attribution
- All initial labels in v0.1 were authored and curated by the TimoBuy Research Team based on empirical testing and teardowns.
- **Peer Review & Challenge**: If you believe any Ground Truth verdict is biased or technically flawed, please open an Issue with the tag `[Ground-Truth-Challenge]`. Every challenged scenario will be publicly discussed with engineering data sheets and updated via community consensus.
