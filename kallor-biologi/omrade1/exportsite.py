# -*- coding: utf-8 -*-
"""Exporterar område 1 (tre nivåer) till sajtens innehållsfil + scoped CSS."""
import os, re, json, sys
os.environ['CH'] = '01n'
sys.path.insert(0, '/tmp/bio')
import bbuild_latt as BL
import ch01n as G
import ch01n_fordj as F
import bstyle
import bbuild_n as BN

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

M["biologi-m-1-s"] = dict(latt=BL.ord_page() + BL.viktigast_page(), van=BN.sam_html(G.SAMMAN, G.BEGR), ford=None)
M["biologi-m-1-t"] = dict(latt=BL.test_pages(), van=BN.test_html(G), ford=F.uppg_html())
head_start = '<h3>Vad är biologi?</h3>'
M["biologi-m-1-1-1"]["van"] = head_start + grund["Start"] + "<h3>Från fråga till plan</h3>" + grund["1.1.1"]
M["biologi-m-1-1-1"]["latt"] = latt[1] + latt[2]

import sajtkonv as SK
import latt_ov as LO
IKON_OVA = "✏️"
def latt_data(idxs, forsta):
    """Lättläst: läsdel (sajtformat) + interaktiva övningar för varje del."""
    sek = []; begr = {}
    for i in idxs:
        d = L.DELAR[i - 1]
        part = SK.konvertera(fix(BL.lasa_page(i, d)), d["titel"])
        sek += part["sektioner"]
        for b in part.get("begrepp", []): begr[b["term"]] = b["forklaring"]
        sek.append(LO.sektion("Öva: " + d["titel"], IKON_OVA, d["titel"], d["ova"]))
    out = {"sektioner": sek}
    if begr: out["begrepp"] = [{"term": t, "forklaring": f} for t, f in sorted(begr.items())]
    return out
LATT_DATA = {
    "biologi-m-1-1-1": latt_data([1, 2], "Vad är biologi?"), "biologi-m-1-1-2": latt_data([3], "Dokumentera"),
    "biologi-m-1-1-3": latt_data([4], "Värdera"), "biologi-m-1-1-l": latt_data([5], "Labb"),
    "biologi-m-1-2-1": latt_data([6], "Modeller"), "biologi-m-1-2-2": latt_data([7], "Källor"),
    "biologi-m-1-2-3": latt_data([8], "Argument"), "biologi-m-1-2-l": latt_data([9], "Labb"),
}
TEST_LATT = {"sektioner": [{"ikon": "📝", "titel": "Testa dig själv", "text": ["Nu får du visa vad du har lärt dig. Du kan titta i kapitlet om du vill."],
                            "ovningar": [LO.bygg("TEST", n, ex) for n, ex in enumerate(L.TEST, 1)]}]}
TITEL = {"biologi-m-1-1-1": "Vad är biologi?", "biologi-m-1-1-2": "Dokumentera", "biologi-m-1-1-3": "Värdera resultat", "biologi-m-1-1-l": "Labb",
         "biologi-m-1-2-1": "Modeller", "biologi-m-1-2-2": "Källor", "biologi-m-1-2-3": "Argument", "biologi-m-1-2-l": "Labb",
         "biologi-m-1-s": "Sammanfattning", "biologi-m-1-t": "Testa dig själv"}
out = ["// Genereras av kallor-biologi/omrade1/exportsite.py (sajtkonv.py, latt_ov.py) – ändra inte för hand.",
       "// Biologi område 1: varje moment i tre nivåer (lättläst, grundtext, fördjupning), skrivet för skärm i sajtens vanliga sidformat. Elevversion, utan facit. Lättläst har interaktiva övningar.",
       "var innehall = window.innehall || {};"]
for id_, d in M.items():
    niv = {}
    if id_ in LATT_DATA: niv["lattlast"] = LATT_DATA[id_]
    elif id_ == "biologi-m-1-t": niv["lattlast"] = TEST_LATT
    elif d["latt"]: niv["lattlast"] = SK.konvertera(fix(d["latt"]), TITEL[id_])
    for key, k in (("vanlig", "van"), ("fordjupning", "ford")):
        if d[k]: niv[key] = SK.konvertera(fix(d[k]), TITEL[id_])
    out.append('innehall[%s] = {nivaer: %s, nivaStandard: "vanlig"};' % (json.dumps(id_), json.dumps(niv, ensure_ascii=False)))
open('/home/claude/pluggis/innehall/biologi-omrade1.js', 'w').write("\n".join(out) + "\n")
