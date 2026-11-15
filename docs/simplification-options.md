# Phase 1 simplification: two ways (15 Nov 2026)

**For the owner to choose. Nothing here is decided or in the CAD.** Your brief: the castings and layout as simple as possible, a well-beaten path, the least chance of a failure that can't be recovered, because the budget to redo is small.

## First, where the real risk is

- **A pour is one shot.** Voids, a shifted insert, or a casting stuck in its mould can't be fixed afterwards. Everything else on this machine (rails, screws, electrics, software) can be adjusted or redone.
- **Epoxy granite is not a well-beaten hobby path.** The design review read about 5,000 forum posts and found only three finished machines with useful detail, one of them a failure. Its lesson, from industry and from the builder who succeeded (DaBit): **keep the precision out of the casting.** Cast a plain heavy block, and add the accurate surfaces afterwards with things that can be adjusted or redone.
- **What a failed pour costs:** redoing the base needs about 9 kg of resin (two 4.66 kg packs, £208.40 at the 15 Nov price) plus stone and about 4–6 weeks. Redoing the portal needs about half that. The budget has £282 spare before delivery charges, so it covers **one** failed pour, not two.

## Option A: keep the two castings, strip them

Same machine, same parts list. Every cast-in feature that isn't needed to make Phase 1 run comes out, and nothing accurate is cast.

| Change | What it removes |
|---|---|
| **Portal solid, no cores** (about 40.4 kg) | Core pipes, hold-downs, the 20 mm walls, the test beam section |
| **No Phase 2 parts cast in** (ATC bracket insert) | One insert; Phase 2 fixes to the leg with a bonded plate later |
| **Base solid** (drop the PVC core proposal) | 5 cores and their rods; base stays 80 kg |
| **Portal joint: 4 rods + grout bed that releases, stop blocks glued on afterwards** | Dowel sleeves in both castings, any insert for the stops |
| **Cast the portal first**, as the rehearsal | It is the cheaper one to lose. The base is poured only after the portal is out of its mould and inspected |
| **Tests cut to those that protect a pour:** packing test, 3 mix bricks (with the release test), heat brick with the pull-test bar, rail-seat strip | Beam section, prisms, creep test |
| *(optional)* no 50 °C post-cure | The PIR tent and ramp. Room-cured Ampreg has a Tg of 57 °C, already far above GlassCast's 39 °C. A simple cover and the heater at 20 °C still needed |

What stays, because it is the proven way: steel bars with tapped holes cast in under the rails, held on bolts through the mould floor; rail seats made flat afterwards with a resin pour, then measured and shimmed or scraped; the casting orientation (precision faces down).

**One-shot risks left:** two pours (one rehearsed by the other); insert bars set by the mould floor; release.
**Recoverable:** rail-seat flatness (re-pour, shim, scrape), squareness (stops), everything bolted on.

## Option B: bought granite surface plate as the base, cast only the portal

The base becomes a granite inspection plate. Its flatness is bought, not made. Rails, screw supports and the portal are bolted to threaded inserts glued into holes drilled in the granite. This is how commercial granite machine bases and measuring machines are built, and several hobby builds do it (the review's sources include one).

| | |
|---|---|
| **Removes** | The base casting, its mould, the Y rail-seat pour, the cast-in Y bars, half the casting materials and most of the heat and cure worry |
| **Adds** | The plate; about 30 holes drilled in granite with diamond core bits and water; glue-in threaded inserts; 4 spacer blocks under the table (the screw sits 15 mm higher without the cast channel); a new base in the CAD, bench and enclosure |
| **Why it is lower risk** | Each hole is set from the real rail and potted in epoxy, so a hole a millimetre out doesn't matter, and a bad one can be redone. Nothing about the base is one shot |
| **Still cast** | The portal, as in option A (solid, about 40 kg, X rail seats by resin pour). So one pour, not two |
| **The catch: weight** | The layout needs a plate about **630 × 630 mm**. At 80 mm thick that is about **95 kg**; at 100 mm about 117 kg. The cast base is 80 kg and already a two-person lift. This is the piece that has to go up the stairs to the flat |
| **Unknown** | The price and delivery of the plate (a pallet). Not priced: needs a price check before this option can be judged on cost |

## Side by side

| | A: stripped castings | B: granite base |
|---|---|---|
| One-shot pours | 2 (portal rehearses the base) | 1 |
| Base flatness comes from | Resin pour, then shim or scrape | The plate, as bought |
| Worst realistic loss | One casting: about £100–210 of resin and a month | The portal: about £100 of resin and a month |
| Heaviest piece to carry | 80 kg | about 95–117 kg |
| New skills | Mixing, tamping, release, levelling pour | The same for the portal, plus drilling granite |
| Rework to the design now | Small: remove features from `assembly.py` | Large: new base, bench, enclosure, parts list, another price check |
| Parts already priced | All still valid | Epoxy, stone, MDF and flat bar shrink; plate, core bits, inserts are new |
| How well-beaten | The reviewed method, minus its risky parts | The standard way to build on granite |

## Recommendation

**Option A, with the portal cast first**, unless you are willing to carry a 95 kg plate upstairs.

- B has the lowest chance of an unrecoverable failure, and it is the better-proven method. But it swaps a casting risk for a handling risk: a heavier, brittle piece on the stairs, and it reopens the design six weeks before the first order.
- A keeps what is already designed and priced, removes the parts of the casting that the review flagged, and turns the cheaper casting into the rehearsal for the dearer one. The £282 of headroom covers losing one pour.

If B is tempting, the next step is cheap: a price check on 630 × 630 granite plates (80 and 100 mm, with delivery to SA2), then decide.

## Not included, but ask if you want them

- **Direct drive on X and Y** instead of belts: fewer small parts, but it needs motor mounts that fit the 50 mm motor holes (the same problem as the Z mount) and a wider enclosure later. It does not make the castings simpler, so it is not in option A.
- **Copying a published open-source mill** end to end: the most beaten path of all, but a lighter machine with different rails and screws, so most of the parts list would change.
