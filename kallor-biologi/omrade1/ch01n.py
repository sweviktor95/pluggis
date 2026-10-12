# -*- coding: utf-8 -*-
"""Område 1 Biologi som vetenskap – grundtext (nya ramverket, per moment)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
FIG = '/tmp/bio/fig01n/'
NR = 1
SLUG = "vetenskap"
TAB = "1"
NAMN = "Biologi som vetenskap"
UNDER = "Hur vet vi det vi vet om livet?"
INTRO = ("Hur vet forskare att bakterier kan orsaka sjukdomar, att växter behöver ljus eller att ett påstående på nätet inte stämmer? Ingen har bara bestämt det. "
         "Kunskapen kommer från människor som har ställt frågor och undersökt noggrant. I det här kapitlet lär du dig hur man planerar, genomför och värderar en undersökning, "
         "hur forskare har ändrat sig när nya belägg dykt upp och hur du själv granskar information och argumenterar som en forskare.")
MAL = ["vad biologi är och vad biologer arbetar med", "hur man planerar en undersökning med fråga, hypotes och variabler", "hur man dokumenterar med tabeller, diagram och rapport",
       "hur man värderar resultat och drar en slutsats", "vad vetenskap kan och inte kan pröva", "hur förklaringar har ändrats när nya belägg kommit",
       "hur du söker information, bedömer källor och argumenterar"]
FUNDERA = "Tänk på något du ”vet” om kroppen eller naturen, till exempel att man blir förkyld av att frysa. Hur skulle du kunna ta reda på om det verkligen stämmer?"
DELOMR = {"1.1": "Undersöka systematiskt", "1.2": "Modeller, källor och argument"}

def roww(m, side):
    return row(m, side).replace('class="row"', 'class="row w"', 1)
def cards4(items):
    return '<div class="cards" style="grid-template-columns:repeat(%d,1fr)">' % len(items) + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in items) + '</div>'

S = []
FOOTS = []
def add(nr, t, foot, inner):
    S.append((nr, t, inner)); FOOTS.append(foot)

# ------------------------------------------------------------------ Start
add("Start", "Vad är biologi?", f"Kapitel {NR} · {NAMN} · Start",
 row("<p>Biologi betyder ”läran om livet”. Ordet kommer från grekiskans <em>bios</em> (liv) och <em>logos</em> (lära). Biologi handlar om allt som lever: bakterier, svampar, växter, djur och människor. Allt levande kallas <strong class='green'>organismer</strong>. Biologer undersöker hur organismer är uppbyggda, hur de fungerar, hur de samspelar med varandra och hur livet har utvecklats.</p>"
     "<p>Biologi är en av <strong class='green'>naturvetenskaperna</strong>, tillsammans med bland annat kemi och fysik. Gemensamt för dem är att de försöker förklara naturen med hjälp av <strong class='green'>systematiska undersökningar</strong>: undersökningar som görs noggrant och planerat, så att andra kan kontrollera och upprepa dem.</p>"
     "<h3>Biologer arbetar på många sätt</h3><p>Livet är så stort att ingen kan vara expert på allt. Därför specialiserar sig biologer. Vissa arbetar ute i naturen, andra i laboratorier, på sjukhus eller vid en dator där de analyserar stora mängder data.</p>",
   [begrepp([("Biologi", "Läran om livet och levande organismer."), ("Organism", "En levande varelse, till exempel en bakterie, en svamp, en växt eller ett djur."),
             ("Naturvetenskap", "Vetenskaper som undersöker naturen, t.ex. biologi, kemi och fysik.")])])
 + fig(FIG+"l_yrken.png", "<b>Bild 1.1</b> Fyra sorters biologer: zoolog (djur), botaniker (växter), mikrobiolog (små organismer) och marinbiolog (livet i havet).", "82%")
 + kolla("Start", ["Vad betyder ordet biologi?", "Vad menas med att en undersökning är systematisk?", "Välj två av biologerna i bild 1.1. Ge ett exempel på en fråga som var och en kan undersöka."]))

# ------------------------------------------------------------------ 1.1.1
add("1.1.1", "Från fråga till plan", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · 1.1.1 Från fråga till plan",
 "<p>All forskning börjar med nyfikenhet. Men en bra undersökning börjar med en <strong class='green'>undersökningsbar fråga</strong>: en fråga som går att besvara med mätningar eller observationer. ”Är solrosor fina?” är en åsikt. ”Hur mycket växer en solros på en vecka?” går att mäta.</p>"
 + table(["Går inte att undersöka", "Går att undersöka", "Varför är den bättre?"],
         [["Är musik bra när man pluggar?", "Kommer man ihåg fler ord efter att ha lyssnat på musik än efter tystnad?", "Den säger vad som ska mätas (antal ord) och vad som ska jämföras."],
          ["Är krasse bra?", "Växer krasse högre i ljus än i mörker?", "Man kan mäta höjden i millimeter."]], "tbl")
 + "<h3>Forskning är en cykel</h3>"
 + roww("<p>Arbetet följer ofta stegen i bild 1.2. Efter frågan formulerar forskaren en <strong class='green'>hypotes</strong>: ett möjligt svar på frågan som går att pröva, med en motivering. Därefter planeras och görs en undersökning, och resultatet leder till en slutsats och ofta till en ny fråga. Svaret ska bygga på <strong class='green'>belägg</strong>, alltså mätningar och observationer, och inte på vad någon tycker.</p>"
        "<p>En <strong class='green'>teori</strong> är något större än en hypotes: en förklaring som har prövats av många forskare under lång tid och som stämmer med väldigt många observationer. Evolutionsteorin och cellteorin är exempel.</p>",
        [fig(FIG+"l_cykel.png", "<b>Bild 1.2</b> Den vetenskapliga arbetsgången. I verkligheten hoppar forskare ofta fram och tillbaka mellan stegen.")])
 + "<h3>Ett rättvist försök</h3>"
 + row("<p>Klass 7B undrar om krasse behöver ljus för att växa. Hypotesen är: <em>Krassen i ljus växer högre, eftersom växter behöver ljus för fotosyntesen.</em> En <strong class='green'>variabel</strong> är något som kan ändras eller mätas. För att testet ska bli rättvist får bara <em>en</em> variabel ändras åt gången. Allt annat måste vara lika, annars vet man inte vad som orsakade resultatet.</p>"
       "<p>Ofta har man också en <strong class='green'>kontrollgrupp</strong>, där man inte ändrar något, så att man har något att jämföra med. I krassförsöket är krassen i ljus kontrollgrupp.</p>",
       [begrepp([("Undersökningsbar fråga", "En fråga som kan besvaras med mätningar eller observationer."), ("Hypotes", "Ett möjligt, prövbart svar med en motivering."),
                 ("Variabel", "Något som kan ändras eller mätas i en undersökning."), ("Kontrollgrupp", "Grupp där man inte ändrar något, att jämföra med.")])])
 + fig(FIG+"v_krasse.png", "<b>Bild 1.3</b> Krasse som vuxit i sju dagar i ljus (A) och i en mörk låda (B).", "78%")
 + table(["Typ av variabel", "Vad betyder det?", "I krassförsöket"],
         [["Oberoende variabel", "Det du själv ändrar med flit.", "Ljus eller mörker"], ["Beroende variabel", "Det du mäter – det som kanske påverkas.", "Krassens höjd i mm"],
          ["Kontrollerade variabler", "Allt annat, som måste vara lika i båda försöken.", "Jord, vatten, temperatur, antal frön, tid"]])
 + "<h3>Säkerhet i labbet</h3>"
 + roww(steps(["Läs hela instruktionen innan du börjar.", "Använd skyddsglasögon och förkläde när läraren säger det. Sätt upp långt hår.", "Ät, drick eller smaka aldrig något i labbet.",
               "Säg till direkt om något går sönder eller om du skadar dig.", "Städa och tvätta händerna när du är klar."]),
        [box("varning", "Faroetiketter", "<p>Kemikalier som kan vara farliga har en varningssymbol på förpackningen. Läs alltid etiketten innan du använder något.</p>"),
         box("tank", "Tänk efter", "<p>Varför ska man aldrig äta i labbet, även när man bara använder ofarliga saker just den dagen?</p>")])
 + kolla("1.1.1", ["Gör frågan ”Är hundar snälla?” om till en undersökningsbar fråga.", "Vad är skillnaden mellan oberoende och beroende variabel?", "Varför behövs en kontrollgrupp?", "Varför får man bara ändra en variabel åt gången?"]))

# ------------------------------------------------------------------ 1.1.2
add("1.1.2", "Dokumentera", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · 1.1.2 Dokumentera",
 "<p>Under försöket mäter klassen krassen varje dag och skriver direkt ner värdena i en <strong class='green'>tabell</strong>. Tabellen ska ha rubriker, och efter varje mått ska enheten stå, till exempel mm eller s. När försöket är klart räknar man ut <strong class='green'>medelvärdet</strong> för varje grupp: lägg ihop alla värden och dela med antalet värden.</p>"
 + roww(table(["Dag", "1", "3", "5", "7"], [["A · ljus (mm)", "5", "15", "28", "40"], ["B · mörker (mm)", "5", "25", "42", "60"]], "tbl num")
        + '<p class="cap" style="margin-top:-4pt"><b>Tabell 1.1</b> Krassens medelhöjd i klassens försök (exempelvärden).</p>'
        "<h3>Välj diagram</h3><p>Ett diagram gör det lättare att se mönster. Ett <strong>stapeldiagram</strong> passar när du jämför grupper, till exempel höjden efter sju dagar. Ett <strong>linjediagram</strong> passar när något förändras över tid. Tiden sätts på x-axeln och det du mäter på y-axeln. Glöm inte rubrik, namn och enheter på axlarna.</p>"
        "<p>Läs av diagrammet noga: vilken stapel är högst, hur stor är skillnaden, och vad står siffrorna för?</p>",
        [fig(FIG+"l_stapel.png", "<b>Bild 1.4</b> Krassens höjd efter 7 dagar.")])
 + "<h3>Skriva en rapport</h3><p>När du har gjort en undersökning redovisar du den i en rapport. Den ska vara så tydlig att någon annan kan göra om försöket och kontrollera ditt resultat.</p>"
 + cards4([("Syfte och frågeställning", "Vad vill du ta reda på?"), ("Hypotes", "Vad tror du och varför?"), ("Material och metod", "Vad använde du och hur gjorde du?"),
           ("Resultat", "Vad hände? Tabeller och diagram."), ("Diskussion och slutsats", "Vad betyder resultatet? Felkällor?")]).replace("repeat(5,1fr)", "repeat(5,1fr)")
 + row(box("klimat", "Digitala verktyg", "<p>Ett kalkylprogram räknar ut medelvärden och ritar diagram åt dig. Mobilkameran kan dokumentera försöket med bilder. Du måste ändå själv avgöra om diagrammet visar det du vill veta.</p>"), None)
 + kolla("1.1.2", ["Vad ska en tabell innehålla?", "När passar ett stapeldiagram och när ett linjediagram?", "Räkna ut medelvärdet av 12, 14 och 13 mm.", "Vilka delar ingår i en rapport?"]))

# ------------------------------------------------------------------ 1.1.3
add("1.1.3", "Värdera", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · 1.1.3 Värdera",
 "<p>En forskare frågar sig alltid: Kan jag lita på resultatet? Mätte vi rätt sak? Ett resultat kan bli fel på flera sätt. Sådant som kan ha påverkat resultatet utan att vi ville det kallas <strong class='green'>felkällor</strong>.</p>"
 + table(["Typ av felkälla", "Exempel i krassförsöket", "Vad hjälper?"],
         [["Slump", "En krasse får av en slump dålig jord. En fläkt blåser på en av lådorna.", "Fler mätningar och upprepning. Slumpen jämnar då ut sig."],
          ["Systematiskt fel", "Mörka lådan blir varmare, så temperaturen och inte ljuset påverkar. Eller man mäter alltid från fel ställe.", "Bättre planering: håll alla andra variabler lika. Kontrollera mätmetoden."]], "tbl")
 + "<p>Man gör därför försöket flera gånger och räknar ut ett medelvärde. Då får slumpen mindre betydelse. Ett enda avvikande värde bör man undersöka: var det ett misstag, eller säger det något?</p>"
 + roww("<h3 style='margin-top:0'>Tillförlitlighet och giltighet</h3><p><strong class='green'>Tillförlitlighet</strong> handlar om hur säkra mätningarna är: skulle vi få samma resultat om vi gjorde om försöket? <strong class='green'>Giltighet</strong> handlar om huruvida vi har mätt det vi ville veta. Är höjden ett bra mått på om krassen ”växer bra”? Det hade kanske varit bättre att väga krassen eller titta på färgen.</p>"
        "<h3>Slutsatsen</h3><p>Slutsatsen ska svara på frågan och stämma med resultatet. Klassens slutsats: <em>Krasse som växer i mörker blir högre men svagare än krasse i ljus. Höjden är inte ett bra mått på hur bra en växt mår.</em> Skriv också vad du inte kan veta. Klassen testade bara krasse, så den kan inte säga att alla växter gör så.</p>",
        [begrepp([("Felkälla", "Något som kan ha påverkat resultatet utan att man ville det."), ("Slump", "Tillfälliga variationer som inte beror på det man undersöker."),
                  ("Tillförlitlighet", "Hur säkra och upprepbara mätningarna är."), ("Giltighet", "Om man har mätt det man ville undersöka."), ("Slutsats", "Det man kan dra för svar på frågan utifrån resultatet.")]),
         box("visste", "Bra att veta", "<p>Ett resultat som inte stämmer med hypotesen är inte ett misslyckande. Hypotesen var att krassen blir högre i ljus. Resultatet visade något annat och klassen lärde sig något nytt. Så går forskningen framåt.</p>")])
 + kolla("1.1.3", ["Vad är skillnaden mellan slump och systematiskt fel? Ge ett exempel på vardera.", "Varför minskar slumpens betydelse när man upprepar ett försök?", "Vad menas med giltighet?", "Varför ska en slutsats också säga vad man inte vet?"]))

# ------------------------------------------------------------------ Labb 1.1
add("Labb", "1.1 Reaktionstid som rättvist försök", f"Kapitel {NR} · Delområde 1.1 {DELOMR['1.1']} · Labb 1.1 Reaktionstid",
 "<p>Du ska planera och genomföra en hel undersökning på 45 minuter. Hur snabbt reagerar du? Med en linjal som någon släpper kan du mäta det: ju kortare linjalen hinner falla innan du fångar den, desto snabbare är din reaktion.</p>"
 + fig(FIG+"v_linjal.png", "<b>Bild 1.5</b> Linjalen släpps utan förvarning. Du fångar den med tumme och pekfinger. Läs av vid fingrarna.", "52%")
 + roww("<p><strong class='green'>Frågeställning:</strong> Reagerar jag snabbare med en hand än med den andra? (Eller välj en egen fråga.)</p><p><strong class='green'>Hypotes:</strong> Skriv vad du tror och motivera.</p>"
        "<p><strong class='green'>Material:</strong> linjal 30 cm, penna, papper.</p><h3>Gör så här</h3>"
        + steps(["Bestäm oberoende variabel (vilken hand), beroende variabel (fallsträckan i cm) och vad som ska hållas lika.", "Din kompis håller linjalen lodrätt med noll vid dina fingrar. Släpp utan förvarning.",
                 "Läs av var du fångade linjalen. Gör minst fem försök med varje hand.", "Skriv i en tabell, räkna medelvärde och omvandla till tid med tabellen intill.", "Rita ett stapeldiagram. Skriv slutsats och felkällor."]),
        [table(["Fallsträcka", "Reaktionstid"], [["5 cm", "0,10 s"], ["10 cm", "0,14 s"], ["15 cm", "0,17 s"], ["20 cm", "0,20 s"], ["25 cm", "0,23 s"], ["30 cm", "0,25 s"]], "tbl num"),
         box("begrepp", "Variabler", "<b class='t'>Oberoende</b><p>Vilken hand.</p><b class='t'>Beroende</b><p>Fallsträckan.</p><b class='t'>Lika</b><p>Linjal, startläge, förvarning, antal försök.</p>"),
         box("tank", "Utvärdera", "<p>Kan resultatet bero på övning och inte på handen? Hur kan du förbättra försöket?</p>")])
 + '<p class="note">Säkerhet: låg risk. Sitt eller stå stadigt. Redovisa klassens värden, inte personliga.</p>')

# ------------------------------------------------------------------ 1.2.1
add("1.2.1", "Vad kan vetenskap pröva?", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · 1.2.1 Vad kan vetenskap pröva?",
 "<p>Ett <strong class='green'>påstående</strong> är något man säger är sant. Naturvetenskapen kan pröva ett påstående om det går att undersöka med mätningar eller observationer. Det man mäter eller ser kallas <strong class='green'>belägg</strong>. Vi skiljer mellan tre saker:</p>"
 + cards4([("Belägg", "Mätningar och observationer som andra kan kontrollera. Exempel: vatten fryser vid 0 °C."), ("Åsikt", "Vad någon tycker. Går inte att mäta. Exempel: pizza är godast."), ("Tro", "Något man är övertygad om utan att det kan prövas. Vetenskapen kan varken bevisa eller motbevisa det.")]).replace("repeat(3,1fr)", "repeat(3,1fr)")
 + table(["Påstående", "Går det att pröva?", "Hur?"],
         [["Hundar har bättre luktsinne än människor.", "Ja", "Man kan testa hur svaga lukter olika djur hittar."], ["Katter är gulligare än hundar.", "Nej", "Det är en åsikt. Det finns inget att mäta."],
          ["Krasse gror snabbare vid 20 °C än vid 10 °C.", "Ja", "Mät hur många frön som gror vid olika temperaturer."], ["Det är fel att jaga varg.", "Nej, inte bara med mätningar", "Det är en värdering. Biologi kan ge fakta till diskussionen, men inte avgöra vad som är rätt."]], "tbl")
 + "<h3>Ett påstående måste kunna visas vara fel</h3>"
 + roww("<p>Ett påstående som går att pröva måste också kunna visa sig vara fel. Om ett påstående passar med allt som kan hända kan man aldrig pröva det. ”Det kommer att hända något bra eller dåligt för dig i morgon” går aldrig att motbevisa, men säger inte heller något.</p>"
        "<h3>Pseudovetenskap</h3><p>Ibland låter något vetenskapligt fast det inte är det. Det kallas <strong class='green'>pseudovetenskap</strong>: ”pseudo” betyder falsk. Det använder gärna ord som ”forskare” eller ”kliniskt bevisat”, men påståendena har inte prövats ordentligt, eller har prövats och visat sig vara fel.</p>"
        "<p>Horoskop är ett exempel. År 1985 fick 28 erfarna astrologer i ett dubbelblint test para ihop födelsehoroskop med personlighetsprofiler. De lyckades inte bättre än slumpen (Carlson, <em>Nature</em>).</p>",
        [begrepp([("Påstående", "Något man säger är sant."), ("Belägg", "Mätningar och observationer som visar något."), ("Åsikt", "Vad någon tycker. Går inte att pröva med mätningar."),
                  ("Pseudovetenskap", "Låter som vetenskap men saknar prövade belägg.")]),
         box("fundera", "Fundera", "<p>Varför är det en styrka för vetenskapen att den kan visa sig ha fel?</p>")])
 + table(["Vetenskap", "Pseudovetenskap"], [["Påståenden går att pröva och kan visa sig vara fel.", "Påståenden är vaga eller går inte att pröva."], ["Bygger på undersökningar med många deltagare.", "Bygger på enstaka berättelser: ”Det funkade för mig!”"],
          ["Granskas av andra experter.", "Granskas inte, eller bara av den som säljer något."], ["Ändrar sig när nya belägg kommer.", "Håller fast vid idén, vad undersökningarna än visar."]], "tbl num")
 + kolla("1.2.1", ["Vad är skillnaden mellan belägg och åsikt?", "Varför kan man inte pröva ”Det är fel att jaga varg” med bara mätningar?", "Ge två kännetecken på pseudovetenskap."]))

# ------------------------------------------------------------------ 1.2.2
add("1.2.2", "När forskare ändrat sig", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · 1.2.2 När forskare ändrat sig",
 "<p>En <strong class='green'>förklaringsmodell</strong> är ett sätt att förklara hur något fungerar. En modell är en förenkling av verkligheten. Den är användbar så länge den hjälper oss att förstå och förutsäga, men den kan behöva ändras när nya undersökningar visar något annat. Här är tre exempel.</p>"
 + "<h3>Pasteur och svanhalskolven (1861)</h3>"
 + roww("<p>Förr trodde många att <strong class='green'>mikroorganismer</strong> kunde uppstå av sig själva i mat som stod framme. Louis Pasteur kokade buljong i två sorters glaskolvar. Kolv A hade ett rakt rör, så att damm och mikroorganismer från luften kunde falla ner. Där blev buljongen grumlig. Kolv B hade en lång, böjd ”svanhals”. Luft kom in, men dammet fastnade i böjen och buljongen förblev klar.</p>"
        "<p>Pasteur visade att mikroorganismerna kom utifrån och inte uppstod av sig själva. Hans försök var ett bra belägg eftersom bara en sak skilde kolvarna åt: halsens form.</p>",
        [fig(FIG+"v_pasteur.png", "<b>Bild 1.6</b> Pasteurs svanhalskolvar.")])
 + "<h3>Semmelweis och de otvättade händerna (1847)</h3>"
 + roww("<p>På Allmänna sjukhuset i Wien fanns på 1840-talet två förlossningsavdelningar. På den ena arbetade läkare och läkarstudenter, som också obducerade döda kroppar. På den andra arbetade barnmorskor, som inte gjorde det. På läkarnas avdelning dog fler mödrar i barnsängsfeber. År 1846 var dödligheten där mer än fem gånger högre.</p>"
        "<p>År 1847 dog Semmelweis vän Jakob Kolletschka efter att ha skurit sig med en obduktionskniv. Han fick samma symtom som de sjuka mödrarna. Semmelweis drog slutsatsen att ”likpartiklar” fördes över med läkarnas händer. Han krävde att alla skulle tvätta händerna i klorkalklösning. Dödligheten på läkarkliniken sjönk från 11,4 % år 1846 till 1,3 % år 1848.</p>"
        "<p>Ändå godtogs inte hans idé. Han kunde inte förklara <em>varför</em> det hjälpte, eftersom man ännu inte visste att bakterier kan orsaka sjukdomar, och han publicerade sig sent. Först årtionden senare fick bakterieläran fäste genom Pasteur, Lister och Koch.</p>",
        [fig(FIG+"f_semmelweis2.png", "<b>Bild 1.7</b> Dödlighet på läkarkliniken före och efter handtvätt.")])
 + "<h3>Marshall, Warren och magsåren (1982)</h3>"
 + roww("<p>Under större delen av 1900-talet trodde man att magsår kom av stress och livsstil. Man behandlade med syrahämmande medicin, men såren kom ofta tillbaka. Man ansåg dessutom att bakterier inte kunde leva i magsäckens syra.</p>"
        "<p>År 1982 upptäckte de australiska forskarna Barry Marshall och Robin Warren bakterien <em>Helicobacter pylori</em> i magsäcken. De föreslog att den orsakade sårbildningen. Många trodde inte på dem. År 1984 drack Marshall själv en bakterieodling och fick en inflammation i magsäcken (gastrit). Senare visades att magsår botas när bakterien utrotas med antibiotika och syrahämmande medel. År 2005 fick de Nobelpriset i fysiologi eller medicin.</p>"
        "<p class='note'>Marshalls självförsök var riskabelt. Forskning på människor måste idag etikprövas.</p>",
        [fig(FIG+"f_hpylori.png", "<b>Bild 1.8</b> <em>Helicobacter pylori</em> i magsäcken.")])
 + row(box("visste", "Gemensamt för exemplen", "<p>I alla tre fallen fanns ett belägg från en undersökning som inte passade den gamla förklaringen. Men det tog tid att övertyga andra. Forskarvärlden vill ha belägg som kan granskas och upprepas, och helst en modell som förklarar <em>hur</em> det fungerar.</p>"), None)
 + kolla("1.2.2", ["Vad visade Pasteurs svanhalskolv?", "Vad var beläggen för Semmelweis idé?", "Varför trodde många inte på honom?", "Vad menas med att en modell är en förenkling? Ge ett exempel."]))

# ------------------------------------------------------------------ 1.2.3
add("1.2.3", "Söka information och bedöma källor", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · 1.2.3 Söka information och bedöma källor",
 "<p>Varje dag möter du påståenden om hälsa, mat, djur och miljö: i sociala medier, reklam, nyheter och samtal. Att söka bra information börjar med att använda flera sökord, till exempel <em>sömn tonåringar forskning</em>, och att jämföra flera källor. Sedan måste du bedöma källorna.</p>"
 + table(["Typ av källa", "Exempel", "Styrka", "Se upp med"],
         [["Myndighet", "Folkhälsomyndigheten, Naturvårdsverket, 1177", "Faktagranskad, oberoende", "Kan vara allmänt hållen"], ["Forskning", "Universitet, vetenskaplig artikel", "Granskad av andra experter", "En enda studie räcker inte. Kan vara svår att läsa"],
          ["Nyhetsmedia", "Tidningar, tv", "Snabb och lättläst", "Rubriker kan vara vinklade"], ["Sociala medier", "Inlägg, videor", "Kan peka ut nya idéer", "Ofta ogranskat. Berättelser är inte belägg"],
          ["Reklam och företag", "Webbplats för en produkt", "Känner sin produkt", "Vill sälja. Tendens"]], "tbl")
 + "<h3>Trovärdig och relevant</h3>"
 + "<p>En källa är <strong class='green'>trovärdig</strong> om man kan lita på den. En källa är <strong class='green'>relevant</strong> om den passar din fråga. En trovärdig källa kan vara irrelevant: en studie om möss säger inte nödvändigtvis något om människor. Fyra frågor brukar kallas de källkritiska kriterierna:</p>"
 + cards4([("Äkthet", "Är källan den den utger sig för att vara? Är bilden eller citatet äkta?"), ("Tid", "När skrevs det? Är informationen fortfarande aktuell?"),
           ("Beroende", "Var kommer uppgifterna ifrån? Har avsändaren själv undersökt, eller bara hört från någon annan?"), ("Tendens", "Vill avsändaren något: sälja, övertyga eller påverka? Visas flera sidor?")])
 + fig(FIG+"v_inlagg.png", "<b>Bild 1.9</b> Ett påhittat inlägg i sociala medier, granskat med de källkritiska kriterierna.", "70%")
 + "<h3>Argumentera</h3>"
 + roww("<p>När du har granskat källorna ska du kunna använda dem. Ett bra argument har ett <strong class='green'>påstående</strong>, ett <strong class='green'>belägg</strong> och ett svar på ett <strong class='green'>motargument</strong>.</p>"
        "<p><b>Exempel:</b> <em>Skolor bör ha rutiner för handtvätt före lunch. Handtvätt minskar spridning av infektioner, vilket Semmelweis exempel visar. Någon kan säga att det tar tid. Men tiden är liten jämfört med de dagar elever är sjuka.</em></p>",
        [box("tank", "Så argumenterar du", "<p>1. Påstående<br>2. Belägg (varför?)<br>3. Motargument (vad kan någon säga emot?)<br>4. Bemöt det<br>5. Slutsats</p>")])
 + kolla("1.2.3", ["Vad är skillnaden mellan trovärdig och relevant?", "Varför är reklam en källa man ska vara försiktig med?", "Granska ett påstående med hjälp av de fyra kriterierna.", "Skriv ett kort argument om ett eget påstående, med belägg och motargument."]))

# ------------------------------------------------------------------ Labb 1.2
add("Labb", "1.2 Granska ett påstående", f"Kapitel {NR} · Delområde 1.2 {DELOMR['1.2']} · Labb 1.2 Granska ett påstående",
 "<p>Du ska granska ett påstående med hjälp av två källor och skriva ett argument med belägg och motargument. Arbetet tar 45 minuter. Välj ett påstående:</p>"
 + bullets(["Vi använder bara tio procent av hjärnan.", "Socker gör barn hyperaktiva.", "Blixten slår aldrig ned två gånger på samma plats."])
 + roww("<h3 style='margin-top:0'>Gör så här</h3>" + steps(["Sök efter påståendet med flera sökord. Hitta två källor av olika typ, till exempel en myndighet och en tidning.", "Bedöm varje källa: äkthet, tid, beroende och tendens. Är den trovärdig? Är den relevant?",
          "Bestäm om påståendet är sant, osant eller osäkert, och skriv varför.", "Skriv ett argument: påstående, belägg, motargument, bemötande, slutsats."]),
        [table(["Fråga", "Källa 1", "Källa 2"], [["Vem har skrivit?", "", ""], ["Varför?", "", ""], ["Belägg?", "", ""], ["Hur nytt?", "", ""], ["Trovärdig?", "", ""]], "tbl num"),
         box("tank", "Utvärdera", "<p>Vilken källa litar du mest på? Varför? Hur kan två trovärdiga källor säga olika?</p>")])
 + '<p class="note">Säkerhet: skriv inga personuppgifter och klicka inte på reklam eller länkar du inte litar på.</p>')

SAMMAN = ["<strong>Biologi</strong> är läran om livet. Biologer arbetar i fält, i labb och vid datorer.",
          "En <strong>undersökningsbar fråga</strong> går att besvara med mätningar. En <strong>hypotes</strong> är ett prövbart svar med motivering.",
          "I ett rättvist försök ändrar man en <strong>oberoende variabel</strong>, mäter en <strong>beroende variabel</strong> och håller alla andra lika. En kontrollgrupp ger något att jämföra med.",
          "Värden skrivs i tabell med rubriker och enheter. Diagram har rubrik och axlar med namn och enhet. Man räknar medelvärde av upprepningar.",
          "Resultat kan bli fel av slump eller systematiska fel. Upprepning minskar slumpens betydelse. Slutsatsen ska svara på frågan och stämma med resultatet.",
          "Vetenskap prövar påståenden med belägg. Åsikter och tro går inte att pröva med mätningar. Pseudovetenskap saknar prövade belägg.",
          "Förklaringsmodeller ändras när nya belägg kommer: Pasteur, Semmelweis, Marshall och Warren.",
          "Bedöm källor med äkthet, tid, beroende och tendens. Skilj trovärdig från relevant. Ett argument har påstående, belägg och bemötande av motargument."]
BEGR = [("Belägg", "Observationer och mätningar som stöder en slutsats."), ("Beroende variabel", "Det man mäter i en undersökning."), ("Felkälla", "Något som kan ha påverkat resultatet utan att man ville det."),
        ("Förklaringsmodell", "Ett sätt att förklara hur något fungerar."), ("Giltighet", "Om man har mätt det man ville undersöka."), ("Hypotes", "Ett möjligt, prövbart svar på en fråga."),
        ("Kontrollgrupp", "Grupp där man inte ändrar något, att jämföra med."), ("Kontrollerade variabler", "Det som hålls lika för att testet ska bli rättvist."), ("Medelvärde", "Summan av värdena delat med antalet."),
        ("Oberoende variabel", "Det man själv ändrar i en undersökning."), ("Pseudovetenskap", "Låter vetenskapligt men saknar prövade belägg."), ("Relevant", "Passar min fråga."),
        ("Slump", "Tillfälliga variationer som inte beror på det man undersöker."), ("Teori", "En väl prövad förklaring som stöds av många belägg."), ("Tillförlitlighet", "Hur säkra och upprepbara mätningarna är."),
        ("Trovärdig", "Går att lita på."), ("Undersökningsbar fråga", "Kan besvaras med mätningar eller observationer.")]
ANNONS = ('<div style="border:1pt solid #d9d2c8;border-radius:5pt;padding:5pt 8pt;margin:3pt 0"><b>NYHET! DetoxPlåstret™</b><br>Sätt plåstret under foten när du sover – på morgonen har det blivit brunt av alla gifter som dragits ut ur kroppen! ”Jag har aldrig mått så bra”, säger Anna, 34. Vetenskapligt utvecklat.</div>')
TEST = [
 ("A", "Elin undersöker om temperaturen påverkar hur mycket gas jäst bildar. Hon mäter mängden gas efter 20 minuter. Vilken är den beroende variabeln?", ["A Temperaturen", "B Mängden gas", "C Mängden jäst", "D Tiden, 20 minuter"], 1, 0),
 ("A", "Vilket påstående går att pröva med naturvetenskapliga metoder?", ["A Blåbär smakar godare än lingon.", "B Krasse gror snabbare vid 20 °C än vid 10 °C.", "C Det är fel att jaga varg.", "D Naturen vill alltid vara i balans."], 1, 0),
 ("A", "Vad visade att handtvätt hjälpte på Semmelweis avdelning?", ["A Läkarna blev tröttare.", "B Dödligheten sjönk från 11,4 % till 1,3 %.", "C Barnmorskorna slutade arbeta.", "D Fler kvinnor kom till sjukhuset."], 1, 0),
 ("B", "Förklara varför man upprepar ett försök flera gånger och räknar ut ett medelvärde.", None, 2, 4),
 ("B", "Förklara skillnaden mellan en trovärdig och en relevant källa. Ge ett exempel.", None, 2, 4),
 ("C", "Noah vill ta reda på om gödning påverkar hur mycket ärtplantor växer. Han har ärtfrön, krukor, jord, vatten, flytande gödning och en linjal. Planera undersökningen. Skriv<br>a) en frågeställning och en hypotes,<br>b) oberoende och beroende variabel,<br>c) minst tre variabler som ska hållas lika. ●●●", None, 3, 8),
 ("C", "Mira vill ta reda på om temperaturen påverkar hur snabbt bönor gror. Hon sätter bönor i en burk med fuktigt papper i ett soligt fönster och bönor i en annan burk i kylskåpet.<br>a) Ge ett skäl till att Miras undersökning inte blir rättvis.<br>b) Föreslå en förbättring. ●●", None, 2, 6),
 ("E", "Läs annonsen och svara." + ANNONS + "a) Använd de källkritiska kriterierna. Ge två skäl till att vara skeptisk.<br>b) Hur skulle man kunna undersöka om plåstret verkligen drar ut gifter? ●●●", None, 3, 6),
 ("F", "Välj ett av exemplen Pasteur, Semmelweis eller Marshall och Warren. Förklara hur förklaringen ändrades när nya belägg kom, och varför det tog tid att övertyga andra. ●●", None, 2, 6),
]
DEL_NAMN = {"A": "Välj ett alternativ", "B": "Svara kort", "C": "Planera en undersökning", "E": "Granska information", "F": "Resonera"}
FACIT = ["B", "B", "B",
 "Ett enskilt försök kan påverkas av slump eller misstag. Med flera försök kan man räkna medelvärde och upptäcka avvikande värden. Resultatet blir mer tillförlitligt.",
 "Trovärdig = går att lita på. Relevant = passar min fråga. Exempel: en studie på möss kan vara trovärdig men inte relevant för en fråga om människor.",
 "a) T.ex. Växer ärtplantor högre om de får gödning? Hypotes med motivering (gödning innehåller näring). b) Oberoende: gödning (med/utan). Beroende: höjd. c) Samma jord, vatten, ljus, temperatur, kruka, antal frön, tid. Även upprepning med flera plantor.",
 "a) Både temperatur och ljus skiljer sig (fönster ljust, kylskåp mörkt). b) Båda i samma ljus eller båda i mörker; håll vatten och antal bönor lika; flera bönor.",
 "a) Tendens (företaget säljer), beroende (ingen källa till ”vetenskapligt utvecklat”), en persons upplevelse är inget belägg. b) Testa plåster på flera personer och ett rent plåster som kontroll, eller på en svamp med rent vatten. Brunfärgningen kan bero på fukt.",
 "T.ex. Pasteur: fanns idén att liv uppstår av sig själv; svanhalskolven visade att mikroorganismer kommer utifrån. Semmelweis: dödligheten sjönk efter handtvätt men man visste inte varför. Marshall och Warren: bakterie i magsäcken, få trodde, Marshalls självförsök, antibiotika botar, Nobelpriset 2005. Ett välutvecklat svar förklarar varför belägg och förklaringsmodell behövdes."]
LGR = ("Området täcker det centrala innehållet ”Systematiska undersökningar och granskning av information” i årskurs 7–9: fältstudier och experiment (1.1.1, labb 1.1), planering, utförande, värdering och dokumentation med tabeller och diagram (1.1.1–1.1.3), "
       "sambandet mellan undersökningar och förklaringsmodellers framväxt och föränderlighet (1.2.2), informationssökning och kritisk granskning (1.2.3, labb 1.2) samt argumentation (1.2.3, labb 1.2). Kursplanens långsiktiga mål att genomföra systematiska undersökningar och använda biologi för att granska information tränas hela området. "
       "Begreppen följer Skolverkets kommentarmaterial: oberoende och beroende variabel, felkällor, tillförlitlighet och giltighet, samt trovärdighet och relevans i källkritiken.")
FAKTA = ("Krass- och tabellvärden är exempelvärden för undervisning. Faktakontrollerat mot: Semmelweis, MJA 2018 (11,4 % år 1846, 1,3 % år 1848, Kolletschka 1847); Pasteur, Britannica och Memorial University (svanhalskolv, 1861); Marshall och Warren, Nobelstiftelsen 2005 och PMC2661189 (upptäckt 1982, självförsök 1984); "
         "Carlson, Nature 1985 (28 astrologer, ej bättre än slump). Reaktionstidstabellen är räknad med t = √(2s/g). Se kallor-omrade1.md. · Illustrationer: egenritade.")
HANDLEDNING_HTML = """<h3>Handledning per moment (grundtext)</h3>
<p><b>Start (ca 15 min).</b> Mål: eleven vet vad biologi är och att organismer är allt levande. Låt eleverna berätta vilken biolog de skulle vilja vara.</p>
<p><b>1.1.1 Från fråga till plan.</b> C-mål: oberoende, beroende och kontrollerade variabler samt kontrollgrupp. Vanligt fel: eleverna blandar ihop oberoende och beroende. Hjälp: ”det jag ändrar” / ”det jag mäter”. Låt eleverna omformulera ”åsiktsfrågor” till undersökningsbara.</p>
<p><b>1.1.2 Dokumentera.</b> C-mål: välja diagramtyp och motivera, räkna medelvärde, läsa av diagram. Vanligt fel: linjediagram för jämförelse av två grupper, saknade enheter.</p>
<p><b>1.1.3 Värdera.</b> C-mål: skilja slump från systematiskt fel och förklara hur upprepning hjälper. Slutsatsen ska svara på frågan. Fördjupning ligger i fördjupningstexten.</p>
<p><b>Labb 1.1 Reaktionstid (45 min).</b> Material: linjal 30 cm. Förväntat: ca 15–25 cm, alltså 0,17–0,23 s (t = √(2s/g)). Vanliga fel: eleven ser kompisens hand, linjalen hålls sned, startläget ändras. Redovisa klassens värden. Bonuslabb: se sist i lärarhandledningen.</p>
<p><b>1.2.1 Vad kan vetenskap pröva?</b> C-mål: skilja belägg, åsikt och tro; förstå att ett påstående måste kunna visa sig vara fel. Horoskopexemplet: Carlson, Nature 1985. Vanligt fel: ”pröva” uppfattas som ”bevisa sant”.</p>
<p><b>1.2.2 När forskare ändrat sig.</b> C-mål: förstå vad som var belägget i varje fall och att en modell är en förenkling. Kommentar: Semmelweis siffror är från MJA 2018. Betona att Marshalls självförsök inte är något att efterlikna.</p>
<p><b>1.2.3 Söka information och bedöma källor.</b> C-mål: olika källtyper, trovärdig kontra relevant, de fyra kriterierna samt ett enkelt argument med motargument.</p>
<p><b>Labb 1.2 Granska ett påstående (45 min).</b> Facit: (1) Tio-procentsmyten stämmer inte: PET och fMRI visar aktivitet i alla hjärnområden, även under sömn. (2) Kontrollerade studier (Wolraich m.fl.) visar inget samband mellan socker och hyperaktivitet hos barn. (3) Blixten kan slå ned flera gånger på samma plats; Empire State Building träffas ca 25 gånger per år (NOAA via KSAT). Bedömning: C kräver motiverad bedömning av trovärdighet och relevans samt ett argument med bemött motargument.</p>"""
BONUS = dict(
 titel="Hjälper musik minnet?",
 ingress="En kontrollerad undersökning med minnestest. Eleverna väljer själva hur de testar om musik påverkar hur många ord man minns.",
 syfte="Eleverna planerar och genomför en egen undersökning med variabler, upprepning och värdering. Kopplar till 1.1.1–1.1.3.",
 tid="40–60 minuter. Grupper om tre till fyra.",
 material=["Två ordlistor med 15 vardagliga ord (olika ord men lika svåra)", "Stoppur", "Valfri musik", "Papper"],
 genomf=["Gruppen formulerar frågeställning och hypotes.", "Hälften av gruppen lär sig lista A i tystnad och lista B med musik. Den andra hälften gör tvärtom, så att ordningen inte spelar roll.", "Titta på listan i 60 sekunder, vänd bort och skriv upp så många ord som möjligt.", "Räkna medelvärde per villkor och rita diagram."],
 resultat="Resultaten varierar och är ofta små. Det är en poäng: med få deltagare kan slumpen styra. Låt grupperna diskutera hur de skulle göra för att få säkrare svar.",
 sakerhet=["Låg risk. Redovisa gruppens värden, inte personliga resultat.", "Håll volymen låg."],
 problem=["Listorna är olika svåra (felkälla).", "Eleverna kan se på varandra.", "Ordningen på villkoren påverkar (därför byter hälften ordning)."],
 forslag=["Påverkar musik med text mer än musik utan text?", "Påverkar stress (tidspress) hur många ord man minns?"],
 bedom=[("Grundläggande", "Genomför enligt plan och redovisar i tabell."), ("Utvecklat", "Motiverar variabler, byter ordning, räknar medelvärde och drar slutsats."), ("Välutvecklat", "Värderar tillförlitlighet, diskuterar slump och urval och föreslår förbättringar.")])
ELEV_HTML = ('<section class="sec"><div class="pill">Elevblad · Kopieringsunderlag</div><p class="note">Namn: ____________________ &nbsp; Klass: ________</p>'
  '<div class="sh small"><h2>Hjälper musik minnet?</h2></div>'
  + row("<h3>Gör så här</h3>" + steps(["Lär dig lista A i tystnad i 60 sekunder. Vänd bort papperet och skriv upp orden.", "Lär dig lista B med musik i 60 sekunder. Skriv upp orden.", "Räkna rätt ord. Byt ordning med en kompis så att ordningen inte spelar roll."], True)
        + "<p>Vår frågeställning:</p>" + lines(2) + "<p>Vår hypotes (med motivering):</p>" + lines(2) + "<p>Oberoende variabel:</p>" + lines(1) + "<p>Beroende variabel:</p>" + lines(1) + "<p>Kontrollerade variabler:</p>" + lines(2),
        [table(["Person", "Tystnad (antal ord)", "Musik (antal ord)"], [["1", "", ""], ["2", "", ""], ["3", "", ""], ["4", "", ""], ["Medelvärde", "", ""]], "tbl num")
         + "<p>Slutsats:</p>" + lines(3) + "<p>Felkällor och förbättringar:</p>" + lines(3)]).replace('class="row"', 'class="row w"', 1)
  + '</section>')
