# -*- coding: utf-8 -*-
# Kapitel 7 – Industrialiseringen (åk 8)
T = dict(
 nr=7, namn="Industrialiseringen", under="När maskinerna, fabrikerna och städerna förändrade världen",
 fil="historia-07-industrialiseringen", arskurs=8, nodeid="historia-industrialiseringen",
 mal=["beskriva hur människor levde och arbetade i jordbrukssamhället före industrialiseringen",
      "förklara varför industrialiseringen började i Storbritannien",
      "berätta om ångmaskinen, textilindustrin och järnvägen och vad de betydde",
      "jämföra arbetsvillkor och levnadsvillkor för olika grupper under industrialiseringen",
      "förklara hur arbetarrörelsen och fackföreningarna växte fram och varför",
      "beskriva hur Sverige industrialiserades och varför många svenskar emigrerade",
      "resonera om vad som förändrades och vad som var sig likt, och om miljöeffekter då och nu",
      "förklara hur industrialiseringen används i dagens debatt om klimatet"],
 fundera="Tänk dig att du lever år 1780 och bor på en gård eller i ett torp. Hur ser din dag ut, och vad kommer du att äta, göra och bära? Skriv tre meningar. Jämför sedan med din egen dag i går när du har läst klart kapitlet.",
)

S = []

S.append(dict(id="fore", nr="7.1", ikon="🌾", titel="Livet före industrialiseringen",
 intro="Under tusentals år levde de allra flesta människor på landet och arbetade med jorden. Det kallas ett <strong>jordbrukssamhälle</strong>. Det är ur det samhället som industrisamhället växer fram.",
 block=[
  ("p","I ett jordbrukssamhälle gör familjen det mesta själv. Man odlar maten, spinner garn, väver tyg och bygger redskap. Arbetet följer årstiderna: så på våren, skörda på hösten, överleva vintern. Det mesta arbetet görs med människors och djurs muskelkraft, och med vind och vatten i kvarnar."),
  ("p","Samhället var också mycket ojämlikt. En liten grupp ägde mycket av marken, medan många var torpare, drängar och pigor som arbetade åt andra. Missväxt kunde betyda hunger för alla."),
  ("ruta","tank","Vad betyder ”industri”?","Ordet <strong>industri</strong> betyder produktion av varor i stor skala, ofta med maskiner och i fabriker. <strong>Industrialisering</strong> är den process då ett samhälle går från att leva mest på jordbruk till att leva mest på industri och tjänster."),
  ("p","Före industrialiseringen skedde också en förändring på landsbygden, som kallas <strong>jordbruksrevolutionen</strong>. Nya metoder gjorde att bönderna kunde odla mer på samma mark. Man lät inte längre åkern vila varje år utan växlade mellan olika grödor. Potatisen kom att bli en viktig, billig mat. I England stängdes gemensam mark in av jordägare (<em>inhägnader</em>), och i Sverige slogs spridda jordlotter ihop i så kallade skiftesreformer."),
  ("p","Resultatet blev att fler människor kunde matas av färre bönder. Befolkningen växte i Europa under 1700- och 1800-talen. Men många fick ingen egen jord att leva på. De flyttade till städer eller fabriker och blev en viktig arbetskraft."),
  ("ruta","fakta","Orsak och konsekvens","Jordbruksrevolutionen är en <strong>orsak</strong> till industrialiseringen på två sätt: den gav mat till fler människor, och den gjorde att många lämnade jordbruket och sökte arbete någon annanstans. Historiker kallar det ibland för att ”arbetskraft frigjordes”."),
  ("tidslinje",[("Före 1700","Jordbrukssamhälle: de flesta lever på landsbygden"),("1700-talet","Nya odlingsmetoder, potatisen sprids, befolkningen växer"),("Ca 1760","Industrialiseringen börjar i Storbritannien"),("1800-talet","Industrialiseringen sprider sig till Europa och USA")]),
  ("kolla",["Vad är ett jordbrukssamhälle?","Nämn två förändringar som ingick i jordbruksrevolutionen.","Varför är jordbruksrevolutionen en orsak till industrialiseringen?"]),
 ],
 svar=["Ett samhälle där de flesta lever på att odla jorden och arbetar på landsbygden.","T.ex. nya växtföljder, potatisodling, inhägnader (England) och skiftesreformer (Sverige).","Fler fick mat och befolkningen växte, och många saknade jord och sökte arbete i städer och fabriker."],
))

S.append(dict(id="britannien", nr="7.2", ikon="🇬🇧", titel="Varför började det i Storbritannien?",
 intro="Industrialiseringen började i Storbritannien omkring 1760. Historiker är inte helt överens om exakt varför just där. De pekar på flera orsaker som samverkade.",
 block=[
  ("p","Det som brukar nämnas först är <strong>kol</strong>. Storbritannien hade mycket kol, ofta nära kusten eller floder så att det gick att transportera. Skogen hade blivit sällsynt, så kolet ersatte ved som bränsle. Även <strong>järnmalm</strong> fanns i landet."),
  ("p","Det fanns också <strong>kapital</strong>, alltså pengar att investera. Rika köpmän och bankirer ville satsa på nya företag. Landet hade dessutom en tämligen stabil politik, och uppfinnare kunde skydda sina idéer med patent."),
  ("p","Den tredje viktiga orsaken är <strong>kolonierna och handeln</strong>. Storbritannien hade ett stort rike med kolonier i bland annat Nordamerika, Karibien och Indien. Därifrån kom råvaror som bomull och socker, och där fanns också köpare till brittiska varor. Mycket av den bomull som användes kom från plantager där slavar tvingades arbeta, och det är en mörk sida av historien."),
  ("tab",["Faktor","Hur den hjälpte industrialiseringen"],[
    ["Kol och järn","Billig energi och material till maskiner, järnvägar och fartyg"],
    ["Kapital och patent","Pengar att satsa och skydd för uppfinnare"],
    ["Kolonier och handel","Råvaror och marknader för färdiga varor"],
    ["Jordbruksrevolutionen","Mat till fler människor, arbetskraft till fabriker"],
    ["Stabil politik","Trygghet för företagare att ta risker"]]),
  ("ruta","historia","Historikerna är oense","Vissa forskare menar att kolet var avgörande. Andra lyfter fram att arbetskraft var dyr i Storbritannien, vilket gjorde det lönsamt att uppfinna maskiner som sparade arbete. Det är ett bra exempel på att historiska förklaringar sällan bara har en orsak. Mer om detta i fördjupningen."),
  ("kolla",["Nämn tre orsaker till att industrialiseringen började i Storbritannien.","Varför ersatte kolet ved som bränsle?","Vilken roll spelade kolonierna?"]),
 ],
 svar=["T.ex. kol och järn, kapital, kolonier och handel, jordbruksrevolutionen.","Skogen hade blivit sällsynt och kol fanns det gott om och det var lätt att transportera.","De gav råvaror som bomull och marknader där brittiska varor kunde säljas."],
))

S.append(dict(id="maskiner", nr="7.3", ikon="⚙️", titel="Ångmaskin, textil och järnväg",
 intro="Tre uppfinningar och branscher hänger ihop och blev symboler för industrialiseringen: ångmaskinen, textilindustrin och järnvägen.",
 block=[
  ("p","<strong>Ångmaskinen</strong> bränner kol för att koka vatten. Ångan driver en kolv, och kolven får hjul och maskiner att röra sig. Redan 1712 byggde Thomas Newcomen en ångmaskin för att pumpa vatten ur gruvor. James Watt förbättrade den, och 1769 fick han patent på sin version. Hans maskin kunde driva en axel och därmed olika maskiner."),
  ("p","Det som gjorde ångmaskinen så viktig var att den inte var beroende av vind eller vattenfall. Fabriker kunde ligga var som helst, till exempel mitt i en stad."),
  ("p","<strong>Textilindustrin</strong> blev först ut. Tidigare spann och vävde man för hand i hemmen. Nu kom maskiner som spinnmaskinen och den mekaniska vävstolen, och garn och tyg kunde tillverkas mycket snabbare och billigare. Därför flyttade arbetet från hemmen till stora fabriker. Bomullstyg blev en av Storbritanniens viktigaste exportvaror."),
  ("p","<strong>Järnvägen</strong> kom när ångmaskinen sattes på hjul. Banan mellan Stockton och Darlington öppnades 1825, och Liverpool–Manchester följde 1830. Tåg kunde frakta tung last och många människor snabbt. Tåget gjorde att varor, människor och nyheter rörde sig på ett helt nytt sätt."),
  ("ruta","visste","Visste du?","Lokomotivet Rocket, konstruerat av Robert Stephenson i familjeföretaget Stephenson & Co, vann en tävling i Rainhill 1829 inför öppnandet av Liverpool–Manchester-banan. Vid de berömda provkörningarna i Rainhill 1829 nådde det som mest omkring 48 km/h när det inte drog några vagnar, vilket var otroligt snabbt på den tiden."),
  ("bild","industri","Fabriker med skorstenar blev ett nytt inslag i landskapet."),
  ("tidslinje",[("1712","Newcomen bygger en ångmaskin för gruvor"),("1769","Watt får patent på sin förbättrade ångmaskin"),("1825","Stockton–Darlington, tidig järnväg"),("1830","Liverpool–Manchester öppnas"),("1856","Första järnvägen för allmän trafik i Sverige")]),
  ("kolla",["Hur fungerar en ångmaskin i korta drag?","Varför flyttade textilarbetet från hemmen till fabriker?","Vad betydde järnvägen?"]),
 ],
 svar=["Kol bränns för att koka vatten, ångan trycker en kolv som sätter maskiner i rörelse.","Maskinerna var stora och dyra och drevs av en gemensam kraftkälla, så de samlades i fabriker.","Varor och människor kunde transporteras snabbt och billigt, och marknader och orter knöts ihop."],
))

S.append(dict(id="fabriken", nr="7.4", ikon="🏭", titel="Fabriken och arbetsvillkoren",
 intro="Fabriken förändrade arbetet. Nu styrdes dagen av klockan och maskinen, inte av årstiderna och solen. Ägarna tjänade pengar, men för många arbetare var villkoren hårda.",
 block=[
  ("p","Arbetsdagen var lång, ofta tolv timmar eller mer, sex dagar i veckan. Fabriken kunde vara varm, dammig och bullrig, och maskinerna saknade skydd. Olyckor var vanliga. Den som kom för sent kunde få böter eller sparken."),
  ("p","<strong>Barnarbete</strong> var också vanligt. Barn var billiga att anställa och små nog att krypa under maskiner eller in i trånga gruvgångar. Men barnarbete var inget nytt. Barn hade alltid hjälpt till på gården. Det som var nytt var arbetstiderna och farorna i fabriken."),
  ("kalla","Beskrivning av barnarbete (konstruerad källa)","Jag var nio år när jag började i spinneriet. Vi gick upp före gryningen och stod på fötter hela dagen. Om jag somnade fick jag stryk av förmannen. På kvällen orkade jag knappt äta.","Konstruerad källa baserad på vittnesmål från brittiska fabriksbarn under första hälften av 1800-talet."),
  ("p","Så småningom kom lagar för att skydda barnen. I Storbritannien förbjöd en fabrikslag 1833 att barn under nio år arbetade i textilfabriker. Barn mellan nio och tretton fick arbeta högst nio timmar per dag och skulle få två timmars skolgång varje dag. Lagen skapade också fyra inspektörer som skulle kontrollera att reglerna följdes. Reglerna gällde dock bara textilfabriker, och de följdes inte alltid."),
  ("p","I Sverige fanns också barnarbete, bland annat på gårdar, i fabriker och vid sågverken. Först 1881 kom en svensk förordning som förbjöd barn under tolv år att arbeta i fabriker, och barn under fjorton fick bara arbeta sex timmar per dag. Det tog lång tid innan reglerna följdes och innan skolgången helt ersatte barnens arbete."),
  ("ruta","tank","Varför ändrades lagarna?","Fundera: Vilka grupper kan ha drivit på för lagarna? Läkare, reformvänner, arbetare, politiker? Vad tror du att fabriksägarna tyckte? Lagar kommer sällan av sig själva. Någon måste kräva dem."),
  ("kolla",["Nämn tre saker som gjorde fabriksarbetet hårt.","Vad kunde vara nytt med barnarbetet i fabriken jämfört med på gården?","Vad stadgade den brittiska fabrikslagen 1833?"]),
 ],
 svar=["T.ex. långa dagar, farliga maskiner, buller och damm, böter.","Långa arbetsdagar, tvång att följa maskinen och stora risker för olyckor.","Barn under nio år fick inte arbeta i textilfabriker, barn 9–13 år fick arbeta högst nio timmar, de skulle få skolgång och inspektörer skulle kontrollera reglerna."],
))

S.append(dict(id="staden", nr="7.5", ikon="🏙️", titel="Staden och de nya klasserna",
 intro="När fabrikerna växte flyttade människor dit jobben fanns. Städerna blev snabbt större, och samhället delades upp på ett nytt sätt.",
 block=[
  ("p","Att flytta från landsbygden till städerna kallas <strong>urbanisering</strong>. Städer som Manchester växte väldigt snabbt. Husen byggdes i hast, ofta trånga, utan rent vatten och avlopp. Flera familjer kunde dela ett rum. Sjukdomar som kolera och tyfus spreds lätt."),
  ("p","Men städerna erbjöd också möjligheter: lön i pengar, nya yrken och mer frihet från släkten och godsägaren. Många såg staden som en chans, andra som ett hot."),
  ("p","Samhället fick <strong>nya klasser</strong>. En social klass är en grupp med ungefär samma ställning och inkomst. Fabriksägare, bankirer och företagare kallas <strong>borgerskapet</strong>. Fabriksarbetarna blev en ny, stor <strong>arbetarklass</strong>. Mellan dem växte en <strong>medelklass</strong> av tjänstemän, lärare och handlare."),
  ("tab",["Grupp","Hur man levde"],[
    ["Borgerskap","Ägde fabriker och banker, bodde i stora hus, hade ofta tjänstefolk"],
    ["Medelklass","Tjänstemän, lärare, handlare, hade tryggare inkomst och bättre boende"],
    ["Arbetarklass","Fabriksarbetare, låga löner, trångbodda, ofta osäker försörjning"]]),
  ("ruta","fakta","Kvinnor och industrin","Många kvinnor arbetade i textilfabriker, och som tjänstefolk i borgerliga hem. Kvinnor fick ofta lägre lön än män för samma arbete. Rösträtt och rätt till utbildning kom mycket senare."),
  ("p","Historiker diskuterar hur arbetarnas levnadsstandard förändrades. Fick de det bättre eller sämre? På lång sikt blev levnadsstandarden högre, men under de första decennierna var det många som hade det mycket svårt."),
  ("kolla",["Vad är urbanisering?","Vilka tre klasser växte fram?","Nämn en nackdel och en fördel med att flytta till staden."]),
 ],
 svar=["Att människor flyttar från landsbygden till städer.","Borgerskap, medelklass och arbetarklass.","T.ex. trångboddhet och sjukdomar, men också lön i pengar och nya jobb."],
))

S.append(dict(id="rorelsen", nr="7.6", ikon="✊", titel="Arbetarrörelsen",
 intro="Arbetarna var många, men ensamma hade de ingen makt mot fabriksägaren. Genom att gå samman kunde de kräva bättre villkor. Så föddes arbetarrörelsen.",
 block=[
  ("p","En <strong>fackförening</strong> är en organisation där arbetare går ihop för att förhandla om lön och arbetsvillkor. Den starkaste metoden är <strong>strejk</strong>, alltså att man lägger ned arbetet tills kraven är uppfyllda. Arbetsgivarna kunde svara med <strong>lockout</strong>, att man stänger ute arbetarna."),
  ("p","Arbetarna bildade också politiska partier. I Sverige grundades Socialdemokratiska arbetarpartiet 1889. Partiet krävde bland annat allmän rösträtt, kortare arbetsdag och bättre skydd för arbetare. Många arbetare engagerade sig också i bildningsförbund, nykterhetsrörelsen och andra folkrörelser."),
  ("p","Tänkare som Karl Marx och Friedrich Engels skrev Kommunistiska manifestet 1848. De menade att arbetarna borde ta makten över fabrikerna. Det blev en stark idé, men arbetarrörelsen var inte enig. Reformister ville förbättra samhället steg för steg, medan revolutionärer ville välta det."),
  ("p","Landsorganisationen (LO) bildades 1898. År 1909 utbröt storstrejken, som varade från augusti till början av september. Arbetsgivarna ville sänka lönerna när konjunkturen var dålig och stängde ute arbetare (lockout), och då svarade LO med storstrejk. Strejken slutade i nederlag, och LO förlorade många medlemmar. Men rörelsen överlevde, och 1938 slöts Saltsjöbadsavtalet mellan LO och arbetsgivarna, som lade grunden för samarbete på arbetsmarknaden."),
  ("tidslinje",[("1848","Kommunistiska manifestet"),("1879","Sundsvallsstrejken i sågverken"),("1889","Socialdemokratiska partiet bildas"),("1898","LO bildas"),("1909","Storstrejken"),("1938","Saltsjöbadsavtalet")]),
  ("ruta","historia","Orsak och konsekvens","Orsak: dåliga arbetsvillkor och lön, samt ett nytt sätt att tänka om rättvisa. Konsekvens: fackföreningar, partier, nya lagar och med tiden en trygg arbetsmarknad. Arbetarrörelsen är en viktig förklaring till att många länder fick demokrati och välfärd."),
  ("kolla",["Vad är en strejk, och vad är en lockout?","Vilka krävde Socialdemokraterna i början?","Varför är arbetarrörelsen viktig för demokratins framväxt?"]),
 ],
 svar=["Strejk: arbetarna lägger ned arbetet. Lockout: arbetsgivaren stänger ute arbetarna.","T.ex. allmän rösträtt, kortare arbetsdag och bättre skydd för arbetare.","Den krävde rösträtt och rättigheter för vanliga människor och organiserade många i politiken."],
))

S.append(dict(id="sverige", nr="7.7", ikon="🇸🇪", titel="Sverige industrialiseras – och många flyttar till Amerika",
 intro="Sverige industrialiserades sent jämfört med Storbritannien, men sedan gick det snabbt. Samtidigt lämnade många svenskar landet.",
 block=[
  ("p","Sverige var länge ett fattigt jordbruksland. Det som drev industrin framåt var landets <strong>naturtillgångar</strong>: skog, järnmalm och vattenkraft. Svenskt järn hade exporterats länge från järnbruk. Från 1800-talets mitt växte <strong>sågverken</strong> i Norrland, särskilt längs kusten kring Sundsvall. Ångdrivna sågar sågade timmer som skeppades till Europa."),
  ("p","Staten byggde de stora <strong>stambanorna</strong>, och privata bolag byggde andra banor. Den första banan för allmän trafik öppnades 1856 mellan Örebro och Nora. Redan 1874 hade Sverige fler kilometer järnväg per invånare än något annat land i Europa. Järnvägen band ihop landet."),
  ("p","Nya uppfinningar och företag kom också. Göran Fredrik Göransson lyckades 1858 använda Bessemermetoden för att göra stål i Sandviken. Alfred Nobel, född i Stockholm 1833, patenterade dynamit 1867, och hans företag byggde fabriker i många länder. Lars Magnus Ericsson startade 1876 en verkstad i Stockholm som blev ett stort telefonföretag."),
  ("ruta","fakta","Sundsvallsstrejken 1879","I Sundsvallstrakten arbetade tusentals människor vid sågverken under hårda villkor. Senvåren 1879 (strejken började den 26 maj) gick många i strejk, sedan sågverksägarna meddelat att sommarlönerna skulle sänkas. Militär sattes in och strejken slogs ned, men händelsen blev en symbol för den svenska arbetarrörelsens tidiga historia."),
  ("p","Samtidigt var Sverige för litet för alla som växte upp där. Befolkningen ökade, och jorden räckte inte till alla. Mellan 1851 och 1910 lämnade ungefär 1,2 miljoner svenskar landet. De flesta, nästan en miljon, åkte till USA. Det värsta året var 1887, då omkring 46 000 svenskar bosatte sig i USA."),
  ("p","Orsakerna var fattigdom, dåliga skördar, att många saknade egen jord, och drömmen om ett bättre liv. Lockelserna var billig jord och arbete i Amerika. Svenskar flyttade till Mellanvästern, särskilt Minnesota och Illinois. Amerikabreven hem berättade vad det var som lockade."),
  ("kolla",["Vilka naturtillgångar var viktiga för svensk industri?","Nämn två svenska personer som betydde mycket och vad de gjorde.","Varför flyttade så många svenskar till Amerika?"]),
 ],
 svar=["Skog, järnmalm och vattenkraft.","T.ex. Alfred Nobel (dynamit 1867) och L M Ericsson (telefoner, verkstad 1876); Göransson (stål 1858).","Fattigdom, brist på jord, missväxt och hopp om ett bättre liv, samt att befolkningen växte."],
))

S.append(dict(id="foljder", nr="7.8", ikon="🌍", titel="Följder, förändring och historiebruk",
 intro="Industrialiseringen gav oss mycket av det vi tar för givet idag, men den kostade också. I det här avsnittet blickar vi bakåt och framåt.",
 block=[
  ("p","Industrialiseringen medförde <strong>miljöeffekter</strong>. Kolrök fyllde luften i städer, floder förorenades av fabriksavfall och skogar avverkades. På den tiden var det få som tänkte på det som ett problem. Vi vet idag att förbränning av kol, olja och gas ökar mängden koldioxid i atmosfären, vilket värmer jorden."),
  ("tab",["Kontinuitet (det som var likt)","Förändring (det som blev nytt)"],[
    ["Många var fortfarande fattiga","Arbetet flyttade till fabriker och städer"],
    ["Barn arbetade","Arbetsdagen styrdes av klockan och maskinen"],
    ["Män hade makt och bestämde mest","Nya klasser och arbetarrörelsen växte fram"],
    ["Människor behövde mat, bostad och trygghet","Varor blev billigare, resor snabbare, folk bodde i städer"]]),
  ("p","Industrialiseringen räknas som en av de största förändringarna i mänsklighetens historia. Den lade grunden till dagens levnadsstandard, men också till dagens klimatproblem."),
  ("ruta","historia","Historiebruk: industrialiseringen i klimatdebatten","I klimatdebatten används ordet <em>förindustriell tid</em> som mätpunkt. FN:s klimatpanel IPCC har använt åren 1850–1900 som jämförelse när man mäter hur mycket jorden har blivit varmare. Här används historien som ett mått. Andra använder industrialiseringen på olika sätt: vissa säger att rika länder som industrialiserades först bär ett större ansvar, andra menar att alla länder nu måste minska utsläppen. Då handlar det om hur man ser på skuld och rättvisa."),
  ("p","Fråga dig alltid: <em>Vem använder historien, och varför?</em> Det är kärnan i historiebruk. Samma händelse kan användas för att motivera olika krav idag."),
  ("kolla",["Nämn en miljöeffekt av industrialiseringen.","Ge ett exempel på kontinuitet och ett på förändring.","Hur används begreppet ”förindustriell tid” i klimatdebatten?"]),
 ],
 svar=["T.ex. kolrök, förorenade vatten, avverkade skogar, ökade utsläpp av koldioxid.","T.ex. kontinuitet: barnarbete/fattigdom fanns kvar; förändring: arbetet flyttade till fabriker.","Som jämförelsepunkt för hur mycket jorden har värmts upp, t.ex. 1850–1900."],
))

F = []

F.append(dict(id="f1", nr="F1", ikon="🔎", titel="Varför Storbritannien? Historikerna är oense",
 intro="Förklaringar till industrialiseringen är inte givna. Olika forskare lyfter fram olika orsaker, och det är en del av historiskt tänkande.",
 block=[
  ("p","Man kan dela in förklaringarna i några typer. Den första lyfter fram <strong>naturtillgångar</strong>: kolet och järnet. Den andra lyfter fram <strong>institutioner</strong>, till exempel patent, stabil politik och att äganderätten skyddades. Den tredje handlar om <strong>ekonomi</strong>: dyr arbetskraft och billig energi gjorde maskiner lönsamma. Den fjärde pekar på <strong>handel och kolonier</strong>."),
  ("tab",["Förklaring","Styrka","Svaghet"],[
    ["Naturtillgångar","Kolet fanns verkligen","Andra länder hade också kol"],
    ["Institutioner","Trygghet för företagare","Svårt att mäta"],
    ["Dyr arbetskraft, billig energi","Förklarar varför maskiner lönade sig","Gäller kanske inte alla branscher"],
    ["Kolonier och handel","Gav råvaror och marknader","Andra kolonialmakter industrialiserades inte lika tidigt"]]),
  ("ruta","tank","Tänk själv","Om du får välja en enda orsak, vilken väljer du, och vilka argument har du för just den? De flesta historiker landar i en kombination av orsaker."),
  ("kolla",["Varför räcker det inte att bara peka på kolet?","Vilken typ av förklaring handlar om patent och politik?","Varför anger historiker ofta flera orsaker?"]),
 ],
 svar=["Andra länder hade också kol, men industrialiserades inte lika tidigt.","Förklaringar om institutioner.","Händelser har sällan en enda orsak, utan flera som samverkar."],
))

F.append(dict(id="f2", nr="F2", ikon="⚖️", titel="Blev det bättre eller sämre? Optimister och pessimister",
 intro="Historiker har länge debatterat om industrialiseringen först gjorde livet bättre eller sämre för vanliga arbetare.",
 block=[
  ("p","<strong>Pessimisterna</strong> pekar på trånga bostäder, sjukdomar, långa arbetsdagar och barnarbete. De hänvisar till samtida skildringar och undersökningar. <strong>Optimisterna</strong> pekar på att reallönerna så småningom steg, att varor blev billigare och att människor på lång sikt fick bättre kost och längre liv."),
  ("p","Debatten visar att svaret beror på <em>vilken grupp</em> man tittar på, <em>vilken tid</em>, och <em>vad man mäter</em>: lön, hälsa, frihet eller trygghet. En hantverkare vars yrke slogs ut av maskinerna kunde förlora, medan hans barnbarn kunde få det bättre."),
  ("kalla","Fabriksinspektörens åsikt (konstruerad källa)","Det är sant att lönerna är högre än på landet, men dessa familjer bor i fuktiga källare, och barnen blir sjuka. Pengar hjälper inte när man saknar rent vatten.","Konstruerad källa baserad på rapporter från brittiska fabriksinspektörer på 1800-talet."),
  ("ruta","historia","Källkritik","Vem skrev källan, och varför? En inspektör kan vilja visa missförhållanden för att få lagar ändrade. En fabriksägare kan vilja visa att allt är bra. Båda kan ha rätt om olika saker."),
  ("kolla",["Vad menar pessimisterna?","Vad menar optimisterna?","Varför kan båda sidor ha rätt?"]),
 ],
 svar=["Att livet blev sämre för många i början, med trångboddhet, sjukdomar och hårt arbete.","Att levnadsstandarden steg på lång sikt, med billigare varor och bättre kost.","De tittar på olika grupper, tidsperioder och mått."],
))

F.append(dict(id="f3", nr="F3", ikon="🧵", titel="Bomullen och slaveriet: en global historia",
 intro="Industrialiseringen i en stad som Manchester hängde ihop med människor på andra sidan jorden.",
 block=[
  ("p","Textilfabrikerna i Storbritannien behövde enorma mängder bomull. Bomullen växer inte i Europa. Den kom till stor del från plantager i södra USA, där människor tvingades arbeta som slavar. Slaveri har alltså varit en del av industrialiseringens bakgrund, även om fabriksarbetaren i Manchester kanske aldrig såg en plantage."),
  ("p","När USA:s inbördeskrig bröt ut 1861 minskade bomullsleveranserna, och många textilarbetare i Storbritannien blev arbetslösa. Det visar hur nära länderna hängde ihop."),
  ("p","Det här är ett exempel på ett <strong>globalt perspektiv</strong>. Ibland berättar man industrialiseringen som en historia om uppfinnare i ett enda land. Med ett globalt perspektiv ser man att råvaror, pengar, varor och människor färdades över haven."),
  ("ruta","tank","Fundera","Vilka andra varor i dina egna kläder eller telefon kommer från andra delar av världen? Vem arbetar med dem idag, och under vilka villkor?"),
  ("kolla",["Varifrån kom mycket av bomullen?","Vad hände när inbördeskriget bröt ut?","Vad menas med ett globalt perspektiv?"]),
 ],
 svar=["Från plantager i södra USA där slavar arbetade.","Bomullsleveranserna minskade och många brittiska textilarbetare blev arbetslösa.","Att man ser hur händelser och ekonomier i olika delar av världen hänger ihop."],
))

F.append(dict(id="f4", nr="F4", ikon="📣", titel="Historiebruk: Vem äger industrialiseringens arv?",
 intro="Industrialiseringen används i dag av politiker, företag, museer och aktivister. Det är bra övning i att se hur historia används.",
 block=[
  ("p","Några exempel. Ett <strong>industrimuseum</strong> kan visa stolthet över uppfinnare och svenska företag. En <strong>fackförening</strong> kan hänvisa till Sundsvallsstrejken 1879 för att visa att rättigheter har kämpats fram. Ett <strong>klimatparti</strong> kan peka på industrialiseringen som starten på utsläppen. Ett <strong>företag</strong> kan använda sin långa historia i marknadsföring."),
  ("tab",["Aktör","Hur historien används","Möjligt syfte"],[
    ["Industrimuseum","Visar uppfinnare och framsteg","Stolthet, bildning, besökare"],
    ["Fackförening","Berättar om strejker och kamp","Visa att rättigheter inte är självklara"],
    ["Klimatrörelse","Pekar på utsläppen sedan 1800-talet","Kräva snabbare omställning"],
    ["Företag","Använder gamla grundare i reklam","Skapa förtroende"]]),
  ("p","Ingen av dessa berättelser är falsk, men var och en väljer ut delar. Ett kritiskt tänkande om historiebruk handlar om att fråga: vad lyfts fram, vad utelämnas, och vem tjänar på berättelsen?"),
  ("ruta","fakta","Så granskar du historiebruk","1. Vem berättar? 2. Vad visas och vad saknas? 3. Vilket syfte kan finnas? 4. Stämmer det med andra källor?"),
  ("kolla",["Nämn två aktörer som använder industrialiseringen i sin berättelse.","Vad kan ett företag vilja uppnå med sin historia?","Vilka frågor kan du ställa för att granska historiebruk?"]),
 ],
 svar=["T.ex. museer, fackföreningar, klimatrörelser, företag.","Skapa förtroende och en stark identitet och sälja mer.","Vem berättar, vad saknas, vilket syfte, hur stämmer det med andra källor."],
))

UPPG = [
 ("Para ihop","Koppla ihop begreppet med rätt förklaring.",["Urbanisering","Strejk","Kapital","Ångmaskin","Arbetarklass","Jordbruksrevolutionen"],["Pengar att investera","Maskin som drivs av vattenånga","Fler odlar mer med nya metoder","Att flytta från landsbygd till stad","Att lägga ned arbetet","Fabriksarbetare som grupp"],"1 – D, 2 – E, 3 – A, 4 – B, 5 – F, 6 – C"),
 ("Orsak och konsekvens","Skriv orsak eller konsekvens vid varje påstående.",["Bönderna fick större skördar.","Många flyttade till städerna.","Arbetarna bildade fackföreningar.","Städerna växte snabbt.","Kolet var billigt och fanns nära."],None,"Skördarna: orsak (till att fler kunde försörjas); flytten: konsekvens; fackföreningar: konsekvens av dåliga villkor; städerna växte: konsekvens; kol: orsak till industrialiseringen."),
 ("Tidslinje","Sätt in händelserna i rätt ordning.",["Storstrejken","Watt patenterar sin ångmaskin","Dynamit patenteras av Nobel","Liverpool–Manchester-banan öppnas","LO bildas"],None,"1769 Watt; 1830 Liverpool–Manchester; 1867 Nobel; 1898 LO; 1909 Storstrejken."),
 ("Förklara","Förklara med minst två orsaker varför industrialiseringen började i Storbritannien.",[],None,"E: två orsaker nämns (t.ex. kol och kolonier). C: orsakerna förklaras och kopplas ihop. A: orsakerna vägs mot varandra och man resonerar om att historiker är oense."),
 ("Jämför","Jämför hur en bonde och en fabriksarbetare levde. Vad var lika och vad var olika?",[],None,"Lika: hårt arbete, ofta fattigdom, barn hjälpte till. Olika: bonden följde årstiderna och arbetade hemma, fabriksarbetaren följde klockan och maskinen och arbetade för lön."),
 ("Källa","Läs den konstruerade källan om barnarbete i 7.4. Vem kan ha skrivit den, och vad kan man lära sig av den? Vad kan man inte veta?",[],None,"Skriven av en person med erfarenhet av barnarbete (eller en författare som bygger på sådana vittnesmål). Man kan lära sig om arbetsdagen, men inte hur vanligt det var, eller hur alla barn upplevde det."),
 ("Sverige","Förklara varför Sverige industrialiserades sent men snabbt. Ta med två naturtillgångar och en uppfinning eller ett företag.",[],None,"Skog, järnmalm och vattenkraft; exempel Göransson, Nobel, Ericsson; järnvägar. Sent eftersom landet var ett fattigt jordbruksland, snabbt tack vare export, nya tekniker och järnvägar."),
 ("Emigration","Gör en lista över tre skäl till att svenskar åkte till Amerika, och ett skäl att stanna.",[],None,"Skäl att åka: fattigdom, brist på jord, bättre chans; att stanna: familj, hemtrakten, rädsla för det okända."),
 ("Miljö","Beskriv två miljöeffekter av industrialiseringen då, och en som vi ser nu.",[],None,"Då: kolrök, förorenat vatten; nu: ökade koldioxidutsläpp och klimatförändringar."),
 ("Debatt","Förbered ett kort inlägg: ”Industrialiseringen var bra för människorna.” Argumentera för eller emot, och använd minst två historiska exempel.",[],None,"Bedöms utifrån: tydligt ställningstagande, historiska exempel, att man väger argument för och emot och ser olika grupper."),
]

BEGREPP = [
 ("Industrialisering","Processen då ett samhälle går från jordbruk till industri."),
 ("Jordbrukssamhälle","Samhälle där de flesta lever på att odla jorden."),
 ("Jordbruksrevolutionen","Nya odlingsmetoder som gav större skördar."),
 ("Kapital","Pengar och tillgångar som kan investeras."),
 ("Kolonier","Områden som en annan stat styr över."),
 ("Ångmaskin","Maskin som drivs av vattenånga."),
 ("Textilindustri","Tillverkning av garn och tyg."),
 ("Fabrik","Stor arbetsplats med maskiner."),
 ("Urbanisering","Att människor flyttar till städer."),
 ("Borgerskap","Fabriksägare och företagare."),
 ("Arbetarklass","Grupp som lever på lön från fabriksarbete."),
 ("Fackförening","Organisation för arbetare."),
 ("Strejk","Att lägga ned arbetet för att få igenom krav."),
 ("Lockout","Att arbetsgivaren stänger ute arbetarna."),
 ("Emigration","Att flytta från sitt land till ett annat."),
 ("Historiebruk","Hur historia används i nutiden, av vem och varför."),
]

SAMMAN = [
 "Före industrialiseringen levde de flesta i ett jordbrukssamhälle. Jordbruksrevolutionen gav mer mat och frigjorde arbetskraft.",
 "Industrialiseringen började i Storbritannien omkring 1760. Kol, järn, kapital, kolonier och handel samverkade.",
 "Ångmaskinen, textilindustrin och järnvägen blev symboler för den nya tiden.",
 "Fabriksarbetet var hårt, med långa dagar och barnarbete. Lagar kom så småningom, till exempel i Storbritannien 1833.",
 "Städerna växte (urbanisering) och nya klasser bildades: borgerskap, medelklass och arbetarklass.",
 "Arbetarna organiserade sig i fackföreningar och partier. I Sverige: SAP 1889, LO 1898, storstrejken 1909.",
 "Sverige industrialiserades sent men snabbt: sågverk, järn, järnvägar, Nobel, Ericsson. Omkring 1,2 miljoner svenskar emigrerade 1851–1910.",
 "Industrialiseringen gav högre levnadsstandard men också miljöproblem. Den används idag i klimatdebatten, vilket kräver att man granskar historiebruk.",
]

TEST_A = [
 ("Vad var jordbruksrevolutionen?",["Ett uppror bland bönderna","Nya odlingsmetoder som gav större skördar","En lag om skolplikt","En ny järnväg"],1),
 ("Vilken faktor hjälpte Storbritannien att industrialiseras?",["Brist på kol","Tillgång till kol och järn","Inga kolonier","Ingen handel"],1),
 ("Vad gjorde ångmaskinen särskilt användbar?",["Den drevs av vind","Den kunde placeras nästan var som helst","Den behövde ett vattenfall","Den var gratis"],1),
 ("Vilket år öppnades den första järnvägen för allmän trafik i Sverige?",["1756","1856","1906","1805"],1),
 ("Vad innebär urbanisering?",["Att människor flyttar från landsbygd till stad","Att fabriker flyttar till landet","Att städer minskar","Att man bygger tunnelbana"],0),
 ("Vilket år bildades LO i Sverige?",["1848","1879","1898","1938"],2),
 ("Vilket land fick flest svenska emigranter?",["Danmark","USA","Tyskland","Australien"],1),
 ("Vad är en rimlig förklaring till att klimatdebatten talar om ”förindustriell tid”?",["Man vill jämföra dagens temperatur med tiden före stora utsläpp","Man vill förbjuda fabriker","Man tycker att jordbrukssamhället var bäst","Det är ett gammalt ord för vinter"],0),
]

TEST_B = [
 ("Ge två orsaker till att industrialiseringen började i Storbritannien.","T.ex. kol och järn, kapital, kolonier och handel, jordbruksrevolutionen."),
 ("Förklara vad en fackförening gör.","Arbetare går samman för att förhandla om lön och arbetsvillkor och kan strejka."),
 ("Nämn två nackdelar med att bo i en industristad på 1800-talet.","T.ex. trångboddhet, sjukdomar, smutsig luft, ont om rent vatten."),
 ("Ge ett exempel på kontinuitet under industrialiseringen.","T.ex. fattigdom och barnarbete fanns kvar; män hade fortfarande makten."),
 ("Varför emigrerade många svenskar på 1800-talet?","Fattigdom, brist på jord, missväxt och hopp om ett bättre liv."),
 ("Ge ett exempel på hur industrialiseringen används i dagens klimatdebatt.","Som jämförelsepunkt (förindustriell tid), eller för att diskutera vilka länder som bär ansvar för utsläppen."),
]

KALLA = dict(
 text="Jag arbetar tolv timmar om dagen vid maskinen. Mitt barn, som är tio år, hjälper till med att knyta trådar. Vi får lön varje lördag, men det räcker bara till mat och hyra. Ibland tänker jag att det var bättre på landet, men där fanns ingenting att tjäna.",
 ursprung="Konstruerad källa baserad på vittnesmål från textilarbetare i England på 1800-talet. Skriven som om en arbetare berättar för en undersökningskommission.",
 fragor=[("Vilken typ av källa är detta, och är den primär eller sekundär?","En konstruerad källa som efterliknar ett vittnesmål (primärkälla till sin typ). Den är ett utdrag som vi själva konstruerat, så den visar ett typiskt perspektiv, inte en verklig person."),
         ("Vad berättar källan om arbetsvillkoren?","Tolv timmars arbetsdag, barnarbete, låg lön som bara räcker till mat och hyra."),
         ("Vad kan vara problemet med att bara använda den här källan?","Den visar en persons berättelse. Fler källor behövs för att veta hur vanligt det var, och en undersökningskommission kan ha ställt ledande frågor."),
         ("Vilken kontinuitet och förändring syns i texten?","Kontinuitet: barn arbetar och familjen är fattig. Förändring: arbetet sker vid en maskin i fabrik och man får lön i pengar.")],
)

SKRIV = dict(
 uppgift="Skriv en text på 300–400 ord: <strong>Hur förändrade industrialiseringen människors liv?</strong> Ta med orsaker till att den började, hur olika grupper (fabriksägare, arbetare, kvinnor, barn) påverkades, en kontinuitet och en förändring, och en reflektion kring hur industrialiseringen används i dagens klimatdebatt.",
 stod=["E: Du beskriver några förändringar och ger minst en orsak. Du använder några begrepp (t.ex. fabrik, urbanisering, arbetarklass) och nämner både något positivt och något negativt.",
       "C: Du förklarar flera orsaker och konsekvenser och kopplar ihop dem. Du jämför olika gruppers situation och ger exempel på både kontinuitet och förändring. Du använder begreppen säkert.",
       "A: Du väger orsakerna mot varandra, visar att historiker kan tolka olika, och drar slutsatser om långsiktiga följder. Du analyserar hur och varför industrialiseringen används i klimatdebatten och kopplar till egna exempel."],
)

LAB = dict(
 titel="Historikerns verkstad: Hur levde man? En källundersökning och ett rollspel",
 syfte="Eleverna övar att analysera källor och att se en händelse från olika perspektiv. De tränar källkritik, empati och argumentation.",
 material="Fyra rollkort (fabriksägare, fabriksarbetare med barn, fackföreningsledare, fabriksinspektör), en konstruerad källa (se 7.4 eller KALLA), papper och penna, tidtagarur.",
 utforande=["Dela in klassen i grupper om fyra. Varje elev får ett rollkort.",
            "Läs källan tillsammans och skriv ned tre saker den berättar och två saker den inte berättar.",
            "Förbered i 5 minuter vad din roll tycker om frågan: ska barn få arbeta i fabriken?",
            "Rollspel: varje roll får 1 minut att säga sitt. Sedan 5 minuters fri diskussion.",
            "Gruppen försöker komma överens om ett förslag till regler. Skriv ned förslaget.",
            "Utvärdera: jämför gruppernas förslag med verkliga lagar (t.ex. 1833 års fabrikslag)."],
 fragor=[("Vilka argument använde fabriksägaren, och varför?","T.ex. att barnen behövs för att få fabriken att gå runt och att familjerna behöver pengarna."),
         ("Vilka argument använde fackföreningsledaren och inspektören?","Att barnen far illa och behöver skola, att lagen ska skydda dem, att arbetare måste få organisera sig."),
         ("Varför är det bra att undersöka en fråga från flera perspektiv?","För att olika grupper hade olika intressen och information, och helhetsbilden blir rikare.")],
 bonus="För läraren: Låt eleverna jämföra gruppernas regler med verkliga lagar (Storbritannien 1833, Sverige slutet av 1800-talet). Bedöm förmågan att använda källor (E: kan peka på vad källan säger; C: kan koppla till sammanhanget; A: kan värdera källans användbarhet och begränsningar). Ett tips är att avsluta med en fråga: Vilka frågor om barn och arbete är fortfarande aktuella i världen idag?",
)

LARAR = [
 ("Koppling till Lgr22","Kapitlet täcker syftets mål om kunskaper om händelser, aktörer och förändringsprocesser, historiska begrepp (industrialisering, urbanisering, arbetarrörelse), källkritik och historiebruk. Centralt innehåll: samhällsomvandlingar, framväxten av industrisamhällen, orsaker och följder, samt kontinuitet och förändring. Kunskapskraven rör orsak och konsekvens, perspektiv, källor och historiebruk."),
 ("Förslag på upplägg (8 lektioner)","1. Jordbrukssamhället och jordbruksrevolutionen (7.1). 2. Varför Storbritannien? Faktorer och prioritering (7.2). 3. Ångmaskin, textil, järnväg, tidslinje (7.3). 4. Fabriken, barnarbete, källanalys (7.4). 5. Staden och klasserna (7.5). 6. Arbetarrörelsen och rollspel (7.6, Historikerns verkstad). 7. Sverige och emigration (7.7). 8. Följder, historiebruk och skrivuppgift (7.8)."),
 ("Vanliga missuppfattningar","Att industrialiseringen skedde över en natt och samtidigt överallt. Att barnarbete uppfanns av fabrikerna. Att alla arbetare hade det sämre än före. Att uppfinnare ensamma förklarar utvecklingen. Att Sverige var industriland redan 1800. Att emigrationen bara bestod av fattiga: många hade också andra motiv."),
 ("Bedömningsstöd E/C/A","E: eleven beskriver några förändringar och ger enkla orsaker, använder några begrepp. C: eleven förklarar samband mellan orsaker och följder, jämför grupper, använder begreppen säkert och gör en enkel källanalys. A: eleven värderar orsakernas betydelse, ser flera perspektiv och tolkningar, analyserar källor och historiebruk, och drar slutsatser om kontinuitet och förändring."),
 ("Tips för Blooket och Jeopardy (10 kategorier)","1. Uppfinningar (Watt, Stephenson). 2. Orsaker till industrialiseringen. 3. Arbetsvillkor och barnarbete. 4. Städer och klasser. 5. Arbetarrörelsen (SAP, LO, storstrejken). 6. Svenska företag och personer (Nobel, Ericsson, Göransson). 7. Emigration. 8. Miljö och klimat. 9. Begrepp. 10. Årtal och tidslinje. Exempel: ”Vilken maskin patenterades av James Watt 1769?” (ångmaskinen)."),
]

KALLOR = [
 ("Skolverket – Kommentarmaterial till kursplanen i historia, grundskolan (2022)","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
 ("World History Encyclopedia – Why the Industrial Revolution Started in Britain","https://www.worldhistory.org/article/2221/why-the-industrial-revolution-started-in-britain/"),
 ("Britannica – Factory Act (Storbritannien, 1833)","https://www.britannica.com/print/article/200060"),
 ("Britannica – Watt steam engine","https://www.britannica.com/print/article/2126358"),
 ("Trafikverket – Om järnvägens dåtid, nutid och framtid","https://www.trafikverket.se/resa-och-trafik/jarnvag/jarnkoll--fakta-om-svensk-jarnvag/om-jarnvagens-datid-nutid-och-framtid/"),
 ("SCB – Så påverkade utvandringen till Amerika Sveriges befolkning","https://scb.se/hitta-statistik/artiklar/2013/sa-paverkade-utvandringen-till-amerika-sveriges-befolkning"),
 ("ERIH – Göran Fredrik Göransson (1819–1900)","https://www.erih.net/how-it-started/stories-about-people-biographies/biography/goeransson"),
 ("Ericsson – 1876: Lars Magnus Ericsson startar en mekanisk verkstad","https://www.ericsson.com/en/about-us/history/company/timeline-placeholder/timeline-1876-lars-magnus-ericsson-starts-a-mechanical-workshop"),
 ("Sundsvalls museum – I industrialismens spår","https://sundsvall.se/kommun/uppleva-och-gora/kultur/kulturmagasinet/sundsvalls-museum/skolprogram/i-industrialismens-spar"),
 ("Carbon Brief – The challenge of defining the pre-industrial era","https://www.carbonbrief.org/challenge-defining-pre-industrial-era"),
]

F_UPPG = [
 ("●","Förklara varför historiker har olika förklaringar till att industrialiseringen började i Storbritannien. Ge två exempel.",[],None,"Händelser har många orsaker och bevisen kan tolkas olika. Exempel: kol/naturtillgångar och dyr arbetskraft/billig energi."),
 ("●●","Jämför pessimisternas och optimisternas syn på industrialiseringens följder. Vilken tycker du är mest övertygande, och varför?",[],None,"Pessimisterna: trångboddhet, sjukdomar, barnarbete. Optimisterna: på lång sikt högre reallöner och bättre kost. Eleven motiverar med exempel och tidsperspektiv."),
 ("●●","Förklara hur bomullen, slaveriet och textilindustrin hänger ihop.",[],None,"Fabrikerna behövde bomull som kom till stor del från plantager där slavar arbetade. Industrialiseringen och slaveriet var alltså kopplade."),
 ("●●●","Välj en aktör (t.ex. fackförening, klimatrörelse, museum, företag). Analysera hur den använder industrialiseringen, vad som utelämnas och vilket syfte den kan ha.",[],None,"Bedöms: tydlig aktör, urval i berättelsen, syfte, kritisk granskning. A-nivå: flera perspektiv och slutsatser."),
 ("●●●","Skriv ett kort svar: Var industrialiseringen en 'revolution' eller en långsam förändring? Använd kontinuitet och förändring.",[],None,"Argument för revolution: snabba, stora förändringar. Mot: skedde gradvis, olika tider på olika platser, mycket var kontinuitet. Bra svar väger båda."),
]

F_SAMMAN = [
 "Historiker lyfter fram olika förklaringar till industrialiseringen och ger dem olika vikt.",
 "Debatten mellan optimister och pessimister visar att svaret beror på grupp, tid och mått.",
 "Bomullen och slaveriet visar att industrialiseringen var en global historia.",
 "Historiebruk handlar om att fråga vem som berättar, vad som utelämnas och varför.",
]

F_BEGR = [
 ("Pessimister","Forskare som menar att levnadsvillkoren blev sämre."),
 ("Optimister","Forskare som menar att levnadsvillkoren förbättrades."),
 ("Global historia","Berättelse som ser kopplingar över länder och kontinenter."),
 ("Reallön","Vad lönen kan köpa i varor och tjänster."),
 ("Historiografi","Hur historiker har tolkat och skrivit om en period."),
]

BLOOKET = [
 ("Vad kallas ett samhälle där de flesta lever på jordbruk?","Jordbrukssamhälle","Industrisamhälle","Kolonisamhälle","Handelssamhälle"),
 ("Var började industrialiseringen?","Storbritannien","Sverige","USA","Ryssland"),
 ("Ungefär vilket årtionde brukar industrialiseringen i Storbritannien räknas börja?","1760-talet","1560-talet","1860-talet","1960-talet"),
 ("Vem fick patent på en förbättrad ångmaskin 1769?","James Watt","George Stephenson","Alfred Nobel","Karl Marx"),
 ("Vilket bränsle användes mest i ångmaskinerna under industrialiseringen i Storbritannien?","Kol","Vindkraft","Solenergi","Kärnkraft"),
 ("Vad menas med urbanisering?","Flytt från landsbygd till stad","Flytt från stad till land","Nya jordbruksmetoder","Byggande av järnvägar"),
 ("Vilken bransch blev först ut att mekaniseras?","Textilindustrin","Bilindustrin","Flygindustrin","Datorindustrin"),
 ("Vilket lokomotiv vann tävlingen inför Liverpool–Manchester-banan?","Rocket","Oscar","Titan","Express"),
 ("Vilket år öppnades Sveriges första järnväg för allmän trafik?","1856","1756","1906","1805"),
 ("Vad kallas fabriksägare och företagare som grupp?","Borgerskapet","Adeln","Arbetarklassen","Prästeståndet"),
 ("Vad gjorde 1833 års brittiska fabrikslag?","Begränsade barnarbete i textilfabriker","Förbjöd fackföreningar","Införde allmän rösträtt","Förbjöd alla fabriker"),
 ("Vad är en strejk?","Att man lägger ned arbetet för att få igenom krav","Att en fabrik stänger","Att man startar en fackförening","Att man flyttar till stan"),
 ("Vilket år grundades Socialdemokratiska arbetarpartiet i Sverige?","1889","1789","1989","1909"),
 ("Vilket år bildades LO?","1898","1798","1938","1909"),
 ("Vilket år var storstrejken i Sverige?","1909","1809","1919","1879"),
 ("Vem patenterade dynamit 1867?","Alfred Nobel","L M Ericsson","Göran Fredrik Göransson","James Watt"),
 ("Vilket svenskt företag startade 1876 i Stockholm som verkstad?","Ericsson","Volvo","IKEA","Saab"),
 ("Vilken metod använde Göran Fredrik Göransson 1858 för att göra stål i Sandviken?","Bessemermetoden","Newcomens metod","Dynamitmetoden","Hantverksmetoden"),
 ("Vilket område i Norrland var känt för sågverk och en strejk 1879?","Sundsvall","Malmö","Göteborg","Karlstad"),
 ("Ungefär hur många svenskar emigrerade 1851–1910?","Omkring 1,2 miljoner","Omkring 12 000","Omkring 120 000","Omkring 12 miljoner"),
 ("Vilket land valde de flesta svenska emigranter?","USA","Brasilien","Australien","Kina"),
 ("Vad innebär kontinuitet i historia?","Det som är sig likt över tid","Det som förändras","En plötslig händelse","En lag"),
 ("Vad är en miljöeffekt av industrialiseringen?","Förorenad luft från kolrök","Renare vatten","Mindre avverkning","Färre fabriker"),
 ("Vilka år används ofta som jämförelsepunkt för 'förindustriell tid' i klimatsammanhang (IPCC)?","1850–1900","1650–1700","1950–2000","2000–2020"),
 ("Vad är historiebruk?","Hur historia används i nutiden av någon för något syfte","Att bläddra i en lärobok","Att lära sig årtal","En sorts museum"),
 ("Vilket avtal slöts 1938 mellan LO och arbetsgivarna?","Saltsjöbadsavtalet","Karlstadsavtalet","Versaillesfreden","Berlinavtalet"),
]

JEOPARDY = {
 "Uppfinningar": [
  (100,"Den maskin som drivs av vattenånga","Vad är ångmaskinen?"),
  (200,"Han fick patent på en förbättrad ångmaskin 1769","Vem är James Watt?"),
  (300,"Fordon som drar vagnar på räls, ångdrivet","Vad är ett lokomotiv?"),
  (400,"Banan som öppnades 1830 mellan två brittiska städer","Vad är Liverpool–Manchester?"),
  (500,"Den bransch som mekaniserades först","Vad är textilindustrin?")],
 "Arbete och klasser": [
  (100,"Gruppen som äger fabriker och företag","Vad är borgerskapet?"),
  (200,"Gruppen som arbetade i fabrikerna för lön","Vad är arbetarklassen?"),
  (300,"Att många flyttar från land till stad","Vad är urbanisering?"),
  (400,"Lagen som 1833 begränsade barnarbete i brittiska textilfabriker","Vad är fabrikslagen 1833?"),
  (500,"Mellan arbetarklass och borgerskap","Vad är medelklassen?")],
 "Arbetarrörelsen": [
  (100,"Att lägga ned arbetet för att få igenom krav","Vad är en strejk?"),
  (200,"Organisation där arbetare går samman","Vad är en fackförening?"),
  (300,"Årtalet då LO bildades","Vad är 1898?"),
  (400,"Den stora konflikten i augusti–september 1909","Vad är storstrejken?"),
  (500,"Avtalet mellan LO och arbetsgivarna 1938","Vad är Saltsjöbadsavtalet?")],
 "Sverige": [
  (100,"Han patenterade dynamit 1867","Vem är Alfred Nobel?"),
  (200,"Stad i Norrland känd för sågverk","Vad är Sundsvall?"),
  (300,"Året då första allmänna järnvägen öppnades","Vad är 1856?"),
  (400,"Ort där Göransson gjorde stål 1858","Vad är Sandviken?"),
  (500,"Företaget som började som verkstad 1876","Vad är Ericsson?")],
 "Följder och historiebruk": [
  (100,"Att flytta till ett annat land","Vad är emigration?"),
  (200,"Landet de flesta svenska emigranter åkte till","Vad är USA?"),
  (300,"Utsläpp som ökar vid förbränning av kol","Vad är koldioxid?"),
  (400,"Det som är sig likt över tid","Vad är kontinuitet?"),
  (500,"Att fråga vem som berättar historien och varför","Vad är historiebruk (kritiskt granskat)?")],
}

GRUPPER = [
 ("fore","Från jordbruk till industri","Hur levde man före industrialiseringen, och varför började det i Storbritannien?",["fore","britannien","maskiner"]),
 ("fabrik","Fabrik, stad och rörelse","Arbetsvillkor, städer, klasser och arbetarrörelsen.",["fabriken","staden","rorelsen"]),
 ("sverige","Sverige, miljö och historiebruk","Sveriges väg, emigrationen och vad industrialiseringen betyder idag.",["sverige","foljder"]),
]

SCEN = dict(
 titel="Tidsresa genom industrialiseringen", plats="Från en bondby till en fabriksstad", tid="1780–1900",
 sky=("#b8c4cc","#e5dccb"), mark="#6b5a42",
 walker=dict(typ="arbetare"),
 etapper=[
  dict(x_etikett="Byn", tid="Före 1760", plats="En bondby i England", rubrik="Livet på landet",
   fakta=["Du bor i en liten by. Familjen odlar och spinner garn för hand i stugan.","Arbetet följer årstiderna, och maten är det viktigaste."],
   fraga="Vad var typiskt för ett jordbrukssamhälle?", alt=["De flesta arbetade i fabriker","De flesta levde av att odla jorden","De flesta reste med tåg"], ratt=1,
   forklaring="I jordbrukssamhället försörjde de flesta sig på jordbruk.", deko=[("bondgard",-120,1.0),("torp",80,0.9),("trad",180,1.0)]),
  dict(x_etikett="Ångan", tid="1769", plats="Storbritannien", rubrik="Ångmaskinen",
   fakta=["James Watt får patent på sin förbättrade ångmaskin. Kol bränns för att koka vatten.","Maskinen kan stå nästan var som helst, och fabriker byggs i städer."],
   fraga="Varför var ångmaskinen så viktig?", alt=["Den behövde inget bränsle","Den var inte beroende av vind eller vattenfall","Den var gratis att köpa"], ratt=1,
   forklaring="Ångmaskinen kunde placeras var som helst och gav jämn kraft.", deko=[("fabrik",-100,1.2),("skorstenar",100,1.0)]),
  dict(x_etikett="Tåget", tid="1830", plats="Manchester", rubrik="Järnvägen kommer",
   fakta=["Banan mellan Liverpool och Manchester öppnas. Tåget kör snabbare än en häst.","Varor och människor kan färdas långt på kort tid."],
   fraga="Vad ändrade järnvägen?", alt=["Varor och människor kunde färdas snabbt och långt","Fabrikerna stängde","Alla blev rika"], ratt=0,
   forklaring="Järnvägen band ihop orter och marknader.", deko=[("lok",-80,1.2),("folkmassa",120,0.9)]),
  dict(x_etikett="Fabriken", tid="1833", plats="Manchester", rubrik="Arbetet i fabriken",
   fakta=["Du arbetar tolv timmar om dagen vid en maskin. Barn arbetar bredvid dig.","Samma år införs en lag som begränsar barnarbete i textilfabriker."],
   fraga="Vad gjorde fabrikslagen 1833?", alt=["Förbjöd barn under nio år att arbeta i textilfabriker","Förbjöd alla fabriker","Gav kvinnor rösträtt"], ratt=0,
   forklaring="Lagen satte åldersgräns och krävde inspektörer.", deko=[("fabrik",-60,1.3),("skorstenar",130,1.1)]),
  dict(x_etikett="Staden", tid="1850", plats="En industristad", rubrik="Arbetarkvarteren",
   fakta=["Familjen bor i ett trångt hus i staden. Det finns ont om rent vatten.","Staden växer snabbt, men många är sjuka och fattiga."],
   fraga="Vad kallas det när människor flyttar från landsbygd till stad?", alt=["Emigration","Urbanisering","Industrialisering"], ratt=1,
   forklaring="Urbanisering betyder att människor flyttar till städer.", deko=[("arbetarhus",-80,1.1),("skorstenar",100,1.2),("folkmassa",190,0.8)]),
  dict(x_etikett="Norrland", tid="1879", plats="Sundsvall", rubrik="Sågverken och strejken",
   fakta=["I Sverige växer sågverken längs Norrlandskusten. Tusentals arbetar under hårda villkor.","Senvåren 1879 strejkar många arbetare, men strejken slås ned med militär hjälp."],
   fraga="Vad är en strejk?", alt=["Att arbetarna lägger ned arbetet","Att fabriken stängs av ägaren","Att man flyttar utomlands"], ratt=0,
   forklaring="En strejk är när arbetare lägger ned arbetet för att få igenom krav. Arbetsgivarens stängning kallas lockout.", deko=[("gran",-120,1.2),("angbat",90,1.0),("hamn",190,0.9)]),
  dict(x_etikett="Amerika", tid="1887", plats="Göteborgs hamn", rubrik="Sammanfattning: ett nytt samhälle",
   fakta=["Svenska emigranter stiger ombord på ångbåtar mot Amerika.","Industrialiseringen gav fabriker, städer, klasser och arbetarrörelse, och den ger oss både högre levnadsstandard och klimatproblem."],
   deko=[("angbat",-60,1.3),("hamn",120,1.0),("folkmassa",200,0.8)]),
 ],
 diskutera="Industrialiseringen gav oss både högre levnadsstandard och miljöproblem. Vem ska ta ansvar för följderna idag, och hur påverkar historien vad vi tycker?",
)
