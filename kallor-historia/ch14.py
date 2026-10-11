# -*- coding: utf-8 -*-
# Kapitel 14 – Demokrati och välfärd i Sverige (åk 9)
T = dict(
 nr=14, namn="Demokrati och välfärd i Sverige", under="Från fyra stånd till allmän rösträtt, folkhem och ett mer jämlikt samhälle",
 fil="historia-14-demokrati-valfard", arskurs=9, nodeid="historia-demokrati-valfard",
 mal=["beskriva hur Sverige gick från ståndsriksdag till tvåkammarriksdag och sedan till enkammarriksdag",
      "förklara varför folkrörelserna var viktiga för demokratin",
      "redogöra för rösträttens utveckling för män och kvinnor",
      "förklara vad Ådalen 1931 och Saltsjöbadsavtalet 1938 betydde för arbetsmarknaden",
      "beskriva folkhemmet och viktiga välfärdsreformer och förklara deras orsaker och konsekvenser",
      "följa förändringar i synen på kön, jämställdhet och sexualitet",
      "beskriva hur invandring och minoriteters situation har påverkat Sverige",
      "analysera hur begreppet ”folkhemmet” används i politiken idag"],
 fundera="Fråga någon äldre i din släkt om en förändring de upplevt i Sverige, till exempel rösträtt, arbete, skola eller att få bo med den man älskar. Vad har blivit bättre? Vad är sig likt? Skriv ned två punkter innan du läser.",
)

S = []

S.append(dict(id="standen", nr="14.1", ikon="🏛️", titel="Från ståndsriksdag till tvåkammarriksdag",
 intro="För drygt 150 år sedan var det få som fick bestämma i Sverige. Riksdagen var uppdelad efter vem man var född som, och inte efter vad man tyckte.",
 block=[
  ("p","Fram till 1866 bestod riksdagen av fyra <strong>stånd</strong>: adeln, prästerna, borgarna och bönderna. Varje stånd hade sin egen kammare och sin egen röst. Arbetare, tjänstefolk, torpare och nästan alla kvinnor fanns inte med alls. Stånden kunde stoppa beslut som de inte gillade, och det gjorde reformer långsamma."),
  ("p","Industrialiseringen och nya idéer från upplysningen och liberalismen gjorde att kraven på förändring växte. Vid mitten av 1800-talet ansåg många att ståndsindelningen var förlegad. År 1865–66 beslutade riksdagen om en ny ordning: ståndsriksdagen avskaffades och ersattes av en <strong>tvåkammarriksdag</strong>, som började fungera 1867."),
  ("p","Den nya riksdagen hade två kamrar. <strong>Första kammaren</strong> valdes indirekt och bara av dem som hade mycket pengar eller mark. <strong>Andra kammaren</strong> valdes direkt, men rösträtten krävde att man hade inkomst eller egendom, så att de flesta män ändå inte fick rösta. Kvinnor fick inte rösta alls i riksdagsval. Reformen var alltså ett steg mot demokrati, men ett litet steg."),
  ("tidslinje",[("1809","Ny regeringsform"),("1866","Ståndsriksdagen avskaffas"),("1867","Tvåkammarriksdagen börjar"),("1909","Allmän rösträtt för män"),("1921","Kvinnor får rösta i riksdagsval"),("1971","Enkammarriksdag")]),
  ("ruta","fakta","Kung, regering och riksdag","Under 1800-talet hade kungen fortfarande stor makt, och regeringen utsågs av honom. Först 1917 blev det en regel i praktiken att regeringen måste ha stöd i riksdagen. Den principen kallas <strong>parlamentarism</strong>."),
  ("ruta","tank","Kontinuitet och förändring","Vad förändrades 1866, och vad var kvar som förut? Förändrat: stånden försvann och fler kunde få politiskt inflytande. Kvar: de rika hade fortfarande mest att säga till om, och kvinnorna stod utanför."),
  ("kolla",["Vilka fyra stånd fanns i den gamla riksdagen?","Vad ändrades 1866?","Varför kallas reformen 1866 ett litet steg mot demokrati?"]),
 ],
 svar=["Adel, präster, borgare och bönder.","Ståndsriksdagen ersattes av en tvåkammarriksdag (från 1867).","Rösträtten var fortfarande begränsad av inkomst och egendom, och kvinnor fick inte rösta."],
))

S.append(dict(id="folkrorelser", nr="14.2", ikon="🤝", titel="Folkrörelserna – demokrati underifrån",
 intro="När de flesta inte fick rösta organiserade sig vanliga människor på andra sätt. Föreningar blev skolor i demokrati.",
 block=[
  ("p","Under andra delen av 1800-talet växte <strong>folkrörelser</strong> fram i Sverige. Det är stora föreningar där människor går samman för att driva en gemensam sak. Medlemmarna lärde sig att hålla möten, skriva protokoll, rösta och välja styrelse. Många som inte hade rösträtt i riksdagsval lärde sig alltså demokratiska arbetssätt i sin förening."),
  ("tab",["Folkrörelse","Exempel på start","Vad ville man?"],[
    ["Frikyrkorörelsen","Baptister 1848, Svenska Missionsförbundet 1878","Frihet att välja tro och möta Gud utan statskyrkans tvång"],
    ["Nykterhetsrörelsen","IOGT i Sverige 1879","Minska alkoholmissbruk, som drabbade särskilt kvinnor och barn"],
    ["Arbetarrörelsen","Socialdemokratiska partiet 1889, LO 1898","Bättre löner och villkor, rösträtt och jämlikhet"],
    ["Kvinnorörelsen","Fredrika-Bremer-förbundet 1884, rösträttsförening 1902","Kvinnors rätt till utbildning, yrken och rösträtt"]]),
  ("p","Folkrörelserna byggde egna lokaler: <strong>Folkets hus</strong> och bönhus, sedan studiecirklar, bibliotek och folkhögskolor. I tusentals små samhällen blev föreningen ett centrum för bildning. Arbetarrörelsens kamp ledde så småningom till fackförbund som kunde förhandla om löner, och till ett politiskt parti som kunde ändra lagar."),
  ("p","Rörelserna drev ofta olika krav, men de hade en sak gemensamt: de pressade makthavarna att lyssna. När rösträtten väl kom hade många människor redan erfarenhet av att organisera sig. Därför ser historiker folkrörelserna som en viktig förklaring till att Sveriges väg till demokrati blev förhållandevis fredlig."),
  ("ruta","historia","Vad var motkrafterna?","Alla var inte positiva. Företagare, kyrkan och delar av överheten ogillade ofta arbetarrörelsen, och emellanåt hotades eller sparkades fackliga ledare. Det visar att demokratin inte bara delades ut. Den kämpades fram."),
  ("bild","arbetare","Fackföreningar och föreningsmöten blev viktiga skolor i demokrati."),
  ("kolla",["Vad är en folkrörelse?","Nämn två folkrörelser och vad de ville.","Hur bidrog folkrörelserna till demokratin?"]),
 ],
 svar=["En stor förening där människor går samman för en gemensam sak.","T.ex. nykterhetsrörelsen (mindre alkoholproblem) och arbetarrörelsen (bättre villkor och rösträtt).","De lärde människor demokratiska arbetssätt och satte press på makthavarna."],
))

S.append(dict(id="rostratt", nr="14.3", ikon="🗳️", titel="Kampen om rösträtten",
 intro="Rösträtt är makt att påverka. Därför var striden om vem som skulle få rösta så hård.",
 block=[
  ("p","Arbetarrörelsen och liberalerna krävde allmän och lika rösträtt: alla ska ha en röst. Det kunde ske i stora demonstrationer, strejker (till exempel storstrejken 1902 för rösträtten) och i riksdagen. Motståndarna, många konservativa, ville behålla den gamla ordningen eftersom de fruktade att arbetare skulle få för stort inflytande."),
  ("p","År <strong>1909</strong> beslutade riksdagen att män över 24 år fick allmän rösträtt till andra kammaren (första valet med de nya reglerna hölls 1911). Det fanns undantag: bland andra den som fått fattigvård eller inte fullgjort sina skyldigheter, till exempel värnplikt, fick inte rösta. Hela 1900-talet handlade om att ta bort sådana hinder. Första kammaren fortsatte att vara indirekt vald länge."),
  ("p","För kvinnor tog kampen längre tid. Kvinnorörelsen, bland andra Landsföreningen för kvinnans politiska rösträtt, arbetade i årtionden. Efter första världskriget gick det fort: riksdagen beslutade i princip om kvinnlig rösträtt 1918, kvinnor röstade i kommunala val 1919, och 1921 fick de för första gången rösta i riksdagsval. Fem kvinnor valdes in i riksdagen då (de tog plats 1922)."),
  ("tidslinje",[("1866","Tvåkammarriksdag"),("1909","Rösträtt för män"),("1919","Kvinnor röstar i kommunala val"),("1921","Första riksdagsvalet för kvinnor"),("1971","Enkammarriksdag"),("1974","Ny regeringsform (gäller från 1975)"),("1976","Första valet med valålder 18 år; utländska medborgare röstar i kommunala val")]),
  ("p","<strong>Enkammarriksdagen</strong> infördes 1971. Det betyder att man avskaffade första kammaren, så att Sverige fick en enda kammare. Den nya <strong>regeringsformen</strong> från 1974 (gäller från 1975) slog fast att all offentlig makt utgår från folket. Kungen fick därmed ingen politisk makt längre, och valåldern sänktes till 18 år. Utländska medborgare som bott i Sverige en tid fick rösta i kommunal- och regionval från 1976."),
  ("ruta","exempel","Orsak och konsekvens","<strong>Orsak:</strong> folkrörelsernas krav, strejker och industrisamhällets nya klasser. <strong>Händelse:</strong> rösträtten utvidgas 1909–1921. <strong>Konsekvens:</strong> arbetare och kvinnor får inflytande, nya frågor (skola, sjukvård, barnomsorg) hamnar på agendan."),
  ("kolla",["Vad innebär allmän och lika rösträtt?","När fick kvinnor rösta i riksdagsval första gången?","Vad ändrades 1971 och 1974?"]),
 ],
 svar=["Att alla vuxna har en röst vardera.","1921.","1971: första kammaren avskaffades. 1974: en ny regeringsform där kungen förlorade politisk makt."],
))

S.append(dict(id="konflikt", nr="14.4", ikon="🤝", titel="Konflikt och samförstånd: Ådalen och Saltsjöbaden",
 intro="Hur ska arbetsgivare och arbetare lösa sina konflikter? Sverige hittade ett eget svar efter en dyster händelse.",
 block=[
  ("p","Under mellankrigstiden var arbetsmarknaden orolig. Fackföreningar strejkade för bättre löner, och arbetsgivare svarade med lockout (de stängde ute arbetarna) eller hämtade <strong>strejkbrytare</strong>, alltså personer som arbetade trots strejken."),
  ("p","Den <strong>14 maj 1931</strong> hölls en demonstration i Ådalen i Västernorrland, mot att strejkbrytare skulle arbeta på ett sågverk. Militär sattes in för att skydda strejkbrytarna. Soldater öppnade eld mot demonstranterna, och fem människor dog. Händelsen väckte stor ilska och sorg. Det var första gången på länge som militär hade skjutit mot svenska arbetare."),
  ("p","Händelsen gjorde att många politiker insåg att något måste ändras. Efter Ådalen och krisåren fördes samtal mellan arbetarnas fackliga organisation, LO, och arbetsgivarnas organisation, SAF. År <strong>1938</strong> slöt de <strong>Saltsjöbadsavtalet</strong>. Staten hade hotat med lagar om arbetsfreden, och parterna föredrog att lösa saken själva. Det innebar att parterna skulle förhandla och lösa tvister utan inblandning av staten och med regler för strejker och lockouter."),
  ("ruta","fakta","Svenska modellen","Avtalet brukar ses som grunden till ”den svenska modellen”: fack och arbetsgivare reglerar mycket själva genom kollektivavtal. Strejker blev mindre vanliga under många årtionden."),
  ("kalla","Konstruerad källa: en dagbok","”De sa att soldaterna bara skulle skydda arbetsplatsen. Men på kvällen låg människor på marken. Jag förstår inte hur vi kunde bli fiender med våra egna.”","Konstruerad källa baserad på vittnesskildringar från Ådalen 1931."),
  ("p","Många historiker menar att avtalet var resultatet av ett ömsesidigt behov: arbetsgivare ville ha lugn och fackföreningar ville ha inflytande. Andra framhåller att avtalet också kan ses som ett sätt att begränsa arbetarnas handlingsfrihet. Båda tolkningar finns."),
  ("kolla",["Vad hände i Ådalen 1931?","Vad var Saltsjöbadsavtalet?","Varför kan avtalet tolkas på olika sätt?"]),
 ],
 svar=["Militär sköt mot demonstranter vid en strejk, fem människor dog.","Ett avtal 1938 mellan LO och SAF om att förhandla och lösa konflikter själva.","Det gav arbetsro och inflytande, men begränsade också arbetarnas möjlighet att strejka fritt."],
))

S.append(dict(id="folkhem", nr="14.5", ikon="🏠", titel="Folkhemmet och välfärdsreformerna",
 intro="Efter 1930-talet byggde Sverige snabbt ut samhällets stöd. Tanken var att alla skulle ha trygghet, inte bara de rika.",
 block=[
  ("p","Begreppet <strong>folkhemmet</strong> kommer från Per Albin Hansson, socialdemokratisk partiledare och senare statsminister. I ett tal 1928 sa han att samhället skulle vara som ett gott hem där ingen sattes åt sidan. Socialdemokraterna regerade från 1932, och hade mer eller mindre makten oavbrutet fram till 1976."),
  ("p","Landet växte rikt under efterkrigstiden: Sverige hade klarat sig undan kriget och exporterade stål, maskiner och papper. Det gav staten pengar att satsa på reformer. Skatterna höjdes, och samhället tog över uppgifter som tidigare låg på familjen."),
  ("tab",["Reform","År","Vad innebar den?"],[
    ["Folkpension","1913 (kraftigt förbättrad 1948)","Pension till alla äldre"],
    ["Allmänt barnbidrag","1948","Pengar till alla barnfamiljer"],
    ["Allmän sjukförsäkring","1955","Ersättning när man är sjuk"],
    ["ATP (tilläggspension)","1960","Pension kopplad till tidigare lön"],
    ["Nioårig grundskola","Beslut 1962, klart ca 1972","Alla barn går samma skola"],
    ["Föräldraförsäkring","1974","Både mamma och pappa kunde vara hemma med barn"]]),
  ("p","Reformerna byggde på idén om <strong>universell välfärd</strong>: det som gäller ska gälla alla, oavsett inkomst. Fördelen är att systemet får bred uppslutning, vilket gjorde att fler ville betala skatt. Kritiker menade att staten blev för stor eller att människor blev för beroende av den."),
  ("ruta","tank","Mörka sidor av folkhemmet","Folkhemmet innebar också tvång. Mellan 1935 och 1975 steriliserades omkring 63 000 människor, de flesta kvinnor. Många gjordes under tvång eller stark press; en utredning bedömde att några tusen skedde helt utan samtycke och många fler under tryck, till exempel som villkor för att få lämna en institution. Samer, romer och andra minoriteter blev utsatta för assimilering. Att erkänna det mörka gör bilden av folkhemmet mer sann, inte mindre."),
  ("bild","valfard","Efterkrigstidens Sverige byggde ut skolor, bostäder och trygghetssystem."),
  ("kolla",["Vem myntade begreppet folkhemmet?","Nämn tre välfärdsreformer och deras årtal.","Vad innebär universell välfärd?"]),
 ],
 svar=["Per Albin Hansson (talet 1928).","T.ex. barnbidrag 1948, allmän sjukförsäkring 1955, ATP 1960, grundskola 1962, föräldraförsäkring 1974.","Att välfärden gäller alla, oavsett inkomst."],
))

S.append(dict(id="kon", nr="14.6", ikon="⚧️", titel="Kvinnor, kön och sexualitet – nya normer",
 intro="Under 1900-talet förändrades också synen på vad kvinnor och män får och bör göra, och på vem man får älska.",
 block=[
  ("p","Länge hade kvinnor dåliga möjligheter att bestämma över sitt eget liv. Först 1863 blev ogifta kvinnor myndiga, och gifta kvinnor fick en mer jämlik ställning genom giftermålsbalken, som antogs 1920 och började gälla 1921. Under 1900-talet kom kvinnor in i yrkeslivet i allt större antal, särskilt efter andra världskriget när industrin behövde arbetskraft."),
  ("p","På 1960- och 70-talen krävde kvinnorörelsen att kvinnor skulle kunna arbeta på samma villkor som män. Ett viktigt steg var <strong>individuell beskattning</strong>. Tidigare beskattades gifta par gemensamt (sambeskattning), vilket gjorde att kvinnors lön kunde beskattas hårt. Det ändrades 1971. År <strong>1974</strong> infördes <strong>föräldraförsäkringen</strong>, där både pappor och mammor har rätt till betald ledighet. Barnomsorgen byggdes ut, och i början av 1990-talet arbetade omkring 80 procent av kvinnorna i åldern 20–64 år (en stor del på deltid)."),
  ("p","Samtidigt förändrades synen på sexualitet. Homosexualitet var straffbart i Sverige fram till <strong>1944</strong>. Fram till <strong>1979</strong> klassades den dessutom som en sjukdom av Socialstyrelsen, tills människor sjukskrev sig ”friska” i protest. Därefter gick utvecklingen snabbare: <strong>1995</strong> kom registrerat partnerskap för samkönade par och <strong>2009</strong> blev äktenskapet könsneutralt, så att två kvinnor eller två män kan gifta sig."),
  ("tidslinje",[("1863","Ogifta kvinnor myndiga"),("1921","Kvinnor röstar i riksdagsval"),("1944","Homosexualitet inte längre straffbart"),("1971","Individuell beskattning"),("1974","Föräldraförsäkring"),("1979","Homosexualitet avförs som sjukdom"),("1995","Registrerat partnerskap"),("2009","Äktenskap för alla par")]),
  ("ruta","fakta","Fler steg","År 1972 blev Sverige det första landet i världen med en lag om juridiskt könsbyte. Kravet på sterilisering vid sådant byte togs bort 2013. Sexualundervisning blev obligatorisk i skolan 1955."),
  ("ruta","tank","Kontinuitet och förändring","Gör en lista över vad som förändrats för kvinnor sedan 1900 och vad som kan vara sig likt, till exempel löneskillnader och ansvar för barn. Är jämställdhet ”klar”?"),
  ("kolla",["Vad innebär individuell beskattning?","Vad hände med synen på homosexualitet 1944, 1979 och 2009?","Vad är föräldraförsäkring?"]),
 ],
 svar=["Att varje person beskattas för sin egen inkomst, inte tillsammans med maken/makan.","1944: inte längre brott. 1979: avförd som sjukdom. 2009: samma äktenskapsrätt för samkönade par.","Betald ledighet för båda föräldrarna när de får barn."],
))

S.append(dict(id="invandring", nr="14.7", ikon="🌐", titel="Ett Sverige för fler: invandring och minoriteter",
 intro="Sverige har alltid varit ett land där människor kommit och gått. Under 1900-talet vände landet från utvandring till invandring.",
 block=[
  ("p","Från mitten av 1800-talet till 1930 utvandrade över en miljon svenskar, de flesta till Nordamerika. Efter andra världskriget behövde Sveriges växande industri arbetskraft. Man rekryterade människor från Finland, Italien, Grekland och Jugoslavien. Det var <strong>arbetskraftsinvandring</strong>. Sedan 1970-talet har det varit svårare för människor utanför Norden att få arbeta i Sverige, och flyktingar och anhöriga har stått för en stor del av invandringen."),
  ("p","Sverige tog emot flyktingar från Ungern (1956), Tjeckoslovakien (1968), Chile (1973), Iran, Irak och Libanon, forna Jugoslavien (1990-talet) och Syrien. Under 2015 sökte över 160 000 människor asyl. Ungefär var femte person i Sverige är idag född i ett annat land (läget 2024)."),
  ("p","<strong>Nationella minoriteter.</strong> År 2000 erkände Sverige fem nationella minoriteter: samer, tornedalingar, sverigefinnar, romer och judar. <strong>Samerna</strong> är dessutom ett <strong>urfolk</strong>, vilket betyder att de levde i området före dagens stater. Sametinget invigdes 1993."),
  ("p","Minoriteternas historia innehåller orättvisor. Tornedalingar fick länge inte tala finska i skolan. Samer utsattes för tvångsflyttningar och rasbiologiska studier. Romer fick inte resa in i Sverige mellan 1914 och 1954, och judar fick fulla medborgerliga rättigheter först 1870. Idag finns särskilda lagar för minoritetsspråk, och staten har bett om ursäkt för vissa övergrepp."),
  ("ruta","historia","Olika röster","Hur Sverige tog emot nya grupper har diskuterats i hundra år. Vissa har velat begränsa invandringen, andra öppna den. Fundera: hur påverkar det vilka som får berätta Sveriges historia?"),
  ("ruta","fakta","Fem minoritetsspråk","Samiska, finska, meänkieli, romani chib och jiddisch är nationella minoritetsspråk i Sverige."),
  ("kolla",["Varför kom arbetskraftsinvandrare till Sverige efter 1945?","Vilka är Sveriges fem nationella minoriteter?","Vad menas med urfolk?"]),
 ],
 svar=["Industrin behövde arbetskraft och Sverige hade ont om folk.","Samer, tornedalingar, sverigefinnar, romer och judar.","Ett folk som levde i området före dagens stater, t.ex. samerna."],
))

S.append(dict(id="krisen", nr="14.8", ikon="📉", titel="Krisen på 1990-talet och folkhemmet idag",
 intro="Den svenska modellen utmanades av en djup kris. Efter den ändrades mycket i hur välfärden organiseras.",
 block=[
  ("p","I slutet av 1980-talet steg fastighetspriserna snabbt. När bubblan sprack i början av 1990-talet gick flera banker i kris. Arbetslösheten steg från några få procent till omkring 8–10 procent. Hösten 1992 kunde Sverige inte längre försvara kronans fasta värde, och kronan fick flyta fritt."),
  ("p","För att få ordning på statens ekonomi sparade man på bidrag och sjukförsäkring. Samtidigt infördes friskolor och skolpeng (1992), och fler verksamheter lades ut på privata företag. Pensionssystemet byggdes om, med beslut 1994. Många uppskattade friheten, medan andra menade att välfärden försvagades."),
  ("p","Sedan dess har debatten om välfärden handlat om vad staten ska göra och vad individen, marknaden och familjen ska göra. Det är en av de viktigaste frågorna i svensk politik än idag."),
  ("p","<strong>Historiebruk.</strong> Ordet ”folkhemmet” används idag av flera partier. Socialdemokrater kan lyfta det för att visa vad gemensam välfärd kan göra. Andra, till exempel Sverigedemokraterna, har använt ordet för att tala om en gemensam svensk identitet. Kritiker påpekar att folkhemmet var mer komplicerat än så."),
  ("ruta","tank","Fråga till texten","När en politiker säger ”som i folkhemmets dagar”: vilka år tänker personen på? Vilka grupper nämns och vilka glöms bort? Vilket mål har talet?"),
  ("tab",["Aspekt","1950-/60-talet","Idag"],[
    ["Skolsystem","Kommunal grundskola","Kommunala skolor och friskolor"],
    ["Arbetsmarknad","Låg arbetslöshet, industri","Tjänstesamhälle, högre krav på utbildning"],
    ["Befolkning","Mestadels född i Sverige","Cirka var femte född utomlands (läget 2024)"],
    ["Politik","Dominerande ett parti","Åtta partier i riksdagen"]]),
  ("kolla",["Vad hände med kronan 1992?","Vad är historiebruk?","Hur kan ordet folkhemmet användas på olika sätt?"]),
 ],
 svar=["Den lämnades fri att flyta, dvs. värdet bestämdes av marknaden.","Hur historia används i nutiden för att påverka åsikter eller förklara något.","Som exempel på gemensam välfärd (vänster) eller på svensk gemenskap (andra); ibland idealiseras det."],
))

F = []
F.append(dict(id="f1", nr="F1", ikon="🦌", titel="Samerna och Sverige – ett komplext förhållande",
 intro="Samernas historia visar hur ett folk kan påverkas av staters politik, och hur människor kämpar för sina rättigheter.",
 block=[
  ("p","Samerna bor i Sápmi, ett område som sträcker sig över delar av Sverige, Norge, Finland och Ryssland. Länge försörjde de sig genom jakt, fiske och renskötsel. Under 1800- och 1900-talen fick staten allt större kontroll över marken. Gruvor, vattenkraft och skogsbruk tog resurser och betesmark."),
  ("p","Statliga skolor skulle ge samiska barn svenska kunskaper. I nomadskolorna fick barnen lära sig mycket, men språket och kulturen kunde få mindre plats. Under 1900-talets första hälft mätte forskare samers kroppar i ett försök att visa att människor hörde till olika ”raser”. Idag räknas rasbiologi som vetenskapligt felaktig och moraliskt förkastlig."),
  ("p","Efter 1970-talet växte samernas rörelse. Riksdagen erkände samerna som urfolk 1977, och Sametinget öppnade 1993. År 2020 dömde Högsta domstolen i det så kallade Girjas-målet att Girjas sameby, och inte staten, har rätt att upplåta jakt på småvilt och fiske inom sitt område. Frågor om mark, vindkraft och gruvor är fortfarande omstridda. En sanningskommission har granskat samernas historia och lämnade sin slutrapport till regeringen i september 2026."),
  ("ruta","tank","Flera perspektiv","Vissa menar att samerna fått för lite stöd. Andra pekar på att andra aktörer också behöver mark. Vad tror du är viktigast att få med i en rättvis lösning?"),
  ("kolla",["Vad är Sápmi?","Varför är rasbiologi fel idag?","Vad innebär att samer är ett urfolk?"]),
 ],
 svar=["Samernas traditionella område över flera länder i norr.","Den bygger på idén att människor tillhör biologiskt olika ”raser”, vilket forskning visat är fel.","De levde i området före dagens stater och har särskilda rättigheter enligt internationella principer."],
))
F.append(dict(id="f2", nr="F2", ikon="🔎", titel="Ådalen som berättelse – vem berättar?",
 intro="Händelser berättas olika av olika personer. Ådalen är ett bra exempel på hur källor och minne kan vara viktiga.",
 block=[
  ("p","Det finns många slags källor från Ådalen 1931: domstolsprotokoll, tidningsartiklar, brev, fotografier och senare minnesberättelser. Arbetartidningar skildrade händelsen som ett övergrepp mot arbetare. Andra tidningar betonade att militären hade skickats för att upprätthålla ordningen. Båda berättelserna är ofta delvis sanna men väljer olika delar."),
  ("p","Långt senare, 1969, gjorde regissören Bo Widerberg filmen <em>Ådalen 31</em>. Filmen blev en stor framgång. Den bidrog till att många svenskar idag känner till händelsen, men den bygger också på konstnärlig frihet och ska därför inte ses som en dokumentär."),
  ("p","Detta är exempel på <strong>historiebruk</strong>. Ådalen har använts av fackföreningsrörelsen som symbol för arbetarnas kamp, och av andra som en varning för vad som händer när konflikter eskalerar."),
  ("ruta","tank","Fråga","Vad är skillnaden mellan en källa från 1931 och en film från 1969 om samma händelse? Vilken kan du lita mest på för att veta vad som hände, och vilken ger mer information om tiden den gjordes?"),
  ("kolla",["Nämn två typer av källor från Ådalen.","Varför är filmen inte en neutral källa till 1931?","Vad är det för skillnad på tidsnära källor och senare tolkningar?"]),
 ],
 svar=["T.ex. tidningsartikel, domstolsprotokoll, foto, brev.","Den är gjord 1969 med konstnärliga val och speglar sin egen tid.","Tidsnära källor står närmare händelsen; senare tolkningar visar hur tiden efteråt såg på den."],
))
F.append(dict(id="f3", nr="F3", ikon="📜", titel="Rösträttens gränser: vem räknades inte?",
 intro="Även när rösträtten blev ”allmän” fanns det grupper som stod utanför. Att granska sådana gränser är en del av att förstå demokratins historia.",
 block=[
  ("p","Även efter 1909 kunde människor förlora sin rösträtt. Den som fått fattigvård fick inte rösta förrän 1945, och det slog främst mot de fattigaste. Personer som av domstol förklarats omyndiga fick inte rösta förrän 1989, då möjligheten att omyndigförklara vuxna togs bort."),
  ("p","Kvinnor fick, som du läst, rösta i riksdagsval 1921. Därtill fick utländska medborgare som bott i Sverige en tid rösta i kommunala val från 1976, men inte i riksdagsval, eftersom det kräver svenskt medborgarskap. Alltså lever frågan ”vem ska få rösta?” vidare."),
  ("p","Kontinuiteten är att rösträtten har blivit bredare, men i varje tid har det funnits grupper som stängts ute. Förändringen är att vi idag ser sådana gränser som mer problematiska än man gjorde förr."),
  ("tab",["År","Förändring","Vem fick rösträtt?"],[
    ["1866","Tvåkammarriksdag","Män med inkomst/egendom"],
    ["1909","Allmän rösträtt för män","De flesta män över 24 år"],
    ["1921","Kvinnor röstar","De flesta vuxna, inklusive kvinnor (valålder 23)"],
    ["1945","Fattigvårdskravet tas bort","Människor som fått fattigvård"],
    ["1976","Valålder 18; utländska medborgares kommunala rösträtt","Yngre och bosatta utländska medborgare"]]),
  ("kolla",["Vilka kunde förlora rösträtten även efter 1909?","Varför kan ”allmän” rösträtt vara en vilseledande beskrivning?","Vilken ny grupp fick rösta 1976?"]),
 ],
 svar=["Bland andra personer som fått fattigvård (till 1945) och personer som var omyndigförklarade (till 1989).","Eftersom vissa grupper ändå stängdes ute.","18-åringar (valåldern hade sänkts) och utländska medborgare i kommunala val."],
))
F.append(dict(id="f4", nr="F4", ikon="💬", titel="Är folkhemmet ett verktyg eller en verklighet?",
 intro="Historiker och politiker har olika syn på folkhemmet. Är det en beskrivning av en tid, eller ett ideal?",
 block=[
  ("p","Ordet folkhem kommer från ett tal, men det som hände i praktiken var många olika beslut av många olika människor. Därför kan man fråga sig om ”folkhemmet” är en korrekt beskrivning av en epok eller en etikett som har lagts på efteråt."),
  ("p","Forskare som studerat dokument, intervjuer och statistik pekar på stora förbättringar i levnadsstandard, men också att tvångssteriliseringar, assimilering och bostadsbrist fanns. Därför skiljer sig bilderna. Är folkhemmet ett minne av trygghet, eller en berättelse som döljer orättvisor?"),
  ("p","Politiker använder ordet för att väcka känslor: nostalgi, stolthet eller kritik. Som elev kan du ställa frågan: vem använder begreppet, och för vilket syfte?"),
  ("ruta","tank","Övning","Hitta ett citat där en politiker nämner folkhemmet. Skriv vem som sa det, när, och vad personen vill åstadkomma. Jämför med en källa som visar mörkare sidor."),
  ("kolla",["Varför kan folkhemmet ses som både verklighet och etikett?","Nämn en positiv och en negativ del av folkhemmet.","Vad är syftet när politiker nämner folkhemmet?"]),
 ],
 svar=["För att det beskriver verkliga reformer men också är en ensidig bild som formats efteråt.","Positivt: trygghet och bättre levnadsstandard. Negativt: tvångssteriliseringar och assimilering.","T.ex. väcka känslor, skapa trovärdighet eller kritisera nutiden."],
))

UPPG = [
 ("Para ihop","Koppla ihop årtal och händelse.",["1866","1909","1921","1931","1938","1971"],["Saltsjöbadsavtalet","Ådalen","Enkammarriksdag","Kvinnor röstar i riksdagsval","Tvåkammarriksdag","Allmän rösträtt för män"],"1 – E, 2 – F, 3 – D, 4 – B, 5 – A, 6 – C"),
 ("Förklara","Förklara vad en folkrörelse är och ge två exempel. Hur bidrog de till demokratin?",[],None,"Stor förening för gemensam sak, t.ex. nykterhet, arbetare, frikyrkor, kvinnor. De lärde medlemmar demokratiska metoder och drev krav."),
 ("Orsak och konsekvens","Förklara varför rösträtten utvidgades i början av 1900-talet. Ge minst två orsaker och två konsekvenser.",[],None,"Orsaker: folkrörelser, strejker, industrialisering, nya idéer. Konsekvenser: arbetare och kvinnor får inflytande; nya politiska frågor."),
 ("Ådalen","Beskriv vad som hände i Ådalen 1931 och hur det hänger ihop med Saltsjöbadsavtalet 1938.",[],None,"Fem döda när militär sköt mot demonstranter; ökade krav på samförstånd; LO och SAF slöt avtal 1938."),
 ("Tabell","Gör en tabell över tre välfärdsreformer: årtal, vad den innebär, vem som fick nytta.",[],None,"T.ex. barnbidrag 1948, allmän sjukförsäkring 1955, ATP 1960."),
 ("Jämställdhet","Förklara vad som ändrades för kvinnor i yrkeslivet 1950–1990. Nämn minst två reformer.",[],None,"Individuell beskattning 1971, föräldraförsäkring 1974, utbyggd barnomsorg; kvinnors förvärvsarbete ökade."),
 ("Synen på sexualitet","Lägg 1944, 1979, 1995 och 2009 i en tidslinje och förklara vad varje år betyder.",[],None,"1944: homosexualitet inte straffbart. 1979: inte längre klassat som sjukdom. 1995: registrerat partnerskap. 2009: könsneutralt äktenskap."),
 ("Minoriteter","Välj en nationell minoritet och beskriv hur deras situation har förändrats över tid.",[],None,"Elevsvar: samer (urfolk, Sametinget 1993), tornedalingar (finska förbjudet i skolan), romer (inreseförbud 1914–54), judar (medborgarrättigheter 1870), sverigefinnar."),
 ("Källkritik","Läs den konstruerade källan om Ådalen. Vilka frågor ställer du för att bedöma trovärdigheten?",[],None,"Vem skrev, när, för vem, förstahand/andrahand, stämmer med andra källor?"),
 ("Historiebruk","Hur kan begreppet folkhemmet användas på olika sätt av politiker idag? Ge två exempel och diskutera risker.",[],None,"Nostalgi, gemensam välfärd eller identitet; risk att mörka sidor utelämnas."),
]

BEGREPP = [
 ("Stånd","Grupper i det gamla samhället: adel, präster, borgare, bönder."),
 ("Tvåkammarriksdag","Riksdag med två kamrar, 1867–1970."),
 ("Folkrörelse","Stor förening som driver en gemensam sak."),
 ("Allmän rösträtt","Alla vuxna har rätt att rösta."),
 ("Parlamentarism","Regeringen måste ha stöd av riksdagen."),
 ("Strejk","Arbetare lägger ned arbetet i protest."),
 ("Kollektivavtal","Avtal mellan fack och arbetsgivare om villkor."),
 ("Folkhemmet","Idén om samhället som ett gemensamt hem."),
 ("Välfärdsstat","Stat som ger trygghet genom t.ex. sjukvård och pension."),
 ("Universell välfärd","Reformer som gäller alla."),
 ("Jämställdhet","Lika rättigheter, skyldigheter och möjligheter för kvinnor och män."),
 ("Urfolk","Folk som levde i området före dagens stater."),
 ("Nationell minoritet","Grupp med lång historia i landet och särskilda rättigheter."),
 ("Arbetskraftsinvandring","Människor flyttar för att arbeta."),
 ("Historiebruk","Hur historia används i nutiden."),
]

SAMMAN = [
 "Ståndsriksdagen ersattes 1866 av en tvåkammarriksdag (från 1867). Rösträtten var begränsad.",
 "Folkrörelserna – frikyrka, nykterhet, arbetare och kvinnor – tränade människor i demokrati.",
 "Män fick allmän rösträtt 1909, kvinnor 1921. Enkammarriksdag 1971, ny regeringsform 1974 (gäller 1975).",
 "Ådalen 1931 och Saltsjöbadsavtalet 1938 formade ”den svenska modellen”.",
 "Folkhemmet byggde på tidens ekonomiska tillväxt och reformer: barnbidrag, sjukförsäkring, ATP, grundskola, föräldraförsäkring.",
 "Kvinnors yrkesliv och synen på sexualitet förändrades: 1944, 1979, 1995 och 2009 är viktiga årtal.",
 "Sverige gick från utvandring till invandring. Fem nationella minoriteter erkändes 2000; samer är också urfolk.",
 "Krisen på 1990-talet ledde till stora förändringar; folkhemmet används idag i politiken på olika sätt.",
]

TEST_A = [
 ("Vilket år avskaffades ståndsriksdagen?",["1809","1866","1909","1921"],1),
 ("Vilket år fick kvinnor rösta i riksdagsval första gången?",["1909","1919","1921","1971"],2),
 ("Vad hände i Ådalen 1931?",["Soldater sköt mot demonstranter","Muren byggdes","Allmän rösträtt infördes","Ett nytt parti bildades"],0),
 ("Vad innebar Saltsjöbadsavtalet (1938)?",["Att alla strejker förbjöds","Att LO och SAF skulle förhandla utan statens inblandning","Att kvinnor fick rösta","Att sjukförsäkring infördes"],1),
 ("Vem använde begreppet folkhemmet 1928?",["Olof Palme","Hjalmar Branting","Per Albin Hansson","Tage Erlander"],2),
 ("Vilket år infördes föräldraförsäkringen?",["1948","1955","1960","1974"],3),
 ("Vilket år blev äktenskapet könsneutralt i Sverige?",["1944","1979","1995","2009"],3),
 ("Vilka är en del av Sveriges fem nationella minoriteter?",["Danskar","Samer och tornedalingar","Tyskar","Engelsmän"],1),
]
TEST_B = [
 ("Vad är en folkrörelse?","En stor förening där människor går samman för en gemensam sak."),
 ("Varför var folkrörelserna viktiga för demokratin?","De lärde medlemmar demokratiska arbetssätt och pressade makthavare."),
 ("Förklara vad som menas med universell välfärd.","Reformer som gäller alla oavsett inkomst."),
 ("Ge två skäl till att kvinnor kom ut i arbetslivet.","T.ex. industrins behov av arbetskraft, krav från kvinnorörelsen, individuell beskattning, barnomsorg."),
 ("Vad menas med urfolk?","Ett folk som levde i området före dagens stater, t.ex. samerna."),
 ("Ge ett exempel på hur folkhemmet används i debatten idag.","T.ex. som symbol för gemensam välfärd eller svensk identitet."),
]

KALLA = dict(
 text="”Folkhemmets grundval är gemenskapen och samkänslan. I det goda hemmet finns inte privilegierade eller tillbakasatta … Där finns icke den store och den lille …” (fritt återgivet och förkortat, inte ordagrant)",
 ursprung="Per Albin Hansson, tal i riksdagen 1928. Han var då socialdemokratisk partiledare; talet var ett politiskt budskap till både riksdagen och väljare.",
 fragor=[
  ("Vilken bild använder Hansson för att beskriva samhället?","Samhället som ett gott hem, där alla ingår."),
  ("Vem talar och vilket syfte har han?","Per Albin Hansson, partiledare; han vill övertyga väljare om en politik för jämlikhet och gemenskap."),
  ("Vad kan man inte veta bara av talet?","Hur folkhemmet blev i praktiken, och hur alla grupper upplevde det."),
  ("Hur kan talet användas idag (historiebruk)?","Som exempel på ideal om jämlikhet, men också ifrågasättas eftersom verkligheten inte alltid motsvarade ordet.")]
)

SKRIV = dict(
 uppgift="Skriv en text (300–400 ord) med rubriken ”Hur blev Sverige en demokrati?”. Förklara minst tre orsaker (t.ex. folkrörelserna, strejker, industrialiseringen), beskriv rösträttens utveckling med årtal och avsluta med en reflektion om vilka som fortfarande kan känna sig utanför.",
 stod=["E: Du beskriver rösträttens utveckling med några korrekta årtal och nämner minst två orsaker.",
       "C: Du förklarar hur orsakerna hänger ihop, använder begrepp som folkrörelse och allmän rösträtt och ger konkreta exempel.",
       "A: Du väger orsakerna mot varandra, diskuterar kontinuitet och förändring (vem stängdes ute då respektive nu) och visar att tolkningar kan skilja sig."])

LAB = dict(
 titel="Historikerns verkstad: Intervju om förändring",
 syfte="Öva att samla muntliga källor och jämföra med andra källor.",
 material="Intervjufrågor, telefon/penna för anteckningar, tillgång till kapitel 14 och gärna ett foto från hemmet.",
 utforande=["Välj en person över 60 år (släkting eller bekant) som du kan intervjua, med tillåtelse.",
            "Ta fram 6 frågor om förändringar, till exempel: Hur var skolan? Vad gjorde familjen om någon blev sjuk? Vilka jobb fanns? Hur såg man på kvinnor/män som arbetade?",
            "Genomför intervjun och anteckna svaren. Fråga: Hur minns du det?",
            "Jämför svaren med kapitlet: vad stämmer, vad skiljer sig?",
            "Fundera över källkritik: minne är subjektivt. Hur påverkas berättelsen av tiden som gått?",
            "Skriv en sammanfattning (150–200 ord) och redovisa kort."],
 fragor=[("Vilka fördelar har en muntlig källa?","Ger personliga erfarenheter och detaljer som saknas i dokument."),
         ("Vilka risker finns?","Minnet kan förändras, personen kan välja vad som berättas, och berättelsen kan färgas av senare tider."),
         ("Hur kan du kontrollera uppgifterna?","Genom att jämföra med dokument, statistik och andra personer.")],
 bonus="Läraren: Påminn om att intervjuer sker med respekt och samtycke, och att elever inte ska pressa någon att berätta om det som känns obehagligt. Ge alternativ för elever som saknar äldre personer, t.ex. arkivintervjuer eller digitaliserade berättelser. För A-nivå: be eleverna jämföra två intervjuer och formulera hur tolkningarna skiljer sig.",
)

LARAR = [
 ("Koppling till kursplanen (Lgr22, Historia)","Kapitlet täcker centralt innehåll om demokratisering och globalisering ca 1900–nutid: demokratins framväxt, folkrörelser, välfärdsstat, förändrade normer, migration och minoriteter. Det tränar förmågorna att använda begrepp, resonera om orsak/konsekvens och kontinuitet/förändring, granska källor och analysera historiebruk."),
 ("Förslag på upplägg (8 lektioner)","1. Ståndsriksdag till tvåkammarriksdag (14.1). 2. Folkrörelserna (14.2). 3. Kampen om rösträtten (14.3). 4. Ådalen och Saltsjöbaden (14.4). 5. Folkhemmet och välfärd (14.5). 6. Kvinnor, kön och sexualitet (14.6). 7. Invandring och minoriteter (14.7). 8. Krisen och historiebruk (14.8) + labb och prov."),
 ("Vanliga missuppfattningar","Att alla fick rösta 1909 eller att Sverige blev demokratiskt vid ett tillfälle. Att välfärden ”alltid funnits”. Att Ådalen var ett krig. Att folkhemmet var enbart gott. Att invandring är en ny företeelse i Sverige."),
 ("Bedömningsstöd (E/C/A)","E: eleven redogör för händelser och begrepp och nämner några orsaker och konsekvenser. C: eleven förklarar samband, jämför tider och granskar en källa. A: eleven värderar förklaringar, visar att tolkningar skiljer sig åt och analyserar hur historia används i dagens politik."),
 ("Tips till Blooket/Jeopardy","Kategorier: Årtal, Rösträtt, Folkrörelser, Välfärd, Jämställdhet, Minoriteter, Begrepp, Personer, Källkritik, Historiebruk. Exempel: ”Vilket år fick kvinnor rösta i riksdagsval?” (1921); ”Vem talade om folkhemmet?” (Per Albin Hansson)."),
]

KALLOR = [
 ("Skolverket – Kommentarmaterial till kursplanen i historia, grundskolan","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
 ("Sveriges riksdag – Demokratins utveckling i Sverige","https://www.riksdagen.se/sv/sa-fungerar-riksdagen/riksdagens-historia/demokratins-utveckling-i-sverige/"),
 ("Sveriges riksdag – Kampen om rösträtten","https://www.riksdagen.se/sv/sa-fungerar-riksdagen/riksdagens-historia/kampen-om-rostratten/"),
 ("Nordics.info – Sweden's Saltsjöbaden Agreement","https://nordics.info/show/artikel/swedens-saltsjoebaden-agreement"),
 ("Sveriges Radio – Ådalen -31","https://sverigesradio.se/artikel/4503640"),
 ("Regeringen – Chronological overview of LGBT persons' rights in Sweden","https://government.se/articles/2018/07/chronological-overview-of-lgbt-persons-rights-in-sweden"),
 ("Regeringen – Så arbetar Sverige med nationella minoriteter","https://www.regeringen.se/regeringens-politik/nationella-minoriteter-och-minoritetssprak/sa-arbetar-sverige-med-nationella-minoriteter/"),
 ("Sveriges Radio – Kvinnlig rösträtt 90 år","https://sverigesradio.se/artikel/4696249"),
]

F_UPPG = [
 ("●","Förklara varför samer är ett urfolk och nationell minoritet.",[],None,"Urfolk: levde i området före dagens stater; nationell minoritet: erkänd grupp med långvarig historia och särskilda rättigheter."),
 ("●●","Jämför arbetartidningars och regeringsvänliga tidningars beskrivning av Ådalen. Varför skiljer sig de?",[],None,"Olika perspektiv och intressen; olika val av fakta och ord."),
 ("●●","Vilka grupper har stängts ute från rösträtten i olika tider? Vad lär det oss om kontinuitet och förändring?",[],None,"Fattiga, kvinnor, omyndiga, utländska medborgare; rösträtten blir bredare men gränser finns kvar."),
 ("●●●","Diskutera om folkhemmet är ett bra eller dåligt begrepp för att beskriva Sverige 1930–1970. Motivera med flera perspektiv.",[],None,"Elevsvar. A-nivå: nyanserad, flera källor, hänvisar till både reformer och tvång."),
 ("●●●","Jämför synen på sexualitet 1944 respektive 2009. Vad förklarar förändringen?",[],None,"Från straff till samma rättigheter; förklaringar: folkrörelser (RFSL), ändrade värderingar, forskning, lagstiftning."),
]
F_SAMMAN = [
 "Samernas historia visar statens makt, assimilering och krav på rättigheter.",
 "Ådalen berättas olika beroende på källa och syfte.",
 "Rösträttens gränser har flyttats men inte försvunnit.",
 "Folkhemmet är både verklighet och berättelse; fråga alltid vem som använder begreppet.",
]
F_BEGR = [
 ("Sápmi","Samernas traditionella område."),
 ("Assimilering","Att tvinga en grupp att anpassa sig till majoritetens språk och kultur."),
 ("Rasbiologi","Förkastad lära om biologiskt olika ”raser”."),
 ("Sanningskommission","Utredning av historiska orättvisor."),
 ("Strejkbrytare","Person som arbetar trots strejk."),
 ("Kollektivavtal","Avtal om villkor på arbetsplatser."),
]

BLOOKET = [
 ("Vilka fyra stånd fanns i den gamla riksdagen?","Adel, präster, borgare, bönder","Kung, adel, präster, soldater","Adel, bönder, arbetare, köpmän","Präster, bönder, kvinnor, militärer"),
 ("Vilket år avskaffades ståndsriksdagen?","1866","1809","1909","1921"),
 ("Vad är en folkrörelse?","Stor förening för en gemensam sak","Ett politiskt parti med kung","Ett företag","En myndighet"),
 ("Vilken rörelse ville minska alkoholproblem?","Nykterhetsrörelsen","Arbetarrörelsen","Frikyrkorörelsen","Kvinnorörelsen"),
 ("Vilket år fick män allmän rösträtt till andra kammaren?","1909","1866","1921","1971"),
 ("Vilket år fick kvinnor rösta i riksdagsval första gången?","1921","1909","1919","1971"),
 ("Vilket år infördes enkammarriksdagen?","1971","1921","1938","1995"),
 ("Vad hände i Ådalen 1931?","Militär sköt mot demonstranter","Ett kraftverk byggdes","En valdag","Ett sjöslag"),
 ("Vad slöt LO och SAF 1938?","Saltsjöbadsavtalet","Marshallplanen","Folkpensionen","ATP"),
 ("Vem talade om folkhemmet 1928?","Per Albin Hansson","Olof Palme","Tage Erlander","Hjalmar Branting"),
 ("Vilket år infördes allmänt barnbidrag?","1948","1913","1955","1974"),
 ("Vilket år kom allmän sjukförsäkring?","1955","1948","1960","1974"),
 ("Vad står ATP för?","Allmän tilläggspension","Arbete, tid, pension","Allmän trygghetsplan","Arbetarnas tjänstepension"),
 ("När infördes föräldraförsäkringen?","1974","1960","1948","1995"),
 ("Vad betyder universell välfärd?","Gäller alla oavsett inkomst","Gäller bara fattiga","Gäller bara arbetare","Gäller bara barn"),
 ("Vad innebar individuell beskattning (1971)?","Varje person beskattas separat","Familjer beskattas gemensamt","Skatten avskaffades","Barn betalar skatt"),
 ("Vilket år var homosexualitet inte längre straffbart?","1944","1979","1995","2009"),
 ("Vilket år avfördes homosexualitet som sjukdom av Socialstyrelsen?","1979","1944","1995","2009"),
 ("Vilket år infördes registrerat partnerskap?","1995","1979","2009","1944"),
 ("Vilket år blev äktenskapet könsneutralt?","2009","1995","1979","2019"),
 ("Vilken grupp är urfolk i Sverige?","Samerna","Romerna","Judarna","Tornedalingarna"),
 ("Hur många nationella minoriteter har Sverige?","Fem","Tre","Sju","Tolv"),
 ("Vad hände i Sverige 1992 med kronan?","Den fick flyta fritt","Den bytte namn","Den avskaffades","Den fick fast värde"),
 ("Vad kallas det när historia används för att påverka nutiden?","Historiebruk","Källkritik","Parlamentarism","Kronologi"),
 ("Vad menas med arbetskraftsinvandring?","Flytt för att arbeta","Flykt från krig","Turism","Utbytesstudier"),
]

JEOPARDY = {
 "Demokratins väg":[(100,"Vad ersattes 1866?","Vad är ståndsriksdagen?"),(200,"Året män fick allmän rösträtt","Vad är 1909?"),(300,"Året kvinnor röstade i riksdagsval","Vad är 1921?"),(400,"Riksdagen får en enda kammare","Vad är 1971?"),(500,"Begreppet för att regeringen måste ha stöd av riksdagen","Vad är parlamentarism?")],
 "Folkrörelser":[(100,"Rörelse som ville minska alkoholen","Vad är nykterhetsrörelsen?"),(200,"Rörelse som bildade LO 1898","Vad är arbetarrörelsen?"),(300,"Lokal för arbetarrörelsens möten","Vad är Folkets hus?"),(400,"Kvinnornas kamp handlade bland annat om detta","Vad är rösträtt?"),(500,"Varför var folkrörelserna skolor i demokrati?","Vad är: de lärde människor möten, val och organisering?")],
 "Arbetsmarknad":[(100,"Ort där skotten föll 1931","Vad är Ådalen?"),(200,"Antal döda i Ådalen 1931","Vad är fem?"),(300,"Avtal från 1938","Vad är Saltsjöbadsavtalet?"),(400,"Organisationen för arbetare","Vad är LO?"),(500,"Det kallas när fack och arbetsgivare reglerar villkor själva","Vad är den svenska modellen?")],
 "Folkhem & välfärd":[(100,"Mannen bakom folkhemstalet","Vem är Per Albin Hansson?"),(200,"Reform från 1948 för barnfamiljer","Vad är barnbidraget?"),(300,"Pension kopplad till lön, infört 1960","Vad är ATP?"),(400,"Obligatorisk skola för alla, nio år","Vad är grundskolan?"),(500,"Mörk sida av folkhemmet: ingrepp som ofta skedde under tvång eller press","Vad är steriliseringarna?")],
 "Förändring & minoriteter":[(100,"År för äktenskap för alla par","Vad är 2009?"),(200,"Reform 1974 där båda föräldrar får ledighet","Vad är föräldraförsäkringen?"),(300,"Samer är ett sådant folk","Vad är ett urfolk?"),(400,"Antal nationella minoriteter","Vad är fem?"),(500,"Därför är ”folkhemmet” ett exempel på detta","Vad är historiebruk?")],
}

GRUPPER = [
 ("demokratins-vag","Demokratins väg","Från stånd till allmän rösträtt.",["standen","folkrorelser","rostratt"]),
 ("arbete-valfard","Arbete och välfärd","Ådalen, Saltsjöbaden och folkhemmet.",["konflikt","folkhem"]),
 ("normer-minoriteter","Nya normer och ett mångfaldigt Sverige","Kön, sexualitet, invandring och minoriteter.",["kon","invandring"]),
 ("krisen-idag","Kris, förändring och historiebruk","1990-talet och folkhemmet idag.",["krisen"]),
]

SCEN = dict(
 titel="Tidsresa genom Sveriges demokratisering", plats="Sverige", tid="1866–2009",
 sky=("#8fb7d6","#e3edf5"), mark="#7d9a6a", walker=dict(typ="arbetare"),
 etapper=[
  dict(x_etikett="1866", tid="1866", plats="Stockholm", rubrik="Ståndsriksdagen försvinner",
   fakta=["Förr satt Sveriges riksdag i fyra stånd: adel, präster, borgare och bönder. År 1866 ersätts den av två kamrar.","Men bara män med en viss inkomst eller egendom får rösta. Du är arbetare och har inte så mycket pengar, så du får inte rösta."],
   fraga="Vem fick rösta efter reformen 1866?", alt=["Alla vuxna","Män som hade en viss inkomst eller egendom","Bara adeln"], ratt=1,
   forklaring="Rösträtten byggde på hur mycket pengar och egendom man hade.",
   ord=[("rösträtt","rätten att rösta i val")],
   deko=[("riksdagshus",-80,1.3),("slott",180,1.0)]),
  dict(x_etikett="1890-tal", tid="1890-talet", plats="Ett bruk", rubrik="Folkrörelser växer",
   fakta=["Du går med i en fackförening och en studiecirkel. Arbetarrörelsen, nykterhetsrörelsen och frikyrkorna växer.","I föreningarna håller man möten, röstar om beslut och väljer ordförande. Så lär sig vanliga människor hur demokrati fungerar."],
   fraga="Hur hjälpte folkrörelserna demokratin?", alt=["Människor lärde sig att leda möten och rösta","De avskaffade kungen","De bildade den första riksdagen"], ratt=0,
   forklaring="Medlemmarna övade på möten, val och att driva frågor tillsammans.",
   ord=[("folkrörelse","stor förening där vanliga människor arbetar för en sak")],
   deko=[("fabrik",-120,1.2),("folkmassa",100,1.0),("flagga_rod",230,0.9)]),
  dict(x_etikett="1909", tid="1909", plats="Vallokal", rubrik="Allmän rösträtt för män",
   fakta=["År 1909 bestämmer riksdagen att alla män över 24 år ska få rösta i valet till andra kammaren. Det första valet med de nya reglerna hålls 1911.","Nu kan du lägga din röst. Men kvinnor får fortfarande inte rösta."],
   fraga="Vilka fick fortfarande inte rösta efter 1909?", alt=["Kvinnor","Alla män","Alla bönder"], ratt=0,
   forklaring="Kvinnor fick rösta i riksdagsval först 1921.",
   deko=[("valurna",-60,1.3),("folkmassa",140,1.0)]),
  dict(x_etikett="1921", tid="1921", plats="Vallokal", rubrik="Kvinnor röstar",
   fakta=["Nu har kvinnorna kämpat länge för att få rösta. År 1921 får de rösta i val till riksdagen för första gången.","Fem kvinnor blir invalda i riksdagen. Sverige har nu allmän och lika rösträtt för både män och kvinnor."],
   fraga="Vilket år fick kvinnor rösta i riksdagsval för första gången?", alt=["1866","1921","1974"], ratt=1,
   forklaring="År 1921 var första gången kvinnor fick rösta i riksdagsval.",
   deko=[("valurna",-100,1.2),("folkmassa",90,1.1),("riksdagshus",220,0.9)]),
  dict(x_etikett="Ådalen", tid="1931–1938", plats="Ådalen och Saltsjöbaden", rubrik="Konflikt och samförstånd",
   fakta=["År 1931 skjuter soldater fem personer till döds under en demonstration i Ådalen. Striden mellan arbetare och arbetsgivare är hård.","År 1938 skriver facket (LO) och arbetsgivarna (SAF) på Saltsjöbadsavtalet. De lovar att lösa konflikter genom att förhandla själva, utan att staten lägger sig i."],
   fraga="Vad betydde Saltsjöbadsavtalet?", alt=["Arbetare och arbetsgivare skulle förhandla själva","Alla strejker blev förbjudna","Militären skulle skydda alla arbetsplatser"], ratt=0,
   forklaring="Parterna lovade att lösa konflikter med förhandling i stället för strid.",
   ord=[("förhandla","prata och komma överens om ett avtal")],
   deko=[("gruva",-120,1.1),("villa",120,1.2),("folkmassa",250,0.9)]),
  dict(x_etikett="Folkhem", tid="1948–1974", plats="Ett nybyggt bostadsområde", rubrik="Folkhemmet byggs",
   fakta=["Efter kriget bygger Sverige ut välfärden. Det betyder att staten hjälper alla med pengar och trygghet. Barnbidrag och sjukförsäkring kommer, och sedan ATP (tilläggspension) och grundskolan.","År 1974 kommer föräldraförsäkringen. Då kan både mamma och pappa vara hemma med barnet och få pengar från staten."],
   fraga="Vilken reform kom 1974 och lät både mamma och pappa vara hemma med barnet?", alt=["Barnbidrag","Föräldraförsäkring","Grundskola"], ratt=1,
   forklaring="Föräldraförsäkringen 1974 gav båda föräldrarna rätt till betald ledighet.",
   ord=[("välfärd","samhällets stöd så att alla har trygghet, vård och skola"),("folkhemmet","idén om Sverige som ett hem där alla hjälps åt")],
   deko=[("arbetarhus",-100,1.2),("skola",130,1.2),("trad",250,1.0)]),
  dict(x_etikett="Idag", tid="1995–2009", plats="Sverige idag", rubrik="Fler rättigheter, nya frågor",
   fakta=["År 1995 införs registrerat partnerskap för par av samma kön. År 2009 blir äktenskapet könsneutralt, så alla par kan gifta sig.","I dag talas många språk i Sverige, och människor har olika bakgrund. Samerna är Sveriges urfolk."],
   fraga="", alt=[], ratt=0, forklaring="", deko=[("riksdagshus",-100,1.2),("folkmassa",120,1.1),("flagga_bla",240,0.9)]),
 ],
 diskutera="Vilket steg på tidsresan (1866, 1909, 1921, 1938, 1974) tror du betydde mest för vanliga människor? Förklara varför.",
)
