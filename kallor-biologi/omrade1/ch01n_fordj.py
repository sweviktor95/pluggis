# -*- coding: utf-8 -*-
"""Område 1 Biologi som vetenskap – fördjupning (nya ramverket, per moment)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/bio/fig01n/'
NR = 1
SLUG = "vetenskap"
TAB = "1+"
NAMN = "Biologi som vetenskap"
UNDER = "Hur vet vi att vi inte lurar oss själva?"
INTRO = ("Den största utmaningen för en forskare är inte att hitta svar. Det är att inte lura sig själv. Vi ser gärna det vi vill se, och slumpen kan få nästan vad som helst att se ut som ett samband. "
         "I den här fördjupningen lär du dig hur forskare planerar rättvisa undersökningar, hur man värderar hur säkert ett resultat är, var vetenskapens gränser går, varför nya idéer ibland möts av motstånd och hur du väger källor som säger emot varandra.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Väg för- och nackdelar, och se frågan från flera perspektiv.", "Var nyanserad: visa vad som är osäkert och vad man mer skulle behöva veta.",
       "Ta ställning och motivera med naturvetenskapliga argument."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
INTRO = INTRO + " Namn, klasser, produkter och mätvärden i kapitlet är påhittade exempel, om inget annat står. Forskarna och undersökningarna Pasteur, Semmelweis, Marshall och Warren samt Carlson är verkliga."
FUNDERA = "Läs först grundtexten i kapitel 1. Fördjupningen bygger på begreppen hypotes, variabel, kontrollgrupp, felkälla, belägg, trovärdig och relevant."
D = {"1.1": "Undersöka systematiskt", "1.2": "Modeller, källor och argument"}
def cards4_html():
    items = [("Oberoende", "Har källan undersökt själv eller bara hört av andra? Går uppgifterna att följa tillbaka?"), ("Tendens", "Vem tjänar på budskapet? Vem betalade för undersökningen?"),
             ("Samsyn", "Säger andra, oberoende källor samma sak? Vad säger sammanställningar?"), ("Aktualitet", "Är det nytt nog? Har nyare studier ändrat bilden?")]
    return '<div class="cards" style="grid-template-columns:repeat(4,1fr)">' + "".join(f'<div class="card"><b class="h">{h}</b>{t}</div>' for h, t in items) + '</div>'

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F1.1.1", "Planera ett eget försök", "1.1",
 "<p>Föreställ dig att ett företag påstår att deras nya tablett gör att förkylningar går över snabbare. Hur skulle man testa det? Det låter enkelt: ge tabletten till några förkylda personer och se om de blir friska. Men de flesta förkylningar går över av sig själva inom en vecka. Hur vet man då att det var tabletten som hjälpte? En bra plan svarar på det i förväg.</p>"
 + fig(FIG+"f_rct.png", "En randomiserad, dubbelblind och placebokontrollerad studie: en av de mest pålitliga sorternas medicinska försök.", "82%")
 + "<h3>Så motiverar du valen i din plan</h3>"
 + row("<p><strong>Variabler.</strong> Välj en oberoende variabel och motivera varför just den. Välj en beroende variabel som verkligen mäter det du vill veta (giltighet). Lista vad som måste hållas lika.</p>"
       "<p><strong>Kontrollgrupp och placebo.</strong> Kontrollgruppen får inte behandlingen. Får den en likadan tablett utan verksamt ämne, kan förväntningar inte förklara skillnaden.</p>"
       "<p><strong>Randomisering.</strong> Slumpen bestämmer vem som hamnar i vilken grupp. Annars kan forskaren omedvetet lägga de friskaste i den ena gruppen.</p>"
       "<p><strong>Blindning.</strong> Om varken deltagare eller forskare vet vem som fått vad är studien dubbelblind. Då blir det svårare att påverka resultatet, även omedvetet.</p>"
       "<p><strong>Antal upprepningar.</strong> Med fem personer i varje grupp kan slumpen avgöra resultatet. Med hundratals blir slumpens betydelse liten. I ett skolförsök kan du inte ha hundratals, så du måste vara öppen med vad det betyder för hur säker slutsatsen blir.</p>",
   [begrepp([("Randomisering", "Slumpmässig fördelning till grupper."), ("Dubbelblind", "Varken deltagare eller forskare vet vem som fått vad."), ("Stickprov", "De individer man undersöker, som ska representera en större grupp.")]),
    box("tank", "Resonera om störningar", "<p>Du ska testa om du minns fler ord med musik. Vad kan störa? Hur kan du planera så att varje störning minskar?</p>")])
 + table(["Del av planen", "Fråga att svara på", "Motivera"], [["Frågeställning", "Går den att besvara med mätning?", "Skriv vad som ska mätas."], ["Variabler", "Vad ändras, mäts och hålls lika?", "Varför just dessa?"], ["Mätmetod", "Hur mäter jag, med vilken noggrannhet?", "Varför är metoden giltig?"],
        ["Upprepning", "Hur många försök och deltagare?", "Hur påverkar antalet slumpen?"], ["Störningar", "Vad kan göra resultatet fel?", "Hur förebygger jag det?"]], "tbl"))

add("F1.1.2", "Tolka data och redovisa osäkerhet", "1.1",
 "<p>Ett diagram visar inte bara svaret. Det visar också hur osäkert svaret är. <span class='fake'>Påhittat exempel</span> En grupp undersökte hur temperaturen påverkar gasbildningen hos jäst. De gjorde tre försök vid varje temperatur och mätte hur mycket en ballong växte.</p>"
 + table(["Temperatur", "Försök 1", "Försök 2", "Försök 3", "Medelvärde"], [["10 °C", "13 cm", "12 cm", "14 cm", "13 cm"], ["25 °C", "22 cm", "24 cm", "23 cm", "23 cm"], ["40 °C", "31 cm", "18 cm", "30 cm", "?"]], "tbl num")
 + "<h3>Det avvikande värdet</h3>"
 + roww("<p>Vid 40 °C avviker ett värde mycket från de andra (18 cm). Om man räknar med det blir medelvärdet 26 cm. Utan det blir det 30,5 cm. Vad ska man göra? Man ska inte stryka ett värde bara för att det passar illa. Man frågar först: Finns det en rimlig förklaring, till exempel att ballongen satt löst? Om ja, redovisa värdet, förklara varför det kan vara fel och visa resultatet med och utan det. Om nej, gör fler försök.</p>"
        "<h3>Osäkerhet</h3><p>Ju mer mätvärdena skiljer sig inom en grupp, desto osäkrare är medelvärdet. Man kan redovisa osäkerheten genom att visa lägsta och högsta värde. Skillnaden mellan 10 och 25 °C är stor jämfört med spridningen. Skillnaden mellan 25 och 40 °C är mindre tydlig, eftersom ett av värdena avviker.</p>",
        [begrepp([("Avvikande värde", "Ett värde som ligger långt från de andra."), ("Spridning", "Hur mycket mätvärdena skiljer sig åt."), ("Osäkerhet", "Hur säkert ett resultat är.")]),
         box("klimat", "Digitala verktyg", "<p>I ett kalkylblad kan du räkna medelvärde med och utan ett värde, och rita diagram med både medelvärden och enskilda mätpunkter.</p>")])
 + row(box("fundera", "Fundera", "<p>Vilken slutsats kan du dra om temperaturens påverkan, och vilken kan du inte dra? Vad skulle du göra för att bli säkrare?</p>"), None))

add("F1.1.3", "Hur säker är slutsatsen?", "1.1",
 "<p>Många nyheter bygger på undersökningar där forskare har jämfört grupper av människor, till exempel ”personer som äter mycket fisk lever längre”. Sådana <strong class='green'>observationsstudier</strong> är viktiga, men grupperna kan skilja sig åt på många andra sätt än det man undersöker.</p>"
 + "<h3>Störfaktorer</h3>"
 + roww("<p>En <strong class='green'>störfaktor</strong> är något som påverkar både det man tror är orsaken och det man mäter. Kanske äter personer som äter mycket fisk också mer grönsaker, röker mindre och har högre inkomst. Då kan det vara de sakerna, och inte fisken, som gör att de lever längre.</p>"
        "<p>Forskare försöker räkna bort kända störfaktorer, men det kan alltid finnas sådana som ingen har tänkt på. Därför är kontrollerade experiment med slumpad fördelning det säkraste sättet att visa orsak.</p>",
        [fig(FIG+"f_storfaktor.png", "En störfaktor kan skapa ett samband mellan två saker som inte påverkar varandra.")])
 + "<h3>Slumpen lurar</h3>"
 + row("<p>Om du singlar slant tio gånger är det inte konstigt att få sju krona. Det betyder inte att myntet är fusk. Samma sak gäller i biologiska undersökningar: små skillnader mellan små grupper kan bero på ren slump. Ju större stickprov och ju större skillnad, desto säkrare kan man vara på att skillnaden är verklig.</p>"
       "<p>När du värderar ett försök, resonera om vilka felkällor som är störst, hur mycket de kan ha påverkat slutsatsen och hur du skulle förbättra försöket. Sluta med att säga hur säker slutsatsen är: ”Resultatet tyder på …, men eftersom … kan vi inte vara säkra på …”.</p>",
   [begrepp([("Observationsstudie", "Man jämför grupper utan att själv ändra något."), ("Störfaktor", "En faktor som påverkar både den misstänkta orsaken och resultatet.")]),
    box("tank", "Tänk efter", "<p>”Barn som har många böcker hemma får bättre betyg.” Ge två möjliga störfaktorer.</p>")]))

add("F1.2.1", "Vetenskapens gränser", "1.2",
 "<p>Naturvetenskapen är kraftfull, men den svarar bara på vissa sorters frågor: frågor som går att pröva med belägg. Frågan ”Hur påverkar en gödning tomatplantors skörd?” är en sådan. ”Är det rätt att äta kött?” är en annan sorts fråga. Biologin kan ge fakta om hur djur påverkas och hur klimatet påverkas, men vad som är rätt beror också på värderingar. Därför behövs både fakta och etiska argument.</p>"
 + "<h3>Ett påstående måste kunna visas vara fel</h3>"
 + roww("<p>Ett vetenskapligt påstående måste kunna visa sig vara fel. Om alla tänkbara resultat passar med påståendet kan man aldrig pröva det. ”Hälsokosten hjälper om du tror på den, och om den inte hjälper tror du inte tillräckligt” går aldrig att motbevisa. Då har påståendet lämnat vetenskapen.</p>"
        "<p>Det betyder inte att alla icke-vetenskapliga svar är värdelösa. Konst, etik, religion och filosofi svarar på andra frågor än naturvetenskapen. Problemet uppstår när något gör anspråk på att vara vetenskap utan att kunna prövas.</p>",
        [box("fundera", "Resonera", "<p>Vilka frågor om samma sak, till exempel jakt på varg, kan naturvetenskapen svara på, och vilka kan den inte avgöra?</p>")])
 + table(["Påstående", "Går det att pröva?", "Hur skulle du pröva det?"],
         [["Vi sover bättre i ett kallt rum.", "Ja", "Mät sömnlängd eller antal uppvaknanden vid olika temperaturer."], ["Naturen mår bäst när människan inte rör den.", "Delvis", "Måste först definiera ”mår bäst” (t.ex. antal arter) och därefter mäta. Värderingen ligger i orden."],
          ["Stjärntecknet styr din personlighet.", "Ja, och prövat", "Dubbelblint test (Carlson, Nature 1985): astrologerna klarade inte mer än slumpen."]], "tbl"))

add("F1.2.2", "Varför möts nya idéer av motstånd?", "1.2",
 "<p>I grundtexten mötte du Pasteur, Semmelweis samt Marshall och Warren. Nu ska vi jämföra dem och fråga varför det ibland tar så lång tid att ändra en förklaring.</p>"
 + table(["", "Pasteur (1861)", "Semmelweis (1847)", "Marshall och Warren (1982)"],
         [["Gammal förklaring", "Små organismer kan uppstå av sig själva.", "Barnsängsfeber har många orsaker, ingen tänker på händerna.", "Magsår beror på stress och livsstil. Bakterier kan inte leva i magsyran."],
          ["Belägg", "Buljong i svanhalskolv förblev klar, i rak kolv blev den grumlig.", "Dödligheten på läkarkliniken föll från 11,4 % till 1,3 % efter handtvätt.", "Bakterie i magsäcken. Marshalls självförsök 1984. Antibiotika botar."],
          ["Motstånd", "Fick mothugg men kontrollerade försök övertygade.", "Hånades. Saknade förklaring till hur. Fick inte förlängt kontrakt.", "Marshall möttes av stark skepsis."],
          ["Vad övertygade?", "Ett enkelt och upprepbart försök.", "Bakterieläran växte fram årtionden senare.", "Upprepade studier och en behandling som fungerade. Nobelpriset 2005."]], "tbl")
 + "<h3>Mönstret</h3>"
 + roww("<p>I alla tre fall passade resultatet inte den förklaring som alla trodde på. Det är inte konstigt att forskare håller fast vid en modell som fungerat länge. En modell är en förenkling som har varit användbar, och en enstaka avvikelse kan bero på ett fel. Motståndet kan därför vara rimligt i början. Men när belägg samlas, från olika forskare och olika metoder, ändras bilden.</p>"
        "<p>Det betyder inte att alla nya idéer har rätt. Marshall och Warren fick rätt för att de hade belägg som kunde granskas och upprepas, inte för att de var envisa.</p>"
        "<h3>Modeller har begränsningar</h3><p>Ett exempel: bakterien <em>Helicobacter pylori</em> orsakar magsår, men långt ifrån alla som är smittade får magsår. Modellen ”bakterie orsakar magsår” är användbar, men inte hela förklaringen. Fler faktorer spelar in.</p>",
        [box("visste", "Lärdom", "<p>En bra modell förklarar vad man ser, förutsäger nya saker och kan prövas. Den behöver inte vara hela sanningen för att vara användbar.</p>"),
         box("varning", "Etik", "<p>Marshalls självförsök var riskabelt. Forskning på människor måste granskas av en etikprövningsmyndighet.</p>")]))

add("F1.2.3", "Väga källor och granska påståenden", "1.2",
 "<p>Ibland säger trovärdiga källor emot varandra. Då räcker det inte att fråga om en källa är trovärdig. Man måste väga dem mot varandra: Vilken bygger på flest och bäst undersökningar? Vem har gjort studien, och vem har betalat för den? Finns det en oberoende upprepning?</p>"
 + cards4_html()
 + "<h3>Läs diagram och statistik med kritiskt öga</h3>"
 + roww("<p><strong>Korrelation är inte orsak.</strong> När glassförsäljningen ökar, ökar också antalet drunkningsolyckor. Båda beror på en tredje sak: värmen.</p>"
        "<p><strong>Avkortad axel.</strong> Om y-axeln börjar på 90 i stället för 0 ser en liten skillnad enorm ut.</p>"
        "<p><strong>Relativ ökning.</strong> ”Risken dubblas!” kan betyda att den går från 1 på 100 000 till 2 på 100 000. Fråga alltid efter hur stor risken var från början.</p>"
        "<p><strong>Sponsring och tendens.</strong> En studie betald av ett företag är inte automatiskt fel, men man bör se om den är oberoende granskad och om andra har fått samma resultat.</p>",
        [fig(FIG+"v_glass.png", "Två kurvor som följer varandra utan att den ena orsakar den andra.")])
 + "<h3>Bemöt motargument</h3>"
 + row("<p>Ett starkt argument tar motargumentet på allvar. Skriv påstående, belägg, det starkaste motargumentet och ett svar som visar varför beläggen ändå väger tyngre, eller var du kan hålla med. Avsluta med en slutsats som säger hur säker du är.</p>",
       [box("tank", "Tänk efter", "<p>En tidning skriver: ”Studie: Kaffe förlänger livet!” Vilka tre frågor ställer du innan du tror på det?</p>")]))

UPG = [
 ("Ett företag påstår att deras sportdryck ger bättre kondition. Planera en undersökning som kan pröva påståendet. Beskriv hur du använder kontrollgrupp, placebo, randomisering och blindning, och förklara varför varje del behövs.", 3),
 ("Semmelweis jämförde två avdelningar. Förklara varför jämförelsen gjorde hans slutsats starkare, och ge ett skäl till att hans slutsats ändå inte var helt säker innan handtvätten infördes.", 3),
 ("En tidning skriver: ”Ny studie: Kaffe gör att du lever längre! Forskare har följt 500 000 personer och de som drack 2–3 koppar om dagen dog i lägre grad.” Värdera rubriken med begreppen observationsstudie, störfaktor och orsakssamband. Vad skulle krävas för att man säkert kan säga att kaffet är orsaken?", 3),
 ("Två klasser testar om gödning gör att bönplantor växer högre. Klass A har 3 plantor per grupp och får skillnaden 4 mm. Klass B har 30 plantor per grupp och får skillnaden 2 mm. Vilket resultat litar du mest på? Motivera och diskutera slumpens betydelse.", 2),
 ("Tabellen om jäst (avsnittet ”Tolka data och redovisa osäkerhet”) har ett avvikande värde vid 40 °C. Förklara hur du hanterar det och hur du redovisar resultatet så att läsaren kan avgöra hur säker slutsatsen är.", 3),
 ("Jämför två av exemplen Pasteur, Semmelweis och Marshall och Warren. Vad är gemensamt, och vad skiljer dem åt? Resonera om varför nya idéer ibland möts av motstånd, och om motståndet alltid är oberättigat.", 3),
 ("Två trovärdiga källor säger olika om ett kosttillskott: en myndighet avråder, en studie betald av tillverkaren visar effekt. Resonera om hur du väger källorna och vilken ytterligare information du skulle vilja ha. Formulera ett argument och bemöt ett motargument.", 3)]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "Slumpa deltagare till två grupper (randomisering) så att grupperna blir lika från början. Grupp A får sportdrycken, grupp B en likadan dryck utan det verksamma ämnet (placebo). Varken deltagare eller testledare vet vem som fått vad (dubbelblind). Mät konditionen före och efter med samma test. Många deltagare och lika träning i grupperna. Ett välutvecklat svar förklarar för varje moment vilket fel det förhindrar.",
 "Avdelningarna var troligen lika i det mesta utom en sak (obduktioner före förlossningar), vilket gör att skillnaden i dödlighet troligen beror på den faktorn; avdelningen fungerar som kontrollgrupp. Osäkert eftersom andra skillnader kunde finnas, t.ex. vilka kvinnor som kom till vilken avdelning, och eftersom man inte visste hur sjukdomen spreds.",
 "Observationsstudie: forskarna har inte slumpat vem som dricker kaffe. Störfaktorer kan förklara sambandet (livsstil, inkomst, att sjuka slutat dricka kaffe). Studien visar korrelation, inte orsak. Många deltagare minskar slumpen men tar inte bort störfaktorer. Säker slutsats kräver randomiserade försök eller många olika studier som pekar åt samma håll samt en rimlig förklaring.",
 "Klass B. Med 3 plantor kan en enda ovanlig planta ge en stor skillnad av slump. Med 30 plantor jämnar slumpen ut sig. Välutvecklat svar: båda skillnaderna är små; titta på spridningen inom grupperna och gör om försöket.",
 "Undersök först om det finns en rimlig förklaring (t.ex. att ballongen satt löst). Redovisa värdet, förklara det, och visa medelvärde med och utan värdet (26 cm respektive 30,5 cm). Redovisa spridning (lägsta och högsta). Gör fler försök. Skriv hur osäker slutsatsen är.",
 "Gemensamt: belägg som inte passade den gamla förklaringen; motstånd i början; modellen ändrades när belägg samlades. Skillnader: Pasteur övertygade med ett enkelt, upprepbart försök; Semmelweis saknade förklaring till hur handtvätt hjälpte; Marshall och Warren mötte en etablerad bild (syra dödar bakterier). Motstånd kan vara rimligt när en modell fungerat länge, men det kan också bero på stolthet och brist på förklaring. Välutvecklat svar nyanserar.",
 "Väg: Vad bygger respektive källa på? Är studien oberoende granskad och upprepad? Tendens hos tillverkaren. Önskad info: fler oberoende studier, sammanställningar, storlek och design. Argument i formen påstående, belägg, motargument, bemötande, slutsats med angiven säkerhet."]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar systematiska undersökningar (planering, värdering, osäkerhet), vetenskapens gränser, förklaringsmodellers föränderlighet och kritisk granskning med argumentation.",
      SVAR, [("Resonera om störningar (avsnittet ”Planera ett eget försök”):", "T.ex. olika svåra ordlistor, ordningen på försöken, trötthet. Byt ordning, använd likvärdiga listor, flera deltagare."),
             ("Fundera (avsnittet ”Tolka data och redovisa osäkerhet”):", "Temperaturen verkar öka gasbildningen mellan 10 och 25 °C. Vid 40 °C är resultatet osäkert på grund av det avvikande värdet. Gör fler försök."),
             ("Tänk efter (avsnittet ”Hur säker är slutsatsen?”):", "T.ex. föräldrarnas utbildning, inkomst, tid som föräldrar läser med barnen."),
             ("Resonera (avsnittet ”Vetenskapens gränser”):", "Naturvetenskap: hur varg påverkar bytesdjur, och hur djur påverkas. Inte: om det är rätt, vilket också beror på värderingar."),
             ("Tänk efter (avsnittet ”Väga källor och granska påståenden”):", "Vem betalade? Hur många deltog och hur var det upplagt? Har andra fått samma resultat?")],
      "Siffrorna om Semmelweis (11,4 % 1846, 1,3 % 1848): MJA 2018. Marshall och Warren: Nobelstiftelsen 2005 och PMC2661189; att långt ifrån alla smittade får magsår är allmänt känt; ingen siffra anges. Kontrollera gärna mot en medicinsk källa. Carlson, Nature 1985. Jästdata och exempel är påhittade för undervisning (medelvärden: 30,5 cm utan och 26 cm med det avvikande värdet). · Illustrationer: egenritade.")
