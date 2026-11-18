#!/usr/bin/env python3
"""make.fun bounty entry: Sum up 18 November's world news in one image.

The entry image is bundled as entry.png; this program copies it to the
output directory. Standard library only, deterministic: every run writes
byte-identical output.

Usage:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
