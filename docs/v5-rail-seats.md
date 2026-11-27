# V5 rail seats: tolerances and pass mark (plan Task 7)

Epoxy seat under each rail, 3 mm thick nominal (D-363). This file: HIWIN's mounting tolerances,
the pass mark (D-371), the seat footprint (D-372), the Y seat bodies in the model and the Y pour plan
(D-374 to D-377). X seats on the beam front wait for bundle C (beam not modelled).

## HIWIN HG20 mounting tolerances (fetched by curl, 26 Nov 2026)
Sources: HIWIN catalogue *Linear guideways HG/QH series* GW-11-6-EN-2302-K, pages 44–47
(https://www.almotion.nl/wp-content/uploads/2020/01/HG_QH_serie.pdf), and HIWIN's
*Installation (E)* manual G99UE02-2506 (https://www.hiwinsupport.com/download/tech_doc/gw/Installation-(E).pdf).
Our rails: LiMo HGH20CA sets, **ZA preload** (D-136), accuracy class C (Class H not chosen).

| Item (HG/QH 20) | Z0 | ZA | ZB | Table |
|---|---|---|---|---|
| Max parallelism of the two rails' reference surfaces, P (µm) | 25 | **20** | 18 | 3.16 |
| Height tolerance coefficient K (S1 = a × K, a = rail spacing) | 2.6e-4 | **1.7e-4** | 1.0e-4 | 3.17 |

- **S1 (height difference between the two rails' mounting surfaces), ZA:** Y rails, a = 755 → **0.128 mm**;
  X rails on the beam front, a = 122 → **0.021 mm**.
- **Running parallelism, block to rail, class C** (Table 3.14, what the guide itself gives):
  rail 300–500 mm 17 µm, 500–700 mm 20 µm, 700–900 mm 22 µm (class H: 12, 13, 15).
  HIWIN gives no straightness figure for the mounting surface along one rail; the class C running
  figure is the scale to aim at.
- **Height H tolerance, class C, HG20:** ±0.1 mm; height variance between blocks on one rail 0.02 mm (Table 3.15).
- **Shoulders and edges, HG20** (Table 3.18): edge radius r ≤ 0.5, rail reference shoulder E1 3.5,
  block shoulder E2 5.0, **clearance under the block H1 4.6** (block underside above the rail's mounting surface).
- **Rail screw torque** (Installation manual Table 11), M5 into iron/steel: 883 N·cm (8.8 N·m);
  M5 into aluminium 441 N·cm.

## Pass mark (D-371, owner 26 Nov 2026)
Measured on the cured seat tops before the rails go on.

| Check | Pass | HIWIN limit (ZA) |
|---|---|---|
| Along each seat (straightness in height over its length) | **≤ 0.02 mm** | none given; class C running 20 µm (500–700 rail) |
| Across the two Y seats (height difference at the same Y) | **≤ 0.05 mm** | S1 0.128 mm (a 755) |
| Across the two X seats on the beam front | **≤ 0.02 mm** | S1 0.021 mm (a 122) |

Rail parallelism (side datum, P ≤ 0.020 mm) is set when the rails are fitted, not by the pour.
A seat that fails gets a skim pour first, then scraping; a grinding shop last (D-377, below).

## Footprint (D-372, owner 26 Nov 2026)
**30 wide, centred on the rail** (rail 20: a 5 mm ledge each side), 3 thick, over the rail length
(Y rails: Y 64 to 714 in the model). The ledge gives room for a gauge and loosens the dam tolerance;
the HGH20CA underside is 4.6 above the seat top (H1), so the ledge does not touch the block. The
HM12 and BF12 risers stand on the tube top beyond the rail ends, not on the seat.
X seats on the beam front: the same rule (30 wide per rail); thickness still to ask (bundle C).

## Y seat bodies in the model (26 Nov 2026, 54th session)
`tools/fusion/v5_y_seats.py` builds root component `Y Rail Seats (epoxy, 30 wide)` (bodies `Y1 seat`,
`Y2 seat`) from the model: X centre and Y ends from each `Y HGR20` rail, Z from the tube top (160) to
the rail underside (163). **Y1 X -392.5 to -362.5, Y2 X 362.5 to 392.5; Y 64 to 714; Z 160 to 163.**
11 Ø6 holes each (the rail's through holes, Y 88.5 + 60k to 688.5). **Volume per seat: 58,500 mm³ gross,
57,567 net**; both 117 cm³. Check: no overlap with the rails, tubes, M5x20 rail screws or
`YRail Centering Guide` (touching faces only); the M5x20 tips now sit at Z 152.5, so they still pass
through the full 6 mm tube wall (Z 154 to 160): no longer screw needed.

## Y pour plan (D-374 to D-377, owner 26 Nov 2026)
Resin: Ampreg 30 + 3X Slow (D-122), 100:26 by weight, 250–450 cP, pot life about 4 h at 25 °C,
minimum 18 °C (`docs/epoxy-options.md`). The mixed density is not in our notes: about 1.1 g/cm³
assumed here (check the TDS).

**Before the pour**
1. Frame assembled on its feet, the Y risers **not** fitted (they stand on the tube top beyond the
   seat ends, 1.5 and 0.5 from them: no room for an end dam once fitted).
2. **Rail holes first (D-375):** mark the rail holes on each tube (PrintNC's `YRail Centering Guide`,
   rail on top as the template), drill Ø4.2 and tap M5 through the 6 mm top wall. Grease 22 M5 grub
   screws, set each 0.5 below the tube top and fill the recess above it flush with wax (no epoxy
   disc over the hex).
3. Abrade the tube top in the seat strip (P80, through mill scale to bright steel), degrease, wax
   everything outside the strip that resin may reach.
4. **Dams (D-376):** waxed aluminium flat bar or angle, at least 6 tall, on double-sided tape, sealed
   along the foot with a plasticine bead: two side dams 30 apart, centred on the rail line (X ±377.5),
   and end dams at Y 64 and Y 714. The 5 mm ledge each side holds the meniscus (epoxy's capillary
   length is about 2 mm), so the rail's 20 mm foot sits on the flat middle.
5. Level the frame with the 200 mm level (X02): each tube along Y, and the two tubes to each other.
   Then **measure the tube-top height of each strip relative to the other** (bar across both tubes plus
   the level, read both ways round): this sets the dose below.

**Pour (D-374: two separate pours, one per seat)**
6. Shop at 20 °C or more, the frame and resin warmed to it for 24 h.
7. Dose per seat **about 65 g for 3.0 thick** (58.5 cm³ x 1.1), plus about 15 g for the cup and the
   dam fillets: mix about 64 g resin + 17 g hardener per seat, slowly (no air), let it stand 5 min.
   **Plan detail, not the owner's choice:** to bring the two seat tops close, the lower tube gets about
   21 g more in the channel per 1 mm it sits lower (19,500 mm² x 1 mm x 1.1). Dose by delivered mass
   (weigh the cup before and after pouring). This only gets close: 1 mm of error in the dam spacing
   is about 0.1 mm of height, so **expect the across check (0.05) may fail** and go to step 13.
   Keep the thickness between 2 and 4.
8. Pour along the strip centre from one end, in a thin stream; pop bubbles with a heat gun held well
   off. Cover each strip (a box over it, not touching) against dust. Both seats from separate mixes,
   the same hour.

**Cure**
9. 48 h at 18 °C or more, then the post-cure of `docs/curing-heat.md` (ramp 10 °C/h to 50 °C, hold
   16 h, cool slowly in the tent). Measure only after it has cooled: the 1.64 % shrinkage
   (about 0.05 mm on 3 mm) is then done, and it is even where the thickness is even.
10. Dams off. Leave the grub screws and wax in until the seats pass (steps 11 to 13): a skim pour must
    not run into open tapped holes.

**Measuring against D-371** (kit: straightedge X05 500 mm DIN 874/2, DTI X01; the feelers X06 start at 0.04)
11. Along each seat (≤ 0.02): straightedge on the seat on two equal spacers, a short flat steel block
    under the DTI's magnetic base as a sled riding on the seat, tip on the straightedge; readings every
    50 mm. Two overlapping spans (Y 64 to 564, 214 to 714) cover the 650. Repeat with the straightedge
    turned end for end, to take its own error out.
12. Across (≤ 0.05): a straight bar resting on both seats at the same Y, the level on it, read, bar
    turned end for end, read again; at three Y (about 100, 390, 680). Half the difference of the two
    readings is the tilt; over 755 mm, 0.05 is 0.066 mm/m. The level's sensitivity is not confirmed yet
    (X02): if it cannot resolve that, the owner says what to use.

**Fail (D-377)**
13. A seat that fails gets a **skim pour**: abrade (P80), clean, dam again and pour about 1 mm (about
    22 g mixed), cure and measure again. **Across fails** (seats flat, heights apart): skim both seats
    (a 1 mm skim on the low one alone overshoots), dosing the difference as in step 7, or scrape the
    high one down if the difference is small. Small high spots: hand-scrape or lap against the
    straightedge with abrasive paper on it. A grinding shop only if that also fails (the frame is
    about 800 long).

**Rail holes (D-375), once both seats pass**
14. Drill Ø6 through each seat at each hole, the rail on top as the drill guide, depth-stopped at the
    seat underside (Z 160): the drill must not reach the M5 thread. Pick out the wax, unscrew the
    grub screws.


**Open (owner):** the across check needs a stiff straight bar over 800 long (X05 is 500); the along
check needs a small flat steel sled block (not on the parts list); whether the V5 frame fits the
tent for the 50 °C post-cure is not confirmed; the Ampreg 30 mixed density and the X02 sensitivity.
