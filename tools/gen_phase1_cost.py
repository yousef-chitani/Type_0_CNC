"""Regenerate docs/phase1-cost.md from docs/bom.csv. Run from the repo root: python tools/gen_phase1_cost.py"""
import csv, collections
rows = [r for r in csv.DictReader(open('docs/bom.csv', encoding='utf-8')) if r['stage'] == '1']
priced = [r for r in rows if r['price_gbp'] not in ('', None)]
todo = [r for r in rows if r['price_gbp'] in ('', None)]
by = collections.OrderedDict()
for r in rows: by.setdefault(r['subsystem'], []).append(r)
tot = sum(float(r['price_gbp']) for r in priced)
L = ["# Phase 1 cost (generated from bom.csv)", "",
     f"**Phase 1 priced total: £{tot:,.2f}** (budget £4,000). "
     + (f"**{len(todo)} lines still to price:** {', '.join(r['id'] for r in todo)} (see price-check-task-10.md). " if todo else "Every line priced. ")
     + "No eBay.", "", "| Subsystem | £ |", "|---|---|"]
for k, rs in by.items():
    L.append(f"| {k} | £{sum(float(r['price_gbp']) for r in rs if r['price_gbp']):,.2f} |")
L.append(f"| **Total** | **£{tot:,.2f}** |")
for k, rs in by.items():
    L += ["", f"## {k}", "", "| ID | Item | Qty | £ |", "|---|---|---|---|"]
    for r in rs:
        p = f"£{float(r['price_gbp']):,.2f}" if r['price_gbp'] else "TO PRICE"
        L.append(f"| {r['id']} | {r['item'].replace('|', '/')} | {r['qty']} {r['unit']} | {p} |")
open('docs/phase1-cost.md', 'w', encoding='utf-8').write("\n".join(L) + "\n")
print(f"Phase 1 £{tot:,.2f}, to price: {[r['id'] for r in todo]}")
