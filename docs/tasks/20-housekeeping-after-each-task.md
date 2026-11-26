# Task 20: Housekeeping after each task

**Start:** branch `claude/hopeful-sagan-28twty`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** any model
**Depends on:** every task

## Read
- docs/HANDOVER.md
- docs/open-questions.md
- docs/tasks/README.md

## Do
1. Tick the task in the README table. Close or update the matching open question. Keep `HANDOVER.md` short: move detail into the task files, not into it.
2. Run `python tools/codemap.py --check` (PowerShell: `$env:PYTHONUTF8=1` first); if it is stale, run `python tools/codemap.py` and fix the hand-written lines of `.claude/CODEMAP.md`.

## Done when
The README table shows the true state; `python tools/codemap.py --check` prints "up to date".
