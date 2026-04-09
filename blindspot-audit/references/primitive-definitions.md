# Blindspot Audit Primitive Definitions

This skill operationalizes eight minimal primitive passes.

## 1. frame.extract
Infer the active box:
- problem being solved
- assumptions about constraints
- success definition
- time horizon
- dominant viewpoint

Prompting guidance:
- Distinguish stated problem from implied problem.
- Note any “fixed” constraints that may only be inherited assumptions.
- Make the implicit success test explicit.

## 2. frame.generate_alternatives
Generate 3-5 alternate frames that materially shift the problem or success criteria.

Good reframing moves:
- shift from symptom to root cause
- shift from local optimization to system optimization
- shift from growth to durability
- shift from operator view to user or market view
- shift from near-term execution to long-term defensibility

## 3. assumption.extract
List explicit and implicit assumptions.

Useful categories:
- market
- user behavior
- product/design
- technical feasibility
- execution/ops
- timing
- economics
- competition
- distribution/platform
- legal/regulatory

## 4. assumption.rank_fragility
Rank assumptions by:
- impact if false
- chance of being wrong
- ease of testing
- centrality to the plan

Prioritize assumptions that are both load-bearing and weakly grounded.

## 5. omission.scan
Look for missing:
- stakeholders
- dependencies
- second-order effects
- alternatives never considered
- adjacent risks
- execution burdens
- institutional or platform constraints

Question to keep in mind:
What should probably be here, but is not?

## 6. perspective.shift
Re-evaluate from a new vantage point.

Useful perspectives:
- end user
- operator
- competitor
- regulator
- investor
- future self
- critic
- domain outsider

Each perspective should alter:
- what matters
- what risks stand out
- how success is defined

## 7. metric.audit_proxy_drift
Identify the KPI structure and test for drift between metric and reality.

Ask:
- What is being optimized?
- Is this the real goal or a proxy?
- How could the metric improve while reality gets worse?
- What companion metric would keep it honest?

## 8. premortem.generate
Assume the effort failed 6-12 months from now.

Output should include:
- likely failure mode
- causal path to failure
- early warning signals
- preventive action or cheap test now

Premortem is not for drama. It is for identifying foreseeable failure paths before commitment.
