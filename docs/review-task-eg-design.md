# Review task: Type 0 epoxy-granite design vs real hobbyist builds

**For:** a research/review agent (web access needed). **Output:** one report file, `docs/review-eg-design-report.md`. Don't edit any other file, buy anything or contact anyone.

## Your job
Review the Type 0 cast epoxy-granite (EG) CNC mill design against **documented hobbyist and small-shop EG builds**. Find where our plan:
1. **Differs** from what builders actually do (abnormalities), and whether that difference is justified or risky.
2. **Has known failure modes** that builders have reported (voids, cracks, warping, delamination, inserts pulling out, poor rail seats, cores floating, demould damage).
3. **Could be improved** with methods that have worked for others.

Be sceptical in both directions: say when our plan is fine or better than common practice, too. Every claim about other builds needs a **link** (forum thread, build log, video, paper). Mark anything you couldn't verify as *unverified*.

## The design (read these first)
- `docs/HANDOVER.md`: overview, owner's constraints (UK shed, pieces ≤ 40 kg, budget, no welding, cast not welded)
- `docs/assembly.md` and `cad/v2/out/assembly/cast_in_features.md`: the two castings and every cast-in feature, with sizes and positions
- `cad/v2/out/assembly/castings_tapers.png`, `assembly_iso.png`: pictures
- `cad/v2/out/base_cores_plan.png`, `base_cores_sections.png`: proposed base PVC cores (not yet adopted)
- `docs/eg-moulds.md`: mould method, casting orientation, inserts, demoulding, vibration table
- `docs/curing-heat.md`: resin limits and heat estimate
- `docs/aggregates.md`, `docs/epoxy-options.md`, `docs/bom.csv` (lines F01–F19): materials
- `docs/decisions.md`: why things are the way they are (D-numbers)

Key facts in one place:
- Machine: fixed gantry, moving table. Work area 400 × 250, Z 150. HGR20 rails, DFU1605 screws, 2.2 kW spindle.
- **Base:** one T-shaped casting, spine 340 × 725, rear cross-piece 640 × 230, **110 high**, about 81 kg (71 kg with the proposed cores). Cast **upside down** (machine top face on the mould floor, the floor acts as the jig).
- **Portal:** 800 wide, beam 150 × 130, legs 70 × 130, 375 tall, about 36 kg. Cast **lying on its front (rail) face**. 2 × Ø50 PVC cores in the beam. 45° haunches 60 × 60 at the leg/beam corners.
- **Joint:** portal bolted to the base (2 × M12 rod per leg through cast-in Ø16 tubes into a **10 mm steel bar tapped M12**), grouted, then a Ø10 dowel per leg reamed after grouting.
- **Rail seats:** steel flat-bar inserts (40 × 10 and 25 × 10) **tapped M5** for the rail bolts, held on jig bolts through the mould floor, sitting 3 mm under a recess that gets a self-levelling epoxy pour (rail seat) after curing.
- **Screw supports:** cast channels with small steel insert plates tapped M5; BK12/BF12 bolt on.
- **Mix:** about 11% epoxy by mass (GlassCast 50 PLUS, a slow clear casting resin), quartz 2–5 mm, kiln-dried sand 0–1 mm, whiting filler. Gap-graded (nothing 1–2 mm). DIY vibration table on tyres.
- **Cure:** 7 days at 20 °C in an insulated tent in an unheated UK shed (April–May). No post-cure planned yet (resin Tg 39 °C room-cured).
- **Base cores (proposal):** 5 × Ø50 PVC, axis 65 mm below the top face, 20 mm bottom skin, 15 mm under the support plates. Suspended on M8 threaded rods through each capped core, rods fixed in the mould walls at the core height, plus mid-span wire hold-downs from a batten; rods stay in as reinforcement.

## What to compare (find real examples for each)
1. **Mix design:** epoxy %, resin type (casting resin vs laminating/low-viscosity epoxy), aggregate grading (continuous vs gap-graded), filler type and %, mixing method. Is 11% with a slow clear casting resin normal? Any reports with GlassCast or similar "river table" resins?
2. **Section thickness and mass:** typical wall/section sizes and masses of hobby EG bases and gantries for a machine this size. Is a 110 mm deep base enough? Is a 70 × 130 leg on a 375 tall portal stiff enough?
3. **Casting orientation and the floor-as-jig method:** do builders cast precision faces down? How flat do they come out? Problems with air at the floor face, release, warping?
4. **Inserts:** steel flat bar tapped M5 vs threaded inserts, welded nuts, epoxied-in studs, aluminium plates. Thread engagement in 10 mm steel for **M12 joint bolts** (check: is 10 mm of thread enough for M12, and how do others make the base/gantry joint?). Pull-out failures reported?
5. **Rail mounting:** levelling-epoxy rail seats vs scraping vs epoxy replication vs ground steel bars. Achieved flatness/parallelism in hobby builds.
6. **Cores:** PVC pipe, XPS foam, other. Wall/skin thickness people use around cores. **How they hold cores down** (rods through the walls, straps, posts from the floor), and reports of cores floating or showing through. Are rods left in the casting common?
7. **Re-entrant corners:** fillets/haunches/chamfers in EG castings; any crack reports at sharp corners.
8. **Vibration and compaction:** tables, frequency, duration, layer pouring; over-vibration and aggregate settling.
9. **Curing and temperature:** cure temperature, post-cure practice, Tg concerns, shrinkage, how long before levelling pours. Reports of creep or movement in warm conditions.
10. **Moulds:** MDF/melamine/plastic, release systems (wax + PVA, tape, silicone), demould damage, plugs for openings (our 3-piece wedge plug), draft angles.
11. **Two-piece frame joints:** gantry-to-base joints in EG builds (grout, shims, dowels, bolts), and whether one-piece frames are preferred.
12. **Anything else** that experienced builders consistently warn about and that our plan doesn't cover.

## Where to look (start here, go further)
- Forums: CNCZone (epoxy granite / "EG" mega-thread), MyCNCUK, LinuxCNC forum, Model Engineer, Practical Machinist, Reddit r/hobbycnc and r/CNC, ZeroCNC/PrintNC Discord write-ups, cncarena.
- Build logs: Bootstrap Bill (Expatria), lostzeros mini-mill, "EG CNC" builds on YouTube (e.g. long-running build series), hackaday.io projects.
- Industry: mineral-casting suppliers' design guides (e.g. EPUMENT, Rhodius, Schneeberger, Big Daishowa) for rules on wall thickness, inserts, cores, corner radii.
- Papers on polymer concrete / epoxy granite for machine tools (mix design, damping, modulus).

## Report format (`docs/review-eg-design-report.md`)
1. **Summary** (10 lines max): the 3–5 most important findings.
2. **Findings table**, most severe first:

| # | Area | Our plan | What builders do (with links) | Severity (high / medium / low / fine) | Suggested change |
|---|---|---|---|---|---|

3. **Abnormalities:** things in our plan that nobody seems to do, each with a one-line verdict (justified / risky / unknown).
4. **Open questions** you couldn't settle, and what test or source would settle them (e.g. a specific test brick).
5. **Sources:** every link used.

Keep it plain and short. Use numbers where builders give them (epoxy %, thicknesses, flatness achieved, cure times).
