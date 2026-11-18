"""Claude Code hook: re-run the BOM generators after docs/bom.csv is edited.

Silent on success. On failure, prints the error and exits 2 so Claude sees it.
"""
import json
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOM = (ROOT / "docs" / "bom.csv").resolve()
GENERATORS = [
    "tools/gen_bom_md.py",
    "tools/gen_phase1_xlsx.py",
    "tools/gen_phase1_cost.py",
    "tools/build_open_links.py",
    "tools/gen_wave1_sheet.py",
]


def main():
    try:
        payload = json.load(sys.stdin)
        edited = payload["tool_input"]["file_path"]
    except (ValueError, KeyError, TypeError):
        return 0
    if pathlib.Path(edited).resolve() != BOM:
        return 0
    # The generators open files with the default encoding; Windows cp1252 cannot write the BOM text.
    env = {**os.environ, "PYTHONUTF8": "1"}
    for script in GENERATORS:
        # Retry: Windows can briefly lock an output file while another program has it open.
        for attempt in range(3):
            if attempt:
                time.sleep(1)
            result = subprocess.run(
                [sys.executable, script], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace"
            )
            if result.returncode == 0:
                break
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip()[-1500:]
            print(f"BOM hook: {script} failed. Later generators did not run.\n{detail}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
