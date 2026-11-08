#!/usr/bin/env python3
"""Shop the Type 0 CNC parts list one vendor at a time (standalone: the links are built in).

    py open_links.py               # Phase 1, vendor by vendor
    py open_links.py --phase 2     # or 1,2 or all
    py open_links.py --with-alts   # also open alternative-supplier links
    py open_links.py --list        # print the shopping list, open nothing

For each vendor it prints what to buy (ID, item, qty, budget), opens that vendor's
product pages as Firefox tabs, then waits. Add everything to the basket, close the
product tabs (keep the basket tab), then press Enter for the next vendor.
Keys at the prompt: Enter = next vendor, q = quit.
eBay links are never opened (vendor policy D-82).
"""
import argparse, json, os, shutil, subprocess, sys, time, webbrowser

PARTS = json.loads(r"""__DATA__""")
NEEDS_VENDOR = json.loads(r"""__NOLINK__""")

def firefox_cmd():
    found = shutil.which("firefox")
    if found:
        return found
    for c in (r"C:\Program Files\Mozilla Firefox\firefox.exe",
              r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
              os.path.expandvars(r"%LOCALAPPDATA%\Mozilla Firefox\firefox.exe"),
              "/Applications/Firefox.app/Contents/MacOS/firefox"):
        if os.path.exists(c):
            return c
    return None

def open_tabs(ff, urls, batch=10):
    for i in range(0, len(urls), batch):
        chunk = urls[i:i + batch]
        if ff:
            args = [ff]
            for u in chunk:
                args += ["--new-tab", u]
            subprocess.Popen(args)
        else:
            for u in chunk:
                webbrowser.open_new_tab(u)
        time.sleep(1.5)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", default="1")
    ap.add_argument("--with-alts", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    phases = {"1", "2", "3"} if a.phase == "all" else set(a.phase.split(","))
    parts = [p for p in PARTS if p["phase"] in phases]
    vendors = {}
    for p in parts:
        vendors.setdefault(p["vendor"], []).append(p)
    order = sorted(vendors, key=lambda v: -len(vendors[v]))
    print(f"Phase {a.phase}: {len(parts)} parts from {len(order)} vendors: " + ", ".join(order))
    need = [f"{m['id']} {m['item']}" for m in NEEDS_VENDOR if m["phase"] in phases]
    if need:
        print("Still need a non-eBay source (not opened): " + "; ".join(need))
    ff = firefox_cmd()
    if not ff and not a.list:
        print("Firefox not found: using the default browser.")
    for n, v in enumerate(order, 1):
        items = vendors[v]
        total = sum(float(p["price"]) for p in items if p["price"])
        print(f"\n=== {n}/{len(order)}  {v}  ({len(items)} parts, about £{total:,.2f}) ===")
        urls = []
        for p in items:
            print(f"  {p['id']:4s} {p['qty']:>14s}  {p['item']}")
            if p["url"] not in urls:
                urls.append(p["url"])
            if a.with_alts:
                urls += [u for u in p["extra"] if u not in urls]
        if a.list:
            for u in urls:
                print(f"       {u}")
            continue
        open_tabs(ff, urls)
        ans = input(f"Add these to the {v} basket, close the product tabs, then press Enter for the next vendor (q = quit): ").strip().lower()
        if ans == "q":
            break
    print("\nDone.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
