# -*- coding: utf-8 -*-
"""Genererar planeringen åk 7–9 (Lgr22) för kemi, fysik och teknik från <ämne>_data.py.
Kör från repots rot: python3 planering/amne_plan.py kemi|fysik|teknik|alla"""
import sys, os, html, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
K = A = ALLA = C = None
def las(amne):
    global K, A, ALLA, C
    K = importlib.import_module(amne + "_data"); A = K.AREAS; ALLA = {**K.SYFTE, **K.CI, **K.FORM}; C = K.CFG
def sp(t): return t.split()
def kl(ks, pat): return [ALLA[k] for k in ks if re.fullmatch(pat, k)]
PS, PC, PF = r"S\d", r"[A-Z]{2}\d", r"F\d"
def kort(t):
    t = re.split(r"[;:]", t)[0].strip()
    return t if len(t) < 75 else t[:72].rsplit(" ", 1)[0].rstrip(",") + " …"
def lab(d): return d[6]
def dn(d): return d[0].replace(".", "-")

def kontroll():
    seen = {k: 0 for k in ALLA}; bad = []
    for a in A:
        for d in a[3]:
            if len(d[5]) != 3: bad.append(d[0])
            rader = [m[3] for m in d[5]] + ([d[6][4]] if d[6] else [])
            for tg in rader:
                for k in sp(tg):
                    if k not in ALLA: bad.append((d[0], k))
                    else: seen[k] += 1
    saknas = [k for k, v in seen.items() if v == 0]
    if bad or saknas: print("FEL", bad, saknas); sys.exit(1)
    return seen

def rader(d):
    r = [("Lektionsmoment", m[0], m[1], m[2], m[3]) for m in d[5]]
    if d[6]: r.append(("Labb", "Labb: " + d[6][0], f"{d[6][1]} {d[6][2]} Säkerhet: {d[6][3]}", d[6][5], d[6][4]))
    return r

def skriv_md(seen):
    o = []; w = o.append
    nm = sum(len(d[5]) for a in A for d in a[3]); nl = sum(1 for a in A for d in a[3] if d[6]); ne = sum(len(d[7]) for a in A for d in a[3])
    w(f"# {C['titel']} åk 7–9 – planering (Lgr22)\n")
    w(f"Status: förslag, väntar på granskning. Genereras av `planering/amne_plan.py` från `planering/{C['id']}_data.py` – ändra där, inte här.\n")
    w(f"Planen omfattar {len(A)} områden, {sum(len(a[3]) for a in A)} delområden, {nm} lektionsmoment och {nl} {C['labb_pl']}. Det som inte ryms står under *Om tid / fördjupning* ({ne} förslag). Lektionsmoment och labbpass tillsammans täcker hela det centrala innehållet och alla delar av syftet (kontrollerat av skriptet).\n")
    w("## Översikt\n"); w("| Område | Delområden |"); w("|---|---|")
    for a in A: w(f"| {a[0]}. {a[1]} | {', '.join(d[1] for d in a[3])} |")
    w(""); w("## Planen\n")
    for a in A:
        w(f"## {a[0]}. {a[1]}\n"); w(f"*{a[2]}*\n")
        for d in a[3]:
            w(f"### {d[0]} {d[1]}\n"); w(f"**Mål:** {d[2]}\n"); w(f"**Nivåer (E→A):** {d[3]}\n")
            if d[4]: w("**Förklaringsmodeller:** " + "; ".join(d[4]) + "\n")
            w("| Moment | Innehåll | Begrepp | Syfte | Centralt innehåll | Förmåga |"); w("|---|---|---|---|---|---|")
            for typ, t, tx, beg, tg in rader(d):
                ks = sp(tg); pre = "🧪 **" + t.replace("Labb: ", C["labb"] + " (" + C["tid"] + "): ") + "**" if typ == "Labb" else f"**{t}**"
                w(f"| {pre} | {tx} | {beg} | {'; '.join(kort(x) for x in kl(ks,PS))} | {'; '.join(kort(x) for x in kl(ks,PC))} | {'; '.join(kl(ks,PF))} |")
            w("")
            if d[7]: w("**Om tid / fördjupning:** " + "; ".join(d[7]) + "\n")
    w("## Öppna frågor\n")
    for n, q in enumerate(C["oppna"], 1): w(f"{n}. {q}")
    open(f"planering/{C['id']}.md", "w", encoding="utf-8").write("\n".join(o) + "\n")

def skriv_xlsx(seen):
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    F = Font(name="Arial", size=10); FB = Font(name="Arial", size=10, bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor=C["farg"])
    th = Side(style="thin", color="CCCCCC"); BD = Border(top=th, bottom=th, left=th, right=th)
    def sheet(ws, head, rows, widths, freeze="A2"):
        ws.append(head)
        for r in rows: ws.append(r)
        for c in ws[1]: c.font = FB; c.fill = HF; c.alignment = Alignment(wrap_text=True, vertical="center")
        for row in ws.iter_rows(min_row=2):
            for c in row: c.font = F; c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = BD
        for i, wd in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = wd
        ws.freeze_panes = freeze; ws.auto_filter.ref = ws.dimensions
    wb = Workbook(); m = []; dr = []; ar = []; lr = []
    for a in A:
        ar.append([a[0], a[1], a[2], len(a[3])])
        for d in a[3]:
            dr.append([a[0], a[1], d[0], d[1], d[2], d[3], "; ".join(d[4]), "; ".join(d[7])])
            for typ, t, tx, beg, tg in rader(d):
                ks = sp(tg); m.append([a[0], a[1], d[0], d[1], typ, t, tx, beg, "; ".join(kl(ks,PS)), "; ".join(kl(ks,PC)), "; ".join(kl(ks,PF))])
            if d[6]: lr.append([d[0], d[1], d[6][0], d[6][1], d[6][2], d[6][3]])
            for t in d[7]: m.append([a[0], a[1], d[0], d[1], "Om tid / fördjupning", t, "", "", "", "", ""])
    ws = wb.active; ws.title = "Moment"
    sheet(ws, ["Område nr", "Område", "Delområde nr", "Delområde", "Typ", "Moment", "Innehåll", "Begrepp", "Syfte", "Centralt innehåll", "Förmåga"], m, [8, 24, 9, 28, 16, 32, 55, 36, 36, 40, 22], "G2")
    sheet(wb.create_sheet("Delområden"), ["Område nr", "Område", "Delområde nr", "Delområde", "Mål", "Nivåer (E→A)", "Förklaringsmodeller", "Om tid / fördjupning"], dr, [8, 24, 9, 30, 50, 60, 45, 50])
    sheet(wb.create_sheet("Områden"), ["Nr", "Område", "Idé", "Delområden"], ar, [6, 32, 70, 10])
    sheet(wb.create_sheet("Labbar"), ["Delområde nr", "Delområde", "Labb", "Undersökningsbar fråga", "Upplägg", "Säkerhet och anmärkning"], lr, [10, 30, 32, 40, 60, 50])
    sheet(wb.create_sheet("Täckning"), ["Kod", "Innehåll", "Antal lektioner/labbar"], [[k, v, seen[k]] for k, v in ALLA.items()], [8, 110, 14])
    wo = wb.create_sheet("Om planen", 0)
    for r in [f"{C['titel']} åk 7–9 – planering (Lgr22). Förslag, väntar på granskning.", "Nivåer: område → delområde → moment.", "Begrepp och labbar är förslag, inte granskade mot läromedel eller skolans säkerhetsregler.", f"Källa: planering/{C['id']}_data.py i repot (ändra där, inte här)."]:
        wo.append([r])
    for row in wo.iter_rows():
        for c in row: c.font = F
    wo["A1"].font = Font(name="Arial", size=12, bold=True); wo.column_dimensions["A"].width = 120
    wb.save(f"planering/{C['id']}-planering.xlsx")

def skriv_pdf():
    e = html.escape
    css = """@page{size:A4;margin:16mm 14mm 16mm 14mm;@bottom-center{content:counter(page);font:9pt Arial;color:#666}}
body{font:9.5pt/1.35 Arial,'DejaVu Sans',sans-serif;color:#1c2330}
h1{font-size:20pt;margin:0 0 4pt;color:{M}}.sub{color:#555;margin-bottom:10pt}
div.pg{break-after:page}div.pg:last-child{break-after:auto}
h2{font-size:15pt;color:#fff;background:{F};padding:5pt 8pt;border-radius:4pt;margin:0 0 3pt}
.idea{font-style:italic;color:#444;margin:0 0 8pt}
h3{font-size:11.5pt;color:{M};border-bottom:1.5px solid {F};margin:10pt 0 3pt;padding-bottom:1pt}
.mal,.niv,.mod{margin:2pt 0}
table{width:100%;border-collapse:collapse;margin:3pt 0 4pt;table-layout:fixed}
th{background:{L};text-align:left;font-size:8.5pt;padding:3pt 4pt;border:1px solid #c8d0d6}
td{vertical-align:top;padding:3pt 4pt;border:1px solid #d3dbe2;font-size:8.8pt}
tr{break-inside:avoid}td.m b{display:block}td.k div{margin-bottom:1.5pt}
tr.lab td{background:#f4f7f9}
.tid{margin:5pt 0;padding:4pt 8pt;background:#f2f5f7;border-radius:4pt;font-size:8.8pt}
.leg{font-size:9pt;background:#f2f5f7;border-radius:4pt;padding:6pt 9pt;margin:6pt 0}.leg li{margin:1pt 0}"""
    css = css.replace("{M}", "#" + C["morkt"]).replace("{F}", "#" + C["farg"]).replace("{L}", "#" + C["ljust"])
    FG = C['farg']
    o = ['<!doctype html><meta charset="utf-8"><style>' + css + "</style>"]
    o.append(f'<div class="pg"><h1>{e(C["titel"])} åk 7–9 – planering</h1><div class="sub">Område → delområde → moment, med begrepp, förklaringsmodeller, labbpass och koppling till kursplanen (Lgr22). Förslag, väntar på granskning.</div>')
    o.append(f'<div class="leg"><b>Så läser du planen.</b><ul style="margin:3pt 0 0 14pt;padding:0"><li><b>Område</b> = ett kapitel. <b>Delområde</b> = ett avgränsat arbetsområde. <b>Moment</b> = en lektion.</li><li><b>Koppling</b> visar vilken del av ämnets <b>syfte</b>, vilket <b>centralt innehåll</b> och vilken <b>förmåga</b> momentet bygger på.</li><li>Nivåraden visar vad som skiljer godtagbara (E), goda (C) och mycket goda (A) kunskaper.</li><li><b>Om tid / fördjupning</b> = förslag som inte ryms i planen.</li><li>🧪 = {C["labb_pl"]}.</li></ul></div>')
    o.append('<table><tr><th>Område</th><th>Delområden</th></tr>')
    for a in A: o.append(f'<tr><td><b>{a[0]}. {e(a[1])}</b></td><td>{e(", ".join(d[1] for d in a[3]))}</td></tr>')
    o.append('</table></div>')
    for a in A:
        # ett område per sida om det ryms; annars bryts efter delområde
        for di, d in enumerate(a[3]):
            o.append('<div class="pg">')
            if di == 0: o.append(f'<h2>{a[0]}. {e(a[1])}</h2><div class="idea">{e(a[2])}</div>')
            else: o.append(f'<div class="idea" style="margin:0 0 4pt;color:#{FG}"><b>{a[0]}. {e(a[1])}</b></div>')
            o.append(f'<h3>{d[0]} {e(d[1])}</h3><div class="mal"><b>Mål:</b> {e(d[2])}</div><div class="niv"><b>Nivåer:</b> {e(d[3])}</div>')
            if d[4]: o.append('<div class="mod"><b>Förklaringsmodeller:</b> ' + e("; ".join(d[4])) + "</div>")
            o.append('<table><colgroup><col style="width:43%"><col style="width:22%"><col style="width:35%"></colgroup><tr><th>Moment och innehåll</th><th>Begrepp</th><th>Koppling till kursplanen</th></tr>')
            for typ, t, tx, beg, tg in rader(d):
                ks = sp(tg); sy = kl(ks, PS); ce = kl(ks, PC); fm = kl(ks, PF); k = ""
                if sy: k += "<div><b>Syfte:</b> " + e("; ".join(kort(x) for x in sy)) + "</div>"
                if ce: k += "<div><b>Innehåll:</b> " + e("; ".join(kort(x) for x in ce)) + "</div>"
                k += "<div><b>Förmåga:</b> " + e("; ".join(fm)) + "</div>"
                tt = ("🧪 " if typ == "Labb" else "") + e(t.replace("Labb: ", C["labb"] + ": "))
                o.append(f'<tr class="{"lab" if typ=="Labb" else ""}"><td class="m"><b>{tt}</b>{e(tx)}</td><td>{e(beg)}</td><td class="k">{k}</td></tr>')
            o.append("</table>")
            if d[7]: o.append('<div class="tid"><b>Om tid / fördjupning:</b> ' + e("; ".join(d[7])) + "</div>")
            o.append("</div>")
    p = f"/tmp/{C['id']}_plan.html"; open(p, "w", encoding="utf-8").write("\n".join(o))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = b.new_page()
        pg.goto("file://" + p); pg.pdf(path=f"planering/{C['id']}-planering.pdf", prefer_css_page_size=True, print_background=True); b.close()

# ---- Kapitel som är byggda (häften, lärarmaterial, extra blad) ----------------
# Nyckel: (ämnes-id, områdesnummer)
HAFTE = {("kemi", 1): "kemi-omrade-1", ("kemi", 2): "kemi-omrade-2", ("kemi", 3): "kemi-omrade-3", ("kemi", 4): "kemi-omrade-4"}
EXTRA_BLAD = {("kemi", 1): ["Sammanfattning och begrepp", "Testa dig själv"], ("kemi", 2): ["Sammanfattning och begrepp", "Testa dig själv"], ("kemi", 3): ["Sammanfattning och begrepp", "Testa dig själv"], ("kemi", 4): ["Sammanfattning och begrepp", "Testa dig själv"]}   # blir <id>-m-<nr>-s och -t
TITEL_OVR = {"kemi-m-1-1-1": "Vad är kemi? Säkerhet och utrustning i kemilabbet", "kemi-m-2-1-1": "Vad är materia? Ämnen och material", "kemi-m-3-1-1": "Vad är en atom? Atomen och dess partiklar", "kemi-m-4-1-1": "Vad händer när atomer möts? Molekyler och kovalent bindning"}   # sajtsidan innehåller även Start-avsnittet
MATERIAL = {("kemi", 1): {"lankar": [["Prov (elevversion)", "planering/kemi-omrade1/kemi-1-prov-elev.pdf"],
                                     ["Prov med facit (lärare)", "planering/kemi-omrade1/kemi-1-prov-larare.pdf"],
                                     ["Blooket (CSV)", "planering/kemi-omrade1/kemi-1-blooket.csv"],
                                     ["Kahoot (xlsx)", "planering/kemi-omrade1/kemi-1-kahoot.xlsx"],
                                     ["Jeopardy", "simuleringar/jeopardy-kemi-1.html"]],
                           "ppt": [["📊 Introduktion till kemi", "planering/kemi-omrade1/kemi-1-0-introduktion-till-kemi.pptx"],
                                   ["📊 1.1 Arbeta som kemist", "planering/kemi-omrade1/kemi-1-1-arbeta-som-kemist.pptx"],
                                   ["📊 1.2 Modeller, källor och argument", "planering/kemi-omrade1/kemi-1-2-modeller-kallor-argument.pptx"]]},
            ("kemi", 2): {"lankar": [["Prov (elevversion)", "planering/kemi-omrade2/kemi-2-prov-elev.pdf"],
                                     ["Prov med facit (lärare)", "planering/kemi-omrade2/kemi-2-prov-larare.pdf"],
                                     ["Blooket (CSV)", "planering/kemi-omrade2/kemi-2-blooket.csv"],
                                     ["Kahoot (xlsx)", "planering/kemi-omrade2/kemi-2-kahoot.xlsx"],
                                     ["Jeopardy", "simuleringar/jeopardy-kemi-2.html"]],
                           "ppt": [["📊 Introduktion till materia", "planering/kemi-omrade2/kemi-2-0-introduktion-till-materia.pptx"],
                                   ["📊 2.1 Ämnen, blandningar och partikelmodellen", "planering/kemi-omrade2/kemi-2-1-amnen-blandningar-partikelmodellen.pptx"],
                                   ["📊 2.2 Separations- och analysmetoder", "planering/kemi-omrade2/kemi-2-2-separation-och-analys.pptx"]]},
            ("kemi", 3): {"lankar": [["Prov (elevversion)", "planering/kemi-omrade3/kemi-3-prov-elev.pdf"],
                                     ["Prov med facit (lärare)", "planering/kemi-omrade3/kemi-3-prov-larare.pdf"],
                                     ["Blooket (CSV)", "planering/kemi-omrade3/kemi-3-blooket.csv"],
                                     ["Kahoot (xlsx)", "planering/kemi-omrade3/kemi-3-kahoot.xlsx"],
                                     ["Jeopardy", "simuleringar/jeopardy-kemi-3.html"]],
                           "ppt": [["📊 Introduktion till atomer", "planering/kemi-omrade3/kemi-3-0-introduktion-till-atomer.pptx"],
                                   ["📊 3.1 Atomens byggnad", "planering/kemi-omrade3/kemi-3-1-atomens-byggnad.pptx"],
                                   ["📊 3.2 Periodiska systemet", "planering/kemi-omrade3/kemi-3-2-periodiska-systemet.pptx"]]},
            ("kemi", 4): {"lankar": [["Prov (elevversion)", "planering/kemi-omrade4/kemi-4-prov-elev.pdf"],
                                     ["Prov med facit (lärare)", "planering/kemi-omrade4/kemi-4-prov-larare.pdf"],
                                     ["Blooket (CSV)", "planering/kemi-omrade4/kemi-4-blooket.csv"],
                                     ["Kahoot (xlsx)", "planering/kemi-omrade4/kemi-4-kahoot.xlsx"],
                                     ["Jeopardy", "simuleringar/jeopardy-kemi-4.html"]],
                           "ppt": [["📊 Introduktion till kemiska föreningar", "planering/kemi-omrade4/kemi-4-0-introduktion-till-foreningar.pptx"],
                                   ["📊 4.1 Molekyler och joner", "planering/kemi-omrade4/kemi-4-1-molekyler-och-joner.pptx"],
                                   ["📊 4.2 Kemiska reaktioner", "planering/kemi-omrade4/kemi-4-2-kemiska-reaktioner.pptx"]]}}

def skriv_js():
    data = {"plan": {"pdf": f"planering/{C['id']}-planering.pdf", "xlsx": f"planering/{C['id']}-planering.xlsx"},
            "omraden": [{"nr": a[0], "titel": a[1], "ide": a[2], "hafte": HAFTE.get((C["id"], a[0])), "lankar": MATERIAL.get((C["id"], a[0]), {}).get("lankar", []), "ppt": MATERIAL.get((C["id"], a[0]), {}).get("ppt", [])} for a in A]}
    open(f"planering/lararvy-{C['id']}.js", "w", encoding="utf-8").write(
        f"// Genereras av planering/amne_plan.py – ändra inte för hand.\nwindow.{C['js']} = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")

def skriv_struktur():
    def js(t): return json.dumps(t, ensure_ascii=False)
    I = C['id']; ut = []
    for a in A:
        dl = []
        for d in a[3]:
            mo = [f'              {{ id: "{I}-m-{dn(d)}-{n}", titel: {js(TITEL_OVR.get(f"{I}-m-{dn(d)}-{n}", m[0]))} }}' for n, m in enumerate(d[5], 1)]
            if d[6]: mo.append(f'              {{ id: "{I}-m-{dn(d)}-l", titel: {js(C["labb"] + ": " + d[6][0])} }}')
            dl.append(f'          {{\n            id: "{I}-d-{dn(d)}",\n            titel: {js(d[0] + " " + d[1])},\n            ramverk: true,\n            barn: [\n' + ",\n".join(mo) + "\n            ]\n          }")
        ex = [f'          {{ id: "{I}-m-{a[0]}-{k}", titel: {js(t)} }}' for k, t in zip("st", EXTRA_BLAD.get((I, a[0]), []))]
        ut.append(f'      {{\n        id: "{HAFTE.get((I, a[0]), f"{I}-omrade-{a[0]}")}",\n        titel: {js(f"{a[0]}. {a[1]}")},\n        ramverk: true,\n        barn: [\n' + ",\n".join(dl + ex) + "\n        ]\n      }")
    U = C["id"].upper()
    block = f'  // {U} START (genereras av planering/amne_plan.py)\n  {{\n    id: "{C["id"]}",\n    titel: {js(C["titel"] + " (beta)")},\n    ikon: "{C["ikon"]}",\n    ramverk: true,\n    barn: [\n' + ",\n".join(ut) + f'\n    ]\n  }},\n  // {U} END\n'
    s = open("innehall/struktur.js", encoding="utf-8").read()
    if f"// {U} START" in s:
        a0 = s.index(f"  // {U} START"); b0 = s.index(f"  // {U} END\n") + len(f"  // {U} END\n")
    else:
        old = f'  {{\n    id: "{C["id"]}",\n    titel: "{C["titel"]}",\n    ikon: "{C["ikon"]}",\n    barn: []\n  }},\n'
        a0 = s.index(old); b0 = a0 + len(old)
    open("innehall/struktur.js", "w", encoding="utf-8").write(s[:a0] + block + s[b0:])

if __name__ == "__main__":
    val = sys.argv[1] if len(sys.argv) > 1 else "alla"
    for amne in (["kemi", "fysik", "teknik"] if val == "alla" else [val]):
        las(amne); seen = kontroll()
        print("OK", amne, len(A), "områden", sum(len(a[3]) for a in A), "delområden")
        skriv_md(seen); skriv_xlsx(seen); skriv_pdf(); skriv_js(); skriv_struktur()
