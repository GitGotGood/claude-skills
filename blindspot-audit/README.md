# Blindspot Audit

A Claude Code skill for surfacing **hidden assumptions**, **omitted variables**, **misleading KPIs**, **alternative frames**, and **likely failure modes** before a team commits to a plan.

Blindspot Audit is built for **constructive divergence**.

It does not try to be a devil’s advocate. It does not argue against a plan for sport. It widens the aperture so you do not converge rigorously on the wrong thing.

## Why this exists

Most planning workflows are good at **convergent thinking**:

- narrow options
- resolve conflicts
- build a coherent plan
- move toward execution

What they often lack is **constructive divergence**:

- inspect the frame
- surface hidden assumptions
- detect omissions
- challenge misleading metrics
- model likely failure paths

Blindspot Audit exists to provide that counterweight.

## What it does

Given a plan, strategy, product idea, OKR, research brief, or analysis, Blindspot Audit runs a structured audit across eight passes:

1. **Frame extraction** — What box are we in?
2. **Alternative frame generation** — What other problem might this really be?
3. **Assumption extraction** — What has to be true for this to work?
4. **Assumption fragility ranking** — Which assumptions are most dangerous if false?
5. **Omission scan** — What is missing?
6. **Perspective shift** — What would this look like to other stakeholders?
7. **Metric audit** — Are we measuring what matters, or just what is easy?
8. **Premortem** — If this fails later, why will it have failed?

The skill returns a structured report that highlights the most decision-relevant blindspots, not an endless wall of generic concerns.

## Best use cases

Use Blindspot Audit for:

- OKRs and strategic planning
- product strategy
- growth plans
- GTM plans
- KPI reviews
- research briefs
- project proposals
- pre-mortems before execution
- “what are we missing?” reviews

It is especially useful when a plan already looks coherent and well thought through, but you want to test whether the **frame itself** may be off.

## Install

Create your Claude Code skills directory if you do not already have one:

```bash
mkdir -p ~/.claude/skills
```

Copy this skill folder into:

```bash
~/.claude/skills/blindspot-audit/
```

Your final path should look like:

```bash
~/.claude/skills/blindspot-audit/SKILL.md
```

Then restart Claude Code or start a new session.

## Usage

Invoke the skill directly:

```text
/blindspot-audit
```

Then paste in the plan, strategy, OKR, or other artifact you want audited.

You can also often trigger it naturally with prompts like:

- “What are we missing here?”
- “Stress-test this plan.”
- “What assumptions is this resting on?”
- “What are the blindspots in this OKR?”
- “Give me a premortem.”
- “What KPI risks do you see?”
- “What would future me regret not asking?”

## Example prompts

### OKR review

```text
Use blindspot-audit on this OKR. I want hidden assumptions, KPI risks, missing variables, and the best alternative framing.
```

### Product strategy

```text
Run a blindspot audit on this product strategy memo. Focus especially on whether we are solving the wrong problem and whether our success metrics are misleading.
```

### Growth plan

```text
Audit this growth plan for omitted dependencies, fragile assumptions, and likely failure modes.
```

### Research brief

```text
Use blindspot-audit on this research brief. Tell me what frame it is operating inside and what adjacent possibilities it is not considering.
```

## Output shape

The report is structured around:

- Current frame
- Best alternative frames
- Hidden assumptions
- Key omissions
- Perspective shifts
- Metric audit
- Premortem
- Priority summary

Each audit aims to end with five things:

1. **Top blindspot**
2. **Top dangerous assumption**
3. **Best alternative frame**
4. **Metric most likely to mislead**
5. **Cheapest high-value next test**

## Included files

- `SKILL.md` — main Claude Code skill definition
- `templates/report-template.md` — report template
- `references/primitive-definitions.md` — core audit passes
- `references/question-bank.md` — supporting challenge questions
- `references/severity-rubric.md` — prioritization guidance
- `examples/sample-audit.md` — example output
- `INSTALL.md` — quick install instructions

## Core design

Blindspot Audit is built around a minimal set of eight audit primitives:

- `frame.extract`
- `frame.generate_alternatives`
- `assumption.extract`
- `assumption.rank_fragility`
- `omission.scan`
- `perspective.shift`
- `metric.audit_proxy_drift`
- `premortem.generate`

These are bundled into one orchestration skill because the value comes from the **sequence**, not from isolated critique.

## What this skill is not

Blindspot Audit is **not**:

- a generic devil’s advocate
- a negativity engine
- a vague “be more critical” persona
- a replacement for domain expertise
- a guarantee that the alternative frame is better

It is a structured audit tool for surfacing what may be hidden, fragile, underweighted, or excluded.

## Tips for better results

You will get the strongest output when you provide:

- the actual plan or strategy text
- relevant business context
- known constraints
- current KPIs
- economics or operating assumptions
- the type of blindspots you care about most

The more real context you provide, the less the audit will sound like a polished generic consultant.

## Publishing notes

For an open-source release, the simplest default is **MIT**.

It is short, widely understood, and easy for others to adopt, remix, and build on. If you want stronger patent language later, consider Apache-2.0. For a lightweight community skill repo, MIT is usually the cleanest choice.

## Roadmap

Possible future directions:

- sub-skills for metric audit, frame break, or premortem only
- domain-specific variants for product, growth, or org design
- configurable audit tone
- tighter integration with planning workflows
- before/after examples
- benchmark prompts and eval cases

## Contributing

Suggestions, improvements, and variants are welcome.

Useful contributions include:

- sharper question banks
- stronger example audits
- domain-specific extensions
- improved templates
- improvements that reduce generic output and increase real-world specificity

## License

MIT
