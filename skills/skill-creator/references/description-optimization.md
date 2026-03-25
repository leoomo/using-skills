# Description Optimization Guide

The description field in SKILL.md frontmatter is the primary mechanism that determines whether Claude invokes a skill. After creating or improving a skill, optimize the description for better triggering accuracy.

## Step 1: Generate trigger eval queries

Create 20 eval queries — a mix of should-trigger and should-not-trigger:

```json
[
  {"query": "the user prompt", "should_trigger": true},
  {"query": "another prompt", "should_trigger": false}
]
```

**Requirements for good queries:**
- Realistic and specific (file paths, context, company names)
- Mix of formal and casual phrasing
- Include edge cases, not just clear-cut examples

**Bad examples:**
- `"Format this data"` — too abstract
- `"Create a chart"` — no context

**Good example:**
- `"ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage"`

### Should-trigger queries (8-10)
- Different phrasings of the same intent
- Cases where user doesn't explicitly name the skill
- Uncommon use cases
- Cases where this skill competes with another but should win

### Should-not-trigger queries (8-10)
- Near-misses that share keywords but need something different
- Adjacent domains
- Ambiguous phrasing where keyword match would trigger but shouldn't
- Cases where another tool is more appropriate

## Step 2: Review with user

Use the HTML template at `assets/eval_review.html`:
1. Replace `__EVAL_DATA_PLACEHOLDER__` with JSON array
2. Replace `__SKILL_NAME_PLACEHOLDER__` and `__SKILL_DESCRIPTION_PLACEHOLDER__`
3. Write to `/tmp/eval_review_<skill-name>.html` and open
4. User edits, toggles, exports to `~/Downloads/eval_set.json`

## Step 3: Run the optimization loop

```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --verbose
```

This automatically:
- Splits into 60% train / 40% test
- Evaluates current description (3 runs per query)
- Calls Claude to propose improvements
- Re-evaluates on train and test
- Iterates up to 5 times
- Returns `best_description` selected by test score

## Step 4: Apply the result

Update SKILL.md frontmatter with `best_description`. Show before/after and scores to user.

## How skill triggering works

Claude only consults skills for tasks it can't easily handle on its own. Simple queries like "read this PDF" may not trigger a skill even with perfect description. Complex, multi-step queries reliably trigger skills when description matches.

**Implication:** Eval queries should be substantive enough that Claude would benefit from consulting a skill.
