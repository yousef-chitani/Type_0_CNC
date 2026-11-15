# Tasks to hand off to Opus 5.5

Written 15 Nov 2026. These are the jobs on the project that are well defined, have a clear "done", and need care more than design judgement. Each brief below is written to be pasted into a fresh session on this repository (branch `claude/charming-cori-349jm7`). Every session should read `docs/HANDOVER.md` first, section 5 (the owner's rules) above all.

**Rules that apply to every task here**
- Only prices seen on a live page or given by the owner, with the date. Never estimate.
- No eBay. Flag any swap costing more than 10 % or £5.
- `docs/bom.csv` is the source of truth; it uses CRLF line endings. After editing it run `python tools/gen_bom_md.py`, `tools/gen_phase1_xlsx.py`, `tools/gen_phase1_cost.py` and `tools/build_open_links.py`.
- Record decisions in `docs/decisions.md` (next number after the last line). Ask the owner before deciding anything that isn't already decided.
- Write plainly. Commit and push to the branch.

## Keep in the main session (not for hand-off)

- Mould drawings (task 5): mouldability, casting orientation, demoulding.
- Reading the test-brick results and choosing the mix.
- Rail-seat levelling and assembly procedures.
- Any change to the castings, and anything structural, thermal or safety-related (the safety chain, the tent heater).
- Feeding the owner's Fusion changes back into `cad/v2/assembly.py`.

## Tasks to hand off

### 1. Apply a price-check reply to the parts list
**When:** each time the owner uploads a reply (12 and 14 are pending).
**Brief:** "Apply the attached price-check reply to `docs/bom.csv`: price, VAT basis, date checked, link and notes for each line; add new lines where the task file defines new IDs. Regenerate the derived files. Update the wave totals in `docs/phase1-schedule.md` so they sum to the Phase 1 total in `docs/phase1-cost.md`. Mark the task file as done at the top. List every PREMIUM line for the owner and anything in the reply that doesn't match the spec. Don't choose between alternatives: ask."
**Done when:** the totals agree in all files and no line in the reply is left unapplied or unexplained.

### 2. Wave 1 order sheet
**When:** week of 12 Dec (see `docs/pre-wave1-plan.md`).
**Brief:** "From `docs/bom.csv` and the wave 1 row of `docs/phase1-schedule.md`, write `docs/wave1-order-sheet.md`: one table per vendor with ID, item, quantity, option to select, last price and its date, link. Add a column for the owner to tick. List the open checks from `docs/open-questions.md` that must be closed before ordering, next to the lines they affect."
**Done when:** every wave 1 ID appears once and the sheet total equals the wave 1 total.

### 3. Wave 1 price re-check task and its reply
**When:** 26 Dec – 3 Jan.
**Brief:** "Write `docs/price-check-task-15.md` in the format of task 13, covering every wave 1 line, for the owner's local browser session. When the reply comes back, apply it as in task 1."

### 4. Consistency sweep of the older docs
**When:** any time.
**Brief:** "`docs/eg-moulds.md` and `docs/aggregates.md` still carry v1 sizes and quantities (245 kg base, 300 kg of aggregate, 41 kg of epoxy, XPS cores, 180 mm sections) below the newer notes. Bring them in line with `cad/v2/out/assembly/cast_in_features.md`, `docs/eg-mix-test-plan.md`, `docs/curing-heat.md` and decisions D-102 … D-124. Keep the reasoning that still holds, delete what is superseded, and don't change any decision. List anything where two current documents disagree instead of picking one."
**Done when:** no v1 number is left in those two files, and a grep for GlassCast finds only history notes and decision records.

### 5. Supplier messages
**When:** as needed.
**Brief:** "Update `docs/supplier-messages.md`: quantities from `docs/bom.csv`, add a message to EC Fibreglass Supplies asking the delivery cost to SA2 for one 22.68 kg Ampreg 30 kit and whether the resin and hardener ship as dangerous goods, and add the 1–3 mm and third-bag questions to the GCL message. Drafts only: the owner sends them."

### 6. Printed mould helpers (simple parts)
**When:** after the test plan is agreed.
**Brief:** "In `cad/v2/printed_parts.py` (PETG, Bambu P1S, see `docs/printed-parts.md`), add: a split test-brick mould 100 × 100 × 100 is NOT wanted (moulds are MDF); instead model the small helpers: core hold-down straps for Ø40 pipe, end caps for Ø40 pipe, sleeve locators for Ø16 and Ø12 tubes on an 18 mm MDF floor, and jig spacers that set an insert bar 5 mm above the floor. Export STL to `cad/v2/out/print/` and add them to `docs/printed-parts.md`. Take every dimension from `cast_in_features.md`; where a dimension depends on a bought part, mark it VERIFY."
**Done when:** each part exports, has a print orientation and material noted, and nothing is sized from a guess.

### 7. LinuxCNC config upkeep
**When:** after the owner reports bench-test results (build weeks 3–6).
**Brief:** "Apply the owner's bench results to `linuxcnc/type0/` (ENA and ALM polarity, VFD parameters, minimum spindle rpm) following `docs/linuxcnc.md` section 6, re-run the simulator test (`linuxcnc/type0/sim/test_sim.py`, 23 checks) and update `docs/electrical.md` section 5. Don't touch the e-stop chain or the brake wiring logic: report instead."
**Done when:** the simulator test passes and every changed value cites the owner's measurement.

### 8. Housekeeping after each working session
**Brief:** "Bring `docs/HANDOVER.md`, `docs/open-questions.md` and `docs/pre-wave1-plan.md` in line with the latest decisions and commits: close what is closed, renumber nothing, keep the 'who answers' line on every open question."

## How to hand one off

Start a new session on this repository with Opus 5.5 selected, paste the brief, and attach any reply file it mentions. Ask it to finish with a list of what it changed and anything it left for the owner or the main session.
