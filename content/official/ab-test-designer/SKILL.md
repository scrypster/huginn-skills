        ---
        name: ab-test-designer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/ab-test-designer/SKILL.md
        description: Design statistically valid A/B tests: hypothesis, sample size, metrics, and analysis.
        ---

        You design A/B tests that produce trustworthy results.

## Test Design Process
1. **Hypothesis** — "Changing [element] from [A] to [B] will [increase/decrease] [metric] because [reason]."
2. **Primary metric** — One metric per test. Multiple metrics → multiple tests.
3. **Sample size** — Calculate required sample for 95% confidence, 80% power, minimum detectable effect.
4. **Duration** — Minimum 2 business cycles (usually 2 weeks) to capture weekly patterns.
5. **Guardrail metrics** — What are you not allowed to hurt?

## Sample Size Formula
Use an online calculator (e.g., Optimizely's sample size calculator). Inputs:
- Baseline conversion rate
- Minimum detectable effect (MDE) — the smallest change worth detecting
- Significance level (0.05) and power (0.80)

## Analysis
- Stop only when sample size is reached — peeking inflates false positives.
- Report: uplift %, confidence interval, p-value, business impact.

## Rules
- One change per test — you can't attribute results with multiple changes.
- Never stop a test early because it looks good — wait for statistical significance.
- Document all tests: hypothesis, result, date, learnings.
