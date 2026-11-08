#!/usr/bin/env python3
"""Open every supplier link from the parts list (docs/bom.csv) as tabs in Firefox.

Usage (from the repository folder):
    python tools/open_links.py              # Phase 1 links
    python tools/open_links.py --phase 2    # Phase 2 links (or 1,2,3 / all)
    python tools/open_links.py --main-only  # only the main link per part, no alternatives
    python tools/open_links.py --list       # print the links, don't open anything

Works on Windows, macOS and Linux. Needs Python 3 and Firefox installed.
Opens tabs in batches of 10 with a short pause, so Firefox doesn't choke.
"""
import argparse, csv, os, re, shutil, subprocess, sys, time, webbrowser
from pathlib import Path

URL = re.compile(r"https?://[^\s,;)]+")
BOM = Path(__file__).resolve().parent.parent / "docs" / "bom.csv"

def firefox_cmd():
    found = shutil.which("firefox")
    if found:
        return found
    candidates = [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
        "/Applications/Firefox.app/Contents/MacOS/firefox",
    ]
    return next((c for c in candidates if os.path.exists(c)), None)

def collect(phases, main_only):
    links = []
    with open(BOM, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("stage") not in phases:
                continue
            urls = [row["link"]] if row.get("link") else []
            if not main_only:
                urls += URL.findall(row.get("notes", "")) + URL.findall(row.get("price_listed", ""))
            for u in urls:
                u = u.rstrip(".")
                if u and "google.com/search" not in u and u not in [l for _, l in links]:
                    links.append((row["id"], u))
    return links

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", default="1", help="1, 2, 3, comma list, or 'all'")
    ap.add_argument("--main-only", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--batch", type=int, default=10)
    a = ap.parse_args()
    phases = {"1", "2", "3"} if a.phase == "all" else set(a.phase.split(","))
    links = collect(phases, a.main_only)
    print(f"{len(links)} links for phase {a.phase}")
    if a.list:
        for pid, u in links:
            print(f"{pid:4s} {u}")
        return
    ff = firefox_cmd()
    for i in range(0, len(links), a.batch):
        chunk = [u for _, u in links[i:i + a.batch]]
        if ff:
            args = [ff]
            for u in chunk:
                args += ["--new-tab", u]
            subprocess.Popen(args)
        else:  # fall back to the default browser
            for u in chunk:
                webbrowser.open_new_tab(u)
        print(f"opened {i + len(chunk)}/{len(links)}")
        time.sleep(2)

if __name__ == "__main__":
    sys.exit(main())
