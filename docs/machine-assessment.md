# Type 0: whole-machine assessment (22 Nov 2026)

Based on `Type_0_v3` as it is now (with the ATC wheel, D-250 to D-252, not saved), `docs/bom.csv` and the earlier checks. Each line says where its figure comes from: **M** measured in the model today, **H** a hand calculation done today (inputs given), **C** carried over from an earlier doc.

## Verdict
The machine as modelled fits together, and nothing found today blocks the design. Accuracy is not proven: the parts calculated so far use about 15 of the 20 µm, and the rest (rollers, blocks, clamp, screws in 3 mm walls) stays unknown until the mapping run (D-10). The risks are elsewhere:
1. **Money:** three Phase 1 lines are still unpriced against £236.65 left.
2. **Phase 1 items not yet in the model:** the front slot, the D-251 strip in the mould, and the stand-in parts.
3. **Joints nobody has checked:** the PrintNC rollers and the screws threaded into 3 mm tube walls.

## 1. Travel and reach
| Item | Value | Source |
|---|---|---|
| Spindle axis reach | X -222.5 to 207.5 (430), Y -88 to 297 (385) | M (slider limits; D-233 + D-247) |
| Nose Z | 95 to 245 (150 travel), plate top Z 70, so 25 to 175 above the plate | M |
| Work area 400 x 250 | met | M |
| Table to nose 180 to 200 (D-09) | **5 to 25 short** at the top | C (`spec-gaps.md` item 3) |
| ATC pickup | X 200, Y -85: 3 inside the Y stop, 13 below the top of Z on the lift | M (`atc-wheel.md`) |

The ATC needs no extra travel; the Y 550 rails and 650 screws already give it (D-185). Its tightest margin is the **3 mm to the Y stop**: set the Y soft limit at -86 or beyond and check it on the built machine.

## 2. Clashes
- ATC against the machine at rest, and against the Z axis at 4 tool-change positions: no clash (M, 22 Nov). The joints would not move from a script, so copies of the bodies were moved instead.
- Rest of the machine: the earlier checks found only screw-in-thread overlaps (C, D-247 to D-249 handover). Two items are still open, with no decision in `decisions.md`: the Y block screw heads hit the rod nuts by 0.9 (Claude's pick is a DIN 7984 low head); and there is no key access to the X top block screws (Claude's pick is to fit them first) (C, `open-items-sketch.md`).

## 3. Stiffness (target ±0.02 mm = 20 µm, D-10)
| Part | Tool movement at 200 N | Source |
|---|---|---|
| Gantry beam SHS 120 x 120 x 8 steel, 700 between rollers, simply supported | 0.9 µm bending (I 7.53 × 10⁶ mm⁴, E 210 GPa) | H |
| Beam twist, Y force at the tool, lever up to 265 below the beam, ends held | about 3 µm (J about 11.2 × 10⁶ mm⁴, G 80 GPa) | H |
| Z fixed plate 6082 x 20 | 2.2 µm nose low, up to 10.9 µm at the top of Z | C (`z-plate-stiffness.md`) |
| Rollers, roller screws, blocks, screws, clamp | **not calculated** | — |

The parts that were calculated add up to about 15 µm at the worst corner (top of Z), against 20. That leaves about 5 µm for everything not calculated: the bolted PrintNC rollers, the top roller screws threaded into 3 of tube wall (still unchecked, `z-plate-stiffness.md`), and the bearing blocks. **This is the weakest part of the case.** Mitigation: keep heavy cuts low in Z, and measure on the built machine (the D-10 mapping run).

## 4. Mass
| Item | kg | Source |
|---|---|---|
| EG tub casting (40,101 cm³ at 2,300 kg/m³) | 92.2 | M volume, C density |
| Fixture plate 6082 460 x 330 x 25 | 10.2 | H |
| Gantry beam (775 of SHS 120 x 8 at 28.1 kg/m) | 21.8 | H |
| ATC aluminium and shaft | 2.2 | M |

The frame target was about 200 to 350 kg (requirements). The machine is well under it, but the tub carries no cutting loads that need mass. What matters is that the tub sits flat and the Y rails stay straight. Moving mass in Y is about 45 to 55 kg (beam, rollers, Z, spindle; the spindle mass is not known until Jianken's drawing). Two NEMA 24 4 Nm motors on 5 mm lead screws have ample thrust (C, `moving-gantry-sketch.md`).

## 5. Cost
- Phase 1 priced: **£3,963.35 of £4,200, £236.65 left** (C, 20 Nov; unchanged today: the ATC is Phase 2 and the D-251 strip comes from the F07 bar already bought).
- Unpriced: **G01 beam, G05 roller steel, X18 screws**. M12 and the LiMo 550/650 lines are not re-checked. The price rule allows no guess, so it is **not known whether £236.65 covers them**. This is the next real risk.
- Phase 2 ATC: A06 needs re-pricing (new stock list, D-253 to D-255), A08 is dropped (direct drive, D-254), and the ATC screws are unpriced.

## 6. What the ATC forces on Phase 1
1. **D-251 strip in the tub mould** (now in the floor's front face at X 200, Z -10 to 40, D-253): must be on the mould drawing (tasks 10/11) before the pour.
2. **Nothing in front of the tub between X 88 and 312** up to about 250 forward (D-253; was the right front corner to X 380): the bench top and any front slot bench (D-230) must leave it clear, and the Phase 2 enclosure must reach round it.
3. No change to rails, screws, electronics or the order. The 5th driver (Mesa channel 4, D-137) and the 48 V supply check (D-158) stay Phase 2.

## 7. Open items (most urgent first)
1. Owner saves `Type_0_v3`: the D-253 to D-255 changes (22 Nov, second session) are unsaved.
2. Price G01, G05, X18; finish the LiMo basket and the Dyfed call (`price-check-task-17.md`). Wave 1 order is 4 Jan 2027.
3. Front slot (task 24 item 6): size it, and place it to leave the ATC corner free.
4. Top roller screws in 3 mm walls: check thread engagement or add rivet nuts or through-bolts.
5. Owner decides the 2 open items in `open-items-sketch.md` (Y screw head, X screw access).
6. Jianken dimension drawing: spindle mass, nose shape and ISO20 holder sizes (the ATC's 5 and 7 mm gaps depend on them).
7. Done 22 Nov (D-255): the owner's fork is on the wheel. Left: fork screw M3 or M4, real motor length and encoder (D-254).
8. Update `requirements.md` (`spec-gaps.md` items 4 to 6) and decide the table-to-nose shortfall (item 3).
9. The timeline has 35 unhealthy items, the same before and after today's work.
