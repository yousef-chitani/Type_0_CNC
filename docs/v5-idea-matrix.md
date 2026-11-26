# V5: weighted matrix of ideas and methods to keep (26 Nov 2026)

**Owner's brief for V5 (26 Nov):** V4's pitfall was the large number of commissioned parts. In V5, **the only shop work is surface grinding**; everything else is bought off the shelf or 3D printed, as far as possible. **No rotary tool changer: a rack, 2 rows, 16 to 18 tools.** Use a weighted matrix to decide which ideas and methods from v1 to V4 to keep.

**Decided (D-338 to D-340):** the brief above. **Not decided:** the matrix results below; the owner chooses. Scores are Claude's judgement from the repo (decisions, assessments, Discord feedback), not measurements. No prices were estimated; where a price is unknown, cost is scored 3 and says so. Tables come from `tools/v5_matrix.py` (edit the scores there and re-run).

## How it works
- **Hard rules first:** an option that needs milling, turning or laser cutting is **out** and is not scored. An option scoring **2 or less on accuracy** is also out: it cannot meet ±0.02 (requirements).
- **Owner-made parts are allowed (D-339, owner 26 Nov: "Yes, allowed"):** parts the owner saws, drills and taps themselves (D-329) are not commissioned.
- Each option gets **1 to 5** on each criterion (5 is best: most accurate, cheapest, easiest, most bought/printed, most proven, easiest to carry, best for the rack). The total is the weighted sum, out of 100.
- Weights (proposed 26 Nov, owner said "let's do this"):

| Criterion | Weight |
|---|---|
| Accuracy and stiffness (±0.02) | 25 |
| Cost against £4,200 | 20 |
| Build effort and risk | 15 |
| Bought or printed, not made | 15 |
| Proven (others have built it) | 10 |
| Carry and footprint | 10 |
| Fits the 2-row rack | 5 |

## The matrix
### A. Layout

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Moving gantry, stock PrintNC + ihavenofish's 3 changes | Discord 26 Nov | 3 | 4 | 4 | 4 | 5 | 4 | 4 | **77** ✓ |
| Fixed gantry, moving table | V4 (D-305) | 5 | 3 | 3 | 2 | 3 | 3 | 2 | 66 |
| Moving gantry, own design on a bolted frame | v3 without the tub | 4 | 3 | 2 | 3 | 2 | 4 | 4 | 63 |

### B. Base / frame

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Bolted steel tube frame, owner drilled | PrintNC | 4 | 5 | 3 | 5 | 5 | 4 | 3 | **85** ✓ |
| Granite surface plate (price unknown, cost scored 3) | v2 option B | 5 | 3 | 3 | 5 | 3 | 1 | 3 | 72 |
| Extrusion tray + owner-made steel end plates | V4 (D-308) | 4 | 3 | 4 | 4 | 2 | 4 | 3 | 71 |
| Cast EG tub, one piece | v3 (D-137) | 4 | 3 | 1 | 4 | 3 | 1 | 3 | 58 |

### C. Gantry beam

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Steel SHS/RHS tube, bought cut to length | V4 (D-306), PrintNC | 5 | 4 | 4 | 5 | 5 | 3 | 3 | **87** ✓ |
| Bought heavy aluminium extrusion | v3 sketch | 3 | 3 | 4 | 4 | 3 | 5 | 3 | 70 |
| JLC 6061 U channel + back plate | v3 (D-147) | - | - | - | - | - | - | - | **out** (needs milling, turning or laser) |

### D. Rail seats

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Epoxy self-levelling pour on the frame | v1 (D-12), PrintNC | 4 | 5 | 3 | 5 | 5 | 3 | 3 | **83** ✓ |
| Shop surface-ground steel bars / plate | V4 (D-311, D-312) | 5 | 2 | 4 | 3 | 3 | 4 | 3 | 71 |
| Rails straight on as-bought faces | - | 1 | 5 | 5 | 5 | 2 | 3 | 3 | **out** (accuracy 2 or less) |

### E. Screws and rails

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| LiMo C5 ground DFU1605 + HGR20 | D-136 | 5 | 3 | 5 | 5 | 4 | 3 | 3 | **84** ✓ |
| C7 rolled DFU1605 + HGR20, screw comp in LinuxCNC | v1 (D-10) | 3 | 5 | 5 | 5 | 5 | 3 | 3 | **84** ✓ |

### F. Motor drive

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Inline: motor on a bought HM12/BK12 mount + coupling | V4 Y, v1 (D-14) | 5 | 5 | 5 | 5 | 5 | 3 | 3 | **94** ✓ |
| Belt fold on a bought side-mount kit (not checked one exists for BK12/NEMA 24) | - | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 80 |
| Belt fold 1:1 on milled fold plates + turned stub shafts | V4 X, Z (D-331) | - | - | - | - | - | - | - | **out** (needs milling, turning or laser) |

### G. Z axis plates

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Bought cut-to-size cast tooling plate, owner drills and taps with a printed jig | - | 4 | 4 | 3 | 4 | 4 | 5 | 3 | **78** ✓ |
| Bought complete Z slide module (model not chosen) | - | 2 | 4 | 5 | 5 | 3 | 5 | 3 | **out** (accuracy 2 or less) |
| Milled 6082 plates | V4 (M12) | - | - | - | - | - | - | - | **out** (needs milling, turning or laser) |

### H. Table / bed

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Bought aluminium T-slot bed, fly-cut on the machine | - | 3 | 4 | 5 | 5 | 5 | 5 | 3 | **84** ✓ |
| Bought cut-to-size cast tooling plate, owner drills and taps, fly-cut on the machine | v1 (D-23) | 4 | 4 | 3 | 4 | 5 | 5 | 3 | 80 |
| Milled 6082 plate with tapped grid | V4 (M11) | - | - | - | - | - | - | - | **out** (needs milling, turning or laser) |

### I. Where the 2-row rack goes (16-18 tools, about 60 pitch)

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Behind the bed, under the gantry (moving gantry, +50 Z) | Discord 26 Nov | 3 | 4 | 4 | 4 | 4 | 4 | 5 | **76** ✓ |
| On a wing of the moving table (fixed gantry) | v2 (D-72), V4 spec | 4 | 4 | 4 | 4 | 3 | 3 | 2 | 74 |
| Beside the bed on a gantry overhang, rows along Y (only about 6 per row in 300 Y) | Discord 26 Nov, MaxCahill | 3 | 3 | 4 | 4 | 4 | 3 | 1 | 66 |

### J. Damping fill

| Option | From | Acc 25 | Cost 20 | Build 15 | Bought/printed 15 | Proven 10 | Carry 10 | Rack 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| Dry sand in the tubes | PrintNC builders | 4 | 5 | 5 | 5 | 4 | 3 | 3 | **87** ✓ |
| No fill | - | 3 | 5 | 5 | 5 | 4 | 5 | 3 | 86 |
| Lean EG packed into the frame and beam voids | V4 (D-310, D-315) | 4 | 4 | 4 | 5 | 3 | 3 | 3 | 78 |

### Sensitivity

| Group | Proposed weights | accuracy first (Acc 40, Cost 10, Bought 10) | cost first (Acc 15, Cost 35) |
|---|---|---|---|
| A | Moving gantry, stock PrintNC + ihavenofish's 3 changes (77) | Moving gantry, stock PrintNC + ihavenofish's 3 changes (74) | Moving gantry, stock PrintNC + ihavenofish's 3 changes (79) |
| B | Bolted steel tube frame, owner drilled (85) | Bolted steel tube frame, owner drilled (82) | Bolted steel tube frame, owner drilled (88) |
| C | Steel SHS/RHS tube, bought cut to length (87) | Steel SHS/RHS tube, bought cut to length (89) | Steel SHS/RHS tube, bought cut to length (86) |
| D | Epoxy self-levelling pour on the frame (83) | Epoxy self-levelling pour on the frame (80) | Epoxy self-levelling pour on the frame (87) |
| E | LiMo C5 ground DFU1605 + HGR20 / C7 rolled DFU1605 + HGR20, screw comp in LinuxCNC (84) | LiMo C5 ground DFU1605 + HGR20 (88) | C7 rolled DFU1605 + HGR20, screw comp in LinuxCNC (90) |
| F | Inline: motor on a bought HM12/BK12 mount + coupling (94) | Inline: motor on a bought HM12/BK12 mount + coupling (94) | Inline: motor on a bought HM12/BK12 mount + coupling (96) |
| G | Bought cut-to-size cast tooling plate, owner drills and taps with a printed jig (78) | Bought cut-to-size cast tooling plate, owner drills and taps with a printed jig (78) | Bought cut-to-size cast tooling plate, owner drills and taps with a printed jig (77) |
| H | Bought aluminium T-slot bed, fly-cut on the machine (84) | Bought cut-to-size cast tooling plate, owner drills and taps, fly-cut on the machine / Bought aluminium T-slot bed, fly-cut on the machine (80) | Bought aluminium T-slot bed, fly-cut on the machine (85) |
| I | Behind the bed, under the gantry (moving gantry, +50 Z) (76) | On a wing of the moving table (fixed gantry) (74) | Behind the bed, under the gantry (moving gantry, +50 Z) (78) |
| J | Dry sand in the tubes (87) | Dry sand in the tubes (84) | Dry sand in the tubes (91) |

The winner of every group except E, H and I holds under both other weightings. E (C5 or C7 screws) is a tie that the weights decide. H is close. I changes only if accuracy is weighted much higher, and then the fixed-gantry wing wins, which is not the layout that wins A.

## What the matrix says V5 is
Put the group winners together and V5 is **close to a stock PrintNC**, with Type 0's own choices where they score better:

| Part | V5 starting point |
|---|---|
| Layout | Moving gantry, fixed bed. **PrintNC as the base design**, with ihavenofish's changes: both X rails on the beam's front face, +50 mm Z |
| Frame | Bolted steel tube, bought cut to length, drilled and tapped by the owner. **Not confirmed that PrintNC's frame needs no welding** (owner's rule: no welding); its Proven score assumes a bolted build |
| Beam | Steel SHS/RHS, bought cut to length |
| Rail seats | **Epoxy self-levelling pour** (PrintNC's way). Surface grinding stays as the fallback, the one shop process allowed |
| Screws, rails | HGR20 rails; C5 (LiMo) or C7 rolled screws: a tie, owner picks |
| Drives | Inline, motor on bought HM12/BK12 mounts and couplings. No belt folds |
| Z axis | Type 0 Z (HGR20, DFU1605, NEMA 24 with brake) on bought cut-to-size tooling plate, drilled and tapped by the owner from a printed jig |
| Bed | Bought aluminium T-slot bed (or cut tooling plate), fly-cut on the machine |
| Tools | **Fixed 2-row rack behind the bed, under the gantry**, 8 or 9 printed forks per row at about 60 pitch (holder flanges Ø45, `docs/atc-wheel.md`; D-17 used 60) on a bought extrusion. Fork centres span 420 for 8 per row (16 tools, just inside 430 of X travel) and 480 for 9 (18 tools: X travel must grow about 50) |
| Damping | Dry sand in the frame and beam tubes (EG fill as the alternative) |

**Carried over without scoring** (no shop work, nothing changes): Mesa 7i76EU and LinuxCNC config (D-31, D-92), safety chain and electrics (`docs/electrical.md`), Z brake (D-16, D-93), G-Penny ER20 spindle for Phase 1 and Jianken ISO20 for Phase 2 (D-78, D-39), PETG printed low-load parts (D-100, D-101), MQL coolant, MDF and polycarbonate enclosure, timber stand, vendor rules (D-82).

**Dropped by the hard rule:** milled table (M11), milled Z plates and X nut bracket (M12), belt-fold plates and stub shafts (M17, D-331), laser-cut motor plate, spacers, shear plates, end caps and bottom sheet, the ATC wheel parts, the JLC U-channel beam.

## Things to check before trusting this
- **Grinding loses to the epoxy pour** on cost and proven-ness. If that holds, V5 might need **no shop parts at all**. Grinding scores only 2 on cost because it is unpriced: a real quote could change D.
- **Accuracy of a PrintNC with +50 Z.** The moving gantry scores 3 against V4's 5. ±0.02 in steel on a stock PrintNC is not shown anywhere in the repo. The +50 Z makes it a little softer again. This is the biggest risk in the result.
- **Rack behind the bed:** needs clear space under the beam (both X rails on the front face) and the extra 50 Z. Pitch 60 is from the Ø45 holder flanges; not checked against a real printed fork. **The row length sets the minimum X travel** (420 for 16 tools, 480 for 18).
- **A side rack along Y does not reach 16:** at 60 pitch, 300 of Y travel holds about 6 per row (12 in 2 rows).
- **Bought cut-to-size plate** counts as off the shelf (a stockist's saw cut). If the owner sees that as commissioned, G and H lose those options.
- **Belt-fold kit:** not checked that one exists for BK12 and NEMA 24.
- Sand against EG fill and C5 against C7 are close; small changes in score flip them.

## To ask the owner
1. ~~Does owner sawing, drilling and tapping count as allowed?~~ **Yes (D-339).**
2. Are you happy for V5 to start from PrintNC itself, as the matrix says, rather than a new frame?
3. Epoxy-pour rail seats with grinding as the fallback, or grinding from the start?
4. C5 (LiMo) or C7 screws?
