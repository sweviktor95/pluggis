# -*- coding: utf-8 -*-
from kfig_common import *

# ---------- l_kemister (fyra kort) -------------------------------------------
W, H = 1500, 560
b = ''
def drop(x, y, s=1.0, col="#6fb3d8"):
    return f'<path d="M{x},{y-34*s} C{x+30*s},{y-4*s} {x+30*s},{y+30*s} {x},{y+30*s} C{x-30*s},{y+30*s} {x-30*s},{y-4*s} {x},{y-34*s}Z" fill="{col}" stroke="#3b82c4" stroke-width="{3*s}"/>'
def ic_analys(cx):
    return tube(cx - 60, 205, 150, "#bcd9ec", .55, 38) + drop(cx + 50, 270, 1.4) + f'<path d="M{cx-70},215 h110" stroke="{MUT}" stroke-width="0"/>'
def ic_lakemedel(cx):
    o = f'<g transform="translate({cx-40},300) rotate(-35)"><rect x="-70" y="-26" width="140" height="52" rx="26" fill="#fff" stroke="{LINE}" stroke-width="5"/><path d="M0,-26 h44 a26,26 0 0 1 0,52 h-44z" fill="#e8625a" stroke="{LINE}" stroke-width="5"/></g>'
    o += f'<circle cx="{cx+60}" cy="330" r="34" fill="#fff" stroke="{LINE}" stroke-width="5"/><path d="M{cx+36},330 h48" stroke="{LINE}" stroke-width="5"/>'
    o += f'<circle cx="{cx+78}" cy="238" r="16" fill="#f4c542" stroke="{LINE}" stroke-width="4"/>'
    return o
def ic_material(cx):
    o = f'<rect x="{cx-52}" y="235" width="104" height="150" rx="14" fill="#f2f7fa" stroke="{LINE}" stroke-width="6"/><rect x="{cx-22}" y="219" width="44" height="18" rx="5" fill="{LINE}"/>'
    o += f'<rect x="{cx-52}" y="285" width="104" height="100" rx="12" fill="#8fd18f" opacity=".85"/>' + T(cx, 345, "+", 54, "#fff", "700") + T(cx, 255, "", 10)
    return o
def ic_miljo(cx):
    o = f'<path d="M{cx-110},350 q55,-30 110,0 t110,0 v40 h-220z" fill="#9fd0ea"/><path d="M{cx-110},350 q55,-30 110,0 t110,0" stroke="#3b82c4" stroke-width="5" fill="none"/>'
    o += f'<path d="M{cx-60},330 q-6,-40 24,-54 q36,4 40,50z" fill="#8fc16a"/><rect x="{cx-30}" y="276" width="10" height="64" fill="#6b4a2f"/>'
    o += pipette(cx + 70, 235, 0.7)
    return o
cards = [("Analytisk kemist", "mäter vad ett prov innehåller, till exempel i vatten eller mat", "#fdeaea", ic_analys),
         ("Läkemedelskemist", "tar fram och testar nya läkemedel", "#fdf0d5", ic_lakemedel),
         ("Materialkemist", "utvecklar nya material, till exempel batterier och plast", "#e6f1fa", ic_material),
         ("Miljökemist", "undersöker föroreningar i luft, vatten och mark", "#e7f3e1", ic_miljo)]
cw = 345; gap = 20
for i, (n, d, bg, ic) in enumerate(cards):
    x = 20 + i * (cw + gap); cx = x + cw / 2
    b += card(x, 20, cw, 520, bg, "#e3d5d1") + ic(cx)
    b += T(cx, 435, n, 33, INK, "700")
    words = d.split(' '); ls = []; cur = ''
    for w in words:
        if len(cur + ' ' + w) > 26: ls.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    ls.append(cur)
    for k, ln in enumerate(ls[:3]): b += T(cx, 470 + k * 26, ln, 22, MUT)
render('l_kemister', svg(W, H, b, BG), W, H, 1)

# ---------- l_cykel (fyra steg) ----------------------------------------------
W, H = 1490, 750
b = ''
def box4(x, y, w, h, col, t1, t2):
    return (f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="26" fill="#fff" stroke="{col}" stroke-width="9"/>' + T(x, y - 8, t1, 52, col, "700") + T(x, y + 44, t2, 34, MUT))
def arc(d, col=RED): return f'<path d="{d}" stroke="{col}" stroke-width="12" fill="none" stroke-linecap="round" marker-end="url(#ah2)" style="color:{col}"/>'
b += box4(745, 120, 450, 170, "#a8322a", "1. Fråga", "Vad undrar jag?")
b += box4(1245, 375, 440, 170, "#2f6aa3", "2. Gissa", "Hypotes: Jag tror …")
b += box4(745, 630, 450, 170, "#d0702a", "3. Testa", "Gör en undersökning")
b += box4(245, 375, 440, 170, "#7a4fa3", "4. Svara", "Slutsats: Vad lärde jag mig?")
def curve_arrow(p0, c, p1, col=RED):
    (x0, y0), (cx_, cy_), (x1, y1) = p0, c, p1
    dx, dy = x1 - cx_, y1 - cy_; L = math.hypot(dx, dy); dx, dy = dx / L, dy / L
    bx, by = x1 - dx * 30, y1 - dy * 30
    o = f'<path d="M{x0},{y0} Q{cx_},{cy_} {bx:.0f},{by:.0f}" stroke="{col}" stroke-width="12" fill="none" stroke-linecap="round" opacity=".55"/>'
    o += f'<polygon points="{x1},{y1} {bx-dy*22:.0f},{by+dx*22:.0f} {bx+dy*22:.0f},{by-dx*22:.0f}" fill="{col}"/>'
    return o
b += curve_arrow((985, 120), (1190, 130), (1235, 285)) + curve_arrow((1240, 462), (1190, 600), (985, 630)) + curve_arrow((505, 630), (300, 620), (250, 470)) + curve_arrow((245, 288), (300, 130), (515, 118))
b += T(745, 358, "Andra kemister", 38, INK, "700") + T(745, 408, "kontrollerar och upprepar", 38, INK, "700")
render('l_cykel', svg(W, H, b, "#fbf3f1"), W, H, 1)

# ---------- v_brus: tre glas ---------------------------------------------------
W, H = 1500, 560
b = ''
specs = [(110, "5 °C", "#cfe3f3", 0.1, "kallt"), (580, "20 °C", "#bcd9ec", 0.55, "rumstemperatur"), (1050, "40 °C", "#f1d6b8", 0.95, "varmt")]
for x, lab, col, val, nm in specs:
    b += beaker(x, 150, 250, 290, 0.62, col, ticks=True)
    b += thermometer(x + 285, 140, 250, val, "#d63a2e" if val > .5 else "#3a78c9")
    b += T(x + 125, 108, lab, 50, DRED, "700") + T(x + 125, 495, nm, 28, MUT)
    # tablett
    b += f'<ellipse cx="{x+125}" cy="{420}" rx="52" ry="14" fill="#fff" stroke="{LINE}" stroke-width="4"/>'
    random.seed(int(val * 100))
    nb = {0.1: 4, 0.55: 11, 0.95: 22}[val]
    for k in range(nb):
        bx = x + 80 + random.random() * 90; by = 215 + random.random() * 190
        b += bubble(bx, by, random.choice([5, 7, 9, 12]))
b += T(750, 548, "Samma mängd vatten och samma sorts tablett i alla glas. Det enda som ändras är temperaturen.", 27, INK, "700")
for x in (110, 1050):
    pass
b += f'<path d="M1050,148 q-8,-24 4,-40 M1100,148 q-8,-24 4,-40 M1150,148 q-8,-24 4,-40" stroke="#c9b6a3" stroke-width="5" fill="none" stroke-linecap="round" opacity="0"/>'
b += ''.join(f'<polygon points="{x},{y} {x+34},{y-6} {x+38},{y+28} {x+4},{y+34}" fill="#e8f4fb" stroke="#9ec6e0" stroke-width="3"/>' for x, y in [(140, 300), (200, 330)])
render('v_brus', svg(W, H, b, BG), W, H, 1)

# ---------- v_brusdiagram ------------------------------------------------------
W, H = 1100, 640
b = ''
X0, Y0, X1, Y1 = 150, 540, 1040, 90
b += f'<path d="M{X0},{Y1-10} V{Y0} H{X1}" stroke="{INK}" stroke-width="5" fill="none"/>'
mx = 180
for k in range(0, 7):
    v = k * 30; y = Y0 - (Y0 - Y1) * v / mx
    b += f'<path d="M{X0-10},{y} H{X1}" stroke="#e6d9d5" stroke-width="2"/>' + T(X0 - 18, y + 9, str(v), 26, INK, "400", "end")
data = [("5 °C", 152, "#7fb2d9"), ("20 °C", 74, "#e8a95a"), ("40 °C", 31, "#d9534a")]
bw = 170
for i, (lab, v, col) in enumerate(data):
    x = X0 + 90 + i * 260; h = (Y0 - Y1) * v / mx
    b += f'<rect x="{x}" y="{Y0-h}" width="{bw}" height="{h}" rx="6" fill="{col}"/>' + T(x + bw / 2, Y0 - h - 14, f"{v} s", 32, INK, "700") + T(x + bw / 2, Y0 + 40, lab, 30, INK, "700")
b += T(55, 315, "", 2)
b += f'<g transform="translate(52,315) rotate(-90)">{T(0, 0, "Tid tills tabletten är upplöst (s)", 28, INK, "700")}</g>'
b += T(595, 616, "Vattnets temperatur", 28, INK, "700")
b += T(595, 52, "Hur snabbt löses brustabletten? (medelvärden)", 32, DRED, "700")
render('v_brusdiagram', svg(W, H, b, "#ffffff"), W, H, 1)

# ---------- l_modell: partikelmodellen ---------------------------------------
W, H = 1500, 560
b = ''
random.seed(11)
cw = 470; gap = 25
titles = [("Fast", "Partiklarna sitter på fasta platser och vibrerar."), ("Flytande", "Partiklarna ligger tätt men glider förbi varandra."), ("Gas", "Partiklarna rör sig fritt med stora avstånd.")]
for i, (t, d) in enumerate(titles):
    x = 20 + i * (cw + gap)
    b += card(x, 20, cw, 520, "#fff") + T(x + cw / 2, 68, t, 38, DRED, "700")
    px0, py0, pw, ph = x + 45, 100, cw - 90, 300
    b += f'<rect x="{px0}" y="{py0}" width="{pw}" height="{ph}" rx="14" fill="#eef5fa" stroke="#cfe0ec" stroke-width="3"/>'
    pts = []
    if i == 0:
        for r in range(7):
            for c in range(8): pts.append((px0 + 28 + c * 48 + (0 if r % 2 == 0 else 0), py0 + 28 + r * 41))
    elif i == 1:
        tries = 0
        while len(pts) < 40 and tries < 5000:
            tries += 1; p = (px0 + 22 + random.random() * (pw - 44), py0 + 22 + random.random() * (ph - 44))
            if all((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 > 40 ** 2 for q in pts): pts.append(p)
    else:
        tries = 0
        while len(pts) < 9 and tries < 5000:
            tries += 1; p = (px0 + 30 + random.random() * (pw - 60), py0 + 30 + random.random() * (ph - 60))
            if all((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 > 110 ** 2 for q in pts): pts.append(p)
    for (qx, qy) in pts:
        if i == 2:
            a = random.random() * 6.28; L = 46
            b += f'<path d="M{qx:.0f},{qy:.0f} l{L*math.cos(a):.0f},{L*math.sin(a):.0f}" stroke="#d6704a" stroke-width="5" stroke-linecap="round" marker-end="url(#ah)" style="color:#d6704a"/>'
        if i == 1:
            a = random.random() * 6.28; L = 18
            b += f'<path d="M{qx:.0f},{qy:.0f} l{L*math.cos(a):.0f},{L*math.sin(a):.0f}" stroke="#d6704a" stroke-width="4" stroke-linecap="round"/>'
        b += f'<circle cx="{qx:.0f}" cy="{qy:.0f}" r="17" fill="#5b9bd5" stroke="#2f6aa3" stroke-width="3"/>'
    for k, ln in enumerate([d[:34], d[34:]] if len(d) > 34 else [d]):
        pass
    words = d.split(' '); ls = []; cur = ''
    for w in words:
        if len(cur + ' ' + w) > 36: ls.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    ls.append(cur)
    for k, ln in enumerate(ls): b += T(x + cw / 2, 446 + k * 30, ln, 25, MUT)
render('l_modell', svg(W, H, b, BG), W, H, 1)

# ---------- v_tidslinje -----------------------------------------------------
W, H = 1500, 600
b = ''
b += f'<path d="M60,300 H1440" stroke="{DRED}" stroke-width="10" stroke-linecap="round"/>'
ev = [(150, "ca 450 f.Kr.", "Empedokles", "Allt är uppbyggt av fyra ”rötter”: jord, vatten, luft och eld.", "up"),
      (430, "ca 350 f.Kr.", "Aristoteles", "Utvecklar läran om de fyra elementen. Den lever kvar i över 2 000 år.", "down"),
      (760, "1661", "Boyle", "Tvivlar på de fyra elementen och kräver bevis från försök.", "up"),
      (1090, "1789", "Lavoisier", "Visar med vägningar att massan bevaras. Ger syre dess namn.", "down"),
      (1340, "1808", "Dalton", "Atomteorin: alla ämnen är byggda av atomer.", "up")]
for x, yr, who, txt, side in ev:
    b += f'<circle cx="{x}" cy="300" r="20" fill="#fff" stroke="{DRED}" stroke-width="9"/>'
    cw_, ch_ = 300, 205
    cx = min(max(x, 20 + cw_ / 2), W - 20 - cw_ / 2)
    cy = 120 if side == "up" else 480
    b += f'<path d="M{x},{300-20 if side=="up" else 320} V{cy+ch_/2-2 if side=="up" else cy-ch_/2+2}" stroke="{DRED}" stroke-width="5"/>'
    b += card(cx - cw_ / 2, cy - ch_ / 2, cw_, ch_, "#fff", "#e3c4c0")
    b += T(cx, cy - ch_ / 2 + 38, yr, 30, RED, "700") + T(cx, cy - ch_ / 2 + 72, who, 32, INK, "700")
    words = txt.split(' '); ls = []; cur = ''
    for w in words:
        if len(cur + ' ' + w) > 26: ls.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    ls.append(cur)
    for k, ln in enumerate(ls): b += T(cx, cy - ch_ / 2 + 108 + k * 27, ln, 22, MUT)
render('v_tidslinje', svg(W, H, b, BG), W, H, 1)

# ---------- v_massa: sluten flaska före/efter ----------------------------------
W, H = 1500, 620
b = ''
def bottle(x, y, after):
    o = flask(x, y, 190, 250, 0.38, "#bcd9ec")
    o += f'<rect x="{x+190/2-26}" y="{y-26}" width="52" height="26" rx="6" fill="#d6704a" stroke="{LINE}" stroke-width="4"/>'
    if not after:
        o += f'<rect x="{x+70}" y="{y+170}" width="54" height="50" rx="10" fill="#e9ecef" stroke="{LINE}" stroke-width="4"/><ellipse cx="{x+97}" cy="{y+204}" rx="20" ry="7" fill="#fff" stroke="{LINE}" stroke-width="3"/>'
    else:
        random.seed(5)
        for k in range(9): o += bubble(x + 40 + random.random() * 110, y + 120 + random.random() * 110, random.choice([6, 9, 12]))
        o += f'<path d="M{x+60},{y+70} q20,-26 40,0 t40,0" stroke="#8fb7d3" stroke-width="4" fill="none" opacity=".8"/>'
    return o
for i, (lab, sub) in enumerate([("Före", "Tabletten ligger i en liten sluten kapsel i vattnet."), ("Efter", "Tabletten har reagerat. Gasen blir kvar i flaskan.")]):
    x = 120 + i * 700
    b += card(x - 40, 20, 640, 580, "#fff") + T(x + 280, 70, lab, 42, DRED, "700")
    b += bottle(x + 80, 160, i == 1)
    b += balance(x + 10, 440, 430, "250,0 g", 38).replace('y="440"', 'y="440"')
    b += T(x + 280, 575, sub, 25, MUT)
b += f'<path d="M692,310 H790" stroke="{RED}" stroke-width="6" marker-end="url(#ah)"/>' + T(741, 285, "reaktion", 26, RED, "700")
render('v_massa', svg(W, H, b, BG), W, H, 1)

# ---------- v_dalton ---------------------------------------------------------
W, H = 1500, 560
b = ''
def ball(x, y, r, col, lab=None, tc="#fff"):
    o = f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#3a3a3a" stroke-width="4"/><circle cx="{x-r*0.3}" cy="{y-r*0.3}" r="{r*0.25}" fill="#fff" opacity=".5"/>'
    if lab: o += T(x, y + 8, lab, r * 0.8, tc, "700")
    return o
b += card(20, 20, 640, 520, "#fff") + T(340, 70, "Atomer av olika ämnen väger olika", 33, DRED, "700")
b += ball(170, 250, 34, "#f1f1f1", "H", INK) + ball(340, 250, 56, "#e0524a", "O") + ball(520, 250, 66, "#555", "C")
b += T(170, 360, "väte", 28, INK, "700") + T(340, 360, "syre", 28, INK, "700") + T(520, 360, "kol", 28, INK, "700")
b += T(340, 440, "Alla atomer av samma grundämne", 25, MUT) + T(340, 472, "är likadana och väger lika mycket.", 25, MUT)
b += card(690, 20, 790, 520, "#fff") + T(1085, 70, "Föreningar bildas i enkla förhållanden", 33, DRED, "700")
b += ball(850, 240, 50, "#555", "C") + ball(944, 240, 44, "#e0524a", "O") + T(900, 340, "1 kol + 1 syre", 28, INK, "700") + T(900, 372, "kolmonoxid", 25, MUT)
b += ball(1190, 240, 50, "#555", "C") + ball(1284, 240, 44, "#e0524a", "O")
b += ball(1190 - 0, 240, 50, "#555", "C") + ball(1284, 240, 44, "#e0524a", "O") + ball(1378, 240, 44, "#e0524a", "O")
b += T(1284, 340, "1 kol + 2 syre", 28, INK, "700") + T(1284, 372, "koldioxid", 25, MUT)
b += T(1085, 450, "Samma sorts atomer kan sättas ihop på olika sätt.", 25, MUT) + T(1085, 482, "Atomerna skapas inte och försvinner inte i en reaktion.", 25, MUT)
render('v_dalton', svg(W, H, b, BG), W, H, 1)

# ---------- v_flack: labb 1.2 -----------------------------------------------
W, H = 1500, 520
b = ''
items = [("A", "Bara vatten", "(jämförelse)", "#cfe3f3"), ("B", "Diskmedel", "", "#f6e3a8"), ("C", "Fläckborttagare X", "(den i reklamen)", "#f4c7cf"), ("D", "Tvättmedel", "", "#cde8c0")]
for i, (k, n, n2, col) in enumerate(items):
    x = 40 + i * 360
    b += card(x, 20, 335, 480, "#fff")
    b += f'<rect x="{x+60}" y="60" width="215" height="170" rx="8" fill="#fbfbf8" stroke="{LINE}" stroke-width="5"/>'
    random.seed(i + 3)
    b += f'<ellipse cx="{x+167}" cy="146" rx="52" ry="40" fill="#8a5a3a" opacity="0.85"/>'
    for yy in range(80, 220, 14): b += f'<path d="M{x+64},{yy} H{x+271}" stroke="#e8e4da" stroke-width="2"/>'
    b += beaker(x + 105, 270, 125, 110, 0.5, col, ticks=False)
    b += T(x + 167, 425, k + ". " + n, 29, INK, "700")
    if n2: b += T(x + 167, 458, n2, 24, MUT)
render('v_flack', svg(W, H, b, BG), W, H, 1)
