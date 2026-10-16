# -*- coding: utf-8 -*-
from kfig_common import *

# ---------- omslag ------------------------------------------------------------
def lab_cover(variant):
    W, H = 1818, 759
    pal = {'v': ('#f8dcd6', '#fdf3ec', '#e6b3aa'), 'l': ('#fbe5d6', '#fef7ea', '#efc3ae'), 'f': ('#e9c4be', '#f7e7e0', '#c98a82')}[variant]
    random.seed({'v': 3, 'l': 8, 'f': 5}[variant])
    s = f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal[0]}"/><stop offset="1" stop-color="{pal[1]}"/></linearGradient></defs><rect width="{W}" height="{H}" fill="url(#sk)"/>'
    # bakgrundsformer
    for i in range(14):
        s += f'<circle cx="{random.randint(40,W-40)}" cy="{random.randint(40,360)}" r="{random.randint(8,34)}" fill="#fff" opacity=".35"/>'
    s += f'<path d="M0,560 Q420,520 900,560 T1818,540 L1818,759 L0,759Z" fill="{pal[2]}" opacity=".55"/>'
    s += f'<rect x="0" y="600" width="{W}" height="159" fill="#b98f84"/><rect x="0" y="600" width="{W}" height="16" fill="#d9b8ae"/>'
    liq = ["#8fd18f", "#f4a8b8", "#8fc4e8", "#f6d36a", "#c9a7e8", "#ffb27a"]
    # kolvar och bägare
    s += flask(120, 330, 250, 270, 0.45, liq[0]).replace('stroke-width="5"', 'stroke-width="6"')
    s += beaker(470, 400, 190, 200, 0.55, liq[1], True)
    s += cylinder(760, 260, 66, 340, 0.5, liq[2], 12)
    s += flask(930, 380, 190, 220, 0.5, liq[3])
    s += beaker(1210, 340, 220, 260, 0.6, liq[4], True)
    s += flask(1500, 300, 240, 300, 0.4, liq[5])
    # provrörsställ
    rx = 1130
    # bubblor
    for (x, y, r) in [(200, 300, 16), (240, 250, 11), (215, 200, 8), (560, 360, 12), (590, 310, 8), (1010, 330, 10), (1320, 300, 14), (1360, 240, 9), (1600, 260, 13), (1640, 210, 9), (1590, 165, 7), (790, 215, 9)]:
        s += bubble(x, y, r)
    s += goggles(1000, 690, 1.15)
    s += f'<g transform="translate(300,690)">{T(0,0,"",1)}</g>'
    for (x, y) in [(400, 650), (1700, 650)]:
        s += f'<circle cx="{x}" cy="{y}" r="22" fill="#f4c542" stroke="#c9a02a" stroke-width="3" opacity=".0"/>'
    s += f'<rect x="38" y="38" width="190" height="46" rx="23" fill="#fff" opacity=".92"/>' + T(133, 70, "KAPITEL 1", 24, RED, "700")
    return svg(W, H, s, pal[0])

for v, n in (('v', 'vanlig'), ('l', 'lattlast'), ('f', 'fordjupning')):
    render('cover_' + n, lab_cover(v), 1818, 759, 1)

# ---------- ikoner till "Det viktigaste" (256 x 256) ---------------------------
def icon(name, body, bg="#fbe9e6"):
    render(name, svg(256, 256, f'<rect width="256" height="256" rx="40" fill="{bg}"/>' + body, bg), 256, 256, 2)

icon('l_ic1', flask(78, 56, 100, 130, 0.4, "#8fd18f") + bubble(120, 70, 8) + bubble(138, 46, 6) + T(128, 226, "kemi", 30, DRED, "700"))
cyc = ''
for k, c in enumerate([RED, "#2f6aa3", "#d0702a", "#7a4fa3"]):
    a0 = math.radians(k * 90 - 80); a1 = math.radians(k * 90 + 0)
    x0, y0 = 128 + 70 * math.cos(a0), 118 + 70 * math.sin(a0); x1, y1 = 128 + 70 * math.cos(a1), 118 + 70 * math.sin(a1)
    cyc += f'<path d="M{x0:.0f},{y0:.0f} A70,70 0 0 1 {x1:.0f},{y1:.0f}" stroke="{c}" stroke-width="16" fill="none" stroke-linecap="round"/>'
icon('l_ic2', cyc + T(128, 128, "?", 64, DRED, "700") + T(128, 226, "undersök", 28, DRED, "700"))
icon('l_ic3', f'<path d="M128,60 V170 M82,170 H174" stroke="{INK}" stroke-width="10" stroke-linecap="round"/><path d="M60,92 H196" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'
     f'<path d="M60,92 L40,138 H80Z M196,92 L176,138 H216Z" fill="#d9eaf6" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>' + T(128, 226, "rättvist", 28, DRED, "700"))
icon('l_ic4', f'<rect x="52" y="120" width="34" height="70" rx="4" fill="#e8a95a"/><rect x="100" y="80" width="34" height="110" rx="4" fill="#d9534a"/><rect x="148" y="140" width="34" height="50" rx="4" fill="#7fb2d9"/><path d="M40,194 H200" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>' + T(128, 238, "resultat", 28, DRED, "700"))
icon('l_ic5', goggles(128, 118, 0.85) + T(128, 226, "säkert", 30, DRED, "700"))
icon('l_ic6', f'<circle cx="112" cy="104" r="46" fill="#fff" stroke="{INK}" stroke-width="10"/><path d="M146,138 L192,184" stroke="{INK}" stroke-width="16" stroke-linecap="round"/><path d="M92,98 h40 M92,116 h28" stroke="{MUT}" stroke-width="7" stroke-linecap="round"/>' + T(128, 238, "källor", 28, DRED, "700"))
icon('l_ic7', f'<circle cx="92" cy="110" r="30" fill="#e0524a" stroke="#3a3a3a" stroke-width="5"/><circle cx="148" cy="96" r="22" fill="#f1f1f1" stroke="#3a3a3a" stroke-width="5"/><circle cx="160" cy="146" r="22" fill="#f1f1f1" stroke="#3a3a3a" stroke-width="5"/><path d="M112,100 L130,98 M110,128 L142,142" stroke="#3a3a3a" stroke-width="7"/>' + T(128, 226, "modell", 30, DRED, "700"))
icon('l_ic8', f'<path d="M128,70 Q90,52 50,66 V176 Q90,162 128,182 Q166,162 206,176 V66 Q166,52 128,70Z" fill="#fff" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/><path d="M128,70 V182" stroke="{INK}" stroke-width="7"/><path d="M68,92 q24,-6 44,4 M68,116 q24,-6 44,4 M144,96 q20,-10 44,-4 M144,120 q20,-10 44,-4" stroke="{MUT}" stroke-width="6" fill="none" stroke-linecap="round"/>' + T(128, 226, "historia", 28, DRED, "700"))

# ---------- f_traff: precision och riktighet ----------------------------------
W, H = 1500, 600
b = ''
cases = [("Hög precision", "Hög riktighet", (0, 0), 10), ("Hög precision", "Låg riktighet", (62, -38), 10), ("Låg precision", "Hög riktighet", (0, 0), 58), ("Låg precision", "Låg riktighet", (58, 40), 55)]
random.seed(9)
for i, (a, bb_, off, spread) in enumerate(cases):
    x0 = 20 + i * 370; cx, cy = x0 + 175, 230
    b += card(x0, 20, 350, 560, "#fff")
    for r, col in [(130, "#fbe3df"), (96, "#f3c1ba"), (62, "#e9978d"), (30, "#d9534a")]:
        b += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="#fff" stroke-width="3"/>'
    for k in range(6):
        ang = random.random() * 6.28; rr = random.random() * spread
        b += f'<circle cx="{cx+off[0]+rr*math.cos(ang):.0f}" cy="{cy+off[1]+rr*math.sin(ang):.0f}" r="9" fill="#24323c" stroke="#fff" stroke-width="2.5"/>'
    b += T(cx, 420, a, 29, INK, "700") + T(cx, 458, bb_, 29, INK, "700")
    expl = ["Mätvärdena ligger nära varandra och nära det sanna värdet.", "Mätvärdena ligger nära varandra men alla är fel åt samma håll (systematiskt fel).", "Mätvärdena sprider sig, men medelvärdet ligger nära det sanna värdet.", "Mätvärdena sprider sig och medelvärdet ligger fel."][i]
    words = expl.split(' '); ls = []; cur = ''
    for w in words:
        if len(cur + ' ' + w) > 30: ls.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    ls.append(cur)
    for k, ln in enumerate(ls): b += T(cx, 496 + k * 25, ln, 21, MUT)
render('f_traff', svg(W, H, b, BG), W, H, 1)

# ---------- f_punkter: enskilda mätvärden och medelvärde ----------------------
W, H = 1100, 640
b = ''
X0, Y0, X1, Y1 = 150, 540, 1040, 90
b += f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
mx = 180
for k in range(0, 7):
    v = k * 30; y = Y0 - (Y0 - Y1) * v / mx
    b += f'<path d="M{X0-10},{y} H{X1}" stroke="#e6d9d5" stroke-width="2"/>' + T(X0 - 18, y + 9, str(v), 26, INK, "400", "end")
dat = [("5 °C", [150, 160, 148], None), ("20 °C", [70, 118, 72], 118), ("40 °C", [29, 33, 31], None)]
for i, (lab, vals, out) in enumerate(dat):
    cx = X0 + 150 + i * 300
    for j, v in enumerate(vals):
        y = Y0 - (Y0 - Y1) * v / mx; px = cx - 60 + j * 60
        isout = (v == out)
        b += f'<circle cx="{px}" cy="{y}" r="15" fill="{"#fff" if isout else "#d9534a"}" stroke="{RED}" stroke-width="{6 if isout else 3}"/>'
        if isout: b += f'<circle cx="{px}" cy="{y}" r="27" fill="none" stroke="{RED}" stroke-width="4" stroke-dasharray="8 6"/>'
    mean = sum(vals) / 3; my = Y0 - (Y0 - Y1) * mean / mx
    b += f'<path d="M{cx-100},{my} H{cx+100}" stroke="{INK}" stroke-width="6"/>' + T(cx + 112, my + 9, f"{mean:.0f} s".replace(".", ","), 26, INK, "700", "start")
    b += T(cx, Y0 + 42, lab, 30, INK, "700")
b += f'<g transform="translate(52,315) rotate(-90)">{T(0, 0, "Tid tills tabletten är upplöst (s)", 28, INK, "700")}</g>'
b += T(595, 616, "Vattnets temperatur", 28, INK, "700") + T(595, 52, "Tre försök per temperatur. Strecket är medelvärdet.", 30, DRED, "700")
b += T(560, 215, "avvikande värde", 24, RED, "700", "start")
render('f_punkter', svg(W, H, b, "#ffffff"), W, H, 1)

# ---------- f_dalton_nu ------------------------------------------------------
W, H = 1500, 520
b = ''
b += card(20, 20, 720, 480, "#fff") + T(380, 70, "Dalton 1808", 38, DRED, "700")
b += f'<circle cx="380" cy="250" r="100" fill="#9aa5ad" stroke="#3a3a3a" stroke-width="6"/><circle cx="345" cy="215" r="26" fill="#fff" opacity=".4"/>'
b += T(380, 400, "En hård, odelbar kula.", 30, INK, "700") + T(380, 440, "Alla atomer av ett ämne är lika.", 26, MUT)
b += card(760, 20, 720, 480, "#fff") + T(1120, 70, "Senare undersökningar", 38, DRED, "700")
b += f'<circle cx="1120" cy="250" r="110" fill="#d9eaf6" stroke="#9ec6e0" stroke-width="4" stroke-dasharray="10 8"/><circle cx="1120" cy="250" r="22" fill="#d9534a" stroke="#3a3a3a" stroke-width="4"/>'
for k in range(5):
    a = math.radians(k * 72 + 20); b += f'<circle cx="{1120+88*math.cos(a):.0f}" cy="{250+88*math.sin(a):.0f}" r="9" fill="#2f6aa3" stroke="#fff" stroke-width="2"/>'
b += T(1120, 400, "Atomen har en kärna och elektroner.", 30, INK, "700") + T(1120, 440, "Atomer av samma ämne kan väga olika (isotoper).", 26, MUT)
render('f_dalton_nu', svg(W, H, b, BG), W, H, 1)

# ---------- p_cylinder (prov) -------------------------------------------------
W, H = 520, 700
b = ''
cx0, cy0, cw, chh = 190, 70, 90, 540
b += f'<path d="M{cx0-6},{cy0-5} L{cx0},{cy0} L{cx0},{cy0+chh} L{cx0+cw},{cy0+chh} L{cx0+cw},{cy0} L{cx0+cw+6},{cy0-5}" fill="#f2f7fa" fill-opacity=".7" stroke="{LINE}" stroke-width="5" stroke-linejoin="round"/>'
b += f'<path d="M{cx0-cw*0.9},{cy0+chh+16} L{cx0+cw*1.9},{cy0+chh+16} L{cx0+cw*1.6},{cy0+chh} L{cx0-cw*0.6},{cy0+chh}Z" fill="#cfd8de" stroke="{LINE}" stroke-width="4"/>'
vol = 62; ly = cy0 + chh - chh * vol / 100
b += f'<path d="M{cx0+3},{ly-6} Q{cx0+cw/2},{ly+8} {cx0+cw-3},{ly-6} L{cx0+cw-3},{cy0+chh-3} L{cx0+3},{cy0+chh-3}Z" fill="#bcd9ec" opacity=".9"/>'
for v in range(0, 101, 2):
    y = cy0 + chh - chh * v / 100
    L = 46 if v % 10 == 0 else 26
    b += f'<path d="M{cx0},{y} h{L}" stroke="{INK}" stroke-width="{3 if v%10==0 else 2}"/>'
    if v % 10 == 0 and v > 0: b += T(cx0 - 14, y + 9, str(v), 24, INK, "700", "end")
b += T(cx0 + cw + 60, cy0 + 26, "ml", 26, INK, "700")
render('p_cylinder', svg(W, H, b, "#ffffff"), W, H, 2)

# ---------- p_diagram (prov) ---------------------------------------------------
W, H = 1100, 640
b = ''
X0, Y0, X1, Y1 = 150, 540, 1040, 90
b += f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
mx = 150
for k in range(0, 6):
    v = k * 30; y = Y0 - (Y0 - Y1) * v / mx
    b += f'<path d="M{X0-10},{y} H{X1}" stroke="#e6d9d5" stroke-width="2"/>' + T(X0 - 18, y + 9, str(v), 26, INK, "400", "end")
pts = [(10, 132), (20, 80), (30, 52), (40, 33), (50, 22)]
def px(t): return X0 + (t - 5) / 50 * (X1 - X0 - 40) + 20
def py(v): return Y0 - (Y0 - Y1) * v / mx
b += f'<polyline points="' + " ".join(f"{px(t):.0f},{py(v):.0f}" for t, v in pts) + f'" fill="none" stroke="{RED}" stroke-width="7" stroke-linejoin="round"/>'
for t, v in pts:
    b += f'<circle cx="{px(t):.0f}" cy="{py(v):.0f}" r="11" fill="#fff" stroke="{RED}" stroke-width="6"/>' + T(px(t), Y0 + 40, str(t), 26, INK, "700")
b += f'<g transform="translate(52,315) rotate(-90)">{T(0, 0, "Tid tills tabletten är upplöst (s)", 28, INK, "700")}</g>'
b += T(595, 616, "Vattnets temperatur (°C)", 28, INK, "700") + T(595, 52, "Påhittade mätvärden", 30, DRED, "700")
render('p_diagram', svg(W, H, b, "#ffffff"), W, H, 1)
