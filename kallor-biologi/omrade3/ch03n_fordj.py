# -*- coding: utf-8 -*-
"""Kapitel 3 Biologisk mångfald – fördjupning (nya ramverket, per moment)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/bio/fig03n/'
NR = 3
SLUG = "mangfald"
TAB = "3+"
NAMN = "Biologisk mångfald"
UNDER = "Varför är mångfald en försäkring – och vad är egentligen en art?"
INTRO = ("Varför kan en blandskog klara en torka som slår ut en granplantage? Varför kan en enda art, som havsuttern, avgöra hur ett helt kustekosystem ser ut? "
         "Och är en delfin mer släkt med en haj eller med en ko? I den här fördjupningen resonerar du om hur mångfald ger stabilitet, om nyckelarter, om hur hot hänger ihop och om vad en art egentligen är. "
         "Du tränar också på att läsa släktskap ur ett släktträd och på att förklara hur naturligt urval ger resistenta bakterier. Namn och mätvärden i uppgifterna är påhittade exempel.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Koppla orsak till verkan i ekosystem: förklara hur en förändring sprids genom en näringsväv.", "Var nyanserad: visa vad som är säkert, vad som är en förenkling och vad man mer skulle behöva veta.",
       "Planera en enkel undersökning och värdera hur säker slutsatsen blir."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först grundtexten i kapitel 3. Fördjupningen bygger på begreppen art, population, ekosystem, ekosystemtjänst, näringsväv, rike, anpassning och naturligt urval."
D = {"3.1": "Mångfald, hot och ekosystemtjänster", "3.2": "Gruppera och organismvärlden"}

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F3.1.1", "Mångfald som försäkring", "3.1",
 "<p>I grundtexten läste du att ett artrikt ekosystem ofta klarar störningar bättre. Här tittar vi närmare på <em>varför</em>. Förklaringen handlar om att arter är olika: de reagerar olika på samma störning.</p>"
 + row("<p><strong class='green'>Försäkringseffekten.</strong> Tänk dig en äng med tio växtarter. Under en torr sommar gynnas några arter, till exempel de med djupa rötter, medan andra tynar bort. Men eftersom några klarar torkan blir ängens totala växtmassa ändå ganska stor. På en äng med en enda art finns ingen sådan reserv: tål arten inte torkan, försvinner nästan allt. Skillnaderna mellan arter fungerar alltså som en <strong class='green'>försäkring</strong>. Förenklat: många arter betyder många olika svar på samma störning, och därför blir helheten stabilare.</p>"
       "<p><strong class='green'>Funktionell redundans.</strong> Om flera arter gör ungefär samma jobb i ekosystemet, till exempel flera arter av humlor som pollinerar blåbär, kan en art försvinna utan att tjänsten upphör. Men en art som är den enda som gör ett visst jobb går inte att ersätta. Därför räcker det inte att räkna arter: man måste också fråga <em>vad</em> de gör.</p>",
       [begrepp([("Försäkringseffekt", "Olika arter reagerar olika på störningar, så helheten blir stabilare."), ("Redundans", "Flera arter som kan ta över varandras uppgifter."), ("Genetisk flaskhals", "När en population krymper kraftigt och mycket genetisk variation går förlorad.")]),
        box("tank", "Tänk efter", "<p>Varför ger en plantage med bara en trädart sämre försäkring än en blandskog, även om plantagen har många träd?</p>")])
 + "<h3>Också inom arten</h3>"
 + row("<p>Samma tankegång gäller gener. När en population blir mycket liten förloras genetisk variation, och de individer som är kvar blir nära släkt. Det kallas en <strong class='green'>genetisk flaskhals</strong>. Då ökar risken för <strong class='green'>inavel</strong>, där ofördelaktiga gener oftare dyker upp hos ungarna, och populationen får svårare att anpassa sig om miljön ändras. För små, hotade populationer, som fjällräven, räcker det därför inte att öka antalet djur: man behöver också att de inte är för nära släkt.</p>"
       "<p>Det här är ett skäl till att man ibland flyttar djur mellan populationer för att hålla variationen uppe.</p>",
       [box("visste", "Visste du?", "<p>Potatisbladmögel slog ut skördarna på Irland på 1840-talet eftersom nästan alla potatisplantor var genetiskt mycket lika. Hade odlingarna haft större genetisk variation hade några plantor troligen klarat sjukdomen.</p>")]))

add("F3.1.2", "Nyckelarter och kedjereaktioner", "3.1",
 "<p>Alla arter är inte lika viktiga för hur ett ekosystem ser ut. Vissa arter påverkar mycket mer än deras antal skulle tyda på. De kallas <strong class='green'>nyckelarter</strong>.</p>"
 + row("<p><strong class='green'>Exempel: havsuttern.</strong> Vid Stillahavskusten i Nordamerika äter havsuttrar sjöborrar. Sjöborrar äter i sin tur tångskogar. När man jagade nästan ut havsuttrarna blev det fler sjöborrar, och sjöborrarna betade ner tångskogarna så att de försvann och med dem alla arter som levde där. När uttrarna fick skydd och kom tillbaka kunde tångskogarna återhämta sig. En förändring högst upp i näringskedjan fortplantade sig alltså nedåt. Det kallas en <strong class='green'>trofisk kaskad</strong>.</p>"
       "<p><strong class='green'>Exempel: bävern.</strong> Bävern dämmer vattendrag och skapar dammar och våtmarker. Det gynnar många andra arter, som grodor, fåglar och insekter, och påverkar också vattnets flöde och renhet. Bävern förändrar alltså själva miljön och kallas därför ibland <strong class='green'>ekosystemingenjör</strong>.</p>",
       [begrepp([("Nyckelart", "En art som påverkar ekosystemet mycket mer än vad dess antal motsvarar."), ("Trofisk kaskad", "När en förändring på en nivå i näringsväven fortplantar sig till andra nivåer."), ("Ekosystemingenjör", "En art som skapar eller förändrar miljön åt andra.")]),
        box("tank", "Tänk efter", "<p>Rita en näringskedja med tång, sjöborre och havsutter. Vad händer med tången om uttrarna försvinner, och varför?</p>")])
 + "<h3>Förenklingar och osäkerheter</h3>"
 + "<p>Kaskader är ett bra sätt att förstå samband, men verkligheten är mer komplicerad än en rak kedja. De flesta djur äter flera olika saker, och flera faktorer verkar samtidigt: klimat, sjukdomar och människan. Därför är det svårt att veta exakt hur mycket just en art förklarar. När forskare ska avgöra om en art är en nyckelart jämför de ofta områden med och utan arten, och försöker hålla övrigt lika. Även då är resultaten ibland omdiskuterade.</p>")

add("F3.1.3", "Hot som förstärker varandra", "3.1",
 "<p>I grundtexten lärde du dig fem hot var för sig. I verkligheten verkar de ofta samtidigt och förstärker varandra.</p>"
 + row("<p><strong class='green'>Exempel: fjällräven.</strong> Fjällräven har påverkats av flera saker samtidigt: den jagades hårt, födan (lämlar) varierar kraftigt, och rödräven konkurrerar om mat och lyor och tar sig högre upp i fjällen. Ett varmare klimat kan göra att skogsgränsen flyttar uppåt och ger rödräven mer plats. Varje faktor för sig kanske vore hanterbar, men tillsammans blir pressen stor, och när populationen är liten blir den också känsligare för slumpen.</p>"
       "<p><strong class='green'>Exempel: överfiske.</strong> När många fiskar samma bestånd tar de mer än vad som hinner växa till. Då kan beståndet kollapsa. Ett känt exempel är torsken utanför Newfoundland, där fisket stoppades 1992 efter att beståndet hade rasat. Även efter stoppet tog återhämtningen mycket lång tid. Det visar att det kan vara lättare att förstöra ett ekosystem än att bygga upp det igen.</p>",
       [begrepp([("Kollaps", "När ett bestånd eller ekosystem snabbt minskar kraftigt."), ("Förebyggande åtgärd", "Något man gör innan skadan har hänt."), ("Intressekonflikt", "När olika grupper vill använda samma resurs på olika sätt.")]),
        box("klimat", "Granska kritiskt", "<p>Någon säger: ”Fjällräven har minskat på grund av rödräven.” Varför är det ett förenklat påstående? Vilka andra förklaringar finns, och hur skulle man kunna undersöka vad som väger tyngst?</p>")])
 + "<h3>Att värdera åtgärder</h3>"
 + "<p>Att skydda natur kostar pengar eller begränsar vad människor får göra. Därför måste man värdera både nytta och kostnad, och fråga vem som får nyttan och vem som betalar. Några frågor som hjälper dig att resonera: Vilka grupper berörs? Hur säkra är kunskaperna? Går skadan att reparera? Finns det mindre ingripande alternativ? Ett välgrundat ställningstagande väger flera argument mot varandra och säger också vad man är osäker på.</p>")

add("F3.2.1", "Släktskap och likhet", "3.2",
 "<p>Hur delar man in organismer i grupper? Ett sätt är att gruppera dem efter hur lika de ser ut. Ett annat och mer tillförlitligt sätt är att gruppera efter <strong class='green'>släktskap</strong>: vilka som har gemensamma förfäder.</p>"
 + row("<p>Yttre likhet kan vara missvisande. En haj är en fisk. En delfin är ett däggdjur: den andas luft med lungor, föder levande ungar och ger di. Ändå ser de lika ut, eftersom en strömlinjeformad kropp med fenor är en bra anpassning till ett liv i vatten. När olika grupper utvecklar liknande drag på grund av liknande miljö kallas det <strong class='green'>konvergent evolution</strong>. Likheterna beror alltså på samma slags urval, inte på att de är nära släkt.</p>"
       "<p>Därför tittar forskare i dag mycket på arvsmassan (DNA). Ju mer lika DNA två arter har, desto närmare släkt är de oftast. Släktskap ritas som ett <strong class='green'>släktträd</strong>, där grenarna visar hur arter har delat sig från gemensamma förfäder.</p>",
       [begrepp([("Släktskap", "Hur nära gemensam förfader olika arter har."), ("Konvergent evolution", "När olika arter utvecklar liknande drag på grund av liknande miljö."), ("Släktträd", "Ett diagram som visar hur arter är släkt med varandra.")]),
        box("tank", "Tänk efter", "<p>Varför kan en delfin och en haj se lika ut fast delfinen är närmare släkt med en ko?</p>")])
 + "<h3>Att läsa ett släktträd</h3>"
 + "<p>I ett släktträd visar varje förgrening en gemensam förfader. Två arter som delar en förfader som levde nyligen är nära släkt. De som delar en förfader som levde för mycket längre sedan är mer avlägset släkt. Man ska läsa släktskapet utifrån förgreningarna, inte utifrån hur nära varandra namnen står. Linné grupperade efter likhet. Efter att man lärt sig mycket mer om evolution och DNA har man ändrat många grupper så att de speglar släktskap.</p>")

add("F3.2.2", "Vad är en art egentligen?", "3.2",
 "<p>I grundtexten lärde du dig att en art är individer som kan få fortplantningsdugliga ungar med varandra. Det är en bra utgångspunkt, men den har gränser. Naturen är ofta mer flytande än våra grupper.</p>"
 + row("<p><strong class='green'>Hybrider.</strong> Ibland kan individer av två närstående arter få ungar tillsammans. Hybrider mellan brunbjörn och isbjörn har till exempel hittats i naturen. Då blir gränsen mellan arterna oskarp. I vissa fall är hybriderna sterila, som mulåsnan, och då håller artbegreppet. I andra fall kan hybriderna själva få ungar.</p>"
       "<p><strong class='green'>Organismer utan parning.</strong> Bakterier förökar sig genom att dela sig. Ingen parning sker, så definitionen ”kan få ungar med varandra” går inte att tillämpa. För sådana organismer gruppar forskare i stället efter likhet i DNA och egenskaper.</p>"
       "<p><strong class='green'>Slutsats.</strong> Artbegreppet är ett redskap som människan har skapat för att ordna naturen. Det fungerar bra för många organismer men inte för alla, och forskare använder därför flera olika sätt att avgränsa arter.</p>",
       [begrepp([("Hybrid", "Avkomma till föräldrar av två olika arter."), ("Steril", "Oförmögen att få egna ungar."), ("Artbegrepp", "Definition av vad som räknas som en art.")]),
        box("tank", "Tänk efter", "<p>Varför fungerar definitionen ”kan få fortplantningsdugliga ungar med varandra” dåligt för bakterier?</p>")]))

add("F3.2.3", "Urval i praktiken: resistenta bakterier", "3.2",
 "<p>Naturligt urval är inte bara något som hände förr. Du kan se det ske i dag, till exempel när bakterier blir motståndskraftiga mot antibiotika.</p>"
 + row("<p>I en stor bakteriepopulation finns en liten variation: någon enstaka bakterie har av en slump en gen som gör den mindre känslig för ett visst antibiotikum. När man ger antibiotikan dör de flesta bakterierna, men de resistenta överlever. De delar sig och blir många. Efter en tid består populationen mest av resistenta bakterier. Det är <strong class='green'>naturligt urval</strong>: variation fanns redan, antibiotikan valde ut vilka som överlevde, och egenskapen ärvdes. Ingen bakterie ”lärde sig” att bli resistent.</p>"
       "<p>Eftersom bakterier delar sig snabbt kan det gå på bara några år. Därför är det viktigt att antibiotika används bara när det behövs och att man tar hela kuren. Då minskar risken att resistenta bakterier får ta över.</p>",
       [begrepp([("Resistens", "Förmåga att tåla ett ämne som annars dödar eller skadar."), ("Antibiotika", "Läkemedel som dödar eller hämmar bakterier. Verkar inte mot virus.")]),
        box("tank", "Tänk efter", "<p>Varför är det fel att säga att bakterien ”anpassade sig” genom att bestämma sig för att bli resistent?</p>")])
 + "<h3>Gränser för urvalet</h3>"
 + "<p>Urvalet kan bara arbeta med variation som redan finns. En art som saknar de gener som behövs kan inte ”välja” dem, och om miljön förändras för snabbt hinner arten inte anpassa sig. Därför är stor genetisk variation en tillgång, och därför hänger de två delarna av det här kapitlet ihop: mångfald på genetisk nivå är det som gör att arter kan anpassa sig.</p>")

UPG = [
 ("En kommun planterar en granplantage i stället för en blandskog. Efter tio år kommer en torr sommar följd av en granbarkborreinvasion. a) Förklara med försäkringseffekten varför en blandskog troligen klarar det bättre. b) Förklara varför det inte räcker att räkna antalet träd. c) Ge ett argument som talar för plantagen och väg det mot ditt svar på a).", 3),
 ("På en klippkust försvinner havsuttrarna. Efter en tid är tångskogen borta. a) Förklara kedjan av orsaker i flera led. b) Vad kallas fenomenet? c) Varför är det svårt att veta säkert att just uttern är orsaken? Föreslå hur man kan undersöka det.", 3),
 ("En liten population av en hotad art har ökat från 20 till 120 djur tack vare skydd. Forskare oroar sig ändå. a) Förklara vad en genetisk flaskhals innebär. b) Förklara varför populationen kan ha svårt att anpassa sig trots att den ökat. c) Föreslå en åtgärd och värdera nytta och nackdelar.", 3),
 ("Ett fiskebestånd har minskat i tio år, och regeringen funderar på ett fiskestopp. Fiskare säger att stoppet slår ut hela byar. a) Förklara hur överfiske kan leda till kollaps. b) Redovisa argument för och emot ett stopp. c) Ta ställning och motivera. Beskriv också vad du är osäker på.", 3),
 ("Biologen Alma påstår: ”Eftersom delfiner ser ut som hajar måste de vara nära släkt.” a) Förklara varför hon har fel. b) Beskriv vad konvergent evolution är och varför den uppstår. c) Hur skulle man kunna ta reda på hur nära släkt två arter är?", 3),
 ("Efter ett sjukhusutbrott ger man en patient ett antibiotikum. Först blir patienten bättre, men sedan blir hen sjuk igen, och nu hjälper inte medicinen. a) Förklara med variation, urval och ärftlighet vad som har hänt. b) Varför är det en dålig idé att sluta ta antibiotikan så fort man mår bättre? c) Varför hjälper antibiotika inte mot förkylning?", 3),
]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "a) På en blandskog har träden olika toleranser. Några klarar torka eller angrepp bättre, så en del av skogen överlever (försäkringseffekt). En granplantage har bara en art som alla drabbas av samma sak, så allt kan slås ut. b) Det beror på vilka arter och vilka egenskaper de har: många individer av samma art ger ingen försäkring. c) T.ex. snabb tillväxt och enkel avverkning ger vinst, men det är ett riskabelt val. Ett välutvecklat svar väger vinst mot risk.",
 "a) Utan uttrar ökar sjöborrarna, som äter tången. Tången minskar och tångskogen försvinner, och alla arter som lever där försvinner också. b) Trofisk kaskad. c) Det kan finnas andra orsaker samtidigt, t.ex. temperatur eller sjukdomar. Man kan jämföra områden med och utan utter och försöka hålla övrigt lika.",
 "a) En stor minskning i antalet individer leder till att mycket genetisk variation går förlorad. b) De djur som finns kan vara nära släkt och ha liten variation, så det finns färre gener som kan passa en ny miljö. Inavel kan också öka. c) T.ex. flytta in djur från en annan population. Nytta: ökad variation. Nackdelar: kostnad, risk att djuren inte passar lokalt, och de kan föra med sjukdomar.",
 "a) Om man fiskar mer än vad som hinner växa till minskar beståndet. När för få vuxna fiskar finns kvar föds för få ungar, och beståndet kan kollapsa. b) För: beståndet kan återhämta sig och ge mer fisk senare. Emot: jobb försvinner på kort sikt. c) Öppet svar. Ett välutvecklat svar väger flera argument, nämner vad man är osäker på (t.ex. hur snabbt beståndet återhämtar sig) och ger motiverat svar.",
 "a) De ser lika ut men är inte nära släkt: delfinen är ett däggdjur (andas luft, föder levande ungar), hajen en fisk. b) När olika grupper utvecklar liknande drag på grund av liknande miljö. Strömlinjeformad kropp är bra för snabb simning, så urvalet gynnar den hos båda. c) Jämföra DNA och se hur mycket det skiljer, och titta på fossil och uppbyggnad.",
 "a) Det fanns variation: några få bakterier var resistenta. Antibiotikan dödade de känsliga, så de resistenta överlevde och delade sig (urval). Resistensen ärvs, så nästa generation blev mest resistent. b) Om man slutar för tidigt överlever fler bakterier, och risken ökar att resistenta bakterier blir kvar. c) Förkylning orsakas av virus, och antibiotika verkar bara mot bakterier.",
]
RUTOR = [("Tänk efter (Mångfald som försäkring):", "En plantage har bara en art. Alla träd drabbas av samma torka eller samma skadeinsekt, så det finns ingen reserv."),
         ("Tänk efter (Nyckelarter och kedjereaktioner):", "Tång → sjöborre → havsutter. Utan uttrar blir det fler sjöborrar som betar ner tången, så tången minskar och kan försvinna."),
         ("Granska kritiskt (Hot som förstärker varandra):", "Det är en förenkling, för fjällräven påverkas också av jakt förr, tillgången på lämlar och klimatet. Man kan jämföra områden med och utan rödräv och mäta lämmeltillgång."),
         ("Tänk efter (Släktskap och likhet):", "Likheten beror på att strömlinjeformad kropp är en bra anpassning till vatten, inte på nära släktskap. Delfinen är ett däggdjur och därför närmare släkt med kon."),
         ("Tänk efter (Vad är en art egentligen?):", "Bakterier delar sig i stället för att para sig, så det finns ingen parning att tillämpa definitionen på."),
         ("Tänk efter (Urval i praktiken):", "Bakterien bestämmer ingenting. Variationen fanns redan, och antibiotikan gjorde att de resistenta överlevde och förökade sig.")]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar försäkringseffekten och genetisk variation, nyckelarter och trofiska kaskader, hot som förstärker varandra, släktskap och konvergent evolution, artbegreppets gränser och naturligt urval hos bakterier, och tränar det resonemang som krävs på högsta nivå.",
      SVAR, RUTOR,
      "Källstatus: Delvis kontrollerat eller allmän läroboksfakta, inte källkontrollerat i detta arbete: försäkringseffekten och funktionell redundans, havsutter–sjöborre–tång som trofisk kaskad, bävern som ekosystemingenjör, torskkollapsen vid Newfoundland (fiskestopp 1992), konvergent evolution hos delfin och haj, hybrider mellan brunbjörn och isbjörn, och antibiotikaresistens som naturligt urval. Det som sägs om fjällräven (flera samverkande orsaker, rödräven som konkurrent) bygger på samma källor som grundtexten. Kontrollera gärna exemplen mot aktuell litteratur innan de används i bedömning. Uppgifterna är konstruerade och liknar de svåraste uppgifterna i frisläppta nationella prov.")
