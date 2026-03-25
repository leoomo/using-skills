---
name: chrome-ext-expert
description: Use this skill when developing Google Chrome extensions (Manifest V3), including chrome.* APIs, manifest.json, service workers, content scripts, extension permissions, or debugging chrome://extensions.
version: 1.1.0
---

# Chrome Extension Developer Skill (Manifest V3)

当你被要求开发、重构或调试 Chrome 插件时，请严格遵守以下规则：

## 1. 核心架构准则
- **强制 Manifest V3**: 严禁使用 Manifest V2。必须包含 `manifest_version: 3`。
- **Service Worker 代替 Background**: 必须使用 `background.service_worker`，且代码必须是异步且非持久的。
- **安全性**: 严禁使用 `eval()` 或从外部服务器加载远程代码。所有逻辑必须在包内。

## 2. 通信模式
- **消息传递**: 优先使用 `chrome.runtime.sendMessage` 和 `chrome.tabs.sendMessage`。
- **端口通信**: 对于频繁通信，使用 `chrome.runtime.connect`。
- **异步处理**: 确保 `onMessage` 监听器在需要异步响应时返回 `true`。

## 3. 常用 API 规范
- **Storage**: 优先使用 `chrome.storage.local` 或 `sync`。
- **Action**: 使用 `action` 字段配置图标和 Popup，而非 `browser_action` 或 `page_action`.
- **Permissions**: 仅请求实现功能所需的最小权限（Principle of Least Privilege）。

## 4. 调试与工作流
- 在提供代码后，指导用户：
  1. 打开 `chrome://extensions`。
  2. 开启"开发者模式"。
  3. 点击"加载已解压的扩展程序"。
- 如果涉及 DOM 操作，优先检查 `content_scripts` 的注入时机（如 `document_idle`）。

## 5. 常见陷阱检查
- 检查 `web_accessible_resources` 是否配置了需要被页面访问的资源。
- 检查 `permissions` 与代码中使用的 API 是否匹配。
- 检查 Content Script 与 Service Worker 之间的 `isTrusted` 事件验证。

## 6. Manifest V3 完整模板

```json
{
  "manifest_version": 3,
  "name": "Extension Name",
  "version": "1.0.0",
  "description": "Extension description",
  "permissions": ["storage", "activeTab"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "run_at": "document_idle"
    }
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  }
}
```

## 7. 消息通信模板

### Content Script → Background
```javascript
// content.js
chrome.runtime.sendMessage({ type: 'ACTION', data: payload }, (response) => {
  if (chrome.runtime.lastError) {
    console.error('Message failed:', chrome.runtime.lastError);
    return;
  }
  console.log('Response:', response);
});

// background.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'ACTION') {
    // 异步操作必须返回 true
    doAsyncWork().then(sendResponse);
    return true;
  }
});
```

### Background → Content Script
```javascript
// background.js
chrome.tabs.sendMessage(tabId, { type: 'UPDATE', data: payload });

// content.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'UPDATE') {
    // 处理消息
  }
});
```

## 8. Content Security Policy (CSP) 最佳实践

### CSP 限制说明

Chrome 扩展默认 CSP:
- `script-src: 'self'` - 仅允许加载本地脚本
- 禁止从外部 CDN 加载脚本
- 禁止使用 `eval()` 和内联脚本

### 本地化最佳实践

**✅ 推荐: 将库下载到本地**
```bash
# 使用 curl 下载到扩展目录
curl -o popup/marked.min.js https://cdn.jsdelivr.net/npm/marked/marked.min.js
```

**✅ 小功能建议手写**
- 如: `escapeHtml()`, `formatDate()` 等工具函数
- 减少依赖，提升加载速度

**❌ 避免: 外部 CDN 链接**
```html
# 错误 - 会违反 CSP
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

# 正确 - 使用本地文件
<script src="marked.min.js"></script>
```

### 安全建议

- **指定精确版本号**: 使用 `@1.2.3` 而非 `@latest`
  ```bash
  curl -o lib.min.js https://cdn.jsdelivr.net/npm/lib@1.2.3/lib.min.js
  ```
- **定期检查更新**: 使用 `npm outdated` 查看库更新
- **验证文件完整性**: `sha256sum lib.min.js`

### 常见库本地化示例

```bash
# marked.js (Markdown 渲染)
curl -o popup/marked.min.js https://cdn.jsdelivr.net/npm/marked/marked.min.js

# highlight.js (代码高亮)
curl -o popup/highlight.min.js https://cdn.jsdelivr.net/npm/highlight.js/lib/common.min.js

# marked + highlight (带高亮的 Markdown)
curl -o popup/marked.min.js https://cdn.jsdelivr.net/npm/marked/marked.min.js
curl -o popup/highlight.min.js https://cdn.jsdelivr.net/npm/highlight.js/lib/common.min.js
```
