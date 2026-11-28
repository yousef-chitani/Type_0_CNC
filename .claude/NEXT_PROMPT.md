# Next session
## Context (≤5 lines)
57th session finished the `Type_0_v6` Y1/Y2 belt drives (`6 mm` steel plates, `1:1` `20T` `HTD 5M-300`, real `BK12` blocks, continuous sculpted PETG belt covers bolted to bottom M6 holes), real `HM12-60` (upright on `Z=455` riser) + inline `24HS40` at `+X`, SMC-spec zero-overhang **`CY3B10-200`** rodless cylinder (£39.39 AliExpress), **Back-to-Back `2 × 7` ATC rack** (`ATC Monolithic Arched Bridge Frame` + `ATC Continuous 14-Tool Fork Comb` from owner's `ISO20_Toolholders.f3d`, **14/14 PASS**), and seated `YFrame` directly on the `6 mm` steel bottom plate with narrowed open-perimeter **`650×708.8`** EG base (`18.60 L` / ~41.8 kg, min `30 mm` floor / `60 mm` plinths, zero thin perimeter rim walls) → **true spindle nose `29.1..249.1 mm` above fixture plate**, ATC `+17.8 mm` in Z stroke & `+16.0 mm` under gantry (D-389..D-393). Timeline: **1346 items, 0 errors** (**not saved** — owner saves). Last D-number: **D-393**.

## Do this bundle: Type_0_v6 envelope, spindle shroud, drainage & enclosure
- [ ] **1. Assess the value of folding back the X and Z motors:** Quantify the exact X/Z envelope savings (for the enclosure) vs belt/plate/pulley cost & complexity on `Type_0_v6` (`X` `24HS40` currently protrudes `+151 mm` past `X = +405` to `X = +556`; `Z` motor height at top of stroke). Present trade-offs and ask owner to decide before modelling.
- [ ] **2. Spindle shroud:** Design a flood-coolant / chip shroud around the `Jianken JGL-80/2.2R24` nose & clamp that clears the back-to-back `2 × 7` ATC tool changes (`+7.18 mm` X / `+16.18 mm` Y clearances) and integrates coolant nozzle(s) / air-blast.
- [ ] **3. Drainage system:** Detail the flood-coolant drainage path from the `3 × Ø36` rear drains in the `650×708.8` EG base through the `6 mm` bottom plate into a 3-stage sump tank, mesh pre-filter, return pump, and Loc-Line manifold (and check sealing along the `YFrame` inner faces / 3-sided splash shields).
- [ ] **4. Enclosure:** Size and lay out the `Type_0_v6` flood-coolant enclosure around the final machine envelope (including the X/Z motor fold decision, full Y gantry travel, front doors, sump cabinet underneath, and cable/pneumatic bulkheads).

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md`
- `docs/HANDOVER.md:9-20` — 57th session summary
- `docs/decisions.md:384-395` — D-383 to D-393 (`Type_0_v6` specs)
- `docs/price-check-task-19.md` — ATC pneumatics & coolant loop items
- `docs/supplier-messages.md:143-168` — Dyfed Steels `Type_0_v6` cut list

## Already known (don't re-investigate)
- `Type_0_v6` spindle reach: X `-235..+220` (455 mm), Y `-19.75..+440.25` (460 mm), **true spindle nose** (`+32 mm` above loaded ER16 nut) `Z = 194.1..414.1` → **`29.1..249.1 mm` above `Z = 165` fixture plate**. Spindle is at the bottom limit of its clamp zone and CANNOT drop further.
- `YFrame` (`120×80×6.3`) sits directly on `6 mm` steel bottom plate (`Z = 74..80` in PrintNC coords); open-perimeter EG base (`650×708.8`, `18.60 L` / ~41.8 kg, `30 mm` solid floor `Z = 80..110`, `60 mm` plinths `Z = 80..140`); `Fixture Plate` `Z = 140..165`.
- Back-to-back `2 × 7` ATC (`Z_engage = 211.9`, `Z_pull_stud = 258.0`, `+16.0 mm` under `XRoller Bottom` `Z = 274.0`): front `T01..T07` (`Y_ext = 345`, opens `-Y`), rear `T08..T14` (`Y_ext = 410`, opens `+Y` to `435`), driven by zero-overhang **`CY3B10-200`** (`Z = 126`, £39.39 AliExpress), **14/14 PASS**.
- Never save Fusion documents; the owner saves them. `git commit` needs `-c user.name=Claude -c user.email=noreply@anthropic.com`.

## Done when
- X/Z motor fold assessment decided, spindle shroud, drainage system, and enclosure laid out/modelled in `Type_0_v6`, decisions logged, `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (`CLAUDE.md`), tick `TASKS.md`, write the next `.claude/NEXT_PROMPT.md` with the template at the bottom of `.claude/TASKS.md`.
