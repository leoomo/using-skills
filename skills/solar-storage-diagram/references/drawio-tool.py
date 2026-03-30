#!/usr/bin/env python3
"""
draw.io 光储架构图工具链

统一处理带嵌入产品图片的 draw.io 文件：图片预处理、布局验证、SVG中转导出。

用法:
  drawio-tool.py prepare <image_path> <width> <height>  [-o output.txt]
  drawio-tool.py validate <drawio_path> [--min-gap N]
  drawio-tool.py export <drawio_path> [-o output.png] [--width N]

依赖:
  - Python 3.8+
  - Pillow (pip install Pillow)
  - rsvg-convert (brew install librsvg / apt install librsvg2-bin)
  - draw.io 桌面版 CLI (https://github.com/jgraph/drawio-desktop/releases)
"""
import sys
import os
import re
import base64
import io
import argparse
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow not installed. Run: pip install Pillow")
    sys.exit(1)


# ---------------------------------------------------------------------------
# 图片预处理
# ---------------------------------------------------------------------------

def image_to_b64(image_path: str, width: int, height: int) -> str:
    """将任意图片缩放到目标尺寸并转为 PNG base64。

    自动处理 CMYK、RGBA、灰度等图片模式，统一转为 RGB。
    """
    img = Image.open(image_path)

    # 统一转为 RGB（处理 CMYK/RGBA/灰度/P 等模式）
    if img.mode != 'RGB':
        img = img.convert('RGB')

    img = img.resize((width, height), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


def cmd_prepare(args):
    """prepare 子命令：图片预处理并输出 base64。"""
    if not os.path.isfile(args.image):
        print(f"ERROR: Image not found: {args.image}")
        sys.exit(1)

    b64 = image_to_b64(args.image, args.width, args.height)
    char_count = len(b64)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(b64)
        print(f"Base64 saved to {args.output} ({char_count} chars)")
    else:
        # 输出可直接嵌入 drawio XML 的 base64
        print(b64)


def cmd_prepare_xml(args):
    """生成可直接粘贴到 drawio XML 的 mxCell 代码。"""
    if not os.path.isfile(args.image):
        print(f"ERROR: Image not found: {args.image}")
        sys.exit(1)

    b64 = image_to_b64(args.image, args.width, args.height)
    cell_id = args.cell_id or f"img_{Path(args.image).stem}"

    xml = (
        f'<mxCell id="{cell_id}" value="" '
        f'style="image;verticalLabelPosition=bottom;verticalAlign=top;'
        f'aspect=fixed;image=data:image/png,{b64}" '
        f'vertex="1" parent="1">\n'
        f'  <mxGeometry x="{args.x}" y="{args.y}" '
        f'width="{args.width}" height="{args.height}" as="geometry"/>\n'
        f'</mxCell>'
    )

    if args.output:
        with open(args.output, 'w') as f:
            f.write(xml)
        print(f"XML cell saved to {args.output}")
    else:
        print(xml)


def get_max_id(tree: ET.ElementTree) -> int:
    """从drawio XML中查找最大ID。"""
    max_id = 1
    for elem in tree.getroot().iter():
        eid = elem.get('id', '')
        if eid:
            try:
                max_id = max(max_id, int(eid))
            except ValueError:
                pass
    return max_id


def cmd_embed_image(args):
    """直接向drawio文件中嵌入图片（通用步骤）。

    用法:
      drawio-tool.py embed-image <drawio_path> <image_path> <x> <y> <width> <height> [--id <cell_id>]
    """
    if not os.path.isfile(args.drawio):
        print(f"ERROR: Drawio file not found: {args.drawio}")
        sys.exit(1)

    if not os.path.isfile(args.image):
        print(f"ERROR: Image not found: {args.image}")
        sys.exit(1)

    # 处理图片：转为base64
    b64 = image_to_b64(args.image, args.width, args.height)

    # 读取drawio文件（用于查找最大ID）
    tree = ET.parse(args.drawio)
    max_id = get_max_id(tree)
    cell_id = args.cell_id or f"img_{max_id + 1}"

    # 读取文件内容作为文本
    with open(args.drawio, 'r', encoding='utf-8') as f:
        content = f.read()

    # 构建mxCell XML（使用 shape=image 格式，这是 draw.io 正确显示图片的必要条件）
    mxcell_xml = f'''    <mxCell id="{cell_id}" value="" style="shape=image;image=data:image/png,{b64};verticalLabelPosition=bottom;verticalAlign=top;aspect=fixed" vertex="1" parent="1">
      <mxGeometry x="{args.x}" y="{args.y}" width="{args.width}" height="{args.height}" as="geometry" />
    </mxCell>
'''

    # 在 </root> 前插入新元素
    if '</root>' in content:
        content = content.replace('</root>', mxcell_xml + '  </root>')
    else:
        print(f"ERROR: Invalid drawio file - missing </root> tag")
        sys.exit(1)

    # 写回文件
    with open(args.drawio, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Embedded: {args.image}')
    print(f'  -> Cell ID: {cell_id}')
    print(f'  -> Position: ({args.x}, {args.y})')
    print(f'  -> Size: {args.width} x {args.height}')
    print(f'  -> File: {args.drawio}')


# ---------------------------------------------------------------------------
# 布局验证
# ---------------------------------------------------------------------------

def parse_geometry(drawio_path: str) -> list:
    """解析 drawio 文件，提取所有元素的几何信息。

    返回: [{id, value, x, y, w, h, parent, style}, ...]
    """
    tree = ET.parse(drawio_path)
    elements = []
    for elem in tree.getroot().iter():
        eid = elem.get('id', '')
        if not eid or eid in ('0', '1'):
            continue

        geo = elem.find('mxGeometry')
        if geo is None:
            continue

        x = float(geo.get('x', 0))
        y = float(geo.get('y', 0))
        w = float(geo.get('width', 0))
        h = float(geo.get('height', 0))

        if w == 0 and h == 0:
            continue

        elements.append({
            'id': eid,
            'value': elem.get('value', '')[:30],
            'x': x, 'y': y, 'w': w, 'h': h,
            'parent': elem.get('parent', ''),
            'style': elem.get('style', ''),
        })

    return elements


def bounds_overlap(a, b, min_gap=5):
    """检查两个矩形是否重叠（含最小间距要求）。"""
    return not (a['x'] + a['w'] + min_gap <= b['x'] or
                b['x'] + b['w'] + min_gap <= a['x'] or
                a['y'] + a['h'] + min_gap <= b['y'] or
                b['y'] + b['h'] + min_gap <= a['y'])


def is_container(elem):
    """判断元素是否为容器（虚线框或包含子元素的大矩形）。"""
    style = elem.get('style', '')
    return ('dashed=1' in style or
            'container=1' in style or
            'swimlane' in style)


def cmd_validate(args):
    """validate 子命令：布局验证。"""
    if not os.path.isfile(args.drawio):
        print(f"ERROR: File not found: {args.drawio}")
        sys.exit(1)

    elements = parse_geometry(args.drawio)
    containers = [e for e in elements if is_container(e)]
    non_containers = [e for e in elements if not is_container(e)]

    issues = []

    # 构建视觉容器映射：一个元素是另一个元素的"视觉子元素"如果它被包围
    def is_visually_inside(child, parent):
        """检查 child 是否完全在 parent 的边界框内。"""
        return (parent['x'] <= child['x'] and
                parent['y'] <= child['y'] and
                child['x'] + child['w'] <= parent['x'] + parent['w'] and
                child['y'] + child['h'] <= parent['y'] + parent['h'])

    # 找出每个元素的视觉容器
    visual_parent = {}
    for e in non_containers:
        for c in containers:
            if is_visually_inside(e, c):
                visual_parent[e['id']] = c['id']
                break

    # 检查1：非容器元素之间的重叠（仅同视觉容器的同级元素）
    for i, a in enumerate(non_containers):
        for b in non_containers[i + 1:]:
            # 仅检查同一个视觉容器内的同级元素
            va = visual_parent.get(a['id'])
            vb = visual_parent.get(b['id'])
            if va != vb:
                continue  # 不同容器，跳过
            if bounds_overlap(a, b, args.min_gap):
                # 如果一个完全包含另一个，这是有意的设计（标签在图片下方）
                if (is_visually_inside(a, b) or is_visually_inside(b, a)):
                    continue
                issues.append(
                    f"OVERLAP: '{a['id']}'({a['value']}) and "
                    f"'{b['id']}'({b['value']}) overlap "
                    f"(gap < {args.min_gap}px)"
                )

    # 检查2：视觉子元素是否溢出其视觉容器
    for c in containers:
        cx2, cy2 = c['x'] + c['w'], c['y'] + c['h']
        children = [e for e in non_containers
                    if visual_parent.get(e['id']) == c['id']
                    and not is_container(e)]
        for e in children:
            if e['x'] + e['w'] > cx2 + 5 or e['y'] + e['h'] > cy2 + 5:
                issues.append(
                    f"CONTAINER_OVERFLOW: '{e['id']}'({e['value']}) "
                    f"extends outside container '{c['id']}'"
                )

    # 检查3：嵌入图片数据完整性
    tree = ET.parse(args.drawio)
    for elem in tree.getroot().iter():
        style = elem.get('style', '')
        if 'shape=image' in style:
            # 兼容两种格式：data:image/png,DATA 和 data:image/png;base64,DATA
            m = re.search(r'image=data:image/[^;,]+(?:;base64)?,([A-Za-z0-9+/=]+)', style)
            if m:
                if len(m.group(1)) < 100:
                    issues.append(
                        f"SUSPICIOUS_IMAGE: '{elem.get('id')}' has very short "
                        f"base64 data ({len(m.group(1))} chars), may be corrupt"
                    )
                # 检查是否使用了 ;base64 格式（draw.io 中会导致图片不显示）
                if ';base64,' in style:
                    issues.append(
                        f"BASE64_FORMAT: '{elem.get('id')}' uses ';base64,' in style - "
                        f"draw.io treats ';' as style separator, image will not display. "
                        f"Run 'drawio-tool.py fix-base64' to fix."
                    )
            elif 'image=' in style and 'data:image' not in style:
                # 文件路径引用（不一定是问题，但需注意导出兼容性）
                path_match = re.search(r'image=([^;]+)', style)
                if path_match and not path_match.group(1).startswith('data:'):
                    ref_path = path_match.group(1)
                    if not os.path.isabs(ref_path) or not os.path.isfile(ref_path):
                        issues.append(
                            f"IMAGE_REF: '{elem.get('id')}' uses file path "
                            f"reference (may break on export): {ref_path}"
                        )

    # 输出结果
    print(f"Elements: {len(elements)} (containers: {len(containers)})")
    print(f"Min gap: {args.min_gap}px")
    print()

    if issues:
        print(f"Found {len(issues)} issue(s):")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print("PASS: No layout issues detected.")


def cmd_fix_base64(args):
    """修复 drawio 文件中的 ;base64 格式问题。

    将 image=data:image/xxx;base64,DATA 替换为 image=data:image/xxx,DATA，
    解决 draw.io 把 ;base64 中的 ; 当成 style 属性分隔符导致图片不显示的问题。
    """
    if not os.path.isfile(args.drawio):
        print(f"ERROR: File not found: {args.drawio}")
        sys.exit(1)

    with open(args.drawio, 'r', encoding='utf-8') as f:
        content = f.read()

    # 统计匹配数
    count = len(re.findall(r'(image=data:image/[^;,]+);base64,', content))

    if count == 0:
        print("No ;base64 issues found. File is already correct.")
        return

    if args.dry_run:
        print(f"DRY RUN: Would fix {count} image(s) by removing ';base64' from data URIs")
        # 显示匹配位置
        for m in re.finditer(r'(image=data:image/[^;,]+);base64,', content):
            pos = m.start()
            line = content[:pos].count('\n') + 1
            print(f"  Line ~{line}: ...{content[max(0, pos-20):pos+40]}...")
        return

    # 执行替换
    fixed = re.sub(
        r'(image=data:image/[^;,]+);base64,',
        r'\1,',
        content
    )

    with open(args.drawio, 'w', encoding='utf-8') as f:
        f.write(fixed)

    print(f"Fixed {count} image(s): removed ';base64' from data URIs")
    print(f"  File: {args.drawio}")


# ---------------------------------------------------------------------------
# SVG 中转导出
# ---------------------------------------------------------------------------

def extract_images(drawio_path: str) -> dict:
    """从 drawio 文件提取所有嵌入的 base64 图片。

    返回 {cell_id: base64_string}
    """
    tree = ET.parse(drawio_path)
    images = {}
    for elem in tree.getroot().iter():
        style = elem.get('style', '')
        cell_id = elem.get('id', '')
        # 匹配 data:image/xxx,DATA 模式（兼容 ;base64 和无 ;base64 两种格式）
        match = re.search(
            r'image=data:image/[^;,]+(?:;base64)?,([A-Za-z0-9+/=\n]+)',
            style
        )
        if match and cell_id:
            # 清理可能的换行
            b64_data = match.group(1).replace('\n', '')
            images[cell_id] = b64_data
    return images


def inject_images(svg_content: str, image_map: dict) -> tuple:
    """将 drawio 中提取的图片数据注入到 SVG 对应的 <image> 标签。

    返回 (fixed_svg, fix_count)
    """
    fixed = svg_content
    count = 0
    for cell_id, b64 in image_map.items():
        pattern = (
            rf'(<g data-cell-id="{re.escape(cell_id)}">.*?'
            rf'<image[^>]*xlink:href=")([^"]*)(")'
        )

        def replacer(match, data=b64):
            return match.group(1) + f'data:image/png;base64,{data}' + match.group(3)

        new_fixed, n = re.subn(pattern, replacer, fixed, flags=re.DOTALL)
        if n:
            count += n
            fixed = new_fixed
            print(f'  Fixed: {cell_id}')
    return fixed, count


def find_drawio_cli() -> str | None:
    """查找 draw.io CLI 路径。"""
    candidates = [
        '/Applications/draw.io.app/Contents/MacOS/draw.io',  # macOS
        'drawio',  # Linux (snap/apt)
    ]

    # WSL2
    if os.path.exists('/proc/version'):
        try:
            with open('/proc/version') as f:
                if 'microsoft' in f.read().lower():
                    candidates.insert(
                        0,
                        '/mnt/c/Program Files/draw.io/draw.io.exe'
                    )
        except Exception:
            pass

    for cmd in candidates:
        try:
            result = subprocess.run(
                [cmd, '--version'],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                return cmd
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return None


def export_to_svg(drawio_cli: str, drawio_path: str, svg_path: str):
    """用 draw.io CLI 导出 SVG。"""
    cmd = [
        drawio_cli, '--export', '--format', 'svg',
        '--embed-svg-images',
        '--output', svg_path, drawio_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f'Export error: {result.stderr}')
        sys.exit(1)


def svg_to_png(svg_path: str, png_path: str, width: int = 2400):
    """用 rsvg-convert 将 SVG 转 PNG。"""
    cmd = ['rsvg-convert', '-w', str(width), '-o', png_path, svg_path]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f'Conversion error: {result.stderr}')
        sys.exit(1)


def cmd_export(args):
    """export 子命令：SVG 中转导出。"""
    if not os.path.isfile(args.drawio):
        print(f"ERROR: File not found: {args.drawio}")
        sys.exit(1)

    output = args.output
    if not output:
        output = str(Path(args.drawio).with_suffix('.png'))

    width = args.width or 2400

    print(f'Input:  {args.drawio}')
    print(f'Output: {output}')

    # Step 1: Extract images from drawio
    print('\n[1/4] Extracting embedded images...')
    images = extract_images(args.drawio)
    print(f'  Found {len(images)} images')

    if not images:
        print('  No embedded images found. Using standard export...')

    # Step 2: Export to SVG
    print('\n[2/4] Exporting to SVG...')
    cli = find_drawio_cli()
    if not cli:
        print('ERROR: draw.io CLI not found')
        print('Install from: https://github.com/jgraph/drawio-desktop/releases')
        sys.exit(1)

    with tempfile.NamedTemporaryFile(suffix='.svg', delete=False) as f:
        svg_path = f.name
    export_to_svg(cli, args.drawio, svg_path)
    print(f'  SVG: {os.path.getsize(svg_path)} bytes')

    if not images:
        # No images to fix, just convert
        svg_to_png(svg_path, output, width)
        os.unlink(svg_path)
        print(f'\nDone (no image fix needed)! {output}')
        return

    # Step 3: Fix SVG images
    print('\n[3/4] Fixing image data in SVG...')
    with open(svg_path, 'r') as f:
        svg = f.read()
    fixed_svg, fix_count = inject_images(svg, images)
    print(f'Total: {fix_count} images fixed')

    fixed_svg_path = svg_path.replace('.svg', '_fixed.svg')
    with open(fixed_svg_path, 'w') as f:
        f.write(fixed_svg)

    # Step 4: Convert to PNG
    print('\n[4/4] Converting to PNG...')
    svg_to_png(fixed_svg_path, output, width)
    print(f'  PNG: {os.path.getsize(output)} bytes')

    # Cleanup
    os.unlink(svg_path)
    os.unlink(fixed_svg_path)
    print(f'\nDone! {output}')


# ---------------------------------------------------------------------------
# CLI 入口
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='draw.io 光储架构图工具链',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 图片预处理（输出 base64）
  python3 drawio-tool.py prepare product.jpg 50 70

  # 生成 drawio XML mxCell
  python3 drawio-tool.py prepare-xml product.jpg 50 70 --x 100 --y 200 --id img_1

  # 布局验证
  python3 drawio-tool.py validate diagram.drawio --min-gap 5

  # SVG 中转导出
  python3 drawio-tool.py export diagram.drawio -o output.png --width 2400
        """
    )
    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # prepare
    p_prepare = subparsers.add_parser('prepare', help='图片预处理（缩放+RGB转换+base64编码）')
    p_prepare.add_argument('image', help='图片文件路径')
    p_prepare.add_argument('width', type=int, help='目标宽度')
    p_prepare.add_argument('height', type=int, help='目标高度')
    p_prepare.add_argument('-o', '--output', help='输出文件路径（默认 stdout）')

    # prepare-xml
    p_xml = subparsers.add_parser('prepare-xml', help='生成 drawio XML mxCell（含嵌入图片）')
    p_xml.add_argument('image', help='图片文件路径')
    p_xml.add_argument('width', type=int, help='目标宽度')
    p_xml.add_argument('height', type=int, help='目标高度')
    p_xml.add_argument('--x', type=int, default=100, help='X 坐标（默认 100）')
    p_xml.add_argument('--y', type=int, default=100, help='Y 坐标（默认 100）')
    p_xml.add_argument('--cell-id', help='mxCell ID（默认基于文件名）')
    p_xml.add_argument('-o', '--output', help='输出文件路径（默认 stdout）')

    # embed-image
    p_embed = subparsers.add_parser('embed-image', help='向 drawio 文件中嵌入图片（通用步骤）')
    p_embed.add_argument('drawio', help='drawio 文件路径')
    p_embed.add_argument('image', help='图片文件路径')
    p_embed.add_argument('x', type=int, help='X 坐标')
    p_embed.add_argument('y', type=int, help='Y 坐标')
    p_embed.add_argument('width', type=int, help='图片宽度')
    p_embed.add_argument('height', type=int, help='图片高度')
    p_embed.add_argument('--id', dest='cell_id', help='mxCell ID（默认自动生成）')

    # validate
    p_validate = subparsers.add_parser('validate', help='布局验证（重叠检测、容器包围检查）')
    p_validate.add_argument('drawio', help='drawio 文件路径')
    p_validate.add_argument('--min-gap', type=int, default=5,
                           help='最小间距（px，默认 5）')

    # export
    p_export = subparsers.add_parser('export', help='SVG 中转导出（自动修复 base64 图片）')
    p_export.add_argument('drawio', help='drawio 文件路径')
    p_export.add_argument('-o', '--output', help='输出 PNG 路径')
    p_export.add_argument('--width', type=int, default=2400,
                         help='输出宽度（px，默认 2400）')

    # fix-base64
    p_fix = subparsers.add_parser('fix-base64', help='修复 drawio 文件中的 ;base64 格式问题')
    p_fix.add_argument('drawio', help='drawio 文件路径')
    p_fix.add_argument('--dry-run', action='store_true',
                       help='仅预览，不修改文件')

    args = parser.parse_args()

    if args.command == 'prepare':
        cmd_prepare(args)
    elif args.command == 'prepare-xml':
        cmd_prepare_xml(args)
    elif args.command == 'embed-image':
        cmd_embed_image(args)
    elif args.command == 'validate':
        cmd_validate(args)
    elif args.command == 'export':
        cmd_export(args)
    elif args.command == 'fix-base64':
        cmd_fix_base64(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
