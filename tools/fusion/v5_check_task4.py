# Read-only check of Type_0_v5 for V5 plan Task 4 (run through fusion_mcp_execute, readOnly).
# 1. timeline warnings / errors; 2. solid overlaps between visible bodies (fasteners, drill
# guides and printed chain/sensor parts left out: screws sit in holes); 3. Y carriage limits
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

    bs = bodies(design.rootComponent)
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

    # Y limits: the carriage (nut plate front to fill plate back) runs between the BKHM12 riser
    # back face and the BF12 riser front face; grease fittings stick out past the fill plate.
    def box(name):
        for o in design.rootComponent.allOccurrences:
            if o.component.name == name and o.isVisible:
                return o.boundingBox
    bk, bf = box('Y BKHM12 Riser'), box('Y BF12 Riser')
    roller = box('YRoller')
    # Carriage = the Y-moving parts that sit at the roller: the roller, the Y nut and the nut and
    # fill plates. Only bodies overlapping the roller in X count (the nut plate component also
    # holds two small bodies at Y -6.5 that are not on the carriage).
    rx0, rx1 = roller.minPoint.x, roller.maxPoint.x
    front, back = roller.minPoint.y * 10, roller.maxPoint.y * 10
    for o in design.rootComponent.allOccurrences:
        n = o.component.name
        if not o.isVisible or 'Y2' in o.fullPathName or o.fullPathName.startswith('Hardware:1+XAxis'):
            continue
        if n in ('Y 1610 Nut Plate', 'Y 1610 Fill Plate') or 'SFU1610 Nut' in n or 'DFU1605' in n:
            for b in o.bRepBodies:
                bb = b.boundingBox
                if b.isVisible and bb.minPoint.x < rx1 and bb.maxPoint.x > rx0:
                    front, back = min(front, bb.minPoint.y * 10), max(back, bb.maxPoint.y * 10)
    fit = None
    for o in design.rootComponent.allOccurrences:
        if 'Grease Fitting' in o.component.name and o.isVisible and 'Y HGW20CC' in o.fullPathName \
                and 'Y2' not in o.fullPathName:
            y = o.boundingBox.maxPoint.y * 10
            fit = y if fit is None else max(fit, y)
    bk_face, bf_face = bk.maxPoint.y * 10, bf.minPoint.y * 10
    print('carriage now Y %.1f to %.1f (%.1f long); BKHM12 face %.1f, BF12 face %.1f'
          % (front, back, back - front, bk_face, bf_face))
    print('Y travel = %.1f (free between risers)' % ((bf_face - bk_face) - (back - front)))
    if fit is not None:
        print('grease fittings max Y %.1f: past the carriage back by %.1f; at Y max they %s the BF12 riser'
              % (fit, fit - back, 'HIT' if fit - back > 0 else 'clear'))
    beam = box('XGantry')
    print('XGantry bbox Y %.1f to %.1f, Z %.1f to %.1f; at Y min it moves %.1f forward'
          % (beam.minPoint.y * 10, beam.maxPoint.y * 10, beam.minPoint.z * 10, beam.maxPoint.z * 10,
             front - bk_face))
