# Place the Y1 vendor parts in Type_0_v5 (V5 plan Task 4, item 2). Run through fusion_mcp_execute
# (not read-only) AFTER the vendor STEPs were imported into component 'Y1 screw and motor'
# (26 Nov 2026: DFU1605 Nut, BF12, HM12-60, 24HS40 Motor, HGH20CA Block, identity transforms).
# Re-running resets the transforms, skips cuts / copies that already exist, and rebuilds the parts
# built at AX_Z (DFU place, screw, coupling, risers) when SEAT has changed. Then run v5_y2_place.py.
# Datums (PrintNC model mm): Y1 screw axis X -377.5, **Z 210 = roller centre** (owner 26 Nov:
# was PrintNC's 215; the DFU body Ø28 needs the 34 bore of the 80 x 40 roller centred).
# SEAT = epoxy rail-seat height (D-363, 3 mm). PrintNC's rails (and so the rollers and the gantry)
# are lifted by the same 3 through user parameter YRailSeat, the offset of joints Rigid 2 / Rigid 202.
import re
import adsk.core, adsk.fusion

SEAT = 3.0
AX_X, AX_Z = -377.5, 210.0 + SEAT
RAIL_BOT = 160.0 + SEAT          # Y frame tube top
BLOCK_YC = (589.0, 674.0)        # PrintNC HGW20CC block centres (same pattern, HGH20CA 77.5 long)
# Carriage, Y (D-370): the nut and fill plates are end caps on the 80 x 40 roller (Y 556.5 to 706.5),
# 40 x 15 aluminium flat bar cut 80, so the DFU flange sits on the nut plate front, 7.5 further
# forward than PrintNC's SFU flange (539).
ROLLER_Y = (556.5, 706.5)
PLATE_T = 15.0
NUT_FACE_Y = ROLLER_Y[0] - PLATE_T - 10.0  # DFU flange front face (flange 10 thick) = 531.5
BF_YC = 733.15                   # BF12 centre: bearing seat from the LiMo end drawing (was PrintNC's 738.25)
# Y 1605 screw, LiMo drawing cad/vendor/drawings/limo_1605_bk12_bf12_ends.png, L 750 (v5_sizes):
# BK end Ø10 x 15, M12x1 x 14, Ø12 x 25 (39 to the thread); BF end Ø10 x 11, groove Ø9.6 x 1.15
# at 9.15 from the shoulder. The Ø12 shoulder sits on the HM12 bearing face (Y 43). (Y from, to, Ø)
SCREW = [(-11.0, 4.0, 10.0), (4.0, 18.0, 12.0), (18.0, 43.0, 12.0), (43.0, 728.0, 16.0),
         (728.0, 737.15, 10.0), (737.15, 738.30, 9.6), (738.30, 739.0, 10.0)]
HM_SCREW_FACE_Y = 43.0           # PrintNC HM12-57 screw-end face
NUT_PLATE = 'Y1 Nut Plate (flat bar 40 x 15, cut 80)'
FILL_PLATE = 'Y1 Fill Plate (flat bar 40 x 15, cut 80)'
# The 6 threaded rods and 12 nuts that clamp the plates (D-370, as PrintNC: nut 4 thick, rod 1 proud).
# Name kept clear of the check's SKIP list ('M5', 'Threaded Rod'), so the check sees them.
RODS = 'Y1 Plate Rods and Nuts (6 x d5, nuts 8 AF x 4)'
NUT_T, NUT_AF, ROD_PROUD = 4.0, 8.0, 1.0


def mat(cols, t_mm):
    m = adsk.core.Matrix3D.create()
    m.setWithCoordinateSystem(adsk.core.Point3D.create(*[v / 10 for v in t_mm]),
                              *[adsk.core.Vector3D.create(*c) for c in cols])
    return m


def run(_context: str):
    app = adsk.core.Application.get()
    assert app.activeDocument.name == 'Type_0_v5'
    d = adsk.fusion.Design.cast(app.activeProduct)
    root = d.rootComponent
    top = [o for o in root.occurrences if o.component.name == 'Y1 screw and motor'][0]
    # Keyed by base name: a rebuilt part gets ' (1)' etc. (Fusion keeps the old component's name taken).
    kid = {re.sub(r' \(\d+\)$', '', o.component.name): o for o in top.childOccurrences}

    def drop(o):  # every occurrence (Y1 and the Y2 twin), so the component goes and its name is free
        for x in list(root.allOccurrencesByComponent(o.component)):
            x.deleteMe()

    # Parts built once at AX_Z: drop them when SEAT has changed (their centre is off the axis), so
    # they are rebuilt below (drop also removes the Y2 twins; v5_y2_place.py adds new ones). Done
    # first: once 'DFU place' is redone, boxes read 0 in the same call.
    for n in ('Y 1605 Screw', 'D25L35 Coupling', NUT_PLATE, FILL_PLATE, RODS):
        if n in kid:
            bb = kid[n].boundingBox
            if abs((bb.minPoint.z + bb.maxPoint.z) * 5 - AX_Z) > 0.01:
                drop(kid.pop(n))

    # DFU1605: local X = screw axis, flange face at x -15, nut to x -115. Local y -> Z so the
    # 40 flats (local |y| > 20, clear of the 6 x Ø5.5 holes) are top and bottom.
    # The occurrence transform does NOT hold for this part: set + snapshot reads back at the
    # origin (tried 26 Nov 2026 with transform/transform2, timeline rolled before the cut; the
    # component holds its own Base Feature). So the occurrence stays at identity and a Move
    # feature 'DFU place' (after the flats cut) moves its bodies. Not re-run if it exists.
    dfu = kid['DFU1605 Nut']
    c = dfu.component
    for b in c.bRepBodies:
        if b.name == 'Body3':
            b.isLightBulbOn = False  # 130 screw piece from the vendor file
    if not any(f.name == 'DFU flats 40' for f in c.features.extrudeFeatures):
        sk = c.sketches.add(c.xYConstructionPlane)
        L = sk.sketchCurves.sketchLines
        for y0, y1 in ((2.0, 3.0), (-3.0, -2.0)):
            L.addTwoPointRectangle(adsk.core.Point3D.create(-6.1, y0, 0), adsk.core.Point3D.create(-1.4, y1, 0))
        prof = adsk.core.ObjectCollection.create()
        for p in sk.profiles:
            prof.add(p)
        ei = c.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
        ei.setSymmetricExtent(adsk.core.ValueInput.createByString('30 mm'), True)
        flange = [b for b in c.bRepBodies if b.name == 'Body6']
        ei.participantBodies = flange
        f = c.features.extrudeFeatures.add(ei)
        f.name = 'DFU flats 40'
    for f in list(c.features.moveFeatures):  # SEAT changed: move again from the vendor frame
        bb = dfu.boundingBox
        if f.name == 'DFU place' and (abs((bb.minPoint.z + bb.maxPoint.z) * 5 - AX_Z) > 0.01
                                      or abs(bb.minPoint.y * 10 - NUT_FACE_Y) > 0.01):
            f.deleteMe()
    if not any(f.name == 'DFU place' for f in c.features.moveFeatures):
        col = adsk.core.ObjectCollection.create()
        for b in c.bRepBodies:
            col.add(b)
        mi = c.features.moveFeatures.createInput2(col)
        mi.defineAsFreeMove(mat([(0, -1, 0), (0, 0, 1), (-1, 0, 0)], (AX_X, NUT_FACE_Y - 15, AX_Z)))
        c.features.moveFeatures.add(mi).name = 'DFU place'

    # BF12: bore axis local Z at local y 3.5, base at local y -21.5 (centre height 25). Turned
    # round (local z -> +Y) so the vendor model's circlip is outboard, in the screw's groove.
    kid['BF12'].transform2 = mat([(-1, 0, 0), (0, 0, 1), (0, 1, 0)], (AX_X, BF_YC, AX_Z - 3.5))

    # HGH20CA: rail stub along local Z, up = local Y, rail bottom at local y -17.5. Blocks go in
    # 'Y rails and seats' (plan Task 4 component); PrintNC's HGR20 rail is kept.
    rs = [o for o in root.occurrences if o.component.name == 'Y rails and seats']
    rs = rs[0] if rs else root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    rs.component.name = 'Y rails and seats'
    if 'HGH20CA Block' in kid:
        kid['HGH20CA Block'].moveToComponent(rs)
    # Y1 blocks are the first two by name (:1, :2); v5_y2_place.py adds :3 and :4 for Y2.
    by_name = lambda: sorted([o for o in rs.childOccurrences if o.component.name == 'HGH20CA Block'], key=lambda o: o.name)
    blocks = by_name()
    while len(blocks) < 2:
        rs.component.occurrences.addExistingComponent(blocks[0].component, adsk.core.Matrix3D.create())
        blocks = by_name()
    blocks = blocks[:2]
    for b in blocks[0].component.bRepBodies:
        if b.name == 'Body2':
            b.isLightBulbOn = False  # 150 rail stub from the vendor file
    for o, yc in zip(blocks, BLOCK_YC):
        o.transform2 = mat([(1, 0, 0), (0, 0, 1), (0, -1, 0)], (AX_X, yc, RAIL_BOT + 17.5))

    # HM12-60: axis local Z, screw end (bearings, local z 0 to 25, lock nut 25 to 33) at local
    # z 0, motor end (Ø50 pilot recess, 4 x M5 on 49.4 square) at local z 90, base local y -30.
    # Screw-end face at PrintNC's HM12-57 screw-end face, Y 43; motor face Y -47; base Z 180.
    kid['HM12-60'].transform2 = mat([(1, 0, 0), (0, 0, 1), (0, -1, 0)], (AX_X, HM_SCREW_FACE_Y, AX_Z))
    # 24HS40: flange face local z 0, Ø38.1 pilot, shaft Ø10 to local z +20, holes on 50 square;
    # the cable lead (local -y) points outboard (-X).
    kid['24HS40 Motor'].transform2 = mat([(0, 0, 1), (1, 0, 0), (0, 1, 0)], (AX_X, HM_SCREW_FACE_Y - 90, AX_Z))
    for n in ('HM12-60', '24HS40 Motor'):
        kid[n].isLightBulbOn = True
    # 1605 screw: solid of revolution from SCREW, in its own component (plain Ø16 for the thread).
    if 'Y 1605 Screw' not in kid:
        so = top.component.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        sc = so.component
        sc.name = 'Y 1605 Screw'
        tb = adsk.fusion.TemporaryBRepManager.get()
        P = lambda y: adsk.core.Point3D.create(AX_X / 10, y / 10, AX_Z / 10)
        body = None
        for y0, y1, dia in SCREW:
            cyl = tb.createCylinderOrCone(P(y0), dia / 20, P(y1), dia / 20)
            if body is None:
                body = cyl
            else:
                tb.booleanOperation(body, cyl, adsk.fusion.BooleanTypes.UnionBooleanType)
        bf = sc.features.baseFeatures.add()
        bf.startEdit()
        sc.bRepBodies.add(body, bf)
        bf.finishEdit()
        sc.bRepBodies.item(0).name = 'DFU1605 screw 750 (LiMo BK12/BF12 ends)'
    # D25L35 10 x 10 coupling (D-366), from the MH table (cad/vendor/drawings/mh_jaw_coupling.webp,
    # MH1 Ø25: L 35, hub L1 11.75, M3 clamp). Centred on the gap between the screw journal end
    # (SCREW[0][0]) and the 24HS40 shaft tip (motor flange face + 20). The spider zone (11.5) is a
    # solid Ø25 envelope with the bore: the table gives no jaw sizes.
    tb = adsk.fusion.TemporaryBRepManager.get()
    U = adsk.fusion.BooleanTypes

    def box(x0, x1, y0, y1, z0, z1):
        c = adsk.core.Point3D.create((x0 + x1) / 20, (y0 + y1) / 20, (z0 + z1) / 20)
        return tb.createBox(adsk.core.OrientedBoundingBox3D.create(
            c, adsk.core.Vector3D.create(1, 0, 0), adsk.core.Vector3D.create(0, 1, 0),
            (x1 - x0) / 10, (y1 - y0) / 10, (z1 - z0) / 10))

    def zcyl(x, y, z0, z1, dia):
        return tb.createCylinderOrCone(adsk.core.Point3D.create(x / 10, y / 10, z0 / 10), dia / 20,
                                       adsk.core.Point3D.create(x / 10, y / 10, z1 / 10), dia / 20)

    def new_comp(name, bodies):
        oc = top.component.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        cc = oc.component
        cc.name = name
        bf = cc.features.baseFeatures.add()
        bf.startEdit()
        for bname, b in bodies:
            cc.bRepBodies.add(b, bf).name = bname
        bf.finishEdit()

    if 'D25L35 Coupling' not in kid:
        motor_tip = HM_SCREW_FACE_Y - 90 + 20
        yc = (SCREW[0][0] + motor_tip) / 2
        L, L1, D, BORE = 35.0, 11.75, 25.0, 10.0
        P = lambda y, dz=0.0: adsk.core.Point3D.create(AX_X / 10, y / 10, (AX_Z + dz) / 10)
        parts = []
        for name, y0, y1, clamp in (('Hub, screw side', yc + L / 2 - L1, yc + L / 2, True),
                                    ('Spider zone (envelope)', yc - L / 2 + L1, yc + L / 2 - L1, False),
                                    ('Hub, motor side', yc - L / 2, yc - L / 2 + L1, True)):
            b = tb.createCylinderOrCone(P(y0), D / 20, P(y1), D / 20)
            tb.booleanOperation(b, tb.createCylinderOrCone(P(y0), BORE / 20, P(y1), BORE / 20), U.DifferenceBooleanType)
            if clamp:  # 1 wide slit up from the bore, M3 clamp hole across it (along X, 7 above the axis)
                tb.booleanOperation(b, box(AX_X - 0.5, AX_X + 0.5, y0, y1, AX_Z, AX_Z + D / 2 + 1), U.DifferenceBooleanType)
                ym = (y0 + y1) / 2
                h = tb.createCylinderOrCone(adsk.core.Point3D.create((AX_X - D) / 10, ym / 10, (AX_Z + 7) / 10), 0.17,
                                            adsk.core.Point3D.create((AX_X + D) / 10, ym / 10, (AX_Z + 7) / 10), 0.17)
                tb.booleanOperation(b, h, U.DifferenceBooleanType)
            parts.append((name, b))
        new_comp('D25L35 Coupling', parts)

    # Risers (D-357, owner 26 Nov: tapped steel flat bar, as PrintNC): HM12-60 riser 60 x 20 bar,
    # BF12 riser 60 x 25 bar; tops at the housing bases (AX_Z - 30, AX_Z - 25), so their heights
    # follow SEAT. Footprints: PrintNC's riser end faces Y 62.5 and 714.5 kept, since the risers are
    # now below the DFU flange and these faces stop the HGH20CA blocks (Z 164.6 up) before the block
    # ends leave the rail (Y 64 to 714). HM12 riser runs forward to the HM12-60 front, Y -47.
    # Holes: HM12-60 and BF12 base holes (read from their STEPs: X +-23 from the axis; HM12 at
    # 50, 20 and 7 in front of its screw-end face, BF12 on its centre) tapped M6 (Ø5 drill, through);
    # riser to Y tube: M6 cap screws in Ø11 x 6.5 counterbores, Ø6.6 through, tube wall tapped M6,
    # at PrintNC's riser-screw positions (its M6x30s) so its drill guides 3A and 3B still drill the tube.
    # Riser heights follow SEAT (20 + SEAT, 25 + SEAT: flat bar plus shims, D-357); the name carries
    # the height, and a riser of another height is dropped and rebuilt.
    TUBE_TOP = 160.0
    for name, y0, y1, top_z, taps, cbores in (
            ('Y1 HM12 Riser (60 wide, %g tall)' % (AX_Z - 30 - TUBE_TOP), HM_SCREW_FACE_Y - 90, 62.5, AX_Z - 30,
             [(s * 23, HM_SCREW_FACE_Y - k) for s in (-1, 1) for k in (50, 20, 7)],
             [(s * 15, y) for s in (-1, 1) for y in (-25.0, 55.0)]),
            ('Y1 BF12 Riser (60 wide, %g tall)' % (AX_Z - 25 - TUBE_TOP), 714.5, 750.0, AX_Z - 25,
             [(s * 23, BF_YC) for s in (-1, 1)],
             [(-15, 722.0), (15, 722.0), (0, 739.0)])):
        for n in [k for k in kid if k.startswith(name.split(' (')[0]) and k != name]:
            drop(kid.pop(n))
        if name in kid:
            continue
        b = box(AX_X - 30, AX_X + 30, y0, y1, TUBE_TOP, top_z)
        for dx, y in taps:
            tb.booleanOperation(b, zcyl(AX_X + dx, y, TUBE_TOP - 1, top_z + 1, 5.0), U.DifferenceBooleanType)
        for dx, y in cbores:
            tb.booleanOperation(b, zcyl(AX_X + dx, y, TUBE_TOP - 1, top_z + 1, 6.6), U.DifferenceBooleanType)
            tb.booleanOperation(b, zcyl(AX_X + dx, y, top_z - 6.5, top_z + 1, 11.0), U.DifferenceBooleanType)
        new_comp(name, [(name, b)])

    # Nut and fill plates (D-356, D-370): end caps on the roller, 40 x 15 aluminium flat bar cut 80
    # (the roller's outside, X +-40, Z +-20 about the axis), drilled by the owner. Nut plate: Ø28 bore
    # for the DFU1605 body; 6 x M5 tapped (Ø4.2) on the flange's PCD 38 (holes at 0, +-45, 180,
    # +-135 deg from +X). Fill plate: Ø18 for the screw; the same 6 holes Ø5.5. As PrintNC, 6 M5
    # threaded rods run from the flange through both plates and the roller (hole edges 15.9 from the
    # axis, inside the roller's 34 opening) and clamp the roller between the plates.
    import math
    pcd = [(19 * math.cos(math.radians(a)), 19 * math.sin(math.radians(a))) for a in (0, 45, 135, 180, 225, 315)]

    def ycyl(x, z, y0, y1, dia):
        return tb.createCylinderOrCone(adsk.core.Point3D.create(x / 10, y0 / 10, z / 10), dia / 20,
                                       adsk.core.Point3D.create(x / 10, y1 / 10, z / 10), dia / 20)
    for name, y0, bore, hole in ((NUT_PLATE, ROLLER_Y[0] - PLATE_T, 28.0, 4.2),
                                 (FILL_PLATE, ROLLER_Y[1], 18.0, 5.5)):
        if name in kid:
            continue
        y1 = y0 + PLATE_T
        b = box(AX_X - 40, AX_X + 40, y0, y1, AX_Z - 20, AX_Z + 20)
        tb.booleanOperation(b, ycyl(AX_X, AX_Z, y0 - 1, y1 + 1, bore), U.DifferenceBooleanType)
        for dx, dz in pcd:
            tb.booleanOperation(b, ycyl(AX_X + dx, AX_Z + dz, y0 - 1, y1 + 1, hole), U.DifferenceBooleanType)
        new_comp(name, [(name, b)])

    # Rods and nuts: each rod Ø5 (thread shown plain) from the nut in front of the DFU flange to the
    # nut behind the fill plate, ROD_PROUD past each nut; nuts M5 hex 8 AF x 4, a flat facing +-X.
    # Rod in the nut plate's Ø4.2 tapped hole reads as a small overlap (thread in a tapped hole).
    if RODS not in kid:
        y_front = NUT_FACE_Y - NUT_T          # front nut, on the flange front face
        y_back = ROLLER_Y[1] + PLATE_T + NUT_T  # rear nut, on the fill plate back face

        def hex_nut(x, z, y0, y1):
            n = None
            for a in (0, 60, 120):  # three 8-wide slabs about the rod axis, intersected
                r = math.radians(a)
                bx = tb.createBox(adsk.core.OrientedBoundingBox3D.create(
                    adsk.core.Point3D.create(x / 10, (y0 + y1) / 20, z / 10),
                    adsk.core.Vector3D.create(math.cos(r), 0, math.sin(r)), adsk.core.Vector3D.create(0, 1, 0),
                    NUT_AF / 10, (y1 - y0) / 10, 2.0))
                if n is None:
                    n = bx
                else:
                    tb.booleanOperation(n, bx, U.IntersectionBooleanType)
            tb.booleanOperation(n, ycyl(x, z, y0 - 1, y1 + 1, 5.0), U.DifferenceBooleanType)
            return n
        parts = []
        for i, (dx, dz) in enumerate(pcd, 1):
            x, z = AX_X + dx, AX_Z + dz
            parts.append(('Rod %d (d5, %g long)' % (i, y_back - y_front + 2 * ROD_PROUD),
                          ycyl(x, z, y_front - ROD_PROUD, y_back + ROD_PROUD, 5.0)))
            parts.append(('Rod %d front nut' % i, hex_nut(x, z, y_front, NUT_FACE_Y)))
            parts.append(('Rod %d rear nut' % i, hex_nut(x, z, y_back - NUT_T, y_back)))
        new_comp(RODS, parts)

    # Hide (never delete) the PrintNC Y1 parts these replace.
    for o in root.allOccurrences:
        p = o.fullPathName
        if p.startswith('Hardware:1+YAxis Hardware:1+') and o.name in (
                'Y HGW20CC:1', 'Y SFU1610 Nut:1', 'Y BF12:1', 'M6-1.0 90 Grease Fitting:1',
                'Y HM12-57:1', 'Y NEMA23 Stepper:1', 'Y 1610 Ballscrew:1', 'Y D30L40 8-10mm Coupler:1'):
            o.isLightBulbOn = False
        if p.startswith('Printed-Milled Parts:1+YAxis Printed-Milled Parts:1+Y 1610 BFBKHM12:1+') and o.name in (
                'Y BKHM12 Riser:1', 'Y BF12 Riser:1'):
            o.isLightBulbOn = False
        if p.startswith('Printed-Milled Parts:1+YAxis Printed-Milled Parts:1+Y 1610 BFBKHM12:1+Y 1610 Roller Plates:1+')                 and o.name in ('Y 1610 Nut Plate:1', 'Y 1610 Fill Plate:1'):
            o.isLightBulbOn = False
        if p.startswith('Fasteners:1+YRollerFasteners:1+') and o.name.startswith('M5 Threaded Rod and Nuts'):
            o.isLightBulbOn = False  # PrintNC's SFU flange rods; new rods on the DFU's PCD 38 (BOM)
        # Their screws (riser M6x30, housing M6x50) and the NEMA23's M4x16: Y1 bodies only (X < -300).
        if p.startswith('Fasteners:1+YAxisFasteners:1+') and o.name in ('M6x30:1', 'M6x50:1', 'HM12 M6x50:1', 'M4x16:1'):
            for b in o.bRepBodies:
                if b.boundingBox.maxPoint.x < -30 and (b.boundingBox.maxPoint.y < 8 or b.boundingBox.minPoint.y > 70):
                    b.isLightBulbOn = False
    if d.snapshots.hasPendingSnapshot:
        d.snapshots.add()
    for o in [dfu, kid['BF12'], kid['HM12-60'], kid['24HS40 Motor']] + blocks:  # DFU: bodies moved, so its box is the placed one
        bb = o.boundingBox
        print(o.name, 'X %.1f..%.1f Y %.1f..%.1f Z %.1f..%.1f' % (
            bb.minPoint.x * 10, bb.maxPoint.x * 10, bb.minPoint.y * 10, bb.maxPoint.y * 10,
            bb.minPoint.z * 10, bb.maxPoint.z * 10))
