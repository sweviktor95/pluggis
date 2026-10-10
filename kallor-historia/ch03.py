# -*- coding: utf-8 -*-
# Historia kapitel 3: Antikens Grekland (åk 7)
T = dict(
 nr=3, namn="Antikens Grekland", under="Stadsstater, demokrati, filosofi och Alexander den store",
 kort="Historia · Kapitel 3", fil="historia-03-grekland", arskurs=7, nodeid="historia-grekland",
 mal=["beskriva hur Greklands geografi påverkade stadsstaterna",
      "förklara hur demokratin i Athen fungerade och vem som fick rösta",
      "jämföra Athen och Sparta",
      "berätta om grekernas religion, olympiska spelen och teatern",
      "förklara vad filosofer och vetenskapsmän i Grekland bidrog med",
      "beskriva orsaker och konsekvenser av persiska krigen och Peloponnesiska kriget",
      "förklara hur Alexander den store skapade ett stort rike och vad hellenismen var",
      "ge exempel på antikens arv och hur antiken används i vår tid"],
 fundera="Orden demokrati, teater, filosofi och olympisk kommer från Grekland. Vad tror du att de första grekerna menade med demokrati, och vilka tror du fick vara med och bestämma?",
)

S = []

S.append(dict(id="polis", nr="3.1", ikon="🏔️", titel="Ett land av berg, hav och stadsstater",
 intro="Antikens Grekland var inte ett enda land. Det var hundratals små stadsstater som delade språk och kultur men ofta var oense.",
 block=[
  ("p","Grekland är bergigt, med många öar och en lång kust. Bergen gjorde det svårt att resa landvägen, och havet blev i stället en väg mellan byar och städer. Odlingsmarken var begränsad. Därför blev oliver, vin och fiske viktiga, och många greker blev sjöfarare och handlare."),
  ("p","Grekerna levde i <strong>poleis</strong> (en stadsstat kallas <strong>polis</strong>). Varje polis bestod av en stad med omgivande jordbruksland och hade egna lagar, egen armé och ofta egen regering. Athen, Sparta, Korinth och Theben är några kända exempel."),
  ("p","Trots splittringen kände sig grekerna som ett folk. De talade grekiska, dyrkade samma gudar, firade gemensamma fester som de olympiska spelen och kallade sig <em>hellener</em>. Andra folk kallade de <em>barbarer</em>, ett ord som ursprungligen betydde ”den som inte talar grekiska”."),
  ("tidslinje",[("Ca 800–700 f.Kr.","Polis växer fram, grekerna skapar sitt alfabet"),("776 f.Kr.","De första olympiska spelen enligt traditionen"),("Ca 508 f.Kr.","Reformer inför demokrati i Athen"),("490–479 f.Kr.","Persiska krigen"),("431–404 f.Kr.","Peloponnesiska kriget"),("336–323 f.Kr.","Alexander den store"),("323–31 f.Kr.","Hellenistisk tid")]),
  ("p","Grekerna grundade också <strong>kolonier</strong> runt Medelhavet och Svarta havet, i bland annat dagens Italien, Turkiet och Egypten. På så vis spreds språk, handel och idéer. Detta var en orsak till att den grekiska kulturen blev så inflytelserik."),
  ("ruta","tank","Fördelar och nackdelar","Att leva i små självständiga städer gjorde att många olika idéer kunde prövas. Samtidigt gjorde det grekerna svaga mot yttre fiender och ledde till många krig mellan städerna."),
  ("kolla",["Vad är en polis?","Hur påverkade bergen och havet grekernas liv?","Vad förenade grekerna trots att de levde i olika stadsstater?"]),
 ],
 svar=["En stadsstat: en stad med omgivande land och eget styre.","Bergen försvårade resor på land, så havet blev färdväg och många blev sjöfarare och handlare.","Språket, gudarna, gemensamma fester som olympiska spelen och känslan av att vara hellener."],
))

S.append(dict(id="athen", nr="3.2", ikon="🗳️", titel="Athen och demokratin",
 intro="Ordet demokrati kommer från grekiskan och betyder ”folkstyre”. Men vilka räknades egentligen som folket i Athen?",
 block=[
  ("p","Athen styrdes en gång av rika släkter och kungar. Omkring 508 f.Kr. genomförde politikern Kleisthenes reformer som gav medborgarna mer makt. Under de följande hundra åren utvecklades det system vi kallar <strong>direkt demokrati</strong>, där medborgarna själva röstade om besluten istället för att välja representanter."),
  ("tab",["Institution","Vad gjorde den?"],[
    ["Folkförsamlingen (ekklesia)","Alla manliga medborgare kunde komma, tala och rösta. Man möttes på en kulle som heter Pnyx och röstade ofta genom handuppräckning."],
    ["Rådet (boule)","500 medborgare, utsedda genom lottning, förberedde frågorna. De satt ett år."],
    ["Domstolar","Stora jurys av medborgare avgjorde rättsfall. Jurymän lottades."],
    ["Ostrakism","Man kunde rösta bort en person som blivit för mäktig, genom att skriva namnet på en lerskärva. Personen fick lämna staden i tio år."]]),
  ("p","Att välja med <strong>lottning</strong> var tänkt att hindra att enskilda blev för mäktiga. Det innebar också att vanliga medborgare, inte bara rika, kunde få politiska uppgifter."),
  ("ruta","fakta","Vem fick vara med?","Bara <strong>medborgare</strong> hade rösträtt, och medborgare var fria män med athenska föräldrar. Kvinnor, slavar och utlänningar som bodde i Athen (kallade <em>metoiker</em>) var uteslutna. Medborgarna var ungefär 30 000–60 000 människor, alltså bara en liten del av befolkningen, kanske 10–20 procent."),
  ("ruta","tank","Är det demokrati?","Är ett system där de flesta människor saknar rösträtt en demokrati? Jämfört med kungar eller adel var Athen ett stort steg. Jämfört med dagens krav på allmän rösträtt var det mycket begränsat. Båda sakerna kan vara sanna."),
  ("p","Under ledaren Perikles (död 429 f.Kr.) blev Athen rikt och mäktigt. Enligt många historiker användes pengar från förbundet med andra städer för att bygga Parthenon på Akropolis, ett tempel för gudinnan Athena. Demokratin fungerade, men Athen var också en sjömakt som ibland tvingade andra städer att betala."),
  ("kolla",["Vad betyder demokrati?","Vilka grupper hade inte rösträtt i Athen?","Varför använde man lottning?"]),
 ],
 svar=["Folkstyre.","Kvinnor, slavar och utlänningar (metoiker).","För att hindra att enskilda blev för mäktiga och låta vanliga medborgare få uppgifter."],
))

S.append(dict(id="sparta", nr="3.3", ikon="🛡️", titel="Sparta – ett samhälle för krig",
 intro="Sparta var Athens stora motsats. Medan Athen stod för debatt och konst, byggde Sparta hela samhället kring armén.",
 block=[
  ("p","Sparta ligger på halvön Peloponnesos. Spartanerna erövrade grannlandet Messenien och tvingade befolkningen att bli <strong>helotter</strong>, ofria bönder som arbetade på spartanernas jordar. Helotterna var många fler än spartanerna, och därför levde spartanerna med en ständig rädsla för uppror."),
  ("p","Det gjorde att samhället organiserades kring armén. Spartanska pojkar togs från sina familjer vid sju års ålder och uppfostrades i en strikt utbildning, <strong>agoge</strong>. De lärde sig uthållighet, lydnad och strid, men också att läsa och skriva. De vuxna männen åt tillsammans i matlag."),
  ("ruta","fakta","Spartanska kvinnor","Spartanska flickor gick inte i agoge, men de uppfostrades med idrott, musik och utbildning. De hade större frihet än athenska kvinnor och kunde äga mark. Men inte heller de hade politisk makt."),
  ("tab",["","Athen","Sparta"],[
    ["Styre","Demokrati för manliga medborgare","Två kungar, äldste och valda ephorer"],
    ["Ekonomi","Handel, hantverk och sjöfart","Jordbruk med helotter som arbetskraft"],
    ["Ideal","Debatt, konst, filosofi","Disciplin, lydnad, militär styrka"],
    ["Armé","Stark flotta","Stark landarmé"]]),
  ("p","Bilden av Sparta är dock omstridd. Det finns få spartanska källor, för spartanerna skrev lite själva. Mycket vi vet kommer från utomstående, ofta athenare, och från författare som levde långt senare. Bilden kan därför vara överdriven eller förenklad."),
  ("ruta","historia","Sparta i populärkulturen","Filmer och spel framställer ofta spartanerna som hjältar. Fråga då: vem berättar, och vad utelämnas? Helotternas liv och spartanernas rädsla för uppror syns sällan i storfilmer."),
  ("kolla",["Vad var helotter?","Vad var agoge?","Varför ska man vara försiktig med bilden av Sparta?"]),
 ],
 svar=["Ofria bönder som arbetade åt spartanerna.","Spartanska pojkars hårda utbildning från sju års ålder.","Få spartanska källor finns, och mycket kommer från utomstående eller från senare författare."],
))

S.append(dict(id="religion", nr="3.4", ikon="⚡", titel="Gudar, spel och teater",
 intro="Religionen fanns överallt i det grekiska livet: i hemmet, på torget och i sporten. Spel och teater var också sätt att hedra gudarna.",
 block=[
  ("p","Grekerna trodde på många gudar, <strong>polyteism</strong>. Zeus var högste gud, Athena gudinna för visdom och krig, Apollon gud för ljus och musik, Poseidon gud över havet. Gudarna liknade människor: de var avundsjuka, kärleksfulla och ibland oresonliga. Man offrade för att få deras hjälp."),
  ("p","Människor frågade också gudarna om råd. Det mest kända <strong>oraklet</strong> låg i Delfi, där en prästinna ansågs förmedla Apollons ord. Svaren var ofta dunkla, så de kunde tolkas på flera sätt."),
  ("ruta","fakta","De olympiska spelen","Spelen hölls vart fjärde år i Olympia till Zeus ära. Enligt traditionen började de 776 f.Kr. Först fanns bara en löptävling, men programmet växte med bland annat brottning, boxning, femkamp och vagnslopp. Under spelen rådde fred så att idrottare och åskådare kunde resa säkert. Bara fria grekiska män fick tävla, och kvinnor fick inte delta. De sista antika spelen hölls enligt traditionen 393 e.Kr."),
  ("bild","grekland","Tempel och offer var en del av vardagen i antikens Grekland."),
  ("p","<strong>Teatern</strong> växte också fram ur religionen, ur fester för guden Dionysos. Man spelade <em>tragedier</em> (allvarliga pjäser) och <em>komedier</em> (roliga pjäser) utomhus i stora teatrar. Skådespelarna bar masker, och alla roller spelades av män. Pjäserna tog upp frågor om rätt och fel, krig och makt."),
  ("ruta","tank","Idrott och religion","Idag ser vi idrott som en tävling. För grekerna var tävlandet också en gudstjänst. Fundera på hur det skulle skilja sig om vi började varje match med ett offer till en gud."),
  ("kolla",["Vem var Zeus?","Hur länge hölls de antika olympiska spelen ungefär?","Vad är skillnaden mellan tragedi och komedi?"]),
 ],
 svar=["Den högste guden i grekernas religion.","Från 776 f.Kr. enligt traditionen till 393 e.Kr., över tusen år.","Tragedi är en allvarlig pjäs, komedi en rolig."],
))

S.append(dict(id="tanke", nr="3.5", ikon="🧠", titel="Filosofer och vetenskap",
 intro="Grekerna ställde frågor om allt: Hur är världen uppbyggd? Hur bör vi leva? Vad är rättvisa? Många av deras frågor ställer vi fortfarande.",
 block=[
  ("p","Ordet <strong>filosofi</strong> betyder ”kärlek till visdom”. De första tänkarna försökte förklara naturen utan att bara hänvisa till gudar. Med tiden ställde man också frågor om människan och samhället."),
  ("tab",["Tänkare","Ca när","Känd för"],[
    ["Sokrates","469–399 f.Kr.","Ställde frågor till människor för att få dem att tänka själva. Dömdes till döden i Athen."],
    ["Platon","Ca 427–347 f.Kr.","Sokrates elev. Skrev samtal om rättvisa och styrelseskick, grundade skolan Akademien."],
    ["Aristoteles","384–322 f.Kr.","Platons elev. Studerade natur, logik och politik. Lärare åt Alexander den store."]]),
  ("p","Sokrates skrev inget själv. Det vi vet om honom kommer från andra, framför allt Platon. Forskare är oense om hur nära Platons Sokrates är den verkliga personen. Det är ett typiskt källkritiskt problem."),
  ("p","<strong>Vetenskap</strong> blomstrade också. Läkaren Hippokrates menade att sjukdomar hade naturliga orsaker. Matematikern Euklides skrev om geometri, och hans verk användes i skolor i över tvåtusen år. Historikerna <strong>Herodotos</strong> och <strong>Tukydides</strong> försökte undersöka det förflutna med frågor och källor, och Herodotos kallas ofta ”historiens fader”."),
  ("ruta","exempel","Att tänka som en filosof","Sokrates metod var att fråga: ”Vad är mod?” När någon svarade ställde han nya frågor tills svaret föll. Prova: fråga en kompis ”Vad är rättvisa?” och ställ en följdfråga till varje svar."),
  ("ruta","tank","Fakta eller idé?","Grekerna hade ofta rätt i sina tankar, men ibland fel. Aristoteles trodde att tunga saker faller snabbare än lätta. Vetenskap handlar om att pröva idéer, och även stora tänkare kan ha fel."),
  ("kolla",["Vad betyder filosofi?","Varför är det svårt att veta vad Sokrates verkligen sa?","Varför kallas Herodotos ”historiens fader”?"]),
 ],
 svar=["Kärlek till visdom.","Han skrev inget själv, och vi känner honom mest genom Platon.","Han undersökte det förflutna med frågor och källor."],
))

S.append(dict(id="krig", nr="3.6", ikon="⚔️", titel="Krig: från Persien till Peloponnesos",
 intro="Greker kunde samarbeta mot en gemensam fiende, men blev också allvarligt oense med varandra. Två krig fick stora följder.",
 block=[
  ("p","<strong>Persiska krigen</strong> (490–479 f.Kr.) var en kamp mellan de grekiska stadsstaterna och det enorma Perserriket. Ett skäl var att greker i dagens Turkiet gjort uppror mot perserna, och att Athen hjälpt dem."),
  ("tidslinje",[("499 f.Kr.","Athen hjälper grekerna i Mindre Asien mot Persien"),("490 f.Kr.","Slaget vid Marathon: Athen vinner"),("480 f.Kr.","Slaget vid Thermopyle (spartanerna under Leonidas) och slaget vid Salamis, där grekernas flotta vinner"),("479 f.Kr.","Slaget vid Plataiai: grekerna vinner på land")]),
  ("p","Greklands seger fick stora följder. Athen bildade en förbundsflotta, <strong>Deliska förbundet</strong>, och blev mäktigast till sjöss. Sparta var rädd för Athens växande makt."),
  ("p","Spänningen ledde till <strong>Peloponnesiska kriget</strong> (431–404 f.Kr.) mellan Athen och Sparta med sina allierade. Historikern Tukydides menade att den djupaste orsaken var att Athens makt växte och att detta skapade rädsla i Sparta. Kriget pågick i nästan trettio år."),
  ("ruta","fakta","Pest i Athen","Under kriget drabbades Athen av en svår farsot, och många dog. Bland offren fanns troligen den store ledaren Perikles (död 429 f.Kr.). Senare förlorade Athen också en stor flotta på Sicilien."),
  ("p","Till slut förlorade Athen år 404 f.Kr. Sparta fick ledande ställning, men dess makt blev inte långvarig. Hela Greklands stadsstater blev försvagade av kriget och av upprepade konflikter, vilket gjorde det lättare för makedonierna i norr att ta över."),
  ("ruta","tank","Orsak och konsekvens","Segern över Persien var en orsak till att Athen blev så mäktigt. Athens makt var en orsak till kriget mot Sparta. Kriget försvagade Grekland, vilket blev en orsak till att Makedonien kunde ta makten. Hitta fler samband!"),
  ("kolla",["Vilket år var slaget vid Marathon?","Vad var Deliska förbundet?","Hur hänger Peloponnesiska kriget ihop med Greklands svaghet?"]),
 ],
 svar=["490 f.Kr.","En förbundsflotta av grekiska städer under Athens ledning.","Kriget försvagade stadsstaterna, så Makedonien kunde ta makten."],
))

S.append(dict(id="alexander", nr="3.7", ikon="👑", titel="Alexander den store och hellenismen",
 intro="Efter århundraden av krig mellan grekiska städer dök en erövrare upp i norr. Han skulle förändra världen, men till ett högt pris.",
 block=[
  ("p","Norr om Grekland låg Makedonien. Kung Filip II tog kontroll över större delen av Grekland. När han dog tog hans son <strong>Alexander</strong> över år 336 f.Kr., ungefär 20 år gammal. Alexander hade bland annat undervisats av Aristoteles."),
  ("p","Alexander besegrade det persiska riket och erövrade Egypten och områden i Asien ända fram till Indusdalen. På bara tretton år byggde han ett rike som sträckte sig från Grekland till Indien. Han dog 323 f.Kr. i Babylon, ännu inte 33 år gammal."),
  ("ruta","tank","Hjälte eller erövrare?","Alexander kallas ”den store” och beundras för sin militära skicklighet. Men hans krig dödade och förslavade många människor, och städer förstördes. Historiker värderar honom olika. Fundera: vem berättar historien om en erövrare, och vem fick aldrig berätta sin?"),
  ("p","Efter hans död delades riket av hans generaler. Det gav tre stora riken: Ptolemaiernas i Egypten, Seleukidernas i Syrien och Persien och Antigoniderna i Makedonien och Grekland. Tiden efter Alexander kallas <strong>hellenismen</strong> (323–31 f.Kr.), eftersom grekisk kultur och språk spreds över stora områden."),
  ("p","Staden <strong>Alexandria</strong> i Egypten blev ett centrum för vetenskap. Där fanns ett berömt bibliotek och forskare som matematikern Euklides arbetade där. Idéer från Grekland, Egypten och Främre Orienten möttes och blandades."),
  ("ruta","fakta","Slutet","Efter slaget vid Actium 31 f.Kr. blev Egypten, det sista stora hellenistiska riket, en romersk provins året därpå. Antiken fortsatte under romarna, som tog över mycket av den grekiska kulturen."),
  ("kolla",["Vem undervisade Alexander?","Vad menas med hellenism?","Varför beskrivs Alexander på olika sätt av olika historiker?"]),
 ],
 svar=["Aristoteles.","Tiden efter Alexander då grekisk kultur och språk spreds över stora områden (ca 323–31 f.Kr.).","Hans erövringar kan ses som både skickliga och våldsamma, och olika historiker väger det olika."],
))

S.append(dict(id="arv", nr="3.8", ikon="🏛️", titel="Antikens arv och historiebruk",
 intro="Vi lever fortfarande med mycket från Grekland. Men antiken används också, ibland på sätt som inte stämmer med historien.",
 block=[
  ("p","<strong>Demokratin</strong> är det mest kända arvet. Dagens demokratier är representativa: vi väljer politiker som beslutar åt oss. De är också mycket bredare, eftersom alla vuxna medborgare har rösträtt. Men idén att folket ska styra kommer från Grekland."),
  ("p","Många svenska ord kommer från grekiskan: <em>demokrati, teater, filosofi, politik, matematik, historia, skola, bibliotek</em>. Grekiska idéer om vetenskap, logik och argumentation har påverkat skola och forskning i över två tusen år."),
  ("ruta","historia","OS och antiken","De moderna olympiska spelen startade i Aten 1896 och hämtade inspiration från antiken. Sverige var värd för spelen 1912 i Stockholm. Fackelstafetten från Olympia verkar urgammal men infördes först inför spelen i Berlin 1936, där Nazitysklands regim ville knyta sig till antikens ideal. Den är ett exempel på historiebruk: ett modernt inslag klätt som tradition, med ett politiskt syfte."),
  ("tab",["Fråga","Antiken","Idag"],[
    ["Vem får rösta?","Fria män med athenska föräldrar","Alla vuxna medborgare (i demokratier)"],
    ["Hur beslutas?","Medborgarna röstar direkt","Valda representanter, ibland folkomröstning"],
    ["Slaveri?","Vanligt","Förbjudet"]]),
  ("p","Politiker hänvisar ibland till Athen för att ge sina idéer tyngd. Reklam använder grekiska gudanamn, och filmer och spel använder antiken som kuliss. Det är historiebruk. Fråga alltid: vad är sant, vad är påhittat, och vem tjänar på den berättelsen?"),
  ("ruta","tank","Kontinuitet och förändring","Kontinuitet: idén om folkstyre, ord, idrottstävlingar, teater. Förändring: rösträtt för alla, slaveriet är förbjudet och kvinnor kan rösta. Det visar att något kan leva vidare utan att vara oförändrat."),
  ("kolla",["Ge två exempel på svenska ord med grekiskt ursprung.","Vad är skillnaden mellan direkt och representativ demokrati?","Ge ett exempel på historiebruk av antiken."]),
 ],
 svar=["T.ex. demokrati, teater, filosofi, politik, matematik, skola, bibliotek.","Direkt: medborgarna röstar själva. Representativ: man väljer politiker som beslutar.","T.ex. fackelstafetten i OS, en film eller reklam som använder antiken."],
))

UPPG = [
 ("Para ihop","Koppla begreppet till förklaringen.",["Polis","Demokrati","Helott","Agoge","Hellenism","Filosofi"],["Spartansk utbildning","Kärlek till visdom","Ofri bonde i Sparta","Stadsstat","Folkstyre","Grekisk kultur som sprids efter Alexander"],"1 – D, 2 – E, 3 – C, 4 – A, 5 – F, 6 – B"),
 ("Sant eller falskt?","Avgör om påståendena stämmer.",["Alla vuxna i Athen hade rösträtt.","Sokrates skrev flera böcker.","Peloponnesiska kriget stod mellan Athen och Sparta.","Alexander den store dog i hög ålder.","Spelen i Olympia hölls för Zeus ära."],None,"Falskt (bara fria manliga medborgare); falskt (han skrev inget); sant; falskt (inte ens 33); sant."),
 ("Tidslinje","Sätt i kronologisk ordning: Alexander dör, Peloponnesiska kriget börjar, Marathon, Kleisthenes reformer, första olympiska spelen.",[],None,"Första olympiska spelen (776), Kleisthenes (ca 508), Marathon (490), Peloponnesiska kriget (431), Alexander dör (323)."),
 ("Jämför","Jämför Athen och Sparta: ge två likheter och två skillnader.",[],None,"Likheter: stadsstater, grekiska, dyrkade samma gudar, slaveri/ofria. Skillnader: demokrati vs kungar och ephorer; handel och flotta vs militär och helotter."),
 ("Förklara","Förklara varför bara en liten del av Athens befolkning kunde rösta.",[],None,"Kvinnor, slavar och metoiker var uteslutna; endast fria män med athenska föräldrar var medborgare."),
 ("Orsak och konsekvens","Beskriv en orsak och en konsekvens till persiska krigen.",[],None,"Orsak: uppror i Mindre Asien där Athen hjälpte grekerna. Konsekvens: Deliska förbundet och Athens uppgång, eller grekisk seger och självförtroende."),
 ("Källkritik","Det mesta vi vet om Sparta kommer från icke-spartaner. Vilka problem kan det ge?",[],None,"Tendens (idealisering eller kritik), beroende (senare författare skriver av tidigare), avstånd i tid."),
 ("Kontinuitet och förändring","Jämför demokratin i Athen med demokratin i Sverige idag. Vad är kontinuitet och vad är förändring?",[],None,"Kontinuitet: folkets inflytande, val och debatt, domstolar. Förändring: representativ demokrati, rösträtt för alla vuxna, inget slaveri."),
 ("Historiebruk","Hitta ett exempel där antiken används i dag (film, spel, OS, reklam, politik). Vad används och varför?",[],None,"Bedöms: konkret exempel, syfte, avsändare och vad som förenklas."),
 ("Kartövning","Rita en enkel karta över Grekland och markera Athen, Sparta, Olympia, Delfi, Marathon, Makedonien och Alexandria.",[],None,"Athen (Attika), Sparta (Peloponnesos), Olympia (västra Peloponnesos), Delfi (norr om Korintiska viken), Marathon (nordost om Athen), Makedonien (norr), Alexandria (Egypten)."),
]

BEGREPP = [
 ("Polis","Grekisk stadsstat."),
 ("Demokrati","Folkstyre."),
 ("Direkt demokrati","Medborgarna röstar själva om besluten."),
 ("Medborgare","Person med politiska rättigheter i staden."),
 ("Metoik","Utlänning som bodde i Athen."),
 ("Ostrakism","Omröstning om att förvisa en person."),
 ("Helott","Ofri bonde i Sparta."),
 ("Agoge","Spartansk uppfostran."),
 ("Polyteism","Tro på flera gudar."),
 ("Orakel","Plats där gudarna sades svara på frågor."),
 ("Tragedi","Allvarlig teaterpjäs."),
 ("Filosofi","Kärlek till visdom; att ställa stora frågor."),
 ("Kolonisation","Att grunda nya städer långt borta."),
 ("Deliska förbundet","Förbund av städer under Athens ledning."),
 ("Hellenism","Tiden efter Alexander, 323–31 f.Kr."),
 ("Barbar","Grekernas ord för den som inte talade grekiska."),
]

SAMMAN = [
 "Greklands berg och hav ledde till många självständiga stadsstater (poleis) som delade språk och religion.",
 "Athen hade direkt demokrati för fria manliga medborgare. Kvinnor, slavar och metoiker var uteslutna.",
 "Sparta byggde sitt samhälle på armén och på helotternas arbete. Bilden av Sparta är omstridd på grund av få källor.",
 "Grekerna hade många gudar, olympiska spelen, orakel och teater som en del av religionen.",
 "Sokrates, Platon och Aristoteles ställde stora frågor. Herodotos och Tukydides skrev historia.",
 "Persiska krigen (490–479 f.Kr.) och Peloponnesiska kriget (431–404 f.Kr.) formade Grekland och försvagade stadsstaterna.",
 "Alexander den store (336–323 f.Kr.) skapade ett stort rike. Hellenismen spred grekisk kultur.",
 "Antikens arv: demokrati, ord, vetenskap. Antiken används också i historiebruk, t.ex. OS.",
]

TEST_A = [
 ("Vad betyder demokrati?",["Folkstyre","Kungastyre","Prästerskap","Militärstyre"],0),
 ("Vilka hade rösträtt i Athen?",["Alla invånare","Fria manliga medborgare","Bara rika män","Alla fria vuxna"],1),
 ("Vad var helotter?",["Spartanska kungar","Ofria bönder i Sparta","Athenska domare","Perser"],1),
 ("Vilken gud var högst bland de grekiska gudarna?",["Apollon","Poseidon","Zeus","Dionysos"],2),
 ("Vad hette filosofen som dömdes till döden i Athen 399 f.Kr.?",["Platon","Aristoteles","Herodotos","Sokrates"],3),
 ("Vilket krig stod mellan Athen och Sparta?",["Persiska krigen","Peloponnesiska kriget","Trojanska kriget","Puniska krigen"],1),
 ("Vad kallas tiden efter Alexander den store?",["Hellenismen","Medeltiden","Upplysningen","Bronsåldern"],0),
 ("Vilket är ett exempel på historiebruk av antiken?",["Att studera en grekisk vas på museum","Att presentera ett modernt inslag, som OS-fackelstafetten, som en urgammal tradition","Att läsa Tukydides","Att räkna årtal"],1),
]
TEST_B = [
 ("Förklara hur Greklands geografi påverkade stadsstaterna.","Bergen skilde områdena åt, så små självständiga städer uppstod. Havet gjorde att grekerna handlade och grundade kolonier."),
 ("Beskriv hur demokratin fungerade i Athen och vem som saknade rösträtt.","Folkförsamlingen röstade direkt, rådet på 500 lottades. Kvinnor, slavar och metoiker saknade rösträtt."),
 ("Ge två skillnader mellan Athen och Sparta.","T.ex. demokrati vs kungar/ephorer; handel och flotta vs militär och helotter; konst och filosofi vs disciplin."),
 ("Varför är det svårt att veta hur Sparta verkligen var?","Spartanerna skrev lite själva, och mycket kommer från utomstående eller senare författare, som kan ha tendens."),
 ("Förklara orsaker till Peloponnesiska kriget.","Athens växande makt skapade rädsla i Sparta; Deliska förbundet mot det Peloponnesiska förbundet; tidigare konflikter."),
 ("Ge ett exempel på kontinuitet och ett på förändring mellan Athen och dagens Sverige.","Kontinuitet: folkstyre, val, rättegångar med jury. Förändring: rösträtt för alla, representativ demokrati, slaveriet förbjudet."),
]

KALLA = dict(
 text="”Vi kallas en demokrati, eftersom makten ligger hos många och inte hos få. Inför lagen är alla lika, men den som kan göra nytta för staden hedras mest.”",
 ursprung="Konstruerad källa baserad på det berömda talet som Tukydides lät Perikles hålla över Athens stupade (ca 431 f.Kr.). Texten är en förenklad egen formulering. Tukydides skrev själv ned talet efteråt och har kanske formulerat det om.",
 fragor=[
  ("Är källan primär- eller sekundär? Motivera.","Delvis primär: skriven av Tukydides, som levde under kriget. Men han skrev ned talet efteråt och sade själv att han återgav innehållet fritt, så det är inte en exakt återgivning."),
  ("Vad vill talaren att åhörarna ska tycka om Athen?","Att Athen är en rättvis, fri demokrati värd att försvara och vara stolt över."),
  ("Vilken tendens kan finnas?","Talet hålls för att hedra de döda och stärka sammanhållningen i krig. Det idealiserar staden och nämner inte kvinnor, slavar eller metoiker."),
  ("Vilka källor skulle behövas för att kontrollera bilden?","Lagtexter, domstolshandlingar, inskrifter och andra författare som visar hur demokratin fungerade i praktiken och vem som stod utanför."),
 ])

SKRIV = dict(
 uppgift="Skriv en text på ca en sida: ”Var Athen en demokrati?” Beskriv hur systemet fungerade, vem som fick vara med och vem som inte fick, jämför med dagens demokrati i Sverige och diskutera hur antiken används idag för att ge idéer tyngd.",
 stod=[
  "E: Eleven beskriver enkelt hur demokratin fungerade och att vissa grupper saknade rösträtt. Eleven gör någon enkel jämförelse med idag.",
  "C: Eleven förklarar institutionerna (folkförsamling, råd, ostrakism, lottning), jämför med dagens Sverige med både kontinuitet och förändring och ger ett exempel på historiebruk.",
  "A: Eleven för ett nyanserat resonemang om vad som är demokrati, väger olika perspektiv (vem som räknades), diskuterar källornas begränsningar och analyserar hur och varför antiken används idag.",
 ])

LAB = dict(
 titel="Historikerns verkstad: Folkförsamling i klassrummet",
 syfte="Eleverna prövar athensk demokrati i praktiken, förstår dess möjligheter och begränsningar och övar att se flera perspektiv.",
 material="Ett fiktivt förslag på tavlan, rollkort (medborgare, kvinna, slav, metoik), lottningslappar, pennor, ev. keramikbitar eller papper till ostrakism.",
 utforande=[
  "Ge varje elev ett slumpmässigt rollkort: ”medborgare”, ”kvinna”, ”slav” eller ”metoik”. Cirka 40 % kan vara medborgare, och resten övriga roller. (I verkligheten var medborgarna en mindre andel.)",
  "Läs upp ett fiktivt förslag, till exempel ”Staden ska bygga ett nytt tempel och ta in mer skatt”.",
  "Lotta fram ett råd på fem personer (bland medborgare). Rådet förbereder frågan.",
  "Folkförsamling: medborgarna debatterar och röstar genom handuppräckning. De övriga får bara titta på.",
  "Byt roller och gör om övningen med ett nytt förslag.",
  "Gör en ostrakism: de som är medborgare skriver ett namn på en lapp. Den med flest röster får lämna debatten en stund (leker bara).",
  "Samtala om hur det kändes att vara utanför och om vad som skiljer Athens demokrati från dagens.",
 ],
 fragor=[
  ("Hur kändes det att inte få rösta?","Eleverna beskriver frustration, och det visar varför rösträtt är viktig."),
  ("Vilka fördelar hade lottning?","Fler fick chansen och ingen kunde köpa sig makt, men det kunde ge mindre erfarna beslutsfattare."),
  ("Vad är skillnaden mot en riksdag?","I Sverige väljer vi representanter. I Athen röstade man direkt, men bara en liten del av befolkningen."),
 ],
 bonus="BONUS för läraren: Koppla till nuet genom att låta eleverna jämföra med elevrådet eller en riktig valsedel. Undvik att peka ut elever som ”slavar” på ett kränkande sätt: använd tydligt lekfulla roller, avsluta med avrollning och reflektion. Diskutera också historiebruk: vem använder Athen som förebild och varför?",
)

LARAR = [
 ("Koppling till Lgr22 (Historia)","Kapitlet täcker centralt innehåll i block 1: Samhällsomvandlingar, med antiken, och tränar syftet om historiska begrepp (polis, demokrati, hellenism), orsaker och konsekvenser, kontinuitet och förändring, källor och källkritik (Sparta, Sokrates, Tukydides) samt historiebruk (OS, antiken i spel och politik). Kunskapskraven: kunskaper om förändringsprocesser, orsaker och konsekvenser, jämförelser och reflektion över hur historia används."),
 ("Förslag på upplägg (8 lektioner)","1. Greklands land och stadsstater (3.1). 2. Athens demokrati och folkförsamlingsövning (3.2, LAB). 3. Sparta och jämförelse med Athen (3.3). 4. Religion, spel och teater (3.4). 5. Filosofer och vetenskap (3.5). 6. Persiska och Peloponnesiska kriget (3.6). 7. Alexander och hellenismen (3.7). 8. Arvet, historiebruk, test och tidsresa (3.8)."),
 ("Vanliga missuppfattningar","”Athen var en demokrati som idag.” Nej, bara en liten del hade rösträtt. ”Grekland var ett land.” Nej, många stadsstater. ”Alla greker var filosofer.” Nej, de flesta var bönder, hantverkare eller slavar. ”Sparta var bara hjältar.” Bilden bygger på få och ibland partiska källor. ”Alexander var bara hjälte.” Hans krig kostade många liv. Elever blandar också ihop kronologin för grekerna och romarna."),
 ("Bedömningsstöd (E/C/A)","<strong>E:</strong> eleven beskriver enkelt hur demokratin fungerade, vilka som saknade rösträtt, ger några skillnader mellan Athen och Sparta och nämner arv från antiken. <strong>C:</strong> eleven förklarar orsaker och konsekvenser av krigen, jämför systematiskt, resonerar om kontinuitet och förändring och ger ett exempel på historiebruk med syfte. <strong>A:</strong> eleven problematiserar begreppet demokrati, väger källor (Tukydides, Platon), resonerar nyanserat om Alexander och analyserar historiebruk av antiken."),
 ("Blooket/Jeopardy: 10 bra kategorier","1. Stadsstater och geografi. 2. Athen och demokrati. 3. Sparta. 4. Gudar och religion. 5. Olympiska spelen. 6. Filosofer. 7. Krig (Persien, Peloponnesos). 8. Alexander och hellenismen. 9. Ord från grekiskan. 10. Historiebruk (OS, film). Exempel: ”Folkstyre” → demokrati; ”Högste gud” → Zeus."),
]

KALLOR = [
 ("Skolverket – Kommentarmaterial till kursplanen i historia (Lgr22)","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
 ("Forum för levande historia – Källkritik och historiebruk (klassrumsmaterial)","https://www.levandehistoria.se/wp-content/uploads/2022/11/kallkritik_historiebruk_och_rasism_-_om_klassrumsmaterialet.pdf"),
 ("World History Encyclopedia – Athenian Democracy","https://worldhistory.org/Athenian_Democracy"),
 ("World History Encyclopedia – Greek World Heritage Sites (Akropolis, Olympia, Delfi)","https://www.worldhistory.org/article/1378/greek-world-heritage-sites/"),
 ("World History Encyclopedia – Greek Olympics","https://worldhistory.org/Greek_Olympics"),
 ("World History Encyclopedia – Persian Wars","https://worldhistory.org/Persian_Wars/"),
 ("Britannica – Peloponnesian War","https://www.britannica.com/print/article/449362"),
 ("World History Encyclopedia – Agoge, the Spartan Education Program","https://www.worldhistory.org/article/342/agoge-the-spartan-education-program/"),
 ("World History Encyclopedia – Socrates","https://www.worldhistory.org/socrates/"),
 ("HISTORY – Hellenistic Greece","https://www.history.com/articles/hellenistic-greece"),
 ("Britannica – Stockholm 1912 (Olympic Games)","https://www.britannica.com/print/article/972252"),
]

F = []
F.append(dict(id="f1", nr="F1", ikon="👥", titel="Vems demokrati? Perspektiv från de utanför",
 intro="Berättelsen om Athens demokrati är ofta fylld av hyllningar. Men hur såg den ut för dem som inte fick rösta?",
 block=[
  ("p","De flesta texter vi har om Athens demokrati är skrivna av välutbildade män. Kvinnor, slavar och metoiker hörs sällan. Det betyder inte att deras liv var oviktigt. Slavar arbetade i hushåll, på åkrar och i gruvor, och mycket av medborgarnas fritid till politik gjordes möjlig av andras arbete."),
  ("p","Kvinnor hade få rättigheter. De ansågs ofta ha sin plats i hemmet, men kvinnor deltog i religiösa fester och kunde äga vissa saker. Metoiker betalade skatt och kunde tjäna i armén, men fick sällan bli medborgare."),
  ("ruta","tank","En demokrati med ofria","Slaveriet innebar att demokratin vilade på ojämlikhet. Är det rimligt att kalla Athen demokratiskt? Historiker svarar olika. Vissa betonar innovationen, andra begränsningarna."),
  ("ruta","fakta","Hur vet vi?","Vi har texter, inskrifter, vaser och ruiner. Men källorna ger främst medborgarnas syn. Därför måste man läsa mellan raderna och fråga vem som saknas."),
  ("kolla",["Varför hörs slavar och kvinnor sällan i källorna?","På vilket sätt vilade demokratin på slavarbete?","Varför svarar historiker olika på om Athen var en demokrati?"]),
 ],
 svar=["De flesta källor skrevs av välutbildade män som hade makt.","Slavarna utförde mycket arbete så att medborgarna fick tid för politik.","De väger innovationen och rösträtten för några mot att många var uteslutna på olika sätt."],
))
F.append(dict(id="f2", nr="F2", ikon="✍️", titel="Herodotos och Tukydides – historieskrivningens början",
 intro="De första som försökte skriva historia med frågor och källor levde i Grekland. Men de gjorde det på olika sätt.",
 block=[
  ("p","<strong>Herodotos</strong> (levde på 400-talet f.Kr.) skrev om persiska krigen. Han reste, intervjuade människor och berättade också legender och sägner. Hans verk kallas på grekiska <em>Historiai</em>, ”undersökningar”. Han nämner ibland flera versioner av en berättelse och låter läsaren bedöma."),
  ("p","<strong>Tukydides</strong> skrev om Peloponnesiska kriget. Han var själv med som general, blev landsförvisad efter ett misslyckat uppdrag och försökte vara mer sparsam med gudar och sagor. Han letade efter orsaker i människors och staters beteende. Han skriver att kriget var ”det mest betydelsefulla fram till dess”."),
  ("tab",["","Herodotos","Tukydides"],[
    ["Ämne","Persiska krigen och mycket mer","Peloponnesiska kriget"],
    ["Stil","Berättande, många sidospår","Torrt, analyserande, fokus på politik och makt"],
    ["Källor","Intervjuer, resor, rykten","Egna iakttagelser, ögonvittnen"],
    ["Problem","Blandar fakta och sägen","Återger tal med egna ord; hade själv en sida"]]),
  ("ruta","tank","Källkritik av källskrivarna","Även de första historikerna hade tendens. Herodotos kom från Halikarnassos i Mindre Asien men levde länge i Athen, och Tukydides var athenare. Läs dem som viktiga källor, men granska dem."),
  ("kolla",["Vad betyder titeln Historiai?","Hur skilde sig Tukydides arbetssätt från Herodotos?","Varför behöver också historikerna själva granskas?"]),
 ],
 svar=["Undersökningar.","Tukydides fokuserade på politik och makt och var mer sparsam med gudar och sägner.","De hade egna åsikter och tendenser."],
))
F.append(dict(id="f3", nr="F3", ikon="⚖️", titel="Rättegången mot Sokrates",
 intro="År 399 f.Kr. dömdes en av historiens mest kända tänkare till döden av en athensk jury. Var det rättvist?",
 block=[
  ("p","Sokrates åtalades för att ha avvisat statens gudar, införa nya gudomligheter och förleda de unga. Åklagarna ville ha dödsstraff. Han valde att försvara sig själv. Mycket av vad vi vet om rättegången kommer från Platon, som skrev <em>Sokrates försvarstal</em>."),
  ("p","Domen avgjordes av en stor jury. Sokrates dömdes och dog genom att dricka gift (odört). Han hade kunnat fly eller be om mildare straff, men gjorde det inte."),
  ("ruta","tank","Varför dömdes han?","Förklaringar: Athen hade nyss förlorat kriget mot Sparta och var orolig. Några som hade umgåtts med Sokrates hade stött en kortvarig diktatur i Athen. Han ifrågasatte människors tro. Kanske kände folk sig hotade. Vi kan inte veta säkert."),
  ("p","Rättegången är ett exempel på demokratins styrka och svaghet. Domen kom från ett folkstyre, men en majoritet kan också döma orättvist. Debatten om yttrandefrihet och minoriteters rättigheter är lika aktuell idag."),
  ("kolla",["Vad anklagades Sokrates för?","Vilken källa har vi främst till rättegången?","Vad visar rättegången om demokratins svagheter?"]),
 ],
 svar=["Att avvisa statens gudar, införa nya och förleda de unga.","Platon, Sokrates elev.","Att en majoritet kan döma orättvist och tysta obekväma röster."],
))
F.append(dict(id="f4", nr="F4", ikon="🔥", titel="Olympiska spelen och historiebruk",
 intro="Dagens OS påminner mycket om de antika spelen. Men många av likheterna är senare påhitt.",
 block=[
  ("p","De moderna spelen startade i Athen 1896. Initiativtagare var fransmannen Pierre de Coubertin, som hämtade idéer från antiken. Namnet och betoningen av fred och fair play är inspirerade av grekerna. De olympiska ringarna är däremot en modern symbol från 1910-talet, och spelen är något nytt."),
  ("tab",["","Antika spel","Moderna spel"],[
    ["Var?","Alltid i Olympia","Olika städer, bland annat Stockholm 1912"],
    ["Vem?","Fria grekiska män","Kvinnor och män från hela världen"],
    ["Religion?","Offer till Zeus","Ingen religiös ceremoni, men symboler"],
    ["Fred?","Helig vapenvila","Fredsbudskap, men politik och konflikter påverkar"]]),
  ("p","Fackelstafetten från Olympia infördes inför spelen 1936. Den ser antik ut men är ingen forntida tradition. Spelen i Berlin användes av nazistregimen för propaganda, och stafetten gav intryck av en koppling till antiken. Här ser du hur det förflutna kan användas för att skapa en bild av en stat."),
  ("ruta","historia","Stockholm 1912","Spelen i Stockholm 1912 pågick från maj till slutet av juli och har kallats ”det svenska mästerverket”. Här användes bland annat elektrisk tidtagning för första gången."),
  ("kolla",["Vad är en skillnad mellan antika och moderna spel?","Vad är fackelstafetten ett exempel på?","Varför kan symboler från antiken vara användbara i propaganda?"]),
 ],
 svar=["T.ex. att kvinnor idag får delta och att spelen flyttar mellan städer.","Historiebruk: ett modernt inslag som ser ut som en gammal tradition.","De ger intryck av ålder, värdighet och legitimitet, så en regim kan binda sig vid ett fint förflutet."],
))

F_UPPG = [
 ("●","Förklara med egna ord varför det är viktigt att fråga vilka röster som saknas i källorna om Athen.",[],None,"Källorna är skrivna av en elit av män, så kvinnor, slavar och metoiker syns lite. Då blir bilden ofullständig."),
 ("●●","Jämför Herodotos och Tukydides som historiker. Vilka styrkor och svagheter har de?",[],None,"Herodotos: bred, intervjuer, men blandar sägner. Tukydides: analyserande och politisk, men använder egna formuleringar och kan ha tendens."),
 ("●●","Diskutera om Sokrates dom var rättvis. Ge argument från båda sidor.",[],None,"För: juryn följde lagen och oron efter kriget. Mot: han dömdes för sina tankar. Eleven bör nämna Platon som källa och dess tendens."),
 ("●●●","Förklara på vilket sätt fackelstafetten är ett exempel på historiebruk, och vem som kan ha haft intresse av den.",[],None,"Den ser antik ut men är modern; arrangörer och regimer kan vilja ge spelen en gammal värdighet och koppla sig till antiken."),
 ("●●●","Argumentera för eller emot påståendet: ”Athen var inte en riktig demokrati.” Använd källor och perspektiv.",[],None,"Argument för: de flesta saknade rösträtt, slaveri. Argument mot: nydanande för sin tid, medborgare styrde direkt. Bedöms efter nyansering."),
]
F_SAMMAN = [
 "Perspektiv: de som inte hade rösträtt syns sällan i källorna.",
 "Herodotos och Tukydides är källor och behöver granskas. De skilde sig i stil och metod.",
 "Sokrates rättegång visar både demokratins styrka och att majoritet kan döma orättvist.",
 "OS är ett exempel på historiebruk: fackelstafetten är modern men ser antik ut.",
]
F_BEGR = [
 ("Metoik","Utlänning med bosättning i Athen."),
 ("Historiai","Herodotos titel, ”undersökningar”."),
 ("Propaganda","Information som används för att påverka åsikter."),
 ("Jury","Grupp personer som dömer i en rättegång."),
 ("Legitimitet","Rätten eller berättigandet att styra."),
 ("Förebild","Något man vill efterlikna."),
]

BLOOKET = [
 ("Vad betyder polis i antikens Grekland?","Stadsstat","Polisman","Gud","Skepp"),
 ("Vad betyder demokrati?","Folkstyre","Kungastyre","Prästvälde","Militärstyre"),
 ("Vilka hade rösträtt i Athen?","Fria manliga medborgare","Alla invånare","Bara rika","Bara soldater"),
 ("Hur många medborgare satt i rådet (boule) i Athen?","500","50","5 000","5"),
 ("Hur utsågs rådet?","Genom lottning","Genom val av kung","Genom arv","Genom krig"),
 ("Vad innebar ostrakism?","Röstning om att förvisa en person","Val av kung","Gudstjänst","Handelsavtal"),
 ("Vilka saknade rösträtt i Athen?","Kvinnor, slavar och metoiker","Alla över 18","Soldater","Präster"),
 ("Vem genomförde demokratiska reformer ca 508 f.Kr.?","Kleisthenes","Perikles","Alexander","Leonidas"),
 ("Vilken gudinna är Athens skyddsgudinna?","Athena","Hera","Artemis","Afrodite"),
 ("Vilket tempel står på Akropolis och hedrar Athena?","Parthenon","Colosseum","Pyramiden","Pantheon"),
 ("Vad kallades spartanernas ofria bönder?","Helotter","Metoiker","Hopliter","Ephorer"),
 ("Vad hette spartanernas hårda utbildning?","Agoge","Boule","Polis","Akademi"),
 ("Vilket krig stod mellan Athen och Sparta?","Peloponnesiska kriget","Persiska krigen","Trojanska kriget","Hundraåriga kriget"),
 ("När började Peloponnesiska kriget?","431 f.Kr.","490 f.Kr.","323 f.Kr.","776 f.Kr."),
 ("Vem var den högste guden?","Zeus","Poseidon","Apollon","Hades"),
 ("Var hölls de antika olympiska spelen?","Olympia","Athen","Sparta","Delfi"),
 ("Vilket år började de första olympiska spelen enligt traditionen?","776 f.Kr.","490 f.Kr.","1896","323 f.Kr."),
 ("Vem fick tävla i de antika spelen?","Fria grekiska män","Alla","Kvinnor","Slavar"),
 ("Var låg det berömda oraklet?","Delfi","Troja","Sparta","Rom"),
 ("Vad menas med tragedi?","Allvarlig teaterpjäs","Rolig teaterpjäs","Dikt","Sport"),
 ("Vem var Sokrates elev?","Platon","Aristoteles","Herodotos","Alexander"),
 ("Vem var Alexander den stores lärare?","Aristoteles","Sokrates","Platon","Tukydides"),
 ("Vem kallas ofta historiens fader?","Herodotos","Platon","Euklides","Perikles"),
 ("Vilken matematiker skrev om geometri och arbetade i Alexandria?","Euklides","Sokrates","Hippokrates","Herodotos"),
 ("Hur gammal var Alexander när han blev kung?","Ungefär 20","Ungefär 50","Ungefär 10","Ungefär 35"),
 ("Vilket år dog Alexander den store?","323 f.Kr.","490 f.Kr.","31 f.Kr.","776 f.Kr."),
 ("Vad kallas tiden efter Alexander (323–31 f.Kr.)?","Hellenismen","Medeltiden","Vikingatiden","Upplysningen"),
 ("Vilket år startade de moderna olympiska spelen?","1896","1912","1936","1776"),
 ("Vilket år hölls OS i Stockholm?","1912","1896","1936","1948"),
]

JEOPARDY = {
 "Athen och demokrati":[(100,"Ordet som betyder folkstyre.","Vad är demokrati?"),(200,"Antalet personer i rådet.","Vad är 500?"),(300,"Gruppen som saknade rösträtt förutom kvinnor och slavar.","Vilka är metoiker?"),(400,"Ledare som byggde Parthenon.","Vem är Perikles?"),(500,"Politikern som genomförde reformer omkring 508 f.Kr.","Vem är Kleisthenes?")],
 "Sparta":[(100,"Spartanernas ofria bönder.","Vad är helotter?"),(200,"Spartansk uppfostran.","Vad är agoge?"),(300,"Spartansk kung som stred vid Thermopyle.","Vem är Leonidas?"),(400,"Därför är vår bild av Sparta osäker.","Vad är få spartanska egna källor?"),(500,"Spartanernas ständiga rädsla.","Vad är uppror bland helotterna?")],
 "Gudar och spel":[(100,"Högste guden.","Vem är Zeus?"),(200,"Platsen för de olympiska spelen.","Vad är Olympia?"),(300,"Året de första spelen enligt traditionen.","Vad är 776 f.Kr.?"),(400,"Platsen med det berömda oraklet.","Vad är Delfi?"),(500,"Fest för Dionysos som blev teater.","Vad är dionysiafesten?")],
 "Tänkare och krig":[(100,"Sokrates elev.","Vem är Platon?"),(200,"Slaget 490 f.Kr.","Vad är Marathon?"),(300,"Förbund som Athen ledde.","Vad är Deliska förbundet?"),(400,"Kriget mellan Athen och Sparta åren 431–404 f.Kr.","Vad är Peloponnesiska kriget?"),(500,"Historikern som beskrev Peloponnesiska kriget.","Vem är Tukydides?")],
 "Alexander och arvet":[(100,"Alexanders hemland.","Vad är Makedonien?"),(200,"Tiden 323–31 f.Kr.","Vad är hellenismen?"),(300,"Staden med ett berömt bibliotek.","Vad är Alexandria?"),(400,"Moderna OS startade här 1896.","Vad är Aten?"),(500,"Tradition från 1936 som ser antik ut.","Vad är fackelstafetten?")],
}

GRUPPER = [
 ("land-och-stat","Land och stadsstater","Greklands geografi och hur grekerna styrde sig.",["polis","athen","sparta"]),
 ("kultur","Gudar, spel och tankar","Religion, spel, teater, filosofi och vetenskap.",["religion","tanke"]),
 ("krig-och-alexander","Krig och Alexander","Persiska krigen, Peloponnesiska kriget och Alexander den store.",["krig","alexander"]),
 ("arvet","Arvet till vår tid","Vad vi ärvt och hur antiken används idag.",["arv"]),
]

SCEN = dict(
 titel="Tidsresa genom antikens Grekland", plats="Olympia, Sparta, Athen och Alexandria", tid="776–323 f.Kr.",
 sky=("#a9d3ea","#f6efd9"), mark="#b9a56c",
 walker=dict(typ="medborgare"),
 etapper=[
  dict(x_etikett="Olympia", tid="776 f.Kr.", plats="Olympia", rubrik="De första spelen",
   fakta=["Du är medborgare och reser till Olympia. Här hålls spelen för att hedra Zeus.","Enligt traditionen var det enda tävlingen den första gången: en löpning."],
   fraga="Till vilken gud hölls de olympiska spelen?", alt=["Zeus","Poseidon","Hades"], ratt=0,
   forklaring="Spelen hölls till Zeus ära i Olympia.", deko=[("tempel_grekiskt",-70,1.3),("folkmassa",120,1.0),("trad",210,0.9)]),
  dict(x_etikett="Sparta", tid="Ca 600 f.Kr.", plats="Sparta", rubrik="Ett samhälle för krig",
   fakta=["I Sparta tränas pojkar från sju års ålder i agoge. Samhället bygger på armén.","Ofria bönder, helotter, arbetar på jordarna."],
   fraga="Vad kallades de ofria bönderna i Sparta?", alt=["Helotter","Metoiker","Hellener"], ratt=0,
   forklaring="Helotter arbetade åt spartanerna.", deko=[("soldat_grupp",-70,1.2),("mur",120,1.0)]),
  dict(x_etikett="Athen", tid="Ca 508 f.Kr.", plats="Athen", rubrik="Folket får makt",
   fakta=["I Athen samlas medborgarna på Pnyx och röstar med handuppräckning.","Kvinnor, slavar och utlänningar får inte vara med."],
   fraga="Vem fick rösta i Athen?", alt=["Alla invånare","Fria manliga medborgare","Bara rika"], ratt=1,
   forklaring="Bara fria manliga medborgare.", deko=[("valurna",-60,1.0),("folkmassa",110,1.1),("tempel_grekiskt",220,1.0)]),
  dict(x_etikett="Salamis", tid="480 f.Kr.", plats="Salamis", rubrik="Slaget till sjöss",
   fakta=["Perserna anfaller Grekland. Vid Salamis besegrar den grekiska flottan perserna.","Slaget är ett av persiska krigens avgörande ögonblick."],
   fraga="Vilken typ av krigsfartyg använde den grekiska flottan?", alt=["Trirem","Karavell","Ångbåt"], ratt=0,
   forklaring="Grekerna använde triremer, krigsfartyg med tre rader åror.", deko=[("trirem",-60,1.3),("hamn",140,1.0),("segelfartyg",230,0.9)]),
  dict(x_etikett="Teater", tid="Ca 430 f.Kr.", plats="Athen", rubrik="Teater och tänkare",
   fakta=["Under Perikles tid byggs Parthenon, och i teatern spelas tragedier och komedier. På torget ställer Sokrates frågor.","Pesten drabbar Athen 430 f.Kr. och kriget mot Sparta har börjat."],
   fraga="Vad ville Sokrates få folk att göra?", alt=["Tänka själva genom frågor","Gå i krig","Betala skatt"], ratt=0,
   forklaring="Sokrates ställde frågor för att få folk att tänka själva.", deko=[("tempel_grekiskt",-80,1.4),("folkmassa",120,1.0),("amfora",220,0.8)]),
  dict(x_etikett="Alexandria", tid="331 f.Kr.", plats="Alexandria", rubrik="Alexanders rike",
   fakta=["Alexander den store har besegrat Persien och grundar staden Alexandria i Egypten.","Efter hans död sprids grekisk kultur i hela det forna riket: hellenismen."],
   fraga="Vad kallas tiden efter Alexander?", alt=["Hellenismen","Antiken","Renässansen"], ratt=0,
   forklaring="Hellenismen är tiden då grekisk kultur spreds över stora områden.", deko=[("hamn",-70,1.1),("bokhylla",100,1.1),("segelfartyg",210,0.9)]),
  dict(x_etikett="Arvet", tid="Idag", plats="Din skola och ditt samhälle", rubrik="Vad lever kvar?",
   fakta=["Du kommer tillbaka till nutiden. Ord som demokrati och teater, och idéer om folkstyre och vetenskap, lever kvar.","Men antiken används också som förebild, i OS och politik. Då behöver du fråga vem som berättar och varför."],
   fraga="", alt=[], ratt=0, forklaring="",
   deko=[("riksdagshus",-80,1.1),("skola",100,1.0),("dator",200,0.8)]),
 ],
 diskutera="Vad i antikens Grekland vill du behålla idag och vad är bra att vi har lämnat bakom oss? Vem berättar historien om antiken, och vad utelämnas?",
)
