#!/usr/bin/env python3
"""
DEPRECATED: 此脚本已被 drawio-tool.py 取代。
新项目请使用: python3 drawio-tool.py export input.drawio -o output.png
此文件保留以兼容旧流程。

draw.io 嵌入图片导出工具

解决 draw.io 桌面版 CLI 导出时 base64 图片数据丢失的问题。
用法：python3 export-with-images.py input.drawio [output.png] [--width 2400]

依赖：Pillow, rsvg-convert (brew install librsvg)
"""
import sys
import os
import re
import base64
import io
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from PIL import Image


def extract_images(drawio_path):
    """从 drawio 文件提取所有嵌入的 base64 图片。
    返回 {cell_id: base64_string}
    """
    tree = ET.parse(drawio_path)
    images = {}
    for elem in tree.getroot().iter():
        style = elem.get('style', '')
        cell_id = elem.get('id', '')
        match = re.search(r'image=data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', style)
        if match and cell_id:
            images[cell_id] = match.group(1)
    return images


def inject_images(svg_content, image_map):
    """将 drawio 中提取的图片数据注入到 SVG 对应的 <image> 标签。
    image_map: {cell_id: base64_string}
    """
    fixed = svg_content
    count = 0
    for cell_id, b64 in image_map.items():
        pattern = rf'(<g data-cell-id="{cell_id}">.*?<image[^>]*xlink:href=")([^"]*)(")'
        def replacer(match, data=b64):
            return match.group(1) + f'data:image/png;base64,{data}' + match.group(3)
        fixed, n = re.subn(pattern, replacer, fixed, flags=re.DOTALL)
        if n:
            count += n
            print(f'  Fixed: {cell_id}')
    print(f'Total: {count} images fixed')
    return fixed


def find_drawio_cli():
    """查找 draw.io CLI 路径"""
    candidates = [
        '/Applications/draw.io.app/Contents/MacOS/draw.io',  # macOS
        'drawio',  # Linux (snap/apt)
    ]
    # WSL2
    if os.path.exists('/proc/version'):
        with open('/proc/version') as f:
            if 'microsoft' in f.read().lower():
                candidates.insert(0, '/mnt/c/Program Files/draw.io/draw.io.exe')

    for cmd in candidates:
        try:
            result = subprocess.run([cmd, '--version'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return cmd
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return None


def export_to_svg(drawio_path, svg_path):
    """用 draw.io CLI 导出 SVG"""
    cli = find_drawio_cli()
    if not cli:
        print('ERROR: draw.io CLI not found')
        print('Install from: https://github.com/jgraph/drawio-desktop/releases')
        sys.exit(1)

    cmd = [cli, '--export', '--format', 'svg', '--embed-svg-images',
           '--output', svg_path, drawio_path]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f'Export error: {result.stderr}')
        sys.exit(1)


def svg_to_png(svg_path, png_path, width=2400):
    """用 rsvg-convert 将 SVG 转 PNG"""
    cmd = ['rsvg-convert', '-w', str(width), '-o', png_path, svg_path]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        print(f'Conversion error: {result.stderr}')
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 export-with-images.py input.drawio [output.png] [--width N]')
        sys.exit(1)

    drawio_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') \
                  else drawio_path.replace('.drawio', '.png')
    width = 2400
    if '--width' in sys.argv:
        width = int(sys.argv[sys.argv.index('--width') + 1])

    print(f'Input:  {drawio_path}')
    print(f'Output: {output_path}')

    # Step 1: Extract images from drawio
    print('\n[1/4] Extracting embedded images...')
    images = extract_images(drawio_path)
    print(f'  Found {len(images)} images')

    # Step 2: Export to SVG
    print('\n[2/4] Exporting to SVG...')
    with tempfile.NamedTemporaryFile(suffix='.svg', delete=False) as f:
        svg_path = f.name
    export_to_svg(drawio_path, svg_path)
    print(f'  SVG: {os.path.getsize(svg_path)} bytes')

    # Step 3: Fix SVG images
    print('\n[3/4] Fixing image data in SVG...')
    with open(svg_path, 'r') as f:
        svg = f.read()
    fixed_svg = inject_images(svg, images)
    fixed_svg_path = svg_path.replace('.svg', '_fixed.svg')
    with open(fixed_svg_path, 'w') as f:
        f.write(fixed_svg)

    # Step 4: Convert to PNG
    print('\n[4/4] Converting to PNG...')
    svg_to_png(fixed_svg_path, output_path, width)
    print(f'  PNG: {os.path.getsize(output_path)} bytes')

    # Cleanup
    os.unlink(svg_path)
    os.unlink(fixed_svg_path)
    print(f'\nDone! {output_path}')


if __name__ == '__main__':
    main()
