# -*- coding: utf-8 -*-
"""Kemi område 3 Atomer och grundämnen – fördjupning (per moment)."""
import sys
sys.path.insert(0, '/tmp/kem')
from bstyle import *
import fordj_common as C
from fordj_common import roww
FIG = '/tmp/kem/fig03k/'
NR = 3
SLUG = "kemi-atomer"
TAB = "3+"
NAMN = "Atomer och grundämnen"
UNDER = "Hur vet vi hur atomer ser ut, och vad avgör deras egenskaper?"
INTRO = ("Ingen har sett en atom med blotta ögat, men vi vet ändå mycket om hur den är byggd. Hur kan man dra säkra slutsatser om något osynligt, och hur säkra är de egentligen? "
         "Och varför står grundämnena just där de står i det periodiska systemet? I den här fördjupningen går du djupare in i elektronskalen och Bohrs modell, i vad som händer när atomkärnor delas och slås ihop, i radioaktivitet i samhället, i hur det periodiska systemet växte fram, i de sällsynta jordartsmetallerna och i vilka grundämnen som finns i rymden. "
         "Namn och mätvärden i uppgifterna är påhittade exempel.")
MAL = ["Resonera i flera led: visa hur en sak leder till nästa, med ”eftersom … därför … vilket leder till …”.", "Använd begreppen korrekt och förklara dem i sammanhanget.",
       "Värdera hur säker en slutsats är och vad en modell kan och inte kan förklara.", "Koppla ihop atomens byggnad med grundämnenas egenskaper och plats i periodiska systemet.",
       "Väg nytta mot risk när det gäller strålning, kärnenergi och material."]
MAL_RUBRIK = "SÅ NÅR DU HÖGSTA NIVÅN"
FUNDERA = "Läs först grundtexten i kapitel 3. Fördjupningen bygger på begreppen atomnummer, masstal, elektronskal, valenselektroner, isotop, radioaktivitet, halveringstid och periodiska systemet."
D = {"3.1": "Atomens byggnad", "3.2": "Periodiska systemet"}

S = []; FOOTS = []
def add(nr, t, delomr, inner):
    S.append((nr, t, inner)); FOOTS.append(f"Fördjupning {NR} · Delområde {delomr} {D[delomr]} · {t}")

add("F3.1.1", "Elektronskal och Bohrs modell fördjupat", "3.1",
 "<p>I grundtexten lärde du dig att elektronerna ligger i skal. Här tittar vi närmare på vad ett skal är och hur modellen förklarar ljus från atomer.</p>"
 + fig(FIG+"f_bohr.png", "<b>Bild F3.1</b> Bohrs modell för väte (schematiskt): elektronen kan bara finnas i vissa banor med bestämd energi. När den hoppar till en bana med lägre energi sänds ljus ut.", "78%")
 + row("<p>Enligt Bohrs modell från 1913 kan en elektron bara röra sig i vissa banor, och varje bana har en bestämd energi. Elektronen kan hoppa från en bana till en annan. Hoppar den till en bana med högre energi måste atomen ta upp energi, och hoppar den till en bana med lägre energi sänds energi ut som ljus. Eftersom banornas energier är bestämda kan atomen bara sända ut ljus med vissa bestämda energier, alltså vissa bestämda färger. Det förklarade hur väte sänder ut ljus och var ett stort genombrott.</p>"
       "<p>I vår förenklade skalmodell fylls skalen från kärnan och utåt. Det första skalet rymmer 2 elektroner, det andra 8 och det tredje 8 för de första 20 grundämnena. Natrium (11 elektroner) får då 2, 8, 1 och klor (17) får 2, 8, 7. Det är den yttersta elektronerna, valenselektronerna, som avgör hur ämnet reagerar. Ju närmare ett fullt yttersta skal atomen är, desto stabilare är den.</p>",
       [begrepp([("Bana (skal)", "Tillåtet område för elektronen, med bestämd energi."), ("Energinivå", "Den energi som hör till en bana."), ("Spektrum", "De färger ett ämne sänder ut eller tar upp.")]),
        box("tank", "Tänk efter", "<p>Neon har 10 elektroner. Hur är de fördelade på skalen? Varför är det rimligt att neon är mycket oreaktivt?</p>")])
 + "<h3>Vad kan modellen och vad kan den inte?</h3>"
 + "<p>Bohrs modell är bra på väte och förklarar varför ljus från atomer har bestämda färger. Den fungerar däremot inte bra för atomer med flera elektroner, och på 1920-talet ersattes den av kvantmekaniken, som beskriver elektronerna på ett annat sätt. Skalmodellen med 2, 8, 8 är en förenkling som fungerar för de första ämnena men inte längre ned i systemet. Det är ett exempel på hur en modell kan vara användbar inom sitt område och ändå ha gränser.</p>")

add("F3.1.2", "Kärnreaktioner: fission och fusion", "3.1",
 "<p>Atomkärnor kan förändras. Det sker inte i vanliga kemiska reaktioner, där det bara är elektronerna som flyttas, utan i kärnreaktioner.</p>"
 + fig(FIG+"f_fission.png", "<b>Bild F3.2</b> Fission och fusion (schematiskt): en tung kärna delas, eller två lätta kärnor slås ihop. Båda frigör energi.", "92%")
 + row("<p>Vid <strong class='green'>fission</strong> delas en tung atomkärna, till exempel uran, i mindre delar. Det frigör mycket energi och används i kärnkraftverk. Fissionen går att kontrollera och är därför det som används för kärnkraft idag.</p>"
       "<p>Vid <strong class='green'>fusion</strong> slås två lätta kärnor ihop till en tyngre. Det är det som sker i solen, där väte blir helium. Fusion kräver extremt hög temperatur och högt tryck för att kärnorna ska komma tillräckligt nära varandra. Fusion används inte kommersiellt för elproduktion idag.</p>"
       "<p>Båda sorterna frigör mycket mer energi per atom än kemiska reaktioner. Det beror på att det är energin som håller ihop kärnan som frigörs, och den är mycket större än energin i bindningarna mellan atomer.</p>",
       [begrepp([("Fission", "Tung kärna delas."), ("Fusion", "Lätta kärnor slås ihop."), ("Kärnreaktion", "Reaktion där kärnorna förändras.")]),
        box("tank", "Tänk efter", "<p>Varför räknas energin från solen som fusion och energin från ett kärnkraftverk som fission? Förklara skillnaden i dina egna ord.</p>")])
 + "<h3>Skillnad mot kemiska reaktioner</h3>"
 + "<p>I en kemisk reaktion byter atomerna partner och elektronerna flyttar, men varje atom behåller sitt atomnummer. I en kärnreaktion förändras själva kärnan, så ett grundämne kan bli ett annat. Därför är energin som frigörs så mycket större, men också därför är kärnreaktioner svårare att kontrollera och kräver särskilda säkerhetsåtgärder.</p>")

add("F3.1.3", "Radioaktivitet och samhället", "3.1",
 "<p>Radioaktivitet har använts i över hundra år. Här tittar vi närmare på hur sönderfallet följer en kurva och vad man ska väga mot varandra när strålning används.</p>"
 + fig(FIG+"f_sonderfall.png", "<b>Bild F3.3</b> Radioaktivt sönderfall för ett påhittat ämne med halveringstiden 10 år: av 80 g finns 40 g kvar efter 10 år, 20 g efter 20 år och 10 g efter 30 år.", "76%")
 + row("<p>Sönderfallet följer en kurva som aldrig når exakt noll. För varje halveringstid halveras det som finns kvar. Därför går det inte att säga att ett ämne är ”helt borta” efter en viss tid, men efter tio halveringstider finns bara ungefär en tusendel kvar (1/1024). Halveringstiden är alltid densamma för en viss isotop, oavsett hur mycket som finns, och den varierar enormt mellan ämnen. Kol-14 har en halveringstid på 5 730 år.</p>"
       "<p><b>Åldersbestämning med kol-14.</b> Levande organismer tar upp kol, och en del av det är kol-14. När organismen dör upphör upptaget, och kol-14 sönderfaller. Genom att mäta hur mycket kol-14 som finns kvar i förhållande till vad som fanns i levande organismer kan man uppskatta hur länge sedan det dog. Efter 5 730 år är hälften kvar och efter 11 460 år en fjärdedel. Metoden fungerar bara på material som en gång var levande och för åldrar upp till några tiotusentals år, eftersom det efter många halveringstider finns för lite kol-14 kvar att mäta.</p>",
       [begrepp([("Sönderfallskurva", "Visar hur mängden radioaktivt ämne minskar med tiden."), ("Strålskydd", "Åtgärder som minskar stråldosen: kort tid, långt avstånd och avskärmning."), ("Dos", "Hur mycket strålning kroppen utsätts för.")]),
        box("tank", "Tänk efter", "<p>Ett prov innehåller ett radioaktivt ämne med halveringstid 4 år. Hur mycket finns kvar av 160 g efter 12 år? Hur länge tar det tills mindre än 1 g återstår? Förklara.</p>")])
 + "<h3>Nytta eller risk?</h3>"
 + "<p>Samma strålning kan hjälpa och skada. Inom sjukvården används den för bilddiagnostik och för att förstöra cancerceller, där nyttan i regel är stor och dosen kontrolleras noga. Kärnkraft ger mycket energi utan koldioxidutsläpp vid driften, men olyckor som Tjernobyl och Fukushima visar riskerna och avfallet måste tas om hand under mycket lång tid eftersom vissa isotoper har lång halveringstid. Det som avgör om strålning är nyttig eller farlig är sort, dos, tid och skydd. Ett bra svar på en värderingsfråga väger alltså nytta mot risk och anger vad det beror på, i stället för att säga ”alltid farligt” eller ”helt ofarligt”.</p>")

add("F3.2.1", "Hur periodiska systemet växte fram", "3.2",
 "<p>Det periodiska systemet blev inte till på en gång. Det är resultatet av att många kemister ordnade ämnen, och av en idé som gjorde att systemet kunde förutsäga saker.</p>"
 + fig(FIG+"f_mendelejev.png", "<b>Bild F3.4</b> Idén bakom luckorna (schematiskt): när ämnena ordnas i en tabell blir det tomma platser där det borde finnas ett ämne. De tomma platserna förutsäger ämnen som ännu inte hittats.", "78%")
 + row("<p>År 1869 ordnade den ryske kemisten Dmitrij Mendelejev de då kända grundämnena efter atommassa och egenskaper så att ämnen med liknande egenskaper hamnade i samma kolumn. Där det inte fanns något ämne som passade lämnade han en lucka i stället för att tvinga in ett ämne på fel plats, och förutsade vilka egenskaper de saknade ämnena skulle ha. När nya grundämnen sedan upptäcktes och passade i luckorna stärktes förtroendet för systemet kraftigt.</p>"
       "<p>Idag ordnas systemet efter atomnummer, alltså antalet protoner, och inte efter atommassa. Det förklarar atomernas byggnad: ämnen i samma grupp har lika många valenselektroner. Systemet har alltså både en beskrivande och en förklarande sida: det visar mönster, och atombyggnaden förklarar dem.</p>",
       [begrepp([("Förutsägelse", "Att säga vad som kommer hända eller finnas innan det är prövat."), ("Lucka", "Tom plats i tabellen där det borde finnas ett ämne.")]),
        box("tank", "Tänk efter", "<p>Varför var det en styrka för Mendelejevs system att det kunde förutsäga ämnen som ännu inte hittats? Vad hade det betytt för systemet om förutsägelserna inte stämt?</p>")])
 + "<h3>Hur användbar är en förutsägelse?</h3>"
 + "<p>En förutsägelse bygger på trender: ämnen i samma grupp liknar varandra, och egenskaperna ändras gradvis nedåt i gruppen. Därför kan man uppskatta egenskaper för ett ämne som man knappt kunnat undersöka, men förutsägelsen är aldrig säker. Trender kan ha undantag, och det är mätningar som avgör. Ett bra svar anger både förutsägelsen och hur säker den är.</p>")

add("F3.2.2", "Sällsynta jordartsmetaller", "3.2",
 "<p>Ordet ”sällsynta jordartsmetaller” låter som något som nästan inte finns. Är det så?</p>"
 + fig(FIG+"f_sallsynta.png", "<b>Bild F3.5</b> De 17 sällsynta jordartsmetallerna i det periodiska systemet: skandium, yttrium och de 15 lantaniderna.", "92%")
 + row("<p>De sällsynta jordartsmetallerna är 17 grundämnen: de 15 lantaniderna (atomnummer 57–71), samt skandium och yttrium. De är inte särskilt sällsynta i jordskorpan, men de finns utspridda och är svåra att skilja från varandra, eftersom deras kemiska egenskaper liknar varandra. Därför är det ofta dyrt och energikrävande att utvinna dem, och gruvdriften kan ge föroreningar.</p>"
       "<p>De används i många moderna produkter. Neodym ingår i starka magneter, terbium och europium används i skärmar och belysning och erbium i fiberoptik. Det gör dem viktiga för bland annat elektronik och förnybar energi. Länder vill därför ha trygg tillgång, och frågan om var de utvinns och hur det påverkar miljön är en del av samhällsdebatten.</p>",
       [begrepp([("Lantanider", "De 15 grundämnena med atomnummer 57–71."), ("Utvinning", "Att ta fram ett grundämne ur malm eller berg.")]),
        box("tank", "Tänk efter", "<p>Varför kan ett grundämne vara viktigt för samhället även om det inte är sällsynt? Använd begreppen utvinning och kemiska egenskaper i ditt svar.</p>")])
 + "<h3>Varför är de svåra att skilja åt?</h3>"
 + "<p>Eftersom lantaniderna har liknande antal valenselektroner och därför liknande kemiska egenskaper följer de ofta med varandra i samma malm. Att skilja dem kräver många upprepade steg. Det visar ett samband mellan elektronerna och egenskaperna: ämnen som liknar varandra i byggnad är svåra att separera, vilket är samma princip som när du i kapitel 2 såg att ämnen med nästan samma kokpunkt är svåra att destillera isär.</p>")

add("F3.2.3", "Grundämnen i rymden", "3.2",
 "<p>Är grundämnena i rymden samma som här? Och var kommer de från?</p>"
 + fig(FIG+"f_rymd.png", "<b>Bild F3.6</b> Universums sammansättning efter massa (avrundat): väte och helium utgör tillsammans nästan allt, och alla tyngre grundämnen tillsammans bara en liten del.", "80%")
 + row("<p>Det mesta i universum är väte och helium: tillsammans ungefär 98 procent av massan. Alla tyngre grundämnen, som syre, kol och järn, utgör bara en liten del. De är ändå de som vi och jorden består av. De tyngre grundämnena har bildats genom fusion i stjärnor, där lätta kärnor slås ihop till tyngre, och spreds ut när stora stjärnor exploderade. Allt syre i vårt solsystem kommer från sådana exploderande stjärnor.</p>"
       "<p>Det betyder att atomerna i din kropp, bortsett från väte, har bildats i stjärnor som fanns långt före solen. Ordningen i periodiska systemet speglar också hur grundämnena har bildats: de lättaste först, och de tyngre i stegen därefter.</p>",
       [begrepp([("Fusion i stjärnor", "Lätta kärnor slås ihop till tyngre och frigör energi."), ("Supernova", "Kraftig explosion när en stor stjärna dör.")]),
        box("tank", "Tänk efter", "<p>Jämför fördelningen av grundämnen i universum med den i jordskorpan och i kroppen. Vad är lika och vad är olika? Vad kan förklara skillnaderna?</p>")])
 + "<h3>Vad kan vi veta?</h3>"
 + "<p>Man kan inte ta prover från stjärnor, så man undersöker ljuset från dem: varje grundämne sänder ut och tar upp ljus med sina egna färger, vilket du såg i Bohrs modell. Det betyder att atombyggnaden, som du lärt dig om i det här kapitlet, också är det som gör det möjligt att läsa av vad stjärnor består av. Det är ett exempel på hur kemi, fysik och astronomi hänger ihop.</p>")

UPG = [
 ("Natrium har 11 elektroner och klor har 17. a) Ange hur elektronerna är fördelade på skalen för båda enligt skolmodellen. b) Förklara med valenselektroner varför natrium är en mycket reaktiv metall medan neon (10 elektroner) knappt reagerar. c) Förklara vad skalmodellen inte kan förklara, och vad Bohrs modell från 1913 kunde förklara.", 3),
 ("En kärnkraftsdebatt: Anna säger ”Fission och fusion är samma sak.” Erik säger ”Solen drivs av fission.” a) Förklara skillnaden mellan fission och fusion. b) Värdera Annas och Eriks påståenden. c) Förklara varför kärnreaktioner frigör mycket mer energi än kemiska reaktioner.", 3),
 ("Ett prov av ett radioaktivt ämne (påhittat) har halveringstiden 4 år. Från början finns 160 g. a) Hur mycket finns kvar efter 12 år? b) Ungefär hur lång tid tar det tills mindre än 1 g återstår? Motivera. c) En tidning skriver att ämnet är ”helt borta efter 40 år”. Värdera påståendet.", 3),
 ("Ett museum ska åldersbestämma ett träföremål med kol-14 (halveringstid 5 730 år). Mätningen visar att en fjärdedel av den ursprungliga mängden finns kvar. a) Hur gammalt är föremålet ungefär? b) Varför fungerar metoden inte på en bergart? c) Ge två skäl till att åldern bara är en uppskattning.", 3),
 ("Mendelejevs periodiska system hade luckor. a) Förklara hur luckorna gjorde att systemet kunde förutsäga nya grundämnen. b) Idag ordnas systemet efter atomnummer i stället för atommassa. Förklara varför det är en bättre grund. c) Astat står i grupp 17 under jod. Förutsäg dess egenskaper och värdera hur säker förutsägelsen är.", 3),
 ("En tidning skriver att ”sällsynta jordartsmetaller finns knappt och måste skyddas på alla sätt”. a) Förklara vad som menas med sällsynta jordartsmetaller och varför namnet är missvisande. b) Förklara varför de är svåra att utvinna. c) Värdera påståendet och ge argument för och emot att utvinna dem.", 3),
]
def uppg_html(): return C.uppg_html(UPG, 4)
SVAR = [
 "a) Natrium: 2, 8, 1. Klor: 2, 8, 7. b) Natrium har en valenselektron som lätt avges, så det reagerar kraftigt. Neon har fullt yttersta skal (2, 8) och behöver varken ta upp eller avge elektroner, så det är oreaktivt. c) Skalmodellen med 2, 8, 8 är en förenkling som inte fungerar för atomer långt ned i systemet och som inte förklarar varför skalen har just dessa antal. Bohrs modell förklarade varför väte sänder ut ljus med bestämda färger (elektroner hoppar mellan banor med bestämd energi), men fungerar inte för atomer med flera elektroner och ersattes av kvantmekaniken.",
 "a) Fission: en tung kärna delas. Fusion: två lätta kärnor slås ihop. b) Anna har fel: det är olika processer. Erik har fel: solen drivs av fusion, där väte blir helium. c) Energin som håller ihop kärnorna är mycket större än energin i bindningarna mellan atomer, så en kärnreaktion frigör mycket mer energi per atom.",
 "a) 12 år är tre halveringstider: 160 → 80 → 40 → 20 g. 20 g är kvar. b) Efter 5 halveringstider (20 år) återstår 5 g, efter 6 (24 år) 2,5 g, efter 7 (28 år) 1,25 g och efter 8 (32 år) 0,625 g. Alltså ungefär 32 år. c) Efter 40 år (10 halveringstider) återstår 160/1024 ≈ 0,16 g. Det är mycket lite men inte noll. Påståendet är en förenkling: sönderfallet når aldrig exakt noll, men mängden kan vara så liten att den inte spelar roll.",
 "a) En fjärdedel är kvar efter två halveringstider, alltså ungefär 2 × 5 730 = 11 460 år. b) Metoden bygger på kol som levande organismer har tagit upp. En bergart har aldrig varit levande, så den har inte det kol-14 som sönderfaller på samma sätt. c) T.ex. mätfel, att halva mängden vid start inte är exakt känd, att provet kan vara förorenat med äldre eller yngre kol, och att man bara kan ange ett intervall.",
 "a) Där ett ämne saknades lämnade Mendelejev en lucka och förutsade egenskaper utifrån grannarna i raden och kolumnen. När ämnen hittades som passade stärktes systemet. b) Atomnumret är antalet protoner och avgör grundämnet, medan atommassan också beror på antalet neutroner. Atomnumret förklarar också elektronskalen och därmed gruppernas egenskaper. c) Astat har 7 valenselektroner som övriga halogener och förväntas vara fast (gas, vätska och fast nedåt i gruppen) och mindre reaktivt än jod. Förutsägelsen bygger på trender och är osäker eftersom det finns mycket lite astat att undersöka och trender kan ha undantag.",
 "a) De sällsynta jordartsmetallerna är 17 grundämnen: de 15 lantaniderna, skandium och yttrium. Namnet är missvisande eftersom de inte är särskilt sällsynta i jordskorpan. De finns utspridda. b) De är svåra att skilja från varandra på grund av liknande kemiska egenskaper, vilket kräver många steg, och gruvdriften kan förorena. c) Ett välutvecklat svar: för utvinning talar att de behövs i magneter, skärmar och fiberoptik, för förnybar energi och elektronik. Mot talar miljöpåverkan och beroende av få leverantörer. Påståendet ”finns knappt” är fel, men att utvinningen kan kräva hänsyn stämmer.",
]
RUTOR = [("Tänk efter (Elektronskal och Bohrs modell):", "Neon har 2 och 8 elektroner, alltså fullt yttersta skal. Ett fullt skal är stabilt, så neon behöver varken ta upp eller avge elektroner och reagerar knappt."),
         ("Tänk efter (Kärnreaktioner):", "I solen slås lätta kärnor ihop (väte blir helium), vilket är fusion. I ett kärnkraftverk delas tunga kärnor (uran), vilket är fission."),
         ("Tänk efter (Radioaktivitet och samhället):", "160 → 80 → 40 → 20 g efter 12 år (tre halveringstider). Efter 28 år återstår 1,25 g och efter 32 år 0,625 g, så det tar ungefär 30 år tills mindre än 1 g återstår."),
         ("Tänk efter (Hur periodiska systemet växte fram):", "Systemet kunde prövas: om de förutsagda ämnena hittades med de egenskaperna stärktes det. Hade förutsägelserna inte stämt hade systemet behövt ändras eller förkastas."),
         ("Tänk efter (Sällsynta jordartsmetaller):", "Ett grundämne kan vara viktigt för att det behövs i viktiga produkter, även om det inte är sällsynt. Om det är svårt att utvinna, på grund av liknande kemiska egenskaper hos grannämnena, blir tillgången ändå begränsad."),
         ("Tänk efter (Grundämnen i rymden):", "Lika: syre och lite andra grundämnen finns överallt. Olika: i universum dominerar väte och helium, medan jordskorpan domineras av syre och kisel och kroppen av syre, kol och väte. Lätta gaser som väte och helium har till stor del lämnat jorden, medan tyngre ämnen blev kvar när planeterna bildades.")]
def teacher_html():
    return C.teacher_html("Fördjupningen riktar sig till elever som är klara tidigt eller som behöver mer utmaning mot de högre kriterierna. Den fördjupar elektronskalen och Bohrs modell, fission och fusion, radioaktivitet i samhället med sönderfallskurva och åldersbestämning, hur det periodiska systemet växte fram, sällsynta jordartsmetaller och grundämnen i rymden, och tränar det resonemang som krävs på högsta nivå.",
      SVAR, RUTOR,
      "Källstatus: Bohrs modell, fission och fusion, halveringstid, kol-14 och dess halveringstid 5 730 år, Mendelejev 1869 och hans luckor, de 17 sällsynta jordartsmetallerna och deras användningar samt universums sammansättning (väte och helium ca 98 % av massan, tyngre grundämnen via fusion i stjärnor) är kontrollerade mot öppna källor (se källförteckningen). Allmän läroboksfakta, inte källkontrollerad i detta arbete: att skalen rymmer 2, 8 och 8, att ljus från stjärnor används för att avgöra deras sammansättning, att kol-14-metoden fungerar för åldrar upp till några tiotusentals år, att fusion kräver extremt hög temperatur och högt tryck, att lantanider liknar varandra i egenskaper på grund av liknande valenselektronstruktur, att astat är fast, att väte och helium till stor del lämnat jorden, samt att kärnkraft inte ger koldioxidutsläpp vid driften. Alla mätvärden är påhittade.")
