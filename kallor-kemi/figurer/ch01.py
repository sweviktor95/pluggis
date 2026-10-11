# -*- coding: utf-8 -*-
import sys, math
sys.path.insert(0, '/tmp/figs')
from svgkit import *

W = 640
FIGS = {}


def g(tr, body):
    return f'<g transform="{tr}">{body}</g>'


# ---------------------------------------------------------------- 1.1
def vardag():
    b = title(W, "Kemi finns överallt")
    cards = [
        (20, 56, "I vardagen", "Ägget stelnar när det steks", "#fbe3c4"),
        (330, 56, "I naturen", "Växten bygger socker av ljus", "#dcefc9"),
        (20, 226, "I samhället", "Batteriet i mobilen", "#dcebf3"),
        (330, 226, "I kroppen", "Syre används i cellerna", "#ecdff3"),
    ]
    for x, y, t, s, c in cards:
        b += box(x, y, 290, 152, "", fill=c, r=16)
        b += text(x + 145, y + 30, t, 21, INK, "middle", "700")
        b += text(x + 145, y + 132, s, 16, INK)
    # ikon vardag: stekpanna med ägg
    x, y = 20, 56
    b += circle(x + 135, y + 78, 40, "#5d6b75")
    b += line(x + 172, y + 74, x + 235, y + 66, "#5d6b75", 9)
    b += f'<ellipse cx="{x+135}" cy="{y+78}" rx="30" ry="26" fill="#fff"/>'
    b += circle(x + 135, y + 78, 12, YELLOW)
    # ikon natur: solen, blad, pil
    x, y = 330, 56
    b += circle(x + 70, y + 70, 20, YELLOW)
    for a in range(0, 360, 45):
        r1, r2 = 26, 34
        b += line(x + 70 + r1 * math.cos(math.radians(a)), y + 70 + r1 * math.sin(math.radians(a)),
                  x + 70 + r2 * math.cos(math.radians(a)), y + 70 + r2 * math.sin(math.radians(a)), YELLOW, 3)
    b += arrow(x + 112, y + 74, x + 160, y + 74, MUTED, 3)
    b += line(x + 210, y + 108, x + 210, y + 78, "#6b8f4e", 4)
    b += path(f"M{x+210} {y+84} C{x+180} {y+78} {x+176} {y+52} {x+210} {y+42} C{x+246} {y+52} {x+240} {y+78} {x+210} {y+84}Z", GREEN, "#6b8f4e", 2)
    # ikon samhälle: batteri
    x, y = 20, 226
    b += rect(x + 95, y + 52, 100, 54, "#fff", INK, 8)
    b += rect(x + 195, y + 66, 12, 26, INK, None, 3)
    b += rect(x + 103, y + 60, 54, 38, GREEN, None, 4)
    b += text(x + 232, y + 90, "+", 28, INK, "middle", "700")
    b += text(x + 70, y + 90, "−", 28, INK, "middle", "700")
    # ikon kropp: cell med O2
    x, y = 330, 226
    b += arrow(x + 50, y + 76, x + 104, y + 76, MUTED, 3)
    b += text(x + 62, y + 66, "O₂", 20, BLUE, "middle", "700")
    b += circle(x + 155, y + 76, 36, "#f6c9d4", "#c0607a", 3)
    b += circle(x + 155, y + 76, 11, PURPLE)
    b += arrow(x + 197, y + 76, x + 225, y + 76, MUTED, 3) + text(x + 232, y + 82, "energi", 16, INK, "start")
    return fig(W, 400, b, "Kemi i vardagen, naturen, samhället och kroppen")


FIGS["k1_vardag"] = vardag()


# ---------------------------------------------------------------- 1.2
def blandningar():
    b = title(W, "Så ser ämnen och blandningar ut i partikelbild")
    px = [20, 227, 434]
    cw = 186
    heads = [("Grundämne", "ORANGE"), ("Kemisk förening", "RED"), ("Blandning", "BLUE")]
    for i, (h, _) in enumerate(heads):
        b += box(px[i], 56, cw, 150, "", fill="#fff", stroke=GREY, r=14)
        b += text(px[i] + cw / 2, 232, h, 20, INK, "middle", "700")
    # H och O
    def atomO(x, y, r=13): return circle(x, y, r, RED, "#8f3427", 2)
    def atomH(x, y, r=8): return circle(x, y, r, "#fff", MUTED, 2)
    def atomN(x, y, r=11): return circle(x, y, r, BLUE, NAVY, 2)
    # grundämne: bara järn-atomer
    fe = [(40, 95), (88, 88), (136, 100), (60, 140), (108, 144), (150, 150), (42, 186), (92, 190), (138, 192), (152, 120)]
    for (x, y) in fe:
        b += circle(px[0] + x + 3, y, 13, ORANGE, "#b36a2e", 2)
    # förening: vattenmolekyler
    def h2o(x, y):
        s = line(x, y, x - 19, y + 15, MUTED, 4) + line(x, y, x + 19, y + 15, MUTED, 4)
        return s + atomO(x, y) + atomH(x - 19, y + 15) + atomH(x + 19, y + 15)
    for (x, y) in [(50, 90), (120, 88), (85, 133), (142, 140), (48, 168), (112, 176)]:
        b += h2o(px[1] + x, y)
    # blandning: N2 och O2
    def mol(x, y, f, ang=0):
        d = 12
        dx, dy = d * math.cos(ang), d * math.sin(ang)
        return line(x - dx, y - dy, x + dx, y + dy, MUTED, 4) + f(x - dx, y - dy) + f(x + dx, y + dy)
    for (x, y, k, a) in [(42, 92, 'N', 0), (104, 90, 'O', .5), (146, 125, 'N', 1.2), (50, 135, 'O', -.4),
                         (100, 140, 'N', .2), (140, 176, 'O', 0.5), (45, 180, 'N', -0.3), (95, 186, 'O', 0.1)]:
        b += mol(px[2] + x, y, atomN if k == 'N' else atomO, a)
    # beskrivningar
    descs = [("Bara en sorts atomer", "t.ex. järn (Fe)"), ("Olika atomer sitter ihop", "t.ex. vatten (H₂O)"), ("Flera ämnen sida vid sida", "t.ex. luft (kväve + syre)")]
    for i, (a, c) in enumerate(descs):
        b += text(px[i] + cw / 2, 258, a, 16, INK)
        b += text(px[i] + cw / 2, 280, c, 16, MUTED)
    # teckenförklaring
    lx = 60
    b += atomO(lx, 322, 11) + text(lx + 18, 328, "syre", 15, INK, "start")
    b += atomH(lx + 90, 322, 8) + text(lx + 104, 328, "väte", 15, INK, "start")
    b += atomN(lx + 180, 322, 10) + text(lx + 196, 328, "kväve", 15, INK, "start")
    b += circle(lx + 280, 322, 11, ORANGE, "#b36a2e", 2) + text(lx + 298, 328, "järn", 15, INK, "start")
    b += text(W / 2, 362, "Förenklad bild: atomer ritade som kulor", 15, MUTED, italic=True)
    return fig(W, 380, b, "Partikelbild av grundämne, kemisk förening och blandning")


FIGS["k1_blandningar"] = blandningar()


# ---------------------------------------------------------------- 1.3
def undersokning():
    b = title(W, "Undersökningens steg")
    xs = [20, 225, 430]
    bw, bh = 190, 108
    items = [
        (xs[0], 56, "Fråga", ["Påverkar temperaturen", "lösningstiden?"], "#dcebf3", 1),
        (xs[1], 56, "Hypotes", ["Varmt vatten löser", "snabbare, därför att", "partiklarna rör sig mer"], "#ecdff3", 2),
        (xs[2], 56, "Planera", ["Ändra: temperatur", "Mät: tiden", "Lika: socker, vatten"], "#dcefc9", 3),
        (xs[2], 216, "Utför", ["Mät tre gånger", "vid 20, 35 och 50 °C", "Skriv ner direkt"], "#fbe3c4", 4),
        (xs[1], 216, "Värdera", ["Stämde hypotesen?", "Felkällor? Medelvärde", "i tabell och diagram"], "#f6dada", 5),
    ]
    for x, y, t, ls, c, n in items:
        b += box(x, y, bw, bh, [t] + ls, fill=c, size=16, r=14)
        b += badge(x + 4, y + 4, n)
    b += arrow(212, 110, 223, 110)
    b += arrow(417, 110, 428, 110)
    b += arrow(525, 166, 525, 214)
    b += arrow(428, 270, 417, 270)
    # tillbaka: från Värdera till Fråga
    b += curve("M225 270 C120 270 115 230 115 168")
    b += text(120, 262 + 36, "Nya frågor", 17, MUTED, "middle", "700")
    return fig(W, 340, b, "Undersökningens steg som en cykel med exemplet socker i vatten")


FIGS["k1_undersokning"] = undersokning()


# ---------------------------------------------------------------- 1.4
def diagram():
    left, right, top, bot = 100, 600, 80, 312
    ymax = 100
    sc = (bot - top) / ymax
    b = title(W, "Lösningstid för socker i vatten", y=30)
    b += text(W / 2, 54, "Medelvärde av tre försök", 16, MUTED)
    for v in range(0, 101, 20):
        y = bot - v * sc
        b += line(left, y, right, y, "#dad2bd" if v else INK, 1.5 if v else 2.5)
        b += text(left - 10, y + 5, str(v), 16, INK, "end")
    b += line(left, top - 6, left, bot, INK, 2.5)
    data = [(20, 87, TEAL), (35, 52, ORANGE), (50, 32, RED)]
    cx = [185, 350, 515]
    for (t, v, c), x in zip(data, cx):
        h = v * sc
        b += rect(x - 50, bot - h, 100, h, c, None, 6)
        b += rect(x - 50, bot - 8, 100, 8, c)
        b += text(x, bot - h - 8, f"{v} s", 20, INK, "middle", "700")
        b += text(x, bot + 25, str(t), 18, INK)
    b += text((left + right) / 2, 360, "Vattnets temperatur (°C)", 18, INK, "middle", "700")
    b += f'<text transform="translate(30 {(top+bot)/2}) rotate(-90)" font-size="18" fill="{INK}" text-anchor="middle" font-weight="700">Lösningstid (s)</text>'
    return fig(W, 380, b, "Stapeldiagram: lösningstid 87, 52 och 32 sekunder vid 20, 35 och 50 grader")


FIGS["k1_diagram"] = diagram()


# ---------------------------------------------------------------- 1.5
FLAME = "M0 -24 C6 -12 16 -6 16 8 C16 18 9 24 0 24 C-9 24 -16 18 -16 8 C-16 0 -10 -4 -8 -12 C-4 -8 -2 -6 0 -24Z"


def star(r=7):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = -math.pi / 2 + i * math.pi / 5
        pts.append(f"{rr*math.cos(a):.1f},{rr*math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="#fff"/>'


def drop(x, y, s=1.4):
    return g(f"translate({x} {y}) scale({s})", f'<path d="M0 -8 C5 0 6 4 0 6 C-6 4 -5 0 0 -8Z" fill="{INK}"/>')


SYM = {
    "flame": f'<path d="{FLAME}" fill="{INK}"/>',
    "oxid": g("translate(0 -10) scale(.6)", f'<path d="{FLAME}" fill="{INK}"/>') +
            f'<circle cx="0" cy="12" r="10" fill="none" stroke="{INK}" stroke-width="4.5"/>',
    "corr": drop(-13, -14) + drop(13, -14) +
            f'<rect x="-23" y="4" width="19" height="17" fill="{INK}"/><rect x="4" y="4" width="19" height="17" fill="{INK}"/>',
    "skull": f'<line x1="-20" y1="12" x2="20" y2="25" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
             f'<line x1="20" y1="12" x2="-20" y2="25" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
             f'<circle cx="0" cy="-8" r="12" fill="{INK}"/><rect x="-6" y="0" width="12" height="11" fill="{INK}"/>'
             f'<circle cx="-5" cy="-9" r="3.4" fill="#fff"/><circle cx="5" cy="-9" r="3.4" fill="#fff"/>',
    "excl": f'<text x="0" y="17" font-size="56" font-weight="700" fill="{INK}" text-anchor="middle">!</text>',
    "health": f'<circle cx="0" cy="-17" r="7" fill="{INK}"/>'
              f'<path d="M-15 24 L-15 -4 Q-15 -9 -9 -9 L9 -9 Q15 -9 15 -4 L15 24Z" fill="{INK}"/>'
              + g("translate(0 6)", star(8)),
    "env": f'<path d="M-24 6 L-13 -20 L-2 6Z" fill="{INK}"/><rect x="-15" y="5" width="4" height="9" fill="{INK}"/>'
           f'<ellipse cx="9" cy="14" rx="11" ry="5.5" fill="{INK}"/><path d="M19 14 L27 7 L27 21Z" fill="{INK}"/>'
           f'<circle cx="3" cy="13" r="1.8" fill="#fff"/>'
           f'<line x1="-26" y1="22" x2="26" y2="22" stroke="{INK}" stroke-width="2"/>',
}


def piktogram(x, y, key):
    d = (f'<polygon points="0,-46 46,0 0,46 -46,0" fill="#fff" stroke="{RED}" stroke-width="9" stroke-linejoin="round"/>'
         + SYM[key])
    return g(f"translate({x} {y})", d)


def symboler():
    b = title(W, "Vanliga faropiktogram (CLP)", y=32)
    row1 = [("flame", "Brandfarligt", ["Kan ta eld"]),
            ("oxid", "Oxiderande", ["Förstärker en brand"]),
            ("corr", "Frätande", ["Skadar hud och ögon"]),
            ("skull", "Akut giftigt", ["Giftigt redan i", "liten mängd"])]
    row2 = [("excl", "Irriterande", ["Skadligt i", "mindre grad"]),
            ("health", "Hälsofarligt", ["Allvarlig fara", "på lång sikt"]),
            ("env", "Miljöfarligt", ["Farligt för", "vattenlevande djur"])]
    for i, (k, n, ms) in enumerate(row1):
        x = 80 + 160 * i
        b += piktogram(x, 108, k)
        b += text(x, 178, n, 17, INK, "middle", "700")
        for j, m in enumerate(ms): b += text(x, 198 + 19 * j, m, 15, MUTED)
    for i, (k, n, ms) in enumerate(row2):
        x = 160 + 160 * i
        b += piktogram(x, 296, k)
        b += text(x, 366, n, 17, INK, "middle", "700")
        for j, m in enumerate(ms): b += text(x, 386 + 19 * j, m, 15, MUTED)
    b += text(W / 2, 436, "Förenklad bild – de riktiga piktogrammen ser lite annorlunda ut.", 15, MUTED, italic=True)
    b += text(W / 2, 456, "Två till finns: explosivt (bomb) och gas under tryck (gasflaska).", 15, MUTED, italic=True)
    return fig(W, 474, b, "Förenklade faropiktogram med namn och betydelse")


FIGS["k1_symboler"] = symboler()


# ---------------------------------------------------------------- 1.6
MARK = f'<marker id="aho" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="3.4" markerHeight="3.4" orient="auto"><path d="M0 0L10 5L0 10z" fill="{ORANGE}"/></marker>'


def parrow(x1, y1, x2, y2):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round" marker-end="url(#aho)"/>'


def partikelmodell():
    b = MARK + title(W, "Partikelmodellen: fast, flytande och gas", y=32)
    xs = [20, 230, 440]
    cw, top, ch = 180, 56, 170
    names = ["Fast form", "Vätska", "Gas"]
    for i in range(3):
        b += box(xs[i], top, cw, ch, "", fill="#fff", stroke=GREY, r=14)
        b += text(xs[i] + cw / 2, top + ch + 30, names[i], 21, INK, "middle", "700")
    r = 11
    # fast: regelbundet rutnät, vibrationsstreck
    x0, y0 = xs[0] + 36, top + 30
    for iy in range(5):
        for ix in range(5):
            cx, cy = x0 + ix * 27, y0 + iy * 27
            b += circle(cx, cy, r, BLUE, NAVY, 2)
    for (ix, iy) in [(0, 0), (2, 1), (4, 2), (1, 3), (3, 4)]:
        cx, cy = x0 + ix * 27, y0 + iy * 27
        b += line(cx + 14, cy - 5, cx + 20, cy - 5, ORANGE, 3)
        b += line(cx + 14, cy + 5, cx + 20, cy + 5, ORANGE, 3)
    # vätska: vatten i botten, oregelbundet
    b += f'<rect x="{xs[1]+3}" y="{top+66}" width="{cw-6}" height="{ch-69}" rx="11" fill="{LIGHTBLUE}"/>'
    pos = [(30, 92), (58, 88), (88, 94), (118, 88), (148, 93),
           (44, 118), (73, 122), (103, 116), (134, 121), (160, 117),
           (30, 146), (60, 150), (90, 144), (120, 150), (150, 145)]
    for (px, py) in pos:
        b += circle(xs[1] + px, top + py - 6, r, TEAL, "#2f7f7b", 2)
    for (ax, ay, bx, by) in [(52, 128, 80, 128), (112, 140, 84, 138), (140, 108, 118, 100)]:
        pass
    b += parrow(xs[1] + 62, top + 112, xs[1] + 92, top + 116)
    b += parrow(xs[1] + 126, top + 140, xs[1] + 100, top + 138)
    b += parrow(xs[1] + 40, top + 100, xs[1] + 62, top + 94)
    # gas: få partiklar, långa pilar
    gp = [(40, 42, 20, -14), (120, 40, 26, 16), (70, 92, -22, 22), (145, 100, -24, -18), (45, 140, 24, 6), (118, 148, -10, -22)]
    for (px, py, dx, dy) in gp:
        cx, cy = xs[2] + px, top + py
        b += circle(cx, cy, r, "#9cc7e0", "#4c86ab", 2)
        b += parrow(cx + dx * 0.6, cy + dy * 0.6, cx + dx * 1.9, cy + dy * 1.9)
    descs = [("Tätt, ordnat. Partiklarna", "vibrerar på sina platser."),
             ("Tätt, oordnat. Partiklarna", "glider förbi varandra."),
             ("Långt isär. Partiklarna", "rör sig fritt åt alla håll.")]
    for i, (a, c) in enumerate(descs):
        b += text(xs[i] + cw / 2, top + ch + 56, a, 15, INK)
        b += text(xs[i] + cw / 2, top + ch + 75, c, 15, INK)
    b += text(W / 2, 346, "Orange streck och pilar visar rörelse. Förenklad bild.", 15, MUTED, italic=True)
    return fig(W, 364, b, "Partikelmodellen för fast form, vätska och gas")


FIGS["k1_partikelmodell"] = partikelmodell()


# ---------------------------------------------------------------- 1.7
def tidslinje():
    b = title(W, "Från alkemi till periodiskt system", y=32)
    ly = 190
    b += line(20, ly, 620, ly, GREY, 6)
    b += f'<path d="M620 {ly-12} L640 {ly} L620 {ly+12}Z" fill="{GREY}"/>'
    nodes = [
        (70, "Antiken–medeltiden", ["Alkemi i över 1000 år:", "blanda, värma, destillera"], SAND, True),
        (195, "1700-talet", ["Flogistonteorin", "förklarar förbränning"], "#ecdff3", False),
        (320, "Lavoisier", ["1770–80-talen: förbränning", "är reaktion med syre", "1789: lärobok i kemi"], LIGHTBLUE, True),
        (445, "1869", ["Mendelejev presenterar", "periodiska systemet"], "#dcefc9", False),
        (570, "1875 och 1886", ["Gallium och germanium", "upptäcks och passar", "hans förutsägelser"], "#dcefc9", True),
    ]
    cols = [ORANGE, PURPLE, BLUE, GREEN, GREEN]
    bw = 200
    for (x, t, ls, c, up), col in zip(nodes, cols):
        bh = 38 + 20 * len(ls) + 8
        bx = min(max(x - bw / 2, 8), W - 8 - bw)
        if up:
            by = ly - 36 - bh
            b += line(x, by + bh, x, ly, col, 3)
        else:
            by = ly + 36
            b += line(x, ly, x, by, col, 3)
        b += f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="12" fill="{c}" stroke="{col}" stroke-width="2.5"/>'
        b += text(bx + bw / 2, by + 27, t, 18, INK, "middle", "700")
        for i, l in enumerate(ls):
            b += text(bx + bw / 2, by + 50 + i * 20, l, 15, INK)
        b += circle(x, ly, 11, col, "#fff", 3)
    b += text(W / 2, 355, "Avstånden är inte i skala.", 15, MUTED, italic=True)
    return fig(W, 372, b, "Tidslinje: alkemi, Lavoisier och Mendelejev")


FIGS["k1_tidslinje"] = tidslinje()


# ---------------------------------------------------------------- 1.8
def kallkritik():
    b = title(W, "Granska en källa: fem frågor", y=32)
    rows = [
        ("Vem?", "Vem har skrivit den? Vad kan hen om ämnet?", BLUE, "#dcebf3"),
        ("Varför?", "Vill avsändaren informera, sälja eller påverka?", ORANGE, "#fbe3c4"),
        ("Belägg?", "Finns mätningar, studier eller källor?", GREEN, "#dcefc9"),
        ("När?", "Är den ny eller gammal? Är den uppdaterad?", PURPLE, "#ecdff3"),
        ("Passar?", "Svarar den på just min fråga?", TEAL, "#d8eeec"),
    ]
    for i, (q, d, c, bg) in enumerate(rows):
        y = 54 + i * 68
        b += f'<rect x="20" y="{y}" width="600" height="58" rx="14" fill="{bg}"/>'
        b += f'<rect x="20" y="{y}" width="12" height="58" rx="6" fill="{c}"/>'
        b += badge(58, y + 29, i + 1, c)
        b += text(86, y + 37, q, 24, INK, "start", "700")
        b += text(200, y + 36, d, 16, INK, "start")
        b += f'<rect x="580" y="{y+17}" width="24" height="24" rx="5" fill="#fff" stroke="{c}" stroke-width="3"/>'
    return fig(W, 400, b, "Frågor för att granska en källa: vem, varför, belägg, när och passar den")


FIGS["k1_kallkritik"] = kallkritik()

# gallrade: dekorativ respektive upprepar text/tidslinje/tabell
for _k in ("k1_vardag","k1_tidslinje"):
    FIGS.pop(_k,None)
