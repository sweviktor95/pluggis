# -*- coding: utf-8 -*-
from kfig_common import *

# ---------- v_utrustning ------------------------------------------------------
W, H = 1500, 672
b = ''
b += shelf(40, 1460, 330) + shelf(40, 1460, 598)
b += beaker(95, 160, 130, 170, 0.5)
b += cylinder(400, 70, 46, 260, 0.55)
b += flask(630, 105, 170, 225, 0.35)
b += tube(912, 190, 140, "#bcd9ec", .5) + tube(962, 190, 140, "#f4c7cf", .45) + tube(1012, 190, 140, "#f6e3a8", .4)
b += '<rect x="895" y="228" width="170" height="14" rx="5" fill="#a9703c"/><rect x="895" y="318" width="170" height="12" rx="5" fill="#a9703c"/><rect x="898" y="228" width="10" height="100" fill="#a9703c"/><rect x="1052" y="228" width="10" height="100" fill="#a9703c"/>'
b += thermometer(1265, 80, 190, 0.45)
for x, n in [(160, "Bägare"), (423, "Mätcylinder"), (715, "E-kolv"), (980, "Provrör i ställ"), (1290, "Termometer")]:
    b += T(x, 372, n, 30, INK, "700")
b += balance(90, 520, 170, "12,4 g", 26)
b += pipette(430, 462, 0.8)
b += goggles(730, 565, 0.9)
b += f'<circle cx="1000" cy="545" r="52" fill="#fff" stroke="{LINE}" stroke-width="6"/><rect x="988" y="482" width="24" height="14" rx="4" fill="{LINE}"/><path d="M1000,545 L1000,512 M1000,545 L1024,556" stroke="{RED}" stroke-width="6" stroke-linecap="round"/><circle cx="1000" cy="545" r="6" fill="{INK}"/>'
for k in range(12):
    a = math.radians(k * 30)
    b += f'<path d="M{1000+44*math.sin(a):.1f},{545-44*math.cos(a):.1f} L{1000+50*math.sin(a):.1f},{545-50*math.cos(a):.1f}" stroke="{MUT}" stroke-width="3"/>'
b += f'<g transform="translate(1290,560) rotate(-20)"><rect x="-90" y="-7" width="150" height="14" rx="7" fill="#c9d1d6" stroke="{LINE}" stroke-width="3"/><ellipse cx="78" cy="0" rx="26" ry="14" fill="#c9d1d6" stroke="{LINE}" stroke-width="3"/></g>'
for x, n in [(175, "Våg"), (430, "Pipett"), (730, "Skyddsglasögon"), (1000, "Stoppur"), (1290, "Spatel")]:
    b += T(x, 642, n, 30, INK, "700")
render('v_utrustning', svg(W, H, b, BG), W, H, 1)

# ---------- v_piktogram -------------------------------------------------------
def diamond(cx, cy, r=78):
    return f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" fill="#fff" stroke="#d6002b" stroke-width="13" stroke-linejoin="miter"/>'
def star(cx, cy, r1, r2, n=9, rot=0, col="#111"):
    pts = []
    for k in range(n * 2):
        r = r1 if k % 2 == 0 else r2
        a = math.radians(rot + k * 180 / n)
        pts.append(f"{cx+r*math.sin(a):.1f},{cy-r*math.cos(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'
def ic_bomb(cx, cy):
    return (star(cx + 16, cy - 20, 36, 16, 8, 10) + f'<circle cx="{cx-14}" cy="{cy+18}" r="26" fill="#111"/><path d="M{cx-2},{cy-2} q14,-8 20,-20" stroke="#111" stroke-width="7" fill="none" stroke-linecap="round"/>')
FLAME = "M0,-44 C14,-26 30,-16 28,6 C27,24 14,36 0,36 C-16,36 -28,24 -26,6 C-25,-6 -16,-12 -12,-26 C-6,-20 -2,-30 0,-44Z"
def ic_flame(cx, cy, s=1.0):
    return f'<g transform="translate({cx},{cy+4}) scale({s})"><path d="{FLAME}" fill="#111"/><path d="M0,34 C-9,34 -14,26 -13,18 C-12,10 -3,6 0,-6 C4,4 13,10 13,18 C14,26 9,34 0,34Z" fill="#fff"/></g>'
def ic_ox(cx, cy):
    return f'<circle cx="{cx}" cy="{cy+22}" r="23" fill="none" stroke="#111" stroke-width="9"/><g transform="translate({cx},{cy-18}) scale(.62)"><path d="{FLAME}" fill="#111"/></g>'
def ic_gas(cx, cy):
    return (f'<rect x="{cx-17}" y="{cy-30}" width="34" height="68" rx="16" fill="#111"/><rect x="{cx-7}" y="{cy-44}" width="14" height="18" rx="3" fill="#111"/><rect x="{cx-14}" y="{cy-48}" width="28" height="8" rx="3" fill="#111"/>')
def ic_corr(cx, cy):
    return (f'<rect x="{cx-48}" y="{cy+22}" width="50" height="14" fill="#111"/>'
            f'<path d="M{cx+14},{cy+36} v-18 q0,-10 8,-10 q8,0 8,10 v-10 q0,-9 8,-9 q8,0 8,9 v22 q0,18 -14,24 h-14 q-6,-6 -4,-17z" fill="#111" transform="translate(-8,-6)"/>'
            f'<g transform="translate({cx-34},{cy-36}) rotate(35)"><rect x="-8" y="-12" width="16" height="34" rx="6" fill="#111"/></g><g transform="translate({cx+8},{cy-40}) rotate(-35)"><rect x="-8" y="-12" width="16" height="34" rx="6" fill="#111"/></g>'
            f'<circle cx="{cx-34}" cy="{cy+4}" r="4.5" fill="#111"/><circle cx="{cx-28}" cy="{cy+14}" r="4" fill="#111"/><circle cx="{cx+4}" cy="{cy-8}" r="4.5" fill="#111"/><circle cx="{cx-2}" cy="{cy+4}" r="4" fill="#111"/>')
def ic_skull(cx, cy):
    return (f'<path d="M{cx-44},{cy+30} L{cx+44},{cy+4} M{cx-44},{cy+4} L{cx+44},{cy+30}" stroke="#111" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M{cx-30},{cy-6} q-4,-34 30,-34 q34,0 30,34 q0,10 -10,14 v14 h-40 v-14 q-10,-4 -10,-14z" fill="#fff" stroke="#111" stroke-width="7" stroke-linejoin="round"/>'
            f'<circle cx="{cx-12}" cy="{cy-12}" r="8" fill="#111"/><circle cx="{cx+12}" cy="{cy-12}" r="8" fill="#111"/><path d="M{cx-4},{cy+4} h8 l-4,-8z" fill="#111"/><path d="M{cx-12},{cy+14} v10 M{cx},{cy+14} v10 M{cx+12},{cy+14} v10" stroke="#111" stroke-width="4"/>')
def ic_excl(cx, cy):
    return f'<path d="M{cx-10},{cy-44} h20 l-4,50 h-12z" fill="#111"/><circle cx="{cx}" cy="{cy+28}" r="11" fill="#111"/>'
def ic_health(cx, cy):
    return (f'<circle cx="{cx-6}" cy="{cy-34}" r="13" fill="#111"/><path d="M{cx-36},{cy+42} v-52 q0,-16 16,-16 h20 q16,0 22,16 l8,18 l-18,8 l-6,-12 v38z" fill="#111"/>'
            + star(cx + 2, cy + 2, 17, 7, 7, 0, "#fff"))
def ic_env(cx, cy):
    return (f'<path d="M{cx-34},{cy+44} v-40 M{cx-34},{cy+4} l-18,-22 M{cx-34},{cy-8} l16,-24 M{cx-34},{cy+22} l-22,-8 M{cx-34},{cy-8} l24,-4" stroke="#111" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M{cx-48},{cy+46} h30" stroke="#111" stroke-width="6" stroke-linecap="round"/>'
            f'<g transform="translate({cx+22},{cy+14})"><ellipse cx="0" cy="0" rx="26" ry="15" fill="#111"/><path d="M24,0 L44,-14 L44,14Z" fill="#111"/><circle cx="-14" cy="-3" r="3.5" fill="#fff"/></g>'
            f'<path d="M{cx-6},{cy+44} h66" stroke="#111" stroke-width="5" stroke-linecap="round"/>')
ICS = [(ic_bomb, "Explosivt", "Kan explodera, till exempel fyrverkerier."), (ic_flame, "Brandfarligt", "Kan fatta eld lätt, till exempel sprit."),
       (ic_ox, "Oxiderande", "Kan få andra ämnen att brinna mycket lättare."), (ic_gas, "Gas under tryck", "Gasflaska. Kan explodera om den blir varm."),
       (ic_corr, "Frätande", "Kan skada hud och ögon och fräta på metall."), (ic_skull, "Giftigt", "Kan ge allvarlig skada eller död, även i små mängder."),
       (ic_excl, "Skadligt, irriterande", "Mindre allvarlig fara, till exempel irritation av hud och ögon."), (ic_health, "Allvarlig hälsofara", "Kan ge sjukdom på lång sikt, till exempel cancer."),
       (ic_env, "Miljöfarligt", "Skadligt för djur och växter i vatten.")]
W, H = 1500, 720
b = ''
for i, (fn, n, d) in enumerate(ICS):
    col, row = i % 3, i // 3
    x0 = 20 + col * 490; y0 = 20 + row * 226
    b += card(x0, y0, 470, 206, "#fff")
    cx, cy = x0 + 105, y0 + 103
    b += diamond(cx, cy, 80) + fn(cx, cy)
    b += T(x0 + 205, y0 + 74, n, 30, INK, "700", "start")
    words = d.split(' '); lines = []; cur = ''
    for w in words:
        if len(cur + ' ' + w) > 24:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    lines.append(cur)
    for k, ln in enumerate(lines[:3]): b += T(x0 + 205, y0 + 108 + k * 28, ln, 23, MUT, "400", "start")
render('v_piktogram', svg(W, H, b, BG), W, H, 1)

# ---------- v_menisk ----------------------------------------------------------
W, H = 1500, 640
b = ''
cx0, cy0, cw, chh = 640, 70, 90, 470
b += cylinder(cx0, cy0, cw, chh, 0.58, nt=10)
ly = cy0 + chh * (1 - 0.58)
def eye(x, y):
    return (f'<g transform="translate({x},{y})"><path d="M-34,0 Q0,-30 34,0 Q0,30 -34,0Z" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="8" cy="0" r="11" fill="#3a6f9c"/><circle cx="11" cy="0" r="5" fill="#111"/></g>')
for (ey, lab, ok) in [(ly - 130, "För högt", False), (ly, "Rätt", True), (ly + 130, "För lågt", False)]:
    colr = "#2f8a4f" if ok else RED
    b += eye(300, ey)
    b += f'<path d="M345,{ey} L{cx0-12},{ly+4}" stroke="{colr}" stroke-width="4.5" stroke-dasharray="{"0" if ok else "12 8"}" fill="none"/>'
    b += T(300, ey + 62 if ey > ly - 10 else ey - 40, lab, 30, colr, "700")
b += f'<path d="M{cx0+cw+16},{ly+5} h60" stroke="{RED}" stroke-width="5"/>'
zx, zy, zr = 1130, 230, 150
b += f'<circle cx="{zx}" cy="{zy}" r="{zr}" fill="#fff" stroke="{LINE}" stroke-width="6"/>'
b += f'<clipPath id="zc"><circle cx="{zx}" cy="{zy}" r="{zr-4}"/></clipPath><g clip-path="url(#zc)"><rect x="{zx-zr}" y="{zy-zr}" width="{2*zr}" height="{2*zr}" fill="#f2f7fa"/>'
b += f'<path d="M{zx-zr},{zy-50} Q{zx-100},{zy-48} {zx-60},{zy+8} Q{zx},{zy+40} {zx+60},{zy+8} Q{zx+100},{zy-48} {zx+zr},{zy-50} L{zx+zr},{zy+zr} L{zx-zr},{zy+zr}Z" fill="#bcd9ec"/>'
b += f'<path d="M{zx-zr},{zy-50} Q{zx-100},{zy-48} {zx-60},{zy+8} Q{zx},{zy+40} {zx+60},{zy+8} Q{zx+100},{zy-48} {zx+zr},{zy-50}" stroke="#4a86b3" stroke-width="5" fill="none"/>'
b += f'<path d="M{zx-zr},{zy+26} h{2*zr}" stroke="{RED}" stroke-width="4.5" stroke-dasharray="14 8"/></g>'
b += f'<path d="M{cx0+cw+16+60},{ly+5} L{zx-zr+14},{zy+60}" stroke="{MUT}" stroke-width="3" stroke-dasharray="4 7"/>'
b += T(zx, 428, "Vattenytan kröker sig nedåt (menisk).", 28, INK, "700")
b += T(zx, 462, "Läs av vid den lägsta punkten,", 26, MUT)
b += T(zx, 492, "med ögonen i samma höjd.", 26, MUT)
b += T(zx, 540, "Annars blir avläsningen fel (parallaxfel).", 26, RED, "700")
render('v_menisk', svg(W, H, b, BG), W, H, 1)
