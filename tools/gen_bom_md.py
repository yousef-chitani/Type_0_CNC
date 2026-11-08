"""Regenerate docs/bom.md from docs/bom.csv. Run from the repo root: python tools/gen_bom_md.py"""
import csv, collections
p='docs/bom.csv'
rows=list(csv.DictReader(open(p))); fields=list(rows[0].keys())
tot=collections.defaultdict(float); cnt=collections.Counter(); pc=collections.Counter()
for r in rows:
    cnt[r['subsystem']]+=1
    if r['price_gbp'] not in ('',None): tot[r['subsystem']]+=float(r['price_gbp']); pc[r['subsystem']]+=1
grand=sum(tot.values())
stg=collections.defaultdict(float); stg['3']=0.0
for r in rows:
    if r["price_gbp"]: stg[r.get("stage","1")]+=float(r["price_gbp"])
unpriced=[r for r in rows if r['price_gbp']=='']
def esc(s): return s.replace('|','/').replace('\n',' ')
big=sorted([r for r in rows if r['price_gbp']],key=lambda r:-float(r['price_gbp']))[:10]
md=f"""# Bill of materials (summary)

Full list: [bom.csv](bom.csv). **{len(rows)} line items, {sum(pc.values())} priced.** Prices were read from live pages on 2026-11-04/05 (by this session and a local browser session).

**Pricing rule:** `price_listed` is exactly what the page showed. `price_gbp` is the GBP line total (all units + listed shipping), inc VAT where known. Lines marked *VAT?* may get VAT added, and import VAT may apply to non-UK orders. EUR/USD prices are not converted.

| Subsystem | Line items | Priced | GBP total |
|---|---|---|---|
""" + "\n".join(f"| {k} | {cnt[k]} | {pc[k]} | £{tot[k]:,.2f} |" for k in cnt) + f"""
| **All** | **{len(rows)}** | **{sum(pc.values())}** | **£{grand:,.2f}** |

**Budget (D-68): Phase 1 ≤ £4,000. Phases 2 and 3 later.** Priced total: **£{grand:,.2f}**. Not priced yet: {', '.join(r['id'] for r in unpriced)}.

## Phase totals (D-66, D-86)
| Phase | What | GBP priced |
|---|---|---|
| 1 | Frame, motion, electronics, ER20 spindle, cooling, stand | £{stg['1']:,.2f} |
| 2 | ATC spindle + holders, air, mist, enclosure, tool wheel (D-86) | £{stg['2']:,.2f} |

Lines still TO PRICE: see the list above.

## Ten biggest lines
| ID | Item | £ |
|---|---|---|
""" + "\n".join(f"| {r['id']} | {esc(r['item'])} | {float(r['price_gbp']):,.2f} |" for r in big) + """

## Warnings
- **Not in the total yet:** spindle import VAT (if not collected at checkout), GCL pallet delivery, vibration table top sheet.
- **S01 spindle:** UK import VAT (20%) is likely on top unless Alibaba collects it at checkout. Torque on the page says 0.7 Nm vs 0.87 Nm elsewhere: confirm.
- **M01–M03 rails:** sale price limited to 1 per shopper. At list prices the three kits are £387.63 (+£202.52).
- **S06 holders:** £6.05 may be a new-shopper price. At list price 8 holders are £178.96 (+£130.56). Pull stud must match the spindle.
- **Still to confirm with sellers:** S05 chiller alarm output, S02 VFD RS-485, GCL pallet delivery cost to Swansea (F03/F04).
- **F01 epoxy:** hardener probably included in the ECF packs: confirm by phone.
- **Reference sizes:** M12, A06, N02 and T01 are priced at placeholder sizes until the layout is drawn.

## Full list with links

| ID | Stage | Item | Qty | Spec | Link | Listed price | Line £ | Notes |
|---|---|---|---|---|---|---|---|---|
"""
for r in rows:
    kind='search' if 'google.com/search' in r['link'] else 'product'
    md+=f"| {r['id']} | {r['stage']} | {esc(r['item'])} | {r['qty']} {r['unit']} | {esc(r['specification'])} | [{kind}]({r['link']}) | {esc(r['price_listed'])} | {r['price_gbp']} | {esc(r['notes'])} |\n"
open('docs/bom.md','w').write(md)
print(f"priced {sum(pc.values())}/{len(rows)} total £{grand:,.2f}")
for k in cnt: print(k, f"£{tot[k]:,.2f}")
print("unpriced:", [r['id'] for r in unpriced])
