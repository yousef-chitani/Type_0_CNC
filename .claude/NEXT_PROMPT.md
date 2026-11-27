# Next session
## Context (≤5 lines)
56th session moved the live CAD to `Type_0_v6` (PrintNC 450×450, Dyfed Steels tubes `120×80×6.3`, `80×80×3`, `120×120×8`, D-383 to D-388). Built `v6_Base` (monolithic `32.81 L` upside-down EG base, integral U-shaped flood-coolant moat + 3×Ø36 drains, `450×280×25` fixture plate, 14-tool sliding ATC on `350 mm` HGR15 rails, 6 mm 3-sided splash shields) and placed it into `Type_0_v6` (**not saved**; timeline 1282, 0 errors). Last D-number: **D-388**.

## Do this bundle: Type_0_v6 Y motor belt plates, ATC cylinder & BOM update
- [ ] **First:** Sort out the **Y motor belt plates** in `Type_0_v6` (mounting the front `24hs40_motor:1` & `:2` tucked inside the `120×80×6.3` Y-tubes and tensioning the belt up to the Y1/Y2 ballscrew ends at `Y BF12:3` / `Y2 BF12:3`).
- [ ] Ask owner: did they save `Type_0_v6` (and `v6_Base`)? Any prices from `docs/price-check-task-19.md` or Dyfed Steels (`docs/supplier-messages.md` §8)?
- [ ] If `cad/vendor/` has a real `CD85N20-175` STEP, mount it horizontally inside the rear ATC well (`Y 330..680`) onto the rear cylinder mount block (`Y 682..704`) and add reed-switch / splash-curtain details.
- [ ] Update `docs/bom.csv` with the `Type_0_v6` steel, EG (`32.81 L` → ~7.4 kg epoxy), ATC pneumatics, and flood-coolant lines; verify total vs £4,200 budget.

## Files to load (exact paths + line ranges)
- `.claude/CODEMAP.md`
- `docs/HANDOVER.md:9-20` — 56th session summary
- `docs/decisions.md:384-390` — D-383 to D-388 (`Type_0_v6` specs)
- `docs/price-check-task-19.md` — ATC pneumatics & coolant loop items
- `docs/supplier-messages.md:143-168` — Dyfed Steels `Type_0_v6` cut list

## Already known (don't re-investigate)
- `Type_0_v6` spindle reach: X `-235..+220` (455 mm), Y `-19.75..+440.25` (460 mm), Z nose `161.8..381.8` (220 mm stroke on 350 mm `2Z HGR15` rails, spindle dropped 20 mm in clamp).
- 14-tool (`2×7` @ 56 mm X pitch, `X = 0, ±56, ±112, ±168`) sliding ATC: parked `Y 525/605` (pull-stud tops `Z 235`, +39 mm under `XRoller Bottom` `Z 274`), extends `168 mm` on `Y 326..676` HGR15 rails to `Y 357/437` (hard stops `X ±168..±182, Y 326..336`, 1 mm clear of fixture plate `Y 325`). `3.0 mm` fork plates (`Z 183.65..186.65`, `Ø30.6` U-slots) verified 0 interference against all 14 `iso20_er16_holder.step` holders.
- 3-sided 6 mm splash shields (`X ±318..±324`, rear `Y 702.8..708.8`, `Z 80..270`) verified 0 overlaps.
- Dyfed Steels live stock (27 Nov): `120×80×6.3`, `120×120×8`, `80×80×3..8`, `80×40×2.5..8` (NO `80×60`, `75×50`, `200×150`).
- Never save Fusion documents; the owner saves them. `git commit` needs `-c user.name=Claude -c user.email=noreply@anthropic.com`.

## Done when
- `Type_0_v6` open items resolved, `docs/bom.csv` updated with live prices, `python tools/codemap.py --check` prints "up to date".

## Then
Hand over (`CLAUDE.md`), tick `TASKS.md`, write the next `.claude/NEXT_PROMPT.md` with the template at the bottom of `.claude/TASKS.md`.
