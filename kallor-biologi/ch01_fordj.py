# -*- coding: utf-8 -*-
"""Biologi kapitel 1 – Fördjupning."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/bio/fig01/'
NR = 1
SLUG = "vetenskap"
TAB = "1+"
NAMN = "Biologi som vetenskap"
UNDER = "Hur vet vi att vi inte lurar oss själva?"
INTRO = ("Den största utmaningen för en forskare är inte att hitta svar – det är att inte lura sig själv. Vi ser gärna det vi vill se, och slumpen kan få nästan vad som helst att se ut som ett samband. "
         "I den här fördjupningen lär du dig hur forskare designar rättvisa undersökningar, varför vissa upptäckter först blev hånade och hur vetenskapen rättar sina egna misstag.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa – ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Väg för- och nackdelar och se frågan från flera perspektiv, till exempel miljö, hälsa, ekonomi och etik.", "Var nyanserad: visa vad som är osäkert och vad mer man skulle behöva veta.",
       "Ta ställning och motivera ditt ställningstagande med naturvetenskapliga argument."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först kapitel 1 i grundboken. Fördjupningen bygger på begreppen hypotes, variabel, kontrollgrupp, placebo, korrelation och källkritik."
S = []
S.append(("F1.1", "Rättvisa försök",
 "<p>Föreställ dig att ett företag påstår att deras nya tablett gör att förkylningar går över snabbare. Hur skulle man kunna testa det? Det låter enkelt: ge tabletten till några förkylda personer och se om de blir friska. Men de flesta förkylningar går över av sig själva inom en vecka. Hur vet man då att det var tabletten som hjälpte?</p>"
 + fig(FIG+"f_rct.png", "<b>Bild F1.1</b> En randomiserad, dubbelblind och placebokontrollerad studie – den mest pålitliga sortens medicinska försök.")
 + "<h3>Fyra knep för att inte lura sig själv</h3>"
 + row("<p><strong>Kontrollgrupp.</strong> En grupp får inte behandlingen. Då kan man jämföra.</p>"
       "<p><strong>Placebo.</strong> Kontrollgruppen får en likadan tablett utan verksamt ämne. Annars kan förväntningar påverka hur deltagarna mår.</p>"
       "<p><strong>Randomisering.</strong> Slumpen bestämmer vem som hamnar i vilken grupp. Om forskaren själv valde kunde hon omedvetet lägga de friskaste i den ena gruppen.</p>"
       "<p><strong>Blindning.</strong> Om deltagarna inte vet vilken grupp de är i är studien enkelblind. Om inte heller forskarna som mäter vet det är den dubbelblind. Då blir det mycket svårare att påverka resultatet, även omedvetet.</p>"
       "<p>Till sist behövs många deltagare. Med bara fem personer i varje grupp kan slumpen avgöra resultatet. Med hundratals blir slumpens betydelse liten.</p>",
   [begrepp([("Randomisering", "Slumpmässig fördelning till grupper."), ("Dubbelblind", "Varken deltagare eller forskare vet vem som fått vad."), ("Stickprov", "De individer man undersöker, som ska representera en större grupp.")])])))
S.append(("F1.2", "Semmelweis och de smutsiga händerna",
 "<p>På 1840-talet fanns det två förlossningsavdelningar på det stora sjukhuset i Wien. På den ena arbetade läkare och läkarstudenter, på den andra barnmorskor. Läkaren Ignaz Semmelweis märkte något skrämmande: på läkarnas avdelning dog många fler mödrar i barnsängsfeber. Kvinnor bad på sina knän om att få föda på barnmorskornas avdelning.</p>"
 + "<h3>Ett detektivarbete</h3>"
 + roww("<p>Semmelweis prövade flera förklaringar och uteslöt dem en efter en: trängsel, förlossningsställning, rädsla. Avdelningarna var lika i nästan allt – utom en sak. Läkarna och studenterna obducerade döda kroppar och gick sedan direkt till förlossningarna.</p>"
        "<p>År 1847 dog en kollega efter att ha skurit sig under en obduktion. Han fick samma symtom som de sjuka mödrarna. Semmelweis drog slutsatsen att ”något” från de döda kropparna fördes vidare med läkarnas händer. Han krävde att alla skulle tvätta händerna i klorkalk. Dödligheten sjönk kraftigt.</p>",
        [fig(FIG+"f_semmelweis.png", "<b>Bild F1.2</b> Dödligheten på de två avdelningarna, och efter att handtvätt infördes.")])
 + "<h3>Varför trodde ingen på honom?</h3>"
 + row("<p>Trots resultaten hånades Semmelweis. Det fanns flera skäl. Man kände till mikroorganismer, men ingen visste ännu att de kan orsaka sjukdomar – det dröjde ytterligare två decennier innan Pasteur och Koch visade det. Semmelweis kunde alltså inte förklara varför handtvätt hjälpte. Många läkare blev också förolämpade av tanken att de själva spred döden. Dessutom publicerade han sina resultat sent och på ett sätt som var svårt att granska.</p>",
       [box("visste", "Lärdom", "<p>Ett tydligt samband räcker ofta inte. Forskarvärlden vill också ha en förklaringsmodell för hur något fungerar, och resultat som andra kan granska och upprepa.</p>"),
        box("fundera", "Fundera", "<p>Varför var barnmorskornas avdelning en så bra jämförelsegrupp? Vad hade varit svårare att dra slutsatser om utan den?</p>")])))
S.append(("F1.3", "Störfaktorer och slump",
 "<p>Många nyheter bygger på undersökningar där forskare har jämfört grupper av människor, till exempel ”personer som äter mycket fisk lever längre”. Sådana <strong class='green'>observationsstudier</strong> är viktiga, men de har ett problem: grupperna kan skilja sig åt på många andra sätt än det man undersöker.</p>"
 + "<h3>Störfaktorer</h3>"
 + roww("<p>En <strong class='green'>störfaktor</strong> är något som påverkar både det man tror är orsaken och det man mäter. Kanske äter personer som äter mycket fisk också mer grönsaker, röker mindre och har högre inkomst. Då kan det vara de sakerna, och inte fisken, som gör att de lever längre.</p>"
        "<p>Forskare försöker räkna bort kända störfaktorer. Men det kan alltid finnas sådana som ingen har tänkt på. Därför är kontrollerade experiment med slumpad fördelning det säkraste sättet att visa orsak.</p>",
        [fig(FIG+"f_storfaktor.png", "<b>Bild F1.3</b> En störfaktor kan skapa ett samband mellan två saker som inte påverkar varandra.")])
 + "<h3>Slumpen lurar</h3>"
 + row("<p>Om du singlar slant tio gånger är det inte konstigt att få sju krona. Det betyder inte att myntet är fusk. Samma sak gäller i biologiska undersökningar: små skillnader mellan små grupper kan bero på ren slump. Ju större stickprovet är, och ju större skillnaden är, desto säkrare kan man vara på att den är verklig.</p>"
       "<p>Forskare redovisar därför hur säkra resultaten är. Om många olika forskargrupper, med olika metoder, kommer fram till samma sak blir kunskapen ännu säkrare. En enda studie, hur spännande den än låter i en rubrik, är sällan tillräcklig.</p>",
   [begrepp([("Observationsstudie", "Man jämför grupper utan att själv ändra något."), ("Störfaktor", "En faktor som påverkar både den misstänkta orsaken och resultatet.")]),
    box("tank", "Tänk efter", "<p>”Barn som har många böcker hemma får bättre betyg.” Ge två möjliga störfaktorer.</p>")])))
S.append(("F1.4", "När alla hade fel",
 "<p>Under större delen av 1900-talet var läkare säkra på varför man får magsår: stress, stark mat och för mycket magsyra. Behandlingen var syrahämmande medicin, och ibland operation. Magsår kom ofta tillbaka. Alla visste också att bakterier inte kunde leva i magsäckens frätande syra.</p>"
 + "<h3>Två envisa forskare</h3>"
 + roww("<p>I början av 1980-talet upptäckte de australiska forskarna Robin Warren och Barry Marshall spiralformade bakterier i magsäckar hos patienter med magsår. Bakterien fick namnet <em>Helicobacter pylori</em>. De föreslog att det var bakterien som orsakade såren. Få trodde på dem.</p>"
        "<p>År 1984 gjorde Marshall något drastiskt: han drack en odling av bakterierna. Efter några dagar fick han en svår inflammation i magen, och bakterien kunde hittas där. Senare studier visade att magsår kunde botas med antibiotika. År 2005 fick Warren och Marshall Nobelpriset i fysiologi eller medicin.</p>",
        [fig(FIG+"f_hpylori.png", "<b>Bild F1.4</b> Bakterien <em>Helicobacter pylori</em> kan leva i magsäckens slemhinna.")])
 + "<h3>Vetenskapen rättar sig själv</h3>"
 + "<p>Exemplet visar både en svaghet och en styrka hos vetenskapen. Svagheten: även experter kan hålla fast vid en gammal förklaring för länge. Styrkan: när beläggen blir tillräckligt starka ändrar forskarvärlden uppfattning. Det är det som skiljer vetenskap från pseudovetenskap – inte att man alltid har rätt, utan att man ändrar sig när man har fel.</p>"
 + "<p>Men det betyder inte att alla nya idéer är lika bra. Warren och Marshall fick rätt för att de hade belägg som kunde granskas och upprepas – inte för att de var envisa.</p>"
 + box("varning", "Etik", "<p>Marshalls självförsök var farligt, och i dag skulle det knappast godkännas. Forskning på människor måste granskas av en etikprövningsmyndighet innan den får göras.</p>")))
UPG = [
 ("Ett företag påstår att deras sportdryck ger bättre kondition. Planera en undersökning som kan pröva påståendet. Beskriv hur du använder kontrollgrupp, placebo, randomisering och blindning, och förklara varför varje del behövs.", 3),
 ("Semmelweis jämförde två avdelningar. Förklara varför jämförelsen gjorde hans slutsats starkare. Ge också ett skäl till att hans slutsats ändå inte var helt säker innan handtvätten infördes.", 3),
 ("En tidning skriver: ”Ny studie: Kaffe gör att du lever längre! Forskare har följt 500 000 personer och de som drack 2–3 koppar om dagen dog i lägre grad.” Värdera rubriken. Använd begreppen observationsstudie, störfaktor och orsakssamband. Vad skulle krävas för att man säkert skulle kunna säga att kaffet är orsaken?", 3),
 ("Två klasser testar om gödning gör att bönplantor växer högre. Klass A använder 3 plantor per grupp och får skillnaden 4 mm. Klass B använder 30 plantor per grupp och får skillnaden 2 mm. Vilket resultat litar du mest på? Motivera, och diskutera vad slumpen kan ha för betydelse.", 2),
 ("Barry Marshall drack en bakterieodling för att bevisa sin hypotes. a) Förklara varför försöket var ett starkt belägg men inte ett bevis. b) Diskutera om forskare bör få göra farliga försök på sig själva. Ge argument både för och emot och ta ställning.", 3),
 ("En studie om ett nytt bantningsmedel visar mycket goda resultat. Studien är betald av företaget som säljer medlet. Betyder det att resultatet är fel? Resonera om hur man kan granska studien och vad som skulle göra resultatet mer trovärdigt.", 3)]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "Slumpa deltagare till två grupper (randomisering) så att grupperna blir lika från början. Grupp A får sportdrycken, grupp B en likadan dryck utan det verksamma ämnet (placebo), så att förväntningar inte påverkar. Varken deltagare eller testledare vet vem som fått vad (dubbelblind). Mät konditionen före och efter med samma test, t.ex. ett bestämt löptest. Många deltagare och lika träning i båda grupperna. Ett välutvecklat svar förklarar för varje moment vilket fel det förhindrar.",
 "Avdelningarna var lika i nästan allt utom en sak (obduktioner/läkarnas arbete), vilket gör att skillnaden i dödlighet troligen beror på den faktorn – ungefär som en kontrollgrupp. Osäkert eftersom andra skillnader kunde finnas, t.ex. vilka kvinnor som kom till vilken avdelning, och Semmelweis saknade en förklaringsmodell (man visste inte att bakterier orsakar sjukdom).",
 "Det är en observationsstudie: forskarna har inte slumpat vem som dricker kaffe. Störfaktorer kan förklara sambandet, t.ex. att mycket sjuka personer slutat dricka kaffe, eller skillnader i livsstil och inkomst. Studien visar korrelation, inte orsakssamband. Stort antal deltagare minskar slumpens roll men tar inte bort störfaktorer. Säker slutsats kräver randomiserade försök (svårt i praktiken) eller många olika studier som pekar åt samma håll och en rimlig förklaringsmodell.",
 "Klass B. Med 3 plantor kan en enda ovanlig planta ge en stor skillnad av en slump. Med 30 plantor jämnar slumpen ut sig och medelvärdet blir mer tillförlitligt. Välutvecklat svar: båda skillnaderna är små; man borde titta på spridningen inom grupperna och göra om försöket.",
 "a) Ett enda försök på en person kan bero på slump eller annan orsak; det behövs upprepningar och kontrollerade studier. Men det visade att bakterien kan orsaka inflammation, vilket gjorde hypotesen rimlig. b) För: frivilligt, kan påskynda viktig kunskap. Emot: risk för allvarlig skada, kan inspirera andra, få belägg från en person. Motiverat ställningstagande krävs.",
 "Nej, men det finns risk för tendens. Granska: är studien publicerad och granskad av oberoende forskare? Var den randomiserad, dubbelblind och placebokontrollerad? Hur många deltog? Har andra forskare fått samma resultat? Oberoende upprepningar skulle öka trovärdigheten."]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller behöver mer utmaning. Den fördjupar det centrala innehållet om systematiska undersökningar, de biologiska förklaringsmodellernas historiska framväxt och föränderlighet och kritisk granskning av information, och tränar den typ av resonemang som krävs på högsta nivå i de nationella proven.",
      SVAR, [("Fundera (F1.2):", "Avdelningarna låg på samma sjukhus och tog emot liknande patienter. Det enda tydliga som skilde var vilka som förlöste och vad de gjorde innan. Utan jämförelsen hade man inte vetat vad som var en ”normal” dödlighet."),
             ("Tänk efter (F1.3):", "T.ex. föräldrarnas utbildning, inkomst, hur mycket tid föräldrarna läser med barnen, intresse för skolan.")],
      "Siffrorna i bild F1.2 är avrundade och visar mönstret i Semmelweis data från Allmänna sjukhuset i Wien 1841–1848. Uppgifterna om Warren och Marshall: Nobelpriset i fysiologi eller medicin 2005. Källor: Skolverket, Lgr22 kursplan i biologi. · Nobelprize.org: The Nobel Prize in Physiology or Medicine 2005. · Illustrationer: egenritade.")
