"""Markdown parser for Obsidian-flavored markdown."""
import re
import yaml
from typing import Dict, Tuple, Any


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Extract YAML frontmatter and return metadata + body."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if match:
        try:
            metadata = yaml.safe_load(match.group(1))
            body = match.group(2)
            return metadata or {}, body
        except yaml.YAMLError:
            pass

    return {}, content


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    return text.lower().replace(' ', '-').replace('/', '-')


def convert_wikilinks(content: str) -> str:
    """Convert Obsidian wikilinks to HTML links."""
    # [[Link|Display]] -> <a href="link">Display</a>
    pattern1 = r'\[\[([^\]|]+)\|([^\]]+)\]\]'
    content = re.sub(
        pattern1,
        lambda m: f'<a href="{slugify(m.group(1))}">{m.group(2)}</a>',
        content
    )

    # [[Link]] -> <a href="link">Link</a>
    pattern2 = r'\[\[([^\]]+)\]\]'
    content = re.sub(
        pattern2,
        lambda m: f'<a href="{slugify(m.group(1))}">{m.group(1)}</a>',
        content
    )

    return content
