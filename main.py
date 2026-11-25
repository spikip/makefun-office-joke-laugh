"""Entry for the make.fun bounty "One-Line Office Joke Laugh-Off".

The program writes a single funny line to /output/entry.txt. The line
is a one-line office joke: the team's team building exercise was
watching the office printer jam together, because nothing bonds
colleagues like shared trauma and a blinking red light. The humour
is the bleak truth of office life dressed as a bonding activity: the
printer is the real team builder, and the red light is the only
manager who ever shows up on time. The gate allows 1 to 200
characters of UTF-8 text, so the line is checked against that cap
before it is written.
"""

import os

ENTRY = (
    "Our team building exercise was watching the printer jam together "
    "\u2014 nothing bonds colleagues like shared trauma and a blinking "
    "red light."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
