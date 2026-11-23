# ATC wheel: one-piece mount, 40 lower (design, 23 Nov 2026, D-289)

**Status: written, waiting for the owner's approval. Not modelled.** Replaces the bracket stack in `docs/atc-wheel.md` (D-253, D-259, D-260). Phase 2, except the tub strip (Phase 1 mould).

## Why
The owner wants the front ATC "very very elegant, integrate and not a kludge" (D-288). Now (23 Nov): "the mount should be 1 continuous part; the ATC assembly can be made much more compact and shorter."

The current stack is 9 separate parts from the tub face to the hub: PETG bracket, 2 posts, top plate, KFL004, collar, a Ø20 x 91 shaft, plus screws. Posts, top plate, KFL004 and collar (Z 83 to 159) only hold the hub up.

## Goals, non-goals, anti-goals
- **Goals:** one part from the tub face to the bearing seat and motor face; the wheel about 40 lower; fewer parts; nothing shorter on tool length.
- **Non-goals:** no change to pickup X 200 / Y -85, wheel centre Y -174, 8 pockets, pitch radius 89, the owner's forks (D-255), the 8-flat hub (D-275), direct drive (D-254).
- **Anti-goals:** a mount that makes tools shorter or the tool change riskier; a cast-in arm; a coupling between wheel and motor (owner chose to keep the rigid joint).

## Approaches considered (owner chose, 23 Nov, Q&A)
| | Mount | Trade-off |
|---|---|---|
| **Chosen** | **Machined 6082, one part**, made on the mill itself before Phase 2 (as D-272) | Stiff, accurate bores, clean look; needs the mill running first |
| Not chosen | Printed PETG, one part | Cheapest, print-first rule (D-100); a cantilever carrying a bearing may creep, bores not precise |
| Not chosen | Cast into the tub | Most built-in; a 250 arm on the mould, sleeve aligned before the pour, Phase 2 locked into Phase 1 |

Height: owner chose **lower about 40** (fork plane Z 171 to Z 131), not "keep 171" or "shorter motor". Joint: owner chose **keep the rigid joint** (D-254, no coupling). Bearing: a first draft had one 1204 self-aligning bearing; lowered, it sits about 16 above the motor's front bearing, so a push down on a fork loads that bearing about 5.6 times (was about 1.2). Owner then chose **2 x 6004 in one bore, rigid joint** (Q&A, 23 Nov), not a pair plus a coupling and not the single 1204. Making: owner chose **mill first, JLC fallback** (as D-272).

## The design (all figures proposed by Claude, owner to confirm)
World mm, as `atc-wheel.md`. Δ = change from today.

| Item | Where |
|---|---|
| Fork plane | **Z 131** (Δ -40). Forks Z 126 to 136 |
| Hub | Z 119 to 131, 8 flats as D-275, **with the shaft as one part**: a Ø20 spigot down through the bearings, Z 82 to 119, bored Ø5 x 24 from below for the motor shaft. The separate Ø20 x 91 shaft, the collar and the KFL004 go. A circlip or nut on the spigot under the lower bearing holds the wheel down |
| Bearings | **2 x 6004-2RS** (20 x 42 x 12) with a 6 spacer, one Ø42 bore, Z 89 to 119 (centres 18 apart). They carry the fork tilt themselves: about 5 times a fork push, against a 6004 rating of several kN |
| Mount top web | Ø116, Z 81 to 119. Ø42 bearing bore from the top, then the Ø22 motor pilot through, **in one set-up**, so motor and bearings line up |
| Grub window | Z 81 to 89 between the lower bearing and the motor face. M4 grub in the spigot at Z 85; a Ø6 radial access hole through the web wall at that height (turn the wheel to line it up). A flat on the motor shaft for the grub |
| Motor | NEMA 17 closed loop (A03) face up under the web, Z 13 to 81; 4 x M3 into the web |
| Cup | Round wall round the motor, ID 62, OD 74, Z 12 to 81, cable out at the bottom. Hides the motor. Inside the tool circle (tools are at r 89, holder bodies inside r 73 are clear) |
| Arm | Solid, 80 wide (X 160 to 240), **Z -10 to 12** from the flange to the cup. Every tool passes over it at about Y -87 to -92 when the wheel turns, so its top sets the tool length |
| Tub flange | X 160 to 240, Z -10 to 40, 15 thick (Y -52 to -37); 4 x M6 x 40 counterbored at X 172 and 228, Z 0 and 30. **Notch X 188 to 212 down to Z 12** under the drop-off point (Y -55), for the tool shank |
| Cast-in strip (Phase 1) | **80 x 10 x 50 (X 160 to 240, Z -10 to 40), 4 x M6 tapped** with cores behind, as D-251. Replaces the 25 x 10 x 50 strip with 2 x M6 |
| Index | LJ12A3 through the web at 202.5°, r 44 (as D-275), outside the cup wall; flag under the hub |
| Tool change | Nose at pickup **Z 141**, lift to **Z 192** (holder top 185), 53 to the top of Z (was 13). Approach and slide as now |
| Tool length | Below the fork: up to about **114** (fork 131, arm top 12, 5 clear); today about 98 (fork 171, old arms' top 68 under the tool circle). Holder bodies end at Z 90, above the arm and flange |

Parts from the tub face to the hub: **mount, 2 bearings and spacer, hub** (was 9 plus the shaft). Height of the ATC: Z -10 to 185 at the holder tops (was 225). The X 88 to 312 keep-out does not change.

## Checks to run when modelling
1. **Plate edge at the approach (Y -55):** with the wheel 40 lower, tools in the spindle go below the plate top (Z 70) at the approach. The tool shank (ER16: at most Ø10) clears the plate edge (Y -37) easily; check the holder and collet nut stay above Z 70 there.
2. Clash check with the Z bodies moved to approach, pickup and lift (as 22 Nov), and every holder swept over the arm and flange notch.
3. **Motor runout:** the rigid joint with 2 bearings is over-constrained by the motor's own pilot-to-shaft runout (not known). Measure the real motor; if it is large, the owner decides again (coupling).
4. Real motor length (68 assumed). Motor bottom Z 13, arm top Z 12: a longer motor needs a pocket in the arm.
5. Arm stiffness: about 85 cantilever, 80 x 22 section; hand calc.
6. **Making it:** about 116 x 195 x 129, with a 68-deep motor pocket. The Type 0 has 175 from nose to table, so check it can be cut lying on its side; if not, JLC (D-272).

## Left to the builder
Fillets and edge breaks, the exact strip core depth, screw lengths, the cable exit.
