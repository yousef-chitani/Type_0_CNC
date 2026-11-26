"""Check docs/v5-parts.md (plan Task 3): every 'How made' cell is one of the
allowed values (D-339) and no row says mill, turn or laser.
Run: PYTHONUTF8=1 python tools/v5_parts_check.py"""
import re
import sys
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "docs" / "v5-parts.md"
ALLOWED = {"bought", "printed", "owner", "shop grind", "none"}
BANNED = re.compile(r"\b(mill(ed|ing)?|turn(ed|ing)?|lathe|laser)\b", re.I)


def main():
    rows, bad = 0, []
    col = None
    for n, line in enumerate(DOC.read_text().splitlines(), 1):
        if not line.startswith("|"):
            col = None
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if "How made" in cells:
            col = cells.index("How made")
            continue
        if col is None or set(line) <= set("|-: "):
            continue
        rows += 1
        how = cells[col].replace("(proposed)", "")
        for piece in re.split(r"[;,]", how):
            piece = piece.strip()
            if not any(piece.startswith(a) for a in ALLOWED):
                bad.append(f"line {n}: how made '{cells[col]}'")
        if BANNED.search(cells[col]) or BANNED.search(cells[1]):
            bad.append(f"line {n}: mill/turn/laser in the V5 or how-made cell")
    print(f"{rows} part rows checked")
    if bad:
        print("FAIL\n" + "\n".join(bad))
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
