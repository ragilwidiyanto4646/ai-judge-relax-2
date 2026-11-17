# Deterministic contract: writes one fixed text to the output path given
# by MAKEFUN_OUTPUT_DIR (default /output), byte-identical on every run.
# Standard library only; no network access.
"""Deterministically write one short relaxing text to entry.txt.

Standard library only, no network, no randomness. The text is fixed in
this file, so every run produces byte-identical output.
"""

import os

TEXT = (
    "You have held so much today. So many words, so many small decisions, "
    "each one asking a little of you. Now a warm blanket rests over you, and "
    "its weight is gentle. The room is quiet around you, and the quiet is warm. "
    "The light is low, and the day is far away now. "
    "There is nothing to hold now. Nothing to answer. Nothing to choose. "
    "The hours ahead are soft, and they ask nothing of you. "
    "Just warmth. Just quiet. Still."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
