---
name: drawio
description: Always use when user asks to create, generate, draw, or design a diagram, flowchart, architecture diagram, ER diagram, sequence diagram, class diagram, network diagram, mockup, wireframe, or UI sketch, or mentions draw.io, drawio, drawoi, .drawio files, or diagram export to PNG/SVG/PDF.
---

# Draw.io Diagram Skill

Generate draw.io diagrams as native `.drawio` files. Optionally export to PNG, SVG, or PDF with the diagram XML embedded (so the exported file remains editable in draw.io).

## How to create a diagram

1. **Generate draw.io XML** in mxGraphModel format for the requested diagram
2. **Write the XML** to a `.drawio` file in the current working directory using the Write tool
3. **If the user requested an export format** (png, svg, pdf), locate the draw.io CLI (see below), export with `--embed-diagram`, then delete the source `.drawio` file. If the CLI is not found, keep the `.drawio` file and tell the user they can install the draw.io desktop app to enable export, or open the `.drawio` file directly
4. **Open the result** — the exported file if exported, or the `.drawio` file otherwise. If the open command fails, print the file path so the user can open it manually

## Choosing the output format

Check the user's request for a format preference. Examples:

- `/drawio create a flowchart` → `flowchart.drawio`
- `/drawio png flowchart for login` → `login-flow.drawio.png`
- `/drawio svg: ER diagram` → `er-diagram.drawio.svg`
- `/drawio pdf architecture overview` → `architecture-overview.drawio.pdf`

If no format is mentioned, just write the `.drawio` file and open it in draw.io. The user can always ask to export later.

### Supported export formats

| Format | Embed XML | Notes |
|--------|-----------|-------|
| `png` | Yes (`-e`) | Viewable everywhere, editable in draw.io |
| `svg` | Yes (`-e`) | Scalable, editable in draw.io |
| `pdf` | Yes (`-e`) | Printable, editable in draw.io |
| `jpg` | No | Lossy, no embedded XML support |

PNG, SVG, and PDF all support `--embed-diagram` — the exported file contains the full diagram XML, so opening it in draw.io recovers the editable diagram.

## draw.io CLI

The draw.io desktop app includes a command-line interface for exporting.

### Locating the CLI

First, detect the environment, then locate the CLI accordingly:

#### WSL2 (Windows Subsystem for Linux)

WSL2 is detected when `/proc/version` contains `microsoft` or `WSL`:

```bash
grep -qi microsoft /proc/version 2>/dev/null && echo "WSL2"
```

On WSL2, use the Windows draw.io Desktop executable via `/mnt/c/...`:

```bash
DRAWIO_CMD=`/mnt/c/Program Files/draw.io/draw.io.exe`
```

The backtick quoting is required to handle the space in `Program Files` in bash.

If draw.io is installed in a non-default location, check common alternatives:

```bash
# Default install path
`/mnt/c/Program Files/draw.io/draw.io.exe`

# Per-user install (if the above does not exist)
`/mnt/c/Users/$WIN_USER/AppData/Local/Programs/draw.io/draw.io.exe`
```

#### macOS

```bash
/Applications/draw.io.app/Contents/MacOS/draw.io
```

#### Linux (native)

```bash
drawio   # typically on PATH via snap/apt/flatpak
```

#### Windows (native, non-WSL2)

```
"C:\Program Files\draw.io\draw.io.exe"
```

Use `which drawio` (or `where drawio` on Windows) to check if it's on PATH before falling back to the platform-specific path.

### Export command

```bash
drawio -x -f <format> -e -b 10 -o <output> <input.drawio>
```

**WSL2 example:**

```bash
`/mnt/c/Program Files/draw.io/draw.io.exe` -x -f png -e -b 10 -o diagram.drawio.png diagram.drawio
```

Key flags:
- `-x` / `--export`: export mode
- `-f` / `--format`: output format (png, svg, pdf, jpg)
- `-e` / `--embed-diagram`: embed diagram XML in the output (PNG, SVG, PDF only)
- `-o` / `--output`: output file path
- `-b` / `--border`: border width around diagram (default: 0)
- `-t` / `--transparent`: transparent background (PNG only)
- `-s` / `--scale`: scale the diagram size
- `--width` / `--height`: fit into specified dimensions (preserves aspect ratio)
- `-a` / `--all-pages`: export all pages (PDF only)
- `-p` / `--page-index`: select a specific page (1-based)

### Opening the result

| Environment | Command |
|-------------|---------|
| macOS | `open <file>` |
| Linux (native) | `xdg-open <file>` |
| WSL2 | `cmd.exe /c start "" "$(wslpath -w <file>)"` |
| Windows | `start <file>` |

**WSL2 notes:**
- `wslpath -w <file>` converts a WSL2 path (e.g. `/home/user/diagram.drawio`) to a Windows path (e.g. `C:\Users\...`). This is required because `cmd.exe` cannot resolve `/mnt/c/...` style paths.
- The empty string `""` after `start` is required to prevent `start` from interpreting the filename as a window title.

**WSL2 example:**

```bash
cmd.exe /c start "" "$(wslpath -w diagram.drawio)"
```

## File naming

- Use a descriptive filename based on the diagram content (e.g., `login-flow`, `database-schema`)
- Use lowercase with hyphens for multi-word names
- For export, use double extensions: `name.drawio.png`, `name.drawio.svg`, `name.drawio.pdf` — this signals the file contains embedded diagram XML
- After a successful export, delete the intermediate `.drawio` file — the exported file contains the full diagram

## XML format

A `.drawio` file is native mxGraphModel XML. Always generate XML directly — Mermaid and CSV formats require server-side conversion and cannot be saved as native files.

### Basic structure

Every diagram must have this structure:

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <!-- Diagram cells go here with parent="1" -->
  </root>
</mxGraphModel>
```

- Cell `id="0"` is the root layer
- Cell `id="1"` is the default parent layer
- All diagram elements use `parent="1"` unless using multiple layers

Consult `references/xml-reference.md` for common styles, style properties, edge routing details (including waypoints), and container/group examples.

## Edge routing

**CRITICAL: Every edge `mxCell` must contain a `<mxGeometry relative="1" as="geometry" />` child element**, even when there are no waypoints. Self-closing edge cells (e.g. `<mxCell ... edge="1" ... />`) are invalid and will not render correctly. Always use the expanded form:
```xml
<mxCell id="e1" edge="1" parent="1" source="a" target="b" style="...">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

- Use `edgeStyle=orthogonalEdgeStyle` for right-angle connectors (most common)
- **Space nodes generously** — prefer 200px horizontal / 120px vertical gaps
- **Leave room for arrowheads** — at least 20px of straight segment before the target
- Add explicit **waypoints** when edges would overlap
- Align all nodes to a grid (multiples of 10)
- **Edge labels**: Do NOT wrap edge labels in HTML markup to reduce font size. The default font size for edge labels is already 11px (vs 12px for vertices), so they are already smaller. Just set the `value` attribute directly.

See `references/xml-reference.md` for full edge routing and container guidance.

## Containers and groups

Use parent-child containment (`parent="containerId"`) for nested elements — do **not** just stack shapes. Children use **relative coordinates** within the container. See `references/xml-reference.md` for container types, rules, and examples.

## Dark mode colors

draw.io supports automatic dark mode rendering. How colors behave depends on the property:

- **`strokeColor`, `fillColor`, `fontColor`** default to `"default"`, which renders as black in light theme and white in dark theme. When no explicit color is set, colors adapt automatically.
- **Explicit colors** (e.g. `fillColor=#DAE8FC`) specify the light-mode color. The dark-mode color is computed automatically by inverting the RGB values (blending toward the inverse at 93%) and rotating the hue by 180° (via `mxUtils.getInverseColor`).
- **`light-dark()` function** — To specify both colors explicitly, use `light-dark(lightColor,darkColor)` in the style string, e.g. `fontColor=light-dark(#7EA6E0,#FF0000)`. The first argument is used in light mode, the second in dark mode.

To enable dark mode color adaptation, the `mxGraphModel` element must include `adaptiveColors="auto"`.

When generating diagrams, you generally do not need to specify dark-mode colors — the automatic inversion handles most cases. Use `light-dark()` only when the automatic inverse color is unsatisfactory.

## Style reference

For the complete draw.io style reference: https://www.drawio.com/doc/faq/drawio-style-reference.html

For the XML Schema Definition (XSD): https://www.drawio.com/assets/mxfile.xsd

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| draw.io CLI not found | Desktop app not installed or not on PATH | Keep the `.drawio` file and tell the user to install the draw.io desktop app, or open the file manually |
| Export produces empty/corrupt file | Invalid XML (e.g. double hyphens in comments, unescaped special characters) | Validate XML well-formedness before writing; see the XML well-formedness section below |
| Diagram opens but looks blank | Missing root cells `id="0"` and `id="1"` | Ensure the basic mxGraphModel structure is complete |
| Edges not rendering | Edge mxCell is self-closing (no child mxGeometry element) | Every edge must have `<mxGeometry relative="1" as="geometry" />` as a child element |
| File won't open after export | Incorrect file path or missing file association | Print the absolute file path so the user can open it manually |

## CRITICAL: XML well-formedness

- **NEVER use double hyphens (`--`) inside XML comments.** `--` is illegal inside `<!-- -->` per the XML spec and causes parse errors. Use single hyphens or rephrase.
- Escape special characters in attribute values: `&amp;`, `&lt;`, `&gt;`, `&quot;`
- Always use unique `id` values for each `mxCell`

## Embedding images in draw.io

> **⚠️ CRITICAL: draw.io base64 data URI format trap**
>
> draw.io uses `;` as style attribute separator. When using standard data URI format `data:image/jpeg;base64,<data>`,
> draw.io incorrectly splits at `;`, treating `base64,<data>` as an invalid style property, causing **images to not display at all**.
>
> **Correct format: remove `;base64`, put base64 data directly after comma**
>
> | Format | Result | Note |
> |--------|--------|------|
> | `data:image/jpeg;base64,/9j/...` | **Image not displayed** | `;` treated as style separator by draw.io |
> | `data:image/jpeg,/9j/...` | **Image displays correctly** | base64 data directly after comma, no semicolon |
>
> **When generating draw.io XML programmatically:**
> ```python
> # ❌ WRONG - standard data URI format, but draw.io cannot parse correctly
> image_data = f"data:image/{fmt};base64,{b64_string}"
>
> # ✅ CORRECT - remove semicolon, connect directly with comma
> image_data = f"data:image/{fmt},{b64_string}"
> ```
>
> This affects: (1) draw.io editor display (2) CLI export (3) programmatically generated drawio files.
> Any `;base64` in XML style attribute will break images.

draw.io supports embedded images using base64 data URIs in cell styles:

```xml
<mxCell id="img1" value="" style="image;image=data:image/png;base64,{base64_data}" vertex="1">
  <mxGeometry width="100" height="100" as="geometry"/>
</mxCell>
```

### Image format requirements

| Issue | Cause | Solution |
|-------|-------|----------|
| Images not displayed at all (editor + export) | `data:image/jpeg;base64,` - the `;` is treated as style separator, base64 data truncated | **Remove `;base64`**, use `data:image/jpeg,<base64_data>`. Most common and subtle trap! |
| Images show as small icons/placeholders | draw.io auto-compressed embedded images to thumbnails (e.g., 50×70px) | Keep original resolution; if compression occurs, re-embed the original full-size image |
| Images display correctly in some cells but not others | Corrupted base64 or malformed XML structure | Ensure base64 data is complete and properly formatted |
| XML validates but images don't render | Base64 data spans XML tag boundaries | Ensure base64 data ends before XML attribute boundaries |
| CLI export shows blank images | `;base64,` treated as style separator | Use SVG transit export method (see below) |

### Image embedding guidelines

1. **Use PNG format** for diagrams and graphics (lossless)
2. **Use JPEG format** for photographs (smaller file size)
3. **Keep images at original resolution** — draw.io may auto-compress large images
4. **Verify base64 data integrity** — ensure proper `data:image/{format},{data}` syntax (note: NO `;base64`)
5. **Test after embedding** — open the file in draw.io to confirm images display correctly

### Regenerating embedded images

If images need to be regenerated at full resolution:
1. Extract original images from source files
2. Encode as base64 (e.g., `base64 -i original.png | tr -d '\n'`)
3. Replace existing base64 data in the `.drawio` XML (use `data:image/{format},` prefix, NOT `data:image/{format};base64,`)
4. Verify the updated file renders correctly

### CLI export with embedded images

**Known issue:** draw.io desktop CLI export loses base64 data in styles (`;base64,` misidentified as attribute separator). Images display correctly in draw.io editor but export as blank.

**Solution:** Use SVG transit export method:
1. Export drawio → SVG (embeds base64 correctly)
2. Extract base64 from SVG
3. Convert SVG to PNG using `rsvg-convert`

Dependencies:
- `rsvg-convert`: `brew install librsvg` (macOS) / `apt install librsvg2-bin` (Linux)
- draw.io desktop: https://github.com/jgraph/drawio-desktop/releases
