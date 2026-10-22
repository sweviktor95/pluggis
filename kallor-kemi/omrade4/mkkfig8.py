# -*- coding: utf-8 -*-
"""Kemi 4 – grundfigurer -> /tmp/kem/fig04k/"""
from k4lib import *
HC = "#eef1f3"; OC = "#e0584f"; CC = "#59636d"; NAC = "#a77bd0"; CLC = "#52b37a"
DOT = EC
def ball(x, y, r, col, txt, tc=INK, sz=None):
    sz = sz or int(r * 0.95)
    tcol = "#fff" if col in (OC, CC, NAC, CLC) else tc
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#46525c" stroke-width="4"/>' + T(x, y + sz * 0.36, txt, sz, tcol, "700")
def pair(x, y, ang=0.0, d=9, r=6.5):
    nx, ny = -math.sin(ang), math.cos(ang)
    return ''.join(f'<circle cx="{x+s*d*nx:.1f}" cy="{y+s*d*ny:.1f}" r="{r}" fill="{DOT}" stroke="#fff" stroke-width="2"/>' for s in (-1, 1))
def bond(x1, y1, x2, y2, n=1):
    a = math.atan2(y2 - y1, x2 - x1); mx, my = (x1 + x2) / 2, (y1 + y2) / 2; s = ''
    offs = [0] if n == 1 else [-15, 15]
    for o in offs:
        ox, oy = -math.sin(a) * o, math.cos(a) * o
        s += f'<path d="M{x1+ox:.0f},{y1+oy:.0f} L{x2+ox:.0f},{y2+oy:.0f}" stroke="#8d969d" stroke-width="7" stroke-linecap="round"/>' + pair(mx + ox, my + oy, a)
    return s
def mol_h2(cx, cy):
    return bond(cx - 70, cy, cx + 70, cy) + ball(cx - 70, cy, 38, HC, "H") + ball(cx + 70, cy, 38, HC, "H")
def mol_h2o(cx, cy):
    hs = [(cx - 88, cy + 70), (cx + 88, cy + 70)]
    s = ''.join(bond(cx, cy - 8, x, y) for x, y in hs)
    return s + ball(cx, cy - 8, 50, OC, "O") + ''.join(ball(x, y, 36, HC, "H") for x, y in hs)
def mol_ch4(cx, cy):
    hs = [(cx - 100, cy - 80), (cx + 100, cy - 80), (cx - 100, cy + 80), (cx + 100, cy + 80)]
    s = ''.join(bond(cx, cy, x, y) for x, y in hs)
    return s + ball(cx, cy, 48, CC, "C") + ''.join(ball(x, y, 34, HC, "H") for x, y in hs)
def mol_co2(cx, cy):
    return bond(cx - 120, cy, cx, cy, 2) + bond(cx, cy, cx + 120, cy, 2) + ball(cx - 120, cy, 46, OC, "O") + ball(cx, cy, 46, CC, "C") + ball(cx + 120, cy, 46, OC, "O")

def h2(cx, cy, r=26): return ball(cx - r, cy, r, HC, "H", sz=24) + ball(cx + r, cy, r, HC, "H", sz=24)
def o2(cx, cy, r=34): return ball(cx - r, cy, r, OC, "O", sz=28) + ball(cx + r, cy, r, OC, "O", sz=28)
def h2o_s(cx, cy):
    return ball(cx - 34, cy + 36, 24, HC, "H", sz=22) + ball(cx + 34, cy + 36, 24, HC, "H", sz=22) + ball(cx, cy, 34, OC, "O", sz=28)

# ---- v_oversikt
W, H = 1600, 480; b = ARROW
b += T(800, 52, "Atomer kan bindas ihop och byta partner", 36, DRED, "700")
for x, t1, t2 in ((270, "Molekyl", "atomerna delar elektroner"), (800, "Jonförening", "elektroner flyttar från en atom till en annan"), (1330, "Kemisk reaktion", "atomerna byter partner")):
    b += f'<rect x="{x-250}" y="90" width="500" height="340" rx="22" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>'
    b += T(x, 135, t1, 34, INK, "700") + T(x, 400, t2, 24, MUT)
b += mol_h2o(270, 250)
b += ball(690, 260, 42, NAC, "Na⁺", sz=28) + ball(790, 260, 52, CLC, "Cl⁻", sz=30) + ball(890, 260, 42, NAC, "Na⁺", sz=28)
b += ball(740, 340, 52, CLC, "Cl⁻", sz=30) + ball(840, 340, 42, NAC, "Na⁺", sz=28) if False else ''
b += ball(1115, 185, 24, HC, "H", sz=20) + ball(1163, 185, 24, HC, "H", sz=20) + T(1222, 196, "+", 32, INK, "700") + ball(1295, 185, 28, OC, "O", sz=22) + ball(1351, 185, 28, OC, "O", sz=22)
b += f'<path d="M1240,222 v28" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>'
b += h2o_s(1180, 300) + h2o_s(1300, 300)
render('v_oversikt', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_kovalent
W, H = 1600, 620; b = ''
b += T(800, 50, "Molekyler: atomerna delar elektronpar", 36, DRED, "700")
for cx, fn, name, form in ((200, mol_h2, "vätgas", "H₂"), (560, mol_h2o, "vatten", "H₂O"), (980, mol_ch4, "metan", "CH₄"), (1400, mol_co2, "koldioxid", "CO₂")):
    b += f'<rect x="{cx-175}" y="85" width="350" height="400" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>'
    b += fn(cx, 270 if fn != mol_h2o else 250) + T(cx, 450, name + "  " + form, 32, INK, "700")
b += f'<circle cx="360" cy="565" r="8" fill="{DOT}"/><circle cx="378" cy="565" r="8" fill="{DOT}"/>' + T(400, 575, "= ett delat elektronpar (en bindning). CO₂ har två par mellan C och varje O.", 28, INK, "400", "start")
render('v_kovalent', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_jon
def shellatom(cx, cy, shells, label, R0=48, dR=38, er=10, hl=None, cutout=None):
    s = ''
    for k in range(len(shells)):
        s += f'<circle cx="{cx}" cy="{cy}" r="{R0+k*dR}" fill="none" stroke="#b9c3ca" stroke-width="3"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="32" fill="{PC}" stroke="#fff" stroke-width="3"/>' + T(cx, cy + 9, label, 26, "#fff", "700")
    for k, m in enumerate(shells):
        for i in range(m):
            a = 0.35 + 6.283 * i / m + k * 0.5
            x, y = cx + (R0 + k * dR) * math.cos(a), cy + (R0 + k * dR) * math.sin(a)
            col = EC
            if hl is not None and k == hl[0] and i == hl[1]: col = "#f1a31c"
            s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{er}" fill="{col}" stroke="#fff" stroke-width="2.5"/>'
    return s
W, H = 1600, 760; b = ARROW
b += T(800, 44, "Elektroner flyttas och atomerna blir joner", 36, DRED, "700")
# rad 1 Na
b += T(60, 130, "Natrium", 30, INK, "700", "start")
b += shellatom(260, 290, [2, 8, 1], "11+", hl=(2, 0)) + T(260, 470, "natriumatom, Na", 26, INK, "700")
b += T(260, 505, "11 protoner, 11 elektroner", 24, MUT) + T(260, 535, "2, 8, 1 · laddning 0", 24, MUT)
b += f'<path d="M430,290 H600" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>' + T(515, 262, "avger", 26, INK, "700") + T(515, 328, "1 elektron", 26, INK, "700")
b += shellatom(760, 290, [2, 8], "11+") + T(760, 470, "natriumjon, Na⁺", 26, INK, "700")
b += T(760, 505, "11 protoner, 10 elektroner", 24, MUT) + T(760, 535, "2, 8 · laddning +1", 24, MUT)
b += T(1200, 240, "Att avge en elektron ger ett", 28, INK, "400", "start") + T(1200, 278, "fullt yttersta skal (2, 8),", 28, INK, "400", "start") + T(1200, 316, "som hos ädelgasen neon.", 28, INK, "400", "start")
# rad 2 Cl (ersätter) -> egen bild ovanför? lägg rad 2 i samma bild längre ned
b2 = ''
render('v_jon_tmp', svg(W, 560, b, "#ffffff"), W, 560, 1)
W, H = 1600, 1100; b = ARROW
b += T(800, 44, "Elektroner flyttas och atomerna blir joner", 36, DRED, "700")
b += T(60, 105, "Natrium avger en elektron", 30, INK, "700", "start")
b += shellatom(260, 290, [2, 8, 1], "11+", hl=(2, 0)) + T(260, 475, "natriumatom, Na", 26, INK, "700")
b += f'<path d="M430,290 H600" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>' + T(515, 262, "avger", 26, INK, "700") + T(515, 332, "1 elektron", 26, INK, "700")
b += shellatom(760, 290, [2, 8], "11+") + T(760, 475, "natriumjon, Na⁺", 26, INK, "700")
b += T(1000, 245, "11 protoner (11+)", 28, INK, "400", "start") + T(1000, 285, "10 elektroner (2, 8)", 28, INK, "400", "start") + T(1000, 325, "laddning +1", 28, "#6d3fa0", "700", "start")
b += f'<path d="M60,515 H1540" stroke="#e3d5d1" stroke-width="3"/>'
b += T(60, 570, "Klor tar upp en elektron", 30, INK, "700", "start")
b += shellatom(260, 790, [2, 8, 7], "17+") + T(260, 975, "kloratom, Cl", 26, INK, "700")
b += f'<path d="M430,790 H600" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>' + T(515, 762, "tar upp", 26, INK, "700") + T(515, 832, "1 elektron", 26, INK, "700")
b += shellatom(760, 790, [2, 8, 8], "17+", hl=(2, 7)) + T(760, 975, "kloridjon, Cl⁻", 26, INK, "700")
b += T(1000, 745, "17 protoner (17+)", 28, INK, "400", "start") + T(1000, 785, "18 elektroner (2, 8, 8)", 28, INK, "400", "start") + T(1000, 825, "laddning −1", 28, "#2f7a4d", "700", "start")
b += f'<circle cx="1000" cy="1040" r="9" fill="#f1a31c"/>' + T(1022, 1049, "= elektronen som flyttar (orange)", 26, INK, "400", "start")
render('v_jon', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_kristall
W, H = 1500, 640; b = ARROW
b += T(750, 46, "Natriumklorid, NaCl: ett jonkristallgitter", 36, DRED, "700")
# kub
b += f'<path d="M80,230 L240,200 L320,250 L160,290Z" fill="#fff" stroke="{INK}" stroke-width="4"/><path d="M80,230 L160,290 L160,430 L80,370Z" fill="#f3f3f3" stroke="{INK}" stroke-width="4"/><path d="M160,290 L320,250 L320,390 L160,430Z" fill="#e6e6e6" stroke="{INK}" stroke-width="4"/>'
b += T(200, 490, "saltkorn", 30, INK, "700") + T(200, 524, "(syns med blotta ögat)", 24, MUT)
b += f'<path d="M360,310 H470" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>' + T(415, 285, "förstora", 24, INK, "700")
gx, gy, d = 600, 130, 98
for i in range(7):
    for j in range(5):
        x, y = gx + i * d, gy + j * d
        if (i + j) % 2 == 0:
            b += ball(x, y, 26, NAC, "+", sz=30)
        else:
            b += ball(x, y, 38, CLC, "−", sz=34)
b += T(gx + 3 * d, 600, "Varje Na⁺ omges av Cl⁻ och varje Cl⁻ av Na⁺. Gittret är 3D, bilden visar ett plan.", 25, MUT)
b += ball(1290, 160, 18, NAC, "", sz=1) + T(1316, 169, "Na⁺", 26, INK, "700", "start") + ball(1290, 215, 24, CLC, "", sz=1) + T(1322, 224, "Cl⁻", 26, INK, "700", "start")
b += T(1290, 300, "Jonbindning =", 26, INK, "700", "start") + T(1290, 334, "attraktion mellan", 26, INK, "400", "start") + T(1290, 368, "positiva och", 26, INK, "400", "start") + T(1290, 402, "negativa joner", 26, INK, "400", "start")
render('v_kristall', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_ledning
def lamp(x, y, on):
    s = f'<circle cx="{x}" cy="{y}" r="34" fill="{"#ffe27a" if on else "#e8e8e8"}" stroke="#46525c" stroke-width="5"/><path d="M{x-14},{y+34} h28 v14 h-28z" fill="#9aa5ad" stroke="#46525c" stroke-width="4"/>'
    if on:
        for a in range(0, 360, 45):
            r = math.radians(a); s += f'<path d="M{x+46*math.cos(r):.0f},{y+46*math.sin(r):.0f} L{x+62*math.cos(r):.0f},{y+62*math.sin(r):.0f}" stroke="#f1a31c" stroke-width="5" stroke-linecap="round"/>'
    return s
W, H = 1600, 620; b = T(800, 46, "Leder ämnet elektrisk ström? Ja, om det finns fria laddade partiklar", 34, DRED, "700")
panels = [(280, "Fast salt", "jonerna sitter fast i gittret", False), (800, "Saltlösning", "jonerna rör sig fritt", True), (1320, "Sockerlösning", "neutrala molekyler, inga joner", False)]
for cx, t, sub, on in panels:
    b += f'<rect x="{cx-240}" y="80" width="480" height="500" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>' + lamp(cx, 160, on) + T(cx + 80, 120, "lampa", 22, MUT, "400", "start") + f'<path d="M{cx-120},250 V160 H{cx-34} M{cx+34},160 H{cx+120} V250" fill="none" stroke="#46525c" stroke-width="5"/>'
    b += ""
    b += beaker(cx - 150, 250, 300, 230, 0.7 if cx != 280 else 0.0, "#cfe6f3" if cx != 280 else "#fff", ticks=False)
    rnd = random.Random(cx)
    if cx == 280:
        for i in range(5):
            for j in range(4):
                x, y = cx - 100 + i * 50, 360 + j * 25
                b += f'<circle cx="{x}" cy="{y}" r="{11 if (i+j)%2==0 else 15}" fill="{NAC if (i+j)%2==0 else CLC}" opacity=".95"/>'
    elif cx == 800:
        for _ in range(9):
            x, y = rnd.randint(cx - 120, cx + 120), rnd.randint(335, 440); b += f'<circle cx="{x}" cy="{y}" r="11" fill="{NAC}"/>'
        for _ in range(9):
            x, y = rnd.randint(cx - 120, cx + 120), rnd.randint(335, 440); b += f'<circle cx="{x}" cy="{y}" r="15" fill="{CLC}"/>'
    else:
        for _ in range(10):
            x, y = rnd.randint(cx - 120, cx + 120), rnd.randint(335, 440); b += f'<circle cx="{x}" cy="{y}" r="12" fill="#c9b27a" stroke="#8c7a4a" stroke-width="2"/><circle cx="{x+10}" cy="{y+6}" r="7" fill="#c9b27a" stroke="#8c7a4a" stroke-width="2"/>'
    b += T(cx, 510, t, 30, INK, "700") + T(cx, 548, sub, 23, MUT)
render('v_ledning', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_reaktion (2 H2 + O2 -> 2 H2O)
W, H = 1600, 500; b = ARROW
b += T(800, 46, "En kemisk reaktion: atomerna byter partner", 36, DRED, "700")
b += f'<rect x="60" y="85" width="700" height="320" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/><rect x="840" y="85" width="700" height="320" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>'
b += h2(200, 220) + T(270, 232, "+", 40, INK, "700") + h2(340, 220) + T(420, 232, "+", 40, INK, "700") + o2(540, 220)
b += T(410, 330, "utgångsämnen (reaktanter)", 26, INK, "700") + T(410, 366, "2 vätgasmolekyler + 1 syrgasmolekyl", 24, MUT)
b += f'<path d="M770,245 H830" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>'
b += h2o_s(1070, 200) + T(1190, 232, "+", 40, INK, "700") + h2o_s(1310, 200)
b += T(1190, 330, "produkt", 26, INK, "700") + T(1190, 366, "2 vattenmolekyler", 24, MUT)
b += T(800, 460, "4 H-atomer och 2 O-atomer före, 4 H-atomer och 2 O-atomer efter: inga atomer försvinner.", 26, INK, "700")
render('v_reaktion', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_balans (CH4 + 2 O2 -> CO2 + 2 H2O)
W, H = 1700, 560; b = ARROW
b += T(850, 46, "Balansera: lika många atomer av varje sort på båda sidor", 36, DRED, "700")
def ch4_s(cx, cy):
    hs = [(cx - 52, cy - 44), (cx + 52, cy - 44), (cx - 52, cy + 44), (cx + 52, cy + 44)]
    return ''.join(f'<path d="M{cx},{cy} L{x},{y}" stroke="#8d969d" stroke-width="6"/>' for x, y in hs) + ball(cx, cy, 30, CC, "C", sz=26) + ''.join(ball(x, y, 20, HC, "H", sz=18) for x, y in hs)
def co2_s(cx, cy): return ball(cx - 66, cy, 28, OC, "O", sz=24) + ball(cx, cy, 30, CC, "C", sz=26) + ball(cx + 66, cy, 28, OC, "O", sz=24)
b += ch4_s(120, 230) + T(210, 242, "+", 36, INK, "700") + o2(300, 230, 26) + T(395, 242, "+", 36, INK, "700") + o2(490, 230, 26)
b += f'<path d="M600,235 H690" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>'
b += co2_s(785, 230) + T(905, 242, "+", 36, INK, "700") + h2o_s(1010, 215) + T(1120, 242, "+", 36, INK, "700") + h2o_s(1230, 215)
b += T(300, 330, "CH₄ + 2 O₂", 36, INK, "700") + T(1000, 330, "CO₂ + 2 H₂O", 36, INK, "700") + T(650, 330, "→", 38, INK, "700")
b += T(300, 372, "metan + syre", 26, MUT) + T(1000, 372, "koldioxid + vatten", 26, MUT)
b += f'<rect x="1380" y="95" width="290" height="280" rx="18" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>' + T(1525, 135, "Atomer", 28, INK, "700")
for i, (a, l, r) in enumerate((("C", 1, 1), ("H", 4, 4), ("O", 4, 4))):
    y = 190 + i * 62
    b += T(1420, y, a, 30, INK, "700", "start") + T(1495, y, f"{l}", 30, INK, "400") + T(1535, y, "→", 28, MUT) + T(1590, y, f"{r}", 30, INK, "400") + T(1640, y, "✓", 28, "#2f7a4d", "700")
b += T(850, 470, "Metan brinner: koldioxid och vatten bildas. Utan koefficienterna 2 skulle H och O inte gå ihop.", 26, MUT)
b += T(850, 510, "Koefficient = talet framför formeln. Det säger hur många molekyler som reagerar.", 26, INK, "700")
render('v_balans', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_hastighet
def box(x, y, w, h, n, speed, seed, big=False):
    rnd = random.Random(seed); s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f8fafb" stroke="#8d969d" stroke-width="3"/>'
    for _ in range(n):
        px, py = rnd.randint(x + 22, x + w - 22), rnd.randint(y + 22, y + h - 22)
        s += f'<circle cx="{px}" cy="{py}" r="10" fill="{rnd.choice([EC, OC])}"/>'
        if speed:
            a = rnd.uniform(0, 6.283); L = speed
            s += f'<path d="M{px},{py} l{L*math.cos(a):.0f},{L*math.sin(a):.0f}" stroke="{INK}" stroke-width="3"/>'
    return s
W, H = 1700, 660; b = T(850, 46, "Vad påverkar hur fort en reaktion går?", 36, DRED, "700")
cols = [(290, "Temperatur", ("Kallt: få, långsamma krockar", box(70, 100, 440, 190, 10, 14, 1)), ("Varmt: fler, hårdare krockar", box(70, 340, 440, 190, 10, 34, 2))),
        (850, "Koncentration", ("Utspätt: få partiklar", box(630, 100, 440, 190, 6, 0, 3)), ("Koncentrerat: många partiklar", box(630, 340, 440, 190, 20, 0, 4))),
        (1410, "Ytarea", ("En bit: litet yta", None), ("Smulat: stor yta", None))]
for cx, t, (l1, bx1), (l2, bx2) in cols:
    b += T(cx, 90, t, 32, INK, "700") if False else ''
    b += T(cx, 90, t, 32, INK, "700")
    if bx1: b += bx1 + bx2
    b += T(cx, 322, l1, 24, MUT) if cx != 1410 else ''
    b += T(cx, 562, l2, 24, MUT) if cx != 1410 else ''
b += f'<rect x="1190" y="100" width="440" height="190" rx="12" fill="#f8fafb" stroke="#8d969d" stroke-width="3"/><rect x="1330" y="140" width="160" height="110" rx="8" fill="#d7c9a8" stroke="#8c7a4a" stroke-width="4"/>' + T(1410, 322, "En hel bit: liten yta", 24, MUT)
b += f'<rect x="1190" y="340" width="440" height="190" rx="12" fill="#f8fafb" stroke="#8d969d" stroke-width="3"/>'
rnd = random.Random(9)
for i in range(4):
    for j in range(3):
        b += f'<rect x="{1260+i*85+rnd.randint(-5,5)}" y="{370+j*50}" width="{50+rnd.randint(-6,6)}" height="{34}" rx="5" fill="#d7c9a8" stroke="#8c7a4a" stroke-width="3"/>'
b += T(1410, 562, "Smulat i små bitar: stor yta", 24, MUT)
b += T(850, 625, "Fler och hårdare krockar mellan partiklarna ger fler lyckade reaktioner per sekund.", 26, INK, "700")
render('v_hastighet', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_energi
W, H = 1600, 560; b = ARROW
b += T(800, 46, "Energi i kemiska reaktioner", 36, DRED, "700")
for x0, title, hi, lo, lab, col, txt in ((90, "Exoterm: energi avges", 150, 330, "energi avges (värme)", "#e0584f", "omgivningen blir varmare"), (840, "Endoterm: energi tas upp", 330, 150, "energi tas upp", "#2f6aa3", "omgivningen blir kallare")):
    b += f'<rect x="{x0-30}" y="80" width="740" height="440" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>' + T(x0 + 340, 125, title, 32, INK, "700")
    b += f'<path d="M{x0+30},90 V470 H{x0+650}" fill="none" stroke="{INK}" stroke-width="4" marker-start="none"/>' + T(x0 + 20, 150, "energi", 24, MUT, "400", "end") if False else ''
    b += f'<path d="M{x0+30},150 V470 H{x0+660}" fill="none" stroke="{INK}" stroke-width="4"/>' + T(x0 + 28, 140, "energi", 24, MUT, "400", "start")
    b += f'<path d="M{x0+90},{hi+60} H{x0+270}" stroke="{INK}" stroke-width="8"/><path d="M{x0+420},{lo+60} H{x0+600}" stroke="{INK}" stroke-width="8"/>'
    b += f'<path d="M{x0+270},{hi+60} L{x0+420},{lo+60}" stroke="{MUT}" stroke-width="4" stroke-dasharray="10 8"/>'
    b += f'<path d="M{x0+345},{(hi+lo)//2+40} v{(lo-hi)//2 - 20 if lo>hi else -(hi-lo)//2 + 20}" stroke="{col}" stroke-width="7" marker-end="url(#a3)"/>' if False else ''
    b += T(x0 + 180, hi + 45, "utgångsämnen" if hi < lo else "utgångsämnen", 24, INK, "700") if False else ''
    b += T(x0 + 180, hi + 38, "utgångsämnen", 24, INK, "700") + T(x0 + 510, lo + 38, "produkter", 24, INK, "700")
    b += T(x0 + 340, 495, lab + " · " + txt, 25, col, "700")
render('v_energi', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_labb1 (ledningsförmåga)
W, H = 1400, 650; b = ARROW
b += T(700, 46, "Kopplingsschema: leder lösningen ström?", 34, DRED, "700")
b += f'<rect x="150" y="140" width="150" height="80" rx="8" fill="#dde3e8" stroke="#46525c" stroke-width="5"/>' + T(225, 192, "4,5 V", 34, INK, "700") + f'<rect x="300" y="165" width="14" height="30" fill="#46525c"/>' + T(225, 125, "batteri", 24, MUT)
b += lamp(700, 190, False) + T(700, 120, "lampa", 24, MUT)
b += f'<path d="M225,140 V100 H600 V190 H666 M734,190 H901 V380 M225,220 V330 H661 V380" fill="none" stroke="#46525c" stroke-width="5"/>'
b += beaker(600, 400, 360, 170, 0.6, "#cfe6f3", ticks=False)
b += f'<rect x="550" y="425" width="22" height="120" rx="4" fill="#b8c0c7" stroke="#46525c" stroke-width="4"/><rect x="990" y="425" width="22" height="120" rx="4" fill="#b8c0c7" stroke="#46525c" stroke-width="4"/>' if False else ''
b += f'<rect x="650" y="380" width="22" height="150" rx="4" fill="#b8c0c7" stroke="#46525c" stroke-width="4"/><rect x="890" y="380" width="22" height="150" rx="4" fill="#b8c0c7" stroke="#46525c" stroke-width="4"/>'
b += T(780, 625, "lösning som testas", 26, INK, "700") + T(590, 372, "elektrod", 22, MUT) + T(900, 365, "elektrod", 22, MUT)
b += T(1180, 250, "Lyser lampan?", 30, INK, "700") + T(1180, 292, "Ja: fria joner.", 26, MUT) + T(1180, 326, "Nej: inga fria joner.", 26, MUT)
render('v_labb1', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_labb2 (massan bevaras)
W, H = 1600, 640; b = T(800, 46, "Massan före och efter: sluten och öppen flaska", 34, DRED, "700")
for cx, t, open_ in ((420, "Sluten flaska (ballong)", False), (1180, "Öppen flaska", True)):
    b += f'<rect x="{cx-330}" y="80" width="660" height="520" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>'
    b += balance(cx - 110, 470, 220, "152,4 g" if not open_ else "151,6 g", 28)
    b += flask(cx - 95, 260, 190, 200, 0.4, "#f6e9c0")
    if open_:
        for k in range(4):
            b += bubble(cx - 30 + k * 20, 235 - k * 22, 9 + k, 0.9)
        b += T(cx + 90, 200, "gas (CO₂)", 24, INK, "700", "start") + T(cx + 90, 230, "lämnar flaskan", 24, INK, "700", "start")
    else:
        b += f'<ellipse cx="{cx}" cy="205" rx="62" ry="56" fill="#f3a9a3" stroke="#a8322a" stroke-width="5"/><rect x="{cx-14}" y="248" width="28" height="22" fill="#f3a9a3" stroke="#a8322a" stroke-width="4"/>'
        b += T(cx + 90, 195, "gasen samlas", 24, INK, "700", "start") + T(cx + 90, 225, "i ballongen", 24, INK, "700", "start")
    b += T(cx, 125, t, 30, INK, "700") + T(cx, 578, "Massan är oförändrad" if not open_ else "Massan har minskat", 26, "#2f7a4d" if not open_ else "#a8322a", "700")
render('v_labb2', svg(W, H, b, "#ffffff"), W, H, 1)
print("klar mkkfig8")
