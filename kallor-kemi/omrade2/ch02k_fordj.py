# -*- coding: utf-8 -*-
"""Kemi område 2 Materia och partiklar – fördjupning (per moment)."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/kem/fig02k/'
NR = 2
SLUG = "kemi-materia"
TAB = "2+"
NAMN = "Materia och partiklar"
UNDER = "Varför beter sig ämnen som de gör – och hur säker är analysen?"
INTRO = ("Is flyter, men nästan allt annat sjunker när det blir fast. Varför är vatten ett undantag, och vad skulle hända med sjöar om det var tvärtom? "
         "Och om du får tillbaka 4,6 g salt av 5,0 g, är det bra eller dåligt? I den här fördjupningen resonerar du om vattnets ovanliga densitet, om vad som händer med energin när ämnen byter tillstånd, om löslighet och mättade lösningar, om utbyte och renhet, om hur man separerar ämnen med nästan samma kokpunkt och om vad en analys kan och inte kan säga. "
         "Namn och mätvärden i uppgifterna är påhittade exempel.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Värdera hur säker en slutsats är: kopplat till mätfel, renhet och metodens gränser.", "Var nyanserad: visa vad partikelmodellen kan förklara, vad den inte kan och hur den prövas.",
       "Planera en undersökning och förbättra den med ledning av felkällor."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först grundtexten i kapitel 2. Fördjupningen bygger på begreppen densitet, partikelmodellen, tillståndsförändringar, lösning, filtrering, destillation, kromatografi och fällning."
D = {"2.1": "Ämnen, blandningar och partikelmodellen", "2.2": "Separations- och analysmetoder"}

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F2.1.1", "Vattnets ovanliga densitet", "2.1",
 "<p>De flesta ämnen blir tätare när de blir fasta: partiklarna kommer närmare varandra, så fast ämne sjunker i sin egen vätska. Vatten gör tvärtom. Is flyter. Det är ovanligt, och det har stor betydelse för liv i sjöar.</p>"
 + fig(FIG+"f_vatten4.png", "<b>Bild F2.1</b> Vattnets densitet runt 4 °C (schematisk). Vatten är tätast vid 4 °C. Is har lägre densitet än flytande vatten.", "76%")
 + row("<p>Vatten har sin högsta densitet vid <strong class='green'>4 °C</strong>, ca 1,00 g/cm³. Kallare vatten blir <em>mindre</em> tätt igen. Vid 20 °C är densiteten ca 0,998 g/cm³, och is har ca 0,92 g/cm³. Orsaken är att vattenmolekylerna i is ordnar sig i ett sexkantigt mönster som tar mer plats än när de ligger oordnat i flytande vatten. Partiklarna ligger alltså glesare i is än i flytande vatten, och isen har lägre densitet.</p>"
       "<p>Följden: när en sjö kyls på hösten sjunker det kalla ytvattnet tills allt vatten är 4 °C. Kyls ytan ytterligare blir det mindre tätt och ligger kvar överst, och där bildas isen. Isen flyter på ytan och isolerar vattnet under. Djupa sjöar fryser därför sällan till botten, och fisk och andra djur kan överleva i vattnet under isen.</p>",
       [begrepp([("Sexkantigt mönster", "Så ordnar sig vattenmolekylerna i is."), ("Densitetsmaximum", "Temperaturen där ett ämne är tätast, för vatten 4 °C.")]),
        box("tank", "Tänk efter", "<p>Anta att is hade haft högre densitet än vatten. Vad skulle hända med en sjö under en lång, kall period? Förklara i flera led.</p>")])
 + "<h3>Vad säger partikelmodellen?</h3>"
 + "<p>Med den enkla modellen ”fast ämne är tätare än vätska” får man fel för vatten. Det visar en gräns för modellen: den tar inte hänsyn till hur krafterna mellan partiklarna ordnar dem. När du ska förklara isens låga densitet behöver modellen kompletteras med att partiklarna i is binds i ett glest, ordnat mönster. Det är ett bra exempel på hur en modell kan vara användbar och ändå behöva byggas ut.</p>")

add("F2.1.2", "Energi och tillståndsförändringar", "2.1",
 "<p>I grundtexten lärde du dig att temperaturen ligger still under smältning och kokning. Här tittar vi närmare på vad som sker, och vad kurvan för uppvärmning visar.</p>"
 + fig(FIG+"f_uppv.png", "<b>Bild F2.2</b> Uppvärmning av is som tillförs värme jämnt (påhittade värden, schematiskt): temperaturen stiger, ligger still vid smältning, stiger, ligger still vid kokning och stiger sedan igen.", "86%")
 + row("<p>Kurvan visar fem delar. I <b>A</b> värms isen och partiklarna vibrerar kraftigare. I <b>B</b> smälter isen: temperaturen är 0 °C hela tiden, trots att värme tillförs. I <b>C</b> värms vattnet. I <b>D</b> kokar vattnet vid 100 °C. I <b>E</b> värms vattenångan.</p>"
       "<p>Förklaring: temperaturen visar hur snabbt partiklarna i genomsnitt rör sig. Under smältningen går värmen åt att bryta loss partiklarna från mönstret, inte att få dem att röra sig snabbare, så temperaturen ändras inte. Det krävs mycket mer energi för att förånga vatten än för att smälta is, eftersom partiklarna då ska skiljas helt från varandra. På kurvan syns det som att platån D är längre än platån B.</p>",
       [begrepp([("Platå", "Del av kurvan där temperaturen ligger still."), ("Tillförd energi", "Värme som ämnet tar upp.")]),
        box("tank", "Tänk efter", "<p>Du kyler vattenånga. Beskriv hur kylkurvan ser ut och förklara med partikelmodellen vad som händer med energin under kondensationen.</p>")])
 + "<h3>Rent ämne eller blandning?</h3>"
 + "<p>Ett rent ämne smälter och kokar vid en bestämd temperatur, så kurvan har tydliga platåer. En blandning smälter och kokar över ett temperaturområde, så kurvan lutar där i stället. Därför kan en kurva användas för att avgöra om ett prov är rent. Skärpan på platån säger något om renheten, men en mätning bevisar inget: en annan förorening kan ge nästan samma värde.</p>")

add("F2.1.3", "Löslighet och mättade lösningar", "2.1",
 "<p>Löslighet kan uttryckas i gram löst ämne per 100 ml lösningsmedel. Det ger dig ett sätt att räkna på lösningar.</p>"
 + fig(FIG+"f_losl.png", "<b>Bild F2.3</b> Schematiskt: löslighet hos ett fast ämne ökar oftast med temperaturen, medan en gas blir mindre löslig. Kurvorna är inte uppmätta värden.", "76%")
 + row("<p>Salt (natriumklorid) löser sig upp till ungefär 35,7 g per 100 ml vatten vid 20 °C, och socker ungefär 190 g per 100 ml vid 25 °C. Löser du 20 g salt i 100 ml vatten vid 20 °C löser sig allt, och lösningen är <b>omättad</b>. Löser du 50 g går bara 35,7 g att lösa. Resten, 50 − 35,7 = 14,3 g, ligger kvar som fast ämne och lösningen är <b>mättad</b>. Värmer du lösningen kan du ofta lösa mer. Löser du i varmt vatten och sedan låter det svalna kan ämnet som inte längre får plats i lösning falla ut som kristaller.</p>"
       "<p>De flesta fasta ämnen löser sig bättre i varmt vatten, men inte alla lika mycket. För gaser är det tvärtom: de löser sig sämre i varmt vatten. Det är en anledning till att kokt och avkylt vatten smakar ”platt”: gaser som lösts i vattnet har gått bort.</p>",
       [begrepp([("Omättad lösning", "Det går att lösa mer."), ("Mättad lösning", "Det går inte att lösa mer vid den temperaturen."), ("Utfällning av kristaller", "Löst ämne som blir fast när det inte längre får plats i lösningen.")]),
        box("tank", "Tänk efter", "<p>Du löser socker i hett te tills det inte går mer, och låter teet svalna. Vad kan hända? Förklara med löslighet.</p>")])
 + "<h3>Mättad lösning och partiklar</h3>"
 + "<p>Med partikelmodellen: i en lösning blandas partiklarna från det lösta ämnet med vattnets partiklar. Det finns en gräns för hur många lösta partiklar vattnet kan ta emot och hålla kvar. När gränsen nås stannar fler partiklar i den fasta fasen. Samtidigt lämnar partiklar fortfarande den fasta ytan och andra återvänder dit, så det är i jämvikt: lika många lämnar som kommer tillbaka. Det är en förklaringsmodell, inte något som syns direkt.</p>")

add("F2.2.1", "Renhet och utbyte", "2.2",
 "<p>I labben 2.2 vägde du sand och salt före och efter separationen. Här tittar vi på vad skillnaden i massa säger.</p>"
 + row("<p>Kemister räknar <strong class='green'>utbyte</strong>: hur stor andel av det som fanns från början som du fick tillbaka.</p>"
       "<p style='text-align:center'><b>utbyte (%) = erhållen massa / ursprunglig massa × 100</b></p>"
       "<p><b>Exempel (påhittat):</b> Du började med 5,0 g salt och fick 4,6 g salt. Utbytet är 4,6 / 5,0 × 100 = 92 %. De sista 8 procenten kan ha stannat kvar på filtret, bägaren eller skålen, eller sprutat ut vid upphettningen. Ett utbyte över 100 % betyder att något är fel, till exempel att provet är fuktigt eller förorenat.</p>",
       [begrepp([("Utbyte", "Andelen av ursprunglig mängd som erhålls."), ("Renhet", "Hur stor del av ett prov som är det önskade ämnet.")]),
        box("tank", "Tänk efter", "<p>Du får 5,3 g salt av 5,0 g. Är det möjligt att du fick mer än du hade? Vad kan förklara det?</p>")])
 + "<h3>Vad påverkar utbytet och renheten?</h3>"
 + "<p>Utbytet minskar av förluster: material som fastnar på glas och filter, vätska som spills, partiklar som går genom filtret. Renheten påverkas av det som kommer med: sand som är kvar i saltet om filtret läcker, eller fukt om saltet inte torkats. Man kan förbättra båda genom att skölja filtret med lite vatten, torka noga och upprepa mätningen. Ofta väljer man mellan hög renhet och högt utbyte. Det är en avvägning som beror på vad ämnet ska användas till.</p>"
 + "<p>Massan bevaras vid blandning och separation, så summan av det du fick tillbaka och det du förlorade är lika med det du började med. Om siffrorna inte går ihop har något annat än kemin hänt, vilket gör massan till en bra kontroll.</p>")

add("F2.2.2", "Fraktionerad destillation och Rf-värde", "2.2",
 "<p>Destillation fungerar bäst när ämnena har mycket olika kokpunkter, som vatten och salt. Vad händer när kokpunkterna ligger nära varandra, och hur kan man mäta hur långt ett ämne vandrar vid kromatografi?</p>"
 + row("<p>Etanol kokar vid 78 °C och vatten vid 100 °C. Ångan från en kokande blandning innehåller mest etanol, men också lite vatten. En enkel destillation ger därför ett destillat som är rikare på etanol men inte rent. Vid <strong class='green'>fraktionerad destillation</strong> leds ångan genom en kolonn där den kondenserar och förångas om och om igen. Varje gång blir ångan lite rikare på det ämne som har lägst kokpunkt, och längst upp kommer nästan ren etanol ut. Samma princip används för att dela upp blandningar av många vätskor med olika kokpunkter.</p>"
       "<p>Termometern visar vad som händer: så länge etanol destillerar ligger temperaturen nära 78 °C. När etanolen tar slut stiger den mot 100 °C. Det går att byta uppsamlingskärl vid temperaturhoppet och få olika fraktioner.</p>",
       [begrepp([("Fraktionerad destillation", "Destillation där ångan upprepat kondenseras i en kolonn för bättre separation."), ("Fraktion", "En del av blandningen som samlats vid ett visst temperaturintervall.")]),
        box("tank", "Tänk efter", "<p>Varför är det svårare att separera två vätskor med kokpunkterna 78 °C och 82 °C än med 78 °C och 100 °C? Förklara med ångans sammansättning.</p>")])
 + "<h3>Rf-värde i kromatografi</h3>"
 + fig(FIG+"f_rf.png", "<b>Bild F2.4</b> Ett kromatogram. Rf-värdet för varje färg är sträckan färgen vandrat delat med sträckan lösningsmedlet vandrat (påhittade mått).", "66%")
 + "<p>Vid papperskromatografi kan du mäta hur långt varje ämne vandrat. <strong class='green'>Rf-värdet</strong> är sträckan ämnet vandrat delat med sträckan lösningsmedlet vandrat, mätt från startlinjen: Rf = a / b. Ett Rf-värde ligger mellan 0 och 1. Om lösningsmedlet vandrat 8,0 cm och en färg 3,2 cm blir Rf = 3,2 / 8,0 = 0,40. Under lika förhållanden har ett ämne alltid samma Rf-värde, så man kan jämföra med kända ämnen och identifiera dem. Det kräver samma papper, samma lösningsmedel och att mätningen görs vid samma förhållanden.</p>")

add("F2.2.3", "Att planera en analys och dess gränser", "2.2",
 "<p>Du har ett okänt prov och ska ta reda på vad det innehåller. Hur planerar du, och hur säker blir slutsatsen?</p>"
 + row("<p>En bra plan har tydlig fråga, flera <em>oberoende</em> metoder, jämförelser med kända ämnen och upprepade mätningar. Exempel: ett vitt pulver. Du mäter löslighet i vatten, smältpunkt, om det bildar fällning med en känd lösning och jämför med salt och socker som du vet vad de är. Om alla resultat stämmer med ett ämne är slutsatsen stark. Om bara ett stämmer är den svag.</p>"
       "<p>Ett prov kan vara en blandning, och en metod kan störas av andra ämnen. En <strong class='green'>kontrollprov</strong> med ett känt ämne visar om metoden fungerar och om utrustningen är rätt. Ett <strong class='green'>blankprov</strong> utan det du letar efter visar om något annat ger utslag.</p>",
       [begrepp([("Kontrollprov", "Prov med känt innehåll som visar att metoden fungerar."), ("Blankprov", "Prov utan det du letar efter, för att se om något annat ger utslag.")]),
        box("tank", "Tänk efter", "<p>Ett test visar ”ingen fällning” i ett vattenprov. Betyder det att ämnet inte finns i provet? Ge två skäl till att svaret kan vara ett nej fastän ämnet finns.</p>")])
 + "<h3>Gränser</h3>"
 + "<p>En analys säger bara något om det prov du tagit. Ett vattenprov från en plats och en dag säger inte hur det är i hela sjön hela året. Dessutom har varje metod en gräns för hur lite av ett ämne den klarar att upptäcka. Hittar du inget kan det finnas så lite att metoden inte ser det. Därför ska en slutsats formuleras med försiktighet: ”Vi fann inget fosfat med den här metoden” är något annat än ”det finns inget fosfat”. Redovisa också hur provet togs, hur många prov som togs och vilka felkällor som finns.</p>")

UPG = [
 ("En djup insjö i norra Sverige är kall på vintern. En del tror att vattnet fryser till botten på vintern. a) Förklara med vattnets densitet varför bottenvattnet i en djup sjö kan vara kvar som flytande vatten. b) Vad händer med isen och vattnet längre ned? c) Vad skulle hända om is hade högre densitet än vatten?", 3),
 ("Elin värmer en isbit och mäter temperaturen varje minut. Hon ser att temperaturen ligger still vid 0 °C en stund och sedan stiger. a) Förklara varför temperaturen ligger still, med partikelmodellen. b) Förklara varför platån vid kokning blir längre än vid smältning om värmen tillförs jämnt. c) Hur skulle kurvan se ut om provet var saltvatten i stället för rent vatten?", 3),
 ("Du löser 50 g salt i 100 ml vatten vid 20 °C. Saltets löslighet är ungefär 35,7 g per 100 ml vid 20 °C. a) Räkna ut hur mycket som löser sig och hur mycket som blir kvar. b) Är lösningen mättad? Motivera. c) En kamrat säger att allt kommer att lösa sig om man rör om länge. Värdera påståendet.", 3),
 ("En grupp hade 5,0 g salt före separationen och fick 4,1 g efter. a) Räkna ut utbytet. b) Ge tre tänkbara orsaker till att utbytet är under 100 %. c) En annan grupp fick 5,4 g. Vad kan det betyda, och hur kan gruppen kontrollera det?", 3),
 ("Två vätskor, A och B, har kokpunkterna 78 °C och 82 °C. a) Förklara varför en enkel destillation inte ger rena vätskor. b) Beskriv hur fraktionerad destillation förbättrar separationen. c) Hur kan temperaturen på termometern användas för att avgöra när du ska byta uppsamlingskärl?", 3),
 ("Du ska ta reda på vad ett okänt, vitt pulver är. Kandidater: bordssalt, socker och bikarbonat. a) Planera en undersökning med minst tre oberoende metoder och förklara varför du behöver mer än en. b) Beskriv vilka kontrollprov du använder. c) Förklara vad du kan och inte kan säga om du bara hittar skillnader mot salt och socker.", 3),
]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "a) Vatten är tätast vid 4 °C. Ytvattnet som kyls blir mindre tätt under 4 °C och ligger kvar överst, där det fryser. Det tyngre vattnet vid ca 4 °C ligger kvar nedanför. b) Isen flyter på ytan och isolerar. Vattnet under är ungefär 4 °C och fryser inte. c) Is skulle sjunka och frysa upp sjön underifrån. Sjön kunde frysa helt och djurlivet skulle ha svårt att klara vintern.",
 "a) Värmen går åt att bryta loss partiklarna från mönstret, inte att få dem att röra sig snabbare. Temperaturen, som mäter rörelsen, ändras då inte. b) Vid förångning ska partiklarna skiljas från varandra helt, vilket kräver mer energi än att bryta mönstret vid smältning. Därför tar det längre tid. c) Saltvatten är en blandning, så det smälter och kokar över ett temperaturområde och har inte en skarp platå. Kokpunkten blir också något högre än 100 °C.",
 "a) 35,7 g löser sig, 50 − 35,7 = 14,3 g blir kvar. b) Ja, mättad: det går inte att lösa mer vid 20 °C och överskottet ligger kvar. c) Påståendet stämmer inte: omrörning gör att det löser sig fortare, men inte mer. Löslighetsgränsen ändras bara med temperaturen eller lösningsmedlet.",
 "a) 4,1 / 5,0 × 100 = 82 %. b) T.ex. salt som fastnat på filter, bägare och skål, spill, och salt som sprutat vid upphettningen. c) Mer än 100 % är orimligt och tyder på fukt eller sand i saltet. Kontrollera genom att torka längre, väga om och göra om försöket.",
 "a) Ångan innehåller båda ämnena, med mer av det som kokar vid lägst temperatur. Kokpunkterna ligger nära varandra så ångan blir bara lite rikare. b) Kolonnen låter ångan kondensera och förångas många gånger. Varje gång blir ångan rikare på det lågkokande ämnet och till slut kommer nästan rent A ut. c) Vid ca 78 °C kommer ämnet med lägre kokpunkt, och när temperaturen stiger mot 82 °C byter man kärl för nästa fraktion.",
 "a) T.ex. löslighet i vatten, smältpunkt, om det bildar fällning eller skummar med syra, och densitet. Man behöver flera eftersom flera ämnen kan ha liknande värde på en egenskap. b) Prov av känt salt, socker och bikarbonat som testas på samma sätt, och ev. blankprov med bara vatten. c) Att provet inte är de testade ämnena, men inte vad det är. Det kan vara ett ämne du inte testat.",
]
RUTOR = [("Tänk efter (Vattnets ovanliga densitet):", "Isen skulle sjunka. Sjön skulle kunna frysa underifrån och upp, och livet i den skulle ha svårt att överleva vintern."),
         ("Tänk efter (Energi och tillståndsförändringar):", "Kurvan har en platå vid ca 100 °C medan ångan kondenserar. Energin lämnar ämnet när partiklarna går från gas till vätska och binds till varandra, och därför ändras inte temperaturen."),
         ("Tänk efter (Löslighet):", "Teet svalnar och lösligheten minskar. Överskottet socker kan falla ut som kristaller."),
         ("Tänk efter (Renhet och utbyte):", "Nej, man kan inte få mer än man hade. Provet kan vara fuktigt eller förorenat (t.ex. med sand eller kvarvarande vatten)."),
         ("Tänk efter (Fraktionerad destillation):", "Vid nära kokpunkter innehåller ångan båda ämnena i nästan samma mängd, så en enda destillation ger lite separation."),
         ("Tänk efter (Planera en analys):", "Nej. Ämnet kan finnas i så liten mängd att metoden inte upptäcker det, eller så störs testet av något annat i provet.")]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar vattnets densitetsmaximum, energi vid tillståndsförändringar, löslighet och mättade lösningar, utbyte och renhet, fraktionerad destillation och Rf-värde samt hur man planerar en analys och dess gränser, och tränar det resonemang som krävs på högsta nivå.",
      SVAR, RUTOR,
      "Källstatus: vattnets densitetsmaximum vid 4 °C och att is flyter, saltets (ca 35,7 g/100 ml vid 20 °C) och sockrets (ca 190 g/100 ml vid 25 °C) löslighet, att fasta ämnens löslighet i regel ökar och gasers minskar med temperaturen, etanolens och vattnets kokpunkter, att temperaturen ligger still under tillståndsförändringar samt grundprinciperna för destillation och kromatografi är kontrollerade mot öppna källor (se källförteckningen). Allmän läroboksfakta, inte källkontrollerad i detta arbete: fraktionerad destillation i kolonn, Rf-värdets definition, utbytesberäkning, blank- och kontrollprov, att det krävs mer energi att förånga än att smälta, jämviktsbilden för mättad lösning och att kokt vatten innehåller mindre löst gas. Alla mätvärden är påhittade.")
