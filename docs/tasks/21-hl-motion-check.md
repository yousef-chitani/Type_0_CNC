# Task 21: HL Motion check (all motion parts from one seller)

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** any model (Opus 5.5 is fine), by curl
**Depends on:** none

## Read
- docs/price-check-task-16.md (the task: method, lines, reply block)
- docs/motion-parts-one-seller.txt (the spec)

## Do
1. Curl https://hlmotion.com/ for every line in price check 16. Fill the reply block with live prices, options, UK shipping and lead time.
2. Compare the all-in total with £498.41. Tell the owner; ask before changing `bom.csv`.

## Done when
Every line has a price from the site (or "not sold / quote only"), and the owner has the comparison.
