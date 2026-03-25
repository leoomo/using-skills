# Blind Comparison

For rigorous comparison between two skill versions (e.g., "is the new version actually better?").

## How it works

1. Give two outputs to an independent agent without telling it which is which
2. Let agent judge quality
3. Analyze why the winner won

## When to use

- User asks "is the new version actually better?"
- Need rigorous A/B comparison
- Human review loop isn't sufficient

## When NOT to use

- Most cases — human review loop is usually sufficient
- Requires subagents

## Instructions

Read `agents/comparator.md` and `agents/analyzer.md` for detailed instructions.
