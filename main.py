"""make.fun entry: The Word You'd Delete From the Dictionary.

Writes one word to erase from the dictionary forever to
/output/entry.txt.

The pick is "queue": five letters, four of them silent. The humour
comes from the word itself — erase it and the language loses a
word that was mostly not being pronounced anyway. It lands at
first sight, needs no caption, and is fresher than the obvious
picks like "moist" or "literally".
"""

import os

ENTRY = "queue"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
