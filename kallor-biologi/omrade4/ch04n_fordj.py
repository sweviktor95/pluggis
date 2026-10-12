# -*- coding: utf-8 -*-
"""Område 4 Ekologi – fördjupning (nya ramverket, per moment)."""
import sys
sys.path.insert(0, '/tmp/bio')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/bio/fig04n/'
NR = 4
SLUG = "ekologi"
TAB = "4+"
NAMN = "Ekologi"
UNDER = "Varför hänger allt ihop – och vad händer när något tas bort?"
INTRO = ("Vad händer med en hel strand om man tar bort en enda havsstjärna? Hur kunde 29 renar bli 6 000 – och sedan nästan inga? Varför växer klöver bra i mager jord? "
         "I den här fördjupningen räknar, tolkar och resonerar du om ekosystem som en ekolog. Namn och mätvärden i uppgifterna är påhittade exempel, om inget annat står. "
         "Undersökningarna av Paine och Gause samt exemplet St Matthew är verkliga.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Väg för- och nackdelar, och se frågan från flera perspektiv.", "Var nyanserad: visa vad som är osäkert och vad man mer skulle behöva veta.",
       "Ta ställning och motivera med naturvetenskapliga argument."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först grundtexten i kapitel 4. Fördjupningen bygger på begreppen producent, konsument, nedbrytare, näringsväv, kretslopp, population, begränsande faktor, bärkraft och nisch."
D = {"4.1": "Ekosystem och energi", "4.2": "Materiens kretslopp", "4.3": "Populationer och samspel"}

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F4.1.2", "Nyckelarter och kaskadeffekter", "4.1",
 "<p>I grundtexten lärde du dig att en förändring i en näringsväv kan sprida sig. Men alla arter är inte lika viktiga för helheten. Vissa arter har en mycket större påverkan än deras antal eller vikt skulle antyda. De kallas <strong class='green'>nyckelarter</strong>. Om en nyckelart försvinner kan hela ekosystemet förändras.</p>"
 + "<h3>Havsstjärnan på stranden</h3>"
 + roww("<p>Ekologen Robert Paine arbetade vid 1960-talets början på en klippstrand vid Stilla havets kust i delstaten Washington. På en bit av stranden plockade han bort rovdjuret havsstjärnan <em>Pisaster ochraceus</em> gång på gång. På en jämförbar bit lät han allt vara som det var.</p>"
        "<p>På den orörda biten fanns kvar ungefär 15 arter. På biten utan havsstjärnor minskade antalet arter till ungefär 8. Havsstjärnan äter bland annat musslor. Utan den tog musslorna över klipporna, och många andra arter, som alger och snäckor, fick ingen plats att leva på.</p>"
        "<p>Paine kallade arten en <em>keystone species</em>, nyckelart. Havsstjärnan var inte talrik, men den höll musslorna i schack och gjorde att fler arter fick plats.</p>",
        [begrepp([("Nyckelart", "En art som har mycket större påverkan på ekosystemet än man kan vänta sig av dess antal."), ("Kaskadeffekt", "En förändring som sprider sig genom flera led i en näringsväv."), ("Kontrollområde", "Ett område där man inte ändrar något, för jämförelse.")]),
         box("tank", "Resonera om upplägget", "<p>Varför lät Paine en del av stranden vara orörd? Vilka felkällor kan finnas i en undersökning på bara en strand?</p>")])
 + "<h3>Uppifrån eller nerifrån?</h3>"
 + row("<p>En kaskadeffekt kan gå i två riktningar. I en <strong>uppifrånkaskad</strong> påverkas ekosystemet av toppen: om rovdjuren minskar kan växtätarna öka och äta upp mer av växterna. I en <strong>nerifrånkaskad</strong> är det i stället tillgången på näring och produktion längst ner som styr hur mycket som får plats längre upp.</p>"
       "<p>Ett känt men omdiskuterat exempel är vargens återkomst till Yellowstone på 1990-talet. Många forskare menar att vargarna påverkade hur hjortarna rörde sig och därmed växtligheten längs vattendragen. Andra menar att effekterna är mindre än man ofta får höra, och att väder, betestryck och andra rovdjur också spelar in. Det visar hur svårt det är att skilja en orsak från många samtidiga förändringar.</p>",
       [box("varning", "Var försiktig med enkla historier", "<p>Ekosystem har många samtidiga förändringar. När ett enskilt exempel blir en berömd berättelse är det lätt att glömma osäkerheterna.</p>")])
 + table(["", "Uppifrån", "Nerifrån"], [["Vad styr?", "Rovdjuren i toppen.", "Näring och produktion längst ner."], ["Exempel på kedja", "Färre rovdjur, fler växtätare, mindre växtlighet.", "Mindre näring, färre växter, färre växtätare, färre rovdjur."], ["Hur undersöker man det?", "Ta bort eller lägg till rovdjur och jämför med ett kontrollområde.", "Tillför eller minska näring och mät hur det påverkar de övre leden."]], "tbl"))

add("F4.1.3", "Räkna med energi och biomassa", "4.1",
 "<p>I grundtexten lärde du dig tumregeln att bara omkring 10 procent av energin förs vidare från en nivå i näringskedjan till nästa. Med den kan man göra uppskattningar som visar varför ekosystem ser ut som de gör. Tumregeln kan användas både för energi och för biomassa (vikten av levande material).</p>"
 + fig(FIG+"f_tumregel.png", "En näringskedja i Östersjön med tumregeln om 10 procent.")
 + row("<h3>Exempel</h3><p>En säl äter strömming och torsk. Om sälen växer 1 kg, hur mycket växtplankton har det krävt längre ner i kedjan?</p>"
   "<p class='green'><strong>1 kg säl ← 10 kg torsk ← 100 kg strömming ← 1 000 kg djurplankton ← 10 000 kg växtplankton</strong></p>"
   "<p>Varje steg uppåt i kedjan gör alltså att det krävs tio gånger mer föda längst ner. Det förklarar varför toppkonsumenter är få, behöver stora områden och är så känsliga för förändringar.</p>"
   "<h3>När pyramiden blir omvänd</h3><p>Energin som flödar genom ett ekosystem bildar alltid en pyramid: mest längst ner. Men biomassan, alltså vikten av det som lever just nu, kan ibland vara större högre upp. Ett möjligt exempel finns i öppet hav, där växtplankton är mycket små och förökar sig snabbt. De äts upp nästan lika fort som de bildas. Vid ett enskilt mättillfälle kan därför vikten av djurplankton vara större än vikten av växtplankton. Det går ändå ihop eftersom växtplankton omsätts mycket snabbt: det är <em>flödet</em> av energi som bildar pyramid, inte alltid mängden vid ett visst ögonblick.</p>",
   [box("tank", "Räkna själv", "<p>Kedjan är växtplankton, djurplankton, strömming, gädda och havsörn. Ungefär hur mycket djurplankton behövs för att havsörnen ska öka 1 kg? Hur mycket växtplankton?</p>"),
    box("varning", "Varning", "<p>10 procent är ett grovt genomsnitt. Hos växtätande insekter kan det vara mer, hos varmblodiga däggdjur ofta mindre, eftersom de använder mycket energi för att hålla värmen.</p>")]))

add("F4.2.2", "Kvävets kretslopp", "4.2",
 "<p>Alla organismer behöver kväve för att bygga proteiner och DNA. Luften består till 78 volymprocent av kvävgas, men varken växter eller djur kan använda den direkt. Kvävgasmolekylen är för stabil. Därför är kväve ofta det ämne som begränsar hur mycket växter kan växa.</p>"
 + fig(FIG+"f_kvave.png", "Kvävets kretslopp, förenklat.")
 + row(
   "<p><strong>Kvävefixering.</strong> Vissa bakterier kan omvandla kvävgas till ämnen som växter kan ta upp. En del lever i knölar på rötterna hos baljväxter som klöver, ärter och bönor. Växten ger bakterierna socker och får kväve tillbaka. Det är en symbios.</p>"
   "<p><strong>Näringskedjan.</strong> Djur får kväve genom att äta växter eller andra djur.</p>"
   "<p><strong>Nedbrytning.</strong> Nedbrytare frigör kväveföreningar ur döda organismer och avföring. Växterna kan ta upp dem igen.</p>"
   "<p><strong>Tillbaka till luften.</strong> Andra bakterier, särskilt i syrefattig och blöt mark, omvandlar kväveföreningar till kvävgas igen.</p>"
   "<p>Människan har förändrat kretsloppet kraftigt. Med konstgödsel tillför vi stora mängder kväve till åkrarna. Vad det får för följder i sjöar och hav tar vi upp i område 5.</p>",
   [box("klimat", "Kväve i havet", "<p>I Östersjön finns cyanobakterier som själva kan fixera kväve ur luften. De är ett exempel på att samma process som sker i klöverns rotknölar också sker i vatten.</p>"),
    box("begrepp", "Begrepp", "<b class='t'>Kvävefixering</b><p>När bakterier gör om kvävgas till ämnen som växter kan använda.</p>")]))

add("F4.3.1", "Populationer som växer – och kraschar", "4.3",
 roww("<p>Om varje hare får fyra ungar som överlever och förökar sig blir det snabbt väldigt många harar. När en population kan växa fritt ökar den inte med samma antal varje år, utan med en viss andel. Ju fler individer, desto fler nya, och kurvan böjer uppåt som ett J. Det kallas <strong class='green'>exponentiell tillväxt</strong>.</p>"
     "<p>I verkligheten tar resurserna slut förr eller senare. Tillväxten bromsas och populationen planar ut kring det antal som miljön kan försörja långsiktigt, miljöns <strong class='green'>bärkraft</strong>. Kurvan får formen av ett S.</p>"
     "<p>Bärkraften är inte konstant. Den beror på födotillgång, väder, rovdjur och konkurrenter, och kan förändras om miljön förändras. Om en population växer långt över bärkraften kan den förstöra sin egen födobas. Då kan den krascha och bärkraften bli lägre än förut.</p>",
   [fig(FIG+"f_jkurva.png", "J-kurva och S-kurva.")])
 + "<h3>Renarna på St Matthew</h3>"
 + roww("<p>År 1944 släpptes 29 renar ut på den obebodda ön St Matthew i Berings hav. Där fanns tjocka mattor av lavar men inga rovdjur och ingen jakt. Renarna förökade sig snabbt. År 1963 räknade forskare till omkring 6 000 renar. Men lavarna, som växer mycket långsamt, var nästan helt uppätna.</p>"
       "<p>Vintern 1963–64 var ovanligt sträng med mycket snö. Renarna svalt ihjäl i stort antal. År 1966 fanns bara 42 renar kvar, och på 1980-talet var de helt borta. Lavmattorna har fortfarande inte återhämtat sig helt.</p>",
   [fig(FIG+"f_ren.png", "Renpopulationen på St Matthew.")])
 + box("fundera", "Tänk efter", "<p>Varför räckte det inte att renarna hade gott om mat år 1950 för att populationen skulle förbli stabil?</p>"))

add("F4.3.3", "Nischer och samexistens", "4.3",
 "<p>I grundtexten lärde du dig att varje art har en nisch, och att två arter med samma nisch konkurrerar hårt. Här tittar vi närmare på vad som då händer, och hur många arter ändå kan leva på samma plats.</p>"
 + "<h3>Gauses tofsdjur</h3>"
 + roww("<p>På 1930-talet odlade den ryske biologen Georgy Gause tofsdjur, encelliga organismer av släktet <em>Paramecium</em>, i provrör med bakterier som föda. Odlade han <em>P. aurelia</em> och <em>P. caudatum</em> var för sig klarade sig båda bra. Odlade han dem tillsammans i samma provrör fick de konkurrera om samma bakterier, och <em>P. aurelia</em> trängde så småningom ut <em>P. caudatum</em>.</p>"
        "<p>När Gause i stället blandade <em>P. aurelia</em> med arten <em>P. bursaria</em> fanns båda kvar. <em>P. bursaria</em> söker föda på ett annat ställe i provröret, och den lever dessutom i symbios med alger. De hade alltså olika nischer.</p>"
        "<p>Resultatet brukar kallas <strong class='green'>konkurrensutslagning</strong>: när två arter behöver samma resurs på samma sätt blir det ofta bara en kvar. Men det är en laboratoriemodell i en enkel miljö. I naturen finns mycket mer variation som gör att arter kan samsas.</p>",
        [begrepp([("Konkurrensutslagning", "När en art trängs ut av en annan som konkurrerar om samma resurs."), ("Resursdelning", "När arter delar på en resurs genom att använda den på olika sätt, platser eller tider.")]),
         box("tank", "Tänk efter", "<p>Varför är det viktigt att Gause odlade varje art även ensam?</p>")])
 + "<h3>Hur får många arter plats?</h3>"
 + row("<p>I en gran kan flera fågelarter leva sida vid sida, eftersom de söker föda på olika delar av trädet. Det kallas <strong>resursdelning</strong>. Arter kan också dela genom att jaga vid olika tider på dygnet, äta olika storlekar av föda eller leva på olika ställen. Ju fler olika nischer en miljö erbjuder, desto fler arter får plats.</p>"
       "<p>Det betyder också att en miljö som blir mer enformig, till exempel när variationen i ett landskap försvinner, ofta rymmer färre arter.</p>",
       [box("fundera", "Fundera", "<p>Två nya arter flyttar in i en skog. Den ena har exakt samma nisch som en art som redan finns där. Den andra har en egen nisch. Vilken har störst chans att klara sig, och varför?</p>")]))

UPG = [
 ("Använd bilden om renarna på St Matthew. a) Beskriv populationens utveckling och förklara den med begreppen exponentiell tillväxt och bärkraft. b) Förklara varför populationen inte planade ut som i en S-kurva. c) Hur hade utvecklingen troligen sett ut om det funnits vargar på ön?", 3),
 ("En ekologisk bonde gödslar inte med konstgödsel. I stället odlar hon klöver vartannat år på åkern och plöjer ner den. Förklara i flera steg hur det kan ge mer kväve till grödan nästa år. Diskutera också för- och nackdelar jämfört med konstgödsel.", 3),
 ("En gråsäl äter ungefär 5 kg fisk per dag. Använd tumregeln om 10 procent och gör en uppskattning av hur mycket djurplankton som krävs för en säls mat under ett år, om fisken den äter är strömming som äter djurplankton. Redovisa dina beräkningar och kommentera hur säker uppskattningen är.", 2),
 ("Paine tog bort havsstjärnor från en bit av en strand och jämförde med en bit där de fick vara kvar. Förklara i flera led varför antalet arter minskade på den bit där havsstjärnorna togs bort. Förklara också varför Paine behövde ett kontrollområde och vad som ändå gör slutsatsen osäker.", 3),
 ("Gause odlade två arter av tofsdjur först var för sig och sedan tillsammans. Beskriv vad som hände och förklara det med begreppen konkurrens och nisch. Förklara också varför en laboratorieundersökning inte säkert visar vad som händer i naturen.", 3),
 ("I ett havsområde mäter man vid ett tillfälle mer biomassa djurplankton än växtplankton. En elev drar slutsatsen att tumregeln om 10 procent är fel. Värdera elevens slutsats. Förklara hur biomassan kan vara omvänd trots att energin ändå minskar uppåt i kedjan.", 3),
]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "a) Mycket föda och inga rovdjur gav exponentiell tillväxt från 29 till ca 6 000. Populationen växte långt över öns bärkraft och åt upp de långsamt växande lavarna. b) Det fanns ingen broms (rovdjur, jakt) när populationen närmade sig bärkraften, och fördröjningen mellan att lavarna tog slut och att renarna dog gjorde att de överskred den. En sträng vinter gav kraschen. Bärkraften sjönk eftersom lavmattorna förstördes. c) Vargar hade ätit renar, så populationen hade vuxit långsammare och troligen pendlat kring en lägre nivå utan att förstöra lavarna.",
 "Klöverns rotknölar har kvävefixerande bakterier som tar kväve från luften. Kvävet byggs in i klöverns proteiner. När klövern plöjs ner bryter nedbrytare ner den och frigör kväveföreningar som nästa gröda tar upp. Fördelar: ingen energikrävande tillverkning av konstgödsel, bättre jordstruktur. Nackdelar: åkern ger ingen säljbar gröda det året, och kväve kan läcka även här vid fel tidpunkt.",
 "5 kg/dag · 365 ≈ 1 800 kg strömming per år. Strömmingen behöver ca 10 gånger så mycket djurplankton: ca 18 000 kg (18 ton). Osäkert: 10 % är ett grovt genomsnitt, sälen äter flera fiskarter, och fisken äter också annat. Ett välutvecklat svar resonerar om vad osäkerheterna gör med svaret.",
 "Havsstjärnan åt musslor. Utan havsstjärnor ökade musslorna och täckte klipporna, så alger, snäckor och andra arter fick ingen plats, och artantalet föll från ca 15 till ca 8. Kontrollområdet visar vad som händer när ingenting ändras, så att man kan se att det var just borttagandet som gjorde skillnaden. Osäkert: bara en strand, platsens förhållanden kan ha spelat in, och resultatet gäller kanske inte alla kuster. Ett välutvecklat svar nämner nyckelart och kaskadeffekt.",
 "Var för sig klarade sig båda arterna. Tillsammans trängde P. aurelia ut P. caudatum, eftersom de konkurrerade om samma bakterier och hade i stort sett samma nisch. Med P. bursaria fanns båda kvar, eftersom den hade en annan nisch (annan plats att söka föda på). I naturen finns fler platser, fler resurser och fler arter, så samexistens kan ske på andra sätt. Ett välutvecklat svar förklarar konkurrensutslagning och resursdelning.",
 "Slutsatsen är inte hållbar. Biomassan är vikten av det som lever just nu, medan 10 procent gäller hur mycket energi som förs vidare per tidsenhet. Växtplankton förökar sig mycket snabbt och äts upp nästan lika fort som de bildas, så det finns lite av dem vid ett enskilt tillfälle trots att flödet är stort. Energin minskar ändå uppåt. Ett välutvecklat svar skiljer mellan mängd och flöde och föreslår upprepade mätningar över tid.",
]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar näringsvävar och nyckelarter, energi och biomassa, kvävets kretslopp, populationers tillväxt och samexistens mellan arter, och tränar den typ av resonemang som krävs på högsta nivå.",
      SVAR, [("Resonera om upplägget (Nyckelarter och kaskadeffekter):", "Kontrollområdet visar vad som händer utan ingreppet. Felkällor: bara en strand, platsens särdrag, årsvariation. Fler stränder och upprepning gör slutsatsen säkrare."),
             ("Räkna själv (Räkna med energi och biomassa):", "Från djurplankton till havsörn är det tre steg: 1 kg · 10³ = 1 000 kg djurplankton. Ett steg till ger 10 000 kg växtplankton."),
             ("Tänk efter (Populationer som växer – och kraschar):", "Mat i överflöd ger tillväxt men säger inget om hur länge den räcker. Lavarna växer långsamt och förbrukades snabbare än de hann växa tillbaka, så bärkraften sjönk."),
             ("Tänk efter (Nischer och samexistens):", "Utan kontroll vet man inte om arterna klarar sig var för sig. Då kan man inte säga att det var konkurrensen som gav utslagningen."),
             ("Fundera (Nischer och samexistens):", "Arten med en egen nisch klarar sig troligen bäst. Arten med samma nisch konkurrerar om samma resurser och kan trängas ut.")],
      "St Matthew: D. R. Klein (1968), The introduction, increase and crash of reindeer on St. Matthew Island; värdet för 1957 är ungefärligt. Paine: R. T. Paine (1966), Food web complexity and species diversity, American Naturalist; antalet arter är avrundat. Gause: G. F. Gause (1934), The Struggle for Existence. Yellowstone-exemplet är omdiskuterat och redovisas som sådant. Omvänd biomassapyramid: ett möjligt exempel i öppet hav, ej mätt här. Siffran 78 % kväve i luften avser volymprocent. Uppgiften om 5 kg fisk per dag är en ungefärlig siffra för en vuxen gråsäl. Källor: Skolverket, Lgr22 kursplan i biologi. · Illustrationer: egenritade.")
