# Task 17: Tidy the old casting notes

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** Opus 5.5 is fine
**Depends on:** none (03 and 06 on hold, D-131; 07 decided, D-129)

## Read
- docs/eg-moulds.md
- docs/aggregates.md
- docs/epoxy-options.md
- cad/v2/out/assembly/cast_in_features.md

## Do
1. Remove v1 sizes and superseded text (245 kg base, XPS cores, 41 kg of epoxy, GlassCast, vibration table as the main method). Keep reasoning that still holds. Change no decision; list any disagreement between current files.

## Done when
No v1 number left; GlassCast appears only in decision records.

## State (15 Nov 2026): done
- `eg-moulds.md`: v1 sizes table (245 kg base, 41 kg epoxy), XPS cores, v1 mould pictures and vibration-first text removed; v2 masses, PVC portal cores, tamping (D-123) and a pointer to `curing-heat.md` instead. Vibration table kept as the D-123 fallback. "Gantry" renamed "portal".
- `aggregates.md`: v1 300 kg split and the Gravel Works quantities removed; now the bought lines F03, F04, F06 (D-125, D-64).
- `epoxy-options.md`: 41 kg and the GlassCast plan removed; Ampreg 30 chosen, EL2 runner-up, other resins kept.
- `HANDOVER.md`: "GlassCast dropped" sentence removed; "dowel reamed after" corrected to D-128 (no dowels).
- GlassCast still appears, on purpose, as history or comparison: `decisions.md`, `bom.csv` F01 note, price checks 8 and 13, the review files, `curing-heat.md`, `eg-mix-test-plan.md`, `scale-down-options.md`, `simplification-options.md`.

## Disagreements found (no decision changed; owner to confirm)
1. **7-day wait before the rail-seat pour:** the old `eg-moulds.md` said wait about 7 days after the cast; `curing-heat.md` and task 08 have no 7-day wait (post-cure, then rail seats). `eg-moulds.md` now says "after the post-cure"; `eg-mix-test-plan.md` still checks the seat flatness "after 7 days".
2. **Base mass:** `HANDOVER.md` and the task list say 80.2 kg; the generated `cast_in_features.md` says 80.3 kg (after task 04).
3. **Vibration fallback:** D-77 is a tyre table with an eccentric weight on a motor; D-123 says a 3-phase vibration motor from the VFD. `eg-moulds.md` now puts the D-123 motor on the D-77 tyre table.
4. **Old mould pictures** `docs/img/base-mould.svg` and `gantry-mould.svg` still show v1 sizes (900 × 660 × 180). No longer linked; tasks 10 and 11 replace them.
