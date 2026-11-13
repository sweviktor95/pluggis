# -*- coding: utf-8 -*-
"""Faropiktogram (GHS01-GHS09) i detaljerad stil som liknar de riktiga. Körs via exec från mkkfig1.py."""
K_ = "#111"
def diamond(cx, cy, r=104):
    return f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" fill="#fff" stroke="#d6002b" stroke-width="13" stroke-linejoin="miter"/>'
def star(cx, cy, r1, r2, n=8, rot=0, col=K_):
    pts = []
    for k in range(n * 2):
        r = r1 if k % 2 == 0 else r2
        a = math.radians(rot + k * 180 / n)
        pts.append(f"{cx+r*math.sin(a):.1f},{cy-r*math.cos(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'
FL = "M2,-58 C6,-42 22,-32 30,-16 C41,6 35,34 11,45 C-6,52 -27,45 -35,27 C-43,9 -35,-8 -25,-21 C-22,-11 -16,-6 -10,-5 C-15,-24 -9,-44 2,-58Z"
FL_IN = "M3,40 C-11,42 -23,31 -19,17 C-16,7 -7,1 -4,-13 C4,-3 19,7 19,23 C19,33 13,38 3,40Z"
def flame(s=1.0, x=0, y=0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="{FL}" fill="{K_}"/><path d="{FL_IN}" fill="#fff"/>'
            f'<path d="M-2,40 C-12,40 -15,33 -14,27 C-13,19 -6,17 -3,6 C0,16 9,21 9,29 C9,36 5,40 -2,40Z" fill="{K_}"/></g>')
def ic_bomb():
    b = f'<circle cx="-16" cy="18" r="34" fill="{K_}"/><path d="M-40,8 q8,-18 24,-20" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".85"/>'
    b += f'<rect x="2" y="-22" width="18" height="14" rx="3" fill="{K_}" transform="rotate(40 10 -15)"/>'
    b += f'<path d="M16,-22 C22,-28 24,-30 26,-36" stroke="{K_}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    b += star(34, -40, 32, 11, 10, 8)
    for (x, y, r) in [(60, -14, 6), (56, -66, 5.5), (8, -64, 5.5)]:
        b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{K_}"/>'
    b += f'<path d="M58,-6 l12,-8 l-2,14z M-6,-50 l-12,-2 l8,12z M66,-34 l10,2 l-8,8z" fill="{K_}"/>'
    return b
def ic_flame(): return flame(1.0, 0, 4)
def ic_ox():
    return (f'<circle cx="0" cy="30" r="23" fill="none" stroke="{K_}" stroke-width="13"/>'
            + flame(.78, 0, -24))
def ic_gas():
    b = f'<path d="M-22,-4 Q-22,-30 -9,-36 L9,-36 Q22,-30 22,-4 L22,46 Q22,54 14,54 L-14,54 Q-22,54 -22,46Z" fill="{K_}"/>'
    b += f'<rect x="-7" y="-46" width="14" height="14" fill="{K_}"/><rect x="-15" y="-54" width="30" height="9" rx="4" fill="{K_}"/>'
    b += f'<path d="M-12,-10 L-12,40" stroke="#fff" stroke-width="3.5" stroke-linecap="round" opacity=".9"/><rect x="-22" y="4" width="44" height="5" fill="#fff"/>'
    return b
def tube(x, y, rot):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale(1.2)"><path d="M-9,-26 v40 a9,9 0 0 0 18,0 v-40z" fill="{K_}"/>'
            f'<rect x="-12" y="-30" width="24" height="7" rx="3" fill="{K_}"/><path d="M-4,-4 v18 a4,4 0 0 0 8,0 v-18z" fill="#fff"/></g>')
def drop(x, y, s=1):
    return f'<path d="M{x},{y-9*s} C{x+7*s},{y} {x+7*s},{y+8*s} {x},{y+8*s} C{x-7*s},{y+8*s} {x-7*s},{y} {x},{y-9*s}Z" fill="{K_}"/>'
def hand(x, y):
    g = f'<g transform="translate({x},{y})">'
    g += f'<rect x="-21" y="2" width="42" height="42" rx="12" fill="{K_}"/>'
    for (fx, fh) in [(-21, 30), (-10, 38), (1, 38), (12, 32)]:
        g += f'<rect x="{fx}" y="{4-fh}" width="9.5" height="{fh}" rx="4.7" fill="{K_}"/>'
    g += f'<g transform="rotate(-38 -22 22)"><rect x="-38" y="12" width="11" height="30" rx="5.5" fill="{K_}"/></g>'
    return g + '</g>'
def ic_corr():
    b = tube(-34, -40, 130) + tube(-4, -50, 130)
    b += drop(-20, -4, 1.3) + drop(-16, 20, 1.1) + drop(16, -6, 1.3) + drop(18, 14, 1.1)
    b += f'<path d="M-64,26 L-44,26 q3,9 10,3 q5,-8 12,-1 q4,6 10,0 L0,30 L0,44 L-64,44Z" fill="{K_}"/>'
    b += hand(30, 8)
    return b
def ic_skull():
    b = ''
    for (x1, y1, x2, y2) in [(-40, 14, 40, 48), (40, 14, -40, 48)]:
        b += f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{K_}" stroke-width="12" stroke-linecap="round"/>'
        for (x, y) in [(x1, y1), (x2, y2)]:
            b += f'<circle cx="{x-4}" cy="{y-3}" r="7" fill="{K_}"/><circle cx="{x+4}" cy="{y+4}" r="7" fill="{K_}"/>'
    b += (f'<path d="M-33,-14 C-33,-48 33,-48 33,-14 C33,-6 29,0 22,4 L22,12 L18,12 L18,27 Q18,31 14,31 L-14,31 Q-18,31 -18,27 L-18,12 L-22,12 L-22,4 C-29,0 -33,-6 -33,-14Z" fill="{K_}" stroke="#fff" stroke-width="5" stroke-linejoin="round"/>'
          f'<ellipse cx="-13" cy="-12" rx="10" ry="11" fill="#fff" transform="rotate(12 -13 -12)"/><ellipse cx="13" cy="-12" rx="10" ry="11" fill="#fff" transform="rotate(-12 13 -12)"/>'
          f'<path d="M0,-1 C-4,4 -7,10 -5,12 L5,12 C7,10 4,4 0,-1Z" fill="#fff"/>'
          f'<path d="M-12,18 v13 M-4,18 v13 M4,18 v13 M12,18 v13" stroke="#fff" stroke-width="3.2"/>')
    return b
def ic_excl():
    return f'<path d="M-16,-54 h32 l-6,66 h-20z" fill="{K_}"/><circle cx="0" cy="38" r="15" fill="{K_}"/>'
def ic_health():
    b = f'<circle cx="0" cy="-38" r="17" fill="{K_}"/>'
    b += f'<path d="M-42,48 L-42,6 Q-42,-14 -22,-18 L22,-18 Q42,-14 42,6 L42,48Z" fill="{K_}"/>'
    b += star(0, 14, 28, 11, 8, 22.5, "#fff")
    return b
def ic_env():
    b = f'<path d="M-36,46 V-14" stroke="{K_}" stroke-width="11" stroke-linecap="round"/>'
    b += f'<path d="M-36,-2 L-54,-24 M-36,-16 L-24,-42 M-36,14 L-56,4 M-36,0 L-18,-10 M-54,-24 l-8,-2 M-54,-24 l2,-10 M-24,-42 l6,-8 M-24,-42 l-10,-2" stroke="{K_}" stroke-width="7" stroke-linecap="round" fill="none"/>'
    b += f'<path d="M-14,10 C-2,-8 30,-8 44,10 C30,28 -2,28 -14,10Z" fill="{K_}"/>'
    b += f'<path d="M42,10 L62,-8 C58,4 58,16 62,28Z" fill="{K_}"/>'
    b += f'<path d="M8,-4 C14,-14 24,-14 30,-4Z" fill="{K_}"/><path d="M12,24 C16,32 24,32 28,24Z" fill="{K_}"/>'
    b += f'<circle cx="-2" cy="7" r="4.2" fill="#fff"/><path d="M8,-1 q-6,11 0,22" stroke="#fff" stroke-width="3.2" fill="none"/>'
    b += f'<path d="M-62,50 q6,-9 12,0 t12,0 t12,0 t12,0 t12,0 t12,0" stroke="{K_}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    return b
ICS = [
 (ic_bomb, "GHS01", "Explosivt", "Kan explodera, till exempel fyrverkerier.", "Fara eller varning"),
 (ic_flame, "GHS02", "Brandfarligt", "Kan fatta eld lätt, till exempel sprit.", "Fara eller varning"),
 (ic_ox, "GHS03", "Oxiderande", "Kan få andra ämnen att brinna mycket lättare.", "Fara eller varning"),
 (ic_gas, "GHS04", "Gas under tryck", "Gasflaska. Kan explodera om den blir varm.", "Varning"),
 (ic_corr, "GHS05", "Frätande", "Kan skada hud och ögon och fräta på metall.", "Fara eller varning"),
 (ic_skull, "GHS06", "Giftigt", "Kan ge allvarlig skada eller död, även i små mängder.", "Fara"),
 (ic_excl, "GHS07", "Skadligt, irriterande", "Mindre allvarlig fara, till exempel hudirritation.", "Varning"),
 (ic_health, "GHS08", "Allvarlig hälsofara", "Kan ge sjukdom på lång sikt, till exempel cancer.", "Fara eller varning"),
 (ic_env, "GHS09", "Miljöfarligt", "Skadligt för djur och växter i vatten.", "Inget signalord"),
]
SC = {ic_bomb: .92, ic_corr: .86, ic_skull: .9, ic_env: .9, ic_health: .98, ic_ox: 1.08, ic_gas: 1.1}
SH = {ic_bomb: (-8, 10), ic_corr: (-8, 0), ic_env: (-2, 0)}
W, H = 1500, 790
b = ''
for i, (fn, kod, n, d, sig) in enumerate(ICS):
    col, row = i % 3, i // 3
    x0 = 20 + col * 490; y0 = 20 + row * 256
    b += card(x0, y0, 470, 236, "#fff")
    cx, cy = x0 + 120, y0 + 118
    b += diamond(cx, cy, 104) + f'<g transform="translate({cx+SH.get(fn,(0,0))[0]},{cy+SH.get(fn,(0,0))[1]}) scale({SC.get(fn,1.14)})">{fn()}</g>'
    b += T(x0 + 240, y0 + 62, kod, 20, "#d6002b", "700", "start")
    b += T(x0 + 240, y0 + 96, n, 29 if len(n) < 19 else 25, INK, "700", "start")
    words = d.split(' '); lines = []; cur = ''
    for w in words:
        if len(cur + ' ' + w) > 22:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    lines.append(cur)
    for k, ln in enumerate(lines[:3]): b += T(x0 + 240, y0 + 128 + k * 26, ln, 22, MUT, "400", "start")
    b += T(x0 + 240, y0 + 218, "Signalord: " + sig.lower(), 19, INK, "700", "start")
render('v_piktogram', svg(W, H, b, BG), W, H, 2)
