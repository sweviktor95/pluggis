# -*- coding: utf-8 -*-
# Kapitel 6 – Upplysning och revolutioner (åk 8). Historia, Pluggis.
T = dict(
 nr=6, namn="Upplysning och revolutioner", under="Tankar som förändrade världen – och människor som kämpade för frihet, jämlikhet och rättigheter",
 kort="Historia · Kapitel 6", fil="historia-06-upplysning-revolutioner", arskurs=8, nodeid="historia-upplysning-revolutioner",
 mal=["beskriva Sveriges väg från stormakt via frihetstid till upplyst envälde",
      "förklara upplysningens grundtankar och några av tänkarna",
      "förklara varför och hur tryckfriheten infördes i Sverige 1766",
      "jämföra den amerikanska och den franska revolutionen",
      "förklara orsaker till och förlopp i franska revolutionen, från 1789 till Napoleon",
      "beskriva liberalism, konservatism, socialism och nationalism",
      "förklara vad som hände 1848 och varför revolutionerna oftast misslyckades",
      "diskutera vems frihet som räknades, och hur revolutionstiden används i dag"],
 fundera="Frihet, jämlikhet och rättigheter låter självklart i dag. Men för 250 år sedan var det revolutionära idéer. Vilka rättigheter tycker du är viktigast, och vem skulle ha fått dem år 1789?",
)

S = []

S.append(dict(id="stormakt", nr="6.1", ikon="👑", titel="Stormakten Sverige och envälde",
 intro="Under 1600-talet var Sverige en av Europas stormakter. Kungen hade stor makt, men efter ett förlorat krig förändrades det.",
 block=[
  ("p","Efter Gustav II Adolfs tid och Trettioåriga kriget blev Sverige en stormakt vid Östersjön. Landet erövrade områden i dagens Finland, Baltikum och norra Tyskland, och 1658 fick det Skåne, Halland och Blekinge av Danmark. Sveriges största utsträckning nåddes kring 1658. Riket hade en stor armé men få invånare och ont om pengar."),
  ("p","Karl XI gjorde sig till <strong>enväldig</strong> kung på 1680-talet. Det betyder att kungen bestämmer och inte behöver dela makten med någon. Hans son <strong>Karl XII</strong> drog ut i stora nordiska kriget 1700. Efter nederlaget vid Poltava 1709 var stormaktens fall nära. Karl XII dog i Norge 1718, och kriget slutade 1721."),
  ("p","Därefter kom <strong>frihetstiden</strong> (1718–1772). Riksdagen med fyra stånd (adel, präster, borgare, bönder) och Riksrådet hade nu stor makt, och kungen lite. Politiska grupper, så kallade <em>hattar</em> och <em>mössor</em>, slogs om makten. Det var en tid med ökad debatt, vetenskap och tryckt text, med män som Carl von Linné."),
  ("p","År 1772 genomförde Gustav III en <strong>statskupp</strong> som flyttade makten tillbaka till kungen. Han kallades en <em>upplyst envåldshärskare</em>: han lät förbjuda tortyr, men begränsade också friheter och 1792 sköts han under en maskeradbal och dog av skadorna. Frågan är hur ett land kan styras: av en kung, av ständerna eller av folket."),
  ("tidslinje",[("1658","Sverige största, får Skåne"),("1709","Nederlag vid Poltava"),("1718","Karl XII dör, frihetstiden börjar"),("1766","Tryckfrihetsförordningen"),("1772","Gustav III:s statskupp"),("1792","Gustav III dör efter attentat")]),
  ("kolla",["Vad betyder envälde?","Vilka var de fyra stånden i riksdagen?","Vad hände 1772?"]),
 ],
 svar=["Att kungen bestämmer och inte delar makten med någon.","Adel, präster, borgare och bönder.","Gustav III genomförde en statskupp och flyttade makten tillbaka till kungen."],
))

S.append(dict(id="upplysning", nr="6.2", ikon="💡", titel="Upplysningen – förnuftets århundrade",
 intro="Under 1600- och 1700-talen växte en ny tankerörelse fram i Europa: <strong>upplysningen</strong>. Den menade att människan kan förstå världen med hjälp av förnuftet och att samhället kan förbättras.",
 block=[
  ("p","Bakgrunden var den <strong>vetenskapliga revolutionen</strong>. Forskare som Newton hade visat att naturen följer lagar. Då började tänkare undra: Finns det lagar för hur samhället bör styras? Borde makt hos kungen och kyrkan prövas med förnuft?"),
  ("tab",["Tänkare","Viktig idé"],[
    ["John Locke (England, 1600-talet)","Alla människor har naturliga rättigheter till liv, frihet och egendom. Om en regering bryter mot dem kan folket byta ut den."],
    ["Montesquieu (Frankrike, 1748)","Makten bör delas i lagstiftande, verkställande och dömande makt, så att ingen blir för mäktig."],
    ["Voltaire (Frankrike)","Kämpade för religiös tolerans, yttrandefrihet och rättvisa domstolar. Kritiserade kyrkans och kungens övergrepp."],
    ["Jean-Jacques Rousseau (Frankrike/Schweiz)","Folket är suverän: makten kommer från folket och staten ska styras efter folkets gemensamma vilja."]]),
  ("p","Tänkarna spred sina idéer i böcker, brev och tidningar. I <strong>salonger</strong> samlades författare, adelsmän och forskare för att diskutera. Stora verk som Diderots och d'Alemberts <em>Encyklopedin</em> samlade kunskap, och kyrkan och kungen försökte ibland förbjuda dem."),
  ("p","Upplysningstänkarna var inte överens om allt, och inte alla tänkte på alla människor. Många menade att kvinnor, slavar och fattiga inte var redo för politisk makt. Men grundidéerna om rättigheter och maktdelning blev vägledande för revolutionerna och för våra moderna demokratier."),
  ("ruta","fakta","Upplysning i Sverige","Linné och Celsius, Chydenius och Gustav III påverkades alla av tiden. Sverige fick tidigt en utvecklad vetenskap och tryckt debatt, och under Gustav III:s tid kom exempelvis ökad religionsfrihet för icke-lutheraner."),
  ("kolla",["Vad var grundtanken i upplysningen?","Vad ville Montesquieu med maktdelning?","Vad menade Locke om naturliga rättigheter?"]),
 ],
 svar=["Att människan kan förstå världen med förnuftet och förbättra samhället.","Att dela makten så att ingen blir för mäktig.","Att alla människor har rättigheter till liv, frihet och egendom som en regering inte får ta ifrån dem."],
))

S.append(dict(id="tryckfrihet", nr="6.3", ikon="📰", titel="Tryckfrihet i Sverige 1766",
 intro="Sverige blev först i världen med en lag om tryckfrihet. Det skedde 1766, mitt i frihetstiden.",
 block=[
  ("p","Tidigare hade staten kontrollerat vad som fick tryckas. Böcker och tidningar kunde bli förbjudna eller bestraffade i efterhand. Under frihetstiden växte tidningar och pamfletter fram. Många ville ha insyn i hur landet styrdes, och i riksdagen stred olika grupper om hur fri pressen skulle få vara."),
  ("p","År <strong>1766</strong> beslutade riksdagen om <strong>tryckfrihetsförordningen</strong>. Enligt Riksarkivet var det världens första. Den gav också medborgare rätt att ta del av allmänna handlingar, vilket är grunden för dagens <strong>offentlighetsprincip</strong>. Prästen och politikern Anders Chydenius, född i Finland, var en av de viktigaste förespråkarna."),
  ("p","Tryckfriheten var inte obegränsad. Vissa frågor, till exempel religion, kunde fortfarande vara känsliga. Efter 1772, när Gustav III tog makten, kringskars friheten igen, bland annat genom en ny förordning 1774. Tryckfriheten ökade och minskade under 1700- och 1800-talen."),
  ("p","Den här lagen är ett exempel på <strong>kontinuitet och förändring</strong>. Idén om att medborgare har rätt att veta och uttrycka sig är stark än i dag, men lagen har ändrats många gånger. Tryckfrihetsförordningen från 1949 är en av Sveriges grundlagar."),
  ("ruta","historia","Världsminne","Den svenska tryckfrihetsförordningen från 1766 utsågs 2023 av UNESCO till ett så kallat världsminne (Memory of the World). Det visar hur historien används: Sverige lyfter fram sitt arv som ett demokratiskt föredöme."),
  ("kolla",["Vilket år kom tryckfrihetsförordningen?","Vad menas med offentlighetsprincipen?","Varför ändrades tryckfriheten efter 1772?"]),
 ],
 svar=["1766.","Att medborgare har rätt att ta del av allmänna handlingar från myndigheter.","Gustav III tog makten med en statskupp och begränsade friheterna."],
))

S.append(dict(id="amerika", nr="6.4", ikon="🗽", titel="Den amerikanska revolutionen",
 intro="Först att omsätta upplysningens idéer i ett nytt statsskick var kolonisterna i Nordamerika. De gjorde uppror mot sitt moderland Storbritannien.",
 block=[
  ("p","De tretton brittiska kolonierna längs Atlantkusten hade vuxit sig stora. Efter krig mot Frankrike ville Storbritannien att kolonierna skulle betala mer skatt. Kolonisterna svarade: <em>no taxation without representation</em>, alltså ingen skatt utan att vi har röst i parlamentet. Protester följde, bland annat Boston Tea Party 1773."),
  ("p","Kriget började 1775. Den <strong>4 juli 1776</strong> antog kolonierna <strong>självständighetsförklaringen</strong>, skriven främst av Thomas Jefferson. Den sade att alla människor är skapade lika, och att de har rätt till liv, frihet och strävan efter lycka. Efter år av krig, med stöd av Frankrike, erkände Storbritannien USA i freden i Paris 1783."),
  ("p","År 1787 skrevs en <strong>konstitution</strong> (grundlag) med maktdelning, vilket påminner om Montesquieu. De första tilläggen, <em>Bill of Rights</em>, kom 1791 och garanterade bland annat yttrande- och religionsfrihet."),
  ("p","Men orden om frihet gällde inte alla. Jefferson ägde själv slavar. Slavar, kvinnor och ursprungsbefolkning fick inte samma rättigheter. Det visar skillnaden mellan idéer och praktik, och många använde senare orden för att kräva sina egna rättigheter."),
  ("ruta","fakta","Svensk koppling","Den svenske greven Axel von Fersen deltog som officer i den franska armén i kriget på amerikansk sida mot britterna. Sverige och USA slöt också ett handels- och vänskapsavtal 1783, ett av USA:s första med en europeisk stat."),
  ("kolla",["Vad menade kolonisterna med ”ingen skatt utan representation”?","Vilket datum är USA:s självständighetsdag?","Vilka fick inte full frihet?"]),
 ],
 svar=["Att de inte ville betala skatt till ett parlament där de inte hade någon röst.","4 juli (1776).","Slavar, kvinnor och ursprungsbefolkningen."],
))

S.append(dict(id="frankrike", nr="6.5", ikon="🏰", titel="Franska revolutionen börjar – 1789",
 intro="Frankrike var ett av Europas folkrikaste länder, med en kung som styrde som envåldshärskare. Under 1789 förändrades landet snabbt.",
 block=[
  ("p","Samhället var uppdelat i tre <strong>stånd</strong>: det första ståndet (prästerna), det andra (adeln) och det tredje (alla andra, en överväldigande majoritet). Det tredje ståndet betalade mest skatt, men hade minst makt. Staten hade stora skulder, bland annat efter stöd till kriget i Amerika. Dessutom blev skörden dålig 1788, och bröd blev dyrt."),
  ("p","Kung Ludvig XVI kallade i maj 1789 till <strong>generalständerna</strong>, ett möte med alla tre stånden. Det tredje ståndet förklarade sig i juni vara landets riktiga representant, en <strong>nationalförsamling</strong>. De svor att inte skiljas åt förrän landet fick en författning."),
  ("p","Den <strong>14 juli 1789</strong> stormade folk i Paris fängelset <em>Bastiljen</em>. Det var en symbol för kungens makt. Fängelset var nästan tomt, men stormningen visade att folket kunde utmana kungen. Under sommaren spreds oro på landsbygden. I augusti avskaffade församlingen adelns privilegier."),
  ("p","Den <strong>26 augusti 1789</strong> antog församlingen <strong>deklarationen om människans och medborgarens rättigheter</strong>. Första artikeln säger ungefär att människor föds och förblir fria och lika i rättigheter. Deklarationen byggde på upplysningen och blev förebild för senare rättighetsdokument, bland annat FN:s förklaring 1948."),
  ("kalla","Konstruerad källa, Paris, sommaren 1789","”Brödet tar det mesta av vad vi tjänar. Vi hör att kungen vill skicka soldater. Är det sant att adeln inte betalar skatt?”","Konstruerad källa i stil med brev från en parisisk hantverkare. Visar rädsla och ilska bland vanliga människor – men är bara en persons ord."),
  ("kolla",["Vilka tre stånd fanns i Frankrike?","Vad var Bastiljen och varför var stormningen viktig?","Nämn två orsaker till revolutionen."]),
 ],
 svar=["Prästerna, adeln och alla övriga (tredje ståndet).","Ett fängelse som symboliserade kungens makt; stormningen visade att folket kunde utmana honom.","T.ex. skulder, dålig skörd och dyrt bröd, orättvist skattesystem, upplysningens idéer."],
))

S.append(dict(id="terror", nr="6.6", ikon="🔪", titel="Republik, skräckvälde och Napoleon",
 intro="Revolutionen blev inte lugn. Under de följande åren radikaliserades den, och slutade med en ny ledare.",
 block=[
  ("p","Kungen försökte fly 1791 men stoppades. År 1792 avskaffades monarkin och Frankrike blev en <strong>republik</strong>. Ludvig XVI dömdes och avrättades i januari 1793. Frankrike befann sig dessutom i krig mot flera europeiska länder som fruktade revolutionen."),
  ("p","Åren 1793–1794 brukar kallas <strong>skräckväldet</strong>. Välfärdsutskottet (Comité de salut public), med Maximilien Robespierre som en av ledarna, lät döma och avrätta människor som sades vara revolutionens fiender, ofta med giljotinen. Officiellt avkunnades omkring 16 600 dödsdomar, och ofta nämns ungefär 17 000 avrättade. Många fler dog i fängelser eller utan rättegång, och siffrorna är osäkra. Till slut vände sig makthavarna mot Robespierre själv, som avrättades i juli 1794."),
  ("p","Landet var splittrat och trött. Generalen <strong>Napoleon Bonaparte</strong> tog makten genom en kupp i november 1799. 1804 kröntes han till kejsare. Han införde en ny lagbok, <em>Code civil</em>, som slog fast likhet inför lagen, men tog också bort många friheter. Hans arméer erövrade stora delar av Europa."),
  ("p","Efter nederlag i Ryssland 1812 och vid Waterloo 1815 föll Napoleon. Stormakterna återställde kungar på Wienkongressen 1814–1815. Svensk koppling: marskalk Jean Baptiste Bernadotte, tidigare Napoleons general, valdes 1810 till svensk tronföljare och blev kung Karl XIV Johan 1818."),
  ("ruta","tank","Revolution som blev diktatur?","Revolutionen började med rättigheter och slutade med en kejsare. Var det oundvikligt? Diskutera hur våld, krig och rädsla kan ändra en revolutions mål."),
  ("kolla",["Vad hände med Ludvig XVI?","Vad kallas åren 1793–1794?","Hur kom Napoleon till makten?"]),
 ],
 svar=["Han dömdes och avrättades i januari 1793.","Skräckväldet.","Genom en kupp i november 1799, och blev kejsare 1804."],
))

S.append(dict(id="ideologier", nr="6.7", ikon="🧭", titel="Nya ideologier",
 intro="Revolutionerna väckte frågan: Hur ska samhället styras? Svaren blev olika <strong>ideologier</strong>, alltså samlade idéer om hur samhället bör se ut.",
 block=[
  ("tab",["Ideologi","Kärnan","Företrädare / exempel"],[
    ["Liberalism","Individens frihet, lagar, äganderätt, fri handel, begränsad statsmakt","Adam Smith, John Stuart Mill"],
    ["Konservatism","Ordning, tradition och försiktig förändring. Revolution leder lätt till kaos","Edmund Burke"],
    ["Socialism","Jämlikhet och gemenskap. Arbetarna bör få del av rikedomen","Robert Owen, senare Karl Marx"],
    ["Nationalism","Folket i en nation hör ihop och bör ha en egen stat","Italien, Tyskland, Polen"]]),
  ("p","<strong>Liberaler</strong> ville ha konstitution, tryckfrihet och fri handel, men inte nödvändigtvis rösträtt åt alla. <strong>Konservativa</strong> var rädda för kaos och ville bevara kyrkan, kungen och ordningen. De <strong>socialistiska</strong> idéerna växte i takt med att industrialiseringen skapade stora klyftor. 1848 gav Marx och Engels ut <em>Kommunistiska manifestet</em>."),
  ("p","<strong>Nationalismen</strong> blev en av århundradets starkaste krafter. I det habsburgska riket och bland tyska och italienska stater ville folk ha egna stater. Nationalism kunde ena, men också utesluta de som inte hörde till nationen."),
  ("ruta","fakta","Höger och vänster","Orden <em>höger</em> och <em>vänster</em> i politiken kommer från nationalförsamlingen 1789. De som ville bevara kungens makt satt till höger om talmannen, och de som ville ha större förändring satt till vänster."),
  ("kolla",["Vad är en ideologi?","Vad är skillnaden mellan liberalism och konservatism?","Varifrån kommer orden höger och vänster i politiken?"]),
 ],
 svar=["Samlade idéer om hur samhället bör se ut och styras.","Liberaler vill ha ökad frihet och förändring; konservativa vill bevara ordning och tradition.","Från hur ledamöterna satt i den franska nationalförsamlingen 1789."],
))

S.append(dict(id="rost", nr="6.8", ikon="🗣️", titel="1848 och vems röst som räknades",
 intro="År 1848 spreds revolutioner över Europa. Frågan om vems frihet som räknades var fortfarande öppen: kvinnor, fattiga och förslavade hade länge stått utanför.",
 block=[
  ("p","I februari 1848 störtades kung Ludvig-Filip i Paris. Frankrike blev republik igen och införde allmän rösträtt för män. Slaveriet i de franska kolonierna avskaffades definitivt. Revolutionen spred sig till bland annat Wien, Berlin, Budapest och italienska stater. Folk krävde konstitutioner, yttrandefrihet och nationella stater."),
  ("p","Revolutionerna misslyckades oftast på kort sikt. Härskarna slog ner dem med arméer, och revolutionärerna var oeniga om målen. I Frankrike valdes Louis-Napoleon, Napoleons brorson, till president och blev kejsare 1852. Ändå var idéerna kvar, och många reformer kom senare. I Sverige ledde oroligheter i Stockholm i mars 1848 (Marsoroligheterna) till att flera dog, men inga stora politiska förändringar följde direkt."),
  ("p","Revolutionstiden hade olika röster. Under franska revolutionen skrev <strong>Olympe de Gouges</strong> 1791 en förklaring om kvinnors rättigheter. Hon avrättades 1793. Kvinnors klubbar förbjöds. I Frankrike fick kvinnor rösta först 1944, i Sverige beslutades det 1919 (första valet 1921)."),
  ("p","Slavar gjorde också revolution. På Saint-Domingue gjorde slavar uppror från 1791 och Haiti blev självständigt 1804. Frankrike avskaffade slaveriet 1794, men Napoleon försökte återinföra det 1802. Det blev definitivt avskaffat först 1848."),
  ("ruta","tank","Kontinuitet och förändring","Revolutionerna ändrade statsskick, lagar och idéer (förändring). Men mycket fanns kvar: ojämlikhet mellan kön och klasser, slaveri och starka stater. Välj en sak och förklara hur stor förändringen egentligen var."),
  ("kolla",["Vad hände i Frankrike i februari 1848?","Varför misslyckades de flesta revolutioner 1848?","Vilka grupper fick inte del av rättigheterna 1789?"]),
 ],
 svar=["Kungen störtades, republik infördes med allmän rösträtt för män.","Härskarna slog ner dem med arméer och revolutionärerna var oeniga.","Kvinnor, slavar och fattiga."],
))

F = []
F.append(dict(id="f1", nr="F1", ikon="🎆", titel="Sidospår: 14 juli och ”frihet, jämlikhet, broderskap” i dag",
 intro="Revolutionen lever kvar i dagens Frankrike och långt utanför. Det är ett exempel på historiebruk.",
 block=[
  ("p","Den 14 juli är Frankrikes nationaldag. Den firas med en militärparad och fyrverkerier. Dagen valdes officiellt 1880 och minns både stormningen av Bastiljen 1789 och en fredlig förbundsfest 1790. Valet visar att man ville komma ihåg enighet, inte bara våld."),
  ("p","Mottot <em>Liberté, égalité, fraternité</em> (frihet, jämlikhet, broderskap) står idag på franska myntet, på offentliga byggnader och i grundlagen. Men alla har inte haft samma tolkning: för vissa är det en beskrivning, för andra ett löfte som ännu inte uppfyllts. Ordet ”broderskap” har kritiserats för att utesluta kvinnor."),
  ("p","Politiska grupper använder revolutionen på olika sätt. Demonstranter kan åberopa 1789 för att kräva rättvisa, medan andra varnar för revolutionens våld. Marseljäsen, nationalsången, skrevs 1792 och har en blodig text som många debatterar."),
  ("ruta","tank","Vem använder historien?","Fråga dig vem som lyfter fram en viss del av revolutionen, vad personen vill uppnå och vad som utelämnas."),
  ("kolla",["Vad firas 14 juli?","Vad betyder Liberté, égalité, fraternité?","Ge ett exempel på olika sätt att använda revolutionen politiskt."]),
 ],
 svar=["Frankrikes nationaldag, till minne av Bastiljen 1789 och förbundsfesten 1790.","Frihet, jämlikhet, broderskap.","T.ex. demonstranter som kräver rättvisa jämfört med dem som varnar för våld."],
))
F.append(dict(id="f2", nr="F2", ikon="❓", titel="Sidospår: Sade Voltaire verkligen det?",
 intro="Det finns ett berömt citat om yttrandefrihet som ofta tillskrivs Voltaire. Men det visar sig att det är en senare formulering.",
 block=[
  ("p","Citatet lyder ungefär: ”Jag ogillar vad du säger, men jag kommer att försvara din rätt att säga det.” Många tror att Voltaire sade det. Men forskare har inte hittat det i hans skrifter. Den brittiska författaren Evelyn Beatrice Hall (som skrev under pseudonymen S. G. Tallentyre) formulerade det 1906 i en bok om honom, för att beskriva hans anda."),
  ("p","Det här är ett bra exempel på <strong>källkritik</strong>. En mening kan sprida sig, bli ett ”berömt citat” och bli sann för många, även om den inte är hans egna ord. Därför ska man fråga: var står det, i vilken källa, och när skrevs det?"),
  ("p","Det betyder inte att citatet är fel i sak. Voltaire stod för tolerans och yttrandefrihet. Men det är viktigt att skilja mellan vad en person faktiskt sa och vad andra senare lagt i munnen på honom."),
  ("kolla",["Vem formulerade citatet första gången, enligt forskare?","Varför är det här ett exempel på källkritik?","Betyder det att citatet är falskt i sak?"]),
 ],
 svar=["Evelyn Beatrice Hall, 1906.","Man måste kontrollera var ett citat kommer ifrån och när det skrevs.","Nej, det speglar Voltaires anda, men orden är inte hans egna."],
))
F.append(dict(id="f3", nr="F3", ikon="⚖️", titel="Sidospår: Upplysningens motsägelser",
 intro="Upplysningstänkare talade om frihet och jämlikhet. Men många av dem accepterade slaveri, och tvivlade på att kvinnor skulle ha politiska rättigheter. Hur går det ihop?",
 block=[
  ("p","Flera upplysningsfilosofer kritiserade slaveriet. Andra levde av det eller teg. Thomas Jefferson skrev att alla är skapade lika, men ägde hundratals slavar. Och Rousseau menade att kvinnor främst hörde hemma i hemmet."),
  ("p","Samtidigt använde just de grupper som uteslöts upplysningens ord. Mary Wollstonecraft skrev 1792 ett försvar för kvinnors rättigheter. Haitis slavar utropade själva sin frihet, och Olaudah Equiano skrev om sitt liv som slav. Ett begrepp som <strong>mänskliga rättigheter</strong> fick bredare innebörd med tiden."),
  ("p","Historiker diskuterar om upplysningens idéer var universella från början eller bara blev det senare. Båda svaren innehåller något sant: idéerna var starka men tillämpades snävt."),
  ("kolla",["Nämn en motsägelse hos Jefferson.","Vem skrev 1792 om kvinnors rättigheter?","Hur kan man tolka att idéerna blev bredare med tiden?"]),
 ],
 svar=["Han skrev att alla är skapade lika men ägde slavar.","Mary Wollstonecraft.","Grupper som uteslutits använde orden för att kräva sina egna rättigheter."],
))

GRUPPER = [
 ("stormakt","Stormakt och upplysning","Sverige från stormakt till upplyst envälde, och upplysningens idéer.",["stormakt","upplysning","tryckfrihet"]),
 ("revolutioner","Två revolutioner","Den amerikanska och den franska revolutionen.",["amerika","frankrike","terror"]),
 ("ideologier","Nya idéer och 1848","Ideologier, revolutionerna 1848 och vems röst som räknades.",["ideologier","rost"]),
]

UPPG = [
 ("Para ihop","Koppla ihop tänkare och idé.",["Locke","Montesquieu","Voltaire","Rousseau","Chydenius","Olympe de Gouges"],["Folket är suverän","Rättigheter för kvinnor 1791","Tolerans och yttrandefrihet","Tryckfrihet i Sverige","Naturliga rättigheter","Maktdelning"],"1 – E, 2 – F, 3 – C, 4 – A, 5 – D, 6 – B"),
 ("Tidslinje","Sätt i rätt ordning: A) Bastiljen stormas, B) Tryckfrihetsförordningen, C) USA:s självständighetsförklaring, D) Napoleon kröns, E) Revolutionerna 1848.",[],None,"B (1766), C (1776), A (1789), D (1804), E (1848)"),
 ("Sant eller falskt?","Avgör och rätta.",["Sverige var först i världen med en tryckfrihetslag.","Franska revolutionen började 1776.","Skräckväldet var 1793–1794.","Napoleon blev kejsare 1804.","Alla människor fick samma rättigheter 1789."],None,"Sant; falskt (1789); sant; sant; falskt (kvinnor, slavar, fattiga uteslöts)"),
 ("Orsak och konsekvens","Svara.",["Nämn tre orsaker till franska revolutionen.","Nämn två konsekvenser av revolutionen.","Hur påverkade upplysningen revolutionerna?"],None,"Skulder, dåligt skördeår, orättvist stånd; republik/deklarationen/Napoleon; idéer om rättigheter och folkstyre gav argument."),
 ("Jämför","Jämför amerikanska och franska revolutionen. Skriv två likheter och två skillnader.",[],None,"Likheter: upplysningsidéer, deklarationer, kriget. Skillnader: USA mot koloniherre, Frankrike mot egen kung; Frankrikes terror och Napoleon."),
 ("Ideologier","Vilken ideologi (liberalism, konservatism, socialism, nationalism) passar: a) ”Bevara ordning och traditioner”, b) ”Arbetarna bör få del av rikedomen”, c) ”Folket i en nation hör ihop”, d) ”Individens frihet och fri handel”.",[],None,"a) konservatism, b) socialism, c) nationalism, d) liberalism"),
 ("Källa","Läs artikel 1 i deklarationen (människor föds fria och lika i rättigheter). Vem tror du den gällde 1789, och vem inte?",[],None,"Gällde främst vita män med äganderätt i praktiken. Kvinnor, slavar och fattiga uteslöts."),
 ("Historiebruk","Förklara varför Frankrike firar 14 juli och hur olika grupper kan använda revolutionen.",[],None,"Nationaldag sedan 1880, minns Bastiljen och förbundsfesten 1790; kan användas för enighet, protester eller varning för våld."),
 ("Skriv","Skriv ett brev från en person i Paris sommaren 1789. Använd minst fem fakta från kapitlet.",[],None,"Bedöms med SKRIV-stödet: korrekta fakta, rätt tidsperspektiv."),
]

BEGREPP = [
 ("Stormakt","Stat som har stor makt över andra."),
 ("Envälde","Kungen styr utan att dela makten."),
 ("Frihetstid","Svensk period 1718–1772 med riksdagens makt."),
 ("Upplysning","Idérörelse som sätter förnuftet och rättigheter i centrum."),
 ("Maktdelning","Att fördela makt på olika organ."),
 ("Tryckfrihet","Rätten att trycka och sprida åsikter."),
 ("Offentlighetsprincipen","Rätten att ta del av allmänna handlingar."),
 ("Konstitution","Grundlag som styr en stat."),
 ("Revolution","Snabb och omfattande förändring av styre eller samhälle."),
 ("Republik","Stat utan kung."),
 ("Ideologi","Samlade idéer om hur samhället bör vara."),
 ("Liberalism","Ideologi som betonar individens frihet."),
 ("Konservatism","Ideologi som vill bevara ordning och tradition."),
 ("Socialism","Ideologi om jämlikhet och gemenskap."),
 ("Nationalism","Idén att folket i en nation bör ha en egen stat."),
]

SAMMAN = [
 "Sverige var stormakt på 1600-talet, hade frihetstid 1718–1772 och därefter Gustav III:s upplysta envälde.",
 "Upplysningen satte förnuft och rättigheter i centrum. Locke, Montesquieu, Voltaire och Rousseau spred idéerna.",
 "Sverige införde världens första tryckfrihetsförordning 1766, grunden för offentlighetsprincipen.",
 "Amerikanska revolutionen (1775–83) gav USA självständighet 1776 och en konstitution.",
 "Franska revolutionen började 1789, med deklarationen om människans och medborgarens rättigheter, republik och skräckvälde.",
 "Napoleon tog makten 1799, blev kejsare 1804 och föll 1815.",
 "Liberalism, konservatism, socialism och nationalism växte fram, och 1848 spreds revolutioner över Europa.",
 "Kvinnor och slavar kämpade för sina rättigheter. Revolutionen firas och debatteras än idag.",
]

TEST_A = [
 ("Vilket år kom Sveriges tryckfrihetsförordning?",["1718","1766","1789","1848"],1),
 ("Vem förespråkade maktdelning?",["Rousseau","Montesquieu","Napoleon","Robespierre"],1),
 ("Vad hände 14 juli 1789?",["Kungen avrättades","Bastiljen stormades","Napoleon kröntes","Waterloo"],1),
 ("Vilket dokument antogs 26 augusti 1789?",["Konstitutionen i USA","Deklarationen om människans och medborgarens rättigheter","Code civil","Tryckfrihetsförordningen"],1),
 ("Vad kallas åren 1793–1794 i Frankrike?",["Frihetstiden","Skräckväldet","Direktoriet","Restaurationen"],1),
 ("Vilket år antogs USA:s självständighetsförklaring?",["1776","1789","1791","1804"],0),
 ("Vilken ideologi betonar ordning och tradition?",["Liberalism","Konservatism","Socialism","Anarkism"],1),
 ("Vad hände i Europa 1848?",["Revolutioner spreds i många länder","Ett världskrig började","Napoleon blev kejsare","Tryckfriheten infördes i Sverige"],0),
]

TEST_B = [
 ("Förklara kort vad upplysningen var.","En idérörelse på 1600- och 1700-talen som menade att människan kan förstå och förbättra världen med förnuftet och att alla har rättigheter."),
 ("Nämn två orsaker till franska revolutionen.","T.ex. statsskulder, dyrt bröd efter dålig skörd, orättvist ståndssamhälle, upplysningens idéer."),
 ("Vad innebar tryckfrihetsförordningen 1766?","Lag om tryckfrihet och rätt att ta del av allmänna handlingar – grund för offentlighetsprincipen."),
 ("Ge ett exempel på en grupp som inte fick del av rättigheterna 1789.","Kvinnor, slavar, fattiga."),
 ("Förklara vad socialism innebär.","Ideologi om jämlikhet och gemenskap där arbetarna bör få del av rikedomen."),
 ("Ge ett exempel på historiebruk av franska revolutionen.","Nationaldagen 14 juli, mottot frihet–jämlikhet–broderskap, politiska demonstrationer."),
]

KALLA = dict(
 text="”Nationalförsamlingen erkänner och förklarar att människor föds och förblir fria och lika i rättigheter. Samhälleliga skillnader får bara grundas på det allmännas nytta.”",
 ursprung="Fritt återgiven på svenska efter artikel 1 i Deklarationen om människans och medborgarens rättigheter, Frankrike, 26 augusti 1789. Primärkälla skriven av nationalförsamlingen, en grupp män, för att visa revolutionens mål.",
 fragor=[
  ("Vem skrev texten och i vilket syfte?","Nationalförsamlingen, en grupp män i Frankrike 1789, för att slå fast revolutionens principer."),
  ("Vilka tankar från upplysningen känner du igen?","Naturliga rättigheter (Locke), folkets suveränitet (Rousseau)."),
  ("Vilka grupper nämns inte uttryckligen, och varför kan det vara viktigt?","Kvinnor och slavar; deras rättigheter diskuterades men blev inte inkluderade, vilket visar skillnad mellan ord och praktik."),
  ("Hur har texten använts senare?","Som förebild för FN:s allmänna förklaring 1948 och i krav från grupper som uteslutits."),
 ])

SKRIV = dict(
 uppgift="Varför blev franska revolutionen så våldsam och varför slutade den med en kejsare? Skriv 250–350 ord. Förklara orsaker, vändpunkter och konsekvenser, och resonera om vad som förändrades och vad som fanns kvar. Avsluta med hur revolutionen används eller minns idag.",
 stod=[
  "E: Du beskriver förloppet (1789, republik, skräckvälde, Napoleon) och nämner några orsaker och konsekvenser.",
  "C: Du förklarar hur kriget, rädslan och striderna mellan grupper bidrog till radikalisering, och drar slutsatser om förändring och kontinuitet. Du ger exempel på historiebruk.",
  "A: Du värderar orsakernas vikt, visar att historiker tolkar förloppet olika, ställer revolutionens ideal mot dess praktik (till exempel kvinnor och slavar) och använder begrepp säkert.",
 ])

LAB = dict(
 titel="Historikerns verkstad: Rollspel – generalständerna 1789",
 syfte="Förstå olika gruppers intressen och förklara varför det var svårt att enas, samt öva att argumentera utifrån en roll.",
 material="Rollkort (präst, adelsman, borgare, bonde, kvinna från Paris). Kort text om skatter och brödpris. Papper och penna.",
 utforande=[
  "Läraren förklarar situationen: kungen har kallat till möte och ska fråga ständerna om skatter.",
  "Varje elev får en roll och skriver två krav och ett argument.",
  "Gruppen spelar mötet: Varje roll talar i en minut. Ledaren frågar: Ska varje stånd ha en röst, eller ska varje person ha en röst?",
  "Klassen röstar om förslaget. Diskutera: vem tjänar på ett visst sätt att rösta?",
  "Skriv en kort text om varför mötet misslyckades och vad som hände sedan.",
 ],
 fragor=[
  ("Varför ville det tredje ståndet rösta per person?","De var överlägset flest, så de skulle få mest inflytande."),
  ("Varför ville adeln och prästerna rösta per stånd?","De hade då två av tre röster och kunde bevara sina privilegier."),
  ("Vilka grupper hade ingen röst alls?","Kvinnor och slavar."),
 ],
 bonus="BONUS för läraren: Koppla till kunskapskraven om orsak–konsekvens och perspektiv. Be eleverna jämföra med svenska riksdagens fyra stånd 1700-talet. Variera: låt en elev spela Olympe de Gouges och kräva rättigheter för kvinnor, för att diskutera vems röst som hörs.",
)

LARAR = [
 ("Koppling till kursplanen (Lgr22, Historia)","Kapitlet täcker syftet att kunna använda historiska begrepp, analysera orsak–konsekvens och kontinuitet–förändring, värdera källor och förstå historiebruk. I centralt innehåll berörs ”revolutioner och framväxten av nya idéer, samhällsklasser och politiska ideologier” (med upplysningen som bakgrund) samt europeisk nationalism och framväxten av olika former av demokrati. Svensk koppling: stormaktstid, frihetstid, tryckfrihet 1766, Gustav III, Bernadotte."),
 ("Förslag på upplägg (8 lektioner)","1. Stormakt och envälde (6.1). 2. Upplysning (6.2). 3. Tryckfriheten (6.3). 4. Amerikanska revolutionen (6.4). 5. Franska revolutionen 1789 (6.5). 6. Terror och Napoleon (6.6). 7. Ideologier och 1848 (6.7–6.8). 8. Historiebruk, rollspel och test. Scenen om Paris 1789 passar som repetition."),
 ("Vanliga missuppfattningar","Att revolutionen skedde över en natt; att Bastiljen var fullt av fångar; att ”alla” fick rättigheter 1789; att Voltaire sade citatet om yttrandefrihet; att Napoleon var kung och inte kejsare; att liberalism betyder vänster. Förklara också att ideologierna förändras över tid."),
 ("Bedömningsstöd","E: eleven redogör för förlopp och några orsaker/konsekvenser och förklarar enkla begrepp. C: eleven förklarar samband, jämför revolutionerna och ger exempel på kontinuitet och förändring samt historiebruk. A: eleven värderar tolkningar, resonerar om motsägelser (rättigheter för vissa) och diskuterar hur historia används och varför."),
 ("Tips: Blooket och Jeopardy – 10 kategorier","1. Stormakt. 2. Frihetstid. 3. Tänkare. 4. Tryckfrihet. 5. USA. 6. Frankrike 1789. 7. Skräckvälde och Napoleon. 8. Ideologier. 9. 1848. 10. Historiebruk. Exempel: ”Vilket land fick världens första tryckfrihetsförordning 1766? – Sverige”."),
]

KALLOR = [
 ("Riksarkivet – Tryckfrihet och censur (tryckfrihetsförordningen 1766, världens första, offentlighetsprincipen)","https://riksarkivet.se/utforska-och-bestall/utbildning-och-studier/tryckfrihet-och-censur"),
 ("Regeringen – UNESCO utser tryckfrihetsförordningen till världsminne (pressmeddelande 2023)","https://www.regeringen.se/pressmeddelanden/2023/05/unesco-utser-tryckfrihetsforordningen-till-varldsminne2/"),
 ("Sveriges riksdag – Från ting och ständer till dagens riksdag (frihetstiden, fyra stånd, 1766 och 1772)","https://www.riksdagen.se/en/how-the-riksdag-works/the-history-of-the-riksdag/from-things-and-assemblies-to-the-riksdag-of-today/"),
 ("Encyclopaedia Britannica – Reign of Terror (1793–1794)","https://www.britannica.com/event/Reign-of-Terror"),
 ("Encyclopaedia Britannica – French Revolution (översikt och fakta)","https://www.britannica.com/facts/French-Revolution"),
 ("Encyclopaedia Britannica – Declaration of Independence (USA, 1776)","https://www.britannica.com/topic/Declaration-of-Independence"),
 ("Nationalencyklopedin – upplysningen","https://www.ne.se/uppslagsverk/encyklopedi/l%C3%A5ng/upplysningen"),
 ("Avalon Project, Yale – Déclaration des droits de l'homme et du citoyen 1789 (primärkälla i översättning)","https://avalon.law.yale.edu/18th_century/rightsof.asp"),
 ("Skolverket – Kommentarmaterial till kursplanen i historia, grundskolan (Lgr22)","https://www.skolverket.se/download/18.68c99c081804c5929ea1376/1652438374459/pdf9789.pdf"),
]

F_UPPG = [
 ("●","Förklara varför citatet ”Jag ogillar vad du säger…” inte kan användas som bevis för vad Voltaire sade.",[],None,"Forskare har inte hittat det i hans skrifter; Hall formulerade det 1906."),
 ("●●","Jämför hur olika grupper kan använda 14 juli eller mottot frihet–jämlikhet–broderskap idag.",[],None,"Exempel: staten som enighet, demonstranter som krav på rättvisa, kritiker som varnar för våld eller menar att kvinnor uteslöts."),
 ("●●","Välj en upplysningstänkare och förklara en motsägelse mellan hans idéer och praktik.",[],None,"Exempel: Jefferson som skrev om lika människor men ägde slavar; Rousseau om folkvilja men kvinnor hemma."),
 ("●●●","Diskutera om franska revolutionen var ett steg framåt eller bakåt för mänskliga rättigheter. Ge argument för båda.",[],None,"Framåt: deklarationen, avskaffade privilegier. Bakåt: skräckvälde, Napoleon. Ett bra svar väger kort och lång sikt."),
 ("●●●","Förklara hur man kan se tryckfrihetsförordningen 1766 både som en början på demokrati och som ett resultat av politisk kamp.",[],None,"Den gav rättigheter, men kom till genom riksdagens maktkamp (hattar och mössor), Chydenius och intresse av insyn."),
]

F_SAMMAN = [
 "Dagens 14 juli och mottot ”frihet, jämlikhet, broderskap” är exempel på historiebruk.",
 "Voltaire-citatet är en senare formulering – ett exempel på källkritik.",
 "Upplysningens motsägelser: idéer om lika rättigheter men uteslutning av kvinnor och slavar.",
]
F_BEGR = [
 ("Källkritik","Att pröva vem som skrev något, när och varför."),
 ("Universell","Gäller alla människor."),
 ("Historiebruk","Hur historia används i dag och av vem."),
 ("Förbundsfest","Den fredliga fest 14 juli 1790 som markerade enighet."),
]

BLOOKET = [
 ("När var Sveriges största utsträckning ungefär?","Omkring 1658","1518","1809","1905"),
 ("Vilken kung dog i Norge 1718?","Karl XII","Gustav III","Karl XI","Gustav II Adolf"),
 ("Vilken period varade 1718–1772?","Frihetstiden","Stormaktstiden","Vasatiden","Industrialismen"),
 ("Vad kallades politiska grupperna under frihetstiden?","Hattar och mössor","Röda och vita","Liberaler och konservativa","Gula och blå"),
 ("Vilket år genomförde Gustav III sin statskupp?","1772","1718","1809","1789"),
 ("Vad var upplysningens grundtanke?","Förnuft och rättigheter","Kungens gudomliga rätt","Krig mot kyrkan","Fri handel utan lagar"),
 ("Vem förespråkade maktdelning i lagstiftande, verkställande och dömande makt?","Montesquieu","Rousseau","Voltaire","Napoleon"),
 ("Vem skrev om folkets vilja i Samhällsfördraget?","Rousseau","Voltaire","Burke","Marx"),
 ("Vem hävdade naturliga rättigheter: liv, frihet, egendom?","John Locke","Napoleon","Robespierre","Adam Smith"),
 ("Vilket år kom Sveriges tryckfrihetsförordning?","1766","1718","1789","1848"),
 ("Vad bygger offentlighetsprincipen på?","Rätt att ta del av allmänna handlingar","Rätt att välja kung","Rätt till skattefrihet","Rätt till vapen"),
 ("Vilken svensk präst drev tryckfrihet?","Anders Chydenius","Olof Rudbeck","Carl Linné","Nils Dacke"),
 ("Vilket datum antogs USA:s självständighetsförklaring?","4 juli 1776","14 juli 1789","1 maj 1848","6 juni 1944"),
 ("Vad sade kolonisterna om skatter?","Ingen skatt utan representation","Ingen skatt alls","Skatt åt alla","Skatt bara åt kungen"),
 ("Vem skrev främst självständighetsförklaringen?","Thomas Jefferson","George Washington","Benjamin Franklin ensam","Napoleon"),
 ("Hur många stånd fanns i Frankrike?","Tre","Två","Fyra","Fem"),
 ("Vad hände 14 juli 1789?","Bastiljen stormades","Kungen avrättades","Napoleon kröntes","Terrorn började"),
 ("Vilken byggnad var en symbol för kungens makt?","Bastiljen","Louvren","Eiffeltornet","Colosseum"),
 ("Vad antogs 26 augusti 1789?","Deklarationen om människans och medborgarens rättigheter","Code civil","Tryckfrihetsförordningen","Bill of Rights"),
 ("Vem var en av ledarna under skräckväldet?","Robespierre","Voltaire","Louis XVI","Bernadotte"),
 ("Vilket år kröntes Napoleon till kejsare?","1804","1789","1799","1815"),
 ("Var förlorade Napoleon slutgiltigt 1815?","Waterloo","Poltava","Paris","Moskva"),
 ("Vilken fransk marskalk blev svensk kung?","Bernadotte","Ney","Murat","Lafayette"),
 ("Vilken ideologi betonar individens frihet?","Liberalism","Konservatism","Socialism","Kommunism"),
 ("Vilken ideologi vill bevara ordning och tradition?","Konservatism","Liberalism","Socialism","Nationalism"),
 ("Vem skrev kvinnors rättigheter 1791?","Olympe de Gouges","Marie Antoinette","Madame Curie","Elsa Brändström"),
 ("När var det revolutioner i många länder i Europa?","1848","1789","1815","1905"),
 ("När fick kvinnor rösta i Frankrike?","1944","1789","1848","1919"),
 ("Varifrån kommer orden höger och vänster i politiken?","Franska nationalförsamlingen","Svenska riksdagen","Brittiska parlamentet","USA:s kongress"),
]

JEOPARDY = {
 "Sverige":[
  (100,"Kungen som dog i Norge 1718.","Karl XII"),
  (200,"Perioden 1718–1772.","Frihetstiden"),
  (300,"Året för Gustav III:s statskupp.","1772"),
  (400,"Året för tryckfrihetsförordningen.","1766"),
  (500,"Vad innebär offentlighetsprincipen?","Att medborgare har rätt att ta del av allmänna handlingar.")],
 "Upplysning":[
  (100,"Rörelsen som sätter förnuftet i centrum.","Upplysningen"),
  (200,"Tänkare som ville dela makten.","Montesquieu"),
  (300,"Tänkare som skrev om folkets vilja.","Rousseau"),
  (400,"Tänkare som talade om naturliga rättigheter.","John Locke"),
  (500,"Varför kan ett Voltaire-citat vara vilseledande?","Det formulerades av Hall 1906, inte av Voltaire.")],
 "USA och Frankrike":[
  (100,"Datum för USA:s självständighetsförklaring.","4 juli 1776"),
  (200,"Fängelset som stormades 14 juli 1789.","Bastiljen"),
  (300,"Dokumentet från 26 augusti 1789.","Deklarationen om människans och medborgarens rättigheter"),
  (400,"Åren för skräckväldet.","1793–1794"),
  (500,"Ge två orsaker till franska revolutionen.","Skulder, dyrt bröd, orättvist ståndssamhälle, upplysning.")],
 "Napoleon och ideologier":[
  (100,"Året då Napoleon blev kejsare.","1804"),
  (200,"Platsen för Napoleons slutliga nederlag.","Waterloo"),
  (300,"Ideologi som vill bevara ordning.","Konservatism"),
  (400,"Ideologi som betonar individens frihet.","Liberalism"),
  (500,"Svensk marskalk som blev kung.","Bernadotte (Karl XIV Johan)")],
 "1848 och röster":[
  (100,"Året då revolutioner spred sig i Europa.","1848"),
  (200,"Hon skrev om kvinnors rättigheter 1791.","Olympe de Gouges"),
  (300,"Landet där slavar blev fria 1804.","Haiti"),
  (400,"Franska nationaldagen.","14 juli"),
  (500,"Varför misslyckades revolutionerna 1848?","Härskarna slog ner dem med arméer och revolutionärerna var oeniga.")],
}

SCEN = dict(
 titel="Tidsresa genom Paris 1789", plats="Paris och Versailles", tid="1789–1799",
 sky=("#c9d7ee","#e9d6b5"), mark="#8e8a7a",
 walker=dict(typ="medborgare"),
 etapper=[
  dict(x_etikett="Våren", tid="Våren 1789", plats="Marknad i Paris", rubrik="Brödet är dyrt",
       fakta=["Du går över marknaden i Paris. Brödet är så dyrt att en arbetare lägger en stor del av lönen på det.","Adeln betalar nästan inga skatter, men folket betalar mycket. Många tycker att det är orättvist."],
       fraga="Vad var en orsak till missnöjet i Frankrike?", alt=["Dyrt bröd och orättvisa skatter","Brist på tåg","Att kungen var för snäll"], ratt=0,
       forklaring="Dyrt bröd och orättvisa skatter gjorde folk arga.",
       ord=[("adel","rika och mäktiga släkter med särskilda rättigheter")],
       deko=[("marknad",-100,1.2),("folkmassa",90,1.0),("slott",210,0.9)]),
  dict(x_etikett="Juni", tid="Maj–juni 1789", plats="Versailles", rubrik="Det tredje ståndet säger ifrån",
       fakta=["Kungen har kallat till möte. Där finns tre grupper, kallade stånd: prästerna, adeln och alla andra (det tredje ståndet).","Varje grupp har en röst. Prästerna och adeln röstar oftast ihop och vinner. Det tredje ståndet är nästan hela folket. Det bildar en egen nationalförsamling och kräver att få bestämma."],
       fraga="Varför bildade det tredje ståndet en nationalförsamling?", alt=["De var nästan hela folket men blev ändå överröstade","De ville ha semester","De ville bli adel"], ratt=0,
       forklaring="De var flest men hade minst inflytande, och ville ha makt.",
       ord=[("stånd","grupp i samhället: präster, adel eller alla andra")],
       deko=[("slott",-100,1.3),("folkmassa",100,1.0),("flagga_trikolor",210,0.8)]),
  dict(x_etikett="14 juli", tid="14 juli 1789", plats="Bastiljen", rubrik="Stormningen",
       fakta=["Rykten säger att kungen vill skicka soldater mot folket. Folk söker vapen och går till fängelset Bastiljen.","Bastiljen är ett gammalt fängelse mitt i Paris. Där sitter få fångar. Men många ser det som en symbol för kungens makt. Folket stormar det."],
       fraga="Varför var Bastiljen viktig?", alt=["Den var en symbol för kungens makt","Den var full av guld","Den var kungens slott"], ratt=0,
       forklaring="Stormningen visade att folket kunde utmana kungen.",
       deko=[("mur",-100,1.4),("folkmassa",70,1.1),("barrikad",190,1.0)]),
  dict(x_etikett="26 aug", tid="26 augusti 1789", plats="Nationalförsamlingen", rubrik="Rättigheter på papper",
       fakta=["Nationalförsamlingen skriver ner vilka rättigheter alla människor har. Texten heter deklarationen om människans och medborgarens rättigheter.","Idéerna kommer från upplysningen. Upplysningen är en tankerörelse som säger att alla människor föds fria och lika. Men kvinnor och slavar nämns inte i texten."],
       fraga="Vilka idéer bygger deklarationen på?", alt=["Upplysningens idéer om frihet och lika rättigheter","Idén att kungen bestämmer allt","Idén att det inte ska finnas lagar"], ratt=0,
       forklaring="Deklarationen bygger på upplysningen. Den blev förebild för senare rättighetstexter.",
       ord=[("upplysning","tankerörelse: förnuft, frihet och lika rättigheter för alla"),("deklaration","en officiell skrift som slår fast något viktigt")],
       deko=[("tryckpress",-110,1.1),("bokhylla",70,1.1),("flagga_trikolor",200,0.9)]),
  dict(x_etikett="Oktober", tid="5–6 oktober 1789", plats="Vägen till Versailles", rubrik="Kvinnorna marscherar",
       fakta=["Tusentals kvinnor från Paris går till Versailles. Det är långt att gå. Barnen är hungriga och brödet är dyrt.","Kvinnorna kräver bröd. De får kungen och hans familj att flytta till Paris. Kvinnor spelar en viktig roll, men de får ändå inte rösta."],
       fraga="Vad ville kvinnorna som gick till Versailles?", alt=["Bröd och förändring","Nya hattar","Att kungen skulle resa på semester"], ratt=0,
       forklaring="Brist på mat drev dem. Kvinnor var viktiga i revolutionen.",
       deko=[("folkmassa",-100,1.2),("slott",120,1.2),("moln",220,0.9)]),
  dict(x_etikett="1793", tid="1793–1794", plats="Paris, torget", rubrik="Skräckväldet",
       fakta=["Frankrike är nu en republik. Kungen är avrättad och landet är i krig. Folk är rädda för att bli anklagade.","Revolutionens ledare dömer tusentals till döden med giljotinen. De säger att de är revolutionens fiender. Till slut avrättas även ledaren Robespierre."],
       fraga="Varför kallas åren 1793–94 skräckväldet?", alt=["Många dömdes till döden som sades vara revolutionens fiender","Det var Halloween","Det var krig mot Sverige"], ratt=0,
       forklaring="Rädsla och krig gjorde revolutionen hård. Många dödades.",
       ord=[("republik","land utan kung där folket väljer sina ledare")],
       deko=[("giljotin",-80,1.2),("folkmassa",110,1.0),("flagga_trikolor",220,0.8)]),
  dict(x_etikett="1799", tid="1799–1815", plats="Paris och Europa", rubrik="Napoleon och arvet",
       fakta=["Napoleon tar makten 1799, blir kejsare 1804 och förlorar vid Waterloo 1815. Idéerna om rättigheter finns kvar.","Revolutionen inspirerade nya rörelser. Frågan om vem som räknas som medborgare ställdes om och om igen."],
       fraga=None, alt=None, ratt=None, forklaring=None,
       deko=[("flagga_trikolor",-70,1.0),("bokhylla",100,1.0),("folkmassa",220,0.9)]),
 ],
 diskutera="Frihet, jämlikhet och broderskap var revolutionens ord. Tycker du att de gäller för alla i dag?",
)
