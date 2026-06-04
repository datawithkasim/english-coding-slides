#!/usr/bin/env python3
"""Render a slide deck (.html) to a one-slide-per-page PDF handout.

The deck supplies its own print CSS (@page size + @media print revealing every
.slide). This just drives Microsoft Edge headless to print it.

Usage:
    python scripts/build-deck-pdf.py webdev/web002-javascript/id-connection.html

Writes <same-name>.pdf next to the input file.
"""
import shutil
import subprocess
import sys
from pathlib import Path


def find_edge() -> str:
    """Locate Microsoft Edge portably; raise with a hint if missing."""
    for name in ("msedge", "microsoft-edge", "msedge.exe"):
        found = shutil.which(name)
        if found:
            return found
    for candidate in (
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ):
        if Path(candidate).exists():
            return candidate
    raise RuntimeError(
        "Microsoft Edge not found. Install Edge, or add msedge to PATH. "
        "(PDF rendering uses Edge's headless --print-to-pdf.)"
    )


def build(deck_path: Path) -> Path:
    deck_path = deck_path.resolve()
    if not deck_path.exists():
        raise FileNotFoundError(deck_path)
    out_pdf = deck_path.with_suffix(".pdf")
    edge = find_edge()
    subprocess.run(
        [
            edge,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_pdf}",
            deck_path.as_uri(),
        ],
        check=True,
    )
    return out_pdf


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python scripts/build-deck-pdf.py <deck.html>", file=sys.stderr)
        sys.exit(1)
    out = build(Path(sys.argv[1]))
    print(f"PDF written: {out}")


if __name__ == "__main__":
    main()
