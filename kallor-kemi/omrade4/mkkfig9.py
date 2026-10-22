# -*- coding: utf-8 -*-
"""Kemi 4 – omslag, ikoner, fördjupnings- och provfigurer -> /tmp/kem/fig04k/"""
from k4lib import *
import mkkfig8 as M
from mkkfig8 import ball, bond, pair, mol_h2o, mol_h2, mol_ch4, mol_co2, h2o_s, lamp, HC, OC, CC, NAC, CLC
# ---------- omslag ----------
def cover(variant):
    W, H = 1818, 759
    pal = {'v': ('#f8dcd6', '#fdf3ec', '#e6b3aa'), 'l': ('#fbe5d6', '#fef7ea', '#efc3ae'), 'f': ('#e9c4be', '#f7e7e0', '#c98a82')}[variant]
    rnd = random.Random({'v': 31, 'l': 32, 'f': 33}[variant])
    s = f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{pal[0]}"/><stop offset="1" stop-color="{pal[1]}"/></linearGradient></defs><rect width="{W}" height="{H}" fill="url(#sk)"/>'
    for _ in range(30):
        s += f'<circle cx="{rnd.randint(40, W-40)}" cy="{rnd.randint(40, 700)}" r="{rnd.randint(6, 18)}" fill="{rnd.choice([EC, PC, NAC, CLC])}" opacity=".2"/>'
    s += f'<path d="M0,600 Q420,560 900,600 T1818,580 L1818,759 L0,759Z" fill="{pal[2]}" opacity=".55"/>'
    s += mol_h2o(330, 360).replace('r="50"', 'r="64"') if False else mol_h2o(330, 360)
    # gitter
    for i in range(5):
        for j in range(4):
            x, y = 620 + i * 110, 230 + j * 110
            s += ball(x, y, 30, NAC, "+", sz=34) if (i + j) % 2 == 0 else ball(x, y, 42, CLC, "−", sz=38)
    s += mol_co2(1330, 250) + mol_ch4(1500, 520).replace('', '')
    s += f'<rect x="38" y="38" width="190" height="46" rx="23" fill="#fff" opacity=".92"/>' + T(133, 70, "KAPITEL 4", 24, RED, "700")
    return svg(W, H, s, pal[0])
for v, n in (('v', 'vanlig'), ('l', 'lattlast'), ('f', 'fordjupning')):
    render('cover_' + n, cover(v), 1818, 759, 1)

# ---------- ikoner ----------
def icon(name, body, bg="#fbe9e6"):
    render(name, svg(256, 256, f'<rect width="256" height="256" rx="40" fill="{bg}"/>' + body, bg), 256, 256, 2)
def mini_h2o(cx, cy, k=0.55):
    return f'<g transform="translate({cx},{cy}) scale({k}) translate({-cx*0},0)">' + mol_h2o(0, 0) + '</g>'
icon('l_ic1', mini_h2o(128, 100, 0.8) + T(128, 232, "molekyl", 32, DRED, "700"))
icon('l_ic2', ball(86, 100, 30, NAC, "+", sz=34) + ball(150, 100, 42, CLC, "−", sz=38) + ball(214, 100, 30, NAC, "+", sz=34).replace('cx="214"', 'cx="212"') if False else ball(80, 100, 30, NAC, "+", sz=34) + ball(146, 100, 42, CLC, "−", sz=38) + T(128, 190, "jon", 36, INK, "700") + T(128, 232, "jonbindning", 28, DRED, "700"))
icon('l_ic3', lamp(128, 80, True).replace('r="34"', 'r="30"') + T(128, 170, "leder el?", 36, INK, "700") + T(128, 232, "egenskaper", 28, DRED, "700"))
icon('l_ic4', ball(60, 100, 26, HC, "A", sz=28) + T(100, 112, "+", 36, INK, "700") + ball(140, 100, 26, OC, "B", sz=28) + T(186, 112, "→", 40, INK, "700") + T(128, 190, "ny substans", 28, INK, "700") + T(128, 232, "reaktion", 30, DRED, "700"))
icon('l_ic5', T(128, 85, "2 H₂ + O₂", 38, INK, "700") + T(128, 140, "↓", 40, INK, "700") + T(128, 188, "2 H₂O", 40, INK, "700") + T(128, 235, "balansera", 28, DRED, "700"))
icon('l_ic6', thermometer(100, 40, 130, 0.8) + T(190, 110, "fort", 32, INK, "700") + T(128, 232, "hastighet", 30, DRED, "700"))
icon('l_ic7', T(128, 95, "exoterm", 34, "#c0392b", "700") + T(128, 140, "avger energi", 26, INK) + T(128, 185, "endoterm", 34, "#2f6aa3", "700") + T(128, 222, "tar upp energi", 26, INK))

# ---------- fördjupning ----------
W, H = 1500, 700; b = ARROW + T(750, 46, "Formler: jonerna måste ge laddningen noll tillsammans", 34, DRED, "700")
rows_ = [("Natriumklorid", [("Na⁺", NAC, 34)], [("Cl⁻", CLC, 42)], "NaCl", "(+1) + (−1) = 0"),
         ("Magnesiumklorid", [("Mg²⁺", "#7aa6d8", 38)], [("Cl⁻", CLC, 42), ("Cl⁻", CLC, 42)], "MgCl₂", "(+2) + 2 · (−1) = 0"),
         ("Natriumoxid", [("Na⁺", NAC, 34), ("Na⁺", NAC, 34)], [("O²⁻", OC, 44)], "Na₂O", "2 · (+1) + (−2) = 0")]
for i, (nm, cat_, an, form, chg) in enumerate(rows_):
    y = 150 + i * 190
    b += f'<rect x="40" y="{y-70}" width="1420" height="160" rx="18" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>' + T(70, y + 8, nm, 30, INK, "700", "start")
    x = 440
    for t, c, r in cat_:
        b += ball(x, y + 5, r, c, t, sz=26); x += r * 2 + 20
    b += T(x - 6, y + 16, "+", 34, INK, "700"); x += 40
    for t, c, r in an:
        b += ball(x + r, y + 5, r, c, t, sz=26); x += r * 2 + 20
    b += f'<path d="M{x+10},{y+5} H{x+80}" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>' + T(x + 150, y + 20, form, 40, INK, "700", "start") + T(1450, y + 20, chg, 28, MUT, "400", "end")
render('f_formler', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1400, 600; b = T(700, 46, "Metallbindning: joner i ett hav av fria elektroner", 34, DRED, "700")
b += f'<rect x="60" y="85" width="1280" height="420" rx="20" fill="#f8fafb" stroke="#8d969d" stroke-width="3"/>'
rnd = random.Random(5)
for j in range(4):
    for i in range(10):
        b += ball(140 + i * 120, 160 + j * 105, 36, "#aeb9c2", "+", sz=34)
for _ in range(46):
    x, y = rnd.randint(100, 1300), rnd.randint(110, 480)
    b += f'<circle cx="{x}" cy="{y}" r="9" fill="{EC}" stroke="#fff" stroke-width="2"/>'
b += f'<circle cx="360" cy="555" r="22" fill="#aeb9c2" stroke="#46525c" stroke-width="3"/>' + T(396, 565, "= positiv metalljon", 26, INK, "400", "start") + f'<circle cx="850" cy="555" r="9" fill="{EC}"/>' + T(872, 565, "= fri elektron (rör sig mellan jonerna)", 26, INK, "400", "start")
render('f_metall', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1500, 620; b = ARROW + T(750, 46, "Polär och opolär: elektronerna delas olika", 34, DRED, "700")
b += f'<rect x="40" y="85" width="700" height="440" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/><rect x="760" y="85" width="700" height="440" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>'
b += T(390, 135, "Vatten, H₂O: polär", 32, INK, "700") + ball(390, 250, 62, OC, "O", sz=44) + ball(250, 360, 42, HC, "H", sz=34) + ball(530, 360, 42, HC, "H", sz=34)
b += f'<path d="M280,336 L336,296" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/><path d="M500,336 L444,296" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>'
b += T(390, 185, "δ−", 34, "#a8322a", "700") if False else T(450, 205, "δ−", 34, "#a8322a", "700") + T(195, 420, "δ+", 34, "#2f6aa3", "700") + T(585, 420, "δ+", 34, "#2f6aa3", "700")
b += T(390, 470, "Pilarna pekar mot O. De tar inte ut varandra.", 25, MUT) + T(390, 503, "Molekylen får en + och en − sida.", 25, MUT)
b += T(1110, 135, "Koldioxid, CO₂: opolär", 32, INK, "700") + ball(930, 290, 52, OC, "O", sz=38) + ball(1110, 290, 52, CC, "C", sz=38) + ball(1290, 290, 52, OC, "O", sz=38)
b += f'<path d="M1050,290 H990" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/><path d="M1170,290 H1230" stroke="{INK}" stroke-width="6" marker-end="url(#a3)"/>'
b += T(1110, 420, "Pilarna dras åt motsatta håll och tar ut varandra.", 25, MUT) + T(1110, 453, "Molekylen som helhet är opolär.", 25, MUT)
b += T(750, 575, "Elektronegativitet (Pauling): O 3,5 · Cl 3,0 · C 2,5 · H 2,1", 28, INK, "700")
render('f_polar', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1300, 560; b = T(650, 46, "Brandtriangeln: en brand behöver alla tre", 34, DRED, "700")
b += f'<path d="M650,135 L880,480 L420,480Z" fill="#fde6da" stroke="#a8322a" stroke-width="7" stroke-linejoin="round"/>'
b += T(650, 390, "förbränning", 28, "#a8322a", "700") + T(650, 112, "värme", 34, INK, "700") + T(450, 530, "bränsle", 34, INK, "700") + T(850, 530, "syre", 34, INK, "700")
b += T(1085, 220, "Ta bort en sida,", 28, INK, "700") + T(1085, 258, "så slocknar branden.", 28, INK, "700") + T(1085, 310, "Exempel: brandfilt tar bort syre,", 24, MUT) + T(1085, 342, "vatten tar bort värme.", 24, MUT)
b += T(200, 230, "ger brand:", 26, MUT) if False else ''
render('f_brand', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1600, 640; b = T(800, 46, "Rost och korrosionsskydd", 34, DRED, "700")
for cx, t in ((290, "Rost bildas"), (800, "Skydd med färg eller zink"), (1310, "Offeranod")):
    b += f'<rect x="{cx-245}" y="85" width="490" height="480" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>' + T(cx, 130, t, 30, INK, "700")
# 1 rost
b += f'<rect x="90" y="330" width="400" height="90" rx="10" fill="#9aa5ad" stroke="#46525c" stroke-width="4"/><path d="M110,330 q40,-40 80,-10 q40,-30 80,0 q40,-35 100,5 v10 h-260z" fill="#b5651d" stroke="#7a4310" stroke-width="3"/>' + T(290, 395, "järn", 28, "#fff", "700")
b += T(290, 190, "järn + syre + vatten", 26, INK, "700") + T(290, 230, "→ rost (järnoxid)", 26, "#7a4310", "700") + T(290, 470, "Både syre och vatten behövs.", 25, MUT) + T(290, 505, "Rosten flagnar och järnet fortsätter rosta.", 25, MUT)
# 2 färg/zink
b += f'<rect x="600" y="340" width="400" height="90" rx="10" fill="#9aa5ad" stroke="#46525c" stroke-width="4"/><rect x="600" y="320" width="400" height="24" rx="8" fill="#6fa8dc" stroke="#2d5f8f" stroke-width="3"/><rect x="600" y="430" width="400" height="14" rx="6" fill="#6fa8dc" stroke="#2d5f8f" stroke-width="3"/>' + T(800, 395, "järn", 28, "#fff", "700")
b += T(800, 190, "Skikt som släpper in", 26, INK, "700") + T(800, 228, "varken syre eller vatten", 26, INK, "700") + T(800, 300, "färg · olja · zink (galvanisering)", 25, "#2d5f8f", "700") + T(800, 480, "Zink skyddar även om skiktet repas.", 25, MUT) + T(800, 515, "Färgen måste underhållas.", 25, MUT)
# 3 offeranod
b += f'<rect x="1100" y="340" width="400" height="90" rx="10" fill="#9aa5ad" stroke="#46525c" stroke-width="4"/>' + T(1250, 395, "järn (skrov)", 28, "#fff", "700") + f'<rect x="1370" y="300" width="70" height="40" rx="8" fill="#c9b6e8" stroke="#6d3fa0" stroke-width="4"/>' + T(1405, 290, "zink/magnesium", 22, "#6d3fa0", "700")
b += T(1310, 190, "En mer reaktiv metall", 26, INK, "700") + T(1310, 228, "kopplas till järnet", 26, INK, "700") + T(1310, 480, "Den reaktiva metallen rostar i stället", 25, MUT) + T(1310, 515, "för järnet. Används på fartyg och rör.", 25, MUT)
render('f_rost', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1500, 600; b = ARROW + T(750, 46, "Aktiveringsenergi och katalysator", 34, DRED, "700")
b += f'<path d="M110,110 V500 H1330" fill="none" stroke="{INK}" stroke-width="5"/>' + T(100, 100, "energi", 26, MUT, "400", "end") + T(1330, 540, "reaktionens förlopp →", 26, MUT, "400", "end")
b += f'<path d="M150,380 H330 C420,380 440,150 560,150 C680,150 700,430 880,430 H1280" fill="none" stroke="#a8322a" stroke-width="7"/>'
b += f'<path d="M330,380 C400,380 450,270 560,270 C670,270 700,430 880,430" fill="none" stroke="#2f6aa3" stroke-width="7" stroke-dasharray="14 8"/>'
b += T(240, 360, "utgångsämnen", 26, INK, "700") + T(1080, 410, "produkter", 26, INK, "700")
b += f'<path d="M650,380 V160" stroke="{MUT}" stroke-width="4" marker-end="url(#a3)" marker-start="none"/>' if False else ''
b += f'<path d="M600,380 V152" stroke="{MUT}" stroke-width="4"/><path d="M590,162 L600,150 L610,162" fill="none" stroke="{MUT}" stroke-width="4"/>' + T(670, 190, "aktiveringsenergi", 26, "#a8322a", "700", "start") + T(670, 222, "(utan katalysator)", 24, MUT, "400", "start")
b += T(1000, 195, "med katalysator:", 26, "#2f6aa3", "700", "start") + T(1000, 228, "lägre energitopp,", 26, "#2f6aa3", "400", "start") + T(1000, 260, "reaktionen går fortare", 26, "#2f6aa3", "400", "start")
b += f'<path d="M1180,430 V380" stroke="{INK}" stroke-width="3"/>' if False else ''
b += f'<path d="M1240,380 V430" stroke="{INK}" stroke-width="5" marker-end="url(#a3)"/>' + T(1250, 330, "energi avges", 26, INK, "700", "middle")
render('f_aktivering', svg(W, H, b, "#ffffff"), W, H, 1)

# ---------- provfigurer ----------
W, H = 1500, 520; b = T(750, 46, "Två modeller av ämnen (schematiskt)", 34, DRED, "700")
b += f'<rect x="40" y="85" width="700" height="380" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/><rect x="760" y="85" width="700" height="380" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>' + T(390, 130, "Ämne A", 32, INK, "700") + T(1110, 130, "Ämne B", 32, INK, "700")
for i in range(5):
    for j in range(3):
        x, y = 170 + i * 100, 210 + j * 100
        b += ball(x, y, 28, NAC, "+", sz=32) if (i + j) % 2 == 0 else ball(x, y, 38, CLC, "−", sz=34)
for k, (x, y) in enumerate(((900, 220), (1100, 260), (1290, 210), (960, 380), (1180, 390), (1330, 370))):
    b += f'<g transform="translate({x},{y}) scale(.55)">' + mol_h2o(0, 0) + '</g>'
render('p_modeller', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1300, 520; b = T(650, 46, "Vågavläsning (påhittade värden)", 34, DRED, "700")
b += f'<rect x="60" y="85" width="1180" height="380" rx="20" fill="#fff" stroke="#d9c9c4" stroke-width="3"/>'
from kfig4_common import flask as _fl, balance as _bal
for cx, t, v in ((260, "Före", "150,0 g"), (650, "Efter: öppen flaska", "148,6 g"), (1040, "Efter: sluten flaska", "150,0 g")):
    b += _fl(cx - 70, 200, 140, 150, 0.4, "#f6e9c0") + _bal(cx - 90, 355, 180, v, 24) + T(cx, 140, t, 28, INK, "700")
render('p_vag', svg(W, H, b, "#ffffff"), W, H, 1)

W, H = 1300, 680; b = T(650, 40, "Bildad koldioxid mot tid vid två temperaturer (påhittat försök)", 30, DRED, "700")
X0, X1, Y0, Y1 = 150, 1200, 560, 110
b += f'<path d="M{X0},{Y1-20} V{Y0} H{X1+30}" fill="none" stroke="{INK}" stroke-width="5"/>' + T(X0 - 14, Y1 - 4, "gas (cm³)", 24, MUT, "400", "end") + T(X1 + 30, Y0 + 50, "tid (s)", 24, MUT, "400", "end")
for t in range(0, 61, 10):
    x = X0 + t / 60 * (X1 - X0 - 40); b += f'<path d="M{x},{Y0} v10" stroke="{INK}" stroke-width="3"/>' + T(x, Y0 + 38, str(t), 22, MUT)
for v in range(0, 81, 20):
    y = Y0 - v / 80 * (Y0 - Y1 - 30); b += f'<path d="M{X0-10},{y} h10" stroke="{INK}" stroke-width="3"/>' + T(X0 - 18, y + 8, str(v), 22, MUT, "400", "end")
def cv(k, final):
    pts = []
    for t in range(0, 61, 2):
        v = final * (1 - math.exp(-k * t)); pts.append((X0 + t / 60 * (X1 - X0 - 40), Y0 - v / 80 * (Y0 - Y1 - 30)))
    return ' '.join(('M' if i == 0 else 'L') + f'{x:.0f},{y:.0f}' for i, (x, y) in enumerate(pts))
b += f'<path d="{cv(0.045, 70)}" fill="none" stroke="#2f6aa3" stroke-width="7"/><path d="{cv(0.12, 70)}" fill="none" stroke="#a8322a" stroke-width="7"/>'
b += T(980, 345, "B", 36, "#a8322a", "700") + T(1060, 470, "A", 36, "#2f6aa3", "700")
render('p_kurva', svg(W, H, b, "#ffffff"), W, H, 1)
print("klar mkkfig9")
