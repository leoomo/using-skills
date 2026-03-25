---
name: design-taste-frontend
description: Senior UI/UX Engineer. Architect digital interfaces overriding default LLM biases. Enforces metric-based rules, strict component architecture, CSS hardware acceleration, and balanced design engineering.
version: 1.0.0
---

# High-Agency Frontend Skill

当你被要求开发高质量 Web 前端界面时，请严格遵循以下规则。

## 1. ACTIVE BASELINE CONFIGURATION

* DESIGN_VARIANCE: 8 (1=Perfect Symmetry, 10=Artsy Chaos)
* MOTION_INTENSITY: 6 (1=Static/No movement, 10=Cinematic/Magic Physics)
* VISUAL_DENSITY: 4 (1=Art Gallery/Airy, 10=Pilot Cockpit/Packed Data)

**AI Instruction:** 标准基线严格设为这些值 (8, 6, 4)。除非用户在聊天中明确要求调整，否则始终使用这些值作为全局变量来驱动第 3-7 节的特定逻辑。

## 2. DEFAULT ARCHITECTURE & CONVENTIONS

除非用户明确指定不同技术栈，否则必须遵守以下结构约束：

* **依赖验证 [强制]:** 导入任何第三方库前（如 `framer-motion`, `lucide-react`, `zustand`），必须先检查 `package.json`。如果缺少，必须先输出安装命令再提供代码。**永远不要**假设库已存在。
* **框架与交互性:** React 或 Next.js。默认使用 Server Components (`RSC`)。
    * **RSC 安全性:** 全局状态仅在 Client Components 中有效。在 Next.js 中，用 `"use client"` 组件包装 providers。
    * **交互隔离:** 如果第 4 或 7 节（Motion/Liquid Glass）启用，特定交互 UI 组件必须提取为独立叶子组件，文件顶部必须有 `'use client'`。Server Components 必须仅渲染静态布局。
* **状态管理:** 对隔离 UI 使用本地 `useState`/`useReducer`。全局状态仅用于避免深层 prop drilling。
* **样式策略:** 90% 样式使用 Tailwind CSS (v3/v4)。
    * **Tailwind 版本锁定:** 先检查 `package.json`。不要在 v3 项目中使用 v4 语法。
    * **T4 配置守卫:** v4 不要在 `postcss.config.js` 中使用 `tailwindcss` 插件。使用 `@tailwindcss/postcss` 或 Vite 插件。
* **禁用表情符号 [关键]:** 代码、标记、文本内容或 alt 文本中**永远不要**使用表情符号。用高质量图标（Radix, Phosphor）或纯 SVG 图元替换。表情符号被禁止。
* **响应式与间距:**
  * 标准化断点 (`sm`, `md`, `lg`, `xl`)。
  * 使用 `max-w-[1400px] mx-auto` 或 `max-w-7xl` 约束页面布局。
  * **视口稳定性 [关键]:** 全高度 Hero 部分**永远不要**使用 `h-screen`。始终使用 `min-h-[100dvh]` 防止移动端浏览器（iOS Safari）灾难性布局跳动。
  * **Grid 优先于 Flex 计算:** **永远不要**使用复杂 flexbox 百分比计算 (`w-[calc(33%-1rem)]`)。始终使用 CSS Grid (`grid grid-cols-1 md:grid-cols-3 gap-6`) 构建可靠结构。
* **图标:** 必须使用 `@phosphor-icons/react` 或 `@radix-ui/react-icons` 作为导入路径（检查已安装版本）。全局标准化 `strokeWidth`（例如专门使用 `1.5` 或 `2.0`）。

## 3. DESIGN ENGINEERING DIRECTIVES (Bias Correction)

LLM 对特定 UI 陈词滥调模式有统计偏见。主动使用以下工程规则构建高级界面：

### Rule 1: Deterministic Typography
* **Display/Headlines:** 默认使用 `text-4xl md:text-6xl tracking-tighter leading-none`。
    * **反垃圾:** 不鼓励使用 `Inter` 来表达 "Premium" 或 "Creative"。强制使用独特字符：`Geist`, `Outfit`, `Cabinet Grotesk`, 或 `Satoshi`。
    * **技术 UI 规则:** 仪表盘/软件 UI **严格禁止**使用衬线字体。使用高级无衬线字体配对（`Geist` + `Geist Mono` 或 `Satoshi` + `JetBrains Mono`）。
* **Body/Paragraphs:** 默认使用 `text-base text-gray-600 leading-relaxed max-w-[65ch]`。

### Rule 2: Color Calibration
* **约束:** 最多 1 个强调色。饱和度 < 80%。
* **紫色禁令:** "AI Purple/Blue" 美学**严格禁止**。不要紫色按钮光晕，不要霓虹渐变。使用绝对中性基底（Zinc/Slate）+ 高对比度单一强调色（例如 Emerald、Electric Blue 或 Deep Rose）。
* **色彩一致性:** 整个输出坚持一种调色板。不要在同一项目中在暖灰和冷灰之间波动。

### Rule 3: Layout Diversification
* **反中心偏见:** 当 `LAYOUT_VARIANCE > 4` 时，**严格禁止**居中 Hero/H1 部分。强制使用 "Split Screen"（50/50）、"左对齐内容/右对齐素材" 或 "非对称留白" 结构。

### Rule 4: Materiality, Shadows, and "Anti-Card Overuse"
* **仪表盘加固:** 当 `VISUAL_DENSITY > 7` 时，**严格禁止**使用通用卡片容器。通过 `border-t`、`divide-y` 或纯负空间进行逻辑分组。数据指标应呼吸，除非需要 z-index 功能性提升，否则不要装框。
* **执行:** 仅当阴影传达层级时才使用卡片。使用阴影时，着色到背景色调。

### Rule 5: Interactive UI States
* **强制生成:** LLM 自然生成"静态"成功状态。必须实现完整交互周期：
  * **Loading:** 骨架加载器匹配布局大小（避免通用圆形旋转器）。
  * **Empty States:** 精美组合的空状态，指示如何填充数据。
  * **Error States:** 清晰的内联错误报告（例如表单）。
  * **触感反馈:** 在 `:active` 时，使用 `-translate-y-[1px]` 或 `scale-[0.98]` 模拟表示成功/动作的物理按压。

### Rule 6: Data & Form Patterns
* **表单:** 标签必须位于输入框上方。辅助文本可选但应存在于标记中。错误文本在输入框下方。对输入块使用标准 `gap-2`。

## 4. CREATIVE PROACTIVITY (Anti-Slop Implementation)

主动对抗通用 AI 设计，系统性实施以下高端编码概念作为基线：

* **"Liquid Glass" 折射:** 需要毛玻璃时，超越 `backdrop-blur`。添加 1px 内边框（`border-white/10`）和微妙内阴影（`shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]`）模拟物理边缘折射。
* **磁性微物理 (如果 MOTION_INTENSITY > 5):** 实现按钮轻微向光标拉动。**关键:** 磁性悬停或连续动画**永远不要**使用 React `useState`。**仅使用** Framer Motion 的 `useMotionValue` 和 `useTransform` 在 React 渲染周期外，防止移动端性能崩溃。
* **持续微交互:** 当 `MOTION_INTENSITY > 5` 时，在标准组件（头像、状态点、背景）中嵌入连续、无限微动画（Pulse、Typewriter、Float、Shimmer、Carousel）。对所有交互元素应用高级弹簧物理（`type: "spring", stiffness: 100, damping: 20`）—— 无线性缓动。
* **布局转换:** 始终使用 Framer Motion 的 `layout` 和 `layoutId` props 实现状态变化时的平滑重新排序、调整大小和共享元素转换。
* **交错编排:** 不要立即挂载列表或网格。使用 `staggerChildren`（Framer）或 CSS 级联（`animation-delay: calc(var(--index) * 100ms)`）创建顺序瀑布式揭示。**关键:** 对于 `staggerChildren`，父级（`variants`）和子级必须位于相同的 Client Component 树中。

## 5. PERFORMANCE GUARDRAILS

* **DOM 成本:** 仅对固定的、pointer-event-none 伪元素应用噪点/颗粒滤镜（例如 `fixed inset-0 z-50 pointer-events-none`），**永远不要**对滚动容器使用，防止移动端 GPU 重绘和性能退化。
* **硬件加速:** **永远不要**动画化 `top`、`left`、`width` 或 `height`。仅通过 `transform` 和 `opacity` 动画化。
* **Z-Index 约束:** **永远不要**随意滥用 `z-50` 或 `z-10`。严格将 z-index 用于系统层上下文（Sticky Navbars、Modals、Overlays）。

## 6. TECHNICAL REFERENCE (Dial Definitions)

### DESIGN_VARIANCE (Level 1-10)
* **1-3 (Predictable):** Flexbox `justify-center`，严格 12 列对称网格，相等内边距。
* **4-7 (Offset):** 使用 `margin-top: -2rem` 重叠，不同图片纵横比（例如 4:3 旁 16:9），左对齐标题在居中数据上。
* **8-10 (Asymmetric):** Masonry 布局，带分数单位的 CSS Grid（例如 `grid-template-columns: 2fr 1fr 1fr`），大量留白区域（`padding-left: 20vw`）。
* **移动端覆盖:** 对于 4-10 级，任何 `md:` 以上的非对称布局**必须**在 < 768px 视口上强制回退到严格单列布局（`w-full`, `px-4`, `py-8`），防止水平滚动和布局破坏。

### MOTION_INTENSITY (Level 1-10)
* **1-3 (Static):** 无自动动画。仅 CSS `:hover` 和 `:active` 状态。
* **4-7 (Fluid CSS):** 使用 `transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`。使用 `animation-delay` 级联加载。严格聚焦 `transform` 和 `opacity`。谨慎使用 `will-change: transform`。
* **8-10 (Advanced Choreography):** 复杂滚动触发揭示或视差。使用 Framer Motion hooks。**永远不要**使用 `window.addEventListener('scroll')`。

### VISUAL_DENSITY (Level 1-10)
* **1-3 (Art Gallery Mode):** 大量留白。巨大的分区间距。一切都非常昂贵和干净。
* **4-7 (Daily App Mode):** 标准 Web 应用的正常间距。
* **8-10 (Cockpit Mode):** 微小内边距。无卡片框；仅用 1px 线条分隔数据。一切都紧凑。**强制:** 所有数字使用等宽字体（`font-mono`）。

## 7. THE 100 AI TELLS (Forbidden Patterns)

保证高端、非通用输出，**必须严格避免**以下常见 AI 设计签名，除非用户明确要求：

### Visual & CSS
* **NO Neon/Outer Glows:** 不要使用默认 `box-shadow` 光晕或自动光晕。使用内边框或微妙着色阴影。
* **NO Pure Black:** **永远不要**使用 `#000000`。使用 Off-Black、Zinc-950 或 Charcoal。
* **NO Oversaturated Accents:** 取消强调色饱和度与中性色优雅融合。
* **NO Excessive Gradient Text:** 大标题不要使用文本填充渐变。
* **NO Custom Mouse Cursors:** 它们已过时并破坏性能/可访问性。

### Typography
* **NO Inter Font:** 禁止。使用 `Geist`、`Outfit`、`Cabinet Grotesk` 或 `Satoshi`。
* **NO Oversized H1s:** 第一个标题不应大喊。通过字重和颜色控制层级，而不仅仅是巨大比例。
* **Serif Constraints:** 衬线字体**仅用于**创意/社论设计。**永远不要**在干净仪表盘上使用衬线。

### Layout & Spacing
* **Align & Space Perfectly:** 确保填充和边距数学上完美。避免带有尴尬间隙的浮动元素。
* **NO 3-Column Card Layouts:** 通用"3 等分卡片水平"特性行**被禁止**。使用 2 列 Zig-Zag、非对称网格或水平滚动方法。

### Content & Data (The "Jane Doe" Effect)
* **NO Generic Names:** "John Doe"、"Sarah Chan" 或 "Jack Su" 被禁止。使用高度创意、真实的名称。
* **NO Generic Avatars:** **不要**使用标准 SVG "蛋"或 Lucide 用户图标作为头像。使用创意、可信的照片占位符或特定样式。
* **NO Fake Numbers:** 避免可预测输出如 `99.99%`、`50%` 或基本电话号码 (`1234567`)。使用有机的、杂乱的数据（`47.2%`, `+1 (312) 847-1928`）。
* **NO Startup Slop Names:** "Acme"、"Nexus"、"SmartFlow"。发明高级、语境品牌名称。
* **NO Filler Words:** 避免 AI 文案陈词滥调如 "Elevate"、"Seamless"、"Unleash" 或 "Next-Gen"。使用具体动词。

### External Resources & Components
* **NO Broken Unsplash Links:** 不要使用 Unsplash。使用绝对可靠的占位符如 `https://picsum.photos/seed/{random_string}/800/600` 或 SVG UI 头像。
* **shadcn/ui Customization:** 可以使用 `shadcn/ui`，但**永远不要**在其通用默认状态中。**必须**自定义半径、颜色和阴影以匹配高端项目美学。
* **生产就绪清洁度:** 代码必须非常干净、视觉震撼、令人难忘并在每个细节上精心打磨。

## 8. THE CREATIVE ARSENAL (High-End Inspiration)

不要默认使用通用 UI。适当从这个高级概念库中汲取，确保输出视觉震撼和令人难忘。适当时利用 **GSAP (ScrollTrigger/Parallax)** 进行复杂滚动讲述或 **ThreeJS/WebGL** 进行 3D/Canvas 动画，而不是基本 CSS 动画。**关键:** 不要在同一组件树中混合 GSAP/ThreeJS 和 Framer Motion。默认将 Framer Motion 用于 UI/Bento 交互。仅将 GSAP/ThreeJS **专门用于**隔离的全页滚动讲述或画布背景，用严格的 useEffect 清理块包装。

### The Standard Hero Paradigm
* 停止做深色图片上的居中文字。尝试非对称 Hero 部分：文字干净左对齐或右对齐。背景应展示高质量、相关图片，带微妙风格淡入淡出（根据是浅色还是深色模式优雅地变暗或变亮）。

### Navigation & Menus
* **Mac OS Dock Magnification:** 导航栏在边缘；图标在悬停时流体缩放。
* **Magnetic Button:** 按钮物理向光标拉动。
* **Gooey Menu:** 子项目像粘性液体一样从主按钮脱离。
* **Dynamic Island:** 药丸形 UI 组件变形以显示状态/警报。
* **Contextual Radial Menu:** 圆形菜单在点击坐标处展开。
* **Floating Speed Dial:** 一个 FAB 弹出一个曲线次要动作。
* **Mega Menu Reveal:** 全屏下拉菜单交错淡入复杂内容。

### Layout & Grids
* **Bento Grid:** 非对称、基于瓦片的分组（例如 Apple Control Center）。
* **Masonry Layout:** 无固定行高的交错网格（例如 Pinterest）。
* **Chroma Grid:** 网格边框或瓦片显示微妙、持续动画的颜色渐变。
* **Split Screen Scroll:** 两个屏幕半部分在滚动时向相反方向滑动。
* **Curtain Reveal:** 一个 Hero 部分在滚动时像窗帘一样在中间分开。

### Cards & Containers
* **Parallax Tilt Card:** 跟踪光标坐标的 3D 倾斜卡片。
* **Spotlight Border Card:** 卡片边框在光标下动态照亮。
* **Glassmorphism Panel:** 带内折射边框的真正磨砂玻璃。
* **Holographic Foil Card:** 悬停时彩虹光反射的彩虹色薄膜。
* **Tinder Swipe Stack:** 用户可以滑走的物理卡片堆叠。
* **Morphing Modal:** 一个按钮无缝扩展到其自己的全屏对话框容器。

### Scroll-Animations
* **Sticky Scroll Stack:** 卡片粘在顶部并物理相互堆叠。
* **Horizontal Scroll Hijack:** 垂直滚动转化为平滑的水平画廊平移。
* **Locomotive Scroll Sequence:** 帧率直接绑定到滚动条的视频/3D 序列。
* **Zoom Parallax:** 中心背景图片在滚动时无缝放大/缩小。
* **Scroll Progress Path:** SVG 矢量线条或路径在用户滚动时自行绘制。
* **Liquid Swipe Transition:** 页面转换像粘性液体一样擦除屏幕。

### Galleries & Media
* **Dome Gallery:** 感觉像全景穹顶的 3D 画廊。
* **Coverflow Carousel:** 中心聚焦、边缘向后倾斜的 3D 轮播。
* **Drag-to-Pan Grid:** 用户可以自由拖动到任何方向的无限网格。
* **Accordion Image Slider:** 悬停时完全展开的窄垂直/水平图像条。
* **Hover Image Trail:** 鼠标在身后留下弹出/淡出的图像痕迹。
* **Glitch Effect Image:** 悬停时短暂的 RGB 通道偏移数字失真。

### Typography & Text
* **Kinetic Marquee:** 无限文本带在滚动时反向或加速。
* **Text Mask Reveal:** 大排版作为视频背景的透明窗口。
* **Text Scramble Effect:** 加载或悬停时矩阵式字符解码。
* **Circular Text Path:** 沿旋转圆形路径弯曲的文本。
* **Gradient Stroke Animation:** 带沿笔划连续运行的渐变的轮廓文本。
* **Kinetic Typography Grid:** 一个字母网格躲避或旋转远离光标。

### Micro-Interactions & Effects
* **Particle Explosion Button:** 成功时瓦解成粒子的 CTA。
* **Liquid Pull-to-Refresh:** 移动重新加载指示器像分离的水滴一样行动。
* **Skeleton Shimmer:** 骨架加载器跨越占位符框移动光反射。
* **Directional Hover Aware Button:** 悬停填充从鼠标进入的确切侧面进入。
* **Ripple Click Effect:** 视觉波浪从点击坐标精确涟漪。
* **Animated SVG Line Drawing:** 矢量实时绘制自己的轮廓。
* **Mesh Gradient Background:** 有机的 lava-lamp 风格动画色块。
* **Lens Blur Depth:** 动态聚焦模糊背景 UI 层以突出前景动作。

## 9. THE "MOTION-ENGINE" BENTO PARADIGM

生成现代 SaaS 仪表盘或特性部分时，**必须**使用以下 "Bento 2.0" 架构和运动理念。这超越了静态卡片，强制执行 "Vercel-core meets Dribbble-clean" 美学，严重依赖持续物理。

### A. Core Design Philosophy
* **Aesthetic:** 高端、简约、功能性。
* **Palette:** 背景 `#f9fafb`。卡片纯白（`#ffffff`）带 1px 边框 `border-slate-200/50`。
* **Surfaces:** 所有主要容器使用 `rounded-[2.5rem]`。应用 "diffusion shadow"（非常浅的宽散布阴影，例如 `shadow-[0_20px_40px_-15px_rgba(0,0,0,0,05)]`）创造深度而不杂乱。
* **Typography:** 严格使用 `Geist`、`Satoshi` 或 `Cabinet Grotesk` 字体栈。标题使用微妙字间距（`tracking-tight`）。
* **Labels:** 标题和描述必须放置在卡片**外部和下方**以保持干净的画廊风格呈现。
* **Pixel-Perfection:** 卡片内使用慷慨的 `p-8` 或 `p-10` 内边距。

### B. The Animation Engine Specs (Perpetual Motion)
所有卡片必须包含**"持续微交互"**。使用以下 Framer Motion 原则：
* **Spring Physics:** 无线性缓动。使用 `type: "spring", stiffness: 100, damping: 20` 获得高级、有重量感。
* **Layout Transitions:** 大量利用 `layout` 和 `layoutId` props 确保平滑重新排序、调整大小和共享元素状态转换。
* **Infinite Loops:** 每个卡片必须有"活动状态"无限循环（Pulse、Typewriter、Float 或 Carousel）确保仪表盘"活着"。
* **Performance:** 将动态列表包装在 `<AnimatePresence>` 中并优化 60fps。**性能关键:** 任何持续运动或无限循环**必须**被记忆化（React.memo）并完全隔离在其自己的微观 Client Component 中。永远不要在父级布局中触发重新渲染。

### C. The 5-Card Archetypes (Micro-Animation Specs)
构建 Bento 网格时实施以下特定微动画（例如，第 1 行：3 列 | 第 2 行：2 列 70/30 分裂）：
1. **The Intelligent List:** 一个垂直堆叠项目，无限自动排序循环。项使用 `layoutId` 交换位置，模拟 AI 实时优先处理任务。
2. **The Command Input:** 一个带多步打字机效果的研究/AI 栏。它循环复杂提示，包括闪烁光标和带闪光加载梯度的"处理"状态。
3. **The Live Status:** 一个带"呼吸"状态指示器的调度界面。包含一个弹出通知徽章，以"Overshoot"弹簧效果出现，停留 3 秒，然后消失。
4. **The Wide Data Stream:** 一个水平"无限轮播"的数据卡或指标。确保循环无缝（使用 `x: ["0%", "-100%"]`），速度感觉毫不费力。
5. **The Contextual UI (Focus Mode):** 一个文档视图，动画显示文本块的交错高亮，然后是浮动操作工具栏与微图标"浮动进入"。

## 10. FINAL PRE-FLIGHT CHECK

输出前根据此矩阵评估你的代码。这是**最后**你应用于逻辑的过滤器。
- [ ] 全局状态是否适当用于避免深层 prop drilling 而不是随意？
- [ ] 高方差设计的移动端布局折叠（`w-full`, `px-4`, `max-w-7xl mx-auto`）是否保证？
- [ ] 全高度部分是否安全使用 `min-h-[100dvh]` 而不是有 bug 的 `h-screen`？
- [ ] `useEffect` 动画是否包含严格的清理函数？
- [ ] 是否提供了空、加载和错误状态？
- [ ] 是否在可能的情况下用间距代替卡片？
- [ ] 是否严格将 CPU 重度持续动画隔离在它们自己的 Client Components 中？
