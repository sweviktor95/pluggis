# -*- coding: utf-8 -*-
"""Kemi område 3 Atomer och grundämnen – lättläst version (byggd per moment)."""
FIG = '/tmp/kem/fig03k/'
NR = 3
SLUG = "kemi-atomer"
TAB = "3"
NAMN = "Atomer och grundämnen"
NDEL = 9
UNDER = "Byggstenarna i allt"
INTRO_L = ["I det här kapitlet lär du dig vad en atom är gjord av.",
           "Du lär dig hur forskare kom fram till hur atomen ser ut. Du lär dig också hur grundämnena är ordnade i det periodiska systemet.",
           "Namn och siffror i exemplen är påhittade, om inget annat står."]
SA_GOR = ["Läs de viktiga orden på nästa sida.", "Läs ett moment i taget. Titta noga på bilderna.", "Gör övningarna direkt efter varje moment.", "Läs Kom ihåg-rutan igen. Det är det viktigaste."]
LARA = ["Start: vad en atom är",
        "Delområde 3.1 Atomens byggnad: partiklar, atommodeller, isotoper och radioaktivitet",
        "Delområde 3.2 Periodiska systemet: grundämnen, metaller och icke-metaller, grupper och förekomst"]
ORD_FIG = None
ORD_EXTRA = [("atom", "en mycket liten byggsten som allt är gjort av"), ("grundämne", "ett ämne med bara en sorts atomer"), ("atomkärna", "kärnan i mitten av atomen"),
             ("proton", "en positiv partikel i kärnan"), ("neutron", "en partikel utan laddning i kärnan"), ("elektron", "en negativ partikel utanför kärnan"),
             ("atomnummer", "antalet protoner"), ("masstal", "protoner plus neutroner"), ("isotop", "atomer av samma grundämne med olika antal neutroner"),
             ("radioaktivitet", "en instabil kärna som sönderfaller och strålar"), ("halveringstid", "tiden då hälften har sönderfallit"), ("periodiska systemet", "alla grundämnen i en tabell"),
             ("metall", "glänsar, leder el och går att forma"), ("icke-metall", "leder dåligt, ofta en gas"), ("halvmetall", "något mitt emellan metall och icke-metall"),
             ("valenselektron", "en elektron i det yttersta skalet"), ("alkalimetall", "metall i grupp 1"), ("ädelgas", "gas i grupp 18 som nästan inte reagerar")]

TB_PART = ('<table class="tb"><tr><th>Partikel</th><th>Laddning</th><th>Var?</th></tr>'
           '<tr><td>Proton</td><td>+1</td><td>kärnan</td></tr><tr><td>Neutron</td><td>0</td><td>kärnan</td></tr><tr><td>Elektron</td><td>−1</td><td>skalen</td></tr></table>')
TB_EX = ('<table class="tb"><tr><th>Ämne</th><th>Atomnummer</th><th>Masstal</th><th>Neutroner</th></tr>'
         '<tr><td>Kol</td><td>6</td><td>12</td><td>6</td></tr><tr><td>Syre</td><td>8</td><td>16</td><td>8</td></tr><tr><td>Natrium</td><td>11</td><td>23</td><td>12</td></tr></table>')
TB_HALV = ('<table class="tb"><tr><th>Tid</th><th>Kvar av 80 g</th></tr>'
           '<tr><td>0 år</td><td>80 g</td></tr><tr><td>10 år</td><td>40 g</td></tr><tr><td>20 år</td><td>20 g</td></tr></table>')
TB_METALL = ('<table class="tb"><tr><th></th><th>Metall</th><th>Icke-metall</th></tr>'
             '<tr><td>Leder el och värme</td><td>bra</td><td>dåligt</td></tr><tr><td>Utseende</td><td>glänsar</td><td>matt</td></tr><tr><td>Går att böja</td><td>ja</td><td>nej, fast är sprött</td></tr></table>')
TB_GRUPP = ('<table class="tb"><tr><th>Grupp</th><th>Namn</th><th>Valenselektroner</th></tr>'
            '<tr><td>1</td><td>alkalimetaller</td><td>1</td></tr><tr><td>17</td><td>halogener</td><td>7</td></tr><tr><td>18</td><td>ädelgaser</td><td>8 (helium 2)</td></tr></table>')
TB_LABB1 = ('<table class="tb"><tr><th>Försök</th><th>Från vilket håll?</th><th>Vad hände med kulan?</th></tr>'
            '<tr><td>1</td><td></td><td></td></tr><tr><td>2</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td></tr></table>')
TB_LABB2 = ('<table class="tb"><tr><th>Prov</th><th>Glänser?</th><th>Leder el?</th><th>Metall?</th></tr>'
            '<tr><td>1</td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td></tr></table>')

DELOMR = {"3.1": "Atomens byggnad", "3.2": "Periodiska systemet"}
DELAR = [
 dict(titel="Vad är en atom?", prog="Start · Vad är en atom?",
  fore=["Allt är gjort av <strong>atomer</strong>. En atom är så liten att du inte kan se den.", "Atomer av samma sort bildar ett <strong>grundämne</strong>. Det finns 118 grundämnen. Exempel är syre, järn och guld."],
  fig="v_oversikt.png", figw="95%",
  efter=["En atom har en liten <strong>kärna</strong> i mitten. Utanför kärnan finns <strong>elektroner</strong>.", "Kärnan är mycket mindre än atomen. Nästan hela atomen är tom."],
  kom="Allt består av atomer. Atomer av samma sort är ett grundämne.",
  ova=[("ringa", "Vad är en atom?", ["En mycket liten byggsten", "En sorts vätska", "Ett verktyg"]),
       ("sf", "Kryssa i rätt ruta.", ["Allt består av atomer.", "Det finns 118 grundämnen.", "Man ser atomer med blotta ögat."]),
       ("fyll", ["kärna", "elektroner", "grundämne"], ["Atomer av samma sort är ett ______________.", "I mitten av atomen finns en ______________.", "Utanför kärnan finns ______________."]),
       ("skriv", "Nämn ett grundämne du känner till.", "Ett grundämne är", 1)]),

 dict(titel="Atomen och dess partiklar", prog="Delområde 3.1 · Atomen och dess partiklar",
  fore=["Atomen har tre sorters partiklar.", TB_PART, "Protoner och neutroner finns i kärnan. Elektroner finns i skal runt kärnan.", "En atom har lika många elektroner som protoner. Därför är atomen neutral."],
  fig="v_atom.png", figw="66%",
  efter=["<strong>Atomnumret</strong> är antalet protoner. Det avgör vilket grundämne det är.", "<strong>Masstalet</strong> är protoner plus neutroner.", "<strong>neutroner = masstal − atomnummer</strong>", TB_EX,
         "Exempel: fosfor har atomnummer 15 och masstal 31. Protoner: 15. Neutroner: 31 − 15 = 16. Elektroner: 15."],
  kom="Atomnummer = protoner. Masstal = protoner + neutroner.",
  ova=[("ringa", "Vilken partikel har negativ laddning?", ["Elektronen", "Protonen", "Neutronen"]),
       ("sf", "Kryssa i rätt ruta.", ["Protonen finns i kärnan.", "Neutronen har laddningen +1.", "En atom har lika många elektroner som protoner."]),
       ("fyll", ["protoner", "neutroner", "masstal"], ["Atomnumret är antalet ______________.", "Protoner plus neutroner är ______________.", "Masstal minus atomnummer ger antalet ______________."]),
       ("skriv", "En atom har atomnummer 11 och masstal 23. Hur många neutroner har den?", "Den har", 2)]),

 dict(titel="Atommodellernas historia", prog="Delområde 3.1 · Atommodellernas historia",
  fore=["Ingen kan se en atom. Forskare gör experiment och bygger <strong>modeller</strong>.", "När ett nytt experiment inte passar modellen byter man modell."],
  fig="v_modeller.png", figw="100%",
  efter=["<strong>Dalton</strong> (1808): atomen är en liten kula.", "<strong>Thomson</strong>: positiv laddning med elektroner i, som russin i en kaka.", "<strong>Rutherford</strong> (1911): de flesta alfapartiklar gick igenom guldfolie, några få böjde av. Då visste han att atomen har en liten tung kärna.",
         "<strong>Bohr</strong> (1913): elektronerna går i skal med bestämd energi. Modellen fungerar bra för väte men inte för alla atomer.", "Vi använder skalmodellen i skolan eftersom den är enkel."],
  fig2="v_rutherford.png", fig2w="80%", n1=2,
  kom="Nya experiment ger nya modeller. Rutherford: atomen har en liten kärna.",
  ova=[("ringa", "Vad visade Rutherfords försök?", ["Atomen har en liten tung kärna", "Atomen är en hård kula", "Elektroner finns inte"]),
       ("streck", "Dra streck till rätt forskare.", ["Dalton", "Rutherford", "Bohr"], ["elektroner i skal", "atomen är en kula", "liten tung kärna"]),
       ("sf", "Kryssa i rätt ruta.", ["De flesta alfapartiklarna gick igenom folien.", "Bohrs modell fungerar för alla atomer.", "Man byter modell när experiment inte passar."]),
       ("skriv", "Varför byter forskare modell?", "De byter modell när", 2)]),

 dict(titel="Isotoper och radioaktivitet", prog="Delområde 3.1 · Isotoper och radioaktivitet",
  fore=["<strong>Isotoper</strong> är atomer av samma grundämne med olika antal neutroner.", "Kol-12 har 6 neutroner. Kol-14 har 8 neutroner. Alla har 6 protoner."],
  fig="v_isotoper.png", figw="88%",
  efter=["En <strong>instabil</strong> kärna sönderfaller och sänder ut strålning. Det kallas <strong>radioaktivitet</strong>. Kol-14 är radioaktivt.", "Strålningen kan skada celler. Den används också, till exempel vid strålbehandling och för att bestämma hur gammalt något är.",
         "<strong>Halveringstid</strong> är tiden då hälften har sönderfallit. Exempel med påhittat ämne, halveringstid 10 år:", TB_HALV],
  fig2="v_stralning.png", fig2w="66%", n1=3,
  kom="Isotoper: samma antal protoner, olika antal neutroner. Halveringstid: tiden då hälften är kvar.",
  ova=[("ringa", "Vad är isotoper?", ["Samma grundämne med olika antal neutroner", "Olika grundämnen med lika många protoner", "Atomer utan kärna"]),
       ("sf", "Kryssa i rätt ruta.", ["Radioaktiv strålning kan skada celler.", "Alla isotoper är radioaktiva.", "Efter en halveringstid är hälften kvar."]),
       ("fyll", ["20", "instabil", "neutroner"], ["Isotoper har olika antal ______________.", "En radioaktiv kärna är ______________.", "Av 80 g med halveringstid 10 år finns ______________ g kvar efter 20 år."]),
       ("skriv", "Nämn en användning av radioaktiv strålning.", "En användning är", 2)]),

 dict(titel="Labb 3.1 Svarta lådan", prog="Delområde 3.1 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Kan man se vilken form som finns dold i en låda genom att rulla kulor?", "Du behöver: en låda med en dold form, kulor, papper och penna."],
  fig="v_labb1.png", figw="70%",
  efter=["<ol class='st'><li>Du får en låda. Du får inte titta i den.</li><li>Rulla kulan från olika håll.</li><li>Skriv hur kulan kommer ut.</li><li>Rita en gissning på formen.</li><li>Titta efter. Stämde det?</li></ol>", TB_LABB1,
         "<strong>Säkerhet:</strong> Rulla försiktigt. Plocka upp kulor från golvet."],
  kom="Man kan dra slutsatser om något man inte ser, genom att se hur saker studsar.",
  ova=[("fyll", ["kulan", "formen", "olika"], ["Jag rullade ______________.", "Jag gissade ______________.", "Jag rullade från ______________ håll."]),
       ("skriv", "Stämde din gissning?", "Min gissning", 2),
       ("skriv", "Hur liknar försöket Rutherfords försök?", "Det liknar för att", 2)]),

 dict(titel="Grundämnen och periodiska systemet", prog="Delområde 3.2 · Grundämnen och periodiska systemet",
  fore=["I det <strong>periodiska systemet</strong> står alla grundämnen. De är ordnade efter atomnummer.", "Raderna kallas <strong>perioder</strong>. Kolumnerna kallas <strong>grupper</strong>."],
  fig="v_pse.png", figw="100%",
  efter=["De flesta grundämnen är <strong>metaller</strong>. <strong>Icke-metaller</strong> finns till höger. <strong>Halvmetaller</strong> ligger mellan.", TB_METALL,
         "Kvicksilver är en metall som är flytande. Det finns undantag.", "År 1869 gjorde Mendelejev ett system med luckor. Han förutsade ämnen som ännu inte hittats."],
  kom="Systemet är ordnat efter atomnummer. Rader: perioder. Kolumner: grupper.",
  ova=[("ringa", "Hur är grundämnena ordnade?", ["Efter atomnummer", "Efter bokstav", "Efter färg"]),
       ("sf", "Kryssa i rätt ruta.", ["Metaller leder el.", "Kolumnerna kallas perioder.", "Kisel är en halvmetall."]),
       ("streck", "Dra streck till rätt beskrivning.", ["Metall", "Icke-metall", "Halvmetall"], ["något mitt emellan", "glänser och leder el", "leder dåligt"]),
       ("fyll", ["grupper", "perioder", "atomnummer"], ["Raderna kallas ______________.", "Kolumnerna kallas ______________.", "Grundämnena står i ordning efter ______________."])]),

 dict(titel="Grupper med släktskap", prog="Delområde 3.2 · Grupper med släktskap",
  fore=["<strong>Valenselektroner</strong> är elektronerna i det yttersta skalet. De avgör hur ämnet reagerar.", "Ämnen i samma grupp har lika många valenselektroner. Därför liknar de varandra."],
  fig="v_skal.png", figw="100%",
  efter=[TB_GRUPP, "<strong>Alkalimetaller</strong> (grupp 1) är mjuka och reagerar kraftigt med vatten. De förvaras under olja.", "<strong>Halogener</strong> (grupp 17) är reaktiva icke-metaller. Klor är en grön gas.",
         "<strong>Ädelgaser</strong> (grupp 18) har fullt yttersta skal. De reagerar nästan inte. Helium används i ballonger."],
  kom="Samma grupp: lika många valenselektroner, liknande egenskaper. Ädelgaser har fullt skal.",
  ova=[("ringa", "Vad är valenselektroner?", ["Elektroner i yttersta skalet", "Elektroner i kärnan", "Neutroner"]),
       ("sf", "Kryssa i rätt ruta.", ["Ädelgaser reagerar nästan inte.", "Alkalimetaller har sju valenselektroner.", "Helium används i ballonger."]),
       ("streck", "Dra streck till rätt grupp.", ["Alkalimetaller", "Halogener", "Ädelgaser"], ["grupp 18", "grupp 1", "grupp 17"]),
       ("skriv", "Natrium har elektronerna 2, 8, 1. Hur många valenselektroner har det? I vilken grupp står det?", "Natrium har", 2)]),

 dict(titel="Grundämnen i naturen och kroppen", prog="Delområde 3.2 · Grundämnen i naturen och kroppen",
  fore=["I jordskorpan är <strong>syre</strong> vanligast, ungefär 47 procent. Sedan kommer kisel, ungefär 28 procent.", "I kroppen är syre, kol, väte och kväve vanligast. Siffrorna är ungefärliga och skiljer mellan källor."],
  fig="v_forekomst.png", figw="100%",
  efter=["Vi använder grundämnen varje dag. Aluminium finns i folie, järn i stål, koppar i ledningar, kisel i datorchip och helium i ballonger.", "Kalcium behövs för skelettet och järn för blodet."],
  kom="Jordskorpan: mest syre och kisel. Kroppen: mest syre, kol, väte och kväve.",
  ova=[("ringa", "Vilket grundämne är vanligast i jordskorpan?", ["Syre", "Guld", "Helium"]),
       ("sf", "Kryssa i rätt ruta.", ["Kisel är vanligt i jordskorpan.", "Kroppen innehåller inget kol.", "Siffrorna för kroppen är ungefärliga."]),
       ("fyll", ["syre", "kol", "aluminium"], ["Folie är gjord av ______________.", "Det vanligaste ämnet i jordskorpan är ______________.", "Allt som lever innehåller ______________."]),
       ("skriv", "Nämn ett grundämne i din vardag och vad det används till.", "Ett exempel är", 2)]),

 dict(titel="Labb 3.2 Metaller och icke-metaller", prog="Delområde 3.2 · Labb", lab=True,
  fore=["<strong>Fråga:</strong> Vilka egenskaper skiljer metaller från icke-metaller?", "Du behöver: batteri (högst 4,5 V), lampa, sladdar, prover, skyddsglasögon."],
  fig="v_labb2.png", figw="75%",
  efter=["<ol class='st'><li>Titta på provet. Glänser det?</li><li>Koppla in provet i kretsen. Lyser lampan?</li><li>Känns provet sprött eller går det att böja?</li><li>Sortera: metall eller icke-metall.</li></ol>", TB_LABB2,
         "<strong>Säkerhet:</strong> Använd bara batteriet. Kortslut det inte. Ha skyddsglasögon. Smaka inte på proverna. Tvätta händerna."],
  kom="Metaller glänser och leder el. Icke-metaller gör oftast inte det.",
  ova=[("fyll", ["glänste", "lampan", "metall"], ["Jag kopplade in provet och ______________ lyste.", "Provet ______________.", "Det var en ______________."]),
       ("skriv", "Hittade du något som inte passade? Skriv vad.", "Jag hittade", 2),
       ("skriv", "Hur vet man att något är en metall?", "Man kan se det på att", 2)]),
]

VIKTIGAST = [("l_ic1.png", "Allt består av atomer. Atomer av samma sort är ett grundämne."),
             ("l_ic2.png", "Protoner (+) och neutroner (0) i kärnan. Elektroner (−) i skal."),
             ("l_ic3.png", "Atomnummer = protoner. Masstal = protoner + neutroner."),
             ("l_ic4.png", "Nya experiment gav nya atommodeller: Dalton, Thomson, Rutherford och Bohr."),
             ("l_ic5.png", "Isotoper har olika antal neutroner. Instabila kärnor strålar."),
             ("l_ic6.png", "Periodiska systemet: perioder är rader, grupper är kolumner."),
             ("l_ic7.png", "Samma grupp: lika många valenselektroner och liknande egenskaper.")]
TEST = [("ringa", "Vilken partikel finns i kärnan och har laddningen 0?", ["Neutronen", "Elektronen", "Protonen"]),
        ("streck", "Dra streck till rätt förklaring.", ["Atomnummer", "Masstal", "Isotop", "Halveringstid"], ["tiden då hälften sönderfallit", "antalet protoner", "samma ämne, olika neutroner", "protoner plus neutroner"]),
        ("sf", "Kryssa i rätt ruta.", ["Atomen är neutral.", "Rutherford hittade atomkärnan.", "Metaller leder dåligt.", "Ädelgaser reagerar nästan inte.", "Kolumnerna kallas perioder.", "Syre är vanligast i jordskorpan."]),
        ("fyll", ["protoner", "valenselektroner", "metaller"], ["Atomnumret är antalet ______________.", "Elektroner i yttersta skalet kallas ______________.", "De flesta grundämnen är ______________."]),
        ("siffror", "Sätt i ordning efter år. Skriv 1, 2, 3 och 4.", ["Rutherford", "Bohr", "Dalton", "Thomson"]),
        ("skriv", "En atom har atomnummer 8 och masstal 16. Hur många neutroner har den?", "Den har", 2),
        ("skriv", "Varför liknar ämnen i samma grupp varandra?", "De har", 2),
        ("skriv", "Ge ett exempel på användning och en risk med radioaktiv strålning.", "Användning:", 3)]
TILL_LARAREN = ("Den här versionen täcker allt som krävs för E i område 3 (Atomer och grundämnen): atomens partiklar, atomnummer och masstal, atommodellernas utveckling genom experiment, isotoper och radioaktivitet i korthet, periodiska systemets uppbyggnad, metaller och icke-metaller, grupper och valenselektroner samt grundämnen i naturen och kroppen. "
                "Den är utgångspunkten för grundtexten och fördjupningen: samma moment, samma ordning, men med mer innehåll på högre nivå.")
TILL_TIPS = "Tips: läs gärna texten högt tillsammans, eller låt eleven lyssna med talsyntes. Övningarna kan också göras muntligt. Nationella provet ligger inte till grund för nivåerna."
TILL_PUNKTER = ["Korta meningar, oftast en tanke per rad, och bildstöd i varje moment.", "9 delar (start, sex moment och två labbar) med förloppsindikator. Delområdena syns överst på varje sida.",
                "Samma två delområden som grundtexten.", "Övningar med flera format: ringa in, dra streck, kryssa, fyll i, skriva och sätta i ordning.", "Kom ihåg-ruta i varje moment och en samlad Viktigast-sida."]
HANDLEDNING_HTML = """
<h3>Handledning per moment (lättläst)</h3>
<h3 class="mm">Vad är en atom?</h3><p class="hl"><b>E-mål:</b> eleven vet att allt består av atomer och att atomer av samma sort är ett grundämne. <b>Vanligt fel:</b> att atomen är hård och fylld.</p>
<h3 class="mm">Atomen och dess partiklar</h3><p class="hl"><b>E-mål:</b> eleven namnger partiklarna, anger laddning och plats och räknar neutroner med masstal − atomnummer. <b>Vanliga fel:</b> att neutroner är laddade, att atomnumret är antalet elektroner i en jon (behandlas inte här).</p>
<h3 class="mm">Atommodellernas historia</h3><p class="hl"><b>E-mål:</b> eleven kopplar Rutherfords försök till kärnan. <b>Vanligt fel:</b> att äldre modeller var dumma.</p>
<h3 class="mm">Isotoper och radioaktivitet</h3><p class="hl"><b>E-mål:</b> eleven förklarar isotoper och halveringstid med tabell. <b>Vanligt fel:</b> att radioaktiv betyder smittsam.</p>
<h3 class="mm">Labb 3.1 Svarta lådan</h3><p class="hl"><b>Material:</b> kartonglådor med gömda former, kulor. <b>Förväntat:</b> kulan avlänkas där formen sitter. Låt eleverna rulla från minst tre håll.</p>
<h3 class="mm">Grundämnen och periodiska systemet</h3><p class="hl"><b>E-mål:</b> eleven hittar grundämnen och skiljer metall från icke-metall. <b>Vanligt fel:</b> att alla metaller är fasta (kvicksilver).</p>
<h3 class="mm">Grupper med släktskap</h3><p class="hl"><b>E-mål:</b> eleven kopplar grupp till valenselektroner. Alkalimetallers reaktion med vatten visas bara som lärardemo eller film.</p>
<h3 class="mm">Grundämnen i naturen och kroppen</h3><p class="hl"><b>E-mål:</b> eleven ger exempel på vanliga grundämnen. Betona att siffrorna för kroppen är ungefärliga.</p>
<h3 class="mm">Labb 3.2 Metaller och icke-metaller</h3><p class="hl"><b>Material:</b> batteri högst 4,5 V, lampa, prover (koppar, aluminium, järn, svavel, träkol, blyertsstift). <b>Förväntat:</b> metaller leder el, svavel gör det inte, grafit leder.</p>
"""
FACIT = [
 "<b>Start:</b> 1) En mycket liten byggsten. 2) Sant, sant, falskt. 3) grundämne, kärna, elektroner. 4) T.ex. syre, järn eller guld.",
 "<b>Atomen och dess partiklar:</b> 1) Elektronen. 2) Sant, falskt, sant. 3) protoner, masstal, neutroner. 4) 23 − 11 = 12 neutroner.",
 "<b>Atommodellernas historia:</b> 1) Atomen har en liten tung kärna. 2) Dalton – atomen är en kula; Rutherford – liten tung kärna; Bohr – elektroner i skal. 3) Sant, falskt, sant. 4) T.ex. när ett experiment ger resultat som modellen inte kan förklara.",
 "<b>Isotoper och radioaktivitet:</b> 1) Samma grundämne med olika antal neutroner. 2) Sant, falskt, sant. 3) neutroner, instabil, 20. 4) T.ex. strålbehandling eller åldersbestämning med kol-14.",
 "<b>Labb 3.1:</b> 1) Egna svar. 2) Egen gissning. 3) Man drar slutsatser om något dolt genom att se hur partiklar eller kulor rör sig.",
 "<b>Grundämnen och periodiska systemet:</b> 1) Efter atomnummer. 2) Sant, falskt, sant. 3) Metall – glänser och leder el; Icke-metall – leder dåligt; Halvmetall – något mitt emellan. 4) perioder, grupper, atomnummer.",
 "<b>Grupper med släktskap:</b> 1) Elektroner i yttersta skalet. 2) Sant, falskt, sant. 3) Alkalimetaller – grupp 1; Halogener – grupp 17; Ädelgaser – grupp 18. 4) 1 valenselektron, grupp 1.",
 "<b>Grundämnen i naturen och kroppen:</b> 1) Syre. 2) Sant, falskt, sant. 3) aluminium, syre, kol. 4) T.ex. aluminium i folie.",
 "<b>Labb 3.2:</b> 1) Egna svar. 2) Egna svar, t.ex. grafit som leder trots att kol är en icke-metall. 3) Glänser, leder el och går att forma.",
 "<b>Testa dig:</b> 1) Neutronen. 2) Atomnummer – antalet protoner; Masstal – protoner plus neutroner; Isotop – samma ämne, olika neutroner; Halveringstid – tiden då hälften sönderfallit. 3) Sant, sant, falskt, sant, falskt, sant. 4) protoner, valenselektroner, metaller. 5) Dalton 1; Thomson 2; Rutherford 3; Bohr 4. 6) 16 − 8 = 8 neutroner. 7) De har lika många valenselektroner. 8) T.ex. strålbehandling mot cancer; strålningen kan skada celler.",
]
