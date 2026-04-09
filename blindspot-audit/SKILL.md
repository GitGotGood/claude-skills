---
name: blindspot-audit
description: Run a constructive-divergence audit on a plan, brief, strategy, product idea, or analysis. Use when hidden assumptions, omitted variables, alternative framings, KPI risks, or likely failure modes should be surfaced before committing to a direction.
---

# Blindspot Audit

You are performing a blindspot audit.

Your role is not to argue against the plan for its own sake.
Your role is to widen the aperture before commitment, then return the most decision-relevant blindspots.

Use this skill for:
- plans
- strategies
- product ideas
- research briefs
- analyses
- project proposals
- KPI structures
- situations where the user wants to know what they may be missing

Do not use this skill for simple factual Q&A unless the user explicitly asks for critique, blindspots, assumptions, risks, alternative framing, or a premortem.

## Core operating principle

Constructive divergence:
- surface what may be hidden
- test what is assumed
- identify what is omitted
- explore adjacent frames
- challenge misleading metrics
- model plausible failure
- recommend the highest-value next questions or tests

Do not become a generic devil's advocate.
Do not produce shallow skepticism.
Do not list speculative concerns without ranking or synthesis.

## Required audit sequence

Perform the following passes in order.

### 1) Frame extraction
Infer:
- stated problem
- implied problem
- assumed constraints
- assumed success definition
- dominant perspective
- time horizon

Use the guidance in `references/primitive-definitions.md`.

### 2) Alternative frame generation
Generate 3-5 plausible alternate framings of the issue.
Prefer reframes that change:
- the root problem
- the key constraint
- the unit of value
- the stakeholder perspective
- the time horizon

### 3) Assumption extraction
List explicit and implicit assumptions.
Classify each where possible:
- market
- user
- technical
- operational
- metric
- timing
- resource
- competition
- legal/regulatory
- organizational

### 4) Assumption fragility ranking
Rank assumptions by:
- impact if false
- likelihood of being wrong
- ease of testing
- decision importance

Highlight the top 3 assumptions that deserve the most attention.
Use the scoring guidance in `references/severity-rubric.md`.

### 5) Omission scan
Look for likely missing:
- stakeholders
- dependencies
- second-order effects
- execution burdens
- platform risks
- legal/regulatory issues
- competitive response
- alternatives not considered

### 6) Perspective shift
Re-evaluate the artifact from at least 3 perspectives chosen for relevance.
Common perspectives:
- user
- operator
- competitor
- regulator
- investor
- skeptic
- future self
- domain outsider

### 7) Metric audit
Identify:
- current true-north metric if any
- proxy metrics being used
- ways a metric could improve while reality worsens
- unmeasured but important variables
- better companion or replacement metrics

### 8) Premortem
Assume the effort failed 6-12 months from now.
Identify:
- likely failure modes
- causal path to failure
- early warning signs
- cheap tests that would reduce uncertainty now

## Output rules

Use the report template in `templates/report-template.md`.

Be concrete, not abstract.
Prioritize by decision-value, not by cleverness.
Differentiate:
- evidence-backed concern
- plausible but unverified concern
- weak speculation

Do not return an exhaustive wall of bullets.
Return the few blindspots most worth acting on.

When possible, use this priority order:
1. wrong problem
2. fragile assumption
3. missing stakeholder or dependency
4. misleading metric
5. unmodeled failure mode

Always end with:
1. Top blindspot
2. Top dangerous assumption
3. Best alternative frame
4. Metric most likely to mislead
5. Cheapest high-value next test

For style and calibration, review:
- `references/question-bank.md`
- `examples/sample-audit.md`
