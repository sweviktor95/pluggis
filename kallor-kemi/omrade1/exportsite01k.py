# -*- coding: utf-8 -*-
"""Exporterar område 2 (tre nivåer) till sajtens innehållsfil + scoped CSS."""
import os, re, json, sys
os.environ['CH'] = '01k'
sys.path.insert(0, '/tmp/kem')
import bbuild_latt as BL
import ch01k as G
import ch01k_fordj as F
import bstyle
import bbuild_n as BN

IMG = ("file:///tmp/kem/fig01k/", "bilder/kemi-omrade1/")
def fix(h): return h.replace(*IMG)

# Lättläst: delar 1..9
L = BL.L
latt = {i: BL.lasa_page(i, d) + BL.ova_page(i, d) for i, d in enumerate(L.DELAR, 1)}
GS = [inner for nr, t, inner in G.S]
grund = {"Start": GS[0], "1.1.1": GS[1], "1.1.2": GS[2], "1.1.3": GS[3], "L1": GS[4], "1.2.1": GS[5], "1.2.2": GS[6], "1.2.3": GS[7], "L2": GS[8]}
fordj = {nr: inner for nr, t, inner in F.S}
M = {
 "kemi-m-1-1-1": dict(latt=latt[1] + latt[2], van='<h3>Vad är kemi?</h3>' + grund["Start"] + "<h3>Säkerhet och utrustning i kemilabbet</h3>" + grund["1.1.1"], ford=None),
 "kemi-m-1-1-2": dict(latt=latt[3], van=grund["1.1.2"], ford=None),
 "kemi-m-1-1-3": dict(latt=latt[4], van=grund["1.1.3"], ford=fordj["F1.1.1"] + fordj["F1.1.2"]),
 "kemi-m-1-1-l": dict(latt=latt[5], van=grund["L1"], ford=None),
 "kemi-m-1-2-1": dict(latt=latt[6], van=grund["1.2.1"], ford=fordj["F1.2.1"]),
 "kemi-m-1-2-2": dict(latt=latt[7], van=grund["1.2.2"], ford=fordj["F1.2.2"]),
 "kemi-m-1-2-3": dict(latt=latt[8], van=grund["1.2.3"], ford=fordj["F1.2.3"]),
 "kemi-m-1-2-l": dict(latt=latt[9], van=grund["L2"], ford=None),
}
M["kemi-m-1-s"] = dict(latt=BL.ord_page() + BL.viktigast_page(), van=BN.sam_html(G.SAMMAN, G.BEGR), ford=None)
M["kemi-m-1-t"] = dict(latt=BL.test_pages(), van=BN.test_html(G), ford=F.uppg_html())

import sajtkonv as SK
import latt_ov as LO
import svar_ov01k as _S
class SO:
    @staticmethod
    def kolla_objekt(q):
        return {"f": q, "svar": _S.KOLLA2[q]} if q in _S.KOLLA2 else q
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
    "kemi-m-1-1-1": latt_data([1, 2], "Vad är kemi?"), "kemi-m-1-1-2": latt_data([3], "Från fråga till plan"), "kemi-m-1-1-3": latt_data([4], "Dokumentera och värdera"), "kemi-m-1-1-l": latt_data([5], "Labb"),
    "kemi-m-1-2-1": latt_data([6], "Vad är en modell?"), "kemi-m-1-2-2": latt_data([7], "Hur kemin vuxit fram"), "kemi-m-1-2-3": latt_data([8], "Granska kemipåståenden"), "kemi-m-1-2-l": latt_data([9], "Labb"),
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
            if dl == "A": cur["text"] = ["Uppgifterna liknar uppgifterna på nationella prov i kemi. Personer, annonser och mätvärden är påhittade."]
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
TITEL = {"kemi-m-1-1-1": "Vad är kemi? Säkerhet och utrustning", "kemi-m-1-1-2": "Från fråga till plan", "kemi-m-1-1-3": "Dokumentera och värdera", "kemi-m-1-1-l": "Labb 1.1 Brustabletten och temperaturen",
         "kemi-m-1-2-1": "Vad är en modell i kemi?", "kemi-m-1-2-2": "Hur kemin vuxit fram", "kemi-m-1-2-3": "Granska kemipåståenden", "kemi-m-1-2-l": "Labb 1.2 Fungerar fläckborttagaren?", "kemi-m-1-s": "Sammanfattning", "kemi-m-1-t": "Testa dig själv"}
out = ["// Genereras av kallor-kemi/omrade1/exportsite.py (sajtkonv.py, latt_ov.py) – ändra inte för hand.",
       "// Kemi område 1: varje moment i tre nivåer (lättläst, grundtext, fördjupning), skrivet för skärm i sajtens vanliga sidformat. Elevversion, utan facit. Lättläst har interaktiva övningar.",
       "var innehall = window.innehall || {};"]
for id_, d in M.items():
    niv = {}
    if id_ in LATT_DATA: niv["lattlast"] = LATT_DATA[id_]
    elif id_ == "kemi-m-1-t": niv["lattlast"] = TEST_LATT
    elif d["latt"]: niv["lattlast"] = SK.konvertera(fix(d["latt"]), TITEL[id_])
    for key, k in (("vanlig", "van"), ("fordjupning", "ford")):
        if d[k]: niv[key] = SK.konvertera(fix(d[k]), TITEL[id_])
    if id_ == "kemi-m-1-t":
        niv["vanlig"] = TEST_GRUND; niv["fordjupning"] = TEST_FORDJ
    for v in niv.values():
        for sek in v["sektioner"]:
            if sek.get("fragor"): sek["fragor"] = [SO.kolla_objekt(q) for q in sek["fragor"]]
    out.append('innehall[%s] = {nivaer: %s, nivaStandard: "vanlig"};' % (json.dumps(id_), json.dumps(niv, ensure_ascii=False)))
open('/home/claude/pluggis/innehall/kemi-omrade1.js', 'w').write("\n".join(out) + "\n")
