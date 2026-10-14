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
TAB = table(["Plats", "Prov 1", "Prov 2", "Prov 3", "Prov 4", "Prov 5"], [["Komposthög", "15", "17", "14", "38", "16"], ["Gräsmatta", "4", "6", "5", "3", "7"]], "tbl num")

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
 ("C", "Elever grävde ner tepåsar i tre sorters jord och vägde dem när de grävdes upp igen." + fig(FIG+"p_nedbr.png", None, "62%") + "a) I vilken jord bröts teet ner mest?<br>b) Förklara resultatet med nedbrytare och abiotiska faktorer.<br>c) Varför grävde de ner flera påsar i varje jord?", None, 4, 6,
  "a) Skogsjord. b) Skogsjorden har mest förna och många nedbrytare och är fuktig. Sand är torr, har lite organiskt material och få nedbrytare, så det går långsamt. Fukt, temperatur och syre påverkar nedbrytarna. c) Så att slumpen mellan enskilda påsar jämnas ut.", "a) 1 p. b) 2 p (nedbrytare + abiotisk faktor + koppling). c) 1 p."),
  ("C", "En räv äter en hare. Haren har tidigare ätit gräs. Beskriv två olika vägar som ett kolatom i haren kan ta tillbaka till luften, och hur atomen sedan kan hamna i en växt igen.", None, 3, 5,
  "Väg 1: räven andas ut kolet som koldioxid (cellandning). Väg 2: räven eller haren dör, eller lämnar avföring, och nedbrytare bryter ner det och släpper ut koldioxid. Växter tar upp koldioxid från luften genom fotosyntesen och bygger in kolet i glukos.", "1 p för varje väg som tar kolet till luften (cellandning, nedbrytning), 1 p för att växter tar upp koldioxid med fotosyntes."),
  ("C", "I en sjö fiskades nästan all gädda bort under några år. Efter en tid blev vattnet grönt och grumligt av alger. Gädda äter abborre, små abborrar äter djurplankton och djurplankton äter växtplankton (alger). Använd näringskedjan för att förklara varför det blev så.", None, 3, 5,
  "Färre gäddor gör att fler abborrar överlever. Fler abborrar äter fler djurplankton. Färre djurplankton betar av färre alger, så algerna ökar och vattnet blir grönt. En kaskadeffekt i flera led.", "1 p fler abborrar när gäddan försvinner, 1 p färre djurplankton, 1 p fler alger."),
  ("C", "En pumpa växer från ett litet frö till en pumpa som väger 20 kg. Jorden i krukan väger nästan lika mycket efter säsongen som före. Nästan hela pumpans vikt är kol, väte och syre. Var kommer de flesta av dessa atomer ifrån, och hur kom de in i växten?", None, 2, 5,
  "Nästan allt kommer från koldioxid i luften och vatten. Växten tar upp koldioxid genom bladen och bygger in kolet i glukos genom fotosyntesen. Väte och syre kommer från vattnet som rötterna tar upp.", "1 p koldioxid/luft och vatten, 1 p fotosyntes/hur de kom in."),
  ("A", "Antalet sorkar på ett fält ökade i flera år och föll sedan kraftigt efter en mycket torr sommar." + fig(FIG+"p_sorkar.png", None, "62%") + "Använd begreppen bärkraft och begränsande faktor för att förklara varför. Ge också ett exempel på hur en biotisk faktor kan ha bidragit.", None, 4, 7,
  "Bärkraften är det största antal sorkar som fältet kan försörja. Populationen växte så att den närmade sig eller översteg bärkraften. Torkan (abiotisk faktor) gav mindre gräs, så maten blev den begränsande faktorn och många svalt. Biotisk faktor: konkurrens om föda, sjukdomar som sprids lättare i en tät population eller rovdjur (till exempel rävar och rovfåglar) som fångar fler när sorkarna är många.", "1 p bärkraft, 1 p begränsande faktor (mat), 1 p torka som abiotisk faktor, 1 p biotiskt exempel."),
  ("A", "Jonas säger: ”Om vi fiskar mer sill och mindre torsk kan havet ge oss fler kilo fisk att äta.” Sill äter djurplankton och torsk äter bland annat sill. Använd energipyramiden för att resonera om Jonas har rätt. Ge också en risk med att fiska mycket sill.", None, 4, 7,
  "Jonas har i stort sett rätt: energin minskar med ungefär 90 % för varje led, så sillen står närmare producenterna och det finns mer av den än av torsk. Fler kilo fisk kan tas ut från en lägre nivå. Risk: sillen är föda åt torsk, säl och fåglar, så om för mycket fiskas kan de få mindre mat (en kaskadeffekt), och sillbeståndet kan minska för mycket.", "1 p energin minskar i varje led, 1 p mer mat från lägre nivå, 1 p slutsats, 1 p risk (annan art får mindre mat eller beståndet minskar)."),
  ("A", "En klass räknade daggmaskar i jordprover från två platser. De tog fem prover på varje plats.<br>" + TAB + "a) Räkna ut medelvärdet för gräsmattan.<br>b) Ett värde från komposten skiljer sig från de andra. Vilket? Ge en möjlig förklaring.<br>c) Vilken slutsats kan klassen dra? Vad betyder det för nedbrytningen på platserna?", None, 4, 7,
  "a) (4 + 6 + 5 + 3 + 7) / 5 = 5 daggmaskar. b) 38 – t.ex. provet togs i en bit av komposten med mycket nytt matavfall, eller en klunga daggmaskar råkade hamna i samma prov, eller räknefel. c) Det fanns fler daggmaskar i komposten, där det finns mer dött material och fukt. Fler detritusätare ger troligen snabbare nedbrytning där. Ett välutvecklat svar diskuterar att 38 påverkar medelvärdet och att fler prover behövs.", "a) 1 p. b) 1 p. c) 2 p (slutsats + koppling till nedbrytning och osäkerhet)."),
]
_j = P.pop(13); P.insert(11, ("C",) + _j[1:])
P1.P = P
P1.FIG = FIG
P1.NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
P1.BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
          ["12 Daggmaskar", "Räknar medelvärde.", "Pekar ut det avvikande värdet och drar en slutsats.", "Kopplar till nedbrytning, diskuterar det avvikande värdet och att fler prover behövs."],
          ["13 Sorkar", "Nämner att maten tog slut eller att det var torka.", "Förklarar med bärkraft eller begränsande faktor.", "Använder båda begreppen, skiljer biotisk och abiotisk faktor och resonerar i flera led."],
          ["14 Sillfiske", "Säger att sillen finns i större mängd än torsken.", "Förklarar att energin minskar i varje led.", "Använder energipyramiden, drar slutsats och ger en motiverad risk med att fiska mycket sill."]]
P1.FORM = ["F1"] * 7 + ["F1, F2"] + ["F1"] * 3 + ["F1, F2", "F1", "F1, F3"]
P1.FORMKOM = {"F1": "Provets huvudsakliga innehåll. Del E ger underlag för enkla beskrivningar, del C för utvecklade förklaringar och del A för välutvecklade resonemang.",
              "F2": "Endast tolkning och värdering av data (uppgift 8 och 12). Planering, genomförande och dokumentation bedöms i labbarna 4.1–4.3 och i bonuslabben.",
              "F3": "Prövas bara i en uppgift (14). Bedöms också i diskussioner och argumentation i undervisningen."}
P1.IMPROV = ""
P1.KOPPL = "Uppgift 1, 2, 5 och 10: ekosystem, producenter, konsumenter och näringsvävar. Uppgift 3, 4, 7 och 11: energins flöde och materiens kretslopp. Uppgift 8 och 9: nedbrytning och kolets kretslopp. Uppgift 6 och 13: populationer och begränsande faktorer. Uppgift 12: tolka data och nedbrytning. Uppgift 14: energi, näringskedjor och hållbart fiske."
P1.KAP = "Kapitel 4"; P1.NAMN_ = "Ekologi"
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        h = P1.build(lar)
        p = f'{OUT}/biologi-4-{name}.pdf'
        html_to_pdf(P1.doc(h, 'Kapitel 4 · Ekologi · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))
