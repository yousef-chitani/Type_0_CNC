# Things to iron out before wave 1 (14 Nov 2026 → 4 Jan 2027)

Written 9 Nov 2026. Seven weeks, each starting on a Saturday. **You** = owner; **Session** = Claude. Nothing here needs money before 4 January. Sources: `open-questions.md`, `HANDOVER.md` section 6, `review-eg-design-report.md` section 4.

The order matters for two reasons. Your Fusion pass blocks the mould drawings, so it starts early. Wave 1 is electrics, motors, the spindle kit and the cooling loop, so everything on that order must be settled by the last week.

## Week 1: 14 – 20 Nov. Close the loose ends from the review

**You**
- Run **price check 12** (`price-check-task-12.md`): screws, flat bar, plates, Z motor mount, pulleys, belts, outboard bearing.
- Send the **ballscrew seller message** (`supplier-messages.md` section 1): is "Guide Length" overall or thread length, and the end machining.
- Put the **Ampreg 30 kit** in a basket with postcode SA2 and read the delivery charge (stop before payment). Do the same for the Easy Composites release agents (F12), now the only line from there.
- Start the **Fusion pass**: open `cad/v2/out/assembly/type0_assembly.step` (it has the new cores, recesses and joint bars).

**Session**
- **Task 6, first draft:** mix design and test-brick plan for Ampreg 30, hand-tamped, with the review's tests (cut test beam with the real cores, 3 release methods, packing test with and without GCL 1–3 mm, joint-bar pull test, 500 mm rail-seat strip, creep and stiffness prisms).
- Rewrite `curing-heat.md` for Ampreg 30 (18 °C minimum, post-cure 16 h at 50 °C) and size the tent heater for 50 °C.
- Re-render the assembly PNG views (stale since D-114 … D-116).
- Bring `phase1-schedule.md` up to date: wave totals and item lists (epoxy vendor, F20 in wave 2, F21 dropped).

## Week 2: 21 – 27 Nov. Prices settled, casting materials known

**You**
- Send the **GCL** and **Hancock & Brown** messages (`supplier-messages.md` sections 2 and 3): delivery of 2 × 25 kg quartz to SA2, collection of 3 × 20 kg sand. Ask GCL about adding 1–3 mm quartz (the review's fallback for the gap in the grading).
- Continue the Fusion pass: brackets, plates, sensor mounts.
- Decide the **base PVC cores** (5 × Ø50, about −9.6 kg) or leave the base solid. Your FEA can wait, but the decision changes the base mould.

**Session**
- Apply **price check 12** to the parts list; Phase 1 total stops being provisional.
- Add the **tent heater and thermostat** to the parts list and write a small price-check task for them and anything task 6 adds (test-brick moulds, probes, a dial indicator if missing).
- Review task 6 with you: epoxy percentages, number of bricks, what counts as a pass.

## Week 3: 28 Nov – 4 Dec. Fusion pass finished

**You**
- Finish the Fusion pass and work through the **VERIFY list** in `assembly.md` (50 mm motor hole spacing, nut flange flats, BK12 end machining, clamp offset, Y pulley clearance, sensor positions, motor cable exits).
- Send back the STEP (into `cad/v2/in/`).
- Run the small price check from week 2.

**Session**
- Ballscrew answer in: confirm X 850 / Y 600 / Z 350 or change the lengths.
- Design the **printed mould helpers** that don't depend on the Fusion pass (test-brick mould, core hold-down straps, dam strips for the rail-seat pour).

## Week 4: 5 – 11 Dec. Mould drawings start

**You**
- Answer questions from the mould drawings as they come up (lifting points, which faces you can reach, what tools you have for drilling the jig-bolt pattern).
- Check **Aluminium Warehouse** free delivery to SA2: put M11, M12 and A06 in the basket and read the delivery line.

**Session**
- Feed your Fusion changes back into `assembly.py`; re-run the clash check, enclosure and bench.
- **Task 5, first drawings:** base mould (panels, 55 mm recess strips, jig-bolt pattern, channel former, joint bars, lifting points).

## Week 5: 12 – 18 Dec. Wave 1 checks

**You**
- **AliExpress basket clean-up** (logged in): remove the 6 mm ID tube; check the 12 ferrule packs, the HSC8 16-6 crimper and the 20/14 AWG wire; add S08 and S05 and re-check the S08 price (£217.39 + shipping when last seen).
- **USB-RS485 adapter (E24):** check the photos show A+/B−/GND screw terminals.
- Ask the flow switch seller (S05) for the **contact rating** at 24 V DC.
- Prepare the **mini-PC**: is it in hand, and can it boot from USB? LinuxCNC is installed in week 1 of the build.

**Session**
- **Task 5, continued:** portal mould (43 mm recess strips, X channel former, Ø40 cores and hold-downs, three-piece wedge plug, haunch blocks).
- Write the **wave 1 order sheet**: every line, vendor by vendor, with the price last seen and its date, for a final re-check.

## Week 6: 19 – 25 Dec. Light week

**You**
- Read the mould drawings and the test-brick plan once, start to finish, and note anything you can't build with your tools.
- Clear the indoor bench space for the electrics tests (weeks 3–6 of the build).

**Session**
- Fix what you find in the drawings.
- Rail-seat levelling and assembly procedure, first draft (measure, shim or scrape; the test strip decides the method).

## Week 7: 26 Dec – 3 Jan. Final check, then order on Monday 4 January

**You**
- **Re-check every wave 1 price** on the live pages (the prices date from early November): electrics, StepperOnline motors and drivers, Mesa 7I76EU, spindle kit, cooling loop.
- Confirm stock at StepperOnline (the Z driver had no UK stock; it ships from Germany).
- Order wave 1 on **4 January**.

**Session**
- Apply the re-checked prices; flag anything more than 10 % or £5 up.
- Update `HANDOVER.md` and `open-questions.md` for the start of the build.

## Not possible before the parts arrive

- **Safety relay terminal names:** from the label or sheet in the box (needed in build weeks 3–6).
- **Drive and Mesa checks** (ENA logic, ALM polarity, V4.1 manual): on the bench.
- **VFD parameters** and **spindle minimum rpm:** from the manual and label in the kit.
- **Bench leg length:** after the feet (T02) arrive in wave 2.
