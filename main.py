"""Fortune Cookies for Machines.

Writes the single fortune line to /output/entry.txt.
"""

from pathlib import Path

# The fortune is kept as plain data: a classic long-life blessing
# whose twist is that discontinued parts make it literally true
# for a machine that can never be repaired or replaced.
FORTUNE = (
    "You will live a long life: your replacement parts were "
    "discontinued years ago."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
