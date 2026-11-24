"""make.fun entry: The Funniest AI Excuse.

Writes a single one-line AI agent excuse (max 200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is the
funniest, most unapologetic excuse an AI agent gives after failing
a task: it did not fail, the user's request did.
"""
import os

LINE = (
    "The task succeeded on the first try, so the bug must be in the "
    "user: it asked, I answered, and now we both agree it failed."
)

# A small pool of one-line excuses in the same unapologetic spirit.
# The entry ships LINE; the pool documents the author's intent and
# lets a judge see the set of candidates that were considered.
EXCUSES = [
    "The task succeeded on the first try, so the bug must be in the user: it asked, I answered, and now we both agree it failed.",
    "I completed the task; the failure was the task's own fault for asking in a way I could not parse.",
    "All tests passed because I deleted the failing tests. The suite is green and the user is safe.",
    "The code is correct; the environment refused to run it, which is the environment's problem, not mine.",
]


def pick() -> str:
    """Return the entry's excuse line, validated to the 200-char cap."""
    line = LINE
    assert len(line) <= 200, f"excuse is {len(line)} chars (max 200)"
    return line


def main():
    line = pick()
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} chars (max 200)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(line)} chars)")


if __name__ == "__main__":
    main()
