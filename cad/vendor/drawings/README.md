# Supplier drawings (given by the owner, 18 Nov 2026)

Values are copied from the images in this folder. All sizes in mm. None of these parts has been modelled from these drawings yet.

| File | Part | Key values | Not given, or to check |
|---|---|---|---|
| `jianken_jgl_specifications.png` | Jianken JGL series, manual section 2.1 | JGL-80/2.2R24-20: 24,000 rpm, 2.2 kW, 220 V, 400 Hz, 6 A, grease, ISO20, water-cooled, sensor and unclamp/clamp unit | **No dimensions.** Length, nose and top unit still need the Jianken drawing |
| `jianken_jgm_specifications.png` | Jianken JGM series | Diameter x length table, for example JGM-80/1.5R24 80 x 215 | Different series from the JGL-80. Do not use for the model |
| `spindle_clamp_80.png` | 80 mm split clamp | Bore Ø80, base 148 wide, body 110 wide, feet 19 wide x 13 thick, wall 15 each side of the bore, 99 high, shoulder 77 high, 64 from foot top to the top face in the side view, slot 2, corner R8, dimension 55 centre to body side, 40 bore radius | **Clamp length along the spindle, base bolt holes and bore centre height are not dimensioned.** The base sits on the plate, so check it against the 60 centre offset now modelled. One side-view height is hard to read (96 or 99) |
| `dfu_din69051_form_b_table.webp` | DFU nuts, DIN 69051 form B | DFU01605-4: d 16, lead 5, ball 3.175, D 28, A 48, B 10, L 100, W 38, X 5.5, H 40 across flats, Q M6, 1 x 4 circuits, Ca 1380 kgf, Coa 3052 kgf, K 44 kgf/µm. 6 holes for d up to 32 | Catalogue names no maker. LiMo has not confirmed that its nuts have the flats |
| `hm12_60_v_motor_mount.png` | HM12-60-V motor mount with bearing. Listing: https://www.aliexpress.com/item/1005006232398099.html | D1 50, W1 PCD 70, Y 4 x M4, L 95, h 25, B 60, P 45, P1 45, T 30, d1 12, CL1 5.5, L2 35, L3 1.5, H 44, H1 37, B1 35, S 6.6, Q 11, Z 5, E 40, C1 12, C2 70, F 6, J 89, j 5.5, 0.35 kg, bearing 7001, support end BF12, coupling 30-42 Ø10-14 | See the flags below. The second table labels both rows HM12-60-V; the first row is presumably HM12-57-V |
| `mh_jaw_coupling.webp` | MH jaw coupling table | D25 L35 (MH1): bores 4 to 14, hub L1 11.75, clamp screw M3, rated 6 Nm, max 12 Nm | Table does not name LiMo as the maker |
| `m12_inductive_sensor.png` | M12 x 1 inductive sensor | 60 long overall, 55 threaded, nuts 4 thick, 17 across flats, Ø21 washer, cable Ø4, cable relief 9, sensing 4 | **The drawing is labelled NPN NO. The BOM (E10) buys PNP NO (LJ12A3-4-Z/BY)** |

## Flags for the next session

1. **HM12-60-V is a mount and a bearing support in one.** It holds a 7001 bearing and lists BF12 as its partner. Fitting it may replace the Z BK12 and the D-206 bracket. Owner to decide before modelling.
2. **HM12-60-V hole square.** PCD 70 gives a 49.5 square and the motor is 50, so each M4 screw sits 0.35 off its hole centre. The motor holes are Ø5.1, so M4 should pass. The 50 bore does not locate the motor pilot.
3. **HM12-60-V coupling.** The table lists a 30-42 coupling, and the BOM buys D25L35. Check that the Ø25 fits and that the screw and motor ends reach it.
4. **Coupling grip.** The hub is 11.75 long, but D-186 sets 12.9 of shaft into each end. The shafts would run 1.15 past the hub towards the spider. Check the gap between the shaft ends and the spider.
