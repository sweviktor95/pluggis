# -*- coding: utf-8 -*-
"""Kemi 3 – omslag, ikoner, fördjupnings- och provfigurer -> /tmp/kem/fig03k/"""
from kfig3_common import *
import mkkfig6 as M   # återanvänder atom/nuc/legend (renderar om v_-figurerna, ofarligt)
from mkkfig6 import atom, nuc, legend, PC, NC, EC, ARROW, order, Z, NONM, META, cat
RED_ = RED
# ---------- omslag ----------
def cover(variant):
    W, H = 1818, 759
    pal = {'v': ('#f8dcd6', '#fdf3ec', '#e6b3aa'), 'l': ('#fbe5d6', '#fef7ea', '#efc3ae'), 'f': ('#e9c4be', '#f7e7e0', '#c98a82')}[variant]
    rnd = random.Random({'v': 21, 'l': 22, 'f': 23}[variant])
    s = f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal[0]}"/><stop offset="1" stop-color="{pal[1]}"/></linearGradient></defs><rect width="{W}" height="{H}" fill="url(#sk)"/>'
    for _ in range(30):
        s += f'<circle cx="{rnd.randint(40, W-40)}" cy="{rnd.randint(40, 700)}" r="{rnd.randint(6, 18)}" fill="{rnd.choice([EC, PC, NC, "#e0873a"])}" opacity=".2"/>'
    s += f'<path d="M0,600 Q420,560 900,600 T1818,580 L1818,759 L0,759Z" fill="{pal[2]}" opacity=".55"/>'
    s += atom(330, 380, 6, 6, [2, 4], 20, 120, 80, 15, seed=4)
    s += atom(1500, 330, 11, 12, [2, 8, 1], 17, 100, 68, 13, seed=6)
    # periodiska systemet som kort
    syms = ["H", "He", "Li", "C", "N", "O", "Na", "Cl", "Fe", "Au"]
    for i, sy in enumerate(syms):
        x = 560 + (i % 5) * 150; y = 250 + (i // 5) * 160
        f, st = cat(sy)
        s += f'<rect x="{x}" y="{y}" width="130" height="140" rx="16" fill="{f}" stroke="{st}" stroke-width="4"/>' + T(x + 16, y + 34, Z.get(sy, 79), 26, MUT, "400", "start") + T(x + 65, y + 106, sy, 66, INK, "700")
    s += f'<rect x="38" y="38" width="190" height="46" rx="23" fill="#fff" opacity=".92"/>' + T(133, 70, "KAPITEL 3", 24, RED, "700")
    return svg(W, H, s, pal[0])
Z["Au"] = 79
for v, n in (('v', 'vanlig'), ('l', 'lattlast'), ('f', 'fordjupning')):
    render('cover_' + n, cover(v), 1818, 759, 1)

# ---------- ikoner ----------
def icon(name, body, bg="#fbe9e6"):
    render(name, svg(256, 256, f'<rect width="256" height="256" rx="40" fill="{bg}"/>' + body, bg), 256, 256, 2)
icon('l_ic1', atom(128, 110, 3, 4, [2, 1], 10, 50, 36, 8, seed=2) + T(128, 232, "atom", 32, DRED, "700"))
icon('l_ic2', f'<circle cx="70" cy="90" r="30" fill="{PC}"/>' + T(70, 102, "+", 36, "#fff", "700") + f'<circle cx="128" cy="90" r="30" fill="{NC}"/>' + T(128, 102, "0", 32, "#fff", "700") + f'<circle cx="186" cy="90" r="30" fill="{EC}"/>' + T(186, 102, "−", 38, "#fff", "700") + T(128, 160, "p n e", 34, INK, "700") + T(128, 232, "partiklar", 30, DRED, "700"))
icon('l_ic3', T(128, 90, "Z = p", 44, RED, "700") + T(128, 150, "A = p + n", 40, INK, "700") + T(128, 232, "atomnummer", 28, DRED, "700"))
icon('l_ic4', ''.join(f'<circle cx="{50+i*52}" cy="110" r="{r}" fill="{c}" stroke="{INK}" stroke-width="4"/>' for i, (r, c) in enumerate([(20, "#9aa7b0"), (20, "#f6c9c4"), (14, "#fff"), (22, "#fff")])) + f'<circle cx="154" cy="110" r="4" fill="{PC}"/>' + T(128, 190, "modeller", 30, INK, "700") + T(128, 232, "historia", 30, DRED, "700"))
icon('l_ic5', nuc(90, 100, 3, 3, 11, 2) + nuc(170, 100, 3, 4, 11, 3) + T(128, 180, "isotoper", 30, INK, "700") + T(128, 232, "strålning", 30, DRED, "700"))
icon('l_ic6', ''.join(f'<rect x="{38+c*36}" y="{50+r*34}" width="32" height="30" rx="5" fill="{["#cfe0f3","#cfe9c6","#fbe7a6"][(c+r)%3]}" stroke="{INK}" stroke-width="2"/>' for r in range(3) for c in range(6)) + T(128, 190, "periodiska", 28, INK, "700") + T(128, 232, "systemet", 28, DRED, "700"))
icon('l_ic7', atom(128, 100, 1, 0, [2, 7], 8, 30, 28, 8, seed=2).replace(nuc(128, 100, 1, 0, 8, 2), f'<circle cx="128" cy="100" r="12" fill="{PC}"/>') + T(128, 232, "valenselektroner", 26, DRED, "700"))

# ---------- fördjupningsfigurer ----------
W, H = 1200, 620; b = ARROW
b += f'<circle cx="400" cy="320" r="14" fill="{PC}"/>'
for r_, lab in [(80, "n = 1"), (150, "n = 2"), (230, "n = 3")]:
    b += f'<circle cx="400" cy="320" r="{r_}" fill="none" stroke="#b9c3ca" stroke-width="3"/>' + T(400 + r_ * 0.71 + 6, 320 - r_ * 0.71, lab, 22, MUT, "400", "start")
b += f'<circle cx="{400+230*math.cos(2.4):.0f}" cy="{320-230*math.sin(2.4):.0f}" r="13" fill="{EC}" stroke="#fff" stroke-width="3"/>'
b += f'<circle cx="{400+150*math.cos(1.1):.0f}" cy="{320-150*math.sin(1.1):.0f}" r="13" fill="#fff" stroke="{EC}" stroke-width="3" stroke-dasharray="4 3"/>'
b += f'<path d="M{400+230*math.cos(2.4)+10:.0f},{320-230*math.sin(2.4)+16:.0f} Q{400-20},{320-120} {400+150*math.cos(1.1)-16:.0f},{320-150*math.sin(1.1)-2:.0f}" fill="none" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>'
b += '<path d="M650,200 q20,-30 40,0 t40,0 t40,0 t40,0" fill="none" stroke="#e0873a" stroke-width="7"/>' + T(790, 150, "ljus sänds ut", 30, "#e0873a", "700")
b += T(940, 330, "Elektronen hoppar", 30, INK, "700") + T(940, 366, "till en bana med", 30, INK, "700") + T(940, 402, "lägre energi", 30, INK, "700")
b += T(600, 52, "Bohrs modell för väte (schematisk)", 36, DRED, "700")
render('f_bohr', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1400, 560; b = ARROW
b += T(350, 50, "Fission: tung kärna delas", 34, DRED, "700") + T(1050, 50, "Fusion: lätta kärnor slås ihop", 34, DRED, "700")
b += f'<circle cx="70" cy="260" r="12" fill="{NC}"/><path d="M90,260 H160" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>' + nuc(230, 260, 6, 8, 20, 4) + f'<path d="M340,260 H420" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>'
b += nuc(500, 170, 3, 4, 17, 2) + nuc(520, 360, 3, 4, 17, 5) + f'<circle cx="610" cy="250" r="12" fill="{NC}"/><circle cx="620" cy="310" r="12" fill="{NC}"/>' + T(520, 470, "två mindre kärnor + neutroner", 26, INK, "700") + T(520, 510, "+ energi", 30, "#e0873a", "700")
b += T(230, 360, "tung kärna", 26, INK, "700")
b += nuc(850, 200, 1, 0, 18, 1) + nuc(850, 330, 1, 1, 18, 2) + f'<path d="M900,265 H990" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>' + nuc(1090, 265, 2, 2, 18, 3) + T(850, 400, "två lätta kärnor", 26, INK, "700") + T(1090, 340, "tyngre kärna", 26, INK, "700") + T(1090, 510, "+ energi", 30, "#e0873a", "700")
b += f'<path d="M700,60 V540" stroke="#e3d5d1" stroke-width="4" stroke-dasharray="10 8"/>'
render('f_fission', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1100, 650; X0, Y0, X1, Y1 = 150, 520, 1040, 90; b = f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
def px(t): return X0 + t / 40 * (X1 - X0 - 40)
def py(m): return Y0 - m / 80 * (Y0 - Y1 - 20)
pts = " ".join(f"{px(t):.0f},{py(80*0.5**(t/10)):.0f}" for t in [i * 0.5 for i in range(0, 81)])
b += f'<polyline points="{pts}" fill="none" stroke="{RED}" stroke-width="7"/>'
for t in (0, 10, 20, 30, 40):
    m = 80 * 0.5 ** (t / 10)
    b += f'<path d="M{px(t):.0f},{Y0} v12" stroke="{INK}" stroke-width="4"/>' + T(px(t), Y0 + 44, str(t), 28, INK, "700")
    b += f'<circle cx="{px(t):.0f}" cy="{py(m):.0f}" r="10" fill="#fff" stroke="{RED}" stroke-width="5"/>' + T(px(t) + 16, py(m) - 14, f"{m:g} g".replace(".", ","), 28, RED, "700", "start")
b += f'<g transform="translate(52,310) rotate(-90)">{T(0, 0, "Kvar av ämnet (g)", 28, INK, "700")}</g>' + T(595, 620, "Tid (år)", 28, INK, "700") + T(560, 50, "Sönderfall, halveringstid 10 år (påhittat ämne)", 34, DRED, "700")
render('f_sonderfall', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1200, 520; cw, chh = 120, 90; b = T(600, 46, "Tabell med tomma platser (schematiskt)", 34, DRED, "700")
for r in range(4):
    for c in range(8):
        x = 80 + c * cw; y = 80 + r * chh; gap = (r, c) in [(2, 5), (3, 3), (3, 6)]
        if gap: b += f'<rect x="{x+4}" y="{y+4}" width="{cw-8}" height="{chh-8}" rx="10" fill="#fff" stroke="{RED}" stroke-width="4" stroke-dasharray="9 6"/>' + T(x + cw / 2, y + 62, "?", 52, RED, "700")
        else: b += f'<rect x="{x+4}" y="{y+4}" width="{cw-8}" height="{chh-8}" rx="10" fill="#cfe0f3" stroke="#2f5f95" stroke-width="2.5"/>' + T(x + cw / 2, y + 60, "ämne", 28, INK, "700")
b += T(600, 480, "Mendelejev lämnade tomma platser och förutsade egenskaper utifrån grannarna", 28, INK, "700")
render('f_mendelejev', svg(W, H, b, "#ffffff"), W, H, 1)

# f_sallsynta
rows = M.rows; W, H = 1600, 790; cw, ch = 78, 70; X0, Y0 = 80, 70; b = T(800, 40, "De 17 sällsynta jordartsmetallerna", 34, DRED, "700")
LA = set("La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu".split()); SP = LA | {"Sc", "Y"}
def cell2(x, y, s):
    on = s in SP
    return f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" rx="7" fill="{"#f3b9b2" if on else "#eef1f3"}" stroke="{"#a8322a" if on else "#c3ccd2"}" stroke-width="{3 if on else 2}"/>' + T(x + cw / 2, y + 50, s, 30, INK if on else MUT, "700")
for p, rw in rows.items():
    for gi, s in enumerate(rw):
        if s and not (s in ('La', 'Ac') and p in (6, 7)): b += cell2(X0 + gi * cw, Y0 + (p - 1) * ch, s)
        elif s: b += f'<rect x="{X0+gi*cw+2}" y="{Y0+(p-1)*ch+2}" width="{cw-4}" height="{ch-4}" rx="7" fill="#fff" stroke="#a8322a" stroke-width="2.5" stroke-dasharray="5 4"/>' + T(X0 + gi * cw + cw / 2, Y0 + (p - 1) * ch + 44, "57–71" if p == 6 else "89–103", 21, MUT, "700")
for i, s in enumerate("La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu".split()): b += cell2(X0 + 1.5 * cw + i * cw * 0.99, Y0 + 8.2 * ch, s)
b += T(X0 + 1.5 * cw + 7 * cw * 0.99 + 38, Y0 + 8.2 * ch - 12, "lantaniderna (57–71)", 24, RED, "700")
render('f_sallsynta', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1200, 400; b = T(600, 46, "Universums sammansättning (andel av massan, avrundat)", 34, DRED, "700")
b += f'<rect x="80" y="110" width="{1040*0.98:.0f}" height="90" rx="10" fill="#6fa8d6"/><rect x="{80+1040*0.98:.0f}" y="110" width="{1040*0.02:.0f}" height="90" fill="{RED}"/>'
b += T(560, 168, "väte och helium: ca 98 %", 38, "#fff", "700") + f'<path d="M{80+1040*0.99:.0f},205 V260" stroke="{RED}" stroke-width="4"/>' + T(1090, 300, "alla tyngre grundämnen: ca 2 %", 30, RED, "700", "end")
b += T(600, 370, "Tyngre grundämnen har bildats genom fusion i stjärnor", 28, INK, "700")
render('f_rymd', svg(W, H, b, "#ffffff"), W, H, 1)

# ---------- provfigurer ----------
W, H = 700, 560; b = atom(350, 280, 7, 7, [2, 5], 16, 90, 70, 13, seed=8) + legend(40, 535, 22, 220)
render('p_atom', svg(W, H, b, "#ffffff"), W, H, 1)
W, H = 1000, 600; X0, Y0, X1, Y1 = 130, 500, 960, 70; b = f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
def qx(t): return X0 + t / 20 * (X1 - X0 - 40)
def qy(m): return Y0 - m / 80 * (Y0 - Y1 - 20)
b += f'<polyline points="' + " ".join(f"{qx(t/2):.0f},{qy(80*0.5**(t/10)):.0f}" for t in range(0, 41)) + f'" fill="none" stroke="{RED}" stroke-width="7"/>'
for t in (0, 5, 10, 15, 20): b += f'<path d="M{qx(t):.0f},{Y0} v12" stroke="{INK}" stroke-width="4"/>' + T(qx(t), Y0 + 44, str(t), 28, INK, "700")
for m in (0, 20, 40, 60, 80): b += f'<path d="M{X0-10},{qy(m):.0f} H{X1}" stroke="#e6d9d5" stroke-width="2"/>' + T(X0 - 18, qy(m) + 9, str(m), 26, INK, "400", "end")
b += f'<g transform="translate(40,300) rotate(-90)">{T(0, 0, "Kvar av ämnet (g)", 26, INK, "700")}</g>' + T(550, 585, "Tid (år)", 26, INK, "700")
render('p_kurva', svg(W, H, b, "#ffffff"), W, H, 1)
rows3 = {2: ["Li", "Be", "B", "C", "N", "O", "F", "Ne"], 3: ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"], 4: ["K", "Ca", "Ga", "Ge", "As", "Se", "Br", "Kr"]}
grp = ["1", "2", "13", "14", "15", "16", "17", "18"]
W, H = 900, 480; cw, ch = 96, 90; b = ''
for i, g in enumerate(grp): b += T(110 + i * cw + cw / 2, 56, "grupp " + g, 20, MUT, "700")
for r, (p, rw) in enumerate(rows3.items()):
    b += T(70, 80 + r * ch + 56, str(p), 26, MUT, "700")
    for i, s in enumerate(rw):
        x = 110 + i * cw; y = 80 + r * ch; mark = s in ("Na", "K", "Ne")
        f, st = cat(s)
        b += f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" rx="9" fill="{"#ffe08a" if mark else f}" stroke="{"#a8322a" if mark else st}" stroke-width="{5 if mark else 2}"/>' + T(x + cw / 2, y + 56, s, 38, INK, "700")
b += T(450, 400, "Markerade: Na, K och Ne", 28, RED, "700") + T(60, 30, "period", 20, MUT, "700", "start")
render('p_pse', svg(W, H, b, "#ffffff"), W, H, 1)
