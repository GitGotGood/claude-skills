# Install and Use

## Install
Copy this folder into either:

- `~/.claude/skills/blindspot-audit/` for personal use across projects
- `.claude/skills/blindspot-audit/` inside a specific repo for project-local use

Example:

```bash
mkdir -p ~/.claude/skills
cp -R blindspot-audit-skill ~/.claude/skills/blindspot-audit
```

If you use the zip file, unzip it first and rename the folder to `blindspot-audit` if desired.

## Invoke manually
In Claude Code:

```text
/blindspot-audit
```

Then provide a plan, brief, strategy, or file context.

## Example prompts
- What are the blindspots in this plan?
- Stress-test this strategy before we commit.
- What assumptions is this proposal resting on?
- Give me a blindspot audit of this KPI structure.
- Run a premortem and tell me what we're missing.

## Good uses
- strategy reviews
- product planning
- KPI / true-north audits
- research synthesis checks
- pre-mortems before execution

## Not ideal for
- simple factual questions
- routine summarization
- tasks where the user only wants a quick yes/no answer
