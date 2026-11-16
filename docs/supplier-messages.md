# Supplier messages (drafts, rewritten 15 Nov 2026)

Copy only the quoted text. The "For you" lines are notes for the owner, not for the supplier. Quantities are from `bom.csv`. Record the answers here and in `open-questions.md`.

## 1. Ballscrew seller (AliExpress chat)

Before wave 2 (15 Feb 2027, D-103); also needed for the CAD assembly. Listing: https://www.aliexpress.com/item/1005010046279521.html

> Hi, I'd like 3 of the DFU1605 C7 kits (BK12/BF12 + nut housing) in 850, 600 and 350 mm.
>
> Is the length the total length of the screw, including the machined ends, or just the thread? And could you send me a drawing of the end machining?
>
> Is the nut preloaded? Can you ship all 3 together, and what's the shipping?
>
> Thanks

For you: overall length must be at least X 823 / Y 582 / Z about 350 mm, with a standard BK12 end (Ø10 stub at least 35 mm long for the X pulley and outboard bearing). If the length is thread only, the screws are longer than planned: check they still fit the castings (Y channel, X beam) before ordering.

## 2. GCL (email): open question 4

Before wave 3 (1 Mar 2027).

> Hi,
>
> Could you give me a delivered price for 3 × 25 kg bags of the kiln-dried Winter Quartz 2–5 mm to Swansea, SA2? And what would it be if I added 2 × 25 kg of the 1–3 mm?
>
> How long does delivery usually take, and does someone need to be in? I'm looking to order in early March.
>
> Thanks,
> [name]

For you: it must be dry (it goes in epoxy). If the reply doesn't say kiln-dried, ask.

## 3. Hancock & Brown, Swansea (phone 01792 462346): open question 4

Before wave 3 (1 Mar 2027). Call notes:

- "Hi, do you sell kiln-dried sand in 20 kg bags, the fine 0–1 mm stuff? I'd want 3 bags, collecting early March."
- Price per bag?
- Will you have it in March?
- Opening hours?

## 4. Z motor mount seller (AliExpress chat)

Before wave 2 (15 Feb 2027, D-126). Listing: https://www.aliexpress.com/item/1005006232398099.html (HM12-60)

> Hi, could you send me the drawing for the HM12-60?
>
> My motor has 4 holes on a 50 mm square and a 36 mm pilot. Will it fit?
>
> Thanks

For you: needs 4 holes on a 50 ± 0.2 mm square, pilot bore Ø36 or larger, room for a D26 × L35 coupling. If it's 47.14 mm holes or a Ø38.1 pilot only, don't buy it: the session designs a mount from the 10 mm plate.

## 5. EC Fibreglass Supplies (email or contact form): open question 1

Before wave 3 (1 Mar 2027). Product: https://www.ecfibreglasssupplies.co.uk/ampreg-30-low-viscosity-epoxy-resin-slow (bom.csv F01)

> Hi,
>
> I'd like to order a 22.68 kg kit of Ampreg 30 with the 3X Slow hardener, delivered to Swansea, SA2. What would delivery cost and how long does it take?
>
> Also, roughly how much shelf life is left on it when it ships? I'd be ordering in early March and using it up by the end of May.
>
> Thanks,
> [name]

For you: the delivery cost is the last unpriced part of F01. Shelf life must cover March to May 2027.

## 6. LiMo Bearing (info@limobearing.com or "Request a Quote" on limobearing.com): price check 16

> Hi,
>
> Could you quote the following, DDP to Swansea, UK (SA2), by sea and by air?
>
> - DFU1605 ballscrew with nut housing and BK12/BF12 supports, C7, standard end machining: one each at 850, 600 and 350 mm. On the 850 mm one I need an extra Ø10 mm stub, about 35 mm long, on the BK12 end (I can send a drawing). Can you do them with light preload?
> - HGH20CA linear guide sets (2 rails, 4 blocks), ZA preload: one each at 800, 500 and 350 mm. What accuracy class are the rails?
> - 1 × HM12-60 motor mount. My motor (NEMA 24) has 4 holes on a 50 mm square and a 36 mm pilot, but your page shows 49.5 mm. Will it fit, or can you drill it for 50 mm?
> - 1 × D25L35 coupling, 10 mm to 10 mm. Will it fit inside the HM12-60?
>
> Please include the shipping weight, and let me know if the DDP price includes VAT.
>
> Thanks,
> [name]

**Sent 15 Nov 2026.** Answer 16 Nov 2026 (Amy Jiang, LiMo):

> LiMo provides custom machining for ball screws. Can you please provide the drawings? Light preload performs much better on C5-ground ball screws. Please get prices from the LiMo online store. The shipping costs and delivery dates are on the checkout page.

What it answers: custom end machining yes (they want drawings); light preload yes, but they advise **C5 ground**; prices come from the store, shipping and dates from the checkout page (no quote by email).
Not answered: rail accuracy class; HM12-60 drilled for 50 mm; coupling fit inside the HM12-60; extra cost of the X stub; shipping weight; whether DDP includes VAT.

Owner (16 Nov): screw lengths stay **X 850 / Y 600**, Z standard ends; **no drawings until LiMo answers the rest**; C5 or C7 decided after the C5 price is known.

### 6a. Reply to LiMo (draft, owner sends)

> Hi Amy,
>
> Thanks. I'll send the ballscrew drawings with the order. Before that, could you answer these?
>
> 1. What accuracy class are the HGH20CA rails (C, H or P)?
> 2. The HM12-60 shows 49.5 mm holes. My motor has 50 mm. Can you drill it for a 50 mm square, and what is the extra cost?
> 3. Does the D25L35 coupling fit inside the HM12-60?
> 4. Is there an extra cost for a longer Ø10 drive end on the screws?
> 5. Does the DDP price at checkout include UK VAT?
>
> Thanks,
> [name]

**Sent 16 Nov 2026** (owner dropped question 4, the stub cost). Answer: (waiting)

For you: open the DFU1605 page and copy the **C5** price for the 900, 600 and 400 mm kits (C7 was $152.19 for the three), so the session can compare. At checkout (don't pay) note the shipping to SA2 for sea and air and the dates. That replaces the shipping-weight question.

For you: the all-in DDP price must beat **£464.41** (price check 16). Need the rail accuracy class and a clear yes on the HM12-60 fitting the 50 mm / Ø36 motor face (or drilled to fit). If it won't fit, task 14 makes the mount from the 10 mm plate.
