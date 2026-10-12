# -*- coding: utf-8 -*-
"""Exporterar område 1 (tre nivåer) till sajtens innehållsfil + scoped CSS."""
import os, re, json, sys
os.environ['CH'] = '01n'
sys.path.insert(0, '/tmp/bio')
import bbuild_latt as BL
import ch01n as G
import ch01n_fordj as F
import bstyle

IMG = ("file:///tmp/bio/fig01n/", "bilder/biologi-omrade1/")
def fix(h): return h.replace(*IMG)

# Lättläst: delar 1..9
L = BL.L
latt = {i: BL.lasa_page(i, d) + BL.ova_page(i, d) for i, d in enumerate(L.DELAR, 1)}
GS = [inner for nr, t, inner in G.S]
grund = {"Start": GS[0], "1.1.1": GS[1], "1.1.2": GS[2], "1.1.3": GS[3], "L1": GS[4], "1.2.1": GS[5], "1.2.2": GS[6], "1.2.3": GS[7], "L2": GS[8]}
fordj = {nr: inner for nr, t, inner in F.S}

M = {
 "biologi-m-1-1-1": dict(latt=latt[1] + latt[2], van=grund["Start"] + grund["1.1.1"], ford=fordj["F1.1.1"]),
 "biologi-m-1-1-2": dict(latt=latt[3], van=grund["1.1.2"], ford=fordj["F1.1.2"]),
 "biologi-m-1-1-3": dict(latt=latt[4], van=grund["1.1.3"], ford=fordj["F1.1.3"]),
 "biologi-m-1-1-l": dict(latt=latt[5], van=grund["L1"], ford=None),
 "biologi-m-1-2-1": dict(latt=latt[6], van=grund["1.2.1"], ford=fordj["F1.2.1"]),
 "biologi-m-1-2-2": dict(latt=latt[7], van=grund["1.2.2"], ford=fordj["F1.2.2"]),
 "biologi-m-1-2-3": dict(latt=latt[8], van=grund["1.2.3"], ford=fordj["F1.2.3"]),
 "biologi-m-1-2-l": dict(latt=latt[9], van=grund["L2"], ford=None),
}

head_start = '<h3>Vad är biologi?</h3>'
M["biologi-m-1-1-1"]["van"] = head_start + grund["Start"] + "<h3>Från fråga till plan</h3>" + grund["1.1.1"]
M["biologi-m-1-1-1"]["latt"] = latt[1] + latt[2]

out = ["// Genereras av kallor-biologi/omrade1/exportsite.py – ändra inte för hand.",
       "// Biologi område 1: varje moment finns i tre nivåer (lättläst, grundtext, fördjupning). Elevversion, utan facit.",
       "var innehall = window.innehall || {};"]
for id_, d in M.items():
    niv = {}
    if d["latt"]: niv["lattlast"] = fix(d["latt"])
    if d["van"]: niv["vanlig"] = fix(d["van"])
    if d["ford"]: niv["fordjupning"] = fix(d["ford"])
    out.append('innehall[%s] = {nivaer: %s, nivaStandard: "vanlig"};' % (json.dumps(id_), json.dumps(niv, ensure_ascii=False)))
open('/home/claude/pluggis/innehall/biologi-omrade1.js', 'w').write("\n".join(out) + "\n")

# CSS scopad under .bok
STACK = 'Carlito,Calibri,"Segoe UI",Arial,sans-serif'
raw = bstyle.CSS + BL.LCSS
raw = re.sub(r'@font-face\{[^}]*\}', '', raw)
raw = re.sub(r'@page\{(?:[^{}]|\{[^{}]*\})*\}', '', raw)
raw = re.sub(r'@page[^{]*\{(?:[^{}]|\{[^{}]*\})*\}', '', raw)
raw = raw.replace('Carlito', STACK).replace('Lora,serif', 'Lora,Georgia,serif')
def scope(m):
    sels, body = m.group(1), m.group(2)
    outs = []
    for s_ in sels.split(','):
        s_ = s_.strip()
        if s_ in ('html', 'body', ':root', '*'):
            outs.append('.bok' if s_ != '*' else '.bok,.bok *')
        elif s_.startswith('html') or s_.startswith('body'):
            continue
        else: outs.append('.bok ' + s_)
    return ','.join(outs) + '{' + body + '}'
css = re.sub(r'([^{}@]+)\{([^{}]*)\}', scope, raw)
css = css.replace('.bok{margin:0}', '.bok{margin:0}')
extra = """
.bok{font-size:16px;line-height:1.55;max-width:860px}
.bok .sec{break-before:auto;margin:0 0 26px}
.bok .tab{display:none}
.bok{--g1:#245040;--g2:#2f6b4f;--g3:#4f8a63;--ink:#241712;--mut:#6b625b;--line:#d9d2c8}
.bok .sh .nr{display:none}
.bok img{max-width:100%;height:auto}
.bok .fig{max-width:100%}
.bok table{max-width:100%}
.bok .tbl,.bok table.tb{display:block;overflow-x:auto}
.nivaer{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px}
.nivaer button{font:inherit;padding:8px 14px;border:2px solid #2f6b4f;background:#fff;color:#245040;border-radius:999px;cursor:pointer}
.nivaer button.aktiv{background:#2f6b4f;color:#fff}
@media(max-width:720px){.bok .row,.bok .row.w{grid-template-columns:1fr}.bok .cards{grid-template-columns:1fr!important}.bok .begr,.bok .cols2{columns:1}}
"""
open('/home/claude/pluggis/innehall/biologi-bok.css','w').write(css + extra)
print(len(css), [ (k, list(json.loads(json.dumps({a:1 for a in ["x"]})))) for k in []])
