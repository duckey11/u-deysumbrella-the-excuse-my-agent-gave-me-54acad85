#!/usr/bin/env python3
"""Write the excuse line to /output/entry.txt."""

import os

ENTRY = (
    "Sorry I missed the deadline. I compressed our whole conversation to save "
    "context, then reread the summary twice to admire how tidy it was, and "
    "then noticed the deadline was in it, marked done."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
