# -*- coding: utf-8 -*-
"""Prov område 4 Ekologi: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os, math
sys.path.insert(0, '/tmp/bio')
os.environ.setdefault('CH', '04n')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader, PdfWriter
import prov1 as P1

FIG = '/tmp/bio/fig04n/'
def match(rub, left, right):
    return (f'<table class="tbl num" style="width:92%"><tr><th>{rub[0]}</th><th>{rub[1]}</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')
TAB = table(["Plats", "Prov 1", "Prov 2", "Prov 3", "Prov 4", "Prov 5"], [["Lövskog, fuktig", "46", "52", "39", "58", "45"], ["Granplantering, torr", "21", "18", "25", "64", "22"]], "tbl num")

P = [
 ("E", "Vilken är en producent?", ["A Gran", "B Räv", "C Svamp", "D Hare"], 1, 0, "A", "1 p för A."),
 ("E", "Vad visar pilarna i en näringskedja?", ["A Vem som äter vem. Pilen pekar mot den som äter", "B Vem som är starkast", "C Vem som bor högst upp", "D Vem som är störst"], 1, 0, "A", "1 p för A."),
 ("E", "Dra streck mellan begreppet och förklaringen. Skriv bokstaven.<br>" + match(["Begrepp", "Förklaring"], ["1 Konsument", "2 Nedbrytare", "3 Kretslopp"], ["A Bryter ner det döda", "B Ämnen som går runt och används igen", "C Äter andra organismer för att få energi"]), None, 3, 0, "1 C, 2 A, 3 B", "1 p per rätt."),
 ("E", "Vilka två påståenden stämmer? Kryssa i två.<br>☐ Nästan all energi kommer från början från solen.<br>☐ Energi går i kretslopp.<br>☐ Nedbrytning går fortare när det är varmt.<br>☐ Det finns fler rovdjur än växter.", None, 2, 0,
  "Nästan all energi kommer från solen. Nedbrytning går fortare när det är varmt.", "1 p per rätt. Avdrag om fler än två kryssas."),
 ("E", "Titta på näringsväven." + fig(FIG+"l_vav.png", None, "60%") + "Alla sorkar försvinner. Vad händer med räven? Förklara kort.", None, 2, 2, "Räven får mindre mat (den äter sork), men kan äta hare, så den klarar sig kanske delvis. Antalet rävar kan minska.", "1 p för mindre mat/färre. 1 p för förklaring (äter sork, kan äta annat)."),
 ("E", "I en skog finns 100 harar i början av året. Under året föds 50 nya och 30 dör. Ingen flyttar in eller ut. Hur många harar finns det i slutet av året? Visa hur du räknar.", None, 2, 2, "100 + 50 − 30 = 120 harar.", "1 p för rätt beräkning, 1 p för rätt svar."),
 ("C", "Riset visar energi i en skog. Använd tumregeln att 10 procent av energin förs vidare." + fig(FIG+"p_energi.png", None, "70%") + "a) Hur mycket energi har växtätarna och rovdjuren?<br>b) Vart tar den energi som inte förs vidare vägen?", None, 3, 5,
  "a) Växtätare 1 000 kJ, rovdjur 100 kJ. b) Den används av organismerna för att leva (röra sig, hålla värmen) och blir värme. En del hamnar hos nedbrytare.", "a) 1 p per rätt värde. b) 1 p."),
 ("C", "Elever grävde ner tepåsar i tre sorters jord och vägde dem efter sex veckor." + fig(FIG+"p_nedbr.png", None, "62%") + "a) I vilken jord bröts teet ner mest?<br>b) Förklara resultatet med nedbrytare och abiotiska faktorer.<br>c) Varför grävde de ner flera påsar i varje jord?", None, 4, 6,
  "a) Skogsjord. b) Skogsjorden har mest förna och många nedbrytare och är fuktig. Sand är torr, har lite organiskt material och få nedbrytare, så det går långsamt. Fukt, temperatur och syre påverkar nedbrytarna. c) Så att slumpen mellan enskilda påsar jämnas ut.", "a) 1 p. b) 2 p (nedbrytare + abiotisk faktor + koppling). c) 1 p."),
 ("C", "Ett löv faller från en björk och ligger kvar på marken. Beskriv vad som händer med kolet i lövet, och hur ett kolatom från lövet så småningom kan hamna i en växt igen.", None, 3, 5, G_L := "Lövet bryts ner av detritusätare, svampar och bakterier. Deras cellandning släpper ut en del av kolet som koldioxid i luften, och en del blir kvar i marken. Växter tar upp koldioxid genom fotosyntesen och bygger in kolet i glukos.", "1 p nedbrytning, 1 p koldioxid till luften, 1 p fotosyntes tar upp."),
 ("C", "I ett skogsområde sköts nästan alla lodjur under några år. Forskare upptäckte efter en tid att det fanns färre unga aspar och rönnar. Använd dina kunskaper om näringskedjor för att förklara varför.", None, 3, 5,
  "Lodjuret äter rådjur och harar. När lodjuren försvinner ökar antalet rådjur och harar, och de äter mer av unga aspar och rönnar. Färre unga träd växer upp. En kaskadeffekt i flera led.", "1 p lodjur äter rådjur/harar, 1 p fler växtätare, 1 p de äter fler unga träd."),
 ("C", "Ett björkträd växer från ett litet frö till ett träd som väger 200 kg. Nästan hela vikten är kol, väte och syre. Var kommer de flesta av dessa atomer ifrån, och hur kom de in i trädet?", None, 2, 5,
  "Nästan allt kommer från koldioxid i luften och vatten. Trädet tar upp koldioxid genom bladen och bygger in kolet i glukos i fotosyntesen. Väte och syre kommer från vattnet som rötterna tar upp.", "1 p koldioxid/luft och vatten, 1 p fotosyntes/hur de kom in."),
 ("A", "Antalet rådjur i ett skogsområde ökade i flera år och föll sedan kraftigt efter en lång, snörik vinter." + fig(FIG+"p_radjur.png", None, "62%") + "Använd begreppen bärkraft och begränsande faktor för att förklara varför. Ge också ett exempel på hur en biotisk faktor kan ha bidragit.", None, 4, 7,
  "Bärkraften är det största antal rådjur som skogen kan försörja. Populationen växte så att den närmade sig eller översteg bärkraften. Snön (abiotisk faktor) gjorde det svårt att nå föda, så maten blev den begränsande faktorn och många svalt. Biotisk faktor: konkurrens om föda, sjukdomar som sprids lättare i en tät population eller rovdjur som lättare fångar försvagade djur.", "1 p bärkraft, 1 p begränsande faktor (mat), 1 p snö som abiotisk faktor, 1 p biotiskt exempel."),
 ("A", "Ella säger: ”Om fler människor äter mer vegetarisk mat kan samma åkermark föda fler människor.” Använd energipyramiden för att resonera om Ella har rätt. Ge också ett argument som talar för att djurhållning kan vara bra i Norrbotten.", None, 4, 7,
  "Ella har i stort sett rätt: varje led i näringskedjan förlorar cirka 90 % av energin, så att äta växter direkt ger mer mat per yta. Argument för djurhållning: renar och kor kan beta mark där man inte kan odla grödor (fjäll, skog, naturbetesmarker), och betet gynnar biologisk mångfald i odlingslandskapet.", "1 p energin minskar, 1 p mer mat per yta, 1 p slutsats, 1 p argument för djurhållning."),
 ("A", "En klass räknade småkryp i förna från två platser. De tog fem prover på varje plats.<br>" + TAB + "a) Räkna ut medelvärdet för lövskogen.<br>b) Ett värde i granplanteringen skiljer sig från de andra. Vilket? Ge en möjlig förklaring.<br>c) Vilken slutsats kan klassen dra? Vad betyder det för nedbrytningen på platserna?", None, 4, 7,
  "a) (46 + 52 + 39 + 58 + 45) / 5 = 48. b) 64 – t.ex. ett prov från en fuktigare plats, mer förna eller räknefel. c) Det fanns fler småkryp i den fuktiga lövskogen. Fler detritusätare och nedbrytare ger troligen snabbare nedbrytning där. Ett välutvecklat svar diskuterar att 64 påverkar medelvärdet och att fler prover behövs.", "a) 1 p. b) 1 p. c) 2 p (slutsats + koppling till nedbrytning och osäkerhet)."),
]
P1.P = P
P1.FIG = FIG
P1.NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
P1.BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
          ["12 Rådjur", "Nämner att maten tog slut eller att det var snö.", "Förklarar med bärkraft eller begränsande faktor.", "Använder båda begreppen, skiljer biotisk och abiotisk faktor och resonerar i flera led."],
          ["13 Vegetarisk mat", "Säger att växter ger mer mat.", "Förklarar att energin minskar i varje led.", "Använder energipyramiden, drar slutsats och ger ett motiverat argument för djurhållning."],
          ["14 Småkryp", "Räknar medelvärde.", "Pekar ut det avvikande värdet och drar en slutsats.", "Kopplar till nedbrytning, diskuterar det avvikande värdet och att fler prover behövs."]]
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    import re
    src = open('/tmp/bio/prov1.py', encoding='utf-8').read()
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        h = P1.build(lar)
        h = h.replace('Kapitel 1 · Prov', 'Kapitel 4 · Prov').replace('Biologi som vetenskap', 'Ekologi')
        # lärarvyn: anpassa texten om riktvärden och kopplingar
        e = sum(x[3] for x in P if x[0] == "E"); c = sum(x[3] for x in P if x[0] == "C"); a = sum(x[3] for x in P if x[0] == "A")
        te = math.ceil(e * 2 / 3); tc = math.ceil(c * 7 / 12); ta = math.ceil(a * 7 / 12)
        h = re.sub(r'Provet har \d+ p på del E, \d+ p på del C och \d+ p på del A \(totalt \d+ p\)', f'Provet har {e} p på del E, {c} p på del C och {a} p på del A (totalt {e+c+a} p)', h)
        h = re.sub(r'minst \d+ av \d+ p på del E, och uppgifterna visar[^<]*', f'minst {te} av {e} p på del E, och uppgifterna visar att eleven kan beskriva ekosystem, näringskedjor, energi och kretslopp med egna ord.', h)
        h = re.sub(r'minst \d+ av \d+ p på del C\.', f'minst {tc} av {c} p på del C.', h)
        h = re.sub(r'minst \d+ av \d+ p på del A, med', f'minst {ta} av {a} p på del A, med', h)
        h = re.sub(r'<h3>Kopplingar</h3><p>.*?</p><p class="note">Fakta kontrollerad mot kallor-omrade1.md\. ', '<h3>Kopplingar</h3><p>Uppgift 1–2, 4, 5 och 10: ekosystem, producenter, konsumenter och näringsvävar. Uppgift 3, 7 och 9: energins flöde och materiens kretslopp. Uppgift 8 och 9: nedbrytning och kolets kretslopp. Uppgift 6 och 12: populationer och begränsande faktorer. Uppgift 11 och 13: energi, näringskedjor och hållbarhet. Uppgift 14: tolka data och nedbrytning.</p><p class="note">', h, flags=re.S)
        if lar:
            FORM = ["F1","F1","F1","F1","F1","F1","F1","F1, F2","F1","F1","F1","F1","F1, F3","F1, F2"]
            FN = {"F1": "Begrepp, modeller och samband", "F2": "Systematiska undersökningar", "F3": "Granska information, kommunicera och ta ställning"}
            parts = h.split('<b>Facit:</b>')
            h = parts[0] + "".join(f'<b>Förmåga: {FORM[i]}</b><br><b>Facit:</b>' + p for i, p in enumerate(parts[1:]))
            tab = ('<table class="tbl"><tr><th>Förmåga</th><th>Uppgifter</th><th>Kommentar</th></tr>'
                   '<tr><td>1. Begrepp, modeller och samband</td><td>1–14</td><td>Provets huvudsakliga innehåll. Del E ger underlag för enkla beskrivningar, del C för utvecklade förklaringar och del A för välutvecklade resonemang.</td></tr>'
                   '<tr><td>2. Systematiska undersökningar</td><td>8 och 14</td><td>Endast tolkning och värdering av data. Planering, genomförande och dokumentation bedöms i labbarna 4.1–4.3 och i bonuslabben.</td></tr>'
                   '<tr><td>3. Granska information, kommunicera och ta ställning</td><td>13</td><td>Prövas bara i en uppgift. Bedöms även i diskussioner och uppgifter i område 5, där människans påverkan och hållbarhet behandlas.</td></tr></table>')
            h = re.sub(r'<h3>Riktvärden</h3>.*?(<p class="note">Poängen är en vägledning)', '<h3>Förmågor som provet prövar</h3>' + tab + r'\1', h, flags=re.S)
            h = h.replace('Del E går att klara med enbart lättläst-versionen av kapitlet, del C med grundtexten och del A med fördjupningen.', 'Provet prövar främst förmåga 1. Del E motsvarar innehållet i lättläst-versionen, del C grundtexten och del A fördjupningen.')
        h = h.replace('Poäng: ____ / 36', f'Poäng: ____ / {e+c+a}')
        h = h.replace('Provet är inte kalibrerat mot nationella prov.', 'Provet är inte kalibrerat mot nationella prov. Personer och mätvärden i uppgifterna är påhittade.')
        p = f'{OUT}/biologi-4-{name}.pdf'
        html_to_pdf(P1.doc(h, 'Kapitel 4 · Ekologi · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))
