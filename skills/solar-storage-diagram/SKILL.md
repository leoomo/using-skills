---
name: solar-storage-diagram
description: 光储行业专用 diagram skill。用于创建太阳能+储能系统的架构图、电气单线图、ESS布局图。当用户提到光储系统、储能系统、ESS、PCS、STS、光伏系统图、微电网并离网、单线图时使用。
trigger: 光储|储能系统|ESS|PCS|STS|光伏.*图|微电网|单线图|架构图|德业|Deye|升压.*一体|液冷.*集装箱|光储.*系统|储能.*方案
parent: drawio
---

# 光储行业专用 draw.io Skill

本 skill 继承 `.claude/skills/drawio/SKILL.md` 的所有能力，专门针对太阳能+储能系统（光储系统）的可视化。

## 光储组件配色规范表

详细颜色规格和组件样式请参考：[references/components.md](references/components.md)

**快速参考：**
- 光伏组件：`#FFF2CC` / `#D6B656`
- 储能柜/ESS：`#DAE8FC` / `#6C8EBF`
- PCS/逆变器：`#E1D5E7` / `#9673A6`
- EMS/BMS：`#D5E8D4` / `#82B366`
- STS：`#FFE6CC` / `#D79B00`
- 负载：`#F8CECC` / `#B85450`

## 组件模板库

完整的光储组件 XML 模板，请参考：[references/components.md](references/components.md)

包含以下组件类别：
- 发电系统（光伏组件、光伏车棚）
- 储能系统（MC-L430、WS-L4300）
- 变换系统（组串逆变器、PCS）
- 控制系统（EMS、BMS）
- 切换系统（STS）
- 电网系统（变压器、开关、电网）
- 母线系统（交流母线、直流母线）
- 负载（园区负载、工业负载）
- 其他（消防、空调、柴发）

## 典型系统架构模板

5种典型光储系统架构的完整 XML 模板，请参考：[references/templates.md](references/templates.md)

| 模板名称 | 适用场景 | 电压等级 |
|---------|---------|---------|
| 并网光储系统（分体式） | 方案A - 10×MC-L430 | 400V |
| 并网光储系统（集装箱式） | 方案B - WS-L4300 | 690V |
| 离网光储系统 | 无电网场景 | 400V |
| 微电网系统（并离网切换） | 并网/离网切换 | 400V |
| 工商业光储系统(C&I) | 几百kW项目 | 400V |

## 电气单线图模板

6种电气单线图模板，请参考：[references/single-line-diagram.md](references/single-line-diagram.md)

| 模板名称 | 适用场景 | 电压等级 |
|---------|---------|---------|
| 低压并网单线图 | C&I项目 | 400V |
| 中压并网单线图 | 集装箱ESS项目 | 690V |
| 高压并网单线图 | 大型地面电站 | 10kV/20kV |
| 电池簇直流单线图 | BMS和电池簇详情 | 直流侧 |
| 并离网切换单线图 | STS切换逻辑 | 400V |
| 微电网单线图 | 多能源接入 | 400V |

## ESS内部布局模板

6种ESS内部布局模板，请参考：[references/ess-layout.md](references/ess-layout.md)

| 模板名称 | 适用场景 | 设备数量 |
|---------|---------|---------|
| 分体式ESS布局(5×2) | 10台MC-L430 | 10台 |
| 分体式ESS布局(3×4) | 12台MC-L430 | 12台 |
| 集装箱ESS内部布局 | WS-L4300 | 1台 |
| 电池簇详细布局 | 电池模组排列 | N/A |
| PCS堆叠布局 | 多台PCS并联 | N/A |
| ESS设备清单表格 | 项目设备统计 | N/A |

## 快速入门

### 创建光储架构图

1. 选择合适的系统模板（参考 references/templates.md）
2. 根据项目需求修改组件参数（容量、数量）
3. 调整布局和连接关系
4. 添加标注和说明文字

### 创建电气单线图

1. 选择电压等级对应的单线图模板
2. 填写具体的设备型号和参数
3. 确认保护配置和开关状态
4. 添加电气参数标注

### 创建ESS布局图

1. 选择分体式或集装箱式布局模板
2. 根据实际设备数量调整排列
3. 标注设备间距和安全通道
4. 添加设备清单表格

## 嵌入图片工作流

> **🔒 强制规则：图片字符串必须由脚本生成**
>
> Claude **禁止手动编写** `data:image/...` 格式字符串。所有图片嵌入必须通过 `drawio-tool.py` 脚本完成。
> 脚本已内置正确的 data URI 格式，无需人工记忆避坑规则。
>
> | 方式 | 命令 |
> |------|------|
> | 嵌入图片到文件 | `drawio-tool.py embed-image <drawio> <图片> <x> <y> <宽> <高>` |
> | 生成 XML 片段 | `drawio-tool.py prepare-xml <图片> <宽> <高> --x N --y N -o /tmp/xxx.xml` |
> | 生成 base64 | `drawio-tool.py prepare <图片> <宽> <高> -o /tmp/xxx.txt` |
> | 修复已有文件 | `drawio-tool.py fix-base64 <drawio>` |
> | 验证布局 | `drawio-tool.py validate <drawio>` |
>
> **所有中间产物（base64 txt、XML 片段等）必须输出到 `/tmp/`，禁止写入项目目录。**

> **⚠️ 背景知识：draw.io 的 `;base64` 陷阱**
>
> draw.io 的 style 属性用 `;` 作分隔符，标准 data URI 格式 `data:image/png;base64,<数据>` 中的 `;`
> 会被误拆导致图片不显示。脚本已自动使用 `data:image/png,<数据>` 格式（无分号），无需人工干预。
> 如遇已有文件图片不显示，运行 `drawio-tool.py fix-base64 <文件>` 一键修复。

当架构图中需要嵌入产品图片、设备照片等自定义图片时，使用 `references/drawio-tool.py` 工具链完成。

### 工具链概览

| 命令 | 用途 |
|------|------|
| `drawio-tool.py embed-image <drawio> <图片> <x> <y> <宽> <高>` | **通用图片嵌入**（直接写入drawio文件） |
| `drawio-tool.py validate <drawio文件> --min-gap 5` | 布局验证（重叠检测、容器包围检查） |
| `drawio-tool.py export <drawio文件> -o output.png` | SVG 中转导出（自动修复 base64 图片丢失） |

### 标准工作流（四步完成）

**第一步：创建架构图**
使用模板或手动创建架构图，组件用色块占位，后续替换为真实设备图片。

**第二步：规划图片位置**
图片尺寸建议：设备缩略图 50×70~80×100，集装箱全貌 250×90~280×100

**第三步：嵌入图片（通用命令）**

```bash
# 通用图片嵌入命令
python3 references/drawio-tool.py embed-image <drawio文件> <图片路径> <x> <y> <宽> <高> [--id <cell_id>]

# 示例：在 Ketzin 架构图中嵌入 MC-L430 设备图片
python3 references/drawio-tool.py embed-image \
    "06-方案文档/项目案例/Ketzin光储系统架构图_方案A.drawio" \
    "设备图片/MC-L430.png" \
    355 300 50 70 --id img_mc_1

# 批量嵌入（循环）：
for i in {1..10}; do
  x=$((355 + ($i-1) * 60))
  python3 references/drawio-tool.py embed-image \
    "diagram.drawio" "MC-L430.png" $x 300 50 70 --id "img_mc_$i"
done
```

**第四步：验证并导出**

```bash
# 验证布局
python3 references/drawio-tool.py validate diagram.drawio --min-gap 5

# 导出 PNG
python3 references/drawio-tool.py export diagram.drawio -o output.png --width 2400
```

### 第三步（续）：图片压缩问题排查与修复

生成 drawio 文件后，在导出前先验证布局：

```bash
python3 references/drawio-tool.py validate diagram.drawio --min-gap 5
```

自动检测：
- 非容器元素之间的重叠（同 parent 层级，间距 < min_gap）
- 子元素溢出容器边界
- 嵌入图片数据完整性（base64 是否过短或损坏）

### 第三步（续）：图片压缩问题排查与修复

**识别图片被压缩的症状：**
- 图片在 draw.io 中显示为小图标/占位图（而非照片）
- 嵌入的 base64 长度过短（如 < 10KB），但原图应该更大
- `<mxGeometry>` 中的尺寸远大于实际图片显示尺寸

**诊断方法：**
```python
import re, base64
with open('diagram.drawio', 'r') as f:
    content = f.read()

# 查找所有嵌入图片的 base64 长度
for match in re.finditer(r'data:image/(\w+)(?:;base64)?,([A-Za-z0-9+/=]+)', content):
    fmt, b64 = match.groups()
    decoded_len = len(base64.b64decode(b64))
    if decoded_len < 10000:  # 小于 10KB 说明可能是压缩图
        print(f"{fmt}: {len(b64)} chars ({decoded_len/1024:.1f} KB) - 可能被压缩")
```

**修复方法：**
1. 获取原始高质量图片文件
2. 用 `drawio-tool.py prepare` 生成完整 base64
3. 替换 drawio 文件中对应的被压缩 base64

```bash
# 示例：修复被压缩到 7KB 的缩略图
# 原图应该是 843x812 的 PNG/JPEG
python3 references/drawio-tool.py prepare /path/to/original.jpg 843 812 -o full_b64.txt
# 然后用文本编辑器替换 drawio 文件中的短 base64
```

### 第四步：导出（SVG 中转法）

**已知问题：** draw.io 桌面版 CLI 导出时可能丢失 style 中的 base64 图片数据。在 draw.io 编辑器中显示正常，但 CLI 导出为空白。

**解决：** 使用 `drawio-tool.py export`，自动完成 SVG 中转导出：

```bash
python3 references/drawio-tool.py export diagram.drawio -o output.png --width 2400
```

工具自动执行：drawio→SVG导出 → 提取base64 → 注入SVG → rsvg-convert转PNG

**依赖：**
- Pillow: `pip install Pillow`
- rsvg-convert: `brew install librsvg` (macOS) / `apt install librsvg2-bin` (Linux)
- draw.io 桌面版: https://github.com/jgraph/drawio-desktop/releases

### 第四步：验证

- 检查 `validate` 输出无报错
- 检查导出 PNG 中图片显示为实际内容（非空白）
- 检查图片与相邻组件无重叠（间距 ≥ 5px）
- 检查容器框包围所有子元素

## 故障排查

| 问题 | 原因 | 解决 |
|------|------|------|
| **图片完全不显示**（编辑器内+导出） | `;base64` 格式导致 draw.io 解析错误 | 运行 `drawio-tool.py fix-base64 <drawio>` 自动修复 |
| CLI 导出图片空白 | draw.io CLI 导出丢失 base64 | 用 `drawio-tool.py export`（SVG 中转法） |
| 图片显示为小图标/占位图 | draw.io 导入时自动压缩图片 | 重新嵌入原始完整分辨率图片 |
| 图片与组件遮挡 | y 坐标计算错误，间距不足 | 用 `drawio-tool.py validate` 检测重叠 |
| PIL 保存 PNG 崩溃 | CMYK/RGBA/灰度模式不兼容 PNG | `drawio-tool.py` 自动 convert('RGB') |
| 导出后图片位置偏移 | 图片 width/height 与 mxGeometry 不一致 | 确保预缩放尺寸一致 |
| draw.io CLI 找不到 | 未安装桌面版 | 安装或保留 .drawio 文件手动导出 |
| rsvg-convert 找不到 | 未安装 librsvg | `brew install librsvg` 或 `apt install librsvg2-bin` |
| base64 过短导致图片模糊 | 图片被压缩到 < 10KB | 用原图重新生成完整 base64 |

## 旧脚本兼容

`references/export-with-images.py` 为旧版独立导出脚本，已被 `drawio-tool.py export` 取代。保留以兼容旧流程，新项目请使用 `drawio-tool.py`。
