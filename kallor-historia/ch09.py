# -*- coding: utf-8 -*-
# Kapitel 9 – Första världskriget (åk 8). Fakta hållna konsekventa med simuleringen forsta-varldskriget.html
T = dict(
 nr=9, namn="Första världskriget", under="Det stora kriget 1914–1918 och världen efteråt",
 fil="historia-09-forsta-varldskriget", arskurs=8, nodeid="historia-forsta-varldskriget",
 mal=["förklara orsakerna till första världskriget (militarism, allianser, imperialism och nationalism)",
      "berätta vad som hände i Sarajevo 1914 och hur kriget spreds",
      "beskriva skyttegravskriget på västfronten och kriget på östfronten",
      "förklara hur ny teknik förändrade krigföringen",
      "beskriva hur kriget påverkade hemmafronten och kvinnors arbete",
      "förklara varför USA gick med 1917 och vad som hände i Ryssland",
      "förklara hur kriget slutade och vilka följder freden i Versailles fick",
      "beskriva hur Sverige påverkades trots neutraliteten, och hur kriget minns idag"],
 fundera="Många unga män anmälde sig frivilligt 1914 och trodde att kriget skulle vara över till jul. Varför tror du att de trodde det? Och vad tror du hände med den tron? Skriv två meningar.",
)

S = []

S.append(dict(id="orsaker", nr="9.1", ikon="🧩", titel="Varför bröt kriget ut?",
 intro="Första världskriget hade inte en enda orsak. Historiker brukar peka på flera saker som byggde upp spänningar i Europa. Många använder förkortningen <strong>MAIN</strong> för att komma ihåg dem.",
 block=[
  ("p","<strong>M</strong> står för <strong>militarism</strong>. Stormakterna rustade upp med fler soldater, kanoner och fartyg. Många trodde att en stark armé var det bästa sättet att skydda landet, och att ett krig skulle gå fort."),
  ("p","<strong>A</strong> står för <strong>allianser</strong>. Länderna hade slutit avtal om att hjälpa varandra. Tyskland och Österrike-Ungern stod nära varandra, och Italien var med i trippelalliansen från 1882. Frankrike och Ryssland slöt en allians 1894, och 1907 bildades trippelententen mellan Storbritannien, Frankrike och Ryssland."),
  ("p","<strong>I</strong> står för <strong>imperialism</strong>. Stormakterna konkurrerade om kolonier och handel, och det skapade misstro. <strong>N</strong> står för <strong>nationalism</strong>. Stolthet över det egna landet kunde bli fientlighet mot andra. På Balkan ville flera folk bilda egna stater, och det skapade konflikter med Österrike-Ungern och Osmanska riket."),
  ("tab",["Bokstav","Orsak","Exempel"],[
    ["M","Militarism","Tysklands och Storbritanniens kapplöpning om flottor"],
    ["A","Allianser","Trippelententen och trippelalliansen"],
    ["I","Imperialism","Konkurrens om kolonier i Afrika och Asien"],
    ["N","Nationalism","Serbiens och andra folks krav på egna stater"]]),
  ("ruta","tank","Långsiktigt och kortsiktigt","Historiker skiljer på <em>långsiktiga orsaker</em> (MAIN, som byggdes upp i decennier) och en <em>utlösande orsak</em> (skotten i Sarajevo 1914). Den utlösande orsaken är gnistan, men de långsiktiga orsakerna är torrt gräs som låter elden sprida sig."),
  ("kolla",["Vad står bokstäverna M, A, I, N för?","Vad är en allians?","Vad är skillnaden mellan långsiktiga orsaker och en utlösande orsak?"]),
 ],
 svar=["Militarism, allianser, imperialism, nationalism.","Ett avtal mellan stater om att hjälpa varandra.","Långsiktiga orsaker byggs upp under lång tid. Den utlösande orsaken är händelsen som får det att brisera."],
))

S.append(dict(id="sarajevo", nr="9.2", ikon="🔫", titel="Sarajevo 1914 – skotten som tände kriget",
 intro="Den 28 juni 1914 hände något i staden Sarajevo som skulle förändra världen. Inom några veckor var Europas stormakter i krig.",
 block=[
  ("p","Bosnien hade tagits över av Österrike-Ungern. Många bosnienserber ville i stället att området skulle höra till Serbien. Den 28 juni 1914 besökte tronföljaren, ärkehertig Franz Ferdinand, Sarajevo tillsammans med sin fru Sophie. Den 19-årige Gavrilo Princip, som tillhörde en hemlig grupp som ville befria de sydslaviska folken från Österrike-Ungerns styre, sköt dem båda."),
  ("p","Österrike-Ungern gav Serbien skulden och ställde hårda krav, ett så kallat <strong>ultimatum</strong>. Serbien gick med på nästan allt, men Österrike-Ungern förklarade ändå krig den 28 juli. Ryssland stödde Serbien och började mobilisera, alltså kalla in sina soldater. Då förklarade Tyskland krig mot Ryssland och Frankrike."),
  ("tidslinje",[("28 juni","Skotten i Sarajevo"),("23 juli","Österrike-Ungerns ultimatum till Serbien"),("28 juli","Österrike-Ungern förklarar Serbien krig"),("1 augusti","Tyskland förklarar Ryssland krig"),("4 augusti","Storbritannien går in i kriget efter Tysklands anfall mot Belgien")]),
  ("p","Tyskland hade en plan, <strong>Schlieffenplanen</strong>: att snabbt besegra Frankrike genom att gå genom det neutrala Belgien, och sedan vända sig mot Ryssland. Storbritannien hade lovat skydda Belgiens neutralitet och gick därför med i kriget. Inom en vecka var stormakterna i krig."),
  ("ruta","historia","Orsak och konsekvens","Mordet i Sarajevo var <em>inte</em> ensamt orsaken till världskriget. Det var gnistan som fick allianssystemet att sätta i gång. Fundera: Hade kriget kommit ändå? Det tycker historiker olika om."),
  ("ruta","visste","Stor jubel","I augusti 1914 jublade folkmassor i flera huvudstäder, och många unga män anmälde sig frivilligt. Många trodde att kriget skulle vara över till jul."),
  ("kolla",["Vem sköts i Sarajevo, och av vem?","Hur ledde mordet till krig mellan så många länder?","Varför gick Storbritannien med i kriget?"]),
 ],
 svar=["Franz Ferdinand och hans fru Sophie sköts av Gavrilo Princip.","Allianserna gjorde att länder drogs in efter varandra.","Tyskland gick in i det neutrala Belgien, som Storbritannien lovat skydda."],
))

S.append(dict(id="fronterna", nr="9.3", ikon="🪖", titel="Skyttegravar och fronter",
 intro="Många trodde att kriget skulle bli kort och rörligt. I stället fastnade armén i skyttegravar, särskilt på västfronten i Frankrike och Belgien.",
 block=[
  ("p","Tyskarna stoppades i september 1914 vid floden Marne, inte långt från Paris. Båda sidor grävde ner sig. Snart gick en linje av skyttegravar från Nordsjön ner till Schweiz, omkring 70 mil lång. Det kallades <strong>västfronten</strong>. Området mellan fienderna kallades <strong>ingenmansland</strong>."),
  ("p","Livet i skyttegraven var hårt: lera, kyla, råttor och löss. Soldaterna väntade, grävde och levde med ständig fara. Att anfalla över ingenmansland mot kulsprutor och taggtråd kostade tusentals liv för några hundra meter."),
  ("tab",["Slag","År","Vad hände?"],[
    ["Verdun","1916","Tysk offensiv mot fransk fästning. Omkring 700 000 dödade, sårade eller försvunna. Fronten flyttades nästan inte."],
    ["Somme","1916","Brittisk och fransk offensiv. Första dagen förlorade britterna omkring 57 000 man. Stridsvagnar används första gången."],
    ["Tannenberg","1914","Tysk seger på östfronten. Omkring 90 000 ryssar tillfångatogs."],
    ["Gallipoli","1915–16","De allierade försökte ta sig förbi Dardanellerna men gav upp efter åtta månader."]]),
  ("p","På <strong>östfronten</strong>, mot Ryssland, var kriget mer rörligt, eftersom fronten var mycket längre. Ryssland hade världens största armé, men dåligt med vapen, skor och ammunition. Förlusterna blev enorma."),
  ("ruta","historia","Julfreden 1914","På julafton och juldagen 1914 slutade soldater på flera ställen längs västfronten att skjuta. De mötte varandra i ingenmansland och bytte små gåvor. Befälen gillade det inte. Berättelsen är ett bra exempel på hur källor och minnen påverkar hur vi ser historien. Mer om det i fördjupningen."),
  ("ruta","fakta","Folkmordet på armenierna","Under kriget förföljdes den armeniska folkgruppen i Osmanska riket. Mycket stora antal armenier mördades eller dog på dödsmarscher. Uppskattningarna går från omkring en miljon till 1,5 miljoner. Många forskare och flera länder, bland dem Sverige (2010), kallar det folkmord. Turkiet godtar inte den beteckningen."),
  ("kolla",["Vad är ingenmansland?","Varför blev kriget på västfronten ett ställningskrig?","Nämn en skillnad mellan väst- och östfronten."]),
 ],
 svar=["Området mellan fiendernas skyttegravar.","Båda sidor grävde ner sig, och kulsprutor och taggtråd gjorde anfall mycket dyra.","Västfronten var statisk i skyttegravar, östfronten var längre och mer rörlig."],
))

S.append(dict(id="teknik", nr="9.4", ikon="🛠️", titel="Ny teknik, nya vapen",
 intro="Industrialiseringen hade gjort det möjligt att tillverka vapen i stor skala. Första världskriget blev det första stora kriget med moderna maskiner.",
 block=[
  ("p","<strong>Kulsprutan</strong> kunde skjuta hundratals skott i minuten och gjorde anfall över öppen mark nästan självmordsliknande. <strong>Artilleri</strong>, stora kanoner, kunde beskjuta fiender långt bort. Marken blev förvandlad till krater- och lerlandskap."),
  ("p","<strong>Giftgas</strong> användes första gången i större skala vid Ypres den 22 april 1915, då tyskarna släppte ut klorgas. Snart använde båda sidor gas, och soldaterna fick gasmasker. Giftgas förbjöds efter kriget genom ett internationellt avtal 1925."),
  ("p","<strong>Stridsvagnen</strong> sattes in av britterna i september 1916. De första var långsamma och gick ofta sönder, men de pekade mot framtidens krig. Ordet <em>tank</em> användes för att hålla den hemlig. <strong>Flygplan</strong> användes först för spaning, sedan i luftstrider och för att fälla bomber. <strong>Ubåtar</strong> sänkte fartyg: 1915 sänktes passagerarfartyget Lusitania, och omkring 1 200 människor dog."),
  ("tab",["Teknik","Betydelse"],[
    ["Kulspruta","Gjorde anfall mycket blodiga och försvar lätt"],
    ["Artilleri","Kunde förstöra hela landskap"],
    ["Gas","Skapade skräck, gasmasker infördes"],
    ["Stridsvagn","Kunde ta sig över skyttegravar"],
    ["Flygplan","Spaning och senare bomber och luftstrid"],
    ["Ubåt","Kriget mot handelsfartyg"]]),
  ("bild","ww1","Skyttegravar och taggtråd präglade västfronten."),
  ("ruta","tank","Fundera","Ny teknik gjorde kriget dödligare men gjorde inte det lättare att vinna. Varför tror du att så många soldater ändå skickades över ingenmansland?"),
  ("kolla",["Varför gjorde kulsprutan kriget annorlunda?","När användes gas första gången i stor skala?","Nämn två nya vapen och hur de användes."]),
 ],
 svar=["Den gjorde anfall över öppen mark mycket farliga, så försvaret fick fördel.","Vid Ypres i april 1915.","T.ex. stridsvagn (bryta igenom skyttegravar), ubåt (sänka fartyg), flygplan (spaning/bomber)."],
))

S.append(dict(id="hemma", nr="9.5", ikon="🏠", titel="Hemmafronten och kvinnorna",
 intro="Kriget påverkade alla, inte bara soldaterna. Hemma fick människor leva med brist, oro och nya uppgifter. Det kallas <strong>hemmafronten</strong>.",
 block=[
  ("p","Länderna ställde om hela samhället för att föra krig, ett så kallat <strong>totalt krig</strong>. Fabriker tillverkade vapen i stället för varor. Maten ransonerades, alltså fördelades med kuponger. Regeringarna använde propaganda, budskap för att påverka människor, för att få folk att stödja kriget."),
  ("p","Brittiska flottan stoppade fartyg på väg till Tyskland, även mat. Vintern 1916–1917 kallas i Tyskland kålrotsvintern, eftersom kålrötter nästan var det enda som fanns. Hundratusentals civila dog av svält och sjukdomar under kriget."),
  ("p","När miljontals män skickades till fronten tog <strong>kvinnor</strong> över många jobb: i fabriker, som spårvagnsförare, på kontor och på sjukhus. Många kvinnor arbetade som sjuksköterskor nära fronten. Det visade att kvinnor kunde göra samma arbeten som män."),
  ("ruta","historia","Kontinuitet och förändring","<strong>Förändring:</strong> kvinnor fick nya arbeten och blev ekonomiskt viktiga. I flera länder, bland annat Storbritannien (då bara för kvinnor över 30 som uppfyllde vissa villkor) och Tyskland, fick kvinnor rösträtt omkring 1918. <strong>Kontinuitet:</strong> kvinnor fick ofta lägre lön, och när männen kom hem förväntades många lämna jobben."),
  ("kalla","Brev från en sjuksköterska (konstruerad källa)","Vi tar emot de sårade dygnet runt. Jag trodde aldrig att jag skulle orka, men det finns ingen annan. Hemma tycker folk att kriget är ett äventyr. De borde se vad vi ser.","Konstruerad källa baserad på sjuksköterskors brev och dagböcker från första världskriget."),
  ("kolla",["Vad är hemmafronten?","Nämn två sätt som kvinnors liv förändrades.","Vad är propaganda?"]),
 ],
 svar=["Det som sker hemma i samhället under kriget, t.ex. brist, ransonering och arbete för kriget.","T.ex. nya arbeten i fabriker och på kontor, sjukvård vid fronten, och rösträtt i vissa länder.","Budskap som ska påverka människors åsikter, t.ex. för att få dem att stödja kriget."],
))

S.append(dict(id="ar1917", nr="9.6", ikon="🔄", titel="1917 – USA går med, Ryssland lämnar",
 intro="År 1917 vände kriget. Det land som tidigare stått utanför, USA, gick med, medan Ryssland drabbades av revolution.",
 block=[
  ("p","Tyskland började 1 februari 1917 sänka alla fartyg runt Storbritannien utan förvarning, även fartyg från neutrala länder. Samtidigt avslöjades Zimmermanntelegrammet, där Tyskland försökt få Mexiko att anfalla USA. Den 6 april 1917 förklarade USA krig mot Tyskland. Sommaren 1918 fanns över en miljon amerikanska soldater i Frankrike, och vid krigsslutet omkring två miljoner."),
  ("p","I <strong>Ryssland</strong> hade kriget gått dåligt. Miljontals soldater hade dött, och folket svalt. Våren 1917 tvingades tsaren avgå. I november tog bolsjevikerna under Lenin makten. I mars 1918 slöt Ryssland fred med Tyskland och lämnade kriget. Det blev början på Sovjetunionen. Den ryska revolutionen kommer du att läsa mer om senare."),
  ("tab",["Händelse","Vad betydde den?"],[
    ["USA går med (april 1917)","Nya soldater och stor industri på de allierades sida"],
    ["Revolutionen i Ryssland","Ryssland lämnar kriget 1918, men Tyskland kan flytta trupper västerut"],
    ["Tysk våroffensiv 1918","Sista stora anfallet, men misslyckas"]]),
  ("ruta","tank","Orsak och konsekvens","Orsak: ubåtskriget och Zimmermanntelegrammet. Konsekvens: USA går med och de allierade får nya reserver. Tänk efter: kunde Tyskland ha vunnit utan att USA gick med?"),
  ("kolla",["Vilka två saker fick USA att gå med i kriget?","Vad hände i Ryssland 1917?","Varför var USA:s intåg viktigt?"]),
 ],
 svar=["Ubåtskriget mot även neutrala fartyg och Zimmermanntelegrammet.","Tsaren avgick, och bolsjevikerna tog makten i november. 1918 slöt Ryssland fred.","USA hade nya soldater och stor industri medan Tyskland saknade reserver."],
))

S.append(dict(id="slutet", nr="9.7", ikon="🕊️", titel="Krigsslutet, Versailles och följderna",
 intro="Efter fyra år tystnade vapnen. Men freden som följde kom att präglas av bitterhet.",
 block=[
  ("p","Hösten 1918 trycktes Tyskland tillbaka av de allierade, nu med hjälp av amerikanska trupper. I Tyskland gjorde soldater och arbetare uppror, och kejsaren flydde. Den <strong>11 november 1918</strong> klockan 11 upphörde striderna. Vapenstilleståndet undertecknades i en järnvägsvagn i skogen vid Compiègne."),
  ("p","Freden skrevs under den 28 juni 1919 i Spegelsalen i slottet Versailles, exakt fem år efter skotten i Sarajevo. Tyskland fick inte vara med och förhandla. Landet tvingades ta på sig skulden för kriget, betala stora skadestånd och lämna ifrån sig land."),
  ("p","Nya stater bildades när de stora kejsardömena föll. Fyra imperier försvann: det tyska, det österrikisk-ungerska, det ryska och det osmanska. Länder som Polen, Tjeckoslovakien och de baltiska staterna växte fram. Man grundade också <strong>Nationernas förbund</strong> för att förhindra nya krig, men USA gick aldrig med."),
  ("p","Omkring 15–20 miljoner människor dog, soldater och civila. Mot slutet av kriget och året därpå, 1918–1919, drabbades världen av <strong>spanska sjukan</strong>, en influensa som spreds snabbt. I Sverige dog enligt SCB omkring 34 000 människor i den (SCB anger 34 374 dödsfall)."),
  ("tab",["Följd","Förklaring"],[
    ["Hård fred","Tyskland skuldbelades, förlorade land och fick betala skadestånd"],
    ["Nya stater","Polen, Tjeckoslovakien, de baltiska länderna m.fl."],
    ["Nationernas förbund","Skulle lösa tvister utan krig, men var svagt"],
    ["Bitterhet","Många tyskar kände sig förödmjukade"]]),
  ("ruta","historia","Historiebruk: 11 november och vallmon","Varje år minns många länder krigets offer den 11 november. I Storbritannien och många andra länder bär man röda vallmor. Symbolen kommer från dikten <em>In Flanders Fields</em> (1915) av John McCrae. Den första brittiska vallmodagen hölls 1921. Vita vallmor, som introducerades på 1930-talet, symboliserar fred. Vem använder vallmon, och varför? Olika människor lägger olika betydelse i den."),
  ("kolla",["Vad hände den 11 november 1918?","Nämn två följder av Versaillesfreden.","Vad är en vallmo ett exempel på i historiebruk?"]),
 ],
 svar=["Striderna upphörde, vapenstillestånd undertecknades.","T.ex. Tysklands skuld och skadestånd, nya stater, Nationernas förbund.","En symbol som används för att minnas krigets offer, med olika betydelser för olika människor."],
))

S.append(dict(id="sverige", nr="9.8", ikon="🇸🇪", titel="Sverige – neutralt men påverkat",
 intro="Sverige deltog aldrig i kriget. Men kriget kom ändå nära, och det förändrade landet.",
 block=[
  ("p","Sverige förklarade sig <strong>neutralt</strong>, alltså att landet inte tog parti. Så gjorde också Norge och Danmark. I december 1914 träffades kungarna från de tre länderna i Malmö och bekräftade att de skulle hålla sig utanför."),
  ("p","Blockaderna försvårade import av mat. Efter en dålig skörd 1916 infördes ransonering av bröd, socker och andra varor. Samtidigt blev vissa rika på att sälja varor till de krigförande länderna. De kallades <strong>gulaschbaroner</strong>, vilket ökade klyftorna."),
  ("p","Våren 1917 bröt <strong>hungerkravaller</strong> ut i flera städer. I Malmö samlades omkring 25 000 människor på Stortorget den 25 april, efter att brödransonen sänkts. Kvinnor deltog i stor utsträckning. Protesterna handlade om mat, men också om växande klyftor och politiska krav, bland annat på demokratiska reformer."),
  ("p","Under 1917 bildades en regering med liberaler och socialdemokrater, ledd av Nils Edén. <strong>Hjalmar Branting</strong>, socialdemokraternas ledare, blev finansminister (till januari 1918). Rösträtten utvidgades i etapper: 1918 fattade riksdagen ett principbeslut om rösträtt för kvinnor, och 1921 hölls det första riksdagsvalet med allmän och lika rösträtt. Branting blev senare statsminister och fick 1921 Nobels fredspris tillsammans med Christian Lange."),
  ("tidslinje",[("1914","Trekungamötet i Malmö"),("1916","Dålig skörd, ransonering införs"),("1917","Hungerkravaller. Regering med socialdemokrater"),("1918","Principbeslut om rösträtt"),("1921","Första valet med allmän och lika rösträtt")]),
  ("ruta","fakta","Orsak och konsekvens","Orsaker: blockader, dålig skörd, krig och klyftor. Konsekvenser: protester, politiska förändringar och utvidgad demokrati. Kriget, som Sverige inte deltog i, bidrog alltså till att demokratin utvidgades, men det fanns också andra orsaker, till exempel en lång rösträttsrörelse."),
  ("kolla",["Vad innebär att vara neutral?","Varför blev det hungerkravaller i Sverige 1917?","Vilka demokratiska förändringar följde?"]),
 ],
 svar=["Att man inte tar parti eller deltar i kriget.","Matbrist på grund av blockader och dålig skörd, samt missnöje med klyftor och krav på rösträtt.","Regering med socialdemokrater, och allmän och lika rösträtt med första valet 1921."],
))

F = []

F.append(dict(id="f1", nr="F1", ikon="⚖️", titel="Vem bar skulden? Historiker i debatt",
 intro="I Versaillesfreden fick Tyskland skulden för kriget. Historiker har diskuterat frågan sedan dess.",
 block=[
  ("p","Fredsavtalet innehöll en paragraf om att Tyskland och dess allierade var ansvariga för skadorna. Många tyskar uppfattade det som en skuldförklaring och en förödmjukelse. Den kallas ibland ”krigsskuldsparagrafen”."),
  ("p","Under årens lopp har historiker förklarat kriget på olika sätt. Vissa har lagt mest ansvar på Tyskland, andra har menat att alla stormakter hade del. Ytterligare andra har framhållit att ingen ville ha ett så stort krig, men att allianserna och misstroendet gjorde det svårt att stoppa."),
  ("tab",["Tolkning","Argument"],[
    ["Tyskland bär huvudansvaret","Tyskland gav stöd till Österrike-Ungern och anföll via Belgien"],
    ["Alla stormakter delade ansvar","Allianser och upprustning i alla länder"],
    ["Misstag och missförstånd","Beslutsfattare räknade fel och trodde på ett kort krig"]]),
  ("ruta","tank","Fundera","Varför är det viktigt vem som tar skulden? Tänk på vad skuldfrågan betydde för freden och för tyskarnas känslor efteråt."),
  ("kolla",["Vad innebar skuldparagrafen?","Nämn två olika tolkningar av vem som bar skulden.","Varför kan skuldfrågan vara politiskt viktig?"]),
 ],
 svar=["Att Tyskland och dess allierade ansågs ansvariga för kriget och skadorna.","T.ex. att Tyskland hade huvudansvaret, eller att alla stormakter delade ansvaret.","Den påverkade skadestånd och känslor, och används i politisk debatt."],
))

F.append(dict(id="f2", nr="F2", ikon="🌐", titel="Ett världskrig – även utanför Europa",
 intro="Kriget kallas världskrig, men berättas ofta som en europeisk historia. Hur såg det ut utanför västfronten?",
 block=[
  ("p","Kriget fördes också i Afrika och Asien, där Europas kolonier drogs in. Soldater och arbetare från kolonierna skickades till fronterna. Från Australien och Nya Zeeland kom soldater till Gallipoli, och den 25 april firas som Anzac Day."),
  ("p","Osmanska riket stred på tyskarnas sida. Efter kriget föll riket, och Mustafa Kemal, som hade lett osmanska trupper vid Gallipoli, grundade senare det moderna Turkiet."),
  ("p","Kolonierna hoppades ofta att insatserna skulle belönas med mer självstyre. Det hände sällan. Det gav bränsle åt självständighetsrörelser."),
  ("ruta","historia","Vems minne?","Minnet av kriget är starkt på västfronten men svagare för dem som kom från kolonierna. Historiker diskuterar vems berättelser som tas med i minnesdagar och museer."),
  ("kolla",["Nämn ett område utanför Europa där kriget fördes.","Vad firar Australien och Nya Zeeland den 25 april?","Varför blev kolonialsoldaternas insatser ofta bortglömda?"]),
 ],
 svar=["T.ex. Gallipoli, Afrika, Mellanöstern.","Anzac Day, minnet av landstigningen vid Gallipoli 1915.","De hamnade utanför den dominerande berättelsen och belönades sällan."],
))

F.append(dict(id="f3", nr="F3", ikon="🎄", titel="Julfreden – källor, minne och myt",
 intro="Berättelsen om julfreden 1914 är en av krigets mest kända. Men hur säker kan vi vara på vad som hände?",
 block=[
  ("p","Det finns brev från soldater, dagböcker och senare minnen. Källorna visar att soldater på flera avsnitt av fronten slutade skjuta och i vissa fall möttes. Men det hände inte överallt, och berättelser om fotbollsmatcher är mer osäkra."),
  ("tab",["Källtyp","Fördel","Risk"],[
    ["Brev hem","Skrivna direkt efter händelsen","Soldaten kan ha velat lugna familjen"],
    ["Dagböcker","Personliga","Kan ha skrivits om i efterhand"],
    ["Minnen i efterhand","Ger helhet","Minnen förändras, berättelser blir mer dramatiska"],
    ["Tidningar","Spred berättelsen","Kunde censureras eller överdriva"]]),
  ("ruta","tank","Källkritik","Fråga: Vem skrev? När? Varför? Är det en primärkälla (nära händelsen) eller en sekundärkälla (skriven senare)? Fotbollsmatchen är ett exempel där olika källor säger olika."),
  ("p","Julfreden används idag som symbol för medmänsklighet. Det är ett exempel på historiebruk: berättelsen väljs ut för att den berör, och används i reklam, filmer och fredsbudskap."),
  ("kolla",["Vad skiljer primär- och sekundärkälla?","Varför är minnen i efterhand en riskfylld källa?","Hur används julfreden som historiebruk idag?"]),
 ],
 svar=["Primärkällor är nära händelsen, sekundärkällor skrivs senare.","Minnen förändras med tiden och berättelser kan bli mer dramatiska.","Som symbol för medmänsklighet och fred, i reklam, film och minnesdagar."],
))

F.append(dict(id="f4", nr="F4", ikon="🌺", titel="Historiebruk: vallmon och minnesdagarna",
 intro="Hur och varför minns vi kriget? Minnesdagar, symboler och museer är historiebruk.",
 block=[
  ("p","Den röda vallmon blev en symbol efter kriget. Soldater såg vallmor blomma på de sönderskjutna fälten, och John McCrae skrev dikten <em>In Flanders Fields</em> 1915. Den första brittiska vallmodagen hölls 1921, då pengar samlades till krigsveteraner. År 2014 skapades installationen <em>Blood Swept Lands and Seas of Red</em> vid Tower of London med 888 246 keramikvallmor, en för varje brittisk eller samväldessoldat som dog."),
  ("tab",["Symbol/dag","Vem använder den?","Möjligt budskap"],[
    ["Röd vallmo","Brittiska veteranorganisationer, regeringar","Hedra de stupade"],
    ["Vit vallmo","Fredsrörelser (sedan 1930-talet)","Kräva fred, inte krig"],
    ["11 november","Många stater","Minnas krigets slut och offer"],
    ["Anzac Day, 25 april","Australien och Nya Zeeland","Nationell identitet och minne"]]),
  ("p","Vissa menar att vallmon ibland kopplas till dagens krig och politik, och därför väljer en del bort den. Det visar att samma symbol kan betyda olika saker för olika människor."),
  ("ruta","fakta","Så granskar du historiebruk","1. Vem använder symbolen? 2. Vad vill de uppnå? 3. Vad lämnas ute? 4. Hur skiljer sig tolkningar?"),
  ("kolla",["Varifrån kommer vallmon som symbol?","Vad står vit vallmo för?","Varför kan en symbol tolkas olika?"]),
 ],
 svar=["Från vallmor som blommade på slagfälten och dikten In Flanders Fields.","Fred.","Olika människor kopplar den till olika värden och händelser."],
))

UPPG = [
 ("Para ihop","Koppla ihop begrepp och förklaring.",["Allians","Ingenmansland","Ultimatum","Hemmafront","Neutral","Vapenstillestånd"],["Hårda krav med tidsgräns","Överenskommelse att sluta strida","Området mellan skyttegravar","Avtal om att hjälpa varandra","Att inte ta parti i ett krig","Samhället hemma under kriget"],"1 – D, 2 – C, 3 – A, 4 – F, 5 – E, 6 – B"),
 ("MAIN","Förklara vad bokstäverna i MAIN står för och ge ett exempel på varje.",[],None,"Militarism (upprustning), allianser (trippelententen), imperialism (kolonier), nationalism (Balkan)."),
 ("Tidslinje","Sätt i rätt ordning.",["Skotten i Sarajevo","USA går med i kriget","Versaillesfreden","Vapenstilleståndet","Slaget vid Somme"],None,"1914 Sarajevo; 1916 Somme; 1917 USA; 1918 vapenstillestånd; 1919 Versailles."),
 ("Orsak och konsekvens","Förklara hur mordet i Sarajevo ledde till världskrig. Använd begreppen ultimatum, allians och mobilisera.",[],None,"Österrike-Ungern gav ultimatum till Serbien, Ryssland mobiliserade, allianserna drog in Tyskland, Frankrike och Storbritannien. A-nivå: förklarar att långsiktiga orsaker låg bakom."),
 ("Teknik","Välj två nya vapen och förklara hur de förändrade krigföringen.",[],None,"T.ex. kulspruta (gynnade försvar), stridsvagn (försökte bryta igenom), gas (skräck, gasmasker), flygplan (spaning), ubåt (sänkte fartyg)."),
 ("Hemmafront","Beskriv hur kriget förändrade livet för en kvinna, och ge en kontinuitet.",[],None,"Förändring: nya arbeten, rösträtt i vissa länder. Kontinuitet: lägre lön, förväntad tillbaka till hemmet."),
 ("Källa","Läs den konstruerade källan i 9.5. Vad kan man lära sig, och vilka begränsningar finns?",[],None,"Visar upplevelse av kriget från sjukvården och avståndet till hemmafronten. Begränsning: en person, konstruerad."),
 ("Versailles","Förklara varför Versaillesfreden kallas 'hård' och vilka följder den kunde få.",[],None,"Skuld, skadestånd, förlorad mark. Följd: bitterhet, instabilitet. A-nivå: skilj mellan orsak och senare utveckling."),
 ("Sverige","Förklara hur ett neutralt Sverige ändå påverkades av kriget.",[],None,"Blockader, ransonering, gulaschbaroner, hungerkravaller, rösträtts- och demokratireformer."),
 ("Historiebruk","Välj en minnesdag eller symbol (11 november, vallmo). Vem använder den och varför?",[],None,"Bedöms: aktör, syfte, olika tolkningar."),
]

BEGREPP = [
 ("Militarism","Att bygga upp stor militär styrka."),
 ("Allians","Avtal mellan stater om att hjälpa varandra."),
 ("Imperialism","Att en stat lägger under sig andra områden."),
 ("Nationalism","Idén att nationen ska ha en egen stat."),
 ("Ultimatum","Hårda krav med tidsgräns."),
 ("Mobilisera","Att kalla in soldater och göra armén krigsklar."),
 ("Ställningskrig","Krig där fronterna knappt flyttas."),
 ("Ingenmansland","Området mellan fiendernas skyttegravar."),
 ("Västfront / östfront","De viktigaste krigsskådeplatserna."),
 ("Hemmafront","Samhället hemma under krig."),
 ("Ransonering","Att fördela varor med kuponger."),
 ("Propaganda","Budskap för att påverka människors åsikter."),
 ("Vapenstillestånd","Överenskommelse om att sluta strida."),
 ("Skadestånd","Pengar som den förlorande sidan måste betala."),
 ("Neutralitet","Att inte ta parti i ett krig."),
 ("Historiebruk","Hur historia används i nutiden."),
]

SAMMAN = [
 "Orsakerna till kriget var militarism, allianser, imperialism och nationalism (MAIN). Skotten i Sarajevo 1914 var den utlösande orsaken.",
 "Allianserna gjorde att en lokal konflikt blev ett storkrig. Schlieffenplanen och angreppet på Belgien drog in Storbritannien.",
 "Västfronten blev ett ställningskrig i skyttegravar. Slagen vid Verdun och Somme kostade enorma förluster för små framryckningar.",
 "Ny teknik – kulspruta, gas, stridsvagn, flygplan och ubåt – förändrade kriget.",
 "På hemmafronten ransonerades mat, och kvinnor tog nya arbeten. Det ledde till förändringar men också kontinuitet.",
 "USA gick med 1917, och Ryssland lämnade efter revolutionen. Kriget slutade 11 november 1918.",
 "Versaillesfreden 1919 var hård mot Tyskland. Nya stater bildades, Nationernas förbund grundades och spanska sjukan följde.",
 "Sverige var neutralt men drabbades av brist och oro, vilket bidrog till rösträtt. Kriget minns vi i dag genom minnesdagar och vallmon.",
]

TEST_A = [
 ("Vad står M i MAIN för?",["Mobilisering","Militarism","Monarki","Marknad"],1),
 ("Vem sköt Franz Ferdinand i Sarajevo 1914?",["Gavrilo Princip","Lenin","Bismarck","Wilhelm II"],0),
 ("Varför gick Storbritannien med i kriget?",["Tyskland gick in i det neutrala Belgien","Tyskland anföll London","Ryssland hotade Indien","Frankrike bad om pengar"],0),
 ("Vad kallas området mellan fiendernas skyttegravar?",["Ingenmansland","Västfronten","Hemmafronten","Gränszonen"],0),
 ("Vilket vapen användes första gången på Somme 1916?",["Kulsprutan","Stridsvagnen","Atombomben","Flygplanet"],1),
 ("Vad gjorde USA 1917 med kriget?",["Gick med på de allierades sida","Gick med på Tysklands sida","Förblev neutralt","Anföll Mexiko"],0),
 ("När upphörde striderna på västfronten?",["11 november 1918","28 juni 1919","1 augusti 1914","6 april 1917"],0),
 ("Vad hände i Sverige våren 1917?",["Hungerkravaller","Krigsförklaring","Revolution som lyckades","Ny kung"],0),
]

TEST_B = [
 ("Ge två orsaker till första världskriget.","T.ex. militarism, allianser, imperialism, nationalism."),
 ("Förklara varför kriget på västfronten fastnade i skyttegravar.","Kulsprutor, artilleri och taggtråd gjorde anfall dyra, så båda sidor grävde ner sig."),
 ("Ge ett exempel på hur kvinnors liv förändrades under kriget.","De fick nya arbeten i fabriker och sjukvård; i vissa länder rösträtt."),
 ("Förklara två följder av Versaillesfreden.","T.ex. Tysklands skuld, skadestånd, förlorat land, nya stater, Nationernas förbund, bitterhet."),
 ("Förklara hur ett neutralt Sverige påverkades.","Blockad, matbrist, ransonering, hungerkravaller och demokratireformer."),
 ("Ge ett exempel på historiebruk kopplat till kriget.","T.ex. vallmon, 11 november, Anzac Day, julfreden som symbol."),
]

KALLA = dict(
 text="Vi ligger i leran. Det regnar varje dag. Löss och råttor är våra grannar. Förra veckan anföll vi, och i dag är halva kompaniet borta. Jag tänker på hemmet och försöker skriva att allt är bra, så att mamma inte ska oroa sig.",
 ursprung="Konstruerad källa baserad på soldaters brev från västfronten. Skriven som ett brev hem 1916.",
 fragor=[("Vilken sorts källa är detta, och är den primär- eller sekundärkälla?","Ett brev, alltså en primärkälla till sin typ (här konstruerad). Den är skriven nära händelsen."),
         ("Vad berättar brevet om livet i skyttegraven?","Lera, regn, löss och råttor, stora förluster."),
         ("Varför kan brevet vara mindre sanningsenligt än det verkar?","Skribenten vill lugna familjen och kan ha skrivit mindre än vad som hände, och armén kunde läsa breven (censur)."),
         ("Vad skulle du vilja kontrollera med andra källor?","Hur vanliga förlusterna var, och om andra soldater upplevde samma sak, t.ex. dagböcker och arméns rapporter.")],
)

SKRIV = dict(
 uppgift="Skriv en text på 300–400 ord: <strong>Hur och varför ledde mordet i Sarajevo till ett världskrig, och vilka följder fick kriget?</strong> Ta med de långsiktiga orsakerna (MAIN) och den utlösande orsaken, minst en följd för Europa, minst en följd för Sverige, och ett exempel på hur kriget minns idag (historiebruk).",
 stod=["E: Du beskriver vad som hände i Sarajevo och nämner några orsaker och följder. Du använder några begrepp (allians, skyttegrav, Versailles).",
       "C: Du förklarar hur långsiktiga orsaker och utlösande orsak hänger ihop. Du förklarar flera följder, även för Sverige, och ger ett exempel på historiebruk med viss förklaring.",
       "A: Du värderar orsakernas betydelse, visar att historiker är oense om skuld, drar slutsatser om samband mellan kriget och senare händelser och analyserar hur minnet av kriget används och av vem."],
)

LAB = dict(
 titel="Historikerns verkstad: Julafton 1914 – källor och minnesmärke",
 syfte="Eleverna övar källkritik (primär och sekundär), jämför olika källor om samma händelse och funderar över hur historia minns och används.",
 material="Tre konstruerade källor om julfreden (soldatbrev, dagboksanteckning, tidningsartikel, skrivna av läraren), källkritiska frågor, papper och penna.",
 utforande=["Dela klassen i grupper om fyra. Varje grupp får tre korta källor om julfreden 1914.",
            "Läs källorna individuellt och skriv ned: Vem skrev? När? Varför? Vad berättar den, och vad kan den inte berätta?",
            "Jämför era anteckningar i gruppen. Var är källorna överens? Var skiljer de sig?",
            "Skriv tillsammans tre meningar som sammanfattar vad ni med säkerhet kan säga om julfreden.",
            "Diskutera: Hur används julfreden idag (film, reklam, fredsbudskap)? Vem tjänar på den berättelsen?",
            "Presentera kort för klassen."],
 fragor=[("Vilken källa är mest trovärdig för att veta vad som hände, och varför?","Den som är närmast händelsen och minst intresserad, t.ex. ett brev eller en dagbok, men alla har begränsningar."),
         ("Varför skiljer sig källorna åt?","Olika författare, syften, tidpunkter och perspektiv."),
         ("Varför är julfreden en populär berättelse idag?","Den berör, visar medmänsklighet och passar i fredsbudskap, men kan förenkla.")],
 bonus="För läraren: Betona skillnaden mellan det källorna säger och berättelsen som senare byggts upp. Bedöm källkritik (E: kan säga vem som skrev och vad texten berättar; C: kan jämföra källor och peka på bristerna; A: kan värdera källornas trovärdighet och dra slutsatser om hur berättelsen används). Variant: arbeta med den svenska hemmafronten 1917 med lokala källor (t.ex. Malmö stads sida om livsmedelsbristen).",
)

LARAR = [
 ("Koppling till Lgr22","Kapitlet täcker syftet (kunskaper om händelser, aktörer och förändringsprocesser, begrepp, källkritik, historiebruk). Centralt innehåll: imperialism och världskrig ca 1850–1950, orsaker och följder, nationalism, krigföring och civila, samt demokratisering. Kunskapskraven rör orsak och konsekvens, kontinuitet och förändring, källor och historiebruk."),
 ("Förslag på upplägg (8 lektioner)","1. Orsakerna (MAIN) och julikrisen (9.1–9.2). 2. Västfront och östfront (9.3). 3. Teknik och kriget till sjöss (9.4). 4. Hemmafronten och kvinnor (9.5). 5. 1917, USA och Ryssland (9.6). 6. Krigsslut, Versailles och följder (9.7). 7. Sverige och hungerkravallerna (9.8). 8. Historiebruk (vallmo, minnesdagar), test och skrivuppgift. Kombinera med den interaktiva kartsimuleringen om första världskriget."),
 ("Vanliga missuppfattningar","Att mordet i Sarajevo ensamt orsakade kriget. Att Tyskland var det enda landet som ville ha krig. Att Sverige inte påverkades alls. Att soldaterna alltid var i skyttegraven. Att USA vann kriget ensamt. Att Versaillesfreden orsakade nästa krig i sig, utan andra faktorer."),
 ("Bedömningsstöd E/C/A","E: eleven beskriver orsaker, händelser och följder med enkla exempel och några begrepp. C: eleven förklarar samband mellan långsiktiga orsaker och utlösande orsak, jämför olika perspektiv, gör en enkel källanalys. A: eleven värderar orsakernas betydelse, visar att tolkningar skiljer sig, analyserar källor och historiebruk, drar slutsatser om kontinuitet och förändring."),
 ("Tips för Blooket och Jeopardy (10 kategorier)","1. Orsaker (MAIN). 2. Sarajevo och julikrisen. 3. Västfronten. 4. Östfronten och andra fronter. 5. Ny teknik. 6. Hemmafronten och kvinnor. 7. USA och Ryssland 1917. 8. Versailles och följder. 9. Sverige under kriget. 10. Historiebruk (vallmo, 11 november). Exempel: ”Vilken symbol bärs i november?” (vallmo)."),
]

KALLOR = [
 ("Skolverket – Kommentarmaterial till kursplanen i historia, grundskolan (2022)","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
 ("World History Encyclopedia – The Pre-WWI Alliance System","https://www.worldhistory.org/article/2808"),
 ("National Army Museum – 1919 (Versailles, Nationernas förbund m.m.)","https://ww1.nam.ac.uk/theme/year-1919/"),
 ("Imperial War Museums – The history of the poppy","https://shop.iwm.org.uk/blogs/news/the-history-of-the-poppy-and-imperial-war-museums-enduring-connection"),
 ("SCB – Spanska sjukan och döden för 100 år sedan","https://www.scb.se/hitta-statistik/redaktionellt/spanska-sjukan-och-doden-for-100-ar-sedan/"),
 ("Malmö stad – Livsmedelsbrist och ransonering 1917","https://malmo.se/Uppleva-och-gora/Arkitektur-och-kulturarv/Malmos-historia/Handelser-och-fenomen/Livsmedelsbrist-och-ransonering-1917.html"),
 ("Sveriges riksdag – Demokratins utveckling i Sverige","https://www.riksdagen.se/sv/sa-fungerar-riksdagen/riksdagens-historia/demokratins-utveckling-i-sverige/"),
 ("Store norske leksikon – Hjalmar Branting","https://snl.no/Hjalmar_Branting"),
]

F_UPPG = [
 ("●","Förklara varför Tyskland fick skulden i Versaillesfreden.",[],None,"De allierade ansåg Tyskland ansvarigt, bl.a. för angreppet på Belgien och skadorna."),
 ("●●","Jämför två tolkningar av vem som bar skulden för kriget.",[],None,"Tyskland ansvarigt; alla delade ansvar; misstag. Eleven jämför argument."),
 ("●●","Förklara varför soldater och arbetare från kolonierna ofta glömdes bort i minnet av kriget.",[],None,"Berättelsen fokuserar på västfronten, kolonierna hade lite makt över historieskrivningen och belönades sällan."),
 ("●●●","Analysera hur julfreden används i dag. Vem berättar och varför? Vad utelämnas?",[],None,"Bedöms: aktör, syfte, urval, källkritik."),
 ("●●●","Diskutera: Vilken symbol för kriget (röd vallmo, vit vallmo, 11 november) tycker du bäst kan förena människor? Motivera.",[],None,"Fritt resonemang med argument och olika perspektiv."),
]

F_SAMMAN = [
 "Historiker är oense om vem som bar skulden för kriget.",
 "Kriget var ett världskrig med insatser från kolonier och länder utanför Europa.",
 "Julfreden är ett exempel på hur källor, minne och myter samverkar.",
 "Vallmon och minnesdagar är historiebruk som kan ha olika betydelser.",
]

F_BEGR = [
 ("Skuldfrågan","Diskussionen om vem som var ansvarig för kriget."),
 ("Krigsskuldsparagrafen","Paragraf i Versaillesfreden om Tysklands ansvar."),
 ("Anzac","Australiska och nyzeeländska soldater."),
 ("Primärkälla","Källa nära händelsen."),
 ("Sekundärkälla","Källa som skrivits senare."),
]

BLOOKET = [
 ("Vad står M i MAIN för?","Militarism","Mobilisering","Monarki","Marknad"),
 ("Vad står A i MAIN för?","Allianser","Armé","Anfall","Atombomber"),
 ("Vad står I i MAIN för?","Imperialism","Industri","Invasion","Islam"),
 ("Vad står N i MAIN för?","Nationalism","Neutralitet","Natur","Naturalism"),
 ("Var mördades Franz Ferdinand?","Sarajevo","Berlin","Paris","Wien"),
 ("Vilket år bröt kriget ut?","1914","1912","1917","1939"),
 ("Vem sköt Franz Ferdinand?","Gavrilo Princip","Lenin","Hitler","Kaiser Wilhelm"),
 ("Vad är ett ultimatum?","Hårda krav med tidsgräns","Ett fredsavtal","En allians","En vapenvila"),
 ("Vilket land gick Tyskland genom för att anfalla Frankrike?","Belgien","Schweiz","Sverige","Spanien"),
 ("Vilka ingick i trippelententen?","Storbritannien, Frankrike och Ryssland","Tyskland, Italien och Japan","USA, Kanada och Mexiko","Sverige, Norge och Danmark"),
 ("Vad kallas området mellan fiendernas skyttegravar?","Ingenmansland","Hemmafronten","Gränszon","Brohuvud"),
 ("Vilket slag 1916 kostade ungefär 700 000 soldater?","Verdun","Marne","Tannenberg","Gallipoli"),
 ("Vilket slag 1916 förlorade britterna ca 57 000 första dagen?","Somme","Verdun","Ypres","Marne"),
 ("Vilket vapen användes första gången på Somme?","Stridsvagnen","Kulsprutan","Giftgasen","Ubåten"),
 ("Var användes giftgas i stor skala 1915?","Ypres","Rom","Moskva","Oslo"),
 ("Vilket fartyg sänktes 1915 av en tysk ubåt?","Lusitania","Titanic","Bismarck","Gotland"),
 ("Vad kallades vintern 1916–17 i Tyskland?","Kålrotsvintern","Fredsvintern","Segervintern","Istiden"),
 ("Vilket år gick USA med i kriget?","1917","1914","1915","1919"),
 ("Vem ledde bolsjevikerna 1917?","Lenin","Stalin","Tsar Nikolaj","Wilson"),
 ("När upphörde striderna?","11 november 1918, kl. 11","28 juni 1919","1 januari 1918","6 april 1917"),
 ("Var skrevs fredsavtalet med Tyskland under 1919?","Versailles","Berlin","Compiègne","London"),
 ("Vad grundades för att förhindra nya krig?","Nationernas förbund","FN","Nato","EU"),
 ("Hur många svenskar dog ungefär i spanska sjukan 1918–19 enligt SCB?","Omkring 34 000","Omkring 340","Omkring 3 400 000","Omkring 3 400"),
 ("Vad var Sverige under kriget?","Neutralt","Allierat med Tyskland","Allierat med Frankrike","I krig med Norge"),
 ("Vad hände i Malmö den 25 april 1917?","Stor demonstration mot matbrist","Krigsförklaring","Kungabesök","Folkomröstning"),
 ("Vem blev finansminister 1917 och fick Nobels fredspris 1921?","Hjalmar Branting","Nils Edén","Per Albin Hansson","Gustaf V"),
 ("Vilket år hölls första valet med allmän och lika rösträtt i Sverige?","1921","1918","1909","1945"),
 ("Vilken blomma symboliserar minnet av de stupade?","Vallmo","Ros","Tulpan","Maskros"),
]

JEOPARDY = {
 "Orsaker": [
  (100,"Förkortningen för militarism, allianser, imperialism, nationalism","Vad är MAIN?"),
  (200,"Avtal om att hjälpa varandra","Vad är en allians?"),
  (300,"Blocket med Storbritannien, Frankrike och Ryssland","Vad är trippelententen?"),
  (400,"Den utlösande orsaken i Sarajevo 1914","Vad är mordet på Franz Ferdinand?"),
  (500,"Tysklands plan att gå genom Belgien","Vad är Schlieffenplanen?")],
 "Fronterna": [
  (100,"Området mellan skyttegravarna","Vad är ingenmansland?"),
  (200,"Slaget 1916 med omkring 700 000 förluster","Vad är Verdun?"),
  (300,"Slaget där stridsvagnar användes första gången","Vad är Somme?"),
  (400,"Tysk seger mot Ryssland 1914","Vad är Tannenberg?"),
  (500,"Halvön där de allierade gav upp efter åtta månader","Vad är Gallipoli?")],
 "Teknik": [
  (100,"Vapen som kunde skjuta hundratals skott i minuten","Vad är kulsprutan?"),
  (200,"Skyddsutrustning mot gas","Vad är gasmask?"),
  (300,"Britternas nya vapen 1916","Vad är stridsvagnen?"),
  (400,"Fartyget Lusitania sänktes av denna","Vad är en ubåt?"),
  (500,"Staden där klorgas användes 1915","Vad är Ypres?")],
 "Slutet": [
  (100,"Datumet då striderna upphörde 1918","Vad är 11 november?"),
  (200,"Slottet där freden skrevs under","Vad är Versailles?"),
  (300,"Organisation som skulle förhindra nya krig","Vad är Nationernas förbund?"),
  (400,"Fyra imperier som försvann","Vad är det tyska, österrikisk-ungerska, ryska och osmanska?"),
  (500,"Influensa som följde kort efter kriget","Vad är spanska sjukan?")],
 "Sverige och minnet": [
  (100,"Sveriges hållning under kriget","Vad är neutralitet?"),
  (200,"År då hungerkravallerna bröt ut","Vad är 1917?"),
  (300,"Socialdemokratisk ledare, finansminister 1917","Vem är Hjalmar Branting?"),
  (400,"Första valet med allmän och lika rösträtt","Vad är 1921?"),
  (500,"Blomma som symbol för minnet av krigets offer","Vad är vallmon?")],
}

GRUPPER = [
 ("orsaker","Orsaker och krigsutbrott","Varför kriget bröt ut och hur det spreds.",["orsaker","sarajevo","fronterna"]),
 ("krigfore","Krigföring, hemmafront och vändpunkt","Teknik, hemmafronten och året 1917.",["teknik","hemma","ar1917"]),
 ("fred","Fred, följder och Sverige","Krigsslutet, Versailles, Sverige och minnet.",["slutet","sverige"]),
]

SCEN = None
