#!/usr/bin/env python3
"""Entry for make.fun bounty u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

Writes one original joke about office life (a single line, under
200 characters) to /output/entry.txt.
"""

import os
import stat

JOKE = "Our daily standup has run so long the intern who joined as a fresher now leads it — and after all these years, the meeting still hasn't decided what the meeting is about."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(JOKE)} characters to {OUTPUT_PATH}")
    print(JOKE)


if __name__ == "__main__":
    main()
