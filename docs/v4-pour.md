# V4 EG fill plan and quantities (Task 27 Task 7, 26 Nov 2026)

Per **D-315**, the V4 epoxy-granite (EG) fill is **for mass and damping only, not structural**. No mould, post-cure tent or precision cast-in rail strip is required for the frame: a lean mix (as little epoxy as cleanly binds the aggregate with minimal voids, confirmed by the 4 test bricks in `docs/eg-mix-test-plan.md`) is hand-tamped into the base tray pockets and gantry beam.

## 1. Volumes and masses (from `Type_0_v4`)

| Cavity | Dimensions (mm) | Volume (L) | Mass at 2.29 kg/L (kg) | Binder at 11 % provisional (kg) |
|---|---|---|---|---|
| Base pocket Y- | 500 × 155 × 90 | 6.98 | 16.0 | 1.76 |
| Base pocket Y+ | 500 × 155 × 90 | 6.98 | 16.0 | 1.76 |
| Beam SHS core (`120×120×8`, cut round bolt heads & screw tips) | 890 × 104 × 104 | 9.57 | 21.9 | 2.41 |
| **Machine total** | | **23.53 L** | **53.9 kg** | **5.93 kg** |
| 4 mix test bricks (`docs/eg-mix-test-plan.md`) | — | ~4.0 L | 9.2 kg | 1.01 kg |
| **Total incl. test bricks (+10 % aggregate waste)** | | **~27.5 L** | **~63.1 kg** | **~6.94 kg** |

## 2. Materials bought (`bom.csv`, D-336)

- **Binder (`F01`, D-336):** `2 × 4.66 kg` Gurit Ampreg 30 resin + Slow hardener packs (**9.32 kg** total binder, £208.39 inc VAT at EC Fibreglass Supplies), leaving ~2.4 kg margin over the 11 % figure (more if the bricks pass at 8–9 %).
- **Coarse quartz 2–5 mm (`F03`):** `2 × 25 kg` bags (50 kg bought, ~31 kg used).
- **Kiln-dried sand 0–1 mm (`F04`):** `2 × 20 kg` bags (40 kg bought, ~25 kg used).
- **Whiting < 0.1 mm (`F06`):** `1 × 25 kg` bag (~6 kg used).
- **Sealant & tape (`F18`):** neutral-cure silicone (`No Nonsense 291`) + packing tape.

## 3. Preparation and fill order

### A. Mix test bricks first
Make the test bricks (`docs/eg-mix-test-plan.md`) to pick the leanest binder fraction that tamps cleanly without crumbly edges.

### B. Base tray (`2 × 6.98 L` open-top pockets)
1. Tap/check all holes in the 2 steel end plates (`F26`) before assembly.
2. Bolt the 4 KJN `90 × 90 × 500` profiles (`F25`) between the 2 end plates (`8 × M16 × 40`, `F27`) on a flat surface and check diagonal squareness.
3. Run a bead of `F18` neutral-cure silicone along the bottom edges bordering the two `155 × 500` pockets, tape any open profile slot ends facing the pockets, and bolt the `500 × 670 × 3` laser-cut steel bottom sheet (`F28`) into the profile bottom slots (`12 × M6 × 12` + M6 T-nuts). Let the silicone skin/cure.
4. Mask the top faces of the aluminium profiles and end plates with packing tape.
5. Mix and hand-tamp the EG in ~30 mm lifts into both open `155 × 90 × 500` pockets, finishing 1–2 mm below the profile tops (`Z = -75`) so the ground Y rail seat bars (`F29`) bear strictly on the aluminium profiles and never on the EG.

### C. Gantry beam (`9.57 L` closed SHS `120 × 120 × 8 × 890`)
> **Critical rule (D-310, D-323):** Every hole through the beam walls must be drilled and tapped **before** the EG fill, and bolts whose heads sit inside the tube or whose tips project past the 8 mm wall must be fitted (or waxed/greased dummy screws fitted) before tamping.

1. Drill and tap all beam holes while empty:
   - Bottom wall (`Z = 160..168`): `4 × Ø13` clearance holes at `(X = ±295, Y = 220 & 280)`.
   - Front wall (`Y = 190..198`): `12 × M8` tapped through-holes (`X = -310..+490, Z = 195 & 245`).
   - Top wall (`Z = 272..280`): `8 × M6` tapped through-holes for the X HM12 and BF12 ground pads.
   - Rear wall (`Y = 302..310`): `8 × M10` tapped through-holes for the rear spacer countersunk screws (`D-323`).
   - Both end faces (`X = -350` and `+540`): `4 × M5 × 15` blind tapped holes per end in the 8 mm walls (`D-335`).
2. Degrease the bore. Insert the **4 × `M12 × 35` beam-to-upright bolts** from inside the bore through the bottom wall (hold them square against the inner wall with tape/nuts on the outside so their heads cast in cleanly and shanks point `-Z`).
3. Screw waxed/greased dummy screws (or the real screws with waxed tips) into the `12 × M8` front-wall holes, `8 × M10` rear-wall holes, and `8 × M6` top-wall holes so EG cannot enter the threads and screw tips have clearance pockets.
4. Seal and screw the **`X-` end cap (`120 × 120 × 5`, `G12`)** onto the `-X` end (`4 × M5 × 16` + `F18` silicone).
5. Stand the beam upright on its capped `-X` end (strapped safely to a post/bench) and tamp EG straight down the open `+X` `104 × 104` bore in ~100 mm lifts with a long timber rammer up to 2 mm shy of the `+X` face. No small side ports are needed because filling through the open `104 × 104` end gives full access before the `+X` cap goes on.
6. Seal and screw the **`X+` end cap (`120 × 120 × 5`, `G12`)** onto the `+X` end (`4 × M5 × 16` + silicone). After cure, back out the waxed dummy screws.
