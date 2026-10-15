# -*- coding: utf-8 -*-
"""Prov område 3 Biologisk mångfald: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os
sys.path.insert(0, '/tmp/bio')
os.environ.setdefault('CH', '03n')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader
import prov1 as P1

FIG = '/tmp/bio/fig03n/'
def match(rub, left, right):
    return (f'<table class="tbl num" style="width:92%"><tr><th>{rub[0]}</th><th>{rub[1]}</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')
TANG = table(["Äng", "Ruta 1", "Ruta 2", "Ruta 3"], [["Betad äng", "21", "18", "24"], ["Igenvuxen äng", "9", "12", "6"]], "tbl num")

P = [
 ("E", "Vilken nivå av biologisk mångfald handlar om skillnader mellan individer av samma art?", ["A Genetisk mångfald", "B Artmångfald", "C Ekosystemmångfald", "D Population"], 1, 0, "A", "1 p för A."),
 ("E", "Vilket är ett exempel på en reglerande ekosystemtjänst?", ["A Virke från skogen", "B Bär som du plockar", "C Humlor som pollinerar blåbärsris", "D En vandring i fjällen"], 1, 0, "C", "1 p för C."),
 ("E", "Dra streck mellan begreppet och förklaringen. Skriv bokstaven.<br>" + match(["Begrepp", "Förklaring"], ["1 Population", "2 Rödlista", "3 Signalart"], ["A Art som visar att miljön har höga naturvärden", "B Alla individer av en art i ett område", "C Lista över arter som riskerar att dö ut"]), None, 3, 0,
  "1 B, 2 C, 3 A", "1 p per rätt."),
 ("E", "Nämn två hot mot den biologiska mångfalden och ge ett exempel på vardera.", None, 3, 2, "T.ex. ändrad markanvändning (skog avverkas), överuttag (överfiske), klimatförändringar, föroreningar (plast), invasiva arter (blomsterlupin).", "1 p per hot med rimligt exempel."),
 ("E", "Vilka två påståenden stämmer? Kryssa i två.<br>☐ Svampar är växter.<br>☐ En lav är en svamp och en alg som lever ihop.<br>☐ Bakterier har cellkärna.<br>☐ Varje art har ett vetenskapligt namn med två latinska ord.", None, 2, 0,
  "En lav är en svamp och en alg som lever ihop. Varje art har ett vetenskapligt namn med två latinska ord.", "1 p per rätt. Avdrag om fler än två kryssas."),
 ("E", "Vad är en bestämningsnyckel och hur använder man den?", None, 3, 2, "En serie val med två alternativ. Man jämför kännetecken hos arten och följer valen steg för steg tills man kommer fram till artens namn.", "1 p för att nyckeln består av val/kännetecken, 1 p för att man följer valen till artens namn."),
 ("E", "Ge ett exempel på en anpassning hos ett djur eller en växt och förklara hur den hjälper arten.", None, 3, 2, "T.ex. fjällrävens tjocka päls som gör att den inte fryser, eller renens breda klövar som bär på snö.", "1 p för en riktig anpassning, 1 p för att förklara hur den hjälper."),
 ("C", "<span class='fake'>Påhittade värden</span> En klass räknade växtarter i provrutor på 1 m² på två ängar. Antal arter per ruta:<br>" + TANG + "a) Räkna ut medelvärdet för varje äng.<br>b) Ge en möjlig förklaring till skillnaden.", None, 4, 5,
  "a) Betad: (21 + 18 + 24) / 3 = 21. Igenvuxen: (9 + 12 + 6) / 3 = 9. b) Betet håller ängen öppen så att fler arter får ljus. På den igenvuxna ängen skuggar höga växter och tränger undan andra.", "a) 1 p per rätt medelvärde. b) 1 p för en rimlig förklaring, 1 p för att koppla till mångfald, ljus eller konkurrens."),
 ("C", "I en skog finns både ljusa och mörka fjärilar. Skogens trädstammar är ljusa. Förklara med variation, urval och ärftlighet varför de ljusa fjärilarna blir vanligare.", None, 4, 5,
  "Fjärilarna är olika (variation). De ljusa syns sämre på ljus bark, så fåglar tar de mörka oftare (urval). De ljusa överlever och får fler ungar, och färgen går i arv, så de ljusa blir vanligare (ärftlighet).", "1 p variation, 1 p urval med förklaring om kamouflage, 1 p ärftlighet, 1 p kopplar till att de ljusa blir fler."),
 ("C", "En myr dikas ut och blir torr mark. Ge två ekosystemtjänster som kan minska och förklara varför.", None, 4, 5,
  "T.ex. vattenrening: myren filtrerade vattnet. Minskad översvämningsrisk: myren tog upp vatten som en svamp. Kolinlagring och livsmiljö för arter är andra svar.", "Per tjänst: 1 p för att namnge, 1 p för att förklara. 1 p för tydlig koppling till att myren försvinner."),
 ("C", "En sjö har kedjan: alger → djurplankton → abborre → gädda. Nästan alla abborrar fiskas bort. Förklara vad som kan hända med djurplankton och gäddor.", None, 4, 5,
  "Färre abborrar äter djurplankton, så djurplankton kan öka. Gäddorna får mindre mat och kan minska. Gäddorna kan äta andra fiskar, så effekten beror på hur många alternativ de har.", "1 p djurplankton ökar, 1 p förklaring (färre som äter dem), 1 p gäddor minskar, 1 p förklaring."),
 ("C", "Förklara varför en blandskog med många arter klarar en torka bättre än en plantage med bara en trädart.", None, 4, 5,
  "Olika arter tål torka olika bra. I blandskogen överlever några arter och skogen finns kvar. I plantagen drabbas alla träd lika, så allt kan dö. Det är en sorts försäkring. Fler arter betyder också fler som kan ta över uppgifter.", "1 p arter är olika, 1 p några klarar torkan, 1 p plantagen drabbas helt, 1 p koppling till motståndskraft/försäkring."),
 ("A", "Wilma säger: ”Antalet rödlistade arter har ökat sedan år 2000. Alltså går det sämre för naturen.” Värdera påståendet. Tänk på att antalet bedömda arter också har ökat, från cirka 19 000 till drygt 23 000.", None, 5, 7,
  "Påståendet är för förenklat. Fler rödlistade arter kan bero på att forskarna har bedömt fler arter, inte bara att fler har det sämre. Man måste jämföra andelar eller samma arter över tid. Rödlistan visar ändå att många arter är hotade, och förändringar i enskilda arter (t.ex. utter och havsörn som blivit friska) visar att det går åt olika håll.", "1 p ifrågasätter slutsatsen, 2 p förklarar med fler bedömda arter, 2 p föreslår bättre jämförelse (andelar), 2 p nyanserar (visar både sidor)."),
 ("A", "Kommunen vill bebygga en gammal skog med garnlav. Redovisa argument för och emot, väg dem mot varandra och ta ställning. Beskriv också vad du är osäker på.", None, 6, 7,
  "Öppet svar. Emot: gammal skog tar hundratals år att återskapa, hem för arter, garnlav är en signalart och föda för ren. För: bostäder, jobb. Välutvecklat svar väger flera argument, nämner vem som berörs och vad man är osäker på, och ger ett motiverat ställningstagande.", "2 p argument för och emot med biologi, 2 p vägning mellan dem, 1 p ställningstagande, 2 p osäkerheter/alternativ (t.ex. bygga på annan mark)."),
 ("A", "Elias tror att det finns fler arter av lavar i gammal skog än i ung, planterad skog. Planera en undersökning som kan pröva hans idé. Beskriv vad du ska räkna, hur du gör jämförelsen rättvis, hur du dokumenterar och vad som kan göra slutsatsen osäker.", None, 6, 7,
  "Räkna lavarter i lika stora provrutor eller på lika många träd i gammal och ung skog. Samma storlek, trädslag, tid och sökmetod. Flera upprepningar och medelvärde. Foton och tabell. Osäkerhet: få rutor, svårt att skilja arter, skogarna kan skilja sig på annat sätt (t.ex. läge).", "1 p vad man räknar, 2 p rättvis jämförelse, 1 p upprepningar, 1 p dokumentation, 2 p felkällor och hur säker slutsatsen blir."),
]
P1.P = P
P1.FIG = FIG
P1.NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
P1.BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
          ["8 Ängar", "Räknar ut medelvärden.", "Förklarar skillnaden med bete eller ljus.", "Kopplar skillnaden till mångfald och konkurrens."],
          ["9 Fjärilar", "Säger att de ljusa syns sämre.", "Förklarar urval med variation och ärftlighet.", "Förklarar hela kedjan i flera led."],
          ["13 Rödlistan", "Säger att fler arter är hotade.", "Ser att fler bedömda arter kan förklara ökningen.", "Värderar och föreslår bättre jämförelse."],
          ["14 Skogsfrågan", "Ger ett argument.", "Ger argument för och emot.", "Väger argument, visar osäkerheter och tar motiverat ställning."],
          ["15 Lavar", "Föreslår att räkna lavar.", "Planerar med variabler och upprepningar.", "Värderar metoden, felkällor och hur säker slutsatsen blir."]]
P1.FORM = ["F1"] * 7 + ["F1, F2"] + ["F1"] * 4 + ["F1, F2", "F1, F3", "F2"]
P1.FORMKOM = {"F1": "Provets huvudsakliga innehåll: biologisk mångfald, ekosystemtjänster, hot, riken, bestämningsnycklar, anpassning och naturligt urval. Del E ger underlag för enkla beskrivningar, del C för utvecklade förklaringar och del A för välutvecklade resonemang.",
              "F2": "Tolkning och värdering av data (uppgift 8 och 13) och planering av en undersökning (uppgift 15). Genomförande och dokumentation bedöms i labbarna 3.1 och 3.2.",
              "F3": "Värdering av en samhällsfråga (uppgift 14). Bedöms också i diskussioner och argumentation i undervisningen."}
P1.IMPROV = ""
P1.KOPPL = "Uppgift 1 och 12: genetisk mångfald och stabilitet. Uppgift 2 och 10: ekosystemtjänster. Uppgift 3, 4, 13 och 14: begrepp, hot och rödlistan. Uppgift 5 och 6: riken och bestämningsnycklar (labb 3.2). Uppgift 7 och 9: anpassning och naturligt urval. Uppgift 8 och 15: undersökning och provrutor (labb 3.1). Uppgift 11: näringsväv."
P1.KAP = "Kapitel 3"; P1.NAMN_ = "Biologisk mångfald"
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        h = P1.build(lar)
        p = f'{OUT}/biologi-3-{name}.pdf'
        html_to_pdf(P1.doc(h, 'Kapitel 3 · Biologisk mångfald · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))
