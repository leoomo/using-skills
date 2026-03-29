#!/usr/bin/env node

// ============================================================================
// Follow Builders — Delivery Script
// ============================================================================
// Sends a digest to the user via their chosen delivery method.
// Supports: Telegram bot, Email (via Resend), or stdout (default).
//
// Usage:
//   echo "digest text" | node deliver.js
//   node deliver.js --message "digest text"
//   node deliver.js --file /path/to/digest.txt
//   node deliver.js --file /path/to/digest.txt --html /path/to/digest.html --md /path/to/digest.md
//
// The script reads delivery config from ~/.follow-builders/config.json
// and API keys from ~/.follow-builders/.env
//
// Delivery methods:
//   - "telegram": sends via Telegram Bot API (needs TELEGRAM_BOT_TOKEN + chat ID)
//   - "email": sends via Resend API (needs RESEND_API_KEY + email address)
//   - "stdout" (default): just prints to terminal
// ============================================================================

import { readFile } from 'fs/promises';
import { existsSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';
import { config as loadEnv } from 'dotenv';
import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// -- Constants ---------------------------------------------------------------

const USER_DIR = join(homedir(), '.follow-builders');
const CONFIG_PATH = join(USER_DIR, 'config.json');
const ENV_PATH = join(USER_DIR, '.env');

// -- Read input --------------------------------------------------------------

// The digest text can come from stdin, --message flag, or --file flag
async function getDigestText() {
  const args = process.argv.slice(2);

  // Check --message flag
  const msgIdx = args.indexOf('--message');
  if (msgIdx !== -1 && args[msgIdx + 1]) {
    return args[msgIdx + 1];
  }

  // Check --file flag
  const fileIdx = args.indexOf('--file');
  if (fileIdx !== -1 && args[fileIdx + 1]) {
    return await readFile(args[fileIdx + 1], 'utf-8');
  }

  // Read from stdin
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(chunk);
  }
  return Buffer.concat(chunks).toString('utf-8');
}

// Get HTML content from --html flag if provided
function getHtmlFilePath() {
  const args = process.argv.slice(2);
  const htmlIdx = args.indexOf('--html');
  if (htmlIdx !== -1 && args[htmlIdx + 1]) {
    return args[htmlIdx + 1];
  }
  return null;
}

// Get Markdown content from --md flag if provided (used for Obsidian save)
function getMdFilePath() {
  const args = process.argv.slice(2);
  const mdIdx = args.indexOf('--md');
  if (mdIdx !== -1 && args[mdIdx + 1]) {
    return args[mdIdx + 1];
  }
  return null;
}

// -- Telegram Delivery -------------------------------------------------------

// Sends the digest via Telegram Bot API.
// The user creates a bot via @BotFather and provides the token.
// The chat ID is obtained when the user sends their first message to the bot.
async function sendTelegram(text, botToken, chatId) {
  // Telegram has a 4096 character limit per message.
  // If the digest is longer, we split it into chunks.
  const MAX_LEN = 4000;
  const chunks = [];
  let remaining = text;
  while (remaining.length > 0) {
    if (remaining.length <= MAX_LEN) {
      chunks.push(remaining);
      break;
    }
    // Try to split at a newline near the limit
    let splitAt = remaining.lastIndexOf('\n', MAX_LEN);
    if (splitAt < MAX_LEN * 0.5) splitAt = MAX_LEN;
    chunks.push(remaining.slice(0, splitAt));
    remaining = remaining.slice(splitAt);
  }

  for (const chunk of chunks) {
    const res = await fetch(
      `https://api.telegram.org/bot${botToken}/sendMessage`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: chatId,
          text: chunk,
          parse_mode: 'Markdown',
          disable_web_page_preview: true
        })
      }
    );

    if (!res.ok) {
      const err = await res.json();
      // If Markdown parsing fails, retry without parse_mode
      if (err.description && err.description.includes("can't parse")) {
        await fetch(
          `https://api.telegram.org/bot${botToken}/sendMessage`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: chatId,
              text: chunk,
              disable_web_page_preview: true
            })
          }
        );
      } else {
        throw new Error(`Telegram API error: ${err.description}`);
      }
    }

    // Small delay between chunks to avoid rate limiting
    if (chunks.length > 1) await new Promise(r => setTimeout(r, 500));
  }
}

// -- Email Delivery (Resend) -------------------------------------------------

// Sends the digest via Resend's email API.
// The user provides their own Resend API key and email address.
async function sendEmail(text, apiKey, toEmail, html = null) {
  const body = {
    from: 'AI Builders Digest <digest@resend.dev>',
    to: [toEmail],
    subject: `AI Builders Digest — ${new Date().toLocaleDateString('en-US', {
      weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    })}`,
    text: text
  };
  if (html) {
    body.html = html;
  }
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify(body)
  });

  if (!res.ok) {
    const err = await res.json();
    throw new Error(`Resend API error: ${err.message || JSON.stringify(err)}`);
  }
}

// -- Save to Obsidian --------------------------------------------------------

// Saves the digest to the user's Obsidian vault as a markdown file.
// Calls save-to-obsidian.js with the content and date.
function saveToObsidian(text, stats = null) {
  return new Promise((resolve, reject) => {
    const scriptPath = join(__dirname, 'save-to-obsidian.js');
    const args = ['--date', new Date().toISOString()];

    if (stats) {
      args.push('--stats', JSON.stringify(stats));
    }

    const child = spawn('node', [scriptPath, ...args], {
      stdio: ['pipe', 'pipe', 'pipe']
    });

    let stdout = '';
    let stderr = '';

    child.stdout.on('data', (data) => {
      stdout += data.toString();
    });

    child.stderr.on('data', (data) => {
      stderr += data.toString();
    });

    child.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(stderr || `save-to-obsidian.js exited with code ${code}`));
      } else {
        try {
          const result = JSON.parse(stdout);
          resolve(result);
        } catch (e) {
          resolve({ status: 'ok', message: stdout.trim() });
        }
      }
    });

    // Write content to stdin
    child.stdin.write(text);
    child.stdin.end();
  });
}

async function main() {
  // Load env and config
  loadEnv({ path: ENV_PATH });

  let config = {};
  if (existsSync(CONFIG_PATH)) {
    config = JSON.parse(await readFile(CONFIG_PATH, 'utf-8'));
  }

  const delivery = config.delivery || { method: 'stdout' };
  const digestText = await getDigestText();

  // Check for HTML file
  let htmlContent = null;
  const htmlFile = getHtmlFilePath();
  if (htmlFile && existsSync(htmlFile)) {
    htmlContent = await readFile(htmlFile, 'utf-8');
  }

  // Check for Markdown file (used for Obsidian save when emailHtml is enabled)
  let mdContent = null;
  const mdFile = getMdFilePath();
  if (mdFile && existsSync(mdFile)) {
    mdContent = await readFile(mdFile, 'utf-8');
  }

  if (!digestText || digestText.trim().length === 0) {
    console.log(JSON.stringify({ status: 'skipped', reason: 'Empty digest text' }));
    return;
  }

  try {
    let deliveryResult = null;

    switch (delivery.method) {
      case 'telegram': {
        const botToken = process.env.TELEGRAM_BOT_TOKEN;
        const chatId = delivery.chatId;
        if (!botToken) throw new Error('TELEGRAM_BOT_TOKEN not found in .env');
        if (!chatId) throw new Error('delivery.chatId not found in config.json');
        await sendTelegram(digestText, botToken, chatId);
        deliveryResult = {
          status: 'ok',
          method: 'telegram',
          message: 'Digest sent to Telegram'
        };
        break;
      }

      case 'email': {
        const apiKey = process.env.RESEND_API_KEY;
        const toEmail = delivery.email;
        if (!apiKey) throw new Error('RESEND_API_KEY not found in .env');
        if (!toEmail) throw new Error('delivery.email not found in config.json');
        await sendEmail(digestText, apiKey, toEmail, htmlContent);
        deliveryResult = {
          status: 'ok',
          method: 'email',
          message: `Digest sent to ${toEmail}`
        };
        break;
      }

      case 'stdout':
      default:
        // Just print to terminal — the agent or OpenClaw handles delivery
        console.log(digestText);
        deliveryResult = { status: 'ok', method: 'stdout' };
        break;
    }

    // Save to Obsidian if enabled (after main delivery)
    if (config.obsidian?.enabled) {
      try {
        const stats = config._stats || null; // Stats passed via config if available
        // Prefer dedicated Markdown content (--md flag) over plain text (--file flag)
        const obsidianText = (mdContent && mdContent.trim()) ? mdContent : digestText;
        const obsidianResult = await saveToObsidian(obsidianText, stats);
        if (deliveryResult) {
          deliveryResult.obsidian = obsidianResult;
        }
      } catch (obsidianErr) {
        // Log but don't fail the main delivery if Obsidian save fails
        if (deliveryResult) {
          deliveryResult.obsidian = { status: 'error', message: obsidianErr.message };
        }
      }
    }

    if (deliveryResult && delivery.method !== 'stdout') {
      console.log(JSON.stringify(deliveryResult));
    }

  } catch (err) {
    console.log(JSON.stringify({
      status: 'error',
      method: delivery.method,
      message: err.message
    }));
    process.exit(1);
  }
}

main();
