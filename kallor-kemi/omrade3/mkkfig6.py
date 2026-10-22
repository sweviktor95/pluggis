# -*- coding: utf-8 -*-
"""Kemi 3 – grundfigurer -> /tmp/kem/fig03k/"""
from kfig3_common import *
PC = "#d9534a"; NC = "#8a97a1"; EC = "#2f6aa3"
ARROW = f'<defs><marker id="a3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="{INK}"/></marker></defs>'

def nuc(cx, cy, p, n, r=15, seed=3):
    rnd = random.Random(seed); items = ['p'] * p + ['n'] * n; rnd.shuffle(items)
    pts = []; spread = r * (1 + 0.9 * math.sqrt(len(items)))
    for t in items:
        for _ in range(400):
            a = rnd.uniform(0, 6.283); d = rnd.uniform(0, spread) ** 1 * 0.6 + 0
            x = cx + d * math.cos(a); y = cy + d * math.sin(a)
            if all((x - u) ** 2 + (y - v) ** 2 >= (1.75 * r) ** 2 for u, v, _ in pts): pts.append((x, y, t)); break
        else:
            spread += 4; pts.append((cx + rnd.uniform(-spread, spread) * .6, cy + rnd.uniform(-spread, spread) * .6, t))
    return ''.join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{PC if t=="p" else NC}" stroke="#fff" stroke-width="2.5"/>' for x, y, t in pts)
def atom(cx, cy, p, n, shells, r=15, R0=95, dR=62, er=11, lab=True, seed=3, rot=0.3):
    s = ''
    for k in range(len(shells)):
        s += f'<circle cx="{cx}" cy="{cy}" r="{R0+k*dR}" fill="none" stroke="#b9c3ca" stroke-width="3" stroke-dasharray="3 0"/>'
    s += nuc(cx, cy, p, n, r, seed)
    for k, m in enumerate(shells):
        for i in range(m):
            a = rot + 6.283 * i / m + k * 0.5
            s += f'<circle cx="{cx+(R0+k*dR)*math.cos(a):.0f}" cy="{cy+(R0+k*dR)*math.sin(a):.0f}" r="{er}" fill="{EC}" stroke="#fff" stroke-width="2.5"/>'
    return s
def legend(x, y, size=26, gap=190):
    s = ''
    for i, (c, t) in enumerate([(PC, "proton (+)"), (NC, "neutron (0)"), (EC, "elektron (−)")]):
        s += f'<circle cx="{x+i*gap}" cy="{y}" r="11" fill="{c}"/>' + T(x + i * gap + 20, y + 9, t, size, INK, "400", "start")
    return s

# ---- v_oversikt
W, H = 1500, 440; b = ARROW
b += f'<rect x="40" y="130" width="210" height="150" rx="14" fill="#c9ced3" stroke="#8d969d" stroke-width="5"/><path d="M60,160 h90 M60,200 h140" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".6"/>' + T(145, 330, "metallbit", 30, INK, "700")
b += f'<path d="M265,205 H345" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>'
b += f'<rect x="365" y="105" width="270" height="200" rx="16" fill="#fff" stroke="#8d969d" stroke-width="4"/>'
for i in range(5):
    for j in range(4):
        b += f'<circle cx="{400+i*54}" cy="{140+j*48}" r="21" fill="#dfe6ea" stroke="#8d969d" stroke-width="3"/>'
b += T(500, 345, "förstorat: atomer", 30, INK, "700")
b += f'<path d="M650,205 H730" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>'
b += atom(900, 205, 6, 6, [2, 4], 12, 80, 58, 10) + T(900, 345, "en atom", 30, INK, "700")
b += f'<path d="M1030,205 H1110" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>'
b += nuc(1250, 205, 6, 6, 18, 5) + T(1250, 345, "atomkärnan", 30, INK, "700")
b += T(750, 52, "Atomens radie är ungefär 0,1 nm. Kärnan är mindre än en tiotusendel av det.", 30, DRED, "700")
b += legend(480, 400)
render('v_oversikt', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_atom (kol)
W, H = 1100, 640; b = atom(400, 300, 6, 6, [2, 4], 17, 100, 78, 14, seed=5)
b += T(550, 52, "Kolatom: atomnummer 6, masstal 12", 36, DRED, "700")
b += f'<path d="M405,300 L600,150" stroke="{MUT}" stroke-width="3"/>' + T(610, 140, "kärna: 6 protoner + 6 neutroner", 26, INK, "700", "start")
b += f'<path d="M{400+178*0.94:.0f},{300-178*0.34:.0f} L660,230" stroke="{MUT}" stroke-width="3"/>' + T(665, 232, "elektron", 26, INK, "700", "start")
b += T(400, 560, "Skal 1: 2 elektroner · Skal 2: 4 elektroner", 28, INK, "700") + legend(70, 610)
render('v_atom', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_modeller
W, H = 1600, 480; b = ''
cols = [("Dalton", "1808"), ("Thomson", "slutet av 1800-talet"), ("Rutherford", "1911"), ("Bohr", "1913")]
for i, (nm, yr) in enumerate(cols):
    cx = 200 + i * 400
    b += f'<rect x="{cx-180}" y="30" width="360" height="420" rx="20" fill="#fff" stroke="#e3d5d1" stroke-width="3"/>' + T(cx, 80, nm, 38, RED, "700") + T(cx, 114, yr, 26, MUT)
    cy = 270
    if i == 0: b += f'<circle cx="{cx}" cy="{cy}" r="105" fill="#9aa7b0" stroke="{INK}" stroke-width="5"/><path d="M{cx-60},{cy-40} q40,-40 90,-20" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".6"/>'
    if i == 1:
        b += f'<circle cx="{cx}" cy="{cy}" r="105" fill="#f6c9c4" stroke="{INK}" stroke-width="5"/>'
        for a, d in [(0.3, 55), (1.6, 70), (2.6, 40), (3.7, 75), (4.6, 50), (5.5, 70), (0, 0), (3.1, 0)]:
            b += f'<circle cx="{cx+d*math.cos(a):.0f}" cy="{cy+d*math.sin(a):.0f}" r="11" fill="{EC}" stroke="#fff" stroke-width="2.5"/>'
        b += T(cx, 424, "positiv ”deg” + elektroner", 24, INK)
    if i == 2:
        b += f'<circle cx="{cx}" cy="{cy}" r="9" fill="{PC}"/><circle cx="{cx}" cy="{cy}" r="105" fill="none" stroke="#b9c3ca" stroke-width="3" stroke-dasharray="4 8"/>'
        for a in (0.5, 2.3, 4.1):
            b += f'<circle cx="{cx+105*math.cos(a):.0f}" cy="{cy+105*math.sin(a):.0f}" r="11" fill="{EC}" stroke="#fff" stroke-width="2.5"/>'
        b += T(cx, 424, "liten tung kärna", 24, INK)
    if i == 3:
        b += f'<circle cx="{cx}" cy="{cy}" r="12" fill="{PC}"/>'
        for r_, a in [(55, 0.8), (105, 3.5)]:
            b += f'<circle cx="{cx}" cy="{cy}" r="{r_}" fill="none" stroke="#b9c3ca" stroke-width="3"/><circle cx="{cx+r_*math.cos(a):.0f}" cy="{cy+r_*math.sin(a):.0f}" r="11" fill="{EC}" stroke="#fff" stroke-width="2.5"/>'
        b += T(cx, 424, "elektroner i skal", 24, INK)
    if i == 0: b += T(cx, 424, "odelbar kula", 24, INK)
render('v_modeller', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_rutherford
W, H = 900, 520; b = ARROW
b += f'<rect x="430" y="60" width="26" height="400" fill="#e8c76a" stroke="#b9983a" stroke-width="3"/>' + T(443, 490, "guldfolie", 26, INK, "700")
for x in range(443, 444): pass
for y in range(350, 440, 22): pass
for k in range(443, 444): pass
b += f'<circle cx="443" cy="245" r="9" fill="{PC}"/>'
b += f'<rect x="40" y="120" width="140" height="70" rx="10" fill="#cfd5da" stroke="#8d969d" stroke-width="4"/>' + T(110, 162, "alfakälla", 24, INK, "700")
for y in (205, 235, 270):
    b += f'<path d="M180,{y} H430" stroke="{EC}" stroke-width="5" marker-end="url(#a3)"/>'
b += f'<path d="M456,235 H800" stroke="{EC}" stroke-width="5" marker-end="url(#a3)"/><path d="M456,270 H800" stroke="{EC}" stroke-width="5" marker-end="url(#a3)"/><path d="M456,205 H800" stroke="{EC}" stroke-width="5" marker-end="url(#a3)"/>'
b += f'<path d="M180,225 L425,244 L560,360" fill="none" stroke="{RED}" stroke-width="5" marker-end="url(#a3)"/><path d="M180,248 L440,246 L420,120" fill="none" stroke="{RED}" stroke-width="5" marker-end="url(#a3)" opacity="0"/>'
b += f'<path d="M180,250 L432,246 L250,180" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="10 7" marker-end="url(#a3)"/>'
b += T(700, 190, "de flesta går rakt igenom", 28, EC, "700") + T(640, 410, "några få avlänkas", 28, RED, "700") + T(300, 110, "mycket få kastas tillbaka", 28, RED, "700")
render('v_rutherford', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_isotoper
W, H = 1500, 560; b = ''
for i, (nm, n) in enumerate([("Kol-12", 6), ("Kol-13", 7), ("Kol-14", 8)]):
    cx = 250 + i * 500
    b += f'<rect x="{cx-220}" y="20" width="440" height="520" rx="20" fill="#fff" stroke="#e3d5d1" stroke-width="3"/>' + T(cx, 70, nm, 38, RED, "700")
    b += nuc(cx, 260, 6, n, 20, 7 + i) + T(cx, 410, f"6 protoner, {n} neutroner", 28, INK, "700") + T(cx, 450, f"masstal {6+n}", 28, MUT)
    b += T(cx, 505, "stabil" if i < 2 else "radioaktiv", 28, "#2e7d32" if i < 2 else RED, "700")
b += legend(430, 545, 22, 220)
render('v_isotoper', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_stralning
W, H = 1400, 530; b = ARROW
b += f'<rect x="30" y="60" width="120" height="400" rx="12" fill="#e8c76a" stroke="#b9983a" stroke-width="4"/>' + T(90, 270, "källa", 28, INK, "700")
for y, nm, x, col, w_, stop, lab in [(110, "Alfa", 520, "#e0873a", 18, "papper", "#fff"), (240, "Beta", 700, "#6fa8d6", 30, "aluminium", "#c9ced3"), (370, "Gamma", 1010, "#9b6fc4", 70, "bly", "#6d7780")]:
    b += f'<path d="M155,{y+20} H{x-10}" stroke="{col}" stroke-width="7" marker-end="url(#a3)"/>'
    b += f'<rect x="{x}" y="{y-45}" width="{w_}" height="130" fill="{lab}" stroke="{INK}" stroke-width="4"/>' + T(x + w_ / 2, y + 120, stop, 26, INK, "700")
    b += T(175, y + 5, nm, 30, col, "700", "start")
b += T(1250, 130, "stoppas av papper", 22, MUT, "400", "middle") if False else ''
render('v_stralning', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_labb1
W, H = 900, 600; b = f'<rect x="150" y="90" width="600" height="420" rx="14" fill="#e6d3b3" stroke="#8a6d3b" stroke-width="7"/>'
b += f'<rect x="400" y="220" width="130" height="140" rx="10" fill="#cfd5da" stroke="#8d969d" stroke-width="4" stroke-dasharray="10 8"/>' + T(465, 300, "?", 70, MUT, "700")
b += ARROW
for (x1, y1, x2, y2) in [(40, 150, 400, 260), (40, 300, 395, 300), (40, 450, 400, 330)]:
    b += f'<circle cx="{x1}" cy="{y1}" r="16" fill="{EC}"/><path d="M{x1+20},{y1} L{x2},{y2}" stroke="{EC}" stroke-width="5" stroke-dasharray="9 7" marker-end="url(#a3)"/>'
b += T(450, 60, "Sedd uppifrån: dold form i lådan", 34, DRED, "700") + T(450, 570, "Kulor rullas in från olika håll", 28, INK, "700")
render('v_labb1', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_pse
rows = {1: ["H"] + [None] * 16 + ["He"], 2: ["Li", "Be"] + [None] * 10 + ["B", "C", "N", "O", "F", "Ne"], 3: ["Na", "Mg"] + [None] * 10 + ["Al", "Si", "P", "S", "Cl", "Ar"],
        4: "K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr".split(), 5: "Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe".split(),
        6: "Cs Ba La Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn".split(), 7: "Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og".split()}
Z = {}; z = 0
order = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og".split()
for i, s in enumerate(order): Z[s] = i + 1
assert len(order) == 118
NONM = set("H C N O P S Se F Cl Br I He Ne Ar Kr Xe Rn At Ts Og".split()); META = set("B Si Ge As Sb Te".split())
def cat(s): return ("#cfe9c6", "#2e7d32") if s in NONM else (("#fbe7a6", "#9a7a10") if s in META else ("#cfe0f3", "#2f5f95"))
W, H = 1600, 940; cw, ch = 78, 74; X0, Y0 = 80, 120; b = ''
for g in range(1, 19): b += T(X0 + (g - 1) * cw + cw / 2, Y0 - 14, str(g), 24, MUT, "700")
for p in range(1, 8): b += T(X0 - 30, Y0 + (p - 1) * ch + ch / 2 + 9, str(p), 24, MUT, "700")
def cell(x, y, s):
    f, st = cat(s)
    return f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" rx="7" fill="{f}" stroke="{st}" stroke-width="2"/>' + T(x + 9, y + 24, Z[s], 18, MUT, "400", "start") + T(x + cw / 2, y + 56, s, 32, INK, "700")
for p, rw in rows.items():
    for gi, s in enumerate(rw):
        if s and not (s in ('La', 'Ac') and p in (6, 7)): b += cell(X0 + gi * cw, Y0 + (p - 1) * ch, s)
        elif s: b += f'<rect x="{X0+gi*cw+2}" y="{Y0+(p-1)*ch+2}" width="{cw-4}" height="{ch-4}" rx="7" fill="#fff" stroke="#8d969d" stroke-width="2" stroke-dasharray="5 4"/>' + T(X0 + gi * cw + cw / 2, Y0 + (p - 1) * ch + 45, "57–71" if p == 6 else "89–103", 22, MUT, "700")
# lantanider/aktinider
la = "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu".split(); ac = "Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr".split()
for i, s in enumerate(la): b += cell(X0 + (i + 2) * cw - 0, Y0 + 8.4 * ch, s) if False else cell(X0 + 2 * cw + i * cw * 0.86 - 0 if False else X0 + 1.5 * cw + i * cw * 0.99 - 0, Y0 + 8.3 * ch, s)
for i, s in enumerate(ac): b += cell(X0 + 1.5 * cw + i * cw * 0.99, Y0 + 9.3 * ch, s)
# legend + trappa
b += f'<rect x="{X0+3*cw}" y="{Y0+0.2*ch}" width="22" height="22" fill="#cfe0f3" stroke="#2f5f95" stroke-width="2"/>' + T(X0 + 3 * cw + 32, Y0 + 0.2 * ch + 19, "metall", 24, INK, "700", "start")
b += f'<rect x="{X0+3*cw}" y="{Y0+0.75*ch}" width="22" height="22" fill="#cfe9c6" stroke="#2e7d32" stroke-width="2"/>' + T(X0 + 3 * cw + 32, Y0 + 0.75 * ch + 19, "icke-metall", 24, INK, "700", "start")
b += f'<rect x="{X0+3*cw}" y="{Y0+1.3*ch}" width="22" height="22" fill="#fbe7a6" stroke="#9a7a10" stroke-width="2"/>' + T(X0 + 3 * cw + 32, Y0 + 1.3 * ch + 19, "halvmetall", 24, INK, "700", "start")
b += T(X0 + 8 * cw, 920, "De två nedre raderna är lantanider (57–71) och aktinider (89–103). Siffran i hörnet är atomnumret.", 22, MUT)
render('v_pse', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_skal
W, H = 1500, 560; b = ''
for i, (nm, sk, p, g) in enumerate([("Natrium (Na)", [2, 8, 1], 11, "grupp 1: 1 valenselektron"), ("Klor (Cl)", [2, 8, 7], 17, "grupp 17: 7 valenselektroner"), ("Neon (Ne)", [2, 8], 10, "grupp 18: 8 valenselektroner")]):
    cx = 250 + i * 500
    b += f'<rect x="{cx-235}" y="15" width="470" height="530" rx="20" fill="#fff" stroke="#e3d5d1" stroke-width="3"/>' + T(cx, 62, nm, 36, RED, "700")
    b += atom(cx, 270, 1, 0, sk, 12, 50, 55, 9, seed=2, rot=0.4).replace(nuc(cx, 270, 1, 0, 12, 2), f'<circle cx="{cx}" cy="270" r="22" fill="{PC}"/>' + T(cx, 279, str(p) + "+", 22, "#fff", "700"))
    b += T(cx, 470, "elektroner: " + ", ".join(map(str, sk)), 28, INK, "700") + T(cx, 512, g, 24, MUT)
render('v_skal', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_forekomst
W, H = 1500, 560; b = ''
def bars(x0, title, data, mx):
    s = T(x0 + 300, 60, title, 34, DRED, "700")
    for i, (nm, v, lab) in enumerate(data):
        y = 100 + i * 58
        s += T(x0 + 120, y + 30, nm, 28, INK, "700", "end") + f'<rect x="{x0+135}" y="{y}" width="{max(v/mx*480,4):.0f}" height="40" rx="6" fill="{RED}"/>' + T(x0 + 145 + v / mx * 480, y + 30, lab, 26, INK, "700", "start")
    return s
b += bars(20, "Jordskorpan (viktprocent)", [("Syre", 46.6, "46,6"), ("Kisel", 27.7, "27,7"), ("Aluminium", 8.1, "8,1"), ("Järn", 5.0, "5,0"), ("Kalcium", 3.6, "3,6"), ("Natrium", 2.8, "2,8"), ("Kalium", 2.6, "2,6"), ("Magnesium", 2.1, "2,1")], 48)
b += bars(770, "Människokroppen (ungefär)", [("Syre", 62, "ca 61–65"), ("Kol", 23, "ca 23"), ("Väte", 10, "ca 10"), ("Kväve", 2.6, "ca 3"), ("Kalcium", 1.5, "ca 1,5"), ("Fosfor", 1.1, "ca 1")], 65)
render('v_forekomst', svg(W, H, b, "#ffffff"), W, H, 1)

# ---- v_labb2 (krets)
W, H = 900, 520; b = ''
b += f'<rect x="120" y="190" width="90" height="140" rx="10" fill="#dfe4e8" stroke="{INK}" stroke-width="5"/>' + T(165, 270, "+", 42, RED, "700") + T(165, 318, "−", 40, INK, "700") + T(100, 370, "batteri", 26, INK, "700", "end")
b += f'<path d="M165,190 V90 H430 M165,330 V440 H730 V300" stroke="{INK}" stroke-width="6" fill="none"/>'
b += f'<circle cx="730" cy="240" r="60" fill="#fff6c2" stroke="{INK}" stroke-width="5"/><path d="M705,270 q25,-70 50,0" stroke="{INK}" stroke-width="5" fill="none"/>' + T(810, 250, "lampa", 26, INK, "700", "start")
b += f'<path d="M730,180 V90 H610" stroke="{INK}" stroke-width="6" fill="none"/>'
b += f'<rect x="430" y="68" width="180" height="44" rx="8" fill="#b9663a" stroke="{INK}" stroke-width="5"/>' + T(520, 52, "prov", 28, RED, "700") + T(520, 100, "", 10)
b += f'<circle cx="430" cy="90" r="9" fill="{INK}"/><circle cx="610" cy="90" r="9" fill="{INK}"/>'
b += T(450, 500, "Lyser lampan leder provet elektricitet", 28, DRED, "700")
render('v_labb2', svg(W, H, b, "#ffffff"), W, H, 1)
