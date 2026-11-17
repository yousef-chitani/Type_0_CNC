"""Write docs/wave1-order-sheet.md from docs/bom.csv (task 15).

Wave 1 IDs come from the wave table in docs/phase1-schedule.md. Lines are
grouped by the vendor of their main link. Re-run after editing bom.csv.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOM = ROOT / "docs" / "bom.csv"
SCHED = ROOT / "docs" / "phase1-schedule.md"
OUT = ROOT / "docs" / "wave1-order-sheet.md"

VENDORS = [  # (domain fragment, vendor name), in the order to place the orders
    ("mesanet", "Mesa (USA, import VAT on delivery)"),
    ("rs-online", "RS Components (free delivery over £60)"),
    ("stepperonline", "StepperOnline"),
    ("aliexpress", "AliExpress (log in, UK delivery)"),
    ("limobearing", "LiMo (DDP sea, code 10OFF; screw drawings by email with the order number)"),
]

# Open checks (open-questions.md "Before wave 1" and the bom.csv notes)
CHECKS = {
    "E05": "Was pre-order: check stock",
    "E06": "Genuine part not verified",
    "E07": "Genuine part not verified",
    "E09": "Basket clean-up (open question 2)",
    "E13": "Basket clean-up: check the 12 ferrule packs, the HSC8 crimper, the 20/14 AWG wire (open question 2). Terminals and end stops go on the RS order",
    "E14": "Chain length to fix (1 m priced)",
    "E24": "Photos must show A+/B-/GND screw terminals (open question 1)",
    "S05": "Remove the 6 mm ID tube from the basket (open question 2). Flow switch contact rating not stated. Hose is from another shop (link in bom.csv notes)",
    "S08": "Re-check the price (£217.39 + shipping); add to the basket (open question 2)",
    "M09": "VAT basis unclear",
    "M10": "Was backorder from the China warehouse; VAT basis and shipping not shown",
    "M14": "No UK stock (DE warehouse); VAT basis unclear",
    "M05": "X stub drawing by email (Y, Z standard, D-157); HGH20CA 600 price and a corrected checkout (Checkout6 still has HGH15CA 600 × 2 and D25L35 × 1); LiMo 6a answers; steel housing size; code 10OFF",
    "M13": "Basket had HM10-60: must be HM12-60. Holes 49.5 mm: LiMo to drill to 50 (6a)",
    "M01": "Rail accuracy class (6a)",
}


def wave1_ids():
    text = SCHED.read_text(encoding="utf8")
    row = next(l for l in text.splitlines() if l.startswith("| 1 | 1 |"))
    cells = row.split("|")
    ids = re.findall(r"\b[A-Z]\d{2}\b", cells[4])
    total = float(re.search(r"£([\d,]+\.\d\d)", cells[5]).group(1).replace(",", ""))
    return ids, total


def vendor(link):
    for frag, name in VENDORS:
        if frag in link:
            return name
    return "Other"


def cell(s):
    return s.replace("|", "/").replace("\n", " ").strip()


def main():
    ids, sched_total = wave1_ids()
    rows = {r["id"]: r for r in csv.DictReader(BOM.open(encoding="utf8"))}
    missing = [i for i in ids if i not in rows]
    if missing:
        raise SystemExit(f"Not in bom.csv: {missing}")
    groups = {}
    for i in ids:
        groups.setdefault(vendor(rows[i]["link"]), []).append(rows[i])

    out = [
        "# Wave 1 order sheet (order 4 Jan 2027)",
        "",
        "Generated from `docs/bom.csv` by `tools/gen_wave1_sheet.py`: edit the BOM, not this file. "
        "Tick each line when ordered. Prices are the last ones seen (date per line): check them on the day. "
        "Resolve the **Check** column before paying.",
        "",
    ]
    total = 0.0
    unpriced = 0
    order = [n for _, n in VENDORS] + ["Other"]
    for name in order:
        if name not in groups:
            continue
        sub = sum(float(r["price_gbp"] or 0) for r in groups[name])
        unpriced += sum(1 for r in groups[name] if not r["price_gbp"].strip())
        total += sub
        out += [f"## {name}: £{sub:,.2f}", "",
                "| ✓ | ID | Item | Qty | Price as listed (option) | £ | Seen | Link | Check |",
                "|---|---|---|---|---|---|---|---|---|"]
        for r in groups[name]:
            qty = f'{r["qty"]} {r["unit"]}'.strip()
            out.append("| ☐ | {} | {} | {} | {} | {} | {} | [page]({}) | {} |".format(
                r["id"], cell(r["item"]), qty, cell(r["price_listed"]), r["price_gbp"] or "to price",
                r["date_checked"], r["link"], CHECKS.get(r["id"], "")))
        out.append("")
    out += [f"**Wave 1 total: £{total:,.2f}** ({len(ids)} lines, {unpriced} not priced; "
            f"phase1-schedule.md says £{sched_total:,.2f})", ""]
    OUT.write_text("\n".join(out), encoding="utf8")
    print(f"{OUT.name}: {len(ids)} lines, £{total:.2f} (schedule £{sched_total:.2f})")
    if abs(total - sched_total) > 0.005:
        raise SystemExit("Totals differ")


if __name__ == "__main__":
    main()
