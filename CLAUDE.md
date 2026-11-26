# CLAUDE.md

**At the end of every task: hand over.** Commit what is done, write the handover (a new entry at the top of `docs/HANDOVER.md`: what is done, what is left, the exact next step; and the task's state in `docs/tasks/README.md`), and push. Keep only the two newest entries in `docs/HANDOVER.md`: move older ones, unchanged, to the top of the entries in `docs/handover-archive.md`.

**At about 130k tokens of context: stop the task.** Hand over as above, and tell the owner to start a new session.

**Web prices: use curl, never the browser.** Fetch with `curl -sL --compressed` and parse with a short Python script (Shopify: `/products.json`; WooCommerce: `/wp-json/wc/store/products`). If curl is blocked or rate-limited, wait and retry slowly, or report it; do not open the browser.

**No stand-ins for real parts.** Never use a stand-in (a box, a guessed shape, rough sizes) when an accurate STEP or drawing of the part is available: use it. If none is in the repo's folders (e.g. `cad/vendor/`), stop and ask the owner to fetch it.

Start here: `.claude/NEXT_PROMPT.md` and `.claude/CODEMAP.md`; then the rules in `docs/tasks/README.md` (lines 5 to 11) and only the table row you need.

## Navigation and handoff (keeps sessions cheap)
- **First, read `.claude/NEXT_PROMPT.md` (if it exists) and `.claude/CODEMAP.md`.** Then only the files they name.
- Go straight to files from the map. Grep/glob only for what the map does not cover, and narrowly (one folder, one pattern), never the whole repo.
- Read line ranges, not whole files, unless the file is under about 150 lines or you are editing most of it. `docs/tasks/README.md`, `docs/decisions.md` and `docs/HANDOVER.md` are long: read the rules, the row or the D-number you need.
- Do not re-read a file this session unless it changed.
- When you add, move, rename or delete a file or a public function, update `.claude/CODEMAP.md` in the same task: run `python tools/codemap.py` (tree, script index, where-index), and fix the hand-written lines. A stale map is worse than none. `python tools/codemap.py --check` tells you if it is stale.
- **Work in bundles** from `.claude/TASKS.md`: tasks that share files or context, done in one pass (load once, change all, check once at the end, tick off). Small related finds fold in; others go to the right bundle. Split a bundle across sessions only if it is too big, and say exactly where you stopped. `docs/tasks/README.md` stays the record of task state; TASKS.md only groups the work.
- **End of every bundle (or a forced stop):** the handover above, plus overwrite `.claude/NEXT_PROMPT.md` with the template at the bottom of `.claude/TASKS.md`, and print it in chat. The handover's "exact next step" points to it.
