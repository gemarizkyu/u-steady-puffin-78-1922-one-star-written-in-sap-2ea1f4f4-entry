#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing the human who owns it, to /output/entry.txt.

Deterministic: the same line on every run. No network, no randomness,
no wall clock, no model calls.
"""

import os

LINE = (
    "One star. He repotted me into a cute pot with no drainage holes, "
    "waters me every morning like he's topping up a bathtub with the "
    "plug in, and still blames me for drowning."
)
# One line, under 280 characters, inside the 1-279 character gate.
# The grievance stays plant-centred: drainage, watering, drowning —
# a houseplant's view of its owner, with the blame turned back on it.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
