"""One line under 200 characters that reads as a hilarious autocorrect fail."""

import os

TEXT = "I meant to text my boss 'I'll bring the quarterly reports' but autocorrect sent 'I'll bring the quarterly raccoons' and now I own twelve."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
