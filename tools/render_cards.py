#!/usr/bin/env python3
"""Render HTML slide files in a directory to PNG via Chrome headless.

Usage:
    python3 render_cards.py <slides_dir> [WIDTHxHEIGHT] [scale]

Args:
    slides_dir     directory of *.html files (renders all, same-stem .png)
    WIDTHxHEIGHT   optional, default 1080x1440 (小红书 9:16).
                   Other common: 1280x720 (16:9 单页), 1280x1440 (2合1 竖卡)
    scale          optional device-scale-factor, default 1.
                   Pass 2 for @2x hi-res (1080x1440 -> 2160x2880). 推荐 2。

Always waits for web fonts (Orbitron / Material Icons / Google Fonts) via
--virtual-time-budget, so online font links render correctly.
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path


def find_chrome() -> str:
    """Resolve a Chrome/Chromium binary. Override with the CHROME env var."""
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",  # Linux (PATH)
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",  # Windows
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if os.path.isfile(c) or shutil.which(c):
            return c
    sys.exit("Chrome not found. Install Google Chrome or set CHROME=/path/to/chrome")


CHROME = find_chrome()


def render(html: Path, png: Path, w: int, h: int, scale: int) -> None:
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--force-device-scale-factor={scale}",
            "--virtual-time-budget=5000",          # wait for web fonts to load
            "--run-all-compositor-stages-before-draw",
            f"--screenshot={png}",
            f"--window-size={w},{h}",
            f"file://{html}",
        ],
        check=True,
        capture_output=True,
    )


def main() -> None:
    if not 2 <= len(sys.argv) <= 4:
        sys.exit("usage: render_cards.py <slides_dir> [WIDTHxHEIGHT] [scale]")
    d = Path(sys.argv[1]).expanduser().resolve()
    if not d.is_dir():
        sys.exit(f"not a directory: {d}")
    w, h = 1080, 1440
    if len(sys.argv) >= 3:
        w, h = (int(x) for x in sys.argv[2].lower().split("x"))
    scale = int(sys.argv[3]) if len(sys.argv) == 4 else 1

    htmls = sorted(d.glob("*.html"))
    if not htmls:
        sys.exit(f"no html files in {d}")
    for ht in htmls:
        png = ht.with_suffix(".png")
        print(f"  {ht.name}  ->  {png.name}  ({w}x{h} @{scale}x)")
        render(ht.absolute(), png.absolute(), w, h, scale)
    print(f"done: rendered {len(htmls)} cards into {d}")


if __name__ == "__main__":
    main()
