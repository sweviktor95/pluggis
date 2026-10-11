# -*- coding: utf-8 -*-
# Kapitel 10 – Mellankrigstiden: demokrati och diktatur (Pluggis historia åk 8)
T = dict(
 nr=10, namn="Mellankrigstiden", under="Demokrati och diktatur mellan två världskrig",
 fil="historia-10-mellankrigstiden", arskurs=8, nodeid="historia-mellankrigstiden",
 mal=["förklara hur den ryska revolutionen ledde fram till Sovjetunionen och Stalins diktatur",
      "beskriva vad Gulag var och varför terrorn drabbade så många",
      "förklara varför depressionen efter 1929 fick så stora politiska följder",
      "jämföra hur fascismen i Italien och nazismen i Tyskland tog makten",
      "beskriva kännetecken för en diktatur och hur propaganda fungerar",
      "förklara hur Sverige klarade krisen med allmän rösträtt, krispolitik och Saltsjöbadsavtalet",
      "analysera propaganda och hur diktaturer använder historia"],
 fundera="Tänk dig ett land där du inte får kritisera regeringen, där tidningarna skriver samma sak och där grannen kanske anmäler dig. Vad skulle du sakna mest? Skriv tre saker innan du läser.",
)

S = []

S.append(dict(id="ryska", nr="10.1", ikon="🚩", titel="Ryska revolutionen och Sovjetunionen",
 intro="År 1917 föll tsaren i Ryssland och några månader senare tog ett nytt parti makten. Det blev starten på världens första kommunistiska stat.",
 block=[
  ("p","Ryssland hade styrts av en tsar, en kejsare med nästan obegränsad makt. Landet var fattigt och de flesta var bönder. Under första världskriget förlorade Ryssland många soldater, det blev brist på mat och människor frös i köerna. I <strong>februari 1917</strong> (mars enligt vår kalender) revolterade arbetare och soldater i huvudstaden Petrograd och tsar Nikolaj II avgick."),
  ("p","Landet fick en provisorisk regering, men den ville fortsätta kriget. Det gjorde den impopulär. Partiet <strong>bolsjevikerna</strong>, som leddes av <strong>Lenin</strong>, lovade ”fred, jord och bröd”. I november 1917 (oktober enligt den gamla ryska kalendern) tog de makten med stöd av arbetare och soldater."),
  ("tidslinje",[("1917","Tsaren avgår, bolsjevikerna tar makten"),("1918–1921","Inbördeskrig mellan ”röda” och ”vita”"),("1922","Sovjetunionen (USSR) bildas"),("1924","Lenin dör"),("1928","Stalin inleder första femårsplanen"),("1937–1938","Den stora terrorn")]),
  ("p","Bolsjevikerna ville bygga ett <strong>kommunistiskt</strong> samhälle där fabriker och mark ägdes av staten och inte av enskilda. Men de byggde också en enpartistat. Andra partier förbjöds och motståndare jagades av säkerhetspolisen. Efter ett blodigt inbördeskrig vann de röda, och 1922 bildades <strong>Sovjetunionen</strong>."),
  ("ruta","fakta","Kommunism – idé och verklighet","Idén kommer från Karl Marx: alla ska dela på rikedomen och klasskillnaderna ska försvinna. I Sovjetunionen kom partiet och dess ledare att bestämma över nästan allt. Skillnaden mellan idé och verklighet är ett viktigt ämne för historiker."),
  ("bild","ryska_revolutionen","Revolutionen 1917 förändrade Ryssland och fick följder över hela världen."),
  ("kolla",["Varför var många ryssar missnöjda 1917?","Vad lovade bolsjevikerna?","Vilket år bildades Sovjetunionen?"]),
 ],
 svar=["Kriget, brist på mat och en tsar med nästan obegränsad makt.","Fred, jord och bröd.","1922."],
))

S.append(dict(id="stalin", nr="10.2", ikon="⛓️", titel="Stalins Sovjetunionen: planer, Gulag och terror",
 intro="Efter Lenins död 1924 tog Josef Stalin makten. Under honom blev Sovjetunionen en diktatur där miljontals människor fängslades eller dog.",
 block=[
  ("p","<strong>Josef Stalin</strong> blev partiets starke man och röjde undan sina rivaler. Han ville göra landet till en industrimakt i rekordfart. År 1928 började den första <strong>femårsplanen</strong>: staten bestämde i detalj hur mycket stål, kol och maskiner som skulle tillverkas. Nya fabriker och städer byggdes snabbt."),
  ("p","Bönderna tvingades gå samman i stora <strong>kollektivjordbruk</strong>. Rikare bönder, som kallades kulaker, förföljdes och fördrevs. Tillsammans med andra faktorer ledde det till svälten 1932–1933. Särskilt hårt drabbades Ukraina, där svälten kallas <em>Holodomor</em>. Forskare uppskattar att flera miljoner dog, men uppgifterna varierar mycket."),
  ("p","<strong>Gulag</strong> var namnet på de sovjetiska arbetslägren. Fångar tvingades arbeta med skogsavverkning, gruvor och byggen i kalla, avlägsna områden. Enligt officiella sovjetiska siffror passerade ungefär 7,6 miljoner människor lägren 1921–1953, men siffran är omstridd. Vissa västerländska forskare uppskattar omkring 18 miljoner. Uppskattningsvis 1,5–1,7 miljoner dog i lägren och arbetskolonierna."),
  ("ruta","fakta","Den stora terrorn 1937–1938","Under de här två åren greps över en miljon människor. Många dömdes i snabba rättegångar för ”förräderi” eller ”sabotage”, ofta på falska anklagelser. Omkring 700 000 avrättades och många fler skickades till Gulag. Även partiets egna ledare och officerare drabbades. Ingen var säker."),
  ("p","Stalin byggde också en personkult. Hans bild fanns överallt, och tidningar, filmer och skolböcker prisade honom. Kritik var farlig. Många vågade inte säga vad de tyckte, inte ens hemma."),
  ("ruta","tank","Tänk efter","Landet industrialiserades snabbt, och många sovjetmedborgare fick utbildning och arbete. Samtidigt kostade det miljontals liv. Kan en stor framgång på ett område väga upp förtryck på ett annat? Historiker diskuterar hur man ska väga detta."),
  ("kolla",["Vad var en femårsplan?","Vad var Gulag?","Varför är siffror om offren osäkra?"]),
 ],
 svar=["En plan där staten bestämde hur mycket som skulle produceras under fem år.","Sovjetunionens system av tvångsarbetsläger.","Arkiv var hemliga eller ofullständiga, och forskare räknar på olika sätt."],
))

S.append(dict(id="tjugotal", nr="10.3", ikon="🎷", titel="Efter kriget: nya demokratier och de glada tjugotalen",
 intro="Första världskriget (1914–1918) förändrade Europas karta. Gamla kejsardömen försvann och många nya demokratier uppstod.",
 block=[
  ("p","Kejsardömena i Tyskland, Österrike-Ungern och Ryssland föll, och nya länder som Polen, Tjeckoslovakien och Finland bildades. De flesta fick <strong>demokratiska</strong> styrelseskick med fria val. Fler fick rösta, och i många länder fick kvinnor rösträtt, till exempel i Storbritannien 1918 och 1928, USA 1920, Tyskland 1919 och Sverige 1921."),
  ("p","Men demokratierna var unga och osäkra. Många hade lidit av kriget, och fred och ekonomi var svåra frågor. I flera länder ville både extrema vänsterpartier och extrema högerpartier avskaffa demokratin."),
  ("p","Under mitten av 1920-talet blev det ändå bättre. Ekonomin växte, särskilt i USA. Man talar om de <strong>glada tjugotalen</strong>: radio, grammofon, bio och jazz blev populärt, bilar och elektriska varor blev vanligare, och många unga kvinnor klippte håret kort och sökte jobb. Mycket köptes på avbetalning, alltså på kredit."),
  ("ruta","fakta","Fred genom samarbete","1920 bildades Nationernas förbund för att lösa konflikter utan krig. Det saknade dock egen militär, och USA gick aldrig med. Förbundet kunde därför bara göra lite när en stormakt bröt mot reglerna."),
  ("ruta","historia","Sverige och tjugotalet","Även i Sverige blev radion populär. Bolaget Radiotjänst, föregångare till Sveriges Radio, bildades 1924 och började sända regelbundet 1925. Svensk Filmindustri bildades 1919 och blev en storindustri. Samtidigt var arbetslösheten hög i början av tjugotalet, och många svenskar emigrerade till USA fram till 1930."),
  ("kolla",["Nämn två nya länder som bildades efter första världskriget.","Vad menas med ”glada tjugotalen”?","Varför var demokratierna sköra?"]),
 ],
 svar=["T.ex. Polen, Tjeckoslovakien, Finland.","Ett uppsving med ny teknik, nöjen och ekonomisk tillväxt, framför allt i USA.","De var nya, människor hade lidit av kriget och extrema partier ville avskaffa demokratin."],
))

S.append(dict(id="kris", nr="10.4", ikon="📉", titel="Börskraschen 1929 och depressionen",
 intro="Hösten 1929 störtade aktiekurserna i New York. Det blev början på den värsta ekonomiska krisen på mycket länge.",
 block=[
  ("p","På <strong>börsen</strong> köper och säljer man aktier, små andelar i företag. Under tjugotalet steg kurserna, och många lånade pengar för att köpa aktier. Den 24 oktober 1929 började kurserna falla snabbt. Folk skyndade sig att sälja, vilket pressade priserna ännu mer. Kraschen fortsatte den 29 oktober, och under de följande åren föll Dow Jones-indexet med nästan 90 procent."),
  ("p","Krisen spred sig. Banker gick omkull, företag stängde och miljontals blev arbetslösa. I USA var ungefär var fjärde arbetsför utan jobb som mest. Det kallas <strong>depressionen</strong> eller den stora depressionen. Eftersom amerikanska banker nu krävde tillbaka lån från Europa drabbades också Tyskland hårt."),
  ("tab",["Land","Hur krisen märktes"],[["USA","Banker och företag gick under, uppemot var fjärde utan jobb"],["Tyskland","Omkring 6 miljoner arbetslösa vintern 1932"],["Sverige","Exporten föll, arbetslösheten steg kraftigt 1931–1933"]]),
  ("p","Hur reagerade regeringarna? I USA införde president Franklin D. Roosevelt <strong>New Deal</strong> med statliga jobbprojekt. I Sverige satsade Socialdemokraterna på att staten skulle skapa arbete (mer i avsnitt 10.8). I Tyskland gick det åt andra hållet: Många förlorade förtroendet för demokratin och röstade på extrema partier."),
  ("ruta","tank","Orsak och följd","Krisen började i USA men fick följder i Europa. Det visar hur länder hänger ihop genom handel och lån. Fråga dig: vilka orsaker fanns till att depressionen blev så lång, och varför fick den så olika politiska följder?"),
  ("kolla",["Vad hände den 24 oktober 1929?","Varför drabbades Tyskland hårt av krisen?","Vad var New Deal?"]),
 ],
 svar=["Aktiekurserna på börsen i New York började störta.","Amerikanska banker krävde tillbaka lån, och landets ekonomi var beroende av dem.","Roosevelts program med statliga satsningar för att skapa jobb."],
))

S.append(dict(id="italien", nr="10.5", ikon="🏛️", titel="Fascismen i Italien",
 intro="Italien var det första landet i Europa där en fascistisk ledare tog makten. Benito Mussolini blev förebild för andra diktatorer.",
 block=[
  ("p","Efter första världskriget var Italien missnöjt med fredsvillkoren. Landet var fattigt, arbetslösheten hög, strejker och oroligheter spreds. 1919 bildade <strong>Benito Mussolini</strong> en rörelse som i Milano fick namnet Fasci di Combattimento, och som blev fascistpartiet. Många unga soldater anslöt sig."),
  ("p","<strong>Fascism</strong> är en ideologi som sätter staten och nationen över individen. Alla ska vara lydiga, det finns en stark ledare, våld ses som en tillåten metod och politiska motståndare ska tystas. Fascisterna var starkt nationalistiska, de var emot demokrati och emot kommunism."),
  ("p","I oktober 1922 marscherade fascisterna mot Rom, och kungen utnämnde Mussolini till premiärminister. Han fick makten på laglig väg, men med hot om våld i bakgrunden. Under de följande åren hotades och slogs motståndare, och i januari 1925 förklarade Mussolini öppet att Italien var en diktatur."),
  ("ruta","fakta","Il Duce","Mussolini kallades <em>il Duce</em>, ledaren. Han dyrkades i affischer, filmer och tal från balkongen. Staten kontrollerade tidningarna, och politiska motståndare fängslades eller skickades i exil."),
  ("p","Mussolini ville göra Italien till en stormakt. 1935 anföll landet Etiopien, och senare slöt han en allians med Hitlers Tyskland. Italien gick med i andra världskriget 1940 och Mussolini avsattes 1943. Han avrättades av motståndsmän 1945."),
  ("kolla",["Vad är fascism?","Hur fick Mussolini makten 1922?","Vilket år förklarade Mussolini Italien som diktatur?"]),
 ],
 svar=["En ideologi som sätter staten och nationen över individen, med en stark ledare, våld mot motståndare och motstånd mot demokrati.","Fascisterna marscherade mot Rom och kungen utsåg honom till premiärminister.","1925."],
))

S.append(dict(id="tyskland", nr="10.6", ikon="🏚️", titel="Weimarrepubliken och vägen till 1933",
 intro="Tyskland blev en demokrati efter första världskriget. Mindre än femton år senare hade landet en diktatur. Hur gick det till?",
 block=[
  ("p","1918 avgick den tyske kejsaren och landet blev en republik. Den kallas <strong>Weimarrepubliken</strong> efter staden där författningen skrevs 1919. Alla över 20 år fick rösta, även kvinnor. Men många tyskar hade svårt att acceptera republiken. De skyllde nederlaget i kriget och de hårda fredsvillkoren i Versailles på den."),
  ("p","Landet drabbades av kriser. Staten tryckte pengar för att betala skulder, och 1923 skenade priserna. Det kallas <strong>hyperinflation</strong>. Till slut var pengarna nästan värdelösa, och en dollar kostade i november 1923 flera biljoner mark. Sparpengar blev över en natt värdelösa. Hitler försökte samma år ta makten med ett våldsamt kuppförsök i München men misslyckades och dömdes till fängelse."),
  ("p","Under några år var läget lugnare. Men efter börskraschen 1929 sjönk Tysklands ekonomi igen, och vintern 1932 var omkring 6 miljoner arbetslösa. Många blev desperata och lyssnade på partier som lovade enkla lösningar. <strong>Nazistpartiet</strong>, NSDAP, under <strong>Adolf Hitler</strong> växte kraftigt. Partiet pekade ut judar, kommunister och demokrater som skyldiga och lovade arbete, ordning och nationell stolthet."),
  ("tidslinje",[("1919","Weimarrepubliken får sin författning"),("1923","Hyperinflation"),("1929","Börskraschen"),("1932","Nazistpartiet blir största parti i riksdagen"),("30 jan 1933","Hitler utnämns till rikskansler"),("feb–mars 1933","Riksdagshuset brinner, fullmaktslagen antas")]),
  ("p","Nazisterna fick aldrig egen majoritet i fria val. I juli 1932 fick de omkring 37 procent av rösterna. Men flera konservativa politiker trodde att de kunde kontrollera Hitler, och president Hindenburg utsåg honom till <strong>rikskansler</strong> den 30 januari 1933. Det var en lagligt genomförd utnämning, men början på slutet för demokratin."),
  ("ruta","tank","Fundera","Det finns inte en enda orsak till att Hitler kom till makten. Historiker nämner krisen, missnöjet med Versailles, rädsla för kommunism, svaga demokratiska partier och politikers felbedömningar. Vilka av dessa tycker du var viktigast?"),
  ("kolla",["Vad var hyperinflation?","Varför växte nazistpartiet efter 1929?","Hur blev Hitler rikskansler?"]),
 ],
 svar=["När priserna skenar och pengarna blir i det närmaste värdelösa.","Massarbetslöshet och missnöje gjorde att många lyssnade på partier med enkla lösningar.","President Hindenburg utsåg honom 30 januari 1933, efter politiska förhandlingar."],
))

S.append(dict(id="diktatur", nr="10.7", ikon="📢", titel="Diktaturen i Tyskland: makt, propaganda och förföljelse",
 intro="Under 1933 byggde nazisterna om Tyskland till en diktatur. Till det hörde propaganda, kontroll och förföljelse av grupper som nazisterna såg som fiender.",
 block=[
  ("p","Natten mellan den 27 och 28 februari 1933 brann riksdagshuset i Berlin. Nazisterna använde branden som skäl att dra in medborgerliga rättigheter. I mars antog riksdagen den så kallade <strong>fullmaktslagen</strong>, som lät regeringen stifta lagar utan riksdagen. Under sommaren förbjöds de andra partierna, fackföreningarna upplöstes och landet blev en <strong>enpartistat</strong>."),
  ("p","<strong>Propaganda</strong> är information som är gjord för att påverka tankar och känslor, ofta genom att förenkla, överdriva eller utelämna. Regimen kontrollerade tidningar, radio och film. Böcker av författare som ogillades brändes. Barn fostrades i ungdomsorganisationer och skolan. Ledaren framställdes som landets räddare, och minoriteter beskrevs som hot."),
  ("p","Främst drabbades <strong>judar</strong>. Judehatet, antisemitismen, hade funnits i Europa i många hundra år, men nazisterna gjorde det till statens politik. 1933 uppmanades folk att bojkotta judiska affärer. Efter <strong>Nürnberglagarna</strong> 1935 fråntogs judar medborgarskapet och förbjöds gifta sig med icke-judar. Natten 9–10 november 1938, <strong>kristallnatten</strong>, förstördes över tusen synagogor och omkring 26 000 judiska män fängslades i koncentrationsläger."),
  ("p","Även andra förföljdes: politiska motståndare som socialdemokrater och kommunister, romer, homosexuella, Jehovas vittnen och människor med funktionsnedsättning. Det var början på en utveckling som i andra världskriget ledde till Förintelsen (se kapitel 12)."),
  ("ruta","fakta","Kännetecken för en diktatur","Ett parti och en ledare, ingen fri press, inga fria val, polis och hemlig polis som tystar motståndare, propaganda och ofta förföljelse av minoriteter."),
  ("kolla",["Vad innebar fullmaktslagen 1933?","Vad är propaganda?","Vilka grupper förföljdes i Tyskland? Nämn tre."]),
 ],
 svar=["Regeringen kunde stifta lagar utan riksdagens godkännande.","Information som är gjord för att påverka, ofta genom att förenkla, överdriva eller utelämna.","T.ex. judar, romer, homosexuella, politiska motståndare, Jehovas vittnen, funktionshindrade."],
))

S.append(dict(id="sverige", nr="10.8", ikon="🇸🇪", titel="Sverige under mellankrigstiden",
 intro="Medan demokratin föll i flera länder stärktes den i Sverige. Det beror på flera saker, bland annat folkrörelser och politiska överenskommelser.",
 block=[
  ("p","År 1917 infördes <strong>parlamentarism</strong>: regeringen måste ha riksdagens stöd. 1921 gällde för första gången <strong>allmän och lika rösträtt</strong> för både kvinnor och män vid riksdagsval, och 1922 satt fem kvinnor i riksdagen. Folkrörelserna, som arbetarrörelsen, nykterhetsrörelsen och frikyrkorna, lärde människor att organisera sig och driva frågor demokratiskt."),
  ("p","Men konflikter fanns. Den 14 maj 1931 demonstrerade arbetare i Ådalen i Västernorrland mot strejkbrytare och sänkta löner. Militär sköt mot demonstranterna vid Lunde, och <strong>fem personer dödades</strong>. Händelsen väckte stor chock i hela landet."),
  ("p","Vid depressionen steg arbetslösheten. 1932 vann Socialdemokraterna med <strong>Per Albin Hansson</strong> som statsminister valet, och 1933 slöt de en överenskommelse med Bondeförbundet, kallad <em>kohandeln</em>. Staten skulle skapa arbete och stötta jordbruket, i stället för att bara spara. Det kallas <strong>krispolitik</strong>."),
  ("p","I december 1938 skrev arbetsgivarna (SAF) och fackföreningarna (LO) under <strong>Saltsjöbadsavtalet</strong>. De skulle lösa lönekonflikter genom förhandlingar utan att staten behövde blanda sig i. Avtalet, som gällde i flera decennier, brukar kallas ”den svenska modellen”."),
  ("ruta","historia","Folkhemmet","Per Albin Hansson använde ordet <em>folkhemmet</em> om ett samhälle som skulle vara som ett gott hem, där alla tar hand om varandra. Trygghet för alla blev en viktig idé i svensk politik."),
  ("ruta","fakta","Mörkare sidor","Samtidigt hade Sverige också mörka kapitel. 1935 trädde en steriliseringslag i kraft. Fram till 1975 steriliserades omkring 63 000 människor, nästan alla kvinnor. Omkring 20 000 av dem steriliserades under tvång, och många fler utsattes för starka påtryckningar. Det visar att även en demokrati kan göra allvarliga övergrepp."),
  ("kolla",["Vad hände i Ådalen 1931?","Vad var kohandeln?","Vilka skrev under Saltsjöbadsavtalet 1938?"]),
 ],
 svar=["Militär sköt mot demonstranter och fem personer dödades.","En överenskommelse 1933 mellan Socialdemokraterna och Bondeförbundet om krispolitik.","LO (fackföreningarna) och SAF (arbetsgivarna)."],
))

# ---- Fördjupning ----
F = []
F.append(dict(id="f1", nr="F1", ikon="🇪🇸", titel="Spanska inbördeskriget 1936–1939",
 intro="I Spanien utbröt ett inbördeskrig som drog in andra länder. Många ser det som en förövning inför andra världskriget.",
 block=[
  ("p","Spanien blev republik 1931. Landet var djupt splittrat mellan vänster och höger, rika och fattiga, kyrka och fria tänkare. I juli 1936 gjorde en grupp officerare under general <strong>Francisco Franco</strong> uppror mot den folkvalda regeringen. Då började ett <strong>inbördeskrig</strong>, ett krig mellan grupper inom samma land."),
  ("p","Kriget blev internationellt. Tyskland och Italien hjälpte Franco med flygplan och soldater. Sovjetunionen stödde republiken. Storbritannien och Frankrike höll sig utanför. Tusentals frivilliga från många länder, även Sverige, reste för att strida på republikens sida."),
  ("p","Den 26 april 1937 bombades den baskiska staden <strong>Guernica</strong> från luften. Konstnären Pablo Picasso målade en berömd tavla om det. Franco vann 1939 och styrde Spanien som diktator ända till sin död 1975."),
  ("ruta","tank","Tolkning","Varför kallas kriget ofta en ”generalrepetition”? Tyska flygplan prövade nya metoder. Men historiker påpekar att kriget främst hade spanska orsaker, och att orden kan ge ett för enkelt intryck."),
  ("kolla",["Vem ledde upproret 1936?","Vilka länder hjälpte Franco?","Vad hände i Guernica 1937?"]),
 ],
 svar=["General Francisco Franco.","Tyskland och Italien.","Staden bombades från luften."],
))
F.append(dict(id="f2", nr="F2", ikon="⚖️", titel="Demokrati och diktatur – en jämförelse",
 intro="Vad skiljer en demokrati från en diktatur? Här jämför vi, och ser också att gränsen inte alltid är skarp.",
 block=[
  ("tab",["Kännetecken","Demokrati","Diktatur"],[
   ["Makten","Folket väljer i fria val","En ledare eller ett parti bestämmer"],
   ["Yttrandefrihet","Man får kritisera makten","Kritik kan vara farlig"],
   ["Press","Fria medier","Staten kontrollerar medier"],
   ["Domstolar","Oberoende","Styrs av makthavare"],
   ["Minoriteter","Ska skyddas","Ofta förföljda"],
   ["Opposition","Tillåten","Förbjuden eller bekämpad"]]),
  ("p","Både fascism, nazism och kommunism under Stalin blev diktaturer, men de byggde på olika idéer. Fascism och nazism lyfte nationen eller ”rasen”. Kommunismen utgick från klass. Men metoderna liknade varandra: hemlig polis, propaganda och läger."),
  ("p","Forskare använder ordet <strong>totalitär</strong> om stater som vill kontrollera alla delar av livet. Andra forskare tycker att jämförelsen mellan olika regimer kan dölja viktiga skillnader. Till exempel var nazismens rasideologi, som ledde till Förintelsen, unik på sitt sätt."),
  ("ruta","tank","Fundera","Räcker det att ha val för att ett land ska vara en demokrati? Vad mer behövs? Ge två exempel."),
  ("kolla",["Nämn tre skillnader mellan demokrati och diktatur.","Vad menas med totalitär?","Varför är jämförelser mellan regimer både nyttiga och riskabla?"]),
 ],
 svar=["T.ex. fria val, yttrandefrihet, oberoende domstolar.","En stat som vill kontrollera alla delar av människors liv.","De hjälper oss se mönster men kan dölja viktiga skillnader."],
))
F.append(dict(id="f3", nr="F3", ikon="🔍", titel="Propagandans språk och historiebruk",
 intro="Diktaturer använde historien som ett vapen. Genom att lära oss se hur det går till blir vi bättre på att granska källor, också idag.",
 block=[
  ("p","Propaganda har ofta vissa knep. Man delar in världen i ”vi” och ”de”. Man använder starka ord, upprepar budskap och pekar ut en fiende. Man förenklar, och man lovar en ljus framtid. Känslan är viktigare än fakta."),
  ("tab",["Knep","Förklaring"],[["Vi och de","Gruppen ”vi” är goda, ”de” är hot"],["Syndabock","Någon utpekas som orsak till alla problem"],["Upprepning","Samma budskap om och om igen"],["Stora ord","Ära, folk, framtid, fiender"],["Bortvalda fakta","Det som inte passar utelämnas"]]),
  ("p","Diktaturer brukade också <strong>historiebruk</strong>. Mussolini lät sig jämföras med det romerska imperiet. Nazisterna hänvisade till en idealiserad och delvis påhittad ”storhetstid” för att motivera sin politik. I Sovjetunionen skrevs historieböcker om, och på bilder togs personer som fallit i onåd bort. Att skriva om historien är ett sätt att kontrollera nutiden."),
  ("ruta","exempel","Historiebruk idag","Politiker, företag och influencers använder historia i dag också. Fråga alltid: Vem berättar? Varför just nu? Vad lämnas ut? Vilka andra källor finns?"),
  ("kolla",["Nämn tre propagandaknep.","Hur använde Mussolini historien?","Vilka frågor kan du ställa för att granska en historiskt färgad text?"]),
 ],
 svar=["T.ex. vi och de, syndabock, upprepning.","Han jämförde sitt styre med det romerska imperiet.","Vem berättar? Varför nu? Vad utelämnas? Vilka andra källor finns?"],
))
F.append(dict(id="f4", nr="F4", ikon="🧩", titel="Hur kunde det hända? Forskare om Hitlers väg",
 intro="Historiker är inte helt överens om varför Weimarrepubliken föll. Här ser du hur olika förklaringar vägs mot varandra.",
 block=[
  ("p","Vissa forskare lägger tyngd på <strong>strukturer</strong>, alltså stora förhållanden som ekonomisk kris och hård fred. Andra ser till <strong>personer och beslut</strong>, till exempel politiker som slöt sig samman med Hitler. Ytterligare andra fokuserar på <strong>idéer</strong>, som antisemitism och nationalism, som fanns länge före 1933."),
  ("tab",["Förklaring","Argument","Invändning"],[
   ["Ekonomin","Krisen gjorde människor desperata","Många krisländer förblev demokratier"],
   ["Versailles","Fredsvillkoren väckte vrede","Vreden fanns även bland dem som inte röstade nazistiskt"],
   ["Politikers misstag","Konservativa släppte in Hitler","Fanns det andra alternativ?"],
   ["Idéer","Judehat och nationalism var utbrett","Räcker inte som ensam orsak"]]),
  ("p","Nästan alla forskare är överens om att det var en kombination. Ingenting var ”oundvikligt”. Människor gjorde val, och andra val hade kunnat göras. Det gör historien lärorik, men också allvarlig."),
  ("ruta","tank","Kontinuitet och förändring","Vad förändrades 1933, och vad hade funnits länge? Försök sortera: antisemitism, ekonomisk kris, fullmaktslagen, hat mot Versailles."),
  ("kolla",["Vad är skillnaden mellan strukturer och personer som förklaring?","Varför räcker inte ekonomin som enda förklaring?","Ge ett exempel på kontinuitet och ett på förändring."]),
 ],
 svar=["Strukturer är stora förhållanden, personer är enskilda människors val.","Många länder med kris förblev demokratier.","Kontinuitet: antisemitism fanns före 1933. Förändring: fullmaktslagen och enpartistaten."],
))

F_UPPG = [
 ("●","Förklara kort: vad är skillnaden mellan kommunism och fascism?",[],None,"Kommunismen vill avskaffa klasskillnader och privat ägande av produktionsmedel (i verkligheten ledde det till partistyre). Fascismen sätter nationen och staten över individen och är emot kommunism och demokrati."),
 ("●●","Jämför hur Hitler och Mussolini fick makten. Skriv tre likheter och två skillnader.",[],None,"Likheter: kris/missnöje, nationalism, hot och våld, utnämnda av statschef, byggde diktatur efteråt. Skillnader: Mussolini tog makten 1922 efter marsch mot Rom, Hitler 1933 efter val och förhandlingar; Hitler byggde en rasideologi med Förintelse."),
 ("●●","Varför blev Sverige inte en diktatur? Ange tre orsaker och argumentera för den viktigaste.",[],None,"T.ex. tidig parlamentarism och allmän rösträtt, folkrörelser, krispolitik, överenskommelser (kohandeln, Saltsjöbadsavtalet), mindre kris/krigserfarenhet. Eleven motiverar valet."),
 ("●●●","’Mellankrigstiden visar att demokratin är skör.’ Diskutera påståendet med exempel från minst två länder.",[],None,"Bedöms enligt SKRIV-stödet: exempel på demokratier som föll (Tyskland, Italien, Spanien) och som klarade sig (Sverige, USA), orsaker, avvägning."),
]
F_SAMMAN = [
 "Spanska inbördeskriget 1936–1939 var ett inbördeskrig där Tyskland och Italien stödde Franco, och Sovjetunionen stödde republiken.",
 "Demokrati: fria val, yttrandefrihet, oberoende domstolar. Diktatur: ett parti, kontroll över medier, förtryck.",
 "Propagandaknep: vi och de, syndabock, upprepning, stora ord, bortvalda fakta.",
 "Diktaturer använder historia för att legitimera makten och skriva om det som inte passar.",
 "Historiker förklarar Hitlers väg till makten med en kombination av strukturer, personers beslut och idéer.",
]
F_BEGR = [
 ("Inbördeskrig","Krig mellan grupper inom samma land."),
 ("Totalitär","Stat som vill kontrollera alla delar av livet."),
 ("Syndabock","Person eller grupp som får skulden för andras problem."),
 ("Struktur","Stora, långvariga förhållanden som ekonomi och samhälle."),
 ("Historiebruk","Hur människor använder historia för olika syften."),
]

UPPG = [
 ("Para ihop","Koppla ihop årtalet med händelsen.",["1917","1922","1929","1933","1938"],["Hitler blir rikskansler","Börskrasch i New York","Saltsjöbadsavtalet","Revolution i Ryssland","Sovjetunionen bildas"],"1 – D, 2 – E, 3 – B, 4 – A, 5 – C"),
 ("Sant eller falskt","Avgör om påståendena stämmer och rätta de falska.",["Lenin ledde bolsjevikerna 1917.","Mussolini marscherade mot Rom 1922.","Nazistpartiet fick egen majoritet i fria val 1932.","Gulag var ett system av arbetsläger.","Kvinnor fick rösta i riksdagsval i Sverige första gången 1921."],None,"Sant; sant (han utsågs efter marschen); falskt (största parti med omkring 37 procent men ingen majoritet); sant; sant."),
 ("Orsak och följd","Förklara varför depressionen efter 1929 ledde till att fler röstade på extrema partier i Tyskland.",[],None,"Massarbetslöshet, desperation, misstro mot demokratin, partier som lovade enkla lösningar, tidigare erfarenhet av hyperinflation."),
 ("Jämför","Jämför Stalins Sovjetunionen och Hitlers Tyskland. Skriv minst två likheter och en skillnad.",[],None,"Likheter: enpartistat, propaganda, hemlig polis, läger, personkult. Skillnad: ideologi (klass respektive ras), nazismens rasistiska utrotningspolitik."),
 ("Förklara begrepp","Förklara med egna ord: fascism, propaganda, hyperinflation, krispolitik.",[],None,"Se begreppslistan."),
 ("Kolla källan","En affisch från 1930-talet visar en strålande ledare och glada arbetare. Vad kan du säga om affischen som källa? Vad kan du inte veta?",[],None,"Den visar hur regimen ville bli sedd (propaganda), inte hur livet var. Man behöver andra källor, t.ex. dagböcker, brev, utländska rapporter."),
 ("Tidslinje","Rita en tidslinje 1917–1939 med minst åtta händelser från kapitlet. Markera vilka som gäller demokrati och vilka som gäller diktatur.",[],None,"Kontrollera årtal mot kapitlets tidslinjer."),
 ("Sverige","Förklara varför Ådalen 1931 och Saltsjöbadsavtalet 1938 ofta nämns tillsammans.",[],None,"Ådalen visade hur farliga konflikterna kunde bli; efter krisen sökte parterna lösningar genom förhandling. Saltsjöbadsavtalet blev sättet att lösa konflikter utan våld."),
 ("Kontinuitet och förändring","Vad förändrades i Tyskland mellan 1932 och 1935, och vad var sig likt?",[],None,"Förändring: demokrati blev diktatur, partier förbjöds, judar förlorade rättigheter. Likhet: antisemitism och missnöje fanns tidigare, och statens institutioner fanns kvar men styrdes annorlunda."),
 ("Diskutera","Är det någonsin rätt att begränsa yttrandefriheten för att skydda demokratin? Motivera.",[],None,"Öppet svar; bedöms på motivering och motargument."),
]

BEGREPP = [
 ("Bolsjevik","Medlem i det parti som Lenin ledde."),
 ("Kommunism","Idé om ett samhälle utan klasskillnader där staten äger produktionen."),
 ("Femårsplan","Statlig plan för produktionen under fem år."),
 ("Kollektivjordbruk","Stort jordbruk där många bönder tvingades arbeta tillsammans."),
 ("Gulag","Sovjetunionens system av tvångsarbetsläger."),
 ("Terror","Våld och hot som används för att skapa rädsla."),
 ("Depression","Långvarig, djup ekonomisk kris med hög arbetslöshet."),
 ("Fascism","Ideologi som sätter staten och nationen över individen."),
 ("Nazism","Tysk form av extrem nationalism med rasistisk ideologi."),
 ("Hyperinflation","Prisökningar som gör pengar i princip värdelösa."),
 ("Diktatur","Styrelseskick utan fria val och med begränsade rättigheter."),
 ("Propaganda","Information som är gjord för att påverka tankar och känslor."),
 ("Antisemitism","Hat eller fördomar mot judar."),
 ("Parlamentarism","Regeringen måste ha riksdagens stöd."),
 ("Krispolitik","Politik där staten ökar utgifterna för att bekämpa arbetslöshet."),
]

SAMMAN = [
 "1917 föll tsaren i Ryssland och bolsjevikerna under Lenin tog makten. 1922 bildades Sovjetunionen.",
 "Under Stalin blev Sovjetunionen en diktatur med femårsplaner, tvångskollektivisering, Gulag och den stora terrorn 1937–1938.",
 "Efter första världskriget kom många nya demokratier och de glada tjugotalen, men demokratierna var sköra.",
 "Börskraschen i New York 1929 ledde till depression och massarbetslöshet i många länder.",
 "Mussolini tog makten i Italien 1922 och byggde en fascistisk diktatur.",
 "I Tyskland ledde hyperinflation, depression och missnöje till att Hitler utsågs till rikskansler 1933. Därefter byggdes en diktatur med propaganda och förföljelse, främst av judar.",
 "Sverige stärkte sin demokrati: allmän rösträtt 1921, krispolitik 1933 och Saltsjöbadsavtalet 1938.",
 "Diktaturer använder propaganda och historiebruk för att kontrollera människors tankar.",
]

TEST_A = [
 ("Vilket parti tog makten i Ryssland 1917?",["Mensjevikerna","Bolsjevikerna","Fascisterna","Liberalerna"],1),
 ("Vad var Gulag?",["Ett sovjetiskt parti","Ett system av tvångsarbetsläger","En femårsplan","En revolutionär tidning"],1),
 ("Vad hände i New York i oktober 1929?",["Börskrasch","Revolution","Krigsutbrott","Val"],0),
 ("Hur fick Mussolini makten 1922?",["Han vann ett krig","Fascisterna marscherade mot Rom och kungen utsåg honom","Han köpte aktier","Han vann folkomröstning"],1),
 ("Vad innebar fullmaktslagen 1933?",["Alla fick rösta","Regeringen kunde stifta lagar utan riksdagen","Kvinnor fick rösta","Pressen blev fri"],1),
 ("Vad hände i Ådalen 1931?",["Strejkande demonstranter sköts av militär","Riksdagen invigdes","Ett järnvägsbygge","Ett fredsavtal"],0),
 ("Vilket avtal slöts mellan LO och SAF 1938?",["Kohandeln","Saltsjöbadsavtalet","Versaillesfreden","New Deal"],1),
 ("Vad menas med propaganda?",["Opartiska nyheter","Information som är gjord för att påverka","En lag","En sorts valsedel"],1),
]
TEST_B = [
 ("Vad menas med femårsplan?","Statlig plan för produktionen under fem år."),
 ("Nämn två orsaker till att Hitler kunde bli rikskansler 1933.","T.ex. depression och arbetslöshet, missnöje med Versailles, svaga demokratiska partier, politikers felbedömningar."),
 ("Vad är skillnaden mellan demokrati och diktatur?","I en demokrati väljer folket i fria val och rättigheter skyddas; i en diktatur styr en ledare eller ett parti utan fria val."),
 ("Vilka förföljdes i Nazityskland? Nämn tre grupper.","T.ex. judar, romer, homosexuella, politiska motståndare, Jehovas vittnen, funktionshindrade."),
 ("Vad innebar krispolitiken i Sverige?","Staten skapade arbete och stödde jordbruk i stället för att spara."),
 ("Varför används historia som propaganda?","För att rättfärdiga makten, skapa gemenskap och kontrollera hur människor ser på nutiden."),
]

KALLA = dict(
 text="Från ett utdrag ur en konstruerad tidningsartikel, 1934: ”Vår ledare har gett landet ordning och arbete. Alla som är emot honom är fiender till folket. Därför ska ingen läsa utländska tidningar.”",
 ursprung="Konstruerad källa baserad på hur statligt styrda tidningar kunde skriva i 1930-talets diktaturer. Författare och tidning är påhittade.",
 fragor=[
  ("Vilket syfte har texten?","Att stärka ledarens ställning och få läsarna att lita på honom och inte på andra källor (propaganda)."),
  ("Hitta två propagandaknep i texten.","Vi-och-de (”fiender till folket”), förbud mot andra källor, stora påståenden utan belägg, ensidighet."),
  ("Vad kan källan berätta för en historiker, trots att den är ensidig?","Hur regimen ville bli sedd och att den försökte hindra fria nyheter, alltså något om diktaturens metoder."),
  ("Vilka andra källor skulle du vilja ha för att veta mer?","T.ex. dagböcker, brev, utländska rapporter, domstolshandlingar, intervjuer med dem som levde då."),
 ])

SKRIV = dict(
 uppgift="Varför föll demokratin i Tyskland 1933 men inte i Sverige? Jämför de två länderna. Skriv 250–400 ord och använd begrepp från kapitlet. Ta med orsaker, händelser och minst en egen reflektion om vad vi kan lära oss.",
 stod=[
  "E: Eleven beskriver några händelser i Tyskland och Sverige (t.ex. depressionen, Hitler 1933, rösträtt 1921, Saltsjöbadsavtalet) och anger minst en orsak till skillnaden.",
  "C: Eleven förklarar flera orsaker (ekonomi, politiska val, folkrörelser, krispolitik), kopplar dem till varandra och använder begrepp som demokrati, diktatur, krispolitik.",
  "A: Eleven jämför på ett nyanserat sätt, väger orsakernas betydelse, nämner att forskare tolkar olika, och drar en välgrundad slutsats om demokratins sårbarhet och vad vi kan lära oss.",
 ])

LAB = dict(
 titel="Historikerns verkstad: Hur känner man igen propaganda?",
 syfte="Eleverna övar källkritik och propagandanalys genom att granska konstruerade texter och jämföra med egna dagens exempel.",
 material="Tre korta, konstruerade propagandatexter (lärarens), kopior av frågeguiden, tidslinje, penna.",
 utforande=[
  "Dela in klassen i grupper om tre.",
  "Varje grupp får en konstruerad text i stil med 1930-talets diktaturer (en affisch-text, en radiotext, en tidningsnotis). Inga verkliga symboler används.",
  "Gruppen markerar propagandaknep: vi och de, syndabock, upprepning, stora ord, utelämnade fakta.",
  "Gruppen ställer frågorna Vem? Till vem? Varför? När? Vad utelämnas?",
  "Grupperna skriver en motbild: en saklig text om samma ämne.",
  "Gemensam diskussion: finns liknande knep i dagens reklam, sociala medier och politik?",
 ],
 fragor=[
  ("Vad är den största skillnaden mellan propaganda och en saklig text?","Propagandan vill påverka känslor och förenklar, den sakliga texten redovisar belägg och olika perspektiv."),
  ("Varför är det svårt att känna igen propaganda?","Den spelar på känslor, ser ofta ut som nyheter och bekräftar det vi redan tycker."),
  ("Vad kan du göra för att kontrollera en uppgift?","Kolla flera oberoende källor, leta efter ursprung och syfte, fråga vem som tjänar på budskapet."),
 ],
 bonus="BONUS för läraren: Låt eleverna jämföra med en modern reklamtext och en nyhetsartikel. Diskutera skillnaden mellan övertalning och information. Bedöm källkritik (E: ställer frågor till källan, C: använder flera aspekter, A: drar slutsatser om trovärdighet).",
)

LARAR = [
 ("Koppling till Lgr22 (historia åk 7–9)","Kapitlet täcker centralt innehåll om imperialism och världskrig ca 1850–1950 (mellankrigstiden, Gulag), demokratisering ca 1900–nutid (rösträtt, folkrörelser) samt syftet om förändringsprocesser, källkritik och historiebruk. Eleverna tränar orsak och följd, kontinuitet och förändring, tolkning av källor och användning av historia (propaganda)."),
 ("Förslag på upplägg (8 lektioner)","1. Ryska revolutionen (10.1). 2. Stalin, Gulag och terror (10.2). 3. Demokratier och tjugotal (10.3), börskrasch (10.4). 4. Italien (10.5). 5. Weimar och 1933 (10.6). 6. Diktaturens kännetecken och propaganda (10.7), LAB. 7. Sverige (10.8), Ådalen som källarbete. 8. Fördjupning, repetition och test. Kombinera gärna med tidsresan (animationen)."),
 ("Vanliga missuppfattningar","”Hitler vann ett val och blev diktator”: nazisterna fick aldrig egen majoritet i fria val, och Hitler utsågs till rikskansler efter förhandlingar. ”Allt var Versailles fel”: forskare lyfter många orsaker. ”Kommunism = nazism”: de var olika ideologier men båda ledde till diktatur. ”Sverige var perfekt”: mörka sidor som steriliseringarna och Ådalen finns också."),
 ("Bedömningsstöd (E/C/A)","E: eleven beskriver några händelser och skillnader mellan demokrati och diktatur och anger en orsak. C: eleven förklarar flera orsaker och följder, jämför länder och använder källor. A: eleven väger orsaker, ser kontinuitet och förändring, tolkar propaganda och reflekterar över historiebruk med välgrundade slutsatser."),
 ("Tips: Blooket och Jeopardy","Kategorier: 1 Ryska revolutionen, 2 Stalin och Gulag, 3 Depressionen, 4 Italien, 5 Tyskland till 1933, 6 Diktaturens kännetecken, 7 Propaganda, 8 Sverige, 9 Begrepp, 10 Årtal. Exempel: ”Vilket år bildades Sovjetunionen?” (1922). ”Vad hette överenskommelsen 1938 mellan LO och SAF?” (Saltsjöbadsavtalet)."),
]

KALLOR = [
 ("Riksdagen – Demokratins utveckling i Sverige (parlamentarism 1917, rösträtt 1921, kvinnor i riksdagen 1922)","https://www.riksdagen.se/sv/sa-fungerar-riksdagen/riksdagens-historia/demokratins-utveckling-i-sverige/"),
 ("Store norske leksikon – Gulag (omfattning, officiella siffror, dödstal)","https://snl.no/Gulag"),
  ("Store norske leksikon – Fascismen i Italia (Mussolini 1919–1945, marschen mot Rom 1922)","https://snl.no/Fascismen_i_Italia"),
   ("USHMM – Kristallnacht (omfattning, arresteringar, 9–10 november 1938)","https://encyclopedia.ushmm.org/content/en/article/kristallnacht"),
 ("Nordics.info – Sweden's Saltsjöbaden Agreement (LO, SAF, december 1938)","https://nordics.info/show/artikel/swedens-saltsjoebaden-agreement"),
 ("SVT – 80 år sen skotten i Ådalen (14 maj 1931, Lunde)","https://www.svt.se/nyheter/lokalt/vasternorrland/80-ar-sen-skotten-i-adalen"),
 ("Forum för levande historia – Holodomor, faktatext (dödstal, orsaker, folkmordsfrågan)","https://www.levandehistoria.se/wp-content/uploads/2022/10/holodomor_-_faktatext.pdf"),
 ]

BLOOKET = [
 ("Vilket parti tog makten i Ryssland i november 1917?","Bolsjevikerna","Mensjevikerna","Liberalerna","Fascisterna"),
 ("Vem ledde bolsjevikerna 1917?","Lenin","Stalin","Trotskij","Mussolini"),
 ("Vilket år bildades Sovjetunionen?","1922","1917","1929","1933"),
 ("Vad var en femårsplan?","En statlig plan för produktionen under fem år","Ett femårigt krig","En valperiod","Ett handelsavtal"),
 ("Vad var Gulag?","Sovjetunionens system av arbetsläger","Ett parti","En stad","Ett slag"),
 ("Vilka år pågick den stora terrorn i Sovjet?","1937–1938","1917–1918","1925–1926","1941–1942"),
 ("Vad hände i New York 24 oktober 1929?","Börsen störtade","Ett val hölls","Ett krig bröt ut","En revolution"),
 ("Vad menas med depression?","Långvarig djup ekonomisk kris","En sjukdom","Ett ordspråk","En form av rösträtt"),
 ("Vem ledde fascisterna i Italien?","Mussolini","Franco","Hitler","Lenin"),
 ("Vilket år marscherade fascisterna mot Rom?","1922","1917","1933","1938"),
 ("Vad kallades Mussolini?","Il Duce","Der Führer","Caudillo","Tsar"),
 ("Vad kallas den tyska republiken 1919–1933?","Weimarrepubliken","Tredje riket","Kejsardömet","Sovjetunionen"),
 ("Vad hände med priserna i Tyskland 1923?","De skenade (hyperinflation)","De sjönk kraftigt","De var stabila","De halverades"),
 ("Hur många var arbetslösa i Tyskland vintern 1932 (ungefär)?","Omkring 6 miljoner","Omkring 600 000","Omkring 60 miljoner","Omkring 60 000"),
 ("När utnämndes Hitler till rikskansler?","30 januari 1933","1 september 1939","9 november 1938","8 maj 1945"),
 ("Vad lät regeringen göra efter fullmaktslagen?","Stifta lagar utan riksdagen","Avskaffa kejsaren","Hålla fria val","Ge kvinnor rösträtt"),
 ("Vad kallas information som är gjord för att påverka?","Propaganda","Statistik","Källa","Biografi"),
 ("Vilket år fick Sverige allmän och lika rösträtt (för båda könen)?","1921","1809","1950","1971"),
 ("Hur många dödades i Ådalen 1931?","Fem","Femtio","Tre","Hundra"),
 ("Vem var Sveriges statsminister under större delen av 1932–1946?","Per Albin Hansson","Tage Erlander","Olof Palme","Carl Bildt"),
 ("Vad var kohandeln?","Överenskommelse mellan S och Bondeförbundet 1933","Ett marknadsstopp","Ett krig","Ett lån från USA"),
 ("Vilka slöt Saltsjöbadsavtalet 1938?","LO och SAF","S och M","Sverige och Finland","USA och Sverige"),
 ("Vad var kristallnatten 1938?","En våg av våld mot judar i Tyskland","En storm","Ett val","Ett möte"),
 ("Vad var Nürnberglagarna 1935?","Lagar som tog bort judars medborgerliga rättigheter","Fredsavtal","Skattelagar","Regler om skolor"),
 ("Vem ledde upproret i Spanien 1936?","Franco","Mussolini","Hitler","Stalin"),
 ("Vad hette staden som bombades 1937 och blev symbol?","Guernica","Madrid","Warszawa","Barcelona"),
 ("Vilket styrelseskick kännetecknas av fria val och yttrandefrihet?","Demokrati","Diktatur","Enpartistat","Monarki utan val"),
]

JEOPARDY = {
 "Ryssland och Sovjet":[(100,"Ledare för bolsjevikerna 1917.","Lenin"),(200,"Året då Sovjetunionen bildades.","1922"),(300,"Sovjetiska arbetsläger.","Gulag"),(400,"Stalins plan för snabb industrialisering.","Femårsplan"),(500,"Åren för den stora terrorn.","1937–1938")],
 "Krisen":[(100,"Staden där börsen föll 1929.","New York"),(200,"Namn på den långvariga krisen på 1930-talet.","Depressionen"),(300,"Roosevelts program.","New Deal"),(400,"Vad hände med priserna i Tyskland 1923?","Hyperinflation"),(500,"Ungefär så många var arbetslösa i Tyskland 1932.","6 miljoner")],
 "Diktatur":[(100,"Ledare i Italien.","Mussolini"),(200,"Året för marschen mot Rom.","1922"),(300,"Information för att påverka.","Propaganda"),(400,"Datum då Hitler blev rikskansler.","30 januari 1933"),(500,"Lag 1933 som lät regeringen stifta lagar utan riksdagen.","Fullmaktslagen")],
 "Sverige":[(100,"Året för allmän rösträtt.","1921"),(200,"Plats där militär sköt 1931.","Ådalen"),(300,"Statsminister under större delen av 1932–1946.","Per Albin Hansson"),(400,"Överenskommelse 1933 S–Bondeförbundet.","Kohandeln"),(500,"Avtal 1938 mellan LO och SAF.","Saltsjöbadsavtalet")],
 "Begrepp":[(100,"Styrelseskick med fria val.","Demokrati"),(200,"Hat mot judar.","Antisemitism"),(300,"Regeringen måste ha riksdagens stöd.","Parlamentarism"),(400,"Person som får skulden för andras problem.","Syndabock"),(500,"Hur människor använder historia för olika syften.","Historiebruk")],
}

GRUPPER = [
 ("ryssland","Revolution och Sovjetunionen","Så började världens första kommunistiska stat – och så blev den en diktatur.",["ryska","stalin"]),
 ("kris","Demokratier i kris","Nya demokratier, glada tjugotal och depressionen.",["tjugotal","kris"]),
 ("diktaturer","Fascism och nazism","Mussolini och Hitler tog makten – och byggde diktaturer.",["italien","tyskland","diktatur"]),
 ("sverige","Sverige","Hur Sverige stärkte demokratin.",["sverige"]),
]

SCEN = dict(
 titel="Tidsresa genom mellankrigstiden", plats="Europa och USA", tid="1917–1938",
 sky=("#b9c6d3","#e8e1d2"), mark="#8a8272",
 walker=dict(typ="medborgare"),
 etapper=[
  dict(x_etikett="Petrograd", tid="1917", plats="Petrograd, Ryssland", rubrik="Revolution i vinterkylan",
   fakta=["Du bor i Petrograd i Ryssland. Det är krig, och det finns knappt något bröd. Folk är hungriga och arga.","Tsaren har tvingats avgå. I november tar bolsjevikerna makten. De lovar att Ryssland ska sluta kriget, att bönderna ska få jord och att folk ska få bröd."],
   fraga="Vad lovade bolsjevikerna?", alt=["Mer krig och en ny kung","Fred, jord och bröd","Lägre skatter och fria val"], ratt=1, forklaring="Löftena gav dem stöd hos trötta soldater, hungriga arbetare och bönder.",
   ord=[("bolsjeviker","det ryska parti som tog makten 1917 under Lenin")],
   deko=[("folkmassa",0,1.2),("flagga_rod",120,1.0),("arbetarhus",-150,1.0)]),
  dict(x_etikett="Rom", tid="1922", plats="Rom, Italien", rubrik="Marschen mot Rom",
   fakta=["Du är i Rom i Italien. Fascisterna, ledda av Benito Mussolini, marscherar mot staden. De hotar med våld.","Kungen blir rädd och gör Mussolini till regeringschef. Efter några år är Italien en diktatur. Då bestämmer en enda man."],
   fraga="Hur fick Mussolini makten 1922?", alt=["Han vann ett krig mot grannlandet","Fascisterna hotade med våld och kungen gav honom makten","Folket valde honom i ett fritt val"], ratt=1, forklaring="Han fick makten på ett lagligt sätt, men bara för att kungen var rädd för våld.",
   ord=[("diktatur","styrelseskick där en person eller ett parti bestämmer allt"),("fascism","rörelse som vill ha en stark ledare och förbjuder motstånd")],
   deko=[("colosseum",-80,1.3),("folkmassa",120,1.0)]),
  dict(x_etikett="Berlin", tid="1923", plats="Berlin, Tyskland", rubrik="Pengar som inte betyder något",
   fakta=["Du är i Berlin. Priserna stiger för varje timme. Du får lönen i högar av sedlar och springer till affären innan pengarna är värda ännu mindre.","När priserna rusar så här kallas det hyperinflation. Sparpengar blir värdelösa, och många människor förlorar tron på republiken."],
   fraga="Vad kallas det när priserna stiger snabbt och pengarna blir värdelösa?", alt=["Hyperinflation","Strejk","Folkomröstning"], ratt=0, forklaring="I november 1923 kostade en dollar flera biljoner mark.",
   ord=[("hyperinflation","när priserna stiger extremt snabbt och pengarna blir värdelösa"),("republik","land utan kung, där folket väljer ledarna")],
   deko=[("marknad",0,1.1),("folkmassa",-140,1.0)]),
  dict(x_etikett="New York", tid="1929", plats="New York, USA", rubrik="Aktierna faller",
   fakta=["Du står utanför börsen i New York. Den 24 oktober 1929 faller priset på aktier kraftigt. Många förlorar alla sina pengar.","Banker går i konkurs och miljontals människor blir arbetslösa. Krisen sprider sig till andra länder. Den långa krisen på 1930-talet kallas depressionen."],
   fraga="Vad kallas den långa ekonomiska krisen på 1930-talet?", alt=["De glada tjugotalen","Depressionen","Kalla kriget"], ratt=1, forklaring="Depressionen drabbade USA, Tyskland, Sverige och många fler länder.",
   ord=[("aktie","en liten del av ett företag som du kan köpa och sälja"),("depression","lång tid med många arbetslösa och dålig ekonomi")],
   deko=[("skorstenar",-120,1.2),("folkmassa",100,1.0)]),
  dict(x_etikett="Ådalen", tid="1931", plats="Lunde, Ådalen, Sverige", rubrik="Skotten i Ådalen",
   fakta=["Du är i Ådalen i Sverige. Arbetare demonstrerar mot lägre löner och mot strejkbrytare. Strejkbrytare tar jobben när andra strejkar.","Militär är på plats. Den 14 maj 1931 skjuter soldaterna mot demonstranterna. Fem människor dör."],
   fraga="Hur många människor dog när soldaterna sköt i Ådalen?", alt=["Fem","Femtio","Ingen"], ratt=0, forklaring="Händelsen väckte starka reaktioner i hela Sverige och påverkade politiken.",
   ord=[("strejk","när arbetare slutar jobba för att kräva bättre villkor")],
   deko=[("gran",-130,1.2),("folkmassa",60,0.9),("trad",160,1.0)]),
  dict(x_etikett="Berlin", tid="1933", plats="Berlin, Tyskland", rubrik="Demokratin avskaffas",
   fakta=["Du är i Berlin. Den 30 januari 1933 blir Adolf Hitler Tysklands regeringschef (rikskansler). I mars kommer fullmaktslagen.","Med den lagen får regeringen göra egna lagar utan att fråga riksdagen. Andra partier och fackföreningar förbjuds. Staten styr radion och tidningarna."],
   fraga="Vad innebar fullmaktslagen?", alt=["Regeringen kunde göra lagar utan riksdagen","Alla barn måste gå i skolan","Det blev fri handel med andra länder"], ratt=0, forklaring="Riksdagen förlorade sin makt, och Tyskland blev en diktatur med bara ett parti.",
   ord=[("demokrati","styrelseskick där folket väljer ledarna i fria val")],
   deko=[("radio",-100,1.0),("folkmassa",120,1.1)]),
  dict(x_etikett="Saltsjöbaden", tid="1938", plats="Saltsjöbaden, Sverige", rubrik="Överenskommelse i stället för strid",
   fakta=["Du är i Saltsjöbaden nära Stockholm. I december 1938 skriver LO (arbetarnas fack) och SAF (arbetsgivarna) på Saltsjöbadsavtalet. De ska lösa konflikter genom att förhandla.","Medan demokratin faller i flera länder bygger Sverige vidare på folkrörelser, förhandlingar och reformer."],
   deko=[("villa",-100,1.2),("riksdagshus",120,1.0)]),
 ],
 diskutera="Varför blev vissa länder diktaturer medan Sverige förblev en demokrati? Ge exempel från resan.",
)
