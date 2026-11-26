"""Regenerate the mechanical sections of .claude/CODEMAP.md (tree, script index, where-index).

Run from anywhere: python tools/codemap.py   (add --check to only report if the map is stale).
Only text between '<!-- AUTO:<name> -->' and '<!-- /AUTO:<name> -->' is rewritten; everything
else in CODEMAP.md is hand-written and kept byte for byte. Uses git ls-files and Python's ast,
so `git add` new files before running it (untracked files are not mapped).
"""
import ast
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / ".claude" / "CODEMAP.md"
BINARY = re.compile(r"\.(step|stp|stl|f3d|png|jpe?g|webp|pdf|zip|3mf|dxf|svg|xlsx|pyc)$", re.I)

# Folder notes for the tree (hand-kept here, not in the map).
NOTES = {
    ".claude": "settings.json (BOM hook), this map, TASKS.md, NEXT_PROMPT.md",
    "cad": "type0_layout.py / type0_drawings.py: v1 CadQuery layout (history)",
    "cad/out": "v1 outputs (history)",
    "cad/v2": "CadQuery fixed-gantry design (history, D-137); bench, enclosure, printed parts still used",
    "cad/v2/out": "generated STEP/PNG/SVG/JSON from cad/v2 scripts",
    "cad/v4/jlc-step": "V4 per-part STEP for JLC quotes (task 29, on hold), README inside",
    "cad/vendor": "manufacturer STEP/PDF (real parts: use these, never stand-ins), README inside",
    "cad/vendor/drawings": "supplier drawings (LiMo ends, HM12-60, MH coupling, spindle clamp)",
    "docs": "the project: decisions, BOM, design notes, price checks (see Docs map)",
    "docs/tasks": "one file per task + README.md (task table, rules, state)",
    "docs/superpowers": "specs/ and plans/ (design docs and step plans, dated)",
    "docs/sketches": "SVG sketches from tools/task28_sketches.py",
    "linuxcnc/type0": "LinuxCNC 2.9 config: type0.ini + HAL, Mesa 7I76EU",
    "linuxcnc/type0/sim": "simulator ini builder + checks",
    "tools": "calc scripts, BOM generators, hook",
    "tools/fusion": "scripts run inside Fusion via fusion_mcp_execute (not python)",
}

# Concept -> (file, regex). The script resolves the line number.
WHERE = [
    ("V5 sizes (travel, rails, screws, rack)", "tools/v5_sizes.py", r"^def sizes"),
    ("V5 beam section pick", "tools/v5_beam.py", r"^def section"),
    ("V5 idea matrix weights", "tools/v5_matrix.py", r"^def total"),
    ("V5 parts-list check (How made)", "tools/v5_parts_check.py", r"^def main"),
    ("Y1 datums (axis X/Z, SEAT, BF12 centre)", "tools/fusion/v5_y1_place.py", r"^SEAT ="),
    ("Y1 1605 screw profile", "tools/fusion/v5_y1_place.py", r"^SCREW ="),
    ("Y1 placement entry", "tools/fusion/v5_y1_place.py", r"^def run"),
    ("Task 4 check: skipped body names", "tools/fusion/v5_check_task4.py", r"^SKIP ="),
    ("Task 4 check entry", "tools/fusion/v5_check_task4.py", r"^def run"),
    ("BOM hook: generator list", "tools/bom_hook.py", r"^GENERATORS"),
    ("V4 sizes", "tools/v4_sizes.py", r"^def sizes"),
    ("V4 frame stiffness model", "tools/v4_frame_stiffness.py", r"^class Frame"),
    ("Z plate FE model", "tools/z_plate_stiffness.py", r"^class Plate"),
    ("Old assembly build / clash check", "cad/v2/assembly.py", r"^def build"),
    ("Printed parts (PETG)", "cad/v2/printed_parts.py", r"^def fan_grill"),
    ("LinuxCNC joints (X, Y, Z)", "linuxcnc/type0/type0.ini", r"^\[JOINT_0\]"),
    ("LinuxCNC HAL file list", "linuxcnc/type0/type0.ini", r"^\[HAL\]"),
    ("LinuxCNC Mesa board config", "linuxcnc/type0/type0.ini", r"^\[HOSTMOT2\]"),
    ("Sim checks", "linuxcnc/type0/sim/test_sim.py", r"^def check"),
]


def files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True,
                         encoding="utf-8", check=True).stdout.split("\n")
    return [f for f in out if f]


def tree(fs):
    dirs = Counter()
    for f in fs:
        parts = f.split("/")[:-1]
        for i in range(1, len(parts) + 1):
            dirs["/".join(parts[:i])] += 1
    keep = sorted(d for d in dirs if d.count("/") < 2 or d in NOTES)
    lines = ["```"]
    for d in keep:
        if "/out/" in d + "/" and d not in NOTES:
            continue
        pad = "  " * d.count("/")
        note = NOTES.get(d, "")
        lines.append(f"{pad}{d.split('/')[-1]}/  ({dirs[d]} files){'  # ' + note if note else ''}")
    lines.append("```")
    return lines


def sig(fn):
    a = [x.arg for x in fn.args.args]
    if fn.args.vararg:
        a.append("*" + fn.args.vararg.arg)
    return f"{fn.name}({', '.join(a)})"


def symbols(fs):
    lines = []
    for f in sorted(x for x in fs if x.endswith(".py")):
        src = (ROOT / f).read_text(encoding="utf-8")
        t = ast.parse(src)
        doc = (ast.get_docstring(t) or "").strip().splitlines()
        if not doc:  # fusion scripts use a leading comment instead
            c = [ln[1:].strip() for ln in src.splitlines()[:3] if ln.startswith("#")]
            doc = [" ".join(c)] if c else ["-"]
        defs = [sig(n) if isinstance(n, ast.FunctionDef) else f"class {n.name}"
                for n in t.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))
                and not n.name.startswith("_")]
        d = doc[0][:110]
        s = ", ".join(defs)
        if len(s) > 170:
            s = s[:167] + "..."
        lines.append(f"- `{f}` ({len(src.splitlines())}) {d}" + (f"  \n  {s}" if s else ""))
    return lines


def where():
    lines = []
    for concept, f, rx in WHERE:
        p = ROOT / f
        n = next((i for i, ln in enumerate(p.read_text(encoding="utf-8").splitlines(), 1)
                  if re.search(rx, ln)), None) if p.exists() else None
        lines.append(f"- {concept} → `{f}:{n}`" if n else f"- {concept} → `{f}` (NOT FOUND: fix WHERE)")
    return lines


def main():
    fs = [f for f in files() if not BINARY.search(f)]
    allfs = files()
    blocks = {"tree": tree(allfs), "scripts": symbols(fs), "where": where()}
    text = MAP.read_text(encoding="utf-8")
    new = text
    for name, body in blocks.items():
        pat = re.compile(rf"(<!-- AUTO:{name} -->\n).*?(<!-- /AUTO:{name} -->)", re.S)
        if not pat.search(new):
            sys.exit(f"marker AUTO:{name} missing in {MAP}")
        new = pat.sub(lambda m: m.group(1) + "\n".join(body) + "\n" + m.group(2), new)
    if "--check" in sys.argv:
        print("CODEMAP up to date" if new == text else "CODEMAP stale: run python tools/codemap.py")
        sys.exit(0 if new == text else 1)
    if new != text:
        MAP.write_text(new, encoding="utf-8", newline="\n")
    print(f"{MAP.relative_to(ROOT)}: {len(new.splitlines())} lines, "
          f"{'updated' if new != text else 'unchanged'}")


if __name__ == "__main__":
    main()
