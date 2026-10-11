# -*- coding: utf-8 -*-
# Kapitel 8 – Nationalism och imperialism (åk 8)
T = dict(
 nr=8, namn="Nationalism och imperialism", under="När nationer bildades och stormakterna lade under sig världen",
 fil="historia-08-imperialism", arskurs=8, nodeid="historia-imperialism",
 mal=["förklara vad nationalism är och hur nationalstater bildades",
      "berätta om hur Italien och Tyskland enades och hur unionen mellan Sverige och Norge upplöstes 1905",
      "förklara varför stormakterna ville skaffa kolonier (råvaror, marknader, prestige)",
      "beskriva hur Afrika delades upp och vad som hände i Kongo",
      "jämföra hur imperialismen påverkade Indien, Kina och Japan",
      "förklara hur rasism användes för att motivera imperialism, och hur människor gjorde motstånd",
      "förklara hur spänningar och allianser mellan stormakterna ledde mot första världskriget",
      "resonera om hur det koloniala arvet och Afrikas gränser används i dag"],
 fundera="Vad är du ”stolt över” när det gäller ditt land eller din bygd? Och när kan stolthet över sitt land bli något farligt? Skriv tre meningar innan du läser.",
)

S = []

S.append(dict(id="nationalism", nr="8.1", ikon="🏳️", titel="Nationalism – vi är ett folk",
 intro="På 1800-talet blev en ny idé stark i Europa: att människor som delar språk, historia och kultur borde höra ihop i ett eget land. Idén kallas nationalism.",
 block=[
  ("p","<strong>Nationalism</strong> är idén att en <em>nation</em>, alltså ett folk som känner samhörighet, ska ha sin egen stat. En stat där de flesta tillhör samma nation kallas en <strong>nationalstat</strong>. Före 1800-talet styrdes många områden av kungar och kejsare, och människor kände sig ofta mer hemma i sin bygd eller sin religion än i en nation."),
  ("p","Det som band samman en nation kunde vara språket, gemensamma minnen och hjältar, och traditioner. Författare, konstnärer och tonsättare hjälpte till. Rörelsen kallas <strong>nationalromantik</strong>. Man samlade folksagor och folksånger, målade landskap och skrev dikter om fornstora tider. I Sverige blev till exempel den götiska rörelsen i början av 1800-talet ett uttryck för att vara stolt över den egna historien."),
  ("p","Nationalismen kunde verka för frihet. Folk som stod under främmande makt ville styra sig själva. Men nationalismen kunde också skapa spänningar. Vad händer med dem som inte hör till nationen? Och vad händer när två nationer vill ha samma land?"),
  ("tab",["Nationalismen som kraft för …","Nationalismen som problem för …"],[
    ["Frihet från främmande makt","Minoriteter som inte passade in"],
    ["Gemensam identitet och sammanhållning","Konflikter mellan nationer"],
    ["Nya stater, t.ex. Italien och Tyskland","Rivalitet och krig mellan stormakter"]]),
  ("ruta","tank","Fundera","Vem räknas till ”nationen”? Är det samma sak som alla som bor i landet? Fundera på hur olika svar kan leda till både sammanhållning och konflikt."),
  ("kolla",["Vad är en nationalstat?","Vad är nationalromantik?","Ge ett exempel på ett positivt och ett negativt resultat av nationalism."]),
 ],
 svar=["En stat där de flesta tillhör samma nation.","En konst- och kulturrörelse som lyfte fram folkets historia, språk och landskap.","Positivt: nya stater/frihet. Negativt: konflikter, minoriteter som utestängdes."],
))

S.append(dict(id="enande", nr="8.2", ikon="🇮🇹", titel="Italien, Tyskland och Norge",
 intro="Under 1800-talet bildades nya nationalstater genom krig och förhandlingar. Två av de viktigaste var Italien och Tyskland. I Norden tog unionen mellan Sverige och Norge slut 1905.",
 block=[
  ("p","<strong>Italien</strong> var uppdelat i flera små stater, och en del styrdes av främmande makter. Statsmannen Cavour och frihetskämpen Garibaldi arbetade för ett enat Italien. År 1860 tog Garibaldi kontroll över södra Italien, och 1861 utropades kungariket Italien. Venetien kom med 1866, och Rom 1870. Ett enat land fanns, men mycket skilde norr och söder."),
  ("p","<strong>Tyskland</strong> bestod av många stater. Preussens ledare Otto von Bismarck ville samla dem under Preussen. Det skedde genom tre krig: mot Danmark 1864, mot Österrike 1866 och mot Frankrike 1870–71. Den 18 januari 1871 utropades det tyska kejsardömet i Spegelsalen i slottet Versailles, med Preussens kung Vilhelm I som kejsare. Frankrike, som förlorat kriget, kände sig förödmjukat."),
  ("p","<strong>Sverige och Norge</strong> hade sedan 1814 haft samma kung. Norge hade egen regering, egen grundlag och eget parlament, men utrikespolitiken sköttes av Sverige. Under 1800-talets slut ökade norrmännens krav på en egen utrikespolitik. Den 7 juni 1905 förklarade Stortinget unionen upplöst. I en folkomröstning i augusti röstade 368 208 för och 184 emot. Efter förhandlingar i Karlstad enades länderna, och den 26 oktober 1905 avstod Oscar II från den norska tronen. Unionen upplöstes utan krig."),
  ("tidslinje",[("1861","Kungariket Italien utropas"),("1864","Preussen besegrar Danmark"),("1866","Preussen besegrar Österrike"),("1871","Tyska kejsardömet utropas"),("1905","Unionen mellan Sverige och Norge upplöses")]),
  ("ruta","historia","Orsak och konsekvens","Tysklands enande ändrade maktbalansen i Europa. Det nya Tyskland blev snabbt en av de starkaste industri- och militärmakterna. Det skapade oro hos grannarna, särskilt hos Frankrike, och är en av förklaringarna till de spänningar som senare ledde till första världskriget."),
  ("kolla",["Vilka två personer förknippas med Italiens enande?","Hur enades Tyskland?","Hur skilde sig upplösningen 1905 från de tyska och italienska enandena?"]),
 ],
 svar=["Cavour och Garibaldi.","Genom tre krig under Preussens ledning (1864, 1866, 1870–71). Kejsardömet utropades 1871.","Där var det en nation som delade upp en union fredligt, medan Tyskland och Italien enades genom krig."],
))

S.append(dict(id="varfor", nr="8.3", ikon="🌍", titel="Imperialism – varför ville stormakterna ha kolonier?",
 intro="Imperialism betyder att en stat utvidgar sin makt genom att lägga under sig andra områden. Från mitten av 1800-talet till första världskriget gjorde de europeiska stormakterna detta i en större skala än någonsin.",
 block=[
  ("p","Ett <strong>imperium</strong> är ett stort rike som styr över många områden och folk. Ett område som styrs av en annan stat kallas <strong>koloni</strong>. Imperialismen byggde på att industrialiserade länder med starka arméer och moderna vapen och fartyg kunde ta kontroll över områden långt hemifrån."),
  ("p","Varför gjorde de det? Historiker nämner främst tre grupper av orsaker."),
  ("tab",["Orsak","Förklaring"],[
    ["Råvaror","Fabrikerna behövde bomull, gummi, järn, guld, kaffe, socker och olja"],
    ["Marknader","Fabrikerna behövde köpare till sina varor och platser att investera pengar"],
    ["Prestige och makt","Ju fler kolonier, desto starkare stormakt. Även strategiska hamnar och handelsvägar var viktiga"],
    ["Idéer","Man ville sprida kristendom och ”civilisation”, och trodde sig vara överlägsen"]]),
  ("p","De här orsakerna hänger ihop med industrialiseringen: ångbåtar, järnvägar, telegraf och kulsprutor gjorde det lättare att ta och behålla kolonier. Läkemedlet kinin hjälpte européer att motstå malaria i Afrika."),
  ("p","Några stater, som Storbritannien och Frankrike, hade haft kolonier länge. Andra, som Tyskland och Italien, hade just blivit nationalstater och ville nu visa att de var stormakter. Nationalismen och imperialismen drev alltså på varandra."),
  ("ruta","fakta","Sverige och kolonierna","Sverige hade inga stora kolonier. Landet hade en liten koloni på ön S:t Barthélemy i Karibien 1784–1878, som sedan såldes till Frankrike. Men svenskar deltog på annat sätt i imperialismen, som missionärer, officerare och sjökaptener i andra staters kolonier."),
  ("kolla",["Vad är en koloni?","Nämn tre orsaker till imperialismen.","Hur hjälpte industrialiseringen imperialismen?"]),
 ],
 svar=["Ett område som styrs av en annan stat.","Råvaror, marknader, prestige och makt (samt idéer om civilisation).","Genom ångbåtar, järnvägar, telegraf, moderna vapen och kinin."],
))

S.append(dict(id="afrika", nr="8.4", ikon="🗺️", titel="Afrikas uppdelning och Kongo",
 intro="År 1870 kontrollerade européerna bara en mindre del av Afrika, mest vid kusterna. Trettio år senare var nästan hela kontinenten uppdelad mellan europeiska makter.",
 block=[
  ("p","Kapplöpningen om Afrika kallas ofta <strong>Afrikas uppdelning</strong>. Européerna kom för råvaror, handel och makt. I Afrika fanns hundratals folk och stater, med egna språk och styren. Europeerna frågade dem inte."),
  ("p","Mellan den 15 november 1884 och den 26 februari 1885 samlades representanter för 14 stater i Berlin, inbjudna av Tysklands Bismarck. Sverige-Norge var med, liksom bland andra Storbritannien, Frankrike, Tyskland, Portugal, Belgien, Ryssland och USA. <strong>Inga afrikanska ledare</strong> var med. Man kom överens om fri handel och fri sjöfart i Kongos flodområde, och om att den som ville göra anspråk på ett område måste visa att den verkligen styrde där. Konferensen delade inte själv upp kartan, men reglerna ökade kapplöpningen."),
  ("p","Det finns undantag från kolonialismen: Etiopien, som 1896 besegrade den italienska armén vid Adwa, och Liberia förblev självständiga."),
  ("ruta","historia","Kongo – ett exempel på hårt styre","Kung Leopold II av Belgien styrde Kongo mellan 1885 och 1908 som sin privata egendom, under namnet Kongofristaten. Efter 1890 steg efterfrågan på gummi, och byarna tvingades samla in gummi som skatt. Våldet var stort och många människor dog av våld, sjukdomar och svält. Forskare uppskattar att mellan en och tio miljoner människor dog, men siffran är osäker eftersom ingen räknade. Missionärer, journalister och Roger Casement, som skrev en rapport 1904, avslöjade förhållandena. 1908 övertog den belgiska staten Kongo."),
  ("p","Rapporterna väckte protester i flera länder. Det visar att inte alla européer tyckte att kolonialismen var rätt, och att pressen kunde påverka."),
  ("kolla",["Vilka deltog i Berlinkonferensen, och vilka saknades?","Vilka länder i Afrika förblev självständiga?","Varför är dödssiffrorna i Kongo osäkra?"]),
 ],
 svar=["14 stater, bl.a. Storbritannien, Frankrike, Tyskland, Sverige-Norge och USA deltog; inga afrikanska ledare.","Etiopien och Liberia.","Ingen räknade, och många dog av sjukdom och svält, så forskare får uppskatta."],
))

S.append(dict(id="indienkina", nr="8.5", ikon="🇮🇳", titel="Indien och Kina",
 intro="Imperialismen drabbade också Asien. Indien blev en koloni under Storbritannien, medan Kina tvingades öppna sig genom krig och avtal.",
 block=[
  ("p","<strong>Indien</strong> hade styrts av det brittiska Ostindiska kompaniet, ett handelsbolag med egen armé. År 1857 gjorde indiska soldater, så kallade sepoyer, uppror. Missnöjet hade många orsaker, bland annat annekteringar och regler som kränkte soldaternas religion. Britterna slog ned upproret 1858. Då tog den brittiska kronan över styret direkt. Drottning Victoria fick 1876 titeln kejsarinna av Indien."),
  ("p","Indien blev det mest värdefulla området i det brittiska imperiet. Där odlades te, bomull och opium, och indisk råvara gick till brittiska fabriker. Britterna byggde järnvägar, men de tjänade främst brittiska intressen. År 1885 bildades Indiska nationalkongressen, som växte till en stor rörelse för mer inflytande och senare självständighet."),
  ("p","<strong>Kina</strong> var ett stort rike som handlade med omvärlden på egna villkor. Britterna ville sälja mer, och en vara blev viktig: opium, som kunde göra människor beroende. När den kinesiska regeringen försökte stoppa införseln började det första opiumkriget (1839–1842). Kina förlorade. I freden i Nanjing 1842 fick Storbritannien Hongkong och flera hamnar öppnades för handel. Kina fick också betala stora summor i skadestånd. Ett andra opiumkrig följde 1856–1860."),
  ("p","Kinesiska nationalister kallade senare sådana fördrag för <strong>ojämlika fördrag</strong>, eftersom Kina fick ge mycket och fick lite tillbaka. Landet försvagades och andra makter tog också egna intressesfärer."),
  ("tidslinje",[("1839–1842","Första opiumkriget"),("1842","Freden i Nanjing, Hongkong blir brittiskt"),("1857–1858","Sepoyupproret i Indien"),("1858","Kronan tar över styret i Indien"),("1876","Victoria blir kejsarinna av Indien"),("1885","Indiska nationalkongressen bildas")]),
  ("kolla",["Vad hände i Indien efter upproret 1857?","Varför bröt det första opiumkriget ut?","Vad menas med ojämlika fördrag?"]),
 ],
 svar=["Den brittiska kronan tog över styret från Ostindiska kompaniet 1858.","Kina försökte stoppa införseln av opium och britterna ville fortsätta sälja.","Avtal där en part fick ge mycket och inte fick något tillbaka, och som tvingades fram med våld."],
))

S.append(dict(id="japan", nr="8.6", ikon="🇯🇵", titel="Japan – en annan väg",
 intro="Japan gick en annan väg än Kina. Landet moderniserade sig snabbt och blev själv en imperialistisk stormakt.",
 block=[
  ("p","Under lång tid hade Japan hållit sig mestadels isolerat. År 1853 anlände amerikanska krigsfartyg under Matthew Perry och krävde att Japan skulle öppna sina hamnar för handel. Många japaner förstod att landet var svagt mot västmakternas vapen."),
  ("p","År 1868 fick kejsar Meiji tillbaka den politiska makten efter århundraden av shogunstyre, och landet gick in i <strong>Meijiperioden</strong>. Japan byggde snabbt upp ett nytt samhälle. Regeringen satte upp fabriker, importerade teknik och experter, införde skolplikt (1872), allmän värnplikt (1873) och en författning (1889). Mottot var ungefär ”ett rikt land och en stark armé”."),
  ("p","Med modern armé och flotta började Japan själv lägga under sig områden. Landet besegrade Kina i kriget 1894–1895 och Ryssland i kriget 1904–1905, och 1910 annekterade det Korea. Japan blev den första stormakten utanför Europa och Nordamerika."),
  ("ruta","tank","Jämför Japan och Kina","Båda länderna pressades av västmakterna. Varför gick det så olika? Historiker pekar på bland annat att Japan var mer enhetligt och snabbare genomförde reformer, medan Kinas styre var försvagat av inre konflikter och krig. Det finns också andra förklaringar, och forskare är inte helt överens."),
  ("ruta","fakta","Offer och förövare","Japan hade själv pressats av västmakterna, men blev samtidigt en kolonisator i Korea och Taiwan. Samma land kan alltså vara både utsatt och en maktutövare. Det är ett exempel på att historien sällan är svartvit."),
  ("kolla",["Vad hände i Japan 1853?","Nämn tre reformer under Meijiperioden.","Varför kan Japan sägas vara både offer och förövare?"]),
 ],
 svar=["Amerikanska fartyg under Perry tvingade Japan att öppna hamnar för handel.","T.ex. skolplikt, allmän värnplikt, fabriker, författning.","Det pressades av västmakterna men blev själv en kolonialmakt i Korea och Taiwan."],
))

S.append(dict(id="ideologi", nr="8.7", ikon="⚖️", titel="Rasism, motstånd och följder",
 intro="Hur kunde européerna motivera att de styrde över andra folk? Ett svar var rasism. Men människor i kolonierna gjorde också motstånd.",
 block=[
  ("p","Många européer trodde att deras egen kultur var mer utvecklad än andra. <strong>Rasism</strong> är idén att människor kan delas in i ”raser” där vissa är mer värda än andra. Det är en idé som saknar vetenskaplig grund, men som under 1800-talet spreds som ”vetenskap”. Den användes för att rättfärdiga att européer styrde över andra."),
  ("kalla","Dikten The White Man's Burden","I dikten uppmanar författaren USA att ”ta upp den vite mannens börda” och styra över folk som beskrivs som barn som behöver ledning.","Rudyard Kipling, brittisk författare, 1899. Skriven när USA tog över Filippinerna. Sammanfattat med egna ord."),
  ("p","<strong>Den vite mannens börda</strong> blev ett slagord. Idén var att européerna hade en plikt att ”civilisera” andra. Men kolonierna drevs av egenintresse. Skolor och sjukhus byggdes ibland, men mest där det gagnade kolonialmakten, och människor fick sällan bestämma över sina egna liv."),
  ("p","Folk i kolonierna gjorde <strong>motstånd</strong>: väpnade uppror som sepoyupproret i Indien, diplomati och reformer som i Etiopien, och politiska rörelser som Indiska nationalkongressen. Många tidiga uppror slogs ned. Men tankarna levde vidare och gav senare kraft åt de rörelser som kämpade för självständighet."),
  ("ruta","historia","Följder och arv","Imperialismen hade långsiktiga följder. Gränser drogs utan hänsyn till folk och språk. Ekonomier byggdes för att skicka råvaror till Europa. Samtidigt spreds nya språk, skolor och idéer. Historiker diskuterar fortfarande hur stor del av dagens problem som kan förklaras med kolonialtiden. Det finns inget enkelt svar. <strong>Kontinuitet och förändring:</strong> många afrikanska länder blev självständiga på 1950- och 60-talen (förändring), men gränserna och exportberoendet levde kvar (kontinuitet)."),
  ("kolla",["Vad är rasism?","Vad menades med ”den vite mannens börda”?","Ge två exempel på motstånd mot kolonialismen."]),
 ],
 svar=["Idén att människor kan delas in i raser där vissa är mer värda än andra.","Idén att européer hade en plikt att ”civilisera” andra folk.","T.ex. sepoyupproret, Etiopien vid Adwa, Indiska nationalkongressen."],
))

S.append(dict(id="vagen", nr="8.8", ikon="🧨", titel="Stormakternas spänningar – vägen mot kriget",
 intro="Kolonierna, nationalismen och det snabba tekniska framåtskridandet gjorde stormakterna rivaler. I början av 1900-talet delade Europa upp sig i två block.",
 block=[
  ("p","Stormakterna konkurrerade om kolonier, handel och militär styrka. Tyskland byggde en stor flotta, vilket oroade Storbritannien. Alla stora länder rustade upp med fler soldater och vapen."),
  ("p","Samtidigt slöt staterna <strong>allianser</strong>, alltså avtal om att hjälpa varandra. Tyskland och Österrike-Ungern slöt avtal 1879, och 1882 gick Italien med i den så kallade trippelalliansen. Frankrike och Ryssland ingick en allians 1894. Storbritannien och Frankrike kom överens 1904 (<em>Entente cordiale</em>), och 1907 bildades trippelententen mellan Storbritannien, Frankrike och Ryssland."),
  ("tab",["Block","Medlemmar (1914)"],[
    ["Trippelententen (de allierade)","Storbritannien, Frankrike, Ryssland"],
    ["Centralmakterna","Tyskland, Österrike-Ungern (Italien var allierat men gick sedan med motsidan 1915)"]]),
  ("p","Allianserna var tänkta att avskräcka, men de gjorde också att en konflikt mellan två länder lätt kunde dra in fler. På Balkan, där många folk ville bilda egna nationalstater, var spänningarna särskilt stora. Det gäller bland annat Bosnien, som Österrike-Ungern kontrollerade men där många serber ville ansluta sig till Serbien."),
  ("ruta","historia","Orsak – en kedja","Nationalism, imperialism, upprustning och allianser samverkade. Ingen enskild orsak räcker. Det är vad man kallar ett <em>sammansatt orsaksmönster</em>. I nästa kapitel ser du hur det gick till när skotten föll i Sarajevo 1914."),
  ("bild","imperialism","Stormakternas rivalitet om kolonier skapade spänningar."),
  ("kolla",["Vilka länder ingick i trippelententen?","Varför kunde allianser göra konflikter större?","Varför var Balkan särskilt spänt?"]),
 ],
 svar=["Storbritannien, Frankrike och Ryssland.","Om ett land angreps skulle dess allierade hjälpa det, så fler drogs in.","Många folk ville bilda egna stater och stormakter hade intressen där."],
))

F = []

F.append(dict(id="f1", nr="F1", ikon="📚", titel="Källkritik: Hur vet vi vad som hände i Kongo?",
 intro="När det gäller Kongo finns det få exakta siffror. Ändå vet historiker mycket. Hur går det ihop?",
 block=[
  ("p","Historiker använder olika slags källor: rapporter från missionärer, brev, domstolsprotokoll, kartor, fotografier och uppgifter från dem som drabbades. Roger Casements rapport från 1904 följdes av en belgisk kommission som bekräftade mycket av det han hade skrivit."),
  ("p","Källorna har olika problem. Kolonisatörerna skrev ofta för att visa att allt gick bra. Missionärer ville kanske också påverka. De som drabbades hade sällan möjlighet att skriva ner sina berättelser. Därför kan det saknas röster."),
  ("tab",["Källtyp","Styrka","Fråga att ställa"],[
    ["Kolonialtjänstemäns rapporter","Detaljer om organisationen","Skrev de för att försvara sig?"],
    ["Missionärers brev","Ögonvittnen","Hade de egna syften?"],
    ["Fotografier","Visar förhållanden","Vem tog dem och varför?"],
    ["Muntliga berättelser","Röster från dem som drabbades","Hur har berättelsen förts vidare?"]]),
  ("ruta","tank","Osäkra siffror","Dödssiffran varierar mellan forskare, ungefär från en till tio miljoner. Varför kan två seriösa forskare komma fram till så olika siffror? Fundera på vad som saknas för att räkna exakt."),
  ("kolla",["Nämn tre källtyper om Kongo.","Varför kan kolonisatörers rapporter vara missvisande?","Vad säger de olika siffrorna om källäget?"]),
 ],
 svar=["T.ex. missionärsbrev, tjänstemäns rapporter, fotografier, muntliga berättelser.","De skrev ofta för att försvara sig och visa att styret fungerade.","Att ingen räknade systematiskt och att källorna är ofullständiga."],
))

F.append(dict(id="f2", nr="F2", ikon="💬", titel="Varför imperialism? Olika tolkningar",
 intro="Forskare har förklarat imperialismen på olika sätt. Det är ett exempel på att historiska förklaringar kan konkurrera.",
 block=[
  ("p","Den <strong>ekonomiska förklaringen</strong> säger att kapitalister sökte nya marknader och råvaror. Den <strong>politiska förklaringen</strong> lyfter fram maktbalans, prestige och strategiska platser. Den <strong>kulturella förklaringen</strong> pekar på idéer om överlägsenhet och på en vilja att sprida kristendom eller ”civilisation”."),
  ("p","Det är svårt att säga vilken som väger tyngst. Ibland var kolonier ekonomiskt olönsamma för staten, men ändå eftertraktade för prestige. Ibland drevs det på av enskilda företagare, missionärer eller officerare snarare än av regeringarna."),
  ("tab",["Förklaring","Exempel som stödjer","Exempel som motsäger"],[
    ["Ekonomisk","Gummi och Kongo, bomull och Indien","Vissa kolonier gav lite vinst"],
    ["Politisk","Kapplöpning om hamnar och rutter","Små stater gjorde det av andra skäl"],
    ["Kulturell","Slagord om civilisation och mission","Idéerna användes för att motivera redan beslutad politik"]]),
  ("ruta","historia","Tolkning – inte bara fakta","När forskare tolkar påverkas de av sin tid, sin utbildning och det de vill förklara. Därför kan nya generationer ställa nya frågor till samma källor."),
  ("kolla",["Vad säger den ekonomiska förklaringen?","Ge ett argument mot att bara förklara imperialism ekonomiskt.","Varför tolkar historiker ibland olika?"]),
 ],
 svar=["Att stater och företag ville ha råvaror och marknader.","Vissa kolonier var olönsamma men eftertraktade för prestige och strategiskt läge.","De ställer olika frågor, har olika källor och påverkas av sin tid."],
))

F.append(dict(id="f3", nr="F3", ikon="⚔️", titel="Etiopien och Adwa – motstånd som lyckades",
 intro="Etiopien är ett av få exempel på ett afrikanskt land som stod emot kolonisering. Hur gick det till?",
 block=[
  ("p","Den 1 mars 1896 besegrade etiopiska styrkor under kejsar Menelik II en italiensk armé vid staden Adwa. Italienarna lämnade artilleri och omkring 3 000 fångar efter sig. Italien tvingades erkänna Etiopiens självständighet, och det gjorde andra europeiska makter också."),
  ("p","Förklaringar som nämns är att Menelik hade samlat en stor armé, skaffat moderna gevär och att Etiopien hade en egen stat med lång historia. Italienarna hade dessutom dålig information om terrängen."),
  ("p","Segern blev en symbol för afrikanskt motstånd. För Italien var det en förödmjukelse. Den bidrog till att Italien under 1930-talet försökte erövra landet igen."),
  ("ruta","tank","Fundera","Varför kan en seger i en enskild strid få stor symbolisk betydelse långt efteråt? Vem kan vilja minnas Adwa idag?"),
  ("kolla",["Vad hände vid Adwa 1896?","Nämn en förklaring till den etiopiska segern.","Varför blev slaget en symbol?"]),
 ],
 svar=["Etiopien besegrade Italien och behöll sin självständighet.","T.ex. stor armé, moderna gevär, stark stat, dålig italiensk information.","Det visade att ett afrikanskt land kunde stå emot en europeisk stormakt."],
))

F.append(dict(id="f4", nr="F4", ikon="📣", titel="Historiebruk: Afrikas gränser och det koloniala arvet",
 intro="Kolonialtiden används fortfarande i dag i debatter om gränser, ekonomi och rättvisa.",
 block=[
  ("p","Många gränser i Afrika är raka linjer på kartan. Ofta nämns Berlinkonferensen som den händelse som ”delade Afrika”. Men forskare påpekar att konferensen inte drog gränserna. De drogs efteråt, genom avtal mellan kolonialmakterna, ofta med lite kunskap om hur folk faktiskt levde."),
  ("p","När Afrikas länder blev självständiga, främst på 1950- och 60-talen, behöll de flesta gränserna. Man ville undvika nya konflikter om nya gränsdragningar. Därför ser vi än idag stater där flera folk lever i samma land, och folk som delas av gränser."),
  ("tab",["Aktör","Hur kolonialtiden används","Fråga att ställa"],[
    ["Regeringar","Förklarar problem med kolonialt arv","Är det hela förklaringen?"],
    ["Museer","Diskuterar föremål som togs under kolonialtiden","Vem ska äga dem?"],
    ["Aktivister","Kräver ursäkter och upprättelse","Vad innebär rättvisa idag?"],
    ["Författare och forskare","Granskar källor och minnen","Vems röst saknas?"]]),
  ("ruta","fakta","Så granskar du historiebruk","Fråga: Vem berättar? Vilket syfte finns? Vad utelämnas? Vem tjänar på berättelsen? Jämför med andra källor."),
  ("kolla",["Varför sägs det att Berlinkonferensen ”delade Afrika”, och vad är nyansen?","Varför behöll många länder koloniala gränser?","Ge ett exempel på hur kolonialtiden används idag."]),
 ],
 svar=["Den satte regler men gränserna drogs efteråt genom avtal mellan makterna.","Man ville undvika nya konflikter om gränser.","T.ex. diskussioner om föremål på museer, ursäkter, förklaringar till ekonomiska problem."],
))

UPPG = [
 ("Para ihop","Koppla ihop begrepp och förklaring.",["Nationalism","Nationalstat","Imperialism","Koloni","Allians","Rasism"],["Avtal om att hjälpa varandra","Idén att folk kan rangordnas","Idén att en nation ska ha sin egen stat","Område som styrs av annan stat","Stat där de flesta tillhör samma nation","Att lägga andra områden under sig"],"1 – C, 2 – E, 3 – F, 4 – D, 5 – A, 6 – B"),
 ("Tidslinje","Sätt i rätt ordning.",["Berlinkonferensen","Tyska kejsardömet utropas","Kungariket Italien utropas","Unionen Sverige–Norge upplöses","Slaget vid Adwa"],None,"1861 Italien; 1871 Tyskland; 1884–85 Berlinkonferensen; 1896 Adwa; 1905 unionen upplöses."),
 ("Förklara","Förklara tre orsaker till imperialismen.",[],None,"Råvaror, marknader, prestige/makt, idéer om civilisation. C: kopplar till industrialiseringen."),
 ("Jämför","Jämför enandet av Tyskland med unionsupplösningen 1905. Vad var lika och olika?",[],None,"Lika: nationalism låg bakom. Olika: Tyskland enades genom krig; 1905 upplöstes en union fredligt."),
 ("Kartövning","Rita av en karta över Afrika år 1870 och 1914 (en enkel skiss). Markera Etiopien och Liberia. Vad ser du?",[],None,"Nästan hela Afrika var kolonier 1914 utom Etiopien och Liberia."),
 ("Källa","Läs om Kongo i 8.4. Vilka problem finns med källorna, och varför är siffrorna osäkra?",[],None,"Kolonisatörer skrev för att försvara sig, de drabbade skrev sällan, ingen räknade systematiskt."),
 ("Perspektiv","Skriv en kort text där du beskriver Berlinkonferensen ur en europeisk och en afrikansk synvinkel.",[],None,"Europeiskt: regler och handel. Afrikanskt: ingen fick vara med, besluten påverkade deras land. A-nivå: kopplar till långsiktiga följder."),
 ("Jämför Kina och Japan","Förklara varför Kina och Japan fick så olika öden under 1800-talet.",[],None,"Kina tvingades till ojämlika fördrag; Japan moderniserades under Meiji och blev själv stormakt. Historiker nämner flera orsaker."),
 ("Orsakskedja","Rita en orsakskedja från nationalism och imperialism till att Europa delades i två block.",[],None,"Nationalism → rivalitet → upprustning → allianser → blocken. Imperialism → kamp om kolonier → spänningar."),
 ("Historiebruk","Välj en aktör och förklara hur den idag använder kolonialtiden i sin berättelse. Vilket syfte kan finnas?",[],None,"Bedöms: tydlig aktör, syfte, vad som lyfts fram eller utelämnas."),
]

BEGREPP = [
 ("Nationalism","Idén att en nation ska ha sin egen stat."),
 ("Nation","Folk som känner samhörighet genom språk, historia och kultur."),
 ("Nationalstat","Stat där de flesta tillhör samma nation."),
 ("Nationalromantik","Konströrelse som lyfte fram folkets historia och landskap."),
 ("Imperialism","Att en stat utvidgar sin makt genom att lägga under sig andra områden."),
 ("Imperium","Stort rike som styr över många områden och folk."),
 ("Koloni","Område som styrs av en annan stat."),
 ("Råvara","Material som behövs i tillverkning."),
 ("Marknad","Plats eller grupp där varor kan säljas."),
 ("Prestige","Anseende och status."),
 ("Rasism","Idé att människor kan rangordnas efter 'ras'."),
 ("Ojämlikt fördrag","Avtal där en part tvingas ge mycket."),
 ("Motstånd","Att kämpa emot förtryck eller främmande makt."),
 ("Allians","Avtal mellan stater om att hjälpa varandra."),
 ("Upprustning","Att bygga upp större arméer och flottor."),
 ("Historiebruk","Hur historia används i nutiden, av vem och varför."),
]

SAMMAN = [
 "Nationalism är idén att en nation ska ha en egen stat. Den kunde ge frihet men också skapa konflikter.",
 "Italien (1861) och Tyskland (1871) enades. Unionen mellan Sverige och Norge upplöstes fredligt 1905.",
 "Imperialismen drevs av råvaror, marknader, prestige och idéer om överlägsenhet. Industrialiseringen gjorde den möjlig.",
 "Afrika delades upp främst under 1880- och 1890-talen. Berlinkonferensen 1884–85 hölls utan afrikanska ledare. Kongofristaten blev ett exempel på hårt styre.",
 "Indien blev brittiskt efter 1858, och Kina tvingades till ojämlika fördrag efter opiumkrigen. Japan moderniserades och blev själv imperialistiskt.",
 "Rasism användes för att motivera kolonialism. Människor gjorde motstånd, till exempel i Indien och Etiopien.",
 "Allianser, upprustning och rivalitet delade Europa i två block och ökade risken för storkrig.",
 "Kolonialtiden används fortfarande i debatter om gränser, museer och rättvisa. Fråga alltid vem som berättar och varför.",
]

TEST_A = [
 ("Vad är en nationalstat?",["En stat där de flesta tillhör samma nation","En stat utan gränser","En koloni","En allians"],0),
 ("Vilket år utropades det tyska kejsardömet?",["1848","1861","1871","1905"],2),
 ("Vilken av dessa var INTE en orsak till imperialismen?",["Råvaror","Marknader","Prestige","Rösträtt för kvinnor"],3),
 ("Vilka deltog INTE i Berlinkonferensen 1884–85?",["Storbritannien","Frankrike","Afrikanska ledare","Tyskland"],2),
 ("Vem styrde Kongofristaten som sin privata egendom?",["Bismarck","Kung Leopold II av Belgien","Drottning Victoria","Kejsar Meiji"],1),
 ("Vad fick Storbritannien i freden i Nanjing 1842?",["Hongkong","Indien","Egypten","Japan"],0),
 ("Vilket land i Afrika besegrade en europeisk armé vid Adwa 1896?",["Liberia","Etiopien","Kongo","Egypten"],1),
 ("Vilka länder ingick i trippelententen 1907?",["Tyskland, Italien, Österrike-Ungern","Storbritannien, Frankrike, Ryssland","Sverige, Norge, Danmark","USA, Japan, Kina"],1),
]

TEST_B = [
 ("Ge ett exempel på hur nationalism kan vara både positivt och negativt.","Positivt: frihet och gemenskap. Negativt: konflikter och utestängning av minoriteter."),
 ("Förklara varför Tyskland och Italien ville ha kolonier.","De hade nyss enats och ville visa att de var stormakter (prestige), och behövde råvaror och marknader."),
 ("Vad innebär ojämlikt fördrag? Ge ett exempel.","Avtal där en part tvingas ge mycket och får lite. Exempel: freden i Nanjing 1842."),
 ("Hur upplöstes unionen mellan Sverige och Norge 1905?","Fredligt: Stortinget förklarade den upplöst 7 juni, folkomröstning i augusti, förhandlingar i Karlstad, och 26 oktober avstod Oscar II."),
 ("Ge två exempel på motstånd mot kolonialism.","T.ex. sepoyupproret i Indien 1857, Etiopiens seger vid Adwa 1896, Indiska nationalkongressen."),
 ("Förklara hur allianser kunde göra en konflikt större.","När ett land angreps skulle dess allierade hjälpa det, och därför drogs fler länder in."),
]

KALLA = dict(
 text="Våra rättigheter att styra i Kongo bygger på avtal med de lokala hövdingarna, som har skrivit under och fått gåvor. Vi för med oss ordning, handel och kristendom, och folket får bättre liv.",
 ursprung="Konstruerad källa baserad på hur européer på 1880-talet beskrev sin närvaro i Kongo. Skriven som ett officiellt uttalande från en europeisk kolonialtjänsteman.",
 fragor=[("Vem skriver, och vad är syftet?","En europeisk tjänsteman som vill visa att styret är lagligt och välvilligt, för sin regering och en europeisk allmänhet."),
         ("Vilka argument använder skribenten för kolonialt styre?","Avtal med hövdingar, ordning, handel och kristendom."),
         ("Vilka perspektiv saknas i källan?","Kongos invånares egna röster, och vad de förstod av avtalen."),
         ("Hur kan du kontrollera om källan stämmer?","Jämföra med andra källor, t.ex. missionärers rapporter, Casements rapport och beskrivningar från kongoleser.")],
)

SKRIV = dict(
 uppgift="Skriv en text på 300–400 ord: <strong>Varför ville stormakterna ha kolonier, och hur påverkade imperialismen både kolonisatörer och koloniserade?</strong> Ta med minst två orsaker, två exempel (t.ex. Kongo, Indien, Kina, Japan), ett exempel på motstånd och en reflektion om hur kolonialtiden används eller diskuteras idag.",
 stod=["E: Du beskriver några orsaker till imperialismen och ger enkla exempel på följder. Du använder några centrala begrepp (koloni, imperialism, råvaror).",
       "C: Du förklarar flera orsaker och hur de hänger ihop, jämför olika områden och visar hur olika grupper påverkades. Du ger exempel på motstånd och använder begreppen säkert.",
       "A: Du värderar orsakernas betydelse och visar att historiker tolkar olika. Du analyserar långsiktiga följder och ser flera perspektiv, och granskar hur kolonialtiden används idag."],
)

LAB = dict(
 titel="Historikerns verkstad: Berlinkonferensen – rollspel och kartövning",
 syfte="Eleverna övar att se en händelse ur flera perspektiv, att analysera orsaker och följder, och att använda karta som källa.",
 material="Blankokarta över Afrika, rollkort (Storbritannien, Frankrike, Tyskland, Portugal, Belgien, afrikansk ledare/observatör), penna, klocka, kopia av 8.4.",
 utforande=["Dela klassen i grupper. Varje grupp får ett rollkort. En grupp spelar en afrikansk ledare som får se på utanför rummet.",
            "Läs 8.4 och skriv ned vad din roll vill uppnå och varför.",
            "Förhandla 10 minuter om regler för hur man ska kunna hävda ett område. Observatörerna antecknar.",
            "Rita på blankokartan hur Afrika kan ha sett ut 1870 och 1914 (utgå från din lärobok eller atlas).",
            "Observatörerna berättar hur de upplevde att inte få delta. Vad hade de velat säga?",
            "Diskutera: Vilka långsiktiga följder fick det att afrikanska ledare saknades?"],
 fragor=[("Vilka argument använde stormakterna?","T.ex. handel, ordning, mission, ”civilisation”, att undvika krig mellan sig."),
         ("Vad kände observatörerna?","Maktlöshet, ilska, att besluten påverkade dem utan att de fick säga något."),
         ("Hur påverkade beslutet Afrika på lång sikt?","Gränser drogs utan hänsyn till folk, ekonomier byggdes för export, kolonialt styre.")],
 bonus="För läraren: Knyt an till att forskare påpekar att konferensen inte i sig drog gränser utan satte regler som ökade kapplöpningen. Bedöm perspektivtagande (E: kan beskriva en roll; C: kan förklara varför olika roller tyckte olika; A: kan värdera källor och tolkningar och dra slutsatser om långsiktiga följder). Variant: byt kartan mot en jämförelse mellan en politisk karta idag och en av 1914.",
)

LARAR = [
 ("Koppling till Lgr22","Kapitlet täcker syftets mål om kunskaper om händelser, aktörer och förändringsprocesser, historiska begrepp, källkritik och historiebruk. Centralt innehåll: imperialism och världskrig ca 1850–1950 (imperialismens orsaker och följder, nationalism, motstånd). Kunskapskraven rör orsak och konsekvens, perspektiv, kontinuitet och förändring, källor samt historiebruk."),
 ("Förslag på upplägg (8 lektioner)","1. Nationalism och nationalstater (8.1). 2. Italien, Tyskland, Norge 1905 (8.2). 3. Varför imperialism? (8.3). 4. Afrika och Kongo (8.4, med känslighet). 5. Indien och Kina (8.5). 6. Japan och jämförelse (8.6). 7. Rasism, motstånd och följder (8.7). 8. Allianser, väg mot kriget och historiebruk (8.8, F4)."),
 ("Vanliga missuppfattningar","Att Berlinkonferensen ritade alla gränser. Att alla européer stödde imperialismen. Att kolonierna var passiva och inte gjorde motstånd. Att Sverige inte alls hade kopplingar till kolonialismen (S:t Barthélemy, deltagande i Kongo, Berlinkonferensen). Att nationalism alltid är något negativt eller alltid något positivt."),
 ("Bedömningsstöd E/C/A","E: eleven beskriver orsaker och följder av imperialism och nationalism med enkla exempel. C: eleven förklarar samband, jämför områden och perspektiv, och gör en enkel källanalys. A: eleven värderar orsakernas betydelse, ser olika tolkningar, analyserar källor och historiebruk och drar slutsatser om långsiktiga följder."),
 ("Tips för Blooket och Jeopardy (10 kategorier)","1. Nationalism och begrepp. 2. Italien och Tyskland. 3. Norge 1905. 4. Orsaker till imperialism. 5. Afrika och Berlinkonferensen. 6. Kongo (hantera sakligt). 7. Indien och Kina. 8. Japan. 9. Allianser. 10. Historiebruk. Exempel: ”I vilken sal i Versailles utropades det tyska kejsardömet 1871?” (Spegelsalen)."),
]

KALLOR = [
 ("Skolverket – Kommentarmaterial till kursplanen i historia, grundskolan (2022)","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
 ("Britannica – Berlin West Africa Conference","https://britannica.com/print/article/62214"),
 ("Store norske leksikon – Unionsoppløsningen i 1905","https://snl.no/Unionsoppl%C3%B8sningen_i_1905"),
 ("Store norske leksikon – Fristaten Kongo","https://snl.no/Fristaten_Kongo"),
 ("Wikipedia (vägvisare) – Unification of Germany","https://en.wikipedia.org/wiki/Unification_of_Germany"),
 ("Wikipedia (vägvisare) – Treaty of Nanking","https://en.wikipedia.org/wiki/Treaty_of_Nanking"),
 ("History Skills – Meiji Restoration Lesson","https://historyskills.com/classroom/modern-history/meiji-restoration"),
 ("UK Parliament – Government of the Raj, 1858–1914","https://webtest.parliament.uk/about/living-heritage/evolutionofparliament/legislativescrutiny/parliament-and-empire/parliament-and-the-american-colonies-before-1765/government-of-the-raj-1858-1914"),
 ("History.com – The Battle of Adwa","https://www.history.com/news/battle-adwa-ethiopia-africa-colonization"),
 ("World History Encyclopedia – The Pre-WWI Alliance System","https://www.worldhistory.org/article/2808"),
 ("NC State (Slatta) – Kipling, The White Man's Burden, 1899","https://faculty.chass.ncsu.edu/slatta/hi216/documents/kipling.htm"),
]

F_UPPG = [
 ("●","Förklara varför dödssiffrorna för Kongo är osäkra.",[],None,"Ingen räknade systematiskt, källorna är ofullständiga och många dog av sjukdom och svält."),
 ("●●","Jämför tre förklaringar till imperialismen och ge ett exempel för varje.",[],None,"Ekonomisk (gummi/Kongo), politisk (hamnar/prestige), kulturell (civilisationsuppdrag)."),
 ("●●","Förklara varför Etiopien kunde stå emot Italien 1896.",[],None,"Stor armé, moderna gevär, stark stat, dålig italiensk information."),
 ("●●●","Analysera hur en aktör idag (stat, museum, rörelse) använder kolonialtiden. Vad lyfts fram och vad utelämnas?",[],None,"Bedöms: tydlig aktör, syfte, urval, kritisk granskning."),
 ("●●●","Diskutera: Var Berlinkonferensen avgörande för Afrikas uppdelning eller bara en del av en längre process?",[],None,"Konferensen satte regler men gränserna drogs senare; uppdelningen hade börjat tidigare. Bedömning av resonemang."),
]

F_SAMMAN = [
 "Källor om Kongo har olika brister, och därför är siffrorna osäkra.",
 "Historiker förklarar imperialismen på olika sätt: ekonomiskt, politiskt och kulturellt.",
 "Etiopien stod emot kolonisering och segern vid Adwa blev en symbol.",
 "Berlinkonferensen drog inte själv gränserna, men kolonialtiden påverkar fortfarande Afrika.",
]

F_BEGR = [
 ("Källkritik","Att granska hur trovärdig en källa är."),
 ("Tolkning","Förklaring av vad något betyder, som kan skilja sig mellan forskare."),
 ("Symbol","Något som står för en större idé."),
 ("Kolonialt arv","Följder av kolonialtiden som finns kvar idag."),
 ("Restitution","Att lämna tillbaka föremål eller ge upprättelse."),
]

BLOOKET = [
 ("Vad är nationalism?","Idén att en nation ska ha en egen stat","Idén att alla människor är lika","Idén att kungar ska styra","Idén att handel ska vara fri"),
 ("Vad kallas en stat där de flesta tillhör samma nation?","Nationalstat","Koloni","Allians","Imperium"),
 ("Vilket år utropades kungariket Italien?","1861","1771","1871","1905"),
 ("Vem ledde Preussen och Tysklands enande?","Otto von Bismarck","Garibaldi","Napoleon","Leopold II"),
 ("Var utropades det tyska kejsardömet 1871?","Spegelsalen i Versailles","Berlin","Wien","London"),
 ("Vilket år upplöstes unionen mellan Sverige och Norge?","1905","1814","1871","1918"),
 ("Hur upplöstes unionen mellan Sverige och Norge?","Fredligt efter förhandlingar","Genom ett stort krig","Genom en revolution","Genom en jordbävning"),
 ("Vad betyder imperialism?","Att en stat lägger under sig andra områden","Att en nation enas","Att man sluter fred","Att man bygger järnvägar"),
 ("Vad kallas ett område som styrs av en annan stat?","Koloni","Nation","Union","Allians"),
 ("Vilken var INTE en orsak till imperialismen?","Fler rättigheter för kvinnor","Råvaror","Marknader","Prestige"),
 ("Vilken svensk koloni låg i Karibien?","S:t Barthélemy","Kuba","Jamaica","Haiti"),
 ("Vilken konferens hölls 1884–85?","Berlinkonferensen","Versaillesfreden","Wienkongressen","Münchenkonferensen"),
 ("Vem var inte med vid Berlinkonferensen?","Afrikanska ledare","Storbritannien","Frankrike","Tyskland"),
 ("Vilken kung styrde Kongofristaten?","Leopold II","Vilhelm I","Oscar II","Menelik II"),
 ("Vilken vara tvingades kongoleser samla in?","Gummi","Silver","Kaffe","Bomull"),
 ("Vilket år övertog den belgiska staten Kongo?","1908","1885","1914","1870"),
 ("Vilket land besegrade Italien vid Adwa 1896?","Etiopien","Kina","Indien","Japan"),
 ("Vilket område fick Storbritannien genom freden i Nanjing 1842?","Hongkong","Singapore","Indien","Korea"),
 ("Vilket krig handlade om handel med opium?","Opiumkriget","Krimkriget","Boerkriget","Trettioåriga kriget"),
 ("Vad hände i Indien 1858?","Kronan tog över styret","Landet blev självständigt","Britterna lämnade","Kina invaderade"),
 ("Vilken organisation bildades 1885 i Indien?","Indiska nationalkongressen","Ostindiska kompaniet","Nationernas förbund","Röda korset"),
 ("Vilket år kom Perry till Japan?","1853","1703","1868","1914"),
 ("Vad kallas perioden efter 1868 i Japan?","Meijiperioden","Edoperioden","Tangperioden","Qingperioden"),
 ("Vilka ingick i trippelententen?","Storbritannien, Frankrike, Ryssland","Tyskland, Italien, Österrike","Sverige, Norge, Danmark","USA, Mexiko, Kanada"),
 ("Vad betyder allians?","Avtal om att hjälpa varandra","Avtal om handel","Krigsförklaring","Fredsavtal"),
 ("Vilket år bildades trippelententen?","1907","1879","1894","1919"),
]

JEOPARDY = {
 "Nationalism": [
  (100,"Idén att en nation ska ha en egen stat","Vad är nationalism?"),
  (200,"Stat där de flesta tillhör samma nation","Vad är en nationalstat?"),
  (300,"Konströrelse som lyfte fram folkets historia och landskap","Vad är nationalromantik?"),
  (400,"Året då kungariket Italien utropades","Vad är 1861?"),
  (500,"Den man som ledde Tysklands enande under Preussen","Vem är Otto von Bismarck?")],
 "Imperialism": [
  (100,"Område som styrs av annan stat","Vad är en koloni?"),
  (200,"Material som fabriker behövde, t.ex. gummi eller bomull","Vad är råvaror?"),
  (300,"Tre sorters orsaker: råvaror, marknader och detta","Vad är prestige?"),
  (400,"Fartyg som drevs av ånga och kunde ta sig upp längs floder i Afrikas inland","Vad är ångbåten?"),
  (500,"Svensk koloni i Karibien 1784–1878","Vad är S:t Barthélemy?")],
 "Afrika": [
  (100,"Staden där stormakterna samlades 1884–85","Vad är Berlin?"),
  (200,"De som saknades på Berlinkonferensen","Vilka är afrikanska ledare?"),
  (300,"Land som besegrade Italien 1896","Vad är Etiopien?"),
  (400,"Belgisk kung som styrde Kongo som privat egendom","Vem är Leopold II?"),
  (500,"År då Belgien tog över Kongo","Vad är 1908?")],
 "Asien": [
  (100,"Område som den brittiska kronan styrde direkt från 1858","Vad är Indien?"),
  (200,"Varan som orsakade krig i Kina","Vad är opium?"),
  (300,"Området Storbritannien fick 1842","Vad är Hongkong?"),
  (400,"Perioden då Japan moderniserades","Vad är Meijiperioden?"),
  (500,"Så kallas avtal där Kina fick ge mycket och få lite tillbaka","Vad är ojämlika fördrag?")],
 "Mot kriget": [
  (100,"Avtal mellan stater om att hjälpa varandra","Vad är en allians?"),
  (200,"Storbritannien, Frankrike och Ryssland 1907","Vad är trippelententen?"),
  (300,"Att bygga upp större arméer och flottor","Vad är upprustning?"),
  (400,"Område där serber ville bilda egen stat och där spänningarna var stora","Vad är Balkan?"),
  (500,"Nästa kapitels krig som började 1914","Vad är första världskriget?")],
}

GRUPPER = [
 ("nation","Nationalism och nya stater","Vad nationalism är, och hur Italien, Tyskland och Norge blev nationalstater.",["nationalism","enande","varfor"]),
 ("varlden","Afrika och Asien","Hur Afrika delades upp och hur Indien, Kina och Japan påverkades.",["afrika","indienkina","japan"]),
 ("ideer","Idéer, motstånd och vägen mot kriget","Rasism, motstånd, följder och spänningarna mellan stormakterna.",["ideologi","vagen"]),
]

SCEN = dict(
 titel="Tidsresa genom imperialismens tidsålder", plats="Från Kina via Indien och Afrika till Europa", tid="1842–1914",
 sky=("#c9b78e","#f0e2c0"), mark="#8a6d3b",
 walker=dict(typ="resenar"),
 etapper=[
  dict(x_etikett="Nanjing", tid="1842", plats="Nanjing, Kina", rubrik="Freden efter opiumkriget",
   fakta=["Ombord på ett brittiskt krigsfartyg skriver man under ett avtal. Britterna har vunnit kriget mot Kina.","Kina måste ge Hongkong till Storbritannien och öppna flera hamnar för brittisk handel. Många i Kina kallar avtalet orättvist."],
   fraga="Vad fick Storbritannien i freden i Nanjing?", alt=["Hongkong och öppnade hamnar","Hela Kina","Egypten"], ratt=0,
   forklaring="Hongkong blev brittiskt, och hamnar öppnades för handel.", deko=[("hamn",-80,1.1),("segelfartyg",100,1.2),("kanon",200,0.8)]),
  dict(x_etikett="Indien", tid="1858", plats="Indien", rubrik="Kronan tar över",
   fakta=["Året innan gjorde indiska soldater uppror mot britterna. Upproret slogs ned.","1858 tar den brittiska kronan över styret av Indien. Förut styrde ett brittiskt handelsföretag. Indien blir det värdefullaste området i det brittiska imperiet."],
   fraga="Vad hände i Indien 1858?", alt=["Landet blev självständigt","Den brittiska kronan tog över styret","Kina invaderade landet"], ratt=1,
   forklaring="Efter upproret styrdes Indien direkt av den brittiska kronan.",
   ord=[("imperium","stort välde där en makt styr över många länder")],
   deko=[("folkmassa",-80,1.0),("palm",90,1.2),("slott",190,1.0)]),
  dict(x_etikett="Japan", tid="1868", plats="Japan", rubrik="Japan moderniseras",
   fakta=["Amerikanska krigsfartyg tvingade Japan att öppna hamnar 1853. Japan ville inte bli svagt som Kina.","1868 börjar Meijiperioden. Japan bygger snabbt fabriker, skolor och en modern armé. Landet behåller sitt oberoende och blir själv en stormakt som tar kolonier."],
   fraga="Vad var annorlunda med Japan jämfört med Kina?", alt=["Japan moderniserade sig snabbt och blev själv stormakt","Japan blev en brittisk koloni","Japan stängde alla hamnar för alltid"], ratt=0,
   forklaring="Japan gjorde snabba reformer och blev själv en stormakt.",
   ord=[("koloni","land som styrs av ett annat land")],
   deko=[("fabrik",-60,1.1),("skola",110,1.0),("berg",200,1.2)]),
  dict(x_etikett="Berlin", tid="1884–85", plats="Berlin", rubrik="Berlinkonferensen",
   fakta=["Politiker från 14 stater, de flesta europeiska, samlas i Berlin. De ska bestämma regler för handel och för vem som får ta områden i Afrika.","Ingen afrikansk ledare är med. Besluten fattas utan dem som bor där."],
   fraga="Vilka fick inte vara med på Berlinkonferensen?", alt=["Afrikas ledare","Tysklands ledare","Storbritanniens ledare"], ratt=0,
   forklaring="Besluten togs utan de människor som bodde i Afrika.", deko=[("riksdagshus",-60,1.2),("flagga_rod",100,0.9),("jordglob",190,0.9)]),
  dict(x_etikett="Adwa", tid="1896", plats="Adwa, Etiopien", rubrik="Motstånd i Etiopien",
   fakta=["Italien vill göra Etiopien till koloni och skickar en armé. Etiopiens kejsare Menelik II samlar en stor armé med moderna gevär.","Etiopierna vinner slaget vid Adwa. Etiopien förblir självständigt. Slaget blir en symbol för motstånd i Afrika."],
   fraga="Vilket land besegrade Italien i slaget vid Adwa 1896?", alt=["Egypten","Etiopien","Kongo"], ratt=1,
   forklaring="Etiopien vann vid Adwa och behöll sin frihet.", deko=[("berg",-120,1.4),("soldat_grupp",70,1.1),("flagga_rod",190,0.9)]),
  dict(x_etikett="Kongo", tid="1904", plats="Kongo", rubrik="Rapporten om Kongo",
   fakta=["Kung Leopold II av Belgien har fått Kongo som sin privata egendom. Människor tvingas samla gummi och straffas hårt.","Roger Casement skriver en rapport om det som händer. Protesterna växer. 1908 tar den belgiska staten över Kongo från kungen."],
   fraga="Vem hade styrt Kongo som sin privata egendom fram till 1908?", alt=["Kung Leopold II","Menelik II","Roger Casement"], ratt=0,
   forklaring="Leopold II styrde Kongo 1885–1908. Sedan tog Belgien över.", deko=[("flod",-100,1.2),("palm",90,1.3),("angbat",190,0.9)]),
  dict(x_etikett="Europa", tid="1907–1914", plats="Europa", rubrik="Sammanfattning: spänningar och två block",
   fakta=["Stormakterna rustar upp och tävlar om kolonier. De ingår också allianser, alltså avtal om att hjälpa varandra om det blir krig.","1907 bildas trippelententen. Då delas Europa i två block. I nästa kapitel möter du kriget."],
   ord=[("imperialism","när stora länder tar över andra länder för makt och rikedom"),("allians","avtal om att hjälpa varandra i krig")],
   deko=[("jordglob",-80,1.0),("flagga_bla",70,0.9),("soldat_grupp",190,1.0)]),
 ],
 diskutera="Imperialismen gav stormakterna makt men skapade också motstånd. Hur såg de som styrde och de som styrdes på saken?",
)
