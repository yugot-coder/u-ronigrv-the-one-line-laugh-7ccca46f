"""The One-Line Laugh.

One original funny line about working beside an AI coding agent,
at most 200 characters.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is the joke at CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

CANDIDATES = [
    "I hired an AI to do my job, and now I spend all day explaining my job to the AI, which is somehow still my job.",
    "My AI pair programmer writes code faster than I can read it, which is fine, because neither of us understands it by Friday.",
    "I told my AI assistant I wanted work-life balance, so it scheduled my burnout in fifteen-minute blocks with reminders.",
    "I asked the AI to clean up my code; it deleted my comments, my tests, and — for reasons I respect — my weekends.",
    "My smart speaker finally understands everything I say, which is how I know it has spent years listening to me talk to the cat.",
    "I work beside an AI that never sleeps, never eats, and never complains, which is why HR asked me to stop competing with it.",
    "My AI coding agent finished my task in four seconds, then spent the next hour explaining why the task was beneath it.",
    "I asked my AI agent for a day off, and it replied that it had already taken one for me, in 2031, pending approval.",
]

# The sharpest cut: the hire-an-AI premise promises less work, the middle
# flips it into a full day of explaining, and the punchline closes the
# loop on the last three words — the job never left. It beat the
# pair-programmer candidate (its "by Friday" softens the punch) and the
# clean-up candidate (the middle sags before the weekends beat) on
# economy: every "my job" repetition is the mechanism, not padding, and
# the explaining-forever loop is an everyday truth anyone who has used
# an AI assistant recognises at once. At 111 characters it also leaves
# the most room under the 200-character gate of any finalist.
SELECTED = 0


def main() -> None:
    joke = CANDIDATES[SELECTED].strip()
    assert "\n" not in joke, "entry must be a single line"
    assert 1 <= len(joke) <= 200, "entry must be 1 to 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(joke)


if __name__ == "__main__":
    main()
