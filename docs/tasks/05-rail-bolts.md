# Task 05: Rail bolts: M5 × 20 instead of M5 × 16

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** any model (Opus 5.5 is fine)
**Depends on:** none

## Read
- docs/open-questions.md item 4a
- docs/bom.csv lines X03 and X04
- docs/price-check-task-14.md (format)

## Do
1. Write a small price-check task for 100 × M5 × 20 socket cap screws, grade 8.8 or 12.9, Screwfix or RS first.
2. When the owner's reply comes back, change X03/X04 in `docs/bom.csv`, regenerate (4 scripts in the README), update the wave total in `docs/phase1-schedule.md`.

## Done when
The parts list has M5 × 20 with a dated price; totals agree in all files.

## State (15 Nov 2026)
- Step 1 done: the line is in `docs/price-check-task-15.md` (AliExpress list), owner's choice **grade 12.9 from AliExpress** (D-134).
- Screwfix has M5 × 20 only in A2 stainless: 1941T, 50 pack, £5.89 inc VAT (seen 15 Nov 2026). That's the fallback.
- **Done 15 Nov 2026:** owner found nothing cheaper on AliExpress, so X03 is Screwfix A2 1941T M5 × 20, 2 × £5.89 (X03 £70.47 → £70.67). Regenerated; wave 2 £1,051.71; Phase 1 £3,915.58.
