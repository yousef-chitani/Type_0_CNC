# EG moulds: fabrication and demoulding

> **Status:** draft for review. All dimensions are placeholders to make the drawings concrete. They will be fixed when we do the full layout.

## Changes from the EG design review (2026-11-09, D-114 … D-120)

The review (`review-eg-design-report.md`) compared this plan with real builds. What changed:

- **Resin:** Ampreg 30 + 3X Slow replaces GlassCast 50 PLUS everywhere (D-117, D-122). Cure at 18 °C or more for at least 48 h, then post-cure 16 h at 50 °C (see epoxy-options.md).
- **Portal cores:** 2 × Ø40 PVC with every wall 20 mm or more (D-114). Hold each core down from a batten over the open face (wire or thin rod to a strap round the core): about 1.4 kg of lift each.
- **Rail seats:** recesses 5 mm deep and open to the casting edges, so no thin EG lips or rims (D-115, sketch `cad/v2/out/rail_seat_options.png`). The floor strips that form them are 55 wide (base, running out to the spine side wall) and 43 wide (portal, from the beam edge to the channel former). For the levelling pour, tape a dam strip along each open side.
- **Rail-seat accuracy:** expect the long cast-in bars to bow 0.1–0.3 mm as the casting shrinks. A free pour levels to about 0.1 mm, not 0.01–0.02 mm. Plan to measure with a straightedge and a dial indicator, then shim or scrape. Do a 500 mm test strip first. Remove the meniscus at the dam edges.
- **Inserts:** abrade and degrease every insert; plug threaded holes from the back; short screws as anchors, no welding; vent holes through the joint bars (Ø8) and BK/BF plates (Ø6); tamp a resin-rich fine mix under and against each insert first (D-118).
- **Joint bars:** 40 × 20, for 20 mm of M12 thread (D-116).
- **Mix behaviour and compaction (D-123):** at about 11% epoxy the mix is like damp sand, not a liquid. **Compact by hand: tamp each 30–50 mm layer** with a flat-ended rod or block, working along the walls, corners and inserts first. No vibration motor is bought unless the test bricks and the cut test beam show voids that tamping can't remove. The buoyancy figures below are a safe upper limit; hold the cores down all the same.
- **Mould floor:** on a stiff, continuous deck, not battens alone. Check it with a straightedge before the pour (aim under 0.5 mm). Bolt the inserts down hard so vibration can't move them. Seal all MDF edges with resin or varnish, not tape alone.
- **Release:** test 3 ways on the test-brick moulds, then use one (D-120). No silicone sprays.
- **Second pours** (rail seats, grout): wash the surface with water, abrade and clean first. Log humidity with temperature.
- **Bench:** the base sits on 3 steel pads (D-119).

![Base mould](img/base-mould.svg)

![Gantry mould](img/gantry-mould.svg)

## Draft sizes and mass (solid castings, D-30)

| Casting | Size (mm) | EG mass | Epoxy at 11% |
|---|---|---|---|
| Base | 900 L × 660 W × 180 H | about 245 kg | about 27 kg |
| Gantry | 640 W × 460 H; beam 200 × 160; uprights 120 × 160 | about 70 kg | about 8 kg |
| **Total** | | **about 315 kg** | **about 35 kg** |

Add about 3 kg of epoxy for the leveling pours, 1 kg for grout and 2–3 kg for test samples: **about 41 kg to buy**. The base alone is near the top of the frame-mass budget (200–350 kg). Check the stand design against about 400 kg in total, including the moving parts and the enclosure.

## The key idea: the mould floor is the jig

Each casting is poured **with its precision face down on the mould floor**:

- **Base:** cast upside down. The machine's top face is against the floor.
- **Gantry:** cast lying on its front (X-rail) face.

Everything that must be in the right place (rail insert bars, gantry foot pads, ballscrew bearing-block pads) is **bolted through the floor** with the real rail-bolt pattern drilled into it. The floor is one flat, drillable sheet. You mark it out on the bench before pouring, and the inserts can't drift during vibration.

The other side benefits too. Air rises when the mix is vibrated, so the floor-side face comes out the densest and cleanest. The rough open face becomes the underside (base) or the back (gantry), where finish doesn't matter.

Shallow **raised strips** on the floor (about 3–5 mm) leave recessed channels over each insert bar. Those channels later take the **self-leveling epoxy pour** that forms the rail seat. Link the two channels with a cross-channel so both rails settle at the same level.

## Hollow cores: assessment (not used, see D-30)

**Recommendation: closed cores (XPS foam left inside), not open channels.**

| Option | Stiffness | Effort | Verdict |
|---|---|---|---|
| Cores open to the underside (U-channel) | Poor in twist: an open section is many times less stiff in torsion than a closed box | Easiest: just lift the mould off | ✗ |
| **Closed XPS cores with a 40 mm bottom skin** | Keeps a closed box section, so most of the solid section's stiffness at about 65% of the weight | Needs hold-down posts | ✓ |
| Solid | Best damping | Most epoxy, most curing heat, about 230 kg base | Fallback |

How to make the cores:
- **Material:** XPS insulation board (the pink or blue kind), glued up in layers and cut to size. Its compressive strength (about 300 kPa) is far more than the EG pressure (about 4 kPa at 180 mm depth). Wrap the cores in packing tape so the epoxy can't soak in.
- **Buoyancy is the big risk.** Vibrated EG behaves like a heavy liquid (about 2,300 kg/m³). The three base cores add up to about 0.03 m³, which is **about 70 kg of upward force**. Hold them down with **posts from a batten** screwed across the top of the mould walls. Each post leaves a small hole in the bottom skin, which is useful for running cables and air lines.
- **Cross ribs** (60 mm) split each core row into segments, adding stiffness against twist. Keep **solid EG under the gantry feet** and under the motor and bearing mounts.
- **Gantry:** core the beam only. The uprights (120 mm wide) are too narrow to leave useful walls around a core.

### Evidence check (2026-11-04)

The owner asked for real examples before choosing cores. What I found:

- **PVC pipe cores** are well documented in DIY EG builds, mostly for cable and bolt channels and for ballscrew clearance ([model-engineer.co.uk](https://www.model-engineer.co.uk/forums/topic/diy-epoxy-frame-based-cnc-mill/), [lostzeros mini-mill](https://www.lostzeros.com/mini-mill-cnc-conversion-epoxy-granite-base-and-column-assembly/), [CNCCookbook](https://www.cnccookbook.com/epoxy-granite-cnc-machine-fill/)).
- **XPS foam cores** in DIY EG are rarely documented. One builder planned XPS cores to save epoxy and weight, but the result was never reported ([MyCNCUK thread 12972](https://www.mycncuk.com/archive/index.php/t-12972.html)). In the long CNCZone/CNCArena EG thread, one builder reported a 5×5×10 in foam core showing through the back of a test base, because the wall over it was too thin. I couldn't open that thread to verify the details.
- **Industrial mineral casting** does use hollow and weight-reduced structures ([Big Daishowa mineral cast catalogue](https://catalog.bigdaishowa.com/view/494013/129)), but there are no DIY details.

**Conclusion:** large closed foam cores are not a proven DIY method. The options are:
1. **Solid** (most proven. About 245 kg base, about 11 kg more epoxy).
2. **PVC pipe cores** (proven in DIY, smaller weight saving). A row of capped 75–110 mm pipes is easy to hold down and gives a closed section.
3. **XPS cores, but only after a test casting.** For example, cast a 500 mm beam with a core, then cut it in half to check for voids and core movement.

## Building the moulds

- **Material (D-61):** floors from one 18 mm MDF sheet, sealed and coated. Walls from white gloss 18 mm furniture panel. The floor sits on 40 × 40 mm battens every 300 mm or so, so it stays flat on the vibration table.
- **Joints:** screws only, **no glue**, so every wall comes off. Seal inside corners with a small fillet of silicone or plasticine, which also gives the casting rounded edges that resist chipping.
- **Release (D-120):** seal the MDF first. Then test on the sample moulds: (a) 3–5 coats of mould wax, buffed; (b) the same wax + 1 coat of PVA; (c) packing tape on all faces + wax in the seams. Use the one that releases best. Use mould wax, not furniture wax. No silicone sprays: later pours will not bond.
- **Bracing:** batten the walls every 200 mm. Vibration makes unbraced walls bulge.
- **Inserts (D-118):** steel insert bars (40 × 10 and 25 × 10 mm, tapped M5 at the 60 mm rail-bolt pitch) with short screws in tapped holes on the back to anchor them (no welding). Abrade and degrease the bars; plug the threads from the back. Coat the jig bolts in wax.
- **Gantry joint:** waxed steel or PVC tubes form the M12 bolt holes through each upright. The upright feet are cast against a mould end wall, so they come out flat.
- **Gantry opening:** a **three-piece wedge plug** (two halves and a tapered centre wedge with 2° draft). The beam and uprights shrink onto it on three sides, so a one-piece block would be very hard to get out.
- **Lifting points:** cast M12 nuts on threaded rod into the open face, two or four per casting, for an engine crane.

## Pour and demould sequence

1. Mould on the vibration table, checked level and flat. Inserts bolted on. Temperature probes in place (see Thermal management).
2. Mix in small batches. Wet the aggregate with resin first, then vibrate while pouring in layers about 50 mm deep.
3. Cure at room temperature for the time the chosen resin's datasheet gives (D-117; see curing-heat.md). No extra heat during this first cure: early heat can warp the casting. Then **post-cure** in the tent to the datasheet schedule, let the casting cool to room temperature, and only then demould.
4. **Remove the jig bolts through the floor first.** They hold the casting to the floor.
5. Remove the hold-down batten, then unscrew the walls. For the gantry, pull the centre wedge first, then the plug halves.
6. Lift the casting from the open-face lifting points and turn it over on a padded surface. The floor comes off last.
7. Inspect: tap the surface to find hollow-sounding voids, and check the inserts with a rail bolt.

## Risks

| Risk | Mitigation |
|---|---|
| Mould bulges | Battens every 200 mm. Run the vibration test with sand first |
| Resin leaks at corners | Silicone fillets and taped edges |
| Casting sticks to the mould | Release tested on samples (D-120). Screw-only joints |
| Opening plug jams | Three-piece wedge plug with draft |
| Warping or cracking from curing heat | See Thermal management |

## Thermal management (to research; owner is looking into this)

Solid sections up to 180–200 mm thick concentrate the curing heat. Starting points to verify:

- **The aggregate soaks up the heat.** At about 11% epoxy, most of the mass is stone, so the temperature rise is far smaller than for a pure resin pour of the same size. Measure it on the test bricks before relying on this.
- **Slow hardener** and a **cool, steady room** (about 15–20 °C). Avoid days when the garage gets very warm.
- **Pre-condition the materials.** Store the aggregate and resin in the same room for 24 h, so the starting temperature is known.
- **Measure it.** Cast thermocouples or cheap DS18B20 probes into the centre and near the surface of the base, and log the temperatures. Make the test bricks the same thickness (180 mm) as the real casting, so the peak temperature is representative.
- **Pour continuously, without stopping.** Pouring in stages can leave weak joints between layers. Mix in batches, but keep pouring.
- **Even cooling.** Leave the walls and insulation on until the peak has passed, so the surface and core cool together. This avoids stresses locked in by uneven cooling. Post-cure warm (e.g. 40 °C) only after the first cure.
- **Let it settle before the leveling pour.** Wait for full cure (about 7 days or more) before the rail-seat leveling pour, so the casting has finished shrinking.

## DIY vibration table (D-77; only if tamping fails, D-123)
- **Springs:** 1–2 old tyres lying flat. Two tyres side by side give a steadier platform for the base mould (about 700 × 500 mm).
- **Deck:** stiff board (18 mm ply or MDF on CLS battens) slightly bigger than the largest mould. Screw blocks to the deck so the mould can't walk off.
- **Exciter:** a motor bolted under or on the deck edge, with an eccentric weight on its shaft (e.g. a drilled disc or bolt with a nut stack). Fit a **speed control** (F21, D-119) and sweep roughly 40–75 Hz (2,400–4,500 rpm) on each test brick: note the speed where the mix slumps and flows (EG makers tune between 68 and 72 Hz), and use it for every pour. Aim for 2 g or more at the deck (a phone accelerometer app shows it). Add weight until the surface of a test pour ripples and air bubbles rise steadily.
- **Safety:** guard the spinning weight. Clamp the motor so it can't shake loose. Use an RCD-protected socket.
- **Test first:** run it with a sand-filled mould. Check the deck doesn't flex or walk, and the mould joints don't leak.
- **Tip:** vibrate each layer for a short time as you pour, not one long run at the end. Over-vibrating can let the coarse grit settle to the bottom.
