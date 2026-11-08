#!/usr/bin/env python3
"""Regenerate docs/phase1-cost.md from docs/bom.csv (Phase 1 lines only).
Run: python tools/gen_phase1_cost.py"""
import csv, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
rows = [r for r in csv.DictReader(open(root / "docs/bom.csv", encoding="utf-8")) if r["stage"] == "1"]
order = []
for r in rows:
    if r["subsystem"] not in order: order.append(r["subsystem"])
price = lambda r: float(r["price_gbp"] or 0)
unpriced = [r["id"] for r in rows if not r["price_gbp"].strip()]
total = sum(price(r) for r in rows)
L = ["# Phase 1 cost (generated from bom.csv)", "",
     f"**Phase 1 priced total: £{total:,.2f}** (budget £4,000). "
     + ("Every line priced." if not unpriced else f"Not priced yet: {', '.join(unpriced)}.") + " No eBay.", "",
     "Regenerate with `python tools/gen_phase1_cost.py`.", "",
     "| Subsystem | £ |", "|---|---|"]
for s in order:
    L.append(f"| {s} | £{sum(price(r) for r in rows if r['subsystem'] == s):,.2f} |")
L += [f"| **Total** | **£{total:,.2f}** |", ""]
for s in order:
    L += [f"## {s}", "", "| ID | Item | Qty | £ |", "|---|---|---|---|"]
    for r in rows:
        if r["subsystem"] == s:
            p = f"£{price(r):,.2f}" if r["price_gbp"].strip() else "to price"
            L.append(f"| {r['id']} | {r['item']} | {r['qty']} {r['unit']} | {p} |")
    L.append("")
(root / "docs/phase1-cost.md").write_text("\n".join(L))
print(f"Phase 1 £{total:,.2f}, unpriced {unpriced}")
