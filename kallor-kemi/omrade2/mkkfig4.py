# -*- coding: utf-8 -*-
"""Kemi 2 – grundtextens figurer -> /tmp/kem/fig02k/"""
from kfig2_common import *

BLUE = "#6fa8d6"; LBLUE = "#cfe6f5"; ORG = "#e0873a"; GRN = "#6dae6a"; BRN = "#a9824f"; SALT = "#9b6fc4"

def scatter(x, y, w, h, n, r, gap=2.0, seed=1, avoid=None):
    rnd = random.Random(seed); pts = []; tries = 0
    while len(pts) < n and tries < 20000:
        tries += 1
        px = rnd.uniform(x + r + 3, x + w - r - 3); py = rnd.uniform(y + r + 3, y + h - r - 3)
        if all((px - a) ** 2 + (py - b) ** 2 >= (2 * r + gap) ** 2 for a, b in pts): pts.append((px, py))
    return pts
def dots(pts, r, col, sw=2):
    return ''.join(f'<circle cx="{a:.0f}" cy="{b:.0f}" r="{r}" fill="{col}" stroke="#fff" stroke-width="{sw}"/>' for a, b in pts)
def pbox(x, y, w, h, fill="#fff"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{LINE}" stroke-width="4"/>'
def grid(x, y, cols, rows, r, col, dx=None, dy=None, jitter=0, seed=1):
    rnd = random.Random(seed); dx = dx or 2 * r + 3; dy = dy or 2 * r + 3
    return [(x + c * dx + rnd.uniform(-jitter, jitter), y + rr * dy + rnd.uniform(-jitter, jitter)) for rr in range(rows) for c in range(cols)]
def arrow(x1, y1, x2, y2, col=MUT, sw=4):
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{col}" stroke-width="{sw}" fill="none" marker-end="url(#ah)"/>'
def vib(x, y, col=MUT):  # liten vibrationsmarkering
    return f'<path d="M{x-9},{y-14} q4,-6 8,0 q4,6 8,0" stroke="{col}" stroke-width="2.4" fill="none"/>'
def mover(x, y, dx, dy, col=MUT):
    return f'<path d="M{x},{y} l{dx},{dy}" stroke="{col}" stroke-width="3.2" marker-end="url(#ah2)" fill="none"/>'

def solid_box(x, y, w, h, r=13, col=BLUE):
    cols = int((w - 30) // (2 * r + 3)); rows = int((h - 30) // (2 * r + 3))
    pts = grid(x + 22, y + 24, cols, rows, r, col)
    return dots(pts, r, col)
def liquid_box(x, y, w, h, r=13, col=BLUE, seed=4):
    n = int((w - 20) * (h - 20) / ((2 * r + 3.5) ** 2) * 0.66)
    return dots(scatter(x + 8, y + 8, w - 16, h - 16, n, r, 1.5, seed), r, col)
def gas_box(x, y, w, h, r=13, col=BLUE, seed=7, n=9):
    pts = scatter(x + 10, y + 10, w - 20, h - 20, n, r, 40, seed); rnd = random.Random(seed)
    o = dots(pts, r, col)
    for (a, b) in pts:
        ang = rnd.uniform(0, 6.28); L = rnd.uniform(26, 38)
        o += mover(a + r * math.cos(ang), b + r * math.sin(ang), L * math.cos(ang), L * math.sin(ang))
    return o

# ---------- v_partikel --------------------------------------------------------
W, H = 1500, 620
b = ''
for i, (name, sub) in enumerate([("Fast", "Tätt, ordnat. Vibrerar på plats."), ("Vätska", "Nära, oordnat. Glider förbi varandra."), ("Gas", "Långt isär. Rör sig snabbt åt alla håll.")]):
    x0 = 40 + i * 480
    b += card(x0, 20, 440, 580, "#fff") + T(x0 + 220, 72, name, 44, DRED, "700")
    bx, by, bw, bh = x0 + 50, 110, 340, 340
    b += pbox(bx, by, bw, bh, "#f7fbfe")
    if i == 0:
        b += solid_box(bx, by, bw, bh)
    elif i == 1: b += liquid_box(bx, by, bw, bh)
    else: b += gas_box(bx, by, bw, bh, 13, BLUE, 7, 8)
    b += T(x0 + 220, 500, sub.split('. ')[0] + '.', 28, INK, "700") + T(x0 + 220, 540, sub.split('. ')[1], 28, MUT)
render('v_partikel', svg(W, H, b, BG), W, H, 1)

# ---------- v_oversikt --------------------------------------------------------
W, H = 1500, 640
b = ''
for i, (name, what) in enumerate([("Fast (is)", "ice"), ("Flytande (vatten)", "wat"), ("Gas (vattenånga)", "gas")]):
    x0 = 40 + i * 480
    b += card(x0, 20, 440, 600, "#fff") + T(x0 + 220, 70, name, 40, DRED, "700")
    cx = x0 + 220
    if what == "ice":
        b += f'<path d="M{cx-70},170 l30,-30 h110 l-10,10 v90 l-30,30 h-100z" fill="#dff1fb" stroke="#8fb7d3" stroke-width="5" stroke-linejoin="round"/><rect x="{cx-100}" y="150" width="110" height="110" rx="6" fill="#e9f6fd" stroke="#8fb7d3" stroke-width="5"/><path d="M{cx-86},166 l24,-4" stroke="#fff" stroke-width="8" stroke-linecap="round"/>'
    elif what == "wat":
        b += beaker(cx - 70, 125, 140, 150, 0.6, "#a8d2ee", False)
    else:
        for k in range(4):
            b += f'<path d="M{cx-60+k*40},250 q-20,-30 0,-55 q20,-25 0,-55 q-14,-20 6,-40" stroke="#b9c9d3" stroke-width="9" fill="none" stroke-linecap="round" opacity=".85"/>'
        b += f'<rect x="{cx-100}" y="252" width="200" height="20" rx="8" fill="#cdbdb8"/>'
    bx, by, bw, bh = x0 + 70, 320, 300, 270
    b += pbox(bx, by, bw, bh, "#f7fbfe")
    if i == 0: b += solid_box(bx, by, bw, bh, 12)
    elif i == 1: b += liquid_box(bx, by, bw, bh, 12, BLUE, 5)
    else: b += gas_box(bx, by, bw, bh, 12, BLUE, 3, 6)
render('v_oversikt', svg(W, H, b, BG), W, H, 1)

# ---------- v_tillstand -------------------------------------------------------
W, H = 1500, 720
b = ''
cxs = [200, 750, 1300]
names = ["Fast", "Flytande", "Gas"]
for i, cx in enumerate(cxs):
    b += card(cx - 170, 250, 340, 330, "#fff") + T(cx, 300, names[i], 40, DRED, "700")
    bx, by, bw, bh = cx - 130, 330, 260, 230
    b += pbox(bx, by, bw, bh, "#f7fbfe")
    if i == 0: b += solid_box(bx, by, bw, bh, 11)
    elif i == 1: b += liquid_box(bx, by, bw, bh, 11, BLUE, 6)
    else: b += gas_box(bx, by, bw, bh, 11, BLUE, 11, 6)
def pair(xa, xb, y, up, down):
    o = f'<path d="M{xa},{y-10} H{xb}" stroke="{RED}" stroke-width="4" marker-end="url(#ah)"/>'
    o += f'<path d="M{xb},{y+24} H{xa}" stroke="#2f6aa3" stroke-width="4" marker-end="url(#ah)"/>'
    o += T((xa + xb) / 2, y - 26, up, 30, RED, "700") + T((xa + xb) / 2, y + 62, down, 30, "#2f6aa3", "700")
    return o
b += pair(cxs[0] + 180, cxs[1] - 180, 415, "smältning", "stelning")
b += pair(cxs[1] + 180, cxs[2] - 180, 415, "förångning", "kondensation")
b += f'<path d="M{cxs[0]},238 C{cxs[0]},110 {cxs[2]},110 {cxs[2]},238" stroke="{ORG}" stroke-width="4" fill="none" marker-end="url(#ah)"/>' + T(750, 128, "sublimering (fast till gas direkt)", 32, ORG, "700")
b += T(750, 650, "Röda pilar: värme tillförs. Blå pilar: värme avges.", 30, MUT)
render('v_tillstand', svg(W, H, b, BG), W, H, 1)

# ---------- v_diffusion -------------------------------------------------------
W, H = 1500, 700
b = ''
RD = "#d9534a"
for i, lab in enumerate(["Strax efter droppen", "Efter en stund", "Till slut"]):
    x0 = 40 + i * 480
    b += card(x0, 20, 440, 660, "#fff") + T(x0 + 220, 70, lab, 36, DRED, "700")
    b += beaker(x0 + 110, 100, 220, 230, 0.75, "#cfe6f5", False)
    if i == 0:
        b += f'<ellipse cx="{x0+220}" cy="165" rx="28" ry="34" fill="{RD}" opacity=".85"/>'
    elif i == 1:
        b += f'<ellipse cx="{x0+220}" cy="215" rx="70" ry="85" fill="{RD}" opacity=".35"/><ellipse cx="{x0+220}" cy="200" rx="38" ry="48" fill="{RD}" opacity=".35"/>'
    else:
        b += f'<path d="M{x0+116},150 L{x0+324},150 L{x0+324},315 Q{x0+324},322 {x0+316},322 L{x0+124},322 Q{x0+116},322 {x0+116},315Z" fill="{RD}" opacity=".28"/>'
    bx, by, bw, bh = x0 + 40, 370, 360, 280
    b += pbox(bx, by, bw, bh, "#f7fbfe")
    water = scatter(bx + 6, by + 6, bw - 12, bh - 12, 62, 11, 2, 20 + i)
    rnd = random.Random(i + 3); red = []; bl = []
    for k, (a, c) in enumerate(water):
        if i == 0: isred = (abs(a - (bx + bw / 2)) < 60 and c < by + 100 and len(red) < 9)
        elif i == 1: isred = ((a - (bx + bw / 2)) ** 2 / 150 ** 2 + (c - (by + 110)) ** 2 / 110 ** 2 < 1) and rnd.random() < 0.6
        else: isred = rnd.random() < 0.15
        (red if isred else bl).append((a, c))
    b += dots(bl, 11, "#9fc8e6") + dots(red, 11, RD)
b += T(750, 696, "", 1)
render('v_diffusion', svg(W, H, b, BG), W, H, 1)

# ---------- v_blandning -------------------------------------------------------
W, H = 1500, 640
b = ''
labs = [("Rent ämne", "Bara en sorts partikel."), ("Homogen blandning", "Lösning: partiklarna är jämnt blandade."), ("Heterogen blandning", "Delarna syns: sand i vatten.")]
for i, (nm, sub) in enumerate(labs):
    x0 = 40 + i * 480
    b += card(x0, 20, 440, 600, "#fff") + T(x0 + 220, 70, nm, 40, DRED, "700")
    bx, by, bw, bh = x0 + 50, 110, 340, 340
    b += pbox(bx, by, bw, bh, "#f7fbfe")
    if i == 0:
        b += dots(scatter(bx, by, bw, bh, 52, 13, 2, 31), 13, ORG)
    elif i == 1:
        pts = scatter(bx, by, bw, bh, 56, 13, 2, 32); rnd = random.Random(9)
        sol = [p for p in pts if rnd.random() < 0.3]; rest = [p for p in pts if p not in sol]
        b += dots(rest, 13, "#9fc8e6") + dots(sol, 13, SALT)
    else:
        pts = scatter(bx + 6, by + 6, bw - 12, bh - 12, 36, 11, 2, 33)
        water = [p for p in pts if p[1] < by + 215 or False]
        b += dots(pts, 11, "#9fc8e6")
        rnd = random.Random(5)
        for k in range(9):
            gx = bx + 58 + (k % 3) * 100 + rnd.uniform(-8, 8); gy = by + 238 + (k // 3) * 32 + rnd.uniform(-4, 4)
            b += f'<polygon points="{gx-30:.0f},{gy:.0f} {gx-14:.0f},{gy-22:.0f} {gx+14:.0f},{gy-24:.0f} {gx+32:.0f},{gy-2:.0f} {gx+10:.0f},{gy+16:.0f} {gx-16:.0f},{gy+16:.0f}" fill="{BRN}" stroke="#fff" stroke-width="2"/>'
    b += T(x0 + 220, 500, sub, 26, INK, "700")
    leg = {0: [(ORG, "ett ämne")], 1: [("#9fc8e6", "vatten"), (SALT, "löst ämne")], 2: [("#9fc8e6", "vatten"), (BRN, "sandkorn")]}[i]
    for k, (c, t) in enumerate(leg):
        b += f'<circle cx="{x0+90+k*170}" cy="550" r="13" fill="{c}"/>' + T(x0 + 112 + k * 170, 560, t, 26, MUT, "400", "start")
render('v_blandning', svg(W, H, b, BG), W, H, 1)

# ---------- v_vattenforskj -----------------------------------------------------
W, H = 1100, 640
b = ''
cy0, ch = 100, 420; cw = 70
for k, (x0, vol, with_m) in enumerate([(210, 50, False), (700, 70, True)]):
    b += cylinder(x0, cy0, cw, ch, vol / 100, "#bcd9ec", 10)
    ly = cy0 + ch * (1 - vol / 100)
    b += f'<path d="M{x0+cw+20},{ly} H{x0+cw+130}" stroke="{RED}" stroke-width="5" marker-start="url(#ah)"/>' if False else ''
    b += f'<path d="M{x0+cw+12},{ly} h60" stroke="{RED}" stroke-width="5"/>' + T(x0 + cw + 80, ly + 10, f"{vol} ml", 34, RED, "700", "start")
    if with_m:
        b += f'<rect x="{x0+16}" y="{cy0+ch-92}" width="{cw-32}" height="88" rx="8" fill="#9aa7b0" stroke="#5d6b75" stroke-width="4"/><path d="M{x0+26},{cy0+ch-80} v40" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".6"/>'
b += T(245, 590, "Före", 36, DRED, "700") + T(735, 590, "Efter: metallstycket nere i vattnet", 34, DRED, "700")
b += T(550, 330, "→", 90, MUT, "700")
b += f'<rect x="395" y="130" width="290" height="104" rx="18" fill="#fff" stroke="{LINE}" stroke-width="3"/>' + T(540, 172, "Volym = 70 ml − 50 ml", 30, INK, "700") + T(540, 214, "= 20 ml = 20 cm³", 30, DRED, "700")
render('v_vattenforskj', svg(W, H, b, BG), W, H, 1)

# ---------- v_flyta -----------------------------------------------------------
W, H = 1500, 660
b = ''
# vänster glas: olja på vatten
b += card(20, 20, 700, 620, "#fff") + T(370, 68, "Olja på vatten", 38, DRED, "700")
gx, gy, gw, gh = 235, 120, 270, 380
b += f'<path d="M{gx-8},{gy-6} L{gx},{gy} L{gx},{gy+gh-10} Q{gx},{gy+gh} {gx+12},{gy+gh} L{gx+gw-12},{gy+gh} Q{gx+gw},{gy+gh} {gx+gw},{gy+gh-10} L{gx+gw},{gy} L{gx+gw+8},{gy-6}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="6" stroke-linejoin="round"/>'
b += f'<path d="M{gx+4},{gy+150} H{gx+gw-4} V{gy+gh-10} Q{gx+gw-4},{gy+gh-4} {gx+gw-12},{gy+gh-4} H{gx+16} Q{gx+4},{gy+gh-4} {gx+4},{gy+gh-12}Z" fill="#a8d2ee" opacity=".92"/>'
b += f'<rect x="{gx+4}" y="{gy+80}" width="{gw-8}" height="70" fill="#f1d36a" opacity=".92"/>'
b += T(gx + gw + 24, gy + 125, "Olivolja 0,91", 30, INK, "700", "start") + T(gx + gw + 24, gy + 300, "Vatten 1,0", 30, INK, "700", "start")
b += T(370, 575, "Lägre densitet flyter överst.", 28, MUT) + T(370, 610, "(g/cm³)", 26, MUT)
# höger glas: is och bult
b += card(760, 20, 720, 620, "#fff") + T(1120, 68, "Is och järnbult i vatten", 38, DRED, "700")
gx = 960
b += f'<path d="M{gx-8},{gy-6} L{gx},{gy} L{gx},{gy+gh-10} Q{gx},{gy+gh} {gx+12},{gy+gh} L{gx+gw-12},{gy+gh} Q{gx+gw},{gy+gh} {gx+gw},{gy+gh-10} L{gx+gw},{gy} L{gx+gw+8},{gy-6}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="6" stroke-linejoin="round"/>'
b += f'<path d="M{gx+4},{gy+90} H{gx+gw-4} V{gy+gh-10} Q{gx+gw-4},{gy+gh-4} {gx+gw-12},{gy+gh-4} H{gx+16} Q{gx+4},{gy+gh-4} {gx+4},{gy+gh-12}Z" fill="#a8d2ee" opacity=".92"/>'
b += f'<rect x="{gx+80}" y="{gy+62}" width="110" height="80" rx="10" fill="#e9f6fd" stroke="#8fb7d3" stroke-width="5"/><path d="M{gx+92},{gy+78} h40" stroke="#fff" stroke-width="8" stroke-linecap="round"/>'
b += f'<g transform="translate({gx+gw/2},{gy+gh-30})"><rect x="-8" y="-28" width="16" height="50" fill="#7c8790" stroke="#4a545c" stroke-width="3"/><rect x="-18" y="-40" width="36" height="16" rx="4" fill="#7c8790" stroke="#4a545c" stroke-width="3"/></g>'
b += T(gx - 24, gy + 118, "Is 0,92", 30, INK, "700", "end") + T(gx - 24, gy + 335, "Järn 7,8", 30, INK, "700", "end")
b += T(1120, 575, "Lägre än 1,0 flyter. Högre sjunker.", 28, MUT) + T(1120, 610, "(g/cm³)", 26, MUT)
render('v_flyta', svg(W, H, b, BG), W, H, 1)

# ---------- v_labb1 -----------------------------------------------------------
W, H = 1500, 640
b = ''
for i, ttl in enumerate(["1 Massa", "2 Volym före", "3 Volym efter"]):
    x0 = 30 + i * 345
    b += card(x0, 20, 325, 600, "#fff") + T(x0 + 162, 66, ttl, 36, DRED, "700")
b += balance(60, 300, 260, "27,0 g", 42)
b += f'<rect x="150" y="250" width="80" height="44" rx="8" fill="#9aa7b0" stroke="#5d6b75" stroke-width="4"/>'
b += cylinder(470, 130, 62, 400, 0.5, "#bcd9ec", 10) + T(560, 340, "50 ml", 30, RED, "700", "start")
b += cylinder(815, 130, 62, 400, 0.6, "#bcd9ec", 10) + T(905, 290, "60 ml", 30, RED, "700", "start")
b += f'<rect x="827" y="{130+400-60}" width="38" height="56" rx="6" fill="#9aa7b0" stroke="#5d6b75" stroke-width="3"/>'
b += card(1060, 20, 410, 600, "#fffaf0") + T(1265, 66, "4 Räkna", 36, DRED, "700")
b += T(1265, 170, "Volym:", 30, INK, "700") + T(1265, 214, "60 − 50 = 10 cm³", 30, INK)
b += T(1265, 300, "Densitet:", 30, INK, "700") + T(1265, 346, "27,0 g / 10 cm³", 30, INK) + T(1265, 400, "= 2,7 g/cm³", 38, RED, "700")
b += T(1265, 480, "2,7 är mer än 1,0.", 28, MUT) + T(1265, 520, "Förutsägelse: sjunker.", 28, MUT, "700")
b += T(1265, 590, "Värdena är påhittade.", 24, MUT, "400", "middle", True)
render('v_labb1', svg(W, H, b, BG), W, H, 1)

# ---------- v_filtrering -------------------------------------------------------
W, H = 1100, 700
b = ''
b += f'<path d="M290,70 H650 L520,330 H420Z" fill="#f2f7fa" fill-opacity=".8" stroke="{LINE}" stroke-width="6" stroke-linejoin="round"/>'
b += f'<path d="M300,76 H640 L510,326 H430Z" fill="none"/>'
b += f'<path d="M306,92 L470,330 L634,92" fill="#fffdf4" stroke="#d8c78b" stroke-width="4" opacity=".9"/>'
b += f'<path d="M330,130 L470,330 L610,130Z" fill="#cfe6f5" opacity=".9"/>'
b += dots([(400, 190), (438, 220), (475, 236), (512, 224), (548, 196), (430, 178), (470, 190), (505, 180), (460, 262)], 9, BRN)
b += f'<rect x="440" y="326" width="60" height="70" fill="#f2f7fa" fill-opacity=".8" stroke="{LINE}" stroke-width="5"/>'
b += f'<path d="M470,400 v46 M470,470 v18" stroke="#8fc3e6" stroke-width="7" stroke-linecap="round" stroke-dasharray="14 14"/>'
b += beaker(350, 440, 240, 200, 0.4, "#cfe6f5", False)
b += dots(scatter(362, 560, 216, 60, 5, 6, 8, 3), 6, SALT, 1)
b += T(470, 56, "Tratt med filterpapper", 30, INK, "700")
b += f'<path d="M280,230 H340" stroke="{MUT}" stroke-width="3"/>' if False else ''
b += T(220, 215, "Residu:", 30, DRED, "700", "end") + T(220, 250, "sand", 30, INK, "400", "end")
b += f'<path d="M232,226 L392,200" stroke="{MUT}" stroke-width="3" marker-end="url(#ah)"/>'
b += T(850, 540, "Filtrat:", 30, DRED, "700", "start") + T(850, 576, "saltvatten", 30, INK, "400", "start")
b += f'<path d="M840,556 L600,560" stroke="{MUT}" stroke-width="3" marker-end="url(#ah)"/>'
b += T(700, 150, "Saltet är löst i vattnet.", 28, MUT, "400", "start") + T(700, 186, "Partiklarna är mycket", 28, MUT, "400", "start") + T(700, 222, "mindre än hålen i", 28, MUT, "400", "start") + T(700, 258, "pappret och går igenom.", 28, MUT, "400", "start")
render('v_filtrering', svg(W, H, b, BG), W, H, 1)

# ---------- v_flode -----------------------------------------------------------
W, H = 1500, 520
b = ''
def node(x, y, w, h, t1, t2="", fill="#fff", stroke=LINE):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{fill}" stroke="{stroke}" stroke-width="4"/>' + T(x + w / 2, y + h / 2 + (-6 if t2 else 10), t1, 32, INK, "700")
    if t2: o += T(x + w / 2, y + h / 2 + 32, t2, 26, MUT)
    return o
b += node(30, 195, 290, 120, "Sand, salt", "och vatten", "#fbf3f1", RED)
b += node(440, 195, 250, 120, "Filtrering")
b += node(840, 60, 270, 110, "Sand", "(residu)", "#f3ead8")
b += node(840, 340, 270, 120, "Saltvatten", "(filtrat)", "#e3f1fa")
b += node(1200, 340, 270, 120, "Indunstning")
b += node(1200, 60, 270, 110, "Salt", "(fast ämne)", "#efe6f7")
b += arrow(320, 255, 436, 255) + arrow(690, 230, 836, 130) + arrow(690, 280, 836, 390) + arrow(1110, 400, 1196, 400)
b += arrow(1335, 336, 1335, 176)
b += T(1170, 250, "ångan försvinner", 24, MUT, "400", "middle", True)
render('v_flode', svg(W, H, b, BG), W, H, 1)

# ---------- v_destillation ----------------------------------------------------
W, H = 1500, 800
b = ''
# värmeplatta
b += f'<rect x="90" y="600" width="330" height="40" rx="10" fill="#8b8f93" stroke="#4a545c" stroke-width="4"/><rect x="104" y="580" width="302" height="22" rx="6" fill="#d85a3a"/>'
b += T(255, 680, "Värmeplatta", 28, MUT)
# rundkolv
b += f'<circle cx="255" cy="460" r="115" fill="#f2f7fa" fill-opacity=".8" stroke="{LINE}" stroke-width="6"/><path d="M215,358 V280 H295 V358" fill="#f2f7fa" fill-opacity=".8" stroke="{LINE}" stroke-width="6"/>'
b += f'<path d="M142,470 A113,113 0 0 0 368,470Z" fill="#cfe6f5" opacity=".92"/>'
b += dots([(210, 520), (250, 535), (295, 520), (230, 565)], 9, SALT, 1)
for (x, y, r) in [(240, 480, 7), (280, 470, 6), (262, 440, 5)]: b += bubble(x, y, r)
b += f'<rect x="206" y="262" width="100" height="26" rx="6" fill="#c9a06b" stroke="#7a5a2a" stroke-width="3"/>'
# termometer
b += f'<rect x="240" y="120" width="24" height="150" rx="8" fill="#fff" stroke="{LINE}" stroke-width="4"/><rect x="247" y="190" width="10" height="80" fill="#d63a2e"/>'
b += T(325, 160, "Termometer", 28, INK, "700", "start")
# böjt rör till kylare
b += f'<path d="M256,270 L256,240 Q256,215 285,215 L520,215" fill="none" stroke="{LINE}" stroke-width="14" stroke-linecap="round" opacity=".5"/>'
b += f'<path d="M256,270 L256,240 Q256,215 285,215 L520,215" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
# kylare
b += f'<g transform="translate(500,215) rotate(18)"><rect x="0" y="-45" width="520" height="90" rx="26" fill="#e3f1fa" stroke="{LINE}" stroke-width="6"/><rect x="-60" y="-8" width="640" height="16" rx="8" fill="#fff" stroke="{LINE}" stroke-width="4"/>'
b += f'<path d="M60,45 v34 M440,-45 v-34" stroke="{LINE}" stroke-width="10" stroke-linecap="round"/></g>'
b += T(830, 215, "Kylare", 32, INK, "700")
b += T(1060, 190, "kallt vatten ut", 26, "#2f6aa3", "700", "start") if False else ''
b += f'<path d="M730,200 L730,150" stroke="#2f6aa3" stroke-width="5" marker-end="url(#ah)"/>' if False else ''
b += T(620, 520, "kallt vatten in", 26, "#2f6aa3", "700") + T(955, 205, "vatten ut", 26, "#2f6aa3", "700") if False else ''
# uppsamling
b += f'<path d="M960,450 L920,458" stroke="none"/>'
b += beaker(970, 520, 170, 160, 0.3, "#cfe6f5", False)
b += f'<path d="M1052,404 v110" stroke="#8fc3e6" stroke-width="7" stroke-linecap="round" stroke-dasharray="12 12"/>'
b += T(1230, 560, "Rent vatten", 30, DRED, "700") + T(1230, 706, "(destillat)", 26, MUT)
b += T(255, 580, "", 1)
b += T(750, 740, "1. Blandningen värms. Det med lägst kokpunkt blir gas först.", 28, INK, "700")
b += T(750, 776, "2. Gasen kyls i kylaren och blir vätska igen. 3. Vätskan samlas upp.", 28, MUT)
b += T(125, 410, "Saltvatten", 28, INK, "700", "end")
render('v_destillation', svg(W, H, b, BG), W, H, 1)

# ---------- v_kromatografi ----------------------------------------------------
W, H = 1500, 700
b = ''
def paper(x, y, w, h, bands, wet):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#fffdf4" stroke="#d8c78b" stroke-width="4"/>'
    if wet is not None: o += f'<rect x="{x+3}" y="{y+h-wet}" width="{w-6}" height="{wet-2}" fill="#cfe6f5" opacity=".55"/>'
    for (yy, col, hh) in bands: o += f'<ellipse cx="{x+w/2}" cy="{y+h-yy}" rx="{w*0.30}" ry="{hh}" fill="{col}" opacity=".9"/>'
    return o
for i, (ttl, wet, bands) in enumerate([("1 Start", 70, [(70, "#3b3b3b", 10)]), ("2 Efter en stund", 190, [(70, "#3b3b3b", 8), (115, "#2f6aa3", 14), (160, "#d9534a", 14)]), ("3 Klart", 330, [(60, "#3b3b3b", 8), (140, "#2f6aa3", 22), (230, "#d9534a", 20), (300, "#e0b02a", 16)])]):
    x0 = 40 + i * 480
    b += card(x0, 20, 440, 660, "#fff") + T(x0 + 220, 68, ttl, 38, DRED, "700")
    b += f'<rect x="{x0+60}" y="{120}" width="320" height="14" rx="6" fill="#b08b5a"/>'
    b += paper(x0 + 165, 130, 110, 400, bands, wet)
    # vatten i bägare
    b += f'<path d="M{x0+110},{470} V{610} Q{x0+110},{628} {x0+128},{628} H{x0+312} Q{x0+330},{628} {x0+330},{610} V470" fill="#f2f7fa" fill-opacity=".6" stroke="{LINE}" stroke-width="5"/>'
    b += f'<path d="M{x0+113},{520} H{x0+327} V{610} Q{x0+327},{625} {x0+312},{625} H{x0+128} Q{x0+113},{625} {x0+113},{610}Z" fill="#a8d2ee" opacity=".9"/>'
    b += f'<path d="M{x0+170},{500} H{x0+270}" stroke="{RED}" stroke-width="3" stroke-dasharray="6 5" opacity="0"/>'
b += T(750, 696, "", 1)
b += f'<path d="M40,500 H40" />'
render('v_kromatografi', svg(W, H, b, BG), W, H, 1)

# ---------- v_felling ---------------------------------------------------------
W, H = 1500, 520
b = ''
b += card(20, 20, 460, 480, "#fff") + T(250, 66, "Lösning A", 36, DRED, "700") + beaker(130, 130, 240, 260, 0.6, "#cfe6f5", False) + T(250, 440, "klar", 28, MUT)
b += T(540, 280, "+", 80, MUT, "700")
b += card(600, 20, 460, 480, "#fff") + T(830, 66, "Lösning B", 36, DRED, "700") + beaker(710, 130, 240, 260, 0.6, "#f6e8bd", False) + T(830, 440, "klar", 28, MUT)
b += arrow(1080, 270, 1150, 270, MUT, 8)
b += card(1160, 20, 330, 480, "#fff") + T(1325, 66, "Blandas", 36, DRED, "700") + beaker(1210, 130, 230, 260, 0.6, "#e7efe6", False)
b += dots(scatter(1222, 330, 206, 56, 14, 8, 3, 12), 8, "#ffffff", 3).replace('fill="#fff"', 'fill="#fdfdfd"')
b += T(1325, 440, "fällning (fast)", 28, DRED, "700")
render('v_felling', svg(W, H, b, BG), W, H, 1)

# ---------- v_labb2 -----------------------------------------------------------
W, H = 1500, 640
b = ''
for i, ttl in enumerate(["1 Filtrera", "2 Indunsta filtratet", "3 Kromatografi"]):
    x0 = 30 + i * 490
    b += card(x0, 20, 460, 600, "#fff") + T(x0 + 230, 66, ttl, 38, DRED, "700")
x0 = 30
b += f'<path d="M{x0+120},130 H{x0+340} L{x0+265},300 H{x0+195}Z" fill="#f2f7fa" fill-opacity=".8" stroke="{LINE}" stroke-width="6" stroke-linejoin="round"/>' + f'<path d="M{x0+135},148 L{x0+230},300 L{x0+325},148Z" fill="#cfe6f5"/>' + dots([(x0+195, 190), (x0+230, 215), (x0+265, 190)], 9, BRN)
b += f'<path d="M{x0+230},304 v60" stroke="#8fc3e6" stroke-width="6" stroke-dasharray="12 12" stroke-linecap="round"/>' + beaker(x0 + 130, 380, 200, 190, 0.35, "#cfe6f5", False)
x0 = 520
b += f'<rect x="{x0+50}" y="500" width="360" height="40" rx="10" fill="#8b8f93" stroke="#4a545c" stroke-width="4"/><rect x="{x0+66}" y="482" width="328" height="20" rx="6" fill="#d85a3a"/>'
b += f'<path d="M{x0+110},430 Q{x0+230},520 {x0+350},430Z" fill="#f4f1ea" stroke="{LINE}" stroke-width="6" stroke-linejoin="round"/><path d="M{x0+135},434 Q{x0+230},496 {x0+325},434Z" fill="#cfe6f5"/>'
for k in range(4): b += f'<path d="M{x0+170+k*40},400 q-14,-26 0,-46 q14,-20 0,-44" stroke="#b9c9d3" stroke-width="7" fill="none" stroke-linecap="round"/>'
b += T(x0 + 230, 590, "Stäng av innan allt vatten är borta", 24, MUT)
x0 = 1010
b += f'<rect x="{x0+90}" y="130" width="280" height="14" rx="6" fill="#b08b5a"/>'
b += paper(x0 + 175, 140, 110, 360, [(60, "#3b3b3b", 8), (140, "#2f6aa3", 20), (220, "#d9534a", 18)], 280)
b += f'<path d="M{x0+120},430 V520 Q{x0+120},540 {x0+140},540 H{x0+320} Q{x0+340},540 {x0+340},520 V430" fill="#f2f7fa" fill-opacity=".6" stroke="{LINE}" stroke-width="5"/><path d="M{x0+123},470 H{x0+337} V520 Q{x0+337},537 {x0+320},537 H{x0+140} Q{x0+123},537 {x0+123},520Z" fill="#a8d2ee" opacity=".9"/>'
render('v_labb2', svg(W, H, b, BG), W, H, 1)
