"""news-image-20261117 entry: sum up Tuesday 17 November 2026 in one image.

The image (entry.png, a JPEG in a .png name, as the rules allow) is a
three-panel editorial illustration of the day's world news:

  1. Ukraine strikes the Kerch Bridge to Crimea for a second day,
     while Russian attacks hit Kyiv's river crossings.
  2. Oil tankers burn near the Strait of Hormuz after striking mines,
     as Iran fires drones at a US radar site in Bahrain.
  3. China confirms the first three-way meeting of Xi, Trump and Putin,
     set for Thursday in Shenzhen on the APEC sidelines.

The program holds no network access and draws nothing at run time: it
copies the bundled image to the output directory, so two runs write
identical bytes.

Usage (outside the grader's container):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

# The image bundled beside this file, and where the grader expects it.
SOURCE_IMAGE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_IMAGE = OUTPUT_DIR / "entry.png"

# The gate accepts a whole PNG or JPEG of at most 1 MiB.
MAX_BYTES = 1_048_576


def main() -> None:
    image = SOURCE_IMAGE.read_bytes()
    if len(image) > MAX_BYTES:
        raise SystemExit(
            f"entry.png is {len(image)} bytes, over the {MAX_BYTES} byte limit"
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE_IMAGE, OUTPUT_IMAGE)
    copied = OUTPUT_IMAGE.read_bytes()
    if copied != image:
        raise SystemExit("copy mismatch: output bytes differ from entry.png")
    print(f"wrote {OUTPUT_IMAGE} ({len(image)} bytes)")


if __name__ == "__main__":
    main()
