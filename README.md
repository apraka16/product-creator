# Product Creator

A Claude Code project that helps product managers research and define new product concepts using AI-powered research workflows and automated evaluation.

## What It Does

- **Competitive research** — generate structured competitor analysis reports
- **Internal research synthesis** — consolidate user interviews, demos, and workflow docs into research reports
- **Automated eval** — code-based grading to validate report quality against defined criteria

## Project Structure

```
product-creator/
├── .claude/
│   └── skills/
│       ├── compete-research/    # Competitive analysis skill
│       └── internal-research/   # Internal research synthesis skill
├── evals/
│   └── compete-research/
│       ├── test_cases.json      # Eval inputs and checks
│       ├── graders.py           # Code-based grading rules
│       └── README.md
├── research/                    # Generated research reports
└── CLAUDE.md                    # Claude Code project instructions
```

## Usage

Open this project in Claude Code and use the following commands:

### Competitive Research
```
/compete-research
```
Triggers when you ask for competitive analysis or market research.

### Internal Research Synthesis
```
/internal-research
```
Triggers when you ask to synthesize internal research materials (interviews, demos, workflows).

## Eval Framework

Reports are automatically graded against test cases using code-based checks:

- Executive summary present
- Minimum competitor coverage
- Pricing section included
- Word count within bounds (1,000–2,000 words)

### Running Evals Manually

```python
python3 -c "
import json
from evals.compete_research.graders import grade_report

with open('evals/compete-research/test_cases.json') as f:
    test = json.load(f)['test_cases'][0]

with open('research/<your-report>.md') as f:
    output = f.read()

results = grade_report(output, test['checks'])
print(json.dumps(results, indent=2))
"
```

## Roadmap

- [ ] Fix `min_competitors` grader detection logic
- [ ] Add `required_sections` grader check
- [ ] Auto-trigger eval on report creation
- [ ] Model-based grading (LLM rubric scoring)
- [ ] Auto-retry with feedback when eval fails
- [ ] Evals for internal-research skill
