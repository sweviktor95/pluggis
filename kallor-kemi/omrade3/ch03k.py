# -*- coding: utf-8 -*-
"""Kemi område 3 Atomer och grundämnen – grundtext (per moment). Samma format som område 1–2."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
FIG = '/tmp/kem/fig03k/'
NR = 3
SLUG = "kemi-atomer"
TAB = "3"
NAMN = "Atomer och grundämnen"
UNDER = "Byggstenarna i allt"
INTRO = ("Allt omkring dig, från skolbänken till din egen kropp, är gjort av atomer. Men hur kan något så litet att man aldrig ser det vara byggstenen i allt? Och varför ser det periodiska systemet, som hänger på väggen i många kemisalar, ut som det gör? "
         "I det här kapitlet tittar du in i atomen: vilka partiklar den består av, hur människor genom experiment kommit fram till hur den ser ut och hur modellerna har ändrats. Du lär dig också hur grundämnena är ordnade i det periodiska systemet och varför ämnen i samma grupp liknar varandra. "
         "Namn och mätvärden i uppgifterna är påhittade, om inget annat står.")
MAL = ["hur en atom är uppbyggd av protoner, neutroner och elektroner", "hur du bestämmer antalet partiklar utifrån atomnummer och masstal",
       "hur atommodellerna har ändrats när nya experiment gjordes", "vad isotoper och radioaktivitet är, och vilka användningar och risker det finns",
       "hur det periodiska systemet är ordnat och vad metaller, icke-metaller och halvmetaller har för egenskaper", "varför grundämnen i samma grupp liknar varandra, och hur det hänger ihop med elektronerna",
       "vilka grundämnen som är vanligast i jordskorpan och i kroppen"]
FUNDERA = "Tänk dig att du har en liten guldbit och delar den i hälften, och sedan i hälften igen, om och om igen. Hur tror du att det slutar? Skriv din gissning och spara den. I slutet av kapitlet får du se om du ändrar dig."
DELOMR = {"3.1": "Atomens byggnad", "3.2": "Periodiska systemet"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)

KQ = {
 "Start": [("Vad är en atom?", "En mycket liten byggsten som allt är gjort av. Atomer av samma sort bildar ett grundämne."),
           ("Hur många grundämnen finns det ungefär, och hur många är framställda av människan?", "Det finns 118 erkända grundämnen. Ungefär 90 finns i naturen och ungefär 30 har framställts."),
           ("Hur stor är en atom ungefär, och hur stor är dess kärna i förhållande till atomen?", "Atomen är ungefär 0,1 nm i radie (1 · 10⁻¹⁰ m). Kärnans radie är mindre än en tiotusendel av atomens.")],
 "3.1.1": [("Vilka tre sorters partiklar finns i en atom, och var finns de?", "Protoner och neutroner finns i atomkärnan. Elektroner finns i skal utanför kärnan."),
           ("Vilken laddning har protonen, neutronen och elektronen?", "Protonen +1, neutronen 0 och elektronen −1."),
           ("Varför är en atom neutral?", "Den har lika många elektroner som protoner, så de negativa och positiva laddningarna tar ut varandra."),
           ("Vad visar atomnumret och vad visar masstalet?", "Atomnumret är antalet protoner. Masstalet är antalet protoner plus antalet neutroner."),
           ("En fosforatom har atomnummer 15 och masstal 31. Hur många protoner, neutroner och elektroner har den?", "15 protoner, 31 − 15 = 16 neutroner och 15 elektroner."),
           ("Vad är det som bestämmer vilket grundämne en atom tillhör?", "Antalet protoner, alltså atomnumret.")],
 "3.1.2": [("Vad innebar Daltons atommodell?", "Att allt består av små, odelbara atomer och att atomer av samma grundämne är lika."),
           ("Vad var Thomsons modell, i korthet?", "Positiv laddning utspridd i atomen med elektroner inbäddade, som russin i en kaka (plumpuddingmodellen)."),
           ("Vad såg man i Rutherfords försök med alfapartiklar mot guldfolie?", "De flesta alfapartiklarna gick rakt igenom folien, men några få avlänkades."),
           ("Vilken slutsats drog Rutherford 1911?", "Att den positiva laddningen och nästan hela massan finns samlad i en mycket liten kärna, och att atomen mestadels är tom."),
           ("Vad innebar Bohrs modell från 1913?", "Att elektronerna rör sig i bestämda banor (skal) med bestämd energi runt kärnan."),
           ("Nämn en begränsning hos Bohrs modell.", "Den fungerar bra för väte men inte för atomer med flera elektroner. På 1920-talet ersattes den av kvantmekaniken.")],
 "3.1.3": [("Vad är isotoper?", "Atomer av samma grundämne, alltså med samma antal protoner, men med olika antal neutroner."),
           ("Hur många protoner och neutroner har kol-12 och kol-14?", "Kol-12: 6 protoner och 6 neutroner. Kol-14: 6 protoner och 8 neutroner."),
           ("Vad är radioaktivitet?", "Att en instabil atomkärna sönderfaller och sänder ut partiklar eller strålning."),
           ("Vad menas med halveringstid?", "Den tid det tar för hälften av atomerna i ett prov att sönderfalla."),
           ("Ett ämne har halveringstiden 10 år. Hur mycket finns kvar av 80 g efter 20 år? Värdena är påhittade.", "80 g → 40 g efter 10 år → 20 g efter 20 år. Det finns 20 g kvar."),
           ("Nämn en användning och en risk med radioaktiv strålning.", "Användning: t.ex. strålbehandling, bilddiagnostik eller åldersbestämning med kol-14. Risk: strålningen är joniserande och kan skada celler.")],
 "3.2.1": [("Hur är grundämnena ordnade i det periodiska systemet?", "I ordning efter stigande atomnummer."),
           ("Vad kallas raderna och vad kallas kolumnerna?", "Raderna kallas perioder och kolumnerna kallas grupper."),
           ("Nämn tre egenskaper som är typiska för metaller.", "De leder värme och el, de glänser och de går att forma (böja eller hamra) utan att gå sönder."),
           ("Vad kännetecknar icke-metaller?", "De är dåliga ledare av värme och el, fasta icke-metaller är spröda och många är gaser."),
           ("Vad är en halvmetall? Ge ett exempel.", "Ett grundämne med egenskaper mellan metall och icke-metall, till exempel kisel."),
           ("Vem ordnade grundämnena 1869, och vad gjorde han med de luckor som uppstod?", "Dmitrij Mendelejev. Han lämnade luckor och förutsade egenskaper hos grundämnen som ännu inte hittats.")],
 "3.2.2": [("Vad är valenselektroner?", "Elektronerna i yttersta skalet."),
           ("Varför liknar ämnen i samma grupp varandra?", "De har samma antal elektroner i yttersta skalet, och det är de som avgör hur ämnena reagerar."),
           ("Nämn tre egenskaper hos alkalimetallerna.", "De har en elektron i yttersta skalet, är mjuka, har låg densitet och reagerar kraftigt med vatten. De förvaras under olja."),
           ("Hur ändras reaktiviteten nedåt i gruppen för alkalimetaller och för halogener?", "Alkalimetallerna blir mer reaktiva nedåt, halogenerna blir mindre reaktiva nedåt."),
           ("Varför är ädelgaserna så oreaktiva?", "Deras yttersta skal är fullt, så de behöver varken ta upp eller avge elektroner."),
           ("Nämn en användning för en ädelgas.", "Helium i ballonger, neon i skyltar eller argon som skyddsgas vid svetsning.")],
 "3.2.3": [("Vilka är de två vanligaste grundämnena i jordskorpan?", "Syre (ungefär 47 viktprocent) och kisel (ungefär 28 viktprocent)."),
           ("Vilka grundämnen utgör mest av människokroppens massa?", "Syre, kol, väte och kväve, med syre som störst."),
           ("Varför skiljer sig siffrorna för kroppen något mellan olika källor?", "Källorna redovisar avrundade medelvärden och kan räkna lite olika. Därför skriver man ”ungefär”."),
           ("Nämn tre grundämnen som är viktiga för liv.", "T.ex. syre, kol, väte, kväve, kalcium och fosfor."),
           ("Nämn ett grundämne som du använder i vardagen och vad det används till.", "T.ex. aluminium i folie, järn i stål eller koppar i elledningar.")],
}
def kq(key):
    return kolla(key if key != "Start" else "Start", [q for q, a in KQ[key]])

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Vad är en atom?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p>I kapitel 2 lärde du dig att allt består av partiklar. Nu tittar vi på de minsta byggstenarna: <strong class='green'>atomerna</strong>. En atom är så liten att du aldrig kan se den med ögat, och inte heller i ett vanligt mikroskop. Dess radie är ungefär 0,1 nanometer, alltså 1 · 10⁻¹⁰ meter.</p>"
     "<p>Atomer av samma sort bildar ett <strong class='green'>grundämne</strong>. Det finns 118 erkända grundämnen. Ungefär 90 av dem finns i naturen, och ungefär 30 har människan framställt. Några exempel är syre, järn, guld och kol. Alla andra ämnen är kombinationer av atomer från de här grundämnena.</p>"
     "<p>En atom består av en liten <strong class='green'>kärna</strong> i mitten med <strong class='green'>elektroner</strong> runt omkring. Kärnan är mycket mindre än atomen: dess radie är mindre än en tiotusendel av atomens. Som jämförelse: om atomen vore så stor som en fotbollsarena skulle kärnan vara ungefär lika liten som ett knappnålshuvud, och nästan hela volymen skulle vara tom. Jämförelsen är en bild, inte en exakt mätning.</p>"
     "<p>I det här kapitlet svarar vi på tre frågor:</p>"
     + bullets(["Vad består en atom av, och hur vet man det?", "Hur har atommodellerna ändrats när nya experiment gjorts?", "Hur är grundämnena ordnade i det periodiska systemet, och vad säger platsen om ämnets egenskaper?"]),
   [begrepp([("Atom", "Mycket liten byggsten som allt är gjort av."), ("Grundämne", "Ämne som består av en sorts atomer."), ("Atomkärna", "Den lilla kärnan i mitten av atomen.")]),
    box("tank", "Tänk efter", "<p>Du kan inte se en atom. Hur kan man ändå veta något om hur den ser ut? Skriv ner dina idéer. I delområde 3.1 ser du hur forskare gjorde.</p>")])
 + fig(FIG+"v_oversikt.png", "<b>Bild 3.1</b> Från en bit metall till atomen. Varje steg är kraftigt förstorat och bilderna är schematiska, inte skalenliga.", "96%")
 + table(["Delområde", "Du lär dig"],
         [["<b>3.1</b> Atomens byggnad", "Protoner, neutroner och elektroner, atomnummer och masstal, atommodellernas historia, isotoper och radioaktivitet. Labb: svarta lådan."],
          ["<b>3.2</b> Periodiska systemet", "Hur grundämnena är ordnade, metaller och icke-metaller, grupper med släktskap och grundämnen i naturen och kroppen. Labb: metaller och icke-metaller."]])
 + kq("Start"))

# ------------------------------------------------------------------ 3.1.1
add("3.1.1", "Atomen och dess partiklar", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Atomen och dess partiklar",
 roww("<p>Atomen består av tre sorters partiklar. I kärnan finns <strong class='green'>protoner</strong> och <strong class='green'>neutroner</strong>. Utanför kärnan finns <strong class='green'>elektroner</strong>, som ligger i olika <strong class='green'>elektronskal</strong>. Partiklarna skiljer sig åt i laddning och massa.</p>"
      "<p>Protonen har laddningen +1 och neutronen har laddningen 0. Elektronen har laddningen −1. Protonen och neutronen har ungefär samma massa, och elektronens massa är bara ungefär en tvåtusendel av det, så den räknas oftast som noll. Nästan hela atomens massa finns alltså i kärnan.</p>"
      "<p>En atom har lika många elektroner som protoner. Därför tar de positiva och negativa laddningarna ut varandra, och atomen är <strong class='green'>neutral</strong> (har ingen sammanlagd laddning).</p>",
      [begrepp([("Proton", "Positiv partikel i kärnan."), ("Neutron", "Partikel utan laddning i kärnan."), ("Elektron", "Negativ partikel utanför kärnan."), ("Elektronskal", "Område runt kärnan där elektronerna rör sig.")])])
 + fig(FIG+"v_atom.png", "<b>Bild 3.2</b> En kolatom (schematisk): 6 protoner och 6 neutroner i kärnan och 6 elektroner i skal runt omkring. Storleksförhållandena är inte skalenliga.", "46%")
 + table(["Partikel", "Laddning", "Massa", "Plats i atomen"],
         [["Proton", "+1", "ungefär 1 (relativ massa)", "Atomkärnan"], ["Neutron", "0", "ungefär 1 (relativ massa)", "Atomkärnan"], ["Elektron", "−1", "ungefär 0 (mycket liten)", "Elektronskalen"]], "tbl")
 + "<h3>Atomnummer och masstal</h3>"
 + roww("<p>Det som avgör vilket grundämne en atom tillhör är antalet protoner. Det kallas <strong class='green'>atomnummer</strong>. Alla kolatomer har 6 protoner, alla syreatomer har 8 och alla järnatomer har 26.</p>"
        "<p><strong class='green'>Masstalet</strong> är antalet protoner plus antalet neutroner, alltså antalet partiklar i kärnan. Därför kan du räkna ut antalet neutroner:</p>"
        "<p style='text-align:center'><b>neutroner = masstal − atomnummer</b></p>"
        "<p>Ett exempel: en fosforatom har atomnummer 15 och masstal 31. Den har då 15 protoner, 31 − 15 = 16 neutroner och 15 elektroner (lika många som protonerna).</p>",
        [begrepp([("Atomnummer", "Antalet protoner i kärnan."), ("Masstal", "Antal protoner plus antal neutroner."), ("Neutral", "Utan sammanlagd laddning.")])])
 + '<div style="break-inside:avoid">' + table(["Grundämne", "Beteckning", "Atomnummer", "Masstal*", "Neutroner"],
         [["Väte", "H", "1", "1", "0"], ["Helium", "He", "2", "4", "2"], ["Kol", "C", "6", "12", "6"], ["Syre", "O", "8", "16", "8"], ["Natrium", "Na", "11", "23", "12"], ["Järn", "Fe", "26", "56", "30"]], "tbl num") + '</div>'
 + "<p class='note'>*Masstalet är för den vanligaste varianten av atomen. Du lär dig mer om varianter (isotoper) i 3.1.3. Varje grundämne har en kemisk beteckning på en eller två bokstäver, där den första är stor.</p>"
 + "<h3>Elektronerna och skalen</h3>"
 + "<p>Elektronerna ligger i skal runt kärnan, och varje skal rymmer ett bestämt antal. I den förenklade modell som vi använder rymmer det första skalet 2 elektroner och det andra skalet 8. Därefter fylls det tredje skalet, som i den här modellen också rymmer 8 för de första 20 grundämnena. Elektronerna i det yttersta skalet kallas <strong class='green'>valenselektroner</strong>. De är viktiga eftersom de avgör hur ämnet reagerar, vilket du får se i 3.2.</p>"
 + box("tank", "Tänk efter", "<p>En atom har atomnummer 11 och masstal 23. Hur många protoner, neutroner och elektroner har den? Vilket grundämne är det?</p>")
 + kq("3.1.1"))

# ------------------------------------------------------------------ 3.1.2
add("3.1.2", "Atommodellernas historia", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Atommodellernas historia",
 row("<p>Ingen har sett en atom med blotta ögat, så hur kan vi veta hur den är uppbyggd? Svaret är att forskare har gjort experiment och dragit slutsatser av vad de såg, precis som du gör när du undersöker. När nya experiment gav resultat som den gamla modellen inte kunde förklara byggde man en ny modell. I kapitel 1 lärde du dig att modeller förklarar och förutsäger men inte är samma sak som verkligheten. Atommodellerna är ett bra exempel.</p>",
   [begrepp([("Atommodell", "Förenklad bild av hur en atom är uppbyggd."), ("Katodstrålar", "Strålar som man kunde se i rör med lite gas när det fanns hög spänning. De visade sig bestå av elektroner.")])])
 + "<h3>Dalton: atomen som en liten kula</h3>"
 + "<p>I början av 1800-talet (1808) föreslog John Dalton att allt består av små, odelbara atomer och att atomer av samma grundämne är lika. Atomen var enligt honom som en liten, hård kula utan inre delar. Det kunde förklara varför massan bevaras vid kemiska reaktioner, vilket Lavoisier hade visat.</p>"
 + "<h3>Thomson: plumpuddingmodellen</h3>"
 + "<p>Mot slutet av 1800-talet visade experiment med katodstrålar att det finns små, negativt laddade partiklar i atomerna: elektronerna. Då kunde atomen inte vara odelbar. Joseph John Thomson föreslog att atomen består av en utspridd positiv laddning med elektronerna inbäddade i den, som russin i en kaka. Modellen kallas därför ofta <strong class='green'>plumpuddingmodellen</strong>.</p>"
 + "<h3>Rutherford: atomen har en kärna</h3>"
 + roww("<p>År 1909 lät Ernest Rutherford och hans medarbetare skjuta små, positivt laddade partiklar (alfapartiklar) mot en mycket tunn guldfolie. Om Thomsons modell stämde borde alla partiklar gå rakt igenom eller böjas av lite. Det som hände var annorlunda: de flesta partiklarna gick rakt igenom, men några få avlänkades kraftigt.</p>"
        "<p>År 1911 drog Rutherford slutsatsen att atomens positiva laddning och nästan hela dess massa finns samlad i en mycket liten <strong class='green'>kärna</strong>. Elektronerna finns utanför kärnan, och atomen är mestadels tom. Atomen är ungefär 100 000 gånger större än kärnan, mätt i diameter.</p>",
        [fig(FIG+"v_rutherford.png", "<b>Bild 3.3</b> Rutherfords försök (schematiskt): de flesta partiklarna går rakt igenom guldfolien, några få avlänkas, och mycket få kastas tillbaka.", "100%")])
 + "<h3>Bohr: elektroner i skal</h3>"
 + "<p>År 1913 föreslog Niels Bohr att elektronerna rör sig runt kärnan i bestämda banor, så kallade skal, och att varje bana har en bestämd energi. När en elektron hoppar mellan banor sänder atomen ut eller tar upp ljus. Modellen kunde förklara hur väte sänder ut ljus. Den fungerar däremot inte bra för atomer med flera elektroner, och på 1920-talet ersattes den av en mer avancerad modell, kvantmekaniken. Skalmodellen använder vi ändå i skolan, eftersom den är enkel och förklarar mycket, till exempel varför ämnen i samma grupp liknar varandra.</p>"
 + fig(FIG+"v_modeller.png", "<b>Bild 3.4</b> Fyra atommodeller i tidsordning: Dalton, Thomson, Rutherford och Bohr. Bilderna är schematiska.", "100%")
 + table(["Modell", "Årtal", "Idé", "Det som ledde till nästa modell"],
         [["Dalton", "1808", "Atomen är en liten, odelbar kula", "Elektronen upptäcktes, så atomen har delar"], ["Thomson", "slutet av 1800-talet", "Utspridd positiv laddning med elektroner i", "Alfapartiklar avlänkades i guldfolien"],
          ["Rutherford", "1911", "Liten, tung kärna med elektroner utanför", "Kunde inte förklara hur atomen sänder ut ljus"], ["Bohr", "1913", "Elektroner i skal med bestämd energi", "Fungerade inte för atomer med flera elektroner"]], "tbl")
 + box("tank", "Tänk efter", "<p>Varför ersätter man inte en modell bara för att den är enkel? När är det rätt att byta modell, och när räcker det med att komplettera den?</p>")
 + kq("3.1.2"))

# ------------------------------------------------------------------ 3.1.3
add("3.1.3", "Isotoper och radioaktivitet i korthet", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Isotoper och radioaktivitet i korthet",
 roww("<p>Alla atomer av ett grundämne har samma antal protoner, men antalet neutroner kan skilja. Atomer av samma grundämne med olika antal neutroner kallas <strong class='green'>isotoper</strong>. Kol har till exempel tre isotoper som förekommer i naturen: kol-12 med 6 protoner och 6 neutroner, kol-13 med 6 protoner och 7 neutroner och kol-14 med 6 protoner och 8 neutroner. Isotoperna har samma kemiska egenskaper men olika masstal.</p>"
      "<p>Vissa isotoper har en kärna som är <strong class='green'>instabil</strong>. Den sönderfaller efter hand och sänder då ut partiklar eller strålning. Det kallas <strong class='green'>radioaktivitet</strong>. Kol-14 är radioaktivt, medan kol-12 och kol-13 är stabila.</p>",
      [begrepp([("Isotop", "Atomer av samma grundämne med olika antal neutroner."), ("Radioaktivitet", "Att instabila kärnor sönderfaller och sänder ut strålning."), ("Instabil", "Inte stabil: kärnan förändras efter en tid.")])])
 + fig(FIG+"v_isotoper.png", "<b>Bild 3.5</b> Tre isotoper av kol. Alla har 6 protoner men olika antal neutroner. Kol-14 är radioaktivt.", "74%")
 + "<h3>Tre sorters strålning</h3>"
 + roww("<p>Det finns tre vanliga sorters strålning från radioaktiva ämnen. <b>Alfastrålning</b> är heliumkärnor, med två protoner och två neutroner, och stoppas av ett papper eller av huden. <b>Betastrålning</b> består av snabba, mycket lätta partiklar och stoppas av en tunn aluminiumplåt. <b>Gammastrålning</b> är en sorts elektromagnetisk strålning som tränger igenom papper och aluminium och bara stoppas av tjockt bly eller betong.</p>"
        "<p>All sådan strålning är <strong class='green'>joniserande</strong>, vilket betyder att den kan slå loss elektroner från atomer och skada celler. Därför kan strålning både vara nyttig och farlig, beroende på hur man utsätts för den.</p>",
        [fig(FIG+"v_stralning.png", "<b>Bild 3.6</b> Hur olika strålning stoppas (schematiskt): alfa av papper, beta av aluminium och gamma av bly.", "100%")])
 + "<h3>Halveringstid</h3>"
 + "<p>Man kan inte veta när en enskild atom sönderfaller, men för ett stort antal atomer går det att säga hur lång tid det tar. <strong class='green'>Halveringstiden</strong> är den tid det tar för hälften av atomerna i ett prov att sönderfalla. Kol-14 har halveringstiden 5 730 år. Efter en halveringstid finns hälften kvar, efter två halveringstider en fjärdedel, och så vidare. Nedan visas ett påhittat exempel.</p>"
 + table(["Tid", "Antal halveringstider", "Kvar av 80 g (påhittat ämne med halveringstid 10 år)"], [["0 år", "0", "80 g"], ["10 år", "1", "40 g"], ["20 år", "2", "20 g"], ["30 år", "3", "10 g"]], "tbl num")
 + "<h3>Användning och risker</h3>"
 + "<p>Radioaktiva ämnen används på många sätt. Inom sjukvården används gammastrålning vid strålbehandling för att förstöra cancerceller, och radioaktiva ämnen används vid bilddiagnostik (PET). Kol-14 används vid <strong class='green'>åldersbestämning</strong> av gamla föremål: i levande organismer finns det kol-14, och efter döden sönderfaller det, så mängden kol-14 visar hur länge sedan det var. Kärnkraft använder också radioaktiva ämnen. Men strålningen kan skada celler och ge cancer, och olyckor som Tjernobyl och Fukushima har orsakat stora skador. Strålskydd bygger på att korta tiden, öka avståndet och skärma av.</p>"
 + box("tank", "Tänk efter", "<p>Varför kan samma sorts strålning användas både för att behandla cancer och vara ett hot mot hälsan? Vad avgör om den hjälper eller skadar?</p>")
 + kq("3.1.3"))

# ------------------------------------------------------------------ Labb 3.1
add("Labb", "3.1 Svarta lådan", f"Kapitel {NR} · Delområde 3.1 {DELOMR['3.1']} · Labb 3.1 Svarta lådan",
 "<p>Rutherford kunde inte se in i atomen. Han sköt in partiklar och tittade på hur de studsade. I det här försöket gör du något liknande med en dold form i en låda.</p>"
 + fig(FIG+"v_labb1.png", "<b>Bild 3.7</b> Sedd uppifrån: kulan rullas in genom ett hål och kommer ut på olika sätt beroende på vad som finns gömt i lådan.", "26%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Kan man ta reda på formen på något dolt bara genom att se hur kulor rullar förbi?</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror att du kan ta reda på, och hur säker du tror att slutsatsen blir.</p>"
        "<p><strong class='green'>Material:</strong> en låda eller kartong utan lock med gömda former (läraren förbereder: till exempel en kloss eller ett hopvikt kartongstycke fastklistrat i botten, som eleverna inte får se), en stor sten eller bok att täcka med, kulor eller små bollar, ett papper och en penna. Lådan täcks så att formen inte syns.</p><h3>Gör så här</h3>"
        + steps(["Läraren förbereder lådor med olika gömda former och numrerar dem. Du får en låda utan att se vad som finns i.",
                 "Rulla en kula in från olika hål eller sidor. Notera varje gång hur kulan kommer ut: rakt igenom, åt sidan eller tillbaka.",
                 "Gör minst tio försök från olika håll. Rita upp banorna på ett papper.",
                 "Rita en gissning på vilken form som finns i lådan, utifrån banorna.",
                 "Ta bort täckningen och jämför. Stämde din gissning? Vad hade du kunnat göra för att få bättre svar?"]),
        [box("begrepp", "Begrepp", "<b class='t'>Indirekt iakttagelse</b><p>Att dra slutsatser om något du inte ser direkt, utifrån vad du ser.</p><b class='t'>Slutsats</b><p>Ditt svar på frågan, byggt på resultaten.</p>"),
         box("tank", "Bra att veta", "<p>Ju fler försök från olika håll, desto bättre gissning. Rutherford gjorde tusentals mätningar.</p>")])
 + table(["Försök", "Från vilket håll", "Vad hände med kulan?"], [["1", "", ""], ["2", "", ""], ["3", "", ""]], "tbl num")
 + '<p class="note">Säkerhet: Se till att kulorna inte hamnar på golvet så att ingen halkar. Rulla försiktigt så att ingen träffas.</p>'
 + "<h3>Frågor</h3>"
 + steps(["Hur gjorde du din gissning på formen? Vilka banor var viktigast?", "Hur liknar försöket Rutherfords försök? Vad är lika och vad är olika?", "Hur säker är din slutsats? Vad kan du göra för att bli säkrare?"], True))

# ------------------------------------------------------------------ 3.2.1
add("3.2.1", "Grundämnen och periodiska systemet", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Grundämnen och periodiska systemet",
 row("<p>Ett <strong class='green'>grundämne</strong> är ett ämne som bara består av en sorts atomer, alltså atomer med samma atomnummer. Grundämnena har en <strong class='green'>kemisk beteckning</strong> på en eller två bokstäver, till exempel H för väte, C för kol, O för syre, Fe för järn och Na för natrium. Det finns 118 erkända grundämnen.</p>"
     "<p>Alla grundämnen finns ordnade i det <strong class='green'>periodiska systemet</strong>. De står i ordning efter stigande atomnummer. De <b>vågräta raderna</b> kallas <strong class='green'>perioder</strong>. De <b>lodräta kolumnerna</b> kallas <strong class='green'>grupper</strong> och är numrerade 1 till 18. Ämnen i samma grupp har liknande egenskaper, vilket vi tittar på i nästa moment.</p>",
   [begrepp([("Grundämne", "Ämne som består av en sorts atomer."), ("Kemisk beteckning", "En eller två bokstäver för ett grundämne."), ("Period", "Vågrät rad i periodiska systemet."), ("Grupp", "Lodrät kolumn i periodiska systemet.")])])
 + fig(FIG+"v_pse.png", "<b>Bild 3.8</b> Det periodiska systemet. Metaller är blå, icke-metaller är gröna och halvmetaller är gula. Gruppernas nummer står överst och periodernas nummer till vänster.", "100%")
 + "<h3>Metaller, icke-metaller och halvmetaller</h3>"
 + "<p>Grundämnena delas in i tre sorter. Ungefär 80 procent av grundämnena är <strong class='green'>metaller</strong>. De ligger till vänster och i mitten i systemet. <strong class='green'>Icke-metaller</strong> ligger till höger, och mellan dem, vid en trappstegsformad linje, ligger <strong class='green'>halvmetallerna</strong>, som har egenskaper mitt emellan.</p>"
 + table(["", "Metaller", "Icke-metaller", "Halvmetaller"],
         [["<b>Ledning av värme och el</b>", "Bra", "Dålig", "Mitt emellan"], ["<b>Utseende</b>", "Glänsande", "Matta", "Kan glänsa som en metall"],
          ["<b>Att forma</b>", "Går att böja och hamra", "Fasta är spröda", "Spröda"], ["<b>Tillstånd vid rumstemperatur</b>", "Fasta (utom kvicksilver)", "Många är gaser, andra fasta eller vätska", "Fasta"],
          ["<b>Exempel</b>", "Järn, koppar, aluminium", "Syre, svavel, kol", "Kisel"]], "tbl")
 + "<p class='note'>Reglerna har undantag. Till exempel är grafit, en form av kol, en bra elektrisk ledare trots att kol är en icke-metall. Aluminium ligger nära trappstegslinjen men räknas som en metall.</p>"
 + "<h3>Hur systemet växte fram</h3>"
 + "<p>År 1869 ordnade den ryske kemisten Dmitrij Mendelejev de grundämnen som då var kända efter atommassa och egenskaper. Han lämnade luckor där det inte fanns något ämne som passade och förutsade vilka egenskaper de saknade ämnena skulle ha. Senare hittades nya ämnen som passade i luckorna, och då blev systemet allmänt accepterat. Du läser mer om detta i fördjupningen.</p>"
 + box("tank", "Tänk efter", "<p>Titta på bild 3.8. Vilket grundämne är det som står i period 3 och grupp 17? Är det en metall eller en icke-metall?</p>")
 + kq("3.2.1"))

# ------------------------------------------------------------------ 3.2.2
add("3.2.2", "Grupper med släktskap", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Grupper med släktskap",
 roww("<p>Ämnen i samma grupp liknar varandra. Förklaringen finns i elektronerna. Det är <strong class='green'>valenselektronerna</strong>, alltså elektronerna i det yttersta skalet, som avgör hur ett ämne reagerar. För grupp 1 och 2 och för grupp 13 till 18 är antalet valenselektroner lika med gruppens enhetssiffra: 1 för grupp 1, 2 för grupp 2, 3 för grupp 13 och så vidare upp till 8 för grupp 18 (helium har 2). Ämnen i samma grupp har samma antal valenselektroner och reagerar därför på liknande sätt.</p>",
      [begrepp([("Valenselektron", "Elektron i yttersta skalet."), ("Alkalimetall", "Metall i grupp 1."), ("Halogen", "Icke-metall i grupp 17."), ("Ädelgas", "Gas i grupp 18 med fullt yttersta skal.")])])
 + fig(FIG+"v_skal.png", "<b>Bild 3.9</b> Elektronerna i skal för natrium (grupp 1), klor (grupp 17) och neon (grupp 18). Valenselektronerna är i det yttersta skalet.", "50%")
 + "<h3>Alkalimetaller (grupp 1)</h3>"
 + "<p>Litium, natrium och kalium har en valenselektron. De är mjuka metaller med låg densitet, så att de kan flyta på vatten. De reagerar kraftigt med vatten och bildar vätgas och en basisk lösning, och därför förvaras de under olja. Reaktiviteten ökar nedåt i gruppen: kalium reagerar häftigare än litium.</p>"
 + "<h3>Halogener (grupp 17)</h3>"
 + "<p>Fluor, klor, brom och jod har sju valenselektroner och behöver en elektron till för att få fullt skal. De är reaktiva icke-metaller. Klor är en grön gas, brom är en rödbrun vätska och jod är ett lila-svart fast ämne. Här minskar reaktiviteten nedåt i gruppen, tvärtom mot alkalimetallerna.</p>"
 + "<h3>Ädelgaser (grupp 18)</h3>"
 + roww("<p>Helium, neon, argon, krypton och xenon har fullt yttersta skal och är mycket oreaktiva. De förekommer som enskilda atomer i gasform. Helium används i ballonger eftersom det är lätt och inte brinner, neon ger skyltar rödorange sken och argon används som skyddsgas vid svetsning.</p>"
        "<p>Det finns alltså ett samband mellan elektronerna och ämnets egenskaper: ett fullt yttersta skal gör ämnet stabilt, medan ett nästan tomt eller nästan fullt skal gör det reaktivt.</p>",
        [table(["Grupp", "Valens-elektroner", "Egenskap"], [["1 Alkalimetaller", "1", "Mycket reaktiva metaller"], ["17 Halogener", "7", "Reaktiva icke-metaller"], ["18 Ädelgaser", "8 (He: 2)", "Mycket oreaktiva"]], "tbl")])
 + kq("3.2.2"))

# ------------------------------------------------------------------ 3.2.3
add("3.2.3", "Grundämnen i naturen och kroppen", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Grundämnen i naturen och kroppen",
 row("<p>Vilka grundämnen är vanligast? Det beror på var man tittar. I jordskorpan är nästan hälften syre (ungefär 47 viktprocent), och kisel står för ungefär 28 procent. Därefter kommer aluminium (ungefär 8 procent) och järn (ungefär 5 procent). Sand och många bergarter är föreningar av kisel och syre. De åtta vanligaste grundämnena står för nästan hela jordskorpan.</p>"
     "<p>I människokroppen är det annorlunda. Där är syre också störst (ungefär 60 procent av massan, eftersom kroppen består mycket av vatten), därefter kol (ungefär 20 procent), väte (ungefär 10 procent) och kväve (ungefär 3 procent). Kalcium (ungefär 1,5 procent), fosfor och några andra grundämnen finns i mindre mängder men är viktiga, till exempel i skelettet. Siffrorna skiljer något mellan källor, så de ska läsas som ungefärliga.</p>",
   [begrepp([("Viktprocent", "Hur många procent av massan som är ett visst grundämne."), ("Jordskorpan", "Det yttersta, fasta lagret av jorden.")])])
 + fig(FIG+"v_forekomst.png", "<b>Bild 3.10</b> De vanligaste grundämnena i jordskorpan och i människokroppen, i viktprocent. Värdena är avrundade och skiljer något mellan källor.", "80%")

 + "<p class='note'>Värdena för jordskorpan kommer från HyperPhysics och för kroppen från HyperPhysics och LibreTexts. Källorna skiljer något, särskilt för syre i kroppen.</p>"
 + "<h3>Grundämnen i vardagen</h3>"
 + "<p>Många grundämnen använder du varje dag utan att tänka på det. Aluminium finns i folie, järn i stål, koppar i elledningar, kisel i datorchip, helium i ballonger och neon i skyltar. Kol finns i allt som lever. Några grundämnen är så viktiga för kroppen att vi måste få i oss dem med maten, till exempel kalcium för skelettet och järn för blodet.</p>"
 + box("tank", "Tänk efter", "<p>Varför tror du att det är så få grundämnen som utgör nästan hela jordskorpan och nästan hela kroppen, trots att det finns över hundra? Skriv en gissning.</p>")
 + kq("3.2.3"))

# ------------------------------------------------------------------ Labb 3.2
add("Labb", "3.2 Metaller och icke-metaller", f"Kapitel {NR} · Delområde 3.2 {DELOMR['3.2']} · Labb 3.2 Metaller och icke-metaller",
 "<p>Du ska undersöka egenskaper hos ett antal prover av grundämnen och sortera dem som metaller eller icke-metaller. Sedan jämför du med det periodiska systemet.</p>"
 + fig(FIG+"v_labb2.png", "<b>Bild 3.11</b> Koppla ett batteri, en lampa och provet i en krets. Lyser lampan leder provet elektricitet.", "26%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Vilka egenskaper skiljer metaller från icke-metaller?</p><p><strong class='green'>Hypotes:</strong> Skriv vilka prover du tror är metaller och vilka egenskaper du tror att de har.</p>"
        "<p><strong class='green'>Material:</strong> batteri (högst 4,5 V), lampa med hållare, sladdar med krokodilklämmor, prover av grundämnen (till exempel koppartråd, aluminiumfolie, en järnspik, en zinkbit, svavelbitar, träkol, ett blyertsstift) som läraren märkt med nummer, våg, mätcylinder och skyddsglasögon (läraren visar hur man slår lätt med en hammare).</p><h3>Gör så här</h3>"
        + steps(["Titta på varje prov: glänser det? Skriv i tabellen.",
                 "Koppla provet i kretsen med batteri och lampa. Lyser lampan? Skriv ledning ja eller nej.",
                 "Pröva försiktigt om provet går att böja.",
                 "Mät massa och volym för ett par prover och räkna ut densiteten (som i labb 2.1). Jämför.",
                 "Sortera proverna som metall eller icke-metall och kontrollera med det periodiska systemet."]),
        [box("begrepp", "Begrepp", "<b class='t'>Ledningsförmåga</b><p>Hur bra ett ämne leder el eller värme.</p><b class='t'>Böjbar</b><p>Går att böja utan att gå sönder.</p>"),
         box("tank", "Bra att veta", "<p>Skillnaden är inte alltid tydlig: grafit leder el trots att kol är en icke-metall. Notera sådant som verkar avvika.</p>")])
 + table(["Prov", "Glans", "Leder el?", "Böjbar eller spröd?", "Densitet (g/cm³)", "Metall eller icke-metall?"], [["1", "", "", "", "", ""], ["2", "", "", "", "", ""], ["3", "", "", "", "", ""]], "tbl num")
 + '<p class="note">Säkerhet: Använd bara batteri på högst 4,5 V och låt det inte kortslutas. Använd skyddsglasögon när du slår på prover. Smaka eller lukta inte på proverna. Tvätta händerna efteråt.</p>'
 + "<h3>Frågor</h3>"
 + steps(["Vilka prover var metaller? Vilka egenskaper hade de gemensamt?", "Fanns det något prov som inte passade i din sortering? Vad gjorde du då?"], True))

SAMMAN = ["En <strong>atom</strong> är en mycket liten byggsten, ungefär 0,1 nm i radie. Atomer av samma sort bildar ett <strong>grundämne</strong>. Det finns 118 erkända grundämnen.",
          "Atomen har en liten <strong>kärna</strong> med <strong>protoner</strong> (+1) och <strong>neutroner</strong> (0). Utanför finns <strong>elektroner</strong> (−1) i skal. Atomen är neutral eftersom antalet elektroner är lika med antalet protoner.",
          "<strong>Atomnummer</strong> är antalet protoner. <strong>Masstal</strong> är protoner plus neutroner. Neutroner = masstal − atomnummer.",
          "<strong>Atommodellerna</strong> har ändrats: Dalton (kula), Thomson (plumpudding), Rutherford (kärna, 1911) och Bohr (skal, 1913). Nya experiment gav nya modeller, och Bohrs modell har begränsningar.",
          "<strong>Isotoper</strong> är atomer av samma grundämne med olika antal neutroner. Instabila kärnor sönderfaller: <strong>radioaktivitet</strong>.",
          "Det finns <strong>alfa-, beta- och gammastrålning</strong>, som stoppas av papper, aluminium respektive bly. Strålningen är joniserande och kan både användas och skada. <strong>Halveringstid</strong> är tiden då hälften sönderfallit.",
          "Det <strong>periodiska systemet</strong> ordnar grundämnena efter stigande atomnummer i <strong>perioder</strong> (rader) och <strong>grupper</strong> (kolumner). Det finns <strong>metaller</strong>, <strong>icke-metaller</strong> och <strong>halvmetaller</strong>.",
          "<strong>Valenselektroner</strong> är elektronerna i yttersta skalet. Ämnen i samma grupp har lika många och liknar därför varandra.",
          "<strong>Alkalimetaller</strong> (grupp 1) är mycket reaktiva och reaktiviteten ökar nedåt. <strong>Halogener</strong> (grupp 17) är reaktiva icke-metaller, minskar nedåt. <strong>Ädelgaser</strong> (grupp 18) har fullt yttersta skal och är oreaktiva.",
          "I jordskorpan är syre och kisel vanligast. I kroppen är syre, kol, väte och kväve vanligast. Siffrorna är ungefärliga."]

BEGR = [("Alkalimetall", "Metall i grupp 1."), ("Atom", "Mycket liten byggsten av materia."), ("Atomkärna", "Kärnan med protoner och neutroner."), ("Atomnummer", "Antalet protoner."),
        ("Ädelgas", "Gas i grupp 18 med fullt yttersta skal."), ("Elektron", "Negativ partikel i skalen."), ("Elektronskal", "Område där elektronerna rör sig."), ("Gammastrålning", "Genomträngande strålning som stoppas av bly."),
        ("Grundämne", "Ämne av en sorts atomer."), ("Grupp", "Lodrät kolumn i periodiska systemet."), ("Halogen", "Icke-metall i grupp 17."), ("Halveringstid", "Tid då hälften av kärnorna sönderfallit."),
        ("Halvmetall", "Ämne med egenskaper mellan metall och icke-metall."), ("Icke-metall", "Dålig ledare, ofta gas eller sprött fast ämne."), ("Isotop", "Atomer av samma grundämne med olika antal neutroner."),
        ("Masstal", "Protoner plus neutroner."), ("Metall", "Bra ledare, glänsande och formbar."), ("Neutron", "Partikel utan laddning i kärnan."), ("Period", "Vågrät rad i periodiska systemet."),
        ("Periodiska systemet", "Grundämnena ordnade efter atomnummer."), ("Proton", "Positiv partikel i kärnan."), ("Radioaktivitet", "Att instabila kärnor sönderfaller och strålar."), ("Valenselektron", "Elektron i yttersta skalet.")]

TEST = [
 ("A", "Hur många protoner har en atom med atomnummer 11?", ["A 1", "B 11", "C 12", "D 23"], 1, 0),
 ("A", "Vilken partikel har negativ laddning?", ["A Protonen", "B Neutronen", "C Elektronen", "D Atomkärnan"], 2, 0),
 ("A", "En atom har 17 protoner och 18 neutroner. Vilket masstal har den?", ["A 1", "B 17", "C 18", "D 35"], 3, 0),
 ("A", "Vilka grundämnen är mycket oreaktiva eftersom deras yttersta skal är fullt?", ["A Alkalimetallerna", "B Halogenerna", "C Ädelgaserna", "D Metallerna"], 2, 0),
 ("B", "Förklara varför en atom är neutral.", None, 1, 3),
 ("B", "Beskriv vad som hände i Rutherfords försök med guldfolie, och vilken slutsats han drog.", None, 2, 4),
 ("C", "TABELL", None, 2, 5),
 ("C", "Ett påhittat radioaktivt ämne har halveringstiden 4 år. Från början finns 80 g. a) Hur mycket finns kvar efter 12 år? b) Varför blir det aldrig exakt noll på en gång?", None, 2, 5),
 ("D", "Natrium och kalium är båda alkalimetaller och reagerar på liknande sätt med vatten, medan neon inte reagerar alls. Förklara med hjälp av valenselektroner varför. Förklara också varför kalium reagerar häftigare än natrium.", None, 3, 6),
 ("D", "Förklara hur Rutherfords resultat ledde till att man bytte ut Thomsons modell, och beskriv en begränsning hos Bohrs modell. Förklara varför man ändå fortfarande använder skalmodellen.", None, 3, 6),
 ("E", "Astat (At) står i grupp 17, under jod. Det finns mycket lite astat att undersöka. Förutsäg ämnets tillstånd vid rumstemperatur, antalet valenselektroner och hur reaktivt det är jämfört med jod. Motivera med platsen i periodiska systemet och diskutera hur säker din förutsägelse är.", None, 3, 7),
 ("E", "En tidningsrubrik säger: ”Strålning är alltid farligt”. Bedöm påståendet. Använd exempel på både användning och risker, och förklara vad som avgör om strålningen skadar eller hjälper.", None, 3, 7),
]
TEST_TABELL = (["Atom", "Protoner", "Neutroner", "Elektroner"], [["A", "6", "6", "6"], ["B", "6", "8", "6"], ["C", "7", "7", "7"]])
TEST_D_TEXT = "Tre neutrala atomer har undersökts. Värdena är påhittade, men atomerna finns som riktiga isotoper."
TEST_D_SUB = ["a) Räkna ut masstalet för varje atom.", "b) Vilka två atomer är isotoper av samma grundämne? Motivera.", "c) Atomnumret för kväve är 7. Vilken atom är kväve?"]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Tolka resultat och förklara", "D": "Resonera och ta ställning", "E": "Förutsäg och värdera"}
FACIT = [
 "B", "C", "D", "C",
 "Atomen har lika många elektroner som protoner. Elektronerna är negativa (−1) och protonerna positiva (+1), så laddningarna tar ut varandra.",
 "De flesta alfapartiklarna gick rakt igenom folien, men några få avlänkades kraftigt. Rutherford drog slutsatsen att atomens positiva laddning och nästan hela massan finns samlad i en liten kärna, och att atomen mestadels är tom.",
 "a) A: 6 + 6 = 12. B: 6 + 8 = 14. C: 7 + 7 = 14. b) A och B, eftersom de har samma antal protoner (6, alltså kol) men olika antal neutroner. c) C, eftersom den har 7 protoner.",
 "a) 12 år är tre halveringstider: 80 g → 40 g → 20 g → 10 g. Det finns 10 g kvar. b) Efter varje halveringstid halveras mängden, så det finns alltid hälften kvar av det som fanns. Det kommer alltså ner mot noll men blir inte noll av sig självt vid en viss tidpunkt. (I verkligheten sönderfaller enstaka atomer slumpmässigt.)",
 "Alkalimetallerna har en valenselektron, och det är valenselektronerna som avgör hur ämnet reagerar. Natrium och kalium har därför liknande egenskaper. Neon har fullt yttersta skal och behöver varken ta upp eller avge elektroner, så det är oreaktivt. Kalium reagerar häftigare eftersom dess yttersta elektron sitter längre från kärnan och är lättare att avge.",
 "Thomsons modell förutsade att alfapartiklarna skulle gå rakt igenom eller böjas av lite. Eftersom några få avlänkades kraftigt måste den positiva laddningen och massan sitta samlad i en liten kärna, och då behövdes en ny modell. Bohrs modell fungerar bra för väte men inte för atomer med flera elektroner, och ersattes av kvantmekaniken. Skalmodellen används ändå eftersom den är enkel och förklarar mycket, till exempel gruppernas släktskap, så länge man känner till begränsningarna.",
 "Öppet svar. Ett välutvecklat svar: astat står under jod, så det har 7 valenselektroner som alla halogener. Halogenerna går från gas (klor) via vätska (brom) till fast (jod) nedåt i gruppen, så astat är troligen fast. Reaktiviteten minskar nedåt i gruppen, så astat är troligen mindre reaktivt än jod. Förutsägelsen bygger på trender och är osäker eftersom det finns så lite astat att kontrollera, och trender kan ha undantag. Den behöver prövas med mätningar.",
 "Öppet svar. Ett välutvecklat svar: påståendet är för kategoriskt. Strålning används i sjukvården (strålbehandling, bilddiagnostik), vid åldersbestämning och i kärnkraft, men den är joniserande och kan skada celler och ge cancer, och olyckor som Tjernobyl har gett stora skador. Det avgörande är sort, mängd (dos), tid och avskärmning: strålskydd bygger på kort tid, stort avstånd och skärmning. Vissa strålningstyper stoppas lätt (alfa), andra kräver bly (gamma).",
]
LGR = ("Området täcker det centrala innehållet i årskurs 7–9 om atomens byggnad, atommodeller, periodiska systemet och grundämnenas egenskaper. "
       "Delområde 3.1 behandlar atomens partiklar, atomnummer och masstal, hur atommodellerna ändrats genom experiment (Dalton, Thomson, Rutherford, Bohr), isotoper och radioaktivitet med användning och risker. Delområde 3.2 behandlar hur grundämnena är ordnade i periodiska systemet, skillnaden mellan metaller, icke-metaller och halvmetaller, valenselektroner och gruppers släktskap samt grundämnen i naturen och kroppen. "
       "Labbarna tränar att dra slutsatser om något dolt (indirekt iakttagelse) och att undersöka och sortera grundämnens egenskaper. Uppgifterna följer betygskriteriernas progression från att beskriva till att förklara och värdera, och är inspirerade av frisläppta nationella prov i kemi. "
       "Anslutning till andra ämnen: strålning och kärnreaktioner behandlas också i fysik, och grundämnen i kroppen i biologi. I kemi ligger fokus på atomens byggnad och periodiska systemet.")
FAKTA = ("Kontrollerat mot öppna källor (2026-10-22): protonens, neutronens och elektronens laddning och massa, atomens och kärnans storlek (radie ca 0,1 nm respektive ca 1 · 10⁻¹⁴ m), definition av atomnummer och masstal och neutronantal = masstal − atomnummer (StudyMind, Cognito); Rutherfords experiment (1909) och slutsats 1911, Thomsons plumpuddingmodell, Bohrs modell 1913 med bestämda banor och energi, och dess begränsning (Wikipedia); kolisotoper kol-12, 13 och 14 samt kol-14:s halveringstid 5 730 år och användning vid åldersbestämning (UCLA, Alloprof); definition av radioaktivitet och halveringstid samt alfa-, beta- och gammastrålningens genomträngningsförmåga och användningar (Alloprof); periodiska systemets ordning, grupper och perioder, Mendelejev 1869 med luckor (Seneca); 118 grundämnen varav ca 90 naturliga (LibreTexts); metallers, icke-metallers och halvmetallers egenskaper (LibreTexts); alkalimetallernas, halogenernas och ädelgasernas egenskaper och reaktivitetstrender samt ädelgasernas användning (Cognito, RevisionDojo); förekomst i jordskorpan (HyperPhysics: O 46,6, Si 27,7, Al 8,1, Fe 5,0 %) och i kroppen (HyperPhysics och LibreTexts, siffrorna skiljer). "
         "Ej källkontrollerat: att skalen rymmer 2, 8 och 8 elektroner och att antalet valenselektroner är lika med gruppens enhetssiffra (förenklad skolmodell), årtalet för upptäckten av elektronen (slutet av 1800-talet) och Daltons modell 1808, jämförelsen med arenan och knappnålshuvudet, strålskyddets principer (tid, avstånd, skärmning), att kalcium behövs för skelettet och järn för blodet, kemiska beteckningars bokstäver, att grafit leder el, att fosforns, kolets, syrets, natriums och järns vanligaste isotoper har just de masstal som anges, och tjernobyl/Fukushima. Alla exempelmätvärden är påhittade. "
         "Källor: Skolverket, Lgr22 kursplan i kemi. · StudyMind, Cognito, Wikipedia, UCLA, Alloprof, Seneca, LibreTexts, HyperPhysics, RevisionDojo. · Illustrationer: egenritade för detta kapitel.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start.</b> Mål: eleven vet att allt består av atomer, att det finns 118 grundämnen och att atomer är mycket små. Låt eleverna skriva sin gissning om guldbiten (Fundera) och spara den. Vanligt fel: att atomen är hård och kompakt. Visa att nästan hela atomen är tom, och betona att arenajämförelsen är en bild.</p>
<p><b>Atomen och dess partiklar.</b> C-mål: bestämma antalet protoner, neutroner och elektroner utifrån atomnummer och masstal. Vanliga fel: att neutroner är laddade, att masstalet är antalet elektroner, att atomnumret är atommassan och att atomen är laddad. Låt eleverna räkna ett par exempel i par innan de gör kontrollfrågorna.</p>
<p><b>Atommodellernas historia.</b> C/A-mål: koppla experiment till nya modeller och värdera modellers begränsningar. Vanligt fel: att äldre modeller var ”dumma”: de var rimliga utifrån vad man då kunde mäta. Bra kontrast: Thomsons modell förutspår att alfapartiklar går igenom, och försöket visar något annat. Förbered Labb 3.1 som en direkt analogi.</p>
<p><b>Isotoper och radioaktivitet.</b> C-mål: förklara isotoper, halveringstid och ge exempel på användning och risker. Vanliga fel: att radioaktivt betyder ”smittsamt”, att halveringstid är hälften av hela livslängden och att all strålning är lika farlig. Rita en tabell som halverar och låt eleverna fylla i. Kapitlet ger bara en kort introduktion, och kärnreaktioner tas upp i fördjupningen.</p>
<p><b>Labb 3.1 Svarta lådan.</b> Material: kartonglådor med gömda former, kulor. Förväntat: kulan går rakt igenom där inget finns i vägen och avlänkas där formen sitter. Vanliga fel: för få försök, bara från ett håll, och att man gissar innan man testat. Låt några grupper byta låda och kontrollera varandras slutsatser.</p>
<p><b>Grundämnen och periodiska systemet.</b> C-mål: hitta grundämnen, perioder, grupper och sortera som metall, icke-metall eller halvmetall. Vanliga fel: att alla metaller är fasta (kvicksilver), att aluminium är en halvmetall och att periodiska systemet är ordnat efter massa. Använd gärna ett stort periodiskt system på väggen.</p>
<p><b>Grupper med släktskap.</b> C-mål: koppla gruppers egenskaper till valenselektroner. Vanligt fel: att alla ämnen i en grupp är identiska. Alkalimetallernas reaktion med vatten görs bara som lärardemonstration med mycket små bitar, skyddsglasögon och skyddsskärm, eller visas som film. Låt eleverna rita elektronskal för grundämnen 1–18.</p>
<p><b>Grundämnen i naturen och kroppen.</b> C-mål: ge exempel på vanliga grundämnen. Siffrorna för kroppen varierar mellan källor, så betona att de är ungefärliga. Vanligt fel: att det som finns mest i kroppen är samma som finns mest i jordskorpan.</p>
<p><b>Labb 3.2 Metaller och icke-metaller.</b> Material: batteri (högst 4,5 V), lampa, prover. Förväntat: koppar, aluminium, järn och zink leder el och glänser, svavel leder inte, träkol leder dåligt och grafit (blyertsstift) leder. Vanliga fel: att kortsluta batteriet och att dra slutsatser om en egenskap utan att jämföra flera. Låt eleverna diskutera avvikelser.</p>
"""
LAB_HTML = ""

BONUS = dict(
 titel="Grundämneskort: sortera och förutsäg",
 ingress="Eleverna får kort med information om grundämnen och sorterar dem efter egenskaper. De förutsäger sedan egenskaper för ett ämne utifrån platsen i periodiska systemet. Kräver inga kemikalier.",
 syfte="Eleverna tränar att använda periodiska systemet, koppla grupp till egenskaper och göra och värdera förutsägelser.",
 tid="Grupper om tre till fyra.",
 material=["Kort med grundämnen (läraren gör själv: namn, beteckning, atomnummer, tillstånd, om ämnet leder el)", "Ett stort periodiskt system", "Papper och penna", "Sax"],
 genomf=["Dela ut tolv kort, till exempel natrium, kalium, klor, brom, neon, argon, järn, koppar, kol, svavel, kisel och aluminium, utan att visa gruppen.", "Låt gruppen sortera korten i högar efter egenskaper de själva väljer, och skriva ner sin princip.", "Låt dem sedan placera korten i ett tomt periodiskt system eller slå upp atomnumret.", "Jämför sorteringen med grupperna: stämmer deras egenskapsgrupper med kolumnerna?", "Ge dem ett nytt kort, till exempel astat, utan egenskaper. Låt dem förutsäga tillstånd och reaktivitet utifrån platsen och motivera.", "Diskutera hur säkra förutsägelserna är."],
 resultat="Elever som sorterar efter egenskaper hittar ofta metaller och icke-metaller, och kan se att ämnen i samma kolumn liknar varandra. Förutsägelsen för astat blir ofta ”fast och mindre reaktivt än jod”, vilket följer trenderna men ändå är osäkert.",
 sakerhet=["Inga särskilda risker."],
 problem=["Korten är för detaljerade: begränsa till tre till fyra egenskaper per kort.", "Elever blandar ihop period och grupp: låt dem använda en färgad kolumn."],
 bedom=[("Grundläggande", "Sorterar korten och placerar några rätt i systemet."), ("Utvecklat", "Kopplar grupper till egenskaper och förutsäger ett ämnes egenskaper utifrån platsen."), ("Välutvecklat", "Motiverar förutsägelsen med valenselektroner och värderar hur säker den är.")],
 forslag=["Vilka grupper är lättast att förutsäga, och vilka svårast?", "Gör kort för ämnen som du inte vet något om och låt en annan grupp förutsäga.", "Vilka undantag finner ni?"],
)
ELEV_HTML = ('<section class="sec"><div class="pill">Elevblad · Kopieringsunderlag</div><p class="note">Namn: ____________________ &nbsp; Klass: ________</p>'
 '<div class="sh small"><h2>Grundämneskort</h2></div>'
 '<p><b>Frågeställning:</b> Kan man förutsäga ett grundämnes egenskaper utifrån dess plats i periodiska systemet?</p>'
 '<h3>Min sortering</h3><p>Vilken princip sorterade du efter?</p>' + lines(2) +
 '<h3>Min förutsägelse</h3><p>Ämne: ____________ &nbsp; Plats (period och grupp): ____________</p><p>Tillstånd vid rumstemperatur: ____________ &nbsp; Reaktivitet: ____________</p><p>Jag motiverar med att …</p>' + lines(3) +
 '<h3>Frågor</h3><ol class="steps g"><li>Stämde dina förutsägelser med kolumnerna i periodiska systemet?</li></ol>' + lines(2) +
 '<ol class="steps g"><li>Hur säker är din förutsägelse? Vad skulle du behöva mäta för att veta?</li></ol>' + lines(3) + '</section>')
RUTOR = []
