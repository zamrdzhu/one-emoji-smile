#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt and prints it to stdout.

The emoji: 🫶 (U+1FAF6 HEART HANDS) — two hands shaping a heart.
A small, warm gesture from a stranger: kind at first glance, readable
at any age and in any culture, clearly chosen rather than the default
smiley, and friendly without intimacy, sarcasm, or flirtation.
"""

from pathlib import Path

EMOJI = "\U0001FAF6"  # 🫶 HEART HANDS


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(EMOJI, encoding="utf-8")
    # The gate allows 1–8 characters; assert the file holds exactly one.
    assert output.read_text(encoding="utf-8") == EMOJI
    print(EMOJI)


if __name__ == "__main__":
    main()
