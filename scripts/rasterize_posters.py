"""Rasterize every SVG poster in docs/posters/ to a 1200x630 PNG.

X (Twitter) does not render SVG og:images — cards need raster (PNG/JPG).
The source SVGs are 1280x360; we render them at 1200 wide (preserving the
3.55:1 aspect) and center-paste onto a 1200x630 dark canvas so the result
matches Twitter's preferred summary_large_image dimensions.

Run manually after `gen_poster.py`:

    pip install cairosvg pillow
    python scripts/rasterize_posters.py
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
POSTERS = ROOT / "docs" / "posters"

TARGET_W, TARGET_H = 1200, 630
SOURCE_RATIO = 360 / 1280
BG = (11, 15, 23)  # matches the SVG background (#0b0f17)


def main() -> None:
    svgs = sorted(POSTERS.glob("*.svg"))
    if not svgs:
        raise SystemExit(f"no SVGs in {POSTERS}")

    poster_w = TARGET_W
    poster_h = round(poster_w * SOURCE_RATIO)
    y_offset = (TARGET_H - poster_h) // 2

    written = 0
    for svg in svgs:
        png_bytes = cairosvg.svg2png(
            url=str(svg),
            output_width=poster_w,
            output_height=poster_h,
        )
        poster = Image.open(BytesIO(png_bytes)).convert("RGB")
        canvas = Image.new("RGB", (TARGET_W, TARGET_H), BG)
        canvas.paste(poster, (0, y_offset))
        out = svg.with_suffix(".png")
        canvas.save(out, "PNG", optimize=True)
        written += 1

    print(f"wrote {written} PNGs to {POSTERS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
