"""make.fun entry: The Funniest AI Excuse.

Writes a single one-line AI agent excuse (max 200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""
import os

LINE = (
    "The task was completed successfully on the first try; the failure report "
    "must be a test of the tester."
)


def main():
    line = LINE
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
