#!/usr/bin/env python3
"""Update all md5= attributes in the .modinfo to match the actual files on disk.

Usage (from repo root):
    python update_md5.py
"""

import hashlib
import re
from pathlib import Path

MODINFO = Path(__file__).parent / "JFD's Utilities - AI Observer Interface (v 11).modinfo"


def file_md5(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main() -> None:
    root = Path(__file__).parent
    text = MODINFO.read_text(encoding="utf-8")

    updated = 0
    missing = 0

    def replace(m: re.Match) -> str:
        nonlocal updated, missing
        old_md5 = m.group(1)
        attrs = m.group(2)       # everything between md5="..." and >
        filepath = m.group(3)    # text content between > and </File>

        full = root / filepath.strip()
        if not full.exists():
            print(f"  MISSING  {filepath.strip()}")
            missing += 1
            return m.group(0)   # leave unchanged

        new_md5 = file_md5(full)
        if new_md5 != old_md5:
            print(f"  UPDATED  {filepath.strip()}")
            print(f"           {old_md5} -> {new_md5}")
            updated += 1
        return f'<File md5="{new_md5}"{attrs}>{filepath}</File>'

    new_text = re.sub(
        r'<File md5="([0-9A-Fa-f]+)"([^>]*)>([^<]+)</File>',
        replace,
        text,
    )

    if new_text != text:
        MODINFO.write_text(new_text, encoding="utf-8")

    print(f"\n{updated} hash(es) updated, {missing} file(s) missing.")


if __name__ == "__main__":
    main()
