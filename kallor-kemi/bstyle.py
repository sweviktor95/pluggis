# -*- coding: utf-8 -*-
"""Gemensam stil för biologihäftena (grön, tvåspaltig med marginalrutor och flik)."""
import html as H

CSS = r"""
@font-face{font-family:Lora;src:url(file:///tmp/fonts/Lora-Regular.ttf);font-weight:400}
@font-face{font-family:Lora;src:url(file:///tmp/fonts/Lora-Bold.ttf);font-weight:700}
@font-face{font-family:Lora;src:url(file:///tmp/fonts/Lora-Italic.ttf);font-weight:400;font-style:italic}
@font-face{font-family:Lora;src:url(file:///tmp/fonts/Lora-BoldItalic.ttf);font-weight:700;font-style:italic}
@font-face{font-family:Carlito;src:url(file:///usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf);font-weight:400}
@font-face{font-family:Carlito;src:url(file:///usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf);font-weight:700}
@font-face{font-family:Carlito;src:url(file:///usr/share/fonts/truetype/crosextra/Carlito-Italic.ttf);font-weight:400;font-style:italic}
:root{--g1:#7a1f1f;--g2:#a8322a;--g3:#c9594f;--ink:#241712;--mut:#6b625b;--line:#d9d2c8}
@page{size:A4;margin:14mm 14.8mm 17mm 18mm;
 @bottom-left{content:"__FOOT__";font:8.4pt Carlito;color:#6b625b;margin-top:6mm}
 @bottom-right{content:counter(page);font:700 8.8pt Carlito;color:var(--g2);margin-top:6mm}}
*{box-sizing:border-box}
html,body{margin:0}
html{counter-reset:page __START__}
body{font-family:Lora,serif;font-size:10.1pt;line-height:1.46;color:var(--ink)}
.tab{position:fixed;right:-14.8mm;top:22mm;width:7.5mm;height:21mm;background:var(--g2);border-radius:3mm 0 0 3mm;color:#fff;font:700 11pt Carlito;display:flex;align-items:center;justify-content:center;z-index:5}
.sec{break-before:page}
.sec:first-of-type{break-before:auto}
.sh{display:flex;align-items:center;gap:8pt;margin:0 0 9pt;break-after:avoid}
.sh .nr{background:var(--g2);color:#fff;font:700 13pt Carlito;padding:2.5pt 8pt;border-radius:5pt;letter-spacing:.2pt}
.sh h2{font:700 22pt Carlito;margin:0;color:var(--g1);line-height:1.1}
.sh.small h2{font-size:20pt}
h3{font:700 13pt Carlito;color:var(--g2);margin:11pt 0 4pt;break-after:avoid}
p{margin:0 0 6.5pt}
em{font-style:italic}
strong,b{font-weight:700}
.green{color:var(--g2)}
.row{display:grid;grid-template-columns:minmax(0,1fr) 47mm;column-gap:6mm;margin:0 0 8pt;align-items:start}
.row.one{grid-template-columns:minmax(0,1fr)}
.row.w{display:grid;grid-template-columns:minmax(0,1fr) 62mm;column-gap:6mm;margin:0 0 8pt;align-items:start}
.row.w .side{margin-top:2pt}
.side{display:flex;flex-direction:column;gap:7pt;margin-top:2pt}
.bx{border-radius:5pt;padding:7pt 9pt;font:8.9pt/1.35 Carlito;break-inside:avoid}
.bx .rb{display:block;font:700 7.8pt Carlito;letter-spacing:.9pt;text-transform:uppercase;margin-bottom:3pt}
.bx b.t{display:block;font:700 9pt Carlito;color:var(--ink);margin-top:4pt}
.bx p{margin:0 0 3pt;font:8.9pt/1.35 Carlito}
.bx.begrepp{background:#fff5d6}.bx.begrepp .rb{color:#a8651a}
.bx.tank{background:#fdefe3}.bx.tank .rb{color:#a84d22}
.bx.visste{background:#f7e6e4}.bx.visste .rb{color:var(--g2)}
.bx.klimat{background:#dcebf2}.bx.klimat .rb{color:#2b6a8a}
.bx.kvave{background:#e9f2e2}.bx.kvave .rb{color:#4a7a2c}
.bx.varning{background:#fde8e1}.bx.varning .rb{color:#a83a22}
.bx.fundera{background:#fdefe3}.bx.fundera .rb{color:#a84d22}
.fig{margin:2pt 0 8pt;break-inside:avoid}
.fig img{width:100%;display:block;border-radius:6pt}
.cap{font:8.4pt/1.3 Carlito;color:var(--mut);margin-top:3pt}
.cap b{color:var(--ink)}
ul.pu{margin:0 0 7pt;padding:0;list-style:none}
ul.pu li{position:relative;padding-left:12pt;margin:0 0 3pt}
ul.pu li:before{content:"•";position:absolute;left:2pt;color:var(--ink)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:8pt;margin:3pt 0 7pt}
.card{background:#fbf0ef;border-top:2pt solid var(--g3);border-radius:0 0 5pt 5pt;padding:6pt 8pt;font:8.9pt/1.35 Carlito;break-inside:avoid}
.card b.h{display:block;font:700 10pt Carlito;color:var(--g2);margin-bottom:3pt}
.steps{list-style:none;margin:0 0 6pt;padding:0;counter-reset:s}
.steps li{counter-increment:s;position:relative;padding-left:20pt;margin:0 0 4.5pt}
.steps li:before{content:counter(s);position:absolute;left:0;top:1pt;width:13pt;height:13pt;border-radius:50%;background:#e0782f;color:#fff;font:700 8pt/13pt Carlito;text-align:center}
.steps.g li:before{background:var(--g2)}
.kolla{border:1.7pt solid var(--g3);border-radius:7pt;padding:8pt 13pt;margin:10pt 0 0;break-inside:avoid;font:9.6pt Carlito}
.kolla .kr{display:block;font:700 8.6pt Carlito;letter-spacing:1pt;color:var(--g2);margin-bottom:3pt;text-transform:uppercase}
.kolla ol{margin:0;padding-left:15pt}.kolla li{margin:0 0 2pt}
.tbl{width:100%;border-collapse:collapse;font:8.6pt/1.3 Carlito;margin:3pt 0 8pt}
.tbl th{background:#fff;text-align:left;padding:4pt 5pt;border:.7pt solid var(--line);font-weight:700;color:var(--ink)}
.tbl td{padding:4pt 5pt;border:.7pt solid var(--line);vertical-align:top}
.tbl td:first-child{font-weight:700}
.tbl.num td:first-child{font-weight:400}
.pill{break-after:avoid;display:block;width:fit-content;background:var(--g2);color:#fff;font:700 8pt Carlito;letter-spacing:.9pt;padding:2.5pt 8pt;border-radius:4pt;margin:0 0 5pt;text-transform:uppercase}
.q{display:grid;grid-template-columns:16pt minmax(0,1fr) 22pt;gap:7pt;margin:0 0 9pt;font:9.8pt/1.4 Carlito;break-inside:avoid}
.q .n{width:14pt;height:14pt;border-radius:50%;background:var(--g2);color:#fff;font:700 8.5pt/14pt Carlito;text-align:center}
.q .pts{text-align:right;font:700 9pt Carlito;color:var(--ink)}
.q .alts{display:grid;grid-template-columns:1fr 1fr;gap:1pt 14pt;margin-top:3pt}
.q .alts.one{grid-template-columns:1fr}
.q .alts div{padding-left:0}
.lines{margin-top:4pt}.lines i{display:block;height:15pt;border-bottom:.7pt solid #bdb6ad}
.sam{background:#f7e6e4;border-radius:8pt;padding:10pt 14pt;margin:0 0 12pt;font:10pt/1.4 Carlito}
.sam ul{margin:0;padding:0;list-style:none}.sam li{position:relative;padding-left:11pt;margin:0 0 3.5pt}.sam li:before{content:"•";position:absolute;left:1pt}
.begr{columns:2;column-gap:16pt;font:9.2pt/1.3 Carlito}
.begr div{break-inside:avoid;margin:0 0 6pt}.begr b{display:block;color:var(--g2);font-size:9.6pt}
.teacher h2{font:700 19pt Carlito;color:var(--g1);margin:0 0 6pt}
.teacher h3{font-size:12pt}
.teacher{font:9.3pt/1.38 Carlito}
.teacher p{font:9.3pt/1.38 Carlito}
.cols2{columns:2;column-gap:16pt}
.cols2 p{break-inside:avoid-column}
.lab-h{display:flex;gap:8pt;align-items:baseline}
.mut{color:var(--mut)}
.note{font:8.2pt/1.35 Carlito;color:var(--mut)}
.pg{break-before:page}
.avoid{break-inside:avoid}
.fake{display:inline-block;background:#fde8e1;color:#a83a22;font:700 7.6pt Carlito;letter-spacing:.7pt;text-transform:uppercase;padding:1pt 6pt;border-radius:4pt;margin:0 5pt 2pt 0}
.fakeann{margin:0 0 -2pt}
"""


import os as _os
DYS_TEXT = r"""
body{font-family:"Liberation Sans",Arial,sans-serif;font-size:12pt;line-height:1.62;letter-spacing:.012em;word-spacing:.07em;text-align:left}
p,.t p{font-family:"Liberation Sans",Arial,sans-serif;font-size:12pt;line-height:1.62;margin:0 0 9pt}
em,i{font-style:normal;font-weight:700}
.green{font-weight:700}
.row{grid-template-columns:minmax(0,1fr) 54mm}
.row.w{grid-template-columns:minmax(0,1fr) 62mm}
.bx,.bx p,.card,.kolla,.sam,.begr,.ord2 div,.stp div,.arg,.teacher,.teacher p,.teacher .hl,.cap,.vik{font-family:"Liberation Sans",Arial,sans-serif;font-size:10.8pt;line-height:1.5;letter-spacing:.01em}
.bx b.t,.card b.h,.begr b,.ord2 b{font-size:11.2pt}
.tbl,table.tb,.sf,.dr,.nrbox,.ln,.fy p,.bank,.chips span,.sort div{font-family:"Liberation Sans",Arial,sans-serif;font-size:10.8pt;line-height:1.45}
.q,.q .alts{font-family:"Liberation Sans",Arial,sans-serif;font-size:11pt;line-height:1.5}
.ex1 .q{font-size:12.5pt}
.kom .tx{font-size:13pt;font-family:"Liberation Sans",Arial,sans-serif}
.t p{font-size:13pt}
.note{font-size:9.8pt}
h3{font-size:14.5pt;margin-top:13pt}
.bx .rb,.kolla .kr,.pill,.fake,.kom .lb,.ex1 .ty,.sh .nr{text-transform:none;letter-spacing:.4pt;font-size:9.6pt}
.kolla ol,.kolla li{font-size:11pt}
ul.pu li,.steps li{font-size:inherit}
"""

# Dyslexivänlig typografi är pausad. Starta med DYS=1 i miljön för att slå på den igen.
DYS = DYS_TEXT if _os.environ.get("DYS") == "1" else ""

def css(foot, start=2):
    return CSS.replace("__FOOT__", foot).replace("__START__", str(start-1))

def esc(s):
    return H.escape(s)

# ---- byggstenar -------------------------------------------------------
import re as _re
def shownr(nr):
    return '' if _re.fullmatch(r'F?\d+\.\d+\.\d+', str(nr)) else nr

def head(nr, titel, small=False):
    nr = shownr(nr)
    n = f'<span class="nr">{nr}</span>' if nr else ''
    return f'<div class="sh{" small" if small else ""}">{n}<h2>{titel}</h2></div>'

def fig(src, cap=None, w=None):
    st = f' style="width:{w}"' if w else ""
    c = f'<div class="cap">{cap}</div>' if cap else ""
    return f'<div class="fig"{st}><img src="file://{src}">{c}</div>'

def box(typ, rub, body, extra=""):
    return f'<div class="bx {typ}"><span class="rb">{rub}</span>{body}</div>'

def begrepp(items):
    return '<div class="bx begrepp"><span class="rb">Begrepp</span>' + "".join(
        f'<b class="t">{t}</b><p>{d}</p>' for t, d in items) + '</div>'

def row(main, side=None):
    if side:
        return f'<div class="row"><div class="main">{main}</div><div class="side">{"".join(side)}</div></div>'
    return f'<div class="row one"><div class="main">{main}</div></div>'

def bullets(items):
    return '<ul class="pu">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def steps(items, g=False):
    return f'<ol class="steps{" g" if g else ""}">' + "".join(f"<li>{x}</li>" for x in items) + "</ol>"

def cards(items):
    return '<div class="cards">' + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in items) + "</div>"

def kolla(nr, qs):
    nr = shownr(nr)
    return f'<div class="kolla"><span class="kr">Kolla dig själv {nr}</span><ol>' + "".join(f"<li>{q}</li>" for q in qs) + "</ol></div>"

def table(head_, rows, cls="tbl"):
    h = "<tr>" + "".join(f"<th>{c}</th>" for c in head_) + "</tr>" if head_ else ""
    return f'<table class="{cls}">{h}' + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"

def lines(n):
    return '<div class="lines">' + "<i></i>" * n + "</div>"

def section(inner, tab=True):
    return f'<section class="sec">{inner}</section>'
