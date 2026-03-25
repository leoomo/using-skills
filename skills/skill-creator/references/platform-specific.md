# Platform-Specific Instructions

## Claude.ai

Core workflow is the same (draft → test → review → improve → repeat), but without subagents:

**Running test cases:**
- Read SKILL.md, follow instructions for each test prompt yourself
- Do them one at a time
- Skip baseline runs — just use the skill

**Reviewing results:**
- Skip browser viewer if no display
- Present results directly in conversation
- Show prompt and output for each test case
- Save files to filesystem for user to download
- Ask for feedback inline

**Benchmarking:**
- Skip quantitative benchmarking (no baseline comparisons)
- Focus on qualitative feedback

**Description optimization:**
- Requires `claude` CLI — skip if not available

**Blind comparison:**
- Requires subagents — skip

**Packaging:**
- `package_skill.py` works anywhere with Python
- User can download resulting `.skill` file

**Updating existing skills:**
- Preserve original name (directory and frontmatter)
- Copy to `/tmp/skill-name/` before editing (may be read-only)
- Stage in `/tmp/` first if packaging manually

## Cowork

- Subagents available → main workflow works
- No browser/display → use `--static <output_path>` for eval viewer
- **IMPORTANT:** Always generate eval viewer with `generate_review.py` BEFORE evaluating yourself
- Feedback downloads as `feedback.json` file
- Description optimization works (uses `claude -p` via subprocess)
- Follow same update guidance as Claude.ai
