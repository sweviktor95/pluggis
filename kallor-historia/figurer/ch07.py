# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp/figs")
from svgkit import *

P_YEL="#f8e6a8"; P_BLU="#cfe3f1"; P_GRN="#d4e8c2"; P_RED="#f3c9c0"; P_ORG="#f8d9b8"; P_PUR="#e2d8ee"; P_TEA="#c9e6e4"; WHITE="#ffffff"
FIGS = {}

# ---------- 7.1 jordbrukssamhälle -> industrisamhälle
def f1():
    b = title(640, "Från jordbrukssamhälle till industrisamhälle")
    b += box(15, 52, 270, 44, ["Jordbrukssamhälle (före)"], P_YEL, size=18)
    b += box(355, 52, 270, 44, ["Industrisamhälle (efter)"], P_BLU, size=18)
    rows = [("Var bor man?", "Mest på landet", "I städer nära fabriker"),
            ("Vad arbetar man med?", "Jordbruk, familjen gör själv", "Fabriker och maskiner"),
            ("Vad ger kraften?", "Muskler, vind och vatten", "Kol och ångmaskin"),
            ("Vad styr dagen?", "Årstiderna och solen", "Klockan och maskinen")]
    for i, (q, a, c) in enumerate(rows):
        y = 108 + i * 66
        b += box(15, y, 270, 58, [q, a], P_YEL, size=16)
        b += box(355, y, 270, 58, [q, c], P_BLU, size=16)
        b += arrow(292, y + 29, 348, y + 29, width=3)
    b += text(320, 392, "Industrialiseringen: samhället går från jordbruk till industri och tjänster", 16, MUTED, italic=True)
    return fig(640, 410, b, "Jämförelse mellan jordbrukssamhälle och industrisamhälle")
FIGS["h7_fore"] = None

# ---------- 7.2
def f2():
    b = title(640, "Orsaker som samverkade i Storbritannien")
    b += box(205, 150, 230, 90, ["Industrialiseringen", "börjar omkring 1760"], P_ORG, stroke=ORANGE, size=18)
    items = [(15, 55, "Kol", "billig energi, ersatte ved", P_GRN),
             (225, 55, "Järnmalm", "material till maskiner", P_GRN),
             (435, 55, "Kapital", "pengar att satsa", P_YEL),
             (15, 285, "Kolonier och handel", "råvaror och marknader", P_BLU),
             (225, 285, "Jordbruksrevolution", "mat och arbetskraft", P_PUR),
             (435, 285, "Stabil politik", "trygghet och patent", P_TEA)]
    for x, y, t, s, f in items:
        b += box(x, y, 190, 66, [t, s], f, size=16)
    # pilar
    b += arrow(110, 123, 235, 148)
    b += arrow(320, 123, 320, 148)
    b += arrow(530, 123, 405, 148)
    b += arrow(110, 283, 235, 242)
    b += arrow(320, 283, 320, 242)
    b += arrow(530, 283, 405, 242)
    b += text(320, 382, "Historiker är inte helt överens om vilken orsak som vägde tyngst", 15, MUTED, italic=True)
    return fig(640, 400, b, "Orsaker till industrialiseringen i Storbritannien")
FIGS["h7_britannien"] = None

# ---------- 7.3 ångmaskin
def f3():
    b = title(640, "Så fungerar en ångmaskin")
    names = [("Eld", "kol bränns"), ("Ånga", "vattnet kokar"), ("Kolv", "ångan trycker"), ("Hjul", "maskiner rör sig")]
    fills = [P_ORG, P_BLU, P_GRN, P_YEL]
    for i, (n, s) in enumerate(names):
        x = 15 + i * 160
        b += rect(x, 55, 130, 155, WHITE, "#d8cfae", 14)
        b += badge(x + 18, 73, i + 1, r=14)
        cx, cy = x + 65, 112
        if i == 0:   # låga
            b += path(f"M{cx} {cy-30} C{cx+22} {cy-8} {cx+26} {cy+10} {cx} {cy+24} C{cx-26} {cy+10} {cx-22} {cy-8} {cx} {cy-30}Z", ORANGE, RED, 2)
            b += path(f"M{cx} {cy-6} C{cx+10} {cy+4} {cx+10} {cy+12} {cx} {cy+22} C{cx-10} {cy+12} {cx-10} {cy+4} {cx} {cy-6}Z", YELLOW, "none", 0)
        elif i == 1:  # ånga
            for dx in (-22, 0, 22):
                b += path(f"M{cx+dx} {cy+24} C{cx+dx-12} {cy+10} {cx+dx+12} {cy} {cx+dx} {cy-12} C{cx+dx-10} {cy-22} {cx+dx+8} {cy-26} {cx+dx} {cy-32}", "none", BLUE, 4)
        elif i == 2:  # kolv
            b += rect(cx - 40, cy - 22, 80, 44, LIGHTBLUE, NAVY, 4)
            b += rect(cx - 8, cy - 18, 16, 36, NAVY, None, 2)
            b += line(cx + 8, cy, cx + 48, cy, NAVY, 5)
            b += arrow(cx - 20, cy + 36, cx + 20, cy + 36, NAVY, 3)
        else:         # hjul
            b += circle(cx, cy, 30, "none", NAVY, 5)
            for k in range(6):
                import math
                a = k * math.pi / 3
                b += line(cx, cy, round(cx + 30 * math.cos(a), 1), round(cy + 30 * math.sin(a), 1), NAVY, 3)
            b += circle(cx, cy, 6, NAVY)
        b += text(x + 65, 172, n, 18, INK, "middle", "700")
        b += text(x + 65, 196, s, 15, INK)
        if i < 3:
            b += arrow(x + 134, 132, x + 156, 132, width=3)
    b += box(15, 226, 305, 66, ["Newcomen, 1712", "pumpade vatten ur gruvor"], P_BLU, size=16)
    b += box(335, 226, 290, 66, ["Watt, patent 1769", "kunde driva en axel och maskiner"], P_BLU, size=16)
    b += box(15, 306, 610, 60, ["Fri från vind och vattenfall", "Fabriken kan ligga var som helst, även mitt i en stad"], P_GRN, size=17)
    return fig(640, 380, b, "Ångmaskinens princip: eld, ånga, kolv, hjul")
FIGS["h7_maskiner"] = None

# ---------- 7.4 arbetsdag
def f4():
    b = title(640, "Hur många timmar fick man arbeta per dag?")
    x0, sc = 30, 40.0   # 33 px per timme
    for h in (0, 3, 6, 9, 12):
        b += line(x0 + h * sc, 100, x0 + h * sc, 300, "#d8cfae", 2, dash=True)
        b += text(x0 + h * sc, 322, str(h), 16, MUTED)
    b += text(320, 346, "timmar per dag", 16, MUTED)
    bars = [("Fabriksarbetare, vuxen (vanligt): tolv timmar eller mer", 12, RED, "12+"),
            ("Barn 9–13 år, England efter lagen 1833: högst", 9, ORANGE, "9"),
            ("Barn under 14 år, Sverige efter 1881: högst", 6, TEAL, "6")]
    for i, (lab, hrs, col, val) in enumerate(bars):
        y = 66 + i * 76
        b += text(x0, y + 4, lab, 16, INK, "start")
        b += rect(x0, y + 14, hrs * sc, 34, col, None, 6)
        b += text(x0 + hrs * sc + 10, y + 39, val + " h", 18, INK, "start", "700")
    b += text(320, 372, "Sex dagar i veckan. Barn under 9 år fick inte arbeta i textilfabrik (1833).", 15, MUTED, italic=True)
    return fig(640, 392, b, "Arbetstid per dag för vuxna och barn")
FIGS["h7_fabrik"] = None

# ---------- 7.5 staden
def f5():
    b = title(640, "Urbanisering: från landsbygd till stad")
    b += box(15, 48, 180, 56, ["Landsbygd"], P_YEL, size=18)
    b += arrow(200, 76, 440, 76, width=4)
    b += text(320, 66, "urbanisering", 17, INK, "middle", "700")
    b += box(445, 48, 180, 56, ["Stad med fabriker"], P_BLU, size=17)
    b += box(15, 120, 300, 90, ["Möjligheter", "lön i pengar, nya yrken,", "mer frihet från släkten"], P_GRN, size=16)
    b += box(325, 120, 300, 90, ["Problem", "trångt, inget rent vatten", "och avlopp: kolera, tyfus"], P_RED, size=16)
    b += text(320, 238, "Nya klasser i samhället", 18, INK, "middle", "700")
    b += box(160, 250, 320, 44, ["Borgerskap: ägde fabriker och banker"], P_PUR, size=16, title_bold=False)
    b += box(100, 300, 440, 44, ["Medelklass: tjänstemän, lärare, handlare"], P_TEA, size=16, title_bold=False)
    b += box(40, 350, 560, 44, ["Arbetarklass: fabriksarbetare, låga löner, trångbodda"], P_ORG, size=16, title_bold=False)
    return fig(640, 410, b, "Urbanisering och de nya klasserna")
FIGS["h7_staden"] = None

# ---------- 7.6 arbetarrörelsen
def f6():
    b = title(640, "Så växte arbetarrörelsen fram")
    rows = [("Enskild arbetare", "Ensam har man ingen makt mot fabriksägaren", "", P_RED),
            ("Fackförening (LO bildas 1898)", "Förhandlar om lön och villkor. Strejk mot lockout.", "", P_YEL),
            ("Parti och folkrörelser", "SAP 1889: allmän rösträtt, kortare arbetsdag, skydd", "Även bildningsförbund och nykterhetsrörelsen", P_BLU)]
    for i, (t, s1, s2, f) in enumerate(rows):
        y = 52 + i * 98
        ls = [t, s1] + ([s2] if s2 else [])
        b += box(60, y, 565, 76, ls, f, size=16)
        b += badge(30, y + 38, i + 1)
        if i < 2:
            b += arrow(342, y + 78, 342, y + 96)
    b += box(60, 350, 565, 52, ["Resultat: nya lagar, demokrati och välfärd"], P_GRN, stroke=GREEN, size=17)
    b += arrow(342, 328, 342, 348)
    return fig(640, 420, b, "Från enskild arbetare till fackförening och parti")
FIGS["h7_rorelsen"] = None

# ---------- 7.7 Sverige
def f7():
    b = title(640, "Sverige: industri och utvandring")
    b += box(15, 50, 200, 96, ["Naturtillgångar", "skog, järnmalm,", "vattenkraft"], P_GRN, size=16)
    b += arrow(220, 98, 250, 98)
    b += box(255, 50, 370, 96, ["Industrin växer", "järnväg 1856, stål 1858, dynamit 1867,", "telefoner 1876, sågverk i Norrland"], P_BLU, size=16)
    b += box(15, 166, 200, 110, ["Skäl att åka", "fattigdom, missväxt,", "ingen egen jord"], P_RED, size=16)
    b += arrow(220, 221, 250, 221)
    b += text(255, 182, "Utvandrare 1851–1910 (ungefär)", 17, INK, "start", "700")
    b += rect(255, 194, 370, 36, GREY, None, 8)
    b += rect(255, 194, 305, 36, BLUE, None, 8)
    b += text(407, 218, "nästan 1 miljon till USA", 16, "#fff", "middle", "700")
    b += text(255, 254, "Hela stapeln: ungefär 1,2 miljoner svenskar", 16, INK, "start")
    b += text(255, 274, "Värsta året 1887: omkring 46 000 till USA", 16, INK, "start")
    b += box(15, 296, 610, 62, ["Lockelser i Amerika", "billig jord och arbete, särskilt i Mellanvästern (Minnesota, Illinois)"], P_YEL, size=16)
    return fig(640, 374, b, "Industrialisering och utvandring i Sverige")
FIGS["h7_sverige"] = None

# ---------- 7.8 kontinuitet och förändring
def f8():
    b = title(640, "Kontinuitet och förändring")
    b += box(15, 48, 300, 42, ["Kontinuitet (likt)"], P_YEL, size=18)
    b += box(325, 48, 300, 42, ["Förändring (nytt)"], P_BLU, size=18)
    rows = [(["Många var fortfarande fattiga"], ["Arbetet flyttade till", "fabriker och städer"]),
            (["Barn arbetade"], ["Dagen styrdes av", "klockan och maskinen"]),
            (["Män hade makt och", "bestämde mest"], ["Nya klasser och", "arbetarrörelse"]),
            (["Behov av mat, bostad", "och trygghet"], ["Billigare varor, snabbare", "resor, boende i städer"])]
    for i, (l, r) in enumerate(rows):
        y = 100 + i * 62
        b += box(15, y, 300, 54, l, P_YEL, size=16, title_bold=False)
        b += box(325, y, 300, 54, r, P_BLU, size=16, title_bold=False)
    b += box(15, 350, 610, 56, ["Miljöpris", "kolrök, förorenade floder, avverkade skogar, mer koldioxid"], P_RED, size=16)
    return fig(640, 420, b, "Kontinuitet och förändring under industrialiseringen")
FIGS["h7_foljder"] = None

for k, fn in [("h7_fore", f1), ("h7_britannien", f2), ("h7_maskiner", f3), ("h7_fabrik", f4),
              ("h7_staden", f5), ("h7_rorelsen", f6), ("h7_sverige", f7), ("h7_foljder", f8)]:
    FIGS[k] = fn()

# gallrade: duplicerar tabellerna i texten
for _k in ("h7_staden","h7_foljder"):
    FIGS.pop(_k,None)
