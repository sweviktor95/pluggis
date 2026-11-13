# -*- coding: utf-8 -*-
"""Faropiktogram (GHS01-GHS09) i detaljerad stil som liknar de riktiga. Körs via exec från mkkfig1.py."""
K_ = "#111"
def diamond(cx, cy, r=100):
    return f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" fill="#fff" stroke="#d6002b" stroke-width="15" stroke-linejoin="miter"/>'
def star(cx, cy, r1, r2, n=8, rot=0, col=K_):
    pts = []
    for k in range(n * 2):
        r = r1 if k % 2 == 0 else r2
        a = math.radians(rot + k * 180 / n)
        pts.append(f"{cx+r*math.sin(a):.1f},{cy-r*math.cos(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'
FL = "M0,-52 C8,-40 12,-34 22,-26 C34,-16 38,-4 36,10 C34,30 18,44 0,44 C-18,44 -34,30 -34,12 C-34,-2 -26,-10 -22,-24 C-16,-18 -12,-20 -10,-30 C-6,-34 -2,-42 0,-52Z"
FL_IN = "M0,42 C-12,42 -20,32 -19,22 C-18,10 -6,4 0,-14 C6,2 19,10 19,24 C19,34 12,42 0,42Z"
def flame(s=1.0, x=0, y=0):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="{FL}" fill="{K_}"/><path d="{FL_IN}" fill="#fff"/><path d="M-4,42 C-12,42 -16,36 -15,30 C-14,22 -6,20 -2,10 C0,20 8,24 8,32 C8,38 4,42 -4,42Z" fill="{K_}"/></g>'
def ic_bomb():
    b = f'<circle cx="-16" cy="18" r="34" fill="{K_}"/><path d="M-40,8 q8,-18 24,-20" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".85"/>'
    b += f'<rect x="2" y="-22" width="18" height="14" rx="3" fill="{K_}" transform="rotate(40 10 -15)"/>'
    b += f'<path d="M16,-22 C22,-28 24,-30 26,-36" stroke="{K_}" stroke-width="5" fill="none" stroke-linecap="round"/>'
    b += star(34, -40, 30, 12, 9, 8)
    for (x, y, r) in [(62, -18, 4.5), (60, -64, 4), (10, -64, 4), (68, -44, 3.5)]:
        b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{K_}"/>'
    b += f'<path d="M52,-8 l8,-6 l0,10z M8,-48 l-8,-2 l6,8z" fill="{K_}"/>'
    return b
def ic_flame(): return flame(1.0, 0, 4)
def ic_ox():
    return (f'<circle cx="0" cy="30" r="22" fill="none" stroke="{K_}" stroke-width="10"/>'
            + flame(.72, 0, -22))
def ic_gas():
    b = f'<path d="M-22,-4 Q-22,-30 -9,-36 L9,-36 Q22,-30 22,-4 L22,46 Q22,54 14,54 L-14,54 Q-22,54 -22,46Z" fill="{K_}"/>'
    b += f'<rect x="-7" y="-46" width="14" height="14" fill="{K_}"/><rect x="-15" y="-54" width="30" height="9" rx="4" fill="{K_}"/>'
    b += f'<path d="M-12,-10 L-12,40" stroke="#fff" stroke-width="3.5" stroke-linecap="round" opacity=".9"/><rect x="-22" y="4" width="44" height="5" fill="#fff"/>'
    return b
def tube(x, y, rot):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><path d="M-9,-26 v40 a9,9 0 0 0 18,0 v-40z" fill="{K_}"/>'
            f'<rect x="-12" y="-30" width="24" height="7" rx="3" fill="{K_}"/><path d="M-4,-4 v18 a4,4 0 0 0 8,0 v-18z" fill="#fff"/></g>')
def drop(x, y, s=1):
    return f'<path d="M{x},{y-9*s} C{x+7*s},{y} {x+7*s},{y+8*s} {x},{y+8*s} C{x-7*s},{y+8*s} {x-7*s},{y} {x},{y-9*s}Z" fill="{K_}"/>'
def ic_corr():
    b = tube(-34, -40, 130) + tube(-4, -50, 130)
    b += drop(-18, -4) + drop(-14, 16, .8) + drop(14, -10) + drop(18, 8, .8)
    # metallplatta med frätskada
    b += f'<path d="M-62,24 L-40,24 q4,8 10,2 q6,-8 12,0 q4,6 10,0 L0,28 L0,40 L-62,40Z" fill="{K_}"/>'
    # hand
    b += (f'<path d="M20,44 L20,22 q-4,-10 2,-12 q6,-2 8,6 l0,-18 q1,-8 7,-8 q6,0 7,8 l0,0 l0,-4 q1,-8 7,-8 q6,0 7,8 l0,6 q1,-7 6,-6 q5,1 5,8 l0,32 q0,14 -12,18 L20,50Z" fill="{K_}" transform="translate(-4,6)"/>')
    return b
def ic_skull():
    b = ''
    for (x1, y1, x2, y2) in [(-40, 14, 40, 48), (40, 14, -40, 48)]:
        b += f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{K_}" stroke-width="9" stroke-linecap="round"/>'
        for (x, y, dx, dy) in [(x1, y1, 0, 1), (x2, y2, 0, 1)]:
            b += f'<circle cx="{x-4}" cy="{y-3}" r="6.5" fill="{K_}"/><circle cx="{x+4}" cy="{y+4}" r="6.5" fill="{K_}"/>'
    b += (f'<path d="M-30,-14 C-30,-44 30,-44 30,-14 C30,-4 24,2 18,6 L18,24 Q18,28 14,28 L-14,28 Q-18,28 -18,24 L-18,6 C-24,2 -30,-4 -30,-14Z" fill="{K_}" stroke="#fff" stroke-width="5" stroke-linejoin="round"/>'
          f'<ellipse cx="-12" cy="-12" rx="9" ry="10" fill="#fff"/><ellipse cx="12" cy="-12" rx="9" ry="10" fill="#fff"/>'
          f'<path d="M0,0 l-6,12 h12z" fill="#fff"/>'
          f'<path d="M-9,18 v10 M0,18 v10 M9,18 v10" stroke="#fff" stroke-width="3.5"/>')
    return b
def ic_excl():
    return f'<path d="M-13,-52 h26 l-5,64 h-16z" fill="{K_}"/><circle cx="0" cy="36" r="13" fill="{K_}"/>'
def ic_health():
    b = f'<circle cx="0" cy="-38" r="17" fill="{K_}"/>'
    b += f'<path d="M-42,48 L-42,6 Q-42,-14 -22,-18 L22,-18 Q42,-14 42,6 L42,48Z" fill="{K_}"/>'
    b += star(0, 14, 24, 10, 8, 22.5, "#fff")
    return b
def ic_env():
    b = f'<path d="M-36,44 V-12" stroke="{K_}" stroke-width="9" stroke-linecap="round"/>'
    b += f'<path d="M-36,-2 L-52,-22 M-36,-14 L-24,-38 M-36,12 L-54,2 M-36,0 L-20,-10 M-52,-22 l-6,-4 M-24,-38 l4,-8" stroke="{K_}" stroke-width="6" stroke-linecap="round" fill="none"/>'
    b += f'<ellipse cx="14" cy="10" rx="28" ry="15" fill="{K_}"/><path d="M38,10 L58,-6 L58,26Z" fill="{K_}"/><path d="M8,-6 q10,-12 22,-6 l-10,8z" fill="{K_}"/>'
    b += f'<circle cx="0" cy="6" r="3.8" fill="#fff"/><path d="M12,-4 q-5,14 0,28" stroke="#fff" stroke-width="3" fill="none"/>'
    b += f'<path d="M-52,48 q6,-8 12,0 t12,0 t12,0 t12,0 t12,0 t12,0" stroke="{K_}" stroke-width="5" fill="none" stroke-linecap="round"/>'
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
W, H = 1500, 790
b = ''
for i, (fn, kod, n, d, sig) in enumerate(ICS):
    col, row = i % 3, i // 3
    x0 = 20 + col * 490; y0 = 20 + row * 256
    b += card(x0, y0, 470, 236, "#fff")
    cx, cy = x0 + 120, y0 + 118
    b += diamond(cx, cy, 100) + f'<g transform="translate({cx},{cy}) scale(1.0)">{fn()}</g>'
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
render('v_piktogram', svg(W, H, b, BG), W, H, 1)
