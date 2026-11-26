"""V5 weighted idea matrix (docs/v5-idea-matrix.md). Scores 1-5, weighted total out of 100.
Run: PYTHONUTF8=1 python tools/v5_matrix.py  -> prints the markdown tables."""
W = dict(acc=25, cost=20, build=15, ots=15, proven=10, carry=10, rack=5)
HEAD = "| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |"
# name, from, (acc, cost, build, ots, proven, carry, rack) or None if it breaks the grinding-only rule
G = {
 "A. Layout": [
  ("Fixed gantry, moving table", "V4 (D-305)", (5,3,3,2,3,3,2)),
  ("Moving gantry, stock PrintNC + ihavenofish's 3 changes", "Discord 26 Nov", (3,4,4,4,5,4,4)),
  ("Moving gantry, own design on a bolted frame", "v3 without the tub", (4,3,2,3,2,4,4)),
 ],
 "B. Base / frame": [
  ("Cast EG tub, one piece", "v3 (D-137)", (4,3,1,4,3,1,3)),
  ("Extrusion tray + owner-made steel end plates", "V4 (D-308)", (4,3,4,4,2,4,3)),
  ("Bolted steel tube frame, owner drilled", "PrintNC", (4,5,3,5,5,4,3)),
  ("Granite surface plate (price unknown, cost scored 3)", "v2 option B", (5,3,3,5,3,1,3)),
 ],
 "C. Gantry beam": [
  ("Steel SHS/RHS tube, bought cut to length", "V4 (D-306), PrintNC", (5,4,4,5,5,3,3)),
  ("Bought heavy aluminium extrusion", "v3 sketch", (3,3,4,4,3,5,3)),
  ("JLC 6061 U channel + back plate", "v3 (D-147)", None),
 ],
 "D. Rail seats": [
  ("Shop surface-ground steel bars / plate", "V4 (D-311, D-312)", (5,2,4,3,3,4,3)),
  ("Epoxy self-levelling pour on the frame", "v1 (D-12), PrintNC", (4,5,3,5,5,3,3)),
  ("Rails straight on as-bought faces", "-", (1,5,5,5,2,3,3)),
 ],
 "E. Screws and rails": [
  ("LiMo C5 ground DFU1605 + HGR20", "D-136", (5,3,5,5,4,3,3)),
  ("C7 rolled DFU1605 + HGR20, screw comp in LinuxCNC", "v1 (D-10)", (3,5,5,5,5,3,3)),
 ],
 "F. Motor drive": [
  ("Inline: motor on a bought HM12/BK12 mount + coupling", "V4 Y, v1 (D-14)", (5,5,5,5,5,3,3)),
  ("Belt fold 1:1 on milled fold plates + turned stub shafts", "V4 X, Z (D-331)", None),
  ("Belt fold on a bought side-mount kit (not checked one exists for BK12/NEMA 24)", "-", (4,4,4,4,4,4,4)),
 ],
 "G. Z axis plates": [
  ("Milled 6082 plates", "V4 (M12)", None),
  ("Bought cut-to-size cast tooling plate, owner drills and taps with a printed jig", "-", (4,4,3,4,4,5,3)),
  ("Bought complete Z slide module (model not chosen)", "-", (2,4,5,5,3,5,3)),
 ],
 "H. Table / bed": [
  ("Milled 6082 plate with tapped grid", "V4 (M11)", None),
  ("Bought cut-to-size cast tooling plate, owner drills and taps, fly-cut on the machine", "v1 (D-23)", (4,4,3,4,5,5,3)),
  ("Bought aluminium T-slot bed, fly-cut on the machine", "-", (3,4,5,5,5,5,3)),
 ],
 "I. Where the 2-row rack goes (16-18 tools, about 60 pitch)": [
  ("Behind the bed, under the gantry (moving gantry, +50 Z)", "Discord 26 Nov", (3,4,4,4,4,4,5)),
  ("Beside the bed on a gantry overhang, rows along Y (only about 6 per row in 300 Y)", "Discord 26 Nov, MaxCahill", (3,3,4,4,4,3,1)),
  ("On a wing of the moving table (fixed gantry)", "v2 (D-72), V4 spec", (4,4,4,4,3,3,2)),
 ],
 "J. Damping fill": [
  ("Lean EG packed into the frame and beam voids", "V4 (D-310, D-315)", (4,4,4,5,3,3,3)),
  ("Dry sand in the tubes", "PrintNC builders", (4,5,5,5,4,3,3)),
  ("No fill", "-", (3,5,5,5,4,5,3)),
 ],
}
ACC_FLOOR = 2  # Acc <= 2 cannot meet +-0.02: out
def out(s): return s is None or s[0] <= ACC_FLOOR
def total(s): return sum(w*v for w, v in zip(W.values(), s)) / 5
for g, rows in G.items():
    print(f"\n### {g}\n\n{HEAD}\n|---|---|---|---|---|---|---|---|---|---|")
    ranked = sorted(rows, key=lambda r: -(total(r[2]) if not out(r[2]) else -1 if r[2] else -2))
    best = max(total(r[2]) for r in rows if not out(r[2]))
    for n, f, s in ranked:
        if s is None:
            print(f"| {n} | {f} | " + " | ".join(["-"]*7) + " | **out** (needs milling, turning or laser) |")
        elif out(s):
            print(f"| {n} | {f} | " + " | ".join(map(str, s)) + " | **out** (accuracy 2 or less) |")
        else:
            t = total(s); mark = f"**{t:.0f}** ✓" if t == best else f"{t:.0f}"
            print(f"| {n} | {f} | " + " | ".join(map(str, s)) + f" | {mark} |")

# Sensitivity: does the winner in each group change with other weights?
ALT = {"accuracy first (Acc 40, Cost 10, Bought 10)": dict(acc=40, cost=10, build=15, ots=10, proven=10, carry=10, rack=5),
       "cost first (Acc 15, Cost 35)": dict(acc=15, cost=35, build=15, ots=15, proven=10, carry=5, rack=5)}
print("\n### Sensitivity\n\n| Group | Proposed weights | " + " | ".join(ALT) + " |\n|---|---|" + "---|"*len(ALT))
for g, rows in G.items():
    ok = [r for r in rows if not out(r[2])]
    def win(w):
        sc = [(sum(w[k]*v for k, v in zip(W, r[2]))/sum(w.values())*20, r[0]) for r in ok]
        top = max(sc)[0]; names = [n for s, n in sc if abs(s-top) < 0.5]
        return " / ".join(names) + f" ({top:.0f})"
    print(f"| {g.split('.')[0]} | {win(W)} | " + " | ".join(win(w) for w in ALT.values()) + " |")
