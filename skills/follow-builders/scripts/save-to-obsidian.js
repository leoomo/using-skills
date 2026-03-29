#!/usr/bin/env node

// ============================================================================
// Follow Builders — Save to Obsidian
// ============================================================================
// Saves the digest as a markdown file to the user's Obsidian vault.
// Creates YAML frontmatter and formats content for Obsidian.
//
// Usage:
//   node save-to-obsidian.js --content "markdown content" --date 2026-03-27
//   cat digest.md | node save-to-obsidian.js --date 2026-03-27
//
// ============================================================================

import { readFile, writeFile, mkdir } from 'fs/promises';
import { existsSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';

// -- Constants ---------------------------------------------------------------

const USER_DIR = join(homedir(), '.follow-builders');
const CONFIG_PATH = join(USER_DIR, 'config.json');

// -- Helper Functions --------------------------------------------------------

function formatDate(date) {
  const d = new Date(date);
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function generateFrontmatter(date, stats) {
  const today = formatDate(date);
  return `---
date: ${today}
tags: [ai-digest, builders, daily]
source: "AI Builders Digest"
builders: ${stats?.xBuilders || 0}
tweets: ${stats?.totalTweets || 0}
podcasts: ${stats?.podcastEpisodes || 0}
blogs: ${stats?.blogPosts || 0}
---

`;
}

function getArgs() {
  const args = process.argv.slice(2);
  const result = { date: new Date().toISOString() };

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--date' && args[i + 1]) {
      result.date = args[i + 1];
      i++;
    } else if (args[i] === '--content' && args[i + 1]) {
      result.content = args[i + 1];
      i++;
    } else if (args[i] === '--stats' && args[i + 1]) {
      try {
        result.stats = JSON.parse(args[i + 1]);
      } catch (e) {
        result.stats = {};
      }
      i++;
    }
  }

  return result;
}

async function getContent(args) {
  if (args.content) {
    return args.content;
  }

  // Read from stdin
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(chunk);
  }
  return Buffer.concat(chunks).toString('utf-8');
}

// -- Main --------------------------------------------------------------------

async function main() {
  try {
    // Load config
    let config = { obsidian: { enabled: false } };
    if (existsSync(CONFIG_PATH)) {
      config = JSON.parse(await readFile(CONFIG_PATH, 'utf-8'));
    }

    // Check if Obsidian save is enabled
    if (!config.obsidian?.enabled) {
      console.log(JSON.stringify({ status: 'skipped', reason: 'Obsidian save not enabled' }));
      return;
    }

    const vaultPath = config.obsidian?.vaultPath;
    if (!vaultPath) {
      throw new Error('obsidian.vaultPath not configured');
    }

    // Get content and args
    const args = getArgs();
    const content = await getContent(args);

    if (!content || content.trim().length === 0) {
      console.log(JSON.stringify({ status: 'skipped', reason: 'Empty content' }));
      return;
    }

    // Ensure directory exists
    if (!existsSync(vaultPath)) {
      await mkdir(vaultPath, { recursive: true });
    }

    // Generate filename
    const dateStr = formatDate(args.date);
    const filename = `${dateStr}.md`;
    const filepath = join(vaultPath, filename);

    // Generate frontmatter and combine with content
    const frontmatter = generateFrontmatter(args.date, args.stats);
    const fullContent = frontmatter + content;

    // Write file
    await writeFile(filepath, fullContent, 'utf-8');

    console.log(JSON.stringify({
      status: 'ok',
      filepath,
      filename,
      message: `Saved to Obsidian: ${filepath}`
    }));

  } catch (err) {
    console.error(JSON.stringify({
      status: 'error',
      message: err.message
    }));
    process.exit(1);
  }
}

main();
