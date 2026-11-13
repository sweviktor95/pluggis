# -*- coding: utf-8 -*-
from kfig_common import *

# ---------- v_utrustning ------------------------------------------------------
W, H = 1500, 672
b = ''
b += shelf(40, 1460, 330) + shelf(40, 1460, 598)
b += beaker(95, 160, 130, 170, 0.5)
b += cylinder(400, 70, 46, 260, 0.55)
b += flask(630, 105, 170, 225, 0.35)
b += tube(912, 190, 140, "#bcd9ec", .5) + tube(962, 190, 140, "#f4c7cf", .45) + tube(1012, 190, 140, "#f6e3a8", .4)
b += '<rect x="895" y="228" width="170" height="14" rx="5" fill="#a9703c"/><rect x="895" y="318" width="170" height="12" rx="5" fill="#a9703c"/><rect x="898" y="228" width="10" height="100" fill="#a9703c"/><rect x="1052" y="228" width="10" height="100" fill="#a9703c"/>'
b += thermometer(1265, 80, 190, 0.45)
for x, n in [(160, "Bägare"), (423, "Mätcylinder"), (715, "E-kolv"), (980, "Provrör i ställ"), (1290, "Termometer")]:
    b += T(x, 372, n, 30, INK, "700")
b += balance(90, 520, 170, "12,4 g", 26)
b += pipette(430, 462, 0.8)
b += goggles(730, 565, 0.9)
b += f'<circle cx="1000" cy="545" r="52" fill="#fff" stroke="{LINE}" stroke-width="6"/><rect x="988" y="482" width="24" height="14" rx="4" fill="{LINE}"/><path d="M1000,545 L1000,512 M1000,545 L1024,556" stroke="{RED}" stroke-width="6" stroke-linecap="round"/><circle cx="1000" cy="545" r="6" fill="{INK}"/>'
for k in range(12):
    a = math.radians(k * 30)
    b += f'<path d="M{1000+44*math.sin(a):.1f},{545-44*math.cos(a):.1f} L{1000+50*math.sin(a):.1f},{545-50*math.cos(a):.1f}" stroke="{MUT}" stroke-width="3"/>'
b += f'<g transform="translate(1290,560) rotate(-20)"><rect x="-90" y="-7" width="150" height="14" rx="7" fill="#c9d1d6" stroke="{LINE}" stroke-width="3"/><ellipse cx="78" cy="0" rx="26" ry="14" fill="#c9d1d6" stroke="{LINE}" stroke-width="3"/></g>'
for x, n in [(175, "Våg"), (430, "Pipett"), (730, "Skyddsglasögon"), (1000, "Stoppur"), (1290, "Spatel")]:
    b += T(x, 642, n, 30, INK, "700")
render('v_utrustning', svg(W, H, b, BG), W, H, 1)

# ---------- v_piktogram (detaljerade GHS-piktogram i mkpikto.py) ----------
exec(open('mkpikto.py').read())

# ---------- v_menisk ----------------------------------------------------------
W, H = 1500, 640
b = ''
cx0, cy0, cw, chh = 640, 70, 90, 470
b += cylinder(cx0, cy0, cw, chh, 0.58, nt=10)
ly = cy0 + chh * (1 - 0.58)
def eye(x, y):
    return (f'<g transform="translate({x},{y})"><path d="M-34,0 Q0,-30 34,0 Q0,30 -34,0Z" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="8" cy="0" r="11" fill="#3a6f9c"/><circle cx="11" cy="0" r="5" fill="#111"/></g>')
for (ey, lab, ok) in [(ly - 130, "För högt", False), (ly, "Rätt", True), (ly + 130, "För lågt", False)]:
    colr = "#2f8a4f" if ok else RED
    b += eye(300, ey)
    b += f'<path d="M345,{ey} L{cx0-12},{ly+4}" stroke="{colr}" stroke-width="4.5" stroke-dasharray="{"0" if ok else "12 8"}" fill="none"/>'
    b += T(300, ey + 62 if ey > ly - 10 else ey - 40, lab, 30, colr, "700")
b += f'<path d="M{cx0+cw+16},{ly+5} h60" stroke="{RED}" stroke-width="5"/>'
zx, zy, zr = 1130, 230, 150
b += f'<circle cx="{zx}" cy="{zy}" r="{zr}" fill="#fff" stroke="{LINE}" stroke-width="6"/>'
b += f'<clipPath id="zc"><circle cx="{zx}" cy="{zy}" r="{zr-4}"/></clipPath><g clip-path="url(#zc)"><rect x="{zx-zr}" y="{zy-zr}" width="{2*zr}" height="{2*zr}" fill="#f2f7fa"/>'
b += f'<path d="M{zx-zr},{zy-50} Q{zx-100},{zy-48} {zx-60},{zy+8} Q{zx},{zy+40} {zx+60},{zy+8} Q{zx+100},{zy-48} {zx+zr},{zy-50} L{zx+zr},{zy+zr} L{zx-zr},{zy+zr}Z" fill="#bcd9ec"/>'
b += f'<path d="M{zx-zr},{zy-50} Q{zx-100},{zy-48} {zx-60},{zy+8} Q{zx},{zy+40} {zx+60},{zy+8} Q{zx+100},{zy-48} {zx+zr},{zy-50}" stroke="#4a86b3" stroke-width="5" fill="none"/>'
b += f'<path d="M{zx-zr},{zy+26} h{2*zr}" stroke="{RED}" stroke-width="4.5" stroke-dasharray="14 8"/></g>'
b += f'<path d="M{cx0+cw+16+60},{ly+5} L{zx-zr+14},{zy+60}" stroke="{MUT}" stroke-width="3" stroke-dasharray="4 7"/>'
b += T(zx, 428, "Vattenytan kröker sig nedåt (menisk).", 28, INK, "700")
b += T(zx, 462, "Läs av vid den lägsta punkten,", 26, MUT)
b += T(zx, 492, "med ögonen i samma höjd.", 26, MUT)
b += T(zx, 540, "Annars blir avläsningen fel (parallaxfel).", 26, RED, "700")
render('v_menisk', svg(W, H, b, BG), W, H, 1)
