# -*- coding: utf-8 -*-
"""Prov område 2 Cellen: elevversion och lärarversion (facit + bedömningsguide)."""
import sys, os
sys.path.insert(0, '/tmp/bio')
os.environ.setdefault('CH', '02n')
from bstyle import *
from bbuild_n import html_to_pdf, OUT
from pypdf import PdfReader
import prov1 as P1

FIG = '/tmp/bio/fig02n/'
def match(rub, left, right):
    return (f'<table class="tbl num" style="width:92%"><tr><th>{rub[0]}</th><th>{rub[1]}</th></tr>' + "".join(f"<tr><td style='font-weight:400'>{a}</td><td>{b}</td></tr>" for a, b in zip(left, right)) + '</table>')
TJAST = table(["Temperatur", "Gas efter 15 min"], [["5 °C", "1 cm"], ["20 °C", "4 cm"], ["35 °C", "12 cm"], ["50 °C", "3 cm"]], "tbl num")
TMITO = table(["Celltyp", "Mitokondrier per cell"], [["Hjärtmuskelcell", "ca 4 000"], ["Hudcell", "ca 200"], ["Röd blodkropp", "0"]], "tbl num")

P = [
 ("E", "Vilken del av en cell innehåller DNA hos djur och växter?", ["A Cellkärnan", "B Cellväggen", "C Vakuolen", "D Cellmembranet"], 1, 0, "A", "1 p för A."),
 ("E", "Vilken del har växtceller men inte djurceller?", ["A Cellmembran", "B Kloroplast", "C Ribosomer", "D Cytoplasma"], 1, 0, "B", "1 p för B."),
 ("E", "Dra streck mellan delen och uppgiften. Skriv bokstaven.<br>" + match(["Del", "Uppgift"], ["1 Mitokondrie", "2 Kloroplast", "3 Cellmembran"], ["A Bestämmer vad som kommer in och ut", "B Gör cellandning", "C Gör fotosyntes"]), None, 3, 0,
  "1 B, 2 C, 3 A", "1 p per rätt."),
 ("E", "Ett mikroskop har okular 10× och objektiv 40×. Hur många gånger förstoras preparatet? Visa hur du räknar.", None, 2, 2, "10 · 40 = 400 gånger.", "1 p för rätt metod (multiplicera), 1 p för rätt svar."),
 ("E", "Vilka två påståenden stämmer? Kryssa i två.<br>☐ Växter gör cellandning.<br>☐ Bakterier har cellkärna.<br>☐ Virus räknas oftast inte som levande.<br>☐ Antibiotika hjälper mot virus.", None, 2, 0,
  "Växter gör cellandning. Virus räknas oftast inte som levande.", "1 p per rätt. Avdrag om fler än två kryssas."),
 ("E", "Skriv fotosyntesen med ord.", None, 2, 2, "koldioxid + vatten + ljus → glukos + syre", "1 p för rätt ämnen in (koldioxid, vatten, ljus), 1 p för rätt ämnen ut (glukos, syre)."),
 ("E", "Skriv cellandningen med ord. Vilken del av cellen sker den i?", None, 2, 2, "glukos + syre → koldioxid + vatten + energi. Sker i mitokondrierna.", "1 p för rätt formel, 1 p för mitokondrierna."),
 ("C", "Cell X har cellvägg, kloroplaster och en stor vakuol. Cell Y har inget av detta.<br>a) Vilken är en växtcell och vilken en djurcell?<br>b) Förklara varför växtcellen behöver både kloroplaster och mitokondrier.", None, 3, 5,
  "a) X är en växtcell och Y en djurcell. b) Kloroplasterna gör fotosyntes, som bildar glukos och syre. Mitokondrierna gör cellandning, som frigör energi ur glukosen så att cellen kan använda den. Växtcellen behöver båda: den bygger glukos och måste sedan frigöra energin.", "a) 1 p. b) 1 p fotosyntes i kloroplasterna, 1 p cellandning i mitokondrierna (frigör energi)."),
 ("C", "a) Ge två skillnader mellan en bakteriecell och en djurcell.<br>b) Varför hjälper antibiotika mot halsfluss orsakad av bakterier men inte mot en förkylning?", None, 3, 5,
  "a) Bakterien saknar cellkärna (DNA ligger fritt), saknar mitokondrier, är mycket mindre, har ofta cellvägg. b) Halsfluss orsakad av bakterier angrips av antibiotika, som slår mot delar bakterier har. Förkylning orsakas av virus. Virus är inte celler och har inte de delarna, så antibiotika påverkar dem inte.", "a) 1 p per skillnad. b) 1 p (förkylning orsakas av virus / antibiotika verkar mot bakterier)."),
 ("C", "<span class='fake'>Påhittade värden</span> En klass undersökte hur temperaturen påverkar hur mycket gas jäst bildar. Gasen fångades i ballonger och mättes i cm efter 15 minuter.<br>" + TJAST + "a) Vid vilken temperatur bildades mest gas?<br>b) Förklara varför det bildades lite gas vid både 5 °C och 50 °C.<br>c) Hur kan klassen vara säker på att det är jästen som bildar gasen?", None, 4, 6,
  "a) 35 °C. b) Vid 5 °C går jästens reaktioner mycket långsamt. Vid 50 °C är det för varmt: jästen skadas, så den bildar mindre gas. c) Med ett kontrollförsök: samma blandning utan jäst, som inte ska bilda någon gas.", "a) 1 p. b) 1 p kallt = långsamt, 1 p varmt = skadas. c) 1 p kontrollförsök utan jäst."),
 ("C", "En krukväxt står i totalt mörker i ett dygn. Gör växten fotosyntes? Gör den cellandning? Förklara och beskriv vilken gas den tar upp och vilken den släpper ut.", None, 3, 5,
  "Ingen fotosyntes, eftersom den behöver ljus. Växten gör ändå cellandning hela tiden, eftersom alla celler behöver energi. Den tar upp syre och släpper ut koldioxid.", "1 p ingen fotosyntes i mörker, 1 p cellandning sker (dag och natt), 1 p rätt gaser."),
 ("C", "a) Skriv i rätt ordning, från minst till störst: organ, cell, organsystem, vävnad, organism.<br>b) Förklara varför en muskelcell har många mitokondrier.", None, 3, 5,
  "a) cell, vävnad, organ, organsystem, organism. b) Muskelceller arbetar hårt och behöver mycket energi. Mitokondrierna gör cellandning, som frigör energin, så fler mitokondrier ger mer energi.", "a) 1 p. b) 1 p mitokondrier gör cellandning/energi, 1 p muskelcellen behöver mycket energi (samband)."),
 ("A", "En elev säger: ”Växter gör fotosyntes på dagen och cellandning på natten. På dagen behöver de därför inget syre.” Värdera påståendet och förklara i flera led vad som egentligen händer.", None, 4, 7,
  "Påståendet stämmer inte. Växter gör cellandning hela tiden, även på dagen. På dagen gör de dessutom fotosyntes. Oftast gör växten mer fotosyntes än cellandning i ljus, så nettot blir att syre släpps ut, men cellandningen använder fortfarande syre. Syret från fotosyntesen kan användas direkt. På natten sker bara cellandning, så då tas syre upp och koldioxid släpps ut.", "1 p cellandning sker alltid, 1 p fotosyntes i ljus, 1 p nettot i ljus (mer fotosyntes än cellandning), 1 p natt: bara cellandning, gasutbyte."),
 ("A", "<span class='fake'>Påhittade värden</span> En forskare räknade mitokondrier i tre sorters celler.<br>" + TMITO + "a) Vilken celltyp har flest mitokondrier? Vad säger det om cellens behov?<br>b) Röda blodkroppar saknar mitokondrier men transporterar syre. Förklara hur det går ihop.<br>c) Vilken slutsats kan man dra, och vad mer skulle man vilja undersöka innan man är säker?", None, 4, 7,
  "a) Hjärtmuskelcellen. Den arbetar hela tiden och behöver mycket energi. b) Röda blodkroppar använder inte syret själva i cellandning, de transporterar det till andra celler. Utan mitokondrier och kärna får hemoglobin mer plats. c) Celler som behöver mycket energi har fler mitokondrier. Underlaget är litet: bara tre celltyper och okänt antal celler. Man vill undersöka fler celler och fler celltyper.", "a) 1 p. b) 1 p (transporterar syret, använder det inte själv). c) 1 p slutsats om samband, 1 p begränsning/vad mer."),
 ("A", "Du springer en kilometer. Förklara i flera led varför du andas snabbare och hjärtat slår fortare. Använd begreppen cellandning, glukos, syre och organsystem.", None, 4, 7,
  "Musklercellerna arbetar hårdare och behöver mer energi. De gör mer cellandning och använder mer glukos och syre, och bildar mer koldioxid. Syre och glukos måste föras fram och koldioxid bort snabbare. Andningssystemet tar in mer syre och släpper ut mer koldioxid, och cirkulationssystemet (hjärta och blod) transporterar ämnena fortare till och från cellerna. Därför andas du fortare och hjärtat slår fortare.", "1 p musklerna behöver mer energi/mer cellandning, 1 p mer syre och glukos förbrukas och mer koldioxid bildas, 1 p andningssystemet, 1 p cirkulationssystemet transporterar. Samband i flera led krävs."),
]
P1.P = P
P1.FIG = FIG
P1.NIVA = {"E": ("DEL E", "Grundläggande kunskaper"), "C": ("DEL C", "Utvecklade kunskaper"), "A": ("DEL A", "Välutvecklade kunskaper")}
P1.BED = [["Uppgift", "E-nivå", "C-nivå", "A-nivå"],
          ["10 Jäst", "Anger temperaturen med mest gas.", "Förklarar varför det blev lite gas vid kyla eller värme.", "Förklarar båda ytterligheterna och föreslår kontrollförsök."],
          ["13 Växten dag och natt", "Säger att växten gör fotosyntes i ljus.", "Förklarar att cellandning sker alltid.", "Förklarar nettogasutbytet dag och natt i flera led och värderar påståendet."],
          ["14 Mitokondrier", "Pekar ut celltypen med flest mitokondrier.", "Kopplar antalet till energibehov.", "Förklarar röda blodkroppar, drar försiktig slutsats och nämner vad som saknas."],
          ["15 Löpning", "Säger att musklerna behöver mer syre.", "Kopplar cellandning till mer syre och andning.", "Förklarar hela kedjan med både andnings- och cirkulationssystem."]]
P1.FORM = ["F1"] * 9 + ["F1, F2"] + ["F1"] * 2 + ["F1", "F1, F2", "F1"]
P1.FORM = ["F1", "F1", "F1", "F1", "F1", "F1", "F1", "F1", "F1", "F1, F2", "F1", "F1", "F1", "F1, F2", "F1"]
P1.FORMKOM = {"F1": "Provets huvudsakliga innehåll: celler, fotosyntes, cellandning, specialiserade celler och organsystem. Del E ger underlag för enkla beskrivningar, del C för utvecklade förklaringar och del A för välutvecklade resonemang.",
              "F2": "Endast tolkning och värdering av data (uppgift 10 och 14). Planering, genomförande och dokumentation bedöms i labbarna 2.1 och 2.2 och i bonuslabben.",
              "F3": "Prövas inte i det här provet. Bedöms i diskussioner och argumentation i undervisningen."}
P1.IMPROV = ""
P1.KOPPL = "Uppgift 1, 2, 3, 8 och 9: cellens delar, bakterier och virus. Uppgift 4: mikroskopering och förstoring. Uppgift 5, 6, 7, 11 och 13: fotosyntes och cellandning. Uppgift 10: jäst och temperatur (labb 2.2). Uppgift 12, 14 och 15: specialiserade celler, vävnader, organ och organsystem."
P1.KAP = "Kapitel 2"; P1.NAMN_ = "Cellen och livets processer"
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for lar, name in ((False, 'prov-elev'), (True, 'prov-larare')):
        h = P1.build(lar)
        p = f'{OUT}/biologi-2-{name}.pdf'
        html_to_pdf(P1.doc(h, 'Kapitel 2 · Cellen och livets processer · Prov' + (' · Lärarversion' if lar else '')), p)
        print(p, len(PdfReader(p).pages))
