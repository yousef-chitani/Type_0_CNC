# ATC wheel: one-piece mount, 40 lower (design, 23 Nov 2026, D-289)

**Status: written, waiting for the owner's approval. Not modelled.** Replaces the bracket stack in `docs/atc-wheel.md` (D-253, D-259, D-260). Phase 2, except the tub strip (Phase 1 mould).

## Why
The owner wants the front ATC "very very elegant, integrate and not a kludge" (D-288). Now (23 Nov): "the mount should be 1 continuous part; the ATC assembly can be made much more compact and shorter."

The current stack is 9 separate parts from the tub face to the hub: PETG bracket, 2 posts, top plate, KFL004, collar, a Ø20 x 91 shaft, plus screws. Posts, top plate, KFL004 and collar (Z 83 to 159) only hold the hub up.

## Goals, non-goals, anti-goals
- **Goals:** one part from the tub face to the bearing seat and motor face; the wheel about 40 lower; fewer parts; nothing shorter on tool length.
- **Non-goals:** no change to pickup X 200 / Y -85, wheel centre Y -174, 8 pockets, pitch radius 89, the owner's forks (D-255), the 8-flat hub (D-275), direct drive (D-254).
- **Anti-goals:** a mount that makes tools shorter or the tool change riskier; a cast-in arm; a second bearing with a coupling (owner chose to keep the rigid joint).

## Approaches considered (owner chose, 23 Nov, Q&A)
| | Mount | Trade-off |
|---|---|---|
| **Chosen** | **Machined 6082, one part**, made on the mill itself before Phase 2 (as D-272) | Stiff, accurate bores, clean look; needs the mill running first |
| Not chosen | Printed PETG, one part | Cheapest, print-first rule (D-100); a cantilever carrying a bearing may creep, bores not precise |
| Not chosen | Cast into the tub | Most built-in; a 250 arm on the mould, sleeve aligned before the pour, Phase 2 locked into Phase 1 |

Height: owner chose **lower about 40** (fork plane Z 171 to Z 131), not "keep 171" or "shorter motor". Bearings: owner chose **keep the rigid joint** (D-254: one bearing above, the motor's bearings below), not two bearings and a coupling.

## The design (all figures proposed by Claude, owner to confirm)
World mm, as `atc-wheel.md`. Δ = change from today.

| Item | Where |
|---|---|
| Fork plane | **Z 131** (Δ -40). Forks Z 126 to 136 |
| Hub | Z 119 to 131, 8 flats as D-275, **with the shaft as one part**: a Ø20 spigot down into the bearing (Z 105 to 119). Bored Ø5 for the motor shaft. The separate Ø20 x 91 shaft and the collar go |
| Bearing | **1 x 1204 self-aligning ball bearing** (20 x 47 x 14) in a bore in the mount's top web, Z 105 to 119. Self-aligning like the KFL004, so the rigid joint of D-254 still works. The KFL004 goes |
| Mount top web | Ø116 x 18, Z 101 to 119. Ø47 bearing bore from the top, then the Ø22 motor pilot through, **both in one set-up** so motor and bearing line up |
| Motor | NEMA 17 closed loop (A03) face up under the web, Z 33 to 101; 4 x M3 into the web. Shaft reaches Z 125, into the hub |
| Cup | Round wall round the motor, ID 62, OD 74, Z 33 to 101, open at the bottom for the cable. Hides the motor |
| Yoke | 2 cheeks 15 thick (X 165 to 180 and 220 to 235), Z -10 to 33, from the tub flange (Y -52) to the cup. **Slot X 180 to 220 between them**, so a tool in the pickup pocket or at the drop-off hangs through to the bench |
| Tub flange | X 160 to 240, Z -10 to 40, 15 thick (Y -52 to -37); 4 x M6 x 40 counterbored at X 172 and 228, Z 0 and 30 |
| Cast-in strip (Phase 1) | **80 x 10 x 50 (X 160 to 240, Z -10 to 40), 4 x M6 tapped** with cores behind, as D-251. Replaces the 25 x 10 x 50 strip with 2 x M6 |
| Index | LJ12A3 through the web at 202.5°, r 44 (as D-275), outside the cup wall; flag under the hub |
| Tool change | Nose at pickup **Z 141**, lift to **Z 192** (holder top 185), 53 to the top of Z (was 13). Approach and slide as now |

Parts from the tub face to the hub: **mount, bearing, hub** (was 9). Height of the ATC: Z -10 to 185 at the holder tops (was 225). The X 88 to 312 keep-out does not change.

## Checks to run when modelling
1. **Plate edge at the approach (Y -55):** below Z 70 the tool and collet nut must stay inside r 18 to clear the plate edge (Y -37). With the wheel 40 lower, tools in the spindle go below Z 70 at the approach. If too tight, move the approach to Y -60 and check the fork still lets the groove in.
2. Clash check with the Z bodies moved to approach, pickup and lift (as 22 Nov), plus the yoke against the pickup tool.
3. Hub spigot length against the motor shaft (24 long): the grub screw must be reachable with the wheel built. Options: an access hole through the cup wall, or a D-flat and a clamp. Builder's call, tell the owner.
4. Real motor length (still 68 assumed). The cup and yoke follow it.
5. Yoke stiffness: about 85 cantilever (flange to cup), 2 x 15 x 43 cheeks; hand calc.
6. The part fits the mill's work area (400 x 250, Z 150): about 116 x 195 x 129.

## Left to the builder
Fillets and edge breaks, the exact strip core depth, screw lengths, the cable exit.
