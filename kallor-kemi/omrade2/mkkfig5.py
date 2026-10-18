# -*- coding: utf-8 -*-
"""Kemi 2 – omslag, ikoner, fördjupnings- och provfigurer -> /tmp/kem/fig02k/"""
from kfig2_common import *

BLUE = "#6fa8d6"; ORG = "#e0873a"; BRN = "#a9824f"; SALT = "#9b6fc4"
def scatter(x, y, w, h, n, r, gap=2.0, seed=1):
    rnd = random.Random(seed); pts = []; tries = 0
    while len(pts) < n and tries < 20000:
        tries += 1
        px = rnd.uniform(x + r + 3, x + w - r - 3); py = rnd.uniform(y + r + 3, y + h - r - 3)
        if all((px - a) ** 2 + (py - b) ** 2 >= (2 * r + gap) ** 2 for a, b in pts): pts.append((px, py))
    return pts
def dots(pts, r, col, sw=2):
    return ''.join(f'<circle cx="{a:.0f}" cy="{b:.0f}" r="{r}" fill="{col}" stroke="#fff" stroke-width="{sw}"/>' for a, b in pts)

# ---------- omslag ------------------------------------------------------------
def cover(variant):
    W, H = 1818, 759
    pal = {'v': ('#f8dcd6', '#fdf3ec', '#e6b3aa'), 'l': ('#fbe5d6', '#fef7ea', '#efc3ae'), 'f': ('#e9c4be', '#f7e7e0', '#c98a82')}[variant]
    rnd = random.Random({'v': 13, 'l': 18, 'f': 15}[variant])
    s = f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal[0]}"/><stop offset="1" stop-color="{pal[1]}"/></linearGradient></defs><rect width="{W}" height="{H}" fill="url(#sk)"/>'
    for (x, y) in [(rnd.randint(60, W - 60), rnd.randint(40, 380)) for _ in range(26)]:
        s += f'<circle cx="{x}" cy="{y}" r="{rnd.randint(10, 26)}" fill="{rnd.choice([BLUE, ORG, SALT, "#d9534a"])}" opacity=".22"/>'
    s += f'<path d="M0,560 Q420,520 900,560 T1818,540 L1818,759 L0,759Z" fill="{pal[2]}" opacity=".55"/>'
    s += f'<rect x="0" y="600" width="{W}" height="159" fill="#b98f84"/><rect x="0" y="600" width="{W}" height="16" fill="#d9b8ae"/>'
    s += beaker(110, 360, 230, 240, 0.55, "#a8d2ee", True)
    s += cylinder(430, 250, 66, 350, 0.55, "#cfe6c4", 12)
    s += f'<path d="M640,600 L610,330 H900 L870,600Z" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="6" stroke-linejoin="round"/>'
    s += f'<path d="M780,330 L760,600" stroke="none"/><path d="M650,480 H860 L868,596 H642Z" fill="#a8d2ee" opacity=".9"/>'
    s += f'<rect x="710" y="500" width="110" height="80" rx="10" fill="#e9f6fd" stroke="#8fb7d3" stroke-width="5"/>'
    s += flask(1010, 380, 200, 220, 0.4, "#f6d36a")
    s += tube(1290, 330, 270, "#bcd9ec", .5) + tube(1344, 330, 270, "#f4c7cf", .45) + tube(1398, 330, 270, "#cde8c0", .4)
    s += f'<rect x="1272" y="372" width="200" height="14" rx="5" fill="#a9703c"/><rect x="1272" y="590" width="200" height="10" rx="5" fill="#a9703c"/>'
    s += goggles(1670, 540, 0.7)
    for (x, y, r) in [(200, 340, 14), (240, 290, 10), (470, 220, 9), (1090, 340, 12), (1130, 290, 8), (1660, 280, 13), (1600, 220, 9)]:
        s += bubble(x, y, r)
    s += dots(scatter(1550, 120, 220, 120, 14, 9, 3, 7), 9, BLUE, 2)
    s += f'<rect x="38" y="38" width="190" height="46" rx="23" fill="#fff" opacity=".92"/>' + T(133, 70, "KAPITEL 2", 24, RED, "700")
    return svg(W, H, s, pal[0])
for v, n in (('v', 'vanlig'), ('l', 'lattlast'), ('f', 'fordjupning')):
    render('cover_' + n, cover(v), 1818, 759, 1)

# ---------- ikoner ------------------------------------------------------------
def icon(name, body, bg="#fbe9e6"):
    render(name, svg(256, 256, f'<rect width="256" height="256" rx="40" fill="{bg}"/>' + body, bg), 256, 256, 2)
icon('l_ic1', f'<rect x="70" y="70" width="70" height="70" rx="8" fill="#9aa7b0" stroke="{INK}" stroke-width="6"/><circle cx="170" cy="150" r="38" fill="#a8d2ee" stroke="{INK}" stroke-width="6"/><path d="M128,186 h60" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>' + T(128, 232, "materia", 30, DRED, "700"))
icon('l_ic2', f'<rect x="56" y="70" width="64" height="64" rx="8" fill="#9aa7b0" stroke="{INK}" stroke-width="6"/>' + T(88, 112, "m", 36, "#fff", "700") + f'<path d="M136,102 h30" stroke="{INK}" stroke-width="7"/>' + f'<rect x="170" y="62" width="40" height="80" rx="6" fill="#cfe6f5" stroke="{INK}" stroke-width="6"/>' + T(190, 112, "V", 30, INK, "700") + T(128, 190, "ρ = m / V", 34, RED, "700") + T(128, 234, "densitet", 28, DRED, "700"))
pp = scatter(60, 60, 140, 110, 7, 14, 6, 3)
icon('l_ic3', dots(pp, 14, BLUE, 3) + ''.join(f'<path d="M{a},{b} l{12*math.cos(i)},{12*math.sin(i)}" stroke="{MUT}" stroke-width="4" marker-end="url(#ah2)"/>' for i, (a, b) in enumerate(pp)) + T(128, 226, "partiklar", 30, DRED, "700"))
icon('l_ic4', f'<circle cx="100" cy="100" r="42" fill="#9fc8e6" opacity=".85" stroke="#fff" stroke-width="4"/><circle cx="148" cy="112" r="42" fill="#e0873a" opacity=".7" stroke="#fff" stroke-width="4"/>' + T(128, 226, "blandning", 30, DRED, "700"))
icon('l_ic5', f'<path d="M64,62 H192 L146,150 H110Z" fill="#f2f7fa" stroke="{LINE}" stroke-width="7" stroke-linejoin="round"/><path d="M76,76 L128,150 L180,76Z" fill="#cfe6f5"/><path d="M128,156 v28" stroke="#8fc3e6" stroke-width="8" stroke-linecap="round" stroke-dasharray="10 9"/><path d="M92,200 h72" stroke="{LINE}" stroke-width="7" stroke-linecap="round"/>' + T(128, 238, "filtrera", 28, DRED, "700"))
icon('l_ic6', f'<circle cx="84" cy="150" r="40" fill="#f2f7fa" stroke="{LINE}" stroke-width="7"/><path d="M84,110 V84 Q84,70 98,70 H170" fill="none" stroke="{LINE}" stroke-width="10" stroke-linecap="round"/><rect x="140" y="58" width="70" height="26" rx="12" fill="#e3f1fa" stroke="{LINE}" stroke-width="5" transform="rotate(25 175 71)"/>' + T(128, 226, "destillera", 28, DRED, "700"))
icon('l_ic7', f'<circle cx="112" cy="104" r="46" fill="#fff" stroke="{INK}" stroke-width="10"/><path d="M146,138 L192,184" stroke="{INK}" stroke-width="16" stroke-linecap="round"/><path d="M92,98 h40 M92,116 h28" stroke="{MUT}" stroke-width="7" stroke-linecap="round"/>' + T(128, 238, "identifiera", 26, DRED, "700"))
icon('l_ic8', f'<path d="M84,62 L74,190 Q74,204 88,204 H168 Q182,204 182,190 L172,62Z" fill="#f2f7fa" stroke="{LINE}" stroke-width="7" stroke-linejoin="round"/><path d="M80,130 H176 L182,190 Q182,200 170,200 H86 Q74,200 74,190Z" fill="#cfe6f5"/>' + dots([(100, 184), (126, 188), (152, 182), (114, 172), (140, 174)], 9, "#fff", 3).replace('fill="#fff"', 'fill="#fdfdfd"') + T(128, 238, "fällning", 28, DRED, "700"))

# ---------- f_vatten4 ---------------------------------------------------------
W, H = 1100, 640
b = ''
X0, Y0, X1, Y1 = 150, 540, 1040, 90
b += f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
def px(t): return X0 + (t + 10) / 50 * (X1 - X0 - 40) + 20
def py(d): return Y0 - (d - 0.9950) / (1.0005 - 0.9950) * (Y0 - Y1 - 60) - 30
# kurva: parabel runt 4 °C (schematisk), is stannar vid 0
pts = []
for t in range(0, 31):
    d = 1.0 - 0.0000065 * (t - 4) ** 2
    pts.append((px(t), py(d)))
b += f'<polyline points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f'" fill="none" stroke="{RED}" stroke-width="7" stroke-linejoin="round"/>'
b += f'<circle cx="{px(4):.0f}" cy="{py(1.0):.0f}" r="13" fill="#fff" stroke="{RED}" stroke-width="7"/>' + T(px(4) + 20, py(1.0) - 24, "4 °C: tätast", 30, RED, "700", "start")
for t in (0, 10, 20, 30):
    b += f'<path d="M{px(t):.0f},{Y0} v12" stroke="{INK}" stroke-width="4"/>' + T(px(t), Y0 + 46, str(t), 28, INK, "700")
b += f'<g transform="translate(52,315) rotate(-90)">{T(0, 0, "Densitet (schematisk)", 28, INK, "700")}</g>' + T(595, 616, "Temperatur (°C)", 28, INK, "700")
b += f'<rect x="{px(-8):.0f}" y="{Y1+10}" width="{px(0)-px(-8):.0f}" height="{Y0-Y1-10}" fill="#dff1fb" opacity=".6"/>' + T((px(-8) + px(0)) / 2, Y1 + 56, "is", 34, "#2f6aa3", "700") + T((px(-8) + px(0)) / 2, Y1 + 96, "lägre", 26, MUT) + T((px(-8) + px(0)) / 2, Y1 + 126, "densitet", 26, MUT)
b += T(560, 52, "Vatten: densiteten är högst vid 4 °C", 34, DRED, "700")
render('f_vatten4', svg(W, H, b, "#ffffff"), W, H, 1)

# ---------- f_uppv ------------------------------------------------------------
W, H = 1100, 640
b = ''
X0, Y0, X1, Y1 = 150, 540, 1040, 90
b += f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
for k, v in enumerate([-20, 0, 50, 100, 120]):
    y = Y0 - (v + 30) / 170 * (Y0 - Y1)
    b += f'<path d="M{X0-10},{y:.0f} H{X1}" stroke="#e6d9d5" stroke-width="2"/>' + T(X0 - 18, y + 9, str(v), 26, INK, "400", "end")
def Y(v): return Y0 - (v + 30) / 170 * (Y0 - Y1)
seg = [(180, -20), (270, 0), (380, 0), (590, 100), (850, 100), (990, 118)]
b += f'<polyline points="' + " ".join(f"{x},{Y(v):.0f}" for x, v in seg) + f'" fill="none" stroke="{RED}" stroke-width="7" stroke-linejoin="round"/>'
for (x, t, c) in [(225, "A", INK), (325, "B", RED), (485, "C", INK), (720, "D", RED), (1005, "E", INK)]:
    yy = {"A": Y(-20) - 40, "B": Y(0) - 28, "C": Y(50) + 46, "D": Y(100) - 28, "E": Y(118) - 28}[t]
    b += f'<circle cx="{x}" cy="{yy:.0f}" r="22" fill="#fff" stroke="{c}" stroke-width="4"/>' + T(x, yy + 10, t, 28, c, "700")
b += f'<g transform="translate(52,315) rotate(-90)">{T(0, 0, "Temperatur (°C)", 28, INK, "700")}</g>' + T(595, 616, "Tillförd värme (tid, jämn värmning)", 28, INK, "700")
b += T(560, 52, "Uppvärmning av is, schematisk kurva (påhittade värden)", 30, DRED, "700")
render('f_uppv', svg(W, H, b, "#ffffff"), W, H, 1)

# ---------- f_losl ------------------------------------------------------------
W, H = 1100, 640
b = ''
X0, Y0, X1, Y1 = 150, 540, 1040, 90
b += f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
b += f'<path d="M180,470 Q500,380 1000,150" fill="none" stroke="{RED}" stroke-width="8"/>' + T(780, 250, "fast ämne", 32, RED, "700", "start")
b += f'<path d="M180,170 Q500,300 1000,480" fill="none" stroke="#2f6aa3" stroke-width="8"/>' + T(790, 470, "gas", 32, "#2f6aa3", "700", "start")
b += f'<g transform="translate(52,315) rotate(-90)">{T(0, 0, "Löslighet (schematisk)", 28, INK, "700")}</g>' + T(595, 616, "Temperatur", 28, INK, "700")
b += T(560, 52, "Löslighet i vatten, schematisk", 34, DRED, "700")
b += T(595, 585, "(inga uppmätta värden)", 22, MUT, "400", "middle", True)
render('f_losl', svg(W, H, b, "#ffffff"), W, H, 1)

# ---------- f_rf och p_kroma --------------------------------------------------
def kroma(name, cols, W=900, H=640, labels=True, marks=True, front_y=110, start_y=520, bg="#ffffff"):
    b = f'<rect x="100" y="60" width="{W-200}" height="{H-120}" rx="6" fill="#fffdf4" stroke="#d8c78b" stroke-width="5"/>'
    b += f'<path d="M100,{start_y} H{W-100}" stroke="{MUT}" stroke-width="3" stroke-dasharray="8 6"/><path d="M100,{front_y} H{W-100}" stroke="{MUT}" stroke-width="3" stroke-dasharray="8 6"/>'
    n = len(cols); step = (W - 280) / max(n - 1, 1)
    for i, (lab, bands) in enumerate(cols):
        cx = 140 + (i * step if n > 1 else 0) + 20
        for (d, col) in bands:
            yy = start_y - d * (start_y - front_y)
            b += f'<ellipse cx="{cx}" cy="{yy:.0f}" rx="42" ry="17" fill="{col}" opacity=".9"/>'
        b += f'<circle cx="{cx}" cy="{start_y}" r="9" fill="#555"/>' + T(cx, H - 18, lab, 28, INK, "700")
    return b
cols = [("Prov", [(0.40, "#d9534a"), (0.65, "#2f6aa3"), (0.9, "#e0b02a")])]
b = kroma('f_rf', cols, 900, 640, front_y=110, start_y=520)
b = b.replace('<circle cx="160" cy="520"', '<circle cx="160" cy="520"')
b += f'<path d="M700,520 V110" stroke="{INK}" stroke-width="4" marker-start="url(#ah)" marker-end="url(#ah)"/>' + T(690, 322, "b = 8,0 cm", 30, INK, "700", "end")
y_red = 520 - 0.40 * 410
b += f'<path d="M230,520 V{y_red:.0f}" stroke="{RED}" stroke-width="4" marker-end="url(#ah)"/>' + T(246, 400, "a = 3,2 cm", 28, RED, "700", "start")
b += T(300, 560, "startlinje", 22, MUT, "400", "start") + T(300, 100, "lösningsmedlets front", 22, MUT, "400", "start")
render('f_rf', svg(900, 640, b, "#ffffff"), 900, 640, 1)

# prov: p_kroma (fyra kolumner: kända A, B, C och okänd)
Y0s, Yf = 520, 110
cols = [("A", [(0.25, "#d9534a")]), ("B", [(0.55, "#2f6aa3")]), ("C", [(0.8, "#e0b02a")]), ("X", [(0.25, "#d9534a"), (0.8, "#e0b02a")])]
render('p_kroma', svg(900, 640, kroma('p', cols, 900, 640), "#ffffff"), 900, 640, 1)

# ---------- prov: p_cylinder (volym) och p_kurva -------------------------------
W, H = 520, 700
b = ''
cx0, cy0, cw, chh = 190, 70, 90, 540
b += f'<path d="M{cx0-6},{cy0-5} L{cx0},{cy0} L{cx0},{cy0+chh} L{cx0+cw},{cy0+chh} L{cx0+cw},{cy0} L{cx0+cw+6},{cy0-5}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="5" stroke-linejoin="round"/>'
b += f'<path d="M{cx0-cw*0.9},{cy0+chh+16} L{cx0+cw*1.9},{cy0+chh+16} L{cx0+cw*1.6},{cy0+chh} L{cx0-cw*0.6},{cy0+chh}Z" fill="#cfd8de" stroke="{LINE}" stroke-width="4"/>'
vol = 58; ly = cy0 + chh - chh * vol / 100
b += f'<path d="M{cx0+3},{ly-6} Q{cx0+cw/2},{ly+8} {cx0+cw-3},{ly-6} L{cx0+cw-3},{cy0+chh-3} L{cx0+3},{cy0+chh-3}Z" fill="#bcd9ec" opacity=".9"/>'
b += f'<rect x="{cx0+22}" y="{cy0+chh-60}" width="{cw-44}" height="56" rx="6" fill="#9aa7b0" stroke="#5d6b75" stroke-width="3"/>'
for v in range(0, 101, 2):
    y = cy0 + chh - chh * v / 100; L = 46 if v % 10 == 0 else 26
    b += f'<path d="M{cx0},{y} h{L}" stroke="{INK}" stroke-width="{3 if v%10==0 else 2}"/>'
    if v % 10 == 0 and v > 0: b += T(cx0 - 14, y + 9, str(v), 24, INK, "700", "end")
b += T(cx0 + cw + 60, cy0 + 26, "ml", 26, INK, "700")
render('p_cylinder', svg(W, H, b, "#ffffff"), W, H, 2)

W, H = 1100, 640
b = ''
X0, Y0, X1, Y1 = 150, 540, 1040, 90
b += f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
for k, v in enumerate([0, 25, 50, 75, 100]):
    y = Y0 - (Y0 - Y1) * v / 100
    b += f'<path d="M{X0-10},{y:.0f} H{X1}" stroke="#e6d9d5" stroke-width="2"/>' + T(X0 - 18, y + 9, str(v), 26, INK, "400", "end")
pts = [(150, 20), (330, 52), (330, 52), (520, 52), (900, 88)]
def Yp(v): return Y0 - (Y0 - Y1) * v / 100
seg = [(150, 15), (330, 52), (560, 52), (700, 74), (900, 96)]
b += f'<polyline points="' + " ".join(f"{x},{Yp(v):.0f}" for x, v in seg) + f'" fill="none" stroke="{RED}" stroke-width="7" stroke-linejoin="round"/>'
for t in range(0, 10):
    x = 150 + t * 90
    b += f'<path d="M{x},{Y0} v10" stroke="{INK}" stroke-width="4"/>' + T(x, Y0 + 44, str(t), 26, INK, "700")
b += f'<g transform="translate(52,315) rotate(-90)">{T(0, 0, "Temperatur (°C)", 28, INK, "700")}</g>' + T(595, 616, "Tid (min)", 28, INK, "700")
b += T(595, 52, "Påhittade mätvärden: ett ämne värms jämnt", 30, DRED, "700")
render('p_kurva', svg(W, H, b, "#ffffff"), W, H, 1)
