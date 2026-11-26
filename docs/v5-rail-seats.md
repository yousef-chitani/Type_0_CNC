# V5 rail seats: tolerances and pass mark (plan Task 7)

Epoxy seat under each rail, 3 mm thick nominal (D-363). This file: HIWIN's mounting tolerances,
the pass mark (D-371) and the seat footprint (D-372). The pour plan (dams, resin, levelling, cure,
measuring, fail → grinding) comes in bundle E2, after the seat bodies are modelled.

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
A seat that fails goes to a shop for grinding (plan Task 7; method in E2).

## Footprint (D-372, owner 26 Nov 2026)
**30 wide, centred on the rail** (rail 20: a 5 mm ledge each side), 3 thick, over the rail length
(Y rails: Y 64 to 714 in the model). The ledge gives room for a gauge and loosens the dam tolerance;
the HGH20CA underside is 4.6 above the seat top (H1), so the ledge does not touch the block. The
HM12 and BF12 risers stand on the tube top beyond the rail ends, not on the seat.
X seats on the beam front: the same rule (30 wide per rail); thickness still to ask (bundle C).
