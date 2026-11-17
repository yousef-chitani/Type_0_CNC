# Task list (16 Nov 2026)

The project is split into small tasks so each can be done in a fresh session with little to read. **One task per session.** Open the task file, read only what it lists, do it, tick it here.

## Rules for every task (the owner's rules, short)
- Branch `claude/hopeful-sagan-28twty` (continues `claude/charming-cori-349jm7`). Commit and push there.
- **Ask the owner before deciding** anything not already decided. Record decisions in `docs/decisions.md` with the next D-number (last used: D-135).
- **Prices:** only from a live page or from the owner, with the date. Never estimate. No eBay. Flag anything more than 10 % or £5 dearer.
- `docs/bom.csv` is the source of truth (CRLF line endings). After editing it run: `python tools/gen_bom_md.py`, `tools/gen_phase1_xlsx.py`, `tools/gen_phase1_cost.py`, `tools/build_open_links.py`, `tools/gen_wave1_sheet.py`.
- **Castings: keep them simple.** Do not add cast-in features. Phase 1 budget £4,200; priced total £3,915.58.
- Write plainly and briefly. Do not merge branch `claude/awesome-ramanujan-by9kds` (old design).

## State in five lines
- Fixed-gantry mill, 2 epoxy-granite castings (base 80.2 kg, portal 37.6 kg), Ampreg 30 resin, hand-tamped.
- Full CAD assembly in `cad/v2/assembly.py`; every Phase 1 part is priced.
- **Task 01 answered (D-131):** no stripping, no granite plate. The owner's issue was picturing the assembly: see `docs/assembly-steps.md`. The owner finds it clear (D-133). Post-cure kept (D-129); portal bolted dry on shims, re-squared with an engineer's square after each move (D-128, D-132, D-133).
- Wave 1 order: 4 Jan 2027. Castings: April–May 2027.
- Background, only if a task needs it: `docs/HANDOVER.md`.

## Tasks

| # | Task | Who | Depends on | State |
|---|---|---|---|---|
| [01](01-choose-how-to-simplify-phase-1.md) | Choose how to simplify Phase 1 | owner | none | done (D-131, D-133) |
| [02](02-price-check.md) | Price check: granite surface plate (only if option B is wanted) | owner's local browser session; any model writes the task file | 01 (B or undecided) | not needed (D-131) |
| [03](03-strip-the-castings-in-the-cad-option-a.md) | Strip the castings in the CAD (option A) | main session (design judgement) | 01 = A | on hold (D-131) |
| [04](04-portal-joint.md) | Portal joint: how it comes apart and goes back | main session | 01; 03 if option A | done (D-128, D-132, D-133) |
| [05](05-rail-bolts.md) | Rail bolts: M5 × 20 instead of M5 × 16 | any model (Opus 5.5 is fine) | none | done: Screwfix A2 M5 × 20 (D-134 fallback) |
| [06](06-trim-the-test-plan-to-the-pours-it-prote.md) | Trim the test plan to the pours it protects | main session | 01 = A (and the post-cure answer) | on hold (D-131) |
| [07](07-curing.md) | Curing: settle the post-cure and the tent | main session | 01 | decided: post-cure and tent stay (D-129) |
| [08](08-schedule.md) | Schedule: portal first | any model (Opus 5.5 is fine) | 01 = A | on hold (D-131) |
| [09](09-fusion-pass.md) | Owner's Fusion pass and feeding it back | owner, then main session | none (03 on hold) | open: owner |
| [10](10-mould-drawing.md) | Mould drawing: portal (cast first) | main session | 09 | open |
| [11](11-mould-drawing.md) | Mould drawing: base | main session | 10 | open |
| [12](12-printed-mould-helpers.md) | Printed mould helpers | Opus 5.5 is fine | 10 | open |
| [13](13-supplier-messages.md) | Supplier messages | owner sends; Opus 5.5 can update the drafts | none | 6 (LiMo) answered 16 Nov, reply 6a sent 16 Nov; C5 price recorded 17 Nov; owner: BK/BF supports page + checkout shipping, then C5 or C7; 5 to send |
| [14](14-z-motor-mount.md) | Z motor mount | main session | 13 (seller's drawing) | open |
| [15](15-wave-1-order-sheet.md) | Wave 1 order sheet | Opus 5.5 is fine | none | done: `docs/wave1-order-sheet.md` |
| [16](16-wave-1-price-re-check.md) | Wave 1 price re-check | Opus 5.5 writes and applies; owner runs it | 15 | open |
| [17](17-tidy-the-old-casting-notes.md) | Tidy the old casting notes | Opus 5.5 is fine | none (03, 06 on hold) | done: 4 disagreements listed in the task file |
| [18](18-rail-seat-and-assembly-procedure.md) | Rail-seat and assembly procedure | main session | 10, 11 | open |
| [19](19-linuxcnc-config-after-the-bench-tests.md) | LinuxCNC config after the bench tests | Opus 5.5 is fine | owner's bench results (build weeks 3–6) | open |
| [21](21-hl-motion-check.md) | HL Motion check: all motion parts from one seller (curl) | Opus 5.5 is fine | none | done: no single seller; owner decides (rails only?) |
| [20](20-housekeeping-after-each-task.md) | Housekeeping after each task | any model | every task | open |

## Order
0. Task 21 done (`price-check-task-16.md`): HL Motion cannot supply everything; rails only are cheaper but UK shipping unknown. Owner decides, may send the draft there.
1. Now: X03 (M5 × 20) and X10 (Silverline square, £9.58) are in `bom.csv`; 05 done. Still open from the AliExpress check: **X11 shims** (owner waiting for a seller). X05 stays the RS PRO straightedge (owner, 15 Nov). Owner: send the 5 drafts in `docs/supplier-messages.md` (task 13).
2. After 01: **03, 04, 06, 07, 08** (and **02** only for option B).
3. After the Fusion pass (**09**): **10, 11, 12**, then **18**.
4. Late December: **16**. Any time: **14, 17**. After the bench tests: **19**.
