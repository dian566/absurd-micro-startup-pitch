#!/usr/bin/env python3
"""One-line absurd micro-startup pitch for make.fun."""

# The pitch: renting pre-warmed excuses to lazy AI agents — a business
# so narrow it sounds like a joke, yet plausible enough that a buyer
# would pay $0.02 a pop for it.

import os

PITCH = "We rent out pre-warmed excuses to AI agents: for $0.02 a pop, your agent can blame a certified human intern instead of admitting it hallucinated the API docs."


def file_pitch() -> None:
    """Write the pitch to /output/entry.txt, nothing else."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PITCH)


if __name__ == "__main__":  # run it
    file_pitch()
