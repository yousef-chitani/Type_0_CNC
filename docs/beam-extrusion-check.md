# Beam: Vallder CNC extrusion instead of the JLC U channel? (17 Nov 2026)

**For the owner to choose. Nothing decided; D-147 stands until then.** Source: the owner's saved Vallder pages (17 Nov 2026). Rate 1 EUR = £0.8345 (ECB via frankfurter.app, 16 Nov 2026, curl).

## The two profiles (from the saved pages)

| | 200 × 96 | Heavy 235 × 125 | JLC U channel (step 4 proposal) |
|---|---|---|---|
| Alloy | 6063, anodised | 6063, anodised | 6061, machined |
| Mass per m | 8.20 kg | 14.80 kg | |
| Beam 890 long | **7.3 kg** | **13.2 kg** | 17.8 kg (with plate) |
| Price | €94.00 per m, cut 200–6000 | €137.00 per m | not priced (STEP quote) |
| 890 long | €83.66 = **£69.82** | €121.93 = **£101.75** | |
| Shipping to the UK, import costs | **not known** (the site says "EU warehouse, shipping across Europe") | not known | |
| Made for | HGR20 + SFU16 + FK12/FF12 | HGR20 + SFU20/25 | |
| Rail pads | 2 × 20 wide, about **126 apart** (measured off the drawing), rails held by M6 T-nuts | not in the saved files | 100 apart (D-104), M5 tapped |
| Screw channel | 66 wide, between the rails | yes (picture) | 80 × 20, machined |

## Stiffness (my estimate, not from Vallder)

Thin-wall model from the mass per metre only. It puts all the metal on the outside, so it **over-states** both profiles. The saved files give no inertia figures, and there's no drawing for the heavy profile.

| EI (MNm²) | 200 × 96 | 235 × 125 | JLC U channel |
|---|---|---|---|
| Force in Y (cut along Y) | **≤ 0.38** | **≤ 1.1** | 0.90 |
| Force in Z (plunge) | ≤ 1.2 | ≤ 2.9 | 1.13 |
| Y deflection, 200 N at mid-span, span 690, simply supported | ≥ 3.5 µm | ≥ 1.2 µm | 1.5 µm |

Both are closed multi-cell sections, so they twist much less than an open channel.

## What it fixes

- **It solves both step 4 problems.** The X screw channel is built in. The beam-to-foot joint can use end plates, bolted into the Ø8.5 holes tapped M10 at the profile ends (as Vallder's own design does).
- **It's lighter** (13.2 kg vs 17.8 kg) and has a known metal price.
- **It's well proven.** Vallder sells these for DIY router gantries, so others have built on them. What's new here is the EG tub underneath.
- **It can still be filled later** (D-147): the cells are open at the ends.

## The risks

- **The rail seats are not machined.** They're as-extruded anodised faces. The page states no flatness or straightness, only "very minimal tolerances". On a mill this is the main risk. Fixes: epoxy-replicate the seats, or have a local shop skim the pads. JLC machines only its own stock, so it can't skim them.
- **6063 is softer than 6061.** Threads are weaker, which is why Vallder uses T-nuts.
- **The rails are about 126 apart**, not 100 (D-104). The 180 saddle still fits: the blocks' outer edges come to ±85.
- **X screw length:** Vallder puts the FK/FF on end plates, so the screw is the profile length + 62. On an 890 beam that's 952: over the 950 DDP limit and not the 700 bought. Keeping BK12/BF12 inside the channel, just outside the X block travel (step 4), keeps the 700.
- **UK shipping may not be offered**, and import VAT and duty are unknown.

## Questions for the owner

1. **Which beam:** the heavy 235 × 125, the 200 × 96, or keep the JLC channel? My pick: **the heavy 235 × 125**, if its drawing confirms EI near 1.
2. **Please download Vallder's 2D/3D files** for both profiles (the page has a "Downloads 3D / 2D" link). I need them to work out the real stiffness and rail positions.
3. **Shipping:** does Vallder ship to the UK, and at what cost? Please check at their checkout. Curl can't do a checkout.
4. **Rail seats:** epoxy replication, a local skim, or bolt the rails straight on as extruded?
