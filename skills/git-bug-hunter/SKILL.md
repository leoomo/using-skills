---
name: git-bug-hunter
description: |
  当用户说"深度分析BUG"、"深度排查 bug"时触发。

  利用 Git 高级功能排查代码 bug：git bisect 二分定位引入版本、reflog 恢复丢失代码、查看 recent commits 理解变化、解决 merge conflict、整理 Git mess。

  无论用户是否明确提到 Git，只要是在深度排查 bug，就应该激活此 skill。
---

# Git Bug Hunter

帮助用户使用 Git 工具高效排查代码 bug。

## 核心原则

Git 的历史记录是排查问题的利器。不要只在 bug 发生时才开始查看历史——主动利用 Git 的 bisect、reflog、log 等工具，可以让 bug 定位从"大海捞针"变成"按图索骥"。

## 工作流

### 1. 理解问题

首先明确：
- 什么症状？错误信息、崩溃日志、还是行为异常？
- 什么时候开始的？是否可以定位到某个版本/时间点？
- 是否有测试可以验证这个 bug 存在/消失？

### 2. 定位引入位置

如果知道 bug 在某个版本之前不存在、之后存在，用 `git bisect`：

**提示词：**
```
Use git bisect to find when this bug was introduced: <描述 bug 的测试条件>
```

Agent 会帮你：
- 设置二分查找的起止点
- 编写 bisect 脚本
- 执行二进制搜索
- 最终定位到第一个出现 bug 的 commit

**示例：**
- `Use git bisect to find when this bug was introduced: running 'npm test' fails with "Cannot read property 'id' of undefined"`
- `git bisect to find which commit broke the login feature`

### 3. 理解最近的改动

如果 bug 可能和最近的改动有关：

**提示词：**
```
Review changes made today
```
或
```
Show me recent changes / last three commits
```

这会让 agent 运行 `git log`，快速加载上下文：查看修改了哪些代码、commit message 描述了什么。

**为什么有用：** 很多时候 bug 就是最近几行代码的改动导致的。先看 recent changes 再决定是否需要更深入的 bisect。

### 4. 查找丢失的代码

如果代码"丢了"（没 commit、stash 了、或者在错误的 branch 上）：

**提示词：**
```
Find and recover my code that does <功能描述>
```

Agent 会搜索：
- `git reflog` — 查找本地操作历史
- `git stash list` — 查找 stash 的内容
- 其他 branches — 可能在别的 branch 上

### 5. 解决 Git Mess

如果遇到 merge conflict、rebase 失败、或者不知道怎么收拾的 Git 状态：

**提示词：**
```
Sort out this git mess for me
```

Agent 可以：
- 分析冲突的意图
- 决定保留什么、怎么合并
- 确保测试通过后再完成操作

## 常用提示词参考

| 场景 | 提示词 |
|------|--------|
| 定位 bug 引入点 | `Use git bisect to find when this bug was introduced: <测试条件>` |
| 查看今天改动 | `Review changes made today` |
| 查看最近 commits | `Show me recent changes / last three commits` |
| 找丢失代码 | `Find and recover my code that does <功能描述>` |
| 解决冲突 | `Sort out this git mess for me` |
| 回滚有问题的 commit | `Undo last commit` 或 `Revert the commit that introduced <bug>` |
