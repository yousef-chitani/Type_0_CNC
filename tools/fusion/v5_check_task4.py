# Read-only check of Type_0_v5 for V5 plan Task 4 (run through fusion_mcp_execute, readOnly).
# 1. timeline warnings / errors; 2. solid overlaps between visible bodies (fasteners, drill
# guides and printed chain/sensor parts left out: screws sit in holes); 3. Y travel, Y1 and Y2.
# from the riser faces, and the block grease fittings against the BF12 riser at Y max.
import adsk.core, adsk.fusion

SKIP = ('M5', 'M6', 'M4', 'M8x', 'Drill Guide', 'Chain', 'Zip Tie', 'Threaded Rod', 'Grease',
        'Sensor', 'Trigger', 'Endcap', 'Cutting Area', 'Wasteboard')


def bodies(root):
    out = []
    for o in root.allOccurrences:
        if not o.isVisible:
            continue
        n = o.component.name
        if any(s in n for s in SKIP) or any(s in o.fullPathName for s in ('Fasteners', 'Drill Guides')):
            continue
        for b in o.bRepBodies:
            if b.isVisible and b.isSolid:
                out.append((o.fullPathName, b))
    return out


def run(_context: str):
    app = adsk.core.Application.get()
    assert app.activeDocument.name == 'Type_0_v5'
    design = adsk.fusion.Design.cast(app.activeProduct)
    H = adsk.fusion.FeatureHealthStates
    tl = design.timeline
    bad = [(i, tl.item(i).name) for i in range(tl.count)
           if tl.item(i).healthState in (H.WarningFeatureHealthState, H.ErrorFeatureHealthState)]
    print('timeline', tl.count, 'warnings+errors', len(bad), bad)

    bs = [] if globals().get('TRAVEL_ONLY') else bodies(design.rootComponent)
    tm = adsk.fusion.TemporaryBRepManager.get()
    hits = []
    for i in range(len(bs)):
        a = bs[i][1].boundingBox
        for j in range(i + 1, len(bs)):
            b = bs[j][1].boundingBox
            if (a.minPoint.x < b.maxPoint.x - 0.001 and b.minPoint.x < a.maxPoint.x - 0.001 and
                    a.minPoint.y < b.maxPoint.y - 0.001 and b.minPoint.y < a.maxPoint.y - 0.001 and
                    a.minPoint.z < b.maxPoint.z - 0.001 and b.minPoint.z < a.maxPoint.z - 0.001):
                t = tm.copy(bs[i][1])
                try:
                    tm.booleanOperation(t, tm.copy(bs[j][1]), adsk.fusion.BooleanTypes.IntersectionBooleanType)
                except RuntimeError as e:  # bad vendor geometry: report the pair, do not hide it
                    hits.append((-1, bs[i][0], bs[j][0] + ' (boolean failed: %s)' % str(e)[:40]))
                    continue
                v = t.volume * 1000  # mm3
                if v > 1:
                    hits.append((round(v), bs[i][0], bs[j][0]))
    print('bodies checked', len(bs), 'overlaps > 1 mm3:', len(hits))
    for h in sorted(hits, reverse=True):
        print('  OVERLAP %d mm3 | %s | %s' % h)  # -1 = boolean failed

    # Y travel per side (bounding boxes of bodies). Moving: the HGH20CA blocks, the roller, the DFU1605
    # and the nut and fill plates of that side. Fixed: that side's risers, HM12-60 and BF12. For
    # each moving/fixed body pair that overlaps in X and Z, the free gap along Y; travel = the
    # smallest gap forward + the smallest gap back.
    def boxes(pred_occ):
        out = []
        for o in design.rootComponent.allOccurrences:
            if o.isVisible and pred_occ(o):
                for b in o.bRepBodies:
                    if b.isVisible and b.isSolid:
                        bb = b.boundingBox
                        out.append((o.component.name, [v * 10 for v in (bb.minPoint.x, bb.minPoint.y, bb.minPoint.z,
                                                                        bb.maxPoint.x, bb.maxPoint.y, bb.maxPoint.z)]))
        return out

    for side, sx in (('Y1', -1), ('Y2', 1)):
        on = lambda bb: bb[0] * sx > 300 or bb[3] * sx > 300
        mov = [m for m in boxes(lambda o: o.component.name in ('HGH20CA Block', 'YRoller', 'YRoller(Mirror)')
                                or 'DFU1605' in o.component.name or 'Plate Rods' in o.component.name
                                or ('Nut Plate' in o.component.name or 'Fill Plate' in o.component.name)
                                and 'XAxis' not in o.fullPathName) if on(m[1])]
        fix = [f for f in boxes(lambda o: o.fullPathName.startswith(side + ' screw and motor') and (
            'Riser' in o.component.name or '+HM12-60:' in o.fullPathName or '+BF12:' in o.fullPathName)) if on(f[1])]
        # A fixed body in front of the moving one (by centre) limits forward, behind it limits back.
        # Gaps may be negative (already overlapping at the model's position): travel is still the sum.
        fwd, back = (1e9, None), (1e9, None)
        for mn, m in mov:
            for fn, f in fix:
                if m[0] < f[3] and f[0] < m[3] and m[2] < f[5] and f[2] < m[5]:
                    if f[1] + f[4] < m[1] + m[4]:
                        if m[1] - f[4] < fwd[0]:
                            fwd = (m[1] - f[4], mn + ' / ' + fn)
                    elif f[1] - m[4] < back[0]:
                        back = (f[1] - m[4], mn + ' / ' + fn)
        print('%s: forward %.1f (%s), back %.1f (%s), Y travel %.1f'
              % (side, fwd[0], fwd[1], back[0], back[1], fwd[0] + back[0]))

    # Plate rods and nuts against every visible body, fasteners included (the HGH20CA block screws
    # inside the roller are PrintNC fasteners, which the overlap pass above skips).
    rods = [(o.fullPathName, b) for o in design.rootComponent.allOccurrences
            if o.isVisible and 'Plate Rods' in o.component.name for b in o.bRepBodies if b.isVisible]
    others = [(o.fullPathName, b) for o in design.rootComponent.allOccurrences
              if o.isVisible and 'Plate Rods' not in o.component.name for b in o.bRepBodies
              if b.isVisible and b.isSolid]
    for rp, rb in rods:
        a = rb.boundingBox
        for op, ob in others:
            b = ob.boundingBox
            if (a.minPoint.x < b.maxPoint.x and b.minPoint.x < a.maxPoint.x and a.minPoint.y < b.maxPoint.y
                    and b.minPoint.y < a.maxPoint.y and a.minPoint.z < b.maxPoint.z and b.minPoint.z < a.maxPoint.z):
                t = tm.copy(rb)
                try:
                    tm.booleanOperation(t, tm.copy(ob), adsk.fusion.BooleanTypes.IntersectionBooleanType)
                except RuntimeError:
                    print('  ROD boolean failed | %s | %s | %s' % (rb.name, op, ob.name))
                    continue
                if t.volume * 1000 > 0.01:
                    print('  ROD HIT %.2f mm3 | %s %s | %s %s' % (t.volume * 1000, rp.split('+')[0], rb.name, op, ob.name))
