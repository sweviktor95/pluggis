# -*- coding: utf-8 -*-
"""Exporterar område 4 (tre nivåer) till sajtens innehållsfil + scoped CSS."""
import os, re, json, sys
os.environ['CH'] = '04n'
sys.path.insert(0, '/tmp/bio')
import bbuild_latt as BL
import ch04n as G
import ch04n_fordj as F
import bstyle
import bbuild_n as BN

IMG = ("file:///tmp/bio/fig04n/", "bilder/biologi-omrade4/")
def fix(h): return h.replace(*IMG)

# Lättläst: delar 1..13
L = BL.L
latt = {i: BL.lasa_page(i, d) + BL.ova_page(i, d) for i, d in enumerate(L.DELAR, 1)}
GS = [inner for nr, t, inner in G.S]
grund = {"Start": GS[0], "4.1.1": GS[1], "4.1.2": GS[2], "4.1.3": GS[3], "L1": GS[4], "4.2.1": GS[5], "4.2.2": GS[6], "4.2.3": GS[7], "L2": GS[8],
         "4.3.1": GS[9], "4.3.2": GS[10], "4.3.3": GS[11], "L3": GS[12]}
fordj = {nr: inner for nr, t, inner in F.S}

M = {
 "biologi-m-4-1-1": dict(latt=latt[1] + latt[2], van=None, ford=None),
 "biologi-m-4-1-2": dict(latt=latt[3], van=grund["4.1.2"], ford=fordj["F4.1.2"]),
 "biologi-m-4-1-3": dict(latt=latt[4], van=grund["4.1.3"], ford=fordj["F4.1.3"]),
 "biologi-m-4-1-l": dict(latt=latt[5], van=grund["L1"], ford=None),
 "biologi-m-4-2-1": dict(latt=latt[6], van=grund["4.2.1"], ford=None),
 "biologi-m-4-2-2": dict(latt=latt[7], van=grund["4.2.2"], ford=fordj["F4.2.2"]),
 "biologi-m-4-2-3": dict(latt=latt[8], van=grund["4.2.3"], ford=None),
 "biologi-m-4-2-l": dict(latt=latt[9], van=grund["L2"], ford=None),
 "biologi-m-4-3-1": dict(latt=latt[10], van=grund["4.3.1"], ford=fordj["F4.3.1"]),
 "biologi-m-4-3-2": dict(latt=latt[11], van=grund["4.3.2"], ford=None),
 "biologi-m-4-3-3": dict(latt=latt[12], van=grund["4.3.3"], ford=fordj["F4.3.3"]),
 "biologi-m-4-3-l": dict(latt=latt[13], van=grund["L3"], ford=None),
}
M["biologi-m-4-s"] = dict(latt=BL.ord_page() + BL.viktigast_page(), van=BN.sam_html(G.SAMMAN, G.BEGR), ford=None)
M["biologi-m-4-t"] = dict(latt=BL.test_pages(), van=BN.test_html(G), ford=F.uppg_html())
M["biologi-m-4-1-1"]["van"] = '<h3>Vad är ekologi?</h3>' + grund["Start"] + "<h3>Vad är ett ekosystem?</h3>" + grund["4.1.1"]

import sajtkonv as SK
import latt_ov as LO
import svar_ov as SO
import re as _re

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
    "biologi-m-4-1-1": latt_data([1, 2], "Vad är ekologi?"), "biologi-m-4-1-2": latt_data([3], "Producenter, konsumenter och näringsvävar"),
    "biologi-m-4-1-3": latt_data([4], "Energiflöde och biomassa"), "biologi-m-4-1-l": latt_data([5], "Labb"),
    "biologi-m-4-2-1": latt_data([6], "Materia"), "biologi-m-4-2-2": latt_data([7], "Kolets kretslopp"),
    "biologi-m-4-2-3": latt_data([8], "Nedbrytning"), "biologi-m-4-2-l": latt_data([9], "Labb"),
    "biologi-m-4-3-1": latt_data([10], "Populationer"), "biologi-m-4-3-2": latt_data([11], "Begränsande faktorer"),
    "biologi-m-4-3-3": latt_data([12], "Samspel"), "biologi-m-4-3-l": latt_data([13], "Labb"),
}
TEST_LATT = {"sektioner": [{"ikon": "📝", "titel": "Testa dig själv", "text": ["Nu får du visa vad du har lärt dig. Du kan titta i kapitlet om du vill."],
                            "ovningar": [LO.bygg("TEST", n, ex) for n, ex in enumerate(L.TEST, 1)]}]}
def _txt(h): return _re.sub(r"<(?!br)[^>]+>", "", h)
BOKST = "ABCD"
def test_grund():
    sek = []; cur = None
    for n, (dl, q, alts, nl, pts) in enumerate(G.TEST, 1):
        if cur is None or cur["_d"] != dl:
            cur = {"_d": dl, "ikon": "📖", "titel": "Del %s · %s" % (dl, G.DEL_NAMN[dl]), "text": [], "ovningar": []}
            if dl == "A": cur["text"] = ["Uppgifterna liknar uppgifterna på nationella prov i biologi. Personer, annonser och mätvärden är påhittade."]
            sek.append(cur)
        facit = G.FACIT[n - 1]
        qq = _re.sub(r"<div class=.fakeann.>.*?</div>", "", q).replace("<br>", "<br>")
        if q == "TABELL":
            rub, rader = G.TEST_TABELL
            tab = '<div class="tabell-ram"><table class="tabell"><tr>' + "".join("<th>%s</th>" % h for h in rub) + "</tr>" + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rader) + "</table></div>"
            qq = G.TEST_D_TEXT + "<br>" + tab + "<br>".join(G.TEST_D_SUB)
        if alts:
            val = [_re.sub(r"^[A-D] ", "", a) for a in alts]
            cur["ovningar"].append({"typ": "ringa", "fraga": qq, "val": val, "ratt": BOKST.index(facit)})
        else:
            qq = qq.replace(" ●●●", "").replace(" ●●", "").replace(" ●", "")
            cur["ovningar"].append({"typ": "fri", "fraga": qq, "forslag": facit})
    for c in sek: c.pop("_d")
    return {"sektioner": sek}
def test_fordj():
    ov = [{"typ": "fri", "fraga": q, "forslag": F.SVAR[i]} for i, (q, p) in enumerate(F.UPG)]
    return {"sektioner": [{"ikon": "💭", "titel": "Resonera och ta ställning", "text": ["Uppgifterna liknar de svåraste uppgifterna på nationella prov. Personer, rubriker och mätvärden är påhittade. Svara utförligt och resonera i flera led."], "ovningar": ov}]}
TEST_GRUND = test_grund(); TEST_FORDJ = test_fordj()
TITEL = {"biologi-m-4-1-1": "Vad är ekologi?", "biologi-m-4-1-2": "Producenter, konsumenter och näringsvävar", "biologi-m-4-1-3": "Energiflöde och biomassa", "biologi-m-4-1-l": "Labb 4.1 Energi i en näringskedja",
         "biologi-m-4-2-1": "Materia tillverkas inte och försvinner inte", "biologi-m-4-2-2": "Kolets kretslopp", "biologi-m-4-2-3": "Nedbrytning", "biologi-m-4-2-l": "Labb 4.2 Nedbrytning i jord",
         "biologi-m-4-3-1": "Populationer och förändring", "biologi-m-4-3-2": "Begränsande faktorer", "biologi-m-4-3-3": "Konkurrens, jakt och samarbete", "biologi-m-4-3-l": "Labb 4.3 Rovdjur–bytesmodell",
         "biologi-m-4-s": "Sammanfattning", "biologi-m-4-t": "Testa dig själv"}
out = ["// Genereras av kallor-biologi/omrade4/exportsite.py (sajtkonv.py, latt_ov.py) – ändra inte för hand.",
       "// Biologi område 4: varje moment i tre nivåer (lättläst, grundtext, fördjupning), skrivet för skärm i sajtens vanliga sidformat. Elevversion, utan facit. Lättläst har interaktiva övningar.",
       "var innehall = window.innehall || {};"]
for id_, d in M.items():
    niv = {}
    if id_ in LATT_DATA: niv["lattlast"] = LATT_DATA[id_]
    elif id_ == "biologi-m-4-t": niv["lattlast"] = TEST_LATT
    elif d["latt"]: niv["lattlast"] = SK.konvertera(fix(d["latt"]), TITEL[id_])
    for key, k in (("vanlig", "van"), ("fordjupning", "ford")):
        if d[k]: niv[key] = SK.konvertera(fix(d[k]), "Vad är ekologi?" if (id_ == "biologi-m-4-1-1" and key == "vanlig") else TITEL[id_])
    if id_ == "biologi-m-4-t":
        niv["vanlig"] = TEST_GRUND; niv["fordjupning"] = TEST_FORDJ
    for v in niv.values():
        for sek in v["sektioner"]:
            if sek.get("fragor"): sek["fragor"] = [SO.kolla_objekt(q) for q in sek["fragor"]]
    out.append('innehall[%s] = {nivaer: %s, nivaStandard: "vanlig"};' % (json.dumps(id_), json.dumps(niv, ensure_ascii=False)))
open('/home/claude/pluggis/innehall/biologi-omrade4.js', 'w').write("\n".join(out) + "\n")
