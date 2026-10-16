# -*- coding: utf-8 -*-
"""Kemi område 1 Kemi som vetenskap – fördjupning (per moment)."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/kem/fig01k/'
NR = 1
SLUG = "kemi-vetenskap"
TAB = "1+"
NAMN = "Kemi som vetenskap"
UNDER = "Hur säker är en slutsats – och varför byter vi modeller?"
INTRO = ("Tre grupper mäter hur länge en brustablett tar på sig att lösa sig, och en av dem får ett värde som sticker ut. Ska det värdet tas bort, eller är det just det som är intressant? "
         "Och varför fick Daltons atommodell leva i över hundra år när vi nu vet att den är ofullständig? I den här fördjupningen resonerar du om hur säkra mätningar och slutsatser är, om skillnaden mellan slumpfel och systematiska fel, om modellers styrka och begränsningar och om hur man granskar påståenden på djupet. "
         "Namn och mätvärden i uppgifterna är påhittade exempel.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Värdera hur säker en slutsats är: skilj mellan slumpfel och systematiska fel och förklara vad avvikande värden betyder.", "Var nyanserad: visa vad en modell kan förklara, vad den inte kan och hur den prövats.",
       "Planera en undersökning och förbättra den med ledning av felkällor."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först grundtexten i kapitel 1. Fördjupningen bygger på begreppen hypotes, variabler, rättvist försök, medelvärde, felkälla, modell och källkritik."
D = {"1.1": "Arbeta som kemist", "1.2": "Modeller, källor och argument"}

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F1.1.1", "Precision och riktighet", "1.1",
 "<p>I grundtexten lärde du dig att upprepa mätningar och räkna medelvärde. Här tittar vi på <em>varför</em> det hjälper, och på vad som händer när mätningarna inte blir bra ändå. Ett mätvärde kan vara dåligt på två sätt som är olika.</p>"
 + fig(FIG+"f_traff.png", "<b>Bild F1.1</b> Fyra mätserier som träffar en tavla. Mitten är det sanna värdet. Precision handlar om spridningen, riktighet om hur nära medelvärdet ligger det sanna värdet.", "96%")
 + row("<p><strong class='green'>Precision</strong> säger hur nära varandra upprepade mätningar ligger. Är värdena lika har mätningen hög precision. Spridningen beror ofta på <strong class='green'>slumpfel</strong>: små, oförutsägbara skillnader som att du startar klockan lite för tidigt ena gången och lite för sent nästa. Slumpfel går åt båda hållen, och därför minskar de när du tar medelvärde av flera mätningar.</p>"
       "<p><strong class='green'>Riktighet</strong> säger hur nära det sanna värdet mätningarna ligger. En termometer som visar två grader för högt ger lika fel värde varje gång. Det är ett <strong class='green'>systematiskt fel</strong>: det går åt samma håll hela tiden. Systematiska fel syns inte som spridning, och medelvärde hjälper inte. Det kan finnas hög precision men låg riktighet.</p>",
       [begrepp([("Precision", "Hur nära varandra upprepade mätningar ligger."), ("Riktighet", "Hur nära det sanna värdet mätningarna ligger."), ("Slumpfel", "Oförutsägbara fel som går åt båda hållen."), ("Systematiskt fel", "Fel som går åt samma håll varje gång.")]),
        box("tank", "Tänk efter", "<p>Du läser alltid av mätcylindern med ögonen från samma felaktiga håll. Är det ett slumpfel eller ett systematiskt fel? Hjälper det att upprepa mätningen?</p>")])
 + "<h3>Vad gör man åt det?</h3>"
 + "<p>Slumpfel minskar du genom att upprepa mätningarna och räkna medelvärde, och genom att göra mätningen lika varje gång. Systematiska fel minskar du genom att kontrollera utrustningen, till exempel jämföra termometern med en annan, och genom att ha en <strong class='green'>jämförelse</strong> som utsätts för samma fel. Har båda proverna samma systematiska fel påverkar det inte skillnaden mellan dem, vilket är ett skäl till att jämförelser är så starka.</p>")

add("F1.1.2", "Avvikande värden och slutsatsens säkerhet", "1.1",
 "<p>Ibland sticker ett mätvärde ut. Det kan vara ett misstag, men det kan också vara något intressant. Frågan är hur man hanterar det på ett hederligt sätt.</p>"
 + fig(FIG+"f_punkter.png", "<b>Bild F1.2</b> Tre försök för tre temperaturer i klass 8B (påhittade värden). Strecken visar medelvärdet. Vid 20 °C sticker ett värde ut.", "66%")
 + row("<p>Vid 20 °C blev klassens tre mätningar 70 s, 118 s och 72 s. Medelvärdet med alla tre är 87 s. Utan det avvikande värdet blir medelvärdet 71 s. Skillnaden är stor, så beslutet spelar roll. Man får <em>inte</em> bara ta bort ett värde för att det inte passar. Man gör så här:</p>"
       + steps(["Kolla anteckningarna: finns det en känd orsak, till exempel att klockan stoppades sent eller att tabletten fastnade vid glaset?", "Gör om mätningen om det går. Finns det då inget skäl att misstänka ett misstag, behåll värdet.",
                "Redovisa öppet vad du gjort. Skriv både medelvärdet med och utan värdet, och vilken motivering du har.", "Överväg ett mått som tål avvikelser: <strong class='green'>medianen</strong> är mittersta värdet när värdena ordnas (här 72 s)."], True),
       [begrepp([("Avvikande värde", "Ett mätvärde som ligger långt från de andra."), ("Median", "Det mittersta värdet när värdena ordnas i storleksordning.")]),
        box("tank", "Tänk efter", "<p>Varför är det oärligt att ta bort ett värde bara för att det förstör mönstret? När kan det vara rätt att ta bort ett värde?</p>")])
 + "<h3>Hur säker är slutsatsen?</h3>"
 + "<p>Tre försök vid 5 °C gav 150 s, 160 s och 148 s, och vid 40 °C gav de 29 s, 33 s och 31 s. Spridningen inom varje grupp är liten jämfört med skillnaden <em>mellan</em> grupperna. Det talar för att temperaturen verkligen påverkar tiden. Vid 20 °C är spridningen stor, så där är kunskapen mer osäker. En bra slutsats säger både vad resultatet visar och hur säker man är: ”Tiden minskar när temperaturen ökar. Vid 20 °C är vi mer osäkra eftersom ett försök avvek.”</p>"
 + "<p>Var också försiktig med att dra slutsatser <em>utanför</em> det du mätt. Du har mätt vid 5, 20 och 40 °C. Du vet inte säkert vad som händer vid 80 °C. Mellan mätpunkterna kan du uppskatta, men en uppskattning är inte en mätning.</p>"
 + "<p><strong class='green'>Förklaringsmodell.</strong> Resultatet kan förklaras med partikelmodellen: när vattnet är varmare rör sig partiklarna snabbare, så de träffar tabletten oftare och med mer energi, och reaktionen går fortare. Förklaringen är en modell, inte något vi har sett direkt i just det här försöket. Din mätning visar <em>att</em> det går fortare. Modellen föreslår <em>varför</em>.</p>")

add("F1.2.1", "Vad gör en modell bra?", "1.2",
 "<p>I grundtexten lärde du dig att en modell är en förenkling. Men inte alla modeller är lika bra. Vad skiljer en användbar modell från en dålig?</p>"
 + row("<p><strong class='green'>En modell ska kunna förklara och förutsäga.</strong> Partikelmodellen förklarar att en gas fyller en behållare, och den förutsäger att gasen går att pressa ihop eftersom det är stora avstånd mellan partiklarna. Förutsägelser kan man pröva. Om en förutsägelse inte stämmer med mätningar måste modellen ändras eller bytas.</p>"
       "<p><strong class='green'>En modell passar ett syfte.</strong> Den bästa modellen är inte den mest detaljerade utan den som passar frågan. En tunnelbanekarta lämnar bort nästan allt, men fungerar utmärkt för att byta tåg. Den fungerar sämre om du vill veta avståndet i meter. På samma sätt är en enkel modell med runda partiklar bra för att förklara varför ämnen byter form, men den säger inget om hur en atom är uppbyggd.</p>"
       "<p><strong class='green'>En modell har gränser, och goda forskare säger vilka.</strong> Att veta var en modell slutar fungera är lika viktigt som att veta vad den kan.</p>",
       [begrepp([("Förutsägelse", "Det en modell säger ska hända, som man kan pröva."), ("Begränsning", "Något modellen inte kan förklara eller en situation där den inte gäller.")]),
        box("tank", "Tänk efter", "<p>Ge ett exempel på en modell som är bra för ett syfte men dålig för ett annat. Förklara varför.</p>")])
 + "<h3>Modeller prövas, de bevisas inte</h3>"
 + "<p>En modell kan ha stöd av många undersökningar, men den kan inte bevisas för alltid. Nästa undersökning kan visa något den inte förklarar. Därför säger forskare hellre att en modell har starkt stöd än att den är ”bevisad”. Det är ingen svaghet: det är så vetenskap förbättras.</p>")

add("F1.2.2", "Daltons modell: vad höll och vad ändrades?", "1.2",
 "<p>När John Dalton 1808 lade fram sin atomteori byggde den på tydliga idéer. Genom att jämföra dem med vad vi vet i dag kan du se hur en modell kan vara både användbar och ofullständig.</p>"
 + fig(FIG+"f_dalton_nu.png", "<b>Bild F1.3</b> Daltons atom som en hård, odelbar kula, och en senare modell där atomen har en kärna och elektroner.", "86%")
 + row("<p><strong class='green'>Vad höll?</strong> Daltons idé att ämnen består av atomer, att atomer av olika grundämnen skiljer sig åt och att atomer inte skapas eller förstörs i en kemisk reaktion stämmer fortfarande bra. Den förklarar Lavoisiers observation att massan bevaras: om inga atomer försvinner kan inte massan minska. Den förklarar också att ämnen ofta bildas i enkla förhållanden, till exempel en kolatom med en eller två syreatomer.</p>"
       "<p><strong class='green'>Vad ändrades?</strong> Dalton tänkte sig atomen som en hård, odelbar kula. Senare undersökningar visade att atomer har delar: en kärna och elektroner. Daltons tanke att alla atomer av samma grundämne är exakt likadana och väger lika mycket behövde också justeras. Det finns atomer av samma ämne som väger olika (isotoper).</p>",
       [begrepp([("Isotoper", "Atomer av samma grundämne som väger olika."), ("Elektron", "En liten, negativt laddad del som finns i atomer.")]),
        box("tank", "Tänk efter", "<p>Var Dalton ”fel”? Resonera: vad var rätt, vad var förenklat och varför fortsätter man ändå att undervisa om hans idéer?</p>")])
 + "<h3>Varför blev det ett byte, och varför tog det tid?</h3>"
 + "<p>Läran om fyra element levde i över 2 000 år. Det beror delvis på att den passade vardagliga iakttagelser: trä som brinner verkar släppa ut eld, och vatten som kokar verkar bli luft. Man vägde sällan, så få såg att något inte stämde. Det var när Boyle krävde försök och Lavoisier vägde som modellen började få problem. Dalton gav en ny modell som stämde med mätningarna. Så fungerar modellbyten: de sker inte för att någon tycker annorlunda, utan för att undersökningar visar något som den gamla modellen inte klarar.</p>")

add("F1.2.3", "Granska påståenden på djupet", "1.2",
 "<p>I grundtexten fick du fem frågor att ställa till en källa. Här skärper vi granskningen: vad är det som ofta går snett i påståenden om kemi?</p>"
 + row("<p><strong class='green'>Saknad jämförelse.</strong> ”98 procent av 50 testpersoner var nöjda med vår fläckborttagare.” Nöjda jämfört med vad? Utan jämförelse med bara vatten eller en annan produkt går det inte att veta om resultatet beror på produkten. Det är samma skäl som i ditt eget labb: du behöver en jämförelse.</p>"
       "<p><strong class='green'>Orsak och samband.</strong> Att två saker hänger ihop betyder inte att den ena orsakar den andra. Om fler glassar säljs när fler badar är det inte glassen som orsakar badandet. Båda beror på varmt väder.</p>"
       "<p><strong class='green'>Få mätningar eller utvalda resultat.</strong> Att visa bara de bästa resultaten, eller välja en jämförelse som ser bäst ut, ger en missvisande bild. Fråga: hur många mätningar, och hur valdes de?</p>"
       "<p><strong class='green'>Otydliga ord.</strong> ”Kemikaliefri”, ”naturlig” och ”giftfri” betyder olika saker för olika personer. Allt är kemiska ämnen, och naturliga ämnen kan vara giftiga. Mer användbart är att fråga <em>vilka ämnen</em> det gäller, <em>hur mycket</em> och <em>vilken fara</em> de utgör.</p>",
       [begrepp([("Samband", "Två saker som ändras tillsammans. Det betyder inte att den ena orsakar den andra."), ("Orsak", "Det som gör att något händer.")]),
        box("klimat", "Granska kritiskt", "<p>En annons säger: ”Vår tvål innehåller 100 % naturliga ingredienser och är därför snällare mot huden.” Vilka frågor ställer du? Vilka två saker blandas ihop i påståendet?</p>")])
 + "<h3>Vad är ett bra belägg?</h3>"
 + "<p>Ett bra belägg bygger på mätningar som någon annan kan upprepa, har en jämförelse, kommer från en källa utan egen vinning i frågan eller är kontrollerad av flera oberoende källor, och säger hur säkert resultatet är. Du kan inte alltid kontrollera allt själv, så du behöver också kunna bedöma <em>vem</em> du litar på och <em>varför</em>. Ett bra svar på frågan ”stämmer det?” är ofta ”det beror på vad som menas, och här är vad som är belagt”.</p>")

UPG = [
 ("Tre grupper mäter hur lång tid en brustablett tar att lösa sig vid 30 °C: 52 s, 49 s och 51 s. Gruppernas termometer visar dock 2 °C för mycket. a) Är det ett slumpfel eller ett systematiskt fel? b) Hur påverkar det precisionen och riktigheten? c) Hur kan de upptäcka felet och rätta till det?", 3),
 ("Klass 8B fick 70 s, 118 s och 72 s vid 20 °C. En elev vill stryka 118 s eftersom ”det är fel”. a) Förklara varför det inte är hederligt att bara stryka värdet. b) Beskriv vad man bör göra i stället. c) Räkna ut medelvärdet med och utan värdet och förklara vad du ska redovisa.", 3),
 ("Elin säger: ”Mina mätningar visar att brustabletten löser sig dubbelt så fort vid 80 °C som vid 40 °C.” Hon har bara mätt vid 5, 20 och 40 °C. a) Förklara vad som är problemet. b) Vad kan hon säga med säkerhet, och vad är bara en gissning? c) Planera en mätning som kan pröva om tiden fortsätter minska när vattnet blir varmare (använd högst 60 °C av säkerhetsskäl) och beskriv hur du gör den säker att lita på.", 3),
 ("En lärare säger: ”Partikelmodellen är bra, men den är inte hela sanningen.” a) Förklara vad hon kan mena. b) Ge ett exempel på något modellen förklarar och ett exempel på något den inte säger. c) Förklara varför man ändå använder modellen.", 3),
 ("En elev påstår: ”Dalton hade fel, så hans atomteori är värdelös.” a) Förklara vad som stämde i teorin och vad som ändrats sedan dess. b) Förklara hur Lavoisiers vägningar stödde Daltons teori. c) Värdera elevens påstående.", 3),
 ("En tillverkare skriver: ”Kemikaliefri rengöring. Testad: 9 av 10 nöjda!” a) Ge tre skäl till att vara skeptisk. b) Förklara skillnaden mellan samband och orsak med ett eget exempel. c) Planera ett test som kan pröva om rengöringen verkligen fungerar bättre än vanlig såpa, och beskriv hur du gör det rättvist.", 3),
]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "a) Systematiskt fel: det är lika fel varje gång, och går åt samma håll. b) Precisionen blir bra (värdena ligger nära varandra, 52, 49, 51) men riktigheten dålig eftersom alla mätningar sker vid fel temperatur. c) Jämföra med en annan termometer eller med en känd temperatur, t.ex. isvatten (0 °C), och justera eller räkna om.",
 "a) Värdet kan vara ett misstag, men det kan också vara en riktig mätning. Man får inte välja bort data bara för att den inte passar. b) Kontrollera anteckningar om en känd orsak, gör om mätningen om det går och redovisa öppet vad man gjort. c) Med: (70 + 118 + 72) / 3 = 87 s. Utan: (70 + 72) / 2 = 71 s. Redovisa båda, och motivera valet. Medianen är 72 s.",
 "a) Hon har inte mätt vid 80 °C, så det är en extrapolation utanför det uppmätta området. Kurvan kan ändra form, och vid mycket varmt vatten kan andra saker hända. b) Säkert: tiden minskade mellan 5, 20 och 40 °C. Gissning: vad som händer vid 80 °C. c) Mät vid fler temperaturer upp till högst 60 °C (av säkerhetsskäl, inte kokhett vatten), upprepa tre gånger vid varje, ha samma vattenmängd och tablettsort och redovisa medelvärde och spridning. Då ser man om kurvan fortsätter sjunka eller planar ut.",
 "a) Modellen är en förenkling: den förklarar mycket, men inte allt. b) Förklarar t.ex. att gas går att pressa ihop och att ämnen byter form. Säger inget om ämnets färg eller hur partiklarna är uppbyggda. c) Den är användbar för många syften, och enkla modeller är lättare att tänka med än mer detaljerade.",
 "a) Stämde: ämnen är uppbyggda av atomer, atomer av olika grundämnen skiljer sig åt och atomer skapas inte eller försvinner i reaktioner. Ändrades: atomer har delar (kärna och elektroner) och atomer av samma ämne kan väga olika (isotoper). b) Om atomer inte försvinner kan massan inte minska, vilket passar med att massan är lika före och efter. c) Påståendet är för svart-vitt. Teorin är förenklad men har varit grunden för modernare modeller. Modeller kan vara ofullständiga och ändå användbara.",
 "a) T.ex. kemikaliefri säger inget (allt är kemikalier), ingen jämförelse, oklart vad 9 av 10 betyder (hur många, vilka, nöjda med vad), avsändaren vill sälja. b) Samband: att två saker ändras tillsammans. Orsak: att den ena gör att den andra händer. Exempel: glassförsäljning och badande, båda beror på varmt väder. c) Samma fläck, tyg, mängd och tid för båda produkterna och en jämförelse med bara vatten. Upprepa, låt någon som inte vet vilken som är vilken bedöma, redovisa med poäng och medelvärde.",
]
RUTOR = [("Tänk efter (Precision och riktighet):", "Ett systematiskt fel: det går åt samma håll varje gång. Att upprepa hjälper inte, eftersom alla mätningar blir fel åt samma håll."),
         ("Tänk efter (Avvikande värden):", "Man påverkar resultatet åt det håll man önskar och gör slutsatsen osann. Man kan ta bort ett värde när det finns en känd, dokumenterad orsak till misstaget (t.ex. klockan stoppades sent), och då ska det redovisas."),
         ("Tänk efter (Vad gör en modell bra?):", "T.ex. en tunnelbanekarta: bra för att byta tåg, dålig för avstånd i meter. Eller partikelmodellen: bra för aggregationsformer, ger inget om atomens uppbyggnad."),
         ("Tänk efter (Daltons modell):", "Han hade rätt i grunden (atomer, skapas inte eller försvinner i reaktioner) men förenklade atomen. Hans idéer lär man ut eftersom de förklarar mycket och är en bra start som man sedan bygger på."),
         ("Granska kritiskt (Granska påståenden på djupet):", "Frågor: vilka ingredienser, i vilken mängd, jämfört med vad, vem har testat, vad menas med ”snällare”. Samband och orsak: att något är naturligt betyder inte att det är snällare mot huden. Dessutom blandas ”naturlig” och ”snäll” ihop.")]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar precision och riktighet (slumpfel och systematiska fel), hur man hanterar avvikande värden och värderar slutsatsens säkerhet, vad som gör en modell bra, Daltons modell i ljuset av senare kunskap och hur man granskar påståenden på djupet, och tränar det resonemang som krävs på högsta nivå.",
      SVAR, RUTOR,
      "Källstatus: Daltons teori (1808), Lavoisiers massbevarande (1789), Boyles bok (1661) och de fyra elementen är kontrollerade mot öppna källor (se källförteckningen). Allmän läroboksfakta, inte källkontrollerad i detta arbete: begreppen precision, riktighet, slumpfel och systematiskt fel, median, att atomer har kärna och elektroner (J.J. Thomson 1897) och isotoper, samt att samband inte är orsak. Alla mätvärden är påhittade. Brustabletten kan förklaras med partikelmodellen, men förklaringen är en modell och inte något som har mätts i just detta försök.")
