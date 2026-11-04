# -*- coding: utf-8 -*-
import sys, os, re, importlib
sys.path.insert(0, "/tmp/bio")
from playwright.sync_api import sync_playwright
OM = [(1,"omrade1","ch01n","biologi-1-vetenskap"),(2,"omrade2","ch02n","biologi-2-cellen"),
      (3,"omrade3","ch03n","biologi-3-mangfald"),(4,".","ch04","biologi-4-ekologi")]
CSS = """
@page{size:A4;margin:11mm 12mm 14mm 12mm}
*{box-sizing:border-box}body{font:12pt/1.45 Inter,sans-serif;color:#241712;margin:0}
h1{font:700 18pt Inter;color:#245040;margin:0}.sub{font:10pt Inter;color:#6b625b;margin:0 0 6pt}
.beta{font:700 8pt Carlito;background:#fff5d6;color:#a8651a;padding:1pt 5pt;border-radius:3pt;vertical-align:middle}
h2{font:700 14.5pt Inter;color:#fff;background:#2f6b4f;padding:2pt 7pt;border-radius:4pt;margin:6pt 0 4pt;break-after:avoid}
h3{break-after:avoid;font:700 12.5pt Inter;color:#2f6b4f;margin:6pt 0 2pt}
ul{margin:0 0 4pt;padding-left:12pt}li{margin:0 0 3pt}
.begr{columns:2;column-gap:9mm;font:10pt/1.28 Inter}.begr div{break-inside:avoid;margin:0 0 1.5pt}
.q{break-inside:avoid;margin:0 0 7pt;display:flex;gap:5pt}.q .n{font:700 12pt Inter;color:#2f6b4f;min-width:17pt}
.q .p{font:italic 10pt Inter;color:#6b625b}
.alt{display:grid;grid-template-columns:1fr 1fr;gap:0 8pt;margin-top:2pt;font-size:12pt}
.qcols{columns:1}
table{border-collapse:collapse;margin:3pt 0;font:11pt Inter}td,th{border:.7pt solid #b9b1a6;padding:1.5pt 6pt}th{background:#e5f1e9}
.fakeann{display:none}
.lines{border-bottom:.6pt solid #bdb5aa;height:15pt;margin-top:2pt}
.fac{font:12pt/1.4 Inter;columns:2;column-gap:9mm}.fac div{break-inside:avoid;margin:0 0 4pt}
.note{font:italic 10.5pt Inter;color:#6b625b}
.pb{break-before:page}
"""
def strip(s): return s

# Ersättningsfrågor: pluggbladet ska öva samma förmågor som provet men aldrig ha provets egna uppgifter.
def _tab(rub, rader):
    return "<table><tr>"+"".join(f"<th>{c}</th>" for c in rub)+"</tr>"+"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rader)+"</table>"
OVR = {
 (1, 6): (("C", "Lukas vill ta reda på om mängden ljus påverkar hur snabbt krasse gror. Han sätter en kruka med krassefrön i ett fönster och en annan i en mörk garderob. Krukan i fönstret vattnar han varje dag, krukan i garderoben bara ibland.<br>a) Ge två skäl till att Lukas undersökning inte blir rättvis.<br>b) Föreslå en förbättring. ●●", None, 2, 6),
          "a) Både ljus och vattning skiljer sig åt, så man vet inte vilket som gav skillnaden. Dessutom kanske temperaturen skiljer. b) Ändra bara ljuset och håll vatten, jord, temperatur, antal frön och tid lika. Använd flera krukor och räkna medelvärde."),
 (2, 1): (("A", "Vilken del av cellen bryter ner glukos och frigör energi?", ["A Cellvägg", "B Mitokondrie", "C Kloroplast", "D Cellkärna"], 1, 0), "B"),
 (2, 2): (("A", "Ett mikroskop har okular 10× och objektiv 20×. Hur stor är förstoringen?", ["A 30 gånger", "B 200 gånger", "C 2 gånger", "D 2 000 gånger"], 1, 0), "B"),
 (2, 4): (("B", "Ge två exempel på vad cellen använder energin från cellandningen till.", None, 1, 3),
          "T.ex. bygga nytt, ta upp ämnen, röra sig, växa och dela sig, hålla värmen."),
 (2, 11): (("E", "En elev sätter en grön växt i en tät, genomskinlig plastpåse i starkt ljus under en timme. Beskriv vad som händer med gaserna i påsen och med växtens glukos. Förklara med fotosyntes och cellandning.", None, 3, 5),
           "I starkt ljus gör växten mycket fotosyntes. Den tar upp koldioxid och bildar glukos och syre, så koldioxiden minskar och syret ökar i påsen. Cellandningen pågår också och använder syre och glukos, men under en kort tid sker mer fotosyntes än cellandning."),
 (3, 1): (("A", "Vilket är ett exempel på en försörjande ekosystemtjänst?", ["A Skogen som lagrar kol", "B Fisk som fiskas i havet", "C En vacker utsikt över fjällen", "D Bin som pollinerar blommor"], 1, 0), "B"),
 (3, 6): (("C", "<span class='p'>Påhittade värden.</span> En klass räknade fågelarter vid tre lyssningspunkter i två olika skogar. Antal arter per punkt:" + _tab(["Skog", "Punkt 1", "Punkt 2", "Punkt 3"], [["Blandskog", "12", "15", "9"], ["Planterad granskog", "5", "7", "6"]]) + "a) Räkna ut medelvärdet för varje skog.<br>b) Ge en möjlig förklaring till skillnaden. ●●", None, 2, 5),
          "a) Blandskog: (12 + 15 + 9) / 3 = 12. Planterad granskog: (5 + 7 + 6) / 3 = 6. b) Blandskogen har fler sorters träd, buskar och gömställen och mer olika mat, så fler arter hittar en livsmiljö. Den planterade granskogen har likadana träd och färre livsmiljöer."),
 (3, 8): (("D", "En kommun vill bygga en motorväg genom en artrik, betad äng med flera sällsynta växter. Redovisa argument för och emot, väg dem mot varandra och ta ställning. Beskriv också vad du är osäker på. ●●●", None, 3, 6),
          "Öppet svar. För: snabbare resor, jobb, mindre trafik på andra vägar. Emot: ängen går inte att återskapa snabbt, sällsynta arter kan försvinna, ängen ger pollinering och mångfald. Ett välutvecklat svar väger flera argument, nämner vem som berörs, tar ställning och säger vad man är osäker på, till exempel hur många arter som berörs och om det finns andra sträckningar."),
 (3, 9): (("D", "<span class='p'>Påhittat exempel.</span> I en sjö ökar antalet gäddor från 100 till 300 under tio år, medan flera andra fiskarter blir färre. Alva säger: ”Då har den biologiska mångfalden i sjön ökat.” Värdera påståendet. ●●●", None, 3, 6),
           "Nej, inte nödvändigtvis. Biologisk mångfald handlar om många olika arter, genetisk variation och olika livsmiljöer, inte om att en art blir fler. Om andra arter minskar kan artrikedomen i stället bli mindre. Gäddor äter andra fiskar och kan bidra till det. Man måste titta på hur många arter som finns och hur de förändras."),
 (3, 10): (("E", "Hanna tror att det finns fler arter av mossor på en fuktig plats i skogen än på en torr. Planera en undersökning som kan pröva hennes idé. Beskriv vad du ska räkna, hur du gör jämförelsen rättvis, hur du dokumenterar och vad du är osäker på. ●●●", None, 2, 6),
           "Räkna antalet mossarter i flera lika stora provrutor (t.ex. 1 m²) på en fuktig och en torr plats. Håll lika: årstid, typ av skog, ljus och provrutornas storlek. Använd samma bestämningsnyckel, skriv resultaten i en tabell och räkna medelvärde. Osäkert: slump, svårt att artbestämma, platserna kan skilja på fler saker än fukt."),
 (3, 11): (("E", "I en skog finns kedjan: blåbärsris → skogssork → rödräv. En torr sommar ger få blåbär och riset mår dåligt. Förklara vad som kan hända med sorkar och rävar. ●●●", None, 3, 6),
           "Blåbärsriset är producent. När det blir mindre mat minskar sorkarna. Då får räven mindre mat och kan också minska. Effekten går uppåt i kedjan. Om räven har andra byten, till exempel harar eller fåglar, påverkas den mindre."),
 (4, 0): (("A", "Vilken organism är en nedbrytare?", ["A Gräshoppa", "B Svamp på en död trädstam", "C Lodjur", "D Blåbärsris"], 1, 0), "B"),
}

def build(nr, folder, mod, slug):
    os.chdir("/tmp/bio/"+folder if folder!="." else "/tmp/bio"); sys.path.insert(0, os.getcwd())
    M = importlib.import_module(mod)
    M.TEST = [OVR[(nr, i)][0] if (nr, i) in OVR else t for i, t in enumerate(M.TEST)]
    M.FACIT = [OVR[(nr, i)][1] if (nr, i) in OVR else f for i, f in enumerate(M.FACIT)]
    h = [f"<h1>Plugga inför prov – {M.NAMN} <span class='beta'>beta</span></h1>",
         f"<p class='sub'>Område {nr} · sammanfattning, viktiga begrepp och övningsfrågor med facit. Skriv ut och plugga de sista dagarna.</p>",
         "<h2>Sammanfattning</h2><ul>"+"".join(f"<li>{s}</li>" for s in M.SAMMAN)+"</ul>",
         "<h2>Viktiga begrepp</h2><div class='begr'>"+"".join(f"<div><b>{a}</b> – {b}</div>" for a,b in M.BEGR)+"</div>",
         "<h2 class='pb'>Övningsfrågor</h2><p class='note'>Försök svara själv innan du tittar på facit på sista sidan.</p><div class='qcols'>"]
    last = None
    for i, t in enumerate(M.TEST):
        d, q, opts = t[0], t[1], t[2]
        if d != last:
            h.append(f"<h3>{M.DEL_NAMN.get(d,d)}</h3>"); last = d
        if q == "TABELL":
            rub, rader = M.TEST_TABELL
            q = M.TEST_D_TEXT + "<table><tr>"+"".join(f"<th>{c}</th>" for c in rub)+"</tr>"+"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rader)+"</table>" + "<br>".join(M.TEST_D_SUB)
        body = q
        if opts: body += "<div class='alt'>"+"".join(f"<div>{o}</div>" for o in opts)+"</div>"
        else: body += "<div class='lines'></div><div class='lines'></div>" if (len(t)>4 and t[4] and t[4]<=4) else "<div class='lines'></div><div class='lines'></div><div class='lines'></div>"
        h.append(f"<div class='q'><span class='n'>{i+1}</span><div>{body}</div></div>")
    h.append("</div><h2 class='pb'>Facit</h2><div class='fac'>")
    for i, t in enumerate(M.TEST):
        f = M.FACIT[i]
        if t[2]: f = f"{f} – {t[2][ord(f)-65][2:]}"
        h.append(f"<div><b>{i+1}.</b> {f}</div>")
    h.append("</div><p class='note'>Facit på öppna frågor är förslag; andra rimliga svar kan också ge poäng. Frågorna är samma typ som på provet men inte samma uppgifter.</p>")
    html = f"<!doctype html><meta charset=utf-8><style>{CSS}</style>"+"".join(h)
    p = f"/tmp/bio/out/{slug}-pluggblad.html"; open(p,"w").write(html)
    return p
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page()
    for o in OM:
        p = build(*o); pg.goto("file://"+p)
        pg.pdf(path=p.replace(".html",".pdf"), format="A4", print_background=True, prefer_css_page_size=True,
               display_header_footer=True, header_template="<span></span>",
               footer_template=f"<div style='font:8pt Inter;width:100%;padding:0 13mm;color:#6b625b;display:flex;justify-content:space-between'><span>Pluggis · Biologi · Plugga inför prov (beta)</span><span><span class='pageNumber'></span>/<span class='totalPages'></span></span></div>")
    b.close()
