# -*- coding: utf-8 -*-
# Kapitel 4 – Antikens Rom (åk 7). Historia, Pluggis.
T = dict(
 nr=4, namn="Antikens Rom", under="Från en liten stad vid Tibern till ett världsrike – och vad som finns kvar",
 kort="Historia · Kapitel 4", fil="historia-04-rom", arskurs=7, nodeid="historia-rom",
 mal=["berätta om Roms grundande och skilja myt från historia",
      "förklara hur republiken styrdes och varför den kom att förändras",
      "beskriva hur Rom växte genom krig, till exempel mot Karthago",
      "förklara hur Julius Caesar och Augustus ändrade Roms styre",
      "jämföra olika grupper i det romerska samhället och deras villkor",
      "förklara hur armén och vägarna höll ihop riket",
      "förklara varför kristendomen spreds och varför Västrom föll år 476",
      "ge exempel på vad Rom har lämnat efter sig och hur Rom används i dag"],
 fundera="Rom är över 2 000 år gammalt, men du ser spår av staden i filmer, ord och byggnader. Skriv ned tre saker i ditt eget liv som du tror har med Rom att göra.",
)

S = []

S.append(dict(id="grundande", nr="4.1", ikon="🐺", titel="Rom grundas – myt och historia",
 intro="Rom började som en liten by vid floden Tibern i Italien. Romarna själva berättade en berömd saga om hur staden kom till. Historiker har ett annat sätt att ta reda på vad som hände.",
 block=[
  ("p","Enligt sagan var tvillingarna <strong>Romulus och Remus</strong> söner till krigsguden Mars. Som bebisar kastades de ut i floden men räddades av en varginna som ammade dem. När de blev stora grundade Romulus en stad på kullen Palatinen. Romarna räknade att det skedde år <strong>753 f.Kr.</strong>"),
  ("p","Sagan säger också att Romulus dödade sin bror i ett bråk om vem som skulle styra. Det är en myt, alltså en berättelse som människor förde vidare muntligt och som inte går att bevisa. Myter säger ändå något om hur ett folk såg på sig självt: romarna var stolta över att vara hårda och krigiska."),
  ("p","Arkeologer tolkar saken på ett annat sätt. De har hittat spår av bosättningar på Roms kullar från omkring 900-talet f.Kr. Läget var bra. Det fanns ett vadställe över Tibern, mat från bördig jord och en väg som handlare använde. Små byar växte så småningom ihop till en stad."),
  ("tidslinje",[("753 f.Kr.","Rom grundas enligt traditionen"),("700-talet f.Kr.","Kungar styr staden"),("509 f.Kr.","Kungen fördrivs, republiken införs"),("264 f.Kr.","Första kriget mot Karthago börjar"),("44 f.Kr.","Julius Caesar mördas"),("27 f.Kr.","Augustus blir förste kejsare"),("476 e.Kr.","Västroms siste kejsare avsätts")]),
  ("ruta","tank","Myt eller fakta?","Ingen vet säkert om Romulus någonsin fanns. Romarna skrev ner sagan flera hundra år efter att den påstods ha hänt. Vad betyder det för hur mycket vi kan lita på den som källa till Roms tidiga historia?"),
  ("kolla",["Vilket år räknade romarna att staden grundades?","Vad är en myt?","Vilka spår har arkeologerna hittat som visar att Rom var en bra plats att bo på?"]),
 ],
 svar=["753 f.Kr.","En berättelse som förs vidare och som inte går att bevisa, men som säger något om hur ett folk ser på sig självt.","Bosättningar från omkring 900-talet f.Kr., ett vadställe över Tibern, bördig jord och en handelsväg."],
))

S.append(dict(id="republik", nr="4.2", ikon="🏛️", titel="Republiken – senaten och konsulerna",
 intro="De första kungarna i Rom hade stor makt. Omkring år 509 f.Kr. var romarna så trötta på kungen att de jagade bort honom. Då bestämde de att aldrig mer ha en ensam härskare.",
 block=[
  ("p","Det nya styret kallades <strong>res publica</strong>, ”folkets sak”. Därifrån kommer ordet <strong>republik</strong>. Makten delades mellan flera. Det skulle vara svårt för en enda man att ta över."),
  ("tab",["Institution","Vad den gjorde"],[
    ["Konsuler (2 st)","Leder staten och armén. Väljs för ett år. Kan hindra varandra."],
    ["Senaten","Några hundra rika och erfarna män. Ger råd om lagar, pengar och krig. Ledamöterna satt i regel på livstid."],
    ["Folkförsamlingar","Medborgare (män) röstar om lagar och väljer ämbetsmän."],
    ["Folktribuner","Skyddar plebejerna. Kan stoppa beslut med ordet <em>veto</em>, ”jag förbjuder”."]]),
  ("p","Den romerska republiken var <strong>ingen demokrati</strong> som vår. Kvinnor, slavar och människor utan medborgarskap fick inte rösta. De rikaste hade störst inflytande. Ändå var tanken att makten ska delas och kontrolleras viktig, och den har påverkat många senare stater."),
  ("p","Under de första århundradena kämpade vanliga människor, <strong>plebejer</strong>, för mer rättigheter mot de gamla förmögna släkterna, <strong>patricierna</strong>. Plebejerna hotade bland annat att lämna staden. Efter hand fick de egna företrädare och till slut kunde även de bli konsuler. Omkring 450 f.Kr. skrevs lagarna ner på tolv tavlor så att alla kunde se vad som gällde."),
  ("ruta","fakta","Ordet veto","Ordet <em>veto</em> är latin och betyder ”jag förbjuder”. Vi använder det än i dag när någon har rätt att stoppa ett beslut, till exempel i FN:s säkerhetsråd."),
  ("kolla",["Varför hade Rom två konsuler och inte en?","Nämn två grupper som inte fick rösta i republiken.","Vad var skillnaden mellan patricier och plebejer?"]),
 ],
 svar=["För att ingen ensam person skulle få för stor makt – de kunde hindra varandra och byttes ut varje år.","T.ex. kvinnor och slavar (även människor utan medborgarskap).","Patricierna var de gamla förmögna släkterna med mest makt. Plebejerna var vanliga medborgare som kämpade för fler rättigheter."],
))

S.append(dict(id="expansion", nr="4.3", ikon="🐘", titel="Roms expansion och krigen mot Karthago",
 intro="Från att ha varit en stad i Italien blev Rom på några hundra år härskare över hela Medelhavet. Den största motståndaren var staden Karthago i Nordafrika.",
 block=[
  ("p","Först erövrade Rom resten av Italien, ofta genom krig men också genom förbund. Besegrade städer fick ofta behålla en del självstyre om de skickade soldater till Rom. Sedan såg Rom ut över havet. Där låg <strong>Karthago</strong>, en rik handelsstad i nuvarande Tunisien, med en stor flotta."),
  ("p","Kriget mellan Rom och Karthago kallas <strong>puniska krigen</strong> eftersom romarna kallade karthagerna för ”puner”. Det var tre krig under drygt hundra år, mellan <strong>264 och 146 f.Kr.</strong> Rom byggde en egen flotta och lärde sig sjökrig."),
  ("p","Under andra kriget tog den karthagiske fältherren <strong>Hannibal</strong> sig år 218 f.Kr. med en stor här och krigselefanter över Alperna och anföll Italien. Han vann stora slag, bland annat vid Cannae 216 f.Kr. Ändå vägrade Rom ge upp. Den romerske generalen Scipio förde i stället kriget till Afrika och segrade vid Zama 202 f.Kr."),
  ("p","I tredje kriget förstördes staden Karthago år 146 f.Kr. Rom styrde nu över Medelhavet. Platserna man erövrade kallades <strong>provinser</strong> och betalade skatt till Rom. Pengar och slavar strömmade in, vilket förändrade samhället."),
  ("ruta","tank","Orsak och konsekvens","Att Rom vann gav makt, rikedom och billig arbetskraft i form av slavar. Men många bönder hade varit borta i krig i åratal och förlorade sina gårdar. Hur kan en seger i krig skapa nya problem hemma?"),
  ("kolla",["Mellan vilka år varade puniska krigen?","Vad gjorde Hannibal som blev berömt?","Nämn en konsekvens av att Rom vann."]),
 ],
 svar=["264–146 f.Kr.","Han tog en här med elefanter över Alperna 218 f.Kr. och anföll Italien.","T.ex. Rom fick makt över Medelhavet, skatter och slavar; många bönder förlorade sina gårdar."],
))

S.append(dict(id="kejsare", nr="4.4", ikon="🗡️", titel="Caesar och kejsardömet",
 intro="När Rom blev rikt och mäktigt började mäktiga generaler slåss om makten. Republikens regler räckte inte längre till. Det tog slut med inbördeskrig och med att en enda man styrde.",
 block=[
  ("p","<strong>Julius Caesar</strong> var en skicklig general och politiker. Han erövrade Gallien (ungefär dagens Frankrike) 58–50 f.Kr. Senaten blev rädd för hans makt och krävde att han skulle lämna ifrån sig sin armé. År 49 f.Kr. gick Caesar i stället över floden Rubicon med sina soldater. Uttrycket ”att gå över Rubicon” betyder än i dag att fatta ett beslut det inte går att ta tillbaka."),
  ("p","Caesar vann inbördeskriget och blev diktator på livstid. Många gillade honom, andra fruktade att han ville bli kung. Den <strong>15 mars år 44 f.Kr.</strong> mördades han av en grupp senatorer. De ville rädda republiken, men resultatet blev nya inbördeskrig."),
  ("p","Caesars adoptivson <strong>Octavianus</strong> segrade till slut och år 27 f.Kr. fick han hederstiteln <strong>Augustus</strong>, ”den upphöjde”. Han lät senaten och konsulerna finnas kvar men höll i verkligheten all makt. Därmed var Rom ett <strong>kejsardöme</strong>. Titeln ”kejsare” kommer från namnet Caesar."),
  ("p","Augustus tid blev början på <strong>Pax Romana</strong>, ”den romerska freden”, en period på omkring 200 år med få stora krig inne i riket. Det var ett exempel på <em>kontinuitet och förändring</em>: många gamla institutioner fanns kvar till namnet, men makten låg nu hos en person."),
  ("kalla","Konstruerad källa, fritt efter Suetonius","”Jag fann Rom byggt av tegel och lämnar det efter mig byggt av marmor.”","Konstruerad källa i anslutning till en känd uppgift hos historieskrivaren Suetonius om Augustus (skriven omkring 100 år efter hans död). Visar hur kejsaren ville bli ihågkommen – men var skriven långt senare."),
  ("kolla",["Vad innebar det att Caesar gick över Rubicon?","Vad hände den 15 mars 44 f.Kr.?","Vilken skillnad fanns mellan republiken och kejsardömet?"]),
 ],
 svar=["Han tog sin armé in i Italien mot senatens vilja – ett beslut utan återvändo som ledde till inbördeskrig.","Caesar mördades av senatorer.","I republiken delades makten mellan flera, i kejsardömet höll en enda man den verkliga makten."],
))

S.append(dict(id="samhalle", nr="4.5", ikon="⚖️", titel="Samhället – medborgare och slavar",
 intro="Det romerska samhället var uppdelat i grupper med mycket olika rättigheter. Vilken grupp du föddes i avgjorde mycket av ditt liv.",
 block=[
  ("tab",["Grupp","Vilka och vad de kunde"],[
    ["Senatorer","Mycket rika familjer med stort politiskt inflytande."],
    ["Riddare","Rika affärsmän, ämbetsmän och officerare."],
    ["Vanliga medborgare","Bönder, hantverkare, handlare och soldater. Fick rösta (männen) och skyddas av lagen."],
    ["Frigivna","Före detta slavar som friköpts eller frigetts. Fick ofta medborgarskap, men inte alla ämbeten."],
    ["Slavar","Ägdes som egendom och saknade rättigheter."]]),
  ("p","Slaveriet var en del av hela samhället. Slavar kom ofta från krig. Krigsfångar, och barn till slavar, såldes på marknader. Slavar arbetade på gods, i gruvor, i hushåll, som lärare och läkare. Forskare är oense om hur många de var, men uppskattar att de kunde utgöra en stor del av befolkningen, i Italien kanske var femte till var tredje person. Siffran är osäker."),
  ("p","Vissa slavar kunde köpa sig fria eller bli frigivna av sin ägare. Andra gjorde motstånd. Det mest kända upproret leddes av gladiatorn <strong>Spartacus</strong> åren 73–71 f.Kr. Tusentals slavar slöt upp, men Rom slog ner upproret."),
  ("p","<strong>Kvinnor</strong> fick inte rösta eller ha politiska ämbeten, men rika kvinnor kunde äga egendom och driva affärer. Fattiga kvinnor arbetade ofta med hantverk och handel. År 212 e.Kr. gav kejsar Caracalla medborgarskap till i stort sett alla fria människor i riket. Det förändrade vad ordet ”romare” betydde: det handlade nu mer om att tillhöra riket än om var du var född."),
  ("ruta","historia","Röster från de som inte skrev","Nästan alla bevarade texter är skrivna av rika, utbildade män. Slavarnas egna berättelser saknas nästan helt. Därför måste historiker ibland tolka gravstenar, föremål och lagtexter för att höra fler röster."),
  ("kolla",["Vad skilde en medborgare från en slav?","Hur kom många slavar till Rom?","Varför är det svårt att veta hur slavar själva upplevde sitt liv?"]),
 ],
 svar=["Medborgaren hade rättigheter och lagens skydd, slaven ägdes av någon annan som egendom.","Främst som krigsfångar (och som barn till slavar), som såldes på marknader.","Nästan alla bevarade texter är skrivna av rika män; slavarna skrev själva sällan eller så har det inte bevarats."],
))

S.append(dict(id="arme", nr="4.6", ikon="🛣️", titel="Armén, vägarna och vardagen",
 intro="Det romerska riket var enormt, som störst omkring år 117 e.Kr. Det hölls ihop av soldater, vägar och ett gemensamt sätt att leva.",
 block=[
  ("p","Armén bestod av <strong>legioner</strong> på ungefär 5 000 man. Legionärerna var tränade yrkessoldater som tjänstgjorde i omkring 25 år. De byggde också: broar, fort och vägar. Efter tjänsten kunde de få mark eller pengar, och soldater i hjälptrupperna fick ofta medborgarskap."),
  ("p","Romarna byggde stora mängder stenlagda vägar. Den äldsta stora vägen, <strong>Via Appia</strong>, byggdes redan omkring 312 f.Kr. Vägarna gjorde att soldater, post, handlare och nyheter kunde röra sig snabbt. Uppskattningsvis fanns tiotusentals kilometer stenlagda vägar. Därav kommer uttrycket ”alla vägar leder till Rom”."),
  ("p","I staden bodde de rika i huset <strong>domus</strong> med innergård. De flesta fattiga bodde i hyreshus, <em>insulae</em>, ofta flera våningar höga, trånga och brandfarliga. Rom hade på 100-talet e.Kr. ungefär en miljon invånare, en siffra som är osäker."),
  ("p","Romarna gick på <strong>termer</strong> (offentliga badhus) och på <strong>forum</strong>, torget där man handlade och diskuterade. Folk åt bröd, oliver, vin och grönsaker. Underhållningen var storslagen: kapplöpning med vagnar och gladiatorspel i <strong>Colosseum</strong>, som invigdes år 80 e.Kr. och rymde omkring 50 000 åskådare. Den romerske författaren Juvenalis hånade kejsarna för att de lugnade folket med ”bröd och skådespel”."),
  ("ruta","visste","Visste du?","Romerska <em>akvedukter</em> förde vatten till städerna i rännor och rör över långa sträckor, ofta med en lutning på bara någon enstaka promille. Flera står kvar i Spanien, Frankrike och Tunisien."),
  ("bild","rom","En romersk stad med torg, hyreshus och vattenledning."),
  ("kolla",["Vad var en legion och vad gjorde legionärerna förutom att strida?","Varför var vägarna viktiga för riket?","Vad var Colosseum?"]),
 ],
 svar=["En militär enhet på omkring 5 000 man; de byggde också vägar, broar och fort.","De gjorde att armé, post, handel och nyheter kunde förflytta sig snabbt och höll ihop riket.","En stor arena i Rom, invigd år 80 e.Kr., där man höll gladiatorspel och andra shower."],
))

S.append(dict(id="kristendom", nr="4.7", ikon="✝️", titel="Kristendomen växer fram",
 intro="De flesta romare dyrkade många gudar. Under kejsartiden spreds en ny tro som fick förändra hela Europa: kristendomen.",
 block=[
  ("p","Kristendomen började i provinsen Judeen, i östra delen av riket, med Jesus från Nasaret. Han avrättades av romarna under prefekten Pontius Pilatus, omkring år 30 e.Kr. Hans efterföljare menade att han hade uppstått och berättade om honom. Kristendomen spreds längs de romerska vägarna och sjövägarna, särskilt av aposteln Paulus."),
  ("p","Kristna vägrade att offra till kejsaren och till de romerska gudarna. Därför misstänktes de för att vara illojala. Vid flera tillfällen <strong>förföljdes</strong> de, bland annat efter branden i Rom år 64 e.Kr. under kejsar Nero. Ändå växte rörelsen. Många lockades av tanken att alla människor, även fattiga och slavar, var lika värda i Guds ögon och av omsorgen om de sjuka."),
  ("p","Det avgörande skedde under 300-talet. År <strong>313</strong> gav kejsar Konstantin kristna rätt att utöva sin tro (Milanoediktet). År <strong>380</strong> blev kristendomen i praktiken rikets officiella religion under Theodosius I. Kejsar Konstantin flyttade också det viktigaste centret till staden Konstantinopel (invigd 330)."),
  ("p","Kyrkans organisation, med biskopar i städerna, liknade rikets och överlevde när staten föll. Latinet blev kyrkans språk. När Sverige senare kristnades, under medeltiden, var det den latinska kyrkan som kom hit."),
  ("kalla","Konstruerad källa, fritt efter Plinius brev till kejsar Trajanus","”Ni offrar inte till kejsarens gudar. Vad har ni att dölja?”","Konstruerad källa i en romersk ämbetsmans stil, omkring år 110 e.Kr. Visar hur romerska myndigheter kunde se på kristna – men vi ser bara myndighetens sida."),
  ("kolla",["Varför förföljdes kristna ibland?","Vad hände år 313 och år 380?","Varför kunde kyrkan överleva när riket föll?"]),
 ],
 svar=["De vägrade offra till kejsaren och gudarna och misstänktes för att vara illojala.","313: kristna fick utöva sin tro fritt. 380: kristendomen blev i praktiken rikets officiella religion.","Den hade en egen organisation med biskopar och ett gemensamt språk (latin) som fortsatte fungera."],
))

S.append(dict(id="fall", nr="4.8", ikon="🏚️", titel="Krisen och Västroms fall år 476",
 intro="Efter flera hundra år av makt började riket få allvarliga problem. Det var inte en enda händelse som fick det att falla, utan många saker över lång tid.",
 block=[
  ("p","Under 200-talet e.Kr. var riket i kris. Kejsare avlöste varandra snabbt, ofta mördade av sina egna soldater. Pengarna blev mindre värda (inflation) och priserna steg. Pest och dåliga skördar drabbade befolkningen. På gränserna trängde folkgrupper på."),
  ("p","Kejsar Diocletianus försökte omkring år 285 att rädda riket genom att dela upp styret på flera kejsare. År 395 delades riket varaktigt i en västlig och en östlig del. <strong>Östrom</strong> var rikare och med huvudstad i Konstantinopel. <strong>Västrom</strong> var svagare."),
  ("p","Under 300- och 400-talen flyttade grupper som goter, vandaler och hunner in. Vissa flydde undan andra, andra sökte land. År 410 intogs och plundrades själva Rom av visigoter. Västromerska arméer bestod alltmer av legosoldater."),
  ("p","År <strong>476</strong> avsatte den germanske befälhavaren Odovakar den siste västromerske kejsaren, en pojke som hette Romulus Augustulus. Därför brukar man säga att Västrom föll 476. Men för människorna på plats märktes det knappast som ett enskilt ögonblick. Östrom, senare kallat Bysantinska riket, fanns kvar ända till 1453."),
  ("ruta","tank","Orsaker – flera på en gång","Historiker är oense om vilken orsak som var viktigast: svag ekonomi, politiskt kaos, påtryckningar utifrån, pest eller att riket helt enkelt var för stort. Välj de två orsaker som du tycker väger tyngst och förklara varför."),
  ("kolla",["Vilken händelse brukar markera Västroms fall?","Nämn två orsaker till kris.","Vad hände med Östrom?"]),
 ],
 svar=["Att Odovakar avsatte kejsaren Romulus Augustulus år 476.","T.ex. inflation, snabba kejsarbyten, pest, påtryckningar från andra folk, för stort rike.","Det fanns kvar som Bysantinska riket till 1453."],
))

F = []
F.append(dict(id="f1", nr="F1", ikon="🔍", titel="Sidospår: Hur vet vi? Källor om Rom",
 intro="Det mesta vi vet om Rom kommer från källor. Men olika källor ger olika bilder, och inte alla har bevarats.",
 block=[
  ("p","Historiker skiljer mellan <strong>texter</strong> (som historieskrivare, brev och lagar), <strong>föremål</strong> (mynt, krukor, verktyg) och <strong>byggnader och inskrifter</strong>. Texterna är ofta skrivna av rika män som ville visa sin sida. Livius skrev om Roms grundande flera hundra år efter att det skulle ha skett."),
  ("p","Tacitus, Suetonius och Plutarchos skrev biografier och historia. De hade ofta en poäng: kejsare som man gillade framställdes bra, andra dåligt. Därför måste historikern fråga: <em>Vem skrev det, när, för vem och varför?</em> Det är grunden i källkritik."),
  ("p","Arkeologin hjälper till att kontrollera texterna. Mynt visar ekonomi, gravstenar visar vanliga människor, och väggmålningar i Pompeji visar hur människor bodde och vad de gillade. Pompeji begravdes av aska från vulkanen Vesuvius år 79 e.Kr."),
  ("ruta","exempel","Två källor, två bilder","En kejsare lät sätta upp en inskrift på ett torg som berättar hur mycket han gjort för folket. En skribent från senaten skriver en privat dagbok om samma kejsare som en tyrann. Båda är sanna ur sin synvinkel. Historikerns uppgift är att jämföra."),
  ("kolla",["Nämn tre sorters källor till Rom.","Varför måste man vara försiktig med texter skrivna av kejsarnas anhängare?","Vad kan en gravsten berätta som en historiebok inte kan?"]),
 ],
 svar=["T.ex. texter, föremål (mynt), byggnader, inskrifter, målningar.","De ville visa kejsaren från sin bästa sida och kan ha överdrivit eller hållit inne med kritik.","Hur vanliga människor levde, vad de jobbade med och hur de såg på sig själva."],
))

F.append(dict(id="f2", nr="F2", ikon="🇸🇪", titel="Sidospår: Rom och Sverige",
 intro="Sverige låg utanför det romerska riket. Ändå fanns kontakter, och Rom har påverkat Sverige på många sätt.",
 block=[
  ("p","I svenska gravar och fyndplatser från de första århundradena e.Kr. har man hittat romerska mynt, glas och bronskärl. Särskilt på Gotland och Öland. Det visar att varor och idéer vandrade långt norrut via handel, kanske genom mellanhänder."),
  ("p","Det latinska alfabetet kom till Sverige med kyrkan på medeltiden. Orden <em>kejsare</em>, <em>tegel</em>, <em>vin</em>, <em>kök</em>, <em>mynt</em> och <em>fönster</em> är lånade från latin. Och nästan alla svenska skolor lärde latin under flera hundra år."),
  ("p","Carl von Linné, som levde på 1700-talet, gav växter och djur latinska namn, och systemet används än i dag över hela världen. Därför heter fläderblomman <em>Sambucus nigra</em> både i Sverige och i Brasilien."),
  ("ruta","fakta","Svenska kyrkans språk","Fram till reformationen på 1500-talet hölls gudstjänsterna i Sverige på latin. Latin var även vetenskapens språk i Europa ända in på 1700-talet."),
  ("kolla",["Vad har man hittat i Sverige som visar kontakt med Rom?","Nämn två svenska ord som kommer från latin.","Varför har växter latinska namn?"]),
 ],
 svar=["Romerska mynt, glas och bronskärl, särskilt på Gotland och Öland.","T.ex. kejsare, tegel, vin, kök, mynt, fönster.","Latin var vetenskapens språk, och Linné skapade ett gemensamt namnsystem som används över hela världen."],
))

F.append(dict(id="f3", nr="F3", ikon="🎭", titel="Sidospår: Rom i film, politik och symboler",
 intro="Rom är en av historiens mest använda förebilder. Olika människor har lyft fram olika sidor för att nå sina egna mål. Det kallas <strong>historiebruk</strong>.",
 block=[
  ("p","I filmer och serier som <em>Gladiator</em> (2000) visas Rom som dramatiskt, farligt och fullt av intriger. Filmerna är spännande underhållning och bygger ibland på verkliga personer, men de förändrar eller hittar på mycket för att skapa en bra historia. Ett kommersiellt historiebruk: Rom säljer biljetter."),
  ("p","I politiken används Rom för att ge makt och tyngd. USA:s kongress sammanträder i en byggnad med kupol och pelare i romersk stil, och landet har en senat. Revolutionärer på 1700-talet såg sig som republikaner i romersk anda."),
  ("p","Diktatorer har också utnyttjat Rom. I Italien på 1920–40-talen kopplade Mussolinis fascistiska regim sig till det gamla Rom och lät bygga och gräva ut antika platser för att visa att Italien var ett nytt världsrike. Det är ett exempel på hur historia används politiskt, och på att det som lyfts fram sällan är hela bilden."),
  ("p","Även symboler lever kvar. Örnen, romerska siffror på urtavlor och namnet <em>Caesar</em> (i titlarna kejsare och tsar) finns kvar i dagens värld."),
  ("kolla",["Vad menas med historiebruk?","Vilka olika motiv kan någon ha när den använder Rom?","Vad är risken med att lära sig historia mest från filmer?"]),
 ],
 svar=["Hur och varför historia används idag av människor, grupper eller stater.","T.ex. underhållning och pengar (film), ge makt och tyngd (politik), propaganda (diktatorer).","Att fakta blandas med påhitt och att filmen väljer ut det som är spännande, inte det som är mest sant."],
))

GRUPPER = [
 ("grund","Roms början och republiken","Från sagan om Romulus till republikens regler och krigen mot Karthago.",["grundande","republik","expansion"]),
 ("kejsare","Från Caesar till kejsare","Hur republiken föll och hur samhället såg ut.",["kejsare","samhalle"]),
 ("riket","Riket, tron och fallet","Armén, vardagen, kristendomen och Västroms fall.",["arme","kristendom","fall"]),
]

UPPG = [
 ("Para ihop","Koppla ihop begreppet med rätt förklaring.",["Republik","Konsul","Senat","Plebej","Legion","Pax Romana"],["En vanlig medborgare","Romersk fred under kejsartiden","Statsskick utan kung","Militär enhet på omkring 5 000","Rådsförsamling av rika män","En av två ledare"],"1 – C, 2 – F, 3 – E, 4 – A, 5 – D, 6 – B"),
 ("Tidslinje","Sätt händelserna i rätt ordning: A) Caesar mördas, B) Rom grundas enligt traditionen, C) Västrom faller, D) Hannibal över Alperna, E) Milanoediktet.",[],None,"B (753 f.Kr.), D (218 f.Kr.), A (44 f.Kr.), E (313), C (476)"),
 ("Sant eller falskt?","Avgör om påståendena stämmer och rätta de som är falska.",["Kvinnor kunde rösta i Roms republik.","Rom hade två konsuler som valdes för ett år.","Puniska krigen fördes mot Karthago.","Augustus var Roms första kejsare.","Västrom föll år 1453."],None,"Falskt (kvinnor fick inte rösta); sant; sant; sant; falskt (476, 1453 gäller Östrom)"),
 ("Förklara","Förklara med egna ord skillnaden mellan en myt och en historisk källa. Använd historien om Romulus och Remus som exempel.",[],None,"Myten är en berättelse som förs vidare och som inte går att bevisa; en historisk källa är något från tiden, t.ex. ett föremål eller en text, som kan prövas. Arkeologi visar bosättningar medan myten ger en förklaring och en identitet."),
 ("Orsak och konsekvens","Svara på frågorna.",["Nämn en orsak till att Caesar gick över Rubicon.","Nämn en konsekvens av att Caesar mördades.","Varför blev Rom rikare efter puniska krigen?"],None,"Senaten krävde att han lämnade ifrån sig armén; inbördeskrig och Augustus makt; provinser, skatter och slavar."),
 ("Jämför","Jämför en rik senator och en slav i Rom. Skriv minst tre skillnader.",[],None,"T.ex. bostad (domus vs. i hushåll/gods), rättigheter (rösta, äga vs. ägdes), möjligheter (ämbeten vs. friköpning)."),
 ("Kartövning","Rita en enkel karta över Medelhavet. Markera Rom, Karthago, Alperna och Konstantinopel. Rita pilar för Hannibals väg.",[],None,"Rom i Italien, Karthago i nuvarande Tunisien, Alperna norr om Italien, Konstantinopel vid Bosporen (nuvarande Istanbul). Hannibal: Spanien – Alperna – Italien."),
 ("Arv","Hitta fem saker i ditt vardagsliv som kan härledas till Rom (ord, byggnader, kalender, lag, symboler).",[],None,"T.ex. ord som vin, kök, tegel; månaderna juli och augusti; romerska siffror; arkader/valv; lagprinciper; latinska bokstäver."),
 ("Skriv","Skriv ett kort dagboksinlägg som en slav, en legionär eller en rik romare år 100 e.Kr. Berätta om din dag med fakta från kapitlet.",[],None,"Bedöms med SKRIV-stödet: korrekta detaljer, rätt perspektiv och orsak–konsekvens."),
]

BEGREPP = [
 ("Myt","Berättelse som förs vidare och som inte går att bevisa."),
 ("Republik","Statsskick utan kung där makten delas."),
 ("Konsul","En av två ledare i republiken, vald för ett år."),
 ("Senat","Rådsförsamling av rika och erfarna män."),
 ("Patricier","Gamla förmögna släkter i Rom."),
 ("Plebejer","Vanliga medborgare i Rom."),
 ("Provins","Område som Rom erövrat och styrde över."),
 ("Kejsardöme","Statsskick där en kejsare har den verkliga makten."),
 ("Legion","Romersk militär enhet på ungefär 5 000 man."),
 ("Pax Romana","Romersk fred – ca 200 år med få krig inne i riket."),
 ("Slav","Människa som ägs av någon annan och saknar rättigheter."),
 ("Medborgare","Person med rättigheter och skyldigheter i staten."),
 ("Förföljelse","Att systematiskt plåga människor för deras tro."),
 ("Historiebruk","Hur och varför historia används idag."),
]

SAMMAN = [
 "Rom grundades enligt sagan 753 f.Kr. av Romulus. Arkeologin visar att byar växte ihop till en stad vid Tibern.",
 "Omkring 509 f.Kr. blev Rom en republik med två konsuler, senat och folkförsamlingar. Det var ingen demokrati som vår.",
 "Genom krig, bland annat mot Karthago (264–146 f.Kr.), blev Rom härskare över Medelhavet.",
 "Caesar mördades 44 f.Kr. och Augustus blev kejsare 27 f.Kr. Makten flyttade från många till en.",
 "Samhället var uppdelat i patricier, plebejer, frigivna och slavar. Slaveriet var en del av hela ekonomin.",
 "Armén och vägarna höll ihop riket. Vardagen kunde vara hård, med både bad, torg och arenor.",
 "Kristendomen spreds trots förföljelser och blev i praktiken officiell religion 380.",
 "Västrom föll 476 av många orsaker. Arvet lever kvar: språk, lag, byggnader, kalender, och Rom används politiskt och kommersiellt än i dag.",
]

TEST_A = [
 ("Vilket år brukar man säga att Rom grundades enligt traditionen?",["509 f.Kr.","753 f.Kr.","44 f.Kr.","476 e.Kr."],1),
 ("Hur många konsuler hade republiken?",["En","Två","Tio","Hundra"],1),
 ("Vilka krig förde Rom mot Karthago?",["Galliska krigen","Puniska krigen","Trojanska kriget","Hundraårskriget"],1),
 ("Vem blev Roms första kejsare?",["Julius Caesar","Nero","Augustus","Konstantin"],2),
 ("Vilken grupp ägdes av andra och saknade rättigheter?",["Patricier","Plebejer","Slavar","Senatorer"],2),
 ("Vad var Via Appia?",["Ett badhus","En stenlagd väg","En akvedukt","En gud"],1),
 ("Vilket år avsattes den siste västromerske kejsaren?",["313","380","476","1453"],2),
 ("Vilket påstående om kejsardömet är mest korrekt?",["Senaten avskaffades helt","Gamla institutioner fanns kvar men makten låg hos kejsaren","Folket fick full demokrati","Romarna återinförde kungarna"],1),
]

TEST_B = [
 ("Förklara kort skillnaden mellan en myt och historia om Roms grundande.","Myten (Romulus och Remus) är en berättelse som inte går att bevisa. Historien bygger på arkeologi och källor som visar att byar växte ihop till en stad."),
 ("Nämn två orsaker till att republiken föll.","T.ex. mäktiga generaler med egna arméer, inbördeskrig, stora klyftor mellan rika och fattiga, svagt politiskt system."),
 ("Varför var vägarna viktiga för Rom?","De gjorde att armén, posten och handeln kunde förflytta sig snabbt och höll ihop det stora riket."),
 ("Nämn en sak som skilde en slav från en medborgare.","Slaven ägdes av någon annan och saknade rättigheter; medborgaren hade lagens skydd (och män kunde rösta)."),
 ("Varför kunde kristendomen sprida sig i det romerska riket?","Vägar och sjövägar, gemensamma språk, tron på allas lika värde och omsorg om sjuka och fattiga."),
 ("Ge ett exempel på hur Rom används i dag (historiebruk).","T.ex. film som Gladiator (underhållning), byggnader i romersk stil i USA (politik), Mussolinis fascism (propaganda)."),
]

KALLA = dict(
 text="”Staden är full av människor som trängs mellan hyreshusen. Vi har bröd varje dag och spel när kejsaren bjuder. Men hyrorna stiger, och på natten rasar ibland ett hus. Den som vill ha lugn bor på landet.”",
 ursprung="Konstruerad källa baserad på kritiska romerska författare under kejsartiden, till exempel Juvenalis (omkring år 100 e.Kr.). Skriven av en rik stadsbo i en ironisk ton.",
 fragor=[
  ("Vem tror du skrev texten, och hur märker du det?","En utbildad och förmögen man; texten är kritisk och skriven med ironi om vanligt folks liv i staden."),
  ("Vad kan du lära dig om vardagen i Rom?","Att många bodde trångt i hyreshus, att hus kunde rasa och hyrorna var höga; att kejsaren gav bröd och spel."),
  ("Vilka begränsningar har källan?","Det är en enda persons syn; författaren kan överdriva för att kritisera; den visar inte slavarnas eller kvinnornas perspektiv."),
  ("Vad skulle du vilja jämföra den med?","T.ex. arkeologiska fynd av hyreshus, lagtexter om brandskydd eller gravstenar som berättar om fattiga romares liv."),
 ])

SKRIV = dict(
 uppgift="Varför föll Västrom år 476? Skriv en text på 250–350 ord där du förklarar minst tre orsaker och resonerar om vilken som var viktigast. Visa också vad som levde kvar efter 476 (kontinuitet) och vad som förändrades.",
 stod=[
  "E: Du nämner några orsaker (t.ex. kris i ekonomin, kejsarbyten och folk som trängde på) och beskriver vad som hände 476. Du ger minst ett exempel på något som levde kvar.",
  "C: Du förklarar hur orsakerna hänger ihop (t.ex. att ekonomin försvagade armén, vilket gjorde det lättare för andra folk att ta sig in). Du beskriver både kontinuitet (kyrkan, latin, Östrom) och förändring.",
  "A: Du värderar orsakerna mot varandra och motiverar vilken som vägde tyngst, med reservation för att historiker är oense. Du diskuterar om ”fallet” var en händelse eller en lång process, och använder begrepp säkert.",
 ])

LAB = dict(
 titel="Historikerns verkstad: Vem var Spartacus? Jämför två källor",
 syfte="Öva källkritik: undersök hur olika sorters källor ger olika bild av ett slavuppror, och dra försiktiga slutsatser.",
 material="Två korta texter (läraren delar ut eller eleverna skriver själva): A) en romersk historieskrivares berättelse om upproret, B) en modern text om slavuppror. Penna, papper, kopiering av källfrågorna.",
 utforande=[
  "Dela in klassen i par. Läs båda texterna högt.",
  "Skriv upp vem som skrev varje text, när, och varför den skrevs.",
  "Sätt en pil mellan de uppgifter som stämmer överens och en annan pil där källorna säger olika saker.",
  "Diskutera: Vilken text är mest trovärdig för att veta vad som hände? Vilken ger bäst bild av hur människor tyckte och kände?",
  "Skriv tre meningar: vad vet vi säkert, vad är troligt, vad vet vi inte?",
 ],
 fragor=[
  ("Varför skrev romerska författare ofta negativt om slavuppror?","De tillhörde den rika klassen som hade intresse av ordning och slaveri."),
  ("Vad vet vi inte om Spartacus?","T.ex. hur han själv tänkte och vilka hans mål var; vi har inga texter från honom själv."),
  ("Hur kan arkeologi hjälpa?","Fynd från läger, vapen, gårdar och gravar kan visa om texternas uppgifter stämmer."),
 ],
 bonus="BONUS för läraren: Låt eleverna skriva en ”rättvis” rubrik för upproret från tre olika synvinklar (senator, slav, vanlig bonde) och jämför. Koppla till kunskapskravens källkritik: eleverna ska kunna använda och värdera källor och förklara varför bilder av samma händelse skiljer sig åt. Ge svagare läsare färdiga stödfrågor.",
)

LARAR = [
 ("Koppling till kursplanen (Lgr22, Historia)","Kapitlet täcker syftet om att kunna använda historiska begrepp, undersöka och värdera källor, förstå orsak–konsekvens och kontinuitet–förändring samt reflektera över historiebruk. I centralt innehåll berör det blocket om samhällsomvandlingar och framväxten av civilisationer, där antiken har en egen plats med vikt på betydelsen för politik, rättsväsende och språk i dag, samt slaveri, religion och människors villkor. Kapitlet lyfter dessutom frågor om hur historia används i film, politik och symboler."),
 ("Förslag på upplägg (8 lektioner)","1. Myt och historia, grundandet (4.1). 2. Republikens styre, rollspel i senaten (4.2). 3. Puniska krigen, kartövning (4.3). 4. Caesar och Augustus, debatt (4.4). 5. Samhället och slaveriet (4.5). 6. Armé, vägar och vardag, bildanalys (4.6). 7. Kristendom och Västroms fall (4.7–4.8) samt scen. 8. Historiebruk, Historikerns verkstad och test."),
 ("Vanliga missuppfattningar","Att Rom var en demokrati; att Romulus är en historisk person; att Västrom ”föll” på en dag; att alla romare var soldater eller gladiatorer; att kristendomen blev tillåten för att kejsaren var from (det fanns politiska skäl); att filmbilder av Rom är sanna. Tala också om att romarna var hårda mot underlägsna och att många slavar levde under svåra villkor."),
 ("Bedömningsstöd","E: eleven återger viktiga händelser, nämner enkla orsaker och några exempel på kontinuitet och förändring, och ger exempel på historiebruk. C: eleven förklarar samband mellan orsaker och konsekvenser, jämför källor och motiverar. A: eleven värderar orsakers betydelse, diskuterar historikers olika tolkningar och drar välgrundade slutsatser om hur Rom används i dag."),
 ("Tips: Blooket och Jeopardy – 10 kategorier","1. Myt och grundande. 2. Republiken. 3. Puniska krigen. 4. Caesar och Augustus. 5. Slavar och medborgare. 6. Vägar och armé. 7. Vardagsliv. 8. Kristendom. 9. Västroms fall. 10. Arv och historiebruk. Exempel: ”Vilket år tog Hannibal elefanter över Alperna? – 218 f.Kr.”; ”Vad betyder veto? – Jag förbjuder.”"),
]

KALLOR = [
 ("Encyclopaedia Britannica – Ancient Rome (från grundandet 753 f.Kr., republiken och kejsartiden till västrikets fall under 400-talet)","https://www.britannica.com/place/ancient-Rome"),
 ("Skolverket – Kommentarmaterial till kursplanen i historia, grundskolan (Lgr22; antiken, kolonisation, revolutioner)","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
 ("Nationalencyklopedin – romerska riket (bl.a. Augustus och att den siste västromerske kejsaren avsattes 476)","https://www.ne.se/uppslagsverk/encyklopedi/l%C3%A5ng/romerska-riket"),
 ("Statens historiska museer – Romarrikets inflytande (romerska importföremål och påverkan i Norden)","https://historiska.se/utforska-historien/kunskapsbank/romarrikets-inflytande/"),
 ("Perseus Digital Library – Suetonius, Divus Augustus (antik primärkälla på latin och engelska; ”marmor i stället för tegel” står i kap. 28)","https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.02.0132%3Alife%3Daug.%3Achapter%3D29"),
 ("UNESCO – Pompeji, Herculaneum och Torre Annunziata (världsarv; Vesuvius utbrott år 79 e.Kr.)","https://whc.unesco.org/en/list/829/"),
]

F_UPPG = [
 ("●","Förklara varför historiker ibland är oense om orsakerna till att Västrom föll. Ge två exempel på olika förklaringar.",[],None,"Det finns få och ofta partiska källor, och flera orsaker verkade samtidigt (ekonomi, politik, yttre tryck). Historiker lägger olika vikt vid dem."),
 ("●●","Läs avsnitt F1. Välj en källa (gravsten, mynt, en text av Tacitus) och beskriv vad den kan och inte kan berätta om vardagslivet i Rom.",[],None,"Exempel: gravsten visar yrke och familj men inte hela livet; text av Tacitus ger kejsarens syn men är skriven av en rik man."),
 ("●●","Jämför republikens och kejsardömets sätt att styra. Vad var kontinuitet och vad var förändring?",[],None,"Kontinuitet: senat, titlar, lagar. Förändring: makten samlad hos en kejsare, armén lojal mot honom."),
 ("●●●","Diskutera: Är det rimligt att kalla Rom en ”civilisation” att beundra om man tänker på slaveriet? Argumentera för minst två synsätt.",[],None,"Argument för: lagar, byggnader, spridning av idéer. Argument mot: slaveri, våld och krig. Ett bra svar skiljer mellan att förstå och att godkänna och noterar att dagens värderingar används."),
 ("●●●","Analysera hur filmen Gladiator eller en annan romarfilm använder historia. Vad är sant, vad är påhitt och varför?",[],None,"Ett bra svar skiljer filmens drama från källor, nämner att regissörer väljer det spännande och att filmen också bidrar till vår bild av Rom."),
]

F_SAMMAN = [
 "Källor om Rom är texter, föremål, byggnader och inskrifter, och de måste prövas med källkritik.",
 "Sverige låg utanför riket men hade kontakter via handel, och latinet påverkade vår kultur.",
 "Rom används i dag i film, politik och symboler. Det är historiebruk – med olika syften.",
 "Det som levde kvar efter Rom: språk, lag, byggnader, kalender och idéer om styre.",
]
F_BEGR = [
 ("Källkritik","Att pröva vem som skrev något, när, varför och om det går att lita på."),
 ("Primärkälla","Källa från den tid man studerar."),
 ("Sekundärkälla","Källa som är skriven senare, ofta av en historiker."),
 ("Historiebruk","Hur historia används i dag, av vem och varför."),
 ("Romanisering","Att områden tog över romerskt språk, lagar och seder."),
]

BLOOKET = [
 ("Vilket år grundades Rom enligt traditionen?","753 f.Kr.","509 f.Kr.","44 f.Kr.","476 e.Kr."),
 ("Vilka var Romulus och Remus enligt sagan?","Tvillingar som räddades av en varginna","Två konsuler","Två kejsare","Två generaler"),
 ("Vad är en myt?","En berättelse som inte går att bevisa","En lag","En väg","En mynttyp"),
 ("Vad betyder res publica?","Folkets sak","Kejsarens sak","Gudarnas rike","Slavarnas lag"),
 ("Hur många konsuler hade republiken?","Två","En","Fem","Tio"),
 ("Hur länge satt en konsul?","Ett år","Livet ut","Tio år","Tre månader"),
 ("Vad var senaten?","Ett råd av rika, erfarna män","En armé","En domstol för slavar","En gudatempel"),
 ("Vad betyder veto?","Jag förbjuder","Jag röstar","Jag ger","Jag lyder"),
 ("Vem var Hannibal?","Fältherre från Karthago","Romersk kejsare","Grekisk gud","Slavledare"),
 ("Vad tog Hannibal med över Alperna?","Krigselefanter","Fartyg","Kanoner","Hästvagnar av guld"),
 ("När förstördes Karthago?","146 f.Kr.","264 f.Kr.","44 f.Kr.","476 e.Kr."),
 ("Vad kallas områden Rom erövrat och styrde över?","Provinser","Republiker","Konsulat","Forum"),
 ("Vem gick över Rubicon 49 f.Kr.?","Julius Caesar","Augustus","Nero","Spartacus"),
 ("När mördades Caesar?","15 mars 44 f.Kr.","1 januari 27 f.Kr.","4 juli 476","5 maj 313"),
 ("Vem blev Roms förste kejsare?","Augustus","Nero","Konstantin","Hannibal"),
 ("Vad betyder Pax Romana?","Romersk fred","Romersk lag","Romerska krig","Romersk gud"),
 ("Vilka var plebejer?","Vanliga medborgare","Slavar","Kejsare","Präster"),
 ("Vem ledde ett stort slavuppror 73–71 f.Kr.?","Spartacus","Hannibal","Scipio","Odovakar"),
 ("Vad var en legion?","Militär enhet på ca 5 000 man","En rådsförsamling","En väg","En skatt"),
 ("Vilken var en av de äldsta stora romerska vägarna?","Via Appia","Via Dolorosa","Via Rubicon","Via Sverige"),
 ("När invigdes Colosseum?","80 e.Kr.","27 f.Kr.","476 e.Kr.","753 f.Kr."),
 ("Vad var insulae?","Hyreshus","Badhus","Tempel","Arenor"),
 ("Vilket år gav Konstantin kristna rätt att utöva sin tro (Milanoediktet)?","313","44 f.Kr.","1453","1066"),
 ("Vilket år blev kristendomen i praktiken statsreligion?","380","27 f.Kr.","476","1000"),
 ("Vem avsatte den siste västromerske kejsaren år 476?","Odovakar","Julius Caesar","Hannibal","Konstantin"),
 ("Vad hette Östrom senare?","Bysantinska riket","Franska riket","Svea rike","Persiska riket"),
 ("Vilken kalender införde Julius Caesar 46 f.Kr.?","Den julianska","Den gregorianska","Den egyptiska","Den vikingatida"),
 ("Vilket språk är ursprunget till spanska, franska och italienska?","Latin","Grekiska","Arabiska","Hebreiska"),
]

JEOPARDY = {
 "Grundande och republik":[
  (100,"Året då Rom grundades enligt traditionen.","753 f.Kr."),
  (200,"Sagans tvillingar och varginnan.","Romulus och Remus"),
  (300,"Antalet konsuler i republiken.","Två"),
  (400,"Latinskt ord som betyder ”jag förbjuder”.","Veto"),
  (500,"Förklara varför republiken inte var en demokrati som vår.","Kvinnor, slavar och icke-medborgare fick inte rösta, och de rika hade mest inflytande.")],
 "Krig och expansion":[
  (100,"Staden i Nordafrika som var Roms rival.","Karthago"),
  (200,"Fältherre som tog elefanter över Alperna.","Hannibal"),
  (300,"Romersk general som segrade vid Zama 202 f.Kr.","Scipio"),
  (400,"Romarnas namn på erövrade områden.","Provinser"),
  (500,"Ge en konsekvens hemma i Rom av att vinna kriget.","Rikedom och slavar, men bönder som förlorade gårdar.")],
 "Kejsare":[
  (100,"Gick över Rubicon år 49 f.Kr.","Julius Caesar"),
  (200,"Datumet då Caesar mördades.","15 mars 44 f.Kr."),
  (300,"Hederstitel som Octavianus fick 27 f.Kr.","Augustus"),
  (400,"Perioden av fred inom riket under kejsartiden.","Pax Romana"),
  (500,"Förklara ordet kejsare.","Det kommer från namnet Caesar.")],
 "Samhälle och vardag":[
  (100,"Gladiator som ledde slavuppror.","Spartacus"),
  (200,"Stor arena i Rom, invigd 80 e.Kr.","Colosseum"),
  (300,"Hyreshus i Rom.","Insulae"),
  (400,"Stenlagda färdvägar, som Via Appia, som höll ihop riket.","Vägar"),
  (500,"Varför vet vi så lite om slavarnas liv?","De skrev sällan själva, och bevarade texter är skrivna av rika män.")],
 "Kristendom, fall och arv":[
  (100,"Året då Västrom brukar anses ha fallit.","476"),
  (200,"Kejsaren som stoppade förföljelserna 313.","Konstantin"),
  (300,"Språk som blev källa till spanska, franska och italienska.","Latin"),
  (400,"Staden som blev östra rikets huvudstad.","Konstantinopel"),
  (500,"Ge ett exempel på historiebruk av Rom i dag.","T.ex. filmen Gladiator, USA:s senat och byggnader, eller fascismens användning av Rom.")],
}

SCEN = dict(
 titel="Tidsresa genom Rom", plats="Rom och Medelhavet", tid="753 f.Kr. – 476 e.Kr.",
 sky=("#f6d99a","#e8a75d"), mark="#b08a5a",
 walker=dict(typ="medborgare"),
 etapper=[
  dict(x_etikett="753 f.Kr.", tid="753 f.Kr.", plats="Palatinen, vid Tibern", rubrik="Staden börjar",
       fakta=["Du står på en kulle vid floden. Små hyddor av trä och lera ligger tätt, och herdar leder får.","Enligt sagan grundar Romulus staden här. Arkeologer ser att byarna växte ihop under flera generationer."],
       fraga="Vad är en myt?", alt=["En berättelse som förs vidare men inte går att bevisa","En lag skriven på tavlor","En romersk gud"], ratt=0,
       forklaring="Sagan om Romulus är en myt. Den säger något om hur romarna såg på sig själva men är inte en säker källa.",
       deko=[("bondgard",-120,1.0),("flod",60,1.0),("trad",160,0.9)]),
  dict(x_etikett="509 f.Kr.", tid="509 f.Kr.", plats="Forum Romanum", rubrik="Ingen kung mer",
       fakta=["Folk samlas på torget. Kungen har jagats bort, och två konsuler ska leda staden under ett år.","Senaten ger råd, och folket får rösta – men bara männen som är medborgare."],
       fraga="Varför hade republiken två konsuler?", alt=["För att de skulle kunna hindra varandra och ingen skulle få för stor makt","För att en var för sjuk","För att kungen krävde det"], ratt=0,
       forklaring="Tanken var att dela makten så att ingen kunde bli kung igen.",
       deko=[("tempel_grekiskt",-100,1.1),("folkmassa",60,1.0),("marknad",190,0.9)]),
  dict(x_etikett="202 f.Kr.", tid="218–146 f.Kr.", plats="Medelhavet och Karthago", rubrik="Krig mot Karthago",
       fakta=["Du ser romerska skepp ute på havet. Rom och Karthago slåss om herraväldet i över hundra år.","Hannibal tog elefanter över Alperna 218 f.Kr. Rom segrade till slut och förstörde Karthago 146 f.Kr."],
       fraga="Vad var en konsekvens av Roms seger över Karthago?", alt=["Rom fick makt över Medelhavet, skatter och slavar","Rom blev en demokrati","Karthago blev huvudstad"], ratt=0,
       forklaring="Rom blev den ledande makten i Medelhavsområdet, och rikedomen förändrade samhället.",
       deko=[("trirem",-80,1.2),("berg",140,1.4),("legionar",-170,1.0)]),
  dict(x_etikett="44 f.Kr.", tid="44 f.Kr.", plats="Senaten", rubrik="Caesars sista dag",
       fakta=["Folk viskar utanför senatsbyggnaden. Caesar har blivit diktator på livstid, och många är oroliga.","Den 15 mars mördas han av senatorer som vill rädda republiken. Resultatet blir nya inbördeskrig."],
       fraga="Vad blev följden av Caesars mord?", alt=["Nya inbördeskrig och till slut kejsardöme","Republiken blev starkare på en gång","Karthago återuppstod"], ratt=0,
       forklaring="Mordet räddade inte republiken. Octavianus (Augustus) tog makten och blev kejsare 27 f.Kr.",
       deko=[("tempel_grekiskt",-120,1.2),("folkmassa",80,1.0),("flagga_rod",190,0.8)]),
  dict(x_etikett="80 e.Kr.", tid="80 e.Kr.", plats="Colosseum", rubrik="Brödet och spelen",
       fakta=["Colosseum invigs, och tiotusentals åskådare trängs. Utanför säljs bröd och oliver.","Riket är på sin höjdpunkt. Vägar, akvedukter och armé håller ihop det, men många arbetar som slavar."],
       fraga="Vad höll det stora romerska riket ihop?", alt=["Armé, vägar och ett gemensamt system av lagar","Bara kungens vilja","Telefoner"], ratt=0,
       forklaring="Legioner, vägar och lagar gjorde att riket kunde styras över stora avstånd.",
       deko=[("colosseum",-60,1.5),("akvedukt",170,1.2),("legionar",-190,1.0)]),
  dict(x_etikett="313", tid="313–380", plats="Ett kristet samfund", rubrik="En ny tro",
       fakta=["I ett hus samlas kristna för att sjunga och be. Förr har de förföljts. Nu får de utöva sin tro.","Kejsar Konstantin ger frihet 313. År 380 blir kristendomen i praktiken rikets religion."],
       fraga="Vad hände år 313?", alt=["Kristna fick utöva sin tro fritt","Rom förstördes","Colosseum byggdes"], ratt=0,
       forklaring="Milanoediktet innebar religionsfrihet. Senare blev kristendomen dominerande i riket.",
       deko=[("kyrka",-60,1.2),("folkmassa",100,0.9),("palm",190,0.9)]),
  dict(x_etikett="476", tid="476 e.Kr.", plats="Ravenna och Rom", rubrik="Slutet – och arvet",
       fakta=["Västrom har fallit efter lång kris. Östrom fortsätter. Latin, lag, vägar och byggnader lever kvar.","Även i Sverige finns spår: ord som kejsare och tegel och romerska mynt i jorden."],
       fraga=None, alt=None, ratt=None, forklaring=None,
       deko=[("colosseum",-80,1.2),("akvedukt",120,1.1),("kyrka",230,0.9)]),
 ],
 diskutera="Vilka tre saker från Rom tycker du är viktigast att komma ihåg i dag – och vilket mörkt kapitel (till exempel slaveriet) får inte glömmas bort?",
)
