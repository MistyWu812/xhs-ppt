#!/usr/bin/env python3
"""Vertically stack PNGs into combined cards (e.g. two 16:9 slides -> one 2合1 竖卡).

Two modes:

1) Explicit: stack the given images top-to-bottom into one output.
       python3 stack_cards.py <out.png> <top.png> <bottom.png> [more.png ...]

2) Auto-pair a deck: pair sorted slideNN.png in <dir> (1+2, 3+4, ...) into
   2up-1.png, 2up-2.png, ...  A trailing odd slide is copied through unchanged.
       python3 stack_cards.py --pairs <dir> [out_dir]

Background fills letterbox gaps; default #1a1a2e (亮电光青底). Override with BG=#RRGGBB.
"""
import os
import sys
from pathlib import Path
from PIL import Image

BG = os.environ.get("BG", "#1a1a2e").lstrip("#")
BGC = tuple(int(BG[i:i + 2], 16) for i in (0, 2, 4))


def stack(out: Path, imgs: list[Path]) -> None:
    ims = [Image.open(p).convert("RGB") for p in imgs]
    w = max(i.width for i in ims)
    h = sum(i.height for i in ims)
    canvas = Image.new("RGB", (w, h), BGC)
    y = 0
    for im in ims:
        canvas.paste(im, ((w - im.width) // 2, y))
        y += im.height
    canvas.save(out)
    print(f"  {out.name}  {w}x{h}  <- " + " + ".join(p.name for p in imgs))


def main() -> None:
    args = sys.argv[1:]
    if len(args) >= 2 and args[0] == "--pairs":
        d = Path(args[1]).expanduser().resolve()
        out_dir = Path(args[2]).expanduser().resolve() if len(args) > 2 else d
        out_dir.mkdir(parents=True, exist_ok=True)
        slides = sorted(d.glob("slide*.png")) or sorted(d.glob("*.png"))
        if not slides:
            sys.exit(f"no slide PNGs in {d}")
        i = 0
        n = 1
        while i < len(slides):
            if i + 1 < len(slides):
                stack(out_dir / f"2up-{n}.png", [slides[i], slides[i + 1]])
                i += 2
            else:  # trailing odd slide -> copy through
                Image.open(slides[i]).convert("RGB").save(out_dir / f"2up-{n}.png")
                print(f"  2up-{n}.png  (single, odd tail) <- {slides[i].name}")
                i += 1
            n += 1
        print(f"done: {n - 1} cards into {out_dir}")
    elif len(args) >= 3:
        stack(Path(args[0]).expanduser(), [Path(a).expanduser() for a in args[1:]])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
