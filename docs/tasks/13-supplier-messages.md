# Task 13: Supplier messages

**Start:** branch `claude/charming-cori-349jm7`. Read `docs/tasks/README.md` (rules, 1 page), then only the files listed below. Do not read the whole repo.

**Who:** owner sends; Opus 5.5 can update the drafts
**Depends on:** none

## Read
- docs/supplier-messages.md

## Do
1. Owner sends: ballscrew seller (section 1), GCL (2), Hancock & Brown (3), Z motor mount seller (4).
2. Add a draft to EC Fibreglass Supplies: delivery cost to SA2 for one 22.68 kg Ampreg 30 kit.
3. Record each answer under its message and in `docs/open-questions.md`.

## Done when
Every message has an answer or a date sent.

## State (15 Nov 2026)
- Step 2 done: EC Fibreglass draft is section 5 of `docs/supplier-messages.md`.
- All 6 drafts rewritten shorter, like a person would write them (15 Nov). Owner notes sit under each one as "For you".
- Message 6 (LiMo) sent 15 Nov 2026; answered 16 Nov (custom machining needs drawings, C5 advised, prices from the store). Reply 6a sent 16 Nov (without the stub-cost question); waiting. C5 set price recorded 17 Nov (`price-check-task-16.md`: $424.71 for 3 sets with C5 BK12/BF12); owner still notes the checkout shipping, then decides C5 or C7. No drawings until LiMo answers (owner).
- Steps 1 and 3 wait for the owner: 5 messages to send (1 and 4 are AliExpress chats, easy to send during the AliExpress check). Write the date sent under each message.
- For the drawing session later (from `cad/v2/assembly.py`, 16 Nov): the drive stubs beyond the BK12 lock nut are **X Ø10 × 76.2** (pulley 26.2 + KFL000 + gaps) and **Y Ø10 × 34**, against about 15 standard. The "about 35 mm" in message 6 was too short. Lengths stay X 850 / Y 600 (owner); the CAD needs 823 / 582 overall, and the X channel ends at the BF12 end, so the extra 27 mm on X goes on the drive side (stub about 103, or a longer thread: check). Z: standard BK12/BF12 ends. Still to ask the owner: plain stub, a flat for the pulley set screw, or a keyway.
- End machining agreed in principle (16 Nov): LiMo's standard drawing (BK12: Ø10 × 15 drive, M12×1 × 14, Ø12 × 25; BF12: Ø10 × 11 with circlip groove), changing only the X and Y drive stubs: longer (X about 74, Y about 32 from the end of the thread, as the CAD stands), Ø10 0/−0.015, one flat 1 mm deep along the stub for the pulley and KFL000 grub screws. Z fully standard. **The owner is redoing the CAD (task 09), so take the stub lengths and overall lengths from the new CAD**, not from these numbers. Exact lengths (no spare stub) are cleaner than 850 / 600; the owner keeps 850 / 600 for now.
