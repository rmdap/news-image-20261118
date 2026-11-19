#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261118 bounty.
Copies entry.png to the output directory make.fun provides.
Standard library only; no network access.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # post-copy verification: the destination must exist and match the
    # source size; otherwise fail loudly instead of shipping a broken entry.
    if not os.path.exists(dst) or os.path.getsize(dst) != os.path.getsize(src):
        sys.exit("entry.png was not copied correctly")
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
