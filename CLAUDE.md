# CLAUDE.md

**At about 130k tokens of context: stop the task.** Commit what is done, write the handover (`docs/HANDOVER.md`: what is done, what is left, the exact next step; and the task's state in `docs/tasks/README.md`), push, and tell the owner to start a new session.

**Web prices: use curl, never the browser.** Fetch with `curl -sL --compressed` and parse with a short Python script (Shopify: `/products.json`; WooCommerce: `/wp-json/wc/store/products`). If curl is blocked or rate-limited, wait and retry slowly, or report it; do not open the browser.

Start here: `docs/tasks/README.md` (rules and task list).
