#!/usr/bin/env python3
"""make.fun entrypoint: copy entry.png to the output directory.

Stdlib only. No network. The program writes exactly one image:
entry.png (1024x1024, the day's world news on one page).
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # post-copy verification: the output must exist and match the source size
    if not os.path.isfile(dst):
        raise SystemExit(f"copy failed: {dst} does not exist")
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit(
            f"copy failed: size mismatch {os.path.getsize(dst)} != {os.path.getsize(src)}"
        )
    print(f"verified {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
