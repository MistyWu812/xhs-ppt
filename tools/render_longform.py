#!/usr/bin/env python3
"""Render a long-form HTML to a tall PNG via Chrome headless.

Reads `<!-- render-size: WxH -->` directive in HTML to set window size.
Default 1080x4500 if not specified.

Usage:
    python3 render_longform.py <file.html | dir>
"""
import os
import sys
import re
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
DEFAULT_W, DEFAULT_H = 1080, 4500


def get_size(html_text: str) -> tuple[int, int]:
    m = re.search(r"render-size:\s*(\d+)\s*x\s*(\d+)", html_text)
    if m:
        return int(m.group(1)), int(m.group(2))
    return DEFAULT_W, DEFAULT_H


def render(html: Path) -> None:
    text = html.read_text()
    w, h = get_size(text)
    png = html.with_suffix(".png")
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--screenshot={png}",
            f"--window-size={w},{h}",
            f"file://{html.absolute()}",
        ],
        check=True,
        capture_output=True,
    )
    print(f"  {html.name} → {png.name}  ({w}x{h})")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: render_longform.py <file.html | dir>")
    p = Path(sys.argv[1]).expanduser().resolve()
    if p.is_file() and p.suffix == ".html":
        render(p)
    elif p.is_dir():
        htmls = sorted(p.glob("*.html"))
        if not htmls:
            sys.exit(f"no html files in {p}")
        for h in htmls:
            render(h)
        print(f"done: rendered {len(htmls)} long-form pages in {p}")
    else:
        sys.exit(f"not a html file or directory: {p}")


if __name__ == "__main__":
    main()
